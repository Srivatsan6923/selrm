"""Deterministic criterion parser (STAGE2_SPEC section 7). No model.
parse_criterion(rule_text, condition) finds the clause of the rule text that states `condition` and returns its
constraints, one dict per kind:
  {"kind": "value", "op": "gt|ge|lt|le", "thr": float, "unit": str}
  {"kind": "time", "scope": "current|ever|window", "n": int, "unit": "day|week|month|year", "inclusive": bool}
  {"kind": "subject", "allowed": ["patient"] or ["patient", "first-degree"]}
  {"kind": "status", "allowed": ["present"]}
  {"kind": "concept", "class": <onto id>}          only when `classes` (label -> id) is given and a label occurs
It returns None when no clause, or more than one, matches the condition (the parser abstains; coverage counts it).
Developed on dev portions only (rule_v1/dev; rule_v2/dev, reg_v1/dev, mcv_v1/dev when registered)."""
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
EXCLUSIVE = r"less than|fewer than|exclusive|does not count|not counted"


def stems(text):
    return {w if w[0].isdigit() else w[:5] for w in re.findall(r"\d+(?:\.\d+)?|[a-z][a-z0-9-]*", text.lower()) if w not in STOP}


def clauses(text):
    """Clauses of a rule text. Commas and semicolons inside parentheses do not split."""
    t = re.sub(r"\([^)]*\)", lambda m: re.sub(r"[,;:]", "\x00", m.group(0)), text)
    parts = re.split(r"[;:](?:\s|$)|\.(?:\s|$)|,\s| (?:and|or) (?=the |a current )| if | for ", t)
    return [p.replace("\x00", ",").strip() for p in parts if p and p.strip()]


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
    for pat, op in VALUE:
        m = re.search(pat, low)
        if m:
            out.append({"kind": "value", "op": op, "thr": float(m.group(1)), "unit": m.group(2)})
            break
    w = re.search(WINDOW, low)
    if w:
        out.append({"kind": "time", "scope": "window", "n": int(float(w.group(1))), "unit": w.group(2),
                    "inclusive": not re.search(EXCLUSIVE, low)})
    else:
        out.append({"kind": "time", "scope": "ever" if re.search(EVER, low) else "current"})
    out.append({"kind": "subject", "allowed": ["patient"] + (["first-degree"] if "first-degree relative" in low else [])})
    out.append({"kind": "status", "allowed": ["present"]})
    hits = [cid for label, cid in (classes or {}).items() if re.search(rf"\b{re.escape(label.lower())}\b", low)]
    if len(set(hits)) == 1:
        out.append({"kind": "concept", "class": hits[0]})
    return out


def parse_criterion(rule_text, condition, classes=None):
    c = find_clause(rule_text, condition)
    return None if c is None else parse_clause(c, classes)
