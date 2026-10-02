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
    cutoff: int | None = None      # constraint: switch iff points of met criteria >= cutoff
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
            if self.cutoff is None:
                return int(any(c.evaluate(mentions, overrides.get(c.cid)) for c in self.criteria))
            met = sum(c.points for c in self.criteria if c.evaluate(mentions, overrides.get(c.cid)))
            return int(met >= self.cutoff)
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

# --------------------------------------------------------------------------
# Library extension to about 40 rules (project spec). Shared keyword sets:
SBP_KW = ["systolic", "blood pressure", "bp "]
VTE_KW = ["thrombo", "dvt", "pulmonary embol"]
CONF_KW = ["confus", "disorient"]
CANCER_KW = ["cancer", "lymphoma", "leukemia", "myeloma", "carcinoma"]
AGE = dict(nm=("numeric",))

RULES += [
    # ---- constraint rules, seen families ----------------------------------
    Rule("ckd_nsaid", "constraint", "Osteoarthritis analgesia",
         "For knee osteoarthritis pain, prescribe naproxen. If the patient's current eGFR is "
         "below {thr_egfr} mL/min/1.73 m2, prescribe acetaminophen instead.",
         [N("egfr", "egfr", "eGFR", ["egfr"], "<", 60, (66, 110), (18, 55), 6,
            alt_threshold=75)],
         "Knee osteoarthritis with pain on walking.",
         default="naproxen", alternative="acetaminophen", age_range=(50, 79),
         family="lab_threshold"),
    Rule("hf_spironolactone", "constraint", "Heart failure therapy",
         "For heart failure with reduced ejection fraction, add spironolactone. If the current "
         "serum potassium is above {thr_k} mmol/L, add dapagliflozin instead.",
         [N("k", "potassium", "potassium", ["potassium"], ">", 5.0, (3.6, 4.6), (5.2, 6.4), 0.3,
            decimals=1, alt_threshold=4.5)],
         "Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.",
         default="spironolactone", alternative="dapagliflozin", age_range=(45, 79),
         family="lab_threshold"),
    Rule("htn_angioedema", "constraint", "Hypertension initiation",
         "For newly diagnosed hypertension, start lisinopril. If the patient has ever had "
         "angioedema (current or past), start amlodipine instead.",
         [F("angioedema", "angioedema", "angioedema", ["angioedema"], counts_past=True)],
         "Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).",
         default="lisinopril", alternative="amlodipine", family="history_switch"),
    Rule("af_asthma", "constraint", "Atrial fibrillation rate control",
         "For rate control in atrial fibrillation, start metoprolol. If the patient currently "
         "has asthma, start diltiazem instead.",
         [F("asthma", "asthma", "asthma", ["asthma"])],
         "Atrial fibrillation with a ventricular rate of 128/min.",
         default="metoprolol", alternative="diltiazem", age_range=(40, 79),
         family="state_switch"),
    Rule("af_valve", "constraint", "Atrial fibrillation anticoagulation",
         "For stroke prevention in atrial fibrillation, start apixaban. If the patient currently "
         "has a mechanical heart valve, start warfarin instead.",
         [F("valve", "mech_valve", "mechanical heart valve", ["mechanical"])],
         "Atrial fibrillation; anticoagulation indicated.",
         default="apixaban", alternative="warfarin", age_range=(45, 79), family="state_switch"),
    Rule("yeast_warfarin", "constraint", "Vaginal candidiasis",
         "For vaginal candidiasis, prescribe oral fluconazole. If the patient is currently "
         "taking warfarin, prescribe clotrimazole pessaries instead.",
         [F("warfarin", "warfarin", "warfarin", ["warfarin"])],
         "Vaginal itching and discharge; candidiasis confirmed on microscopy.",
         default="oral fluconazole", alternative="clotrimazole pessaries", sex="female",
         age_range=(25, 64), family="drug_interaction"),
    Rule("lyme_pregnancy", "constraint", "Early Lyme disease",
         "For early Lyme disease, prescribe doxycycline. If the patient is currently pregnant, "
         "prescribe amoxicillin instead.",
         [F("pregnancy", "pregnancy", "pregnancy", ["pregnan"])],
         "Erythema migrans rash ten days after a tick bite.",
         default="doxycycline", alternative="amoxicillin", sex="female", age_range=(20, 40),
         family="state_switch"),
    Rule("crc_screen", "constraint", "Colorectal cancer screening",
         "For colorectal cancer screening, order a fecal immunochemical test. If the patient or "
         "a first-degree relative (parent, sibling or child) has had colorectal cancer at any "
         "time, order a colonoscopy instead.",
         [F("crc", "crc", "colorectal cancer", ["colorectal cancer", "colon cancer", "bowel cancer"],
            counts_past=True, counts_family=True)],
         "Routine screening visit; no bowel symptoms.",
         default="a fecal immunochemical test", alternative="a colonoscopy", age_range=(45, 49),
         family="family_switch", verb="Order"),
    Rule("postop_hit", "constraint", "Postoperative thromboprophylaxis",
         "For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has "
         "ever had heparin-induced thrombocytopenia (current or past), prescribe fondaparinux "
         "instead.",
         [F("hit", "hit", "heparin-induced thrombocytopenia", ["heparin-induced"],
            counts_past=True)],
         "First day after elective total hip replacement.",
         default="enoxaparin", alternative="fondaparinux", age_range=(55, 84),
         family="history_switch"),
    Rule("uti_sulfa", "constraint", "Uncomplicated cystitis",
         "For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient is "
         "allergic to sulfonamide antibiotics, prescribe nitrofurantoin instead.",
         [F("sulfa", "sulfa_allergy", "sulfonamide allergy", ["sulfonamide", "sulfa"])],
         "Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.",
         default="trimethoprim-sulfamethoxazole", alternative="nitrofurantoin", sex="female",
         age_range=(18, 64), family="allergy_switch"),
    # ---- score rules (MedCalc-Bench style, partial), seen family ------------
    Rule("qsofa", "score", "qSOFA",
         "qSOFA (as used here): 1 point each for a respiratory rate of {thr_rr}/min or more; "
         "altered mentation; systolic blood pressure of {thr_sbp} mmHg or less. Only current "
         "findings count.",
         [N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 22, (12, 18), (22, 36), 3),
          F("mentation", "confusion", "altered mentation", CONF_KW),
          N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<=", 100, (110, 150), (72, 100), 6)],
         "Suspected urinary sepsis, assessed in the emergency department.",
         family="additive_score"),
    Rule("hasbled", "score", "HAS-BLED (partial)",
         "HAS-BLED (as used here, partial): 1 point each for a current systolic blood pressure "
         "above {thr_sbp} mmHg; a major bleeding event at any time; age above {thr_age} years; "
         "current use of aspirin. Other HAS-BLED items are not part of this question.",
         [N("sbp", "sbp", "systolic blood pressure", SBP_KW, ">", 160, (112, 150), (164, 196), 8),
          F("bleed", "bleeding", "bleeding history", ["bleed"], counts_past=True),
          N("age", "age", "age", ["age"], ">", 65, (45, 58), (67, 88), 4, **AGE),
          F("aspirin", "aspirin", "aspirin use", ["aspirin"])],
         "Atrial fibrillation; anticoagulation being considered.",
         family="additive_score"),
    Rule("padua", "score", "Padua (partial)",
         "Padua prediction score (as used here, partial): 3 points for active cancer; 3 points "
         "for a venous thromboembolism of the patient, current or previous; 1 point for age "
         "{thr_age} years or more; 1 point for current heart failure. Other Padua items are not "
         "part of this question.",
         [F("cancer", "cancer", "active cancer", CANCER_KW, points=3),
          F("vte", "vte", "venous thromboembolism", VTE_KW, counts_past=True, points=3),
          N("age", "age", "age", ["age"], ">=", 70, (40, 62), (71, 90), 5, **AGE),
          F("hf", "chf", "heart failure", ["heart failure"])],
         "Admitted with community-acquired pneumonia; expected to stay in bed for several days.",
         family="additive_score"),
    Rule("rcri", "score", "RCRI (partial)",
         "Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery "
         "disease at any time; heart failure at any time; a stroke or TIA at any time; a current "
         "serum creatinine above {thr_cr} mg/dL. Other items are not part of this question.",
         [F("cad", "cad", "coronary artery disease", ["coronary"], counts_past=True),
          F("hf", "chf", "heart failure", ["heart failure"], counts_past=True),
          F("stroke", "stroke", "stroke/TIA", ["stroke", "transient ischemic", "tia"],
            counts_past=True),
          N("cr", "creatinine", "creatinine", ["creatinine"], ">", 2.0, (0.6, 1.5), (2.2, 4.4), 0.3,
            decimals=1, alt_threshold=1.5)],
         "Preoperative assessment before elective colectomy.",
         age_range=(50, 84), family="additive_score"),
    Rule("sirs", "score", "SIRS (partial)",
         "SIRS criteria (as used here, partial): 1 point each for temperature above {thr_temp} C; "
         "heart rate above {thr_hr}/min; respiratory rate above {thr_rr}/min; white cell count "
         "above {thr_wbc} x10^9/L. Only current findings count.",
         [N("temp", "temperature", "temperature", ["temperature"], ">", 38.0, (36.2, 37.5),
            (38.4, 40.2), 0.4, decimals=1),
          N("hr", "heart_rate", "heart rate", ["heart rate"], ">", 90, (58, 84), (96, 140), 5),
          N("rr", "rr", "respiratory rate", ["respiratory rate"], ">", 20, (12, 16), (22, 34), 3),
          N("wbc", "wbc", "white cell count", ["white cell", "wbc"], ">", 12.0, (4.5, 10.8),
            (12.6, 22.0), 0.8, decimals=1)],
         "Productive cough for three days; assessed in the emergency department.",
         family="additive_score"),
    Rule("centor", "score", "Centor (partial)",
         "Centor score (as used here, partial): 1 point each for temperature above {thr_temp} C; "
         "tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.",
         [N("temp", "temperature", "temperature", ["temperature"], ">", 38.0, (36.4, 37.5),
            (38.2, 39.8), 0.4, decimals=1),
          F("exudate", "exudate", "tonsillar exudate", ["exudate"]),
          F("nodes", "neck_nodes", "tender cervical lymph nodes", ["lymph node", "lymphaden"])],
         "Sore throat for three days.",
         age_range=(16, 55), family="additive_score"),
    Rule("wells_dvt", "score", "Wells DVT (partial)",
         "Wells DVT score (as used here, partial): 1 point each for active cancer; a venous "
         "thromboembolism of the patient, current or previous; current calf swelling of "
         "{thr_calf} cm or more compared with the other leg. Other Wells items are not part of "
         "this question.",
         [F("cancer", "cancer", "active cancer", CANCER_KW),
          F("vte", "vte", "venous thromboembolism", VTE_KW, counts_past=True),
          N("calf", "calf_swelling", "calf swelling", ["calf circumference", "calf swelling"], ">=",
            3.0, (0.0, 1.5), (3.0, 6.0), 0.8, decimals=1)],
         "Left leg pain for two days after a long-haul flight.",
         family="additive_score"),
    Rule("news2_red", "score", "NEWS2 red items",
         "NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory "
         "rate of {thr_rr}/min or more; oxygen saturation of {thr_spo2}% or less; systolic blood "
         "pressure of {thr_sbp} mmHg or less; new confusion. Only current findings count.",
         [N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 25, (12, 20), (25, 38), 3,
            points=3),
          N("spo2", "spo2", "oxygen saturation", ["saturation", "spo2"], "<=", 91, (95, 100),
            (78, 91), 3, points=3),
          N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<=", 90, (104, 150), (70, 90), 6,
            points=3),
          F("confusion", "confusion", "new confusion", CONF_KW, points=3)],
         "Shortness of breath and fever; assessed on the medical ward.",
         family="additive_score"),
]

# --------------------------------------------------------------------------
# Grammar rules: held-out structural families, test only. G() writes the rule
# text from the family and (criterion, condition phrase) pairs; Rule.label is
# the program for every family (cutoff = points needed to switch).
HELDOUT_FAMILIES = frozenset({"any_of", "all_of", "two_of_three", "score_cutoff"})


def G(rid, family, title, intro, default, alternative, conds, setting, cutoff=None, **kw):
    crits = [c for c, _ in conds]
    head, switch = f"{intro}, prescribe {default}.", f"prescribe {alternative} instead"
    phrases = [p for _, p in conds]
    if family == "any_of":
        text = f"{head} If {' or '.join(phrases)}, {switch}."
    elif family == "all_of":
        text, cutoff = f"{head} If {' and '.join(phrases)}, {switch}.", len(crits)
    elif family == "two_of_three":
        text, cutoff = (f"{head} If at least two of the following apply, {switch}: "
                        f"{'; '.join(phrases)}."), 2
    elif family == "score_cutoff":
        items = "; ".join(f"{c.points} point{'s' if c.points > 1 else ''} for {p}"
                          for c, p in conds)
        text = f"{head} Score {items}. If the score is {cutoff} or more, {switch}."
    else:
        raise ValueError(family)
    return Rule(rid, "constraint", title, text, crits, setting, default=default,
                alternative=alternative, family=family, cutoff=cutoff, **kw)


RULES += [
    G("any_htn", "any_of", "Hypertension in women", "For newly diagnosed hypertension",
      "lisinopril", "amlodipine",
      [(F("pregnancy", "pregnancy", "pregnancy", ["pregnan"]), "the patient is currently pregnant"),
       (N("k", "potassium", "potassium", ["potassium"], ">", 5.0, (3.6, 4.6), (5.2, 6.4), 0.3,
          decimals=1), "the current serum potassium is above {thr_k} mmol/L")],
      "Newly diagnosed hypertension (blood pressure 150/96 mmHg on two visits).",
      sex="female", age_range=(24, 42)),
    G("any_gout", "any_of", "Gout flare", "For an acute gout flare", "naproxen", "colchicine",
      [(F("ulcer", "peptic_ulcer", "active peptic ulcer", ["ulcer"]),
        "the patient has an active peptic ulcer"),
       (N("egfr", "egfr", "eGFR", ["egfr"], "<", 30, (45, 95), (12, 29), 6),
        "the current eGFR is below {thr_egfr} mL/min/1.73 m2")],
      "Acute gout flare of the left knee."),
    G("any_ppx", "any_of", "Inpatient thromboprophylaxis",
      "For thromboprophylaxis in a medical inpatient", "enoxaparin", "compression stockings",
      [(N("plt", "platelets", "platelet count", ["platelet"], "<", 50, (150, 380), (12, 49), 8),
        "the current platelet count is below {thr_plt} x10^9/L"),
       (F("hit", "hit", "heparin-induced thrombocytopenia", ["heparin-induced"], counts_past=True),
        "the patient has ever had heparin-induced thrombocytopenia (current or past)")],
      "Admitted with a urinary tract infection; mobility reduced.", age_range=(50, 84)),
    G("all_metformin", "all_of", "Metformin dosing", "For type 2 diabetes",
      "metformin 1000 mg twice daily", "metformin 500 mg twice daily",
      [(N("egfr", "egfr", "eGFR", ["egfr"], "<", 45, (50, 95), (25, 44), 4),
        "the current eGFR is below {thr_egfr} mL/min/1.73 m2"),
       (N("age", "age", "age", ["age"], ">=", 75, (55, 70), (76, 90), 4, **AGE),
        "the patient is aged {thr_age} years or more")],
      "Type 2 diabetes on metformin; annual medication review."),
    G("all_gastro", "all_of", "Gastroprotection", "For hip osteoarthritis pain",
      "naproxen alone", "naproxen with omeprazole",
      [(N("age", "age", "age", ["age"], ">=", 65, (40, 58), (66, 85), 4, **AGE),
        "the patient is aged {thr_age} years or more"),
       (F("aspirin", "aspirin", "aspirin use", ["aspirin"]),
        "the patient is currently taking aspirin")],
      "Hip osteoarthritis with pain on walking."),
    G("all_spiro", "all_of", "Spironolactone dosing",
      "For heart failure with reduced ejection fraction", "spironolactone 25 mg daily",
      "spironolactone 12.5 mg daily",
      [(N("k", "potassium", "potassium", ["potassium"], ">", 4.8, (3.6, 4.5), (4.9, 5.4), 0.2,
          decimals=1), "the current serum potassium is above {thr_k} mmol/L"),
       (N("egfr", "egfr", "eGFR", ["egfr"], "<", 50, (55, 95), (30, 49), 4),
        "the current eGFR is below {thr_egfr} mL/min/1.73 m2")],
      "Heart failure with reduced ejection fraction (ejection fraction 32%).",
      age_range=(50, 84)),
    G("two_apixaban", "two_of_three", "Apixaban dosing",
      "For stroke prevention in atrial fibrillation", "apixaban 5 mg twice daily",
      "apixaban 2.5 mg twice daily",
      [(N("age", "age", "age", ["age"], ">=", 80, (60, 76), (81, 94), 3, **AGE),
        "the patient is aged {thr_age} years or more"),
       (N("wt", "weight", "weight", ["weight", "weighs"], "<=", 60, (66, 98), (42, 60), 4),
        "the current weight is {thr_wt} kg or less"),
       (N("cr", "creatinine", "creatinine", ["creatinine"], ">=", 1.5, (0.6, 1.2), (1.5, 2.8),
          0.2, decimals=1), "the current serum creatinine is {thr_cr} mg/dL or more")],
      "Atrial fibrillation; anticoagulation indicated."),
    G("two_pneumonia", "two_of_three", "Pneumonia treatment", "For community-acquired pneumonia",
      "oral amoxicillin", "intravenous co-amoxiclav",
      [(F("confusion", "confusion", "new confusion", CONF_KW), "the patient has new confusion"),
       (N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 30, (14, 24), (30, 40), 4),
        "the current respiratory rate is {thr_rr}/min or more"),
       (N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<", 90, (104, 150), (70, 89), 8),
        "the current systolic blood pressure is below {thr_sbp} mmHg")],
      "Community-acquired pneumonia confirmed on chest radiograph.", age_range=(40, 79)),
    G("two_throat", "two_of_three", "Sore throat", "For acute sore throat", "ibuprofen",
      "penicillin V",
      [(N("temp", "temperature", "temperature", ["temperature"], ">", 38.0, (36.4, 37.5),
          (38.2, 39.8), 0.4, decimals=1), "the current temperature is above {thr_temp} C"),
       (F("exudate", "exudate", "tonsillar exudate", ["exudate"]),
        "the patient currently has tonsillar exudate"),
       (F("nodes", "neck_nodes", "tender cervical lymph nodes", ["lymph node", "lymphaden"]),
        "the patient currently has tender anterior cervical lymph nodes")],
      "Sore throat for two days.", age_range=(16, 55)),
    G("cut_vte", "score_cutoff", "Inpatient thromboprophylaxis score",
      "For thromboprophylaxis in a medical inpatient", "compression stockings", "enoxaparin",
      [(F("cancer", "cancer", "active cancer", CANCER_KW, points=3), "active cancer"),
       (F("vte", "vte", "venous thromboembolism", VTE_KW, counts_past=True, points=3),
        "a venous thromboembolism of the patient, current or previous"),
       (N("age", "age", "age", ["age"], ">=", 70, (40, 62), (71, 90), 5, **AGE),
        "age {thr_age} years or more"),
       (F("hf", "chf", "heart failure", ["heart failure"]), "current heart failure")],
      "Admitted with community-acquired pneumonia; expected to stay in bed for several days.",
      cutoff=4),
    G("cut_sepsis", "score_cutoff", "Sepsis escalation",
      "For suspected infection on the medical ward", "oral amoxicillin",
      "intravenous piperacillin-tazobactam",
      [(N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 22, (12, 18), (22, 36), 3,
          points=2), "a current respiratory rate of {thr_rr}/min or more"),
       (F("mentation", "confusion", "altered mentation", CONF_KW), "current altered mentation"),
       (N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<=", 100, (110, 150), (72, 100), 6),
        "a current systolic blood pressure of {thr_sbp} mmHg or less")],
      "Suspected chest infection; assessed on the medical ward.", cutoff=3),
    G("cut_bleed", "score_cutoff", "Antiplatelet choice",
      "For dual antiplatelet therapy after a myocardial infarction", "aspirin plus ticagrelor",
      "aspirin plus clopidogrel",
      [(F("bleed", "bleeding", "bleeding history", ["bleed"], counts_past=True, points=2),
        "a major bleeding event at any time"),
       (N("age", "age", "age", ["age"], ">=", 75, (50, 70), (76, 90), 4, **AGE),
        "age {thr_age} years or more"),
       (N("egfr", "egfr", "eGFR", ["egfr"], "<", 30, (45, 95), (12, 29), 6),
        "a current eGFR below {thr_egfr} mL/min/1.73 m2")],
      "Recovering on the ward after a myocardial infarction treated with a stent.", cutoff=2),
]

RULES_BY_ID = {r.rid: r for r in RULES}
