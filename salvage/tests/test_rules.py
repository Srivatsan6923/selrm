import re

from selrm.engine import pivots
from selrm.rules import HELDOUT_FAMILIES, OPS, RULES, RULES_BY_ID, Mention


def _numeric():
    return [(r, c) for r in RULES for c in r.criteria if c.kind == "numeric"]


def test_library_shape():
    assert len(RULES) >= 40 and len({r.rid for r in RULES}) == len(RULES)
    families = {r.family for r in RULES}
    assert HELDOUT_FAMILIES <= families and len(families - HELDOUT_FAMILIES) >= 5
    held = [r for r in RULES if r.family in HELDOUT_FAMILIES]
    assert all(sum(r.family == f for r in held) >= 3 for f in HELDOUT_FAMILIES)
    assert all(r.kind == "constraint" for r in held)
    assert sum(r.kind == "score" for r in RULES) >= 10


def test_every_criterion_can_decide_its_rule():
    for r in RULES:
        assert len({c.cid for c in r.criteria}) == len(r.criteria)
        assert len({c.concept for c in r.criteria}) == len(r.criteria)
        for c in r.criteria:
            assert pivots(r, c), (r.rid, c.cid)


def _stated_op(text, cid):
    i = text.index("{thr_%s}" % cid)
    before = text[:i].split()[-1]
    after = re.split(r"[;,]|\.\s|\.$", text[i:], maxsplit=1)[0]
    if before in ("below", "above"):
        return {"below": "<", "above": ">"}[before]
    return ">=" if "or more" in after else "<=" if "or less" in after else None


def test_stated_thresholds_match_the_program():
    for r, c in _numeric():
        assert _stated_op(r.text, c.cid) == c.op, (r.rid, c.cid)
        for thr in filter(None, (c.threshold, c.alt_threshold)):
            assert (f"{thr:.{c.decimals}f}" if c.decimals else str(int(thr))) in \
                r.rule_text({c.cid: thr})
    for r in RULES:
        assert "{" not in r.rule_text() and r.rule_text().endswith(".")


def test_numeric_ranges_sit_on_their_sides():
    for r, c in _numeric():
        op, thr = OPS[c.op], c.threshold
        assert not any(op(v, thr) for v in c.default_range), (r.rid, c.cid)
        assert all(op(v, thr) for v in c.flip_range), (r.rid, c.cid)
        step = 10 ** -c.decimals
        window = [round(thr + k * step, c.decimals)
                  for k in range(-round(c.near_delta / step), round(c.near_delta / step) + 1)]
        assert any(not op(v, thr) for v in window), (r.rid, c.cid)
        if c.alt_threshold is not None:
            alt = c.alt_threshold
            lo, hi = sorted((alt, thr))
            grid = [round(lo + k * step, c.decimals) for k in range(round((hi - lo) / step) + 1)]
            assert any(op(v, alt) and not op(v, thr) for v in grid), (r.rid, c.cid)
            far = max(c.default_range, key=lambda v: abs(v - thr))
            assert not op(far, alt), (r.rid, c.cid)       # a base value under the altered rule


def test_cutoff_rules_execute_their_text():
    def m(concept, value=True, **kw):
        return Mention(concept, "finding" if value is True else "numeric", value, **kw)

    apx = RULES_BY_ID["two_apixaban"]
    assert apx.label([m("age", 85), m("weight", 55), m("creatinine", 1.0)], "age") == 1
    assert apx.label([m("age", 85), m("weight", 70), m("creatinine", 1.0)], "age") == 0
    assert apx.label([m("age", 70), m("weight", 55), m("creatinine", 1.6)], "age") == 1
    vte = RULES_BY_ID["cut_vte"]           # 3 cancer + 3 vte + 1 age + 1 heart failure >= 4
    assert vte.label([m("cancer"), m("age", 75)], "cancer") == 1
    assert vte.label([m("cancer"), m("age", 50)], "cancer") == 0
    assert vte.label([m("chf"), m("age", 75)], "age") == 0
    assert vte.label([m("vte", time="past"), m("chf"), m("age", 50)], "vte") == 1
    htn = RULES_BY_ID["any_htn"]
    assert htn.label([m("pregnancy", subject="sister"), m("potassium", 4.2)], "pregnancy") == 0
    assert htn.label([m("pregnancy"), m("potassium", 4.2)], "pregnancy") == 1
    assert RULES_BY_ID["crc_screen"].claims("crc") == ("Order a fecal immunochemical test.",
                                                        "Order a colonoscopy.")
