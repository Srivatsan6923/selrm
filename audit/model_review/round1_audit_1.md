# Audit sample 1


## 1.1 ('sirs', 'hr', 'boundary', 'long') templates=train

RULE: SIRS criteria (as used here, partial): 1 point each for temperature above 38.0 C; heart rate above 90/min; respiratory rate above 20/min; white cell count above 12.0 x10^9/L. Only current findings count.
CONDITION: heart rate above 90
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 1 point.'

BASE (answer s):
Patient: female, 41 years.
Productive cough for three days; assessed in the emergency department.
Her partner is nearsighted.
Uses a smartphone for reminders.
Heart rate 68/min at rest this morning.
Phosphate 3.6 mg/dL in 2008.
Eats a varied diet.
Feeds birds in the backyard.
Drinks plenty of water.
WBC on the blood count drawn at this assessment: 9.2 x10^9/L.
Non-smoker.
Respiratory rate, counted over a full minute today, is 13/min.
Her cousin has a chipped front tooth.
Temperature 37.4 C at this assessment.
Bakes bread at home.
Vaccinations up to date.
Magnesium 2.0 mg/dL in 2017.
Ferritin 60 ng/mL in 2006.
Sings in a weekly choir.
Lives on a quiet street.
Watches football on weekends.
Height 170 cm.

FLIP (answer s'): -Heart rate 68/min at rest this morning. | +Heart rate 115/min at rest this morning.

NEAR (answer s): -Heart rate 68/min at rest this morning. | +Heart rate 90/min at rest this morning.

MISSING (answer neither (undetermined)): -Heart rate 68/min at rest this morning.

PRES (answer s): full text
41-year-old woman.
Productive cough for three days; assessed in the emergency department.
Feeds birds in the backyard.
Bakes bread at home.
Height 170 cm.
Respiratory rate 13/min at this assessment.
Magnesium 2.0 mg/dL in 2017.
Watches football on weekends.
Sings in a weekly choir.
Vaccinations up to date.
Temperature today: 37.4 C.
Phosphate 3.6 mg/dL in 2008.
Her cousin has a chipped front tooth.
Eats a varied diet.
Non-smoker.
Uses a smartphone for reminders.
Lives on a quiet street.
Complete blood count this morning: white cell count 9.2 x10^9/L.
Her partner is nearsighted.
Drinks plenty of water.
Pulse taken this morning: heart rate 68/min.
Ferritin 60 ng/mL in 2006.


## 1.2 ('gs047', 'c2', 'negation', 'long') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. If the patient is currently taking aspirin and the patient currently has tonsillar exudate, prescribe diltiazem instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Man of 43 years.
Atrial fibrillation with a ventricular rate of 128/min.
Tonsils slightly red but clean, without pus.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2015.
Sleeps seven hours a night.
During a checkup in 2016, total protein was 7.0 g/dL.
His wife has recovered from a dislocated finger.
Photographs local wildlife.
Paints watercolors as a hobby.
His roommate lives with psoriasis.
Enjoys board games.
Currently on low-dose aspirin for heart protection.
His wife burned a hand on a stove years ago.
Drives a car.
Prefers morning appointments.
Knits as a hobby.
In 2022, lipase was 30 U/L.
His sister sprained a thumb last month.

FLIP (answer s'): -Tonsils slightly red but clean, without pus. | +Tonsils swollen and coated with yellow exudate.

NEAR (answer s): -Tonsils slightly red but clean, without pus. | +Tonsillar exudate absent on examination.

MISSING (answer neither (undetermined)): -Tonsils slightly red but clean, without pus. | +Tonsillar exudate: unknown.

PRES (answer s): full text
Male patient of 43 years.
Atrial fibrillation with a ventricular rate of 128/min.
His roommate lives with psoriasis.
Uses a daily aspirin on a cardiologist's recommendation.
His wife has recovered from a dislocated finger.
His sister sprained a thumb last month.
Drives a car.
Prefers morning appointments.
Knits as a hobby.
Sees a dentist yearly.
Enjoys board games.
Paints watercolors as a hobby.
Tonsils pink and clean on inspection.
Photographs local wildlife.
During a checkup in 2016, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2015.
Sleeps seven hours a night.
In 2022, lipase was 30 U/L.
His wife burned a hand on a stove years ago.


## 1.3 ('gs193', 'c1', 'numeric', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current blood urea nitrogen is 20 mg/dL or more, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: blood urea nitrogen at least 20
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
42-year-old man.
Suspected chest infection; assessed on the medical ward.
Enjoys gardening.
Lives on a quiet street.
Hearing normal to conversation.
BUN at this assessment: 8 mg/dL.

FLIP (answer s'): -BUN at this assessment: 8 mg/dL. | +BUN at this assessment: 40 mg/dL.

NEAR (answer s): -BUN at this assessment: 8 mg/dL. | +BUN at this assessment: 18 mg/dL.

MISSING (answer neither (undetermined)): -BUN at this assessment: 8 mg/dL.

PRES (answer s): full text
Male, 42 years.
Suspected chest infection; assessed on the medical ward.
Lives on a quiet street.
BUN on today's chemistry panel: 8 mg/dL.
Hearing normal to conversation.
Enjoys gardening.


## 1.4 ('gs112', 'c2', 'subject', 'easy') templates=test

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the patient is currently taking aspirin; 2 points if the current ALT is above 200 U/L. If the score is 5 or more, prescribe dapagliflozin instead.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Male patient of 72 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Owns a bicycle.
Current ALT 250 U/L.
His sister has known coronary artery disease.

FLIP (answer s'): +Currently on low-dose aspirin for heart protection.

NEAR (answer s): +His roommate is on low-dose aspirin.

MISSING (answer neither (undetermined)): +Aspirin use: unknown.

PRES (answer s): full text
Man of 72 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
ALT now 250 U/L.
His sister has angina from coronary artery disease.
Owns a bicycle.


## 1.5 ('s1_adrop', 'sbp', 'time', 'easy') templates=train

RULE: A-DROP (as used here, partial): 1 point each for a current blood urea nitrogen of 21 mg/dL or more; a current oxygen saturation of 90% or less; new confusion or disorientation; a current systolic blood pressure of 90 mmHg or less. Age is scored separately and is not part of this question.
CONDITION: systolic blood pressure at or below 90
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 1 point.'

BASE (answer s):
62-year-old woman.
Fever and cough with new consolidation on chest radiograph.
Systolic blood pressure 104 mmHg at a clinic visit in 2024.
Grows tomatoes in the garden.
Listens to podcasts.
Memory and concentration normal on bedside testing.
Manual cuff blood pressure today: 117/74 mmHg.
Keeps houseplants.
Oxygen saturation by finger probe today: 96%.
Today's BUN is 12 mg/dL.

FLIP (answer s'): -Manual cuff blood pressure today: 117/74 mmHg. | +Manual cuff blood pressure today: 73/48 mmHg.

NEAR (answer s): -Systolic blood pressure 104 mmHg at a clinic visit in 2024. | +Systolic blood pressure 74 mmHg at a clinic visit in 2024.

MISSING (answer neither (undetermined)): -Systolic blood pressure 104 mmHg at a clinic visit in 2024. | -Manual cuff blood pressure today: 117/74 mmHg.

PRES (answer s): full text
Female, 62 years.
Fever and cough with new consolidation on chest radiograph.
Listens to podcasts.
Oriented to person, place and time.
BUN at this assessment: 12 mg/dL.
Grows tomatoes in the garden.
Blood pressure today: 117/74 mmHg.
In 2024, systolic blood pressure was 104 mmHg.
Pulse oximetry this morning: oxygen saturation 96%.
Keeps houseplants.


## 1.6 ('s2_atria_bleed', 'egfr', 'boundary', 'alt') templates=test

RULE: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 45 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.
CONDITION: eGFR below 45
CLAIMS: s = 'The eGFR criterion contributes 0 points.' | s' = 'The eGFR criterion contributes 3 points.'

BASE (answer s):
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Currently aged 62 years.
Teeth in good repair.
Current eGFR 73 mL/min/1.73 m2.
Sees a dentist yearly.
Current Hgb 15.8 g/dL.
Echocardiogram shows normal left ventricular wall thickness.

FLIP (answer s'): -Current eGFR 73 mL/min/1.73 m2. | +Current eGFR 34 mL/min/1.73 m2.

NEAR (answer s): -Current eGFR 73 mL/min/1.73 m2. | +Current eGFR 45 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Current eGFR 73 mL/min/1.73 m2.

PRES (answer s): full text
An adult man.
Atrial fibrillation; a decision on warfarin is pending.
Retinal examination shows healthy vessels.
Sees a dentist yearly.
Teeth in good repair.
Current age 62 years.
Latest Hgb result: 15.8 g/dL.
eGFR now 73 mL/min/1.73 m2.


## 1.7 ('gs249', 'c2', 'negation', 'easy') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If the patient has ever had a venous thromboembolism (current or past) and the patient has an active peptic ulcer, prescribe dapagliflozin instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
76-year-old man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Speaks English and Spanish.
Height 170 cm.
No dyspepsia or melena.
Non-smoker.
Previously had a DVT, in 2010.

FLIP (answer s'): -No dyspepsia or melena. | +Taking omeprazole for a gastric ulcer diagnosed at endoscopy this week.

NEAR (answer s): -No dyspepsia or melena. | +No ulcer of the stomach or duodenum at any time.

MISSING (answer neither (undetermined)): -No dyspepsia or melena. | +Active peptic ulcer: not recorded.

PRES (answer s): full text
Patient: male, 76 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Deep vein thrombosis following knee surgery in 2010; resolved with treatment.
Non-smoker.
Height 170 cm.
Speaks English and Spanish.
Bowel habit normal; no abdominal pain.


## 1.8 ('gs224', 'c2', 'numeric', 'long') templates=test

RULE: For knee osteoarthritis pain, prescribe naproxen. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time or the current platelet count is 350 x10^9/L or more, prescribe acetaminophen instead.
CONDITION: platelet count at least 350
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Female patient of 59 years.
Knee osteoarthritis with pain on walking.
Sleeps seven hours a night.
In 2014, lipase was 30 U/L.
Sees a dentist yearly.
Varicose veins: none seen.
Platelet count now 269 x10^9/L.
Teeth in good repair.
Her wife has recovered from a dislocated finger.
In 2015, folate was 12 ng/mL.
Uses sunscreen in summer.
Photographs local wildlife.
Enjoys board games.
Her sister has a lazy eye.
Plays the piano.
Drives a car.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Prefers morning appointments.
Her roommate sprained a thumb last month.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Her roommate wears contact lenses.

FLIP (answer s'): -Platelet count now 269 x10^9/L. | +Platelet count now 494 x10^9/L.

NEAR (answer s): -Platelet count now 269 x10^9/L. | +Platelet count now 334 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count now 269 x10^9/L.

PRES (answer s): full text
Woman of 59 years.
Knee osteoarthritis with pain on walking.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Enjoys board games.
Photographs local wildlife.
Pupils equal and reactive to light.
Owns a bicycle.
Sees a dentist yearly.
Uses sunscreen in summer.
Her roommate sprained a thumb last month.
Coagulation tests normal on recent bloodwork.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Current platelet count 269 x10^9/L.
Her roommate wears contact lenses.
In 2014, lipase was 30 U/L.
Prefers morning appointments.
Her wife has recovered from a dislocated finger.
Teeth in good repair.
Drives a car.
Plays the piano.
Her sister has a lazy eye.
In 2015, folate was 12 ng/mL.


## 1.9 ('gs087', 'c2', 'subject', 'easy') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the current temperature is above 38.0 C and the patient has ever had heart failure (current or past), prescribe naproxen with omeprazole instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
A 46-year-old woman.
Hip osteoarthritis with pain on walking.
Oral temperature this morning: 39.2 C.
Plays chess online.
Keeps a step counter.
Bakes bread at home.

FLIP (answer s'): +Chronic heart failure (NYHA class II).

NEAR (answer s): +Her husband had heart failure in 2020.

MISSING (answer neither (undetermined)): +Heart failure: not asked about.

PRES (answer s): full text
46-year-old woman.
Hip osteoarthritis with pain on walking.
Bakes bread at home.
Keeps a step counter.
Plays chess online.
Temperature today: 39.2 C.


## 1.10 ('gs223', 'c1', 'time', 'long') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current calf swelling compared with the other leg is 3.0 cm or more and the current platelet count is below 150 x10^9/L, prescribe aspirin plus clopidogrel instead.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Female patient of 42 years.
Recovering on the ward after a myocardial infarction treated with a stent.
In 2013, folate was 12 ng/mL.
Knits as a hobby.
Current calf swelling 0.2 cm compared with the other leg.
Owns a bicycle.
Lives in a second-floor apartment.
Plays the piano.
Drives a car.
Sees a dentist yearly.
During a checkup in 2014, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Her father lives with psoriasis.
Enjoys board games.
Her sister wears contact lenses.
Photographs local wildlife.
Platelet count now 109 x10^9/L.
Back in 2023, calf swelling measured 0.6 cm.
Zinc of 85 mcg/dL in 2018.
Uses sunscreen in summer.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers morning appointments.

FLIP (answer s'): -Current calf swelling 0.2 cm compared with the other leg. | +Current calf swelling 4.5 cm compared with the other leg.

NEAR (answer s): -Back in 2023, calf swelling measured 0.6 cm. | +Back in 2023, calf swelling measured 5.4 cm.

MISSING (answer neither (undetermined)): -Current calf swelling 0.2 cm compared with the other leg. | -Back in 2023, calf swelling measured 0.6 cm.

PRES (answer s): full text
Woman of 42 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Owns a bicycle.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
Prefers morning appointments.
Sees a dentist yearly.
Plays the piano.
Pupils equal and reactive to light.
In 2013, folate was 12 ng/mL.
Records from 2023 list calf swelling at 0.6 cm.
Calf swelling now amounts to 0.2 cm of extra girth in the larger calf.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Her sister wears contact lenses.
Enjoys board games.
Zinc of 85 mcg/dL in 2018.
During a checkup in 2014, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Current platelet count 109 x10^9/L.
Photographs local wildlife.
Her father lives with psoriasis.


## 1.11 ('gs186', 'c1', 'boundary', 'long') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the current serum creatinine is above 2.0 mg/dL; 2 points if the patient currently has heart failure; 1 point if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe acetaminophen instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: female, 72 years.
Knee osteoarthritis with pain on walking.
Her coworker had a splinter removed from a finger.
Drinks plenty of water.
Grows tomatoes in the garden.
Lives on a quiet street.
Her partner broke a wrist, which has healed.
Plays chess online.
Collects postcards.
Serum calcium 9.4 mg/dL in 2013.
Non-smoker.
Vitamin D 38 ng/mL in 2024 (wellness visit).
Chloride 103 mmol/L in 2021.
Enjoys cooking.
Serum creatinine today: 0.9 mg/dL.
Volunteers at a library.
Her husband is left-handed.
Vaccinations up to date.
Nails normal.
Height 170 cm.
Mechanical aortic valve, functioning normally on echocardiography today.
Heart failure with reduced ejection fraction.
Keeps a step counter.
Eats a varied diet.
Uses public transport.

FLIP (answer s'): -Serum creatinine today: 0.9 mg/dL. | +Serum creatinine today: 2.2 mg/dL.

NEAR (answer s): -Serum creatinine today: 0.9 mg/dL. | +Serum creatinine today: 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Serum creatinine today: 0.9 mg/dL.

PRES (answer s): full text
72-year-old woman.
Knee osteoarthritis with pain on walking.
Vaccinations up to date.
Enjoys cooking.
Breathless on mild exertion because of heart failure.
Her coworker had a splinter removed from a finger.
Her partner broke a wrist, which has healed.
Non-smoker.
Her husband is left-handed.
Eats a varied diet.
Vitamin D 38 ng/mL in 2024 (wellness visit).
Serum calcium 9.4 mg/dL in 2013.
Lives on a quiet street.
Uses public transport.
Collects postcards.
Volunteers at a library.
Nails normal.
Height 170 cm.
Creatinine 0.9 mg/dL on this morning's labs.
Has a mechanical aortic valve.
Keeps a step counter.
Drinks plenty of water.
Chloride 103 mmol/L in 2021.
Grows tomatoes in the garden.
Plays chess online.


## 1.12 ('gs235', 'c1', 'negation', 'easy') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient has ever had diabetes (current or past); 3 points if the patient has new confusion; 2 points if the patient is allergic to penicillin; 2 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time. If the score is 6 or more, prescribe a progestin-only pill instead.
CONDITION: diabetes
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female patient of 31 years.
Requests contraception.
Owns a bicycle.
Teeth in good repair.
Paints watercolors as a hobby.
Bowel cancer cured by surgery years ago, without recurrence.
Penicillin allergy: anaphylaxis.

FLIP (answer s'): +Has type 2 diabetes on metformin.

NEAR (answer s): +Never diagnosed with diabetes.

MISSING (answer neither (undetermined)): +Diabetes: status unclear from the records at hand.

PRES (answer s): full text
Woman of 31 years.
Requests contraception.
Owns a bicycle.
Bowel cancer cured by surgery years ago, without recurrence.
Teeth in good repair.
Known penicillin allergy with angioedema.
Paints watercolors as a hobby.


## 1.13 ('gs182', 'c1', 'numeric', 'easy') templates=train

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current weight is below 67 kg and the patient is allergic to sulfonamide antibiotics, prescribe warfarin instead.
CONDITION: weight below 67
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
A 80-year-old man.
Atrial fibrillation; anticoagulation indicated.
Sulfa antibiotics cause an itchy allergic rash in this patient.
Listens to podcasts.
Weighs 93 kg on the scale this morning.
Feeds birds in the backyard.
Has a pet dog.
Non-smoker.

FLIP (answer s'): -Weighs 93 kg on the scale this morning. | +Weighs 50 kg on the scale this morning.

NEAR (answer s): -Weighs 93 kg on the scale this morning. | +Weighs 70 kg on the scale this morning.

MISSING (answer neither (undetermined)): -Weighs 93 kg on the scale this morning.

PRES (answer s): full text
Male, 80 years.
Atrial fibrillation; anticoagulation indicated.
Weight checked today on a calibrated scale: 93 kg.
Non-smoker.
Listens to podcasts.
Feeds birds in the backyard.
Has a sulfa allergy that causes skin blistering.
Has a pet dog.


## 1.14 ('gs196', 'c2', 'subject', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient currently has tonsillar exudate or the patient currently has tender anterior cervical lymph nodes, prescribe acetaminophen instead.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Female patient of 52 years.
Acute low back pain after lifting.
Tonsils slightly red but clean, without pus.
In 2024, lipase was 30 U/L.
Uses sunscreen in summer.
Knits as a hobby.
Has two cats.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
Owns a bicycle.
Prefers morning appointments.
Prefers to be addressed by first name.
Her father has a lazy eye.
Sleeps seven hours a night.
Enjoys board games.
Her wife has recovered from a dislocated finger.
Lives in a second-floor apartment.
Her wife wears contact lenses.
Zinc of 85 mcg/dL in 2018.
Teeth in good repair.

FLIP (answer s'): +Tender, swollen lymph nodes in the front of the neck.

NEAR (answer s): +Her wife has a throat infection with tender anterior cervical lymph nodes.

MISSING (answer neither (undetermined)): +Tender cervical lymph nodes: unknown.

PRES (answer s): full text
Woman of 52 years.
Acute low back pain after lifting.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Zinc of 85 mcg/dL in 2018.
Owns a bicycle.
In 2024, lipase was 30 U/L.
Teeth in good repair.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Prefers morning appointments.
Her wife burned a hand on a stove years ago.
Tonsils pink and clean on inspection.
Her father has a lazy eye.
Knits as a hobby.
Enjoys board games.
Has two cats.
Her wife wears contact lenses.
Lives in a second-floor apartment.
Her wife has recovered from a dislocated finger.


## 1.15 ('gs231', 'c1', 'time', 'superseded') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 2 points if the current respiratory rate is above 20/min; 2 points if the current serum potassium is above 4.5 mmol/L; 3 points if the patient has ever had heparin-induced thrombocytopenia (current or past); 2 points if the current blood urea nitrogen is 21 mg/dL or more. If the score is 6 or more, prescribe azithromycin instead.
CONDITION: respiratory rate above 20
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
58-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
BUN on today's chemistry panel: 26 mg/dL.
On admission, respiratory rate was 13/min; it has since been repeated.
Nails normal.
Has a pet dog.
Does crossword puzzles.
No heparin products on the medication chart today.
Respiratory rate today: 13/min.
Potassium 5.3 mmol/L on today's blood work.

FLIP (answer s'): -Respiratory rate today: 13/min. | +Respiratory rate today: 22/min.

NEAR (answer s): -On admission, respiratory rate was 13/min; it has since been repeated. | +On admission, respiratory rate was 34/min; it has since been repeated.

MISSING (answer neither (undetermined)): -On admission, respiratory rate was 13/min; it has since been repeated. | -Respiratory rate today: 13/min.

PRES (answer s): full text
Patient: male, 58 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Respiratory rate of 13/min measured yesterday was replaced by a repeat measurement.
Has a pet dog.
Respiratory rate, counted over a full minute today, is 13/min.
No heparin given so far during this admission.
Serum potassium today: 5.3 mmol/L.
BUN 26 mg/dL this morning.
Does crossword puzzles.
Nails normal.


## 1.16 ('gs113', 'c2', 'boundary', 'easy') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time or the current ALT is above 200 U/L, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male patient of 59 years.
Suspected chest infection; assessed on the medical ward.
Plays the piano.
HbA1c 5.3% at a routine check.
Current ALT 44 U/L.
Teeth in good repair.
Prefers morning appointments.

FLIP (answer s'): -Current ALT 44 U/L. | +Current ALT 446 U/L.

NEAR (answer s): -Current ALT 44 U/L. | +Current ALT 200 U/L.

MISSING (answer neither (undetermined)): -Current ALT 44 U/L.

PRES (answer s): full text
Man of 59 years.
Suspected chest infection; assessed on the medical ward.
Random glucose 92 mg/dL.
Prefers morning appointments.
Teeth in good repair.
Plays the piano.
ALT now 44 U/L.


## 1.17 ('gs021', 'c4', 'negation', 'long') templates=train

RULE: For acute sore throat, prescribe ibuprofen. Score 1 point if the current serum creatinine is 1.2 mg/dL or more; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had diabetes (current or past); 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 7 or more, prescribe penicillin V instead.
CONDITION: venous thromboembolism in the family
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Patient: male, 43 years.
Sore throat for two days.
Vaccinations up to date.
Does crossword puzzles.
His brother is nearsighted.
Sodium 140 mmol/L in 2012.
Enjoys gardening.
Drinks two cups of coffee a day.
His mother has a stutter.
Keeps houseplants.
Nails normal.
Type 2 diabetes diagnosed in 2010, resolved after weight loss.
Heart rate counted over a full minute at this assessment: 114/min.
Phosphate 3.6 mg/dL in 2020.
Height 170 cm.
Vitamin B12 450 pg/mL in 2011.
Creatinine 1.8 mg/dL on this morning's labs.
Plays chess online.
Collects postcards.
Bicarbonate 26 mmol/L in 2023 (annual physical).

FLIP (answer s'): +On treatment for a deep vein thrombosis in the left leg.

NEAR (answer s): +No venous thromboembolism at any time, personally or among first-degree relatives.

MISSING (answer neither (undetermined)): +Information on venous thromboembolism in the family was not obtained.

PRES (answer s): full text
Male, 43 years.
Sore throat for two days.
Phosphate 3.6 mg/dL in 2020.
Nails normal.
Keeps houseplants.
Collects postcards.
Vitamin B12 450 pg/mL in 2011.
Height 170 cm.
Drinks two cups of coffee a day.
His mother has a stutter.
Does crossword puzzles.
His brother is nearsighted.
Plays chess online.
Enjoys gardening.
Steroid-induced diabetes in 2010, resolved once the steroids were stopped.
Bicarbonate 26 mmol/L in 2023 (annual physical).
Heart rate today: 114/min.
Kidney function today: creatinine 1.8 mg/dL.
Sodium 140 mmol/L in 2012.
Vaccinations up to date.


## 1.18 ('t2d_metformin', 'egfr', 'numeric', 'alt') templates=test

RULE: For newly diagnosed type 2 diabetes, start metformin. If the patient's current eGFR is below 45 mL/min/1.73 m2, start sitagliptin instead.
CONDITION: eGFR below 45
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Male patient of 53 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current eGFR 61 mL/min/1.73 m2.
Pupils equal and reactive to light.

FLIP (answer s'): -Current eGFR 61 mL/min/1.73 m2. | +Current eGFR 33 mL/min/1.73 m2.

NEAR (answer s): -Current eGFR 61 mL/min/1.73 m2. | +Current eGFR 46 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Current eGFR 61 mL/min/1.73 m2.

PRES (answer s): full text
Man of 53 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Pupils equal and reactive to light.
eGFR now 61 mL/min/1.73 m2.


## 1.19 ('gs146', 'c3', 'subject', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 3 points if the patient has ever had heart failure (current or past); 1 point if the patient has ever had a stroke or TIA (current or past). If the score is 4 or more, prescribe azithromycin instead.
CONDITION: stroke/TIA
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Patient: female, 18 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Drinks two cups of coffee a day.
Abdomen soft, with no masses on examination.
Heart failure during sepsis in 2024, resolved as the infection cleared.
Lives on a quiet street.
Sings in a weekly choir.
Visual fields full to confrontation.

FLIP (answer s'): -Visual fields full to confrontation. | +Acute ischemic stroke this week.

NEAR (answer s): -Visual fields full to confrontation. | +Her cousin had a stroke in 2024.

MISSING (answer neither (undetermined)): -Visual fields full to confrontation. | +Information on stroke/TIA was not obtained.

PRES (answer s): full text
18-year-old woman.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Sings in a weekly choir.
Drinks two cups of coffee a day.
Bowel habit regular.
Previously had heart failure from a thyroid problem in 2024, resolved with treatment.
Lives on a quiet street.
Cranial nerves intact.


## 1.20 ('news2_red', 'rr', 'time', 'easy') templates=test

RULE: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.
CONDITION: respiratory rate at least 25
CLAIMS: s = 'The respiratory rate criterion contributes 0 points.' | s' = 'The respiratory rate criterion contributes 3 points.'

BASE (answer s):
Man of 41 years.
Shortness of breath and fever; assessed on the medical ward.
Observations now: respiratory rate 13/min.
Records from 2017 list respiratory rate at 14/min.
Pupils equal and reactive to light.
Gives a clear account of the illness.
Latest oxygen saturation reading: 95%.
Observations now: blood pressure 118/75 mmHg.

FLIP (answer s'): -Observations now: respiratory rate 13/min. | +Observations now: respiratory rate 37/min.

NEAR (answer s): -Records from 2017 list respiratory rate at 14/min. | +Records from 2017 list respiratory rate at 28/min.

MISSING (answer neither (undetermined)): -Observations now: respiratory rate 13/min. | -Records from 2017 list respiratory rate at 14/min.

PRES (answer s): full text
Male patient of 41 years.
Shortness of breath and fever; assessed on the medical ward.
Speech clear; follows commands.
Current respiratory rate 13/min.
Current systolic blood pressure 118 mmHg.
Current oxygen saturation 95%.
Pupils equal and reactive to light.
Back in 2017, respiratory rate measured 14/min.


## 1.21 ('rcri', 'cr', 'boundary', 'alt') templates=train

RULE: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.
CONDITION: creatinine above 1.5
CLAIMS: s = 'The creatinine criterion contributes 0 points.' | s' = 'The creatinine criterion contributes 1 point.'

BASE (answer s):
Patient: male, 50 years.
Preoperative assessment before elective colectomy.
Takes no medicines for angina.
Listens to podcasts.
Vaccinations up to date.
Writes with the right hand.
Neurological examination unremarkable.
Creatinine 1.0 mg/dL on this morning's labs.

FLIP (answer s'): -Creatinine 1.0 mg/dL on this morning's labs. | +Creatinine 1.6 mg/dL on this morning's labs.

NEAR (answer s): -Creatinine 1.0 mg/dL on this morning's labs. | +Creatinine 1.5 mg/dL on this morning's labs.

MISSING (answer neither (undetermined)): -Creatinine 1.0 mg/dL on this morning's labs.

PRES (answer s): full text
50-year-old man.
Preoperative assessment before elective colectomy.
Serum creatinine today: 1.0 mg/dL.
No exertional chest discomfort.
Cranial nerves intact.
Writes with the right hand.
Vaccinations up to date.
Listens to podcasts.


## 1.22 ('gs037', 'c2', 'negation', 'easy') templates=test

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If the age of the patient is above 60 years or the patient is allergic to sulfonamide antibiotics, prescribe dapagliflozin instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 45 years.
Has two cats.
Photographs local wildlife.
Sees a dentist yearly.
Current drug allergies: none.

FLIP (answer s'): -Current drug allergies: none. | +Sulfonamide antibiotic allergy: generalized rash.

NEAR (answer s): -Current drug allergies: none. | +Has never been allergic to sulfonamide antibiotics.

MISSING (answer neither (undetermined)): -Current drug allergies: none. | +Sulfonamide allergy: unknown.

PRES (answer s): full text
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Photographs local wildlife.
Has two cats.
Medication allergies: none at present.
Sees a dentist yearly.
Currently aged 45 years.


## 1.23 ('s1_psi', 'bun', 'numeric', 'alt') templates=train

RULE: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 20 mg/dL or more. Age, sex and other items of the index are not part of this question.
CONDITION: blood urea nitrogen at least 20
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 20 points.'

BASE (answer s):
A 52-year-old woman.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Non-smoker.
Eats a varied diet.
Drinks two cups of coffee a day.
Arterial pH 7.43 on the blood gas taken at this assessment.
BUN 13 mg/dL this morning.

FLIP (answer s'): -BUN 13 mg/dL this morning. | +BUN 26 mg/dL this morning.

NEAR (answer s): -BUN 13 mg/dL this morning. | +BUN 19 mg/dL this morning.

MISSING (answer neither (undetermined)): -BUN 13 mg/dL this morning.

PRES (answer s): full text
52-year-old woman.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Arterial blood gas this morning: pH 7.43.
BUN at this assessment: 13 mg/dL.
Eats a varied diet.
Drinks two cups of coffee a day.
Non-smoker.


## 1.24 ('gs096', 'c1', 'subject', 'easy') templates=test

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 2 points if the patient currently has a major bleed; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 1 point if the patient has ever had angioedema (current or past); 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past). If the score is 3 or more, prescribe azithromycin instead.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Man of 34 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Enjoys board games.
Varicose veins: none seen.
Sees a dentist yearly.
Walks without calf pain.
Examination shows no signs of blood loss.
Recurrent angioedema, under allergy follow-up.
Drives a car.

FLIP (answer s'): -Examination shows no signs of blood loss. | +Currently has a major bleed from a duodenal ulcer, with transfusion under way.

NEAR (answer s): -Examination shows no signs of blood loss. | +His friend has major bleeding from the bowel at present.

MISSING (answer neither (undetermined)): -Examination shows no signs of blood loss. | +Active major bleeding: unknown.

PRES (answer s): full text
Male patient of 34 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Ankle-brachial index normal today.
Coagulation tests normal on recent bloodwork.
Drives a car.
Bowel habit normal, without any blood in the stool.
Sees a dentist yearly.
Lives with chronic angioedema that flares several times a year.
Enjoys board games.


## 1.25 ('curb65', 'bun', 'time', 'easy') templates=train

RULE: CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
CONDITION: urea above 19
CLAIMS: s = 'The urea criterion contributes 0 points.' | s' = 'The urea criterion contributes 1 point.'

BASE (answer s):
Female patient.
Community-acquired pneumonia confirmed on chest radiograph.
Answers questions appropriately.
Systolic blood pressure 122 mmHg at this assessment.
Keeps houseplants.
Blood urea nitrogen of 17 mg/dL recorded in 2008.
Respiratory rate 21/min this morning.
Drinks two cups of coffee a day.
BUN at this assessment: 12 mg/dL.
Age 40 years, calculated today from the date of birth.

FLIP (answer s'): -BUN at this assessment: 12 mg/dL. | +BUN at this assessment: 28 mg/dL.

NEAR (answer s): -Blood urea nitrogen of 17 mg/dL recorded in 2008. | +Blood urea nitrogen of 33 mg/dL recorded in 2008.

MISSING (answer neither (undetermined)): -Blood urea nitrogen of 17 mg/dL recorded in 2008. | -BUN at this assessment: 12 mg/dL.

PRES (answer s): full text
Sex: female.
Community-acquired pneumonia confirmed on chest radiograph.
Manual cuff blood pressure today: 122/77 mmHg.
Drinks two cups of coffee a day.
Respiratory rate, counted over a full minute today, is 21/min.
BUN on today's chemistry panel: 12 mg/dL.
In 2008, blood urea nitrogen was 17 mg/dL.
Alert and attentive.
Keeps houseplants.
Age on arrival: 40 years.


## 1.26 ('gs158', 'c2', 'boundary', 'easy') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time or the current white cell count is above 15.0 x10^9/L, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: white cell count above 15.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male patient of 63 years.
Suspected chest infection; assessed on the medical ward.
Lives in a second-floor apartment.
Knits as a hobby.
Pupils equal and reactive to light.
Latest WBC is 11.4 x10^9/L.
Sees a dentist yearly.

FLIP (answer s'): -Latest WBC is 11.4 x10^9/L. | +Latest WBC is 20.1 x10^9/L.

NEAR (answer s): -Latest WBC is 11.4 x10^9/L. | +Latest WBC is 15.0 x10^9/L.

MISSING (answer neither (undetermined)): -Latest WBC is 11.4 x10^9/L.

PRES (answer s): full text
Man of 63 years.
Suspected chest infection; assessed on the medical ward.
Sees a dentist yearly.
Current white cell count 11.4 x10^9/L.
Knits as a hobby.
Lives in a second-floor apartment.
Pupils equal and reactive to light.


## 1.27 ('gs169', 'c1', 'negation', 'long') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If the patient is currently taking aspirin, prescribe dapagliflozin instead.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Patient: male, 63 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Bakes bread at home.
Sings in a weekly choir.
Keeps houseplants.
Phosphate 3.6 mg/dL in 2016.
Uses reading glasses for small print.
Drinks plenty of water.
His aunt is nearsighted.
Eats a varied diet.
Vaccinations up to date.
Enjoys gardening.
Keeps a step counter.
Drinks two cups of coffee a day.
Collects postcards.
Bicarbonate 26 mmol/L in 2018 (annual physical).
Uses a smartphone for reminders.
Watches football on weekends.
His mother had a splinter removed from a finger.
Grows tomatoes in the garden.
Nails normal.

FLIP (answer s'): +Takes one enteric-coated aspirin with breakfast every day.

NEAR (answer s): +Not taking aspirin.

MISSING (answer neither (undetermined)): +Information on aspirin use was not obtained.

PRES (answer s): full text
A 63-year-old man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Watches football on weekends.
Drinks plenty of water.
Uses reading glasses for small print.
Grows tomatoes in the garden.
Bicarbonate 26 mmol/L in 2018 (annual physical).
Keeps houseplants.
Phosphate 3.6 mg/dL in 2016.
Vaccinations up to date.
Sings in a weekly choir.
Drinks two cups of coffee a day.
Uses a smartphone for reminders.
His mother had a splinter removed from a finger.
His aunt is nearsighted.
Nails normal.
Keeps a step counter.
Collects postcards.
Bakes bread at home.
Eats a varied diet.
Enjoys gardening.


## 1.28 ('gs049', 'c1', 'numeric', 'long') templates=test

RULE: For acute migraine, prescribe sumatriptan. If the current respiratory rate is 30/min or more or the current white cell count is above 12.0 x10^9/L, prescribe naproxen instead.
CONDITION: respiratory rate at least 30
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Woman of 40 years.
Acute migraine without aura, typical of prior attacks.
Her friend burned a hand on a stove years ago.
Enjoys board games.
Current respiratory rate 15/min.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Photographs local wildlife.
Current white cell count 10.8 x10^9/L.
During a checkup in 2018, total protein was 7.0 g/dL.
Owns a bicycle.
Sees a dentist yearly.
Sleeps seven hours a night.
Has two cats.
Plays the piano.
Drives a car.
Knits as a hobby.
Her friend lives with psoriasis.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2023.
Zinc of 85 mcg/dL in 2016.

FLIP (answer s'): -Current respiratory rate 15/min. | +Current respiratory rate 36/min.

NEAR (answer s): -Current respiratory rate 15/min. | +Current respiratory rate 29/min.

MISSING (answer neither (undetermined)): -Current respiratory rate 15/min.

PRES (answer s): full text
Female patient of 40 years.
Acute migraine without aura, typical of prior attacks.
Knits as a hobby.
Latest WBC is 10.8 x10^9/L.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2023.
Her friend burned a hand on a stove years ago.
Prefers to be addressed by first name.
Has two cats.
Enjoys board games.
Her friend lives with psoriasis.
Sleeps seven hours a night.
Drives a car.
Photographs local wildlife.
Lives in a second-floor apartment.
Owns a bicycle.
Zinc of 85 mcg/dL in 2016.
Observations now: respiratory rate 15/min.
During a checkup in 2018, total protein was 7.0 g/dL.
Sees a dentist yearly.
Plays the piano.


## 1.29 ('gs011', 'c2', 'subject', 'long') templates=train

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient currently has a major bleed and the patient has ever had heart failure (current or past), prescribe nitrofurantoin instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Patient: female, 25 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Feeds birds in the backyard.
Drinks plenty of water.
Vaccinations up to date.
Height 170 cm.
Magnesium 2.0 mg/dL in 2019.
Ferritin 60 ng/mL in 2023.
Phosphate 3.6 mg/dL in 2020.
Vomiting large amounts of blood today from a major bleed in the esophagus.
Lives on a quiet street.
Grows tomatoes in the garden.
Uses public transport.
Collects postcards.
Uses a smartphone for reminders.
Non-smoker.
Her housemate has a fear of heights.
Sings in a weekly choir.
Her cousin broke a wrist, which has healed.
Drinks alcohol occasionally.
Watches football on weekends.

FLIP (answer s'): +Heart failure, under regular review in a cardiology clinic.

NEAR (answer s): +Her brother-in-law lives with chronic heart failure.

MISSING (answer neither (undetermined)): +Heart failure: not documented in the records available.

PRES (answer s): full text
25-year-old woman.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Phosphate 3.6 mg/dL in 2020.
Drinks plenty of water.
Feeds birds in the backyard.
Sings in a weekly choir.
Height 170 cm.
Active major upper gastrointestinal bleed, requiring blood transfusion.
Uses public transport.
Ferritin 60 ng/mL in 2023.
Grows tomatoes in the garden.
Vaccinations up to date.
Her housemate has a fear of heights.
Her cousin broke a wrist, which has healed.
Magnesium 2.0 mg/dL in 2019.
Drinks alcohol occasionally.
Collects postcards.
Non-smoker.
Watches football on weekends.
Lives on a quiet street.
Uses a smartphone for reminders.


## 1.30 ('gs116', 'c1', 'time', 'long') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the current weight is 60 kg or less, prescribe sitagliptin instead.
CONDITION: weight at or below 60
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Woman of 46 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Drives a car.
Zinc of 85 mcg/dL in 2021.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her roommate sprained a thumb last month.
Has two cats.
Latest weight 67 kg.
Enjoys board games.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Her roommate has recovered from a dislocated finger.
Knits as a hobby.
Prefers morning appointments.
Records from 2014 list weight at 74 kg.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Teeth in good repair.
During a checkup in 2023, free T3 was 3.2 pg/mL.

FLIP (answer s'): -Latest weight 67 kg. | +Latest weight 53 kg.

NEAR (answer s): -Records from 2014 list weight at 74 kg. | +Records from 2014 list weight at 49 kg.

MISSING (answer neither (undetermined)): -Latest weight 67 kg. | -Records from 2014 list weight at 74 kg.

PRES (answer s): full text
Female patient of 46 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Back in 2014, weight measured 74 kg.
Knits as a hobby.
Teeth in good repair.
Uses sunscreen in summer.
Her roommate has recovered from a dislocated finger.
Pupils equal and reactive to light.
Sees a dentist yearly.
Her roommate sprained a thumb last month.
Has two cats.
Enjoys board games.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Current weight 67 kg.
Zinc of 85 mcg/dL in 2021.
Lives in a second-floor apartment.
Drives a car.
Prefers to be addressed by first name.
Prefers morning appointments.


## 1.31 ('s4_glasgow_imrie', 'bun', 'boundary', 'long') templates=train

RULE: Glasgow-Imrie score for acute pancreatitis (as used here, partial): 1 point each for age above 55 years; a current white cell count above 15.0 x10^9/L; a current blood urea nitrogen above 45 mg/dL. Other Glasgow-Imrie items are not part of this question.
CONDITION: blood urea nitrogen above 45
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 1 point.'

BASE (answer s):
Patient: female.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Height 170 cm.
Wears a seat belt when driving.
Vitamin B12 450 pg/mL in 2023.
Has a pet dog.
Watches football on weekends.
Enjoys gardening.
Collects postcards.
Age today: 40 years.
Plays chess online.
Complete blood count this morning: white cell count 12.8 x10^9/L.
Sodium 140 mmol/L in 2008.
Vaccinations up to date.
Vitamin D 38 ng/mL in 2012 (wellness visit).
Her coworker has a broken finger in a splint.
Her neighbor has a stutter.
Today's BUN is 36 mg/dL.
Her brother-in-law has a fear of heights.
Her cousin is left-handed.

FLIP (answer s'): -Today's BUN is 36 mg/dL. | +Today's BUN is 69 mg/dL.

NEAR (answer s): -Today's BUN is 36 mg/dL. | +Today's BUN is 45 mg/dL.

MISSING (answer neither (undetermined)): -Today's BUN is 36 mg/dL.

PRES (answer s): full text
Female patient.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Vaccinations up to date.
Her coworker has a broken finger in a splint.
Her brother-in-law has a fear of heights.
Wears a seat belt when driving.
Her cousin is left-handed.
WBC 12.8 x10^9/L on today's sample.
Enjoys gardening.
Vitamin D 38 ng/mL in 2012 (wellness visit).
BUN at this assessment: 36 mg/dL.
Her neighbor has a stutter.
Age at this assessment: 40 years.
Has a pet dog.
Height 170 cm.
Collects postcards.
Watches football on weekends.
Vitamin B12 450 pg/mL in 2023.
Sodium 140 mmol/L in 2008.
Plays chess online.


## 1.32 ('gs062', 'c2', 'negation', 'easy') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. Score 1 point if the current eGFR is below 30 mL/min/1.73 m2; 3 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 1 point if the patient is allergic to sulfonamide antibiotics; 3 points if the current platelet count is 350 x10^9/L or more. If the score is 7 or more, prescribe clindamycin instead.
CONDITION: vascular disease
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Woman of 55 years.
Spreading redness and warmth of the right shin for two days.
Uses sunscreen in summer.
Enjoys board games.
Sulfonamide antibiotic allergy: generalized rash.
Plays the piano.
Current eGFR 73 mL/min/1.73 m2.
Current platelet count 516 x10^9/L.

FLIP (answer s'): +Heart attack years ago, with full recovery.

NEAR (answer s): +Has never had a heart attack or peripheral artery disease.

MISSING (answer neither (undetermined)): +Vascular disease: unknown.

PRES (answer s): full text
Female patient of 55 years.
Spreading redness and warmth of the right shin for two days.
Plays the piano.
eGFR now 73 mL/min/1.73 m2.
Develops hives whenever given sulfonamide antibiotics.
Platelet count now 516 x10^9/L.
Uses sunscreen in summer.
Enjoys board games.


## 1.33 ('gs073', 'c1', 'numeric', 'long') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the age of the patient is 65 years or more and the current oxygen saturation is 91% or less, prescribe naproxen with omeprazole instead.
CONDITION: age at least 65
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Patient: female.
Hip osteoarthritis with pain on walking.
Eats a varied diet.
Vitamin B12 450 pg/mL in 2018.
Does crossword puzzles.
Sings in a weekly choir.
Age 43 years, calculated today from the date of birth.
Vaccinations up to date.
Enjoys cooking.
Grows tomatoes in the garden.
Uses a smartphone for reminders.
Ferritin 60 ng/mL in 2012.
Lives on a quiet street.
Vitamin D 38 ng/mL in 2015 (wellness visit).
Height 170 cm.
Oxygen saturation 81% at rest today.
Sodium 140 mmol/L in 2010.
Listens to podcasts.
Her brother-in-law previously wore dental braces.
Hearing normal to conversation.
Volunteers at a library.
Her partner is nearsighted.

FLIP (answer s'): -Age 43 years, calculated today from the date of birth. | +Age 79 years, calculated today from the date of birth.

NEAR (answer s): -Age 43 years, calculated today from the date of birth. | +Age 64 years, calculated today from the date of birth.

MISSING (answer neither (undetermined)): -Age 43 years, calculated today from the date of birth.

PRES (answer s): full text
Female patient.
Hip osteoarthritis with pain on walking.
Vaccinations up to date.
Sings in a weekly choir.
Enjoys cooking.
Listens to podcasts.
Volunteers at a library.
Eats a varied diet.
Lives on a quiet street.
Grows tomatoes in the garden.
Hearing normal to conversation.
Age at this assessment: 43 years.
Her partner is nearsighted.
Vitamin B12 450 pg/mL in 2018.
Ferritin 60 ng/mL in 2012.
Does crossword puzzles.
Uses a smartphone for reminders.
Height 170 cm.
Vitamin D 38 ng/mL in 2015 (wellness visit).
Her brother-in-law previously wore dental braces.
Sodium 140 mmol/L in 2010.
Oxygen saturation by finger probe today: 81%.


## 1.34 ('gs217', 'c1', 'subject', 'easy') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the patient is currently taking warfarin or the current serum potassium is above 4.8 mmol/L, prescribe clindamycin instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Male patient of 64 years.
Spreading redness and warmth of the right shin for two days.
Enjoys board games.
Knits as a hobby.
Current serum potassium 4.4 mmol/L.
Drives a car.
Paints watercolors as a hobby.

FLIP (answer s'): +Currently on warfarin, prescribed by the cardiology clinic.

NEAR (answer s): +His friend is on warfarin with monthly INR checks.

MISSING (answer neither (undetermined)): +Warfarin: unknown.

PRES (answer s): full text
Man of 64 years.
Spreading redness and warmth of the right shin for two days.
Enjoys board games.
Latest potassium result: 4.4 mmol/L.
Paints watercolors as a hobby.
Drives a car.
Knits as a hobby.


## 1.35 ('gs102', 'c3', 'time', 'superseded') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If at least two of the following apply, prescribe azithromycin instead: the patient has ever had angioedema (current or past); the current calf swelling compared with the other leg is 3.0 cm or more; the current systolic blood pressure is 140 mmHg or more.
CONDITION: systolic blood pressure at least 140
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Patient: male, 40 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Tape measurement today shows a calf circumference gap of 4.0 cm.
Bakes bread at home.
Manual cuff blood pressure today: 105/67 mmHg.
On admission, systolic blood pressure was 114 mmHg; it has since been repeated.

FLIP (answer s'): -Manual cuff blood pressure today: 105/67 mmHg. | +Manual cuff blood pressure today: 142/89 mmHg.

NEAR (answer s): -On admission, systolic blood pressure was 114 mmHg; it has since been repeated. | +On admission, systolic blood pressure was 144 mmHg; it has since been repeated.

MISSING (answer neither (undetermined)): -Manual cuff blood pressure today: 105/67 mmHg. | -On admission, systolic blood pressure was 114 mmHg; it has since been repeated.

PRES (answer s): full text
40-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Blood pressure 105/67 mmHg this morning.
Systolic blood pressure was 114 mmHg yesterday, before today's repeat.
Calf circumference measured this morning is 4.0 cm greater on one side.
Bakes bread at home.


## 1.36 ('gs164', 'c3', 'boundary', 'long') templates=test

RULE: For knee osteoarthritis pain, prescribe naproxen. Score 1 point if the current serum creatinine is above 2.0 mg/dL; 1 point if the patient has ever had heparin-induced thrombocytopenia (current or past); 2 points if the current platelet count is below 150 x10^9/L; 1 point if the current ALT is above 200 U/L. If the score is 3 or more, prescribe acetaminophen instead.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Man of 62 years.
Knee osteoarthritis with pain on walking.
Photographs local wildlife.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2020.
Plays the piano.
During a checkup in 2021, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Owns a bicycle.
His sister has a lazy eye.
His friend lives with psoriasis.
Enjoys board games.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2008.
His friend burned a hand on a stove years ago.
Current ALT 399 U/L.
Latest creatinine result: 2.3 mg/dL.
His friend wears contact lenses.
Heparin exposure within the past 100 days: none.
Current platelet count 300 x10^9/L.
Sees a dentist yearly.
Has two cats.

FLIP (answer s'): -Current platelet count 300 x10^9/L. | +Current platelet count 55 x10^9/L.

NEAR (answer s): -Current platelet count 300 x10^9/L. | +Current platelet count 150 x10^9/L.

MISSING (answer neither (undetermined)): -Current platelet count 300 x10^9/L.

PRES (answer s): full text
Male patient of 62 years.
Knee osteoarthritis with pain on walking.
Last received heparin more than a year ago.
His friend lives with psoriasis.
Plays the piano.
His sister has a lazy eye.
Has two cats.
Pupils equal and reactive to light.
His friend burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2020.
Enjoys board games.
His friend wears contact lenses.
Platelet count now 300 x10^9/L.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Current serum creatinine 2.3 mg/dL.
Photographs local wildlife.
During a checkup in 2021, total protein was 7.0 g/dL.
Zinc of 85 mcg/dL in 2008.
Sees a dentist yearly.
ALT now 399 U/L.
Owns a bicycle.
Prefers to be addressed by first name.
Lives in a second-floor apartment.


## 1.37 ('gs155', 'c1', 'negation', 'long') templates=train

RULE: For early Lyme disease, prescribe doxycycline. If at least two of the following apply, prescribe amoxicillin instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the patient has ever had heart failure (current or past); the current oxygen saturation is below 90%.
CONDITION: coronary artery disease in the family
CLAIMS: s = 'Prescribe doxycycline.' | s' = 'Prescribe amoxicillin.'

BASE (answer s):
A 53-year-old woman.
Erythema migrans rash ten days after a tick bite.
Uses public transport.
Her partner has a stutter.
Writes with the right hand.
Enjoys gardening.
Total bilirubin 0.6 mg/dL in 2011.
Drinks alcohol occasionally.
Uses a smartphone for reminders.
Non-smoker.
Serum calcium 9.4 mg/dL in 2018.
Her brother is left-handed.
Chronic heart failure (NYHA class II).
Drinks two cups of coffee a day.
Plays chess online.
Nails normal.
Keeps houseplants.
Sings in a weekly choir.
Lives on a quiet street.
Enjoys cooking.
Oxygen saturation at this assessment is 94%.

FLIP (answer s'): +Her brother is being treated for coronary artery disease.

NEAR (answer s): +Denies coronary artery disease, past or present.

MISSING (answer neither (undetermined)): +Coronary artery disease in the family: not recorded.

PRES (answer s): full text
Female, 53 years.
Erythema migrans rash ten days after a tick bite.
Nails normal.
Enjoys gardening.
Plays chess online.
Sings in a weekly choir.
Non-smoker.
Her brother is left-handed.
Pulse oximetry this morning: oxygen saturation 94%.
Enjoys cooking.
Heart failure, under regular review in a cardiology clinic.
Uses a smartphone for reminders.
Drinks two cups of coffee a day.
Serum calcium 9.4 mg/dL in 2018.
Her partner has a stutter.
Writes with the right hand.
Total bilirubin 0.6 mg/dL in 2011.
Drinks alcohol occasionally.
Uses public transport.
Keeps houseplants.
Lives on a quiet street.


## 1.38 ('sirs', 'temp', 'numeric', 'easy') templates=test

RULE: SIRS criteria (as used here, partial): 1 point each for temperature above 38.0 C; heart rate above 90/min; respiratory rate above 20/min; white cell count above 12.0 x10^9/L. Only current findings count.
CONDITION: temperature above 38.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
Male patient of 58 years.
Productive cough for three days; assessed in the emergency department.
Latest WBC is 4.7 x10^9/L.
Heart rate now 72/min on the monitor.
Uses sunscreen in summer.
Observations now: respiratory rate 13/min.
Knits as a hobby.
Current temperature 36.4 C.

FLIP (answer s'): -Current temperature 36.4 C. | +Current temperature 39.3 C.

NEAR (answer s): -Current temperature 36.4 C. | +Current temperature 37.8 C.

MISSING (answer neither (undetermined)): -Current temperature 36.4 C.

PRES (answer s): full text
Man of 58 years.
Productive cough for three days; assessed in the emergency department.
Knits as a hobby.
Current heart rate 72/min.
Current respiratory rate 13/min.
Uses sunscreen in summer.
Current white cell count 4.7 x10^9/L.
Temperature now 36.4 C (tympanic).


## 1.39 ('gs185', 'c2', 'subject', 'easy') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. If the patient is currently taking clarithromycin and the patient has ever had heparin-induced thrombocytopenia (current or past), prescribe acetaminophen instead.
CONDITION: heparin-induced thrombocytopenia
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: female, 64 years.
Knee osteoarthritis with pain on walking.
Not on any blood thinner at present.
Takes clarithromycin as part of Helicobacter pylori treatment.
Uses public transport.

FLIP (answer s'): -Not on any blood thinner at present. | +Active heparin-induced thrombocytopenia with a positive functional assay.

NEAR (answer s): -Not on any blood thinner at present. | +Her aunt was diagnosed with heparin-induced thrombocytopenia this week.

MISSING (answer neither (undetermined)): -Not on any blood thinner at present. | +Heparin-induced thrombocytopenia: not asked about.

PRES (answer s): full text
64-year-old woman.
Knee osteoarthritis with pain on walking.
Uses public transport.
No heparin products on the medication chart today.
Started clarithromycin this morning for sinusitis.


## 1.40 ('gs082', 'c1', 'time', 'easy') templates=test

RULE: For primary prevention, prescribe atorvastatin. If the current white cell count is below 4.0 x10^9/L, prescribe ezetimibe instead.
CONDITION: white cell count below 4.0
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Man of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Back in 2012, white cell count measured 8.0 x10^9/L.
Latest WBC is 7.7 x10^9/L.
Enjoys board games.

FLIP (answer s'): -Latest WBC is 7.7 x10^9/L. | +Latest WBC is 3.4 x10^9/L.

NEAR (answer s): -Back in 2012, white cell count measured 8.0 x10^9/L. | +Back in 2012, white cell count measured 3.8 x10^9/L.

MISSING (answer neither (undetermined)): -Back in 2012, white cell count measured 8.0 x10^9/L. | -Latest WBC is 7.7 x10^9/L.

PRES (answer s): full text
Male patient of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Enjoys board games.
Current white cell count 7.7 x10^9/L.
Records from 2012 list white cell count at 8.0 x10^9/L.


## 1.41 ('c3_nice_step1', 'age', 'boundary', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe amlodipine. If the patient's current age is below 55 years or the patient has ever had diabetes (current or past), prescribe ramipril instead.
CONDITION: age below 55
CLAIMS: s = 'Prescribe amlodipine.' | s' = 'Prescribe ramipril.'

BASE (answer s):
Sex: male.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Nails normal.
Height 170 cm.
His partner has a broken finger in a splint.
His housemate is left-handed.
No excessive thirst or urination.
His coworker broke a wrist, which has healed.
Eats a varied diet.
Age on arrival: 61 years.
Speaks English and Spanish.
Bicarbonate 26 mmol/L in 2014 (annual physical).
Sings in a weekly choir.
Drinks plenty of water.
Listens to podcasts.
Hearing normal to conversation.
Vaccinations up to date.
Drinks alcohol occasionally.
Uses public transport.
His brother-in-law previously wore dental braces.
Sodium 140 mmol/L in 2012.
Feeds birds in the backyard.
Volunteers at a library.
Non-smoker.

FLIP (answer s'): -Age on arrival: 61 years. | +Age on arrival: 42 years.

NEAR (answer s): -Age on arrival: 61 years. | +Age on arrival: 55 years.

MISSING (answer neither (undetermined)): -Age on arrival: 61 years.

PRES (answer s): full text
Male patient.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Takes no medicines to lower blood sugar.
Feeds birds in the backyard.
Eats a varied diet.
Sings in a weekly choir.
Non-smoker.
Speaks English and Spanish.
Drinks alcohol occasionally.
Uses public transport.
Hearing normal to conversation.
Volunteers at a library.
Vaccinations up to date.
Sodium 140 mmol/L in 2012.
Height 170 cm.
Bicarbonate 26 mmol/L in 2014 (annual physical).
His brother-in-law previously wore dental braces.
Age 61 years, calculated today from the date of birth.
Drinks plenty of water.
His coworker broke a wrist, which has healed.
His housemate is left-handed.
Nails normal.
Listens to podcasts.
His partner has a broken finger in a splint.


## 1.42 ('gs129', 'c1', 'negation', 'easy') templates=test

RULE: For primary prevention, prescribe atorvastatin. If the patient has ever had angioedema (current or past) or the patient is currently taking clarithromycin, prescribe ezetimibe instead.
CONDITION: angioedema
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Woman of 56 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Paints watercolors as a hobby.
Photographs local wildlife.
Sleeps seven hours a night.
Free of facial or oropharyngeal edema.
Enjoys board games.

FLIP (answer s'): -Free of facial or oropharyngeal edema. | +An episode of angioedema years ago, with full recovery.

NEAR (answer s): -Free of facial or oropharyngeal edema. | +Has never had angioedema.

MISSING (answer neither (undetermined)): -Free of facial or oropharyngeal edema. | +Angioedema: unknown.

PRES (answer s): full text
Female patient of 56 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Photographs local wildlife.
Face and neck without swelling on examination.
Enjoys board games.


## 1.43 ('gs215', 'c2', 'numeric', 'easy') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If at least two of the following apply, prescribe naproxen with omeprazole instead: the patient has ever had heparin-induced thrombocytopenia (current or past); the current platelet count is below 150 x10^9/L; the patient is currently taking clarithromycin.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
67-year-old man.
Hip osteoarthritis with pain on walking.
Non-smoker.
Complete blood count today: platelets 241 x10^9/L.
Active heparin-induced thrombocytopenia with a positive functional assay.

FLIP (answer s'): -Complete blood count today: platelets 241 x10^9/L. | +Complete blood count today: platelets 49 x10^9/L.

NEAR (answer s): -Complete blood count today: platelets 241 x10^9/L. | +Complete blood count today: platelets 156 x10^9/L.

MISSING (answer neither (undetermined)): -Complete blood count today: platelets 241 x10^9/L.

PRES (answer s): full text
Male, 67 years.
Hip osteoarthritis with pain on walking.
Platelets 241 x10^9/L on this morning's blood count.
Non-smoker.
On an argatroban infusion this morning for heparin-induced thrombocytopenia.


## 1.44 ('gs038', 'c2', 'subject', 'long') templates=test

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the patient has an active peptic ulcer and the patient has new confusion, prescribe intravenous co-amoxiclav instead.
CONDITION: new confusion
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
Female patient of 72 years.
Community-acquired pneumonia confirmed on chest radiograph.
Sees a dentist yearly.
Her friend wears contact lenses.
Paints watercolors as a hobby.
Has an active duodenal ulcer.
Enjoys board games.
Teeth in good repair.
Sleeps seven hours a night.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Owns a bicycle.
Knits as a hobby.
Her roommate sprained a thumb last month.
Drives a car.
Prefers to be addressed by first name.
Gives a clear account of the illness.
During a checkup in 2014, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2010.

FLIP (answer s'): -Gives a clear account of the illness. | +Disoriented to time and place, which is new for the patient.

NEAR (answer s): -Gives a clear account of the illness. | +Her sister has become disoriented this week.

MISSING (answer neither (undetermined)): -Gives a clear account of the illness. | +New confusion: unknown.

PRES (answer s): full text
Woman of 72 years.
Community-acquired pneumonia confirmed on chest radiograph.
Active peptic ulcer disease.
Owns a bicycle.
Sees a dentist yearly.
Speech clear; follows commands.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Knits as a hobby.
Her friend wears contact lenses.
Pupils equal and reactive to light.
Teeth in good repair.
During a checkup in 2014, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Enjoys board games.
Drives a car.
Free T4 of 1.2 ng/dL in 2010.
Her roommate sprained a thumb last month.
Sleeps seven hours a night.


## 1.45 ('gs049', 'c2', 'time', 'superseded') templates=train

RULE: For acute migraine, prescribe sumatriptan. If the current respiratory rate is 30/min or more or the current white cell count is above 12.0 x10^9/L, prescribe naproxen instead.
CONDITION: white cell count above 12.0
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
A 19-year-old woman.
Acute migraine without aura, typical of prior attacks.
White cell count of 6.0 x10^9/L measured yesterday was replaced by a repeat measurement.
Respiratory rate, counted over a full minute today, is 24/min.
Complete blood count this morning: white cell count 8.5 x10^9/L.
Keeps a step counter.

FLIP (answer s'): -Complete blood count this morning: white cell count 8.5 x10^9/L. | +Complete blood count this morning: white cell count 15.7 x10^9/L.

NEAR (answer s): -White cell count of 6.0 x10^9/L measured yesterday was replaced by a repeat measurement. | +White cell count of 20.7 x10^9/L measured yesterday was replaced by a repeat measurement.

MISSING (answer neither (undetermined)): -White cell count of 6.0 x10^9/L measured yesterday was replaced by a repeat measurement. | -Complete blood count this morning: white cell count 8.5 x10^9/L.

PRES (answer s): full text
Female, 19 years.
Acute migraine without aura, typical of prior attacks.
Yesterday, white cell count was 6.0 x10^9/L; today's value replaces it.
Respiratory rate 24/min this morning.
WBC 8.5 x10^9/L on today's sample.
Keeps a step counter.


## 1.46 ('gs133', 'c2', 'boundary', 'long') templates=test

RULE: For primary prevention, prescribe atorvastatin. If the patient is currently taking clarithromycin and the age of the patient is above 55 years, prescribe ezetimibe instead.
CONDITION: age above 55
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
An adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 49 years.
During a checkup in 2024, total protein was 7.0 g/dL.
Knits as a hobby.
Her uncle lives with psoriasis.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2020.
Her wife has a lazy eye.
Prefers to be addressed by first name.
Teeth in good repair.
Enjoys board games.
Plays the piano.
Sees a dentist yearly.
Prefers morning appointments.
Lives in a second-floor apartment.
Currently taking clarithromycin for an ear infection.
Her sister has recovered from a dislocated finger.
Her wife sprained a thumb last month.

FLIP (answer s'): -Current age 49 years. | +Current age 88 years.

NEAR (answer s): -Current age 49 years. | +Current age 55 years.

MISSING (answer neither (undetermined)): -Current age 49 years.

PRES (answer s): full text
Woman, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Lives in a second-floor apartment.
During a checkup in 2024, total protein was 7.0 g/dL.
Currently aged 49 years.
Her uncle lives with psoriasis.
Her wife sprained a thumb last month.
Sees a dentist yearly.
Enjoys board games.
Knits as a hobby.
Teeth in good repair.
Plays the piano.
On clarithromycin for a chest infection, day 3 of 7.
Photographs local wildlife.
Prefers to be addressed by first name.
Her wife has a lazy eye.
Zinc of 85 mcg/dL in 2020.
Prefers morning appointments.
Her sister has recovered from a dislocated finger.


## 1.47 ('s2_atria_bleed', 'htn', 'negation', 'easy') templates=train

RULE: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 30 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.
CONDITION: hypertension
CLAIMS: s = 'The hypertension criterion contributes 0 points.' | s' = 'The hypertension criterion contributes 1 point.'

BASE (answer s):
Adult man.
Atrial fibrillation; a decision on warfarin is pending.
Age today: 69 years.
Retinal vessels look healthy on fundoscopy.
Hgb today: 14.1 g/dL.
eGFR today: 93 mL/min/1.73 m2.
Listens to podcasts.

FLIP (answer s'): -Retinal vessels look healthy on fundoscopy. | +Hypertension, treated with amlodipine.

NEAR (answer s): -Retinal vessels look healthy on fundoscopy. | +Denies hypertension, past or present.

MISSING (answer neither (undetermined)): -Retinal vessels look healthy on fundoscopy. | +Hypertension: not documented in the records available.

PRES (answer s): full text
Male patient.
Atrial fibrillation; a decision on warfarin is pending.
Listens to podcasts.
This morning's blood test shows an eGFR of 93 mL/min/1.73 m2.
No left ventricular hypertrophy on the echocardiogram.
Age at this assessment: 69 years.
Blood count today: Hgb 14.1 g/dL.


## 1.48 ('gs243', 'c1', 'numeric', 'long') templates=test

RULE: For early Lyme disease, prescribe doxycycline. If the current serum potassium is above 4.5 mmol/L or the patient has ever had coronary artery disease (current or past), prescribe amoxicillin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe doxycycline.' | s' = 'Prescribe amoxicillin.'

BASE (answer s):
Female patient of 61 years.
Erythema migrans rash ten days after a tick bite.
Pupils equal and reactive to light.
Owns a bicycle.
Chest pain on exertion: none reported.
Her friend wears contact lenses.
Current serum potassium 3.5 mmol/L.
Zinc of 85 mcg/dL in 2022.
Sleeps seven hours a night.
Enjoys board games.
Has two cats.
Her friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2006.
Paints watercolors as a hobby.
Plays the piano.
Uses sunscreen in summer.
In 2010, folate was 12 ng/mL.
Prefers to be addressed by first name.
Photographs local wildlife.
Drives a car.
Prefers morning appointments.
Knits as a hobby.
Lives in a second-floor apartment.
Sees a dentist yearly.

FLIP (answer s'): -Current serum potassium 3.5 mmol/L. | +Current serum potassium 5.3 mmol/L.

NEAR (answer s): -Current serum potassium 3.5 mmol/L. | +Current serum potassium 4.3 mmol/L.

MISSING (answer neither (undetermined)): -Current serum potassium 3.5 mmol/L.

PRES (answer s): full text
Woman of 61 years.
Erythema migrans rash ten days after a tick bite.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Drives a car.
Has two cats.
Her friend lives with psoriasis.
Prefers to be addressed by first name.
Latest potassium result: 3.5 mmol/L.
Lives in a second-floor apartment.
Enjoys board games.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2022.
Plays the piano.
Knits as a hobby.
Her friend wears contact lenses.
Climbs two flights of stairs without symptoms.
Sees a dentist yearly.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2006.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Photographs local wildlife.
In 2010, folate was 12 ng/mL.


## 1.49 ('gs044', 'c2', 'subject', 'easy') templates=train

RULE: For an acute gout flare, prescribe colchicine. If the patient is allergic to penicillin and the patient currently has a mechanical heart valve, prescribe prednisone instead.
CONDITION: mechanical heart valve
CLAIMS: s = 'Prescribe colchicine.' | s' = 'Prescribe prednisone.'

BASE (answer s):
44-year-old woman.
Acute gout flare of the right first metatarsophalangeal joint.
Penicillin triggers an allergic reaction with wheezing in this patient.
Drinks alcohol occasionally.

FLIP (answer s'): +Mechanical heart valve in the mitral position.

NEAR (answer s): +Her neighbor has a mechanical heart valve and needs regular clotting tests.

MISSING (answer neither (undetermined)): +Mechanical heart valve: not recorded.

PRES (answer s): full text
Patient: female, 44 years.
Acute gout flare of the right first metatarsophalangeal joint.
Allergic to penicillin (urticaria).
Drinks alcohol occasionally.


## 1.50 ('uti_sulfa', 'sulfa', 'time', 'long') templates=test

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient is allergic to sulfonamide antibiotics, prescribe nitrofurantoin instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Woman of 40 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Her wife sprained a thumb last month.
Has two cats.
Her wife has recovered from a dislocated finger.
Paints watercolors as a hobby.
Photographs local wildlife.
In 2024, lipase was 30 U/L.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2013.
In 2019, folate was 12 ng/mL.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Her sister has a lazy eye.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Current drug allergies: none.
Knits as a hobby.
Uses sunscreen in summer.

FLIP (answer s'): -Current drug allergies: none. | +Develops hives whenever given sulfonamide antibiotics.

NEAR (answer s): -Current drug allergies: none. | +Had a sulfa antibiotic allergy as an infant that was outgrown long ago.

MISSING (answer neither (undetermined)): -Current drug allergies: none. | +Sulfonamide allergy: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 40 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Her wife has recovered from a dislocated finger.
Her wife sprained a thumb last month.
Prefers morning appointments.
In 2019, folate was 12 ng/mL.
Paints watercolors as a hobby.
Has two cats.
Prefers to be addressed by first name.
Medication allergies: none at present.
Teeth in good repair.
Uses sunscreen in summer.
Knits as a hobby.
Lives in a second-floor apartment.
Her sister has a lazy eye.
In 2024, lipase was 30 U/L.
Pupils equal and reactive to light.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2013.
Sees a dentist yearly.


## 1.51 ('gs051', 'c1', 'boundary', 'long') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the current serum potassium is above 4.5 mmol/L, prescribe clindamycin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Female, 75 years.
Spreading redness and warmth of the right shin for two days.
TSH 1.6 mIU/L in 2015.
Uses public transport.
Her husband is being treated for eczema.
Speaks English and Spanish.
Non-smoker.
Has a pet dog.
Watches football on weekends.
Her housemate is nearsighted.
Nails normal.
Phosphate 3.6 mg/dL in 2008.
Wears a seat belt when driving.
Enjoys gardening.
Magnesium 2.0 mg/dL in 2008.
Enjoys cooking.
Serum calcium 9.4 mg/dL in 2023.
Potassium measured at this assessment is 4.0 mmol/L.
Her brother-in-law has a chipped front tooth.
Grows tomatoes in the garden.
Writes with the right hand.
Her husband wears hearing aids.

FLIP (answer s'): -Potassium measured at this assessment is 4.0 mmol/L. | +Potassium measured at this assessment is 5.0 mmol/L.

NEAR (answer s): -Potassium measured at this assessment is 4.0 mmol/L. | +Potassium measured at this assessment is 4.5 mmol/L.

MISSING (answer neither (undetermined)): -Potassium measured at this assessment is 4.0 mmol/L.

PRES (answer s): full text
Patient: female, 75 years.
Spreading redness and warmth of the right shin for two days.
Wears a seat belt when driving.
Enjoys gardening.
Her brother-in-law has a chipped front tooth.
Her housemate is nearsighted.
Non-smoker.
Writes with the right hand.
Serum calcium 9.4 mg/dL in 2023.
Nails normal.
Phosphate 3.6 mg/dL in 2008.
Magnesium 2.0 mg/dL in 2008.
Enjoys cooking.
TSH 1.6 mIU/L in 2015.
Watches football on weekends.
Labs this morning: potassium 4.0 mmol/L.
Her husband is being treated for eczema.
Uses public transport.
Speaks English and Spanish.
Grows tomatoes in the garden.
Has a pet dog.
Her husband wears hearing aids.


## 1.52 ('gs067', 'c2', 'negation', 'easy') templates=test

RULE: For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the patient has active cancer; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current heart rate is 109/min or more.
CONDITION: diabetes in the family
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Woman of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Plays the piano.
Has metastatic lung cancer, receiving palliative treatment.
Random glucose 92 mg/dL.
Current heart rate 97/min.

FLIP (answer s'): -Random glucose 92 mg/dL. | +Her father is diabetic.

NEAR (answer s): -Random glucose 92 mg/dL. | +Has never had diabetes.

MISSING (answer neither (undetermined)): -Random glucose 92 mg/dL. | +Diabetes in the family: unknown.

PRES (answer s): full text
Female patient of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Heart rate now 97/min on the monitor.
Has melanoma skin cancer and is receiving treatment for it.
HbA1c 5.3% at a routine check.
Plays the piano.


## 1.53 ('gs161', 'c2', 'numeric', 'easy') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient is allergic to penicillin or the age of the patient is 65 years or more, prescribe intermittent pneumatic compression instead.
CONDITION: age at least 65
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Male patient.
Admitted for community-acquired pneumonia; immobile.
Not allergic to any antibiotics.
Keeps a step counter.
Plays chess online.
Enjoys cooking.
Age at this assessment: 59 years.
Speaks English and Spanish.

FLIP (answer s'): -Age at this assessment: 59 years. | +Age at this assessment: 71 years.

NEAR (answer s): -Age at this assessment: 59 years. | +Age at this assessment: 62 years.

MISSING (answer neither (undetermined)): -Age at this assessment: 59 years.

PRES (answer s): full text
Sex: male.
Admitted for community-acquired pneumonia; immobile.
No beta-lactam allergy.
Age 59 years, calculated today from the date of birth.
Plays chess online.
Keeps a step counter.
Speaks English and Spanish.
Enjoys cooking.


## 1.54 ('gs088', 'c1', 'subject', 'easy') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. Score 1 point if the patient is currently taking warfarin; 3 points if the patient has ever had asthma (current or past); 1 point if the patient has new confusion. If the score is 4 or more, prescribe sitagliptin instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Woman of 68 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Anticoagulant therapy: none at present.
Lives in a second-floor apartment.
Asthma in the early school years, outgrown long ago.
Gives a clear account of the illness.
Plays the piano.

FLIP (answer s'): -Anticoagulant therapy: none at present. | +Currently on warfarin, prescribed by the cardiology clinic.

NEAR (answer s): -Anticoagulant therapy: none at present. | +Her roommate is anticoagulated with warfarin.

MISSING (answer neither (undetermined)): -Anticoagulant therapy: none at present. | +Warfarin: unknown.

PRES (answer s): full text
Female patient of 68 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Formerly had asthma in elementary school; well for many years without inhalers.
Current anticoagulants: none.
Plays the piano.
Lives in a second-floor apartment.
Speech clear; follows commands.


## 1.55 ('s1_psi', 'bun', 'time', 'superseded') templates=train

RULE: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 30 mg/dL or more. Age, sex and other items of the index are not part of this question.
CONDITION: blood urea nitrogen at least 30
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 20 points.'

BASE (answer s):
Male, 48 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Blood urea nitrogen was 24 mg/dL yesterday, before today's repeat.
BUN at this assessment: 17 mg/dL.
Plays chess online.
Arterial pH on today's blood gas: 7.40.
Takes no diuretics.
Lives on a quiet street.
Drinks plenty of water.

FLIP (answer s'): -BUN at this assessment: 17 mg/dL. | +BUN at this assessment: 60 mg/dL.

NEAR (answer s): -Blood urea nitrogen was 24 mg/dL yesterday, before today's repeat. | +Blood urea nitrogen was 46 mg/dL yesterday, before today's repeat.

MISSING (answer neither (undetermined)): -Blood urea nitrogen was 24 mg/dL yesterday, before today's repeat. | -BUN at this assessment: 17 mg/dL.

PRES (answer s): full text
A 48-year-old man.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
BUN on today's chemistry panel: 17 mg/dL.
Plays chess online.
Drinks plenty of water.
Blood urea nitrogen of 24 mg/dL measured yesterday was replaced by a repeat measurement.
Lives on a quiet street.
Arterial pH 7.40 on the blood gas taken at this assessment.
Recent echocardiogram normal.


## 1.56 ('gs065', 'c3', 'boundary', 'long') templates=test

RULE: For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the patient has ever had angioedema (current or past); the patient has ever had asthma (current or past); the current serum potassium is above 5.0 mmol/L.
CONDITION: serum potassium above 5.0
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Man of 51 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Owns a bicycle.
Prefers to be addressed by first name.
His roommate wears contact lenses.
Latest potassium result: 3.7 mmol/L.
Drives a car.
Has two cats.
Prefers morning appointments.
Enjoys board games.
An episode of angioedema years ago, with full recovery.
Knits as a hobby.
Teeth in good repair.
His sister burned a hand on a stove years ago.
Pupils equal and reactive to light.
Sees a dentist yearly.
Paints watercolors as a hobby.
Plays the piano.
In 2010, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2015.

FLIP (answer s'): -Latest potassium result: 3.7 mmol/L. | +Latest potassium result: 5.8 mmol/L.

NEAR (answer s): -Latest potassium result: 3.7 mmol/L. | +Latest potassium result: 5.0 mmol/L.

MISSING (answer neither (undetermined)): -Latest potassium result: 3.7 mmol/L.

PRES (answer s): full text
Male patient of 51 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Free T4 of 1.2 ng/dL in 2015.
Pupils equal and reactive to light.
His roommate wears contact lenses.
Prefers morning appointments.
Owns a bicycle.
Drives a car.
Teeth in good repair.
Plays the piano.
Formerly had recurrent angioedema, in remission for many years now.
Current serum potassium 3.7 mmol/L.
Prefers to be addressed by first name.
Has two cats.
Sees a dentist yearly.
Enjoys board games.
In 2010, lipase was 30 U/L.
His sister burned a hand on a stove years ago.
Paints watercolors as a hobby.
Knits as a hobby.


## 1.57 ('gs247', 'c1', 'negation', 'easy') templates=train

RULE: For an acute gout flare, prescribe colchicine. If the patient currently has a venous thromboembolism, prescribe prednisone instead.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe colchicine.' | s' = 'Prescribe prednisone.'

BASE (answer s):
Female, 57 years.
Acute gout flare of the right first metatarsophalangeal joint.
Reads most evenings.
Vaccinations up to date.
Not on any blood thinners.

FLIP (answer s'): -Not on any blood thinners. | +On treatment for a deep vein thrombosis in the left leg.

NEAR (answer s): -Not on any blood thinners. | +No venous thromboembolism at any time, personally or among first-degree relatives.

MISSING (answer neither (undetermined)): -Not on any blood thinners. | +Information on current venous thromboembolism was not obtained.

PRES (answer s): full text
57-year-old woman.
Acute gout flare of the right first metatarsophalangeal joint.
Vaccinations up to date.
Reads most evenings.
No inherited clotting condition such as factor V Leiden.


## 1.58 ('gs223', 'c2', 'numeric', 'long') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current calf swelling compared with the other leg is 3.0 cm or more and the current platelet count is below 150 x10^9/L, prescribe aspirin plus clopidogrel instead.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Man of 42 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Prefers morning appointments.
His sister sprained a thumb last month.
Knits as a hobby.
Plays the piano.
Free T4 of 1.2 ng/dL in 2019.
Sees a dentist yearly.
Current platelet count 220 x10^9/L.
His father has recovered from a dislocated finger.
Enjoys board games.
During a checkup in 2006, total protein was 7.0 g/dL.
Current calf swelling 3.4 cm compared with the other leg.
In 2017, folate was 12 ng/mL.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Has two cats.
His sister has a lazy eye.
Pupils equal and reactive to light.

FLIP (answer s'): -Current platelet count 220 x10^9/L. | +Current platelet count 145 x10^9/L.

NEAR (answer s): -Current platelet count 220 x10^9/L. | +Current platelet count 153 x10^9/L.

MISSING (answer neither (undetermined)): -Current platelet count 220 x10^9/L.

PRES (answer s): full text
Male patient of 42 years.
Recovering on the ward after a myocardial infarction treated with a stent.
His sister has a lazy eye.
His sister sprained a thumb last month.
Prefers morning appointments.
In 2017, folate was 12 ng/mL.
Plays the piano.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2019.
During a checkup in 2006, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Calf swelling now amounts to 3.4 cm of extra girth in the larger calf.
Has two cats.
Knits as a hobby.
His father has recovered from a dislocated finger.
Lives in a second-floor apartment.
Platelet count now 220 x10^9/L.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Sees a dentist yearly.


## 1.59 ('gs108', 'c2', 'subject', 'easy') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had coronary artery disease (current or past) and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe amlodipine instead.
CONDITION: venous thromboembolism in the family
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
65-year-old man.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Wears a seat belt when driving.
No known blood clotting disorder.
Does crossword puzzles.
Reads most evenings.
Sings in a weekly choir.
Coronary artery disease, with angina when walking uphill.

FLIP (answer s'): -No known blood clotting disorder. | +On treatment for a deep vein thrombosis in the left leg.

NEAR (answer s): -No known blood clotting disorder. | +His housemate previously took blood thinners for a deep vein thrombosis.

MISSING (answer neither (undetermined)): -No known blood clotting disorder. | +Information on venous thromboembolism in the family was not obtained.

PRES (answer s): full text
A 65-year-old man.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sings in a weekly choir.
Wears a seat belt when driving.
Coronary artery disease, followed in cardiology clinic every six months.
Reads most evenings.
Not on any blood thinners.
Does crossword puzzles.


## 1.60 ('s1_news2_other', 'temp', 'time', 'easy') templates=test

RULE: NEWS2 (as used here, partial: only the stated band of each listed item): 3 points for a heart rate of 131/min or more; 3 points for a systolic blood pressure of 220 mmHg or more; 2 points for a temperature of 39.1 C or more; 2 points for current use of supplemental oxygen. Any other value of these items scores 0 here, and the other NEWS2 items are not part of this question. Only current findings count.
CONDITION: temperature at least 39.1
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 2 points.'

BASE (answer s):
Woman of 86 years.
Newly admitted to the medical ward with a chest infection.
Current systolic blood pressure 162 mmHg.
Plays the piano.
Temperature now 37.9 C (tympanic).
Records from 2009 list temperature at 36.5 C.
Heart rate now 62/min on the monitor.
Prefers to be addressed by first name.
Photographs local wildlife.

FLIP (answer s'): -Temperature now 37.9 C (tympanic). | +Temperature now 40.0 C (tympanic).

NEAR (answer s): -Records from 2009 list temperature at 36.5 C. | +Records from 2009 list temperature at 39.4 C.

MISSING (answer neither (undetermined)): -Temperature now 37.9 C (tympanic). | -Records from 2009 list temperature at 36.5 C.

PRES (answer s): full text
Female patient of 86 years.
Newly admitted to the medical ward with a chest infection.
Prefers to be addressed by first name.
Current temperature 37.9 C.
Current heart rate 62/min.
Observations now: blood pressure 162/101 mmHg.
Plays the piano.
Back in 2009, temperature measured 36.5 C.
Photographs local wildlife.


## 1.61 ('gs085', 'c2', 'boundary', 'easy') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had asthma (current or past) and the current ALT is above 200 U/L, prescribe fondaparinux instead.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Patient: male, 82 years.
First day after elective total hip replacement.
Previously had asthma in childhood; symptom-free and off inhalers for decades.
ALT today: 27 U/L.
Height 170 cm.
Collects postcards.

FLIP (answer s'): -ALT today: 27 U/L. | +ALT today: 358 U/L.

NEAR (answer s): -ALT today: 27 U/L. | +ALT today: 200 U/L.

MISSING (answer neither (undetermined)): -ALT today: 27 U/L.

PRES (answer s): full text
Male, 82 years.
First day after elective total hip replacement.
Childhood asthma, resolved by adolescence.
Height 170 cm.
Collects postcards.
Liver tests today: ALT 27 U/L.


## 1.62 ('gs110', 'c1', 'negation', 'easy') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the patient has had a major bleeding event at any time, prescribe aspirin plus clopidogrel instead.
CONDITION: bleeding history
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Male patient of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Paints watercolors as a hobby.
Bowel habit normal, without any blood in the stool.
Owns a bicycle.
Sleeps seven hours a night.

FLIP (answer s'): -Bowel habit normal, without any blood in the stool. | +Major bleed from the stomach at present, with hemoglobin falling.

NEAR (answer s): -Bowel habit normal, without any blood in the stool. | +Has never had a major bleed.

MISSING (answer neither (undetermined)): -Bowel habit normal, without any blood in the stool. | +Bleeding history: unknown.

PRES (answer s): full text
Man of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Owns a bicycle.
Examination shows no signs of blood loss.


## 1.63 ('gs182', 'c1', 'numeric', 'easy') templates=train

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current weight is below 67 kg and the patient is allergic to sulfonamide antibiotics, prescribe warfarin instead.
CONDITION: weight below 67
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
A 76-year-old woman.
Atrial fibrillation; anticoagulation indicated.
Enjoys cooking.
Hearing normal to conversation.
Listens to podcasts.
Weight 80 kg at this assessment.
Allergic to sulfa antibiotics (hives).
Bakes bread at home.

FLIP (answer s'): -Weight 80 kg at this assessment. | +Weight 57 kg at this assessment.

NEAR (answer s): -Weight 80 kg at this assessment. | +Weight 68 kg at this assessment.

MISSING (answer neither (undetermined)): -Weight 80 kg at this assessment.

PRES (answer s): full text
Patient: female, 76 years.
Atrial fibrillation; anticoagulation indicated.
Weight checked today on a calibrated scale: 80 kg.
Bakes bread at home.
Allergies: sulfa drugs (rash).
Listens to podcasts.
Hearing normal to conversation.
Enjoys cooking.


## 1.64 ('gs080', 'c1', 'subject', 'long') templates=test

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. Score 3 points if the patient is currently taking warfarin; 1 point if the patient currently has tender anterior cervical lymph nodes; 3 points if the patient has ever had a peptic ulcer (current or past). If the score is 7 or more, prescribe doxycycline instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Female patient of 75 years.
Productive cough and fever; consolidation on chest radiograph.
Free T4 of 1.2 ng/dL in 2013.
In 2013, lipase was 30 U/L.
Her friend wears contact lenses.
Her friend lives with psoriasis.
Duodenal ulcer years ago; recovered fully with treatment.
During a checkup in 2015, total protein was 7.0 g/dL.
Her friend has a lazy eye.
Current anticoagulants: none.
Plays the piano.
Her sister sprained a thumb last month.
Paints watercolors as a hobby.
Photographs local wildlife.
Tender, swollen lymph nodes in the front of the neck.
Has two cats.
Knits as a hobby.
Uses sunscreen in summer.
Sees a dentist yearly.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Teeth in good repair.
Pupils equal and reactive to light.

FLIP (answer s'): -Current anticoagulants: none. | +Anticoagulated with warfarin; INR checked monthly at the clinic.

NEAR (answer s): -Current anticoagulants: none. | +Her wife is on warfarin with monthly INR checks.

MISSING (answer neither (undetermined)): -Current anticoagulants: none. | +Warfarin: status unclear from the records at hand.

PRES (answer s): full text
Woman of 75 years.
Productive cough and fever; consolidation on chest radiograph.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Duodenal ulcer years ago; recovered fully with treatment.
Prefers morning appointments.
Knits as a hobby.
Has two cats.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Anterior cervical lymph nodes enlarged and tender to touch.
Sees a dentist yearly.
Her friend has a lazy eye.
Plays the piano.
In 2013, lipase was 30 U/L.
Her friend lives with psoriasis.
Her sister sprained a thumb last month.
Anticoagulant therapy: none at present.
Free T4 of 1.2 ng/dL in 2013.
Uses sunscreen in summer.
During a checkup in 2015, total protein was 7.0 g/dL.
Teeth in good repair.
Her friend wears contact lenses.
Photographs local wildlife.


## 1.65 ('gs196', 'c2', 'time', 'long') templates=train

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient currently has tonsillar exudate or the patient currently has tender anterior cervical lymph nodes, prescribe acetaminophen instead.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
A 45-year-old man.
Acute low back pain after lifting.
His partner had a splinter removed from a finger.
Enjoys cooking.
Grows tomatoes in the garden.
His brother-in-law has a chipped front tooth.
Ferritin 60 ng/mL in 2010.
Lives on a quiet street.
Hearing normal to conversation.
Wears a seat belt when driving.
Neck soft and nontender.
Speaks English and Spanish.
Keeps a step counter.
Plays chess online.
Nails normal.
Reads most evenings.
Uses reading glasses for small print.
TSH 1.6 mIU/L in 2009.
Vaccinations up to date.
His partner has a fear of heights.
Bakes bread at home.
Uses public transport.
His housemate completed physical therapy for a shoulder injury.

FLIP (answer s'): -Neck soft and nontender. | +A single tender anterior cervical lymph node on the left.

NEAR (answer s): -Neck soft and nontender. | +Tender anterior cervical lymph nodes during tonsillitis in 2022, since resolved.

MISSING (answer neither (undetermined)): -Neck soft and nontender. | +Tender cervical lymph nodes: not asked about.

PRES (answer s): full text
Patient: male, 45 years.
Acute low back pain after lifting.
Speaks English and Spanish.
Nails normal.
Enjoys cooking.
Vaccinations up to date.
His partner had a splinter removed from a finger.
His housemate completed physical therapy for a shoulder injury.
Bakes bread at home.
Keeps a step counter.
His brother-in-law has a chipped front tooth.
Ferritin 60 ng/mL in 2010.
Uses public transport.
Grows tomatoes in the garden.
TSH 1.6 mIU/L in 2009.
His partner has a fear of heights.
Wears a seat belt when driving.
Uses reading glasses for small print.
No tender swellings in the neck.
Plays chess online.
Hearing normal to conversation.
Lives on a quiet street.
Reads most evenings.


## 1.66 ('any_gout', 'egfr', 'boundary', 'long') templates=test

RULE: For an acute gout flare, prescribe naproxen. If the patient has an active peptic ulcer or the current eGFR is below 30 mL/min/1.73 m2, prescribe colchicine instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe colchicine.'

BASE (answer s):
Woman of 49 years.
Acute gout flare of the left knee.
Lives in a second-floor apartment.
Her wife wears contact lenses.
Owns a bicycle.
Has two cats.
eGFR now 93 mL/min/1.73 m2.
Zinc of 85 mcg/dL in 2005.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Sees a dentist yearly.
Prefers morning appointments.
Photographs local wildlife.
Drives a car.
Her friend has a lazy eye.
Abdomen soft and non-tender.
Her wife burned a hand on a stove years ago.
Her uncle sprained a thumb last month.
During a checkup in 2008, total protein was 7.0 g/dL.
Enjoys board games.
Uses sunscreen in summer.

FLIP (answer s'): -eGFR now 93 mL/min/1.73 m2. | +eGFR now 21 mL/min/1.73 m2.

NEAR (answer s): -eGFR now 93 mL/min/1.73 m2. | +eGFR now 30 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -eGFR now 93 mL/min/1.73 m2.

PRES (answer s): full text
Female patient of 49 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Her wife burned a hand on a stove years ago.
Appetite good; no indigestion.
Current eGFR 93 mL/min/1.73 m2.
Enjoys board games.
Sleeps seven hours a night.
Drives a car.
Owns a bicycle.
Has two cats.
Her wife wears contact lenses.
Prefers morning appointments.
During a checkup in 2008, total protein was 7.0 g/dL.
Her uncle sprained a thumb last month.
Her friend has a lazy eye.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2005.
Photographs local wildlife.
Lives in a second-floor apartment.
Uses sunscreen in summer.


## 1.67 ('gs235', 'c2', 'negation', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient has ever had diabetes (current or past); 3 points if the patient has new confusion; 2 points if the patient is allergic to penicillin; 2 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time. If the score is 6 or more, prescribe a progestin-only pill instead.
CONDITION: new confusion
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
25-year-old woman.
Requests contraception.
Colorectal cancer in 2024, treated with chemotherapy and radiation; scans clear since.
Penicillin triggers an allergic reaction with wheezing in this patient.
Wears a seat belt when driving.
Plays chess online.
No excessive thirst or urination.
Listens to podcasts.
Alert and attentive.
Drinks two cups of coffee a day.

FLIP (answer s'): -Alert and attentive. | +Confused on arrival, a sudden change from baseline.

NEAR (answer s): -Alert and attentive. | +No confusion, according to the nursing staff.

MISSING (answer neither (undetermined)): -Alert and attentive. | +New confusion: not documented in the records available.

PRES (answer s): full text
Female, 25 years.
Requests contraception.
Bowel cancer in 2024; all treatment completed and the patient was declared cancer-free.
Listens to podcasts.
Wears a seat belt when driving.
Allergic to penicillin (urticaria).
Drinks two cups of coffee a day.
Urine dipstick shows no sugar.
Plays chess online.
Memory and concentration normal on bedside testing.


## 1.68 ('gs131', 'c2', 'numeric', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If at least two of the following apply, prescribe naproxen with omeprazole instead: the patient has ever had a venous thromboembolism (current or past); the current systolic blood pressure is below 100 mmHg; the patient has ever had asthma (current or past).
CONDITION: systolic blood pressure below 100
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Woman of 51 years.
Hip osteoarthritis with pain on walking.
Current systolic blood pressure 119 mmHg.
Inhaler use: none.
Sees a dentist yearly.
Has two cats.
Pulmonary embolism years ago, treated for six months.
Teeth in good repair.
Owns a bicycle.

FLIP (answer s'): -Current systolic blood pressure 119 mmHg. | +Current systolic blood pressure 79 mmHg.

NEAR (answer s): -Current systolic blood pressure 119 mmHg. | +Current systolic blood pressure 101 mmHg.

MISSING (answer neither (undetermined)): -Current systolic blood pressure 119 mmHg.

PRES (answer s): full text
Female patient of 51 years.
Hip osteoarthritis with pain on walking.
Sees a dentist yearly.
Observations now: blood pressure 119/75 mmHg.
Lungs clear, without wheeze or prolonged expiration.
Owns a bicycle.
Pulmonary embolism years ago, treated for six months.
Has two cats.
Teeth in good repair.


## 1.69 ('gs130', 'c2', 'subject', 'long') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient is allergic to penicillin, prescribe naproxen with omeprazole instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Male, 66 years.
Hip osteoarthritis with pain on walking.
Lives on a quiet street.
Drinks plenty of water.
Enjoys cooking.
Bakes bread at home.
Drinks alcohol occasionally.
Nails normal.
Speaks English and Spanish.
Hearing normal to conversation.
His husband has a broken finger in a splint.
His housemate wears hearing aids.
Vitamin B12 450 pg/mL in 2014.
Phosphate 3.6 mg/dL in 2016.
Has a pet dog.
Vitamin D 38 ng/mL in 2006 (wellness visit).
Does crossword puzzles.
Bowel cancer, midway through a course of chemotherapy.
His brother-in-law is left-handed.
Reads most evenings.
His housemate completed physical therapy for a shoulder injury.

FLIP (answer s'): +Allergies: penicillin (rash).

NEAR (answer s): +His husband gets an itchy rash from penicillin.

MISSING (answer neither (undetermined)): +Penicillin allergy: not asked about.

PRES (answer s): full text
A 66-year-old man.
Hip osteoarthritis with pain on walking.
Does crossword puzzles.
His housemate completed physical therapy for a shoulder injury.
Drinks alcohol occasionally.
Enjoys cooking.
Hearing normal to conversation.
Drinks plenty of water.
Has colon cancer and is receiving treatment from an oncologist.
Reads most evenings.
Lives on a quiet street.
Has a pet dog.
His brother-in-law is left-handed.
Vitamin D 38 ng/mL in 2006 (wellness visit).
Bakes bread at home.
Vitamin B12 450 pg/mL in 2014.
Phosphate 3.6 mg/dL in 2016.
His housemate wears hearing aids.
His husband has a broken finger in a splint.
Nails normal.
Speaks English and Spanish.


## 1.70 ('gs168', 'c2', 'time', 'easy') templates=test

RULE: For early Lyme disease, prescribe doxycycline. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time or the current weight is 60 kg or less, prescribe amoxicillin instead.
CONDITION: weight at or below 60
CLAIMS: s = 'Prescribe doxycycline.' | s' = 'Prescribe amoxicillin.'

BASE (answer s):
Female patient of 67 years.
Erythema migrans rash ten days after a tick bite.
Latest weight 91 kg.
Pupils equal and reactive to light.
Enjoys board games.
Drives a car.
Back in 2012, weight measured 87 kg.
Coagulation tests normal on recent bloodwork.

FLIP (answer s'): -Latest weight 91 kg. | +Latest weight 53 kg.

NEAR (answer s): -Back in 2012, weight measured 87 kg. | +Back in 2012, weight measured 58 kg.

MISSING (answer neither (undetermined)): -Latest weight 91 kg. | -Back in 2012, weight measured 87 kg.

PRES (answer s): full text
Woman of 67 years.
Erythema migrans rash ten days after a tick bite.
Pupils equal and reactive to light.
Drives a car.
Current weight 91 kg.
Enjoys board games.
Records from 2012 list weight at 87 kg.
Varicose veins: none seen.


## 1.71 ('gs164', 'c3', 'boundary', 'long') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. Score 1 point if the current serum creatinine is above 2.0 mg/dL; 1 point if the patient has ever had heparin-induced thrombocytopenia (current or past); 2 points if the current platelet count is below 150 x10^9/L; 1 point if the current ALT is above 200 U/L. If the score is 3 or more, prescribe acetaminophen instead.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: male, 64 years.
Knee osteoarthritis with pain on walking.
Blood panel at this assessment: creatinine 1.5 mg/dL.
ALT on blood drawn this morning: 303 U/L.
Non-smoker.
Serum calcium 9.4 mg/dL in 2016.
Uses a smartphone for reminders.
His brother-in-law has a chipped front tooth.
His cousin is nearsighted.
Drinks plenty of water.
Height 170 cm.
His housemate has a stutter.
Grows tomatoes in the garden.
Vitamin D 38 ng/mL in 2016 (wellness visit).
Eats a varied diet.
His aunt is left-handed.
Complete blood count today: platelets 285 x10^9/L.
Sodium 140 mmol/L in 2012.
Reads most evenings.
Bicarbonate 26 mmol/L in 2018 (annual physical).

FLIP (answer s'): -Complete blood count today: platelets 285 x10^9/L. | +Complete blood count today: platelets 129 x10^9/L.

NEAR (answer s): -Complete blood count today: platelets 285 x10^9/L. | +Complete blood count today: platelets 150 x10^9/L.

MISSING (answer neither (undetermined)): -Complete blood count today: platelets 285 x10^9/L.

PRES (answer s): full text
A 64-year-old man.
Knee osteoarthritis with pain on walking.
Sodium 140 mmol/L in 2012.
His aunt is left-handed.
Eats a varied diet.
Vitamin D 38 ng/mL in 2016 (wellness visit).
Grows tomatoes in the garden.
Bicarbonate 26 mmol/L in 2018 (annual physical).
Platelet count today: 285 x10^9/L.
His housemate has a stutter.
Drinks plenty of water.
Uses a smartphone for reminders.
Serum calcium 9.4 mg/dL in 2016.
Height 170 cm.
ALT 303 U/L on today's labs.
Non-smoker.
His brother-in-law has a chipped front tooth.
Serum creatinine today: 1.5 mg/dL.
His cousin is nearsighted.
Reads most evenings.


## 1.72 ('gs114', 'c2', 'negation', 'easy') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. Score 2 points if the patient has ever had coronary artery disease (current or past); 1 point if the patient has ever had a venous thromboembolism (current or past); 2 points if the patient currently has tender anterior cervical lymph nodes. If the score is 5 or more, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: venous thromboembolism
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Female patient of 67 years.
Suspected chest infection; assessed on the medical ward.
Tender, swollen lymph nodes in the front of the neck.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Has two cats.

FLIP (answer s'): +Ongoing treatment for venous thrombosis of the left arm.

NEAR (answer s): +Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.

MISSING (answer neither (undetermined)): +Venous thromboembolism: unknown.

PRES (answer s): full text
Woman of 67 years.
Suspected chest infection; assessed on the medical ward.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Anterior cervical lymph nodes enlarged and tender to touch.
Has two cats.


## 1.73 ('c1_nitrofurantoin', 'egfr', 'numeric', 'long') templates=train

RULE: For acute cystitis, prescribe nitrofurantoin. If the current eGFR is below 45 mL/min/1.73 m2, prescribe fosfomycin instead.
CONDITION: eGFR below 45
CLAIMS: s = 'Prescribe nitrofurantoin.' | s' = 'Prescribe fosfomycin.'

BASE (answer s):
A 37-year-old woman.
Burning on passing urine and urinary frequency for three days; no fever or flank pain.
Height 170 cm.
Magnesium 2.0 mg/dL in 2012.
Enjoys cooking.
Albumin 4.1 g/dL in 2007 (routine blood test).
Wears a seat belt when driving.
Watches football on weekends.
Her brother-in-law is left-handed.
Uses reading glasses for small print.
Serum calcium 9.4 mg/dL in 2017.
Her cousin wears hearing aids.
Her brother has a fear of heights.
Drinks two cups of coffee a day.
Her mother has a broken finger in a splint.
Non-smoker.
Reads most evenings.
Vitamin B12 450 pg/mL in 2017.
eGFR 60 mL/min/1.73 m2 on today's labs.
Vaccinations up to date.

FLIP (answer s'): -eGFR 60 mL/min/1.73 m2 on today's labs. | +eGFR 28 mL/min/1.73 m2 on today's labs.

NEAR (answer s): -eGFR 60 mL/min/1.73 m2 on today's labs. | +eGFR 47 mL/min/1.73 m2 on today's labs.

MISSING (answer neither (undetermined)): -eGFR 60 mL/min/1.73 m2 on today's labs.

PRES (answer s): full text
Female, 37 years.
Burning on passing urine and urinary frequency for three days; no fever or flank pain.
Drinks two cups of coffee a day.
Uses reading glasses for small print.
Albumin 4.1 g/dL in 2007 (routine blood test).
Her mother has a broken finger in a splint.
Wears a seat belt when driving.
Her brother has a fear of heights.
Her brother-in-law is left-handed.
Height 170 cm.
Watches football on weekends.
Her cousin wears hearing aids.
Vitamin B12 450 pg/mL in 2017.
Reads most evenings.
Non-smoker.
Magnesium 2.0 mg/dL in 2012.
Serum calcium 9.4 mg/dL in 2017.
Vaccinations up to date.
Enjoys cooking.
eGFR today: 60 mL/min/1.73 m2.


## 1.74 ('gs135', 'c1', 'subject', 'long') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient currently has tonsillar exudate and the patient has had a major bleeding event at any time, prescribe warfarin instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Female patient of 65 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
Teeth in good repair.
Sleeps seven hours a night.
Uses sunscreen in summer.
Her friend has a lazy eye.
Major intracranial bleed after a fall years ago, with full recovery.
Her wife has recovered from a dislocated finger.
Sees a dentist yearly.
Has two cats.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2013.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Plays the piano.
During a checkup in 2008, total protein was 7.0 g/dL.

FLIP (answer s'): +Tonsils swollen and coated with yellow exudate.

NEAR (answer s): +Her friend currently has a throat infection with tonsillar exudate.

MISSING (answer neither (undetermined)): +Tonsillar exudate: unknown.

PRES (answer s): full text
Woman of 65 years.
Atrial fibrillation; anticoagulation indicated.
Zinc of 85 mcg/dL in 2013.
Lives in a second-floor apartment.
Major intracranial bleed after a fall years ago, with full recovery.
Sees a dentist yearly.
Has two cats.
Her wife has recovered from a dislocated finger.
Her friend has a lazy eye.
Prefers morning appointments.
During a checkup in 2008, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Sleeps seven hours a night.
Plays the piano.


## 1.75 ('gs017', 'c2', 'time', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time or the patient is currently taking aspirin, prescribe amlodipine instead.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
A 45-year-old woman.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Hearing normal to conversation.
Drinks alcohol occasionally.
Ferritin 60 ng/mL in 2018.
Reads most evenings.
Uses a smartphone for reminders.
Her neighbor is nearsighted.
Abdomen soft, with no masses on examination.
Chloride 103 mmol/L in 2013.
Plays chess online.
Watches football on weekends.
Writes with the right hand.
Her brother is left-handed.
Uses public transport.
Nails normal.
Speaks English and Spanish.
Drinks two cups of coffee a day.
Drinks plenty of water.
Takes no antiplatelet medicines.
Listens to podcasts.
Enjoys cooking.

FLIP (answer s'): -Takes no antiplatelet medicines. | +Active medications today include aspirin 81 mg once daily.

NEAR (answer s): -Takes no antiplatelet medicines. | +Completed a six-week course of aspirin after ankle surgery in 2012.

MISSING (answer neither (undetermined)): -Takes no antiplatelet medicines. | +Information on aspirin use was not obtained.

PRES (answer s): full text
Female, 45 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Her brother is left-handed.
Drinks alcohol occasionally.
Watches football on weekends.
Plays chess online.
Bowel habit regular.
Hearing normal to conversation.
Nails normal.
Her neighbor is nearsighted.
Writes with the right hand.
Drinks two cups of coffee a day.
Ferritin 60 ng/mL in 2018.
Drinks plenty of water.
Uses public transport.
Listens to podcasts.
Not on any antiplatelet medication.
Speaks English and Spanish.
Reads most evenings.
Enjoys cooking.
Uses a smartphone for reminders.
Chloride 103 mmol/L in 2013.
