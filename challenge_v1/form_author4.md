# challenge_v1 writing form: author4

Read `challenge_v1/WRITING_GUIDE.md` first. Fill in every field after the colon. Save this file as `challenge_v1/notes_<your name>.md`.
40 groups; your second author fills `check_ok` and `check_comment`.

## c001   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

Patient: 55-year-old female. Reason for the visit: Acute low back pain after lifting.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 6.1 x10^9/L, the current value
  fact 2: the patient had angioedema in the past (years ago); it is over or resolved, not current
FLIP: one line that replaces your line for fact 1, stating: white cell count: 14.3 x10^9/L, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: white cell count: 12.0 x10^9/L, the current value.
Every line that mentions white cell count must contain one of these words (a longer word that starts with one is fine): 'white cell' | 'wbc'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c003   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

Patient: 50-year-old female. Reason for the visit: Atrial fibrillation; anticoagulation indicated.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had colorectal cancer in the past (in 2020); it is over or resolved, not current
  fact 2: white cell count: 12.7 x10^9/L, the current value
  Do not mention coronary artery disease in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient had coronary artery disease in the past (years ago); it is over or resolved, not current.
NEAR-MISS: one line that is added to the base note, stating: the patient's sister had coronary artery disease in the past (years ago); it is over or resolved, not current.
Every line that mentions coronary artery disease must contain one of these words (a longer word that starts with one is fine): 'coronary'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c004   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the current serum potassium is above 5.0 mmol/L; the patient currently has a mechanical heart valve; the patient has ever had coronary artery disease (current or past).

Patient: 72-year-old female. Reason for the visit: Productive cough and fever; consolidation on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum potassium: 3.8 mmol/L, the current value
  fact 2: the patient has a mechanical heart valve now
FLIP: one line that replaces your line for fact 1, stating: serum potassium: 5.4 mmol/L, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: serum potassium: 4.9 mmol/L, the current value.
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

## c005   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.

Patient: 24-year-old female. Reason for the visit: Sore throat for two days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had a myocardial infarction or peripheral artery disease in the past (years ago); it is over or resolved, not current
  fact 2: white cell count: 8.6 x10^9/L, the current value
  Do not mention tonsillar exudate in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has tonsillar exudate now.
NEAR-MISS: one line that is added to the base note, stating: the patient's father has tonsillar exudate now.
Every line that mentions tonsillar exudate must contain one of these words (a longer word that starts with one is fine): 'exudate'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c006   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the current blood urea nitrogen is above 19 mg/dL; the patient has had a major bleeding event at any time; the patient currently has heart failure.

Patient: 86-year-old female. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: blood urea nitrogen: 22 mg/dL, the current value
  Do not mention a major bleed in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient had a major bleed in the past (in 2016); it is over or resolved, not current.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have a major bleed (a clear denial).
Every line that mentions a major bleed must contain one of these words (a longer word that starts with one is fine): 'bleed'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c011   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

Patient: 46-year-old female. Reason for the visit: Acute low back pain after lifting.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum potassium: 5.4 mmol/L, the current value
  Do not mention coronary artery disease in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient had coronary artery disease in the past (in 2011); it is over or resolved, not current.
NEAR-MISS: one line that is added to the base note, stating: the patient's sister had coronary artery disease in the past (years ago); it is over or resolved, not current.
Every line that mentions coronary artery disease must contain one of these words (a longer word that starts with one is fine): 'coronary'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c016   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

Patient: 51-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 63/min, the current value
  fact 2: an earlier heart rate of 78/min, measured in 2019
  fact 3: the patient has coronary artery disease now
  fact 4: eGFR: 39 mL/min/1.73 m2, the current value
FLIP: one line that replaces your line for fact 1, stating: heart rate: 101/min, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: an earlier heart rate of 101/min, measured in 2019.
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

## c017   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For inpatient VTE prophylaxis, prescribe enoxaparin. Score 1 point if the patient has ever had angioedema (current or past); 1 point if the patient has new confusion; 2 points if the current temperature is above 38.0 C; 2 points if the age of the patient is 65 years or more. If the score is 5 or more, prescribe intermittent pneumatic compression instead.

Patient: adult male. Reason for the visit: Admitted for community-acquired pneumonia; immobile.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had angioedema in the past (years ago); it is over or resolved, not current
  fact 2: the patient has new confusion now
  fact 3: age: 46 years, the current value
  fact 4: temperature: 38.5 C, the current value
FLIP: one line that replaces your line for fact 3, stating: age: 68 years, the current value.
NEAR-MISS: one line that replaces your line for fact 3, stating: age: 62 years, the current value.
Every line that mentions age must contain one of these words (a longer word that starts with one is fine): 'age'.

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

## c019   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): Alvarado score (as used here, partial): 2 points for current tenderness in the right lower quadrant (right iliac fossa); 2 points for a current white cell count above 10.0 x10^9/L; 1 point for a current temperature of 37.3 C or more. Other Alvarado items are not part of this question.

Patient: 33-year-old male. Reason for the visit: Abdominal pain for one day; assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 6.0 x10^9/L, the current value
  fact 2: temperature: 36.5 C, the current value
FLIP: one line that replaces your line for fact 1, stating: white cell count: 11.9 x10^9/L, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: white cell count: 10.0 x10^9/L, the current value.
Every line that mentions white cell count must contain one of these words (a longer word that starts with one is fine): 'white cell' | 'wbc'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c023   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

Patient: adult male. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 56 years, the current value
  fact 2: calf swelling: 3.4 cm, the current value
FLIP: one line that replaces your line for fact 1, stating: age: 76 years, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: age: 65 years, the current value.
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

## c026   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

Patient: 55-year-old male. Reason for the visit: Hip osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum creatinine: 1.6 mg/dL, the current value
  Do not mention diabetes in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has diabetes now.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have diabetes (a clear denial).
Every line that mentions diabetes must contain one of these words (a longer word that starts with one is fine): 'diabet'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c028   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.

Patient: 40-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: platelet count: 35 x10^9/L, the current value
  fact 2: the patient had coronary artery disease in the past (years ago); it is over or resolved, not current
  fact 3: the patient has tender anterior cervical lymph nodes now
  fact 4: an earlier weight of 84 kg, measured in 2017
  fact 5: weight: 71 kg, the current value
FLIP: one line that replaces your line for fact 5, stating: weight: 60 kg, the current value.
NEAR-MISS: one line that replaces your line for fact 4, stating: an earlier weight of 57 kg, measured in 2017.
Every line that mentions weight must contain one of these words (a longer word that starts with one is fine): 'weight' | 'weighs'.

header: 
reason: 
fact 1: 
fact 2: 
fact 3: 
fact 4: 
fact 5: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c032   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

Patient: adult female. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 72 years, the current value
  Do not mention a peptic ulcer in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has a peptic ulcer now.
NEAR-MISS: one line that is added to the base note, stating: the patient's sister has a peptic ulcer now.
Every line that mentions a peptic ulcer must contain one of these words (a longer word that starts with one is fine): 'ulcer'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c043   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.

Patient: 30-year-old female. Reason for the visit: Shortness of breath and fever; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: respiratory rate: 15/min, the current value
  fact 2: oxygen saturation: 98%, the current value
  fact 3: systolic blood pressure: 150 mmHg, the current value
  Do not mention new confusion in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has new confusion now.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have new confusion (a clear denial).
Every line that mentions new confusion must contain one of these words (a longer word that starts with one is fine): 'confus' | 'disorient'.

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

## c048   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

Patient: 35-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: eGFR: 52 mL/min/1.73 m2, the current value
  fact 2: the patient had diabetes in the past (in 2014); it is over or resolved, not current
FLIP: one line that replaces your line for fact 1, stating: eGFR: 28 mL/min/1.73 m2, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: eGFR: 30 mL/min/1.73 m2, the current value.
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

## c051   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.

Patient: 60-year-old male. Reason for the visit: Recovering on the ward after a myocardial infarction treated with a stent.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum potassium: 4.4 mmol/L, the current value
  fact 2: the patient's sister has a venous thromboembolism (DVT or pulmonary embolism) now
FLIP: one line that replaces your line for fact 1, stating: serum potassium: 5.2 mmol/L, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: serum potassium: 5.0 mmol/L, the current value.
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

## c055   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

Patient: adult male. Reason for the visit: Coffee-ground vomiting since the early hours; assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 46 years, the current value
  fact 2: systolic blood pressure: 127 mmHg, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has heart failure now.
NEAR-MISS: one line that is added to the base note, stating: the patient had heart failure in the past (years ago); it is over or resolved, not current.
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

## c058   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the current systolic blood pressure is above 160 mmHg; the age of the patient is 75 years or more; the patient has ever had asthma (current or past).

Patient: adult male. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had asthma in the past (years ago); it is over or resolved, not current
  fact 2: systolic blood pressure: 122 mmHg, the current value
  fact 3: age: 60 years, the current value
FLIP: one line that replaces your line for fact 2, stating: systolic blood pressure: 167 mmHg, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: systolic blood pressure: 160 mmHg, the current value.
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

## c061   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

Patient: adult female. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 72 years, the current value
  Do not mention a myocardial infarction or peripheral artery disease in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has a myocardial infarction or peripheral artery disease now.
NEAR-MISS: one line that is added to the base note, stating: the patient's wife has a myocardial infarction or peripheral artery disease now.
Every line that mentions a myocardial infarction or peripheral artery disease must contain one of these words (a longer word that starts with one is fine): 'myocardial infarction' | 'peripheral artery' | 'heart attack'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c065   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum creatinine is above 2.0 mg/dL and the patient has ever had heart failure (current or past), prescribe aspirin plus clopidogrel instead.

Patient: 79-year-old male. Reason for the visit: Recovering on the ward after a myocardial infarction treated with a stent.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum creatinine: 2.3 mg/dL, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has heart failure now.
NEAR-MISS: one line that is added to the base note, stating: the patient's wife has heart failure now.
Every line that mentions heart failure must contain one of these words (a longer word that starts with one is fine): 'heart failure'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c067   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).

Patient: adult female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 82 years, the current value
  Do not mention cancer in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient had cancer in the past (in 2014); it is over or resolved, not current.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have cancer (a clear denial).
Every line that mentions cancer must contain one of these words (a longer word that starts with one is fine): 'cancer' | 'lymphoma' | 'leukemia' | 'myeloma' | 'carcinoma'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c070   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the patient is allergic to penicillin; 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe acetaminophen instead.

Patient: 83-year-old female. Reason for the visit: Knee osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago); it is over or resolved, not current
  fact 2: heart rate: 99/min, the current value
  Do not mention a penicillin allergy in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has a penicillin allergy now.
NEAR-MISS: one line that is added to the base note, stating: the patient had a penicillin allergy in the past (years ago); it is over or resolved, not current.
Every line that mentions a penicillin allergy must contain one of these words (a longer word that starts with one is fine): 'penicillin'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c074   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

Patient: adult male. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 47 years, the current value
  fact 2: the patient has a myocardial infarction or peripheral artery disease now
FLIP: one line that replaces your line for fact 1, stating: age: 75 years, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: age: 63 years, the current value.
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

## c082   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia treated at home, prescribe amoxicillin. Score 1 point if the current systolic blood pressure is above 160 mmHg; 1 point if the patient is allergic to sulfonamide antibiotics; 2 points if the patient has ever had asthma (current or past); 3 points if the patient has active cancer. If the score is 6 or more, prescribe doxycycline instead.

Patient: 42-year-old female. Reason for the visit: Productive cough and fever; consolidation on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has cancer now
  fact 2: systolic blood pressure: 146 mmHg, the current value
  fact 3: the patient had asthma in the past (years ago); it is over or resolved, not current
FLIP: one line that replaces your line for fact 2, stating: systolic blood pressure: 172 mmHg, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: systolic blood pressure: 155 mmHg, the current value.
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

## c090   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

Patient: 34-year-old female. Reason for the visit: Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 77/min, the current value
  fact 2: an earlier serum potassium of 4.4 mmol/L, measured in 2017
  fact 3: serum potassium: 3.9 mmol/L, the current value
FLIP: one line that replaces your line for fact 3, stating: serum potassium: 5.2 mmol/L, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: an earlier serum potassium of 5.0 mmol/L, measured in 2017.
Every line that mentions serum potassium must contain one of these words (a longer word that starts with one is fine): 'potassium'.

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

## c096   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For musculoskeletal pain, prescribe ibuprofen. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time and the patient is allergic to penicillin, prescribe acetaminophen instead.

Patient: 45-year-old male. Reason for the visit: Acute low back pain after lifting.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had coronary artery disease in the past (years ago); it is over or resolved, not current
  Do not mention a penicillin allergy in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has a penicillin allergy now.
NEAR-MISS: one line that is added to the base note, stating: the patient's friend has a penicillin allergy now.
Every line that mentions a penicillin allergy must contain one of these words (a longer word that starts with one is fine): 'penicillin'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c098   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. Score 2 points for a major bleeding event at any time; 1 point for age 75 years or more; 1 point for a current eGFR below 30 mL/min/1.73 m2. If the score is 2 or more, prescribe aspirin plus clopidogrel instead.

Patient: adult male. Reason for the visit: Recovering on the ward after a myocardial infarction treated with a stent.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: eGFR: 77 mL/min/1.73 m2, the current value
  fact 2: age: 51 years, the current value
  Do not mention a major bleed in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient had a major bleed in the past (years ago); it is over or resolved, not current.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have a major bleed (a clear denial).
Every line that mentions a major bleed must contain one of these words (a longer word that starts with one is fine): 'bleed'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c099   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

Patient: adult male. Reason for the visit: Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 70 years, the current value
  fact 2: weight: 77 kg, the current value
FLIP: one line that replaces your line for fact 1, stating: age: 81 years, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: age: 73 years, the current value.
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

## c107   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If the current blood urea nitrogen is above 19 mg/dL or the current heart rate is above 90/min, prescribe ezetimibe instead.

Patient: 51-year-old male. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: blood urea nitrogen: 13 mg/dL, the current value
  fact 2: heart rate: 69/min, the current value
FLIP: one line that replaces your line for fact 1, stating: blood urea nitrogen: 21 mg/dL, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: blood urea nitrogen: 19 mg/dL, the current value.
Every line that mentions blood urea nitrogen must contain one of these words (a longer word that starts with one is fine): 'bun' | 'urea nitrogen'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c108   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time and the patient has active cancer, prescribe azithromycin instead.

Patient: 70-year-old female. Reason for the visit: Presents with acute streptococcal pharyngitis (rapid antigen test positive).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient's sister had diabetes in the past (years ago); it is over or resolved, not current
  Do not mention cancer in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has cancer now.
NEAR-MISS: one line that is added to the base note, stating: the patient's roommate has cancer now.
Every line that mentions cancer must contain one of these words (a longer word that starts with one is fine): 'cancer' | 'lymphoma' | 'leukemia' | 'myeloma' | 'carcinoma'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c109   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the current systolic blood pressure is above 160 mmHg; the age of the patient is 75 years or more; the patient has ever had asthma (current or past).

Patient: adult female. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 64 years, the current value
  fact 2: the patient had asthma in the past (years ago); it is over or resolved, not current
  fact 3: systolic blood pressure: 142 mmHg, the current value
FLIP: one line that replaces your line for fact 3, stating: systolic blood pressure: 179 mmHg, the current value.
NEAR-MISS: one line that replaces your line for fact 3, stating: systolic blood pressure: 160 mmHg, the current value.
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

## c117   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For acute streptococcal pharyngitis, prescribe amoxicillin. If the current white cell count is above 12.0 x10^9/L and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe azithromycin instead.

Patient: 67-year-old female. Reason for the visit: Presents with acute streptococcal pharyngitis (rapid antigen test positive).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 13.0 x10^9/L, the current value
  Do not mention diabetes in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has diabetes now.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have diabetes (a clear denial).
Every line that mentions diabetes must contain one of these words (a longer word that starts with one is fine): 'diabet'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c120   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the patient has an active peptic ulcer, prescribe clotrimazole pessaries instead.

Patient: 29-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a peptic ulcer now
  Do not mention a myocardial infarction or peripheral artery disease in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has a myocardial infarction or peripheral artery disease now.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have a myocardial infarction or peripheral artery disease (a clear denial).
Every line that mentions a myocardial infarction or peripheral artery disease must contain one of these words (a longer word that starts with one is fine): 'myocardial infarction' | 'peripheral artery' | 'heart attack'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c121   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current systolic blood pressure is 90 mmHg or less, prescribe fondaparinux instead.

Patient: 79-year-old female. Reason for the visit: First day after elective total hip replacement.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 149 mmHg, the current value
  fact 2: an earlier systolic blood pressure of 142 mmHg, measured in 2023
  fact 3: the patient has a myocardial infarction or peripheral artery disease now
FLIP: one line that replaces your line for fact 1, stating: systolic blood pressure: 80 mmHg, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: an earlier systolic blood pressure of 85 mmHg, measured in 2023.
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

## c132   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For heart failure with reduced ejection fraction, prescribe spironolactone. If the current white cell count is above 12.0 x10^9/L or the current temperature is above 38.0 C, prescribe dapagliflozin instead.

Patient: 58-year-old male. Reason for the visit: Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: an earlier temperature of 36.8 C, measured in 2010
  fact 2: temperature: 37.1 C, the current value
  fact 3: white cell count: 8.1 x10^9/L, the current value
FLIP: one line that replaces your line for fact 2, stating: temperature: 39.0 C, the current value.
NEAR-MISS: one line that replaces your line for fact 1, stating: an earlier temperature of 39.0 C, measured in 2010.
Every line that mentions temperature must contain one of these words (a longer word that starts with one is fine): 'temperature'.

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

## c136   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.

Patient: 45-year-old female. Reason for the visit: Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 132 mmHg, the current value
  fact 2: heart rate: 72/min, the current value
  fact 3: blood urea nitrogen: 11 mg/dL, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has heart failure now.
NEAR-MISS: one line that is added to the base note, stating: the patient had heart failure in the past (years ago); it is over or resolved, not current.
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

## c138   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

Patient: adult male. Reason for the visit: Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: weight: 91 kg, the current value
  fact 2: age: 57 years, the current value
FLIP: one line that replaces your line for fact 2, stating: age: 75 years, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: age: 74 years, the current value.
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

## c147   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has a mechanical heart valve; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the age of the patient is 65 years or more.

Patient: adult male. Reason for the visit: Acute low back pain after lifting.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 68 years, the current value
  Do not mention a mechanical heart valve in the base note at all, not even to deny it.
FLIP: one line that is added to the base note, stating: the patient has a mechanical heart valve now.
NEAR-MISS: one line that is added to the base note, stating: the patient explicitly does not have a mechanical heart valve (a clear denial).
Every line that mentions a mechanical heart valve must contain one of these words (a longer word that starts with one is fine): 'mechanical'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c158   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): For knee osteoarthritis pain, prescribe naproxen. If at least two of the following apply, prescribe acetaminophen instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the patient has ever had angioedema (current or past).

Patient: 57-year-old male. Reason for the visit: Knee osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had angioedema in the past (years ago); it is over or resolved, not current
  fact 2: calf swelling: 1.2 cm, the current value
FLIP: one line that replaces your line for fact 2, stating: calf swelling: 3.2 cm, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: calf swelling: 2.5 cm, the current value.
Every line that mentions calf swelling must contain one of these words (a longer word that starts with one is fine): 'calf circumference' | 'calf swelling'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c160   (writer: author4; checker: author1)

Rule, for context only (do not refer to it in the note): qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

Patient: 30-year-old male. Reason for the visit: Suspected urinary sepsis, assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: respiratory rate: 12/min, the current value
  fact 2: systolic blood pressure: 144 mmHg, the current value
FLIP: one line that replaces your line for fact 2, stating: systolic blood pressure: 100 mmHg, the current value.
NEAR-MISS: one line that replaces your line for fact 2, stating: systolic blood pressure: 105 mmHg, the current value.
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
