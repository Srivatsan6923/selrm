"""Role B checks that run on CPU: example builders, ledger check, claims, GPU stats.
Run: python tests/test_role_b.py  (or python -m pytest -q tests)"""
import os, sys, tempfile, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import smoke as S
from selrm import runq
from selrm.formats import FORMATS, build_examples, gold_record, reader_units, well_formed


def _recs():
    seen, _ = S.split_rules()
    return S.corpus(S.generate(150, 1, seen, "t", "train", S.TRAIN_TPL), "triplets")


def test_budget_and_balance():
    recs = _recs()
    for fmt in FORMATS:
        for n in (len(recs), 1001):
            ex, st = build_examples(recs, fmt, n=n)
            assert len(ex) == n == st["n"], (fmt, n, len(ex))
        ex, st = build_examples(recs, fmt)
        ans = [e["completion"][-1] for e in ex if e["part"] in ("verdict", "rationale", "judge")]
        assert ans.count("+") == ans.count("-"), fmt
        if fmt in ("summary2", "value2", "ledger2"):
            assert st["reader"] + st["judge"] == len(recs) and abs(st["reader"] - st["judge"]) <= 1


def test_two_stage_isolation_and_targets():
    recs = _recs()
    cases = {r["case_text"] for r in recs}
    for fmt in ("summary2", "value2", "ledger2"):
        ex, _ = build_examples(recs, fmt)
        for e in ex:
            if e["part"] == "judge":
                assert not any(c in e["prompt"] for c in cases)       # judge never sees the case
                assert e["completion"] in "+-"
        value = [e["completion"] for e in ex if e["part"] == "reader"] if fmt == "value2" else []
        assert all("subject:" not in v and "found:" in v for v in value)


def test_resampling_and_determinism():
    recs = _recs()
    a, sa = build_examples(recs, "ledger2", resample_p=0.0)
    b, sb = build_examples(recs, "ledger2", resample_p=1.0)
    c, _ = build_examples(recs, "ledger2", resample_p=1.0)
    assert sa["pairs_swapped"] == 0 and sb["pairs_swapped"] > 0 and b == c


def test_well_formed():
    recs = reader_units(_recs())
    for r in recs:
        for fmt in ("ledger2", "value2"):
            assert well_formed(gold_record(r, fmt), r["case_text"], fmt), (fmt, r["iid"])
    r = recs[0]
    good = gold_record(r, "ledger2")
    assert not well_formed("", r["case_text"], "ledger2")
    assert not well_formed(good.replace("subject:", "subj:"), r["case_text"], "ledger2")
    assert not well_formed(good.replace("found: ", "found: zzz ", 1), r["case_text"], "ledger2")
    assert not well_formed(good, r["case_text"], "value2")                 # extra fields
    assert well_formed("need: x\nfound: not mentioned", "", "value2")


def test_claims_and_stats():
    d = tempfile.mkdtemp() + "/R1"
    assert runq.claim(d, "pod-a") and not runq.claim(d, "pod-b")
    old = time.time() - runq.STALE_OWN_S - 5
    os.utime(f"{d}/HEARTBEAT", (old, old))
    assert runq.state(d) == "free" and runq.claim(d, "pod-b")            # stale own claim
    open(f"{d}/CLAIMED_C", "w").close()
    os.remove(f"{d}/CLAIMED_B")
    os.utime(f"{d}/HEARTBEAT", (old, old))
    assert runq.state(d) == "claimed"                                     # other role: 3 h rule
    os.remove(f"{d}/CLAIMED_C")
    runq.claim(d, "pod-c"); runq.release(d, False, "x")
    runq.claim(d, "pod-c"); runq.release(d, False, "y")
    assert runq.state(d) == "failed"
    st = runq.util_stats([90.0] * 10 + [10.0] * 10 + [50.0] * 3)
    assert st["gpu_windows_below40"] == 0.5 and st["gpu_util_p10"] == 10.0, st


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok", name)
