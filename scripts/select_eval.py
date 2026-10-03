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
Outputs: results/D-SEL-<name>/scores_sel~<set>.jsonl {qid, sample, answer, correct} and
summary_sel~<set>.json, set = sel/medqa, sel/careqa, sel/medeinst (+ control_acc, trap_acc, pair_acc)
and sel/keypairs (pair_acc: both questions of a MedQA key pair right; pairs from C, --keypairs);
results/D-CAL/summary.json (temperatures, combination weights, dev likelihoods);
results/D-SELN/summary_sel~keypairs.json (slices selector=<name> with N1..N64: key-pair accuracy
among the first N samples of the key-pair questions extended to 64 samples).
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


POOL_SET = {"medqa_test": "medqa", "careqa_en": "careqa", "medeinst_test": "medeinst"}   # set sel/<name>


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
    ap.add_argument("--keypairs", help="C's MedQA key pairs: JSON list of [row_a, row_b] (rows of the MedQA test file)")
    a = ap.parse_args()
    cal = calibrate(a.pools, a.scores)
    os.makedirs(os.path.join(a.out, "D-CAL"), exist_ok=True)
    json.dump(cal, open(os.path.join(a.out, "D-CAL", "summary.json"), "w", encoding="utf-8", newline="\n"), indent=1)
    open(os.path.join(a.out, "D-CAL", "DONE"), "w").close()
    pairs = [(f"medqa_test-{x:05d}", f"medqa_test-{y:05d}") for x, y in json.load(open(a.keypairs))] if a.keypairs else []
    for pool in a.pool or ("medqa_test", "careqa_en", "medeinst_test"):
        if not os.path.exists(os.path.join(a.pools, pool, "DONE")):
            continue
        qs, by_q = load_pool(os.path.join(a.pools, pool))
        sc = {n: load_scores(os.path.join(a.scores, pool, f"{n}.jsonl")) for n in
              ("medprm", "medprm-swap", "ledger2-triplets", "ledger2-triplets-swap", "ledger2-blocks")}
        sel = selectors(cal, sc)
        for name, fn in sel.items():
            rows = select(name, fn, qs, by_q, 16)
            extra = {"N": 16} | (pair_metrics(qs, rows) if pool == "medeinst_test" else {})
            s = write(a.out, f"D-SEL-{name}", POOL_SET[pool], rows, extra)
            print(pool, name, round(s["acc"], 1), {k: v for k, v in extra.items() if k.endswith("acc")})
            if pool == "medqa_test" and pairs:
                acc, n_pairs = keypair_acc(pairs, {r["qid"]: r["correct"] for r in rows})
                write(a.out, f"D-SEL-{name}", "keypairs", [r for r in rows if any(r["qid"] in p for p in pairs)],
                      {"N": 16, "pair_acc": acc, "n_pairs": n_pairs})
        ext = {q for q, ss in by_q.items() if len(ss) >= 64}
        if pool == "medqa_test" and pairs and ext:   # selection pressure on the key-pair questions with 64 samples
            kp = [(x, y) for x, y in pairs if x in ext and y in ext]
            curve = {}
            for name in ("combined", "stepcheck", "oracle", "ledger", "selfcons"):
                if name in sel:
                    curve[f"selector={name}"] = {}
                    for n in (1, 2, 4, 8, 16, 32, 64):
                        rows = select(name, sel[name], qs, {q: by_q[q] for q in ext}, n)
                        curve[f"selector={name}"][f"N{n}"] = keypair_acc(kp, {r["qid"]: r["correct"] for r in rows})[0]
            d = os.path.join(a.out, "D-SELN")
            os.makedirs(d, exist_ok=True)
            json.dump({"run_id": "D-SELN", "set": "sel/keypairs", "n_pairs": len(kp)} | curve,
                      open(os.path.join(d, "summary_sel~keypairs.json"), "w", encoding="utf-8", newline="\n"), indent=1)
            open(os.path.join(d, "DONE"), "w").close()
    for run in os.listdir(a.out):
        if run.startswith("D-SEL"):
            open(os.path.join(a.out, run, "DONE"), "w").close()


if __name__ == "__main__":
    main()
