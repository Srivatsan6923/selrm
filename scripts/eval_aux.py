"""Auxiliary-supervision analysis (docs/AUX_PROTOCOL.md S1, S2; secondary analysis, specified after the planned
comparisons). No GPU.
  python scripts/eval_aux.py --results DIR [--out results_git/C-AUX] [--report docs/AUX_RESULTS.md]
Runs are found by name in DIR: B-AUX-<dataset>-<recipe>-s<seed> (dataset nli4ct | medeinst; recipe r1 | r1b | r2 |
r3 | r4) and B-AUX-trialgpt-<recipe>-s<seed>-f<fold> (the model that did not train on fold <fold>). Scores are read
from scores_clin_v1~<set>.jsonl: nli4ct_test; medeinst_test and medeinst_neg; trialgpt_cv (fold items only).
Prediction rules, metrics and clusters as fixed in the protocol:
  NLI4CT    Entailment iff u > 0; primary = mean of faithfulness (altering items: prediction differs from the gold
            label of the original) and consistency (preserving items: prediction equals the original's
            prediction); cluster = trial report.
  MedEinst  pair reversal (d(control) > 0 and d(trap) < 0; ties fail); cluster = (y_gt, y_bias) label pair.
            S2 hold on medeinst_neg (d > 0), with and without items whose denied line names a diagnosis.
  TrialGPT  NEI iff max(u_s, u_s') < 0 or u_s = u_s', else met / not met; macro-F1 on non-N/A items pooled over the
            five held-out folds; cluster = patient.
Contrasts: per dataset (3)-(2) primary, (3)-(1b) secondary, (3)-(1) descriptive; S2 (4)-(1) and (3)-(2).
Seed-averaged paired cluster bootstrap (1,000, seed 0): one cluster draw per replicate, every seed of both recipes
recomputed on it and averaged. Holm over the three primary contrasts; a separate Holm family for (3)-(1b)."""
import argparse, collections, json, os, re, statistics, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

NAME = re.compile(r"^B-AUX-(nli4ct|medeinst|trialgpt)-(r1b|r1|r2|r3|r4)-s(\d+)(?:-f(\d))?$")
CONTRASTS = [("r3", "r2", "primary"), ("r3", "r1b", "secondary"), ("r3", "r1", "descriptive")]
S2_CONTRASTS = [("r4", "r1", "descriptive"), ("r3", "r2", "descriptive")]
CATS = ("met", "not_met", "nei")


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def fmt(x, nd=1):
    return "-" if x is None else f"{x:.{nd}f}"


def scores(results, run, name):
    p = f"{results}/{run}/scores_{name.replace('/', '~')}.jsonl"
    return {r["iid"]: r["u"] for r in load(p)} if os.path.exists(p) else None


def runs(results):
    out = collections.defaultdict(lambda: collections.defaultdict(dict))
    for d in sorted(os.listdir(results)) if os.path.isdir(results) else []:
        m = NAME.match(d)
        if m and os.path.exists(f"{results}/{d}/DONE"):
            ds, rec, seed, fold = m.group(1), m.group(2), int(m.group(3)), m.group(4)
            if ds == "trialgpt":
                out[ds][rec].setdefault(seed, {})[int(fold)] = d
            else:
                out[ds][rec][seed] = d
    return out


# ---------------------------------------------------------------- per-item values of one run (one seed)

def nli_items(recs, u):
    """{uuid: (cluster, kind, indicator)} for contrast items: kind 'faith' (altering) or 'cons' (preserving)."""
    pred = {r["meta"]["uuid"]: u[r["iid"]] > 0 for r in recs}
    gold = {r["meta"]["uuid"]: r["label"] == 1 for r in recs}
    out = {}
    for r in recs:
        m = r["meta"]
        if m["causal_type"] == "Altering":
            out[m["uuid"]] = (r["rid"], "faith", pred[m["uuid"]] != gold[m["original_uuid"]])
        elif m["causal_type"] == "Preserving":
            out[m["uuid"]] = (r["rid"], "cons", pred[m["uuid"]] == pred[m["original_uuid"]])
    return out


def me_items(recs, u):
    d = collections.defaultdict(dict)
    for r in recs:
        d[r["tid"]][(r["case_kind"], r["claim_role"])] = u[r["iid"]]
        d[r["tid"]]["cluster"] = r["rid"]
    out = {}
    for tid, x in d.items():
        dc, dt = x[("base", "s")] - x[("base", "s_prime")], x[("flip", "s")] - x[("flip", "s_prime")]
        out[tid] = (x["cluster"], "pair", dc > 0 and dt < 0)
    return out


def neg_items(recs, u):
    d = collections.defaultdict(dict)
    for r in recs:
        d[r["tid"]][r["claim_role"]] = u[r["iid"]]
        d[r["tid"]]["cluster"] = (r["meta"]["y_gt"], r["meta"]["y_bias"])
        d[r["tid"]]["named"] = r["meta"].get("diagnosis_named", False)
    return {t: (x["cluster"], "named" if x["named"] else "hold", x["s"] - x["s_prime"] > 0) for t, x in d.items()}


def tg_items(recs, u_by_fold):
    """{tid: (patient, gold, pred)} for non-N/A items, each predicted by the run that held its fold out."""
    d = collections.defaultdict(dict)
    for r in recs:
        f = r["meta"]["fold"]
        if r["meta"]["category"] == "na" or f not in u_by_fold or u_by_fold[f] is None:
            continue
        d[r["tid"]][r["claim_role"]] = u_by_fold[f][r["iid"]]
        d[r["tid"]]["meta"] = r["meta"]
    out = {}
    for t, x in d.items():
        us, up = x["s"], x["s_prime"]
        pred = "nei" if max(us, up) < 0 or us == up else ("met" if us > up else "not_met")
        out[t] = (x["meta"]["patient_id"], x["meta"]["category"], pred)
    return out


# ---------------------------------------------------------------- metrics on a list of item values

def nli_metric(vals):
    f = [v[2] for v in vals if v[1] == "faith"]
    c = [v[2] for v in vals if v[1] == "cons"]
    return 100.0 * (sum(f) / len(f) + sum(c) / len(c)) / 2


def share(vals):
    return 100.0 * sum(v[2] for v in vals) / len(vals)


def tg_metric(vals):
    return M.prf([v[1] for v in vals], [v[2] for v in vals], CATS)["macroF1"]


def per_seed(items_by_seed, metric):
    return {s: metric(list(v.values())) for s, v in sorted(items_by_seed.items())}


def contrast(a, b, metric):
    """a, b: {seed: {item: value}}; paired seed-averaged cluster bootstrap on items scored in every run."""
    common = set.intersection(*(set(v) for v in list(a.values()) + list(b.values())))
    items = [{"cl": next(iter(a.values()))[k][0], "a": {s: v[k] for s, v in a.items()}, "b": {s: v[k] for s, v in b.items()}}
             for k in sorted(common, key=str)]
    mean = lambda key: (lambda xs: statistics.mean(metric([x[key][s] for x in xs]) for s in xs[0][key]))
    r = M.paired_cluster_bootstrap(items, "cl", mean("a"), mean("b"))
    return r | {"seeds_a": sorted(a), "seeds_b": sorted(b)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True)
    ap.add_argument("--out", default=f"{REPO}/results_git/C-AUX")
    ap.add_argument("--report", default=f"{REPO}/docs/AUX_RESULTS.md")
    ap.add_argument("--data-c", default=f"{REPO}/data")
    a = ap.parse_args()
    R = runs(a.results)
    rec = lambda n: load(f"{a.data_c}/clin_v1/{n}/records.jsonl")
    res, L = {}, ["# Auxiliary supervision (secondary analysis, specified after the planned comparisons)", "",
                  "Generated by `scripts/eval_aux.py` from per-example scores (no typed numbers). Protocol: "
                  "`docs/AUX_PROTOCOL.md` S1, S2. Values in %; CIs: paired cluster bootstrap, seed-averaged.", ""]
    jobs = []
    if R.get("nli4ct"):
        recs = rec("nli4ct_test")
        it = {r: {s: nli_items(recs, scores(a.results, run, "clin_v1/nli4ct_test")) for s, run in v.items()}
              for r, v in R["nli4ct"].items()}
        jobs.append(("nli4ct", "mean of faithfulness and consistency", it, nli_metric))
    if R.get("medeinst"):
        recs = rec("medeinst_test")
        it = {r: {s: me_items(recs, scores(a.results, run, "clin_v1/medeinst_test")) for s, run in v.items()}
              for r, v in R["medeinst"].items()}
        jobs.append(("medeinst", "pair reversal", it, share))
        if os.path.exists(f"{a.data_c}/clin_v1/medeinst_neg/records.jsonl"):
            nrec = rec("medeinst_neg")
            nit = {r: {s: neg_items(nrec, u) for s, run in v.items()
                       if (u := scores(a.results, run, "clin_v1/medeinst_neg"))} for r, v in R["medeinst"].items()}
            jobs.append(("medeinst_neg", "hold on denied evidence (S2)", {r: v for r, v in nit.items() if v}, share))
    if R.get("trialgpt"):
        recs = rec("trialgpt_cv")
        it = {r: {s: tg_items(recs, {f: scores(a.results, run, "clin_v1/trialgpt_cv") for f, run in folds.items()})
                  for s, folds in v.items()} for r, v in R["trialgpt"].items()}
        jobs.append(("trialgpt", "macro-F1 (pooled held-out folds)", it, tg_metric))
    primary, secondary = {}, {}
    for ds, label, it, metric in jobs:
        res[ds] = {"metric": label, "recipes": {r: (lambda ps: {"by_seed": ps, **{k: v for k, v in M.seed_table(ps).items() if k in ("mean", "sd", "n")}})(per_seed(v, metric))
                                                 for r, v in sorted(it.items())}, "contrasts": {}}
        for x, y, kind in (S2_CONTRASTS if ds == "medeinst_neg" else CONTRASTS):
            if x in it and y in it:
                c = contrast(it[x], it[y], metric) | {"kind": kind}
                res[ds]["contrasts"][f"{x} - {y}"] = c
                if kind == "primary":
                    primary[ds] = c["p"]
                elif kind == "secondary":
                    secondary[ds] = c["p"]
        if ds == "medeinst_neg":
            res[ds]["without_diagnosis_named"] = {r: per_seed({s: {k: x for k, x in v.items() if x[1] == "hold"}
                                                                for s, v in seeds.items()}, share)
                                                  for r, seeds in it.items()}
    for fam, ps in (("primary", primary), ("secondary", secondary)):
        for ds, p in M.holm(ps).items() if ps else []:
            next(c for c in res[ds]["contrasts"].values() if c["kind"] == fam)["p_holm"] = p
    os.makedirs(a.out, exist_ok=True)
    json.dump(res, open(f"{a.out}/summary.json", "w", encoding="utf-8", newline="\n"), indent=1)
    for ds, r in res.items():
        L += [f"## {ds}: {r['metric']}", "", "| recipe | mean | s.d. | by seed |", "|---|---|---|---|"]
        L += [f"| {k} | {fmt(v['mean'])} | {fmt(v['sd'])} | " + ", ".join(f"s{s} {fmt(x)}" for s, x in v["by_seed"].items())
              + " |" for k, v in r["recipes"].items()]
        L += ["", "| contrast | kind | difference [95% CI] | p | p (Holm) |", "|---|---|---|---|---|"]
        L += [f"| {k} | {c['kind']} | {fmt(c['diff'])} [{fmt(c['lo'])}, {fmt(c['hi'])}] | {fmt(c['p'], 3)} | "
              f"{fmt(c.get('p_holm'), 3)} |" for k, c in r["contrasts"].items()]
        L.append("")
    if not res:
        L.append("not run")
    open(a.report, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print(json.dumps({ds: {k: v["mean"] for k, v in r["recipes"].items()} for ds, r in res.items()}, indent=1))


if __name__ == "__main__":
    main()
