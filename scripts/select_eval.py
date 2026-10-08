"""Answer selection on candidate pools (D-CAL, D-SEL-*, D-SELN; Table 5, Fig. 3 right).

  python scripts/select_eval.py --pools DIR --scores DIR --out results [--pool medqa_test ...]

Inputs: pools from scripts/make_pool.py (DIR/<pool>/questions.jsonl, samples.jsonl) and
trace scores from scripts/score_pool.py (SCORES/<pool>/<scorer>.jsonl; scorers: medprm,
medprm-swap, ledger2-triplets, ledger2-triplets-swap, ledger2-blocks). Trace score = the
minimum of its step scores (log-odds), as written by score_pool.py.

Selectors (one D-SEL-<name> run each; N = 16 samples, nested pools):
  single       sample 0
  selfcons     majority vote over eligible samples; ties -> the earliest sample among the tied answers
  stepcheck    highest step-check trace score;  stepcheck-swap: scores with another question's vignette
  ledger       highest Ledger-RM trace score
  combined     highest min(sigmoid(a_l s_ledger + b_l), sigmoid(a_s s_step + b_s)); a, b per scorer by
               Platt scaling on the MedQA dev pool (D-CAL), likelihood of trace correctness; also the
               product and a logistic combination fitted on the same dev pool
  combined-swap  combined, both scores computed with another question's vignette
  no-nearmiss  combined with the ledger model trained on blocks (its own a, b)
  oracle       correct if any eligible sample is correct
Ineligible samples (no final answer) are never selected; a question with none counts as wrong.
Ties in a score -> the earliest sample. Every selection is deterministic.
Outputs: results/D-SEL-<name>/scores_sel~<set>.jsonl {qid, sample, answer, correct} and
summary_sel~<set>.json, set = sel/medqa, sel/careqa, sel/medeinst (+ control_acc, trap_acc, pair_acc)
and sel/keypairs (pool medqa_kp; pair_acc: both questions of a MedQA key pair right; the pairs are
C's clin_v1/keypairs_medqa_oneway, configs/keypairs_d.json);
results/D-CAL/summary.json (Platt parameters, combination weights, dev likelihoods and AUCs; key-pair
questions are left out of the dev pool);
results/D-SELN/summary_sel~keypairs.json (slices selector=<name> with N1..N64: key-pair accuracy
among the first N samples of the key-pair questions extended to 64 samples).
results_git/D-SEL-comparisons.json: paired differences a - b of two selectors on identical items
(SEL_CMP), bootstrap over questions (key pairs, MedEinst: whole pairs) with C's
selrm.metrics.paired_cluster_bootstrap (1,000 resamples, seed 0); read by make_tables as cmp/<name>/<field>.
"""
import argparse
import json
import math
import os
from collections import Counter

import sys

import numpy as np
from scipy.optimize import minimize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from selrm import metrics as M  # noqa: E402
from selrm.formats import MALFORMED_U  # noqa: E402

DEV = "medqa_dev"
LEDGERS = ("ledger2-triplets", "ledger2-blocks", "ledger2-tripclin")
MAIN = {"triplets": "ledger2-triplets", "tripclin": "ledger2-tripclin"}
# Paired selector comparisons stated in the text of Table 5 (name, pool, a, b): a - b.
SEL_CMP = [("sel-mqa-comb-step", "medqa_test", "combined", "stepcheck"),
           ("sel-cqa-comb-step", "careqa_en", "combined", "stepcheck"),
           ("sel-key-comb-step", "medqa_kp", "combined", "stepcheck"),
           ("sel-me-comb-step", "medeinst_test", "combined", "stepcheck"),
           ("sel-mqa-comb-swap", "medqa_test", "combined", "combined-swap"),
           ("sel-mqa-step-swap", "medqa_test", "stepcheck", "stepcheck-swap"),
           ("sel-mqa-comb-nonear", "medqa_test", "combined", "no-nearmiss"),
           ("sel-me-comb-nonear", "medeinst_test", "combined", "no-nearmiss")]


POOL_SET = {"medqa_test": "medqa", "careqa_en": "careqa", "medeinst_test": "medeinst",
            "medqa_kp": "keypairs"}   # set sel/<name>
PAIRS = [tuple(p) for p in json.load(open(os.path.join(ROOT, "configs", "keypairs_d.json"), encoding="utf-8"))["pairs"]]
KPQ = {q for p in PAIRS for q in p}


def load_pool(d):
    """Questions and samples; the extension (samples 16-63 of the key-pair questions) is merged in."""
    qs = {q["qid"]: q for q in map(json.loads, open(os.path.join(d, "questions.jsonl"), encoding="utf-8"))}
    by_q = {}
    for f in ("samples.jsonl", "samples_ext.jsonl"):
        if os.path.exists(os.path.join(d, f)):
            for s in map(json.loads, open(os.path.join(d, f), encoding="utf-8")):
                by_q.setdefault(s["qid"], {})[s["sample"]] = s
    return qs, by_q


def load_scores(path):
    """Trace scores of a scorer, with those of the pool extension (<scorer>.ext.jsonl) merged in."""
    if not os.path.exists(path):
        return None
    out = {}
    for p in (path, path[:-len(".jsonl")] + ".ext.jsonl"):
        if os.path.exists(p):
            for j in map(json.loads, open(p, encoding="utf-8")):
                out[(j["qid"], j["sample"])] = j["score"]
    return out


def pair_metrics(qs, rows):
    """MedEinst: control, trap and pair accuracy (both cases of a pair right), over the pool's pairs."""
    by = {}
    for r in rows:
        m = qs[r["qid"]]["meta"]
        by.setdefault(m["case_id"], {})[m["case_type"]] = r["correct"]
    pct = lambda xs: 100.0 * sum(xs) / len(xs) if xs else None
    full = [v for v in by.values() if set(v) == {"control", "trap"}]
    return {"control_acc": pct([v["control"] for v in full]), "trap_acc": pct([v["trap"] for v in full]),
            "pair_acc": pct([v["control"] and v["trap"] for v in full]), "n_pairs": len(full)}


def keypair_acc(pairs, correct):
    """Share of key pairs whose two questions are both answered correctly by the selected traces."""
    full = [(a, b) for a, b in pairs if a in correct and b in correct]
    return (100.0 * sum(correct[a] and correct[b] for a, b in full) / len(full) if full else None), len(full)


def units(pool, qs, rows):
    """{unit: correct}: per question, or per pair (both questions right) for key pairs and MedEinst."""
    c = {r["qid"]: r["correct"] for r in rows}
    if pool == "medqa_kp":
        return {f"{a}|{b}": c[a] and c[b] for a, b in PAIRS if a in c and b in c}
    if pool == "medeinst_test":
        by = {}
        for q, v in c.items():
            by.setdefault(qs[q]["meta"]["case_id"], []).append(v)
        return {k: all(v) for k, v in by.items() if len(v) == 2}
    return c


def compare(ua, ub):
    """a - b in points on identical units, paired bootstrap over units (C's paired_cluster_bootstrap)."""
    items = [(k, ua[k], ub[k]) for k in sorted(ua.keys() & ub.keys())]
    pct = lambda i: (lambda xs: 100.0 * sum(x[i] for x in xs) / len(xs))
    return M.paired_cluster_bootstrap(items, lambda x: x[0], pct(1), pct(2))


def sig(x):
    return 1.0 / (1.0 + math.exp(-max(-60.0, min(60.0, x))))


def fit_logistic(xs, labels):
    """[w_1..w_m, b] maximising the likelihood of sigmoid(w . x + b) for the correctness labels: Platt
    scaling for one score, the fitted combination for two. Fitted on standardised columns (conditioning),
    returned on the original scale. A temperature alone, sigmoid(s / T), cannot fit these scores: they
    are mostly negative while most traces are correct (D-CAL of 3 Oct: T -> infinity)."""
    X, y = np.column_stack(xs).astype(float), np.array(labels, float)
    mu, sd = X.mean(0), X.std(0) + 1e-12
    Z = np.column_stack([(X - mu) / sd, np.ones(len(X))])

    def nll(w):
        p = 1 / (1 + np.exp(-np.clip(Z @ w, -60, 60)))
        return -np.mean(y * np.log(p + 1e-12) + (1 - y) * np.log(1 - p + 1e-12))
    r = minimize(nll, np.zeros(Z.shape[1]), method="Nelder-Mead", options={"maxiter": 4000})
    w = r.x[:-1] / sd
    return [float(v) for v in w] + [float(r.x[-1] - (r.x[:-1] * mu / sd).sum())], float(r.fun)


def auc(scores, labels):
    """Probability that a correct trace scores above an incorrect one (ties count one half)."""
    from scipy.stats import rankdata
    r, y = rankdata(scores), np.array(labels, bool)
    n1, n0 = y.sum(), (~y).sum()
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)) if n1 and n0 else None


def pick(cands, key):
    """cands: [(sample, answer)] eligible, in sample order; key(sample) -> score (None: never picked)."""
    best = None
    for k, ans in cands:
        v = key(k)
        if v is not None and (best is None or v > best[0]):
            best = (v, k, ans)
    return (best[1], best[2]) if best else (None, None)


def calibrate(pools, scores_dir):
    """D-CAL: Platt scaling of every scorer and the logistic combination, on the dev pool."""
    qs, by_q = load_pool(os.path.join(pools, DEV))
    cal = {"pool": DEV, "platt": {}, "nll": {}, "auc": {}}
    sc = {n: load_scores(os.path.join(scores_dir, DEV, f"{n}.jsonl")) for n in
          ("medprm",) + LEDGERS}
    # questions of a key pair are test items (validation rows of C's key pairs): never calibrated on
    rows = [(qid, k, s["final"] == qs[qid]["answer"]) for qid, ss in by_q.items() if qid not in KPQ
            for k, s in ss.items() if s["eligible"]]
    for n, s in sc.items():
        if s:
            pts = [(s[(q, k)], y) for q, k, y in rows if s.get((q, k)) is not None]
            cal["platt"][n], cal["nll"][n] = fit_logistic([[p for p, _ in pts]], [y for _, y in pts])
            cal["auc"][n] = auc([p for p, _ in pts], [y for _, y in pts])
    for led in LEDGERS:
        if sc["medprm"] and sc[led]:
            pts = [(sc[led][(q, k)], sc["medprm"][(q, k)], y) for q, k, y in rows
                   if sc[led].get((q, k)) is not None and sc["medprm"].get((q, k)) is not None]
            x1, x2, y = zip(*pts)
            cal[f"logistic:{led}"], cal[f"nll:logistic:{led}"] = fit_logistic([x1, x2], y)
    # the pre-specified trace score is the minimum step score (malformed reader output: MALFORMED_U);
    # dev AUC of the ledger scores under alternative aggregations, reported, never used for selection
    alt = {"mean": lambda u, w: float(np.mean(u)), "last": lambda u, w: u[-1],
           "min_well_formed": lambda u, w: min([x for x, ok in zip(u, w) if ok] or [MALFORMED_U])}
    for led in LEDGERS:
        f = os.path.join(scores_dir, DEV, f"{led}.jsonl")
        if os.path.exists(f):
            J = {(j["qid"], j["sample"]): j for j in map(json.loads, open(f, encoding="utf-8"))}
            got = [(J[(q, k)], y) for q, k, y in rows if "well_formed" in J.get((q, k), {})]
            if not got:
                continue
            cal.setdefault("auc_alt", {})[led] = {a: auc([g(j["u"], j["well_formed"]) for j, _ in got],
                                                         [y for _, y in got]) for a, g in alt.items()}
            cal.setdefault("share_traces_with_malformed_step", {})[led] = float(
                np.mean([not all(j["well_formed"]) for j, _ in got]))
    cal["n_traces"], cal["correct_share"] = len(rows), float(np.mean([y for _, _, y in rows]))
    cal["n_questions"], cal["excluded_keypair_questions"] = len(set(by_q) - KPQ), len(set(by_q) & KPQ)
    return cal


def selectors(cal, sc, main="ledger2-triplets"):
    """main: the ledger model of the Ledger and Combined rows (--ledger); with the clinical-pairs model the
    rule-only model stays as ledger-rule / combined-rule, the reference of no-nearmiss."""
    A = cal["platt"]

    def p(n, s, k):
        v = s.get(k)
        return None if v is None or n not in A else sig(A[n][0] * v + A[n][1])

    def comb(led, step, mode="min"):
        def f(k):
            a, b = p(led[0], led[1], k), p("medprm", step, k)
            if a is None or b is None:
                return None
            if mode == "min":
                return min(a, b)
            if mode == "product":
                return a * b
            w = cal.get(f"logistic:{led[0]}")
            return None if not w else w[0] * led[1][k] + w[1] * step[k] + w[2]
        return f
    out = {"single": None, "selfcons": None, "oracle": None}
    if sc.get("medprm"):
        out["stepcheck"] = lambda k: sc["medprm"].get(k)
    if sc.get("medprm-swap"):
        out["stepcheck-swap"] = lambda k: sc["medprm-swap"].get(k)
    if sc.get(main):
        out["ledger"] = lambda k: sc[main].get(k)
    if sc.get(main) and sc.get("medprm"):
        for mode, name in (("min", "combined"), ("product", "combined-product"), ("logistic", "combined-logistic")):
            out[name] = comb((main, sc[main]), sc["medprm"], mode)
    if sc.get(main + "-swap") and sc.get("medprm-swap"):
        out["combined-swap"] = comb((main, sc[main + "-swap"]), sc["medprm-swap"])
    if main != "ledger2-triplets" and sc.get("ledger2-triplets") and sc.get("medprm"):
        out["ledger-rule"] = lambda k: sc["ledger2-triplets"].get(k)
        out["combined-rule"] = comb(("ledger2-triplets", sc["ledger2-triplets"]), sc["medprm"])
    if sc.get("ledger2-blocks") and sc.get("medprm"):
        out["no-nearmiss"] = comb(("ledger2-blocks", sc["ledger2-blocks"]), sc["medprm"])
    return out


def select(name, fn, qs, by_q, n):
    rows = []
    for qid in sorted(by_q):
        ss = by_q[qid]
        cands = [(k, ss[k]["final"]) for k in sorted(ss) if k < n and ss[k]["eligible"]]
        gold = qs[qid]["answer"]
        if name == "single":
            k, ans = (0, ss[0]["final"]) if 0 in ss and ss[0]["eligible"] else (None, None)
        elif name == "selfcons":
            c = Counter(a for _, a in cands)
            top = max(c.values()) if c else 0
            k, ans = next(((k, a) for k, a in cands if c[a] == top), (None, None))
        elif name == "oracle":
            k, ans = next(((k, a) for k, a in cands if a == gold), cands[0] if cands else (None, None))
        else:
            k, ans = pick(cands, lambda s: fn((qid, s)))
        rows.append({"qid": qid, "sample": k, "answer": ans, "correct": ans == gold})
    return rows


def write(out_root, run, name, rows, extra=None):
    """results/<run>/scores_sel~<name>.jsonl (per question) and summary_sel~<name>.json (set sel/<name>)."""
    d = os.path.join(out_root, run)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"scores_sel~{name}.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    summ = {"run_id": run, "set": f"sel/{name}",
            "acc": 100.0 * sum(r["correct"] for r in rows) / len(rows) if rows else None,
            "n": len(rows)} | (extra or {})
    json.dump(summ, open(os.path.join(d, f"summary_sel~{name}.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    return summ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", required=True)
    ap.add_argument("--scores", required=True)
    ap.add_argument("--out", default=os.path.join(ROOT, "results"))
    ap.add_argument("--pool", action="append", default=None)
    ap.add_argument("--ledger", choices=sorted(MAIN), default="triplets",
                    help="ledger model of the Ledger and Combined rows: rule triplets, or rule triplets + clinical pairs "
                         "(B-TR-tripclin-s0; only once every pool is scored with it, DECISIONS_D 3 Oct)")
    a = ap.parse_args()
    cal = calibrate(a.pools, a.scores)
    os.makedirs(os.path.join(a.out, "D-CAL"), exist_ok=True)
    json.dump(cal, open(os.path.join(a.out, "D-CAL", "summary.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    open(os.path.join(a.out, "D-CAL", "DONE"), "w").close()
    by_sel = {}
    for pool in a.pool or ("medqa_test", "careqa_en", "medeinst_test", "medqa_kp"):
        if not os.path.exists(os.path.join(a.pools, pool, "DONE")):
            continue
        qs, by_q = load_pool(os.path.join(a.pools, pool))
        man = json.load(open(os.path.join(a.pools, pool, "MANIFEST.json"), encoding="utf-8"))
        d = os.path.join(a.out, f"D-POOL-{pool}")          # the pool's own facts as a result (App. G)
        os.makedirs(d, exist_ok=True)
        json.dump({"run_id": f"D-POOL-{pool}"} | {k: man.get(k) for k in (
            "n_questions", "n_samples", "eligible", "ineligible_share", "generated_tokens", "wall_seconds", "gpu",
            "vllm", "sampling", "policy", "question_sample")}, open(os.path.join(d, "summary.json"), "w",
                                                                 encoding="utf-8", newline="\n"), indent=1)
        open(os.path.join(d, "DONE"), "w").close()
        sc = {n: load_scores(os.path.join(a.scores, pool, f"{n}.jsonl")) for n in
              ("medprm", "medprm-swap", "ledger2-triplets", "ledger2-triplets-swap", "ledger2-blocks",
               "ledger2-tripclin", "ledger2-tripclin-swap")}
        sel = selectors(cal, sc, MAIN[a.ledger])
        rows_by = {name: select(name, fn, qs, by_q, 16) for name, fn in sel.items()}
        diag = {}
        if "combined-swap" in rows_by and "stepcheck-swap" in rows_by:
            # why the swapped rows coincide: the minimum of the two calibrated scores is the step check's
            # wherever the ledger's calibrated probability is the larger one
            A, m = cal["platt"], MAIN[a.ledger]

            def led_min(led, step):
                ks = [k for k in step if led.get(k) is not None and step[k] is not None]
                return 100.0 * sum(sig(A[m][0] * led[k] + A[m][1]) < sig(A["medprm"][0] * step[k] + A["medprm"][1])
                                   for k in ks) / len(ks)
            pairs = list(zip(rows_by["combined-swap"], rows_by["stepcheck-swap"]))
            diag = {"n_same_sample_as_stepcheck_swap": sum(x["sample"] == y["sample"] for x, y in pairs),
                    "n_same_answer_as_stepcheck_swap": sum(x["answer"] == y["answer"] for x, y in pairs),
                    "ledger_is_minimum_share": led_min(sc[m], sc["medprm"]),
                    "ledger_is_minimum_share_swap": led_min(sc[m + "-swap"], sc["medprm-swap"])}
        for name, rows in rows_by.items():
            extra = {"N": 16} | (pair_metrics(qs, rows) if pool == "medeinst_test" else {})
            if name == "combined-swap":
                extra |= diag
            if pool == "medqa_kp":
                extra |= dict(zip(("pair_acc", "n_pairs"), keypair_acc(PAIRS, {r["qid"]: r["correct"] for r in rows})))
            by_sel[(pool, name)] = units(pool, qs, rows)
            s = write(a.out, f"D-SEL-{name}", POOL_SET[pool], rows, extra)
            print(pool, name, round(s["acc"], 1), {k: v for k, v in extra.items() if k.endswith("acc")})
        ext = {q for q, ss in by_q.items() if len(ss) >= 64}
        if pool == "medqa_kp" and ext:   # selection pressure on the key-pair questions with 64 samples
            kp = [(x, y) for x, y in PAIRS if x in ext and y in ext]
            curve, per = {}, []
            for name in ("combined", "stepcheck", "oracle", "ledger", "selfcons"):
                if name in sel:
                    curve[f"selector={name}"] = {}
                    for n in (1, 2, 4, 8, 16, 32, 64):
                        rows = select(name, sel[name], qs, {q: by_q[q] for q in ext}, n)
                        curve[f"selector={name}"][f"N{n}"] = keypair_acc(kp, {r["qid"]: r["correct"] for r in rows})[0]
                        per += [{"selector": name, "N": n} | r for r in rows]
            d = os.path.join(a.out, "D-SELN")
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "scores_sel~keypairs.jsonl"), "w", encoding="utf-8", newline="\n") as f:
                f.writelines(json.dumps(r) + "\n" for r in per)
            json.dump({"run_id": "D-SELN", "set": "sel/keypairs", "n_pairs": len(kp)} | curve,
                      open(os.path.join(d, "summary_sel~keypairs.json"), "w", encoding="utf-8", newline="\n"), indent=1)
            open(os.path.join(d, "DONE"), "w").close()
    cp = os.path.join(a.out, "D-SEL-comparisons.json")
    cmp = json.load(open(cp, encoding="utf-8")) if os.path.exists(cp) else {}
    for name, pool, x, y in SEL_CMP:
        if x == "combined" and y == "no-nearmiss" and (pool, "combined-rule") in by_sel:
            x = "combined-rule"      # only the near-misses differ (rule-only blocks vs rule-only triplets)
        if (pool, x) in by_sel and (pool, y) in by_sel:
            cmp[name] = {"pool": pool, "a": x, "b": y, "set": f"sel/{POOL_SET[pool]}",
                         "metric": "acc" if pool in ("medqa_test", "careqa_en") else "pair_acc"} | compare(
                by_sel[(pool, x)], by_sel[(pool, y)])
    if cmp:
        json.dump(cmp, open(cp, "w", encoding="utf-8", newline="\n"), indent=1)
    for run in os.listdir(a.out):
        if run.startswith("D-SEL") and os.path.isdir(os.path.join(a.out, run)):
            open(os.path.join(a.out, run, "DONE"), "w").close()


if __name__ == "__main__":
    main()
