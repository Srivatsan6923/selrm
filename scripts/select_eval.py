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
  combined     highest min(sigmoid(s_ledger / T_l), sigmoid(s_step / T_s)); T fitted on the MedQA dev
               pool (D-CAL) by the likelihood of trace correctness; also product and a logistic
               combination fitted on the same dev pool (reported in D-CAL)
  combined-swap  combined, both scores computed with another question's vignette
  no-nearmiss  combined with the ledger model trained on blocks (its own T)
  oracle       correct if any eligible sample is correct
Ineligible samples (no final answer) are never selected; a question with none counts as wrong.
Ties in a score -> the earliest sample. Every selection is deterministic.
Outputs: results/D-SEL-<name>/scores_sel~<pool>.jsonl {qid, sample, answer, correct} and
summary_sel~<pool>.json {"set", "acc", "n", "N"} (+ pair_acc etc. once C's key pairs and
MedEinst pairs exist); results/D-CAL/summary.json (temperatures, combination weights, dev
likelihoods); results/D-SELN/summary_sel~<pool>.json (selector=<name> slices with N1..N64).
Intervals and paired tests come from selrm.metrics (C) once it has an item-level bootstrap.
"""
import argparse
import json
import math
import os
from collections import Counter

import numpy as np
from scipy.optimize import minimize

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEV = "medqa_dev"


def load_pool(d):
    qs = {q["qid"]: q for q in map(json.loads, open(os.path.join(d, "questions.jsonl"), encoding="utf-8"))}
    by_q = {}
    for s in map(json.loads, open(os.path.join(d, "samples.jsonl"), encoding="utf-8")):
        by_q.setdefault(s["qid"], {})[s["sample"]] = s
    return qs, by_q


def load_scores(path):
    if not os.path.exists(path):
        return None
    out = {}
    for j in map(json.loads, open(path, encoding="utf-8")):
        out[(j["qid"], j["sample"])] = j["score"]
    return out


def sig(x):
    return 1.0 / (1.0 + math.exp(-max(-60.0, min(60.0, x))))


def fit_temperature(scores, labels):
    """T > 0 maximising the likelihood of sigmoid(s / T) for the correctness labels."""
    s, y = np.array(scores, float), np.array(labels, float)

    def nll(logt):
        p = 1 / (1 + np.exp(-np.clip(s / math.exp(logt[0]), -60, 60)))
        return -np.mean(y * np.log(p + 1e-12) + (1 - y) * np.log(1 - p + 1e-12))
    r = minimize(nll, [0.0], method="Nelder-Mead")
    return float(math.exp(r.x[0])), float(r.fun)


def fit_logistic(x1, x2, labels):
    X, y = np.column_stack([x1, x2, np.ones(len(x1))]), np.array(labels, float)

    def nll(w):
        p = 1 / (1 + np.exp(-np.clip(X @ w, -60, 60)))
        return -np.mean(y * np.log(p + 1e-12) + (1 - y) * np.log(1 - p + 1e-12))
    r = minimize(nll, np.zeros(3), method="Nelder-Mead", options={"maxiter": 4000})
    return [float(v) for v in r.x], float(r.fun)


def pick(cands, key):
    """cands: [(sample, answer)] eligible, in sample order; key(sample) -> score (None: never picked)."""
    best = None
    for k, ans in cands:
        v = key(k)
        if v is not None and (best is None or v > best[0]):
            best = (v, k, ans)
    return (best[1], best[2]) if best else (None, None)


def calibrate(pools, scores_dir):
    """D-CAL: temperatures for every scorer and the logistic combination, on the dev pool."""
    qs, by_q = load_pool(os.path.join(pools, DEV))
    cal = {"pool": DEV, "temperatures": {}, "nll": {}}
    sc = {n: load_scores(os.path.join(scores_dir, DEV, f"{n}.jsonl")) for n in
          ("medprm", "ledger2-triplets", "ledger2-blocks")}
    rows = [(qid, k, s["final"] == qs[qid]["answer"]) for qid, ss in by_q.items() for k, s in ss.items() if s["eligible"]]
    for n, s in sc.items():
        if s:
            pts = [(s[(q, k)], y) for q, k, y in rows if s.get((q, k)) is not None]
            cal["temperatures"][n], cal["nll"][n] = fit_temperature([p for p, _ in pts], [y for _, y in pts])
    for led in ("ledger2-triplets", "ledger2-blocks"):
        if sc["medprm"] and sc[led]:
            pts = [(sc[led][(q, k)], sc["medprm"][(q, k)], y) for q, k, y in rows
                   if sc[led].get((q, k)) is not None and sc["medprm"].get((q, k)) is not None]
            cal[f"logistic:{led}"], cal[f"nll:logistic:{led}"] = fit_logistic(*zip(*pts))
    cal["n_traces"] = len(rows)
    return cal


def selectors(cal, sc):
    T = cal["temperatures"]

    def p(n, s, k):
        v = s.get(k)
        return None if v is None or n not in T else sig(v / T[n])

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
    if sc.get("ledger2-triplets"):
        out["ledger"] = lambda k: sc["ledger2-triplets"].get(k)
    if sc.get("ledger2-triplets") and sc.get("medprm"):
        for mode, name in (("min", "combined"), ("product", "combined-product"), ("logistic", "combined-logistic")):
            out[name] = comb(("ledger2-triplets", sc["ledger2-triplets"]), sc["medprm"], mode)
    if sc.get("ledger2-triplets-swap") and sc.get("medprm-swap"):
        out["combined-swap"] = comb(("ledger2-triplets", sc["ledger2-triplets-swap"]), sc["medprm-swap"])
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


def write(out_root, run, pool, rows, extra=None):
    d = os.path.join(out_root, run)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"scores_sel~{pool}.jsonl"), "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    summ = {"run_id": run, "set": f"sel/{pool}", "acc": 100.0 * sum(r["correct"] for r in rows) / len(rows),
            "n": len(rows)} | (extra or {})
    json.dump(summ, open(os.path.join(d, f"summary_sel~{pool}.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    return summ


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pools", required=True)
    ap.add_argument("--scores", required=True)
    ap.add_argument("--out", default=os.path.join(ROOT, "results"))
    ap.add_argument("--pool", action="append", default=None)
    a = ap.parse_args()
    cal = calibrate(a.pools, a.scores)
    os.makedirs(os.path.join(a.out, "D-CAL"), exist_ok=True)
    json.dump(cal, open(os.path.join(a.out, "D-CAL", "summary.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    open(os.path.join(a.out, "D-CAL", "DONE"), "w").close()
    for pool in a.pool or ("medqa_test", "careqa_en"):
        if not os.path.exists(os.path.join(a.pools, pool, "DONE")):
            continue
        qs, by_q = load_pool(os.path.join(a.pools, pool))
        sc = {n: load_scores(os.path.join(a.scores, pool, f"{n}.jsonl")) for n in
              ("medprm", "medprm-swap", "ledger2-triplets", "ledger2-triplets-swap", "ledger2-blocks")}
        sel = selectors(cal, sc)
        for name, fn in sel.items():
            s = write(a.out, f"D-SEL-{name}", pool, select(name, fn, qs, by_q, 16), {"N": 16})
            print(pool, name, round(s["acc"], 1))
        sub = {q for q, x in qs.items() if x.get("subset64")}
        if sub:                     # selection pressure on the 64-sample subset
            curve = {}
            for name in ("combined", "stepcheck", "oracle", "ledger", "selfcons"):
                if name in sel:
                    curve[f"selector={name}"] = {
                        f"N{n}": 100.0 * sum(r["correct"] for r in select(name, sel[name], qs, {q: by_q[q] for q in sub}, n))
                        / len(sub) for n in (1, 2, 4, 8, 16, 32, 64)}
            d = os.path.join(a.out, "D-SELN")
            os.makedirs(d, exist_ok=True)
            json.dump({"run_id": "D-SELN", "set": f"sel/{pool}", "n_questions": len(sub)} | curve,
                      open(os.path.join(d, f"summary_sel~{pool}.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    for run in os.listdir(a.out):
        if run.startswith("D-SEL"):
            open(os.path.join(a.out, run, "DONE"), "w").close()


if __name__ == "__main__":
    main()
