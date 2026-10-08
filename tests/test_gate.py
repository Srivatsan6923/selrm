"""Gate library (crit_parse, link, gate): python tests/test_gate.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.crit_parse import find_clause, parse_criterion
from selrm.gate import gate, shift
from selrm.link import Linker, choose
import datetime

E = lambda found, subject="patient", status="present", time="current", **k: {
    "need": "x", "found": found, "subject": subject, "status": status, "time": time, **k}
by = lambda cons: {c["kind"]: c for c in cons}


def test_parse():
    r = ("For cellulitis, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: "
         "the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current "
         "heart rate is above 90/min; the current neutrophil count is 0.5 x10^9/L or less.")
    c = by(parse_criterion(r, "diabetes"))
    assert c["subject"]["allowed"] == ["patient", "first-degree"] and c["time"]["scope"] == "ever" and "value" not in c
    c = by(parse_criterion(r, "heart rate above 90"))
    assert (c["value"]["op"], c["value"]["thr"], c["time"]["scope"]) == ("gt", 90.0, "current")
    c = by(parse_criterion(r, "neutrophil count at or below 0.5"))
    assert (c["value"]["op"], c["value"]["thr"]) == ("le", 0.5)
    assert parse_criterion(r, "pregnancy") is None                      # no clause: abstain
    w = "If the patient had a major bleeding event within 6 months before the visit, prescribe X instead."
    assert by(parse_criterion(w, "bleeding"))["time"] == {"kind": "time", "scope": "window", "n": 6, "unit": "month",
                                                           "inclusive": True}
    assert find_clause("If the patient is currently taking warfarin, prescribe warfarin instead.", "warfarin") \
        == "If the patient is currently taking warfarin"


def test_gate_fields():
    case = "Potassium 5.6 in 2007. Potassium 4.0 today. Her sister has diabetes. Her friend has gout."
    num = parse_criterion("If the current serum potassium is above 5.0 mmol/L, prescribe X instead.", "potassium above 5.0")
    assert gate([E("5.6", time="past (2007)"), E("4.0")], num, case)["applies"] == 0      # past value does not count
    assert gate([E("5.6")], num, case)["applies"] == 1
    assert gate([E("5.0")], num, "Potassium 5.0")["applies"] == 0                          # boundary value
    assert gate([E("7.7")], num, case)["checks"]["quotation"] == 0                         # not in the case
    fam = parse_criterion("If the patient or a first-degree relative has had diabetes at any time, do X.", "diabetes")
    assert gate([E("Her sister has diabetes.", subject="other (sister)")], fam, case)["applies"] == 1
    own = parse_criterion("If the patient currently has gout, do X.", "gout")
    assert gate([E("Her friend has gout.", subject="other (friend)")], own, case)["applies"] == 0
    assert gate([E("not mentioned", status="absent")], own, case)["applies"] == 0
    assert gate([E("x")], None, "x")["applies"] is None                                    # parser abstained


def test_window_boundary():
    assert shift(datetime.date(2025, 3, 31), 1, "month") == datetime.date(2025, 2, 28)
    case, ref = "bleed", "2025-07-22"
    win = lambda inclusive: [{"kind": "time", "scope": "window", "n": 6, "unit": "month", "inclusive": inclusive}]
    g = lambda day, inclusive: gate([E("bleed", time=f"past ({day})")], win(inclusive), case, ref)["applies"]
    assert g("2025-01-22", True) == 1 and g("2025-01-22", False) == 0      # the boundary day, both conventions
    assert g("2025-01-23", True) == 1 and g("2025-01-23", False) == 1
    assert g("2025-01-21", True) == 0 and g("2025-01-21", False) == 0
    assert g("2025-03", True) == 1 and g("2024-11", True) == 0             # a whole month on one side
    assert g("2025-01", True) is None and g("2025", True) is None          # straddles the boundary: not computable
    assert gate([E("bleed", time="past")], win(True), case, ref)["applies"] is None
    assert gate([E("bleed", time="past (2025-03-01)")], win(True), case, None)["applies"] is None   # no reference date


def test_concept_and_link():
    cons = [{"kind": "concept", "class": "C1"}, {"kind": "status", "allowed": ["present"]}]
    onto = {"closure": {"C1": ["D1", "D2"]}}
    assert gate([E("takes apixaban", concept="D1")], cons, "takes apixaban", onto=onto)["applies"] == 1
    assert gate([E("takes apixaban", concept="D9")], cons, "takes apixaban", onto=onto)["applies"] == 0
    assert gate([E("takes apixaban")], cons, "takes apixaban", onto=onto)["applies"] is None        # reader abstained
    L = Linker([{"id": "D1", "label": "apixaban", "synonyms": ["Eliquis"]}, {"id": "D2", "label": "rivaroxaban"}])
    assert L.candidates("Eliquis")[0][::2] == ("D1", "exact") and L.candidates("APIXABAN.")[0][::2] == ("D1", "normalised")
    assert L.candidates("rivaroxiban")[0][0] == "D2"
    assert choose(L.candidates("Eliquis"), "D1") == "D1" and choose(L.candidates("Eliquis"), "D7") is None


if __name__ == "__main__":
    for name, f in list(globals().items()):
        if name.startswith("test_"):
            f()
    print("ok")
