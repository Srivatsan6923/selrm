import pytest

from selrm import engine, shortcuts
from selrm.rules import RULES_BY_ID


@pytest.fixture(scope="module")
def ts():
    return [engine.make_triplet(rid, cid, nm, tier, split, 0)
            for split in ("train", "test") for rid, cid, nm, tier in engine.cells()]


def _kind(t):
    return RULES_BY_ID[t["rule"]].crit(t["criterion"]).kind


def test_always_default(ts):
    assert all(shortcuts.score(t, shortcuts.always_default) == dict.fromkeys(engine.WANT, 1)
               for t in ts)


def test_concept_named_reverses_on_finding_flips_and_fails_their_near_misses(ts):
    for t in ts:
        d = shortcuts.score(t, shortcuts.concept_named)
        if _kind(t) == "finding":
            assert d == {"base": 1, "flip": -1, "near": -1, "pres": 1}
        else:
            assert d == dict.fromkeys(engine.WANT, -1)


def test_oracle_solves_every_claim_of_every_triplet(ts):
    for t in ts:
        for claim in t["claims"]:
            assert shortcuts.score(t, shortcuts.oracle, claim) == {"base": 1, "flip": -1,
                                                                   "near": 1, "pres": 1}


def test_naive_parser_holds_numeric_near_misses_and_fails_time_ones(ts):
    for t in ts:
        d = shortcuts.score(t, shortcuts.naive_number_parser)
        if _kind(t) == "finding":
            assert d == dict.fromkeys(engine.WANT, 1)
        else:
            assert (d["base"], d["flip"], d["pres"]) == (1, -1, 1), t["tid"]
            assert d["near"] == (1 if t["nm_kind"] == "numeric" else -1), t["tid"]


def _case(rid, cid, text, overrides=None):
    t = {"rule": rid, "criterion": cid, "overrides": overrides or {}}
    return shortcuts.naive_number_parser(t, {"text": text})


def test_naive_parser_reads_the_value_after_the_keyword():
    assert _case("t2d_metformin", "egfr", "In 2019, eGFR fell to 22 mL/min/1.73 m2.") == -1
    assert _case("t2d_metformin", "egfr", "eGFR (2019): 61 mL/min/1.73 m2.") == 1
    assert _case("t2d_metformin", "egfr", "eGFR 40 mL/min/1.73 m2.") == 1
    assert _case("t2d_metformin", "egfr", "eGFR 40 mL/min/1.73 m2.", {"egfr": 45}) == -1
    assert _case("curb65", "sbp", "Blood pressure 84/50 mmHg on arrival.") == -1
    assert _case("curb65", "age", "Aged 64.\nNon-smoker.") == 1
    assert _case("curb65", "bun", "Non-smoker.") == 1                  # nothing to parse
    assert _case("hf_spironolactone", "k", "Potassium today: 5.1 mmol/L.") == -1
