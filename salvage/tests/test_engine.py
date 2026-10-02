import copy
import json
import re
from collections import Counter
from dataclasses import replace

import pytest

from selrm import engine
from selrm import phrases as P
from selrm.rules import FIRST_DEGREE, OPS, RULES, RULES_BY_ID

SEEDS = range(3)
FIELDS = {"tid", "rule", "family", "criterion", "nm_kind", "tier", "split", "rule_text",
          "claims", "overrides", "cases"}


@pytest.fixture(scope="module")
def generated():
    stats = Counter()
    ts = [engine.make_triplet(rid, cid, nm, tier, split, s, stats)
          for split in ("train", "test") for rid, cid, nm, tier in engine.cells() for s in SEEDS]
    return ts, stats


@pytest.fixture(scope="module")
def ts(generated):
    return generated[0]


def _rule(t):
    return RULES_BY_ID[t["rule"]]


def _crit(t):
    return _rule(t).crit(t["criterion"])


def _age(t):
    """The patient's age: the age criterion's value, else the header's."""
    case = t["cases"]["base"]
    ages = [m["value"] for m in case["state"] if m["concept"] == "age"]
    head = case["text"].split("\n")[0]
    return ages[0] if ages else int(re.search(r"\d+", head)[0])


def _target(t, k):
    c = _crit(t)
    return [m for m in engine.state_from_json(t["cases"][k]["state"]) if m.concept == c.concept]


def test_every_cell_generates_and_passes_check(generated):
    ts, stats = generated
    assert len(ts) == 2 * len(engine.cells()) * len(SEEDS)
    assert len({t["tid"] for t in ts}) == len(ts)
    assert [e for t in ts for e in engine.check(t)] == []
    assert stats["rejected"] / stats["proposed"] < 0.05


def test_cells_cover_every_criterion_and_tier():
    cs = engine.cells()
    assert {(r, c) for r, c, _, _ in cs} == {(r.rid, c.cid) for r in RULES for c in r.criteria}
    assert {t for *_, t in cs} == set(engine.TIERS)
    assert all(nm == "time" for _, _, nm, t in cs if t in ("superseded", "delabelled"))
    assert all(RULES_BY_ID[r].crit(c).kind == "numeric" for r, c, _, t in cs if t == "superseded")
    assert {r for r, _, _, t in cs if t == "delabelled"} == {"strep_amox", "uti_sulfa"}
    assert all(RULES_BY_ID[r].crit(c).alt_threshold is not None for r, c, _, t in cs if t == "alt")
    assert ("migraine_cad", "cad", "time", "easy") not in cs      # past counts for cad


def test_output_fields_claims_and_labels(ts):
    for t in ts:
        rule = _rule(t)
        assert set(t) == FIELDS and t["family"] == rule.family
        kinds = ["applicability", "criterion", "conclusion"] if rule.kind == "constraint" \
            else ["applicability", "conclusion"]
        assert list(t["claims"]) == kinds
        assert t["claims"]["conclusion"] == list(rule.claims(t["criterion"]))
        for k, case in t["cases"].items():
            assert set(case) == {"text", "labels", "state", "ledger"}
            assert case["labels"] == dict.fromkeys(kinds, engine.WANT[k])


def test_claim_wording():
    t = engine.make_triplet("t2d_metformin", "egfr", "numeric", "alt", "test", 0)
    assert t["claims"]["applicability"][1] == ("An eGFR value below 45 mL/min/1.73 m2 reported in "
                                               "the case counts for this patient under the rule.")
    assert t["claims"]["criterion"] == ["The eGFR criterion is not met.", "The eGFR criterion is met."]
    t = engine.make_triplet("strep_amox", "pen_allergy", "subject", "easy", "test", 0)
    assert t["claims"]["applicability"][0] == ("A penicillin allergy reported in the case does not "
                                               "count for this patient under the rule.")


def test_deterministic_and_json_roundtrip():
    a = engine.make_triplet("curb65", "bun", "time", "superseded", "test", 7)
    assert a == engine.make_triplet("curb65", "bun", "time", "superseded", "test", 7)
    assert json.loads(json.dumps(a)) == a
    assert a != engine.make_triplet("curb65", "bun", "time", "superseded", "test", 8)


def test_invalid_cell_is_refused():
    with pytest.raises(ValueError):
        engine.make_triplet("strep_amox", "pen_allergy", "numeric", "easy", "train", 0)
    with pytest.raises(ValueError):
        engine.make_triplet("migraine_cad", "cad", "time", "easy", "train", 0)
    with pytest.raises(ValueError):
        engine.make_triplet("curb65", "rr", "numeric", "alt", "train", 0)


def test_check_catches_corruption():
    t = engine.make_triplet("strep_amox", "pen_allergy", "negation", "easy", "train", 0)

    def errs(edit):
        u = copy.deepcopy(t)
        edit(u)
        return " ".join(engine.check(u))

    assert engine.check(t) == []
    assert "label: near" in errs(lambda u: u["cases"]["near"]["labels"].update(criterion=1))
    assert "keyword: base" in errs(
        lambda u: u["cases"]["base"].update(text=u["cases"]["base"]["text"] + "\nAllergic to penicillin."))
    assert "flip: changes []" in errs(
        lambda u: u["cases"]["flip"].update(state=u["cases"]["base"]["state"]))
    assert "pres: same text" in errs(
        lambda u: u["cases"]["pres"].update(text=u["cases"]["base"]["text"]))
    assert "edit: near" in errs(
        lambda u: u["cases"]["near"].update(text=u["cases"]["near"]["text"] + "\nNon-smoker.\nSwims."))
    assert "ledger: flip" in errs(lambda u: u["cases"]["flip"]["ledger"][0].update(found="Allergic."))
    assert "claims" in errs(lambda u: u["claims"].pop("criterion"))
    n = engine.make_triplet("t2d_metformin", "egfr", "numeric", "easy", "train", 0)
    two = copy.deepcopy(n)
    two["cases"]["near"]["state"] += two["cases"]["base"]["state"]     # two current eGFR values
    assert "state: near" in " ".join(engine.check(two))


def test_cutoff_rules_hold_the_other_criteria_where_the_target_decides(ts):
    for t in ts:
        rule = _rule(t)
        if rule.cutoff is None:
            continue
        crit, ov = _crit(t), t["overrides"]
        state = engine.state_from_json(t["cases"]["base"]["state"])
        met = sum(c.points for c in rule.criteria if c is not crit and c.evaluate(state))
        assert met < rule.cutoff <= met + crit.points, t["tid"]
        if t["family"] == "all_of":
            assert all(c.evaluate(state) for c in rule.criteria if c is not crit)
        assert rule.label(state, crit.cid, ov) == 0


def test_near_misses_differ_from_a_counted_mention_in_one_attribute(ts):
    for t in ts:
        c, kind = _crit(t), t["nm_kind"]
        base, flip, near = (_target(t, k) for k in ("base", "flip", "near"))
        assert len(flip) == 1 and c.applies(flip[0]) and flip[0].status == "present"
        if c.kind == "numeric":
            thr = t["overrides"].get(c.cid, c.threshold)
            op = OPS[c.op]
            (b,) = base
            assert not op(b.value, thr) and op(flip[0].value, thr)
            if kind == "numeric":
                (m,) = near
                assert not op(m.value, thr) and abs(m.value - thr) <= c.near_delta + 1e-9
                assert abs(m.value - thr) < abs(b.value - thr)
            else:
                (m,) = [x for x in near if x != b]
                assert m.time == "past" and op(m.value, thr) and not c.applies(m)
                assert m.form == ("superseded" if t["tier"] == "superseded" else "past")
            continue
        assert all(m.form == "generic" and m.status == "absent" for m in base)
        if kind == "negation":
            (m,) = near
            assert m.status == "absent" and m.form == "absent"
            continue
        (m,) = [x for x in near if x not in base]
        assert not c.applies(m)
        if kind == "subject":
            assert m.subject in P.persons(c.concept, t["split"], _age(t))
            assert c.applies(replace(m, subject="patient"))       # only the subject excludes it
            assert not (c.counts_family and m.subject in FIRST_DEGREE)
        else:
            assert m.subject == "patient" and m.time == "past" and not c.counts_past
            assert c.applies(replace(m, time="current"))          # only the time excludes it
            assert m.form == ("delabelled" if t["tier"] == "delabelled" else "past")


def test_flips_cover_patient_past_and_family_ways():
    ways = Counter()
    for split in ("train", "test"):
        for s in range(40):
            t = engine.make_triplet("contra_vte", "vte", "negation", "easy", split, s)
            (m,) = _target(t, "flip")
            ways["family" if m.subject in FIRST_DEGREE else m.time] += 1
            assert m.subject in ("patient", *P.persons("vte", split, _age(t)))
    assert set(ways) == {"current", "past", "family"}


def test_base_findings_appear_both_with_and_without_a_line(ts):
    seen = Counter(bool(_target(t, "base")) for t in ts if _crit(t).kind == "finding")
    assert seen[True] and seen[False]


def test_ledgers_describe_the_target_and_prose_matches_their_length(ts):
    ratios = []
    for t in ts:
        c = _crit(t)
        for k, case in t["cases"].items():
            mentions = _target(t, k)
            assert [(e["subject"], e["status"], e["time"]) for e in case["ledger"]] == \
                ([(m.subject, m.status, m.time) for m in mentions] or [("patient", "absent", "current")])
            assert all(e["need"] == c.label for e in case["ledger"])
            text, prose = engine.ledger_text(case["ledger"]), engine.prose(case["ledger"])
            words = prose
            for e in case["ledger"]:            # the fields themselves may say "count"
                words = words.replace(e["found"], "").replace(e["need"], "")
            assert not re.search(r"\b(counts?|met|prescribe|criterion|points?)\b", words.lower())
            ratios.append(len(prose) / len(text))
    assert 0.8 < sum(ratios) / len(ratios) < 1.25 and min(ratios) > 0.6 and max(ratios) < 1.6


def test_alt_flip_disagrees_with_the_original_threshold(ts):
    alt = [t for t in ts if t["tier"] == "alt"]
    assert alt
    for t in alt:
        rule, c = _rule(t), _crit(t)
        assert t["overrides"] == {c.cid: c.alt_threshold}
        assert engine.fmt(c.alt_threshold, c) in t["rule_text"]
        state = engine.state_from_json(t["cases"]["flip"]["state"])
        assert rule.label(state, c.cid, t["overrides"]) == 1 and rule.label(state, c.cid) == 0


def test_tier_sizes(ts):
    for t in ts:
        n_fill = sum(s in engine.FILLER_SET for s in t["cases"]["base"]["text"].split("\n"))
        assert n_fill >= 15 if t["tier"] == "long" else 1 <= n_fill <= 4


def test_age_criterion_moves_age_out_of_the_header(ts):
    for t in ts:
        head = t["cases"]["base"]["text"].split("\n")[0]
        has_age = any(c.concept == "age" for c in _rule(t).criteria)
        assert bool(re.search(r"\d", head)) != has_age, head


def _patterns(split):
    def rx(s):
        return re.compile(re.sub(r"\\\{\w+\\\}", ".+?", re.escape(s)))
    tpls = [rx(x) for bank in P.BANKS.values() for xs in bank.values() for x in P.by_split(xs, split)]
    heads = [rx(x) for x in P.by_split(P.HEADER, split) + P.by_split(P.HEADER_NO_AGE, split)]
    return tpls, heads, set(P.by_split(P.FILLERS, split))


def test_each_split_uses_only_its_own_phrases(ts):
    pats = {s: _patterns(s) for s in ("train", "test")}
    for t in ts:
        tpls, heads, fillers = pats[t["split"]]
        for case in t["cases"].values():
            head, setting, *body = case["text"].split("\n")
            assert any(h.fullmatch(head) for h in heads), head
            assert setting == _rule(t).setting
            for s in body:
                assert s in fillers or any(p.fullmatch(s) for p in tpls), (t["tid"], s)
            for m in engine.state_from_json(case["state"]):
                assert m.subject == "patient" or m.subject in P.persons(m.concept, t["split"],
                                                                         _age(t))
