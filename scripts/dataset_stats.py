"""Rule-library statistics, split overlap and dataset counts (A-D15).

  python scripts/dataset_stats.py [--data data] [--out results/A-D15]

Writes summary.json: rules by source and signature class; per fold the held-out
classes and rule counts; overlap between training and L2 rules (canonical
programs, criterion subexpressions, rule texts) and between train and test
templates and cue words; per registered set the counts and reject rates from
its MANIFEST.
"""
import argparse
import datetime
import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import folds as FD  # noqa: E402
from selrm import phrases as P  # noqa: E402
from selrm import rules, rules_constraint, rules_grammar, rules_score  # noqa: E402
from selrm.library import LIBRARY, LIBRARY_BY_ID  # noqa: E402


def crit_key(c):
    return (c.concept, c.kind, c.op, c.threshold, c.counts_past, c.counts_family, c.points)


def program_key(r):
    return (r.kind, r.logic, r.cutoff, tuple(sorted(map(crit_key, r.criteria), key=str)))


def overlap(train, held):
    tr_prog = {program_key(r) for r in train}
    tr_crit = {crit_key(c) for r in train for c in r.criteria}
    tr_text = {r.rule_text() for r in train}
    held_crit = [crit_key(c) for r in held for c in r.criteria]
    return {"programs": 100.0 * sum(program_key(r) in tr_prog for r in held) / len(held),
            "criterion_subexpressions": 100.0 * sum(k in tr_crit for k in held_crit) / len(held_crit),
            "rule_texts": 100.0 * sum(r.rule_text() in tr_text for r in held) / len(held)}


def template_overlap():
    lists = [P.FILLERS, P.FILLERS_OTHER, P.FILLERS_LAB, P.HEADER, P.HEADER_NO_AGE, P.PERSONS, P.MISSING] + \
        [L for b in P.BANKS.values() for L in b.values()]
    tr = {t for L in lists for t in P.by_split(L, "train")}
    te = {t for L in lists for t in P.by_split(L, "test")}
    cues = [P.NEG_CUES, P.TIME_CUES, P.CURRENT_CUES]
    ctr = {w for lex in cues for w in lex["train"]}
    cte = {w for lex in cues for w in lex["test"]}
    return {"templates_train": len(tr), "templates_test": len(te), "templates_shared": len(tr & te),
            "cue_words_train": len(ctr), "cue_words_test": len(cte), "cue_words_shared": len(ctr & cte)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default="data")
    ap.add_argument("--out", default="results/A-D15")
    a = ap.parse_args()
    src = {"pilot": rules.RULES, "constraint": rules_constraint.RULES, "score": rules_score.RULES,
           "grammar_curated": rules_grammar.RULES, "grammar_sampled": rules_grammar.SAMPLED}
    out = {"run_id": "A-D15", "date": datetime.date.today().isoformat(), "git_commit": D.git_commit(),
           "rules_by_source": {k: len(v) for k, v in src.items()},
           "rules_by_kind": dict(Counter(r.kind for r in LIBRARY)), "rules_total": len(LIBRARY),
           "invented_rules_L3inv": len(rules_grammar.invented_rules()),
           "classes": {c: len(v) for c, v in FD.classes(LIBRARY).items()},
           "classes_by_source": {k: len({FD.sig_class(r) for r in v}) for k, v in src.items()},
           "templates": template_overlap()}
    folds_path = Path(a.data) / "rule_v1" / "FOLDS.json"
    F = json.loads(folds_path.read_text()) if folds_path.exists() else json.loads(json.dumps(FD.make_folds(LIBRARY)))
    out["folds"] = {}
    for k, f in F["folds"].items():
        train = [LIBRARY_BY_ID[x] for x in f["train_rules"]]
        held = [LIBRARY_BY_ID[x] for x in f["l2_rules"]]
        out["folds"][k] = {"l2_classes": f["l2_classes"], "n_classes": len(F["classes"]),
                           "n_l2_rules": len(held), "n_l1_rules": len(f["l1_rules"]),
                           "n_train_rules": len(train), "overlap_train_vs_L2": overlap(train, held)}
    reg_path = Path(a.data) / "REGISTRY.json"
    out["datasets"] = {}
    if reg_path.exists():
        for name, v in json.loads(reg_path.read_text()).items():
            m = json.loads((Path(a.data) / v["manifest"]).read_text())
            rej = m.get("rejects", {})
            out["datasets"][name] = {k: m[k] for k in ("n_groups", "n_cases", "n_records", "cases_by_kind",
                                                       "record_share")} | {
                "nm_kind": m["groups_by"]["nm_kind"], "tier": m["groups_by"]["tier"],
                "n_rules": len(m["groups_by"]["rid"]),
                "reject_rate": 100.0 * rej["rejected"] / rej["proposed"] if rej.get("proposed") else None,
                "shortcut_validation": m["shortcut_validation"]["result"]}
    d = Path(a.out)
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    (d / "DONE").write_text("")
    print(json.dumps({k: out[k] for k in ("rules_by_source", "rules_total", "templates")}, indent=1))
    for k, f in out["folds"].items():
        print("fold", k, f["n_l2_rules"], f["n_train_rules"], f["overlap_train_vs_L2"])


if __name__ == "__main__":
    main()
