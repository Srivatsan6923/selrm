"""ec_v1: registered eligibility criteria as executable programs, rendered as triplets.

A formalised criterion (ec_v1/formalized.json; scripts/build_ec_v1.py) becomes a one-criterion
program. Criteria without a time window run through the frozen engine (selrm/engine.py): same
phrase banks (test split), invariants, near-miss kinds and presentation edits as rule_v1. Window
criteria ("within N days/weeks/months/years") use dated events and a stated visit date, as in
selrm/xr.py; the day exactly N units before the visit counts.

Records follow role C's interface for registered criteria: rule_text = "Inclusion criterion: <text>"
or "Exclusion criterion: <text>", condition = the criterion text, conclusion claims only, with
s = "The patient does not meet this criterion." (correct on base and near-miss) and
s' = "The patient meets this criterion." (correct on the flip).
"""
from __future__ import annotations

import datetime as dt
import random
import re
from dataclasses import asdict

from selrm import engine as E
from selrm import phrases as P
from selrm import rules_grammar as RG
from selrm import xr
from selrm.rules import FIRST_DEGREE, OPS, Criterion, Rule
from selrm.schema import validate
from selrm.smoke import ledger_to_prose

SET = "ec_v1"
CLAIMS = ("The patient does not meet this criterion.", "The patient meets this criterion.")
SETTING = "Screening visit for a clinical trial."
# numeric rendering: decimals, near-miss window, plausible range
NUM = {"platelets": (0, 8, 5, 900), "creatinine": (1, 0.2, 0.3, 12), "egfr": (0, 5, 5, 140),
       "hemoglobin": (1, 0.5, 4, 19), "alt_enzyme": (0, 10, 5, 900), "potassium": (1, 0.2, 2.2, 7.5),
       "inr": (1, 0.2, 0.8, 6), "neutrophils": (1, 0.2, 0.1, 20), "wbc": (1, 0.8, 0.5, 40),
       "bmi": (1, 1.5, 14, 70), "weight": (0, 4, 30, 220), "age": (0, 4, 18, 95), "sbp": (0, 8, 60, 230),
       "heart_rate": (0, 5, 30, 180), "temperature": (1, 0.3, 34.5, 41.5), "spo2": (0, 2, 70, 100),
       "rr": (0, 3, 6, 50), "bun": (0, 4, 3, 150)}


def keywords(concept):
    from selrm.library import LIBRARY
    return tuple(sorted({k for r in LIBRARY for c in r.criteria if c.concept == concept for k in c.keywords}))


def full_text(f):
    return f"{f['criterion_type'].capitalize()} criterion: {f['rule_text']}"


# plausible values for every case; a criterion whose threshold leaves no plausible value on one side is
# excluded (scripts/build_ec_v1.py guard), so the hard limits of NUM are only a fallback
SOFT = {"platelets": (20, 600), "creatinine": (0.4, 10), "egfr": (8, 130), "hemoglobin": (6, 18),
        "alt_enzyme": (8, 600), "potassium": (2.8, 6.8), "inr": (0.8, 5), "neutrophils": (0.2, 15), "wbc": (1.0, 30),
        "bmi": (17, 60), "weight": (45, 160), "age": (18, 95), "sbp": (80, 200), "heart_rate": (40, 160),
        "temperature": (35.8, 40.5), "spo2": (80, 100), "rr": (10, 40), "bun": (5, 120)}


def criterion(f):
    """The program of a formalised criterion as a rule_v1 Criterion (cid 'c')."""
    kinds = tuple(f["near_kinds"])
    if f["input"] == "numeric":
        dec, nd, lo, hi = NUM[f["concept"]]
        slo, shi = SOFT[f["concept"]]
        t = f["threshold"]
        side = 8 * nd
        if f["op"] in (">", ">="):
            dr = (max(slo if slo < t - nd else lo, t - side), t - nd / 2)
            fr = (t, min(shi if shi > t + nd / 2 else hi, t + side))
        else:
            dr = (t + nd / 2, min(shi if shi > t + nd else hi, t + side))
            fr = (max(slo if slo < t - nd / 2 else lo, t - side), t)
        return Criterion("c", f["concept"], "numeric", f["rule_text"], keywords(f["concept"]), op=f["op"],
                         threshold=t, default_range=dr, flip_range=fr, near_delta=nd, decimals=dec,
                         nm=tuple(k for k in kinds if k in ("numeric", "time")) or ("numeric",))
    return Criterion("c", f["concept"], "finding", f["rule_text"], keywords(f["concept"]),
                     counts_past=f["times"] == "ever", counts_family=f["subjects"] == "family",
                     nm=tuple(k for k in kinds if k in ("subject", "negation", "time")))


def population(f):
    """Sex and age range of the cases: the formalisation's sex restriction, then the trial's registered
    sex and ages (ec_v1/registry_population.json), within the generator's adult range."""
    p = f.get("population") or {}
    sex = "female" if f["sex"] == "female" or p.get("sex") == "FEMALE" else \
        "male" if f["sex"] == "male" or p.get("sex") == "MALE" else None
    lo = max(18, int(p.get("min_age") or 0), 20 if sex == "female" else 30)
    hi = min(95, int(p.get("max_age") or 95), 44 if f["concept"] == "pregnancy" else 85)
    return sex, (lo, hi) if lo <= hi else (max(18, int(p.get("min_age") or 18)), hi)


def rule(f):
    sex, ages = population(f)
    return Rule(f"ec_{f['cand']}", "constraint", f["nct_id"], full_text(f).replace("{", "{{").replace("}", "}}"),
                [criterion(f)], SETTING, default="(not met)", alternative="(met)", sex=sex, age_range=ages,
                family="ec", logic="any")


def time_unsettled(f):
    """A current-only finding whose text does not say whether a past occurrence counts: the formaliser
    left out the time near-miss, and no case states a past occurrence. Rescued rows lost the time kind
    for another reason (scripts/build_ec_v1.py RESCUE), so their time scope stays settled."""
    return f["input"] == "finding" and f["times"] == "current" and "time" not in f["near_kinds"] \
        and not f.get("rescued")


def kinds(f):
    """Near-miss kinds to render: those the formalisation allows that the engine can build."""
    if f["times"] == "window":
        return [k for k in f["near_kinds"] if k in ("time", "subject", "negation")]
    c = criterion(f)
    return [k for k in f["near_kinds"] if k in E.nm_kinds(c) and (k != "boundary" or c.op in ("<", ">"))
            and not (k == "boundary" and age_arguable(f))]


def age_arguable(f):
    """Ages are stated in completed years, so 'over 65' or '65 or younger' is arguable for a patient
    aged 65; 'below 70' and '70 or older' are not."""
    return f["concept"] == "age" and f["op"] in (">", "<=")


def _to_ec(recs, f):
    """Engine records -> ec_v1 records: conclusion claims only, C's claim texts."""
    out = []
    for r in recs:
        if r["claim_type"] != "conclusion":
            continue
        r = dict(r, rule_text=full_text(f), condition=f["rule_text"], claim_text=CLAIMS[r["claim_role"] == "s_prime"],
                 iid=r["iid"], meta=dict(r["meta"], nct_id=f["nct_id"], criterion_type=f["criterion_type"],
                                         cand=f["cand"]))
        validate(r)
        out.append(r)
    return out


# ---------------------------------------------------------------- window criteria
UNIT_DAYS = {"days": 1, "weeks": 7}
REL_EVENT = {"stroke": "{Poss} {rel} had a stroke {when}.", "vte": "{Poss} {rel} was treated for a DVT {when}.",
             "bleeding": "{Poss} {rel} had a major bleed {when}.",
             "vascular": "{Poss} {rel} had a heart attack {when}.", "fall": "{Poss} {rel} fell at home {when}."}


def window_start(visit, n, unit):
    if unit in UNIT_DAYS:
        return visit - dt.timedelta(days=n * UNIT_DAYS[unit])
    return xr.add_months(visit, -n * (12 if unit == "years" else 1))


def event_holds(f, state):
    visit = next(dt.date.fromisoformat(m.value) for m in state if m.kind == "date")
    start = window_start(visit, f["window_n"], f["window_unit"])
    for m in state:
        if m.concept != f["concept"] or m.status != "present":
            continue
        if m.subject != "patient" and not (f["subjects"] == "family" and m.subject in FIRST_DEGREE):
            continue
        if m.date and dt.date.fromisoformat(m.date) >= start:
            return True
    return False


def _when(visit, d, unit, form):
    if form == "dated":
        return f"on {d.day} {xr.MONTHS[d.month - 1]} {d.year}" if unit in UNIT_DAYS else \
            f"in {xr.MONTHS[d.month - 1]} {d.year}"
    days = (visit - d).days
    if unit == "days" or (unit == "weeks" and days < 14):
        return f"{days} day{'s' * (days != 1)} ago"
    if unit == "weeks":
        return f"{days // 7} weeks ago"
    months = (visit.year - d.year) * 12 + visit.month - d.month
    return f"{months // 12} years ago" if unit == "years" else f"{months} month{'s' * (months != 1)} ago"


def window_group(f, kind, seed):
    """base (nothing said), flip (event inside the window), near-miss (outside the window,
    another person inside it, or an explicit denial) and a presentation edit."""
    rng = random.Random(f"{SET}/{f['cand']}/{kind}/{seed}")
    n, unit, c = f["window_n"], f["window_unit"], f["concept"]
    visit = dt.date(rng.choice((2024, 2025)), rng.randint(1, 12), rng.randint(1, 28))
    step = UNIT_DAYS.get(unit)
    span = n * step if step else None

    def at(inside):
        if step:                                    # day-level dates
            k = rng.randint(1, max(1, span - max(1, span // 4))) if inside else \
                rng.randint(span + max(2, span // 3), 3 * span + 2)
            return visit - dt.timedelta(days=k)
        months = n * (12 if unit == "years" else 1)
        k = rng.randint(1, max(1, months - 2)) if inside else rng.randint(months + 2, months + 30)
        return xr.add_months(visit, -k)
    form = rng.choice(("relative", "dated"))
    sex = population(f)[0] or rng.choice(("female", "male"))
    poss = "Her" if sex == "female" else "His"
    age = rng.randint(*population(f)[1])
    # within days or weeks: no finished course of treatment, and no line that dates the treatment, not the event
    tpl = [t for t in xr.EVENTS[c][2] if not (step and ("completed" in t or t.startswith("Was treated for")))]

    def event(d, subject="patient"):
        when = _when(visit, d, unit, form)
        if subject == "patient":
            j = rng.randrange(len(tpl))
            return xr.XMention(c, "finding", True, "patient", "present", "past", d.isoformat(), f"event{j}"), \
                tpl[j].format(when=when)
        return xr.XMention(c, "finding", True, subject, "present", "past", d.isoformat(), "rel_event"), \
            REL_EVENT[c].format(Poss=poss, rel=subject, when=when)
    flip = event(at(True))
    if kind == "time":
        near = event(at(False))
    elif kind == "subject":
        others = [p for p in P.persons(c, "test", age) if not (f["subjects"] == "family" and p in FIRST_DEGREE)]
        near = event(at(True), rng.choice(others))
    else:
        near = (xr.XMention(c, "finding", True, "patient", "absent", "current", None, "never"), xr.NEVER[c])
    hdr = rng.choice(P.ids(P.HEADER, "test"))
    noun = "woman" if sex == "female" else "man"

    def head(h):
        return P.HEADER[h].format(age=age, noun=noun, Noun=noun.capitalize(), sex=sex, Sex=sex.capitalize())
    kw = keywords(c) + xr.EVENTS[c][1]
    fill = [P.FILLERS[j] for j in rng.sample([j for j in P.ids(P.FILLERS, "test")
                                              if not any(k in P.FILLERS[j].lower() for k in kw)], rng.randint(1, 3))]
    visit_m = xr.XMention("visit_date", "date", visit.isoformat(), form="visit")
    date_line = f"Visit date: {visit.day} {xr.MONTHS[visit.month - 1]} {visit.year}."
    pos = rng.randint(0, len(fill))

    def case(h, target, order=None):
        body = fill[:pos] + ([target[1]] if target else []) + fill[pos:]
        if order:
            body = [body[i] for i in order]
        return {"text": "\n".join([head(h), date_line, SETTING] + body),
                "state": [visit_m] + ([target[0]] if target else []), "line": target[1] if target else None}
    order = list(range(len(fill)))
    while len(order) > 1 and order == sorted(order):
        rng.shuffle(order)
    cases = {"base": case(hdr, None), "flip": case(hdr, flip), "near": case(hdr, near),
             "pres": case(rng.choice([h for h in P.ids(P.HEADER, "test") if h != hdr]), None, order)}
    tid = f"{SET}.test.ec_{f['cand']}.c.{kind}.easy.{seed}"
    out = []
    for k, cs in cases.items():
        y = int(event_holds(f, cs["state"]))
        led = [{"need": f["rule_text"], "found": cs["line"], "subject": "patient" if m.subject == "patient"
                else f"other ({m.subject})", "status": m.status, "time": "current" if not m.date else
                f"past ({(visit - dt.date.fromisoformat(m.date)).days} days before the visit date)"}
               for m in cs["state"] if m.concept == c] or \
              [{"need": f["rule_text"], "found": "not mentioned", "subject": "patient", "status": "absent",
                "time": "current"}]
        common = dict(tid=tid, set=SET, split="test", tier="easy", level="registered", rid=f"ec_{f['cand']}", cid="c",
                      family="ec", nm_kind=kind, case_kind=k, rule_text=full_text(f), case_text=cs["text"],
                      condition=f["rule_text"], state=[asdict(m) for m in cs["state"]], ledger=led,
                      prose=ledger_to_prose(led),
                      meta={"nct_id": f["nct_id"], "criterion_type": f["criterion_type"], "cand": f["cand"],
                            "keywords": list(kw), "criterion_holds": y, "seed": seed, "overrides": {},
                            "tpl": [], "tpl_split": "test", "window": [n, unit]})
        for role, text in zip(("s", "s_prime"), CLAIMS):
            r = dict(common, iid=f"{tid}/{k}/conclusion/{role}", claim_type="conclusion", claim_role=role,
                     claim_text=text, label=int((role == "s_prime") == (y == 1)))
            validate(r)
            out.append(r)
    return out


# ---------------------------------------------------------------- groups and tests
def groups(f, seeds=(0,)):
    """Records of every (near-miss kind, seed) group of one criterion: one group per kind, so that the
    authors' sign-off covers every case of the set."""
    out = []
    for kind in kinds(f):
        for seed in seeds:
            if f["times"] == "window":
                out += window_group(f, kind, seed)
            else:
                out += _to_ec(_engine_group(f, kind, seed), f)
    return out


PRESENT_ONLY = re.compile(r"(?i)\b(at present|currently|current|now|today|at the moment|presently)\b")


def _engine_group(f, kind, seed):
    """One engine group. For a criterion that counts past occurrences, a general line scoped to the
    present ('No allergies at present.') leaves the past open, so such a draw is replaced by the
    next seed (seed + 1000, ...)."""
    generic = set(P.BANKS.get(f["concept"], {}).get("generic", []))
    for s in range(seed, seed + 50_000, 1000):
        recs = E.make_group(rule(f), "c", kind, "easy", "test", s, SET, "registered")
        if f["times"] != "ever" or not any(line in generic and PRESENT_ONLY.search(line) for r in recs
                                           for line in r["case_text"].split("\n")):
            return recs
    raise RuntimeError("every draw has a present-scoped general line")


def boundary_tests(f):
    """Executed checks shown on the sign-off sheet: value or occurrence -> met?"""
    if f["input"] == "numeric":
        dec, nd, lo, hi = NUM[f["concept"]]
        step = 10 ** -dec
        t = f["threshold"]
        vals = (round(t - step, dec), t, round(t + step, dec))
        if age_arguable(f):
            vals = (round(t - step, dec), round(t + step, dec))    # no case states the age at the threshold
        return [(f"current value {E.fmt(v, criterion(f))}", OPS[f["op"]](v, t)) for v in vals]
    if f["times"] == "window":
        visit = dt.date(2025, 3, 15)
        start = window_start(visit, f["window_n"], f["window_unit"])
        mk = lambda d: [xr.XMention("visit_date", "date", visit.isoformat()),  # noqa: E731
                        xr.XMention(f["concept"], "finding", True, "patient", "present", "past", d.isoformat())]
        return [(f"visit {visit}, event on {d} ({lab})", event_holds(f, mk(d)))
                for d, lab in ((start, "boundary day"), (start - dt.timedelta(days=1), "one day earlier"),
                               (visit - dt.timedelta(days=1), "day before the visit"))]
    from selrm.rules import Mention
    c = criterion(f)
    rows = [("patient, present now", Mention(f["concept"], "finding"))]
    if not time_unsettled(f):                      # otherwise the text does not decide it, and no case shows it
        rows.append(("patient, past or resolved", Mention(f["concept"], "finding", time="past")))
    rows += [("patient, explicit denial", Mention(f["concept"], "finding", status="absent")),
             ("sister, present now", Mention(f["concept"], "finding", subject="sister")),
             ("friend, present now", Mention(f["concept"], "finding", subject="friend"))]
    return [(lab, c.evaluate([m])) for lab, m in rows] + [("not mentioned", c.evaluate([]))]


DISPLAY = {"mech_valve": "a mechanical heart valve", "hit": "heparin-induced thrombocytopenia",
           "pen_allergy": "a penicillin allergy", "sulfa_allergy": "a sulfonamide allergy",
           "contrast_allergy": "an allergy to iodinated contrast", "peptic_ulcer": "a peptic ulcer",
           "vascular": "a myocardial infarction or peripheral artery disease",
           "vte": "a venous thromboembolism", "chf": "heart failure", "cad": "coronary artery disease",
           "bleeding": "a major bleed", "stroke": "a stroke or TIA", "cancer": "cancer", "asthma": "asthma",
           "diabetes": "diabetes", "hypertension": "hypertension", "pregnancy": "pregnancy",
           "angioedema": "angioedema", "warfarin": "warfarin treatment", "aspirin": "aspirin use",
           "lithium": "lithium treatment", "methotrexate": "methotrexate treatment",
           "clarithromycin": "clarithromycin treatment", "fall": "a fall"}
NUMERIC = {"hemoglobin": ("hemoglobin", "g/dL"), "neutrophils": ("neutrophil count", "x10^9/L"),
           "bmi": ("body mass index", "kg/m2"), "inr": ("INR", ""), "age": ("age", "years")}


def program_text(f):
    if f["input"] == "numeric":
        name, u = NUMERIC.get(f["concept"]) or RG.NUMERIC_NAMES.get(f["concept"], (f["concept"], ""))
        return f"met iff the patient's current {name} {f['op']} {f['threshold']:g} {u}".strip()
    who = "the patient or a first-degree relative" if f["subjects"] == "family" else "the patient"
    when = {"current": "now (the criterion does not say whether a past occurrence counts; no case states one)"
            if time_unsettled(f) else "now (current)", "ever": "at any time (current or past)",
            "window": f"within the {f['window_n']} {f['window_unit']} before the visit date (boundary day counts)"}[f["times"]]
    extra = f"; also listed in the text but never mentioned in cases: {', '.join(f['other_disjuncts'])}" \
        if f["other_disjuncts"] else ""
    what = "a myocardial infarction (heart attack)" if f["concept"] == "vascular" and f["times"] == "window" \
        else DISPLAY.get(f["concept"], f["concept"].replace("_", " "))     # window cases render heart attacks only
    return f"met iff {who} has {what} {when}{extra}"


def rendered_ok(recs):
    """Text checks on rendered cases: no unfilled slot; ledger quotes occur in the case."""
    bad = []
    for r in recs:
        t = r["case_text"]
        if "None" in t or "{" in t or "}" in t:
            bad.append((r["iid"], "unfilled slot"))
        for e in r["ledger"]:
            if e["found"] != "not mentioned" and e["found"] not in t:
                bad.append((r["iid"], "ledger quote not in case"))
    return bad
