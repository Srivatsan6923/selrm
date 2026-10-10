"""mcv_v1 items: criterion claims on untouched notes, values naturally near a threshold, and value edits.

Everything is computed through the score specifications: a threshold is where an item's points change when
one released value is moved, so no unit table is needed and the labels of edited cases come from the rule code
on the edited dictionary (STAGE2_TASKS_A, A1.3).
"""
import copy
import hashlib
import re

from selrm import mcv

# Band of a value "naturally near a threshold": the item's points change when the released value moves by this
# much. Absolute for age and temperature, relative otherwise (rates, pressures, laboratory values).
BAND_ABS = {"years": 3, "months": 36, "degrees celsius": 0.5, "degrees fahrenheit": 0.9}
BAND_REL = 0.10

# A note that already says the value in words is not edited for that input.
WORDS = {
    "heart rate": r"tachycardi|bradycardi",
    "pulse": r"tachycardi|bradycardi",
    "respiratory rate": r"tachypn|bradypn",
    "temperature": r"febrile|fever|pyrexi|hypotherm|hypertherm",
    "blood pressure": r"hypotens|hypertens|normotens|shock",
    "age": r"elderly|geriatric|middle-aged|young|adolescent|child|infant|toddler|teenage|octogenarian|nonagenarian|septuagenarian",
    "o₂ saturation": r"hypox|desaturat",
    "pao2": r"hypox",
    "sodium": r"hyponatr|hypernatr",
    "potassium": r"hypokal|hyperkal",
    "hemoglobin": r"an(a)?emi",
    "hematocrit": r"an(a)?emi|polycyth",
    "white blood cell": r"leu[ck]ocytosis|leu[ck]openi|neutropeni",
    "platelet": r"thrombocytopeni|thrombocytosis",
    "creatinine": r"renal failure|kidney injury|renal insufficiency|azot(a)?emi",
    "bun": r"azot(a)?emi|ur(a)?emi",
    "bilirubin": r"jaundice|icter|hyperbilirubin",
    "glucose": r"hyperglyc|hypoglyc",
    "albumin": r"hypoalbumin",
    "body mass index": r"obes|overweight|underweight",
    "inr": r"coagulopath",
    "ph": r"acidosis|alkalosis|acid(a)?emi|alkal(a)?emi",
}


def fmt(k):
    return str(int(k)) if float(k) == int(k) else str(k)


def claim(score, item, k):
    return f"Under the {score.name}, the item '{item.name}' scores {fmt(k)} point{'' if abs(k) == 1 else 's'} for this patient."


def finite(item):
    return all(isinstance(v, (int, float)) for v in item.levels) and len(item.levels) > 1


def other_level(item, k, target=None):
    """The level the s_prime claim names: the edit's target, else the nearest other level (ties: the lower)."""
    if target is not None:
        return target
    return min((v for v in item.levels if v != k), key=lambda v: (abs(v - k), v))


def slug(name):
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:40]


def struct(item):
    return {"kind": item.kind, "inputs": list(item.inputs), "levels": list(item.levels), "subject": item.subject,
            "time": item.time, "thresholds": {k: [u, list(c)] for k, (u, c) in item.thresholds.items()},
            "support": dict(item.support)}


def _records(score, item, i, row, definition, tid, case_kind, text, ent, k_s, k_sp, extra):
    """The two claim records of one case. s names k_s, s_prime names k_sp; the label is from the rule code."""
    pts = item.points(ent)
    out = []
    for role, k in (("s", k_s), ("s_prime", k_sp)):
        rec = {
            "iid": f"{tid}/{case_kind}/criterion/{role}", "tid": tid, "set": "mcv_v1", "split": extra["split"],
            "tier": "external", "level": "external", "rid": f"c{score.cid}", "cid": f"{i:02d}_{slug(item.name)}",
            "family": score.name, "nm_kind": extra.get("nm_kind", "none"), "case_kind": case_kind,
            "rule_text": definition, "case_text": text, "condition": item.name, "claim_type": "criterion",
            "claim_role": role, "claim_text": claim(score, item, k), "label": int(pts == k),
            "state": [], "ledger": [], "prose": "",
            "meta": {"row": int(row["Row Number"]), "note_id": row["Note ID"], "calculator_id": score.cid,
                     "points": pts, "claimed_points": k, **extra.get("meta", {})},
            "crit": {"source": "stated", "provenance": f"MedCalc-Bench Verified {mcv.PIN['tag']}, score text of the instance",
                     "text_sha": hashlib.sha256(definition.encode("utf-8")).hexdigest()},
            "cluster": row["Note ID"], "note_type": "human" if row["Note Type"] == "Extracted" else "model",
            "stratum": mcv.stratum(item, row["ent"]), "struct": struct(item),
        }
        if "edit_type" in extra:
            rec["edit_type"] = extra["edit_type"]
        out.append(rec)
    return out


def definitions(rows):
    """{cid: the one score definition of the calculator}; rows that ship none (28 SOFA rows) take it."""
    out = {}
    for r in rows:
        t = mcv.score_text(r["Ground Truth Explanation"])
        if t is not None:
            assert out.setdefault(r["cid"], t) == t, f"calculator {r['cid']} ships two definitions"
    return out


def criteria(rows, specs, defs, split="test"):
    """One record pair per finite-level item of every score on every note."""
    out = []
    for r in rows:
        s = specs[r["cid"]]
        for i, it in enumerate(s.items):
            if finite(it):
                k = it.points(r["ent"])
                tid = f"mcv_{split}_{int(r['Row Number']):05d}_{i:02d}"
                out += _records(s, it, i, r, defs[r["cid"]], tid, "base", r["Patient Note"], r["ent"], k,
                                other_level(it, k), {"split": split})
    return out


# ---- thresholds found through the rule code ---------------------------------------------------------------
def _with(ent, key, value):
    e = copy.copy(ent)
    e[key] = [value, ent[key][1]] if isinstance(ent[key], (list, tuple)) else value
    return e


def _raw(ent, key):
    v = ent.get(key)
    v = v[0] if isinstance(v, (list, tuple)) else v
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def _unit(ent, key):
    v = ent.get(key)
    return str(v[1]).strip().lower() if isinstance(v, (list, tuple)) else ""


def band(ent, key):
    v, u = _raw(ent, key), _unit(ent, key)
    return BAND_ABS[u] if u in BAND_ABS else abs(v) * BAND_REL


def near_threshold(item, ent):
    """Input keys whose released value is within the band of a point where the item's points change."""
    base, out = item.points(ent), []
    for key in item.thresholds:
        v = _raw(ent, key)
        if v is None:
            continue
        b = band(ent, key)
        if any(_safe(item, _with(ent, key, v + d)) not in (base, None) for d in (-b, b)):
            out.append(key)
    return out


def _safe(item, ent):
    try:
        return item.points(ent)
    except Exception:
        return None


def natural_band(records, rows, specs):
    """criteria records of numeric items whose value lies in the band of a threshold (no edit)."""
    by_row = {int(r["Row Number"]): r for r in rows}
    out = []
    for rec in records:
        r = by_row[rec["meta"]["row"]]
        it = specs[r["cid"]].items[int(rec["cid"][:2])]
        keys = near_threshold(it, r["ent"]) if it.thresholds else []
        if keys:
            rec = copy.deepcopy(rec)
            rec["meta"]["band_inputs"] = keys
            out.append(rec)
    return out


# ---- value edits ------------------------------------------------------------------------------------------
def decimals(v):
    s = repr(float(v)) if not float(v).is_integer() else str(int(v))
    return len(s.split(".")[1]) if "." in s else 0


def value_pattern(v):
    """The value as a number token: 126 also as 126.0; 7.3 also as 7.30. No digit or decimal point around it."""
    if float(v).is_integer():
        core = rf"{int(v):d}(?:\.0+)?"
        core = core.replace("-", r"\-")
    else:
        core = re.escape(repr(float(v))) + "0*"
    return re.compile(rf"(?<![\d.,]){core}(?![\d]|[.,]\d)")


def plausible(rows):
    """{(cid, key, unit): (lowest, highest released value)} over the given rows: the range edits stay inside."""
    out = {}
    for r in rows:
        for key in r["ent"]:
            v = _raw(r["ent"], key)
            if v is not None:
                k = (r["cid"], key, _unit(r["ent"], key))
                lo, hi = out.get(k, (v, v))
                out[k] = (min(lo, v), max(hi, v))
    return out


def change_point(item, ent, key, direction, lo, hi):
    """Walking from the released value in one direction in steps of its own precision: the first value at
    which the item's points change, and the last value before it. None if no change inside [lo, hi]."""
    v = _raw(ent, key)
    d = decimals(v)
    step = 10 ** -d
    base, prev = item.points(ent), v
    n = 0
    while True:
        n += 1
        x = round(v + direction * n * step, d)
        if x < lo or x > hi or n > 200000:
            return None
        p = _safe(item, _with(ent, key, x))
        if p is None:
            return None
        if p != base:
            return x, prev, p
        prev = x


def value_edit(item, ent, key, lo, hi):
    """(flip value, near value, flipped points) for one input, or None.

    Flip: the nearest value across the nearest threshold, moved on by 5% of it (at least one step, at most
    half the distance walked) while the points stay those just across, so a flip never crosses a second bound.
    Near-miss: on the original side, strictly nearer to the threshold, at least one step from both.
    """
    v = _raw(ent, key)
    d = decimals(v)
    step = 10 ** -d
    cands = [c + (direction,) for direction in (1, -1) if (c := change_point(item, ent, key, direction, lo, hi))]
    if not cands:
        return None
    first, last, pts, direction = min(cands, key=lambda c: (abs(c[0] - v), -c[3]))
    gap = round(abs(last - v) / step)
    if gap < 2:                                  # no room for a strictly nearer value on the same side
        return None
    near = round(v + direction * (gap // 2 + gap % 2) * step, d)
    flip = first
    margin = min(gap // 2, max(1, round(0.05 * abs(first) / step)))
    for n in range(max(1, margin), 0, -1):       # move on while the points stay the flipped level
        x = round(first + direction * n * step, d)
        if lo <= x <= hi and _safe(item, _with(ent, key, x)) == pts and all(
                _safe(item, _with(ent, key, round(first + direction * m * step, d))) == pts for m in range(n)):
            flip = x
            break
    if _safe(item, _with(ent, key, near)) != item.points(ent) or near in (v, last + direction * step):
        return None
    return flip, near, pts


def render_value(v, d):
    return f"{v:.{d}f}"


def edit_note(note, v, new):
    """Replace the single occurrence of the value by the new one, keeping its written precision; else None."""
    pat = value_pattern(v)
    hits = list(pat.finditer(note))
    if len(hits) != 1:
        return None
    m = hits[0]
    written = m.group(0)
    d = len(written.split(".")[1]) if "." in written else 0
    d = max(d, decimals(new))
    return note[:m.start()] + render_value(new, d) + note[m.end():]


def said_in_words(note, key):
    low, k = note.lower(), key.lower()
    return any(name in k and re.search(pat, low) for name, pat in WORDS.items())


def second_form(note, row_units, key, unit):
    """True if the note carries a number in another unit seen for this input (a second form of the value)."""
    others = {u for u in row_units.get(key, ()) if u != unit and u}
    low = note.lower()
    for u in others:
        short = {"degrees celsius": r"°\s*c\b|celsius", "degrees fahrenheit": r"°\s*f\b|fahrenheit"}.get(u, re.escape(u))
        if re.search(rf"\d\s*(?:{short})", low):
            return True
    return False


def value_edits(rows, specs, defs, ranges, units, split="test"):
    """Triplets (base, flip, near) of numeric items; returns (records, skip counts by reason)."""
    out, skips = [], {}

    def skip(why):
        skips[why] = skips.get(why, 0) + 1

    for r in rows:
        s = specs[r["cid"]]
        feeds = {}
        for it in s.items:
            for k in it.inputs:
                feeds[k] = feeds.get(k, 0) + 1
        for i, it in enumerate(s.items):
            if not finite(it) or not it.thresholds:
                continue
            for key in it.thresholds:
                v = _raw(r["ent"], key)
                if v is None:
                    skip("input not released as a number")
                    continue
                if feeds[key] > 1:
                    skip("value feeds another item")
                    continue
                unit = _unit(r["ent"], key)
                if (r["cid"], key, unit) not in ranges:
                    skip("input and unit not seen in the training rows")
                    continue
                lo, hi = ranges[(r["cid"], key, unit)]
                ed = value_edit(it, r["ent"], key, lo, hi)
                if ed is None:
                    skip("no threshold in range or no room for a near-miss")
                    continue
                if said_in_words(r["Patient Note"], key):
                    skip("note states the value in words")
                    continue
                if second_form(r["Patient Note"], units.get(r["cid"], {}), key, unit):
                    skip("note gives the value in a second unit")
                    continue
                flip_v, near_v, _ = ed
                texts = {"flip": edit_note(r["Patient Note"], v, flip_v), "near": edit_note(r["Patient Note"], v, near_v)}
                if texts["flip"] is None:
                    skip("value string not exactly once in the note")
                    continue
                base_k = it.points(r["ent"])
                ents = {"base": r["ent"], "flip": _with(r["ent"], key, flip_v), "near": _with(r["ent"], key, near_v)}
                flip_k = it.points(ents["flip"])
                assert flip_k != base_k and it.points(ents["near"]) == base_k
                tid = f"mcv_{split}_{int(r['Row Number']):05d}_{i:02d}_v_{slug(key)}"
                texts["base"] = r["Patient Note"]
                for kind in ("base", "flip", "near"):
                    out += _records(s, it, i, r, defs[r["cid"]], tid, kind, texts[kind], ents[kind], base_k, flip_k,
                                    {"split": split, "edit_type": "value", "nm_kind": "numeric",
                                     "meta": {"input": key, "unit": unit, "value": {"base": v, "flip": flip_v, "near": near_v}}})
    return out, skips
