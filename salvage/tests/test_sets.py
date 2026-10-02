import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

from selrm import engine
from selrm.rules import HELDOUT_FAMILIES, RULES_BY_ID

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def _run(script, *args):
    r = subprocess.run([sys.executable, str(SCRIPTS / script), *args], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    return r.stdout


def _load(path):
    return [json.loads(s) for s in Path(path).read_text(encoding="utf-8").splitlines()]


def test_test_set_composition(tmp_path):
    out = tmp_path / "test.jsonl"
    _run("make_set.py", "--set", "test", "--n", "200", "--out", str(out))
    ts = _load(out)
    assert len(ts) == 200 and all(t["split"] == "test" for t in ts)
    held = [t for t in ts if t["family"] in HELDOUT_FAMILIES]
    assert len(held) == 50
    assert sum(t["tier"] == "easy" for t in ts) == 120
    assert {t["tier"] for t in held} <= {"easy", "long", "superseded"}
    assert {t["tier"] for t in ts if t not in held} == set(engine.TIERS)
    assert len({tuple(t["cases"][k]["text"] for k in ("base", "flip", "near")) for t in ts}) == 200
    assert [e for t in ts for e in engine.check(t)] == []


def test_dev_set_uses_seen_families_and_train_phrases(tmp_path):
    out = tmp_path / "dev.jsonl"
    _run("make_set.py", "--set", "dev", "--n", "60", "--out", str(out))
    ts = _load(out)
    assert len(ts) == 60 and all(t["split"] == "train" for t in ts)
    assert not [t for t in ts if t["family"] in HELDOUT_FAMILIES]


def test_training_corpora(tmp_path):
    _run("make_train.py", "--n", "400", "--out", str(tmp_path))
    corpora = {p.stem: _load(p) for p in tmp_path.glob("*.jsonl")}
    assert set(corpora) == {"balanced", "flips", "triplets", "no_pres", "conclusion_only"}
    for name, exs in corpora.items():
        assert len(exs) == 400 and Counter(e["label"] for e in exs) == {0: 200, 1: 200}
        assert all(".train." in e["tid"] and e["tier"] in ("easy", "long") for e in exs)
        assert not [e for e in exs if RULES_BY_ID[e["rule"]].family in HELDOUT_FAMILIES]
        assert all(e["label"] == (e["case"] == "flip") for e in exs)
        if name != "balanced":       # pairs: adjacent, one label each, same claim
            for x, y in zip(exs[::2], exs[1::2]):
                assert x["pair"] == y["pair"] and x["claim"] == y["claim"]
                assert {x["label"], y["label"]} == {0, 1} and x["tid"] == y["tid"]
    assert all(e["pair"] is None for e in corpora["balanced"])
    assert {e["case"] for e in corpora["flips"]} == {"base", "pres", "flip"}
    trip0 = [e for e in corpora["triplets"] if e["label"] == 0]
    assert sum(e["case"] == "near" for e in trip0) == 100
    assert {e["case"] for e in corpora["no_pres"]} == {"base", "near", "flip"}
    assert {e["claim"] for e in corpora["conclusion_only"]} == {"conclusion"}
    assert {e["claim"] for e in corpora["triplets"]} == {"applicability", "criterion", "conclusion"}
    near = Counter(e["nm_kind"] for e in trip0 if e["case"] == "near")
    assert set(near) == {"numeric", "subject", "negation", "time"}
    # the same pairs, cut differently: flips and triplets share their label-1 halves
    assert [e["tid"] for e in corpora["flips"]] == [e["tid"] for e in corpora["triplets"]]
    m = json.loads((tmp_path / "manifest.json").read_text())
    assert m["triplets"]["n"] == 400 and 0.05 < m["flips"]["pres_share_of_label0"] < 0.3
