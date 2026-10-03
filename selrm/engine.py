"""Triplet engine (A-D0): canonical instance records (docs/INTERFACES.md section 1).

make_group(rule, cid, nm_kind, tier, split, seed) renders base, flip, near
and pres cases (and, on request, the missing twin) for one target criterion
and returns one record per (case, claim type, claim role). A proposal is kept only if check() passes: labels
from executing the rule program, a flip that changes exactly the target
criterion, near-miss and presentation cases that change none, the keyword
pattern behind Proposition 1, keyword-free fillers, one-line edits between
base, flip and near-miss, presentation state equal to base, and ledgers that
quote the case. Rejections are counted per reason in `stats`.

Missing twin: the base case with the decisive input unknown. A measured input
is dropped; a finding gets an explicit "not recorded" line in place of its
base line (history items are absent when omitted). Both claims are labelled 0,
and enumerating completions of the input (the base and the flip mention) must
reach both outcomes of every claim type. It is drawn from its own random
stream, so requesting it leaves the other cases unchanged.
"""
from __future__ import annotations

import difflib
import random
from collections import Counter
from dataclasses import asdict, replace
from itertools import combinations

from selrm import phrases as P
from selrm.library import LIBRARY, LIBRARY_BY_ID
from selrm.rules import FIRST_DEGREE, OPS, Mention
from selrm.schema import validate
from selrm.smoke import ledger_to_prose

TIERS = ("easy", "long", "superseded", "delabelled", "alt")
WANT = {"base": 0, "flip": 1, "near": 0, "pres": 0}
NOW = 2026
NO_LINE = 0.3          # share of default findings rendered with no line at all
MAX_TRIES = 50
OPW = {"<": "below", "<=": "at or below", ">": "above", ">=": "at least"}
ALL_KEYWORDS = frozenset(k for r in LIBRARY for c in r.criteria for k in c.keywords)


def nm_kinds(c):
    """Criterion.nm_kinds() plus `boundary` (a value exactly at a strict threshold)."""
    kinds = c.nm_kinds()
    if c.kind == "numeric" and c.op in ("<", ">") and "numeric" in kinds:
        kinds = kinds + ["boundary"]
    return kinds


def cells(rules=LIBRARY):
    """Every valid (rid, cid, nm_kind, tier)."""
    return [(r.rid, c.cid, nm, tier) for r in rules for c in r.criteria if pivots(r, c)
            for nm in nm_kinds(c) for tier in TIERS if _tier_ok(c, nm, tier)]


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
    def w(c):
        return c.points if rule.logic == "atleast" else 1
    cut = {"any": 1, "all": len(rule.criteria), "atleast": rule.cutoff}[rule.logic]
    others = [c for c in rule.criteria if c is not crit]
    return [s for k in range(len(others) + 1) for s in combinations(others, k)
            if sum(map(w, s)) < cut <= sum(map(w, s)) + w(crit)]


def _steps(x, c):
    """x in units of the criterion's last decimal (exact comparison of rounded values)."""
    return int(round(x * 10 ** c.decimals))


def fmt(v, crit):
    return f"{v:.{crit.decimals}f}" if crit.decimals else str(int(v))


def condition_text(c, thr=None):
    if c.kind == "finding":
        return c.label
    return f"{c.label} {OPW[c.op]} {fmt(c.threshold if thr is None else thr, c)}"


def claim_pairs(rule, c, thr):
    pairs = {"conclusion": rule.claims(c.cid)}
    if rule.kind == "constraint":
        cond = condition_text(c, thr)
        pairs["criterion"] = (f"Under the rule, the condition \"{cond}\" does not hold for this patient.",
                              f"Under the rule, the condition \"{cond}\" holds for this patient.")
    return pairs


def case_labels(rule, c, ov, state):
    """Executed label per claim type: 1 if s' is correct, 0 if s is."""
    out = {"conclusion": rule.label(state, c.cid, ov)}
    if rule.kind == "constraint":
        out["criterion"] = int(c.evaluate(state, ov.get(c.cid)))
    return out


def state_from_json(state):
    return tuple(Mention(**m) for m in state)


def make_group(rule, cid, nm_kind, tier, split, seed, set_name="rule_v1", level="L0",
               stats=None, tpl_split=None, missing=False, readapply=False):
    """Canonical records for one group; resamples until check() passes.
    tpl_split: template split when it differs from the record split (dev uses
    test templates); missing: also emit the missing twin; readapply: also emit
    reading and application pairs where the group admits them."""
    rule = LIBRARY_BY_ID[rule] if isinstance(rule, str) else rule
    if (rule.rid, cid, nm_kind, tier) not in cells([rule]):
        raise ValueError(f"invalid cell {(rule.rid, cid, nm_kind, tier)}")
    tid = f"{set_name}.{split}.{rule.rid}.{cid}.{nm_kind}.{tier}.{seed}"
    rng = random.Random(tid)
    rng_m = random.Random(tid + "/missing") if missing else None
    errors = []
    for _ in range(MAX_TRIES):
        try:
            g = _propose(rule, rule.crit(cid), nm_kind, tier, tpl_split or split, rng, rng_m)
            errors = check(rule, g)
        except ValueError as e:      # a draw had no admissible value, or a label raised
            g, errors = None, [f"draw: {e}"]
        if stats is not None:
            stats["proposed"] += 1
            if errors:
                stats["rejected"] += 1
                stats.update(f"reject {rule.rid} {nm_kind} {e.split(':')[0]}" for e in errors)
        if not errors:
            recs = to_records(rule, g, tid, set_name, split, level, seed, tpl_split or split)
            if readapply:
                recs += readapply_records(rule, g, tid, set_name, split, level, seed, tpl_split or split)
            for r in recs:
                validate(r)
            return recs
    raise RuntimeError(f"{tid}: no valid group in {MAX_TRIES} tries; last: {errors}")


def _draw(rng, c, lo, hi, ok):
    for _ in range(200):
        v = round(rng.uniform(lo, hi), c.decimals) if c.decimals else rng.randint(int(lo), int(hi))
        if ok(v):
            return v
    raise ValueError(f"{c.cid}: no admissible value in [{lo}, {hi}]")


def _propose(rule, crit, nm_kind, tier, split, rng, rng_m=None):
    ov = {crit.cid: crit.alt_threshold} if tier == "alt" else {}
    thr = ov.get(crit.cid, crit.threshold)
    sex = rule.sex or rng.choice(("female", "male"))
    poss = "Her" if sex == "female" else "His"
    met = {c.cid for c in rng.choice(pivots(rule, crit))}

    # Values first, so that an age criterion sets the age that years depend on.
    vals = {}
    for c in rule.criteria:
        if c.kind == "numeric" and c is not crit:
            op = OPS[c.op]
            if c.cid in met:           # context held met: a value just across the threshold
                lo, hi = c.flip_range
                near = (max(lo, c.threshold - 2 * c.near_delta), min(hi, c.threshold)) \
                    if c.op in ("<", "<=") else (max(lo, c.threshold), min(hi, c.threshold + 2 * c.near_delta))
                lo_hi = near if near[0] <= near[1] else c.flip_range
                ok = lambda v, c=c, op=op: op(v, c.threshold)  # noqa: E731
            else:
                lo_hi, ok = c.default_range, lambda v, c=c, op=op: not op(v, c.threshold)
            vals[c.cid] = _draw(rng, c, *lo_hi, ok)
    if crit.kind == "numeric":
        op = OPS[crit.op]

        def close(lo_hi, k=3):         # flip-side values within k near-miss windows of the threshold
            lo, hi = lo_hi
            w = (max(lo, thr - k * crit.near_delta), min(hi, thr)) if crit.op in ("<", "<=") \
                else (max(lo, thr), min(hi, thr + k * crit.near_delta))
            return w if w[0] <= w[1] else lo_hi
        if nm_kind == "numeric":       # strictly inside the window, default side, not at threshold
            near_v = _draw(rng, crit, thr - crit.near_delta, thr + crit.near_delta,
                           lambda v: not op(v, thr)
                           and 0 < _steps(abs(v - thr), crit) < _steps(crit.near_delta, crit))
        elif nm_kind == "boundary":
            near_v = thr
        if nm_kind in ("numeric", "boundary"):
            base_v = _draw(rng, crit, *crit.default_range,
                           lambda v: not op(v, thr) and abs(v - thr) > abs(near_v - thr))
        else:                          # time: a flip-side value at a time the criterion ignores
            clear = lambda v: not op(v, thr) and _steps(abs(v - thr), crit) >= _steps(crit.near_delta, crit)  # noqa: E731
            # a superseded value is recent: today's value within 4 windows of the threshold
            # where the default range reaches that close
            lo, hi = crit.default_range
            if tier == "superseded":
                w = (max(lo, thr + crit.near_delta), min(hi, thr + 4 * crit.near_delta)) \
                    if crit.op in ("<", "<=") else (max(lo, thr - 4 * crit.near_delta), min(hi, thr - crit.near_delta))
                lo, hi = w if w[0] <= w[1] else (lo, hi)
            base_v = _draw(rng, crit, lo, hi, clear)
            past_v = _draw(rng, crit, *close(crit.flip_range), lambda v: op(v, thr))
            old_v = _draw(rng, crit, lo, hi, clear)
        if tier == "alt":              # flip where the original threshold gives the other answer
            orig = crit.threshold
            flip_v = _draw(rng, crit, min(thr, orig), max(thr, orig),
                           lambda v: op(v, thr) and not op(v, orig))
        elif crit.op in (">=", "<=") and rng.random() < 1 / 3:
            flip_v = thr               # an inclusive threshold is met exactly at the stated value
        else:
            flip_v = _draw(rng, crit, *close(crit.flip_range), lambda v: op(v, thr))
        vals[crit.cid] = base_v
    age = next((vals[c.cid] for c in rule.criteria if c.concept == "age"), None) \
        or rng.randint(*rule.age_range)

    # The patient's ages across the group (an age criterion moves it between base
    # and flip): people and years must be plausible for all of them.
    ages = (age, flip_v) if crit.concept == "age" else (age,)

    spouses = [p for p in ("husband", "wife", "partner") if p in P.by_split(P.PERSONS, split)]
    spouse = rng.choice(spouses)       # one spouse word per group

    def people(concept):
        pools = [P.persons(concept, split, a) for a in ages]
        return [p for p in pools[0] if all(p in q for q in pools[1:])
                and (p == spouse or p not in spouses)]

    def year():
        return rng.randint(max(2005, min(NOW - 2, NOW - min(ages) + 18)), NOW - 2)

    def pick(options, avoid=None, same_year=None):
        idx = [i for i in P.ids(options, split) if i != avoid
               and (same_year is None or ("{year}" in options[i]) == same_year)]
        return rng.choice(idx or P.ids(options, split))

    def line(c, form, value=True, subject="patient"):
        i = pick(P.BANKS[c.concept][form])
        status, time = P.FORMS[form]
        y = year() if "{year}" in P.BANKS[c.concept][form][i] else None
        return {"m": Mention(c.concept, c.kind, value, subject, status, time, form, y),
                "tpl": (c.concept, form, i)}

    def rel_form(c):
        return ("rel_past" if c.counts_past and "rel_past" in P.BANKS[c.concept]
                and rng.random() < 0.5 else "rel")

    def counting(c):
        """A finding mention the criterion counts: the patient now, or the past
        or a first-degree relative where the predicate counts those."""
        way = rng.choice(["patient"] + ["past"] * c.counts_past + ["family"] * c.counts_family)
        if way == "family":
            kin = [p for p in people(c.concept) if p in FIRST_DEGREE]
            return line(c, rel_form(c), subject=rng.choice(kin))
        return line(c, "present" if way == "patient" else "past")

    def filler(kind, i):
        return {"filler": kind, "tpl": ("filler", kind, i),
                "who": rng.choice(people(None)) if kind == "other" else None,
                "year": year() if kind == "lab" else None}

    # Concepts present in some case of the group; a generic absence line that could
    # deny one of them (phrases.OVERLAP) is omitted (closed world: absent anyway).
    present = {c.concept for c in rule.criteria if c.kind == "numeric" or c.cid in met} | {crit.concept}

    def quiet(c):
        return any(o != c.concept and o in g for g in P.OVERLAP if c.concept in g for o in present)

    # 1. Context: other criteria at defaults or held met, fillers; one shared order.
    body = []
    for c in rule.criteria:
        if c is crit:
            continue
        if c.kind == "numeric":
            body.append(line(c, "current", vals[c.cid]))
        elif c.cid in met:
            body.append(counting(c))
        elif rng.random() >= NO_LINE and not quiet(c):
            body.append(line(c, "generic"))
    if tier == "long":
        n_other, n_lab = rng.randint(2, 4), rng.randint(2, 4)
        n_neutral = rng.randint(15, 20) - n_other - n_lab
        body += [filler("other", i) for i in rng.sample(P.ids(P.FILLERS_OTHER, split), n_other)]
        body += [filler("lab", i) for i in rng.sample(P.ids(P.FILLERS_LAB, split), n_lab)]
    else:
        n_neutral = rng.randint(1, 4)
    body += [filler("neutral", i) for i in rng.sample(P.ids(P.FILLERS, split), n_neutral)]
    rng.shuffle(body)

    # 2. Target: base, flip and near-miss lines (extra = a line added to base).
    # The flip and the near-miss each replace the same base line (or add one line
    # where the base has none), so every case of a group has the same number of
    # mentions of the concept. Numeric time: base and flip also carry an old
    # default-side value, and the near-miss moves only that old value across.
    old = old_near = None
    if crit.kind == "numeric":
        base = line(crit, "current", base_v)
        flip = dict(base, m=replace(base["m"], value=flip_v))
        if nm_kind in ("numeric", "boundary"):
            near = dict(base, m=replace(base["m"], value=near_v))
        else:
            near = base
            old = line(crit, "superseded" if tier == "superseded" else "past", old_v)
            old_near = dict(old, m=replace(old["m"], value=past_v))
    else:
        base = None if rng.random() < NO_LINE or quiet(crit) else line(crit, "generic")
        flip = counting(crit)
        if nm_kind == "negation":
            near = line(crit, "absent")
        elif nm_kind == "subject":
            others = [p for p in people(crit.concept)
                      if not (crit.counts_family and p in FIRST_DEGREE)]
            form = "rel_past" if flip["m"].time == "past" and "rel_past" in P.BANKS[crit.concept] else "rel"
            near = line(crit, form, subject=rng.choice(others))     # same time as the flip
        else:                          # time
            near = line(crit, "delabelled" if tier == "delabelled" else "past")

    p = rng.randint(0, len(body))
    q = rng.randint(0, len(body) + (base is not None))

    def lines_with(target, add=old):
        ls = body[:p] + ([target] if target else []) + body[p:]
        if add:
            ls.insert(q, add)
        return ls

    # 3. Presentation edit: the base state with other templates, header and order.
    frames = P.HEADER_NO_AGE if any(c.concept == "age" for c in rule.criteria) else P.HEADER
    hdr = pick(frames)
    base_ls = lines_with(base)
    # Meaning-preserving: findings, superseded values and fillers keep their lines
    # (a template states a specific fact); numeric values and dated past values
    # are reworded with the same value and year; header frame and order change.
    pres_ls = []
    for x in base_ls:
        if "m" in x and x["m"].kind == "numeric" and x["m"].form in ("current", "past"):
            bank = P.BANKS[x["m"].concept][x["m"].form]
            i = pick(bank, avoid=x["tpl"][2], same_year="{year}" in bank[x["tpl"][2]])
            pres_ls.append(dict(x, tpl=(x["tpl"][0], x["tpl"][1], i)))
        else:
            pres_ls.append(x)
    order = list(range(len(pres_ls)))
    for _ in range(20):                # a new order whenever there are two lines to swap
        rng.shuffle(order)
        if len(order) < 2 or order != sorted(order):
            break
    pres_ls = [pres_ls[i] for i in order]

    by_concept = {c.concept: c for c in rule.criteria}
    noun = "woman" if sex == "female" else "man"

    def say(x):
        if "filler" in x:
            kind, i = x["filler"], x["tpl"][2]
            bank = {"neutral": P.FILLERS, "other": P.FILLERS_OTHER, "lab": P.FILLERS_LAB}[kind]
            return bank[i].format(Poss=poss, rel=x["who"], year=x["year"])
        m, (concept, form, i) = x["m"], x["tpl"]
        if form == "missing":
            what = by_concept[concept].label
            return P.MISSING[i].format(What=what[0].upper() + what[1:], what=what)
        kw = {"Poss": poss, "rel": m.subject, "year": m.year}
        if m.kind == "numeric":
            kw.update(v=fmt(m.value, by_concept[concept]), dia=round(0.55 * m.value + 15))  # 90 -> 64
        return P.BANKS[concept][form][i].format(**kw)

    def case(frame, ls, labelled=True):
        head = P.HEADER_NO_AGE[frame] if frames is P.HEADER_NO_AGE else P.HEADER[frame]
        text_lines = [say(x) for x in ls]
        state = [x["m"] for x in ls if "m" in x]
        return {"text": "\n".join([head.format(age=age, noun=noun, Noun=noun.capitalize(), sex=sex,
                                               Sex=sex.capitalize()), rule.setting] + text_lines),
                "lines": text_lines, "state": state,
                "fillers": [t for t, x in zip(text_lines, ls) if "filler" in x],
                "tpl": [x["tpl"] for x in ls], "hdr": frame,
                "labels": case_labels(rule, crit, ov, state) if labelled else None,
                "ledger": ledger(crit, thr, [(t, x["m"]) for t, x in zip(text_lines, ls) if "m" in x])}

    cases = {"base": case(hdr, base_ls), "flip": case(hdr, lines_with(flip)),
             "near": case(hdr, lines_with(near, old_near or old)),
             "pres": case(pick(frames, avoid=hdr), pres_ls)}
    if rng_m is not None:              # missing twin: the decisive input unknown
        unknown = None if crit.kind == "numeric" else {
            "m": Mention(crit.concept, "finding", True, "patient", "unknown", "current", "missing"),
            "tpl": (crit.concept, "missing", rng_m.choice(P.ids(P.MISSING, split)))}
        cases["missing"] = case(hdr, lines_with(unknown, None), labelled=False)
    # the decisive lines alone (application cases; reading claims quote them)
    one_line = {k: case(hdr, [x], labelled=False) for k, x in (("base", base), ("flip", flip)) if x}
    return {"rule": rule, "crit": crit, "nm_kind": nm_kind, "tier": tier, "ov": ov, "thr": thr,
            "claims": claim_pairs(rule, crit, thr), "cases": cases, "one_line": one_line}


def ledger(c, thr, lines):
    """The program's ledger for the condition under test: one entry per mention of
    its concept, in text order; one 'not mentioned' entry if there is none."""
    need = condition_text(c, thr)
    out = [{"need": need,
            "found": fmt(m.value, c) if m.kind == "numeric" else text,
            "subject": "patient" if m.subject == "patient" else f"other ({m.subject})",
            "status": m.status,
            "time": "current" if m.time == "current" else (f"past ({m.year})" if m.year else "past")}
           for text, m in lines if m.concept == c.concept]
    # an unmentioned finding is absent (closed world); an unmentioned measurement is unknown
    return out or [{"need": need, "found": "not mentioned", "subject": "patient",
                    "status": "unknown" if c.kind == "numeric" else "absent", "time": "current"}]


def check(rule, g):
    """Invariant violations of one proposed group ([] if none)."""
    crit, ov, cases = g["crit"], g["ov"], g["cases"]
    errs, ev = [], {}
    for k, want in WANT.items():
        st = cases[k]["state"]
        try:
            got = case_labels(rule, crit, ov, st)
            ev[k] = [c.evaluate(st, ov.get(c.cid)) for c in rule.criteria]
        except ValueError as e:
            errs.append(f"state: {k}: {e}")
            continue
        if set(got.values()) != {want}:
            errs.append(f"label: {k} executes to {got}, want {want}")
    if len(ev) == len(WANT):
        changed = [c.cid for c, a, b in zip(rule.criteria, ev["base"], ev["flip"]) if a != b]
        if changed != [crit.cid]:
            errs.append(f"flip: changes {changed}, want [{crit.cid}]")
        errs += [f"{k}: changes a criterion" for k in ("near", "pres") if ev[k] != ev["base"]]
    for k in WANT:   # findings: named in flip and near only; numerics: everywhere
        named = any(kw in cases[k]["text"].lower() for kw in crit.keywords)
        if named != (crit.kind == "numeric" or k in ("flip", "near")):
            errs.append(f"keyword: {k} {'names' if named else 'does not name'} {crit.concept}")
    rule_kw = [kw for c in rule.criteria for kw in c.keywords]
    for k, case in cases.items():
        if any(kw in f.lower() for f in case["fillers"] for kw in rule_kw):
            errs.append(f"filler: {k} has a line with a keyword of the rule")
        for e in case["ledger"]:
            if e["found"] != "not mentioned" and e["found"] not in case["text"]:
                errs.append(f"ledger: {k} quotes {e['found']!r}, not in the case")
    for k in ("flip", "near"):
        removed, added = _edit(cases["base"]["lines"], cases[k]["lines"])
        if added != 1 or removed > 1:
            errs.append(f"edit: {k} removes {removed} and adds {added} lines")
    for k, case in cases.items():   # every slot filled, nothing rendered from a missing value
        if "None" in case["text"] or "{" in case["text"] or "}" in case["text"]:
            errs.append(f"render: {k} has an unfilled slot")
    if cases["pres"]["lines"] == cases["base"]["lines"]:
        errs.append("pres: only the header changes")
    if cases["pres"]["text"] == cases["base"]["text"]:
        errs.append("pres: same text as base")
    if Counter(cases["pres"]["state"]) != Counter(cases["base"]["state"]):
        errs.append("pres: state differs from base")
    if "missing" in cases:
        errs += _check_missing(rule, crit, ov, cases)
    return errs


def _check_missing(rule, crit, ov, cases):
    """Only the decisive input changes from base, it is unknown, and its
    completions (the base and the flip mention) reach both outcomes."""
    def rest(st):
        return [m for m in st if m.concept != crit.concept]

    def tgt(st):
        return [m for m in st if m.concept == crit.concept]

    miss, errs = cases["missing"]["state"], []
    if Counter(rest(miss)) != Counter(rest(cases["base"]["state"])):
        errs.append("missing: other inputs differ from base")
    if [m.status for m in tgt(miss)] != ([] if crit.kind == "numeric" else ["unknown"]):
        errs.append("missing: decisive input is not unknown")
    outs = [case_labels(rule, crit, ov, rest(miss) + tgt(cases[k]["state"])) for k in ("base", "flip")]
    if any({o[t] for o in outs} != {0, 1} for t in outs[0]):
        errs.append("missing: completions do not reach both outcomes")
    return errs


def _edit(a, b):
    """(lines removed, lines added) going from a to b."""
    ops = difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes()
    return (sum(i2 - i1 for tag, i1, i2, _, _ in ops if tag != "equal"),
            sum(j2 - j1 for tag, _, _, j1, j2 in ops if tag != "equal"))


def readapply_records(rule, g, tid, set_name, split, level, seed, tpl_split=None):
    """Reading and application pairs for the base-flip pair of a group (A-D8).

    read: the base and the flip case, with claims quoting the decisive line of
    each (s quotes the base line, s' the flip line). apply: a one-line case
    holding only that line, with the original conclusion claims. Groups are
    tid.base / tid.flip with case kinds read and apply; claim_type conclusion,
    so metrics.decisions() returns d for both. [] when the base has no decisive
    line or the one-line cases do not decide the conclusion (another input of
    the rule would be needed)."""
    crit, ov, one = g["crit"], g["ov"], g["one_line"]
    if set(one) != {"base", "flip"}:
        return []
    try:
        y = {k: rule.label(one[k]["state"], crit.cid, ov) for k in one}
    except ValueError:
        return []
    if y != {"base": 0, "flip": 1}:
        return []
    line = {k: one[k]["lines"][0] for k in one}
    if line["base"] in g["cases"]["flip"]["text"] or line["flip"] in g["cases"]["base"]["text"]:
        return []
    read = tuple(f"The case states: \"{line[k]}\"" for k in ("base", "flip"))
    out = []
    for origin in ("base", "flip"):
        for kind, case, claims in (("read", g["cases"][origin], read),
                                   ("apply", one[origin], rule.claims(crit.cid))):
            t = f"{tid}.{origin}"
            common = dict(tid=t, set=set_name, split=split, tier=g["tier"], level=level, rid=rule.rid,
                          cid=crit.cid, family=rule.family, nm_kind=g["nm_kind"], case_kind=kind,
                          rule_text=rule.rule_text(ov), case_text=case["text"],
                          condition=condition_text(crit, g["thr"]),
                          state=[asdict(m) for m in case["state"]], ledger=case["ledger"],
                          prose=ledger_to_prose(case["ledger"]),
                          meta={"tpl": ["/".join(map(str, x)) for x in case["tpl"]], "hdr": case["hdr"],
                                "tpl_split": tpl_split or split, "seed": seed, "overrides": ov,
                                "keywords": list(crit.keywords), "source_tid": tid, "origin": origin,
                                "criterion_holds": int(origin == "flip")})
            for role, text in zip(("s", "s_prime"), claims):
                out.append(dict(common, iid=f"{t}/{kind}/conclusion/{role}", claim_type="conclusion",
                                claim_role=role, claim_text=text,
                                label=int((role == "s_prime") == (origin == "flip"))))
    return out


def to_records(rule, g, tid, set_name, split, level, seed, tpl_split=None):
    crit = g["crit"]
    out = []
    for k, case in g["cases"].items():
        common = dict(tid=tid, set=set_name, split=split, tier=g["tier"], level=level,
                      rid=rule.rid, cid=crit.cid, family=rule.family, nm_kind=g["nm_kind"],
                      case_kind=k, rule_text=rule.rule_text(g["ov"]), case_text=case["text"],
                      condition=condition_text(crit, g["thr"]),
                      state=[asdict(m) for m in case["state"]], ledger=case["ledger"],
                      prose=ledger_to_prose(case["ledger"]),
                      meta={"tpl": ["/".join(map(str, t)) for t in case["tpl"]], "hdr": case["hdr"],
                            "tpl_split": tpl_split or split, "seed": seed, "overrides": g["ov"],
                            "keywords": list(crit.keywords),
                            # decision bit for the ablations: the criterion under test holds
                            # (None for a missing twin: undetermined)
                            "criterion_holds": None if k == "missing" else
                            int(crit.evaluate(case["state"], g["ov"].get(crit.cid)))})
        for ctype, (s, s2) in g["claims"].items():
            y = None if k == "missing" else case["labels"][ctype]   # missing: neither claim holds
            for role, text in (("s", s), ("s_prime", s2)):
                out.append(dict(common, iid=f"{tid}/{k}/{ctype}/{role}", claim_type=ctype,
                                claim_role=role, claim_text=text,
                                label=0 if y is None else int((role == "s_prime") == (y == 1))))
    return out
