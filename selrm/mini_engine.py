"""Minimal triplet generator for a first training run (stand-in for engine.py).
Labels come only from Rule.label(); each triplet is checked before it is kept."""
from __future__ import annotations
import random
from selrm.rules import Mention

RELATIVES     = ["mother", "father", "sister", "brother", "aunt", "uncle", "cousin"]
NON_FIRST_DEG = ["aunt", "uncle", "cousin", "grandmother"]
PROMPT = ("Rule: {rule}\n\nCase:\n{case}\n\nClaim: {claim}\n\n"
          "Is the claim correct for this case under the stated rule? Answer + or -.")

def _rand(rng, c, lo, hi):
    v = rng.uniform(lo, hi)
    return round(v, c.decimals) if c.decimals else float(int(round(v)))

def _fmt(c, v):
    return f"{v:.{c.decimals}f}" if c.decimals else f"{int(v)}"

def _near_value(rng, c):
    for _ in range(200):
        v = _rand(rng, c, c.threshold - c.near_delta, c.threshold + c.near_delta)
        if not c.evaluate((Mention(c.concept, "numeric", v),)):
            return v
    raise RuntimeError(f"no numeric near-miss for {c.cid}")

def _background(rng, rule, cid):
    return [Mention(c.concept, "numeric", _rand(rng, c, *c.default_range))
            for c in rule.criteria
            if c.cid != cid and c.kind == "numeric" and c.concept != "age"]

def _states(rng, rule, c, nm_kind):
    bg = _background(rng, rule, c.cid)
    if c.kind == "finding":
        flip = bg + [Mention(c.concept, "finding")]
        if nm_kind == "subject":
            pool = NON_FIRST_DEG if c.counts_family else RELATIVES
            nm = Mention(c.concept, "finding", subject=rng.choice(pool))
        elif nm_kind == "negation":
            nm = Mention(c.concept, "finding", status="absent")
        else:
            nm = Mention(c.concept, "finding", time="past", year=rng.randint(2005, 2020))
        return bg, flip, bg + [nm]
    base = bg + [Mention(c.concept, "numeric", _rand(rng, c, *c.default_range))]
    flip = bg + [Mention(c.concept, "numeric", _rand(rng, c, *c.flip_range))]
    if nm_kind == "numeric":
        near = bg + [Mention(c.concept, "numeric", _near_value(rng, c))]
    else:  # an old value on the flip side; current value unchanged
        near = base + [Mention(c.concept, "numeric", _rand(rng, c, *c.flip_range),
                               time="past", year=rng.randint(2010, 2023))]
    return base, flip, near

def _line(rule, m):
    c = next(c for c in rule.criteria if c.concept == m.concept)
    if m.kind == "numeric":
        return f"{c.label}: {_fmt(c, m.value)}" + (f" (measured {m.year})" if m.time == "past" else " (today)")
    if m.status == "absent":
        return f"No {c.label}."
    if m.subject != "patient":
        return f"Family history: the patient's {m.subject} has {c.label}."
    if m.time == "past":
        return f"History of {c.label} in {m.year}, now resolved."
    return f"Current: {c.label}."

def render(rule, state, age, sex):
    for m in state:
        if m.concept == "age":
            age = int(m.value)
    lines = [_line(rule, m) for m in state if m.concept != "age"]
    return "\n".join([f"Patient: {age}-year-old {sex}. {rule.setting}"] + lines)

def generate(n_triplets, seed, rules):
    rng, out, rejects = random.Random(seed), [], 0
    while len(out) < n_triplets:
        rule = rng.choice(rules)
        c = rng.choice(rule.criteria)
        nm_kind = rng.choice(c.nm_kinds())
        states = _states(rng, rule, c, nm_kind)
        labels = [rule.label(s, c.cid) for s in states]
        if labels != [0, 1, 0]:
            rejects += 1
            continue
        age = rng.randint(*rule.age_range)
        sex = rule.sex or rng.choice(["male", "female"])
        s, s2 = rule.claims(c.cid)
        tid = f"t{seed}_{len(out):06d}"
        inst = []
        for kind, st, y in zip(("base", "flip", "near"), states, labels):
            case = render(rule, st, age, sex)
            for claim, ok in ((s, y == 0), (s2, y == 1)):
                inst.append(dict(tid=tid, rid=rule.rid, cid=c.cid, nm_kind=nm_kind,
                                 case_kind=kind, family=rule.family,
                                 prompt=PROMPT.format(rule=rule.rule_text(), case=case, claim=claim),
                                 answer="+" if ok else "-"))
        out.append(inst)
    return out, rejects

# --- wording by concept type (overrides the earlier _line) ---
DRUG_CONCEPTS    = {"clarithromycin"}
ALLERGY_CONCEPTS = {"pen_allergy"}

def _line(rule, m):
    c = next(c for c in rule.criteria if c.concept == m.concept)
    if m.kind == "numeric":
        return f"{c.label}: {_fmt(c, m.value)}" + (f" (measured {m.year})" if m.time == "past" else " (today)")
    who = "the patient's " + m.subject
    if m.concept in DRUG_CONCEPTS:
        if m.status == "absent":   return f"Medications reviewed: not taking {c.label}."
        if m.subject != "patient": return f"Household: {who} is currently taking {c.label}."
        if m.time == "past":       return f"Took {c.label} in {m.year}; course completed."
        return f"Current medications: {c.label}."
    if m.concept in ALLERGY_CONCEPTS:
        if m.status == "absent":   return f"No known {c.label}."
        if m.subject != "patient": return f"Family history: {who} has a {c.label}."
        if m.time == "past":       return f"{c.label.capitalize()} recorded in {m.year}; since removed after allergy testing."
        return f"Allergies: {c.label} (documented)."
    if m.status == "absent":       return f"No {c.label}."
    if m.subject != "patient":     return f"Family history: {who} has {c.label}."
    if m.time == "past":           return f"History of {c.label} in {m.year}, now resolved."
    return f"Active problems: {c.label}."

# --- v2: rendering variety (overrides _line, render, generate) ---
from selrm.rules import RULES as _ALL_RULES

HEADERS = ["Patient: {age}-year-old {sex}. {setting}",
           "{age}-year-old {sex}. {setting}",
           "{Sex}, {age} years. {setting}"]

TEMPLATES = {
    "num_now":  ["{label}: {val} (today)", "Today's {label}: {val}", "{label} measured this morning: {val}"],
    "num_past": ["{label}: {val} (measured {year})", "{label} in {year} was {val}", "Prior {label} ({year}): {val}"],
    "drug_present": ["Current medications: {label}.", "Currently taking {label}.", "Medication list includes {label}."],
    "drug_absent":  ["Medications reviewed: not taking {label}.", "Not on {label}.", "No current {label} use."],
    "drug_other":   ["Household: {who} is currently taking {label}.", "{who} is on {label}.", "{who} was recently prescribed {label}."],
    "drug_past":    ["Took {label} in {year}; course completed.", "A course of {label} was completed in {year}.", "{label} was stopped in {year}."],
    "allergy_present": ["Allergies: {label} (documented).", "Documented {label}.", "Known {label}, rash on exposure."],
    "allergy_absent":  ["No known {label}.", "Allergy history negative for {label}.", "Denies {label}."],
    "allergy_other":   ["Family history: {who} has a {label}.", "{who} has a documented {label}.", "{who} reports a {label}."],
    "allergy_past":    ["{label} recorded in {year}; since removed after allergy testing.",
                        "A {label} label from {year} was removed after negative testing.",
                        "{label} listed in {year}; de-labelled after a negative challenge."],
    "cond_present": ["Active problems: {label}.", "Current problem list: {label}.", "Ongoing: {label}."],
    "cond_absent":  ["No {label}.", "Negative for {label}.", "Denies {label}."],
    "cond_other":   ["Family history: {who} has {label}.", "{who} has {label}.", "{who} was diagnosed with {label}."],
    "cond_past":    ["History of {label} in {year}, now resolved.", "{label} in {year}, resolved.",
                     "Past history: {label} ({year}), resolved."],
}

BACKGROUND = ["Seasonal allergic rhinitis.", "Hypothyroidism on levothyroxine.", "Osteoarthritis of the left knee.",
              "Former smoker, quit in 2015.", "Appendectomy in 2003.", "Gastroesophageal reflux disease.",
              "Mild intermittent asthma.", "Works as a teacher.", "Drinks alcohol socially.", "Lives with a partner.",
              "Vaccinations up to date.", "Uses reading glasses.", "No recent travel.",
              "Iron-deficiency anemia, treated in 2019.", "Takes vitamin D supplements.", "Eczema on both hands.",
              "Cholecystectomy in 2012.", "Exercises twice a week.", "Latex allergy (contact dermatitis).",
              "Sulfa allergy (rash).", "Lumbar disc herniation in 2017.", "Myopia since childhood."]
ALL_KW  = {k for r in _ALL_RULES for c in r.criteria for k in c.keywords}
BG_POOL = [b for b in BACKGROUND if not any(k in b.lower() for k in ALL_KW)]

def _cap(s):
    return s[0].upper() + s[1:] if len(s) > 1 and s[0].islower() and s[1].islower() else s

def _pick(key, tpl):
    T = TEMPLATES[key]
    return T[tpl % len(T)]

def _line(rule, m, tpl=0):
    c = next(c for c in rule.criteria if c.concept == m.concept)
    if m.kind == "numeric":
        key = "num_past" if m.time == "past" else "num_now"
        return _cap(_pick(key, tpl).format(label=c.label, val=_fmt(c, m.value), year=m.year))
    group = "drug" if m.concept in DRUG_CONCEPTS else "allergy" if m.concept in ALLERGY_CONCEPTS else "cond"
    if m.status == "absent":     key = "absent"
    elif m.subject != "patient": key = "other"
    elif m.time == "past":       key = "past"
    else:                        key = "present"
    label = c.label.replace("active ", "") if key == "past" else c.label
    return _cap(_pick(f"{group}_{key}", tpl).format(label=label, who="the patient's " + m.subject, year=m.year))

def render(rule, state, age, sex, style=None):
    style = style or {"tpl": 0, "hdr": 0, "bg": [], "pos": 0}
    for m in state:
        if m.concept == "age":
            age = int(m.value)
    hdr = HEADERS[style["hdr"] % len(HEADERS)].format(age=age, sex=sex, Sex=sex.capitalize(), setting=rule.setting)
    body = list(style["bg"])
    pos = min(style["pos"], len(body))
    body[pos:pos] = [_line(rule, m, style["tpl"]) for m in state if m.concept != "age"]
    return "\n".join([hdr] + body)

def generate(n_triplets, seed, rules):
    rng, out, rejects = random.Random(seed), [], 0
    while len(out) < n_triplets:
        rule = rng.choice(rules)
        c = rng.choice(rule.criteria)
        nm_kind = rng.choice(c.nm_kinds())
        states = _states(rng, rule, c, nm_kind)
        labels = [rule.label(s, c.cid) for s in states]
        if labels != [0, 1, 0]:
            rejects += 1
            continue
        age = rng.randint(*rule.age_range)
        sex = rule.sex or rng.choice(["male", "female"])
        bg = rng.sample(BG_POOL, rng.randint(0, 3))
        style = {"tpl": rng.randrange(60), "hdr": rng.randrange(60), "bg": bg, "pos": rng.randint(0, len(bg))}
        s, s2 = rule.claims(c.cid)
        tid = f"t{seed}_{len(out):06d}"
        inst = []
        for kind, st, y in zip(("base", "flip", "near"), states, labels):
            case = render(rule, st, age, sex, style)
            for claim, ok in ((s, y == 0), (s2, y == 1)):
                inst.append(dict(tid=tid, rid=rule.rid, cid=c.cid, nm_kind=nm_kind,
                                 case_kind=kind, family=rule.family,
                                 prompt=PROMPT.format(rule=rule.rule_text(), case=case, claim=claim),
                                 answer="+" if ok else "-"))
        out.append(inst)
    return out, rejects
