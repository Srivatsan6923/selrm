import importlib.util
import json
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
spec = importlib.util.spec_from_file_location("aux", ROOT / "scripts" / "build_aux_corpora.py")
aux = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aux)
REG = json.loads((ROOT / "data" / "REGISTRY.json").read_text(encoding="utf-8"))
PARENTS_PRESENT = all((ROOT / "data" / REG[p]["path"]).exists() for p in aux.PARENTS.values())


@pytest.mark.skipif(not PARENTS_PRESENT, reason="parent corpora not built in this clone")
def test_subsamples_are_whole_groups_of_the_same_blocks():
    out, shared, n_blocks = aux.build(REG)
    again, _, _ = aux.build(REG)
    assert n_blocks == 401
    for k, (picked, lines) in out.items():
        assert lines == again[k][1]                                   # deterministic
        recs = [json.loads(x) for x in lines]
        sizes = Counter(r["tid"] for r in recs)
        assert aux.N <= len(recs) < aux.N + max(sizes.values())        # stops at the first group boundary
        assert len(sizes) == len(picked)                                # whole groups only
        no_missing = Counter(r["label"] for r in recs if r["case_kind"] != "missing")
        assert no_missing[0] == no_missing[1]                           # one correct claim per pair
    smaller = min(len(p) for p, _ in out.values())
    assert len(shared) >= smaller - aux.BLOCK                           # same groups up to the shorter set
    tri = Counter(json.loads(x)["case_kind"] for x in out["aux_triplets_20k"][1])
    assert abs(tri["base"] - tri["near"]) <= 2 * aux.BLOCK * 4         # half base, half near-miss per block
