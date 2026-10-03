"""challenge_v1: author-written cases from state specifications (FINAL_TASKS A P0.3; HUMAN_TASKS H2).

  python scripts/challenge_v1.py kit        # specs + writing forms in challenge_v1/
  python scripts/challenge_v1.py assemble   # notes_<authorN>.md -> notes_<authorN>.jsonl -> records, report
  python scripts/challenge_v1.py assemble --freeze   # register data/challenge_v1/test when complete

160 groups on L2 rules (fold 1), 32 per near-miss kind, easy tier. A group's states come from the
engine (same programs and invariants as rule_v1), but the authors never see generated text: the
form lists the facts of each case in plain words. Labels are computed by executing the rule
program on the specified states. A group enters the set only if its notes pass the assembler's
checks and a second author has approved its current text.
"""
import argparse
import datetime
import hashlib
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402
from selrm import engine as E  # noqa: E402
from selrm import phrases as P  # noqa: E402
from selrm import rules_grammar as RG  # noqa: E402
from selrm.schema import validate  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "challenge_v1"
SET, N, AUTHORS = "challenge_v1", 160, ("author1", "author2", "author3", "author4")
NAME = {"aspirin": "daily aspirin use", "bleeding": "a major bleed", "cad": "coronary artery disease",
        "cancer": "cancer", "chf": "heart failure", "confusion": "new confusion", "crc": "colorectal cancer",
        "diabetes": "diabetes", "exudate": "tonsillar exudate", "fall": "a fall",
        "hemoptysis": "coughing up blood (hemoptysis)", "mech_valve": "a mechanical heart valve",
        "neck_nodes": "tender anterior cervical lymph nodes", "pen_allergy": "a penicillin allergy",
        "peptic_ulcer": "a peptic ulcer", "rlq_tenderness": "right lower quadrant tenderness",
        "sulfa_allergy": "a sulfonamide allergy", "supp_oxygen": "supplemental oxygen",
        "vascular": "a myocardial infarction or peripheral artery disease", "warfarin": "warfarin treatment",
        "vte": "a venous thromboembolism (DVT or pulmonary embolism)", "stroke": "a stroke or TIA",
        "pregnancy": "pregnancy", "clarithromycin": "clarithromycin treatment", "hit": "heparin-induced thrombocytopenia"}


def unit(concept):
    if concept in RG.NUMERIC_NAMES:
        return RG.NUMERIC_NAMES[concept][1]
    t = P.BANKS[concept]["current"][0]
    m = re.search(r"\{v\}\s?([^\s;,]+)", t)
    u = m.group(1).rstrip(".") if m else ""
    return u if u and not u.isalpha() or u in ("kg", "cm", "mmHg") else ""


def name(c):
    if c.kind == "numeric":                        # the rule's own name for the input (not, e.g., 'urea' for BUN)
        return RG.NUMERIC_NAMES.get(c.concept, (c.label, None))[0]
    return NAME.get(c.concept) or re.sub(r"\s*\(patient or first-degree relative\)|^(current|active) | at any time$",
                                         "", c.label)


def fact(m, by_concept):
    """A mention of the state in plain words (None: not stated; the closed world makes it absent)."""
    c = by_concept[m["concept"]]
    who = "the patient" if m["subject"] == "patient" else f"the patient's {m['subject']}"
    if m["kind"] == "numeric":
        u = unit(c.concept)
        v = E.fmt(m["value"], c) + ("" if not u or u[0] in "/%" else " ") + u
        if m["time"] == "current":
            return f"{name(c)}: {v}, the current value"
        if m["form"] == "superseded":
            return f"an earlier {name(c)} of {v}, measured yesterday and replaced by today's value"
        return f"an earlier {name(c)} of {v}, measured in {m['year']}" if m["year"] else \
            f"an earlier {name(c)} of {v}, measured years ago"
    when = f"in {m['year']}" if m["year"] else "years ago"
    if c.concept == "fall":                       # an event, counted in the months before admission
        if m["status"] == "absent":
            return None if m["form"] == "generic" else \
                f"{who} explicitly has not fallen in the past six months (a clear denial)"
        if m["time"] == "current":
            return f"{who} fell once at home in the weeks before this admission"
        return f"{who} fell {when}, long before the past six months"
    if m["status"] == "absent":
        return None if m["form"] == "generic" else f"{who} explicitly does not have {name(c)} (a clear denial)"
    what = name(c)
    if c.concept == "vascular":                    # one concrete condition rather than an either/or
        what = "peripheral artery disease" if m["time"] == "current" else "a myocardial infarction (heart attack)"
    if m["time"] == "current":
        return f"{who} has {what} now"
    if c.counts_past:                              # counted anyway: no need to say it ended
        return f"{who} had {what} in the past ({when})"
    return f"{who} had {what} in the past ({when}); it is over or resolved, not current"


PERSON_WORDS = sorted(set(P.PERSONS) | {"son", "daughter", "mother", "father", "sister", "brother", "wife", "husband",
                                       "partner", "parent", "sibling", "child", "children", "twin", "spouse", "aunt",
                                       "uncle", "cousin", "niece", "nephew", "grandmother", "grandfather", "friend",
                                       "neighbor", "neighbour"})
PERSON_RE = re.compile(r"(?i)(?<!\w)(?:step-?|half-)?(" + "|".join(map(re.escape, PERSON_WORDS))
                       + r")s?(?:-in-law)?(?![\w-])")
OWN_PAST = re.compile(r"(?i)\bas an? (?:child|kid|teenager|teen|baby|infant|toddler)\b")   # the patient's own past
NEG = r"\b(?:no|not|never|denies|denied|without|negative|free of|ruled out|none|nor|absent|nil|excluded)\b|n't\b"
DENIAL = re.compile("(?i)" + NEG + r"|\bnon-")
POST_NEG = r"\b(?:none|nil|absent|negative|excluded|ruled out|denied|not present)\b|\b(?:no|not)\s*(?=[,;.()]|$)"
CLAUSE = r"(?:(?!apart from|except|other than|\bbut\b)[^,;.()])*?"   # within one clause, no exception
OVER_WORDS = (r"resolved|(?:is|was|now|long|all) over|over now|no longer|stopped|outgrown|outgrew|recovered|"
              r"remission|cured|ceased|discontinued|not current|none since|no recurrence|now tolerates|until|used to|"
              r"former(?:ly)?|healed|gone|went away|cleared|settled|ended|quit|off|explanted|removed|replaced|completed")
OVER = re.compile(r"(?i)\b(?:" + OVER_WORDS + r")\b")
NOT_OVER = re.compile(r"(?i)\b(?:still|ongoing|not yet)\b")
PAST = re.compile(r"(?i)\b(?:ago|previous(?:ly)?|history|past|earlier|had|was|were|yesterday|childhood|"
                  r"as an? (?:child|kid|teenager|teen|baby|infant)|(?:19|20)\d\d|" + OVER_WORDS + r")\b")
NOT_CURRENT = re.compile(r"(?i)\b(?:history of|h/o|previous(?:ly)?|prior|in the past|ago|formerly|former|used to|"
                         r"resolved|no longer|outgrown|outgrew|in remission|cured|recovered from|childhood|"
                         r"as an? (?:child|kid|teenager|teen))\b|(?<!since )(?<!from )\b(?:19|20)\d\d\b")
ENDED = r"\b(?:stopped|discontinued|ceased|quit)\b"
REPORTING = re.compile(r"(?i)\b(?:reports?|reported|says?|said|notes?|noted|notices?|noticed|states?|stated|"
                       r"describes?|described|according to|tells?|told|collateral|brought|worried|concerned|"
                       r"thinks?|thought|believes?|mentions?|mentioned|observed|informs?|informed)\b"
                       r"|\bper (?:his|her|their|the|a)\b")
SEX = {"female": re.compile(r"(?i)\b(woman|female|lady|girl|f|mrs|ms|miss)\b|\d\s*f\b"),
       "male": re.compile(r"(?i)\b(man|male|gentleman|boy|m|mr)\b|\d\s*m\b")}
PRONOUNS = {"female": r"\b(?:she|her|hers|herself)\b", "male": r"\b(?:he|him|his|himself)\b"}
AGE_WORDS = re.compile(r"(?i)\b(?:\w+ties|elderly|young|younger|older|old|teen\w*|middle-aged|senior|aged|"
                       r"adolescent|retired|pensioner)\b")
MEDICAL = re.compile(r"(?i)\b(?:pulse|bpm|tachy\w*|brady\w*|febrile|afebrile|fevers?|pyrex\w*|sats|saturation|"
                     r"oxygen|o2|cannula|nebuli[sz]\w*|bp|blood pressure|hypertens\w*|hypotens\w*|medications?|"
                     r"medicines?|tablets?|pills?|prescri\w*|mg|insulin|metformin|furosemide|diuretics?|warfarin|"
                     r"apixaban|rivaroxaban|dabigatran|edoxaban|heparin|aspirin|clopidogrel|statins?|inhalers?|"
                     r"steroids?|antibiotics?|chemo\w*|dialysis|transfus\w*)\b")
SYNONYMS = (r"fevers?|febrile|afebrile|pyrex\w*|temperature", r"bp|blood pressure|hypertens\w*|hypotens\w*",
            r"sats|saturation|oxygen|o2|spo2", r"pulse|bpm|tachy\w*|brady\w*|heart rate")
NUMBER = re.compile(r"(?<![\w.^])\d+(?:\.\d+)?(?!\d|\.\d)")
UNIT_NOISE = re.compile(r"(?i)[x×]\s*10\s*\^?\s*9|10\s*\^\s*9|10⁹|/\s*1\.73\s*m(?:2|²)?")   # numbers inside units
EXTRA_WORDS = {"fall": r"\bf(a|e)ll(s|en|ing)?\b", "weight": r"\bweigh"}      # natural forms the keywords miss
UNIT_RE = {"mg/dL": r"mg\s*/\s*dl", "mmol/L": r"mmol\s*/\s*l|meq\s*/\s*l", "x10^9/L": r"10\s*\^?\s*9|10⁹|×\s*10",
           "mL/min/1.73 m2": r"ml\s*/\s*min", "g/dL": r"g\s*/\s*dl", "mmHg": r"mm\s*hg", "/min": r"/\s*min|per minute|bpm|breaths|beats",
           "C": r"[°º]\s*c\b|(?<=\d)\s*c\b|celsius|degrees", "%": r"%|percent", "kg": r"(?<![a-z])kg\b|kilogram",
           "kg/m2": r"kg\s*/\s*m", "U/L": r"u\s*/\s*l|units", "years": r"year|\byrs?\b|\baged?\b|\by\.?\s*/?\s*o\b",
           "cm": r"(?<![a-z])cm\b|centimet"}


def kw_pattern(kw, strict=False):
    """Keywords are lower-case stems matched at the start of a word; a trailing space marks a whole word.
    strict (for lines that should not touch the rule at all): short stems match whole words only, so
    'bungalow' does not name BUN."""
    whole = kw.endswith(" ") or (strict and len(kw.strip()) <= 4)
    return re.compile(r"(?i)\b" + re.escape(kw.strip()) + (r"\b" if whole else ""))


def named_word(text, keywords, concept=None, strict=False):
    """The whole word through which text names the condition ('Agent' for the stem 'age'), or None."""
    extra = EXTRA_WORDS.get(concept)
    m = (extra and re.search("(?i)" + extra, text)) or \
        next((m for k in keywords for m in [kw_pattern(k, strict).search(text)] if m), None)
    return m.group(0) + re.match(r"[\w-]*", text[m.end():]).group(0) if m else None


def names(text, keywords, concept=None, strict=False):
    return named_word(text, keywords, concept, strict) is not None


def _kw(keywords, concept=None):
    return "(?:" + "|".join([re.escape(k.strip()) for k in keywords]
                            + ([EXTRA_WORDS[concept][2:]] if concept in EXTRA_WORDS else [])) + ")"


def negated(text, keywords, concept=None):
    """The condition's name is denied within one clause: a denial word before it ('no asthma', 'never had
    a DVT'; not 'no allergies apart from penicillin'), 'non-' on the name itself ('non-diabetic'), or a
    denial after it ('Diabetes: none', 'DVT ruled out')."""
    kw = _kw(keywords, concept)
    return bool(re.search(f"(?i)(?:{NEG}){CLAUSE}\\b{kw}", text) or re.search(f"(?i)\\bnon-{kw}", text)
                or re.search(f"(?i)\\b{kw}[\\w-]*{CLAUSE}(?:{POST_NEG})", text))


def in_setting(word, setting):
    """The reason for the visit already gives this word, or a synonym of it ('febrile' for 'fever')."""
    cls = next((c for c in SYNONYMS if re.fullmatch(f"(?i){c}", word)), re.escape(word))
    return bool(re.search(rf"(?i)\b(?:{cls})\b", setting))


def numbers(line, year=None):
    """(number, position) for each number a line states, leaving out numbers inside units (10^9, 1.73 m2),
    digits attached to letters (SpO2) and the mention's own year."""
    clean = UNIT_NOISE.sub(lambda m: " " * len(m.group(0)), line)
    return [(x.group(0), x.start()) for x in NUMBER.finditer(clean) if x.group(0) != str(year)]


def stated_value(line, keywords, concept, year=None):
    """The first number after the input's name (from the line start when the name is absent), skipping
    the mention's own year: 'Creatinine 1.1, was 2.4' states 1.1, not 2.4."""
    hits = [m.end() for k in keywords for m in [kw_pattern(k).search(line)] if m]
    extra = EXTRA_WORDS.get(concept) and re.search("(?i)" + EXTRA_WORDS[concept], line)
    start = min(hits + ([extra.end()] if extra else []), default=0)
    return next((v for v, pos in numbers(line, year) if pos >= start), None)


def shown(keywords, concept=None):
    extra = {"fall": " | 'fell' | 'fall'", "weight": " | 'weighed'"}.get(concept, "")
    return " | ".join(f"'{k.strip()}'" for k in keywords) + extra


def fingerprint(n, s):
    """Six hex digits that identify a group's written lines and the facts they state; the second author
    approves exactly these, so a later edit, or a change of the facts, needs a new check."""
    lines = [s["gid"]] + [f["text"] for f in s["facts"]] + [s["edits"][k]["text"] for k in ("flip", "near")] + \
        [n.get("header", ""), n.get("reason", "")] + [n[k] for k in sorted(n) if k.startswith("fact ")] + \
        list(n.get("extra", [])) + [n.get("FLIP", ""), n.get("NEAR", "")]
    return hashlib.sha1("\n".join(lines).encode("utf-8")).hexdigest()[:6]


def _diff(base, other):
    return [m for m in base if m not in other], [m for m in other if m not in base]


# ---------------------------------------------------------------- kit
def specs():
    F = json.loads((ROOT / "data" / "rule_v1" / "FOLDS.json").read_text(encoding="utf-8"))["folds"]["1"]
    cells = D.sample_specs([D.RULES_BY_ID[x] for x in F["l2_rules"]], N, SET, tier_w={"easy": 1})
    out = []
    for i, (rid, cid, nm, tier) in enumerate(cells):
        recs = E.make_group(D.RULES_BY_ID[rid], cid, nm, tier, "test", i, SET, "L2")
        rule, crit = D.RULES_BY_ID[rid], D.RULES_BY_ID[rid].crit(cid)
        by_concept = {c.concept: c for c in rule.criteria}
        st = {k: next(r["state"] for r in recs if r["case_kind"] == k) for k in ("base", "flip", "near")}
        head = next(r["case_text"] for r in recs if r["case_kind"] == "base").split("\n")[0]
        age = re.search(r"\d+", head)
        sex = "female" if re.search(r"(?i)\b(woman|female)\b", head) else "male"
        facts = [{"mention": m, "text": fact(m, by_concept)} for m in st["base"]]
        stated = [f for f in facts if f["text"]]
        edits = {}
        for k in ("flip", "near"):
            removed, added = _diff(st["base"], st[k])
            assert len(added) == 1 and len(removed) <= 1, (rid, k)
            idx = next((j for j, f in enumerate(stated) if removed and f["mention"] == removed[0]), None)
            edits[k] = {"op": "replace" if idx is not None else "add", "fact": None if idx is None else idx + 1,
                        "text": fact(added[0], by_concept), "mention": added[0]}
        out.append({"gid": f"c{i + 1:03d}", "tid": recs[0]["tid"], "rid": rid, "cid": cid, "nm_kind": nm, "tier": tier,
                    "rule_text": recs[0]["rule_text"], "setting": rule.setting,
                    "patient": (f"{age.group(0)}-year-old " if age else "adult ") + sex, "sex": sex,
                    "facts": [{"n": j + 1, "text": f["text"], "mention": f["mention"]} for j, f in enumerate(stated)],
                    "edits": edits, "states": st, "concept": name(crit), "keywords": list(crit.keywords),
                    "other_keywords": sorted({k for c in rule.criteria if c is not crit for k in c.keywords}),
                    "labels": {k: E.case_labels(rule, crit, recs[0]["meta"]["overrides"], E.state_from_json(st[k]))
                               for k in st}})
    rng = random.Random(SET)
    by_kind = defaultdict(list)
    for s in out:
        by_kind[s["nm_kind"]].append(s)
    for kind in sorted(by_kind):                    # 8 groups of every kind per author
        g = by_kind[kind]
        rng.shuffle(g)
        for j, s in enumerate(g):
            s["author"] = AUTHORS[j % 4]
            s["checker"] = AUTHORS[(j + 1) % 4]
    return out


def form(s):
    lines = [f"## {s['gid']}   (writer: {s['author']}; checker: {s['checker']})", "",
             f"Rule, for context only (do not refer to it in the note): {s['rule_text']}", "",
             f"Patient: {s['patient']}. Reason for the visit: {s['setting']}", "",
             "BASE note: one line for each fact below, in this order, in your own words."]
    lines += [f"  fact {f['n']}: {f['text']}" for f in s["facts"]]
    if not s["facts"]:
        lines.append("  (no fact to state beyond the patient and the reason for the visit)")
    if D.RULES_BY_ID[s["rid"]].crit(s["cid"]).kind == "finding":
        lines.append(f"  Do not mention {s['concept']} in the base note at all, not even to deny it.")
    for k, lab in (("flip", "FLIP"), ("near", "NEAR-MISS")):
        e = s["edits"][k]
        where = f"replaces your line for fact {e['fact']}" if e["op"] == "replace" else "is added to the base note"
        lines.append(f"  {lab} (instruction): one line that {where}, stating: {e['text']}.")
    lines += [f"Every line that mentions {s['concept']} must contain one of these words (a longer word that starts "
              f"with one is fine): {shown(s['keywords'], D.RULES_BY_ID[s['rid']].crit(s['cid']).concept)}.", "",
              "header: ", "reason: "] + [f"fact {f['n']}: " for f in s["facts"]] + \
             ["extra: ", "FLIP: ", "NEAR: ", "check_ok: ", "check_comment: ", ""]
    return "\n".join(lines)


def kit():
    S = specs()
    KIT.mkdir(exist_ok=True)
    with open(KIT / "specs.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for s in S:
            f.write(json.dumps(s, sort_keys=True) + "\n")
    for a in AUTHORS:
        mine = sorted((s for s in S if s["author"] == a), key=lambda s: s["gid"])
        head = (f"# challenge_v1 writing form: {a}\n\nRead `challenge_v1/WRITING_GUIDE.md` first. Fill in every "
                f"field after the colon. Save this file as `challenge_v1/notes_{a}.md` (UTF-8).\n"
                f"{len(mine)} groups. Your second author checks them in this same file: `check_ok` (yes or no, "
                f"with the fingerprint from `challenge_v1/ASSEMBLY_REPORT.md`) and `check_comment`.\n\n")
        (KIT / f"form_{a}.md").write_text(head + "\n".join(form(s) for s in mine), encoding="utf-8")
    print(json.dumps({"groups": len(S), "by_kind": Counter(s["nm_kind"] for s in S),
                      "by_author": Counter(s["author"] for s in S),
                      "by_author_kind": Counter((s["author"], s["nm_kind"]) for s in S).most_common(3)}, default=str))


# ---------------------------------------------------------------- assemble
FIELD = re.compile(r"^(header|reason|fact \d+|extra|FLIP|NEAR|check_ok|check_comment):[ \t]*(.*)$")


def parse(md):
    """{gid: {field: value}} from a filled form (extra may repeat), and the group ids that occur twice."""
    out, cur, twice = {}, None, set()
    for line in md.splitlines():
        m = re.match(r"^## (c\d{3})\b", line)
        if m:
            if m.group(1) in out:
                twice.add(m.group(1))
            cur = out.setdefault(m.group(1), {"extra": []})
            continue
        m = FIELD.match(line)
        if cur is not None and m:
            k, v = m.group(1), m.group(2).strip()
            if k == "extra":
                if v:
                    cur["extra"].append(v)
            else:
                cur[k] = v
    return out, twice


def check(s, n):
    """Problems of one filled group ([] if none).
    - Header: the stated age (on 'adult' forms none, and no age words) and sex.
    - Reason and extra lines: the reason adds no input of the rule and no number or medical word that the
      reason for the visit lacks; extra lines carry no input of the rule, no number, no medical word.
    - Cases: the base never names the decisive finding; no case names a condition the specification
      leaves unmentioned; FLIP and NEAR differ.
    - Each fact, FLIP and NEAR line against its mention: a listed word for the condition under test; the
      value exactly as given, as the only number after its name, with its unit; the year; the person (a
      relative has the condition rather than reports it; the patient's lines name no one else and use the
      patient's pronouns); a denial tied to the name for an absent fact and none for a present one; a
      current fact reads as current, a fact marked over says so in words, an undated past fact reads as
      past.
    A group that passes needs the second author's approval of exactly its text and facts:
    check_ok: yes <fingerprint>."""
    errs = []
    need = ["header", "reason", "FLIP", "NEAR"] + [f"fact {f['n']}" for f in s["facts"]]
    errs += [f"{k} is empty" for k in need if not n.get(k)]
    if errs:
        return errs
    rule = D.RULES_BY_ID[s["rid"]]
    crit = rule.crit(s["cid"])
    adult, sex = s["patient"].startswith("adult"), s["sex"]
    other = "male" if sex == "female" else "female"
    hdr = n["header"]
    if adult:
        if re.search(r"\d", hdr) or AGE_WORDS.search(hdr):
            errs.append("header: give no age and no age words here (the age is a fact of the rule)")
    elif not re.search(r"(?<!\d)" + re.match(r"\d+", s["patient"]).group(0) + r"(?!\d)", hdr):
        errs.append(f"header: the age {re.match(r'[0-9]+', s['patient']).group(0)} is not given")
    if not SEX[sex].search(hdr) or SEX[other].search(hdr):
        errs.append(f"header: the sex ({sex}) is not given clearly")
    for x in n.get("extra", []):
        why = [f"the word '{w}' names {c.label}" for c in rule.criteria
               for w in [named_word(x, c.keywords, c.concept, strict=True)] if w]
        med, aged = MEDICAL.search(x), adult and AGE_WORDS.search(x)
        why += ([f"'{med.group(0)}' is medical"] if med else []) + (["it gives a number"] if re.search(r"\d", x) else []) \
            + ([f"'{aged.group(0)}' hints at the age"] if aged else [])
        if why:
            errs.append(f"extra '{x[:40]}': {'; '.join(why)}; extra lines must be unrelated to the rule and to health")
    reason, setting = n["reason"], s["setting"]
    for c in rule.criteria:
        w = named_word(reason, c.keywords, c.concept, strict=True)
        if w and not names(setting, c.keywords, c.concept):
            errs.append(f"reason: the word '{w}' names {c.label}, which the reason for the visit does not")
    given = {v for v, _ in numbers(setting)}
    added = [m.group(0) for m in MEDICAL.finditer(reason) if not in_setting(m.group(0), setting)]
    added += [v for v, _ in numbers(reason) if v not in given]
    added += [m.group(0) for m in AGE_WORDS.finditer(reason) if adult and not AGE_WORDS.search(setting)]
    if added:
        errs.append(f"reason: adds {', '.join(repr(a) for a in added)}, which the reason for the visit does not give")
    for k, t in assemble_texts(s, n).items():
        if crit.kind == "finding" and k == "base" and names(t, s["keywords"], crit.concept):
            errs.append(f"base: names {s['concept']}, which the base must not mention")
        stated = {m["concept"] for m in s["states"][k] if m["form"] != "generic"}
        for c in rule.criteria:
            if c is not crit and c.kind == "finding" and c.concept not in stated and names(t, c.keywords, c.concept):
                errs.append(f"{k}: mentions {c.label}, which the specification leaves unmentioned")
    if n["FLIP"].strip().lower() == n["NEAR"].strip().lower():
        errs.append("FLIP and NEAR are the same line")
    lines = [(f"fact {f['n']}", f["mention"], n[f"fact {f['n']}"]) for f in s["facts"]] + \
            [(key, s["edits"][k]["mention"], n[key]) for k, key in (("flip", "FLIP"), ("near", "NEAR"))]
    for label, m, line in lines:
        c = next(x for x in rule.criteria if x.concept == m["concept"])
        if c is crit and not names(line, s["keywords"], crit.concept):
            errs.append(f"{label}: does not name {s['concept']} (use one of {shown(s['keywords'], crit.concept)})")
        if m["kind"] == "numeric":
            v, u = E.fmt(m["value"], c), unit(c.concept)
            got = stated_value(line, c.keywords, c.concept, m.get("year"))
            reading = re.sub(re.escape(v) + r"\s*/\s*\d+", v, line) if c.concept == "sbp" else line   # 150/90
            count = len(numbers(reading, m.get("year")))
            if got is None:
                errs.append(f"{label}: the value {v} is not in the line")
            elif got != v:
                errs.append(f"{label}: write the value exactly as given, {v} (the line gives {got})")
            elif count > 1:
                errs.append(f"{label}: gives {count} numbers; state only the value {v}"
                            + (f" and the year {m['year']}" if m.get("year") else ""))
            if u and u in UNIT_RE and not re.search("(?i)" + UNIT_RE[u], line):
                errs.append(f"{label}: the unit {u} is not in the line")
            if m["time"] == "past" and re.search(r"(?i)\b(?:today|now|current(?:ly)?)\b", line):
                errs.append(f"{label}: an earlier value must not read as today's")
        if m.get("year") and str(m["year"]) not in line:
            errs.append(f"{label}: the year {m['year']} is not in the line")
        if m["subject"] != "patient":
            if not re.search(r"(?i)(?<![\w-])" + re.escape(m["subject"]) + r"(?!-in-law)(?![\w-])", line):
                errs.append(f"{label}: the person '{m['subject']}' is not named")
            if REPORTING.search(line):
                errs.append(f"{label}: the {m['subject']} must have the condition; do not report it "
                            f"('per', 'says', 'worried about')")
            wrong = re.search(r"(?i)\b" + ("his" if sex == "female" else "her") + r"\s+" + re.escape(m["subject"]), line)
            if wrong:
                errs.append(f"{label}: '{wrong.group(0)}' does not fit a {sex} patient")
        else:
            if PERSON_RE.search(OWN_PAST.sub("", line)):
                errs.append(f"{label}: names another person, but the fact is about the patient")
            wrong = re.search("(?i)" + PRONOUNS[other], line)
            if wrong:
                errs.append(f"{label}: '{wrong.group(0)}' does not fit a {sex} patient")
        if m["kind"] == "finding":
            over = m["status"] == "present" and m["time"] == "past" and not c.counts_past and c.concept != "fall"
            if m["status"] == "absent" and not negated(line, c.keywords, c.concept):
                errs.append(f"{label}: should be a clear denial of {name(c)} ('No ...', 'Denies ...', '...: none')")
            elif m["status"] == "present" and not over and negated(line, c.keywords, c.concept):
                errs.append(f"{label}: reads as a denial, but the fact is present")
            if m["status"] == "present" and m["time"] == "current" and c.concept != "fall" and (
                    NOT_CURRENT.search(re.sub(r"(?i)\bsince\s+\w+", "", line))
                    or re.search(f"(?i){ENDED}{CLAUSE}\\b{_kw(c.keywords, c.concept)}", line)):
                errs.append(f"{label}: reads as past or over, but the fact is current (no 'history of', 'previous', "
                            f"'resolved' or year; 'since <year>' is fine)")
            if over and (not OVER.search(line) or NOT_OVER.search(line)):
                errs.append(f"{label}: must say that it is over (resolved, no longer, outgrown, ...); "
                            f"a date alone is not enough")
        if m["status"] == "present" and m["time"] == "past" and not m.get("year") and not PAST.search(line):
            errs.append(f"{label}: does not read as past or earlier")
    if errs:
        return errs
    fp = fingerprint(n, s)
    words = re.sub(r"[^a-z0-9]+", " ", n.get("check_ok", "").lower()).split()
    if words[:1] == ["no"] and words[1:2] in ([], [fp]):
        errs.append(f"the second author answered no ({n.get('check_comment', '')}); revise the lines, clear check_ok "
                    f"and check_comment, and ask for a new check (fingerprint now {fp})")
    elif words != ["yes", fp]:
        errs.append(f"passes the checks; awaiting the second author: check_ok: yes {fp}")
    return errs


def assemble_texts(s, n):
    base = [n["header"], n["reason"]] + [n[f"fact {f['n']}"] for f in s["facts"]] + n["extra"]
    out = {"base": "\n".join(base)}
    for k, key in (("flip", "FLIP"), ("near", "NEAR")):
        e, ls = s["edits"][k], list(base)
        if e["op"] == "replace":
            ls[1 + e["fact"]] = n[key]
        else:
            ls.insert(random.Random(s["gid"]).randint(2, len(ls)), n[key])
        out[k] = "\n".join(ls)
    return out


def records(s, n, author):
    rule = D.RULES_BY_ID[s["rid"]]
    crit = rule.crit(s["cid"])
    thr, ov = crit.threshold, {}
    texts = assemble_texts(s, n)
    out = []
    for k, text in texts.items():
        st = E.state_from_json(s["states"][k])
        labels = E.case_labels(rule, crit, ov, st)
        ledger = E.ledger(crit, thr, [(_line_of(s, n, k, m), m) for m in st
                                      if m.concept == crit.concept and m.form != "generic"])   # no author line
        assert all(e["found"] == "not mentioned" or e["found"] in text for e in ledger), (s["gid"], k)
        common = dict(tid=f"{SET}.test.{s['gid']}", set=SET, split="test", tier="author", level="L2", rid=rule.rid,
                      cid=crit.cid, family=rule.family, nm_kind=s["nm_kind"], case_kind=k, rule_text=s["rule_text"],
                      case_text=text, condition=E.condition_text(crit, thr),
                      state=s["states"][k], ledger=ledger, prose=E.ledger_to_prose(ledger),
                      meta={"author": author, "checker": s["checker"], "check_comment": n.get("check_comment", ""),
                            "spec_tid": s["tid"], "tpl": [], "tpl_split": "author", "seed": int(s["gid"][1:]),
                            "overrides": ov, "keywords": s["keywords"],
                            "criterion_holds": int(crit.evaluate(st, None))})
        for ctype, (a, b) in E.claim_pairs(rule, crit, thr).items():
            for role, t in (("s", a), ("s_prime", b)):
                r = dict(common, iid=f"{common['tid']}/{k}/{ctype}/{role}", claim_type=ctype, claim_role=role,
                         claim_text=t, label=int((role == "s_prime") == (labels[ctype] == 1)))
                validate(r)
                out.append(r)
    return out


def _line_of(s, n, k, m):
    """The author's line that states mention m in case k."""
    for f in s["facts"]:
        if f["mention"] == {**m.__dict__}:
            line = n[f"fact {f['n']}"]
            for kk, key in (("flip", "FLIP"), ("near", "NEAR")):
                e = s["edits"][kk]
                if k == kk and e["op"] == "replace" and e["fact"] == f["n"]:
                    return n[key]
            return line
    return n["FLIP" if k == "flip" else "NEAR"]


def assemble(freeze=False, kit_dir=KIT, restore=False):
    """Checks every notes_<authorN>.md and writes ASSEMBLY_REPORT.md. A group is read only from its
    writer's file, where the second author also writes check_ok. freeze registers the set once all
    groups are accepted; restore rewrites the records of the frozen set and checks its sha256."""
    S = {json.loads(l)["gid"]: json.loads(l) for l in open(kit_dir / "specs.jsonl", encoding="utf-8")}
    report, recs, done = ["# challenge_v1 assembly report\n"], [], Counter()
    for md in sorted(kit_dir.glob("notes_*.md")):
        who = md.stem[len("notes_"):]
        if who not in AUTHORS:                      # file names carry the assigned id, never a person's name
            report.append(f"- {md.name}: not read; rename it to notes_<authorN>.md (one of {', '.join(AUTHORS)})")
            continue
        raw = md.read_bytes()
        try:
            text = raw.decode("utf-8-sig")
        except UnicodeDecodeError:
            text = raw.decode("cp1252", errors="replace")
            report.append(f"- {md.name}: not saved as UTF-8 (read as Windows-1252); save it as UTF-8")
        notes, twice = parse(text)
        report += [f"- {who} {gid}: written twice in {md.name}; keep one" for gid in sorted(twice)]
        with open(md.with_suffix(".jsonl"), "w", encoding="utf-8", newline="\n") as f:
            for gid, n in sorted(notes.items()):
                f.write(json.dumps(dict(gid=gid, author=who, **n), sort_keys=True) + "\n")
        for gid, n in sorted(notes.items()):
            if gid not in S:
                report.append(f"- {who} {gid}: unknown group id")
                continue
            if S[gid]["author"] != who:
                report.append(f"- {who} {gid}: belongs to {S[gid]['author']}; the group and its check go in "
                              f"notes_{S[gid]['author']}.md")
                continue
            errs = check(S[gid], n) + ([f"written twice in {md.name}"] if gid in twice else [])
            if not errs:
                try:
                    recs += records(S[gid], n, S[gid]["author"])   # the assigned id, never a person's name
                except (AssertionError, ValueError, KeyError) as e:
                    errs = [f"internal check failed ({e!r}); please tell role A"]
            if errs:
                report.append(f"- {who} {gid}: " + "; ".join(errs))
                done["awaiting check" if errs[0].startswith("passes the checks") else "rejected"] += 1
            else:
                done["accepted"] += 1
    missing = sorted(set(S) - {r["tid"].split(".")[-1] for r in recs})
    report.append(f"\naccepted {done['accepted']}, awaiting check {done['awaiting check']}, rejected {done['rejected']}, "
                  f"not yet written or accepted {len(missing)}")
    (kit_dir / "ASSEMBLY_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(report[-1].strip())
    if freeze or restore:
        if missing:
            sys.exit(f"refusing to {'freeze' if freeze else 'restore'}: {len(missing)} groups missing")
        _register(recs, restore)
    return recs, report


def _register(recs, restore=False):
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    name = f"{SET}/test"
    d = ROOT / "data" / SET / "test"
    lines = [json.dumps(r, sort_keys=True) + "\n" for r in recs]
    sha = hashlib.sha256("".join(lines).encode("utf-8")).hexdigest()
    if restore:                                     # records are not in git; rebuild them from the notes
        if sha != registry.get(name, {}).get("sha256"):
            sys.exit(f"refusing to restore {name}: sha256 {sha[:16]} differs from the registry")
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text("".join(lines), encoding="utf-8", newline="\n")
        return print(f"restored {name}: sha256 matches")
    if registry.get(name, {}).get("frozen"):
        sys.exit(f"refusing to rebuild: {name} is frozen (use --restore to write its records)")
    d.mkdir(parents=True, exist_ok=True)
    (d / "records.jsonl").write_text("".join(lines), encoding="utf-8", newline="\n")
    created = datetime.date.today().isoformat()
    man = {"name": "test", "set": SET, "split": "test", "level": "L2", "tier": "author", "created": created,
           "generator": "scripts/challenge_v1.py assemble", "frozen": True, "n_groups": len({r["tid"] for r in recs}),
           "n_records": len(recs), "sha256": sha, "git_commit": D.git_commit(),
           "by_kind": dict(Counter(r["nm_kind"] for r in recs if r["case_kind"] == "base" and r["claim_role"] == "s"
                                   and r["claim_type"] == "conclusion")),
           "by_author": dict(Counter(r["meta"]["author"] for r in recs if r["case_kind"] == "base"
                                     and r["claim_role"] == "s" and r["claim_type"] == "conclusion")),
           "shortcut_validation": D.validate_shortcuts(d / "records.jsonl")}
    (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    registry[name] = {"path": f"{SET}/test/records.jsonl", "split": "test", "level": "L2", "tier": "author",
                      "n_groups": man["n_groups"], "n_records": len(recs), "manifest": f"{SET}/test/MANIFEST.json",
                      "frozen": True, "created": created, "sha256": sha}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(f"{name} frozen: {man['n_groups']} groups, sha256 {sha[:16]}, shortcuts {man['shortcut_validation']['result']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("kit", "assemble"))
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--restore", action="store_true", help="rewrite the frozen records from the notes")
    a = ap.parse_args()
    kit() if a.cmd == "kit" else assemble(a.freeze, restore=a.restore)
