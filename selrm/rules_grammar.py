"""Grammar-composed constraint rules. G() writes the rule text from a structural
family and (criterion, condition phrase) pairs; Rule.label with Rule.logic is
the program for every family."""
from selrm.rules import AGE, CANCER_KW, CONF_KW, SBP_KW, VTE_KW, F, G, N, Rule  # noqa: F401


RULES = [
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


# --------------------------------------------------------------------------
# Grammar-sampled rules (A-D3). A rule = scenario x operator x typed conditions.
# Conditions reuse concepts that have phrase banks; applicability is part of the
# condition (current only, at any time, patient or first-degree relative), and
# numeric conditions reuse threshold configurations the library already tests.
# Two concepts are never combined if a template of one names the other.
import random as _random  # noqa: E402
from itertools import combinations as _combinations  # noqa: E402

from selrm import phrases as _P  # noqa: E402

FINDING_CONDITIONS = {   # concept -> {applicability: (phrase in the rule, criterion label)}
    "pen_allergy": {"current": ("the patient is allergic to penicillin", "penicillin allergy")},
    "sulfa_allergy": {"current": ("the patient is allergic to sulfonamide antibiotics",
                                  "sulfonamide allergy")},
    "pregnancy": {"current": ("the patient is currently pregnant", "pregnancy")},
    "peptic_ulcer": {"current": ("the patient has an active peptic ulcer", "active peptic ulcer"),
                     "ever": ("the patient has ever had a peptic ulcer (current or past)",
                              "peptic ulcer at any time")},
    "clarithromycin": {"current": ("the patient is currently taking clarithromycin", "clarithromycin")},
    "warfarin": {"current": ("the patient is currently taking warfarin", "warfarin")},
    "aspirin": {"current": ("the patient is currently taking aspirin", "aspirin use")},
    "cad": {"ever": ("the patient has ever had coronary artery disease (current or past)",
                     "coronary artery disease"),
            "family": ("the patient or a first-degree relative (parent, sibling or child) has had "
                       "coronary artery disease at any time", "coronary artery disease in the family")},
    "vte": {"current": ("the patient currently has a venous thromboembolism",
                        "current venous thromboembolism"),
            "ever": ("the patient has ever had a venous thromboembolism (current or past)",
                     "venous thromboembolism"),
            "family": ("the patient or a first-degree relative (parent, sibling or child) has had "
                       "a venous thromboembolism at any time", "venous thromboembolism in the family")},
    "stroke": {"ever": ("the patient has ever had a stroke or TIA (current or past)", "stroke/TIA")},
    "chf": {"current": ("the patient currently has heart failure", "current heart failure"),
            "ever": ("the patient has ever had heart failure (current or past)", "heart failure")},
    "diabetes": {"ever": ("the patient has ever had diabetes (current or past)", "diabetes"),
                 "family": ("the patient or a first-degree relative (parent, sibling or child) has "
                            "had diabetes at any time", "diabetes in the family")},
    "vascular": {"ever": ("the patient has ever had a myocardial infarction or peripheral artery "
                          "disease (current or past)", "vascular disease")},
    "confusion": {"current": ("the patient has new confusion", "new confusion")},
    "angioedema": {"ever": ("the patient has ever had angioedema (current or past)", "angioedema")},
    "asthma": {"current": ("the patient currently has asthma", "asthma"),
               "ever": ("the patient has ever had asthma (current or past)", "asthma at any time")},
    "mech_valve": {"current": ("the patient currently has a mechanical heart valve",
                               "mechanical heart valve")},
    "hit": {"ever": ("the patient has ever had heparin-induced thrombocytopenia (current or past)",
                     "heparin-induced thrombocytopenia")},
    "crc": {"family": ("the patient or a first-degree relative (parent, sibling or child) has had "
                       "colorectal cancer at any time", "colorectal cancer")},
    "bleeding": {"current": ("the patient currently has a major bleed", "active major bleeding"),
                 "ever": ("the patient has had a major bleeding event at any time", "bleeding history")},
    "cancer": {"current": ("the patient has active cancer", "active cancer"),
               "ever": ("the patient has had cancer at any time (active or in remission)",
                        "cancer at any time")},
    "exudate": {"current": ("the patient currently has tonsillar exudate", "tonsillar exudate")},
    "neck_nodes": {"current": ("the patient currently has tender anterior cervical lymph nodes",
                               "tender cervical lymph nodes")},
}
NUMERIC_NAMES = {   # concept -> (name in the rule, unit)
    "egfr": ("eGFR", "mL/min/1.73 m2"), "platelets": ("platelet count", "x10^9/L"),
    "alt_enzyme": ("ALT", "U/L"), "bun": ("blood urea nitrogen", "mg/dL"),
    "rr": ("respiratory rate", "/min"), "sbp": ("systolic blood pressure", "mmHg"),
    "age": ("age", "years"), "potassium": ("serum potassium", "mmol/L"),
    "creatinine": ("serum creatinine", "mg/dL"), "temperature": ("temperature", "C"),
    "heart_rate": ("heart rate", "/min"), "wbc": ("white cell count", "x10^9/L"),
    "spo2": ("oxygen saturation", "%"), "weight": ("weight", "kg"),
    "calf_swelling": ("calf swelling compared with the other leg", "cm"),
}
SCENARIOS = [   # (intro, default, alternative, setting, sex, age_range)
    ("For acute streptococcal pharyngitis", "amoxicillin", "azithromycin",
     "Presents with acute streptococcal pharyngitis (rapid antigen test positive).", None, (18, 70)),
    ("For newly diagnosed type 2 diabetes", "metformin", "sitagliptin",
     "Newly diagnosed type 2 diabetes (HbA1c 7.9%).", None, (35, 79)),
    ("For newly diagnosed hypertension", "lisinopril", "amlodipine",
     "Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).", None, (30, 79)),
    ("For inpatient VTE prophylaxis", "enoxaparin", "intermittent pneumatic compression",
     "Admitted for community-acquired pneumonia; immobile.", None, (40, 89)),
    ("For musculoskeletal pain", "ibuprofen", "acetaminophen",
     "Acute low back pain after lifting.", None, (20, 70)),
    ("For primary prevention", "atorvastatin", "ezetimibe",
     "Primary prevention; LDL cholesterol 182 mg/dL.", None, (40, 75)),
    ("For an acute gout flare", "colchicine", "prednisone",
     "Acute gout flare of the right first metatarsophalangeal joint.", None, (35, 85)),
    ("For acute migraine", "sumatriptan", "naproxen",
     "Acute migraine without aura, typical of prior attacks.", None, (18, 60)),
    ("For contraception", "a combined oral contraceptive", "a progestin-only pill",
     "Requests contraception.", "female", (19, 40)),
    ("For knee osteoarthritis pain", "naproxen", "acetaminophen",
     "Knee osteoarthritis with pain on walking.", None, (50, 85)),
    ("For heart failure with reduced ejection fraction", "spironolactone", "dapagliflozin",
     "Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.", None,
     (45, 85)),
    ("For rate control in atrial fibrillation", "metoprolol", "diltiazem",
     "Atrial fibrillation with a ventricular rate of 128/min.", None, (40, 85)),
    ("For stroke prevention in atrial fibrillation", "apixaban", "warfarin",
     "Atrial fibrillation; anticoagulation indicated.", None, (45, 85)),
    ("For vaginal candidiasis", "oral fluconazole", "clotrimazole pessaries",
     "Vaginal itching and discharge; candidiasis confirmed on microscopy.", "female", (20, 64)),
    ("For early Lyme disease", "doxycycline", "amoxicillin",
     "Erythema migrans rash ten days after a tick bite.", None, (18, 70)),
    ("For thromboprophylaxis after hip replacement", "enoxaparin", "fondaparinux",
     "First day after elective total hip replacement.", None, (55, 89)),
    ("For uncomplicated cystitis", "trimethoprim-sulfamethoxazole", "nitrofurantoin",
     "Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.", "female",
     (18, 70)),
    ("For community-acquired pneumonia", "oral amoxicillin", "intravenous co-amoxiclav",
     "Community-acquired pneumonia confirmed on chest radiograph.", None, (30, 89)),
    ("For acute sore throat", "ibuprofen", "penicillin V", "Sore throat for two days.", None, (16, 60)),
    ("For suspected infection on the medical ward", "oral amoxicillin",
     "intravenous piperacillin-tazobactam", "Suspected chest infection; assessed on the medical ward.",
     None, (40, 89)),
    ("For dual antiplatelet therapy after a myocardial infarction", "aspirin plus ticagrelor",
     "aspirin plus clopidogrel",
     "Recovering on the ward after a myocardial infarction treated with a stent.", None, (40, 89)),
    ("For hip osteoarthritis pain", "naproxen alone", "naproxen with omeprazole",
     "Hip osteoarthritis with pain on walking.", None, (45, 85)),
    ("For community-acquired pneumonia treated at home", "amoxicillin", "doxycycline",
     "Productive cough and fever; consolidation on chest radiograph.", None, (18, 80)),
    ("For cellulitis of the lower leg", "cephalexin", "clindamycin",
     "Spreading redness and warmth of the right shin for two days.", None, (18, 85)),
]
# Concepts a scenario's setting already decides or contradicts (a new diabetes
# diagnosis is diabetes; a myocardial infarction is coronary and vascular disease
# and implies antiplatelet and heparin exposure; a stated rate, pressure or fever
# fixes that value); the sampler never pairs them.
EXCLUDE = {
    "Newly diagnosed type 2 diabetes (HbA1c 7.9%).": {"diabetes"},
    "Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).": {"sbp"},
    "Primary prevention; LDL cholesterol 182 mg/dL.": {"cad", "vascular", "stroke"},
    "Requests contraception.": {"pregnancy"},
    "Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.": {"chf"},
    "Atrial fibrillation with a ventricular rate of 128/min.": {"heart_rate"},
    "Recovering on the ward after a myocardial infarction treated with a stent.":
        {"cad", "vascular", "aspirin", "hit"},
    "Productive cough and fever; consolidation on chest radiograph.": {"temperature"},
    "Spreading redness and warmth of the right shin for two days.": {"calf_swelling"},
}

# Concept pairs never sampled into one rule: a line of one implies the other (a
# myocardial infarction is coronary disease; warfarin "for blood clots" implies
# VTE) or their values are coupled (eGFR and creatinine, weight and BMI).
COUPLED = ({"cad", "vascular"}, {"vte", "warfarin"}, {"egfr", "creatinine"}, {"weight", "bmi"},
           {"sbp", "map"})

OPERATORS = (("single", 0.2), ("any_of", 0.25), ("all_of", 0.2), ("two_of_three", 0.15),
             ("score_cutoff", 0.2))


def _hand_written():
    from selrm import rules as _R, rules_constraint as _C, rules_score as _S
    return _R.RULES + _C.RULES + _S.RULES + RULES


def _numeric_configs():
    """Threshold configurations already used by hand-written rules, per concept."""
    out = {}
    for r in _hand_written():
        for c in r.criteria:
            if c.kind == "numeric":
                cfg = (c.op, c.threshold, c.default_range, c.flip_range, c.near_delta, c.decimals,
                       tuple(c.keywords))
                out.setdefault(c.concept, [])
                if cfg not in out[c.concept]:
                    out[c.concept].append(cfg)
    return out


def _finding_keywords():
    out = {}
    for r in _hand_written():
        for c in r.criteria:
            if c.kind == "finding":
                out.setdefault(c.concept, tuple(c.keywords))
    return out


def _collisions(keywords):
    """Concept pairs where a template of one contains a keyword of the other."""
    bad = set()
    for a, bank in _P.BANKS.items():
        texts = [t.lower() for L in bank.values() for t in L]
        for b, ks in keywords.items():
            if a != b and any(k in t for t in texts for k in ks):
                bad.add(frozenset((a, b)))
    return bad


def _has_forms(concept, variant):
    """The concept's bank has every form the criterion's cases render."""
    if variant == "value":
        need = {"current"} if concept == "age" else {"current", "past", "superseded"}
    else:
        need = {"generic", "present", "absent", "rel", "past"} | \
            ({"rel_past"} if variant in ("ever", "family") else set())
    return need <= set(_P.BANKS.get(concept, {}))


def _condition(concept, variant, cid, numeric_cfg, finding_kw, points=1):
    if numeric_cfg is None:
        phrase, label = FINDING_CONDITIONS[concept][variant]
        return F(cid, concept, label, finding_kw[concept], counts_past=variant in ("ever", "family"),
                 counts_family=variant == "family", points=points), phrase
    op, thr, dr, fr, nd, dec, kw = numeric_cfg
    name, unit = NUMERIC_NAMES[concept]
    slot = "{thr_%s}%s%s" % (cid, "" if unit[0] in "/%" else " ", unit)
    subject = "the age of the patient" if concept == "age" else f"the current {name}"
    phrase = {"<": f"{subject} is below {slot}", ">": f"{subject} is above {slot}",
              ">=": f"{subject} is {slot} or more", "<=": f"{subject} is {slot} or less"}[op]
    label = "calf swelling" if concept == "calf_swelling" else name
    extra = {"nm": ("numeric",)} if concept == "age" else {}
    return N(cid, concept, label, list(kw), op, thr, dr, fr, nd, decimals=dec, points=points,
             **extra), phrase


def sample_rules(n=250, seed=2027, scenarios=None, prefix="gs", title="Sampled rule"):
    """n grammar-sampled constraint rules; deterministic for fixed banks and seed."""
    rng = _random.Random(seed)
    num_cfg, fkw = _numeric_configs(), _finding_keywords()
    keywords = {**fkw, **{c: cfgs[0][6] for c, cfgs in num_cfg.items()}}
    bad = _collisions(keywords)
    variants = [(c, v) for c, vs in FINDING_CONDITIONS.items() for v in vs if _has_forms(c, v)] + \
               [(c, "value") for c in NUMERIC_NAMES if c in num_cfg and _has_forms(c, "value")]
    ops, weights = zip(*OPERATORS)
    out, seen = [], set()
    while len(out) < n:
        intro, default, alt, setting, sex, ages = rng.choice(scenarios or SCENARIOS)
        op = rng.choices(ops, weights)[0]
        k = {"single": 1, "any_of": 2, "all_of": 2, "two_of_three": 3,
             "score_cutoff": rng.choice((3, 4))}[op]
        pool = [(c, v) for c, v in variants
                if not any(kw in setting.lower() for kw in keywords[c]) and c not in EXCLUDE.get(setting, ())
                and (c != "pregnancy" or (sex == "female" and ages[1] <= 45))]
        chosen = []
        for c, v in rng.sample(pool, len(pool)):
            if len(chosen) == k:
                break
            if all(c != d and frozenset((c, d)) not in bad and {c, d} not in COUPLED for d, _ in chosen):
                chosen.append((c, v))
        key = (setting, op, tuple(sorted(chosen)))
        if len(chosen) < k or key in seen:
            continue
        points, cutoff = [1] * k, None
        if op == "score_cutoff":
            points = [rng.choice((1, 2, 3)) for _ in range(k)]
            lo, hi = max(points) + 1, sum(points) - min(points) + 1
            if len(set(points)) == 1 or lo > hi:
                continue
            cutoff = rng.randint(lo, hi)
        conds = [_condition(c, v, f"c{i + 1}", rng.choice(num_cfg[c]) if v == "value" else None,
                            fkw, points[i]) for i, (c, v) in enumerate(chosen)]
        rid, name = f"{prefix}{len(out):03d}", f"{title} {len(out):03d}"
        if op == "single":
            (crit, phrase), = conds
            rule = Rule(rid, "constraint", name,
                        f"{intro}, prescribe {default}. If {phrase}, prescribe {alt} instead.",
                        [crit], setting, default=default, alternative=alt, sex=sex, age_range=ages)
        else:
            rule = G(rid, op, name, intro, default, alt, conds, setting, cutoff=cutoff, sex=sex,
                     age_range=ages)
        rule.family = f"g_{op}"
        if not all(pivots_exist(rule, c) for c in rule.criteria):
            continue
        seen.add(key)
        out.append(rule)
    return out


def pivots_exist(rule, crit):
    """Some set of the other criteria makes crit alone decide the conclusion."""
    def w(c):
        return c.points if rule.logic == "atleast" else 1
    cut = {"any": 1, "all": len(rule.criteria), "atleast": rule.cutoff}[rule.logic]
    others = [c for c in rule.criteria if c is not crit]
    return any(sum(map(w, s)) < cut <= sum(map(w, s)) + w(crit)
               for k in range(len(others) + 1) for s in _combinations(others, k))


# L3-inv: the same grammar over invented conditions and orders (neutral names,
# no clinical meaning). These rules are test-only and never enter LIBRARY.
INVENTED = [("Varnell syndrome", "lorvatide", "pemraxin"), ("Okata fever", "solvadine", "tarnicept"),
            ("Tessaly disease", "velimor", "quantrel"), ("Quorin syndrome", "ostravin", "dalmerol"),
            ("Delmar fever", "fenrastat", "kivolane"), ("Pallis disease", "brexadol", "corlitane"),
            ("Corvane syndrome", "zephalin", "trivosan"), ("Hestin disease", "melcadine", "orvitrex"),
            ("Ulvar fever", "pandiloxin", "sertavane"), ("Mirelle syndrome", "hylomide", "renquazol"),
            ("Zentha disease", "valtimide", "isomarin"), ("Brask fever", "gendrotil", "lumacept")]


def invented_rules(n=60, seed=2028):
    scen = [(f"For {c}", a, b, f"Referred with {c}.", None, (25, 75)) for c, a, b in INVENTED]
    return sample_rules(n, seed, scen, prefix="inv", title="Invented rule")


SAMPLED = sample_rules()

