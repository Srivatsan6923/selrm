"""Diagnostics of Appendix F (owner C), from per-example scores only. No GPU.
  python scripts/diagnostics.py pk RUN_DIR [RUN_DIR ...]      composition gap on rule_v1/readapply + L0 rows
  python scripts/diagnostics.py shift RUN_DIR [RUN_DIR ...]   shift classes and kappa on rule_v1/missing
Composition gap (v13 Sec. 'Parts and whole'; A's readapply set): per triplet <tid>, P = correct reversal on the
reading pair (d(read at <tid>.base) > 0 and d(read at <tid>.flip) < 0), K = the same on the application pair,
U = d(base) > 0 and d(flip) < 0 at <tid>; G = 1 - Pr[U | P and K]. Also Pr[P], Pr[K], Pr[U]. The L0 columns of the
table: base accuracy, tied preferences and unnecessary reversal (UR: share of triplets with a correct base
preference whose near-miss decision is reversed, d(near) < 0), with its denominator, from rule_v1/test_L0.
Shift (App. F, Eq. 1-2): for each missing twin with d0 = d(missing) and an ordinary case x of the same group
with correct sign y (rule_v1/missing holds one base or flip case per group), delta = d(x) - d0. Cases with
y*d0 < 0 are sorted, in this order, into crossed (y*delta > |d0|), unmoved (|delta| <= tau, tau = the run's median
|d(pres) - d(base)| on rule_v1/test_L2), wrong direction (y*delta < 0) and short; d0 = 0 is counted apart. kappa =
median(y*delta over y*d0 < 0) / median(u(s+, x) - u(s-, x)) with s+ / s- the correct / incorrect claim of the
ordinary cases (the model's response to an error inside a step). Writes RUN_DIR/diagnostics.json."""
import argparse, collections, json, os, statistics, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M


def load_jsonl(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def records(data, name):
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    return load_jsonl(f"{data}/{reg[name]['path']}")


def scores(run, name):
    p = f"{run}/scores_{name.replace('/', '~')}.jsonl"
    return {r["iid"]: r["u"] for r in load_jsonl(p)} if os.path.exists(p) else None


def dmap(recs, u):
    """{(tid, case_kind): d} for conclusion claims with both roles scored."""
    J = M.judgments([r for r in recs if r["iid"] in u], [u[r["iid"]] for r in recs if r["iid"] in u])
    return {k: j["d"] for k, j in J.items()}


def pk(run, data):
    recs, u = records(data, "rule_v1/readapply"), scores(run, "rule_v1/readapply")
    if u is None:
        return None
    d = dmap(recs, u)
    tids = sorted({r["tid"] for r in recs if r["case_kind"] in ("base", "flip")})
    ev = []
    for t in tids:
        if not all(k in d for k in ((t, "base"), (t, "flip"), (f"{t}.base", "read"), (f"{t}.flip", "read"),
                                    (f"{t}.base", "apply"), (f"{t}.flip", "apply"))):
            continue
        P = d[(f"{t}.base", "read")] > 0 and d[(f"{t}.flip", "read")] < 0
        K = d[(f"{t}.base", "apply")] > 0 and d[(f"{t}.flip", "apply")] < 0
        U = d[(t, "base")] > 0 and d[(t, "flip")] < 0
        ev.append((P, K, U))
    pkset = [e for e in ev if e[0] and e[1]]
    out = {"n": len(ev), "P": 100.0 * sum(e[0] for e in ev) / len(ev), "K": 100.0 * sum(e[1] for e in ev) / len(ev),
           "U": 100.0 * sum(e[2] for e in ev) / len(ev), "n_P_and_K": len(pkset),
           "G": 100.0 * (1 - sum(e[2] for e in pkset) / len(pkset)) if pkset else None}
    l0, u0 = records(data, "rule_v1/test_L0"), scores(run, "rule_v1/test_L0")
    if u0 is not None:
        T = M.decisions(l0, [u0[r["iid"]] for r in l0])
        s = M.summarise(T)["all"]
        nm = M.nearmiss_table(T)["all"]
        out |= {"L0_BaseAcc": s["BaseAcc"], "L0_Tie": s["Tie"], "L0_UR": nm["UnnecessaryReversal"],
                "L0_UR_n": nm["n_base_correct"]}
    return out


def shift(run, data):
    recs, u = records(data, "rule_v1/missing"), scores(run, "rule_v1/missing")
    l2, u2 = records(data, "rule_v1/test_L2"), scores(run, "rule_v1/test_L2")
    if u is None or u2 is None:
        return None
    J = M.judgments(recs, [u[r["iid"]] for r in recs])
    d2 = dmap(l2, u2)
    tau = statistics.median(abs(d2[(t, "pres")] - d2[(t, "base")]) for (t, k) in d2 if k == "pres" and (t, "base") in d2)
    cls, opp, gaps = collections.Counter(), [], []
    for (t, k), j in J.items():
        if k == "missing" or j["y"] == 0 or (t, "missing") not in J:
            continue
        d0, y, dx = J[(t, "missing")]["d"], j["y"], j["d"]
        gaps.append(y * dx)                    # u(s+, x) - u(s-, x) on the ordinary case
        if d0 == 0:
            cls["d0_zero"] += 1
            continue
        if y * d0 > 0:
            cls["baseline_agrees"] += 1
            continue
        delta = dx - d0
        opp.append(y * delta)
        cls["crossed" if y * delta > abs(d0) else "unmoved" if abs(delta) <= tau else
            "wrong_direction" if y * delta < 0 else "short"] += 1
    n_opp = sum(cls[k] for k in ("crossed", "unmoved", "wrong_direction", "short"))
    return {"tau": tau, "counts": dict(cls), "n_opposed": n_opp,
            "shares_of_opposed": {k: 100.0 * cls[k] / n_opp for k in ("crossed", "unmoved", "wrong_direction", "short")} if n_opp else None,
            "kappa": statistics.median(opp) / statistics.median(gaps) if opp and gaps and statistics.median(gaps) else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["pk", "shift"])
    ap.add_argument("runs", nargs="+")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    a = ap.parse_args()
    for run in a.runs:
        res = (pk if a.what == "pk" else shift)(run, a.data)
        print(os.path.basename(os.path.normpath(run)), json.dumps(res))
        if res is not None:
            p = f"{run}/diagnostics.json"
            old = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
            json.dump(old | {a.what: res}, open(p, "w", encoding="utf-8", newline="\n"), indent=1)


if __name__ == "__main__":
    main()
