"""reg_v1: registered eligibility criteria compiled from published annotation (STAGE2_TASKS_A, A6).

Sources: the Leaf Clinical Trials corpus (LCT) and Chia. A criterion is one line of a registered eligibility
section. It is kept only if its annotation is a single condition of one of two shapes and nothing else:
  numeric   an observation or the age with one comparison (operator, value, optional unit)
  window    a condition, procedure or drug with one temporal comparison "within N units" in the past
The annotation gives the structure (`struct`); a script compiles it to a condition of selrm/engine2.py.
Conventions the annotation does not fix (reference date, boundary day, which value) are stated in the rule text.
"""
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "data" / "_ext" / "reg"
OPS = {"GT": ">", "GTEQ": ">=", "LT": "<", "LTEQ": "<="}
UNITS = {"day": "days", "week": "weeks", "month": "months", "year": "years"}
CONVENTIONS = {
    "numeric": "Conventions: the value meant is the patient's current value as stated in the case.",
    "window": ("Conventions: time is counted back from the visit date stated in the case; an event on the day exactly "
               "{n} {unit} before the visit still counts; only events of the patient count."),
}
NUM = re.compile(r"^\d+(?:\.\d+)?$")
WORDS = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve".split())}


def brat(ann_path):
    """Entities, events, attributes and relations of one BRAT file."""
    T, E, A, Rl = {}, {}, defaultdict(dict), []
    for ln in open(ann_path, encoding="utf-8"):
        p = ln.rstrip("\n").split("\t")
        if not p or not p[0]:
            continue
        k = p[0][0]
        if k == "T" and len(p) >= 3:
            head = p[1].split(" ")
            spans = " ".join(head[1:]).split(";")
            T[p[0]] = {"type": head[0], "start": int(spans[0].split()[0]), "end": int(spans[-1].split()[-1]), "text": p[2]}
        elif k == "E" and len(p) >= 2:
            parts = p[1].split()
            typ, trig = parts[0].split(":")
            E[p[0]] = {"type": typ, "trigger": trig, "args": [tuple(x.split(":")) for x in parts[1:]]}
        elif k == "A" and len(p) >= 2:
            parts = p[1].split()
            A[parts[1]][parts[0]] = parts[2] if len(parts) > 2 else True
        elif k in "R*" and len(p) >= 2:
            Rl.append(p[1].split())
    return T, E, A, Rl


def lines_of(text):
    out, pos = [], 0
    for ln in text.split("\n"):
        out.append((pos, pos + len(ln), ln))
        pos += len(ln) + 1
    return out


def clean(line):
    """The criterion text without its list number or bullet."""
    return re.sub(r"^\s*(?:\d+[.)]|[-*•])\s*", "", line).strip().rstrip(";").strip()


def lct_candidates():
    """Candidate criteria of the Leaf corpus: (record dict, None) or (None, drop reason) per annotated line."""
    out = []
    for ann in sorted((EXT / "lct").rglob("*.ann")):
        text = ann.with_suffix(".txt").read_text(encoding="utf-8")
        T, E, A, Rl = brat(ann)
        lines = lines_of(text)
        section = "inclusion"
        by_line = defaultdict(list)
        for eid, e in E.items():
            t = T.get(e["trigger"])
            if t is None:
                continue
            i = next((n for n, (a, b, _) in enumerate(lines) if a <= t["start"] < b + 1), None)
            by_line[i].append(eid)
        rel_ents = {x for r in Rl for x in r[1:] for x in [x.split(":")[-1]]}
        for i, (a, b, ln) in enumerate(lines):
            low = ln.strip().lower()
            if low.startswith("inclusion"):
                section = "inclusion"
            elif low.startswith("exclusion"):
                section = "exclusion"
            ids = by_line.get(i, [])
            if not ids:
                continue
            types = sorted(E[x]["type"] for x in ids)
            rec, why = _lct_compile(ids, types, E, T, A, rel_ents, clean(ln))
            if rec:
                rec.update(source="LCT", trial=ann.stem, section=section, line=i, text=clean(ln))
            out.append((rec, why, types))
    return out


def _arg(e, name):
    return next((v for k, v in e["args"] if k == name), None)


def _lct_compile(ids, types, E, T, A, rel_ents, text):
    if any(x in rel_ents for x in ids):
        return None, "linked by a relation (or, and, example, cause, ...)"
    comps = [x for x in ids if E[x]["type"] == "Eq-Comparison"]
    mains = [x for x in ids if E[x]["type"] != "Eq-Comparison"]
    if len(comps) != 1 or len(mains) != 1:
        return None, "not one entity with one comparison"
    m, c = E[mains[0]], E[comps[0]]
    op_t, val_t, unit_t, tu_t = _arg(c, "Operator"), _arg(c, "Value"), _arg(c, "Unit"), _arg(c, "Temporal-Unit")
    period = _arg(c, "Temporal-Period")
    past = bool(period) and A[period].get("Eq-Temporal-Period-Value") == "past"
    if _arg(c, "Value2") or _arg(c, "Temporal-Recency") or not val_t or (period and not past) or (not op_t and not (past and tu_t)):
        return None, "comparison without one operator and one value, or with a second value, a recency or a period other than the past"
    op = OPS.get(A[op_t].get("Eq-Operator-Value")) if op_t else "<="        # 'in the past N units' carries no operator span
    words = T[val_t]["text"].replace(",", "").strip()
    value = str(WORDS[words.lower()]) if words.lower() in WORDS else words
    if op is None or not NUM.match(value):
        return None, "operator not one of >, >=, <, <=, or value not a number"
    name_t = _arg(m, "Name")
    extra = [k for k, _ in m["args"] if k not in ("Name", "Numeric-Filter", "Temporality")]
    if extra:
        return None, "entity with further arguments (severity, stability, location, ...)"
    if m["type"] in ("Observation", "Age") and _arg(m, "Numeric-Filter") == comps[0] and not tu_t and not _arg(m, "Temporality"):
        if m["type"] == "Observation" and not name_t:
            return None, "observation without a name"
        name = "age" if m["type"] == "Age" else T[name_t]["text"]
        unit = T[unit_t]["text"] if unit_t else ("years" if m["type"] == "Age" else "")
        if not op_t:
            return None, "numeric comparison without an operator"
        return {"kind": "numeric", "name": name, "op": op, "value": value, "value_text": words, "unit": unit, "op_text": T[op_t]["text"],
                "entity": m["type"], "obs_type": A[mains[0]].get("Observation-Type-Value", "")}, None
    if m["type"] in ("Condition", "Procedure", "Drug") and _arg(m, "Temporality") == comps[0] and tu_t and name_t:
        unit = UNITS.get(A[tu_t].get("Eq-Temporal-Unit-Value"))
        if unit is None or op not in ("<", "<=") or not value.isdigit():
            return None, "temporal comparison that is not 'within N days, weeks, months or years'"
        return {"kind": "window", "name": T[name_t]["text"], "op": op, "value": value, "value_text": words, "unit": unit,
                "op_text": T[op_t]["text"] if op_t else T[period]["text"], "unit_text": T[tu_t]["text"], "entity": m["type"]}, None
    return None, "not an observation or age with a value, nor a condition, procedure or drug with a time window"


# ---- Chia --------------------------------------------------------------------------------------------------
CHIA_FLAGS = {"Non-query-able", "Subjective", "Not_a_criteria", "Non-representable", "Parsing_Error", "Context_Error",
              "Grammar_Error", "Informed_consent", "Competing_trial", "Undefined_semantics", "Post-eligibility",
              "Pregnancy_considerations", "Intoxication_considerations"}
CHIA_NUM = re.compile(r"^\s*(>=|<=|>|<|≥|≤|at least|greater than or equal to|less than or equal to|greater than|less than|"
                      r"more than|above|below|over|under)\s*(\d+(?:\.\d+)?)\s*(.*)$", re.I)
CHIA_OP = {">=": ">=", "≥": ">=", "at least": ">=", "greater than or equal to": ">=", "<=": "<=", "≤": "<=",
           "less than or equal to": "<=", ">": ">", "greater than": ">", "more than": ">", "above": ">", "over": ">",
           "<": "<", "less than": "<", "below": "<", "under": "<", "or older": ">=", "or more": ">=", "or greater": ">=",
           "or above": ">=", "or higher": ">=", "or less": "<=", "or younger": "<=", "or below": "<=", "or lower": "<="}
CHIA_POST = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*([^\d]*?)\s*(or older|or more|or greater|or above|or higher|or less|or younger|or below|or lower)\s*$", re.I)
CHIA_WIN = re.compile(r"^\s*(within|in|during)\s+(?:the\s+)?(?:last|past|previous|prior)?\s*(\d+)\s*(day|week|month|year)s?"
                      r"(?:\s+(?:prior to|before|of)\s+.*)?\s*$", re.I)


def chia_candidates():
    out = []
    for ann in sorted((EXT / "chia").glob("*.ann")):
        text = ann.with_suffix(".txt").read_text(encoding="utf-8")
        T, _, _, Rl = brat(ann)
        lines = lines_of(text)
        rels = defaultdict(list)
        for r in Rl:
            if len(r) == 3 and r[1].startswith("Arg1:"):
                rels[r[1][5:]].append((r[0], r[2][5:]))
        linked = {x.split(":")[-1] for r in Rl for x in r[1:]}
        by_line = defaultdict(list)
        for tid, t in T.items():
            i = next((n for n, (a, b, _) in enumerate(lines) if a <= t["start"] < b + 1), None)
            by_line[i].append(tid)
        for i, (a, b, ln) in enumerate(lines):
            ids = by_line.get(i, [])
            if not ids:
                continue
            types = sorted(T[x]["type"] for x in ids)
            rec, why = _chia_compile(ids, types, T, rels, linked)
            if rec:
                rec.update(source="Chia", trial=ann.stem.split("_")[0], section="inclusion" if ann.stem.endswith("inc") else "exclusion",
                           line=i, text=clean(ln))
            out.append((rec, why, types))
    return out


def _chia_compile(ids, types, T, rels, linked):
    if set(types) & CHIA_FLAGS:
        return None, "flagged by the annotators (" + ", ".join(sorted(set(types) & CHIA_FLAGS)) + ")"
    if len(ids) != 2:
        return None, "not one entity with one value or one temporal expression"
    main = next((x for x in ids if T[x]["type"] in ("Measurement", "Person", "Condition", "Procedure", "Drug")), None)
    other = next((x for x in ids if x != main), None)
    if main is None or other is None:
        return None, "not one entity with one value or one temporal expression"
    link = [r for r, tgt in rels.get(main, []) if tgt == other]
    if len(link) != 1 or any(x in linked for x in ids if x not in (main, other)):
        return None, "entity and value not linked by exactly one relation"
    mt, ot = T[main], T[other]
    if link[0].lower() == "has_value" and ot["type"] == "Value" and mt["type"] in ("Measurement", "Person"):
        m = CHIA_NUM.match(ot["text"])
        post = CHIA_POST.match(ot["text"])
        if not m and post:                               # '18 years or older'
            class _M:
                def group(self, i, p=post):
                    return (None, p.group(3), p.group(1), p.group(2))[i]
            m = _M()
        if not m:
            return None, "value not of the form 'operator number unit'"
        name = "age" if mt["type"] == "Person" and re.search(r"\bage", mt["text"], re.I) else mt["text"]
        if mt["type"] == "Person" and name != "age":
            return None, "person entity that is not the age"
        return {"kind": "numeric", "name": name, "op": CHIA_OP[m.group(1).lower()], "value": m.group(2), "value_text": m.group(2), "unit": m.group(3).strip(),
                "op_text": m.group(1), "entity": mt["type"], "obs_type": ""}, None
    if link[0].lower() == "has_temporal" and ot["type"] == "Temporal" and mt["type"] in ("Condition", "Procedure", "Drug"):
        m = CHIA_WIN.match(ot["text"])
        if not m:
            return None, "temporal expression not of the form 'within N days, weeks, months or years'"
        return {"kind": "window", "name": mt["text"], "op": "<=", "value": m.group(2), "value_text": m.group(2), "unit": m.group(3).lower() + "s",
                "op_text": m.group(1), "unit_text": m.group(3), "entity": mt["type"]}, None
    return None, "not a measurement or age with a value, nor a condition, procedure or drug with a time window"


# ---- checks and compilation --------------------------------------------------------------------------------
def text_check(rec):
    """Every number, unit and operator of the structure occurs in the criterion text."""
    t = rec["text"]
    ok = rec["value_text"] in t.replace(",", "") and rec["op_text"] in t
    if rec["kind"] == "numeric":
        ok = ok and (not rec["unit"] or rec["unit"] in t) and (rec["name"] == "age" or rec["name"] in t)
    else:
        ok = ok and rec["unit_text"] in t and rec["name"] in t
    return ok


def struct(rec):
    if rec["kind"] == "numeric":
        return {"kind": "numeric", "name": rec["name"], "op": rec["op"], "threshold": float(rec["value"]), "unit": rec["unit"],
                "subject": "patient", "time": "current"}
    return {"kind": "window", "event": rec["name"], "n": int(rec["value"]), "unit": rec["unit"],
            "boundary": "inclusive (stated in the rule text; the annotation does not fix it)", "reference": "visit date",
            "subject": "patient", "status": "present"}


def describe(rec):
    """The compiled program in words, for the model check and the authors' sheet."""
    if rec["kind"] == "numeric":
        words = {">": "greater than", ">=": "greater than or equal to", "<": "less than", "<=": "less than or equal to"}[rec["op"]]
        return f"The criterion holds exactly when the patient's current {rec['name']} is {words} {rec['value']} {rec['unit']}".strip() + "."
    return (f"The criterion holds exactly when the patient had the event \"{rec['name']}\" at some time within the {rec['value']} "
            f"{rec['unit']} before the visit.")


def rule_text(rec):
    conv = CONVENTIONS[rec["kind"]].format(n=rec["value"], unit=rec.get("unit"))
    return f"{rec['section'].capitalize()} criterion: {rec['text']}\n{conv}"
