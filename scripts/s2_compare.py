"""Stage-2 primary comparisons (docs/ANALYSIS_PLAN_STAGE2.md) from per-example scores. No GPU.
  python scripts/s2_compare.py            -> results_git/C-S2-comparisons.json
(7) mcv_v1/criteria_test, human-written notes, stratum stated or denied, criterion stated: verdict x triplets minus
    verdict x blocks, balanced accuracy of the preferred claim (mean of the accuracy on items that score points and on
    items that score none; d = u(s) - u(s') > 0 is right, ties fail).
(8) same items: [triplets: stated minus none] minus [critic: stated minus none], balanced accuracy.
(9) mcv_v1/edits_test, human-written notes, criterion stated: triplets minus blocks, triplet accuracy
    (d(base) > 0, d(flip) < 0, d(near) > 0).
Seeds 0-4 are pooled per item (an item's value is its mean over the seeds scored); paired bootstrap over notes
(10,000 resamples, two-sided p). Accuracy on items that score points and on items that score none is always
written next to a balanced accuracy. Holm over the family is applied when (10)-(12) exist (key p_holm)."""
import collections, json, os, statistics, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

RES, MCV = f"{REPO}/results_git", f"{REPO}/scratch/acode_s2/data/mcv_v1"
B = 10000


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def scores(run, name):
    p = f"{RES}/{run}/scores_{name.replace('/', '~')}.jsonl"
    return {r["iid"]: r["u"] for r in load(p)} if os.path.exists(p) else None


def system_runs(kind):
    return ["C-S2-mcv-critic"] if kind == "critic" else [f"C-S2-mcv-verdict-{kind}-s{s}" for s in range(5)]


def d_by(recs, u, suffix=""):
    d = collections.defaultdict(dict)
    for r in recs:
        d[(r["tid"], r["case_kind"])][r["claim_role"]] = u[r["iid"] + suffix]
    return {k: v["s"] - v["s_prime"] for k, v in d.items()}


def criteria_items(recs, kind, cond):
    """{tid: mean over seeds of [d > 0]} on criteria_test (cond 'stated' or 'none')."""
    suffix, name = ("", "mcv_v1/criteria_test") if cond == "stated" else (f"@{cond}", f"mcv_v1/criteria_test@{cond}")
    vals = collections.defaultdict(list)
    for run in system_runs(kind):
        u = scores(run, name)
        if u:
            for (tid, _), d in d_by(recs, u, suffix).items():
                vals[tid].append(d > 0)
    return {t: statistics.mean(v) for t, v in vals.items()}, max((len(v) for v in vals.values()), default=0)


def edit_items(recs, kind):
    vals = collections.defaultdict(list)
    for run in system_runs(kind):
        u = scores(run, "mcv_v1/edits_test")
        if u:
            d = d_by(recs, u)
            for tid in {t for t, _ in d}:
                vals[tid].append(d[(tid, "base")] > 0 and d[(tid, "flip")] < 0 and d[(tid, "near")] > 0)
    return {t: statistics.mean(v) for t, v in vals.items()}, max((len(v) for v in vals.values()), default=0)


def bal(items, key):
    pos = [x[key] for x in items if x["points"]]
    zero = [x[key] for x in items if not x["points"]]
    return 100.0 * (statistics.mean(pos) + statistics.mean(zero)) / 2


def parts(items, key):
    pos = [x[key] for x in items if x["points"]]
    zero = [x[key] for x in items if not x["points"]]
    return {"balanced_accuracy": bal(items, key), "acc_items_scoring_points": 100.0 * statistics.mean(pos), "n_points": len(pos),
            "acc_items_scoring_none": 100.0 * statistics.mean(zero), "n_none": len(zero)}


def descriptive(crit, edits):
    """Descriptive cells for the MedCalc-V table, means over the seeds scored (no test):
    '<system>|<portion>@<cond>|<slice>' -> criteria: {BalAcc, Acc, acc_items_scoring_points, acc_items_scoring_none,
    n, seeds}; edits: {TA, Rev, Hold, n, seeds}. Slices: all, note_type=, stratum= (criteria); all, note_type=human,
    edit_type= (edits)."""
    cells = {}
    slices_c = [("all", lambda r: True)] + [(f"note_type={v}", lambda r, v=v: r["note_type"] == v) for v in ("human", "model")] + [
        (f"stratum={v}", lambda r, v=v: r["stratum"] == v) for v in ("stated", "denied", "default")]
    slices_e = [("all", lambda r: True), ("note_type=human", lambda r: r["note_type"] == "human")] + [
        (f"edit_type={v}", lambda r, v=v: r.get("edit_type") == v) for v in ("value", "sentence")]
    for kind in ("critic", "blocks", "triplets"):
        for cond in ("stated", "none", "wrong"):
            suffix = "" if cond == "stated" else f"@{cond}"
            for portion, recs, slices in (("criteria_test", crit, slices_c), ("edits_test", edits, slices_e)):
                per = collections.defaultdict(list)
                for run in system_runs(kind):
                    u = scores(run, f"mcv_v1/{portion}{suffix}") or scores(run.replace("C-S2-mcv-", "C-S2-mcv2-"), f"mcv_v1/{portion}{suffix}")
                    if not u:
                        continue
                    for name, keep in slices:
                        sub = [r for r in recs if keep(r)]
                        if not sub:
                            continue
                        if portion == "criteria_test":
                            d = d_by(sub, u, suffix)
                            pts = {r["tid"]: bool(r["meta"]["points"]) for r in sub}
                            items = [{"points": pts[t], "ok": float(v > 0)} for (t, _), v in d.items()]
                            if all(any(x["points"] == b for x in items) for b in (True, False)):
                                p = parts(items, "ok")
                                per[name].append({"BalAcc": p["balanced_accuracy"], "Acc": 100.0 * statistics.mean(x["ok"] for x in items),
                                                  "acc_items_scoring_points": p["acc_items_scoring_points"],
                                                  "acc_items_scoring_none": p["acc_items_scoring_none"], "n": len(items)})
                        else:
                            d = d_by(sub, u, suffix)        # criterion claims: triplet parts computed here
                            T = [(d[(t, "base")] > 0, d[(t, "flip")] < 0, d[(t, "near")] > 0) for t in sorted({t for t, _ in d})]
                            pc = lambda f: 100.0 * statistics.mean(f(x) for x in T)
                            per[name].append({"TA": pc(all), "Rev": pc(lambda x: x[0] and x[1]), "Hold": pc(lambda x: x[0] and x[2]), "n": len(T)})
                for name, v in per.items():
                    cells[f"{'critic' if kind == 'critic' else 'verdict-' + kind}|{portion}@{cond}|{name}"] = {
                        k: statistics.mean(x[k] for x in v) for k in v[0]} | {"seeds": len(v)}
    return cells


def main():
    out = {"plan": "docs/ANALYSIS_PLAN_STAGE2.md", "bootstrap": {"B": B, "seed": 0, "unit": "note"}, "comparisons": {}}
    crit = [r for r in load(f"{MCV}/criteria_test/records.jsonl") if r["note_type"] == "human" and r["stratum"] in ("stated", "denied")]
    meta = {r["tid"]: r for r in crit}
    cells, seeds = {}, {}
    for kind in ("triplets", "blocks", "critic"):
        for cond in ("stated", "none"):
            cells[(kind, cond)], seeds[(kind, cond)] = criteria_items(crit, kind, cond)
    need = [("triplets", "stated"), ("blocks", "stated"), ("triplets", "none"), ("critic", "stated"), ("critic", "none")]
    if all(cells[k] for k in need):
        tids = sorted(set.intersection(*(set(cells[k]) for k in need)))
        items = [{"cl": meta[t]["cluster"], "points": bool(meta[t]["meta"]["points"]),
                  **{f"{k}_{c}": cells[(k, c)][t] for k, c in need}} for t in tids]
        out["mcv_criteria_cells"] = {f"{k}_{c}": parts(items, f"{k}_{c}") | {"seeds": seeds[(k, c)]} for k, c in need}
        out["mcv_criteria_n"] = {"items": len(items), "notes": len({x["cl"] for x in items})}
        r7 = M.paired_cluster_bootstrap(items, "cl", lambda xs: bal(xs, "triplets_stated"), lambda xs: bal(xs, "blocks_stated"), B=B)
        out["comparisons"]["7"] = r7 | {"contrast": "verdict x triplets minus verdict x blocks, criterion stated", "metric": "balanced accuracy", "expectation": "> 0"}
        r8 = M.paired_cluster_bootstrap(items, "cl", lambda xs: bal(xs, "triplets_stated") - bal(xs, "triplets_none"),
                                        lambda xs: bal(xs, "critic_stated") - bal(xs, "critic_none"), B=B)
        out["comparisons"]["8"] = r8 | {"contrast": "[triplets: stated - none] minus [critic: stated - none]", "metric": "balanced accuracy", "expectation": "> 0"}
    ed = [r for r in load(f"{MCV}/edits_test/records.jsonl") if r["note_type"] == "human"]
    emeta = {r["tid"]: r for r in ed}
    et, ns_t = edit_items(ed, "triplets")
    eb, ns_b = edit_items(ed, "blocks")
    ec, _ = edit_items(ed, "critic")
    if et and eb:
        tids = sorted(set(et) & set(eb))
        items = [{"cl": emeta[t]["cluster"], "a": et[t], "b": eb[t]} for t in tids]
        ta = lambda key: (lambda xs: 100.0 * statistics.mean(x[key] for x in xs))
        r9 = M.paired_cluster_bootstrap(items, "cl", ta("a"), ta("b"), B=B)
        out["comparisons"]["9"] = r9 | {"contrast": "verdict x triplets minus verdict x blocks, criterion stated", "metric": "triplet accuracy",
                                        "expectation": "> 0", "TA_triplets": ta("a")(items), "TA_blocks": ta("b")(items),
                                        "TA_critic": 100.0 * statistics.mean(ec[t] for t in tids if t in ec) if ec else None,
                                        "seeds": [ns_t, ns_b]}
    out["mcv_cells"] = descriptive(load(f"{MCV}/criteria_test/records.jsonl"), load(f"{MCV}/edits_test/records.jsonl"))
    json.dump(out, open(f"{RES}/C-S2-comparisons.json", "w", encoding="utf-8", newline="\n"), indent=1)
    print(json.dumps({k: {x: (round(v[x], 2) if isinstance(v[x], float) else v[x]) for x in ("diff", "lo", "hi", "p", "n_items", "n_clusters")}
                      for k, v in out["comparisons"].items()}, indent=1))
    print(json.dumps(out.get("mcv_criteria_cells"), indent=1)[:1500])


if __name__ == "__main__":
    main()
