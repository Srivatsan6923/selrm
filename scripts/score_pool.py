r"""Step scores for every trace of a candidate pool (D-CAL, D-SEL-*; Table 5).

  python scripts/score_pool.py ledger   --pool DIR --model MERGED_DIR --fmt ledger2 --out FILE [--swap]
  python scripts/score_pool.py medprm   --pool DIR --model DIR --out FILE [--swap]
  python scripts/score_pool.py validate --model MERGED_DIR --fmt ledger2 --records FILE --b-scores FILE --out DIR

A trace's score is the minimum of its step scores (ROLE.md). --swap gives every question
the vignette (question text) of another question, a fixed derangement (rotation by half
the pool, sorted by qid), keeping the options and the steps: the control that shows
whether a score depends on the supplied case.

ledger    Ledger-RM (a merged copy of one of B's kept adapters, scripts/merge_adapter.py),
          served with vLLM. Per step, the reader gets selrm.prompts.reader_prompt with rule ""
          (no rule is stated), case = the question text and condition = the step, and writes
          the record by greedy decoding (max 384 tokens); the judge gets
          selrm.prompts.judge_prompt with claim = the step; u = logit("+") - logit("-") at the
          answer position (INTERFACES 3), raw logits. A record that fails
          selrm.formats.well_formed (or was cut off) gives u = MALFORMED_U (-20). Chat template
          as in B's evaluation (user turn only, enable_thinking=False).
medprm    the step check: the released Med-PRM (configs/adapters.json "stepcheck"), input and
          readout of its model card: system prompt, "Question: <question with (A)..(D)>\n\n
          Explanation: Step 1: ... ки Step 2: ... ки"; per marker, softmax over the " +"/" -"
          logits; we store the log-odds u = logit(" +") - logit(" -") and the probability. No
          retrieved documents are given (no retriever is part of this study).
validate  scores frozen rule records with the merged ledger model and compares with B's own
          scores of the same adapter (per-record u, decisions, triplet accuracy); the merged
          vLLM path is used for selection only if it reproduces B's evaluation.
Output (ledger, medprm): JSONL, one line per trace {qid, sample, u: [...], score, records: [...]}
with the reader outputs kept, plus <out>.meta.json (model, versions, counts, seconds).
"""
import argparse
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from selrm import formats as F  # noqa: E402
from selrm import prompts as P  # noqa: E402

STOP = [248046, 248044]          # <|im_end|>, <|endoftext|> (Qwen3.5; configs/models_b.json)
MEDPRM_SYSTEM = ("You are an evaluator assessing the logicality and validity of the reasoning in each step of the "
                 "given explanation. In order to support the evaluation, the relevant documents, the question, and "
                 "the explanation are provided sequentially. If the reasoning contains errors, output - after that "
                 "step. If the reasoning in a step is logical and valid, output + after that step. ")


def load_pool(d):
    qs = {q["qid"]: q for q in map(json.loads, open(os.path.join(d, "questions.jsonl"), encoding="utf-8"))}
    ss = [s for s in map(json.loads, open(os.path.join(d, "samples.jsonl"), encoding="utf-8"))]
    return qs, ss


def vignettes(qs, swap):
    ids = sorted(qs)
    if not swap:
        return {q: qs[q]["question"] for q in ids}
    k = len(ids) // 2
    return {q: qs[ids[(i + k) % len(ids)]]["question"] for i, q in enumerate(ids)}


# ------------------------------------------------------------------ ledger model (vLLM)
class Ledger:
    def __init__(self, model, fmt, tp=1):
        import vllm
        from transformers import AutoTokenizer
        self.vllm, self.fmt = vllm, fmt
        self.tok = AutoTokenizer.from_pretrained(model)
        self.plus, self.minus = (self.tok.convert_tokens_to_ids(t) for t in ("+", "-"))
        assert len(self.tok("+", add_special_tokens=False).input_ids) == 1
        self.llm = vllm.LLM(model=model, dtype="bfloat16", max_model_len=8192, enable_prefix_caching=True,
                            tensor_parallel_size=tp,
                            seed=0, generation_config="vllm", logprobs_mode="raw_logits", max_logprobs=20,
                            limit_mm_per_prompt={"image": 0, "video": 0})
        self.missing = 0

    def ids(self, texts):
        s = [self.tok.apply_chat_template([{"role": "user", "content": t}], tokenize=False,
                                          add_generation_prompt=True, enable_thinking=False) for t in texts]
        return [{"prompt_token_ids": x} for x in self.tok(s, add_special_tokens=False).input_ids]

    def read(self, recs):
        sp = self.vllm.SamplingParams(temperature=0, max_tokens=384, stop_token_ids=STOP)
        outs = self.llm.generate(self.ids([P.reader_prompt(r, prose=self.fmt == "summary2") for r in recs]), sp)
        res = []
        for r, o in zip(recs, outs):
            text, done = o.outputs[0].text, o.outputs[0].finish_reason == "stop"
            res.append((text, (done or self.fmt == "summary2") and F.well_formed(text, r["case_text"], self.fmt)))
        return res

    def judge(self, recs, texts):
        sp = self.vllm.SamplingParams(temperature=0, max_tokens=1, logprobs=20)
        outs = self.llm.generate(self.ids([P.judge_prompt(r, F.judge_view(t, self.fmt)) for r, t in zip(recs, texts)]), sp)
        u = []
        for o in outs:
            lp = o.outputs[0].logprobs[0]
            if self.plus in lp and self.minus in lp:
                u.append(lp[self.plus].logprob - lp[self.minus].logprob)
            else:                      # one of the two outside the top 20: bound by the 20th logit
                self.missing += 1
                floor = min(v.logprob for v in lp.values())
                u.append((lp[self.plus].logprob if self.plus in lp else floor)
                         - (lp[self.minus].logprob if self.minus in lp else floor))
        return u

    def score(self, recs):
        """-> [(u, reader_output, well_formed)] for records with case_text, condition, claim_text."""
        units = {}
        for r in recs:
            units.setdefault((r["case_text"], r["condition"]), r)
        keys = list(units)
        read = dict(zip(keys, self.read([units[k] for k in keys])))
        ok = [i for i, r in enumerate(recs) if read[(r["case_text"], r["condition"])][1]]
        u = [F.MALFORMED_U] * len(recs)
        for i, x in zip(ok, self.judge([recs[i] for i in ok], [read[(recs[i]["case_text"], recs[i]["condition"])][0]
                                                                for i in ok])):
            u[i] = x
        return [(x, *read[(r["case_text"], r["condition"])]) for x, r in zip(u, recs)]


def run_ledger(a):
    qs, ss = load_pool(a.pool)
    vig = vignettes(qs, a.swap)
    lm = Ledger(a.model, a.fmt, a.tp)
    recs, where = [], []
    for j, s in enumerate(ss):
        for k, st in enumerate(s["steps"]):
            recs.append({"rule_text": "", "case_text": vig[s["qid"]], "condition": st, "claim_text": st})
            where.append((j, k))
    t0 = time.time()
    res = lm.score(recs)
    per = [[] for _ in ss]
    for (j, _), (u, text, ok) in zip(where, res):
        per[j].append((u, text, ok))
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        for s, p in zip(ss, per):
            us = [x for x, _, _ in p]
            f.write(json.dumps({"qid": s["qid"], "sample": s["sample"], "u": us, "score": min(us) if us else None,
                                "records": [t for _, t, _ in p], "well_formed": [ok for _, _, ok in p]}) + "\n")
    meta(a, {"steps": len(recs), "unique_reader_units": len({(r["case_text"], r["condition"]) for r in recs}),
             "malformed": sum(not ok for _, _, ok in res), "judge_token_missing_from_top20": lm.missing,
             "seconds": round(time.time() - t0, 1)})


# ------------------------------------------------------------------ step check (Med-PRM, HF)
def run_medprm(a):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    qs, ss = load_pool(a.pool)
    vig = vignettes(qs, a.swap)
    tok = AutoTokenizer.from_pretrained(a.model)
    if tok.pad_token is None:          # Llama 3.1 has none; padded positions are masked and never read
        tok.pad_token = tok.eos_token
    tok.padding_side = "right"
    model = AutoModelForCausalLM.from_pretrained(a.model, dtype=torch.bfloat16).cuda().eval()
    plus = tok(" +", add_special_tokens=False)["input_ids"][0]
    minus = tok(" -", add_special_tokens=False)["input_ids"][0]
    texts = []
    for s in ss:
        q = qs[s["qid"]]
        question = vig[s["qid"]] + "\n\n" + "\n".join(f"({k}) {v}" for k, v in q["options"].items())
        expl = " ".join(f"Step {i + 1}:  {st} ки" for i, st in enumerate(s["steps"]))
        texts.append(tok.apply_chat_template([{"role": "system", "content": MEDPRM_SYSTEM},
                                              {"role": "user", "content": f"Question: {question}\n\nExplanation: {expl}"}],
                                             tokenize=False, add_generation_prompt=True))
    t0, out = time.time(), [None] * len(ss)
    order = sorted(range(len(ss)), key=lambda i: len(texts[i]))
    for b in range(0, len(order), a.batch):
        idx = order[b:b + a.batch]
        enc = tok([texts[i] for i in idx], return_tensors="pt", padding=True, add_special_tokens=True,
                  return_offsets_mapping=True)
        offs = enc.pop("offset_mapping")
        with torch.no_grad():
            logits = model(**{k: v.cuda() for k, v in enc.items()}).logits.float()
        for row, i in enumerate(idx):
            pos = [p for p, (s0, e0) in enumerate(offs[row].tolist()) if texts[i][s0:e0] == " ки"]
            lg = logits[row, pos][:, [plus, minus]]
            u = (lg[:, 0] - lg[:, 1]).tolist()
            out[i] = {"u": u, "p": torch.softmax(lg, dim=-1)[:, 0].tolist()}
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        for s, o in zip(ss, out):
            ok = len(o["u"]) == len(s["steps"])
            f.write(json.dumps({"qid": s["qid"], "sample": s["sample"], "u": o["u"], "p": o["p"],
                                "score": min(o["u"]) if o["u"] else None, "markers_match_steps": ok}) + "\n")
    meta(a, {"traces": len(ss), "marker_mismatch": sum(len(o["u"]) != len(s["steps"]) for s, o in zip(ss, out)),
             "seconds": round(time.time() - t0, 1)})


# ------------------------------------------------------------------ validation against B
def run_validate(a):
    from selrm import metrics as M
    recs = [json.loads(line) for line in open(a.records, encoding="utf-8")]
    b = {j["iid"]: j for j in map(json.loads, open(a.b_scores, encoding="utf-8"))}
    lm = Ledger(a.model, a.fmt, a.tp)
    t0 = time.time()
    res = lm.score(recs)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "scores.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r, (u, text, ok) in zip(recs, res):
            f.write(json.dumps({"iid": r["iid"], "u": u, "reader_output": text}) + "\n")
    uv, ub = [x for x, _, _ in res], [b[r["iid"]]["u"] for r in recs]
    same_reader = sum(t.strip() == b[r["iid"]].get("reader_output", "").strip() for r, (_, t, _) in zip(recs, res))
    Tv, Tb = M.decisions(recs, uv), M.decisions(recs, ub)
    agree = sum(1 for tid in Tv for k in Tv[tid]["d"] if (Tv[tid]["d"][k] > 0) == (Tb[tid]["d"][k] > 0))
    n_d = sum(len(Tv[tid]["d"]) for tid in Tv)
    import statistics
    summ = {"records": len(recs), "reader_output_identical": same_reader,
            "u_pearson": statistics.correlation(uv, ub), "u_mean_abs_diff": statistics.fmean(abs(x - y) for x, y in zip(uv, ub)),
            "preference_sign_agreement": agree / n_d, "n_preferences": n_d,
            "vllm": M.summarise(Tv)["all"], "b": M.summarise(Tb)["all"],
            "judge_token_missing_from_top20": lm.missing, "seconds": round(time.time() - t0, 1)}
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    print(json.dumps(summ, indent=1))


def meta(a, extra):
    import torch
    import transformers
    try:
        import vllm
        vv = vllm.__version__
    except ImportError:
        vv = None
    json.dump({"mode": a.mode, "pool": getattr(a, "pool", None), "model": a.model,
               "merged_from": json.load(open(os.path.join(a.model, "MERGED.json"))) if os.path.exists(os.path.join(a.model, "MERGED.json")) else None,
               "fmt": getattr(a, "fmt", None), "swap": getattr(a, "swap", False), "vllm": vv,
               "torch": torch.__version__, "transformers": transformers.__version__,
               "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None} | extra,
              open(a.out + ".meta.json", "w"), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["ledger", "medprm", "validate"])
    ap.add_argument("--pool")
    ap.add_argument("--model", required=True)
    ap.add_argument("--fmt", default="ledger2")
    ap.add_argument("--out", required=True)
    ap.add_argument("--swap", action="store_true")
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--tp", type=int, default=1, help="tensor parallel GPUs (2 on 24 GB cards)")
    ap.add_argument("--records")
    ap.add_argument("--b-scores", dest="b_scores")
    a = ap.parse_args()
    {"ledger": run_ledger, "medprm": run_medprm, "validate": run_validate}[a.mode](a)


if __name__ == "__main__":
    main()
