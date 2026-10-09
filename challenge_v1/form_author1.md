# challenge_v1 writing form: author1

Read `challenge_v1/WRITING_GUIDE.md` first. Fill in every field after the colon. Save this file as `challenge_v1/notes_author1.md` (UTF-8).
40 groups. Your second author checks them in this same file: `check_ok` (yes or no, with the fingerprint from `challenge_v1/ASSEMBLY_REPORT.md`) and `check_comment`.

## c007   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

Patient: adult female. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: calf swelling compared with the other leg: 0.8 cm, the current value
  fact 2: age: 49 years, the current value
  fact 3: the patient has colorectal cancer now
  FLIP (instruction): one line that replaces your line for fact 2, stating: age: 71 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: age: 65 years, the current value.
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

## c008   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

Patient: 44-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum potassium: 5.3 mmol/L, the current value
  Do not mention diabetes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient's father had diabetes in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have diabetes (a clear denial).
Every line that mentions diabetes must contain one of these words (a longer word that starts with one is fine): 'diabet'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c009   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the current blood urea nitrogen is above 19 mg/dL; the patient has had a major bleeding event at any time; the patient currently has heart failure.

Patient: 78-year-old male. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had a major bleed in the past (years ago)
  fact 2: blood urea nitrogen: 9 mg/dL, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: blood urea nitrogen: 29 mg/dL, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: blood urea nitrogen: 17 mg/dL, the current value.
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

## c018   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has ever had heart failure (current or past); the current platelet count is below 50 x10^9/L; the current temperature is above 38.0 C.

Patient: 42-year-old female. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: platelet count: 35 x10^9/L, the current value
  fact 2: temperature: 36.8 C, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had heart failure in the past (in 2014).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have heart failure (a clear denial).
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

## c025   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.

Patient: adult female. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: blood urea nitrogen: 13 mg/dL, the current value
  fact 2: respiratory rate: 19/min, the current value
  fact 3: age: 49 years, the current value
  fact 4: systolic blood pressure: 139 mmHg, the current value
  FLIP (instruction): one line that replaces your line for fact 4, stating: systolic blood pressure: 70 mmHg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 4, stating: systolic blood pressure: 90 mmHg, the current value.
Every line that mentions systolic blood pressure must contain one of these words (a longer word that starts with one is fine): 'systolic' | 'blood pressure' | 'bp'.

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

## c027   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.

Patient: 51-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: weight: 74 kg, the current value
  fact 2: heart rate: 68/min, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: heart rate: 98/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: heart rate: 90/min, the current value.
Every line that mentions heart rate must contain one of these words (a longer word that starts with one is fine): 'heart rate'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c029   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time and the patient has active cancer, prescribe azithromycin instead.

Patient: 59-year-old female. Reason for the visit: Presents with acute streptococcal pharyngitis (rapid antigen test positive).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had diabetes in the past (years ago)
  Do not mention cancer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has cancer now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's uncle has cancer now.
Every line that mentions cancer must contain one of these words (a longer word that starts with one is fine): 'cancer' | 'lymphoma' | 'leukemia' | 'myeloma' | 'carcinoma'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c041   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For rate control in atrial fibrillation, prescribe metoprolol. If the current weight is 60 kg or less or the current respiratory rate is 30/min or more, prescribe diltiazem instead.

Patient: 46-year-old male. Reason for the visit: Atrial fibrillation with a ventricular rate of 128/min.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: respiratory rate: 20/min, the current value
  fact 2: an earlier weight of 94 kg, measured in 2017
  fact 3: weight: 67 kg, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: weight: 50 kg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: an earlier weight of 54 kg, measured in 2017.
Every line that mentions weight must contain one of these words (a longer word that starts with one is fine): 'weight' | 'weighs' | 'weighed'.

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

## c046   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For rate control in atrial fibrillation, prescribe metoprolol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 2 points if the patient has ever had a venous thromboembolism (current or past); 3 points if the patient has ever had coronary artery disease (current or past); 1 point if the current white cell count is above 12.0 x10^9/L. If the score is 4 or more, prescribe diltiazem instead.

Patient: 45-year-old male. Reason for the visit: Atrial fibrillation with a ventricular rate of 128/min.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 5.5 x10^9/L, the current value
  fact 2: the patient had diabetes in the past (in 2010)
  fact 3: the patient had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago)
  FLIP (instruction): one line that replaces your line for fact 1, stating: white cell count: 13.9 x10^9/L, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: white cell count: 12.0 x10^9/L, the current value.
Every line that mentions white cell count must contain one of these words (a longer word that starts with one is fine): 'white cell' | 'wbc'.

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

## c049   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

Patient: adult male. Reason for the visit: Coffee-ground vomiting since the early hours; assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 46 years, the current value
  fact 2: systolic blood pressure: 144 mmHg, the current value
  Do not mention heart failure in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has heart failure now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have heart failure (a clear denial).
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

## c054   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.

Patient: 16-year-old male. Reason for the visit: Sore throat for two days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: white cell count: 10.0 x10^9/L, the current value
  fact 2: the patient has tonsillar exudate now
  FLIP (instruction): one line that replaces your line for fact 1, stating: white cell count: 12.7 x10^9/L, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: white cell count: 12.0 x10^9/L, the current value.
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

## c057   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If the current serum creatinine is 1.5 mg/dL or more and the patient has ever had heart failure (current or past), prescribe intravenous co-amoxiclav instead.

Patient: 56-year-old female. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: an earlier serum creatinine of 0.9 mg/dL, measured in 2006
  fact 2: serum creatinine: 1.1 mg/dL, the current value
  fact 3: the patient has heart failure now
  FLIP (instruction): one line that replaces your line for fact 2, stating: serum creatinine: 1.6 mg/dL, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: an earlier serum creatinine of 1.9 mg/dL, measured in 2006.
Every line that mentions serum creatinine must contain one of these words (a longer word that starts with one is fine): 'creatinine'.

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

## c059   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. Score 3 points if the age of the patient is 65 years or more; 2 points if the current systolic blood pressure is below 90 mmHg; 1 point if the current blood urea nitrogen is above 19 mg/dL; 3 points if the patient has ever had diabetes (current or past). If the score is 6 or more, prescribe intravenous piperacillin-tazobactam instead.

Patient: adult female. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 88 mmHg, the current value
  fact 2: age: 46 years, the current value
  fact 3: an earlier blood urea nitrogen of 11 mg/dL, measured in 2016
  fact 4: blood urea nitrogen: 14 mg/dL, the current value
  fact 5: the patient has diabetes now
  FLIP (instruction): one line that replaces your line for fact 4, stating: blood urea nitrogen: 28 mg/dL, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: an earlier blood urea nitrogen of 28 mg/dL, measured in 2016.
Every line that mentions blood urea nitrogen must contain one of these words (a longer word that starts with one is fine): 'bun' | 'urea nitrogen'.

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

## c063   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the current weight is 60 kg or less; the patient currently has heart failure.

Patient: 82-year-old female. Reason for the visit: Atrial fibrillation; anticoagulation indicated.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has heart failure now
  fact 2: an earlier weight of 94 kg, measured in 2007
  fact 3: weight: 96 kg, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: weight: 49 kg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: an earlier weight of 50 kg, measured in 2007.
Every line that mentions weight must contain one of these words (a longer word that starts with one is fine): 'weight' | 'weighs' | 'weighed'.

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

## c064   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had asthma (current or past); 1 point if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past); 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time. If the score is 6 or more, prescribe nitrofurantoin instead.

Patient: 39-year-old female. Reason for the visit: Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had a peptic ulcer in the past (in 2024)
  fact 2: the patient had asthma in the past (years ago)
  fact 3: calf swelling compared with the other leg: 4.5 cm, the current value
  Do not mention diabetes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had diabetes in the past (in 2021).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's roommate had diabetes in the past (years ago).
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

## c068   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For primary prevention, prescribe atorvastatin. If the current blood urea nitrogen is above 19 mg/dL or the current heart rate is above 90/min, prescribe ezetimibe instead.

Patient: 46-year-old female. Reason for the visit: Primary prevention; LDL cholesterol 182 mg/dL.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: blood urea nitrogen: 12 mg/dL, the current value
  fact 2: heart rate: 76/min, the current value
  fact 3: an earlier heart rate of 64/min, measured in 2008
  FLIP (instruction): one line that replaces your line for fact 2, stating: heart rate: 104/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: an earlier heart rate of 105/min, measured in 2008.
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

## c069   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had heart failure (current or past); the patient has an active peptic ulcer; the age of the patient is 65 years or more.

Patient: adult male. Reason for the visit: Newly diagnosed type 2 diabetes (HbA1c 7.9%).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had heart failure in the past (in 2022)
  fact 2: age: 56 years, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: age: 69 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: age: 62 years, the current value.
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

## c073   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

Patient: adult male. Reason for the visit: Acute pulmonary embolism confirmed on CT pulmonary angiography.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 156 mmHg, the current value
  fact 2: age: 70 years, the current value
  fact 3: oxygen saturation: 98%, the current value
  fact 4: heart rate: 75/min, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: oxygen saturation: 84%, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: oxygen saturation: 90%, the current value.
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

## c075   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

Patient: adult female. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 72 years, the current value
  Do not mention a myocardial infarction or peripheral artery disease in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had a myocardial infarction (heart attack) in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's roommate had a myocardial infarction (heart attack) in the past (years ago).
Every line that mentions a myocardial infarction or peripheral artery disease must contain one of these words (a longer word that starts with one is fine): 'myocardial infarction' | 'peripheral artery' | 'heart attack'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c078   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

Patient: 65-year-old male. Reason for the visit: Acute low back pain after lifting.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: serum potassium: 5.4 mmol/L, the current value
  Do not mention coronary artery disease in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had coronary artery disease in the past (in 2009).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's friend had coronary artery disease in the past (years ago).
Every line that mentions coronary artery disease must contain one of these words (a longer word that starts with one is fine): 'coronary'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c081   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For thromboprophylaxis in a medical inpatient, prescribe compression stockings. Score 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. If the score is 4 or more, prescribe enoxaparin instead.

Patient: adult female. Reason for the visit: Admitted with community-acquired pneumonia; expected to stay in bed for several days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 71 years, the current value
  Do not mention a venous thromboembolism (DVT or pulmonary embolism) in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's wife had a venous thromboembolism (DVT or pulmonary embolism) in the past (years ago).
Every line that mentions a venous thromboembolism (DVT or pulmonary embolism) must contain one of these words (a longer word that starts with one is fine): 'thrombo' | 'dvt' | 'pulmonary embol'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c083   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

Patient: 51-year-old female. Reason for the visit: Suspected urinary sepsis, assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 141 mmHg, the current value
  fact 2: respiratory rate: 17/min, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: respiratory rate: 29/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: respiratory rate: 20/min, the current value.
Every line that mentions respiratory rate must contain one of these words (a longer word that starts with one is fine): 'respiratory rate'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c091   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.

Patient: 85-year-old female. Reason for the visit: Spreading redness and warmth of the right shin for two days.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: weight: 84 kg, the current value
  fact 2: the patient's sister has coronary artery disease now
  FLIP (instruction): one line that replaces your line for fact 1, stating: weight: 55 kg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: weight: 61 kg, the current value.
Every line that mentions weight must contain one of these words (a longer word that starts with one is fine): 'weight' | 'weighs' | 'weighed'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c093   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. Score 3 points if the age of the patient is 65 years or more; 2 points if the current systolic blood pressure is below 90 mmHg; 1 point if the current blood urea nitrogen is above 19 mg/dL; 3 points if the patient has ever had diabetes (current or past). If the score is 6 or more, prescribe intravenous piperacillin-tazobactam instead.

Patient: adult female. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: systolic blood pressure: 136 mmHg, the current value
  fact 2: age: 74 years, the current value
  fact 3: blood urea nitrogen: 23 mg/dL, the current value
  Do not mention diabetes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had diabetes in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's sister had diabetes in the past (years ago).
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

## c095   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

Patient: adult female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 98/min, the current value
  fact 2: age: 52 years, the current value
  Do not mention a peptic ulcer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had a peptic ulcer in the past (years ago).
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's uncle had a peptic ulcer in the past (years ago).
Every line that mentions a peptic ulcer must contain one of these words (a longer word that starts with one is fine): 'ulcer'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c097   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.

Patient: 64-year-old female. Reason for the visit: Shortness of breath and fever; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: respiratory rate: 14/min, the current value
  fact 2: systolic blood pressure: 113 mmHg, the current value
  fact 3: oxygen saturation: 97%, the current value
  FLIP (instruction): one line that replaces your line for fact 1, stating: respiratory rate: 25/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: respiratory rate: 23/min, the current value.
Every line that mentions respiratory rate must contain one of these words (a longer word that starts with one is fine): 'respiratory rate'.

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

## c104   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For newly diagnosed type 2 diabetes, prescribe metformin. If the patient has ever had angioedema (current or past) and the patient has ever had coronary artery disease (current or past), prescribe sitagliptin instead.

Patient: 35-year-old female. Reason for the visit: Newly diagnosed type 2 diabetes (HbA1c 7.9%).

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient had angioedema in the past (years ago)
  Do not mention coronary artery disease in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient had coronary artery disease in the past (in 2014).
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

## c110   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

Patient: 33-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: eGFR: 68 mL/min/1.73 m2, the current value
  fact 2: the patient has diabetes now
  fact 3: an earlier eGFR of 82 mL/min/1.73 m2, measured in 2022
  FLIP (instruction): one line that replaces your line for fact 1, stating: eGFR: 12 mL/min/1.73 m2, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: an earlier eGFR of 14 mL/min/1.73 m2, measured in 2022.
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

## c113   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had a venous thromboembolism (current or past), prescribe clotrimazole pessaries instead.

Patient: 63-year-old female. Reason for the visit: Vaginal itching and discharge; candidiasis confirmed on microscopy.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a venous thromboembolism (DVT or pulmonary embolism) now
  Do not mention tender anterior cervical lymph nodes in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has tender anterior cervical lymph nodes now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient had tender anterior cervical lymph nodes in the past (in 2024); it is over or resolved, not current.
Every line that mentions tender anterior cervical lymph nodes must contain one of these words (a longer word that starts with one is fine): 'lymph node' | 'lymphaden'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c116   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.

Patient: adult male. Reason for the visit: Suspected sepsis; admitted from the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 54 years, the current value
  fact 2: platelet count: 226 x10^9/L, the current value
  Do not mention new confusion in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has new confusion now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient's wife has new confusion now.
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

## c118   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

Patient: adult male. Reason for the visit: Community-acquired pneumonia confirmed on chest radiograph.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 52 years, the current value
  fact 2: calf swelling compared with the other leg: 0.1 cm, the current value
  fact 3: the patient's sister has colorectal cancer now
  FLIP (instruction): one line that replaces your line for fact 1, stating: age: 73 years, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: age: 65 years, the current value.
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

## c122   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): Johns Hopkins Fall Risk Assessment Tool (as used here, partial): 1 point for age 60 years or more; 5 points for one fall in the six months before this admission; 1 point for new confusion (altered awareness of the surroundings). Other items are not part of this question.

Patient: adult female. Reason for the visit: Admitted to the medical ward with a urinary infection.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 54 years, the current value
  Do not mention a fall in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient fell once at home in the weeks before this admission.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly has not fallen in the past six months (a clear denial).
Every line that mentions a fall must contain one of these words (a longer word that starts with one is fine): 'fallen' | 'fell' | 'fall'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c123   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.

Patient: 23-year-old female. Reason for the visit: Requests contraception.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: weight: 86 kg, the current value
  fact 2: platelet count: 48 x10^9/L, the current value
  fact 3: the patient has tender anterior cervical lymph nodes now
  fact 4: the patient's father has coronary artery disease now
  FLIP (instruction): one line that replaces your line for fact 1, stating: weight: 52 kg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: weight: 63 kg, the current value.
Every line that mentions weight must contain one of these words (a longer word that starts with one is fine): 'weight' | 'weighs' | 'weighed'.

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

## c130   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For inpatient VTE prophylaxis, prescribe enoxaparin. Score 1 point if the patient has ever had angioedema (current or past); 1 point if the patient has new confusion; 2 points if the current temperature is above 38.0 C; 2 points if the age of the patient is 65 years or more. If the score is 5 or more, prescribe intermittent pneumatic compression instead.

Patient: adult male. Reason for the visit: Admitted for community-acquired pneumonia; immobile.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 73 years, the current value
  fact 2: temperature: 38.4 C, the current value
  Do not mention angioedema in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has angioedema now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have angioedema (a clear denial).
Every line that mentions angioedema must contain one of these words (a longer word that starts with one is fine): 'angioedema'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c135   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. Score 3 points if the age of the patient is 65 years or more; 2 points if the current systolic blood pressure is below 90 mmHg; 1 point if the current blood urea nitrogen is above 19 mg/dL; 3 points if the patient has ever had diabetes (current or past). If the score is 6 or more, prescribe intravenous piperacillin-tazobactam instead.

Patient: adult male. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: an earlier systolic blood pressure of 121 mmHg, measured in 2014
  fact 2: blood urea nitrogen: 27 mg/dL, the current value
  fact 3: systolic blood pressure: 148 mmHg, the current value
  fact 4: age: 66 years, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: systolic blood pressure: 89 mmHg, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: an earlier systolic blood pressure of 79 mmHg, measured in 2014.
Every line that mentions systolic blood pressure must contain one of these words (a longer word that starts with one is fine): 'systolic' | 'blood pressure' | 'bp'.

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

## c139   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.

Patient: 57-year-old male. Reason for the visit: Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: heart rate: 70/min, the current value
  FLIP (instruction): one line that replaces your line for fact 1, stating: heart rate: 111/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 1, stating: heart rate: 100/min, the current value.
Every line that mentions heart rate must contain one of these words (a longer word that starts with one is fine): 'heart rate'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c145   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

Patient: 68-year-old female. Reason for the visit: Hip osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has diabetes now
  fact 2: serum creatinine: 1.1 mg/dL, the current value
  FLIP (instruction): one line that replaces your line for fact 2, stating: serum creatinine: 2.0 mg/dL, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 2, stating: serum creatinine: 1.4 mg/dL, the current value.
Every line that mentions serum creatinine must contain one of these words (a longer word that starts with one is fine): 'creatinine'.

header: 
reason: 
fact 1: 
fact 2: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 

## c146   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the patient is allergic to penicillin; 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe acetaminophen instead.

Patient: 74-year-old female. Reason for the visit: Knee osteoarthritis with pain on walking.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has a venous thromboembolism (DVT or pulmonary embolism) now
  fact 2: the patient has a penicillin allergy now
  fact 3: heart rate: 77/min, the current value
  FLIP (instruction): one line that replaces your line for fact 3, stating: heart rate: 100/min, the current value.
  NEAR-MISS (instruction): one line that replaces your line for fact 3, stating: heart rate: 86/min, the current value.
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

## c154   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For stroke prevention in atrial fibrillation, prescribe apixaban. Score 2 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient currently has tonsillar exudate; 2 points if the current ALT is above 120 U/L; 2 points if the current weight is 60 kg or less. If the score is 6 or more, prescribe warfarin instead.

Patient: 63-year-old female. Reason for the visit: Atrial fibrillation; anticoagulation indicated.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: the patient has coronary artery disease now
  fact 2: weight: 56 kg, the current value
  fact 3: ALT: 56 U/L, the current value
  Do not mention tonsillar exudate in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has tonsillar exudate now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have tonsillar exudate (a clear denial).
Every line that mentions tonsillar exudate must contain one of these words (a longer word that starts with one is fine): 'exudate'.

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

## c155   (writer: author1; checker: author2)

Rule, for context only (do not refer to it in the note): For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

Patient: adult male. Reason for the visit: Suspected chest infection; assessed on the medical ward.

BASE note: one line for each fact below, in this order, in your own words.
  fact 1: age: 67 years, the current value
  Do not mention a peptic ulcer in the base note at all, not even to deny it.
  FLIP (instruction): one line that is added to the base note, stating: the patient has a peptic ulcer now.
  NEAR-MISS (instruction): one line that is added to the base note, stating: the patient explicitly does not have a peptic ulcer (a clear denial).
Every line that mentions a peptic ulcer must contain one of these words (a longer word that starts with one is fine): 'ulcer'.

header: 
reason: 
fact 1: 
extra: 
FLIP: 
NEAR: 
check_ok: 
check_comment: 
