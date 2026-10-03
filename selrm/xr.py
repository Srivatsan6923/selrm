"""Rule-side items (xr_v1): the case is fixed and only the applicability clause of the rule
changes. One item = two rules x three cases (contested, positive, negative); it is solved only if
all six judgments are right (crossed accuracy, XA).

Dimensions (the rule that counts the contested form first):
  window       "at any time" vs "within the W months before the visit date"; or W2 vs W1 months
  currency     "has ever had X (current or past)" vs "currently has X"
  subject      "the patient or a first-degree relative" vs "the patient"
  inclusivity  "T or more" vs "above T" (and "T or less" vs "below T")

Time lives in this module only; rule_v1 has no reference date and no windows, and nothing here
changes its code or hashes. Every case states a visit date (a `visit_date` pseudo-mention in the
state, so the state alone determines the label). An event carries its date; "within the W months
before the visit date" counts an event on or after the date exactly W calendar months before the
visit (that boundary day counts; the rule text says so). Events are rendered as "N months ago" or
as a month and year. They keep at least two months from the window's start (W months before the
visit), and positive events lie 1 to W-2 months before the visit, so the month-level rendering
cannot change a label.
"""
from __future__ import annotations

import calendar
import datetime as dt
import random
from collections import defaultdict
from dataclasses import asdict, dataclass

from selrm import phrases as P
from selrm import rules_grammar as RG
from selrm.rules import FIRST_DEGREE, OPS
from selrm.schema import validate
from selrm.smoke import ledger_to_prose

SET = "xr_v1"
MONTHS = list(calendar.month_name)[1:]


def add_months(d: dt.date, k: int) -> dt.date:
    """d moved by k calendar months; the day is clamped to the end of a shorter month."""
    y, m = divmod(d.month - 1 + k, 12)
    year, month = d.year + y, m + 1
    return dt.date(year, month, min(d.day, calendar.monthrange(year, month)[1]))


@dataclass(frozen=True)
class XMention:
    concept: str
    kind: str                      # finding | numeric | date (the visit date)
    value: object = True
    subject: str = "patient"
    status: str = "present"        # present | absent
    time: str = "current"          # current | past
    date: str | None = None        # ISO date of a dated event (window items)
    form: str = ""
    year: int | None = None


@dataclass(frozen=True)
class XCrit:
    """One condition with an explicit applicability clause."""
    concept: str
    kind: str                      # finding | numeric
    subjects: str = "patient"      # patient | family (patient or first-degree relative)
    times: str = "current"         # current | ever | window
    window: int | None = None      # months, when times == "window"
    op: str | None = None
    threshold: float | None = None

    def applies(self, m: XMention, visit: dt.date) -> bool:
        if m.concept != self.concept:
            return False
        if m.subject != "patient" and not (self.subjects == "family" and m.subject in FIRST_DEGREE):
            return False
        if m.time == "past" and self.times == "current":
            return False
        if self.times == "window" and m.time == "past":
            return m.date is not None and dt.date.fromisoformat(m.date) >= add_months(visit, -self.window)
        return True

    def holds(self, state) -> bool:
        visit = next(dt.date.fromisoformat(m.value) for m in state if m.kind == "date")
        app = [m for m in state if self.applies(m, visit)]
        if self.kind == "finding":
            return any(m.status == "present" for m in app)
        vals = [m.value for m in app if m.status == "present"]
        if len(vals) != 1:
            raise ValueError(f"{self.concept}: expected one applicable value, got {vals}")
        return OPS[self.op](vals[0], self.threshold)


# ---------------------------------------------------------------- inventories
# window: dated events. noun phrase in the rule, keywords, event lines with {when}
EVENTS = {
    "stroke": ("a stroke or TIA", ("stroke", "tia", "transient ischemic"),
               ["Had a transient ischemic attack {when}, with full recovery.",
                "Was admitted with a minor stroke {when} and has recovered.",
                "Had a stroke {when}; no weakness remains."]),
    "vte": ("a venous thromboembolism (DVT or pulmonary embolism)", ("thromb", "dvt", "pulmonary embol"),
            ["Was treated for a deep vein thrombosis of the right leg {when}.",
             "Had a pulmonary embolism {when}, treated with anticoagulation.",
             "Was diagnosed with a DVT {when} and completed treatment."]),
    "bleeding": ("a major bleed", ("bleed", "hemorrhag", "transfusion"),
                 ["Had a major gastrointestinal bleed {when} that needed a transfusion.",
                  "Was admitted with a major bleed from a duodenal ulcer {when}.",
                  "Needed a blood transfusion for a major bleed {when}."]),
    "vascular": ("a myocardial infarction (heart attack)", ("myocardial infarction", "heart attack"),
                 ["Had a heart attack {when}, treated with a stent.",
                  "Was admitted with a myocardial infarction {when}.",
                  "Had a myocardial infarction {when}; free of chest pain since."]),
    "fall": ("a fall", ("fell", "fall"),
             ["Fell at home {when} and bruised a hip.",
              "Had a fall on the stairs {when}.",
              "Tripped and fell in the garden {when}."]),
}
NEVER = {"stroke": "Has never had a stroke or TIA.", "vte": "Has never had a DVT or pulmonary embolism.",
         "bleeding": "Has never had a major bleed.", "vascular": "Has never had a heart attack.",
         "fall": "Has never fallen."}
# currency and subject reuse the frozen phrase banks (test-split templates)
NP = {"vte": "a venous thromboembolism", "cancer": "cancer", "asthma": "asthma", "bleeding": "a major bleed",
      "peptic_ulcer": "a peptic ulcer", "chf": "heart failure", "diabetes": "diabetes", "crc": "colorectal cancer",
      "cad": "coronary artery disease", "stroke": "a stroke or TIA"}
CURRENCY = ("vte", "cancer", "asthma", "bleeding", "peptic_ulcer", "chf", "diabetes")
SUBJECT = ("vte", "cancer", "asthma", "diabetes", "cad", "stroke")
WINDOWS_EVER = (3, 6, 12)
WINDOW_PAIRS = ((3, 12), (6, 24), (3, 24))

CLAUSES = {   # dimension -> variant -> phrasings ({np}, {Np}, {W}); index shared by the two rules
    "window": {"ever": ["the patient has had {np} at any time",
                        "the patient has had {np} at any time in the past",
                        "the patient has had {np} at any point, however long ago"],
               "window": ["the patient has had {np} within the {W} months before the visit date "
                          "(an event exactly {W} months before the visit date counts)",
                          "the patient has had {np} in the {W} months up to the visit date, including "
                          "the day exactly {W} months before it",
                          "the patient has had {np} on or after the date {W} months before the visit date"]},
    "currency": {"ever": ["the patient has ever had {np} (current or past)",
                          "the patient has had {np} at any time, now or in the past",
                          "the patient has {np} now or has had it in the past"],
                 "current": ["the patient currently has {np}", "the patient has {np} at present",
                             "the patient has {np} at the time of this visit"]},
    "subject": {"family": ["the patient or a first-degree relative (parent, sibling or child) has had {np} "
                           "at any time",
                           "the patient, a parent, a sibling or a child has ever had {np} (current or past)",
                           "{np} has occurred at any time in the patient or in a parent, sibling or child"],
                "patient": ["the patient has had {np} at any time",
                            "the patient has ever had {np} (current or past)",
                            "{np} has occurred at any time in the patient"]},
    "inclusivity": {"high_incl": ["{subj} is {T} or more", "{subj} is at least {T}", "{subj} is {T} or higher"],
                    "high_excl": ["{subj} is above {T}", "{subj} is more than {T}", "{subj} is greater than {T}"],
                    "low_incl": ["{subj} is {T} or less", "{subj} is at most {T}", "{subj} is {T} or lower"],
                    "low_excl": ["{subj} is below {T}", "{subj} is less than {T}", "{subj} is lower than {T}"]},
}
FAMILY_DENIAL = "No parent, sibling or child has had {np}."
# Scenarios (by words of their intro) in which the condition plausibly changes the choice.
FIT = {
    "stroke": ("contraception", "stroke prevention", "dual antiplatelet", "migraine"),
    "vte": ("contraception", "VTE prophylaxis", "thromboprophylaxis", "stroke prevention"),
    "bleeding": ("VTE prophylaxis", "dual antiplatelet", "musculoskeletal", "osteoarthritis", "stroke prevention"),
    "vascular": ("migraine", "musculoskeletal", "osteoarthritis", "contraception"),
    "fall": ("stroke prevention", "VTE prophylaxis", "thromboprophylaxis", "osteoarthritis", "musculoskeletal"),
    "cancer": ("VTE prophylaxis", "thromboprophylaxis", "stroke prevention", "contraception"),
    "asthma": ("rate control", "musculoskeletal", "osteoarthritis", "hypertension"),
    "peptic_ulcer": ("musculoskeletal", "osteoarthritis", "dual antiplatelet"),
    "chf": ("musculoskeletal", "osteoarthritis", "type 2 diabetes", "hypertension"),
    "diabetes": ("primary prevention", "hypertension", "gout"),
    "cad": ("migraine", "musculoskeletal", "osteoarthritis", "contraception"),
    "egfr": ("type 2 diabetes", "musculoskeletal", "osteoarthritis", "stroke prevention", "VTE prophylaxis"),
    "creatinine": ("type 2 diabetes", "musculoskeletal", "osteoarthritis", "stroke prevention", "VTE prophylaxis"),
    "platelets": ("VTE prophylaxis", "dual antiplatelet", "stroke prevention"),
    "alt_enzyme": ("primary prevention",),
    "bun": ("community-acquired pneumonia", "suspected infection"),
    "rr": ("community-acquired pneumonia", "suspected infection"),
    ("sbp", "low"): ("community-acquired pneumonia", "suspected infection"),
    ("sbp", "high"): ("migraine", "contraception"),
    "age": ("contraception", "musculoskeletal", "osteoarthritis", "community-acquired pneumonia",
            "stroke prevention"),
    "potassium": ("heart failure", "hypertension"),
    "temperature": ("sore throat", "suspected infection", "community-acquired pneumonia"),
    "heart_rate": ("community-acquired pneumonia", "suspected infection"),
    "wbc": ("suspected infection", "community-acquired pneumonia"),
    "spo2": ("community-acquired pneumonia", "suspected infection"),
    "weight": ("VTE prophylaxis", "contraception"),
}


def _keywords(concept):
    if concept in EVENTS:
        return EVENTS[concept][1]
    return RG._finding_keywords().get(concept) or next(
        c.keywords for r in RG._hand_written() for c in r.criteria if c.concept == concept)


def _scenarios(concept, current=False, direction=None):
    """Scenarios a concept fits (FIT), not excluded by the setting (an outpatient visit excludes
    the acute forms), and whose alternative the condition does not rule out."""
    fit = FIT[(concept, direction)] if (concept, direction) in FIT else FIT[concept]
    out = []
    for intro, default, alt, setting, sex, ages in RG.SCENARIOS:
        if not any(w in intro for w in fit):
            continue
        ex = RG.EXCLUDE.get(setting, set())
        if concept in ex or (current and (concept, "current") in ex) or RG._contra(concept, default, alt):
            continue
        out.append((intro, default, alt, setting, sex, ages))
    return out


def _fmt(v, dec):
    return f"{v:.{dec}f}" if dec else str(int(round(v)))


# ---------------------------------------------------------------- items
def make_item(i, dim, rng):
    """One item: two rules (count, nocount) and three cases rendered once."""
    if dim == "inclusivity":
        return _numeric_item(i, rng)
    concept = rng.choice(sorted(EVENTS) if dim == "window" else CURRENCY if dim == "currency" else SUBJECT)
    scen = _scenarios(concept, current=dim == "currency")
    intro, default, alt, setting, sex, ages = rng.choice(scen)
    sex = sex or rng.choice(("female", "male"))
    age = rng.randint(max(ages[0], 30 if dim == "subject" else ages[0]), ages[1])
    visit = dt.date(rng.choice((2024, 2025)), rng.randint(1, 12), rng.randint(1, 28))
    phr = i % 3
    np_ = EVENTS[concept][0] if dim == "window" else NP[concept]
    meta = {"dimension": dim, "concept": concept, "phrasing": phr, "visit_date": visit.isoformat(),
            "synthetic_intervention": True, "source": "synthetic (rules_grammar scenarios)"}
    if dim == "window":
        if rng.random() < 0.5:
            w_no = rng.choice(WINDOWS_EVER)
            count = XCrit(concept, "finding", times="ever")
            nocount = XCrit(concept, "finding", times="window", window=w_no)
            k_contested = rng.randint(w_no + 2, w_no + 30)
            texts = (CLAUSES["window"]["ever"][phr], CLAUSES["window"]["window"][phr].replace("{W}", str(w_no)))
            meta["pair"] = f"ever vs {w_no} months"
        else:
            w_no, w_yes = rng.choice(WINDOW_PAIRS)
            count = XCrit(concept, "finding", times="window", window=w_yes)
            nocount = XCrit(concept, "finding", times="window", window=w_no)
            k_contested = rng.randint(w_no + 2, w_yes - 2)
            texts = tuple(CLAUSES["window"]["window"][phr].replace("{W}", str(w)) for w in (w_yes, w_no))
            meta["pair"] = f"{w_yes} vs {w_no} months"
        k_positive = rng.randint(1, max(1, w_no - 2))
        form = "relative" if (i // 3) % 2 == 0 else "dated"
        meta["date_form"] = form
        tpl = EVENTS[concept][2]

        def event(k):
            d = add_months(visit, -k)
            when = (f"{k} month{'s' * (k != 1)} ago" if form == "relative"
                    else f"in {MONTHS[d.month - 1]} {d.year}")
            j = rng.randrange(len(tpl))
            return ([XMention(concept, "finding", True, "patient", "present", "past", d.isoformat(), f"event{j}")],
                    [tpl[j].format(when=when)], [f"xr/event/{concept}/{j}"])
        cases = {"contested": event(k_contested), "positive": event(k_positive),
                 "negative": ([XMention(concept, "finding", True, "patient", "absent", "current", None, "never")],
                              [NEVER[concept]], [f"xr/never/{concept}"])}
        meta["months_before"] = {"contested": k_contested, "positive": k_positive}
    else:
        bank = P.BANKS[concept]
        test = lambda form: P.ids(bank[form], "test")  # noqa: E731

        def line(form, subject="patient"):
            j = rng.choice(test(form))
            status, time = P.FORMS[form]
            yr = rng.randint(min(max(2005, visit.year - age + 18, visit.year - 15), visit.year - 2), visit.year - 2) \
                if "{year}" in bank[form][j] else None
            poss = "Her" if sex == "female" else "His"
            return (XMention(concept, "finding", True, subject, status, time, None, form, yr),
                    bank[form][j].format(Poss=poss, rel=subject, year=yr), f"{concept}/{form}/{j}")
        never = [j for j in test("absent") if any(w in bank["absent"][j].lower()
                                                  for w in ("never", "at any time", "current or past"))]

        def absent(extra=False):
            j = rng.choice(never)
            ms = [XMention(concept, "finding", True, "patient", "absent", "current", None, "absent")]
            ls, tp = [bank["absent"][j]], [f"{concept}/absent/{j}"]
            if extra:
                ms.append(XMention(concept, "finding", True, "first-degree relatives", "absent", "current", None,
                                   "family_denial"))
                ls.append(FAMILY_DENIAL.format(np=np_))
                tp.append("xr/family_denial")
            return ms, ls, tp
        if dim == "currency":
            count = XCrit(concept, "finding", times="ever")
            nocount = XCrit(concept, "finding", times="current")
            texts = (CLAUSES["currency"]["ever"][phr], CLAUSES["currency"]["current"][phr])
            picks = {"contested": line("past"), "positive": line("present")}
            cases = {k: ([m], [t], [tp]) for k, (m, t, tp) in picks.items()}
            cases["negative"] = absent()
        else:
            count = XCrit(concept, "finding", subjects="family", times="ever")
            nocount = XCrit(concept, "finding", subjects="patient", times="ever")
            texts = (CLAUSES["subject"]["family"][phr], CLAUSES["subject"]["patient"][phr])
            kin = [p for p in P.persons(concept, "test", age) if p in FIRST_DEGREE]
            rel = rng.choice(kin)
            rel_form = rng.choice([f for f in ("rel", "rel_past") if f in bank])
            pos_form = rng.choice(("present", "past"))
            picks = {"contested": line(rel_form, rel), "positive": line(pos_form)}
            cases = {k: ([m], [t], [tp]) for k, (m, t, tp) in picks.items()}
            cases["negative"] = absent(extra=True)
            meta["relative"] = rel
    fill = dict(np=np_, Np=np_[0].upper() + np_[1:])
    clause = {"count": texts[0].format(**fill), "nocount": texts[1].format(**fill)}
    return _assemble(i, dim, meta, intro, default, alt, setting, sex, age, visit, rng,
                     {"count": count, "nocount": nocount}, clause, cases, _keywords(concept), header_age=True)


def _numeric_item(i, rng):
    cfgs = [(c, cfg) for c, L in sorted(RG._numeric_configs().items()) if c in RG.NUMERIC_NAMES
            and c not in ("calf_swelling",) for cfg in L]
    concept, (op, thr, dr, fr, nd, dec, kw) = rng.choice(cfgs)
    high = op in (">", ">=")
    scen = _scenarios(concept, direction="high" if high else "low")
    intro, default, alt, setting, sex, ages = rng.choice(scen)
    sex = sex or rng.choice(("female", "male"))
    visit = dt.date(rng.choice((2024, 2025)), rng.randint(1, 12), rng.randint(1, 28))
    phr = i % 3
    name, unit = RG.NUMERIC_NAMES[concept]
    T = _fmt(thr, dec) + ("" if unit[0] in "/%" else " ") + unit
    subj = "the age of the patient" if concept == "age" else f"the current {name}"
    d = "high" if high else "low"
    clause = {"count": CLAUSES["inclusivity"][f"{d}_incl"][phr].format(subj=subj, T=T),
              "nocount": CLAUSES["inclusivity"][f"{d}_excl"][phr].format(subj=subj, T=T)}
    crits = {"count": XCrit(concept, "numeric", op=">=" if high else "<=", threshold=thr),
             "nocount": XCrit(concept, "numeric", op=">" if high else "<", threshold=thr)}
    sign = 1 if high else -1
    vals = {"contested": thr, "positive": round(thr + sign * 2 * nd, dec), "negative": round(thr - sign * 2 * nd, dec)}
    age = vals["contested"] if concept == "age" else rng.randint(*ages)
    bank = P.BANKS[concept]["current"]

    def line(v):
        j = rng.choice(P.ids(bank, "test"))
        return ([XMention(concept, "numeric", v, form="current")],
                [bank[j].format(v=_fmt(v, dec), dia=round(0.55 * v + 15))], [f"{concept}/current/{j}"],
                [_fmt(v, dec)])
    cases = {k: line(v) for k, v in vals.items()}
    meta = {"dimension": "inclusivity", "concept": concept, "phrasing": phr, "visit_date": visit.isoformat(),
            "direction": d, "threshold": thr, "values": vals, "synthetic_intervention": True,
            "source": "synthetic (rules_grammar scenarios; thresholds of hand-written rules)"}
    return _assemble(i, "inclusivity", meta, intro, default, alt, setting, sex, age, visit, rng, crits, clause,
                     cases, kw, header_age=concept != "age")


def _assemble(i, dim, meta, intro, default, alt, setting, sex, age, visit, rng, crits, clause, cases, kw,
              header_age):
    frames = P.HEADER if header_age else P.HEADER_NO_AGE
    hdr = rng.choice(P.ids(frames, "test"))
    noun = "woman" if sex == "female" else "man"
    head = frames[hdr].format(age=age, noun=noun, Noun=noun.capitalize(), sex=sex, Sex=sex.capitalize())
    clean = [j for j in P.ids(P.FILLERS, "test") if not any(k in P.FILLERS[j].lower() for k in kw)]
    fill = [P.FILLERS[j] for j in rng.sample(clean, rng.randint(1, 3))]
    date_line = f"Visit date: {visit.day} {MONTHS[visit.month - 1]} {visit.year}."
    visit_m = XMention("visit_date", "date", visit.isoformat(), form="visit")
    out_cases = {}
    for k, (ms, ls, tp, *found) in cases.items():
        body = fill + ls
        order = list(range(len(body)))
        rng.shuffle(order)
        lines = [head, date_line, setting] + [body[j] for j in order]
        out_cases[k] = {"text": "\n".join(lines), "state": [visit_m] + list(ms), "target_lines": ls, "tpl": tp,
                        "found": found[0] if found else [None] * len(ls)}
    rules = {v: {"text": f"{intro}, prescribe {default}. If {clause[v]}, prescribe {alt} instead.",
                 "crit": crits[v], "condition": clause[v]} for v in ("count", "nocount")}
    return {"item": i, "dim": dim, "meta": dict(meta, hdr=hdr), "default": default, "alternative": alt,
            "rules": rules, "cases": out_cases, "keywords": list(kw)}


def label(item, variant, case):
    return int(item["rules"][variant]["crit"].holds(item["cases"][case]["state"]))


def _ledger(crit, condition, case):
    visit = next(dt.date.fromisoformat(m.value) for m in case["state"] if m.kind == "date")
    ms = [m for m in case["state"] if m.concept == crit.concept]
    out = []
    for m, line, found in zip(ms, case["target_lines"], case["found"]):
        if m.date:
            d = dt.date.fromisoformat(m.date)
            months = (visit.year - d.year) * 12 + visit.month - d.month
            when = f"past ({months} months before the visit date)"
        else:
            when = "current" if m.time == "current" else f"past ({m.year})" if m.year else "past"
        out.append({"need": condition, "found": found or line,
                    "subject": "patient" if m.subject == "patient" else f"other ({m.subject})",
                    "status": m.status, "time": when})
    return out or [{"need": condition, "found": "not mentioned", "subject": "patient", "status": "absent",
                    "time": "current"}]


def records(item, seed):
    out = []
    for v in ("count", "nocount"):
        rule = item["rules"][v]
        tid = f"{SET}.test.{item['item']:03d}.{v}"
        claims = {"conclusion": (f"Prescribe {item['default']}.", f"Prescribe {item['alternative']}."),
                  "criterion": (f"Under the rule, the condition \"{rule['condition']}\" does not hold for this patient.",
                                f"Under the rule, the condition \"{rule['condition']}\" holds for this patient.")}
        for k, case in item["cases"].items():
            y = label(item, v, k)
            ledger = _ledger(rule["crit"], rule["condition"], case)
            common = dict(tid=tid, set=SET, split="test", tier="rule_side", level="xr",
                          rid=f"xr{item['item']:03d}_{v}", cid=rule["crit"].concept, family=item["dim"],
                          nm_kind=item["dim"], case_kind=k, rule_text=rule["text"], case_text=case["text"],
                          condition=rule["condition"], state=[asdict(m) for m in case["state"]], ledger=ledger,
                          prose=ledger_to_prose(ledger),
                          meta={"xr": dict(item["meta"], item=item["item"], variant=v, case_role=k,
                                           counts_contested=v == "count"),
                                "tpl": case["tpl"], "tpl_split": "test", "seed": seed, "overrides": {},
                                "keywords": item["keywords"], "criterion_holds": y})
            for ctype, (s, s2) in claims.items():
                for role, text in (("s", s), ("s_prime", s2)):
                    r = dict(common, iid=f"{tid}/{k}/{ctype}/{role}", claim_type=ctype, claim_role=role,
                             claim_text=text, label=int((role == "s_prime") == (y == 1)))
                    validate(r)
                    out.append(r)
    return out


DIMS = ("window", "currency", "subject", "inclusivity")


def build(n=400, seed=2029):
    """n items, equal per dimension, deterministic."""
    items = []
    for i in range(n):
        dim = DIMS[i % len(DIMS)]
        items.append(make_item(i, dim, random.Random(f"{SET}/{seed}/{i}")))
    return items


# ---------------------------------------------------------------- crossed accuracy
def crossed_accuracy(recs, scores, claim_type="conclusion", exclude=(), partial=False):
    """XA: share of items whose six judgments (two rules x three cases) are all right. scores[j]
    is u(claim of record j); a judgment is right when d = u(s) - u(s') has the sign of the label
    (ties are wrong; an unparsable answer must be passed as a tie, not dropped). Also per dimension.
    exclude: item ids left out (e.g. data/xr_v1/KNOWN_ISSUES.json). An item with fewer than six
    judgments raises, unless partial=True, which leaves it out and reports n_incomplete."""
    u = {}
    for r, sc in zip(recs, scores):
        if r["claim_type"] == claim_type and r["meta"]["xr"]["item"] not in exclude:
            u[(r["tid"], r["case_kind"], r["claim_role"])] = (sc, r)
    right = defaultdict(list)
    for (tid, ck, role), (sc, r) in u.items():
        if role == "s" and (tid, ck, "s_prime") in u:
            d = sc - u[(tid, ck, "s_prime")][0]
            right[(r["meta"]["xr"]["item"], r["nm_kind"])].append(d > 0 if r["label"] == 1 else d < 0)
    incomplete = [k for k, v in right.items() if len(v) != 6]
    if incomplete and not partial:
        raise ValueError(f"{len(incomplete)} items lack some of their six judgments, e.g. {incomplete[:3]}")
    solved = {k: all(v) for k, v in right.items() if len(v) == 6}
    by = defaultdict(list)
    for (item, dim), ok in solved.items():
        by[dim].append(ok)
    pct = lambda xs: round(100.0 * sum(xs) / len(xs), 1) if xs else None  # noqa: E731
    return {"XA": pct(list(solved.values())), "n_items": len(solved), "n_incomplete": len(incomplete),
            **{f"XA_{d}": pct(v) for d, v in sorted(by.items())}}
