import datetime as dt

from selrm import ec, xr

BASE = dict(nct_id="NCT00000000", criterion_type="exclusion", simplifications=[], other_disjuncts=[], sex="any",
            threshold=0, op="none", subjects="patient", times="none", window_n=0, window_unit="none")


def test_window_boundary_day_counts_for_every_unit():
    visit = dt.date(2025, 3, 31)
    for n, unit, start in ((14, "days", dt.date(2025, 3, 17)), (2, "weeks", dt.date(2025, 3, 17)),
                           (1, "months", dt.date(2025, 2, 28)), (1, "years", dt.date(2024, 3, 31))):
        assert ec.window_start(visit, n, unit) == start
        f = dict(BASE, concept="stroke", times="window", window_n=n, window_unit=unit)

        def state(d):
            return [xr.XMention("visit_date", "date", visit.isoformat()),
                    xr.XMention("stroke", "finding", True, "patient", "present", "past", d.isoformat())]
        assert ec.event_holds(f, state(start))
        assert not ec.event_holds(f, state(start - dt.timedelta(days=1)))


def test_groups_follow_the_program_and_claims_interface():
    F = [dict(BASE, cand="t1", rule_text="Platelet count <50,000/uL", concept="platelets", input="numeric", op="<",
              threshold=50, near_kinds=["numeric", "boundary", "time"]),
         dict(BASE, cand="t2", rule_text="History of heparin-induced thrombocytopenia", concept="hit",
              input="finding", times="ever", near_kinds=["subject", "negation"]),
         dict(BASE, cand="t3", rule_text="Stroke within 3 months (the day exactly 3 months before the visit counts)",
              concept="stroke", input="finding", times="window", window_n=3, window_unit="months",
              near_kinds=["time", "subject", "negation"])]
    for f in F:
        recs = ec.groups(f)
        assert recs and not ec.rendered_ok(recs)
        want = {"base": 0, "flip": 1, "near": 0, "pres": 0}
        for r in recs:
            assert r["rule_text"] == "Exclusion criterion: " + f["rule_text"] and r["claim_type"] == "conclusion"
            assert r["claim_text"] == ec.CLAIMS[r["claim_role"] == "s_prime"]
            assert r["label"] == int((r["claim_role"] == "s_prime") == (want[r["case_kind"]] == 1))
