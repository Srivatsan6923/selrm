"""Stage-2 triplet engine: conditions with a time window, a class or a number (rule_v2, cls_v1, reg_v1).

rule_v1's engine and its hashes are untouched: this module has its own conditions, mentions and templates and
reuses only rule_v1's scenarios, headers, people and neutral fillers. A rule is a scenario (default and
alternative prescription) and one or two conditions joined by `any` or `all`.

  window   an event of the patient within N days, months or years before the visit date that the case states.
           The day exactly N units before the visit counts, and the rule text says so.
  class    the patient currently takes a drug, or has a finding or a disease, of a class of onto_v1. The case
           names a member (ingredient, brand name, label or exact synonym); the rule names the class.
  numeric  a current value against a threshold (registered criteria).

Near-miss kinds: window (the event before the window), class (a member of a sibling class or a term too
general to establish membership), numeric (a value toward the threshold), and subject, negation and time as
in rule_v1. The base case does not mention the target concept; flip and near-miss add one line at the same
position. Labels come from executing the rule on the case's state.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import random
from dataclasses import dataclass, field

from selrm import phrases as P
from selrm.xr import add_months

LEDGER2_KEYS = ("need", "found", "subject", "status", "time", "concept", "applies")
MAX_TRIES = 40
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December")
# Templates below are split train / test by index (phrases.split_of): four train, two test per bank.
VISIT = ("Visit date: {d}.", "Seen in clinic on {d}.", "Date of this visit: {d}.", "Assessment date: {d}.",
         "Reviewed on {d}.", "Clinic visit on {d}.")
DATE_STYLES = 6


def fmt_date(d, style):
    m = MONTHS[d.month - 1]
    return (f"{d.day} {m} {d.year}", d.isoformat(), f"{m} {d.day}, {d.year}", f"{d.day} {m[:3]} {d.year}",
            f"{m[:3]} {d.day}, {d.year}", f"{d.day}th of {m} {d.year}" if d.day not in (1, 2, 3, 21, 22, 23, 31)
            else f"{m} {d.day} of {d.year}")[style]


# event: key -> (noun, with article, third-person past, bare participle, keywords)
EVENTS = {
    "admission": ("hospital admission", "a hospital admission", "was admitted to hospital", "Admitted to hospital", ("admi",)),
    "surgery": ("operation under general anaesthesia", "an operation under general anaesthesia",
                "had an operation under general anaesthesia", "Operated under general anaesthesia", ("operat", "anaesth")),
    "transfusion": ("blood transfusion", "a blood transfusion", "received a blood transfusion", "Transfused with blood", ("transfus",)),
    "fall": ("fall", "a fall", "had a fall", "Fell at home", ("fall", "fell")),
    "fracture": ("bone fracture", "a bone fracture", "sustained a bone fracture", "Sustained a bone fracture", ("fractur",)),
    "antibiotic": ("course of antibiotics", "a course of antibiotics", "started a course of antibiotics",
                   "Started a course of antibiotics", ("antibiotic",)),
    "vaccine": ("live vaccine dose", "a live vaccine dose", "received a live vaccine dose", "Given a live vaccine dose", ("vaccin",)),
    "seizure": ("seizure", "a seizure", "had a seizure", "Had a seizure", ("seizure",)),
    "chemo": ("cycle of chemotherapy", "a cycle of chemotherapy", "received a cycle of chemotherapy",
              "Given a cycle of chemotherapy", ("chemotherap",)),
    "contrast": ("iodinated contrast scan", "an iodinated contrast scan", "had an iodinated contrast scan",
                 "Scanned with iodinated contrast", ("contrast",)),
}
EVENT_T = {
    "present": ("{Bare} on {d}.", "Last {noun}: {d}.", "{Poss} most recent {noun} was on {d}.", "Records show {np} on {d}.",
                "{Noun} dated {d}.", "There was {np} on {d}."),
    "absent": ("No {noun} on record.", "Denies any {noun}.", "{Noun}: not reported.", "Has not had {np}.",
               "Never had {np}.", "Record negative for {noun}."),
    "rel": ("{Poss} {rel} {past} on {d}.", "Of note, {poss} {rel} {past} on {d}.", "Family: the {rel} {past} on {d}.",
            "The {rel} {past} on {d}.", "It was the {rel} who {past} on {d}.", "{Poss} {rel}, for one, {past} on {d}."),
}
CLASS_T = {
    "drug": {
        "present": ("Takes {x} daily.", "Current medication: {x}.", "On {x}.", "Regular medicines include {x}.",
                    "Is maintained on {x}.", "Medication list: {x}."),
        "absent": ("Not taking {x}.", "Denies taking {x}.", "No {x} use.", "Does not take {x}.",
                   "Never took {x}.", "Is without {x}."),
        "rel": ("{Poss} {rel} takes {x}.", "{Poss} {rel} is on {x}.", "Family: the {rel} takes {x}.", "The {rel} uses {x}.",
                "{Poss} {rel} is maintained on {x}.", "It is the {rel} who takes {x}."),
        "past": ("Stopped {x} in {year}.", "Previously took {x}; stopped in {year}.", "{X} was stopped in {year}.",
                 "Completed a course of {x} in {year}.", "Formerly on {x} ({year}).", "Was on {x} some years ago, in {year}."),
    },
    "phenotype": {
        "present": ("Examination shows {x}.", "Has {x}.", "Findings: {x}.", "Noted to have {x}.",
                    "Presents with {x}.", "Assessment documents {x}."),
        "absent": ("No {x}.", "Denies {x}.", "{X}: not present.", "Does not have {x}.", "Negative for {x}.", "{X} absent."),
        "rel": ("{Poss} {rel} has {x}.", "Family history: the {rel} has {x}.", "{X} in {poss} {rel}.", "The {rel} has {x}.",
                "{Poss} {rel} presents with {x}.", "It is the {rel} who has {x}."),
        "past": ("{X} resolved in {year}.", "Previously had {x}, resolved in {year}.", "Had {x} in {year}; healed.",
                 "{X} in {year}, since resolved.", "Formerly had {x} ({year}); recovered.", "{X} some years ago, in {year}; recovered."),
    },
}
CLASS_T["disease"] = dict(CLASS_T["phenotype"], present=("Diagnosed with {x}.", "Has {x}.", "Known {x}.", "Diagnosis: {x}.",
                                                         "Carries a diagnosis of {x}.", "Under follow-up for {x}."))
NUM_T = {"present": ("{Name} {v} {unit}.", "{Name}: {v} {unit}.", "{Name} measured at {v} {unit}.", "{Name} is {v} {unit}.",
                     "{Name} of {v} {unit}.", "{Name} reads {v} {unit}."),
         "past": ("{Name} {v} {unit} in {year}.", "{Name} in {year}: {v} {unit}.", "Previously, in {year}, {name} {v} {unit}.",
                  "{Name} was {v} {unit} in {year}.", "Formerly ({year}) {name} {v} {unit}.", "{Name} {v} {unit} some years ago, in {year}.")}
CLASS_PHRASE = {"drug": "the patient is currently taking a drug of the class \"{name}\"",
                "phenotype": "the patient currently has a finding of the class \"{name}\"",
                "disease": "the patient currently has a disease of the class \"{name}\""}
CLASS_LABEL = {"drug": "current use of a drug of the class {name}", "phenotype": "current finding of the class {name}",
               "disease": "current disease of the class {name}"}
OPS = {"<": lambda a, b: a < b, "<=": lambda a, b: a <= b, ">": lambda a, b: a > b, ">=": lambda a, b: a >= b}
OPW = {"<": "below", "<=": "at or below", ">": "above", ">=": "at or above"}


@dataclass(frozen=True)
class Cond:
    cid: str
    kind: str                       # window | class | numeric
    key: str                        # event key | class id | measurement name
    # window
    n: int = 0
    unit: str = ""                  # days | months | years
    # class
    domain: str = ""
    name: str = ""                  # class name shown (EPC name or ontology label)
    members: tuple = ()             # ((term id, (names...)), ...)
    near: tuple = ()                # ((term id, name, 'sibling' | 'general'), ...)
    # numeric
    op: str = ""
    threshold: float = 0.0
    decimals: int = 0
    lo: float = 0.0
    hi: float = 0.0
    num_unit: str = ""

    @property
    def label(self):
        if self.kind == "window":
            return f"{EVENTS[self.key][0]} within {self.n} {self.unit} before the visit"
        if self.kind == "class":
            return CLASS_LABEL[self.domain].format(name=self.name)
        return f"{self.key} {OPW[self.op]} {fmt_num(self.threshold, self)}"

    @property
    def phrase(self):
        if self.kind == "window":
            return (f"the patient {EVENTS[self.key][2]} within {self.n} {self.unit} before the visit date "
                    f"(a date exactly {self.n} {self.unit} before the visit still counts)")
        if self.kind == "class":
            return CLASS_PHRASE[self.domain].format(name=self.name)
        return f"the current {self.key} is {OPW[self.op]} {fmt_num(self.threshold, self)} {self.num_unit}".rstrip()

    def start(self, ref):
        """First day of the window."""
        if self.unit == "days":
            return ref - dt.timedelta(days=self.n)
        return add_months(ref, -self.n * (12 if self.unit == "years" else 1))

    def counts(self, m, ref):
        """Does this mention establish the condition?"""
        if m["concept"] != self.key or m["subject"] != "patient" or m["status"] != "present":
            return False
        if self.kind == "window":
            d = dt.date.fromisoformat(m["date"])
            return self.start(ref) <= d <= ref
        if m["time"] != "current":
            return False
        if self.kind == "class":
            return m["term"] in {t for t, _ in self.members}
        return OPS[self.op](m["value"], self.threshold)

    def evaluate(self, state, ref):
        return any(self.counts(m, ref) for m in state)

    def struct(self):
        if self.kind == "window":
            return {"kind": "window", "event": self.key, "n": self.n, "unit": self.unit, "boundary": "inclusive",
                    "reference": "visit date", "subject": "patient", "status": "present"}
        if self.kind == "class":
            return {"kind": "class", "class_id": self.key, "domain": self.domain, "subject": "patient", "status": "present",
                    "time": "current"}
        return {"kind": "numeric", "name": self.key, "op": self.op, "threshold": self.threshold, "unit": self.num_unit,
                "subject": "patient", "time": "current"}


def fmt_num(v, c):
    return f"{v:.{c.decimals}f}" if c.decimals else str(int(round(v)))


@dataclass(frozen=True)
class Rule2:
    rid: str
    logic: str                      # any | all (one condition: any)
    conds: tuple
    intro: str
    default: str
    alternative: str
    setting: str
    sex: str | None = None
    ages: tuple = (30, 64)
    family: str = ""
    source: dict = field(default_factory=dict, hash=False, compare=False)

    def crit(self, cid):
        return next(c for c in self.conds if c.cid == cid)

    def text(self):
        joiner = " or " if self.logic == "any" else " and "
        return (f"{self.intro}, prescribe {self.default}. If {joiner.join(c.phrase for c in self.conds)}, "
                f"prescribe {self.alternative} instead.")

    def claims(self):
        return f"Prescribe {self.default}.", f"Prescribe {self.alternative}."

    def label(self, state, ref):
        met = [c.evaluate(state, ref) for c in self.conds]
        return int(any(met) if self.logic == "any" else all(met))


def sig_class(rule):
    """Signature class of a stage-2 rule: operator and the kinds of its conditions."""
    op = "single" if len(rule.conds) == 1 else rule.logic
    return f"{op}|{'+'.join(sorted(c.kind for c in rule.conds))}"


def nm_kinds(c):
    return {"window": ("window", "negation", "subject"), "class": ("class", "negation", "subject", "time"),
            "numeric": ("numeric", "boundary", "time")}[c.kind]


def lower_first(x):
    return x if len(x) > 1 and x[1].isupper() else x[0].lower() + x[1:]


def _say(c, m, poss, style):
    """The line of one mention."""
    i = m["tpl"]
    if c.kind == "window":
        noun, np_, past, bare, _ = EVENTS[c.key]
        d = fmt_date(dt.date.fromisoformat(m["date"]), style) if m.get("date") else ""
        form = "rel" if m["subject"] != "patient" else m["status"]
        return EVENT_T[form][i].format(Bare=bare, noun=noun, Noun=noun[0].upper() + noun[1:], np=np_, past=past, d=d,
                                       Poss=poss, poss=poss.lower(), rel=m["subject"])
    if c.kind == "class":
        form = "rel" if m["subject"] != "patient" else "past" if m["time"] == "past" else m["status"]
        x = m["name"] if c.domain == "drug" else lower_first(m["name"])
        return CLASS_T[c.domain][form][i].format(x=x, X=x[0].upper() + x[1:], Poss=poss, poss=poss.lower(), rel=m["subject"],
                                                 year=m.get("year"))
    form = "past" if m["time"] == "past" else "present"
    return NUM_T[form][i].format(Name=c.key[0].upper() + c.key[1:], name=c.key, v=fmt_num(m["value"], c), unit=c.num_unit,
                                 year=m.get("year")).replace(" .", ".")


def _mention(c, rng, split, form, ref, people, extra=None):
    """A mention of condition c in one form; `extra` carries a date, a term or a value."""
    extra = extra or {}
    bank = {"window": EVENT_T, "numeric": NUM_T}.get(c.kind) or CLASS_T[c.domain]
    tpl = rng.choice(P.ids(bank[form if form in bank else "present"], split))
    m = {"concept": c.key, "kind": c.kind, "subject": "patient", "status": "present", "time": "current", "tpl": tpl}
    if form == "absent":
        m["status"] = "absent"
    if form == "rel":
        m["subject"] = rng.choice(people)
    if form == "past":
        m["time"], m["year"] = "past", rng.randint(ref.year - 12, ref.year - 3)
    m.update(extra)
    return m


def _inside(c, rng, ref):
    """A date inside the window: the boundary day in a quarter of the draws, else at least two days inside."""
    start = c.start(ref)
    span = (ref - start).days
    if rng.random() < 0.25 or span < 5:
        return start
    return start + dt.timedelta(days=rng.randint(2, span - 1))


def _before(c, rng, ref):
    """A date before the window, at least two days and at most about one more window length earlier."""
    start = c.start(ref)
    span = max((ref - start).days, 10)
    return start - dt.timedelta(days=rng.randint(2, span))


def _member(c, rng):
    term, names = rng.choice(c.members)
    j = rng.randrange(len(names))
    return {"term": term, "name": names[j], "name_type": "label" if j == 0 else "brand" if c.domain == "drug" else "synonym"}


def _counting(c, rng, split, ref, people):
    if c.kind == "window":
        return _mention(c, rng, split, "present", ref, people, {"date": _inside(c, rng, ref).isoformat()})
    if c.kind == "class":
        return _mention(c, rng, split, "present", ref, people, _member(c, rng))
    v = _draw(c, rng, True)
    return _mention(c, rng, split, "present", ref, people, {"value": v})


def _draw(c, rng, met, near=False):
    """A value on the met or unmet side; near: within a tenth of the range of the threshold, unmet side."""
    step = 10 ** -c.decimals
    span = (c.hi - c.lo) * (0.1 if near else 1.0)
    for _ in range(400):
        lo, hi = (c.threshold - span, c.threshold + span) if near else (c.lo, c.hi)
        v = round(rng.uniform(max(lo, c.lo), min(hi, c.hi)) / step) * step
        v = round(v, c.decimals)
        if OPS[c.op](v, c.threshold) == met and v != c.threshold:
            return v
    raise ValueError(f"{c.cid}: no value")


def propose(rule, crit, nm_kind, tier, split, rng):
    sex = rule.sex or rng.choice(("female", "male"))
    poss = "Her" if sex == "female" else "His"
    age = rng.randint(*rule.ages)
    ref = dt.date(2026, 1, 1) + dt.timedelta(days=rng.randint(0, 270))
    style = rng.choice(P.ids(range(DATE_STYLES), split))
    people = [p for p in P.persons(None, split, age) if p not in ("husband", "wife", "partner", "coworker", "neighbor",
                                                                   "housemate", "roommate", "friend", "brother-in-law")] \
        or P.persons(None, split, age)
    # context: the other condition held unmet (any) or met (all), fillers, the visit date
    body = [{"visit": rng.choice(P.ids(VISIT, split))}]
    for c in rule.conds:
        if c is not crit:
            if rule.logic == "all":
                body.append({"c": c, "m": _counting(c, rng, split, ref, people)})
            elif c.kind == "numeric":
                body.append({"c": c, "m": _mention(c, rng, split, "present", ref, people, {"value": _draw(c, rng, False)})})
    n_fill = rng.randint(15, 20) if tier == "long" else rng.randint(1, 4)
    n_other = rng.randint(2, 4) if tier == "long" else 0
    body += [{"filler": P.FILLERS[i]} for i in rng.sample(P.ids(P.FILLERS, split), min(n_fill - n_other, len(P.ids(P.FILLERS, split))))]
    body += [{"filler": P.FILLERS_OTHER[i].format(Poss=poss, rel=rng.choice(people))}
             for i in rng.sample(P.ids(P.FILLERS_OTHER, split), n_other)]
    rng.shuffle(body)

    # target lines
    base = None
    if crit.kind == "numeric":
        far = _draw(crit, rng, False)
        base = _mention(crit, rng, split, "present", ref, people, {"value": far})
        flip = dict(base, value=crit.threshold if crit.op in ("<=", ">=") and rng.random() < 1 / 3 else _draw(crit, rng, True))
        if nm_kind == "numeric":
            v = _draw(crit, rng, False, near=True)
            if abs(v - crit.threshold) >= abs(far - crit.threshold):
                raise ValueError("near value not nearer")
            near = dict(base, value=v)
        elif nm_kind == "boundary":
            if crit.op not in ("<", ">"):
                raise ValueError("no boundary near-miss for an inclusive threshold")
            near = dict(base, value=crit.threshold)
        else:                              # time: a past value on the met side, next to the current one
            near = [base, _mention(crit, rng, split, "past", ref, people, {"value": _draw(crit, rng, True)})]
    else:
        flip = _counting(crit, rng, split, ref, people)
        if nm_kind == "negation":
            extra = {"date": None} if crit.kind == "window" else {k: flip[k] for k in ("term", "name", "name_type")}
            near = _mention(crit, rng, split, "absent", ref, people, extra)
        elif nm_kind == "subject":
            extra = {"date": flip["date"]} if crit.kind == "window" else {k: flip[k] for k in ("term", "name", "name_type")}
            near = _mention(crit, rng, split, "rel", ref, people, extra)
        elif nm_kind == "time":
            near = _mention(crit, rng, split, "past", ref, people, {k: flip[k] for k in ("term", "name", "name_type")})
        elif nm_kind == "window":
            near = dict(flip, date=_before(crit, rng, ref).isoformat())
        elif nm_kind == "class":
            term, name, how = rng.choice(crit.near)
            near = dict(flip, term=term, name=name, name_type=how)
        else:
            raise ValueError(nm_kind)
    p = rng.randint(0, len(body))

    def lines(target):
        ts = target if isinstance(target, list) else [target] if target else []
        return body[:p] + [{"c": crit, "m": t} for t in ts] + body[p:]

    frames = P.HEADER
    hdr = rng.choice(P.ids(frames, split))
    noun = "woman" if sex == "female" else "man"

    def case(frame, ls, date_style):
        out, state = [], []
        for x in ls:
            if "visit" in x:
                out.append(VISIT[x["visit"]].format(d=fmt_date(ref, date_style)))
            elif "filler" in x:
                out.append(x["filler"])
            else:
                out.append(_say(x["c"], x["m"], poss, date_style))
                state.append((x["c"], x["m"], out[-1]))
        head = frames[frame].format(age=age, noun=noun, Noun=noun.capitalize(), sex=sex, Sex=sex.capitalize())
        st = [{k: v for k, v in m.items() if k != "tpl"} for _, m, _ in state]
        return {"text": "\n".join([head, rule.setting] + out), "lines": out, "state": st,
                "fillers": [x["filler"] for x in ls if "filler" in x],
                "ledger": ledger(crit, ref, [(m, t) for c, m, t in state if c is crit]),
                "labels": {"conclusion": rule.label(st, ref), "criterion": int(crit.evaluate(st, ref))}}

    base_ls = lines(base)
    order = list(range(len(base_ls)))
    for _ in range(20):
        rng.shuffle(order)
        if len(order) < 2 or order != sorted(order):
            break
    other_style = rng.choice([s for s in P.ids(range(DATE_STYLES), split) if s != style] or [style])
    other_hdr = rng.choice([h for h in P.ids(frames, split) if h != hdr] or [hdr])
    cases = {"base": case(hdr, base_ls, style), "flip": case(hdr, lines(flip), style), "near": case(hdr, lines(near), style),
             "pres": case(other_hdr, [base_ls[i] for i in order], other_style)}
    what = EVENTS[crit.key][0] if crit.kind == "window" else crit.label if crit.kind == "class" else crit.key
    miss = P.MISSING[rng.choice(P.ids(P.MISSING, split))].format(What=what[0].upper() + what[1:], what=what)
    unknown = dict(cases["base"])
    if crit.kind == "numeric":              # the measurement is not given at all
        ls = [x for x in base_ls if x.get("m") is not base]
        unknown = case(hdr, ls, style)
    else:
        ls = cases["base"]["lines"][:p] + [miss] + cases["base"]["lines"][p:]
        unknown = dict(cases["base"], text="\n".join(cases["base"]["text"].split("\n")[:2] + ls), lines=ls,
                       ledger=[_entry(crit, None, "not mentioned", status="unknown")])
    unknown["labels"] = None
    cases["missing"] = unknown
    return {"rule": rule, "crit": crit, "nm_kind": nm_kind, "tier": tier, "cases": cases, "ref": ref,
            "near_term": near if isinstance(near, dict) else None, "flip_m": flip}


def _entry(c, m, found, status=None, applies=False):
    e = {"need": c.label, "found": found, "subject": "patient", "status": status or "absent", "time": "current"}
    if m is not None:
        e["subject"] = "patient" if m["subject"] == "patient" else f"other ({m['subject']})"
        e["status"] = m["status"]
        e["time"] = m["date"] if m.get("date") else f"past ({m['year']})" if m["time"] == "past" else "current"
    e["concept"] = (m or {}).get("term") or ""
    e["applies"] = "yes" if applies else "no"
    return e


def ledger(c, ref, mentions):
    """Stage-2 record of the condition under test: one entry per mention of its concept, with the date in
    `time` for dated events, the linked term in `concept` for class conditions, and the `applies` bit."""
    out = [_entry(c, m, fmt_num(m["value"], c) if c.kind == "numeric" else text, applies=c.counts(m, ref)) for m, text in mentions]
    return out or [_entry(c, None, "not mentioned", status="unknown" if c.kind == "numeric" else "absent")]


def prose(entries):
    out = []
    for e in entries:
        if e["found"] == "not mentioned":
            out.append(f"The note does not mention {e['need']}." if e["status"] != "unknown"
                       else f"The note gives no information on {e['need']}.")
            continue
        who = "the patient" if e["subject"] == "patient" else "the patient's " + e["subject"][7:-1]
        when = "at present" if e["time"] == "current" else "in the " + e["time"] if e["time"].startswith("past") else "on " + e["time"]
        link = f" It refers to {e['concept']}." if e["concept"] else ""
        out.append(f"For {e['need']}, the note states \"{e['found']}\"; this concerns {who}, is recorded as {e['status']}, {when}.{link}")
    return " ".join(out)


def check(g):
    """Invariant violations of a proposed group ([] if none)."""
    rule, crit, cases, ref = g["rule"], g["crit"], g["cases"], g["ref"]
    errs = []
    want = {"base": 0, "flip": 1, "near": 0, "pres": 0}
    for k, y in want.items():
        if cases[k]["labels"] != {"conclusion": y, "criterion": y}:
            errs.append(f"label {k}")
    for other in rule.conds:                                   # the flip changes the target condition only
        if other is not crit and other.evaluate(cases["flip"]["state"], ref) != other.evaluate(cases["base"]["state"], ref):
            errs.append("flip changes another condition")
    b = cases["base"]["lines"]
    for k in ("flip", "near"):
        extra = [x for x in cases[k]["lines"] if x not in b]
        gone = [x for x in b if x not in cases[k]["lines"]]
        if len(extra) != 1 or len(gone) > 1:
            errs.append(f"{k} is not a one-line edit")
    if sorted(cases["pres"]["state"], key=str) != sorted(cases["base"]["state"], key=str):
        errs.append("pres state differs")
    if cases["pres"]["text"] == cases["base"]["text"]:
        errs.append("pres text equals base")
    names = set()
    if crit.kind == "class":
        names = {n.lower() for _, ns in crit.members for n in ns} | {n.lower() for _, n, _ in crit.near}
    elif crit.kind == "window":
        names = set(EVENTS[crit.key][4])
    for k, case in cases.items():
        for f in case["fillers"]:
            if any(n in f.lower() for n in names):
                errs.append("filler names the concept")
        for e in case["ledger"]:
            if e["found"] != "not mentioned" and crit.kind != "numeric" and e["found"] not in case["text"]:
                errs.append("ledger quote not in case")
        if "{" in case["text"] or "None" in case["text"]:
            errs.append("unfilled slot")
    if crit.kind != "numeric" and any(n in cases["base"]["text"].lower() for n in names if len(n) > 3):
        errs.append("base names the concept")
    return errs


def validate2(rec):
    """Canonical record with the stage-2 fields (STAGE2_SPEC section 3)."""
    from selrm.schema import CASE_KINDS, CLAIM_TYPES, REQUIRED
    for k, t in REQUIRED.items():
        if not isinstance(rec.get(k), t):
            raise ValueError(f"{k} missing or not {t.__name__} in {rec.get('iid')}")
    if rec["case_kind"] not in CASE_KINDS or rec["claim_type"] not in CLAIM_TYPES or rec["label"] not in (0, 1):
        raise ValueError(f"bad record {rec['iid']}")
    for e in rec["ledger"]:
        if tuple(e) != LEDGER2_KEYS or e["applies"] not in ("yes", "no"):
            raise ValueError(f"bad stage-2 ledger entry in {rec['iid']}: {e}")
    for k in ("crit", "cluster", "struct"):
        if k not in rec:
            raise ValueError(f"{k} missing in {rec['iid']}")


def make_group(rule, cid, nm_kind, tier, split, seed, set_name, level, tpl_split=None, stats=None, cluster=None):
    """Records of one group (base, flip, near, pres, missing; conclusion and criterion claims)."""
    crit = rule.crit(cid)
    if nm_kind not in nm_kinds(crit):
        raise ValueError(f"invalid near-miss kind {nm_kind} for {crit.kind}")
    tid = f"{set_name}.{split}.{rule.rid}.{cid}.{nm_kind}.{tier}.{seed}"
    rng = random.Random(tid)
    errs = []
    for _ in range(MAX_TRIES):
        try:
            g = propose(rule, crit, nm_kind, tier, tpl_split or split, rng)
            errs = check(g)
        except ValueError as e:
            g, errs = None, [f"draw: {e}"]
        if stats is not None:
            stats["proposed"] += 1
            stats["rejected"] += bool(errs)
            stats.update(f"reject {crit.kind} {nm_kind} {e}" for e in errs)
        if not errs:
            return to_records(g, tid, set_name, split, level, seed, tpl_split or split, cluster)
    raise RuntimeError(f"{tid}: no valid group in {MAX_TRIES} tries; last: {errs}")


def to_records(g, tid, set_name, split, level, seed, tpl_split, cluster=None):
    rule, crit, ref = g["rule"], g["crit"], g["ref"]
    text = rule.text()
    s, s2 = rule.claims()
    claims = {"conclusion": (s, s2),
              "criterion": (f"Under the rule, the condition \"{crit.label}\" does not hold for this patient.",
                            f"Under the rule, the condition \"{crit.label}\" holds for this patient.")}
    out = []
    for k, case in g["cases"].items():
        meta = {"seed": seed, "tpl_split": tpl_split, "criterion_holds": None if k == "missing" else case["labels"]["criterion"],
                "sig_class": sig_class(rule), "near_term": {x: g["near_term"].get(x) for x in ("term", "name", "name_type")}
                if g["near_term"] and crit.kind == "class" else None,
                "flip_name_type": g["flip_m"].get("name_type") if isinstance(g["flip_m"], dict) else None, **rule.source}
        common = dict(tid=tid, set=set_name, split=split, tier=g["tier"], level=level, rid=rule.rid, cid=crit.cid,
                      family=rule.family or sig_class(rule), nm_kind=g["nm_kind"], case_kind=k, rule_text=text,
                      case_text=case["text"], condition=crit.label, state=case["state"], ledger=case["ledger"],
                      prose=prose(case["ledger"]), meta=meta,
                      crit={"source": "stated", "provenance": "generated rule (selrm.engine2)",
                            "text_sha": hashlib.sha256(text.encode("utf-8")).hexdigest()},
                      cluster=cluster or rule.rid, struct=crit.struct(), ref_date=ref.isoformat())
        for ctype, (a, b) in claims.items():
            y = None if k == "missing" else case["labels"][ctype]
            for role, t in (("s", a), ("s_prime", b)):
                rec = dict(common, iid=f"{tid}/{k}/{ctype}/{role}", claim_type=ctype, claim_role=role, claim_text=t,
                           label=0 if y is None else int((role == "s_prime") == (y == 1)))
                validate2(rec)
                out.append(rec)
    return out
