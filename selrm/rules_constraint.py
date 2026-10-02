"""Constraint rules beyond the pilot (seen structural families)."""
from selrm.rules import F, N, Rule

RULES = [
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
         "Primary care visit; asks about screening tests.",
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
]
