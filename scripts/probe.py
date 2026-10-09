"""Exploratory probe (v13 App. 'Exploratory'; FINAL_TASKS_C P1, last): does the critic's residual stream encode the
criterion outcome on held-out signature classes? No GPU.
  python scripts/probe.py RUN_DIR [--data DIR]      (RUN_DIR holds hidden_rule_v1~test_{L0,L2}.npz from eval_c.py)
Records: the critic's verdict prompts for the conclusion claim s of the flip and near-miss cases (both mention the
target concept, so the outcome is not the keyword's presence); target = meta.criterion_holds (flip 1, near 0).
Train on rule_v1/test_L0 (training rules), test on rule_v1/test_L2 (rules of held-out signature classes, A's folds).
Logistic regression on standardised activations; layer and C chosen by 5-fold cross-validation grouped by rule on
L0 only, then fitted on all of L0 and applied once to L2. Control task (Hewitt and Liang 2019): each condition gets
a fixed random label (sha256 of the condition text), same pipeline. 95% CIs: bootstrap over rules (1,000).
Writes RUN_DIR/probe.json."""
import argparse, hashlib, json, os, sys

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.preprocessing import StandardScaler

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

CS = (0.001, 0.01, 0.1, 1.0)
KINDS = ("flip", "near")


def load(run_dir, data, name):
    z = np.load(f"{run_dir}/hidden_rule_v1~{name}.npz")
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    recs = {r["iid"]: r for r in map(json.loads, open(f"{data}/{reg['rule_v1/' + name]['path']}", encoding="utf-8"))}
    rows = [(i, recs[iid]) for i, iid in enumerate(z["iid"]) if recs[iid]["case_kind"] in KINDS]
    X = z["h"][[i for i, _ in rows]].astype(np.float32)          # (n, layers, d)
    R = [r for _, r in rows]
    y = np.array([int(r["meta"]["criterion_holds"]) for r in R])
    ctrl = np.array([hashlib.sha256(r["condition"].encode()).digest()[0] & 1 for r in R])
    return X, R, y, ctrl, [int(x) for x in z["layers"]]


def choose(X, y, groups):
    """(layer index, C) with the best grouped 5-fold accuracy on the training set."""
    best = None
    for li in range(X.shape[1]):
        for c in CS:
            acc = []
            for tr, va in GroupKFold(5).split(X, y, groups):
                sc = StandardScaler().fit(X[tr, li])
                m = LogisticRegression(C=c, max_iter=2000).fit(sc.transform(X[tr, li]), y[tr])
                acc.append((m.predict(sc.transform(X[va, li])) == y[va]).mean())
            if best is None or np.mean(acc) > best[0]:
                best = (float(np.mean(acc)), li, c)
    return best


def fit_eval(Xtr, ytr, gtr, Xte, yte, Rte, seen):
    cv, li, c = choose(Xtr, ytr, gtr)
    sc = StandardScaler().fit(Xtr[:, li])
    m = LogisticRegression(C=c, max_iter=2000).fit(sc.transform(Xtr[:, li]), ytr)
    ok = m.predict(sc.transform(Xte[:, li])) == yte
    items = [{"rid": r["rid"], "ok": bool(o), "seen": r["condition"] in seen} for r, o in zip(Rte, ok)]
    acc = lambda xs: 100.0 * sum(x["ok"] for x in xs) / len(xs)
    point, lo, hi = M.cluster_bootstrap(items, "rid", acc)
    un = [x for x in items if not x["seen"]]
    p2, lo2, hi2 = M.cluster_bootstrap(un, "rid", acc) if un else (None, None, None)
    return {"acc": point, "CI95": [lo, hi], "layer_index": li, "C": c, "cv_acc_train": 100.0 * cv,
            "unseen_conditions": {"acc": p2, "CI95": [lo2, hi2], "n": len(un)}}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    a = ap.parse_args()
    Xtr, Rtr, ytr, ctr, layers = load(a.run_dir, a.data, "test_L0")
    Xte, Rte, yte, cte, _ = load(a.run_dir, a.data, "test_L2")
    gtr = np.array([r["rid"] for r in Rtr])
    seen = {r["condition"] for r in Rtr}       # conditions of the training records (control labels are per condition)
    probe = fit_eval(Xtr, ytr, gtr, Xte, yte, Rte, seen)
    control = fit_eval(Xtr, ctr, gtr, Xte, cte, Rte, seen)
    out = {"run": os.path.basename(os.path.normpath(a.run_dir)), "train": "rule_v1/test_L0", "test": "rule_v1/test_L2",
           "records": "conclusion claim s of flip and near-miss cases", "target": "meta.criterion_holds",
           "layers": layers, "probe": probe | {"layer": layers[probe["layer_index"]]},
           "control": control | {"layer": layers[control["layer_index"]], "labels": "sha256(condition) first bit"},
           "selectivity": probe["acc"] - control["acc"], "n_train": len(ytr), "n_test": len(yte),
           "test_majority": 100.0 * max(yte.mean(), 1 - yte.mean()), "test_rules": len({r["rid"] for r in Rte}),
           "train_rules": len({r["rid"] for r in Rtr}), "shared_rules": len({r["rid"] for r in Rte} & {r["rid"] for r in Rtr}),
           "shared_conditions": len({r["condition"] for r in Rte} & {r["condition"] for r in Rtr})}
    json.dump(out, open(f"{a.run_dir}/probe.json", "w", encoding="utf-8", newline="\n"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
