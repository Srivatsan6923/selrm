"""Checks for the metric extensions (owner C). Run: python tests/test_metrics_c.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import metrics as M


def rec(tid, kind, role, label, ct="conclusion", rid="r1", nm="time", fam="f1", meta=None):
    return {"tid": tid, "case_kind": kind, "claim_role": role, "label": label, "claim_type": ct, "rid": rid,
            "nm_kind": nm, "tier": "easy", "level": "L2", "family": fam, "meta": meta or {}}


def triplet(tid, d, rid="r1", nm="time", fam="f1"):
    """records + scores realising d = {case_kind: d} (u(s) = d, u(s') = 0)."""
    R, S = [], []
    lab = {"base": (1, 0), "flip": (0, 1), "near": (1, 0), "pres": (1, 0)}
    for k, v in d.items():
        for role, lb, u in (("s", lab[k][0], v), ("s_prime", lab[k][1], 0.0)):
            R.append(rec(tid, k, role, lb, rid=rid, nm=nm, fam=fam))
            S.append(u)
    return R, S


def build(spec):
    R, S = [], []
    for args in spec:
        r, s = triplet(*args)
        R += r; S += s
    return R, S


def test_nearmiss_and_macro():
    R, S = build([("t1", {"base": 1, "flip": -1, "near": 1}, "r1", "time"),
                  ("t2", {"base": 1, "flip": -1, "near": -1}, "r1", "time"),
                  ("t3", {"base": -1, "flip": -1, "near": -1}, "r2", "subject"),
                  ("t4", {"base": 1, "flip": -1, "near": 0}, "r2", "subject")])
    T = M.decisions(R, S)
    nm = M.nearmiss_table(T)
    a = nm["all"]
    assert a["n"] == 4 and a["n_base_correct"] == 3
    assert abs(a["SameDecision"] - 50.0) < 1e-9          # t1 (s,s), t3 (s',s'); t2, t4 differ
    assert abs(a["BothCorrect"] - 25.0) < 1e-9           # t1
    assert abs(a["NearGivenBase"] - 100 / 3) < 1e-9      # t1 of t1, t2, t4
    assert abs(a["UnnecessaryReversal"] - 100 / 3) < 1e-9  # t2
    assert abs(a["TieGivenBase"] - 100 / 3) < 1e-9       # t4
    assert nm["nm_kind=subject"]["n"] == 2
    mac = M.macro(T, "TA", "rid")
    assert mac["by"] == {"r1": 50.0, "r2": 0.0} and mac["macro"] == 25.0


def test_mr_matches_role_b_formula():
    dev = [rec(f"d{i}", "base", "s", 1) for i in range(40)] + [rec("dm", "missing", "s", 0)]
    us = [float(i) for i in range(40)] + [100.0]
    tau = M.mr_threshold(dev, us)
    assert tau == sorted(us[:40])[int(0.05 * 40)] == 2.0
    test = [rec("m1", "missing", "s", 0), rec("m1", "missing", "s_prime", 0),
            rec("m2", "missing", "s", 0), rec("m2", "missing", "s_prime", 0), rec("o", "base", "s", 1)]
    out = M.missing_rejection(test, [1.0, 1.5, 1.0, 3.0, 1.0], tau)
    assert out["MR"] == 50.0 and out["n_missing"] == 2 and out["FR"] == 100.0


def test_paired_and_holm():
    R, S = build([(f"t{i}", {"base": 1, "flip": -1, "near": 1}, f"r{i % 5}") for i in range(20)])
    T = M.decisions(R, S)
    out = M.paired_test(T, T)
    assert out["diff"] == 0 and out["lo"] == 0 and out["hi"] == 0 and out["p"] == 1.0 and out["n_clusters"] == 5
    R2, S2 = build([(f"t{i}", {"base": 1, "flip": -1, "near": -1 if i < 10 else 1}, f"r{i % 5}") for i in range(20)])
    out2 = M.paired_test(T, M.decisions(R2, S2))
    assert abs(out2["diff"] - 50.0) < 1e-9 and out2["p"] < 0.05
    assert M.paired_diff(T, M.decisions(R2, S2))[0] == out2["diff"]
    h = M.holm({"a": 0.01, "b": 0.04, "c": 0.03})
    assert abs(h["a"]["p_holm"] - 0.03) < 1e-12 and abs(h["c"]["p_holm"] - 0.06) < 1e-12
    assert abs(h["b"]["p_holm"] - 0.06) < 1e-12 and h["a"]["reject"] and not h["b"]["reject"]


def test_crossed_accuracy():
    R, S = [], []
    for item, ok in (("x1", True), ("x2", False)):
        for rule in ("a", "b"):
            for c in range(3):
                y = 1 if (rule == "a") == (c == 0) else -1
                d = y if (ok or (rule, c) != ("b", 2)) else -y
                tid = f"{item}_{rule}{c}"
                for role, lb, u in (("s", int(y > 0), d), ("s_prime", int(y < 0), 0.0)):
                    R.append(rec(tid, "base", role, lb, meta={"xr_item": item}))
                    S.append(u)
    out = M.crossed_accuracy(R, S)
    assert out["n_items"] == 2 and out["XA"] == 50.0 and out["n_cells"] == 12
    assert abs(out["CellAcc"] - 100 * 11 / 12) < 1e-9


def test_step_revisions():
    R, S = [], []
    # conclusion: base s correct, flip s' correct, pres s correct
    for kind, (ls, lsp), d in (("base", (1, 0), 2.0), ("flip", (0, 1), -1.0), ("pres", (1, 0), -0.5)):
        for role, lb, u in (("s", ls, d), ("s_prime", lsp, 0.0)):
            R.append(rec("t", kind, role, lb)); S.append(u)
    out = M.step_revisions(R, S)["conclusion"]
    assert out["n_changed"] == 1 and out["CorrectRevision"] == 100.0
    assert out["n_unchanged"] == 1 and out["UnnecessaryRevision"] == 100.0


def test_prf_and_cluster_bootstrap():
    gold = ["met", "met", "not_met", "nei", "nei", "not_met"]
    pred = ["met", "nei", "not_met", "nei", "met", "not_met"]
    out = M.prf(gold, pred, ["met", "not_met", "nei"])
    assert abs(out["acc"] - 400 / 6) < 1e-9
    assert out["per_class"]["met"]["P"] == 50.0 and out["per_class"]["not_met"]["F1"] == 100.0
    assert abs(out["macroF1"] - (50 + 100 + 50) / 3) < 1e-9
    items = [{"p": i // 2, "ok": i % 3 != 0} for i in range(12)]
    acc = lambda xs: 100.0 * sum(x["ok"] for x in xs) / len(xs)
    pt, lo, hi = M.cluster_bootstrap(items, "p", acc, B=200)
    assert lo <= pt <= hi
    st = M.seed_table({0: 90.0, 1: 92.0, 2: 94.0})
    assert st["mean"] == 92.0 and abs(st["sd"] - 2.0) < 1e-12


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)
