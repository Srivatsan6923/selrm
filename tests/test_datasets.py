"""rule_v1 builder (A-D4, A-D7) on a small build: rule and template splits,
corpus composition, missing sets, shortcut validation, determinism."""
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pytest

from selrm import datasets as D
from selrm import phrases as P
from selrm.library import LIBRARY_BY_ID

ROOT = Path(__file__).resolve().parents[1]


def _build(out, seed_env="0"):
    env = dict(os.environ, PYTHONHASHSEED=seed_env)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "build_rule_v1.py"), "--out", str(out),
                    "--scale", "0.02"], check=True, capture_output=True, env=env)
    return json.loads((out / "REGISTRY.json").read_text())


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    out = tmp_path_factory.mktemp("build")
    reg = _build(out)
    sets = {name.split("/")[1]: [json.loads(x) for x in open(out / v["path"], encoding="utf-8")]
            for name, v in reg.items()}
    folds = json.loads((out / "rule_v1" / "FOLDS.json").read_text())["folds"]["1"]
    return out, reg, sets, folds


def test_rules_and_templates_by_split(built):
    _, _, sets, f = built
    for name, recs in sets.items():
        rids = {r["rid"] for r in recs}
        if name == "test_L3inv":            # invented rules: test-only, outside the library
            assert {r["level"] for r in recs} == {"L3-inv"} and not rids & set(LIBRARY_BY_ID)
            continue
        key = {"test_L2": "l2_rules", "missing": "l2_rules", "test_hard": "l2_rules",
               "test_L1": "l1_rules"}.get(name, "train_rules")
        assert rids <= set(f[key]), name
        level = {"l2_rules": "L2", "l1_rules": "L1"}.get(key, "L3-alt" if name == "test_L3alt" else "L0")
        assert {r["level"] for r in recs} == {level}, name
        tpl = "train" if name.startswith(("train_", "div_", "abl_")) else "test"
        for r in recs:
            assert r["meta"]["tpl_split"] == tpl
            assert all(P.split_of(int(t.rsplit("/", 1)[1])) == tpl for t in r["meta"]["tpl"])
            assert P.split_of(r["meta"]["hdr"]) == tpl


def test_corpus_composition(built):
    _, _, sets, _ = built
    sizes = [len(sets[f"train_{k}"]) for k in D.CORPORA]
    assert min(sizes) >= 1200 and max(sizes) - min(sizes) <= 16     # one group of 4 cases x 4 claims
    for kind in D.CORPORA:
        by_group = defaultdict(set)
        for r in sets[f"train_{kind}"]:
            by_group[r["tid"]].add(r["case_kind"])
        groups = list(by_group.values())
        if kind in ("natural", "balanced"):
            assert all(len(g) == 1 for g in groups)
            n, counts = (200, {"flip": 21}) if kind == "natural" else (20, {"flip": 7})
            if len(groups) >= n:
                assert Counter(k for g in groups[:n] for k in g)["flip"] == counts["flip"]
        else:
            core = {"base", "flip"} if kind == "blocks" else {"flip"}
            assert all(core <= g for g in groups)
            block = Counter(k for g in groups[:14] for k in g)
            assert block["pres"] == block["missing"] == 6
            if kind == "triplets":
                assert block["base"] == block["near"] == 7 and all(len(g & {"base", "near"}) == 1 for g in groups)


def test_ladder_tiers_and_readapply(built):
    _, _, sets, _ = built
    assert {r["tier"] for r in sets["test_L3alt"]} == {"alt"}
    assert {r["tier"] for r in sets["test_hard"]} <= {"long", "superseded", "delabelled"}
    kinds = defaultdict(set)
    for r in sets["readapply"]:
        kinds[r["meta"].get("source_tid", r["tid"])].add((r["tid"], r["case_kind"]))
    for tid, ks in kinds.items():
        assert ks == {(tid, "base"), (tid, "flip"), (tid, "near"), (tid + ".base", "read"),
                      (tid + ".base", "apply"), (tid + ".flip", "read"), (tid + ".flip", "apply")}


def test_missing_sets(built):
    _, _, sets, _ = built
    test = {r["iid"]: r for r in sets["test_L2"]}
    for name in ("missing", "dev_missing"):
        kinds = defaultdict(set)
        for r in sets[name]:
            kinds[r["tid"]].add(r["case_kind"])
            if r["case_kind"] == "missing":
                assert r["label"] == 0
                assert all(e["status"] == "unknown" for e in r["ledger"])
            elif name == "missing":
                assert r == test[r["iid"]]          # ordinary cases are the test_L2 records
        assert all(len(k) == 2 and "missing" in k for k in kinds.values())


def test_manifests_and_shortcuts(built):
    out, reg, _, _ = built
    for name, v in reg.items():
        m = json.loads((out / v["manifest"]).read_text())
        assert m["n_records"] == v["n_records"] and m["template_split_hash"] == D.template_split_hash()
        short = name.split("/")[1]
        want = "n/a" if short.startswith(("train_", "div_", "abl_")) or "missing" in short else "PASS"
        assert m["shortcut_validation"]["result"] == want, m["shortcut_validation"]


def test_build_is_deterministic(built, tmp_path):
    _, reg, _, _ = built
    again = _build(tmp_path, seed_env="12345")
    assert {k: v["sha256"] for k, v in again.items()} == {k: v["sha256"] for k, v in reg.items()}


def test_ablation_corpora(built):
    _, _, sets, _ = built
    assert not [r for r in sets["abl_nopres_triplets"] if r["case_kind"] == "pres"]
    assert {r["claim_type"] for r in sets["abl_conclusion_triplets"]} == {"conclusion"}
    probe = [r for r in sets["abl_probe_blocks"] if r["meta"].get("probe")]
    train = [r for r in sets["abl_probe_blocks"] if not r["meta"].get("probe")]
    assert probe and {r["case_kind"] for r in probe} <= {"near", "pres"}
    assert train == sets["train_blocks"]                    # the trained part is train_blocks itself


def test_new_experiment_corpora(built):
    _, _, sets, _ = built
    for held in ("subject", "negation", "time"):        # leave one near-miss kind out
        recs = sets[f"train_triplets_lo_{held}"]
        assert recs and held not in {r["nm_kind"] for r in recs}
    for pct in (5, 12, 25):                               # dose: near-misses in pct of 100 groups
        by_group = defaultdict(set)
        for r in sets[f"train_dose_{pct:02d}"]:
            by_group[r["tid"]].add(r["case_kind"])
        block = Counter(k for g in list(by_group.values())[:100] for k in g)
        assert len(by_group) >= 100 and block["near"] == pct and block["base"] == 100 - pct
        assert block["flip"] == 100 and block["pres"] == block["missing"] == 43
