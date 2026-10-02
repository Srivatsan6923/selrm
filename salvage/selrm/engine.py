"""Triplet engine (project spec, section "Engine").

make_triplet() renders base, flip, near-miss and presentation cases for one
(rule, criterion, near-miss kind, tier, split, seed) with step-level claims
(applicability, criterion, conclusion), a label per claim and the program's
ledger for the criterion under test. A proposal is kept only if check()
passes: labels from executing the rule program, a flip that changes exactly
the target criterion, near-miss and presentation cases that change none, the
keyword pattern behind Proposition 1, keyword-free fillers, one-line edits
between base, flip and near-miss, and ledgers that quote the case.
"""
from __future__ import annotations

import difflib
import random
import re
from collections import Counter
from dataclasses import asdict, replace
from itertools import combinations

from selrm import phrases as P
from selrm.rules import FIRST_DEGREE, OPS, RULES, RULES_BY_ID, Mention

TIERS = ("easy", "long", "superseded", "delabelled", "alt")
CLAIMS = ("applicability", "criterion", "conclusion")
WANT = {"base": 0, "flip": 1, "near": 0, "pres": 0}
NOW = 2026
NO_LINE = 0.3          # share of default findings rendered with no line at all
MAX_TRIES = 50
FILLER_SET = frozenset(P.FILLERS)
ALL_KEYWORDS = frozenset(k for r in RULES for c in r.criteria for k in c.keywords)
OP_WORDS = {"<": "below", "<=": "at or below", ">": "above", ">=": "at or above"}


def cells(rules=RULES):
    """Every valid (rid, cid, nm_kind, tier)."""
    return [(r.rid, c.cid, nm, tier) for r in rules for c in r.criteria if pivots(r, c)
            for nm in c.nm_kinds() for tier in TIERS if _tier_ok(c, nm, tier)]


def _tier_ok(c, nm, tier):
    if tier == "superseded":
        return c.kind == "numeric" and nm == "time"
    if tier == "delabelled":
        return nm == "time" and "delabelled" in P.BANKS.get(c.concept, {})
    if tier == "alt":
        return c.alt_threshold is not None
    return tier in ("easy", "long")


def pivots(rule, crit):
    """Sets of other criteria to hold met so that crit alone decides the
    conclusion (score rules: none; any-rules: the empty set)."""
    if rule.kind == "score":
        return [()]
    w = (lambda c: c.points) if rule.cutoff else (lambda c: 1)
    cut = rule.cutoff or 1
    others = [c for c in rule.criteria if c is not crit]
    return [s for k in range(len(others) + 1) for s in combinations(others, k)
            if sum(map(w, s)) < cut <= sum(map(w, s)) + w(crit)]


def state_from_json(state):
    return tuple(Mention(**m) for m in state)


def fmt(v, crit):
    return f"{v:.{crit.decimals}f}" if crit.decimals else str(int(v))


def with_unit(v, crit):
    unit = P.UNITS[crit.concept]
    return fmt(v, crit) + ("" if unit[0] in "/%" else " ") + unit


def claims(rule, crit, ov):
    """Step-level claim pairs [s, s'], s correct on base and near-miss."""
    if crit.kind == "finding":
        thing = P.NOUN[crit.concept]
    else:
        thr = ov.get(crit.cid, crit.threshold)
        thing = f"{P.NOUN[crit.concept]} {OP_WORDS[crit.op]} {with_unit(thr, crit)}"
    thing = thing[0].upper() + thing[1:] + " reported in the case"
    out = {"applicability": [f"{thing} does not count for this patient under the rule.",
                             f"{thing} counts for this patient under the rule."]}
    if rule.kind == "constraint":    # score rules: criterion and conclusion coincide
        out["criterion"] = [f"The {crit.label} criterion is not met.",
                            f"The {crit.label} criterion is met."]
    out["conclusion"] = list(rule.claims(crit.cid))
    return out


def labels(rule, crit, ov, state):
    """Executed label of each claim pair: 0 if s is correct, 1 if s' is."""
    thr = ov.get(crit.cid, crit.threshold)
    counted = [m for m in state if crit.applies(m) and m.status == "present"
               and (crit.kind == "finding" or OPS[crit.op](m.value, thr))]
    out = {"applicability": int(bool(counted))}
    if rule.kind == "constraint":
        out["criterion"] = int(crit.evaluate(state, thr))
    out["conclusion"] = rule.label(state, crit.cid, ov)
    return out


def ledger_text(entries):
    return "\n".join("; ".join(f"{k}: {e[k]}" for k in ("need", "found", "subject", "status",
                                                          "time")) for e in entries)


def prose(entries):
    """The ledger's facts as free text of about the same length, with no decision."""
    out = []
    for e in entries:
        who = "the patient" if e["subject"] == "patient" else f"the patient's {e['subject']}"
        if e["found"] == "missing":
            out.append(f"For {e['need']}, the case says nothing, so for {who} it is "
                       f"{e['status']} and {e['time']}.")
        else:
            out.append(f"For {e['need']}, the case says \"{e['found']}\", about {who}, as "
                       f"{e['status']} and {e['time']}.")
    return " ".join(out)


def make_triplet(rule, cid, nm_kind, tier, split, seed, stats=None):
    """One triplet as a JSON-ready dict; resamples until check() passes.

    stats, if given, is a Counter that collects proposals and reject reasons.
    """
    rule = RULES_BY_ID[rule] if isinstance(rule, str) else rule
    if (rule.rid, cid, nm_kind, tier) not in cells([rule]):
        raise ValueError(f"invalid cell {(rule.rid, cid, nm_kind, tier)}")
    tid = f"{rule.rid}.{cid}.{nm_kind}.{tier}.{split}.{seed}"
    rng = random.Random(tid)
    for _ in range(MAX_TRIES):
        try:
            t = {"tid": tid, **_propose(rule, rule.crit(cid), nm_kind, tier, split, rng)}
            errors = check(t)
        except ValueError as e:      # a draw had no admissible value, or a label raised
            errors = [f"draw: {e}"]
        if stats is not None:
            stats["proposed"] += 1
            if errors:
                stats["rejected"] += 1
                stats.update("reject " + e.split(":")[0] for e in errors)
        if not errors:
            return t
    raise RuntimeError(f"{tid}: no valid triplet in {MAX_TRIES} tries; last: {errors}")


def _draw(rng, c, lo, hi, ok):
    for _ in range(100):
        v = round(rng.uniform(lo, hi), c.decimals) if c.decimals else rng.randint(int(lo), int(hi))
        if ok(v):
            return v
    raise ValueError(f"{c.cid}: no admissible value in [{lo}, {hi}]")


def _propose(rule, crit, nm_kind, tier, split, rng):
    ov = {crit.cid: crit.alt_threshold} if tier == "alt" else {}
    thr = ov.get(crit.cid, crit.threshold)
    sex = rule.sex or rng.choice(("female", "male"))
    poss = "Her" if sex == "female" else "His"
    met = {c.cid for c in rng.choice(pivots(rule, crit))}

    # Values first, so that an age criterion sets the age that years depend on.
    # Other criteria sit at their defaults, or are held met where the rule needs
    # them for the target to decide (cutoff families).
    vals = {}
    for c in rule.criteria:
        if c.kind == "numeric" and c is not crit:
            op = OPS[c.op]
            lo_hi, ok = ((c.flip_range, lambda v: op(v, c.threshold)) if c.cid in met else
                         (c.default_range, lambda v: not op(v, c.threshold)))
            vals[c.cid] = _draw(rng, c, *lo_hi, ok)
    if crit.kind == "numeric":
        op = OPS[crit.op]
        if nm_kind == "numeric":
            near_v = _draw(rng, crit, thr - crit.near_delta, thr + crit.near_delta,
                           lambda v: not op(v, thr))
            base_v = _draw(rng, crit, *crit.default_range,
                           lambda v: not op(v, thr) and abs(v - thr) > abs(near_v - thr))
        else:                # time: a flip-side value at a time the criterion ignores
            base_v = _draw(rng, crit, *crit.default_range, lambda v: not op(v, thr))
            past_v = _draw(rng, crit, *crit.flip_range, lambda v: op(v, thr))
        if tier == "alt":    # flip where the original threshold gives the other answer
            orig = crit.threshold
            flip_v = _draw(rng, crit, min(thr, orig), max(thr, orig),
                           lambda v: op(v, thr) and not op(v, orig))
        else:
            flip_v = _draw(rng, crit, *crit.flip_range, lambda v: op(v, thr))
        vals[crit.cid] = base_v
    age = next((vals[c.cid] for c in rule.criteria if c.concept == "age"), None) \
        or rng.randint(*rule.age_range)

    def pick(options, avoid=None):
        options = P.by_split(options, split)
        return rng.choice([o for o in options if o != avoid] or options)

    def line(c, form, value=True, subject="patient"):
        tpl = pick(P.BANKS[c.concept][form])
        status, time = P.FORMS[form]
        year = (rng.randint(max(2005, min(NOW - 2, NOW - age + 18)), NOW - 2)
                if "{year}" in tpl else None)
        return Mention(c.concept, c.kind, value, subject, status, time, form, year), tpl

    def rel_form(c):
        return ("rel_past" if c.counts_past and "rel_past" in P.BANKS[c.concept]
                and rng.random() < 0.5 else "rel")

    def counting(c):
        """A finding mention that the criterion counts: the patient now, or the
        past or a first-degree relative where the predicate counts those."""
        way = rng.choice(["patient"] + ["past"] * c.counts_past + ["family"] * c.counts_family)
        if way == "family":
            kin = [p for p in P.persons(c.concept, split, age) if p in FIRST_DEGREE]
            return line(c, rel_form(c), subject=rng.choice(kin))
        return line(c, "present" if way == "patient" else "past")

    # 1. Context: the other criteria, fillers; shuffled once, shared by base/flip/near.
    body = []
    for c in rule.criteria:
        if c is crit:
            continue
        if c.kind == "numeric":
            body.append(line(c, "current", vals[c.cid]))
        elif c.cid in met:
            body.append(counting(c))
        elif rng.random() >= NO_LINE:
            body.append(line(c, "generic"))
    n_fill = rng.randint(15, 20) if tier == "long" else rng.randint(1, 4)
    body += [(None, f) for f in rng.sample(P.by_split(P.FILLERS, split), n_fill)]
    rng.shuffle(body)

    # 2. Target: base, flip and near-miss lines (extra = a line added to base).
    extra = None
    if crit.kind == "numeric":
        base = line(crit, "current", base_v)
        flip = (replace(base[0], value=flip_v), base[1])
        if nm_kind == "numeric":
            near = (replace(base[0], value=near_v), base[1])
        else:
            near, extra = base, line(crit, "superseded" if tier == "superseded" else "past", past_v)
    else:
        base = None if rng.random() < NO_LINE else line(crit, "generic")
        flip = counting(crit)
        near = base
        if nm_kind == "negation":
            near = line(crit, "absent")
        elif nm_kind == "subject":
            others = [p for p in P.persons(crit.concept, split, age)
                      if not (crit.counts_family and p in FIRST_DEGREE)]
            extra = line(crit, rel_form(crit), subject=rng.choice(others))
        else:                # time
            extra = line(crit, "delabelled" if tier == "delabelled" else "past")

    p = rng.randint(0, len(body))
    q = rng.randint(0, len(body) + (base is not None))

    def lines_with(target, add=None):
        ls = body[:p] + ([target] if target else []) + body[p:]
        if add:
            ls.insert(q, add)
        return ls

    # 3. Presentation edit: the base state with other templates, header and order.
    frames = P.HEADER_NO_AGE if any(c.concept == "age" for c in rule.criteria) else P.HEADER
    hdr = pick(frames)
    def repick(m, tpl):      # another template of the form that shows the same fields
        opts = [o for o in P.by_split(P.BANKS[m.concept][m.form], split)
                if o != tpl and ("{year}" in o) == ("{year}" in tpl)]
        return rng.choice(opts) if opts else tpl

    base_ls = lines_with(base)
    pres_ls = [(m, repick(m, tpl) if m else tpl) for m, tpl in base_ls]
    rng.shuffle(pres_ls)
    cases = {"base": (hdr, base_ls), "flip": (hdr, lines_with(flip)),
             "near": (hdr, lines_with(near, extra)), "pres": (pick(frames, avoid=hdr), pres_ls)}

    by_concept = {c.concept: c for c in rule.criteria}
    noun = "woman" if sex == "female" else "man"

    def say(m, tpl):
        if m is None:
            return tpl
        kw = {"Poss": poss, "rel": m.subject, "year": m.year}
        if m.kind == "numeric":
            kw.update(v=fmt(m.value, by_concept[m.concept]), dia=round(0.6 * m.value + 4))
        return tpl.format(**kw)

    def case(frame, ls):
        head = frame.format(age=age, noun=noun, Noun=noun.capitalize(), sex=sex,
                            Sex=sex.capitalize())
        state = [m for m, _ in ls if m]
        entries = [{"need": crit.label,
                    "found": with_unit(m.value, crit) if m.kind == "numeric" else say(m, tpl),
                    "subject": m.subject, "status": m.status, "time": m.time}
                   for m, tpl in ls if m and m.concept == crit.concept]
        return {"text": "\n".join([head, rule.setting] + [say(m, tpl) for m, tpl in ls]),
                "labels": labels(rule, crit, ov, state),
                "state": [asdict(m) for m in state],
                "ledger": entries or [{"need": crit.label, "found": "missing", "subject": "patient",
                                       "status": "absent", "time": "current"}]}

    return {"rule": rule.rid, "family": rule.family, "criterion": crit.cid, "nm_kind": nm_kind,
            "tier": tier, "split": split, "rule_text": rule.rule_text(ov),
            "claims": claims(rule, crit, ov), "overrides": ov,
            "cases": {k: case(*v) for k, v in cases.items()}}


def check(t):
    """Invariant violations of one triplet ([] if none)."""
    rule = RULES_BY_ID[t["rule"]]
    crit = rule.crit(t["criterion"])
    ov, cases = t["overrides"], t["cases"]
    errs, ev = [], {}
    kinds = [k for k in CLAIMS if k != "criterion" or rule.kind == "constraint"]
    if list(t["claims"]) != kinds or any(len(set(t["claims"][k])) != 2 for k in kinds):
        errs.append(f"claims: want two distinct claims for each of {kinds}")
    for k, want in WANT.items():
        ms = state_from_json(cases[k]["state"])
        try:
            got = labels(rule, crit, ov, ms)
            ev[k] = [c.evaluate(ms, ov.get(c.cid)) for c in rule.criteria]
        except ValueError as e:
            errs.append(f"state: {k}: {e}")
            continue
        if got != dict.fromkeys(kinds, want) or cases[k]["labels"] != got:
            errs.append(f"label: {k} executes to {got}, stored {cases[k]['labels']}, want {want}")
    if len(ev) == len(WANT):
        changed = [c.cid for c, a, b in zip(rule.criteria, ev["base"], ev["flip"]) if a != b]
        if changed != [crit.cid]:
            errs.append(f"flip: changes {changed}, want [{crit.cid}]")
        errs += [f"{k}: changes a criterion" for k in ("near", "pres") if ev[k] != ev["base"]]
    for k in WANT:   # findings: named in flip and near only; numerics: everywhere
        named = any(kw in cases[k]["text"].lower() for kw in crit.keywords)
        if named != (crit.kind == "numeric" or k in ("flip", "near")):
            errs.append(f"keyword: {k} {'names' if named else 'does not name'} {crit.concept}")
    lines = {k: c["text"].split("\n") for k, c in cases.items()}
    for k, ls in lines.items():
        if any(s in FILLER_SET and any(kw in s.lower() for kw in ALL_KEYWORDS) for s in ls):
            errs.append(f"filler: {k} has a keyword line")
        entries = cases[k]["ledger"]
        mentions = [m for m in state_from_json(cases[k]["state"]) if m.concept == crit.concept]
        if not 1 <= len(entries) <= 3 or len(entries) != max(1, len(mentions)):
            errs.append(f"ledger: {k} has {len(entries)} entries for {len(mentions)} mentions")
        for e in entries:   # findings quote a whole line; numerics give the value shown
            found = e["found"] if crit.kind == "finding" else re.match(r"[\d.]+", e["found"])[0]
            if e["found"] != "missing" and found not in (ls if crit.kind == "finding"
                                                         else cases[k]["text"]):
                errs.append(f"ledger: {k} quotes {e['found']!r}, not in the case")
    for k in ("flip", "near"):
        removed, added = _edit(lines["base"], lines[k])
        additive = k == "near" and t["nm_kind"] in ("subject", "time")
        if added != 1 or removed > (0 if additive else 1):
            errs.append(f"edit: {k} removes {removed} and adds {added} lines")
    if cases["pres"]["text"] == cases["base"]["text"]:
        errs.append("pres: same text as base")
    if Counter(state_from_json(cases["pres"]["state"])) != Counter(state_from_json(cases["base"]["state"])):
        errs.append("pres: state differs from base")
    return errs


def _edit(a, b):
    """(lines removed, lines added) going from a to b."""
    ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
    return (sum(i2 - i1 for tag, i1, i2, _, _ in ops if tag != "equal"),
            sum(j2 - j1 for tag, _, _, j1, j2 in ops if tag != "equal"))
