import datetime as dt
import importlib.util
from pathlib import Path

from selrm import xr

spec = importlib.util.spec_from_file_location("build_xr", Path(__file__).parents[1] / "scripts" / "build_xr_v1.py")
build_xr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_xr)


def test_add_months_clamps_to_month_end():
    assert xr.add_months(dt.date(2026, 3, 31), -1) == dt.date(2026, 2, 28)
    assert xr.add_months(dt.date(2026, 1, 15), -13) == dt.date(2024, 12, 15)


def test_window_counts_the_boundary_day_only_from_then_on():
    visit = xr.XMention("visit_date", "date", "2026-03-14")
    crit = xr.XCrit("stroke", "finding", times="window", window=6)

    def at(day):
        return [visit, xr.XMention("stroke", "finding", True, "patient", "present", "past", day)]
    assert crit.holds(at("2025-09-14"))          # exactly six months before: counts
    assert not crit.holds(at("2025-09-13"))      # one day earlier: does not
    assert xr.XCrit("stroke", "finding", times="ever").holds(at("2015-01-01"))
    assert not xr.XCrit("stroke", "finding", times="current").holds(at("2026-03-01"))


def test_items_pass_validation_and_defeat_rule_blind_scorers():
    items = xr.build(48, 7)
    recs = [r for it in items for r in xr.records(it, 7)]
    errs, res, ok = build_xr.validate(items, recs)
    assert not errs and ok, (errs[:5], res)
    assert res["program"]["XA"] == 100
    for name in ("ignores_rule_text_counting_rule", "ignores_rule_text_other_rule",
                 "never_counts_contested", "always_counts_contested", "always_default", "concept_named"):
        assert res[name]["XA"] == 0
