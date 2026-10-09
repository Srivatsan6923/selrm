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
    codes = {r["iid"]: f"print('{'+' if r['label'] else '-'}')\n" for r in recs}   # genprm: stand-in check code
    for fmt in FORMATS:
        for n in (len(recs), 1001):
            ex, st = build_examples(recs, fmt, n=n, codes=codes)
            if fmt == "verdict_bt":            # items are claim pairs: n sequences = n // 2 pairs
                assert st["n"] == 2 * len(ex) == 2 * (n // 2), (fmt, n, len(ex))
                continue
            if fmt == "ledger2_verify":        # the ledger2 budget plus n // 6 verification examples
                assert len(ex) == st["n"] == n + n // 6 and st["verify"] == n // 6, (fmt, n, len(ex))
                continue
            assert len(ex) == n == st["n"], (fmt, n, len(ex))
        ex, st = build_examples(recs, fmt, codes=codes)
        if fmt == "verdict_bt":
            continue
        ans = [e["completion"][-1] for e in ex if e["part"] in ("verdict", "rationale", "judge", "genprm")]
        if fmt == "ledger2_verify":
            st = dict(st, reader=st["reader"], judge=st["judge"])
        assert ans.count("+") == ans.count("-"), fmt
        if fmt in ("summary2", "summary2_case", "value2", "ledger2", "ledger2_verify", "conddrv", "ledger2_case"):
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
    # summary2_case (FINAL_TASKS_B P0.4): same reader targets as summary2, and the judge does see the case
    ex, _ = build_examples(recs, "summary2_case")
    ex2, _ = build_examples(recs, "summary2")
    judge = [e for e in ex if e["part"] == "judge"]
    assert judge and all(any(c in e["prompt"] for c in cases) for e in judge)
    assert [e["completion"] for e in ex if e["part"] == "reader"] == [e["completion"] for e in ex2 if e["part"] == "reader"]
    # ledger2_case (NEXT_TASKS_B 2): ledger2's reader targets; the judge sees rule, case, ledger and claim
    ex, _ = build_examples(recs, "ledger2_case")
    ex2, _ = build_examples(recs, "ledger2")
    judge = [e for e in ex if e["part"] == "judge"]
    assert judge and all(any(c in e["prompt"] for c in cases) and "Evidence record:" in e["prompt"] for e in judge)
    assert [e["completion"] for e in ex if e["part"] == "reader"] == [e["completion"] for e in ex2 if e["part"] == "reader"]
    # conddrv: the reader gets its record's claim and no condition (one unit per record); ledger2 targets; judge blind
    ex, st = build_examples(recs, "conddrv")
    by = {r["iid"]: r for r in recs}
    rd = [e for e in ex if e["part"] == "reader"]
    assert rd and st["reader_units"] == len(recs)
    assert all("Condition under test" not in e["prompt"] and f"Claim: {by[e['src']]['claim_text']}" in e["prompt"]
               and e["completion"] == gold_record(by[e["src"]], "ledger2") for e in rd)
    assert all(not any(c in e["prompt"] for c in cases) for e in ex if e["part"] == "judge")


def test_resampling_and_determinism():
    recs = _recs()
    a, sa = build_examples(recs, "ledger2", resample_p=0.0)
    b, sb = build_examples(recs, "ledger2", resample_p=1.0)
    c, _ = build_examples(recs, "ledger2", resample_p=1.0)
    assert sa["pairs_swapped"] == 0 and sb["pairs_swapped"] > 0 and b == c
    assert sa["unique_judge_pairs"] * 2 == sa["judge"]                   # p=0: each pair at most once per pass
    # swaps stay inside (rule, condition, claim type): same anchors, so the (rule, claim) texts
    # of the judge examples are identical at p=0 and p=1; only ledgers and labels move
    rc = lambda ex: sorted((e["prompt"].split("Evidence record:")[0], e["prompt"].split("Claim:")[1])
                           for e in ex if e["part"] == "judge")
    assert rc(a) == rc(b)
    assert sum(e["prompt"] != f["prompt"] for e, f in zip(a, b) if e["part"] == "judge") > 0


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


def test_program_on_gold_bit():
    """The program on the gold decision bit solves every triplet (bit semantics are right)."""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
    from eval_local import program_u
    from selrm.metrics import decisions, summarise
    seen, held = S.split_rules()
    for rules in (seen, held):
        recs = [r for t in S.generate(60, 5, rules, "t", "test", S.TEST_TPL) for r in t]
        u = [program_u(r, gold_record(r, "ledger2_dec"), True) for r in recs]
        for ct in ("conclusion", "criterion"):
            assert summarise(decisions(recs, u, ct))["all"]["TA"] == 100.0, ct


def test_claims_and_stats():
    d = tempfile.mkdtemp() + "/R1"
    assert runq.claim(d, "pod-a", settle_s=0) and not runq.claim(d, "pod-b", settle_s=0)
    old = time.time() - runq.STALE_OWN_S - 5
    os.utime(f"{d}/HEARTBEAT", (old, old))
    assert runq.state(d) == "claimed"               # fresh claim file + old heartbeat: still live (race fix)
    os.utime(f"{d}/CLAIMED_B", (old, old))
    assert runq.state(d) == "free" and runq.claim(d, "pod-b", settle_s=0)   # dead pod: claim and heartbeat old
    assert runq.count(d, "KILLED_") == 1           # the takeover is recorded against the run
    open(f"{d}/CLAIMED_C", "w").close()
    os.remove(f"{d}/CLAIMED_B")
    for f in ("HEARTBEAT", "CLAIMED_C"):
        os.utime(f"{d}/{f}", (old, old))
    assert runq.state(d) == "claimed"                                     # other role: 3 h rule
    os.remove(f"{d}/CLAIMED_C")
    runq.claim(d, "pod-c", settle_s=0); runq.release(d, False, "x")
    runq.claim(d, "pod-c", settle_s=0); runq.release(d, False, "y")
    assert runq.state(d) == "failed"
    st = runq.util_stats([90.0] * 10 + [10.0] * 10 + [50.0] * 3)
    assert st["gpu_windows_below40"] == 0.5 and st["gpu_util_p10"] == 10.0, st


def test_low_util_stop():
    """A run below 40% for the 10-minute window (after warm-up) is stopped and marked for that GPU model."""
    import tempfile
    from selrm import runq
    saved = runq.gpu_sample, runq.gpu_name, runq.os._exit
    d, exits = tempfile.mkdtemp(), []
    try:
        runq.gpu_name, runq.os._exit = (lambda: ("TESTGPU", 80.0)), exits.append
        open(f"{d}/CLAIMED_B", "w").write("x")
        runq.gpu_sample = lambda: (30.0, 1000.0)
        m = runq.GpuMonitor(f"{d}/job.csv", log=lambda *_: None)
        m.start_run(d)
        for _ in range(29):
            m.tick()
        assert not exits
        m.tick()
        assert exits == [6] and runq.low_util_on(d, "TESTGPU") and not runq.low_util_on(d, "OTHER")
        assert not os.path.exists(f"{d}/CLAIMED_B")
        exits.clear()
        runq.gpu_sample = lambda: (45.0, 1000.0)
        m = runq.GpuMonitor(f"{d}/job2.csv", log=lambda *_: None)
        m.start_run(d)
        for _ in range(60):
            m.tick()
        assert not exits
    finally:
        runq.gpu_sample, runq.gpu_name, runq.os._exit = saved


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok", name)
