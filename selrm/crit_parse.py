"""Deterministic criterion parser (STAGE2_SPEC section 7). No model.
parse_criterion(rule_text, condition, classes) finds the clause of the rule text that states `condition` and returns
its constraints, one dict per kind:
  {"kind": "value", "op": "gt|ge|lt|le", "thr": float, "unit": str}
  {"kind": "time", "scope": "current|ever|window", "n": int, "unit": "day|week|month|year", "inclusive": bool}
  {"kind": "subject", "allowed": ["patient"] or ["patient", "first-degree"]}
  {"kind": "status", "allowed": ["present"]}
  {"kind": "concept", "class": <onto id or None>}     the clause names a class ('of the class "X"'); the id comes
                                                      from `classes` (lower-case class name -> id), None if unknown
It returns None when no clause, or more than one, matches the condition (the parser abstains; coverage counts it).
from_struct(struct) gives the same list from a record's reference structure (role A's `struct`), for the
gate_struct variant and for the parser's precision. Developed on dev portions only (rule_v1/dev, rule_v2/dev,
cls_v1/dev; reg_v1/dev and mcv_v1/dev when their struct forms are read)."""
import re

NUM = r"(\d+(?:\.\d+)?)"
UNIT = r"\s*((?:%|[^\s,;()]+(?: m2)?)?)"
STOP = set("a an the of or and in at to for is are has have had with any time above below over under least most more "
           "less than patient current currently use history".split())
VALUE = [  # first match wins
    (rf"at or below {NUM}{UNIT}", "le"), (rf"at or above {NUM}{UNIT}", "ge"),
    (rf"{NUM}{UNIT} or (?:more|above|higher|greater|older)", "ge"), (rf"{NUM}{UNIT} or (?:less|below|lower|fewer|younger)", "le"),
    (rf"(?:at least|not less than|>=|≥) ?{NUM}{UNIT}", "ge"), (rf"(?:at most|no more than|not more than|<=|≤) ?{NUM}{UNIT}", "le"),
    (rf"(?:above|over|more than|greater than|higher than|older than|exceeds|>) ?{NUM}{UNIT}", "gt"),
    (rf"(?:below|under|less than|lower than|younger than|<) ?{NUM}{UNIT}", "lt")]
WINDOW = rf"(?:within|in|during) (?:the )?(?:(?:last|past|previous|preceding) )?{NUM} (day|week|month|year)s?"
EVER = r"\bever\b|at any time|current or past|history of|previously"
EXCLUSIVE = r"less than|fewer than|exclusive|does not count|not counted|no longer counts"
CLASS = r'the class "([^"]+)"'
OPS = {">": "gt", ">=": "ge", "<": "lt", "<=": "le"}
SHIFT = 0xE000        # private-use code points hide separators inside brackets and quotes while splitting


def stems(text):
    return {w if w[0].isdigit() else w[:5] for w in re.findall(r"\d+(?:\.\d+)?|[a-z][a-z0-9-]*", text.lower()) if w not in STOP}


def clauses(text):
    """Clauses of a rule text. Nothing inside parentheses or double quotes splits."""
    hide = lambda m: re.sub(r"[,;:. ]", lambda c: chr(ord(c.group(0)) + SHIFT), m.group(0))
    t = re.sub(r'\([^)]*\)|"[^"]*"', hide, text)
    parts = re.split(r"[;:](?:\s|$)|\.(?:\s|$)|,\s| (?:and|or) (?=the |a current )| if | for ", t)
    show = lambda p: "".join(chr(ord(c) - SHIFT) if SHIFT <= ord(c) < SHIFT + 128 else c for c in p)
    return [show(p).strip() for p in parts if p and p.strip()]


def find_clause(rule_text, condition):
    """The one clause sharing the most content words with the condition; None on no overlap or a tie."""
    want = stems(condition)
    scored = sorted(((len(want & stems(c)), c) for c in clauses(rule_text)
                     if not c.endswith(" instead")), reverse=True)     # the consequent names no condition
    if not scored or scored[0][0] == 0 or (len(scored) > 1 and scored[0][0] == scored[1][0] and scored[0][1] != scored[1][1]):
        return None
    return scored[0][1]


def parse_clause(clause, classes=None):
    out, low = [], clause.lower()
    w = re.search(WINDOW, low)
    for pat, op in VALUE:
        m = None if w else re.search(pat, low)     # a window clause states a period, not a threshold
        if m:
            out.append({"kind": "value", "op": op, "thr": float(m.group(1)), "unit": m.group(2)})
            break
    if w:
        out.append({"kind": "time", "scope": "window", "n": int(float(w.group(1))), "unit": w.group(2),
                    "inclusive": not re.search(EXCLUSIVE, low)})
    else:
        out.append({"kind": "time", "scope": "ever" if re.search(EVER, low) else "current"})
    out.append({"kind": "subject", "allowed": ["patient"] + (["first-degree"] if "first-degree relative" in low else [])})
    out.append({"kind": "status", "allowed": ["present"]})
    c = re.search(CLASS, clause)
    if c:
        out.append({"kind": "concept", "class": (classes or {}).get(c.group(1).lower())})
    return out


def parse_criterion(rule_text, condition, classes=None):
    c = find_clause(rule_text, condition)
    return None if c is None else parse_clause(c, classes)


def from_struct(st):
    """Constraints from role A's `struct` (rule_v2, cls_v1: kinds finding, numeric, window, class); None for a
    form this does not read (e.g. mcv_v1's item structure)."""
    kind = (st or {}).get("kind")
    if kind not in ("finding", "numeric", "window", "class") or "inputs" in st:
        return None
    out = []
    if kind == "numeric":
        out.append({"kind": "value", "op": OPS[st["op"]], "thr": float(st["threshold"]), "unit": ""})
    if kind == "window":
        out.append({"kind": "time", "scope": "window", "n": int(st["n"]), "unit": st["unit"].rstrip("s"),
                    "inclusive": st["boundary"] == "inclusive"})
    else:
        out.append({"kind": "time", "scope": st.get("time", "current")})
    out.append({"kind": "subject", "allowed": ["patient"] + (["first-degree"] if "first-degree" in st.get("subject", "") else [])})
    out.append({"kind": "status", "allowed": [st.get("status", "present")]})
    if kind == "class":
        out.append({"kind": "concept", "class": st["class_id"]})
    return out


def same(a, b):
    """Two constraint lists agree (units are not compared: struct carries none)."""
    key = lambda cs: sorted((c["kind"], sorted((k, str(v)) for k, v in c.items() if k not in ("kind", "unit"))) for c in cs)
    return a is not None and b is not None and key(a) == key(b)
