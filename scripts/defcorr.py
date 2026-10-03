"""Default correction (Table 4 training-free row; shi2024cad): u'(s, x) = u(s, x) + a [u(s, x) - u(s, no case)]
from the critic's scores (C-TF-critic) and the same backbone's case-free scores (C-TF-defcorr-nocase).
a is chosen on rule_v1/dev by triplet accuracy from a grid fixed here (ties -> the smaller a), then
frozen and applied to every other set. No GPU.
  python scripts/defcorr.py [--data DIR]   -> results_git/C-TF-defcorr/{scores_*, summary_*, meta.json, DONE}"""
import argparse, json, os, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

GRID = (0.0, 0.25, 0.5, 1.0, 2.0, 4.0)
RES = f"{REPO}/results_git"


def load(path):
    with open(path, encoding="utf-8") as f:
        return {r["iid"]: r["u"] for r in map(json.loads, f)}


def records(data, name):
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    with open(f"{data}/{reg[name]['path']}", encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def combined(name, alpha):
    u = load(f"{RES}/C-TF-critic/scores_{name.replace('/', '~')}.jsonl")
    u0 = load(f"{RES}/C-TF-defcorr-nocase/scores_nocase~{name.replace('/', '~')}.jsonl")
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
    sets = sorted(p[len("scores_nocase~"):-6].replace("~", "/") for p in os.listdir(f"{RES}/C-TF-defcorr-nocase")
                  if p.startswith("scores_nocase~") and p.endswith(".jsonl"))
    summ_all = {}
    for s in sets:
        u = combined(s, alpha)
        with open(f"{out}/scores_{s.replace('/', '~')}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for k, v in u.items():
                f.write(json.dumps({"iid": k, "u": v}) + "\n")
        recs = records(a.data, s)
        summ = {"run_id": "C-TF-defcorr", "set": s, "claim_type": "conclusion", "alpha": alpha}
        if s.startswith("xr_v1"):
            summ |= M.crossed_accuracy(recs, [u[r["iid"]] for r in recs])
        elif s not in ("rule_v1/missing", "rule_v1/dev_missing"):
            T = M.decisions(recs, [u[r["iid"]] for r in recs])
            summ |= M.summarise(T)
            if summ.get("all"):
                summ["CI95"] = {m: list(M.bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
        json.dump(summ, open(f"{out}/summary_{s.replace('/', '~')}.json", "w", encoding="utf-8", newline="\n"), indent=1)
        summ_all[s] = summ.get("all") or {k: summ.get(k) for k in ("XA", "n_items")}
    if {"rule_v1/dev_missing", "rule_v1/missing"} <= set(sets):
        dm, mi = records(a.data, "rule_v1/dev_missing"), records(a.data, "rule_v1/missing")
        ud, um = combined("rule_v1/dev_missing", alpha), combined("rule_v1/missing", alpha)
        mr = M.missing_rejection(mi, [um[r["iid"]] for r in mi], M.mr_threshold(dm, [ud[r["iid"]] for r in dm]))
        p = f"{out}/summary_rule_v1~test_L2.json"
        if os.path.exists(p):
            d = json.load(open(p, encoding="utf-8"))
            json.dump(d | {k: mr[k] for k in ("MR", "FR", "threshold")}, open(p, "w", encoding="utf-8", newline="\n"), indent=1)
        summ_all["missing"] = mr
    meta = {"run_id": "C-TF-defcorr", "role": "C", "inputs": ["C-TF-critic", "C-TF-defcorr-nocase"], "alpha": alpha,
            "grid": GRID, "dev_TA_by_alpha": dev_ta, "selection": "rule_v1/dev TA, ties -> smaller alpha",
            "date": time.strftime("%Y-%m-%d"), "summaries": summ_all}
    json.dump(meta, open(f"{out}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{out}/DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n")
    print("alpha", alpha, "dev TA by alpha", dev_ta)
    print(json.dumps(summ_all, indent=1)[:2000])


if __name__ == "__main__":
    main()
