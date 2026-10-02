"""Shared metric code (owner: C). Everyone imports this; nobody re-implements it.

Input: canonical records plus one score per record (higher = claim judged
correct). For a case and claim type, d = u(s) - u(s_prime). d > 0 prefers s.
Ties (d == 0) count as failures everywhere.
"""
from __future__ import annotations

import collections
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
    keys, rng, stats = list(groups), random.Random(seed), []
    for _ in range(B):
        vals = [v for k in (rng.choice(keys) for _ in keys) for v in groups[k]]
        stats.append(100.0 * sum(vals) / len(vals))
    stats.sort()
    return stats[int(B * alpha / 2)], stats[int(B * (1 - alpha / 2)) - 1]


def paired_diff(Ta, Tb, metric="TA", unit="rid", B=1000, seed=0, alpha=0.05):
    """Difference a - b on the same triplets, same resampled rules. -> (diff, lo, hi)"""
    groups = collections.defaultdict(list)
    for tid in Ta.keys() & Tb.keys():
        fa, fb = _flags(Ta[tid]), _flags(Tb[tid])
        if fa is not None and fb is not None:
            groups[Ta[tid][unit]].append((fa[metric], fb[metric]))
    keys, rng, stats = list(groups), random.Random(seed), []
    point = [p for k in keys for p in groups[k]]
    diff = 100.0 * (sum(a for a, _ in point) - sum(b for _, b in point)) / len(point)
    for _ in range(B):
        vals = [p for k in (rng.choice(keys) for _ in keys) for p in groups[k]]
        stats.append(100.0 * (sum(a for a, _ in vals) - sum(b for _, b in vals)) / len(vals))
    stats.sort()
    return diff, stats[int(B * alpha / 2)], stats[int(B * (1 - alpha / 2)) - 1]
