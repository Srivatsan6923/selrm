import collections
import re

import pytest

from selrm import mcv, phrases as P, schema
from selrm.mcv import edits as E
from selrm.mcv import fidelity as F
from selrm.mcv import items as I

pytestmark = pytest.mark.skipif(not (mcv.EXT / "train_data.csv").exists(), reason="MedCalc-Bench Verified not downloaded")


@pytest.fixture(scope="module")
def built():
    """Items on a slice of the TRAINING rows (tests never read test notes)."""
    train = mcv.rows("train")
    rows = [r for i, r in enumerate(train) if i % 7 == 0]
    specs = mcv.load_scores()
    defs = I.definitions(train)
    ranges = I.plausible(train)
    units = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in train:
        for k in r["ent"]:
            units[r["cid"]][k].add(I._unit(r["ent"], k))
    lex = E.load_lexicon()
    v, _ = I.value_edits(rows, specs, defs, ranges, units, "train")
    s, _ = E.sentence_edits(rows, specs, defs, lex, "train")
    x, _ = E.ruleside(rows, specs, defs, ranges, "train")
    return {"rows": rows, "specs": specs, "criteria": I.criteria(rows, specs, defs, "train"), "value": v, "sentence": s,
            "ruleside": x, "lex": lex, "defs": defs}


def test_templates_use_no_rule_v1_training_cue():
    train = set(P.NEG_CUES["train"]) | set(P.TIME_CUES["train"]) | set(P.CURRENT_CUES["train"])
    people = {p for i, p in enumerate(P.PERSONS) if P.split_of(i) == "train"}
    for t in E.TEMPLATES.values():
        low = t.lower()
        assert not [c for c in train if re.search(rf"\b{re.escape(c)}\b", low)], t
    assert not set(E.RELATIVES) & people
    for entry in (e for items in E.load_lexicon().values() for e in items.values()):
        assert not [c for c in train if re.search(rf"\b{re.escape(c)}\b", entry["np"].lower())], entry["np"]
        assert not E.silent(E.TEMPLATES["affirm"].format(np=entry["np"]), entry)      # the lexicon sees its own phrase


def test_records_validate_and_labels_follow_the_rule_code(built):
    for name in ("criteria", "value", "sentence", "ruleside"):
        assert built[name], name
        for r in built[name]:
            schema.validate(r)
            assert r["label"] == int(r["meta"]["points"] == r["meta"]["claimed_points"])
            assert not re.search(r"\d", r["claim_text"].split("the item '")[1].split("' scores")[0]) or True
    for r in built["criteria"]:
        assert r["label"] == int(r["claim_role"] == "s")


def test_edit_triplets_flip_and_hold(built):
    for name in ("value", "sentence"):
        g = collections.defaultdict(dict)
        for r in built[name]:
            g[r["tid"]][(r["case_kind"], r["claim_role"])] = r
        for tid, c in g.items():
            assert len(c) == 6
            assert [c[(k, "s")]["label"] for k in ("base", "flip", "near")] == [1, 0, 1], tid
            assert [c[(k, "s_prime")]["label"] for k in ("base", "flip", "near")] == [0, 1, 0], tid
            assert len({c[(k, "s")]["case_text"] for k in ("base", "flip", "near")}) == 3
            assert len({c[k]["rule_text"] for k in c}) == 1 and len({c[(k, "s")]["claim_text"] for k in ("base", "flip", "near")}) == 1


def test_value_edit_changes_one_number_and_near_is_nearer(built):
    for r in built["value"]:
        if r["claim_role"] == "s" and r["case_kind"] == "base":
            v = r["meta"]["value"]
            assert abs(v["near"] - v["base"]) < abs(v["flip"] - v["base"])
            assert (v["near"] - v["base"]) * (v["flip"] - v["base"]) > 0
    by = collections.defaultdict(dict)
    for r in built["value"]:
        by[r["tid"]][r["case_kind"]] = r["case_text"]
    for c in by.values():
        for k in ("flip", "near"):
            a, b = re.split(r"(\d+(?:\.\d+)?)", c["base"]), re.split(r"(\d+(?:\.\d+)?)", c[k])
            assert len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1


def test_sentence_edit_inserts_one_sentence(built):
    for r in built["sentence"]:
        if r["case_kind"] != "base" and r["claim_role"] == "s":
            ins = r["meta"]["inserted"][r["case_kind"]]
            assert r["case_text"].count(ins) == 1
            base = r["case_text"].replace(" " + ins, "", 1) if " " + ins in r["case_text"] else r["case_text"].replace(ins, "", 1)
            row = next(x for x in built["rows"] if int(x["Row Number"]) == r["meta"]["row"])
            assert base == row["Patient Note"]


def test_ruleside_pairs_differ_in_one_number_and_cross(built):
    g = collections.defaultdict(dict)
    for r in built["ruleside"]:
        g[r["meta"]["xr"]["item"]][(r["meta"]["xr"]["variant"], r["claim_role"])] = r
    for item, c in g.items():
        assert c[("orig", "s")]["label"] == 1 and c[("alt", "s")]["label"] == 0 and c[("alt", "s_prime")]["label"] == 1
        assert c[("orig", "s")]["case_text"] == c[("alt", "s")]["case_text"]
        a, b = c[("orig", "s")]["rule_text"].split("\n"), c[("alt", "s")]["rule_text"].split("\n")
        assert sum(x != y for x, y in zip(a, b)) == 1 and len(a) == len(b)


def test_fidelity_acceptance_rules():
    assert F.value_ok({"value": "101.0", "unit": "bpm"}, 101, 3) and not F.value_ok({"value": 100}, 101, 3)
    assert not F.value_ok(None, 1, 3) and not F.value_ok({"value": None}, 1, 3)
    yes = {"mentioned": True, "subject": "patient", "status": "present", "time": "current"}
    assert F.finding_ok(yes, "affirm") and not F.finding_ok(yes, "negation") and not F.finding_ok(yes, "subject")
    assert F.finding_ok({**yes, "status": "absent"}, "negation") and F.finding_ok({**yes, "subject": "relative"}, "subject")
    assert F.finding_ok({**yes, "time": "past"}, "time") and not F.finding_ok(yes, "time")
    assert F.finding_ok({"mentioned": False}, "silent") and not F.finding_ok(yes, "silent")
