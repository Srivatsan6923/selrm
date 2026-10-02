"""Engine (A-D0): canonical records, invariants, splits, tiers."""
import copy
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pytest

from selrm import engine as E
from selrm import phrases as P
from selrm.library import LIBRARY, LIBRARY_BY_ID
from selrm.rules import FIRST_DEGREE, OPS, Mention
from selrm.schema import validate

SEEDS = range(2)
ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def generated():
    stats = Counter()
    groups = [E.make_group(*cell, split, s, "t", "L0", stats)
              for split in ("train", "test") for cell in E.cells() for s in SEEDS]
    return groups, stats


@pytest.fixture(scope="module")
def groups(generated):
    return generated[0]


def _cases(recs):
    """case_kind -> one record per case (claims share the case fields)."""
    return {r["case_kind"]: r for r in recs}


def _crit(r):
    return LIBRARY_BY_ID[r["rid"]].crit(r["cid"])


def _target(rec):
    c = _crit(rec)
    return [Mention(**m) for m in rec["state"] if m["concept"] == c.concept]


def test_every_cell_generates_valid_records(generated):
    groups, stats = generated
    assert len(groups) == 2 * len(E.cells()) * len(SEEDS)
    assert stats["rejected"] / stats["proposed"] < 0.05
    iids = set()
    for recs in groups:
        rule = LIBRARY_BY_ID[recs[0]["rid"]]
        kinds = ["conclusion", "criterion"] if rule.kind == "constraint" else ["conclusion"]
        assert len(recs) == 4 * len(kinds) * 2
        for r in recs:
            validate(r)
            iids.add(r["iid"])
            st = [Mention(**m) for m in r["state"]]
            y = E.case_labels(rule, _crit(r), r["meta"]["overrides"], st)[r["claim_type"]]
            assert r["label"] == int((r["claim_role"] == "s_prime") == (y == 1))
            assert y == E.WANT[r["case_kind"]]
            assert r["meta"]["criterion_holds"] == (r["case_kind"] == "flip")
    assert len(iids) == sum(len(g) for g in groups)


def test_cells_cover_every_criterion_kind_and_tier():
    cs = E.cells()
    assert {(r, c) for r, c, _, _ in cs} == {(r.rid, c.cid) for r in LIBRARY for c in r.criteria}
    assert {t for *_, t in cs} == set(E.TIERS)
    assert {nm for _, _, nm, _ in cs} == {"numeric", "boundary", "subject", "negation", "time"}
    for rid, cid, nm, tier in cs:
        c = LIBRARY_BY_ID[rid].crit(cid)
        if nm == "boundary":
            assert c.kind == "numeric" and c.op in ("<", ">")
        if tier in ("superseded", "delabelled"):
            assert nm == "time"


def test_proposition_1_keyword_pattern(groups):
    for recs in groups:
        c = _crit(recs[0])
        for k, r in _cases(recs).items():
            named = any(kw in r["case_text"].lower() for kw in c.keywords)
            assert named == (c.kind == "numeric" or k in ("flip", "near")), (r["iid"], named)


def test_near_misses_differ_from_a_counted_mention_in_one_attribute(groups):
    for recs in groups:
        cs = _cases(recs)
        c, kind = _crit(recs[0]), recs[0]["nm_kind"]
        thr = cs["base"]["meta"]["overrides"].get(c.cid, c.threshold)
        base, flip, near = (_target(cs[k]) for k in ("base", "flip", "near"))
        assert len(base) <= len(flip) == len(near) <= len(base) + 1     # same mention count
        (f,) = [m for m in flip if c.applies(m)]
        assert f.status == "present"
        if c.kind == "numeric":
            op = OPS[c.op]
            (b,) = [m for m in base if m.time == "current"]
            assert not [m for m in base + flip if m.time == "past" and op(m.value, thr)]
            if kind in ("numeric", "boundary"):
                (m,) = near
                assert not op(m.value, thr) and abs(m.value - thr) < abs(b.value - thr)
                if kind == "boundary":
                    assert m.value == thr
                else:
                    assert 0 < E._steps(abs(m.value - thr), c) < E._steps(c.near_delta, c)
            else:
                (m,) = [x for x in near if x != b]
                assert m.time == "past" and op(m.value, thr) and not c.applies(m)
            continue
        if kind == "negation":
            (m,) = near
            assert m.status == "absent" and m.form == "absent"
            continue
        (m,) = [x for x in near if x not in base]
        assert not c.applies(m)
        if kind == "subject":   # another person, at the flip's time: only the person differs
            assert m.subject != "patient" and not (c.counts_family and m.subject in FIRST_DEGREE)
            assert m.time == f.time, recs[0]["tid"]
        else:
            assert m.subject == "patient" and m.time == "past" and not c.counts_past


def test_test_split_uses_only_test_templates_people_and_fillers(groups):
    for recs in groups:
        r = recs[0]
        for rec in _cases(recs).values():
            for t in rec["meta"]["tpl"]:
                assert P.split_of(int(t.rsplit("/", 1)[1])) == r["split"], (r["iid"], t)
            assert P.split_of(rec["meta"]["hdr"]) == r["split"]
            for m in rec["state"]:
                assert m["subject"] == "patient" or m["subject"] in P.by_split(P.PERSONS, r["split"])


def test_ledgers_quote_the_case_and_prose_has_no_decision(groups):
    for recs in groups:
        for r in _cases(recs).values():
            for e in r["ledger"]:
                assert e["found"] == "not mentioned" or e["found"] in r["case_text"]
                assert e["need"] == r["condition"]
            # quoted case lines and the condition itself may say "count"
            words = re.sub(r'"[^"]*"', "", r["prose"]).replace(r["condition"], "").lower()
            assert not re.search(r"\b(prescribe|counts?|holds?|points?)\b", words), r["prose"]


def test_no_generic_absence_denies_a_present_concept(groups):
    for recs in groups:
        for r in _cases(recs).values():
            gen = {m["concept"] for m in r["state"] if m["form"] == "generic"}
            pres = {m["concept"] for m in r["state"] if m["status"] == "present"}
            assert not [(a, b) for g in P.OVERLAP for a in gen & g for b in pres & g if a != b], r["iid"]


def test_presentation_edits_preserve_every_fact(groups):
    """Only numeric current and dated past values are reworded; findings,
    superseded values and fillers keep their lines; the order changes."""
    for recs in groups:
        cs = _cases(recs)
        keep = lambda r: sorted(t for t in r["meta"]["tpl"]                     # noqa: E731
                                if not (t.split("/")[1] in ("current", "past") and
                                        any(m["concept"] == t.split("/")[0] and m["kind"] == "numeric"
                                            for m in r["state"])))
        assert keep(cs["pres"]) == keep(cs["base"]), recs[0]["tid"]


def test_tiers(groups):
    for recs in groups:
        r = _cases(recs)["base"]
        n_fill = sum(t.startswith("filler/") for t in r["meta"]["tpl"])
        if r["tier"] == "long":
            assert n_fill >= 15
            assert any("/other/" in t for t in r["meta"]["tpl"]) and any("/lab/" in t for t in r["meta"]["tpl"])
        else:
            assert 1 <= n_fill <= 4
        if r["tier"] == "alt":
            c = _crit(r)
            st = [Mention(**m) for m in _cases(recs)["flip"]["state"]]
            rule = LIBRARY_BY_ID[r["rid"]]
            assert rule.label(st, c.cid, r["meta"]["overrides"]) == 1 and rule.label(st, c.cid) == 0
        if r["tier"] in ("superseded", "delabelled"):
            near = _target(_cases(recs)["near"])
            assert r["tier"] in {m.form for m in near}


def test_age_criterion_moves_age_out_of_the_header(groups):
    for recs in groups:
        r = recs[0]
        head = r["case_text"].split("\n")[0]
        has_age = any(c.concept == "age" for c in LIBRARY_BY_ID[r["rid"]].criteria)
        assert bool(re.search(r"\d", head)) != has_age, head


def test_relatives_are_plausible_for_every_age_in_the_group(groups):
    old = {"mother", "father", "aunt", "uncle"}
    for recs in groups:
        cs = _cases(recs)
        c = _crit(recs[0])
        if c.concept != "age":
            continue
        ages = [m["value"] for k in ("base", "flip") for m in cs[k]["state"] if m["concept"] == "age"]
        words = {w for r in cs.values() for w in re.findall(r"[a-z-]+", r["case_text"].lower())}
        if max(ages) >= 65:
            assert not words & old, (recs[0]["tid"], words & old)
        if max(ages) >= 40:
            assert not words & {"grandmother", "grandfather"}, recs[0]["tid"]


def test_missing_twins_drop_only_the_decisive_input():
    for cell in E.cells():
        plain = E.make_group(*cell, "test", 0, "t", "L0")
        recs = E.make_group(*cell, "test", 0, "t", "L0", missing=True)
        assert [r for r in recs if r["case_kind"] != "missing"] == plain     # other cases unchanged
        miss = [r for r in recs if r["case_kind"] == "missing"]
        c = _crit(miss[0])
        assert len(miss) == len(plain) // 4 and all(r["label"] == 0 for r in miss)
        tgt = [m for m in miss[0]["state"] if m["concept"] == c.concept]
        assert [m["status"] for m in tgt] == ([] if c.kind == "numeric" else ["unknown"])
        assert [e["status"] for e in miss[0]["ledger"]] == ["unknown"]
        base = _cases(plain)["base"]
        assert sorted(map(str, (m for m in miss[0]["state"] if m["concept"] != c.concept))) == \
            sorted(map(str, (m for m in base["state"] if m["concept"] != c.concept)))


def test_deterministic_and_invalid_cells():
    a = E.make_group("curb65", "bun", "time", "superseded", "test", 7)
    assert a == E.make_group("curb65", "bun", "time", "superseded", "test", 7)
    assert json.loads(json.dumps(a)) == a
    assert a != E.make_group("curb65", "bun", "time", "superseded", "test", 8)
    for cell in [("strep_amox", "pen_allergy", "numeric", "easy"), ("migraine_cad", "cad", "time", "easy"),
                 ("curb65", "rr", "boundary", "easy")]:
        with pytest.raises(ValueError):
            E.make_group(*cell, "train", 0)


def test_check_catches_corruption():
    rule = LIBRARY_BY_ID["strep_amox"]
    rng = __import__("random").Random(1)
    g = E._propose(rule, rule.crit("pen_allergy"), "negation", "easy", "train", rng)
    assert E.check(rule, g) == []

    def errs(edit):
        h = copy.deepcopy(g)
        edit(h)
        return " ".join(E.check(rule, h))

    assert "label: near" in errs(lambda h: h["cases"]["near"].update(state=h["cases"]["flip"]["state"]))
    assert "keyword: base" in errs(lambda h: h["cases"]["base"].update(
        text=h["cases"]["base"]["text"] + "\nAllergic to penicillin."))
    assert "pres: same text" in errs(lambda h: h["cases"]["pres"].update(text=h["cases"]["base"]["text"]))
    assert "edit: near" in errs(lambda h: h["cases"]["near"].update(
        lines=h["cases"]["near"]["lines"] + ["Extra line.", "Another line."]))
    assert "ledger: flip" in errs(lambda h: h["cases"]["flip"]["ledger"][0].update(found="Allergic."))


def test_validate_shortcuts_passes(tmp_path):
    recs = [r for cell in E.cells() for r in E.make_group(*cell, "test", 0, "t", "L2")]
    path = tmp_path / "t.jsonl"
    path.write_text("".join(json.dumps(r) + "\n" for r in recs))
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_shortcuts.py"), str(path)],
                         capture_output=True, text=True)
    assert out.returncode == 0 and "PASS" in out.stdout, out.stdout + out.stderr
