import json
from pathlib import Path

import pytest

from selrm import struct_view as V

ROOT = Path(__file__).resolve().parents[1]


def test_constraint_forms():
    w = V.constraints({"kind": "window", "event": "admission", "n": 6, "unit": "months", "subject": "patient", "status": "present"})
    assert {"kind": "time", "scope": "window", "n": 6, "unit": "month", "inclusive": True} in w
    c = V.constraints({"kind": "class", "class_id": "HP:1", "domain": "phenotype", "subject": "patient", "status": "present", "time": "current"})
    assert {"kind": "concept", "class": "HP:1"} in c and {"kind": "subject", "allowed": ["patient"]} in c
    n = V.constraints({"kind": "numeric", "concept": "egfr", "op": "<", "threshold": 45, "subject": "patient", "time": "current"})
    assert {"kind": "value", "op": "lt", "thr": 45, "unit": ""} in n
    f = V.constraints({"kind": "finding", "concept": "cad", "op": None, "threshold": None, "subject": "patient or first-degree relative", "time": "ever"})
    assert {"kind": "subject", "allowed": ["patient", "first-degree"]} in f and any(x.get("scope") == "ever" for x in f)
    assert V.constraints({"kind": "finding", "levels": [0, 1], "inputs": []}) is None


@pytest.mark.skipif(not (ROOT / "data/onto_v1/classes.json").exists(), reason="onto_v1 tables missing")
def test_closure_and_terms_agree_with_the_tables():
    cl, terms, info = V.closure(), V.terms(), V.info()
    assert set(cl) == set(info) and all(m in terms for ms in cl.values() for m in ms)
    seen = [m for ms in cl.values() for m in ms]
    assert len(seen) == len(set(seen))                      # no member in two classes
    assert {v["split"] for v in info.values()} == {"train", "dev", "test"}


@pytest.mark.skipif(not (ROOT / "data/cls_v1/test/records.jsonl").exists(), reason="cls_v1 records not restored")
def test_every_frozen_struct_converts():
    for name in ("cls_v1/test", "rule_v2/dev", "reg_v1/dev"):
        p = ROOT / "data" / name / "records.jsonl"
        if p.exists():
            for ln in open(p, encoding="utf-8"):
                assert V.constraints(json.loads(ln)["struct"]) is not None
