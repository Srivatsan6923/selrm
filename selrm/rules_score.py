"""Additive scoring rules (MedCalc-Bench style, partial definitions)."""
from selrm.rules import AGE, CANCER_KW, CONF_KW, SBP_KW, VTE_KW, F, N, Rule

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
