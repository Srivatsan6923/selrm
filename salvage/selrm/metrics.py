"""Metrics (project spec, "Frozen decisions"): Rev, Hold, TA, PresHold, TieRate,
BaseAcc and unnecessary revision, with 95% bootstrap CIs over rules, and
paired bootstrap differences between two systems.

A row is one scored (triplet, claim type): {"tid", "rule", "family", "heldout",
"kind", "nm_kind", "tier", "claim", "d"}, where d maps base/flip/near/pres to a
score difference: d > 0 prefers s, d < 0 prefers s', and d == 0 is a tie,
which fails whichever sign is required. Only the flip changes labels, so
correct revision (label changes, judged right on both sides) equals Rev.
"""
import random
from collections import defaultdict

from selrm.rules import HELDOUT_FAMILIES, RULES_BY_ID


def _sign(x):
    return (x > 0) - (x < 0)


STATS = {
    "rev": lambda d: d["base"] > 0 and d["flip"] < 0,
    "hold": lambda d: d["near"] > 0,
    "ta": lambda d: d["base"] > 0 and d["flip"] < 0 and d["near"] > 0,
    "pres_hold": lambda d: d["pres"] > 0,
    "ties": lambda d: sum(v == 0 for v in d.values()) / len(d),       # share of tied cases
    "base_acc": lambda d: d["base"] > 0,
    # label-preserving edits (near-miss, presentation) whose decision differs from base
    "unnecessary_revision": lambda d: ((_sign(d["near"]) != _sign(d["base"])) +
                                       (_sign(d["pres"]) != _sign(d["base"]))) / 2,
}


def row(t, d, claim="conclusion"):
    rule = RULES_BY_ID[t["rule"]]
    return {"tid": t["tid"], "rule": rule.rid, "family": rule.family,
            "heldout": rule.family in HELDOUT_FAMILIES, "kind": rule.crit(t["criterion"]).kind,
            "nm_kind": t["nm_kind"], "tier": t["tier"], "claim": claim, "d": d}


def _draws(rules, boot, seed):
    rng = random.Random(seed)
    return [[rng.choice(rules) for _ in rules] for _ in range(boot)]


def _ci(values, boot):
    values = sorted(values)
    return values[int(0.025 * boot)], values[min(boot - 1, int(0.975 * boot))]


def summarize(rows, boot=1000, seed=0):
    """{"n": n, stat: (percent, ci_low, ci_high)}; the CI resamples rules with
    replacement and keeps all rows of each drawn rule."""
    by_rule = defaultdict(list)
    for r in rows:
        by_rule[r["rule"]].append(r)
    if not by_rule:
        return {"n": 0}
    rules = sorted(by_rule)
    draws = _draws(rules, boot, seed)
    out = {"n": len(rows)}
    for name, f in STATS.items():
        tot = {rid: (sum(f(r["d"]) for r in rs), len(rs)) for rid, rs in by_rule.items()}

        def pct(ids):
            return 100 * sum(tot[i][0] for i in ids) / sum(tot[i][1] for i in ids)

        out[name] = (pct(rules), *_ci([pct(ids) for ids in draws], boot))
    return out


def breakdown(rows, key, **kw):
    """summarize() per value of key (e.g. "nm_kind", "tier", "claim", "heldout")."""
    groups = defaultdict(list)
    for r in rows:
        groups[r[key]].append(r)
    return {g: summarize(rs, **kw) for g, rs in sorted(groups.items(), key=lambda x: str(x[0]))}


def paired(rows_a, rows_b, stat="ta", boot=1000, seed=0):
    """Difference a - b in points, (diff, ci_low, ci_high): both systems are
    scored on the same (tid, claim) rows and resampled with the same rules."""
    f = STATS[stat]
    b = {(r["tid"], r["claim"]): r for r in rows_b}
    if len(b) != len(rows_a) or any((r["tid"], r["claim"]) not in b for r in rows_a):
        raise ValueError("paired() needs both systems scored on the same rows")
    tot = defaultdict(lambda: [0.0, 0])
    for r in rows_a:
        t = tot[r["rule"]]
        t[0] += f(r["d"]) - f(b[(r["tid"], r["claim"])]["d"])
        t[1] += 1
    rules = sorted(tot)

    def diff(ids):
        return 100 * sum(tot[i][0] for i in ids) / sum(tot[i][1] for i in ids)

    return (diff(rules), *_ci([diff(ids) for ids in _draws(rules, boot, seed)], boot))
