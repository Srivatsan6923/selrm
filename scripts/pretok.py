"""Pre-tokenise B's training corpora and evaluation prompts on CPU, so a GPU job
never builds data. Usage:
  python scripts/pretok.py --root ROOT --queue QUEUE.json --tokenizer TOKDIR
For every run in the queue:
  ROOT/tok/train/<train_key>/{train.npz, stats.json, READY}
  ROOT/tok/eval/<set>/<kind>.npz     (prompt ids; kind = verdict | rationale |
                                      reader_ledger | reader_prose)
Datasets are read from ROOT/data/<name>.jsonl (name as in data/REGISTRY.json).
Prompts get the chat template with thinking disabled (INTERFACES 2); every
completion ends with the end-of-turn token so generation formats learn to stop."""
import argparse, json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.formats import build_examples, reader_units
from selrm.prompts import rationale_prompt, reader_prompt, verdict_prompt

EVAL_KIND = {"verdict": "verdict", "rationale": "rationale", "summary2": "reader_prose",
             "value2": "reader_ledger", "ledger2": "reader_ledger"}


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def train_key(spec):
    p = spec.get("resample_p", 0.3) if spec["format"] in ("summary2", "value2", "ledger2") else 0
    return (f"{spec['format']}__{spec['corpus'].replace('/', '~')}__n{spec.get('n_examples') or 'all'}"
            f"__p{p}__c{spec.get('construction_seed', 0)}")


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


def build_train(root, spec, tok, end, max_len):
    d = f"{root}/tok/train/{train_key(spec)}"
    if os.path.exists(f"{d}/READY"):
        return d, "exists"
    recs = load_jsonl(f"{root}/data/{spec['corpus']}.jsonl")
    ex, stats = build_examples(recs, spec["format"], n=spec.get("n_examples"),
                               resample_p=spec.get("resample_p", 0.3),
                               seed=spec.get("construction_seed", 0))
    P = tok_ids(tok, [chat(tok, e["prompt"]) for e in ex])
    C = tok_ids(tok, [e["completion"] + end for e in ex])
    seqs, npr, over = [], [], 0
    for p, c in zip(P, C):
        if len(p) + len(c) > max_len:
            over += 1
            continue
        seqs.append(p + c)
        npr.append(len(p))
    if over > 0.005 * len(ex):
        raise SystemExit(f"{over} of {len(ex)} examples exceed max_len {max_len} in {d}")
    ids, off = pack(seqs)
    os.makedirs(d, exist_ok=True)
    np.savez(f"{d}/train.npz", ids=ids, off=off, npr=np.asarray(npr, dtype=np.int32))
    L = np.diff(off)
    stats |= {"key": train_key(spec), "spec": {k: spec.get(k) for k in ("format", "corpus", "n_examples",
              "resample_p", "construction_seed")}, "dropped_over_max_len": over, "max_len": max_len,
              "examples": len(seqs), "tokens": int(off[-1]), "len_mean": float(L.mean()),
              "len_max": int(L.max()), "completion_tokens": int(off[-1] - np.sum(npr)),
              "tokenizer": tok.name_or_path, "end_of_turn": end,
              "parts": {k: sum(e["part"] == k for e in ex) for k in {e["part"] for e in ex}}}
    json.dump(stats, open(f"{d}/stats.json", "w"), indent=1)
    open(f"{d}/READY", "w").write("ok\n")
    return d, f"built {len(seqs)} examples, {int(off[-1])} tokens"


def build_eval(root, set_name, kind, tok):
    d, path = f"{root}/tok/eval/{set_name}", f"{root}/tok/eval/{set_name}/{kind}.npz"
    if os.path.exists(path):
        return path, "exists"
    recs = load_jsonl(f"{root}/data/{set_name}.jsonl")
    if kind in ("verdict", "rationale"):
        fn = verdict_prompt if kind == "verdict" else rationale_prompt
        keys, texts = [r["iid"] for r in recs], [fn(r) for r in recs]
    else:
        units = reader_units(recs)
        keys = ["/".join(r["iid"].split("/")[:2]) for r in units]
        texts = [reader_prompt(r, prose=kind == "reader_prose") for r in units]
    ids, off = pack(tok_ids(tok, [chat(tok, t) for t in texts]))
    os.makedirs(d, exist_ok=True)
    np.savez(path + ".tmp.npz", ids=ids, off=off, keys=np.asarray(keys))
    os.replace(path + ".tmp.npz", path)
    return path, f"built {len(keys)} prompts, max {int(np.diff(off).max())} tokens"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--queue", required=True)
    ap.add_argument("--tokenizer", required=True)
    ap.add_argument("--max_len", type=int, default=1024)
    a = ap.parse_args()
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(a.tokenizer)
    end = end_of_turn(tok)
    runs = json.load(open(a.queue))["runs"]
    for spec in runs:
        if spec.get("train", True):
            print(spec["run_id"], *build_train(a.root, spec, tok, end, spec.get("max_len", a.max_len)), flush=True)
        for s in spec["eval_sets"]:
            print(spec["run_id"], s, *build_eval(a.root, s, EVAL_KIND[spec["format"]], tok), flush=True)


if __name__ == "__main__":
    main()
