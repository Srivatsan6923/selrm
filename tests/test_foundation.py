"""Run: python -m pytest -q tests  (or: python tests/test_foundation.py)"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import smoke as S
from selrm.metrics import decisions, summarise, bootstrap_ci, paired_diff
from selrm.prompts import verdict_prompt, reader_prompt, judge_prompt, ledger_to_text, answer
from selrm.rules import RULES_BY_ID, Mention
from selrm.schema import validate


def _sets():
    seen, held = S.split_rules()
    tr = S.generate(200, 1, seen, "t", "train", S.TRAIN_TPL)
    te = S.generate(200, 3, held, "t", "test", S.TEST_TPL)
    return tr, te


def test_schema_and_labels():
    tr, te = _sets()
    for recs in tr + te:
        for r in recs:
            validate(r)
            rule = RULES_BY_ID[r["rid"]]
            st = [Mention(**m) for m in r["state"]]
            y = rule.label(st, r["cid"]) if r["claim_type"] == "conclusion" else int(rule.crit(r["cid"]).evaluate(st))
            assert r["label"] == int((r["claim_role"] == "s_prime") == (y == 1))
        by = {(r["case_kind"], r["claim_role"]): r["label"] for r in recs if r["claim_type"] == "conclusion"}
        assert by[("base", "s")] == 1 and by[("flip", "s_prime")] == 1 and by[("near", "s")] == 1 and by[("pres", "s")] == 1


def test_heldout_rules_and_templates():
    tr, te = _sets()
    assert not ({r["rid"] for t in tr for r in t} & {r["rid"] for t in te for r in t})
    assert {r["meta"]["tpl"] for t in tr for r in t} <= set(S.TRAIN_TPL)
    assert {r["meta"]["tpl"] for t in te for r in t} <= set(S.TEST_TPL)


def test_corpora_same_size_and_content():
    tr, _ = _sets()
    b, t = S.corpus(tr, "blocks"), S.corpus(tr, "triplets")
    assert len(b) == len(t)
    assert not any(r["case_kind"] == "near" for r in b) and any(r["case_kind"] == "near" for r in t)


def test_metrics_and_prompts():
    _, te = _sets()
    recs = [r for t in te for r in t]
    T = decisions(recs, [float(r["label"]) for r in recs])
    assert summarise(T)["all"]["TA"] == 100.0
    lo, hi = bootstrap_ci(T, "TA", B=200)
    assert lo == hi == 100.0
    T0 = decisions(recs, [1.0 if r["claim_role"] == "s" else 0.0 for r in recs])
    assert summarise(T0)["all"]["TA"] == 0.0 and paired_diff(T, T0, "TA", B=200)[0] == 100.0
    r = recs[0]
    assert r["claim_text"] in verdict_prompt(r) and r["case_text"] not in judge_prompt(r, ledger_to_text(r["ledger"]))
    assert r["condition"] in reader_prompt(r) and answer(r) in "+-"


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn(); print("ok", name)
