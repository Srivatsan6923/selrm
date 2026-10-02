"""Shortcut scorers (project spec, "Shortcut validation"; paper Proposition 1).

A scorer maps (triplet, case, claim type) to d = u(s, x) - u(s', x): d > 0
prefers s, the claim correct on base and near-miss; d < 0 prefers s'; d = 0 is
a tie. Only the oracle depends on the claim type.
"""
import re

from selrm import engine
from selrm.rules import OPS, RULES_BY_ID

_NUM = re.compile(r"\d+(?:\.\d+)?")


def _crit(t):
    return RULES_BY_ID[t["rule"]].crit(t["criterion"])


def always_default(t, case, claim="conclusion"):
    return 1


def concept_named(t, case, claim="conclusion"):
    """Uses the case only through h_k: is the decisive concept named anywhere?"""
    text = case["text"].lower()
    return -1 if any(k in text for k in _crit(t).keywords) else 1


def oracle(t, case, claim="conclusion"):
    """Executes the rule program on the case's serialized state."""
    rule = RULES_BY_ID[t["rule"]]
    state = engine.state_from_json(case["state"])
    return 1 if engine.labels(rule, _crit(t), t["overrides"], state)[claim] == 0 else -1


def naive_number_parser(t, case, claim="conclusion"):
    """First number after the concept's keyword on each line, against the
    stated threshold; fires if any line crosses it. Blind to subject, status
    and time; keeps the default on findings, where there is nothing to parse."""
    c = _crit(t)
    if c.kind != "numeric":
        return 1
    thr = t["overrides"].get(c.cid, c.threshold)
    for line in case["text"].lower().split("\n"):
        ends = [i + len(k) for k in c.keywords if (i := line.find(k)) >= 0]
        if not ends:
            continue
        for n in _NUM.finditer(line, min(ends)):
            if n.group().isdigit() and len(n.group()) == 4 and 1900 <= int(n.group()) <= 2100:
                continue                       # a year, not the value
            if OPS[c.op](float(n.group()), thr):
                return -1
            break
    return 1


SCORERS = {"always_default": always_default, "concept_named": concept_named,
           "oracle": oracle, "naive_number_parser": naive_number_parser}


def score(t, scorer, claim="conclusion"):
    return {k: scorer(t, case, claim) for k, case in t["cases"].items()}
