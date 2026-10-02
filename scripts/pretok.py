"""Pre-tokenise B's training corpora and evaluation prompts on CPU, so a GPU job
never builds data. Usage:
  python scripts/pretok.py --root ROOT --queue QUEUE.json [--models DIR]
For every run in the queue, with <tag> = its base model ("unsloth--Qwen3.5-9B"),
whose tokenizer is loaded from DIR/<tag> (default ROOT/models):
  ROOT/tok/<tag>/train/<train_key>/{train.npz, stats.json, READY}
  ROOT/tok/<tag>/eval/<set>/<kind>.npz   (kind = verdict | rationale | reader_ledger | reader_prose)
Datasets are read from ROOT/data/<name>.jsonl (name as in data/REGISTRY.json).
Prompts get the chat template with thinking disabled (INTERFACES 2); every
completion ends with the end-of-turn token so generation formats learn to stop.
Gold ledgers must pass the eval-time malformed check (formats.well_formed), and all
records of one (case, condition) must carry the same ledger and prose, else prep stops.
Files are written under pid-unique temporary names and renamed; READY is written last."""
import argparse, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.formats import TWO_STAGE, VERSION, build_examples, dataset_path, gold_record, reader_unit, reader_units, well_formed
from selrm.prompts import rationale_prompt, reader_prompt, verdict_prompt

BASE = "unsloth/Qwen3.5-9B"
MAX_LEN = 1024
EVAL_KIND = {"verdict": "verdict", "verdict_bt": "verdict", "rationale": "rationale", "summary2": "reader_prose",
             "value2": "reader_ledger", "ledger2": "reader_ledger", "ledger2_dec": "reader_ledger",
             "dec_judge": "reader_ledger", "bit_reader": "reader_ledger"}


def tok_tag(spec):
    return spec.get("base_model", BASE).replace("/", "--")


def max_len(spec):
    return spec.get("hp", {}).get("max_len", MAX_LEN)


def train_key(spec):
    p = spec.get("resample_p", 0.3) if spec["format"] in TWO_STAGE else 0
    w = f"__w{os.path.basename(spec['pair_weights']).rsplit('.', 1)[0]}" if spec.get("pair_weights") else ""
    return (f"{spec['format']}__{spec['corpus'].replace('/', '~')}__n{spec.get('n_examples') or 'all'}"
            f"__p{p}__c{spec.get('construction_seed', 0)}__L{max_len(spec)}{w}__v{VERSION}")


def train_dir(root, spec):
    return f"{root}/tok/{tok_tag(spec)}/train/{train_key(spec)}"


def eval_path(root, spec, set_name):
    return f"{root}/tok/{tok_tag(spec)}/eval/{set_name}/{EVAL_KIND[spec['format']]}.npz"


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def chat(tok, text):
    return tok.apply_chat_template([{"role": "user", "content": text}], tokenize=False,
                                   add_generation_prompt=True, enable_thinking=False)


def end_of_turn(tok):
    """The text the chat template puts after an assistant message (must be one token)."""
    m = [{"role": "user", "content": "q"}, {"role": "assistant", "content": "XYZ"}]
    end = tok.apply_chat_template(m, tokenize=False, enable_thinking=False).split("XYZ")[-1].strip()
    assert len(tok(end, add_special_tokens=False).input_ids) == 1, end
    return end


def pack(seqs):
    off = np.zeros(len(seqs) + 1, dtype=np.int64)
    off[1:] = np.cumsum([len(s) for s in seqs])
    return np.concatenate([np.asarray(s, dtype=np.int32) for s in seqs]) if seqs else np.zeros(0, np.int32), off


def tok_ids(tok, texts, bs=2048):
    out = []
    for i in range(0, len(texts), bs):
        out += tok(texts[i:i + bs], add_special_tokens=False).input_ids
    return out


def save_npz(path, **arrays):
    tmp = f"{path}.{os.getpid()}.tmp.npz"
    np.savez(tmp, **arrays)
    os.replace(tmp, path)


def check_gold(recs, fmts, where):
    """Every (case, condition) unit: one ledger/prose for all its records, and the gold
    ledger passes the eval-time malformed check. Raises with examples otherwise."""
    groups, bad = {}, []
    for r in recs:
        groups.setdefault(reader_unit(r), []).append(r)
    for unit, rs in groups.items():
        if any(x["ledger"] != rs[0]["ledger"] or x["prose"] != rs[0]["prose"] for x in rs[1:]):
            bad.append(f"{rs[0]['iid']}: records of one (case, condition) carry different ledgers/prose")
        for f in fmts:
            if f != "summary2" and not well_formed(gold_record(rs[0], f), rs[0]["case_text"], f):
                bad.append(f"{rs[0]['iid']}: gold {f} ledger fails the malformed check: {gold_record(rs[0], f)!r}")
    if bad:
        raise SystemExit(f"{where}: {len(bad)} gold-ledger problems, e.g.\n" + "\n".join(bad[:10]))


def build_train(root, spec, tok, end):
    d = train_dir(root, spec)
    if os.path.exists(f"{d}/READY"):
        return d, "exists"
    recs = [r for r in load_jsonl(dataset_path(root, spec["corpus"])) if not r["meta"].get("probe")]   # probes: scoring only
    if spec["format"] not in ("verdict", "verdict_bt", "summary2"):    # rationale targets carry the ledger2 text
        check_gold(recs, ["ledger2" if spec["format"] == "rationale" else spec["format"]], spec["corpus"])
    pw = json.load(open(f"{root}/{spec['pair_weights']}")) if spec.get("pair_weights") else None
    ex, stats = build_examples(recs, spec["format"], n=spec.get("n_examples"),
                               resample_p=spec.get("resample_p", 0.3),
                               seed=spec.get("construction_seed", 0), pair_weights=pw)
    if spec["format"] == "verdict_bt":            # prompt pairs (correct, wrong) stored as consecutive sequences
        A = tok_ids(tok, [chat(tok, e["prompt"]) for e in ex])
        B = tok_ids(tok, [chat(tok, e["prompt_b"]) for e in ex])
        P, C = [s for ab in zip(A, B) for s in ab], [[] for _ in range(2 * len(ex))]
    else:
        P = tok_ids(tok, [chat(tok, e["prompt"]) for e in ex])
        C = tok_ids(tok, [e["completion"] + end for e in ex])
    seqs, npr, over, L = [], [], 0, max_len(spec)
    for p, c in zip(P, C):
        if len(p) + len(c) > L:
            over += 1
            continue
        seqs.append(p + c)
        npr.append(len(p))
    if spec["format"] == "verdict_bt" and over:
        raise SystemExit(f"{over} pair sequences exceed max_len {L} in {d}")   # dropping one breaks the pairing
    if over > 0.005 * len(ex):
        raise SystemExit(f"{over} of {len(ex)} examples exceed max_len {L} in {d}")
    ids, off = pack(seqs)
    os.makedirs(d, exist_ok=True)
    save_npz(f"{d}/train.npz", ids=ids, off=off, npr=np.asarray(npr, dtype=np.int32),
             vocab=np.asarray(len(tok)), pairs=np.asarray(int(spec["format"] == "verdict_bt")))
    lens = np.diff(off)
    stats |= {"key": train_key(spec), "tokenizer": tok_tag(spec), "vocab": len(tok),
              "spec": {k: spec.get(k) for k in ("format", "corpus", "n_examples", "resample_p", "construction_seed")},
              "dropped_over_max_len": over, "max_len": L, "examples": len(seqs), "tokens": int(off[-1]),
              "len_mean": float(lens.mean()), "len_max": int(lens.max()),
              "completion_tokens": int(off[-1] - np.sum(npr)), "end_of_turn": end,
              "parts": {k: sum(e["part"] == k for e in ex) for k in sorted({e["part"] for e in ex})}}
    tmp = f"{d}/stats.json.{os.getpid()}"
    json.dump(stats, open(tmp, "w"), indent=1)
    os.replace(tmp, f"{d}/stats.json")
    open(f"{d}/READY", "w").write("ok\n")
    return d, f"built {len(seqs)} examples, {int(off[-1])} tokens"


def build_eval(root, spec, set_name, tok):
    path = eval_path(root, spec, set_name)
    if os.path.exists(path):
        return path, "exists"
    kind = EVAL_KIND[spec["format"]]
    recs = load_jsonl(dataset_path(root, set_name))
    if kind in ("verdict", "rationale"):
        fn = verdict_prompt if kind == "verdict" else rationale_prompt
        keys, texts = [r["iid"] for r in recs], [fn(r) for r in recs]
    else:
        check_gold(recs, ["ledger2", "value2"] if kind == "reader_ledger" else [], set_name)
        units = reader_units(recs)
        keys = ["/".join(r["iid"].split("/")[:2]) for r in units]
        texts = [reader_prompt(r, prose=kind == "reader_prose") for r in units]
    ids, off = pack(tok_ids(tok, [chat(tok, t) for t in texts]))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    save_npz(path, ids=ids, off=off, keys=np.asarray(keys), vocab=np.asarray(len(tok)))
    return path, f"built {len(keys)} prompts, max {int(np.diff(off).max())} tokens"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--queue", required=True)
    ap.add_argument("--models", default=None, help="dir with <tag>/ tokenizer files (default ROOT/models)")
    a = ap.parse_args()
    from transformers import AutoTokenizer
    toks = {}
    for spec in json.load(open(a.queue))["runs"]:
        tag = tok_tag(spec)
        if tag not in toks:
            t = AutoTokenizer.from_pretrained(f"{a.models or a.root + '/models'}/{tag}")
            toks[tag] = (t, end_of_turn(t))
        tok, end = toks[tag]
        if spec.get("train", True):
            print(spec["run_id"], *build_train(a.root, spec, tok, end), flush=True)
        for s in spec["eval_sets"]:
            print(spec["run_id"], s, *build_eval(a.root, spec, s, tok), flush=True)


if __name__ == "__main__":
    main()
