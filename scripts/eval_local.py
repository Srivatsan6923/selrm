"""Score canonical records with a local model (base or LoRA adapter) and write
results/<run_id>/scores_<set>.jsonl and summary_<set>.json (INTERFACES 3-4).
Usage (normally called by train_eval_job.py with the trained model in memory):
  python scripts/eval_local.py --root ROOT --run_id RID --format FMT --set SET [--adapter DIR]

Scoring: u = logit("+") - logit("-") at the answer position.
verdict    one forward pass per record (pre-tokenised prompts)
rationale  greedy-generate ledger + answer per record, then u at the answer position
genprm     greedy-generate a Python check per record, execute it (restricted, no imports, time
           limit), write its real output after it, then u at the answer position
two-stage  greedy-generate the reader output once per (case, condition); malformed
           ledger -> u = -20 for both claims; else judge forward pass per record.
Batches are padded on the left; a self-check compares batched and single-prompt
scores and falls back to exact-length buckets (no padding) if they disagree."""
import argparse, collections, json, os, sys, time
import numpy as np
import torch
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.crit_parse import from_struct, parse_criterion
from selrm.link import load_onto
from selrm.gate import gate
from selrm.formats import (BITS, MALFORMED_U, entry_g, PROSE, TWO_STAGE, parse_entries, judge_for, dataset_path, gold_record, judge_view, read_bit,
                           reader_unit, reader_units, unit_key, well_formed)
from selrm.metrics import bootstrap_ci, cluster_bootstrap, crossed_accuracy, decisions, summarise
from selrm.prompts import judge_prompt, ledger_to_text

KIND = {"verdict": "verdict", "verdict_bt": "verdict", "rationale": "rationale", "summary2": "reader_prose",
        "summary2_case": "reader_prose", "value2": "reader_ledger", "ledger2": "reader_ledger", "ledger2_dec": "reader_ledger",
        "dec_judge": "reader_ledger", "bit_reader": "reader_ledger", "ledger2_verify": "reader_ledger",
        "genprm": "genprm", "conddrv": "reader_derive", "ledger2_case": "reader_ledger", "ledger_g": "reader_ledger"}
PROGRAM_U = 10.0            # |u| when the rule program decides from the predicted bit
MODES = (None, "oracle_ledger", "program_bit", "ledger_swap", "verify", "ledger_edit", "gate", "gate_struct")
# Executes generated checks one per stdin line (JSON string) in a separate interpreter: no imports
# (restricted builtins, so no network or files), 2 s per check; prints the last printed line or "error".
CHECK_HARNESS = r'''
import builtins, json, signal, sys
def _stop(*a): raise TimeoutError
ALARM = hasattr(signal, "setitimer")          # POSIX (the GPU pods); no per-check limit on Windows
if ALARM:
    signal.signal(signal.SIGALRM, _stop)
SAFE = {k: getattr(builtins, k) for k in ("abs", "all", "any", "bool", "dict", "enumerate", "float", "int", "len",
        "list", "max", "min", "range", "round", "set", "sorted", "str", "sum", "tuple", "zip")}
for line in sys.stdin:
    out = []
    g = {"__builtins__": dict(SAFE, print=lambda *a, **k: out.append(" ".join(map(str, a))))}
    try:
        if ALARM:
            signal.setitimer(signal.ITIMER_REAL, 2.0)
        exec(compile(json.loads(line), "<check>", "exec"), g)
        res = (out[-1].strip()[:20] if out else "") or "none"
    except BaseException:
        res = "error"
    finally:
        if ALARM:
            signal.setitimer(signal.ITIMER_REAL, 0)
    print(json.dumps(res), flush=True)
'''


def check_block(text):
    """(code, end) of the first ```python block of a genprm output, or (None, None)."""
    a = text.find("```python\n")
    b = text.find("```", a + 10) if a >= 0 else -1
    return (text[a + 10:b], b + 3) if b >= 0 else (None, None)


def run_checks(codes, batch=1024):
    """Executed output of each check (None -> "error"); batches of 1024 per interpreter.
    Known limit: a check stuck inside one C call outlives its alarm; the batch then times out
    and its unfinished checks count as "error"."""
    import subprocess
    outs = ["error"] * len(codes)
    idx = [i for i, c in enumerate(codes) if c is not None]
    for k in range(0, len(idx), batch):
        part = idx[k:k + batch]
        try:
            r = subprocess.run([sys.executable, "-I", "-c", CHECK_HARNESS], capture_output=True, text=True,
                               input="".join(json.dumps(codes[i]) + "\n" for i in part), timeout=300)
            got = r.stdout.splitlines()
        except subprocess.TimeoutExpired as e:
            got = (e.stdout.decode() if isinstance(e.stdout, bytes) else e.stdout or "").splitlines()
        for i, line in zip(part, got):
            outs[i] = json.loads(line)
    return outs


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def unpack(path, vocab=None):
    z = np.load(path)
    if vocab is not None and "vocab" in z and int(z["vocab"]) != vocab:
        raise RuntimeError(f"{path} was tokenised with a vocabulary of {int(z['vocab'])}, model has {vocab}")
    ids, off = z["ids"], z["off"]
    return [ids[off[i]:off[i + 1]].tolist() for i in range(len(off) - 1)], list(z["keys"])


class Scorer:
    def __init__(self, model, tok, bs_score=64, bs_gen=64, max_new=384, log=print):
        self.model, self.tok, self.log = model, tok, log
        self.bs_score, self.bs_gen, self.max_new = bs_score, bs_gen, max_new
        if torch.cuda.is_available() and torch.cuda.get_device_properties(0).total_memory < 60 * 2**30:
            self.bs_gen = min(bs_gen, 128)      # generation states for 256 sequences need an 80 GB card
        self.plus, self.minus = (tok.convert_tokens_to_ids(t) for t in ("+", "-"))
        assert tok("+", add_special_tokens=False).input_ids == [self.plus]
        assert tok("-", add_special_tokens=False).input_ids == [self.minus]
        self.pad = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
        # no generation_config.json in the repo: stop on <|im_end|> and <|endoftext|> explicitly
        self.eos = sorted(({tok.convert_tokens_to_ids(t) for t in ("<|im_end|>", "<|endoftext|>")}
                           | {tok.eos_token_id}) - {None, tok.unk_token_id})
        self.nl = {i for t, i in tok.get_vocab().items() if tok.convert_tokens_to_string([t]).endswith("\n")}
        self.dev = next(model.parameters()).device
        self.pad_ok = None
        self.gen_tokens = 0
        # u in fp32 from the hidden state that feeds lm_head (bf16 logits sit on a 0.125-0.25 grid,
        # which creates exact ties d == 0 that the metrics count as failures)
        head = model.get_output_embeddings()
        self.w = (head.weight[self.plus].float() - head.weight[self.minus].float()).to(self.dev)
        self.b = (head.bias[self.plus] - head.bias[self.minus]).float() if getattr(head, "bias", None) is not None else 0.0
        self.scale = 1.0 / float(getattr(model.config, "logits_scaling", None) or 1.0)   # Granite divides logits by 16
        self._h = None
        head.register_forward_pre_hook(self._grab)
        self.u_path = None

    def _batches(self, seqs, bs):
        """Indices sorted by length; exact-length buckets when padding is not trusted."""
        order = sorted(range(len(seqs)), key=lambda i: (len(seqs[i]), i))
        if self.pad_ok is False:
            out, cur = [], []
            for i in order:
                if cur and (len(seqs[i]) != len(seqs[cur[0]]) or len(cur) == bs):
                    out.append(cur); cur = []
                cur.append(i)
            return out + ([cur] if cur else [])
        return [order[i:i + bs] for i in range(0, len(order), bs)]

    def _left_pad(self, seqs):
        L = max(len(s) for s in seqs)
        ids = torch.full((len(seqs), L), self.pad, dtype=torch.long)
        att = torch.zeros((len(seqs), L), dtype=torch.long)
        for j, s in enumerate(seqs):
            ids[j, L - len(s):] = torch.tensor(s)
            att[j, L - len(s):] = 1
        return ids.to(self.dev), att.to(self.dev)

    def _grab(self, module, args):
        self._h = args[0]

    @torch.no_grad()
    def _last(self, seqs):
        ids, att = self._left_pad(seqs)
        self._h = None
        out = self.model(input_ids=ids, attention_mask=att, logits_to_keep=1, use_cache=False)
        lg = out.logits[:, -1, :].float()
        u_bf16 = lg[:, self.plus] - lg[:, self.minus]
        if self._h is not None and self._h.shape[0] == len(seqs):
            u = (self._h[:, -1, :].float() @ self.w + self.b) * self.scale
            if self.u_path is None:       # once: the fp32 path must agree with the logits up to bf16 rounding
                gap = float((u - u_bf16).abs().max())
                self.u_path = "fp32-hidden" if gap <= 0.5 + 0.02 * float(u.abs().max()) else "logits"
                self.log(f"u path: {self.u_path} (max |u_fp32 - u_bf16logits| = {gap:.4f})")
            if self.u_path == "fp32-hidden":
                return u.cpu().numpy()
        elif self.u_path is None:
            self.u_path = "logits"
            self.log("u path: logits (lm_head pre-hook did not fire)")
        return u_bf16.cpu().numpy()

    def check_padding(self, seqs, n=8):
        """Batched (left-padded) vs one-at-a-time scores on prompts of mixed length."""
        pick = sorted(range(len(seqs)), key=lambda i: len(seqs[i]))
        pick = [pick[int(k * (len(pick) - 1) / (n - 1))] for k in range(n)]
        single = np.array([self._last([seqs[i]])[0] for i in pick])
        batched = self._last([seqs[i] for i in pick])
        diff = float(np.abs(single - batched).max())
        tol = 0.5 + 0.02 * float(np.abs(single).max())   # bf16 noise between batch shapes is ~0.1-0.2; a padding bug moves u by units
        self.pad_ok = diff <= tol
        self.log(f"padding self-check: max |u_batch - u_single| = {diff:.4f} (tol {tol:.3f}) -> "
                 f"{'left padding' if self.pad_ok else 'exact-length buckets'}")
        return diff

    def score(self, seqs):
        u = np.zeros(len(seqs), dtype=np.float64)
        for b in self._batches(seqs, self.bs_score):
            u[b] = self._last([seqs[i] for i in b])
        return u

    @torch.no_grad()
    def generate(self, seqs, sample=False, seed=0):
        """Greedy (or seeded sampling at T=0.7, top-p 0.95), fixed max length; returns generated
        ids without the end token, and whether generation stopped by itself."""
        if sample:
            torch.manual_seed(seed)
        extra = {"do_sample": True, "temperature": 0.7, "top_p": 0.95} if sample else {"do_sample": False}
        out, done = [None] * len(seqs), [False] * len(seqs)
        batches, t0, g0 = self._batches(seqs, self.bs_gen), time.time(), self.gen_tokens
        for k, b in enumerate(batches):
            if k and k % 25 == 0:         # long generation phases (rationale on rule_v1) stay observable
                self.log(f"generate: batch {k}/{len(batches)}, {self.gen_tokens - g0} tokens, "
                         f"{(self.gen_tokens - g0) / max(1e-9, time.time() - t0):.0f} tok/s")
            ids, att = self._left_pad([seqs[i] for i in b])
            g = self.model.generate(input_ids=ids, attention_mask=att, **extra,
                                    max_new_tokens=self.max_new, eos_token_id=self.eos,
                                    pad_token_id=self.pad, use_cache=True)
            g = g[:, ids.shape[1]:].tolist()
            for i, row in zip(b, g):
                cut = next((k for k, t in enumerate(row) if t in self.eos), None)
                done[i] = cut is not None
                out[i] = row[:cut] if cut is not None else row
                self.gen_tokens += len(out[i]) + done[i]
        return out, done

    def answer_prefix(self, prompt, gen):
        """Prompt + generated ledger up to the answer line of a rationale output.
        The answer is the first '+'/'-' token right after a newline; if the model
        never wrote one, a newline is appended and the answer is read there."""
        for k, t in enumerate(gen):
            if t in (self.plus, self.minus) and k > 0 and gen[k - 1] in self.nl:
                return prompt + gen[:k], True
        nl = self.tok("\n", add_special_tokens=False).input_ids
        return prompt + gen + nl, False


def chat_ids(tok, texts):
    s = [tok.apply_chat_template([{"role": "user", "content": t}], tokenize=False,
                                 add_generation_prompt=True, enable_thinking=False) for t in texts]
    return tok(s, add_special_tokens=False).input_ids


def evaluate(sc: Scorer, root, run_id, fmt, set_name, out_dir, log=print, tag="unsloth--Qwen3.5-9B",
             mode=None):
    """-> summary dict; writes scores_<set>.jsonl and summary_<set>.json. Prompts come
    pre-tokenised from ROOT/tok/<tag>/eval/<set>/<kind>.npz (scripts/pretok.py).
    Two-stage modes (Table 9 / Sec. 7.4 analyses on a trained adapter):
      oracle_ledger  the judge reads the program's target ledger instead of the reader's
      program_bit    the rule program decides from the reader's predicted decision bit
      ledger_swap    the judge reads another case's ledger (same rule, condition, claim);
                     summary = agreement with the verdict that ledger implies
      ledger_edit    the judge reads the program's ledger with subject, status or time edited;
                     summary = agreement with the program's verdict after the edit
      verify         reader outputs re-read entry by entry, rejected ones regenerated once"""
    assert mode in MODES, mode
    t0 = time.time()
    recs = load_jsonl(dataset_path(root, set_name))
    seqs, keys = unpack(f"{root}/tok/{tag}/eval/{set_name}/{KIND[fmt]}.npz", len(sc.tok))
    if sc.pad_ok is None:
        sc.check_padding(seqs)
    extra, rows = {}, []
    if fmt in ("verdict", "verdict_bt"):
        assert keys == [r["iid"] for r in recs], "eval prompts out of sync with records"
        u = sc.score(seqs)
        rows = [{"iid": r["iid"], "u": float(x)} for r, x in zip(recs, u)]
    elif fmt == "rationale":
        assert keys == [r["iid"] for r in recs], "eval prompts out of sync with records"
        gens, done = sc.generate(seqs)
        pref = [sc.answer_prefix(p, g) for p, g in zip(seqs, gens)]
        u = sc.score([p for p, _ in pref])
        rows = [{"iid": r["iid"], "u": float(x), "reader_output": sc.tok.decode(g), "answered": a, "stopped": d}
                for r, x, g, (_, a), d in zip(recs, u, gens, pref, done)]
        extra = {"rationale_no_answer": sum(not a for _, a in pref), "gen_not_stopped": sum(not d for d in done)}
    elif fmt == "genprm":
        assert keys == [r["iid"] for r in recs], "eval prompts out of sync with records"
        gens, done = sc.generate(seqs)
        texts = [sc.tok.decode(g) for g in gens]
        blocks = [check_block(t) for t in texts]
        outs = run_checks([c for c, _ in blocks])
        # the generated text up to the end of its check, the real output, then the answer is read
        tails = [(t[:end] if end else t.rstrip()) + "\nOutput: " + o + "\n" for t, (_, end), o in zip(texts, blocks, outs)]
        u = sc.score([p + sc.tok(tl, add_special_tokens=False).input_ids for p, tl in zip(seqs, tails)])
        rows = [{"iid": r["iid"], "u": float(x), "reader_output": t, "check_output": o, "stopped": d}
                for r, x, t, o, d in zip(recs, u, texts, outs, done)]
        extra = {"check_missing": sum(c is None for c, _ in blocks), "check_error": sum(o == "error" for o in outs),
                 "gen_not_stopped": sum(not d for d in done), "gen_tokens": int(sum(len(g) for g in gens))}
    elif mode == "ledger_swap":
        return ledger_swap(sc, recs, fmt, run_id, set_name, out_dir, log, t0)
    elif mode == "ledger_edit":
        return ledger_edit(sc, recs, fmt, run_id, set_name, out_dir, log, t0, root)
    else:
        units = reader_units(recs, fmt)
        assert keys == [unit_key(r, fmt) for r in units], "eval prompts out of sync"
        if mode == "oracle_ledger":
            outs, done = [gold_record(r, fmt) for r in units], [True] * len(units)
        else:
            gens, done = sc.generate(seqs)
            outs = [sc.tok.decode(g) for g in gens]
        text = {}
        for r, out, d in zip(units, outs, done):
            ok = (d or fmt in PROSE) and well_formed(out, r["case_text"], fmt)   # a cut-off ledger is unparsable
            text[reader_unit(r, fmt)] = (out, ok)
        if mode == "verify":
            extra_v = verification_pass(sc, units, seqs, text, fmt)
        u = np.full(len(recs), MALFORMED_U)
        routed = gate_units(units, text, fmt, mode) if mode in ("gate", "gate_struct") else None
        if mode == "program_bit":
            u = np.array([program_u(r, *text[reader_unit(r, fmt)]) for r in recs])
        elif routed:
            idx = [i for i, r in enumerate(recs) if "record" in routed[reader_unit(r, fmt)]]
            if idx:
                gs = [routed[reader_unit(recs[i], fmt)] for i in idx]
                u[idx] = sc.score(chat_ids(sc.tok, [judge_for(recs[i], g["record"], "ledger2_case" if g["route"] == "judge_case"
                                                              else fmt) for i, g in zip(idx, gs)]))
        else:
            idx = [i for i, r in enumerate(recs) if text[reader_unit(r, fmt)][1]]
            if idx:
                u[idx] = sc.score(chat_ids(sc.tok, [judge_for(recs[i], text[reader_unit(recs[i], fmt)][0], fmt)
                                                    for i in idx]))
        rows = [{"iid": r["iid"], "u": float(x), "reader_output": text[reader_unit(r, fmt)][0]} for r, x in zip(recs, u)]
        bad = sum(not ok for _, ok in text.values())
        extra = {"reader_units": len(units), "malformed_units": bad, "mode": mode,
                 "malformed_rate": round(bad / max(1, len(units)), 4), "gen_not_stopped": sum(not d for d in done)}
        if mode == "verify":
            extra |= extra_v
        if routed:
            for row, r in zip(rows, recs):
                row |= {k: v for k, v in routed[reader_unit(r, fmt)].items() if k != "record"}
            g = list(routed.values())
            extra |= {"routes": dict(collections.Counter(x["route"] for x in g)),
                      "gate_coverage": round(sum(x["route"] == "gate" for x in g) / max(1, len(g)), 4),
                      "bit_changed": sum(x["route"] == "gate" and x["applies_gate"] != x["applies_reader"] for x in g)}
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/scores_{set_name.replace('/', '~')}.jsonl", "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    summ = summarize(recs, [row["u"] for row in rows], run_id, set_name)
    summ["eval"] = extra | {"seconds": round(time.time() - t0, 1), "pad_ok": sc.pad_ok, "u_path": sc.u_path}
    json.dump(summ, open(f"{out_dir}/summary_{set_name.replace('/', '~')}.json", "w"), indent=1)
    a = summ.get("all", {})
    log(f"{run_id} {set_name}: TA {a.get('TA', float('nan')):.1f} Rev {a.get('Rev', float('nan')):.1f} "
        f"Hold {a.get('Hold', float('nan')):.1f} n={a.get('n')} ({summ['eval']['seconds']} s)")
    return summ


def gate_units(units, text, fmt, mode):
    """Ledger-RM-G routing per reader unit (STAGE2_SPEC 7) for formats whose record ends in a decision line.
    -> {unit: {"route", "checks", "applies_reader", "applies_gate", "record"}}. route: fallback_none (no criterion
    text) and fallback_malformed carry no "record" (their u stays MALFORMED_U; the composite takes the verdict-only
    score); gate = the gate's bit replaces the reader's and the judge reads the record only; judge_case = some check
    is not computable, the reader's bit stands and the judge also sees the case. gate_struct takes the constraints
    from the record's `struct` instead of the parser."""
    assert fmt in ("ledger2_dec", "ledger_g"), fmt
    g_fmt = fmt == "ledger_g"            # stage-2 record: the bit is a line of every entry
    opath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "onto_v1", "classes.json")
    onto = load_onto(opath) if os.path.exists(opath) else None
    out = {}
    for r in units:
        rec_text, ok = text[reader_unit(r, fmt)]
        if not r["rule_text"] or not ok:
            out[reader_unit(r, fmt)] = {"route": "fallback_malformed" if r["rule_text"] else "fallback_none"}
            continue
        head = rec_text.strip() if g_fmt else rec_text.strip().rpartition("\n\n")[0]
        entries = parse_entries(head)
        cons = (from_struct(r.get("struct")) if mode == "gate_struct"
                else parse_criterion(r["rule_text"], r["condition"], onto and onto["classes"]))
        g = gate(entries, cons, r["case_text"], r.get("ref_date"), onto)
        done = g["applies"] is not None
        if not done:
            record = rec_text.strip()                    # the reader's bit stands; the judge also sees the case
        elif g_fmt:                                      # each entry's bit is replaced by the gate's value for it
            record = "\n\n".join(entry_g(e | {"applies": "yes" if v == 1 else "no"}) for e, v in zip(entries, g["entries"]))
        else:
            record = head + "\n\n" + BITS[g["applies"]]
        out[reader_unit(r, fmt)] = {"route": "gate" if done else "judge_case", "checks": g["checks"],
                                    "applies_reader": read_bit(rec_text), "applies_gate": g["applies"], "record": record}
    return out


def verification_pass(sc, units, seqs, text, fmt):
    """Every entry of every well-formed ledger is re-read against the case (verify prompt,
    rejected if u < 0); a ledger with a rejected entry (or a malformed one) is regenerated
    once by seeded sampling and replaced if the new ledger is well formed with fewer rejected
    entries. Updates text in place; returns counts."""
    from selrm.formats import parse_entries, verify_prompt

    def rejected(pairs):
        idx = [(k, e) for k, (out, ok) in pairs.items() if ok for e in parse_entries(out)]
        u = sc.score(chat_ids(sc.tok, [verify_prompt(by_unit[k], e) for k, e in idx])) if idx else []
        n = {k: 0 for k in pairs}
        for (k, _), x in zip(idx, u):
            n[k] += int(x < 0)
        return n, len(idx), int(sum(x < 0 for x in u))

    by_unit = {reader_unit(r): r for r in units}
    rej, n_entries, n_rej = rejected(text)
    redo = [i for i, r in enumerate(units) if rej[reader_unit(r)] or not text[reader_unit(r)][1]]
    replaced = 0
    if redo:
        gens, done = sc.generate([seqs[i] for i in redo], sample=True, seed=0)
        new = {}
        for i, g, d in zip(redo, gens, done):
            out = sc.tok.decode(g)
            new[reader_unit(units[i])] = (out, d and well_formed(out, units[i]["case_text"], fmt))
        rej2, _, _ = rejected(new)
        for k, (out, ok) in new.items():
            if ok and (not text[k][1] or rej2[k] < rej[k]):
                text[k], replaced = (out, ok), replaced + 1
    return {"verify_entries": n_entries, "verify_rejected_entries": n_rej, "verify_regenerated": len(redo),
            "verify_replaced": replaced}


def program_u(rec, out, ok):
    """Rule program on the predicted decision bit: claim s is correct iff the condition does
    not hold, s_prime iff it holds; 'unknown' rejects both; malformed -> MALFORMED_U."""
    bit = read_bit(out)
    if not ok or bit == "bad":
        return MALFORMED_U
    if bit is None:
        return -PROGRAM_U
    return PROGRAM_U if (rec["claim_role"] == "s") == (bit == 0) else -PROGRAM_U


def ledger_swap(sc, recs, fmt, run_id, set_name, out_dir, log, t0, seed=0):
    """Judge given another case's target ledger (same rule, condition, claim type and claim,
    other group): agreement of sign(u) with the verdict that ledger implies (Sec. 7.4)."""
    import random
    rng, by = random.Random(seed), {}
    for r in recs:
        by.setdefault((r["rid"], r["condition"], r["claim_type"], r["claim_role"]), []).append(r)
    pairs = []
    for r in recs:
        others = [x for x in by[(r["rid"], r["condition"], r["claim_type"], r["claim_role"])] if x["tid"] != r["tid"]]
        if others:
            pairs.append((r, rng.choice(others)))
    u = sc.score(chat_ids(sc.tok, [judge_prompt(r, judge_view(gold_record(x, fmt), fmt)) for r, x in pairs]))
    rows = [{"iid": r["iid"], "ledger_of": x["iid"], "u": float(v), "expected": x["label"]}
            for (r, x), v in zip(pairs, u)]
    agree = [(row["u"] > 0) == (row["expected"] == 1) for row in rows]
    summ = {"run_id": run_id, "set": set_name, "mode": "ledger_swap", "n": len(rows),
            "agreement": round(100.0 * sum(agree) / max(1, len(agree)), 2),
            "eval": {"seconds": round(time.time() - t0, 1), "u_path": sc.u_path}}
    os.makedirs(out_dir, exist_ok=True)
    name = set_name.replace("/", "~") + "~swap"
    with open(f"{out_dir}/scores_{name}.jsonl", "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    json.dump(summ, open(f"{out_dir}/summary_{name}.json", "w"), indent=1)
    log(f"{run_id} {set_name} ledger swap: agreement {summ['agreement']} n={len(rows)}")
    return summ


def ledger_edit(sc, recs, fmt, run_id, set_name, out_dir, log, t0, root):
    """Judge given the program's ledger with one field edited (ROOT/derived/<set>/field_edits.jsonl,
    scripts/field_edits.py): agreement of sign(u) with the label the program gives after the edit,
    overall, per field and for edits that do or do not change the label (Sec. 7.4)."""
    by = {r["iid"]: r for r in recs}
    E = load_jsonl(f"{root}/derived/{set_name}/field_edits.jsonl")
    u = sc.score(chat_ids(sc.tok, [judge_prompt(by[e["iid"]], judge_view(ledger_to_text(e["ledger"]), fmt))
                                   for e in E]))
    rows = [{"iid": e["iid"], "field": e["field"], "kind": e.get("kind"), "changed": e["changed"], "u": float(v),
             "expected": e["label"]} for e, v in zip(E, u)]
    agree = lambda rs: round(100.0 * sum((r["u"] > 0) == (r["expected"] == 1) for r in rs) / max(1, len(rs)), 2)
    groups = {"all": rows} | {f"field={f}": [r for r in rows if r["field"] == f] for f in ("subject", "status", "time")}
    groups |= {f"changed={c}": [r for r in rows if r["changed"] == c] for c in (0, 1)}
    groups |= {f"kind={k}": [r for r in rows if r["kind"] == k] for k in ("finding", "numeric")}
    groups |= {f"kind={k},changed={c}": [r for r in rows if r["kind"] == k and r["changed"] == c]
               for k in ("finding", "numeric") for c in (0, 1)}
    summ = {"run_id": run_id, "set": set_name, "mode": "ledger_edit", "n": len(rows), "agreement": agree(rows),
            "by": {k: {"agreement": agree(v), "n": len(v)} for k, v in groups.items()},
            "eval": {"seconds": round(time.time() - t0, 1), "u_path": sc.u_path}}
    os.makedirs(out_dir, exist_ok=True)
    name = set_name.replace("/", "~") + "~edit"
    with open(f"{out_dir}/scores_{name}.jsonl", "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    json.dump(summ, open(f"{out_dir}/summary_{name}.json", "w"), indent=1)
    log(f"{run_id} {set_name} field edits: agreement {summ['agreement']} n={len(rows)}")
    return summ


def pair_reversal(recs, scores):
    """Pair sets without near-misses (C's MedEinst: base = control, flip = trap): a pair is solved iff d > 0 on base
    and d < 0 on flip (ties fail), as C's eval_clinical.py; 95% CI resampling pairs."""
    u = {}
    for r, x in zip(recs, scores):
        if r["claim_type"] == "conclusion":
            u.setdefault(r["tid"], {})[(r["case_kind"], r["claim_role"])] = x
    items = [{"tid": t, "base": v[("base", "s")] > v[("base", "s_prime")], "flip": v[("flip", "s")] < v[("flip", "s_prime")]}
             for t, v in sorted(u.items()) if len(v) == 4]
    rate = lambda key: (lambda xs: 100.0 * sum(all(x[k] for k in key) for x in xs) / len(xs))
    point, lo, hi = cluster_bootstrap(items, "tid", rate(("base", "flip")))
    return {"Reversal": point, "CI95": [lo, hi], "control_correct": rate(("base",))(items),
            "trap_correct": rate(("flip",))(items), "n_pairs": len(items)}


def summarize(recs, scores, run_id, set_name):
    """summarise() for every claim type present, CIs for the conclusion claim."""
    out = {"run_id": run_id, "set": set_name, "claim_type": "conclusion"}
    T = decisions(recs, scores, "conclusion")
    out |= summarise(T)
    if out.get("all"):                 # sets without complete triplets (missing, read/apply) get no CI
        out["CI95"] = {m: list(bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
    step = {}
    for ct in sorted({r["claim_type"] for r in recs} - {"conclusion"}):
        step[ct] = summarise(decisions(recs, scores, ct)).get("all", {})
    if step:
        out["step"] = step
    if not out.get("all") and {r["case_kind"] for r in recs} == {"base", "flip"}:   # pair sets (MedEinst)
        out["pairs"] = pair_reversal(recs, scores)
    if recs and "xr" in recs[0]["meta"]:     # xr_v1 rule-side items: crossed accuracy; A keeps the item in meta.xr.item
        out["xr"] = {ct: crossed_accuracy(recs, scores, item_of=lambda r: r["meta"]["xr"]["item"], claim_type=ct)
                     for ct in sorted({r["claim_type"] for r in recs})}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--run_id", required=True)
    ap.add_argument("--format", required=True)
    ap.add_argument("--set", required=True, action="append")
    ap.add_argument("--adapter", default=None)
    ap.add_argument("--base", default=None, help="base model dir (default: from configs)")
    ap.add_argument("--bs_score", type=int, default=64)
    ap.add_argument("--bs_gen", type=int, default=64)
    a = ap.parse_args()
    if os.environ.get("SELRM_BACKEND", "unsloth") == "unsloth":
        import unsloth  # noqa: F401  (before transformers)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import finetune
    model, tok = finetune.load_for_eval(a.base, a.adapter)
    sc = Scorer(model, tok, a.bs_score, a.bs_gen)
    tag = os.path.basename(os.path.normpath(a.base)) if a.base else "unsloth--Qwen3.5-9B"
    for s in a.set:
        evaluate(sc, a.root, a.run_id, a.format, s, f"{a.root}/results/{a.run_id}", tag=tag)


if __name__ == "__main__":
    main()
