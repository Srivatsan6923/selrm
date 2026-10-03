"""Signature classes and folds (A-D3).

signature(rule): the structural signature of a rule (kind, operator, depth,
input types, numeric operators, applicability predicates). sig_class(rule):
the class used for the ladder: operator x input types x applicability scope.
make_folds(rules): three folds; each holds out whole classes (L2), and within
the remaining classes a share of rules (L1, unseen rules of a seen class);
the rest are training rules (L0). Classes with fewer than MIN_CLASS rules are
never held out. The search is seeded and deterministic; the frozen result is
written next to each dataset version (data/<set>/FOLDS.json).
"""
from __future__ import annotations

import random
from collections import defaultdict

from selrm.engine import nm_kinds, pivots

N_FOLDS = 3
MIN_CLASS = 4          # smaller classes always stay in training
L1_SHARE = 0.10        # rules of each training class held out as L1 (at least 1 from 5 rules)
L2_SHARE = (0.12, 0.30)  # bounds on the share of rules held out per fold
OPERATORS = ("single", "any", "all", "kofn", "score")
NM_KINDS = {"numeric", "boundary", "subject", "negation", "time"}


def scope(c):
    return "family" if c.counts_family else "ever" if c.counts_past else "current"


def operator(rule):
    if rule.kind == "score":
        return "score"
    if len(rule.criteria) == 1:
        return "single"
    return {"any": "any", "all": "all", "atleast": "kofn"}[rule.logic]


def signature(rule):
    return {"kind": rule.kind, "operator": operator(rule), "depth": len(rule.criteria),
            "inputs": sorted({c.kind for c in rule.criteria}),
            "ops": sorted({c.op for c in rule.criteria if c.kind == "numeric"}),
            "applicability": sorted({scope(c) for c in rule.criteria if c.kind == "finding"})}


def sig_class(rule):
    s = signature(rule)
    inputs = "mixed" if len(s["inputs"]) == 2 else s["inputs"][0]
    app = "-" if not s["applicability"] else "ext" if set(s["applicability"]) - {"current"} else "cur"
    return f"{s['operator']}|{inputs}|{app}"


def classes(rules):
    out = defaultdict(list)
    for r in rules:
        out[sig_class(r)].append(r.rid)
    return dict(sorted(out.items()))


def _kinds(rules):
    return {nm for r in rules for c in r.criteria if pivots(r, c) for nm in nm_kinds(c)}


def _valid(held, cls, by_id, n_rules):
    """Every fold: training keeps every operator, input type and scope; held-out
    rules cover every near-miss kind and a bounded share of the library."""
    for h in held:
        train = [c for c in cls if c not in h]
        parts = [set(x) for x in zip(*(c.split("|") for c in train))]
        if not (set(OPERATORS) <= parts[0] and {"numeric", "finding", "mixed"} <= parts[1]
                and {"cur", "ext"} <= parts[2]):
            return False
        rids = [rid for c in h for rid in cls[c]]
        if not L2_SHARE[0] <= len(rids) / n_rules <= L2_SHARE[1]:
            return False
        if _kinds([by_id[rid] for rid in rids]) != NM_KINDS:
            return False
    return True


def make_folds(rules, seed=0, per_fold=None):
    cls = classes(rules)
    by_id = {r.rid: r for r in rules}
    eligible = [c for c, rids in cls.items() if len(rids) >= MIN_CLASS]
    k = per_fold or (5 if len(eligible) >= 15 else 4)
    if len(eligible) < N_FOLDS * k:
        raise ValueError(f"{len(eligible)} eligible classes, need {N_FOLDS * k}")
    for s in range(seed, seed + 10000):
        order = sorted(eligible)
        random.Random(s).shuffle(order)
        held = [sorted(order[i * k:(i + 1) * k]) for i in range(N_FOLDS)]
        if _valid(held, cls, by_id, len(rules)):
            break
    else:
        raise RuntimeError("no valid fold assignment")
    folds = {}
    for i, h in enumerate(held, 1):
        rng = random.Random(f"l1.{s}.{i}")
        l1 = []
        for c, rids in cls.items():
            if c not in h and len(rids) >= 5:
                l1 += rng.sample(rids, max(1, round(L1_SHARE * len(rids))))
        l2 = [rid for c in h for rid in cls[c]]
        folds[i] = {"l2_classes": h, "l2_rules": l2, "l1_rules": sorted(l1),
                    "train_rules": [r.rid for r in rules if r.rid not in set(l1) | set(l2)]}
    return {"seed": s, "class_def": "operator|inputs|applicability (cur, ext = past or family)",
            "min_class": MIN_CLASS, "l1_share": L1_SHARE, "classes": cls, "folds": folds}
