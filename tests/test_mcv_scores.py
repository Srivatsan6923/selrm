import inspect
import re

import pytest

from selrm import mcv

pytestmark = pytest.mark.skipif(not (mcv.EXT / "test_data.csv").exists(), reason="MedCalc-Bench Verified not downloaded")


@pytest.fixture(scope="module")
def data():
    return mcv.rows("test") + mcv.rows("train")


def test_counts_of_the_pinned_release():
    t = mcv.rows("test")
    assert len(t) == 380 and len({r["cid"] for r in t}) == 19
    assert sum(r["Note Type"] == "Extracted" for r in t) == 230
    assert len(mcv.rows("train")) == 2426


def test_every_specified_score_reproduces_every_answer(data):
    specs = mcv.load_scores()
    for r in data:
        if r["cid"] in specs:
            assert specs[r["cid"]].total(r["ent"]) == r["answer"], r["Row Number"]


def test_items_are_well_formed(data):
    for cid, s in mcv.load_scores().items():
        keys = {k for r in data if r["cid"] == cid for k in r["ent"]}
        names = [it.name for it in s.items]
        assert len(set(names)) == len(names)
        for it in s.items:
            assert it.kind in ("numeric", "finding", "mixed") and it.time in ("current", "ever", "unstated")
            assert set(it.inputs) <= keys, (cid, it.name, set(it.inputs) - keys)
            assert set(it.thresholds) <= set(it.inputs)
            finite = all(isinstance(v, (int, float)) for v in it.levels)
            for r in data:
                if r["cid"] == cid and finite:
                    assert it.points(r["ent"]) in it.levels, (cid, it.name, r["Row Number"])
                    assert mcv.stratum(it, r["ent"]) in ("stated", "denied", "default")


def test_no_row_level_special_cases():
    from selrm.mcv import scores as pkg
    import pkgutil, importlib
    for m in pkgutil.iter_modules(pkg.__path__):
        src = inspect.getsource(importlib.import_module(f"selrm.mcv.scores.{m.name}"))
        assert not re.search(r"Row Number|Note ID|Patient Note|pmc-\d", src), m.name
