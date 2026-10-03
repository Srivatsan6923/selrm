"""Sampling-noise check (App. F; FINAL_TASKS_C P1): the log-odds readout against a sampled readout on one open
judge (the untrained backbone), from the same forward passes. No GPU.
  python scripts/noise_check.py RUN_DIR [--logodds results_git/C-TF-critic] [--set rule_v1/test_L2]
RUN_DIR holds topk_<set>.jsonl (scripts/eval_c.py, task field topk): the top-k next-token logits at the answer
position of every verdict prompt, with the '+' and '-' logits. The log-odds readout is logit('+') - logit('-') of the
same forward passes; --logodds adds the fp32 readout of a scoring run of the same model as a cross-check. The sampled readout draws N tokens per record at temperature T with nucleus
top-p (v13: verdict frequencies over 32 samples; T 0.7, top-p 0.95, the generation settings of the runner),
renormalised over the top-k tokens (the mass outside them is reported as coverage); the record's score is the
share of '+' among the N draws, so d = share(s) - share(s'), and equal shares are ties (failures). Ten simulation
seeds; TA, Rev, Hold and tie rate as mean and s.d., against the log-odds readout of the same records (u =
logit('+') - logit('-')). Writes RUN_DIR/noise_check.json."""
import argparse, json, math, os, random, statistics, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M


def load_jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def records(data, name):
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    return load_jsonl(f"{data}/{reg[name]['path']}")


def nucleus(top_ids, top_logits, T, top_p):
    """(ids, probabilities) after temperature and top-p, renormalised over the top-k tokens."""
    m = max(top_logits)
    w = [math.exp((l - m) / T) for l in top_logits]
    z = sum(w)
    pairs = sorted(zip(top_ids, (x / z for x in w)), key=lambda t: -t[1])
    keep, c = [], 0.0
    for i, p in pairs:
        keep.append((i, p))
        c += p
        if c >= top_p:
            break
    z = sum(p for _, p in keep)
    return [i for i, _ in keep], [p / z for _, p in keep]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--logodds", default=None, help="optional scoring run of the same model (cross-check)")
    ap.add_argument("--tok", default=f"{REPO}/scratch/qwen35_tok", help="tokenizer: '+' and '-' ids as B's Scorer")
    ap.add_argument("--set", default="rule_v1/test_L2")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--n", type=int, default=32)
    ap.add_argument("--T", type=float, default=0.7)
    ap.add_argument("--top_p", type=float, default=0.95)
    ap.add_argument("--seeds", type=int, default=10)
    a = ap.parse_args()
    name = a.set.replace("/", "~")
    top = {r["iid"]: r for r in load_jsonl(f"{a.run_dir}/topk_{name}.jsonl")}
    recs = [r for r in records(a.data, a.set) if r["iid"] in top]
    from transformers import AutoTokenizer
    plus_id, minus_id = (AutoTokenizer.from_pretrained(a.tok).convert_tokens_to_ids(t) for t in ("+", "-"))
    cover = []
    dist = {}
    for r in recs:
        t = top[r["iid"]]
        cover.append(sum(math.exp(l - t["logsumexp"]) for l in t["top_logits"]))
        dist[r["iid"]] = nucleus(t["top_ids"], t["top_logits"], a.T, a.top_p)
    base = M.summarise(M.decisions(recs, [top[r["iid"]]["plus"] - top[r["iid"]]["minus"] for r in recs]))["all"]
    res = []
    for seed in range(a.seeds):
        rng = random.Random(seed)
        u = []
        for r in recs:
            ids, ps = dist[r["iid"]]
            draws = rng.choices(ids, weights=ps, k=a.n)
            u.append(sum(d == plus_id for d in draws) / a.n)
        s = M.summarise(M.decisions(recs, u))["all"]
        res.append(s)
    agg = {m: {"mean": statistics.mean(x[m] for x in res), "sd": statistics.stdev(x[m] for x in res) if len(res) > 1 else 0.0}
           for m in ("TA", "Rev", "Hold", "Tie", "BaseAcc")}
    out = {"set": a.set, "n_triplets": base["n"], "logodds": base, "sampled": agg, "samples_per_record": a.n,
           "temperature": a.T, "top_p": a.top_p, "seeds": a.seeds, "plus_id": plus_id, "minus_id": minus_id,
           "topk_coverage": {"median": statistics.median(cover), "min": min(cover)},
           "plus_minus_in_topk": sum(plus_id in top[r["iid"]]["top_ids"] and minus_id in top[r["iid"]]["top_ids"] for r in recs),
           "note": "sampled readout = share of '+' among N draws from the model's next-token distribution (top-k, T, top-p)"}
    if a.logodds:
        lo = {r["iid"]: r["u"] for r in load_jsonl(f"{a.logodds}/scores_{name}.jsonl")}
        out["logodds_run"] = {"run": os.path.basename(a.logodds.rstrip("/")),
                              "summary": M.summarise(M.decisions(recs, [lo[r["iid"]] for r in recs]))["all"]}
    json.dump(out, open(f"{a.run_dir}/noise_check.json", "w", encoding="utf-8", newline="\n"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
