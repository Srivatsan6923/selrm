"""Shortcut scorers on a test set (A-D14, Table 7).

  python scripts/shortcut_scorers.py [--data data] [--test rule_v1/test_L2] [--train rule_v1/train_triplets]

Each scorer gives every record a score u (higher = claim judged correct) and
writes results/A-D14-<scorer>/{meta.json, scores_<set>.jsonl, summary_<set>.json, DONE}:
  always_default   u(s) = 1, u(s') = 0
  claim_only       logistic regression on the claim's words (sees no case)
  concept_named    prefers s' iff a keyword of the decisive concept occurs in the case
  attribute_blind  logistic regression on the decisive concept's mentions without
                   subject, status and time (named; a value on the flip side)
  bag_of_words     logistic regression on the words of the case
  trigger_train    ConText-style reading of the decisive lines with the training
                   cue and person lexicons, then the rule program
  trigger_all      the same with the test cues and people added
Learned scorers are trained on the conclusion records of the training corpus.
"""
import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import phrases as P  # noqa: E402
from selrm.metrics import bootstrap_ci, decisions, summarise  # noqa: E402
from selrm.rules import OPS, Mention  # noqa: E402
from selrm.rules_grammar import invented_rules  # noqa: E402

D.register(invented_rules())
YEAR = re.compile(r"\b(19|20)\d\d\b")
NUM = re.compile(r"\d+(?:\.\d+)?")


def load(path):
    return [json.loads(x) for x in open(path, encoding="utf-8")]


def crit(r):
    return D.RULES_BY_ID[r["rid"]].crit(r["cid"])


def case_y(recs):
    """Training pairs (case text, case record, y) with y = 1 if s' is correct."""
    out = [(r["case_text"], r, r["label"]) for r in recs
           if r["claim_type"] == "conclusion" and r["claim_role"] == "s_prime"
           and r["case_kind"] in ("base", "flip", "near", "pres")]
    return out


def as_u(r, p_flip):
    """Score of the record's claim from P(s' correct)."""
    return float(p_flip if r["claim_role"] == "s_prime" else 1.0 - p_flip)


def blind(r):
    c = crit(r)
    ms = [m for m in r["state"] if m["concept"] == c.concept]
    named = any(k in r["case_text"].lower() for k in c.keywords)
    thr = r["meta"]["overrides"].get(c.cid, c.threshold)
    flip = c.kind == "numeric" and any(OPS[c.op](m["value"], thr) for m in ms)
    num = c.kind == "numeric"
    return [named, flip, num, named and num, flip and num, len(ms)]


def read_lines(r, lex):
    """ConText-style reader: mentions of the decisive concept from its lines."""
    c = crit(r)
    out = []
    for line in r["case_text"].split("\n")[2:]:
        low = line.lower()
        hits = [low.find(k) for k in c.keywords if k in low]
        if not hits:
            continue
        who = next((p for p in lex["persons"] if re.search(rf"(?<![\w-]){re.escape(p)}(?![\w-])", low)),
                   "patient")
        neg = any(re.search(rf"\b{re.escape(w)}\b", low) for w in lex["neg"])
        past = bool(YEAR.search(line)) or any(re.search(rf"\b{re.escape(w)}\b", low) for w in lex["time"])
        value = True
        if c.kind == "numeric":
            nums = [float(x) for x in NUM.findall(low[min(hits):]) if not YEAR.fullmatch(x)]
            if not nums:
                continue
            value = nums[0]
        out.append(Mention(c.concept, c.kind, value, who, "absent" if neg else "present",
                           "past" if past else "current"))
    return out


def trigger(r, lex):
    rule, c = D.RULES_BY_ID[r["rid"]], crit(r)
    state = [Mention(**m) for m in r["state"] if m["concept"] != c.concept] + read_lines(r, lex)
    try:
        y = rule.label(state, c.cid, r["meta"]["overrides"]) if r["claim_type"] == "conclusion" \
            else int(c.evaluate(state, r["meta"]["overrides"].get(c.cid)))
    except ValueError:          # no readable current value: fall back to the default answer
        y = 0
    return float(y)


def lexicon(splits):
    return {"neg": [w for s in splits for w in P.NEG_CUES[s]],
            "time": [w for s in splits for w in P.TIME_CUES[s]],
            "persons": sorted({p for s in splits for p in P.by_split(P.PERSONS, s)}, key=len, reverse=True)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--test", default="rule_v1/test_L2")
    ap.add_argument("--train", default="rule_v1/train_triplets")
    ap.add_argument("--out", default="results")
    a = ap.parse_args()
    test = load(Path(a.data) / a.test / "records.jsonl")
    train = case_y(load(Path(a.data) / a.train / "records.jsonl"))
    texts, recs, ys = zip(*train)
    ys = np.array(ys)
    scores = {}

    scores["always_default"] = [1.0 if r["claim_role"] == "s" else 0.0 for r in test]
    scores["concept_named"] = [
        1.0 if (r["claim_role"] == "s_prime") == any(k in r["case_text"].lower() for k in crit(r).keywords)
        else 0.0 for r in test]

    claims = [(r["claim_text"], r["label"]) for r in load(Path(a.data) / a.train / "records.jsonl")
              if r["claim_type"] == "conclusion"]
    vc = CountVectorizer(binary=True).fit([t for t, _ in claims])
    m = LogisticRegression(max_iter=2000).fit(vc.transform([t for t, _ in claims]), [y for _, y in claims])
    scores["claim_only"] = list(m.predict_proba(vc.transform([r["claim_text"] for r in test]))[:, 1])

    m = LogisticRegression(max_iter=2000).fit(np.array([blind(r) for r in recs], float), ys)
    p = m.predict_proba(np.array([blind(r) for r in test], float))[:, 1]
    scores["attribute_blind"] = [as_u(r, q) for r, q in zip(test, p)]

    vb = CountVectorizer(binary=True, min_df=2).fit(texts)
    m = LogisticRegression(max_iter=3000).fit(vb.transform(texts), ys)
    p = m.predict_proba(vb.transform([r["case_text"] for r in test]))[:, 1]
    scores["bag_of_words"] = [as_u(r, q) for r, q in zip(test, p)]

    for name, splits in (("trigger_train", ("train",)), ("trigger_all", ("train", "test"))):
        lex = lexicon(splits)
        scores[name] = [as_u(r, trigger(r, lex)) for r in test]

    set_name = a.test.replace("/", "__")
    for name, u in scores.items():
        d = Path(a.out) / f"A-D14-{name}"
        d.mkdir(parents=True, exist_ok=True)
        T = decisions(test, u)
        S = summarise(T)
        S.update(run_id=f"A-D14-{name}", set=a.test, claim_type="conclusion",
                 CI95={k: bootstrap_ci(T, k) for k in ("TA", "Rev", "Hold")})
        (d / f"scores_{set_name}.jsonl").write_text(
            "".join(json.dumps({"iid": r["iid"], "u": x}) + "\n" for r, x in zip(test, u)), encoding="utf-8")
        (d / f"summary_{set_name}.json").write_text(json.dumps(S, indent=1), encoding="utf-8")
        (d / "meta.json").write_text(json.dumps({
            "run_id": f"A-D14-{name}", "model": name, "train": a.train, "test": a.test,
            "date": datetime.date.today().isoformat(), "git_commit": D.git_commit(),
            "sklearn": __import__("sklearn").__version__}, indent=1), encoding="utf-8")
        (d / "DONE").write_text("")
        print(f"{name:16s} TA {S['all']['TA']:5.1f}  Rev {S['all']['Rev']:5.1f}  Hold {S['all']['Hold']:5.1f}  "
              + "  ".join(f"{k[8:]} {v['TA']:.0f}" for k, v in sorted(S.items()) if k.startswith("nm_kind=")))


if __name__ == "__main__":
    main()
