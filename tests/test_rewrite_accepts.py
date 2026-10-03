import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("rt", ROOT / "scripts" / "rewrite_tier.py")
RT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(RT)


def _rec(value):
    return {"state": [{"concept": "creatinine", "kind": "numeric", "subject": "patient", "status": "present",
                       "time": "current", "form": "current", "value": value}]}


def test_a_value_of_one_is_a_value():
    for v in (1.0, 1, 0.0, 2.4):                    # 1.0 == True in Python; it must still count as a value
        good = [{"concept": "creatinine", "value": v, "subject": "patient", "status": "present", "time": "current"}]
        assert RT.accepts(_rec(v), good, {"creatinine": 1}), v
        wrong = [dict(good[0], value=v + 0.5)]
        assert not RT.accepts(_rec(v), wrong, {"creatinine": 1}), v
    missing = [{"concept": "creatinine", "value": None, "subject": "patient", "status": "present", "time": "current"}]
    assert not RT.accepts(_rec(1.0), missing, {"creatinine": 1})


def test_ledger_entries_come_back_in_schema_order():
    rec = {"ledger": [{"found": "Creatinine 1.0 mg/dL", "need": "creatinine above 1.5", "status": "present",
                       "subject": "patient", "time": "current"}]}       # sorted keys, as read from disk
    led = RT.anchored_ledger(rec, "Creatinine 1.0 mg/dL today.", [], {"kind": "numeric", "concept": "creatinine"},
                             {"creatinine": 1})
    assert tuple(led[0]) == RT.LEDGER_KEYS
