"""Gate of Ledger-RM-G (STAGE2_SPEC section 7): recompute `applies` from the reader's record and the parsed
criterion. gate(record, constraints, case, ref_date, onto) -> {"checks": {...}, "applies": 1 | 0 | None}.
record: list of entries {need, found, subject, status, time[, concept]}. Each check is 1, 0 or None (not
computable). An entry applies when every check is 1; the record applies when some entry does (three-valued: None
when no entry is all 1 but one has no 0). `checks` are those of the deciding entry.
onto: {"closure": {class id: [member ids]}}."""
import calendar, datetime, re

FIRST_DEGREE = {"mother", "father", "parent", "sister", "brother", "sibling", "son", "daughter", "child"}
OPS = {"gt": lambda x, t: x > t, "ge": lambda x, t: x >= t, "lt": lambda x, t: x < t, "le": lambda x, t: x <= t}
KINDS = ("quotation", "value", "time", "concept", "subject", "status")


def shift(d, n, unit):
    """d minus n units; month and year steps clamp the day to the month's length."""
    if unit in ("day", "week"):
        return d - datetime.timedelta(days=n * (7 if unit == "week" else 1))
    m = d.year * 12 + d.month - 1 - n * (12 if unit == "year" else 1)
    y, mo = divmod(m, 12)
    return datetime.date(y, mo + 1, min(d.day, calendar.monthrange(y, mo + 1)[1]))


def entry_dates(time):
    """'past (2024-06-15)' -> (day, day); 'past (2024-06)' -> the month; 'past (2024)' -> the year; else None."""
    m = re.fullmatch(r"past \((\d{4})(?:-(\d{2}))?(?:-(\d{2}))?\)", time)
    if not m:
        return None
    y, mo, d = (int(x) if x else None for x in m.groups())
    lo = datetime.date(y, mo or 1, d or 1)
    hi = lo if d else datetime.date(y, mo or 12, calendar.monthrange(y, mo or 12)[1])
    return lo, hi


def time_check(time, c, ref_date):
    if time == "current" or c["scope"] == "ever":
        return 1
    if c["scope"] == "current":
        return 0
    span = entry_dates(time)
    if span is None or ref_date is None:
        return None
    ref = datetime.date.fromisoformat(ref_date) if isinstance(ref_date, str) else ref_date
    start = shift(ref, c["n"], c["unit"])            # the boundary day
    after = lambda d: d >= start if c["inclusive"] else d > start
    if after(span[0]) and span[1] <= ref:            # the whole span is inside the window
        return 1
    return 0 if not after(span[1]) or span[0] > ref else None    # wholly outside, else the span straddles an end


def value_check(found, c):
    m = re.search(r"-?\d+(?:\.\d+)?", found)
    # ponytail: no unit conversion; rule_v1 records carry bare numbers. Add a unit table when a dev set has units.
    return int(OPS[c["op"]](float(m.group(0)), c["thr"])) if m else None


def subject_check(subject, c):
    if subject == "patient":
        return 1
    who = subject[len("other ("):-1] if subject.startswith("other (") else subject
    return int("first-degree" in c["allowed"] and who in FIRST_DEGREE)


def entry_checks(e, constraints, case, ref_date, onto):
    ws = lambda s: " ".join(s.split())
    ch = {"quotation": int(e["found"] == "not mentioned" or ws(e["found"]) in ws(case))}
    for c in constraints:
        k = c["kind"]
        if k == "value":
            ch[k] = value_check(e["found"], c)
        elif k == "time":
            ch[k] = time_check(e["time"], c, ref_date)
        elif k == "subject":
            ch[k] = subject_check(e["subject"], c)
        elif k == "status":
            ch[k] = int(e["status"] in c["allowed"])
        elif k == "concept":
            members = ((onto or {}).get("closure") or {}).get(c["class"])
            ch[k] = None if members is None or not e.get("concept") else int(e["concept"] in members)
    return ch


def gate(record, constraints, case, ref_date=None, onto=None):
    if constraints is None:                          # the parser abstained
        return {"checks": dict.fromkeys(KINDS), "applies": None}
    best, rank = None, -1
    for e in record:
        ch = entry_checks(e, constraints, case, ref_date, onto)
        r = 0 if 0 in ch.values() else 1 if None in ch.values() else 2
        if r > rank:
            best, rank = ch, r
    if best is None:                                 # empty record: nothing found
        return {"checks": dict.fromkeys(KINDS), "applies": 0}
    return {"checks": {k: best.get(k) for k in KINDS}, "applies": (0, None, 1)[rank]}
