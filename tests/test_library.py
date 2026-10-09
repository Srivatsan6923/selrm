"""Rule library (A-D1..D3): programs match their stated text."""
import re

from selrm.engine import pivots
from selrm.library import LIBRARY, LIBRARY_BY_ID
from selrm.rules import OPS, RULES, Mention


def _numeric():
    return [(r, c) for r in LIBRARY for c in r.criteria if c.kind == "numeric"]


def test_library_shape_and_pilot_unchanged():
    assert len(LIBRARY_BY_ID) == len(LIBRARY) >= 41
    assert [r.rid for r in RULES] == [r.rid for r in LIBRARY[:11]]      # smoke data depends on these
    assert len(RULES) == 11
    for r in LIBRARY:
        assert r.kind in ("constraint", "score") and r.logic in ("any", "all", "atleast")
        assert (r.cutoff is not None) == (r.logic == "atleast")
        assert len({c.cid for c in r.criteria}) == len({c.concept for c in r.criteria}) == len(r.criteria)


def test_every_criterion_can_decide_its_rule():
    for r in LIBRARY:
        for c in r.criteria:
            assert pivots(r, c), (r.rid, c.cid)


def _stated_op(text, cid):
    i = text.index("{thr_%s}" % cid)
    before = text[:i].split()[-1]
    after = re.split(r"[;,]|\.\s|\.$| and | or (?!more|less)", text[i:], maxsplit=1)[0]
    if before in ("below", "above"):
        return {"below": "<", "above": ">"}[before]
    return ">=" if "or more" in after else "<=" if "or less" in after else None


def test_stated_thresholds_match_the_program():
    for r, c in _numeric():
        assert _stated_op(r.text, c.cid) == c.op, (r.rid, c.cid)
        for thr in filter(None, (c.threshold, c.alt_threshold)):
            assert (f"{thr:.{c.decimals}f}" if c.decimals else str(int(thr))) in r.rule_text({c.cid: thr})
    for r in LIBRARY:
        assert "{" not in r.rule_text() and r.rule_text().endswith(".")


def test_numeric_ranges_sit_on_their_sides():
    for r, c in _numeric():
        op, thr = OPS[c.op], c.threshold
        assert not any(op(v, thr) for v in c.default_range), (r.rid, c.cid)
        assert all(op(v, thr) for v in c.flip_range), (r.rid, c.cid)
        step = 10 ** -c.decimals
        window = [round(thr + k * step, c.decimals)
                  for k in range(-round(c.near_delta / step) + 1, round(c.near_delta / step))]
        assert any(not op(v, thr) and v != thr for v in window), (r.rid, c.cid)
        if c.alt_threshold is not None:
            alt = c.alt_threshold
            lo, hi = sorted((alt, thr))
            grid = [round(lo + k * step, c.decimals) for k in range(round((hi - lo) / step) + 1)]
            assert any(op(v, alt) and not op(v, thr) for v in grid), (r.rid, c.cid)
            assert not op(max(c.default_range, key=lambda v: abs(v - thr)), alt), (r.rid, c.cid)


def test_logic_executes_the_text():
    def m(concept, value=True, **kw):
        return Mention(concept, "finding" if value is True else "numeric", value, **kw)

    apx = LIBRARY_BY_ID["two_apixaban"]
    assert apx.logic == "atleast" and apx.cutoff == 2
    assert apx.label([m("age", 85), m("weight", 55), m("creatinine", 1.0)], "age") == 1
    assert apx.label([m("age", 85), m("weight", 70), m("creatinine", 1.0)], "age") == 0
    met = LIBRARY_BY_ID["all_metformin"]
    assert met.logic == "all"
    assert met.label([m("egfr", 40), m("age", 80)], "egfr") == 1
    assert met.label([m("egfr", 40), m("age", 70)], "egfr") == 0
    vte = LIBRARY_BY_ID["cut_vte"]                  # 3 cancer + 3 vte + 1 age + 1 heart failure >= 4
    assert vte.label([m("cancer"), m("age", 75)], "cancer") == 1
    assert vte.label([m("chf"), m("age", 75)], "age") == 0
    htn = LIBRARY_BY_ID["any_htn"]
    assert htn.label([m("pregnancy", subject="sister"), m("potassium", 4.2)], "pregnancy") == 0
    assert LIBRARY_BY_ID["crc_screen"].claims("crc") == ("Order a fecal immunochemical test.",
                                                         "Order a colonoscopy.")


def test_no_coupled_concepts_or_setting_conflicts():
    from selrm.rules_grammar import COUPLED, EXCLUDE
    for r in LIBRARY:
        cs = {c.concept for c in r.criteria}
        assert not [p for p in COUPLED if p <= cs], r.rid
        app = {(c.concept, "family" if c.counts_family else "ever" if c.counts_past else "current")
               for c in r.criteria}
        assert not (cs | app) & EXCLUDE.get(r.setting, set()), r.rid
    from selrm.rules_grammar import SAMPLED, _contra
    for r in SAMPLED:      # sampled rules never switch to a drug their condition rules out
        assert not [c.concept for c in r.criteria if _contra(c.concept, r.default, r.alternative)], r.rid


def test_claims_use_the_verb_of_the_rule_text():
    for r in LIBRARY:
        if r.kind == "constraint":
            text = r.rule_text().lower()
            assert f"{r.verb.lower()} {r.default.lower()}." in text, r.rid
            assert f"{r.verb.lower()} {r.alternative.lower()} instead" in text, r.rid


def test_every_rule_turns_exactly_at_its_stated_thresholds():
    """Boundary tests for every rule: with the other criteria held at a deciding
    setting, the conclusion changes exactly where the stated operator puts each
    threshold (one step below, at, one step above; altered thresholds too)."""
    for r, c in _numeric():
        held = pivots(r, c)[0]
        rest = [Mention(o.concept, o.kind, (o.flip_range if o in held else o.default_range)[0])
                if o.kind == "numeric" else Mention(o.concept, "finding")
                for o in r.criteria if o is not c and (o.kind == "numeric" or o in held)]
        step = 10 ** -c.decimals
        for thr, ov in ((c.threshold, {}), (c.alt_threshold, {c.cid: c.alt_threshold})):
            if thr is None:
                continue
            for v in (round(thr - step, c.decimals), thr, round(thr + step, c.decimals)):
                got = r.label(rest + [Mention(c.concept, "numeric", v)], c.cid, ov)
                assert got == int(OPS[c.op](v, thr)), (r.rid, c.cid, v)
