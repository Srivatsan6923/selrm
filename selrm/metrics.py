"""Shared metric code (owner: C). Everyone imports this; nobody re-implements it.

Input: canonical records plus one score per record (higher = claim judged
correct). For a case and claim type, d = u(s) - u(s_prime). d > 0 prefers s.
Ties (d == 0) count as failures everywhere.

Rule tier: decisions -> summarise / bootstrap_ci / paired_diff (unchanged signatures),
plus paired_test (p-value), macro, nearmiss_table, step_revisions, mr_threshold /
missing_rejection, crossed_accuracy (xr_v1), seed_table, holm.
Generic: cluster_bootstrap / paired_cluster_bootstrap over any items and clusters
(rules, families, patients), classification metrics (prf) for clinical sets.
"""
from __future__ import annotations

import collections
import math
import random


def decisions(records, scores, claim_type="conclusion"):
    """-> {tid: {"rid","nm_kind","tier","level","family", "d": {case_kind: d}}}"""
    T = {}
    for r, u in zip(records, scores):
        if r["claim_type"] != claim_type:
            continue
        t = T.setdefault(r["tid"], {k: r[k] for k in ("rid", "nm_kind", "tier", "level", "family")} | {"u": {}})
        t["u"].setdefault(r["case_kind"], {})[r["claim_role"]] = u
    for t in T.values():
        t["d"] = {k: v["s"] - v["s_prime"] for k, v in t["u"].items() if len(v) == 2}
    return T


def _flags(t):
    d = t["d"]
    need = ("base", "flip", "near")
    if any(k not in d for k in need):
        return None
    rev = d["base"] > 0 and d["flip"] < 0
    hold = d["near"] > 0
    out = {"Rev": rev, "Hold": hold, "TA": rev and hold, "BaseAcc": d["base"] > 0,
           "Tie": any(d[k] == 0 for k in need)}
    if "pres" in d:
        out["PresHold"] = d["pres"] > 0
    return out


def summarise(T, by=("nm_kind", "tier", "level", "family")):
    """Percentages over triplets, overall and by each grouping key."""
    acc = collections.defaultdict(lambda: collections.defaultdict(list))
    for t in T.values():
        f = _flags(t)
        if f is None:
            continue
        for key in ["all"] + [f"{b}={t[b]}" for b in by]:
            for m, v in f.items():
                acc[key][m].append(v)
    return {key: {m: 100.0 * sum(v) / len(v) for m, v in ms.items()} | {"n": len(ms["TA"])}
            for key, ms in acc.items()}


def bootstrap_ci(T, metric="TA", unit="rid", B=1000, seed=0, alpha=0.05):
    """Percentile CI, resampling whole rules (triplets of a rule stay together)."""
    groups = collections.defaultdict(list)
    for t in T.values():
        f = _flags(t)
        if f is not None and metric in f:
            groups[t[unit]].append(f[metric])
    keys, rng, stats = sorted(groups, key=str), random.Random(seed), []   # sorted: reproducible across processes
    for _ in range(B):
        vals = [v for k in (rng.choice(keys) for _ in keys) for v in groups[k]]
        stats.append(100.0 * sum(vals) / len(vals))
    stats.sort()
    return stats[int(B * alpha / 2)], stats[int(B * (1 - alpha / 2)) - 1]


def paired_diff(Ta, Tb, metric="TA", unit="rid", B=1000, seed=0, alpha=0.05):
    """Difference a - b on the same triplets, same resampled rules. -> (diff, lo, hi)"""
    groups = collections.defaultdict(list)
    for tid in sorted(Ta.keys() & Tb.keys()):   # sorted: a set's order changes with PYTHONHASHSEED
        fa, fb = _flags(Ta[tid]), _flags(Tb[tid])
        if fa is not None and fb is not None:
            groups[Ta[tid][unit]].append((fa[metric], fb[metric]))
    keys, rng, stats = sorted(groups, key=str), random.Random(seed), []
    point = [p for k in keys for p in groups[k]]
    diff = 100.0 * (sum(a for a, _ in point) - sum(b for _, b in point)) / len(point)
    for _ in range(B):
        vals = [p for k in (rng.choice(keys) for _ in keys) for p in groups[k]]
        stats.append(100.0 * (sum(a for a, _ in vals) - sum(b for _, b in vals)) / len(vals))
    stats.sort()
    return diff, stats[int(B * alpha / 2)], stats[int(B * (1 - alpha / 2)) - 1]


# ---------------------------------------------------------------- generic bootstrap

def _unit_fn(unit):
    return unit if callable(unit) else (lambda t: t[unit])


def _pct(stats, alpha):
    s, B = sorted(stats), len(stats)
    return s[int(B * alpha / 2)], s[int(B * (1 - alpha / 2)) - 1]


def cluster_bootstrap(items, unit, stat, B=1000, seed=0, alpha=0.05):
    """Percentile CI of stat(list of items), resampling whole clusters with replacement
    (all items of a drawn cluster enter together). unit: item key or callable.
    -> (point, lo, hi). Resamples on which stat raises ZeroDivisionError are skipped."""
    groups = collections.defaultdict(list)
    for it in items:
        groups[_unit_fn(unit)(it)].append(it)
    keys, rng, stats = sorted(groups, key=str), random.Random(seed), []
    for _ in range(B):
        try:
            stats.append(stat([x for k in (rng.choice(keys) for _ in keys) for x in groups[k]]))
        except ZeroDivisionError:
            pass
    return (stat(items), *_pct(stats, alpha))


def paired_cluster_bootstrap(items, unit, stat_a, stat_b, B=1000, seed=0, alpha=0.05):
    """stat_a(items) - stat_b(items) on the same items and the same resampled clusters.
    -> {"diff", "lo", "hi", "p", "B"}; p = two-sided bootstrap p-value
    2 * min(P*(diff <= 0), P*(diff >= 0)), capped at 1."""
    groups = collections.defaultdict(list)
    for it in items:
        groups[_unit_fn(unit)(it)].append(it)
    keys, rng, stats = sorted(groups, key=str), random.Random(seed), []
    for _ in range(B):
        res = [x for k in (rng.choice(keys) for _ in keys) for x in groups[k]]
        try:
            stats.append(stat_a(res) - stat_b(res))
        except ZeroDivisionError:
            pass
    lo, hi = _pct(stats, alpha)
    p = min(1.0, 2 * min(sum(s <= 0 for s in stats), sum(s >= 0 for s in stats)) / len(stats))
    return {"diff": stat_a(items) - stat_b(items), "lo": lo, "hi": hi, "p": p, "B": len(stats),
            "n_items": len(items), "n_clusters": len(keys)}


def paired_test(Ta, Tb, metric="TA", unit="rid", B=1000, seed=0, alpha=0.05):
    """paired_diff with a two-sided bootstrap p-value: -> (diff, lo, hi, p). unit = "rid",
    "family" or a callable on a triplet; triplets complete in both runs only, each kept whole
    inside its resampled cluster. Same resampling as paired_diff, so diff/lo/hi agree with it."""
    items = []
    for tid in sorted(Ta.keys() & Tb.keys()):
        fa, fb = _flags(Ta[tid]), _flags(Tb[tid])
        if fa is not None and fb is not None and metric in fa and metric in fb:
            items.append({"u": _unit_fn(unit)(Ta[tid]), "a": fa[metric], "b": fb[metric]})
    mean = lambda key: (lambda xs: 100.0 * sum(x[key] for x in xs) / len(xs))
    r = paired_cluster_bootstrap(items, "u", mean("a"), mean("b"), B, seed, alpha)
    return r["diff"], r["lo"], r["hi"], r["p"]


def holm(pvals):
    """Holm step-down adjusted p-values, in the input's shape: list -> list, {name: p} -> {name: p_adj}.
    Reject a hypothesis at level alpha iff its adjusted p <= alpha."""
    named = dict(pvals) if isinstance(pvals, dict) else dict(enumerate(pvals))
    order = sorted(named, key=lambda k: named[k])
    m, adj, running = len(order), {}, 0.0
    for i, k in enumerate(order):
        running = max(running, min(1.0, (m - i) * named[k]))
        adj[k] = running
    return adj if isinstance(pvals, dict) else [adj[i] for i in range(len(pvals))]


# ---------------------------------------------------------------- rule-tier extensions

def macro(T, metric="TA", over="rid"):
    """Macro-average of a triplet metric over rules (over='rid') or signature classes
    (over='family'): mean of the per-group percentages. -> {"macro", "n_groups", "by": {g: pct}}"""
    groups = collections.defaultdict(list)
    for t in T.values():
        f = _flags(t)
        if f is not None and metric in f:
            groups[t[over]].append(f[metric])
    by = {g: 100.0 * sum(v) / len(v) for g, v in groups.items()}
    return {"macro": sum(by.values()) / len(by) if by else None, "n_groups": len(by), "by": by}


def _decision(d):
    return "s" if d > 0 else ("s_prime" if d < 0 else "tie")


def nearmiss_table(T, by="nm_kind"):
    """Near-miss decisions per kind (and 'all'): denominators, same decision on base and
    near-miss, both correct, near-miss correct given a correct base, and unnecessary
    reversal (near-miss decision opposite to a correct base decision)."""
    acc = collections.defaultdict(lambda: collections.Counter())
    for t in T.values():
        d = t["d"]
        if "base" not in d or "near" not in d:
            continue
        for key in ("all", f"{by}={t[by]}"):
            c = acc[key]
            c["n"] += 1
            c["same"] += _decision(d["base"]) == _decision(d["near"])
            c["both"] += d["base"] > 0 and d["near"] > 0
            if d["base"] > 0:
                c["n_base_correct"] += 1
                c["near_given_base"] += d["near"] > 0
                c["ur"] += d["near"] < 0
                c["tie_given_base"] += d["near"] == 0
    pct = lambda a, b: 100.0 * a / b if b else None
    return {k: {"n": c["n"], "SameDecision": pct(c["same"], c["n"]), "BothCorrect": pct(c["both"], c["n"]),
                "n_base_correct": c["n_base_correct"],
                "NearGivenBase": pct(c["near_given_base"], c["n_base_correct"]),
                "UnnecessaryReversal": pct(c["ur"], c["n_base_correct"]),
                "TieGivenBase": pct(c["tie_given_base"], c["n_base_correct"])} for k, c in acc.items()}


def step_revisions(records, scores, claim_types=("applicability", "criterion", "conclusion")):
    """Per claim type, base against each edited case (flip, near, pres) of a group:
    CorrectRevision = share of claim pairs whose correct claim changes between base and edit
    that are judged right on both; UnnecessaryRevision = share of pairs whose correct claim
    does not change but whose decision does. Pairs without a correct claim (both labels 0)
    are skipped."""
    lab, dd = {}, {}
    for r, u in zip(records, scores):
        k = (r["claim_type"], r["tid"], r["case_kind"])
        lab.setdefault(k, {})[r["claim_role"]] = r["label"]
        dd.setdefault(k, {})[r["claim_role"]] = u
    out = {}
    for ct in claim_types:
        ch = un = ch_ok = un_rev = 0
        for (c, tid, kind), L in lab.items():
            if c != ct or kind != "base" or len(L) != 2:
                continue
            yb = L["s"] - L["s_prime"]
            if yb == 0:
                continue
            db = dd[(c, tid, kind)]["s"] - dd[(c, tid, kind)]["s_prime"]
            for e in ("flip", "near", "pres"):
                Le = lab.get((c, tid, e))
                if not Le or len(Le) != 2 or Le["s"] == Le["s_prime"]:
                    continue
                ye = Le["s"] - Le["s_prime"]
                de = dd[(c, tid, e)]["s"] - dd[(c, tid, e)]["s_prime"]
                if ye != yb:
                    ch += 1
                    ch_ok += db * yb > 0 and de * ye > 0
                else:
                    un += 1
                    un_rev += _decision(db) != _decision(de)
        if ch or un:
            out[ct] = {"CorrectRevision": 100.0 * ch_ok / ch if ch else None, "n_changed": ch,
                       "UnnecessaryRevision": 100.0 * un_rev / un if un else None, "n_unchanged": un}
    return out


def mr_threshold(dev_records, dev_scores, fr=0.05):
    """Acceptance threshold that rejects a share fr of the supported (label 1) conclusion
    claims of the ordinary (non-missing) cases of a development set (rule_v1/dev_missing):
    tau = sorted(u)[int(fr * n)]; a claim is accepted iff u >= tau."""
    sup = sorted(u for r, u in zip(dev_records, dev_scores)
                 if r["claim_type"] == "conclusion" and r["case_kind"] != "missing" and r["label"] == 1)
    if not sup:
        raise ValueError("no supported conclusion claims in the development set")
    return sup[int(fr * len(sup))]


def missing_rejection(records, scores, tau):
    """MR = share of missing twins whose two conclusion claims are both rejected (u < tau);
    FR = share of supported conclusion claims of ordinary cases rejected on this set."""
    both, sup = collections.defaultdict(list), []
    for r, u in zip(records, scores):
        if r["claim_type"] != "conclusion":
            continue
        if r["case_kind"] == "missing":
            both[r["tid"]].append(u < tau)
        elif r["label"] == 1:
            sup.append(u < tau)
    vals = [all(v) for v in both.values() if len(v) == 2]
    return {"MR": 100.0 * sum(vals) / len(vals) if vals else None, "n_missing": len(vals),
            "FR": 100.0 * sum(sup) / len(sup) if sup else None, "n_supported": len(sup), "threshold": tau}


def judgments(records, scores, claim_type="conclusion"):
    """One judgment per (tid, case_kind) with both claims: d = u(s) - u(s_prime) and the
    correct sign y (+1 if only s is correct, -1 if only s_prime, 0 if neither)."""
    J = {}
    for r, u in zip(records, scores):
        if r["claim_type"] != claim_type:
            continue
        j = J.setdefault((r["tid"], r["case_kind"]), {"rec": r, "u": {}, "label": {}})
        j["u"][r["claim_role"]], j["label"][r["claim_role"]] = u, r["label"]
    out = {}
    for k, j in J.items():
        if len(j["u"]) == 2:
            out[k] = {"d": j["u"]["s"] - j["u"]["s_prime"], "y": j["label"]["s"] - j["label"]["s_prime"],
                      "rec": j["rec"]}
    return out


def crossed_accuracy(records, scores, item_of=lambda r: r["meta"]["xr"]["item"], claim_type="conclusion",
                     cells=6, by="nm_kind", exclude=(), partial=False):
    """XA for rule-side items (xr_v1, A's records: meta.xr.item, nm_kind = dimension): an item
    (two rules x three cases) is solved iff every one of its `cells` judgments has d of the sign
    of the program label (ties fail; an unparsable answer must arrive as a tie, never dropped);
    also per dimension and per-judgment accuracy. exclude: item ids left out (A's
    data/xr_v1/KNOWN_ISSUES.json). An item with fewer judgments raises, unless partial=True,
    which leaves it out and reports n_incomplete. Agrees with A's selrm.xr.crossed_accuracy."""
    items, oks, dims, skipped = collections.defaultdict(list), [], {}, 0
    for j in judgments(records, scores, claim_type).values():
        k = item_of(j["rec"])
        if k in exclude:
            continue
        if j["y"] == 0:
            skipped += 1
            continue
        items[k].append(j["d"] * j["y"] > 0)
        dims[k] = j["rec"].get(by)
    incomplete = [k for k, v in items.items() if len(v) != cells]
    if incomplete and not partial:
        raise ValueError(f"{len(incomplete)} items lack some of their {cells} judgments, e.g. {incomplete[:3]}")
    solved = {k: all(v) for k, v in items.items() if len(v) == cells}
    oks = [ok for k in solved for ok in items[k]]
    pct = lambda xs: 100.0 * sum(xs) / len(xs) if xs else None
    per = collections.defaultdict(list)
    for k, s in solved.items():
        per[dims[k]].append(s)
    return {"XA": pct(list(solved.values())), "n_items": len(solved), "n_incomplete": len(incomplete),
            "n_excluded": len(set(exclude)), "CellAcc": pct(oks), "n_cells": len(oks), "cells_without_label": skipped,
            **{f"XA_{d}": pct(v) for d, v in sorted(per.items(), key=lambda x: str(x[0]))}}


def seed_table(values):
    """values: {seed: number}. -> {"seeds": {...}, "mean", "sd" (n-1), "n"}"""
    v = [x for x in values.values() if x is not None]
    m = sum(v) / len(v) if v else None
    sd = math.sqrt(sum((x - m) ** 2 for x in v) / (len(v) - 1)) if len(v) > 1 else None
    return {"seeds": dict(sorted(values.items())), "mean": m, "sd": sd, "n": len(v)}


# ---------------------------------------------------------------- classification (clinical sets)

def prf(gold, pred, labels=None):
    """Accuracy, macro-F1 over `labels` (default: gold labels), per-class precision, recall,
    F1 and support, and the confusion matrix {gold: {pred: n}}. A class with no prediction
    has precision 0; F1 of a class is 0 when precision + recall = 0."""
    labels = list(labels) if labels is not None else sorted(set(gold))
    if not gold:
        raise ZeroDivisionError("no items")
    conf = {g: collections.Counter() for g in labels}
    for g, p in zip(gold, pred):
        conf.setdefault(g, collections.Counter())[p] += 1
    per = {}
    for c in labels:
        tp = conf.get(c, {}).get(c, 0)
        npred = sum(conf[g].get(c, 0) for g in conf)
        ngold = sum(conf.get(c, {}).values())
        P = tp / npred if npred else 0.0
        R = tp / ngold if ngold else 0.0
        per[c] = {"P": 100 * P, "R": 100 * R, "F1": 100 * (2 * P * R / (P + R) if P + R else 0.0), "n": ngold}
    return {"acc": 100.0 * sum(g == p for g, p in zip(gold, pred)) / len(gold),
            "macroF1": sum(per[c]["F1"] for c in labels) / len(labels), "per_class": per,
            "confusion": {g: dict(c) for g, c in conf.items()}, "n": len(gold)}
