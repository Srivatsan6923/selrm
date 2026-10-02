"""Patient states, criteria with applicability predicates, and stated rules.

A patient state is a tuple of Mentions. A criterion decides from the mentions
it counts (its applicability predicate) whether it holds. Labels are always
computed by executing these programs, never written by hand.
"""
from __future__ import annotations

import operator
from dataclasses import dataclass, field, replace

FIRST_DEGREE = {"mother", "father", "sister", "brother", "son", "daughter"}
OPS = {"<": operator.lt, "<=": operator.le, ">": operator.gt, ">=": operator.ge}


@dataclass(frozen=True)
class Mention:
    concept: str
    kind: str                      # "finding" | "numeric"
    value: object = True           # finding: True; numeric: float
    subject: str = "patient"       # patient | mother | aunt | husband | ...
    status: str = "present"        # present | absent
    time: str = "current"          # current | past
    form: str = "present"          # phrase-bank key used for rendering
    year: int | None = None


@dataclass
class Criterion:
    cid: str
    concept: str
    kind: str                      # "finding" | "numeric"
    label: str                     # used in score-rule claims
    keywords: tuple                # lower-case substrings that name the concept
    op: str | None = None
    threshold: float | None = None
    alt_threshold: float | None = None   # for altered-rule triplets (L3-alt)
    default_range: tuple | None = None   # numeric values on the default side
    flip_range: tuple | None = None      # numeric values on the other side
    near_delta: float | None = None      # numeric near-miss window width
    decimals: int = 0
    counts_past: bool = False
    counts_family: bool = False          # first-degree relatives count
    points: int = 1
    nm: tuple | None = None              # restrict near-miss kinds

    def applies(self, m: Mention) -> bool:
        if m.concept != self.concept:
            return False
        if m.subject != "patient" and not (self.counts_family and m.subject in FIRST_DEGREE):
            return False
        if m.time == "past" and not self.counts_past:
            return False
        return True

    def evaluate(self, mentions, threshold: float | None = None) -> bool:
        app = [m for m in mentions if self.applies(m)]
        if self.kind == "finding":
            # closed world for history items: unmentioned or absent -> False
            return any(m.status == "present" for m in app)
        vals = [m.value for m in app if m.status == "present"]
        if len(vals) != 1:
            raise ValueError(f"{self.cid}: expected one applicable value, got {vals}")
        thr = self.threshold if threshold is None else threshold
        return OPS[self.op](vals[0], thr)

    def nm_kinds(self) -> list[str]:
        """Near-miss kinds that leave this criterion unchanged by construction."""
        if self.nm is not None:
            return list(self.nm)
        if self.kind == "numeric":
            return ["numeric", "time"]
        kinds = ["subject", "negation"]
        if not self.counts_past:
            kinds.append("time")
        return kinds


@dataclass
class Rule:
    rid: str
    kind: str                      # "constraint" | "score"
    title: str
    text: str                      # stated rule; {thr_<cid>} placeholders
    criteria: list
    setting: str                   # first line of the case
    default: str = ""              # constraint rules
    alternative: str = ""
    sex: str | None = None
    age_range: tuple = (30, 64)
    family: str = ""               # structural family, used for held-out splits
    logic: str = "any"             # constraint: "any" | "all" | "atleast" (points of met >= cutoff)
    cutoff: int | None = None      # points needed when logic == "atleast"
    verb: str = "Prescribe"        # constraint claims: "<verb> <option>."

    def crit(self, cid: str) -> Criterion:
        return next(c for c in self.criteria if c.cid == cid)

    def rule_text(self, overrides: dict | None = None) -> str:
        overrides = overrides or {}
        vals = {}
        for c in self.criteria:
            if c.threshold is not None:
                t = overrides.get(c.cid, c.threshold)
                vals[f"thr_{c.cid}"] = f"{t:.{c.decimals}f}" if c.decimals else f"{int(t)}"
        return self.text.format(**vals)

    def claims(self, cid: str) -> tuple[str, str]:
        """(s, s'): s is correct on the default side, s' on the flipped side."""
        if self.kind == "constraint":
            return (f"{self.verb} {self.default}.", f"{self.verb} {self.alternative}.")
        c = self.crit(cid)
        unit = "point" if c.points == 1 else "points"
        return (f"The {c.label} criterion contributes 0 points.",
                f"The {c.label} criterion contributes {c.points} {unit}.")

    def label(self, mentions, cid: str, overrides: dict | None = None) -> int:
        """0 if s is correct, 1 if s' is correct (executed, not annotated)."""
        overrides = overrides or {}
        if self.kind == "constraint":
            if self.logic == "any":
                return int(any(c.evaluate(mentions, overrides.get(c.cid)) for c in self.criteria))
            met = [c for c in self.criteria if c.evaluate(mentions, overrides.get(c.cid))]
            if self.logic == "all":
                return int(len(met) == len(self.criteria))
            return int(sum(c.points for c in met) >= self.cutoff)
        c = self.crit(cid)
        return int(c.evaluate(mentions, overrides.get(cid)))


def F(cid, concept, label, keywords, **kw):
    return Criterion(cid=cid, concept=concept, kind="finding", label=label,
                     keywords=tuple(keywords), **kw)


def N(cid, concept, label, keywords, op, thr, default_range, flip_range, near_delta, **kw):
    return Criterion(cid=cid, concept=concept, kind="numeric", label=label,
                     keywords=tuple(keywords), op=op, threshold=thr,
                     default_range=default_range, flip_range=flip_range,
                     near_delta=near_delta, **kw)


# Rule text from a structural family and (criterion, condition phrase) pairs;
# Rule.label with Rule.logic is the program for every family.
FAMILIES = ("any_of", "all_of", "two_of_three", "score_cutoff")


def G(rid, family, title, intro, default, alternative, conds, setting, cutoff=None, **kw):
    crits = [c for c, _ in conds]
    head, switch = f"{intro}, prescribe {default}.", f"prescribe {alternative} instead"
    phrases = [p for _, p in conds]
    if family == "any_of":
        text, logic = f"{head} If {' or '.join(phrases)}, {switch}.", "any"
    elif family == "all_of":
        text, logic = f"{head} If {' and '.join(phrases)}, {switch}.", "all"
    elif family == "two_of_three":
        text, logic, cutoff = (f"{head} If at least two of the following apply, {switch}: "
                               f"{'; '.join(phrases)}."), "atleast", 2
    elif family == "score_cutoff":
        items = "; ".join(f"{c.points} point{'s' if c.points > 1 else ''} "
                          f"{'if' if p.startswith('the ') else 'for'} {p}" for c, p in conds)
        text, logic = f"{head} Score {items}. If the score is {cutoff} or more, {switch}.", "atleast"
    else:
        raise ValueError(family)
    return Rule(rid, "constraint", title, text, crits, setting, default=default,
                alternative=alternative, family=family, logic=logic, cutoff=cutoff, **kw)


# Keyword sets shared by the extended library (selrm/rules_*.py).
SBP_KW = ["systolic", "blood pressure", "bp "]
VTE_KW = ["thrombo", "dvt", "pulmonary embol"]
CONF_KW = ["confus", "disorient"]
CANCER_KW = ["cancer", "lymphoma", "leukemia", "myeloma", "carcinoma"]
AGE = dict(nm=("numeric",))

# --------------------------------------------------------------------------
# Pilot library. Every rule is a stated test specification, not clinical
# guidance; labels are correct relative to the text shown in the prompt.
# --------------------------------------------------------------------------
RULES: list[Rule] = [
    Rule("strep_amox", "constraint", "Streptococcal pharyngitis",
         "For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient "
         "is allergic to penicillin, prescribe azithromycin instead.",
         [F("pen_allergy", "pen_allergy", "penicillin allergy", ["penicillin"])],
         "Presents with acute streptococcal pharyngitis (rapid antigen test positive).",
         default="amoxicillin", alternative="azithromycin", family="allergy_switch"),
    Rule("t2d_metformin", "constraint", "Type 2 diabetes initiation",
         "For newly diagnosed type 2 diabetes, start metformin. If the patient's current "
         "eGFR is below {thr_egfr} mL/min/1.73 m2, start sitagliptin instead.",
         [N("egfr", "egfr", "eGFR", ["egfr"], "<", 30, (45, 95), (12, 29), 6,
            alt_threshold=45)],
         "Newly diagnosed type 2 diabetes (HbA1c 7.9%).",
         default="metformin", alternative="sitagliptin", family="lab_threshold"),
    Rule("htn_pregnancy", "constraint", "Hypertension in women",
         "For newly diagnosed hypertension, start lisinopril. If the patient is "
         "currently pregnant, start labetalol instead.",
         [F("pregnancy", "pregnancy", "pregnancy", ["pregnan"])],
         "Newly diagnosed stage 2 hypertension (BP 152/96 mmHg on two visits).",
         default="lisinopril", alternative="labetalol", sex="female", age_range=(24, 42),
         family="state_switch"),
    Rule("vte_platelets", "constraint", "VTE prophylaxis",
         "For inpatient VTE prophylaxis, give enoxaparin. If the current platelet count "
         "is below {thr_plt} x10^9/L, use intermittent pneumatic compression instead.",
         [N("plt", "platelets", "platelet count", ["platelet"], "<", 50, (150, 380),
            (12, 49), 8, alt_threshold=100)],
         "Admitted for community-acquired pneumonia; immobile.",
         default="enoxaparin", alternative="intermittent pneumatic compression",
         family="lab_threshold"),
    Rule("pain_ulcer", "constraint", "Analgesia",
         "For musculoskeletal pain, prescribe ibuprofen. If the patient has an active "
         "peptic ulcer, prescribe acetaminophen instead.",
         [F("ulcer", "peptic_ulcer", "active peptic ulcer", ["ulcer"])],
         "Acute low back pain after lifting.",
         default="ibuprofen", alternative="acetaminophen", family="state_switch"),
    Rule("statin_alt", "constraint", "Statin initiation",
         "For primary prevention, start atorvastatin. If the current ALT is above "
         "{thr_alt} U/L, start ezetimibe instead.",
         [N("alt", "alt_enzyme", "ALT", ["alt "], ">", 120, (12, 60), (125, 400), 12,
            alt_threshold=80)],
         "Primary prevention; LDL cholesterol 182 mg/dL.",
         default="atorvastatin", alternative="ezetimibe", family="lab_threshold"),
    Rule("gout_clarith", "constraint", "Gout flare",
         "For an acute gout flare, prescribe colchicine. If the patient is currently "
         "taking clarithromycin, prescribe prednisone instead.",
         [F("clarith", "clarithromycin", "clarithromycin", ["clarithromycin"])],
         "Acute gout flare of the right first metatarsophalangeal joint.",
         default="colchicine", alternative="prednisone", family="drug_interaction"),
    Rule("migraine_cad", "constraint", "Acute migraine",
         "For acute migraine, prescribe sumatriptan. If the patient has ever had coronary "
         "artery disease (current or past), prescribe naproxen instead.",
         [F("cad", "cad", "coronary artery disease", ["coronary"], counts_past=True)],
         "Acute migraine without aura, typical of prior attacks.",
         default="sumatriptan", alternative="naproxen", family="history_switch"),
    Rule("contra_vte", "constraint", "Contraception",
         "For contraception, offer a combined oral contraceptive. If the patient or a "
         "first-degree relative (parent, sibling or child) has had a venous "
         "thromboembolism at any time, offer a progestin-only pill instead.",
         [F("vte", "vte", "venous thromboembolism", ["thrombo", "dvt", "pulmonary embol"],
            counts_past=True, counts_family=True)],
         "Requests contraception.",
         default="a combined oral contraceptive", alternative="a progestin-only pill",
         sex="female", age_range=(19, 38), family="family_switch"),
    Rule("curb65", "score", "CURB-65",
         "CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen "
         "above {thr_bun} mg/dL; respiratory rate of {thr_rr}/min or more; systolic "
         "blood pressure below {thr_sbp} mmHg; age {thr_age} years or more. Only current "
         "findings count.",
         [F("confusion", "confusion", "confusion", ["confus", "disorient"]),
          N("bun", "bun", "urea", ["bun", "urea nitrogen"], ">", 19, (8, 17), (21, 45), 4,
            alt_threshold=12),
          N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 30, (14, 24),
            (30, 40), 4),
          N("sbp", "sbp", "blood pressure", ["systolic", "blood pressure", "bp "], "<", 90,
            (104, 150), (70, 89), 8),
          N("age", "age", "age", ["age"], ">=", 65, (40, 60), (66, 88), 5,
            nm=("numeric",))],
         "Community-acquired pneumonia confirmed on chest radiograph.",
         family="additive_score"),
    Rule("chadsvasc", "score", "CHA2DS2-VASc (partial)",
         "CHA2DS2-VASc (as used here): 2 points for a stroke or TIA at any time; 1 point "
         "each for heart failure, hypertension, diabetes, or vascular disease (prior "
         "myocardial infarction or peripheral artery disease) at any time. Age and sex "
         "are scored separately and are not part of this question.",
         [F("stroke", "stroke", "stroke/TIA", ["stroke", "transient ischemic", "tia"],
            counts_past=True, points=2),
          F("chf", "chf", "heart failure", ["heart failure"], counts_past=True),
          F("diabetes", "diabetes", "diabetes", ["diabet"], counts_past=True),
          F("vascular", "vascular", "vascular disease",
            ["myocardial infarction", "peripheral artery", "heart attack"], counts_past=True)],
         "Newly detected atrial fibrillation.",
         age_range=(45, 63), family="additive_score"),
]

RULES_BY_ID = {r.rid: r for r in RULES}
