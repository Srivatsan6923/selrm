"""Score canonical records with a local model (base or LoRA adapter) and write
results/<run_id>/scores_<set>.jsonl and summary_<set>.json (INTERFACES 3-4).
Usage (normally called by train_eval_job.py with the trained model in memory):
  python scripts/eval_local.py --root ROOT --run_id RID --format FMT --set SET [--adapter DIR]

Scoring: u = logit("+") - logit("-") at the answer position.
verdict    one forward pass per record (pre-tokenised prompts)
rationale  greedy-generate ledger + answer per record, then u at the answer position
two-stage  greedy-generate the reader output once per (case, condition); malformed
           ledger -> u = -20 for both claims; else judge forward pass per record.
Batches are padded on the left; a self-check compares batched and single-prompt
scores and falls back to exact-length buckets (no padding) if they disagree."""
import argparse, json, os, sys, time
import numpy as np
import torch
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.formats import MALFORMED_U, TWO_STAGE, reader_units, well_formed
from selrm.metrics import bootstrap_ci, decisions, summarise
from selrm.prompts import judge_prompt

KIND = {"verdict": "verdict", "rationale": "rationale", "summary2": "reader_prose",
        "value2": "reader_ledger", "ledger2": "reader_ledger"}


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def unpack(path):
    z = np.load(path)
    ids, off = z["ids"], z["off"]
    return [ids[off[i]:off[i + 1]].tolist() for i in range(len(off) - 1)], list(z["keys"])


class Scorer:
    def __init__(self, model, tok, bs_score=64, bs_gen=64, max_new=384, log=print):
        self.model, self.tok, self.log = model, tok, log
        self.bs_score, self.bs_gen, self.max_new = bs_score, bs_gen, max_new
        self.plus, self.minus = (tok.convert_tokens_to_ids(t) for t in ("+", "-"))
        assert tok("+", add_special_tokens=False).input_ids == [self.plus]
        assert tok("-", add_special_tokens=False).input_ids == [self.minus]
        self.pad = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
        # no generation_config.json in the repo: stop on <|im_end|> and <|endoftext|> explicitly
        self.eos = sorted({tok.convert_tokens_to_ids(t) for t in ("<|im_end|>", "<|endoftext|>")}
                          | {tok.eos_token_id} - {None, tok.unk_token_id})
        self.nl = {i for t, i in tok.get_vocab().items() if tok.convert_tokens_to_string([t]).endswith("\n")}
        self.dev = next(model.parameters()).device
        self.pad_ok = None
        self.gen_tokens = 0

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

    @torch.no_grad()
    def _last(self, seqs):
        ids, att = self._left_pad(seqs)
        out = self.model(input_ids=ids, attention_mask=att, logits_to_keep=1, use_cache=False)
        lg = out.logits[:, -1, :].float()
        return (lg[:, self.plus] - lg[:, self.minus]).cpu().numpy()

    def check_padding(self, seqs, n=8, tol=0.15):
        """Batched (left-padded) vs one-at-a-time scores on prompts of mixed length."""
        pick = sorted(range(len(seqs)), key=lambda i: len(seqs[i]))
        pick = [pick[int(k * (len(pick) - 1) / (n - 1))] for k in range(n)]
        single = np.array([self._last([seqs[i]])[0] for i in pick])
        batched = self._last([seqs[i] for i in pick])
        diff = float(np.abs(single - batched).max())
        self.pad_ok = diff <= tol
        self.log(f"padding self-check: max |u_batch - u_single| = {diff:.4f} -> "
                 f"{'left padding' if self.pad_ok else 'exact-length buckets'}")
        return diff

    def score(self, seqs):
        u = np.zeros(len(seqs), dtype=np.float64)
        for b in self._batches(seqs, self.bs_score):
            u[b] = self._last([seqs[i] for i in b])
        return u

    @torch.no_grad()
    def generate(self, seqs):
        """Greedy, fixed max length; returns generated ids without the end token, and
        whether generation stopped by itself."""
        out, done = [None] * len(seqs), [False] * len(seqs)
        for b in self._batches(seqs, self.bs_gen):
            ids, att = self._left_pad([seqs[i] for i in b])
            g = self.model.generate(input_ids=ids, attention_mask=att, do_sample=False,
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


def evaluate(sc: Scorer, root, run_id, fmt, set_name, out_dir, log=print):
    """-> summary dict; writes scores_<set>.jsonl and summary_<set>.json."""
    t0 = time.time()
    recs = load_jsonl(f"{root}/data/{set_name}.jsonl")
    seqs, keys = unpack(f"{root}/tok/eval/{set_name}/{KIND[fmt]}.npz")
    if sc.pad_ok is None:
        sc.check_padding(seqs)
    extra, rows = {}, []
    if fmt == "verdict":
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
    else:
        units = reader_units(recs)
        assert keys == ["/".join(r["iid"].split("/")[:2]) for r in units], "eval prompts out of sync"
        gens, done = sc.generate(seqs)
        text = {}
        for r, g, d in zip(units, gens, done):
            out = sc.tok.decode(g)
            ok = (d or fmt == "summary2") and well_formed(out, r["case_text"], fmt)   # a cut-off ledger is unparsable
            text[(r["tid"], r["case_kind"], r["condition"])] = (out, ok)
        idx = [i for i, r in enumerate(recs) if text[(r["tid"], r["case_kind"], r["condition"])][1]]
        u = np.full(len(recs), MALFORMED_U)
        if idx:
            u[idx] = sc.score(chat_ids(sc.tok, [judge_prompt(recs[i], text[(recs[i]["tid"], recs[i]["case_kind"],
                                                                          recs[i]["condition"])][0]) for i in idx]))
        rows = [{"iid": r["iid"], "u": float(x), "reader_output": text[(r["tid"], r["case_kind"], r["condition"])][0]}
                for r, x in zip(recs, u)]
        bad = sum(not ok for _, ok in text.values())
        extra = {"reader_units": len(units), "malformed_units": bad,
                 "malformed_rate": round(bad / max(1, len(units)), 4), "gen_not_stopped": sum(not d for d in done)}
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/scores_{set_name.replace('/', '~')}.jsonl", "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    summ = summarize(recs, [row["u"] for row in rows], run_id, set_name)
    summ["eval"] = extra | {"seconds": round(time.time() - t0, 1), "pad_ok": sc.pad_ok}
    json.dump(summ, open(f"{out_dir}/summary_{set_name.replace('/', '~')}.json", "w"), indent=1)
    a = summ.get("all", {})
    log(f"{run_id} {set_name}: TA {a.get('TA', float('nan')):.1f} Rev {a.get('Rev', float('nan')):.1f} "
        f"Hold {a.get('Hold', float('nan')):.1f} n={a.get('n')} ({summ['eval']['seconds']} s)")
    return summ


def summarize(recs, scores, run_id, set_name):
    """summarise() for every claim type present, CIs for the conclusion claim."""
    out = {"run_id": run_id, "set": set_name, "claim_type": "conclusion"}
    T = decisions(recs, scores, "conclusion")
    out |= summarise(T)
    if T:
        out["CI95"] = {m: list(bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
    step = {}
    for ct in sorted({r["claim_type"] for r in recs} - {"conclusion"}):
        step[ct] = summarise(decisions(recs, scores, ct)).get("all", {})
    if step:
        out["step"] = step
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
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import finetune
    model, tok = finetune.load_for_eval(a.base, a.adapter)
    sc = Scorer(model, tok, a.bs_score, a.bs_gen)
    for s in a.set:
        evaluate(sc, a.root, a.run_id, a.format, s, f"{a.root}/results/{a.run_id}")


if __name__ == "__main__":
    main()
