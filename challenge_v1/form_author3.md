# challenge_v1 writing form: author3

Read `challenge_v1/WRITING_GUIDE.md` first. Fill in every field after the colon. Save this file as `challenge_v1/notes_author3.md`.
40 groups; your second author fills `check_ok` (yes and the fingerprint from `challenge_v1/ASSEMBLY_REPORT.md`, or no) and `check_comment`.

## c012   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For rate control in atrial fibrillation, prescribe metoprolol. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient currently has tonsillar exudate, prescribe diltiazem instead.

Patient: 58-year-old male. Reason for the visit: Atrial fibrillation with a ventricular rate of 128/min.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has tonsillar exudate now
  Do not mention colorectal cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient's sister had colorectal cancer in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's friend had colorectal cancer in the past (years ago).
Every line that mentions colorectal cancer must contain one of these words (a longer word that starts with one is fine): 'colorectal cancer' | 'colon cancer' | 'bowel cancer'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c014   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For knee osteoarthritis pain, prescribe naproxen. If the patient is allergic to penicillin and the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time, prescribe acetaminophen instead.

Patient: 67-year-old male. Reason for the visit: Knee osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a penicillin allergy now
  Do not mention coronary artery disease in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had coronary artery disease in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have coronary artery disease (a clear denial).
Every line that mentions coronary artery disease must contain one of these words (a longer word that starts with one is fine): 'coronary'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c022   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. Score 1 point if the patient is currently taking aspirin; 2 points if the patient has ever had heart failure (current or past); 1 point if the patient has had a major bleeding event at any time; 3 points if the current respiratory rate is 25/min or more. If the score is 4 or more, prescribe intravenous co-amoxiclav instead.

Patient: 62-year-old male. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: respiratory rate: 30/min, the current value
  Do not mention daily aspirin use in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has daily aspirin use now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient had daily aspirin use in the past (years ago); it is over or resolved, not current.
Every line that mentions daily aspirin use must contain one of these words (a longer word that starts with one is fine): 'aspirin'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c024   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the patient is allergic to penicillin; 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe acetaminophen instead.

Patient: 53-year-old male. Reason for the visit: Knee osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 65/min, the current value
  fact 2: the patient's father has a venous thromboembolism (DVT or pulmonary embolism) now
  fact 3: the patient has a penicillin allergy now
  FLIP (instruction): one line that replaces your line for fact 1, stating: heart rate: 104/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: heart rate: 90/min, the current value.
Every line that mentions heart rate must contain one of these words (a longer word that starts with one is fine): 'heart rate'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c031   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For inpatient VTE prophylaxis, prescribe enoxaparin. Score 1 point if the patient has ever had angioedema (current or past); 1 point if the patient has new confusion; 2 points if the current temperature is above 38.0 C; 2 points if the age of the patient is 65 years or more. If the score is 5 or more, prescribe intermittent pneumatic compression instead.

Patient: adult male. Reason for the visit: Admitted for community-acquired pneumonia; immobile.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: temperature: 36.6 C, the current value
  fact 2: the patient has new confusion now
  fact 3: an earlier temperature of 37.3 C, measured in 2009
  fact 4: age: 72 years, the current value
  FLIP (instruction): one line that replaces your line for fact 1, stating: temperature: 38.6 C, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: an earlier temperature of 38.2 C, measured in 2009.
Every line that mentions temperature must contain one of these words (a longer word that starts with one is fine): 'temperature'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
fact 4: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c034   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If the age of the patient is 75 years or more and the patient has ever had a venous thromboembolism (current or past), prescribe ezetimibe instead.

Patient: adult female. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago)
  fact 2: age: 60 years, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: age: 86 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: age: 73 years, the current value.
Every line that mentions age must contain one of these words (a longer word that starts with one is fine): 'age'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c040   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

Patient: 35-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: eGFR: 51 mL/min/1.73 m2, the current value
  fact 2: the patient had diabetes in the past (in 2016)
  fact 3: an earlier eGFR of 90 mL/min/1.73 m2, measured in 2013
  FLIP (instruction): one line that replaces your line for fact 1, stating: eGFR: 15 mL/min/1.73 m2, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: an earlier eGFR of 14 mL/min/1.73 m2, measured in 2013.
Every line that mentions eGFR must contain one of these words (a longer word that starts with one is fine): 'egfr'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c042   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.

Patient: 59-year-old male. Reason for the visit: Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 88/min, the current value
  fact 2: systolic blood pressure: 148 mmHg, the current value
  fact 3: blood urea nitrogen: 10 mg/dL, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has heart failure now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have heart failure (a clear denial).
Every line that mentions heart failure must contain one of these words (a longer word that starts with one is fine): 'heart failure'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c044   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.

Patient: 35-year-old male. Reason for the visit: Shortness of breath and fever; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 119 mmHg, the current value
  fact 2: respiratory rate: 15/min, the current value
  fact 3: oxygen saturation: 97%, the current value
  fact 4: an earlier oxygen saturation of 95%, measured in 2020
  FLIP (instruction): one line that replaces your line for fact 3, stating: oxygen saturation: 90%, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 4, stating: an earlier oxygen saturation of 86%, measured in 2020.
Every line that mentions oxygen saturation must contain one of these words (a longer word that starts with one is fine): 'saturation' | 'spo2'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
fact 4: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c050   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

Patient: 61-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had diabetes in the past (in 2013)
  fact 2: serum potassium: 4.6 mmol/L, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: serum potassium: 5.6 mmol/L, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: serum potassium: 5.0 mmol/L, the current value.
Every line that mentions serum potassium must contain one of these words (a longer word that starts with one is fine): 'potassium'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c053   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

Patient: adult male. Reason for the visit: Acute pulmonary embolism confirmed on CT pulmonary angiography.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 94/min, the current value
  fact 2: age: 64 years, the current value
  fact 3: systolic blood pressure: 130 mmHg, the current value
  fact 4: oxygen saturation: 96%, the current value
  Do not mention cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has cancer now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's uncle has cancer now.
Every line that mentions cancer must contain one of these words (a longer word that starts with one is fine): 'cancer' | 'lymphoma' | 'leukemia' | 'myeloma' | 'carcinoma'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
fact 4: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c056   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If the patient has ever had heart failure (current or past) and the age of the patient is 75 years or more, prescribe ezetimibe instead.

Patient: adult female. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 61 years, the current value
  fact 2: the patient has heart failure now
  FLIP (instruction): one line that replaces your line for fact 1, stating: age: 75 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: age: 74 years, the current value.
Every line that mentions age must contain one of these words (a longer word that starts with one is fine): 'age'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c060   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

Patient: 76-year-old female. Reason for the visit: Atrial fibrillation; anticoagulation indicated.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 12.7 x10^9/L, the current value
  fact 2: the patient has coronary artery disease now
  Do not mention colorectal cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has colorectal cancer now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's wife has colorectal cancer now.
Every line that mentions colorectal cancer must contain one of these words (a longer word that starts with one is fine): 'colorectal cancer' | 'colon cancer' | 'bowel cancer'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c062   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

Patient: 27-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: eGFR: 89 mL/min/1.73 m2, the current value
  fact 2: the patient's sister has diabetes now
  FLIP (instruction): one line that replaces your line for fact 1, stating: eGFR: 23 mL/min/1.73 m2, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: eGFR: 30 mL/min/1.73 m2, the current value.
Every line that mentions eGFR must contain one of these words (a longer word that starts with one is fine): 'egfr'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c071   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of 25 mg/dL or more; current altered mental status (confusion or disorientation); a current heart rate of 109/min or more. Age is scored separately and is not part of this question.

Patient: 70-year-old male. Reason for the visit: Acute exacerbation of COPD; assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: blood urea nitrogen: 19 mg/dL, the current value
  fact 2: heart rate: 83/min, the current value
  Do not mention new confusion in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has new confusion now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have new confusion (a clear denial).
Every line that mentions new confusion must contain one of these words (a longer word that starts with one is fine): 'confus' | 'disorient'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c084   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

Patient: 32-year-old male. Reason for the visit: Spreading redness and warmth of the right shin for two days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a venous thromboembolism (DVT or pulmonary embolism) now
  fact 2: ALT: 36 U/L, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: ALT: 156 U/L, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: ALT: 120 U/L, the current value.
Every line that mentions ALT must contain one of these words (a longer word that starts with one is fine): 'alt'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c088   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the current systolic blood pressure is above 160 mmHg; the age of the patient is 75 years or more; the patient has ever had asthma (current or past).

Patient: adult female. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 135 mmHg, the current value
  fact 2: an earlier systolic blood pressure of 129 mmHg, measured in 2016
  fact 3: age: 76 years, the current value
  FLIP (instruction): one line that replaces your line for fact 1, stating: systolic blood pressure: 170 mmHg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: an earlier systolic blood pressure of 167 mmHg, measured in 2016.
Every line that mentions systolic blood pressure must contain one of these words (a longer word that starts with one is fine): 'systolic' | 'blood pressure' | 'bp'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c089   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

Patient: adult male. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: calf swelling compared with the other leg: 1.0 cm, the current value
  fact 2: the patient's sister had colorectal cancer in the past (years ago)
  fact 3: age: 54 years, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: age: 74 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: age: 65 years, the current value.
Every line that mentions age must contain one of these words (a longer word that starts with one is fine): 'age'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c094   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

Patient: 59-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum potassium: 3.7 mmol/L, the current value
  fact 2: the patient's father has diabetes now
  FLIP (instruction): one line that replaces your line for fact 1, stating: serum potassium: 5.5 mmol/L, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: serum potassium: 5.0 mmol/L, the current value.
Every line that mentions serum potassium must contain one of these words (a longer word that starts with one is fine): 'potassium'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c103   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.

Patient: adult male. Reason for the visit: Pleuritic chest pain and breathlessness for two days; seen in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 58 years, the current value
  Do not mention cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has cancer now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient had cancer in the past (years ago); it is over or resolved, not current.
Every line that mentions cancer must contain one of these words (a longer word that starts with one is fine): 'cancer' | 'lymphoma' | 'leukemia' | 'myeloma' | 'carcinoma'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c105   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time and the patient has active cancer, prescribe azithromycin instead.

Patient: 66-year-old male. Reason for the visit: Presents with acute streptococcal pharyngitis (rapid antigen test positive).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has cancer now
  Do not mention diabetes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has diabetes now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's wife has diabetes now.
Every line that mentions diabetes must contain one of these words (a longer word that starts with one is fine): 'diabet'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c111   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia treated at home, prescribe amoxicillin. Score 1 point if the current systolic blood pressure is above 160 mmHg; 1 point if the patient is allergic to sulfonamide antibiotics; 2 points if the patient has ever had asthma (current or past); 3 points if the patient has active cancer. If the score is 6 or more, prescribe doxycycline instead.

Patient: 52-year-old male. Reason for the visit: Productive cough and fever; consolidation on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has cancer now
  fact 2: the patient has asthma now
  fact 3: systolic blood pressure: 135 mmHg, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: systolic blood pressure: 170 mmHg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: systolic blood pressure: 153 mmHg, the current value.
Every line that mentions systolic blood pressure must contain one of these words (a longer word that starts with one is fine): 'systolic' | 'blood pressure' | 'bp'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c114   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 1 point if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 1 point if the patient has had cancer at any time (active or in remission); 2 points if the patient has ever had heart failure (current or past). If the score is 3 or more, prescribe nitrofurantoin instead.

Patient: 24-year-old female. Reason for the visit: Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had diabetes in the past (years ago)
  fact 2: systolic blood pressure: 120 mmHg, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: systolic blood pressure: 179 mmHg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: systolic blood pressure: 153 mmHg, the current value.
Every line that mentions systolic blood pressure must contain one of these words (a longer word that starts with one is fine): 'systolic' | 'blood pressure' | 'bp'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c115   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.

Patient: 66-year-old female. Reason for the visit: Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has warfarin treatment now
  fact 2: calf swelling compared with the other leg: 1.1 cm, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: calf swelling compared with the other leg: 3.8 cm, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: calf swelling compared with the other leg: 2.9 cm, the current value.
Every line that mentions calf swelling compared with the other leg must contain one of these words (a longer word that starts with one is fine): 'calf circumference' | 'calf swelling'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c119   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had a venous thromboembolism (current or past), prescribe clotrimazole pessaries instead.

Patient: 36-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has tender anterior cervical lymph nodes now
  Do not mention a venous thromboembolism (DVT or pulmonary embolism) in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has a venous thromboembolism (DVT or pulmonary embolism) now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have a venous thromboembolism (DVT or pulmonary embolism) (a clear denial).
Every line that mentions a venous thromboembolism (DVT or pulmonary embolism) must contain one of these words (a longer word that starts with one is fine): 'thrombo' | 'dvt' | 'pulmonary embol'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c124   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): NEWS2 (as used here, partial: only the stated band of each listed item): 3 points for a heart rate of 131/min or more; 3 points for a systolic blood pressure of 220 mmHg or more; 2 points for a temperature of 39.1 C or more; 2 points for current use of supplemental oxygen. Any other value of these items scores 0 here, and the other NEWS2 items are not part of this question. Only current findings count.

Patient: 86-year-old female. Reason for the visit: Newly admitted to the medical ward with a chest infection.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: temperature: 37.2 C, the current value
  fact 2: heart rate: 87/min, the current value
  fact 3: systolic blood pressure: 144 mmHg, the current value
  Do not mention supplemental oxygen in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has supplemental oxygen now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have supplemental oxygen (a clear denial).
Every line that mentions supplemental oxygen must contain one of these words (a longer word that starts with one is fine): 'supplemental oxygen'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c126   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

Patient: adult male. Reason for the visit: Acute pulmonary embolism confirmed on CT pulmonary angiography.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 124 mmHg, the current value
  fact 2: oxygen saturation: 94%, the current value
  fact 3: heart rate: 99/min, the current value
  fact 4: age: 55 years, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: heart rate: 110/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: heart rate: 107/min, the current value.
Every line that mentions heart rate must contain one of these words (a longer word that starts with one is fine): 'heart rate'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
fact 4: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c129   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

Patient: 56-year-old female. Reason for the visit: Sore throat for two days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: temperature: 36.9 C, the current value
  fact 2: the patient had a myocardial infarction (heart attack) in the past (in 2009)
  FLIP (instruction): one line that replaces your line for fact 1, stating: temperature: 39.2 C, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: temperature: 37.7 C, the current value.
Every line that mentions temperature must contain one of these words (a longer word that starts with one is fine): 'temperature'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c137   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current blood urea nitrogen is above 19 mg/dL.

Patient: 32-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: blood urea nitrogen: 14 mg/dL, the current value
  fact 2: the patient has diabetes now
  Do not mention colorectal cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had colorectal cancer in the past (in 2021).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have colorectal cancer (a clear denial).
Every line that mentions colorectal cancer must contain one of these words (a longer word that starts with one is fine): 'colorectal cancer' | 'colon cancer' | 'bowel cancer'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c140   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

Patient: 47-year-old female. Reason for the visit: Acute low back pain after lifting.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 13.5 x10^9/L, the current value
  Do not mention angioedema in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had angioedema in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's roommate had angioedema in the past (years ago).
Every line that mentions angioedema must contain one of these words (a longer word that starts with one is fine): 'angioedema'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c143   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For thromboprophylaxis in a medical inpatient, prescribe compression stockings. Score 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. If the score is 4 or more, prescribe enoxaparin instead.

Patient: adult male. Reason for the visit: Admitted with community-acquired pneumonia; expected to stay in bed for several days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 71 years, the current value
  Do not mention cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has cancer now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient had cancer in the past (in 2020); it is over or resolved, not current.
Every line that mentions cancer must contain one of these words (a longer word that starts with one is fine): 'cancer' | 'lymphoma' | 'leukemia' | 'myeloma' | 'carcinoma'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c144   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. Score 1 point if the current platelet count is below 50 x10^9/L; 1 point if the patient is currently taking warfarin; 1 point if the patient has ever had diabetes (current or past); 3 points if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe a progestin-only pill instead.

Patient: 32-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a mechanical heart valve now
  fact 2: platelet count: 320 x10^9/L, the current value
  fact 3: the patient had diabetes in the past (years ago)
  FLIP (instruction): one line that replaces your line for fact 2, stating: platelet count: 49 x10^9/L, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: platelet count: 50 x10^9/L, the current value.
Every line that mentions platelet count must contain one of these words (a longer word that starts with one is fine): 'platelet'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c148   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.

Patient: 75-year-old male. Reason for the visit: Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: calf swelling compared with the other leg: 1.1 cm, the current value
  fact 2: the patient has colorectal cancer now
  FLIP (instruction): one line that replaces your line for fact 1, stating: calf swelling compared with the other leg: 3.0 cm, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: calf swelling compared with the other leg: 2.4 cm, the current value.
Every line that mentions calf swelling compared with the other leg must contain one of these words (a longer word that starts with one is fine): 'calf circumference' | 'calf swelling'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c149   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

Patient: adult male. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: calf swelling compared with the other leg: 3.1 cm, the current value
  fact 2: age: 54 years, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: age: 70 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: age: 65 years, the current value.
Every line that mentions age must contain one of these words (a longer word that starts with one is fine): 'age'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c150   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

Patient: 28-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: eGFR: 29 mL/min/1.73 m2, the current value
  Do not mention diabetes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had diabetes in the past (in 2016).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's roommate had diabetes in the past (years ago).
Every line that mentions diabetes must contain one of these words (a longer word that starts with one is fine): 'diabet'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c152   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If the age of the patient is 75 years or more and the patient has ever had a venous thromboembolism (current or past), prescribe ezetimibe instead.

Patient: adult male. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 77 years, the current value
  Do not mention a venous thromboembolism (DVT or pulmonary embolism) in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's sister had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago).
Every line that mentions a venous thromboembolism (DVT or pulmonary embolism) must contain one of these words (a longer word that starts with one is fine): 'thrombo' | 'dvt' | 'pulmonary embol'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c153   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If the current serum creatinine is 1.5 mg/dL or more and the patient has ever had heart failure (current or past), prescribe intravenous co-amoxiclav instead.

Patient: 87-year-old female. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum creatinine: 1.7 mg/dL, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had heart failure in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have heart failure (a clear denial).
Every line that mentions heart failure must contain one of these words (a longer word that starts with one is fine): 'heart failure'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c156   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

Patient: adult female. Reason for the visit: Coffee-ground vomiting since the early hours; assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 50 years, the current value
  fact 2: systolic blood pressure: 154 mmHg, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has heart failure now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's father has heart failure now.
Every line that mentions heart failure must contain one of these words (a longer word that starts with one is fine): 'heart failure'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c157   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. Score 1 point if the current platelet count is below 50 x10^9/L; 1 point if the patient is currently taking warfarin; 1 point if the patient has ever had diabetes (current or past); 3 points if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe a progestin-only pill instead.

Patient: 38-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a mechanical heart valve now
  fact 2: platelet count: 262 x10^9/L, the current value
  fact 3: the patient has warfarin treatment now
  Do not mention diabetes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had diabetes in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have diabetes (a clear denial).
Every line that mentions diabetes must contain one of these words (a longer word that starts with one is fine): 'diabet'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c159   (writer: author3; checker: author4)

Rule, for context only (do not refer to it in the note): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

Patient: 43-year-old female. Reason for the visit: Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 76/min, the current value
  fact 2: serum potassium: 4.1 mmol/L, the current value
  fact 3: an earlier heart rate of 67/min, measured in 2020
  FLIP (instruction): one line that replaces your line for fact 1, stating: heart rate: 102/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: an earlier heart rate of 99/min, measured in 2020.
Every line that mentions heart rate must contain one of these words (a longer word that starts with one is fine): 'heart rate'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 
