import pytest

from selrm import metrics


def _r(rule, base, flip, near, pres=1, tid=None, claim="conclusion", **kw):
    return {"tid": tid or f"{rule}-{base}{flip}{near}{pres}", "rule": rule, "claim": claim,
            "kind": "finding", "nm_kind": "subject", "tier": "easy", "heldout": False,
            "d": {"base": base, "flip": flip, "near": near, "pres": pres}, **kw}


def test_rates_on_a_hand_example():
    rows = [_r("a", 1, -1, 1), _r("a", 1, -1, -1), _r("b", 1, 1, 1, pres=-1), _r("b", -1, -1, 1)]
    s = metrics.summarize(rows, boot=200)
    assert s["n"] == 4
    got = [s[k][0] for k in ("rev", "hold", "ta", "pres_hold", "ties", "base_acc")]
    assert got == [50, 75, 25, 75, 0, 75]
    # decision changes on label-preserving edits: row 2 near, row 3 pres, row 4 near and pres
    assert s["unnecessary_revision"][0] == pytest.approx(100 * (0.5 + 0.5 + 1) / 4)


def test_a_tie_fails_whichever_sign_is_required():
    rows = [_r("a", 0, -1, 1), _r("a", 1, 0, 1), _r("a", 1, -1, 0)]
    s = metrics.summarize(rows, boot=10)
    assert s["rev"][0] == pytest.approx(100 / 3)
    assert s["hold"][0] == pytest.approx(200 / 3)
    assert s["ta"][0] == 0
    assert s["ties"][0] == 25          # 3 of 12 cases


def test_real_valued_margins():
    s = metrics.summarize([_r("a", 0.3, -2.5, 1e-9), _r("a", 0.3, 0.1, -0.2)], boot=10)
    assert (s["rev"][0], s["hold"][0], s["ta"][0]) == (50, 50, 50)


def test_bootstrap_resamples_rules():
    rows = [_r(rid, 1, -1, 1) for rid in "ab"] + [_r(rid, 1, 1, 1) for rid in "cde"]
    s = metrics.summarize(rows, boot=500, seed=3)
    pt, lo, hi = s["ta"]
    assert pt == 40 and lo < pt < hi and 0 <= lo and hi <= 100
    assert s == metrics.summarize(rows, boot=500, seed=3)
    assert s["hold"] == (100, 100, 100)          # every rule agrees: no spread


def test_rows_of_one_rule_move_together():
    # one rule with many triplets dominates; resampling rules (not triplets) shows it
    rows = [_r("big", 1, -1, 1, tid=f"big{i}") for i in range(50)] + \
        [_r(rid, 1, 1, 1) for rid in "xyz"]
    pt, lo, hi = metrics.summarize(rows, boot=500)["ta"]
    assert lo == 0 and hi > 95 and pt == pytest.approx(5000 / 53)


def test_paired_difference_resamples_rules_jointly():
    a = [_r(rid, 1, -1, 1, tid=f"{rid}{i}") for rid in "abcd" for i in range(3)]
    b = [_r(rid, 1, -1, -1 if rid in "ab" else 1, tid=f"{rid}{i}") for rid in "abcd" for i in range(3)]
    diff, lo, hi = metrics.paired(a, b, "ta", boot=500)
    assert diff == 50 and 0 <= lo <= diff <= hi <= 100
    assert metrics.paired(a, a, "ta", boot=50) == (0, 0, 0)
    with pytest.raises(ValueError):
        metrics.paired(a, b[:-1])


def test_breakdown_and_row():
    rows = [_r("a", 1, -1, 1, nm_kind="time"), _r("a", 1, -1, -1, nm_kind="subject")]
    b = metrics.breakdown(rows, "nm_kind", boot=10)
    assert list(b) == ["subject", "time"] and b["time"]["ta"][0] == 100 and b["subject"]["ta"][0] == 0
    t = {"tid": "x", "rule": "two_apixaban", "criterion": "cr", "nm_kind": "time",
         "tier": "superseded"}
    assert metrics.row(t, {"base": 1}, "criterion") == {
        "tid": "x", "rule": "two_apixaban", "family": "two_of_three", "heldout": True,
        "kind": "numeric", "nm_kind": "time", "tier": "superseded", "claim": "criterion",
        "d": {"base": 1}}
    assert metrics.summarize([]) == {"n": 0}
