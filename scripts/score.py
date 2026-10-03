"""Extended rule-tier metrics of one run from its per-example scores (owner C; B and D call it).
  python scripts/score.py RUN_DIR [--set rule_v1/test_L2 ...] [--data DIR] [--out FILE]
For each set with scores_<set>.jsonl in RUN_DIR (default: every scored rule_v1 set):
summarise (TA, Rev, Hold, PresHold, BaseAcc, Tie by kind/tier/level/family), CIs with rules
and with signature classes as clusters, macro-averages over rules and classes, near-miss
decisions with denominators, step revisions per claim type; MR/FR on rule_v1/missing with
the threshold from the run's rule_v1/dev_missing scores. Records are read from DIR (A's
layout: REGISTRY.json + rule_v1/<set>/records.jsonl; default $SELRM_DATA or scratch/rv1).
Writes JSON to --out (default: stdout)."""
import argparse, glob, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def records(data, name):
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    return load_jsonl(f"{data}/{reg[name]['path']}")


def run_scores(run_dir, name):
    p = f"{run_dir}/scores_{name.replace('/', '~')}.jsonl"
    return {r["iid"]: r["u"] for r in load_jsonl(p)} if os.path.exists(p) else None


def set_metrics(recs, u):
    T = M.decisions(recs, u)
    out = {"summary": M.summarise(T)}
    if out["summary"].get("all"):
        out["CI95_rule"] = {m: list(M.bootstrap_ci(T, m, "rid")) for m in ("TA", "Rev", "Hold")}
        out["CI95_family"] = {m: list(M.bootstrap_ci(T, m, "family")) for m in ("TA", "Rev", "Hold")}
        out["macro"] = {f"{m}_{over}": {k: v for k, v in M.macro(T, m, over).items() if k != "by"}
                        for m in ("TA", "Rev", "Hold") for over in ("rid", "family")}
        out["nearmiss"] = M.nearmiss_table(T)
    out["step"] = M.step_revisions(recs, u)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--set", action="append")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--out")
    ap.add_argument("--write-summary", action="store_true", help="also write RUN_DIR/summary_<set>.json")
    a = ap.parse_args()
    sets = a.set or sorted(os.path.basename(p)[7:-6].replace("~", "/")
                           for p in glob.glob(f"{a.run_dir}/scores_rule_v1~*.jsonl") if p.count("~") == 1)
    res = {"run": os.path.basename(os.path.normpath(a.run_dir))}
    for s in sets:
        u = run_scores(a.run_dir, s)
        if u is None or s in ("rule_v1/missing", "rule_v1/dev_missing"):
            continue
        recs = records(a.data, s)
        res[s] = set_metrics(recs, [u[r["iid"]] for r in recs])
    ud, ut = run_scores(a.run_dir, "rule_v1/dev_missing"), run_scores(a.run_dir, "rule_v1/missing")
    if ud and ut:
        dm, mi = records(a.data, "rule_v1/dev_missing"), records(a.data, "rule_v1/missing")
        tau = M.mr_threshold(dm, [ud[r["iid"]] for r in dm])
        res["missing"] = M.missing_rejection(mi, [ut[r["iid"]] for r in mi], tau)
    if a.write_summary:                  # RESULTS_SCHEMA summary_<set>.json for runs C produces off-GPU
        for s, m in res.items():
            if not isinstance(m, dict) or "summary" not in m:
                continue
            summ = {"run_id": res["run"], "set": s, "claim_type": "conclusion"} | m["summary"]
            if "CI95_rule" in m:
                summ["CI95"] = m["CI95_rule"]
            if m.get("step"):
                summ["step"] = m["step"]
            if s == "rule_v1/test_L2" and "missing" in res:
                summ |= {k: res["missing"][k] for k in ("MR", "FR", "threshold")}
            json.dump(summ, open(f"{a.run_dir}/summary_{s.replace('/', '~')}.json", "w", encoding="utf-8",
                                 newline="\n"), indent=1)
    text = json.dumps(res, indent=1)
    if a.out:
        open(a.out, "w", encoding="utf-8", newline="\n").write(text)
    else:
        print(text)


if __name__ == "__main__":
    main()
