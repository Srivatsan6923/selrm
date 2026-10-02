"""Additive scoring rules (MedCalc-Bench style, partial definitions)."""
from selrm.rules import AGE, CANCER_KW, CONF_KW, F, N, SBP_KW, VTE_KW, Rule

RULES = [
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


# ---- batch S1 ----
# Batch S1: partial additive scores from acute and critical care (sepsis,
# pneumonia severity, early-warning and respiratory scores). New concepts:
# arterial_ph, map, supp_oxygen (banks in S1_banks.json).
BUN_KW = ["bun", "urea nitrogen"]
SPO2_KW = ["saturation", "spo2"]
PH_KW = ["arterial ph", "arterial blood gas"]
# Low-side temperature and white cell count: numeric/boundary near-misses only, because the
# past and superseded templates of those banks describe raised values ("peaked at", "reached").
LOW_ONLY = dict(nm=("numeric",))

_S1 = [
    Rule("s1_psi", "score", "PSI (partial)",
         "Pneumonia Severity Index (as used here, partial): 30 points for active cancer; "
         "10 points for current heart failure; 10 points for a stroke or TIA at any time; "
         "30 points for a current arterial pH below {thr_ph}; 20 points for a current blood urea "
         "nitrogen of {thr_bun} mg/dL or more. Age, sex and other items of the index are not part "
         "of this question.",
         [F("cancer", "cancer", "active cancer", CANCER_KW, points=30),
          F("hf", "chf", "heart failure", ["heart failure"], points=10),
          F("stroke", "stroke", "stroke/TIA", ["stroke", "transient ischemic", "tia"],
            counts_past=True, points=10),
          N("ph", "arterial_ph", "arterial pH", PH_KW, "<", 7.35, (7.38, 7.45), (7.20, 7.34), 0.03,
            decimals=2, points=30),
          N("bun", "bun", "blood urea nitrogen", BUN_KW, ">=", 30, (8, 24), (30, 60), 4,
            alt_threshold=20, points=20)],
         "Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.",
         age_range=(45, 89), family="additive_score"),
    Rule("s1_smartcop", "score", "SMART-COP (partial)",
         "SMART-COP (as used here, partial, for patients older than 50 years): 2 points for a current "
         "systolic blood pressure below {thr_sbp} mmHg; 1 point for a current respiratory rate of "
         "{thr_rr}/min or more; 1 point for a current heart rate of {thr_hr}/min or more; 2 points "
         "for a current oxygen saturation of {thr_spo2}% or less; 2 points for a current arterial pH "
         "below {thr_ph}. Other SMART-COP items are not part of this question.",
         [N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<", 90, (104, 150), (70, 89), 8,
            points=2),
          N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 30, (14, 24), (30, 40), 4),
          N("hr", "heart_rate", "heart rate", ["heart rate"], ">=", 125, (60, 110), (125, 150), 5),
          N("spo2", "spo2", "oxygen saturation", SPO2_KW, "<=", 90, (94, 100), (78, 90), 3,
            points=2),
          N("ph", "arterial_ph", "arterial pH", PH_KW, "<", 7.35, (7.38, 7.45), (7.20, 7.34), 0.03,
            decimals=2, points=2)],
         "Admitted with community-acquired pneumonia; reviewed by the medical team.",
         age_range=(51, 89), family="additive_score"),
    Rule("s1_adrop", "score", "A-DROP (partial)",
         "A-DROP (as used here, partial): 1 point each for a current blood urea nitrogen of "
         "{thr_bun} mg/dL or more; a current oxygen saturation of {thr_spo2}% or less; new confusion "
         "or disorientation; a current systolic blood pressure of {thr_sbp} mmHg or less. Age is "
         "scored separately and is not part of this question.",
         [N("bun", "bun", "blood urea nitrogen", BUN_KW, ">=", 21, (8, 16), (21, 45), 4),
          N("spo2", "spo2", "oxygen saturation", SPO2_KW, "<=", 90, (94, 100), (78, 90), 3),
          F("confusion", "confusion", "new confusion", CONF_KW),
          N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<=", 90, (104, 150), (70, 90), 6)],
         "Fever and cough with new consolidation on chest radiograph.",
         age_range=(40, 85), family="additive_score"),
    Rule("s1_idsa_minor", "score", "IDSA/ATS minor criteria (partial)",
         "IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): "
         "1 point each for a current white cell count below {thr_wbc} x10^9/L; a current platelet "
         "count below {thr_plt} x10^9/L; a current temperature below {thr_temp} C; a current blood "
         "urea nitrogen of {thr_bun} mg/dL or more. Other criteria are not part of this question.",
         [N("wbc", "wbc", "white cell count", ["white cell", "wbc"], "<", 4.0, (5.0, 16.0),
            (1.5, 3.9), 0.8, decimals=1, **LOW_ONLY),
          N("plt", "platelets", "platelet count", ["platelet"], "<", 100, (150, 380), (30, 99), 8,
            alt_threshold=150),
          N("temp", "temperature", "temperature", ["temperature"], "<", 36.0, (36.4, 39.0),
            (34.0, 35.9), 0.4, decimals=1, **LOW_ONLY),
          N("bun", "bun", "blood urea nitrogen", BUN_KW, ">=", 20, (8, 15), (20, 45), 4)],
         "Community-acquired pneumonia on chest radiograph; admitted to the medical ward.",
         age_range=(40, 85), family="additive_score"),
    Rule("s1_mews", "score", "MEWS (partial)",
         "Modified Early Warning Score (as used here, partial: only the stated band of each listed "
         "item): 3 points for a systolic blood pressure of {thr_sbp} mmHg or less; 3 points for a "
         "heart rate of {thr_hr}/min or more; 3 points for a respiratory rate of {thr_rr}/min or "
         "more; 2 points for a temperature of {thr_temp} C or more. Any other value of these items "
         "scores 0 here, and the other MEWS items are not part of this question. Only current "
         "findings count.",
         # Base values all score 0 in the published MEWS too (RR 9-14, SBP 101-199, HR 51-100,
         # T 35-38.4); near-misses fall in its 2-point bands, which the text explicitly zeroes.
         [N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<=", 70, (101, 150), (55, 70), 6,
            points=3),
          N("hr", "heart_rate", "heart rate", ["heart rate"], ">=", 130, (55, 100), (130, 160), 5,
            points=3),
          N("rr", "rr", "respiratory rate", ["respiratory rate"], ">=", 30, (12, 14), (30, 40), 4,
            points=3),
          N("temp", "temperature", "temperature", ["temperature"], ">=", 38.5, (36.0, 38.0),
            (38.5, 40.2), 0.4, decimals=1, points=2)],
         "Abdominal pain and vomiting; assessed on the surgical admissions unit.",
         age_range=(30, 79), family="additive_score"),
    Rule("s1_news2_other", "score", "NEWS2 other items (partial)",
         "NEWS2 (as used here, partial: only the stated band of each listed item): 3 points for a "
         "heart rate of {thr_hr}/min or more; 3 points for a systolic blood pressure of {thr_sbp} "
         "mmHg or more; 2 points for a temperature of {thr_temp} C or more; 2 points for current "
         "use of supplemental oxygen. Any other value of these items scores 0 here, and the other "
         "NEWS2 items are not part of this question. Only current findings count.",
         [N("hr", "heart_rate", "heart rate", ["heart rate"], ">=", 131, (55, 90), (131, 160), 4,
            points=3),
          N("sbp", "sbp", "systolic blood pressure", SBP_KW, ">=", 220, (111, 180), (220, 250), 8,
            points=3),
          N("temp", "temperature", "temperature", ["temperature"], ">=", 39.1, (36.2, 38.0),
            (39.1, 40.5), 0.4, decimals=1, points=2),
          F("o2", "supp_oxygen", "supplemental oxygen", ["supplemental oxygen"], points=2)],
         "Newly admitted to the medical ward with a chest infection.",
         age_range=(35, 89), family="additive_score"),
    Rule("s1_sofa", "score", "SOFA (partial)",
         "SOFA score (as used here, partial): 1 point each for a current platelet count below "
         "{thr_plt} x10^9/L; a current serum creatinine of {thr_cr} mg/dL or more; a current mean "
         "arterial pressure below {thr_map} mmHg. Other SOFA items are not part of this question.",
         [N("plt", "platelets", "platelet count", ["platelet"], "<", 150, (160, 380), (100, 149), 8),
          N("cr", "creatinine", "creatinine", ["creatinine"], ">=", 1.2, (0.5, 0.9), (1.2, 1.9), 0.3,
            decimals=1),
          N("map", "map", "mean arterial pressure", ["mean arterial pressure"], "<", 70, (76, 105),
            (55, 69), 5)],
         "Sepsis from a chest infection; admitted to the intensive care unit.",
         age_range=(40, 85), family="additive_score"),
    Rule("s1_meds", "score", "MEDS (partial)",
         "Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a "
         "current platelet count below {thr_plt} x10^9/L; 3 points for an age above {thr_age} years; "
         "2 points for current altered mental status (confusion or disorientation). Other items of "
         "the score are not part of this question.",
         [N("plt", "platelets", "platelet count", ["platelet"], "<", 150, (160, 380), (40, 149), 8,
            points=3),
          N("age", "age", "age", ["age"], ">", 65, (45, 58), (67, 88), 4, points=3, **AGE),
          F("ams", "confusion", "altered mental status", CONF_KW, points=2)],
         "Suspected sepsis; admitted from the emergency department.",
         family="additive_score"),
    Rule("s1_bap65", "score", "BAP-65 (partial)",
         "BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of "
         "{thr_bun} mg/dL or more; current altered mental status (confusion or disorientation); a "
         "current heart rate of {thr_hr}/min or more. Age is scored separately and is not part of "
         "this question.",
         [N("bun", "bun", "blood urea nitrogen", BUN_KW, ">=", 25, (8, 20), (25, 50), 4),
          F("ams", "confusion", "altered mental status", CONF_KW),
          N("hr", "heart_rate", "heart rate", ["heart rate"], ">=", 109, (60, 100), (109, 140), 5)],
         "Acute exacerbation of COPD; assessed in the emergency department.",
         age_range=(45, 89), family="additive_score"),
    Rule("s1_spesi", "score", "sPESI (partial)",
         "Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for "
         "active cancer; a current heart rate of {thr_hr}/min or more; a current systolic blood "
         "pressure below {thr_sbp} mmHg; a current oxygen saturation below {thr_spo2}%; an age above "
         "{thr_age} years. Other items of the index are not part of this question.",
         [F("cancer", "cancer", "active cancer", CANCER_KW),
          N("hr", "heart_rate", "heart rate", ["heart rate"], ">=", 110, (60, 100), (110, 140), 5),
          N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<", 100, (112, 160), (75, 99), 8),
          N("spo2", "spo2", "oxygen saturation", SPO2_KW, "<", 90, (94, 100), (78, 89), 3),
          N("age", "age", "age", ["age"], ">", 80, (50, 74), (81, 94), 4, **AGE)],
         "Acute pulmonary embolism confirmed on CT pulmonary angiography.",
         family="additive_score"),
]


# ---- batch S2 ----
# Batch S2: additive scores from cardiovascular, thrombosis and bleeding risk
# (partial versions, single-threshold items, points as published).
#
# New concepts (banks in S2_banks.json): hypertension, hemoptysis (keywords
# "coughing up blood" etc., because "hemoptysis" already occurs in the bleeding
# bank), bmi, and hemoglobin (same name, keyword "hgb" and bank as batch C1).
HTN_KW = ["hypertens"]
HEMOPTYSIS_KW = ["coughing up blood", "coughs up blood", "coughed up blood"]
BMI_KW = ["body mass index", "bmi"]
HGB_KW = ["hgb"]
STROKE_KW = ["stroke", "transient ischemic", "tia"]


def htn():
    return F("htn", "hypertension", "hypertension", HTN_KW, counts_past=True)


def hemoptysis(points):
    return F("hemoptysis", "hemoptysis", "hemoptysis", HEMOPTYSIS_KW, points=points)


_S2 = [
    # Gage 2001 (JAMA): all five items.
    Rule("s2_chads2", "score", "CHADS2",
         "CHADS2 (as used here): 2 points for a stroke or TIA at any time; 1 point each for "
         "heart failure at any time, hypertension at any time, diabetes at any time, and a "
         "current age of {thr_age} years or more.",
         [F("stroke", "stroke", "stroke/TIA", STROKE_KW, counts_past=True, points=2),
          F("chf", "chf", "heart failure", ["heart failure"], counts_past=True),
          htn(),
          F("diabetes", "diabetes", "diabetes", ["diabet"], counts_past=True),
          N("age", "age", "age", ["age"], ">=", 75, (50, 70), (76, 90), 4, **AGE)],
         "Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.",
         family="additive_score"),
    # Wells 2000 (Thromb Haemost): HR >100 1.5, hemoptysis 1, malignancy 1. Previous DVT/PE
    # (1.5) left out: a criterion cannot count past mentions only, and "current or previous"
    # lets the flip show the PE under assessment.
    Rule("s2_wells_pe", "score", "Wells PE (partial)",
         "Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current "
         "heart rate above {thr_hr}/min; 1 point each for current hemoptysis (coughing up blood) "
         "and active cancer. Other Wells items are not part of this question.",
         [N("hr", "heart_rate", "heart rate", ["heart rate"], ">", 100, (62, 92), (106, 140), 5,
            points=1.5),
          hemoptysis(1),
          F("cancer", "cancer", "active cancer", CANCER_KW)],
         "Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.",
         age_range=(30, 79), family="additive_score"),
    # Le Gal 2006 (Ann Intern Med): active malignancy 2, hemoptysis 2, age >65 1. Previous
    # DVT/PE (3) left out as in s2_wells_pe (it would also copy padua's VTE item).
    Rule("s2_geneva", "score", "Revised Geneva (partial)",
         "Revised Geneva score (as used here, partial): 2 points each for active cancer and "
         "current hemoptysis (coughing up blood); 1 point for a current age above {thr_age} "
         "years. Other Geneva items are not part of this question.",
         [F("cancer", "cancer", "active cancer", CANCER_KW, points=2),
          hemoptysis(2),
          N("age", "age", "age", ["age"], ">", 65, (45, 58), (67, 88), 4, **AGE)],
         "Pleuritic chest pain and breathlessness for two days; seen in the emergency department.",
         family="additive_score"),
    # Caprini 2005 (Dis Mon): history of DVT/PE 3 and family history of thrombosis 3 (one
    # criterion here), malignancy present or previous 2, BMI >25 1.
    Rule("s2_caprini", "score", "Caprini (partial)",
         "Caprini score (as used here, partial): 3 points for a venous thromboembolism of the "
         "patient or a first-degree relative (parent, sibling or child) at any time; 2 points "
         "for cancer at any time (active or previous); 1 point for a current body mass index "
         "above {thr_bmi} kg/m2. Other Caprini items, including age, are not part of this "
         "question.",
         [F("vte", "vte", "venous thromboembolism", VTE_KW, counts_past=True, counts_family=True,
            points=3),
          F("cancer", "cancer", "cancer", CANCER_KW, counts_past=True, points=2),
          N("bmi", "bmi", "body mass index", BMI_KW, ">", 25.0, (19.5, 24.0), (26.0, 34.0), 0.8,
            decimals=1)],
         "Admitted for an emergency bowel resection.",
         age_range=(40, 79), family="additive_score"),
    # Khorana 2008 (Blood): platelets >=350, Hb <10, WBC >11, BMI >=35 (cancer site omitted).
    # Platelets: numeric near-misses only (the platelet past/superseded templates describe low counts).
    Rule("s2_khorana", "score", "Khorana (partial)",
         "Khorana score (as used here, partial): 1 point each for a current platelet count of "
         "{thr_plt} x10^9/L or more; a current hemoglobin below {thr_hgb} g/dL; a current white "
         "cell count above {thr_wbc} x10^9/L; a current body mass index of {thr_bmi} kg/m2 or "
         "more. Other Khorana items, including the cancer site, are not part of this question.",
         [N("plt", "platelets", "platelet count", ["platelet"], ">=", 350, (160, 300), (350, 520),
            25, alt_threshold=300, nm=("numeric",)),
          N("hgb", "hemoglobin", "hemoglobin", HGB_KW, "<", 10.0, (11.5, 15.5), (7.0, 9.6), 0.6,
            decimals=1, alt_threshold=11.0),
          N("wbc", "wbc", "white cell count", ["white cell", "wbc"], ">", 11.0, (4.5, 9.8),
            (11.6, 18.0), 0.6, decimals=1),
          N("bmi", "bmi", "body mass index", BMI_KW, ">=", 35.0, (22.0, 32.0), (35.0, 44.0), 1.0,
            decimals=1)],
         "Newly diagnosed colon cancer; first chemotherapy cycle planned for next week.",
         age_range=(35, 79), family="additive_score"),
    # Gage 2006 (Am Heart J): malignancy 1, older (>75) 1, reduced platelet function incl.
    # aspirin 1, rebleeding risk (prior bleed) 2.
    Rule("s2_hemorr2hages", "score", "HEMORR2HAGES (partial)",
         "HEMORR2HAGES score (as used here, partial): 2 points for a major bleeding event at any "
         "time; 1 point each for active cancer, a current age above {thr_age} years, and current "
         "use of aspirin. Other HEMORR2HAGES items are not part of this question.",
         [F("bleed", "bleeding", "bleeding history", ["bleed"], counts_past=True, points=2),
          F("cancer", "cancer", "active cancer", CANCER_KW),
          N("age", "age", "age", ["age"], ">", 75, (55, 70), (76, 92), 4, **AGE),
          F("aspirin", "aspirin", "aspirin use", ["aspirin"])],
         "Atrial fibrillation; warfarin therapy under consideration.",
         family="additive_score"),
    # O'Brien 2015 (Eur Heart J): bleeding history 2, age >=75 1, eGFR <60 1, antiplatelet 1.
    Rule("s2_orbit", "score", "ORBIT (partial)",
         "ORBIT bleeding score (as used here, partial): 2 points for a major bleeding event at "
         "any time; 1 point each for a current age of {thr_age} years or more, a current eGFR "
         "below {thr_egfr} mL/min/1.73 m2, and current use of aspirin. Other ORBIT items are not "
         "part of this question.",
         [F("bleed", "bleeding", "bleeding history", ["bleed"], counts_past=True, points=2),
          N("age", "age", "age", ["age"], ">=", 75, (55, 70), (76, 90), 4, **AGE),
          N("egfr", "egfr", "eGFR", ["egfr"], "<", 60, (66, 110), (18, 55), 6, alt_threshold=75),
          F("aspirin", "aspirin", "aspirin use", ["aspirin"])],
         "Atrial fibrillation; starting apixaban is being considered.",
         family="additive_score"),
    # Fang 2011 (JACC): anemia (Hb <13 g/dL in men) 3, eGFR <30 3, age >=75 2, hypertension 1.
    # Men only, so the single Hb threshold is the published one; prior hemorrhage left out
    # because the bleeding bank's generic line "Hemoglobin normal..." would contradict a low Hb.
    Rule("s2_atria_bleed", "score", "ATRIA bleeding, men (partial)",
         "ATRIA bleeding score for men (as used here, partial): 3 points each for a current "
         "hemoglobin below {thr_hgb} g/dL and a current eGFR below {thr_egfr} mL/min/1.73 m2; "
         "2 points for a current age of {thr_age} years or more; 1 point for hypertension at any "
         "time. Other ATRIA items are not part of this question.",
         [N("hgb", "hemoglobin", "hemoglobin", HGB_KW, "<", 13.0, (14.0, 17.0), (9.0, 12.6), 0.6,
            decimals=1, points=3),
          N("egfr", "egfr", "eGFR", ["egfr"], "<", 30, (45, 95), (12, 29), 6, points=3,
            alt_threshold=45),
          N("age", "age", "age", ["age"], ">=", 75, (55, 70), (76, 90), 4, points=2, **AGE),
          htn()],
         "Atrial fibrillation; a decision on warfarin is pending.",
         sex="male", family="additive_score"),
    # Morrow 2000 (Circulation): SBP <100 3, HR >100 2, weight <67 kg 1, history of
    # diabetes, hypertension or angina 1 (hypertension kept). SBP default 110-125 renders at
    # most 125/79 (diastolic = 0.6*SBP+4), below 130/80, so no reading next to the
    # hypertension item looks hypertensive.
    Rule("s2_timi_stemi", "score", "TIMI STEMI (partial)",
         "TIMI risk score for ST-elevation myocardial infarction (as used here, partial): 3 "
         "points for a current systolic blood pressure below {thr_sbp} mmHg; 2 points for a "
         "current heart rate above {thr_hr}/min; 1 point each for a current weight below "
         "{thr_wt} kg and hypertension at any time. Other TIMI items, including age, are not "
         "part of this question.",
         [N("sbp", "sbp", "systolic blood pressure", SBP_KW, "<", 100, (110, 125), (70, 98), 6,
            points=3),
          N("hr", "heart_rate", "heart rate", ["heart rate"], ">", 100, (62, 92), (106, 140), 5,
            points=2),
          N("wt", "weight", "weight", ["weight", "weighs"], "<", 67, (72, 98), (45, 66), 4),
          htn()],
         "Admitted with an acute ST-elevation myocardial infarction.",
         age_range=(40, 84), family="additive_score"),
]

RULES += _S1 + _S2
