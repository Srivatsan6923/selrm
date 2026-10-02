import re

import pytest

from selrm import phrases as P
from selrm.rules import FIRST_DEGREE, RULES

ALL_KW = {k for r in RULES for c in r.criteria for k in c.keywords}
SLOTS = {"v", "dia", "year", "Poss", "rel"}
NAMING = {"present", "past", "absent", "rel", "rel_past", "delabelled", "current", "superseded"}
CUE_FREE = {"present", "rel", "current"}
SPLITS = ("train", "test")


def _templates():
    for concept, bank in P.BANKS.items():
        for form, tpls in bank.items():
            for i, tpl in enumerate(tpls):
                yield concept, form, SPLITS[i % 2], tpl


def _cues(text, lexicon, split):
    t = text.lower()
    return [c for c in lexicon[split] if re.search(rf"\b{re.escape(c)}\b", t)]


def _criteria():
    for r in RULES:
        for c in r.criteria:
            yield r, c


_NUMERIC = {c.concept for _, c in _criteria() if c.kind == "numeric"}


def test_every_criterion_has_the_forms_its_triplets_need():
    for r, c in _criteria():
        bank = P.BANKS[c.concept]
        need = {"current"} if c.kind == "numeric" else {"generic", "present", "absent", "rel", "past"}
        if c.kind == "numeric" and "time" in c.nm_kinds():
            need |= {"past", "superseded"}
        if c.kind == "finding" and c.counts_past:
            need.add("rel_past")
        assert need <= set(bank), (c.cid, need - set(bank))
        for form, tpls in bank.items():
            # two per split, so a presentation edit can switch templates
            assert len(tpls) >= (2 if form == "rel_past" else 4), (c.concept, form)


def test_templates_use_known_slots_and_render():
    for concept, form, _, tpl in _templates():
        assert set(re.findall(r"{(\w+)}", tpl)) <= SLOTS, tpl
        out = tpl.format(v=12, dia=40, year=2015, Poss="Her", rel="aunt")
        assert "{" not in out and out.endswith("."), out
        assert ("{year}" in tpl) <= (P.FORMS[form][1] == "past"), tpl
        assert ("{rel}" in tpl) == form.startswith("rel"), tpl
        assert ("{v}" in tpl) == (form in ("current", "superseded") or
                                  (form == "past" and concept in _NUMERIC)), tpl


def test_naming_forms_name_the_concept_and_nothing_else_in_the_rule():
    for r, c in _criteria():
        others = {k for o in r.criteria if o is not c for k in o.keywords}
        for form, tpls in P.BANKS[c.concept].items():
            for tpl in tpls:
                low = tpl.lower()
                assert not [k for k in others if k in low], (r.rid, tpl)
                named = any(k in low for k in c.keywords)
                assert named == (form in NAMING), (c.cid, form, tpl)


def test_numeric_value_follows_a_keyword():
    for _, c in _criteria():
        if c.kind == "numeric":
            for tpl in sum(P.BANKS[c.concept].values(), []):
                low = tpl.lower()
                first_kw = min(i for k in c.keywords if (i := low.find(k)) >= 0)
                assert first_kw < low.index("{v}"), tpl


def test_cue_words_are_split():
    lexicons = (P.NEG_CUES, P.TIME_CUES, P.CURRENT_CUES)
    words = [c for lex in lexicons for s in SPLITS for c in lex[s]]
    assert len(words) == len(set(words))         # each cue: one lexicon, one split
    bad = []
    for concept, form, split, tpl in _templates():
        if form == "generic":
            continue
        other = SPLITS[split == "train"]
        own = {name: _cues(tpl, lex, split) for name, lex in
               (("neg", P.NEG_CUES), ("time", P.TIME_CUES), ("current", P.CURRENT_CUES))}
        if [c for lex in lexicons for c in _cues(tpl, lex, other)]:
            bad.append((split, tpl, "cue of the other split"))
        if form in CUE_FREE and (own["neg"] or own["time"]):
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


def test_person_names_only_through_the_rel_slot():
    for text in [tpl for *_, tpl in _templates()] + P.FILLERS:
        assert not [p for p in P.PERSONS if re.search(rf"\b{re.escape(p)}\b", text.lower())], text


def test_split_by_parity():
    for items in [P.FILLERS, P.PERSONS, P.HEADER, P.HEADER_NO_AGE] + \
            [tpls for bank in P.BANKS.values() for tpls in bank.values()]:
        tr, te = P.by_split(items, "train"), P.by_split(items, "test")
        assert tr and te and len(tr) + len(te) == len(items)
        assert not set(tr) & set(te)
    with pytest.raises(ValueError):
        P.by_split(P.FILLERS, "dev")


def test_people_pools_cover_every_split():
    for _, c in _criteria():
        if c.kind != "finding":
            continue
        for split in SPLITS:
            pool = P.persons(c.concept, split)
            assert pool and set(pool) <= set(P.by_split(P.PERSONS, split))
            if c.counts_family:
                assert set(pool) & FIRST_DEGREE and set(pool) - FIRST_DEGREE, (c.cid, split)


def test_fillers_settings_and_headers_carry_no_keyword():
    assert len(set(P.FILLERS)) == len(P.FILLERS)
    for f in P.FILLERS:
        assert not [k for k in ALL_KW if k in f.lower()], f
    for r in RULES:
        kws = {k for c in r.criteria for k in c.keywords}
        assert not [k for k in kws if k in r.setting.lower()], r.rid
    for frame in P.HEADER + P.HEADER_NO_AGE:
        for sex, noun in (("female", "woman"), ("male", "man")):
            out = frame.format(age=47, noun=noun, Noun=noun.capitalize(), sex=sex, Sex=sex.capitalize())
            assert not [k for k in ALL_KW if k in out.lower()], out
