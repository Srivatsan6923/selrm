"""Default correction (Table 4 training-free row; shi2024cad): u'(s, x) = u(s, x) + a [u(s, x) - u(s, no case)]
from the critic's scores (C-TF-critic) and the same backbone's case-free scores (C-TF-defcorr-nocase).
a is chosen on rule_v1/dev by triplet accuracy from a grid fixed here (ties -> the smaller a), then
frozen and applied to every other set. No GPU.
  python scripts/defcorr.py [--data DIR]   -> results_git/C-TF-defcorr/{scores_*, summary_*, meta.json, DONE}"""
import argparse, json, os, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

# first grid 0..4 (its best dev value was its upper end, so it was extended on dev only); inf = the limit
# u(s, x) - u(s, no case), the contrast alone (decisions depend on the sign of d only)
GRID = (0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, float("inf"))
RES = f"{REPO}/results_git"
js = lambda al: "inf" if al == float("inf") else al     # JSON has no infinity


def load(path):
    with open(path, encoding="utf-8") as f:
        return {r["iid"]: r["u"] for r in map(json.loads, f)}


XR = f"{REPO}/scratch/acode_xr/data/xr_v1"     # A's xr_v1 records and KNOWN_ISSUES.json (not in the rule_v1 registry)
# clinical sets: (run holding the critic's scores, run that receives the corrected scores)
CRITIC = {"clin_v1/medeinst_test": ("C-ME-critic", "C-ME-defcorr"), "clin_v1/nli4ct_test": ("C-NL-critic", "C-NL-defcorr"),
          "clin_v1/keypairs_medqa_oneway": ("C-KP-critic", "C-KP-defcorr"), "clin_v1/keypairs_careqa_oneway": ("C-KP-critic", "C-KP-defcorr"),
          "clin_v1/trialgpt_test": ("C-TG-critic", "C-TG-defcorr"), "clin_v1/trialgpt_dev": ("C-TG-critic-dev", "C-TG-defcorr-dev")}
NOCASE = ("C-TF-defcorr-nocase", "C-TF-defcorr-nocase2")


def records(data, name):
    if name == "xr_v1/test":
        path = f"{XR}/test/records.jsonl"
    elif name.startswith("clin_v1/"):
        path = f"{REPO}/data/{name}/records.jsonl"
    else:
        reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
        path = f"{data}/{reg[name]['path']}"
    with open(path, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def combined(name, alpha):
    u = load(f"{RES}/{CRITIC.get(name, ('C-TF-critic',))[0]}/scores_{name.replace('/', '~')}.jsonl")
    u0 = load(next(p for p in (f"{RES}/{d}/scores_nocase~{name.replace('/', '~')}.jsonl" for d in NOCASE) if os.path.exists(p)))
    if alpha == float("inf"):
        return {k: v - u0[k] for k, v in u.items()}
    return {k: (1 + alpha) * v - alpha * u0[k] for k, v in u.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    a = ap.parse_args()
    dev = records(a.data, "rule_v1/dev")
    dev_ta = {}
    for al in GRID:
        u = combined("rule_v1/dev", al)
        dev_ta[al] = M.summarise(M.decisions(dev, [u[r["iid"]] for r in dev]))["all"]["TA"]
    alpha = max(GRID, key=lambda al: (dev_ta[al], -al))
    out = f"{RES}/C-TF-defcorr"
    os.makedirs(out, exist_ok=True)
    sets = sorted({p[len("scores_nocase~"):-6].replace("~", "/") for d in NOCASE if os.path.isdir(f"{RES}/{d}")
                   for p in os.listdir(f"{RES}/{d}") if p.startswith("scores_nocase~") and p.endswith(".jsonl")})
    summ_all = {}
    for s in sets:
        u = combined(s, alpha)
        if s.startswith("clin_v1/"):   # make_tables reads a clinical set of C-TF-<x> from C-ME-<x>; summary by eval_clinical
            me = f"{RES}/{CRITIC[s][1]}"
            os.makedirs(me, exist_ok=True)
            with open(f"{me}/scores_{s.replace('/', '~')}.jsonl", "w", encoding="utf-8", newline="\n") as f:
                for k, v in u.items():
                    f.write(json.dumps({"iid": k, "u": v}) + "\n")
            json.dump({"run_id": CRITIC[s][1], "role": "C", "inputs": [CRITIC[s][0], *NOCASE], "alpha": js(alpha),
                       "note": "default correction of the critic, alpha frozen on rule_v1/dev (C-TF-defcorr)"},
                      open(f"{me}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
            open(f"{me}/DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n")
            summ_all[s] = f"{CRITIC[s][1]} (summary by scripts/eval_clinical.py)"
            continue
        with open(f"{out}/scores_{s.replace('/', '~')}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for k, v in u.items():
                f.write(json.dumps({"iid": k, "u": v}) + "\n")
        recs = records(a.data, s)
        summ = {"run_id": "C-TF-defcorr", "set": s, "claim_type": "conclusion", "alpha": js(alpha)}
        if s.startswith("xr_v1"):
            known = {i for x in json.load(open(f"{XR}/KNOWN_ISSUES.json", encoding="utf-8"))["issues"] for i in x["items"]}
            summ |= M.crossed_accuracy(recs, [u[r["iid"]] for r in recs]) | {
                "without_known_issues": M.crossed_accuracy(recs, [u[r["iid"]] for r in recs], exclude=known)}
        elif s not in ("rule_v1/missing", "rule_v1/dev_missing"):
            T = M.decisions(recs, [u[r["iid"]] for r in recs])
            summ |= M.summarise(T)
            crit = M.summarise(M.decisions(recs, [u[r["iid"]] for r in recs], "criterion")).get("all")
            if crit:                      # criterion-claim TA (the "step" block of B's summaries)
                summ["step"] = {"criterion": crit}
            if summ.get("all"):
                summ["CI95"] = {m: list(M.bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
        json.dump(summ, open(f"{out}/summary_{s.replace('/', '~')}.json", "w", encoding="utf-8", newline="\n"), indent=1)
        summ_all[s] = summ.get("all") or {k: summ.get(k) for k in ("XA", "n_items")}
    if {"rule_v1/dev_missing", "rule_v1/missing"} <= set(sets):
        dm, mi = records(a.data, "rule_v1/dev_missing"), records(a.data, "rule_v1/missing")
        ud, um = combined("rule_v1/dev_missing", alpha), combined("rule_v1/missing", alpha)
        mr = M.missing_rejection(mi, [um[r["iid"]] for r in mi], M.mr_threshold(dm, [ud[r["iid"]] for r in dm]))
        for n in ("test_L2", "missing"):      # make_tables reads MR at the top of summary_rule_v1~missing.json
            p = f"{out}/summary_rule_v1~{n}.json"
            if os.path.exists(p):
                d = json.load(open(p, encoding="utf-8"))
                json.dump(d | {k: mr[k] for k in ("MR", "FR", "threshold")}, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
        summ_all["missing"] = mr
    meta = {"run_id": "C-TF-defcorr", "role": "C", "inputs": ["C-TF-critic", "C-TF-defcorr-nocase"], "alpha": js(alpha),
            "grid": [js(g) for g in GRID], "dev_TA_by_alpha": {str(js(k)): v for k, v in dev_ta.items()}, "selection": "rule_v1/dev TA, ties -> smaller alpha",
            "date": time.strftime("%Y-%m-%d"), "summaries": summ_all}
    json.dump(meta, open(f"{out}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{out}/DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n")
    print("alpha", alpha, "dev TA by alpha", dev_ta)
    print(json.dumps(summ_all, indent=1)[:2000])


if __name__ == "__main__":
    main()
