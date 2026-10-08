import itertools

import pytest

from selrm import kb_criterion as K

pytestmark = pytest.mark.skipif(not (K.EXT / "release_conditions.json").exists(), reason="DDXPlus release not downloaded")


def test_counts_of_the_release():
    cond, ev = K.kb()
    assert len(cond) == 49 and len(ev) == 223
    assert sum(len(c["symptoms"]) for c in cond.values()) == 605
    assert sum(len(c["antecedents"]) for c in cond.values()) == 283
    assert sorted(sum(e["data_type"] == t for e in ev.values()) for t in "BCM") == [5, 10, 208]
    assert sum(bool(e["is_antecedent"]) for e in ev.values()) == 113


def test_text_is_symmetric_and_partitions_the_lists():
    cond, ev = K.kb()
    for a, b in itertools.combinations(sorted(cond), 2):
        t = K.render(a, b)
        assert t == K.render(b, a) and t.endswith(K.PROCEDURE)
        oa, ob, both = K.lists(a, b)
        assert not set(oa) & set(ob) and not set(oa) & set(both) and not set(ob) & set(both)
        assert set(oa) | set(both) == set(K.findings(a)) and set(ob) | set(both) == set(K.findings(b))
        for e in oa + ob + both:
            assert ev[e]["question_en"] in t


def test_text_states_no_decision_and_no_answer_values():
    cond, ev = K.kb()
    a, b = sorted(cond)[:2]
    t = K.render(a, b)
    assert "most likely" not in t.lower()
    for e in ev.values():                           # categorical findings appear by question only
        for v in e["value_meaning"].values():
            if len(v.get("en", "")) > 12:
                assert f"- {v['en']}" not in t
