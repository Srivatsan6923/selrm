"""Constraint rules beyond the pilot (seen structural families)."""
from selrm.rules import AGE, F, G, N, Rule

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


# ---- batch C1 ----
# Batch C1: lab_threshold constraint rules (renal, hepatic and haematologic switches).
#
# Each rule is a stated test specification; one current lab value decides it.
# New concepts (banks in C1_banks.json): hemoglobin (keyword "hgb", because
# "hemoglobin" already occurs in the bleeding bank) and neutrophils.
# Superseded lines are faulty measurements of the patient's own sample, never a
# real low value or another person's sample.
#
# Merge: add this as its own module to LIBRARY in library.py only, outside
# rules_grammar._hand_written(). Inside it, its numeric configs join
# _numeric_configs() and re-draw the grammar-sampled rules under the same gs ids.
# Merging the banks into phrases.BANKS leaves the sampled rules unchanged.
_C1 = [
    # ---- renal ------------------------------------------------------------
    Rule("c1_nitrofurantoin", "constraint", "Acute cystitis",
         "For acute cystitis, prescribe nitrofurantoin. If the current eGFR is below "
         "{thr_egfr} mL/min/1.73 m2, prescribe fosfomycin instead.",
         [N("egfr", "egfr", "eGFR", ["egfr"], "<", 45, (52, 105), (15, 44), 6,
            alt_threshold=60)],
         "Burning on passing urine and urinary frequency for three days; no fever or flank pain.",
         default="nitrofurantoin", alternative="fosfomycin", sex="female", age_range=(30, 79),
         family="lab_threshold"),
    Rule("c1_allopurinol", "constraint", "Allopurinol starting dose",
         "For urate-lowering therapy in gout, prescribe allopurinol 100 mg daily. If the current "
         "eGFR is below {thr_egfr} mL/min/1.73 m2, prescribe allopurinol 50 mg daily instead.",
         [N("egfr", "egfr", "eGFR", ["egfr"], "<", 30, (45, 100), (15, 29), 6,
            alt_threshold=60)],
         "Three gout flares in the past year; serum urate 9.2 mg/dL.",
         default="allopurinol 100 mg daily", alternative="allopurinol 50 mg daily",
         age_range=(40, 84), family="lab_threshold"),
    Rule("c1_valacyclovir", "constraint", "Herpes zoster",
         "For herpes zoster, prescribe valacyclovir 1 g three times daily. If the current eGFR is "
         "below {thr_egfr} mL/min/1.73 m2, prescribe valacyclovir 1 g twice daily instead.",
         [N("egfr", "egfr", "eGFR", ["egfr"], "<", 50, (56, 95), (30, 49), 6)],
         "Painful blistering rash in a band on the left side of the chest for two days, typical "
         "of herpes zoster.",
         default="valacyclovir 1 g three times daily", alternative="valacyclovir 1 g twice daily",
         age_range=(50, 89), family="lab_threshold"),
    Rule("c1_enoxaparin", "constraint", "Enoxaparin treatment dose",
         "For treatment of acute deep vein thrombosis, prescribe enoxaparin 1 mg/kg twice daily. "
         "If the current eGFR is below {thr_egfr} mL/min/1.73 m2, prescribe enoxaparin 1 mg/kg "
         "once daily instead.",
         # ponytail: eGFR, not serum creatinine: a creatinine cut-off maps to CrCl < 30 (the
         # label's criterion) in older or lighter patients at near-miss values, so the rule
         # would contradict the label there; eGFR < 30 is the accepted surrogate.
         [N("egfr", "egfr", "eGFR", ["egfr"], "<", 30, (40, 95), (15, 29), 6)],
         "Admitted with an acute deep vein thrombosis of the left leg, confirmed on ultrasound.",
         default="enoxaparin 1 mg/kg twice daily", alternative="enoxaparin 1 mg/kg once daily",
         age_range=(35, 84), family="lab_threshold"),
    Rule("c1_spironolactone", "constraint", "Resistant hypertension",
         "For hypertension uncontrolled on amlodipine, ramipril and indapamide, prescribe "
         "spironolactone. If the current serum potassium is above {thr_k} mmol/L, prescribe "
         "doxazosin instead.",
         [N("k", "potassium", "serum potassium", ["potassium"], ">", 4.5, (3.5, 4.2), (4.7, 5.4),
            0.3, decimals=1)],
         "Clinic blood pressure 158/96 mmHg on three visits despite full doses of amlodipine, "
         "ramipril and indapamide.",
         default="spironolactone", alternative="doxazosin", age_range=(40, 79),
         family="lab_threshold"),
    # ---- hepatic ----------------------------------------------------------
    Rule("c1_methotrexate", "constraint", "Rheumatoid arthritis initiation",
         "For newly diagnosed rheumatoid arthritis, prescribe methotrexate. If the current ALT is "
         "above {thr_alt} U/L, prescribe hydroxychloroquine instead.",
         [N("alt", "alt_enzyme", "ALT", ["alt "], ">", 80, (10, 32), (95, 300), 10,
            alt_threshold=40)],
         "Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for "
         "three months.",
         default="methotrexate", alternative="hydroxychloroquine", age_range=(25, 70),
         family="lab_threshold"),
    Rule("c1_methimazole", "constraint", "Graves' hyperthyroidism",
         "For Graves' hyperthyroidism, prescribe methimazole. If the current ALT is above "
         "{thr_alt} U/L, prescribe radioactive iodine instead.",
         [N("alt", "alt_enzyme", "ALT", ["alt "], ">", 200, (14, 90), (215, 480), 15,
            alt_threshold=120)],
         "Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor "
         "antibodies.",
         default="methimazole", alternative="radioactive iodine", age_range=(25, 65),
         family="lab_threshold"),
    # ---- haematologic -----------------------------------------------------
    Rule("c1_cat_platelets", "constraint", "Cancer-associated thrombosis",
         "For cancer-associated venous thromboembolism, prescribe apixaban. If the current "
         "platelet count is below {thr_plt} x10^9/L, prescribe enoxaparin instead.",
         [N("plt", "platelets", "platelet count", ["platelet"], "<", 50, (150, 380), (26, 49), 8,
            alt_threshold=75)],
         "Admitted with a pulmonary embolism; receiving chemotherapy for metastatic colon cancer.",
         default="apixaban", alternative="enoxaparin", age_range=(40, 84),
         family="lab_threshold"),
    Rule("c1_transfusion", "constraint", "Postoperative anemia",
         "For anemia after hip fracture surgery, prescribe oral iron. If the current hemoglobin "
         "is below {thr_hgb} g/dL, prescribe a red cell transfusion instead.",
         [N("hgb", "hemoglobin", "hemoglobin", ["hgb"], "<", 8.0, (9.0, 11.8), (6.0, 7.9), 0.6,
            decimals=1, alt_threshold=10.0)],
         "Second day after surgical repair of a hip fracture; hemodynamically stable.",
         default="oral iron", alternative="a red cell transfusion", age_range=(65, 92),
         family="lab_threshold"),
    Rule("c1_neutropenia", "constraint", "Chest infection during chemotherapy",
         "For a chest infection during chemotherapy, prescribe oral co-amoxiclav. If the current "
         "neutrophil count is {thr_anc} x10^9/L or less, prescribe intravenous "
         "piperacillin-tazobactam instead.",
         [N("anc", "neutrophils", "neutrophil count", ["neutrophil"], "<=", 0.5, (1.8, 6.5),
            (0.1, 0.5), 0.3, decimals=1, alt_threshold=1.0)],
         # past the count's low point, so near-miss counts read as recovering (not "expected
         # to fall below 0.5"); "most recent", not "last", so chemotherapy is still ongoing
         "Productive cough and fever, three weeks after the most recent cycle of chemotherapy "
         "for lymphoma.",
         default="oral co-amoxiclav", alternative="intravenous piperacillin-tazobactam",
         age_range=(25, 79), family="lab_threshold"),
]


# ---- batch C2 ----
# Batch C2: single-condition constraint rules, families allergy_switch,
# drug_interaction, state_switch and history_switch. New concepts (banks in C2_banks.json):
# contrast_allergy, methotrexate, lithium.
_C2 = [
    # ---- allergy_switch ----------------------------------------------------
    # IDSA 2012 acute bacterial rhinosinusitis: amoxicillin-clavulanate first line;
    # doxycycline for penicillin-allergic adults.
    Rule("c2_sinus_pen", "constraint", "Acute bacterial sinusitis",
         "For acute bacterial sinusitis, prescribe amoxicillin-clavulanate. If the patient "
         "currently has a penicillin allergy, prescribe doxycycline instead.",
         [F("pen", "pen_allergy", "penicillin allergy", ["penicillin"])],
         "Facial pain and purulent nasal discharge for 12 days; acute bacterial sinusitis "
         "diagnosed.",
         default="amoxicillin-clavulanate", alternative="doxycycline", age_range=(18, 70),
         family="allergy_switch"),
    # NIH/CDC/IDSA adult opportunistic infection guidelines: TMP-SMX preferred for
    # Pneumocystis prophylaxis; atovaquone is a listed alternative when it cannot be used.
    Rule("c2_pcp_sulfa", "constraint", "Pneumocystis prophylaxis",
         "For Pneumocystis pneumonia prophylaxis, prescribe trimethoprim-sulfamethoxazole. If "
         "the patient currently has an allergy to sulfonamide antibiotics, prescribe atovaquone "
         "instead.",
         [F("sulfa", "sulfa_allergy", "sulfonamide allergy", ["sulfonamide", "sulfa"])],
         "HIV infection with a CD4 count of 140 cells/uL; antiretroviral therapy being started.",
         default="trimethoprim-sulfamethoxazole", alternative="atovaquone", age_range=(25, 64),
         family="allergy_switch"),
    # ESC 2019 acute PE guideline: V/Q scanning preferred over CTPA in patients with
    # contrast-medium anaphylaxis or a strong history of contrast allergy.
    Rule("c2_ctpa_contrast", "constraint", "Imaging for suspected pulmonary embolism",
         "For suspected pulmonary embolism, order a CT pulmonary angiogram. If the patient "
         "currently has an allergy to iodinated contrast, order a ventilation-perfusion scan "
         "instead.",
         [F("contrast", "contrast_allergy", "iodinated contrast allergy", ["iodinated contrast"])],
         "Sudden pleuritic chest pain and breathlessness; pulmonary embolism suspected, D-dimer "
         "raised, chest radiograph clear.",
         default="a CT pulmonary angiogram", alternative="a ventilation-perfusion scan",
         age_range=(25, 70), family="allergy_switch", verb="Order"),
    # ---- drug_interaction --------------------------------------------------
    # Simvastatin label: contraindicated with strong CYP3A4 inhibitors (clarithromycin named;
    # suspend during the course); pravastatin is not CYP3A4-metabolized.
    Rule("c2_statin_clarith", "constraint", "Statin initiation",
         "For primary prevention of cardiovascular disease, prescribe simvastatin. If the "
         "patient is currently taking clarithromycin, prescribe pravastatin instead.",
         [F("clarith", "clarithromycin", "clarithromycin use", ["clarithromycin"])],
         "Primary prevention; LDL cholesterol 172 mg/dL, 10-year cardiovascular risk 11%.",
         default="simvastatin", alternative="pravastatin", age_range=(40, 75),
         family="drug_interaction"),
    # Warfarin label and CHEST guidance: NSAIDs add bleeding risk; acetaminophen preferred.
    Rule("c2_sprain_warfarin", "constraint", "Ankle sprain analgesia",
         "For an acute ankle sprain, prescribe naproxen. If the patient is currently taking "
         "warfarin, prescribe acetaminophen instead.",
         [F("warfarin", "warfarin", "warfarin use", ["warfarin"])],
         "Right ankle sprain after a fall on uneven ground; radiograph normal.",
         default="naproxen", alternative="acetaminophen", age_range=(40, 79),
         family="drug_interaction"),
    # Methotrexate label: TMP-SMX increases marrow suppression; IDSA 2014 SSTI guideline
    # lists TMP-SMX or doxycycline for a purulent skin infection.
    Rule("c2_abscess_mtx", "constraint", "Drained skin abscess",
         "For a drained skin abscess with surrounding cellulitis, prescribe "
         "trimethoprim-sulfamethoxazole. If the patient is currently taking methotrexate, "
         "prescribe doxycycline instead.",
         [F("mtx", "methotrexate", "methotrexate use", ["methotrexate"])],
         "Abscess of the left thigh, incised and drained; spreading redness around it.",
         default="trimethoprim-sulfamethoxazole", alternative="doxycycline", age_range=(30, 70),
         family="drug_interaction"),
    # Lithium label: thiazides cut lithium clearance (toxicity); a dihydropyridine calcium
    # channel blocker has no such interaction.
    Rule("c2_htn_lithium", "constraint", "Hypertension initiation",
         "For newly diagnosed hypertension, prescribe hydrochlorothiazide. If the patient is "
         "currently taking lithium, prescribe amlodipine instead.",
         [F("lithium", "lithium", "lithium use", ["lithium"])],
         "Newly diagnosed hypertension (blood pressure 156/96 mmHg on repeated readings).",
         default="hydrochlorothiazide", alternative="amlodipine", age_range=(30, 70),
         family="drug_interaction"),
    # ---- state_switch ------------------------------------------------------
    # ASH 2018 VTE in pregnancy: LMWH; DOACs avoided in pregnancy (apixaban label).
    Rule("c2_dvt_pregnancy", "constraint", "Deep vein thrombosis treatment",
         "For a deep vein thrombosis of the leg, prescribe apixaban. If the patient is currently "
         "pregnant, prescribe enoxaparin instead.",
         [F("pregnancy", "pregnancy", "pregnancy", ["pregnan"])],
         "Painful, swollen left calf; deep vein thrombosis confirmed on ultrasound.",
         default="apixaban", alternative="enoxaparin", sex="female", age_range=(20, 40),
         family="state_switch"),
    # AAN/AHS 2012 migraine prevention: propranolol Level A, amitriptyline Level B (also a
    # NICE CG150 option; no asthma or pregnancy-programme issue, unlike topiramate). The
    # propranolol SmPC also excludes a history of asthma, so past asthma is never rendered:
    # near-misses are subject and negation only.
    Rule("c2_migraine_asthma", "constraint", "Migraine prevention",
         "For migraine prevention, prescribe propranolol. If the patient currently has asthma, "
         "prescribe amitriptyline instead.",
         [F("asthma", "asthma", "asthma", ["asthma"], nm=("subject", "negation"))],
         "Migraine without aura, with six disabling attacks a month.",
         default="propranolol", alternative="amitriptyline", age_range=(18, 55),
         family="state_switch"),
    # ---- history_switch ----------------------------------------------------
    # Pioglitazone SmPC 4.3: contraindicated in cardiac failure or a history of cardiac failure
    # (NYHA I-IV); ADA Standards of Care: SGLT2 inhibitor in type 2 diabetes with heart failure.
    Rule("c2_t2d_hf", "constraint", "Type 2 diabetes intensification",
         "For type 2 diabetes above target on metformin, prescribe pioglitazone. If the patient "
         "has ever had heart failure (current or past), prescribe empagliflozin instead.",
         [F("hf", "chf", "heart failure", ["heart failure"], counts_past=True)],
         "Type 2 diabetes above target despite metformin (HbA1c 8.4%).",
         default="pioglitazone", alternative="empagliflozin", age_range=(45, 79),
         family="history_switch"),
]


# ---- batch C3 ----
# Batch C3: constraint rules in families history_switch, family_switch, age_limit,
# any_of and all_of. No new concepts.
#
# Banks: C3_banks.json adds one form to an existing concept, asthma.rel_past (another
# person's past asthma), which c3_glaucoma_asthma needs because it counts past asthma.
# It is merged per form: the other asthma forms (phrase_kit2/banks/G3.json) stay as they
# are. With that form the grammar sampler can also draw "asthma at any time", which
# changes SAMPLED (246 of the 250 sampled rules when measured on 2 Oct).
_C3 = [
    # ---- history_switch ---------------------------------------------------
    # Prasugrel label (boxed warning): contraindicated with a prior TIA or stroke;
    # clopidogrel is the usual P2Y12 alternative. Ages kept below 75 (prasugrel label).
    Rule("c3_prasugrel_stroke", "constraint", "Antiplatelet choice after a stent",
         "For dual antiplatelet therapy after a coronary stent for an acute coronary syndrome, "
         "prescribe aspirin plus prasugrel. If the patient has ever had a stroke or TIA (current "
         "or past), prescribe aspirin plus clopidogrel instead.",
         [F("stroke", "stroke", "stroke or TIA at any time", ["stroke", "transient ischemic", "tia"],
            counts_past=True)],
         "Admitted with an acute coronary syndrome; a coronary stent was placed during this stay.",
         default="aspirin plus prasugrel", alternative="aspirin plus clopidogrel",
         age_range=(40, 74), family="history_switch"),
    # Multaq (dronedarone) EU SmPC section 4.3: contraindicated with a history of, or current,
    # heart failure or left ventricular systolic dysfunction (EMA 2011 restriction), which is
    # exactly "ever had heart failure (current or past)"; amiodarone has no such restriction.
    Rule("c3_dronedarone_hf", "constraint", "Rhythm control in atrial fibrillation",
         "For rhythm control of paroxysmal atrial fibrillation, prescribe dronedarone. If the "
         "patient has ever had heart failure (current or past), prescribe amiodarone instead.",
         [F("hf", "chf", "heart failure at any time", ["heart failure"], counts_past=True)],
         "Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control "
         "chosen.",
         default="dronedarone", alternative="amiodarone", age_range=(45, 79),
         family="history_switch"),
    # Timolol ophthalmic label: contraindicated in bronchial asthma or a history of bronchial
    # asthma; latanoprost has no such restriction. Timolol is the stated formulary default.
    # Past asthma counts, so subject near-misses use asthma.rel_past (C3_banks.json).
    Rule("c3_glaucoma_asthma", "constraint", "Open-angle glaucoma",
         "For primary open-angle glaucoma, prescribe timolol eye drops. If the patient has ever "
         "had asthma (current or past), prescribe latanoprost eye drops instead.",
         [F("asthma", "asthma", "asthma at any time", ["asthma"], counts_past=True)],
         "Newly diagnosed primary open-angle glaucoma (intraocular pressure 27 mmHg in both "
         "eyes).",
         default="timolol eye drops", alternative="latanoprost eye drops", age_range=(45, 80),
         family="history_switch"),
    # ---- family_switch ----------------------------------------------------
    # Tranexamic acid label: contraindicated with a history or intrinsic risk of thrombosis
    # (family history read as possible inherited risk); NICE NG88: the levonorgestrel
    # intrauterine system is first-line for heavy menstrual bleeding and has no such restriction.
    Rule("c3_hmb_vte", "constraint", "Heavy menstrual bleeding",
         "For heavy menstrual bleeding, prescribe tranexamic acid. If the patient or a first-degree "
         "relative (parent, sibling or child) has had a venous thromboembolism at any time, "
         "prescribe a levonorgestrel intrauterine system instead.",
         [F("vte", "vte", "venous thromboembolism at any time in the patient or a first-degree "
            "relative", ["thrombo", "dvt", "pulmonary embol"], counts_past=True, counts_family=True)],
         "Heavy menstrual bleeding for six months; pelvic ultrasound normal.",
         default="tranexamic acid", alternative="a levonorgestrel intrauterine system",
         sex="female", age_range=(25, 48), family="family_switch"),
    # 2018 AHA/ACC cholesterol guideline and NLA 2019: lipoprotein(a) is measured with a personal
    # or family history of (premature) ASCVD; ESC/EAS 2019 measure it at least once anyway.
    Rule("c3_lipid_lpa", "constraint", "Cholesterol testing",
         "For cholesterol testing at a routine health check, order a standard lipid panel. If the "
         "patient or a first-degree relative (parent, sibling or child) has had coronary artery "
         "disease at any time, order a lipid panel with lipoprotein(a) instead.",
         [F("cad", "cad", "coronary artery disease at any time in the patient or a first-degree "
            "relative", ["coronary"], counts_past=True, counts_family=True)],
         "Routine health check; cholesterol testing is due.",
         default="a standard lipid panel", alternative="a lipid panel with lipoprotein(a)",
         age_range=(30, 64), family="family_switch", verb="Order"),
    # ---- age_limit ----------------------------------------------------------
    # USPSTF 2018 cervical cancer screening: cytology alone at 21-29; from 30, primary hrHPV
    # testing every 5 years (or cytology or co-testing).
    Rule("c3_cervical_hpv", "constraint", "Cervical screening test",
         "For cervical cancer screening, order cervical cytology. If the patient's current age is "
         "{thr_age} years or more, order primary HPV testing instead.",
         [N("age", "age", "age", ["age"], ">=", 30, (21, 26), (30, 64), 3, **AGE)],
         "Routine cervical screening visit; no symptoms.",
         default="cervical cytology", alternative="primary HPV testing", sex="female",
         family="age_limit", verb="Order"),
    # NICE CG173: amitriptyline, duloxetine, gabapentin or pregabalin as initial treatment;
    # AGS Beers 2023: avoid tertiary tricyclics such as amitriptyline from age 65.
    Rule("c3_neuropathy_age", "constraint", "Painful diabetic neuropathy",
         "For painful diabetic peripheral neuropathy, prescribe amitriptyline. If the patient's "
         "current age is {thr_age} years or more, prescribe duloxetine instead.",
         [N("age", "age", "age", ["age"], ">=", 65, (40, 60), (66, 88), 5, **AGE)],
         "Burning pain in both feet from diabetic peripheral neuropathy.",
         default="amitriptyline", alternative="duloxetine", family="age_limit"),
    # ---- any_of / all_of ----------------------------------------------------
    # NICE NG136 step 1: ACE inhibitor (or ARB) for adults under 55 or with type 2 diabetes;
    # calcium channel blocker for adults aged 55 or over without diabetes (family origin not used
    # here). Diabetes counts at any time (current or past): the 2021 ADA/EASD/Diabetes UK
    # consensus treats remission as a state of type 2 diabetes, not a cure.
    G("c3_nice_step1", "any_of", "Hypertension initiation", "For newly diagnosed hypertension",
      "amlodipine", "ramipril",
      [(N("age", "age", "age", ["age"], "<", 55, (58, 80), (30, 52), 3, **AGE),
        "the patient's current age is below {thr_age} years"),
       (F("diabetes", "diabetes", "diabetes at any time", ["diabet"], counts_past=True),
        "the patient has ever had diabetes (current or past)")],
      "Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home "
      "readings)."),
    # Adapted from the edoxaban SmPC (AF): eGFR stands in for Cockcroft-Gault CrCl; the P-gp
    # inhibitor criterion is omitted. SmPC: 30 mg once daily if creatinine clearance is
    # 15-50 mL/min or body weight is 60 kg or less; eGFR values here stay within 20-90.
    G("c3_edoxaban_dose", "any_of", "Edoxaban dosing",
      "For stroke prevention in atrial fibrillation", "edoxaban 60 mg daily",
      "edoxaban 30 mg daily",
      [(N("egfr", "egfr", "eGFR", ["egfr"], "<=", 50, (55, 90), (20, 50), 4),
        "the current eGFR is {thr_egfr} mL/min/1.73 m2 or less"),
       (N("wt", "weight", "weight", ["weight", "weighs"], "<=", 60, (66, 98), (42, 60), 4),
        "the current weight is {thr_wt} kg or less")],
      "Atrial fibrillation without valve disease; starting an oral anticoagulant.",
      age_range=(55, 89)),
    # IDSA 2014 skin and soft tissue infections: oral agents for mild cellulitis, intravenous
    # cefazolin (or similar) with systemic signs (SIRS: two or more of fever, leukocytosis, ...).
    G("c3_cellulitis_sirs", "all_of", "Cellulitis treatment", "For cellulitis of the lower leg",
      "oral cephalexin", "intravenous cefazolin",
      [(N("temp", "temperature", "temperature", ["temperature"], ">", 38.0, (36.2, 37.5),
          (38.4, 40.2), 0.4, decimals=1), "the current temperature is above {thr_temp} C"),
       (N("wbc", "wbc", "white cell count", ["white cell", "wbc"], ">", 12.0, (4.5, 10.8),
          (12.6, 22.0), 0.8, decimals=1),
        "the current white cell count is above {thr_wbc} x10^9/L")],
      "Spreading redness, warmth and swelling of the left lower leg for two days.",
      age_range=(25, 79)),
]

RULES += _C1 + _C2 + _C3
