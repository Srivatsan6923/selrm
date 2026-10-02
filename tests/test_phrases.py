"""Phrase banks: 6 templates per form (0-3 train, 4-5 test), keyword and cue discipline."""
import re

from selrm import phrases as P
from selrm.library import LIBRARY
from selrm.rules import FIRST_DEGREE

ALL_KW = {k for r in LIBRARY for c in r.criteria for k in c.keywords}
SLOTS = {"v", "dia", "year", "Poss", "rel"}
NAMING = {"present", "past", "absent", "rel", "rel_past", "delabelled", "current", "superseded"}
LEX = {"neg": P.NEG_CUES, "time": P.TIME_CUES, "current": P.CURRENT_CUES}
SPLITS = ("train", "test")


def _templates():
    for concept, bank in P.BANKS.items():
        for form, tpls in bank.items():
            for i, tpl in enumerate(tpls):
                yield concept, form, P.split_of(i), tpl


def _cues(text, lexicon, split):
    return [c for c in lexicon[split] if re.search(rf"\b{re.escape(c)}\b", text.lower())]


def _criteria():
    for r in LIBRARY:
        for c in r.criteria:
            yield r, c


def test_layout_six_per_form_and_forms_present():
    for r, c in _criteria():
        bank = P.BANKS[c.concept]
        need = {"current"} if c.kind == "numeric" else {"generic", "present", "absent", "rel", "past"}
        if c.kind == "numeric" and "time" in c.nm_kinds():
            need |= {"past", "superseded"}
        if c.kind == "finding" and c.counts_past:
            need.add("rel_past")
        assert need <= set(bank), (c.cid, need - set(bank))
    for concept, bank in P.BANKS.items():
        for form, tpls in bank.items():
            assert len(tpls) == 6, (concept, form)
    assert len(P.FILLERS) % 6 == len(P.FILLERS_OTHER) % 6 == len(P.FILLERS_LAB) % 6 == 0
    assert len(P.HEADER) == len(P.HEADER_NO_AGE) == 6 and len(P.PERSONS) % 6 == 0


def test_zero_overlap_between_splits():
    lists = [P.FILLERS, P.FILLERS_OTHER, P.FILLERS_LAB, P.HEADER, P.HEADER_NO_AGE, P.PERSONS] + \
        [tpls for bank in P.BANKS.values() for tpls in bank.values()]
    for items in lists:
        tr, te = set(P.by_split(items, "train")), set(P.by_split(items, "test"))
        assert tr and te and not tr & te
    train_text = {t for *_, s, t in _templates() if s == "train"}
    assert not train_text & {t for *_, s, t in _templates() if s == "test"}
    for lex in LEX.values():
        assert not set(lex["train"]) & set(lex["test"])
    words = [c for lex in LEX.values() for s in SPLITS for c in lex[s]]
    assert len(words) == len(set(words))


def test_templates_use_known_slots_and_render():
    for concept, form, _, tpl in _templates():
        assert set(re.findall(r"{(\w+)}", tpl)) <= SLOTS, tpl
        assert ("{dia}" in tpl) <= (concept == "sbp"), tpl
        out = tpl.format(v=12, dia=40, year=2015, Poss="Her", rel="aunt")
        assert "{" not in out and out.endswith("."), out
        assert ("{year}" in tpl) <= (P.FORMS[form][1] == "past"), tpl
        assert ("{rel}" in tpl) == form.startswith("rel"), tpl


def test_keyword_discipline_within_rules():
    for r, c in _criteria():
        others = {k for o in r.criteria if o is not c for k in o.keywords}
        for form, tpls in P.BANKS[c.concept].items():
            for tpl in tpls:
                low = tpl.lower()
                assert not [k for k in others if k in low], (r.rid, tpl)
                assert any(k in low for k in c.keywords) == (form in NAMING), (c.cid, form, tpl)
                if c.kind == "numeric":
                    first = min(i for k in c.keywords if (i := low.find(k)) >= 0)
                    between = low[first:low.index("{v}")].replace("{year}", "")
                    assert not re.search(r"\d", between), tpl


def test_cue_words_are_split():
    bad = []
    for concept, form, split, tpl in _templates():
        if form == "generic":
            continue
        other = SPLITS[split == "train"]
        own = {k: _cues(tpl, lex, split) for k, lex in LEX.items()}
        if [c for lex in LEX.values() for c in _cues(tpl, lex, other)]:
            bad.append((split, tpl, "cue of the other split"))
        if form in ("present", "rel", "current") and (own["neg"] or own["time"]):
            bad.append((split, tpl, "negation or past-time cue"))
        if form == "current" and not own["current"]:
            bad.append((split, tpl, "no current cue"))
        if form == "absent" and not own["neg"]:
            bad.append((split, tpl, "no negation cue"))
        if form == "superseded" and not own["time"]:
            bad.append((split, tpl, "no time cue"))
        if form in ("past", "rel_past", "delabelled") and not ("{year}" in tpl or own["time"]):
            bad.append((split, tpl, "no year or time cue"))
    assert bad == []


def test_missing_lines_are_split_and_render():
    assert len(P.MISSING) % 6 == 0
    tr, te = set(P.by_split(P.MISSING, "train")), set(P.by_split(P.MISSING, "test"))
    assert tr and te and not tr & te
    for i, tpl in enumerate(P.MISSING):
        assert set(re.findall(r"{(\w+)}", tpl)) <= {"What", "what"}, tpl
        assert tpl.format(What="X", what="x").endswith(".")
        other = SPLITS[P.split_of(i) == "train"]
        assert not [c for lex in LEX.values() for c in _cues(tpl, lex, other)], tpl


def test_people_names_and_pools():
    texts = [t for *_, t in _templates()] + P.FILLERS + P.FILLERS_OTHER + P.FILLERS_LAB + P.MISSING
    for text in texts:
        assert not [p for p in P.PERSONS if re.search(rf"\b{re.escape(p)}\b", text.lower())], text
    for _, c in _criteria():
        if c.kind != "finding":
            continue
        for split in SPLITS:
            for age in (17, 30, 50, 70, 90):
                pool = P.persons(c.concept, split, age)
                assert pool and set(pool) <= set(P.by_split(P.PERSONS, split)), (c.cid, split, age)
                if c.counts_family:
                    assert set(pool) & FIRST_DEGREE and set(pool) - FIRST_DEGREE, (c.cid, split, age)


def test_fillers_settings_and_headers_carry_no_keyword():
    for f in P.FILLERS + P.FILLERS_OTHER + P.FILLERS_LAB:
        assert not [k for k in ALL_KW if k in f.lower()], f
    assert all(set(re.findall(r"{(\w+)}", f)) == set() for f in P.FILLERS)
    assert all(f.startswith("{Poss} {rel}") for f in P.FILLERS_OTHER)
    assert all(set(re.findall(r"{(\w+)}", f)) == {"year"} for f in P.FILLERS_LAB)
    for r in LIBRARY:
        kws = {k for c in r.criteria for k in c.keywords}
        assert not [k for k in kws if k in r.setting.lower()], r.rid
    for frame in P.HEADER + P.HEADER_NO_AGE:
        for sex, noun in (("female", "woman"), ("male", "man")):
            out = frame.format(age=47, noun=noun, Noun=noun.capitalize(), sex=sex, Sex=sex.capitalize())
            assert not [k for k in ALL_KW if k in out.lower()], out
