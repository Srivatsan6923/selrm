# Audit sample 1


## 1.1 ('rcri', 'cr', 'boundary', 'long') templates=train

RULE: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 2.0 mg/dL. Other items are not part of this question.
CONDITION: creatinine above 2.0
CLAIMS: s = 'The creatinine criterion contributes 0 points.' | s' = 'The creatinine criterion contributes 1 point.'

BASE (answer s):
57 years old, male.
Preoperative assessment before elective colectomy.
Plays chess online.
Creatinine 1.2 mg/dL on this morning's labs.
Jugular venous pressure not raised.
TSH 1.6 mIU/L in 2015.
Uses a smartphone for reminders.
His coworker is nearsighted.
Keeps houseplants.
Ferritin 60 ng/mL in 2005.
Speech fluent and face symmetric.
His cousin has a stutter.
Height 170 cm.
Watches football on weekends.
Reads most evenings.
Magnesium 2.0 mg/dL in 2014.
Bakes bread at home.
Has a pet dog.
Sings in a weekly choir.
Vitamin B12 450 pg/mL in 2010.
Enjoys cooking.
Takes no medicines for angina.
Nails normal.

FLIP (answer s'): -Creatinine 1.2 mg/dL on this morning's labs. | +Creatinine 4.0 mg/dL on this morning's labs.

NEAR (answer s): -Creatinine 1.2 mg/dL on this morning's labs. | +Creatinine 2.0 mg/dL on this morning's labs.

MISSING (answer neither (undetermined)): -Creatinine 1.2 mg/dL on this morning's labs.

PRES (answer s): full text
57-year-old man.
Preoperative assessment before elective colectomy.
TSH 1.6 mIU/L in 2015.
Vitamin B12 450 pg/mL in 2010.
Reads most evenings.
Bakes bread at home.
Sings in a weekly choir.
Enjoys cooking.
Keeps houseplants.
His coworker is nearsighted.
Uses a smartphone for reminders.
His cousin has a stutter.
Speech fluent and face symmetric.
Takes no medicines for angina.
Ferritin 60 ng/mL in 2005.
Magnesium 2.0 mg/dL in 2014.
Serum creatinine today: 1.2 mg/dL.
Watches football on weekends.
Jugular venous pressure not raised.
Plays chess online.
Has a pet dog.
Height 170 cm.
Nails normal.


## 1.2 ('gs095', 'c1', 'negation', 'long') templates=test

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time or the current white cell count is above 12.0 x10^9/L, prescribe amlodipine instead.
CONDITION: coronary artery disease in the patient or a first-degree relative
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Woman of 68 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Free T4 of 1.2 ng/dL in 2021.
Sees a dentist yearly.
Her sister has a lazy eye.
Her roommate burned a hand on a stove years ago.
Chest pain on exertion: none reported.
Enjoys board games.
Her sister sprained a thumb last month.
Plays the piano.
In 2018, lipase was 30 U/L.
Sleeps seven hours a night.
Photographs local wildlife.
Current white cell count 4.8 x10^9/L.
During a checkup in 2014, total protein was 7.0 g/dL.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.

FLIP (answer s'): -Chest pain on exertion: none reported. | +Her sister has known coronary artery disease.

NEAR (answer s): -Chest pain on exertion: none reported. | +Has never had coronary artery disease.

MISSING (answer neither (undetermined)): -Chest pain on exertion: none reported. | +Coronary artery disease in the patient or a first-degree relative: unknown.

PRES (answer s): full text
Female patient of 68 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Teeth in good repair.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Chest pain on exertion: none reported.
Free T4 of 1.2 ng/dL in 2021.
Enjoys board games.
During a checkup in 2014, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Latest WBC is 4.8 x10^9/L.
In 2018, lipase was 30 U/L.
Plays the piano.
Sleeps seven hours a night.
Her sister sprained a thumb last month.
Her sister has a lazy eye.
Photographs local wildlife.
Her roommate burned a hand on a stove years ago.
Pupils equal and reactive to light.


## 1.3 ('sirs', 'hr', 'numeric', 'long') templates=train

RULE: SIRS criteria (as used here, partial): 1 point each for temperature above 38.0 C; heart rate above 90/min; respiratory rate above 20/min; white cell count above 12.0 x10^9/L. Only current findings count.
CONDITION: heart rate above 90
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 1 point.'

BASE (answer s):
44 years old, female.
Productive cough for three days; assessed in the emergency department.
Respiratory rate, counted over a full minute today, is 12/min.
Albumin 4.1 g/dL in 2014 (routine blood test).
Her aunt completed physical therapy for a shoulder injury.
White cell count today: 9.2 x10^9/L.
Wears a seat belt when driving.
Sodium 140 mmol/L in 2023.
Heart rate today: 68/min.
Lives on a quiet street.
Total bilirubin 0.6 mg/dL in 2006.
Has a pet dog.
Her aunt has a stutter.
Listens to podcasts.
Drinks plenty of water.
Temperature 37.0 C at this assessment.
Bakes bread at home.
Watches football on weekends.
Feeds birds in the backyard.
Speaks English and Spanish.
Eats a varied diet.
Vitamin B12 450 pg/mL in 2018.
Wears glasses when driving.

FLIP (answer s'): -Heart rate today: 68/min. | +Heart rate today: 137/min.

NEAR (answer s): -Heart rate today: 68/min. | +Heart rate today: 86/min.

MISSING (answer neither (undetermined)): -Heart rate today: 68/min.

PRES (answer s): full text
44-year-old woman.
Productive cough for three days; assessed in the emergency department.
Heart rate 68/min at rest this morning.
Drinks plenty of water.
Has a pet dog.
Eats a varied diet.
Wears glasses when driving.
Feeds birds in the backyard.
Lives on a quiet street.
Respiratory rate 12/min this morning.
Wears a seat belt when driving.
Her aunt completed physical therapy for a shoulder injury.
Watches football on weekends.
Speaks English and Spanish.
Her aunt has a stutter.
Albumin 4.1 g/dL in 2014 (routine blood test).
Temperature today: 37.0 C.
WBC 9.2 x10^9/L on today's sample.
Listens to podcasts.
Sodium 140 mmol/L in 2023.
Bakes bread at home.
Vitamin B12 450 pg/mL in 2018.
Total bilirubin 0.6 mg/dL in 2006.


## 1.4 ('curb65', 'confusion', 'subject', 'long') templates=test

RULE: CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
CONDITION: confusion
CLAIMS: s = 'The confusion criterion contributes 0 points.' | s' = 'The confusion criterion contributes 1 point.'

BASE (answer s):
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Her roommate has a lazy eye.
Prefers to be addressed by first name.
Current systolic blood pressure 109 mmHg.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Knits as a hobby.
Enjoys board games.
Drives a car.
Her wife lives with psoriasis.
Her father sprained a thumb last month.
Uses sunscreen in summer.
Blood urea nitrogen 14 mg/dL on the current labs.
Prefers morning appointments.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Current age 42 years.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2010.
In 2015, lipase was 30 U/L.
Current respiratory rate 19/min.
Gives a clear account of the illness.

FLIP (answer s'): -Gives a clear account of the illness. | +Newly disoriented and unable to give a clear history.

NEAR (answer s): -Gives a clear account of the illness. | +Her father is newly disoriented.

MISSING (answer neither (undetermined)): -Gives a clear account of the illness. | +Confusion: status unclear from the records at hand.

PRES (answer s): full text
Woman, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Blood urea nitrogen now: 14 mg/dL.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2010.
Her father sprained a thumb last month.
Drives a car.
Prefers morning appointments.
In 2015, lipase was 30 U/L.
Currently aged 42 years.
Gives a clear account of the illness.
Her sister wears contact lenses.
Her roommate has a lazy eye.
Enjoys board games.
Pupils equal and reactive to light.
Knits as a hobby.
Her wife lives with psoriasis.
Lives in a second-floor apartment.
Observations now: respiratory rate 19/min.
Sleeps seven hours a night.
Observations now: blood pressure 109/69 mmHg.
Prefers to be addressed by first name.
Photographs local wildlife.


## 1.5 ('gs058', 'c2', 'time', 'long') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the current ALT is above 120 U/L and the patient is allergic to penicillin, prescribe azithromycin instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Female, 26 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Wears glasses when driving.
Collects postcards.
Her mother previously wore dental braces.
Sodium 140 mmol/L in 2023.
Uses a smartphone for reminders.
Has a pet dog.
Sings in a weekly choir.
Hearing normal to conversation.
Her aunt is nearsighted.
Keeps a step counter.
Drinks plenty of water.
Lives on a quiet street.
Bicarbonate 26 mmol/L in 2019 (annual physical).
Liver tests today: ALT 191 U/L.
Listens to podcasts.
Her housemate has a broken finger in a splint.

FLIP (answer s'): +Penicillin triggers an allergic reaction with wheezing in this patient.

NEAR (answer s): +Penicillin used to cause hives, but the allergy has resolved.

MISSING (answer neither (undetermined)): +Penicillin allergy: could not be determined from the information available.

PRES (answer s): full text
Patient: female, 26 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Her housemate has a broken finger in a splint.
Uses a smartphone for reminders.
Sings in a weekly choir.
Collects postcards.
Her mother previously wore dental braces.
Wears glasses when driving.
Sodium 140 mmol/L in 2023.
Has a pet dog.
Keeps a step counter.
Her aunt is nearsighted.
Hearing normal to conversation.
ALT today: 191 U/L.
Drinks plenty of water.
Bicarbonate 26 mmol/L in 2019 (annual physical).
Listens to podcasts.
Lives on a quiet street.


## 1.6 ('gs043', 'c3', 'boundary', 'easy') templates=test

RULE: For acute sore throat, prescribe ibuprofen. Score 1 point if the current ALT is above 120 U/L; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe penicillin V instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Man of 47 years.
Sore throat for two days.
ALT now 290 U/L.
Enjoys board games.
Prefers morning appointments.
Heart rate now 74/min on a pulse check.
Recovered from a pulmonary embolism in 2008.

FLIP (answer s'): -Heart rate now 74/min on a pulse check. | +Heart rate now 107/min on a pulse check.

NEAR (answer s): -Heart rate now 74/min on a pulse check. | +Heart rate now 90/min on a pulse check.

MISSING (answer neither (undetermined)): -Heart rate now 74/min on a pulse check.

PRES (answer s): full text
Male patient of 47 years.
Sore throat for two days.
Current heart rate 74/min.
Recovered from a pulmonary embolism in 2008.
Prefers morning appointments.
Current ALT 290 U/L.
Enjoys board games.


## 1.7 ('gs143', 'c3', 'negation', 'easy') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient has ever had heparin-induced thrombocytopenia (current or past); the current ALT is above 120 U/L; the patient currently has tonsillar exudate.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
83-year-old man.
First day after elective total hip replacement.
No membrane, film or spots seen over the tonsils.
Bakes bread at home.
Liver tests today: ALT 60 U/L.
Heparin-induced thrombocytopenia in 2007, resolved once heparin was stopped.
Lives on a quiet street.

FLIP (answer s'): -No membrane, film or spots seen over the tonsils. | +Spots of exudate on the left tonsil.

NEAR (answer s): -No membrane, film or spots seen over the tonsils. | +There is no exudate over the tonsils this morning.

MISSING (answer neither (undetermined)): -No membrane, film or spots seen over the tonsils. | +Tonsillar exudate: could not be determined from the information available.

PRES (answer s): full text
Patient: male, 83 years.
First day after elective total hip replacement.
Heparin-induced thrombocytopenia in 2007, resolved once heparin was stopped.
ALT 60 U/L on today's labs.
Bakes bread at home.
Lives on a quiet street.
No membrane, film or spots seen over the tonsils.


## 1.8 ('s2_atria_bleed', 'hgb', 'numeric', 'easy') templates=test

RULE: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 30 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.
CONDITION: hemoglobin below 13.0
CLAIMS: s = 'The hemoglobin criterion contributes 0 points.' | s' = 'The hemoglobin criterion contributes 3 points.'

BASE (answer s):
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Uses sunscreen in summer.
Teeth in good repair.
Latest Hgb result: 15.6 g/dL.
Current eGFR 51 mL/min/1.73 m2.
Retinal examination shows healthy vessels.
Current age 57 years.

FLIP (answer s'): -Latest Hgb result: 15.6 g/dL. | +Latest Hgb result: 9.2 g/dL.

NEAR (answer s): -Latest Hgb result: 15.6 g/dL. | +Latest Hgb result: 13.1 g/dL.

MISSING (answer neither (undetermined)): -Latest Hgb result: 15.6 g/dL.

PRES (answer s): full text
An adult man.
Atrial fibrillation; a decision on warfarin is pending.
Uses sunscreen in summer.
Retinal examination shows healthy vessels.
eGFR now 51 mL/min/1.73 m2.
Current Hgb 15.6 g/dL.
Teeth in good repair.
Currently aged 57 years.


## 1.9 ('gs065', 'c1', 'subject', 'easy') templates=train

RULE: For acute sore throat, prescribe ibuprofen. If the patient has an active peptic ulcer and the patient currently has asthma, prescribe penicillin V instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Patient: female, 17 years.
Sore throat for two days.
Asthma attack this month needing nebulizers; still wheezy at this assessment.
No black or bloody stools.
Nails normal.

FLIP (answer s'): -No black or bloody stools. | +A stomach ulcer is causing burning pain after meals.

NEAR (answer s): -No black or bloody stools. | +Her aunt has an active peptic ulcer.

MISSING (answer neither (undetermined)): -No black or bloody stools. | +Active peptic ulcer: not asked about.

PRES (answer s): full text
17 years old, female.
Sore throat for two days.
No black or bloody stools.
Nails normal.
Asthma attack this month needing nebulizers; still wheezy at this assessment.


## 1.10 ('s3_blatchford', 'bun', 'time', 'easy') templates=test

RULE: Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.
CONDITION: blood urea nitrogen above 18
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 2 points.'

BASE (answer s):
Female patient of 66 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Knits as a hobby.
Current heart rate 66/min.
Observations now: blood pressure 148/93 mmHg.
Blood urea nitrogen 10 mg/dL on the current labs.
Back in 2016, blood urea nitrogen stood at 14 mg/dL.

FLIP (answer s'): -Blood urea nitrogen 10 mg/dL on the current labs. | +Blood urea nitrogen 21 mg/dL on the current labs.

NEAR (answer s): -Back in 2016, blood urea nitrogen stood at 14 mg/dL. | +Back in 2016, blood urea nitrogen stood at 22 mg/dL.

MISSING (answer neither (undetermined)): -Blood urea nitrogen 10 mg/dL on the current labs. | -Back in 2016, blood urea nitrogen stood at 14 mg/dL.

PRES (answer s): full text
Woman of 66 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Knits as a hobby.
Blood urea nitrogen now: 10 mg/dL.
Records from 2016 list blood urea nitrogen at 14 mg/dL.
Heart rate now 66/min on a pulse check.
Current systolic blood pressure 148 mmHg.


## 1.11 ('gs013', 'c1', 'boundary', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the current heart rate is above 90/min, prescribe amlodipine instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Patient: female, 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Bakes bread at home.
Speaks English and Spanish.
Phosphate 3.6 mg/dL in 2014.
Enjoys cooking.
Non-smoker.
Drinks plenty of water.
Keeps a step counter.
Vitamin D 38 ng/mL in 2010 (wellness visit).
Her coworker has a stutter.
Grows tomatoes in the garden.
Plays chess online.
Drinks alcohol occasionally.
Heart rate counted over a full minute at this assessment: 66/min.
Wears a seat belt when driving.
Her husband is nearsighted.
Feeds birds in the backyard.
Hearing normal to conversation.
Chloride 103 mmol/L in 2013.
Height 170 cm.
Wears glasses when driving.

FLIP (answer s'): -Heart rate counted over a full minute at this assessment: 66/min. | +Heart rate counted over a full minute at this assessment: 96/min.

NEAR (answer s): -Heart rate counted over a full minute at this assessment: 66/min. | +Heart rate counted over a full minute at this assessment: 90/min.

MISSING (answer neither (undetermined)): -Heart rate counted over a full minute at this assessment: 66/min.

PRES (answer s): full text
69-year-old woman.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Speaks English and Spanish.
Grows tomatoes in the garden.
Enjoys cooking.
Keeps a step counter.
Feeds birds in the backyard.
Phosphate 3.6 mg/dL in 2014.
Drinks alcohol occasionally.
Non-smoker.
Her coworker has a stutter.
Pulse taken this morning: heart rate 66/min.
Plays chess online.
Bakes bread at home.
Wears glasses when driving.
Wears a seat belt when driving.
Height 170 cm.
Drinks plenty of water.
Her husband is nearsighted.
Vitamin D 38 ng/mL in 2010 (wellness visit).
Chloride 103 mmol/L in 2013.
Hearing normal to conversation.


## 1.12 ('gs134', 'c2', 'negation', 'long') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient has ever had diabetes (current or past) or the patient is currently taking warfarin, prescribe warfarin instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Male patient of 77 years.
Atrial fibrillation; anticoagulation indicated.
In 2018, lipase was 30 U/L.
His sister lives with psoriasis.
His roommate burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2017.
Photographs local wildlife.
Drives a car.
Sleeps seven hours a night.
Enjoys board games.
Plays the piano.
Paints watercolors as a hobby.
Knits as a hobby.
His sister has recovered from a dislocated finger.
Prefers morning appointments.
HbA1c 5.3% at a routine check.
Pupils equal and reactive to light.
Lives in a second-floor apartment.

FLIP (answer s'): +Anticoagulated with warfarin; INR checked monthly at the clinic.

NEAR (answer s): +Has never been prescribed warfarin.

MISSING (answer neither (undetermined)): +Warfarin: status unclear from the records at hand.

PRES (answer s): full text
Man of 77 years.
Atrial fibrillation; anticoagulation indicated.
Pupils equal and reactive to light.
Prefers morning appointments.
Paints watercolors as a hobby.
His sister lives with psoriasis.
His sister has recovered from a dislocated finger.
Photographs local wildlife.
In 2018, lipase was 30 U/L.
Knits as a hobby.
Zinc of 85 mcg/dL in 2017.
Lives in a second-floor apartment.
Enjoys board games.
Plays the piano.
Drives a car.
HbA1c 5.3% at a routine check.
Sleeps seven hours a night.
His roommate burned a hand on a stove years ago.


## 1.13 ('s2_orbit', 'age', 'numeric', 'long') templates=train

RULE: ORBIT bleeding score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for a current age of 75 years or more, a current eGFR below 60 mL/min/1.73 m2, and current use of aspirin. Other ORBIT items are not part of this question.
CONDITION: age at least 75
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Female patient.
Atrial fibrillation; starting apixaban is being considered.
Chloride 103 mmol/L in 2020.
Sodium 140 mmol/L in 2024.
Her brother-in-law is left-handed.
Her neighbor has a chipped front tooth.
Lives on a quiet street.
Writes with the right hand.
Drinks plenty of water.
Uses a smartphone for reminders.
Her brother has a broken finger in a splint.
Hearing normal to conversation.
Hemoglobin normal on today's blood count.
Listens to podcasts.
Has a pet dog.
Watches football on weekends.
Age as of today: 63 years.
Collects postcards.
Total bilirubin 0.6 mg/dL in 2022.
This morning's blood test shows an eGFR of 106 mL/min/1.73 m2.
Eats a varied diet.
Speaks English and Spanish.
Vaccinations up to date.

FLIP (answer s'): -Age as of today: 63 years. | +Age as of today: 75 years.

NEAR (answer s): -Age as of today: 63 years. | +Age as of today: 73 years.

MISSING (answer neither (undetermined)): -Age as of today: 63 years.

PRES (answer s): full text
Sex: female.
Atrial fibrillation; starting apixaban is being considered.
eGFR 106 mL/min/1.73 m2 on today's labs.
Has a pet dog.
Listens to podcasts.
Vaccinations up to date.
Her brother-in-law is left-handed.
Speaks English and Spanish.
Hearing normal to conversation.
Watches football on weekends.
Sodium 140 mmol/L in 2024.
Age 63 years, calculated today from the date of birth.
Her brother has a broken finger in a splint.
Uses a smartphone for reminders.
Total bilirubin 0.6 mg/dL in 2022.
Chloride 103 mmol/L in 2020.
Lives on a quiet street.
Collects postcards.
Writes with the right hand.
Her neighbor has a chipped front tooth.
Eats a varied diet.
Hemoglobin normal on today's blood count.
Drinks plenty of water.


## 1.14 ('gs026', 'c3', 'subject', 'long') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If at least two of the following apply, prescribe naproxen with omeprazole instead: the patient currently has tender anterior cervical lymph nodes; the patient has ever had asthma (current or past); the patient has active cancer.
CONDITION: active cancer
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Female patient of 64 years.
Hip osteoarthritis with pain on walking.
Pupils equal and reactive to light.
Asthma, on a daily inhaled steroid.
In 2021, folate was 12 ng/mL.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Her uncle sprained a thumb last month.
During a checkup in 2016, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Sees a dentist yearly.
Owns a bicycle.
Uses sunscreen in summer.
Knits as a hobby.
Enjoys board games.
Prefers morning appointments.
Her friend has a lazy eye.
Prefers to be addressed by first name.
Weight steady over the past year.
Photographs local wildlife.

FLIP (answer s'): -Weight steady over the past year. | +Has metastatic lung cancer, receiving palliative treatment.

NEAR (answer s): -Weight steady over the past year. | +Her father is being treated for leukemia.

MISSING (answer neither (undetermined)): -Weight steady over the past year. | +Active cancer: status unclear from the records at hand.

PRES (answer s): full text
Woman of 64 years.
Hip osteoarthritis with pain on walking.
Photographs local wildlife.
Prefers to be addressed by first name.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Asthma, on a daily inhaled steroid.
Weight steady over the past year.
Sees a dentist yearly.
Pupils equal and reactive to light.
Owns a bicycle.
During a checkup in 2016, total protein was 7.0 g/dL.
Her uncle sprained a thumb last month.
In 2021, folate was 12 ng/mL.
Enjoys board games.
Prefers morning appointments.
Uses sunscreen in summer.
Her friend has a lazy eye.
Sleeps seven hours a night.


## 1.15 ('gs037', 'c2', 'time', 'long') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. Score 3 points if the patient is currently taking aspirin; 1 point if the current weight is 60 kg or less; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 4 or more, prescribe a progestin-only pill instead.
CONDITION: weight at or below 60
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
20 years old, female.
Requests contraception.
Enjoys gardening.
Serum calcium 9.4 mg/dL in 2024.
Non-smoker.
Nails normal.
Her partner is being treated for eczema.
Vaccinations up to date.
Weight 66 kg at this assessment.
Enjoys cooking.
Drinks alcohol occasionally.
Keeps houseplants.
Weight of 70 kg recorded in 2024.
Drinks plenty of water.
TSH 1.6 mIU/L in 2024.
Her aunt is nearsighted.
Has a pet dog.
Her grandmother is left-handed.
Bakes bread at home.
Volunteers at a library.
Lives on a quiet street.
Active medications today include aspirin 81 mg once daily.
Collects postcards.
No exertional chest discomfort.
Writes with the right hand.

FLIP (answer s'): -Weight 66 kg at this assessment. | +Weight 57 kg at this assessment.

NEAR (answer s): -Weight of 70 kg recorded in 2024. | +Weight of 58 kg recorded in 2024.

MISSING (answer neither (undetermined)): -Weight 66 kg at this assessment. | -Weight of 70 kg recorded in 2024.

PRES (answer s): full text
Patient: female, 20 years.
Requests contraception.
Bakes bread at home.
No exertional chest discomfort.
Lives on a quiet street.
Nails normal.
Her aunt is nearsighted.
Weight checked today on a calibrated scale: 66 kg.
Her grandmother is left-handed.
Her partner is being treated for eczema.
Drinks plenty of water.
Serum calcium 9.4 mg/dL in 2024.
Non-smoker.
Keeps houseplants.
Enjoys cooking.
Active medications today include aspirin 81 mg once daily.
TSH 1.6 mIU/L in 2024.
Has a pet dog.
Drinks alcohol occasionally.
Enjoys gardening.
Volunteers at a library.
Vaccinations up to date.
Weight was 70 kg when measured in 2024.
Writes with the right hand.
Collects postcards.


## 1.16 ('gs207', 'c1', 'boundary', 'easy') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current serum potassium is above 5.0 mmol/L; the patient is currently taking aspirin; the patient has ever had coronary artery disease (current or past).
CONDITION: serum potassium above 5.0
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Woman of 67 years.
Acute low back pain after lifting.
Sees a dentist yearly.
Chest pain on exertion: none reported.
Current serum potassium 3.6 mmol/L.
Uses a daily aspirin on a cardiologist's recommendation.
Drives a car.

FLIP (answer s'): -Current serum potassium 3.6 mmol/L. | +Current serum potassium 5.6 mmol/L.

NEAR (answer s): -Current serum potassium 3.6 mmol/L. | +Current serum potassium 5.0 mmol/L.

MISSING (answer neither (undetermined)): -Current serum potassium 3.6 mmol/L.

PRES (answer s): full text
Female patient of 67 years.
Acute low back pain after lifting.
Latest potassium result: 3.6 mmol/L.
Sees a dentist yearly.
Chest pain on exertion: none reported.
Drives a car.
Uses a daily aspirin on a cardiologist's recommendation.


## 1.17 ('gs138', 'c1', 'negation', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the patient currently has heart failure and the current serum potassium is above 5.0 mmol/L, prescribe a progestin-only pill instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
38 years old, female.
Requests contraception.
Drinks alcohol occasionally.
Potassium 5.7 mmol/L on today's blood work.
Takes no diuretics.

FLIP (answer s'): -Takes no diuretics. | +Heart failure with reduced ejection fraction.

NEAR (answer s): -Takes no diuretics. | +No heart failure, past or present.

MISSING (answer neither (undetermined)): -Takes no diuretics. | +Current heart failure: could not be determined from the information available.

PRES (answer s): full text
38-year-old woman.
Requests contraception.
Drinks alcohol occasionally.
Labs this morning: potassium 5.7 mmol/L.
Takes no diuretics.


## 1.18 ('sirs', 'temp', 'numeric', 'easy') templates=test

RULE: SIRS criteria (as used here, partial): 1 point each for temperature above 38.0 C; heart rate above 90/min; respiratory rate above 20/min; white cell count above 12.0 x10^9/L. Only current findings count.
CONDITION: temperature above 38.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
Male patient of 39 years.
Productive cough for three days; assessed in the emergency department.
Observations now: respiratory rate 13/min.
Heart rate now 62/min on a pulse check.
Current white cell count 9.5 x10^9/L.
Paints watercolors as a hobby.
Owns a bicycle.
Current temperature 37.3 C.

FLIP (answer s'): -Current temperature 37.3 C. | +Current temperature 38.5 C.

NEAR (answer s): -Current temperature 37.3 C. | +Current temperature 37.9 C.

MISSING (answer neither (undetermined)): -Current temperature 37.3 C.

PRES (answer s): full text
Man of 39 years.
Productive cough for three days; assessed in the emergency department.
Paints watercolors as a hobby.
Latest WBC is 9.5 x10^9/L.
Owns a bicycle.
Current heart rate 62/min.
Temperature now 37.3 C (tympanic).
Current respiratory rate 13/min.


## 1.19 ('gs151', 'c2', 'subject', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient has ever had asthma (current or past); the current calf swelling compared with the other leg is 3.0 cm or more.
CONDITION: asthma at any time
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male, 41 years.
Suspected chest infection; assessed on the medical ward.
Chest clear on auscultation, with no wheeze.
Drinks two cups of coffee a day.
Tape measurement today shows a calf circumference gap of 3.5 cm.

FLIP (answer s'): -Chest clear on auscultation, with no wheeze. | +Asthma that began after a chest infection in 2016 and resolved within a year.

NEAR (answer s): -Chest clear on auscultation, with no wheeze. | +His housemate has severe asthma.

MISSING (answer neither (undetermined)): -Chest clear on auscultation, with no wheeze. | +Asthma at any time: not asked about.

PRES (answer s): full text
41-year-old man.
Suspected chest infection; assessed on the medical ward.
Drinks two cups of coffee a day.
Calf circumference measured this morning is 3.5 cm greater on one side.
Chest clear on auscultation, with no wheeze.


## 1.20 ('gs066', 'c3', 'time', 'superseded') templates=test

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If at least two of the following apply, prescribe nitrofurantoin instead: the patient is currently taking clarithromycin; the current heart rate is above 90/min; the current temperature is above 38.0 C.
CONDITION: temperature above 38.0
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Female patient of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Heart rate now 59/min on a pulse check.
On clarithromycin for a chest infection, day 3 of 7.
Lives in a second-floor apartment.
Current temperature 36.8 C.
Teeth in good repair.
Last month, temperature was 37.0 C; the newest measurement replaces it.

FLIP (answer s'): -Current temperature 36.8 C. | +Current temperature 38.9 C.

NEAR (answer s): -Last month, temperature was 37.0 C; the newest measurement replaces it. | +Last month, temperature was 38.5 C; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Current temperature 36.8 C. | -Last month, temperature was 37.0 C; the newest measurement replaces it.

PRES (answer s): full text
Woman of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Last month, temperature was 37.0 C; the newest measurement replaces it.
Teeth in good repair.
Current heart rate 59/min.
Temperature now 36.8 C (tympanic).
Lives in a second-floor apartment.
On clarithromycin for a chest infection, day 3 of 7.


## 1.21 ('all_spiro', 'k', 'boundary', 'long') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone 25 mg daily. If the current serum potassium is above 4.8 mmol/L and the current eGFR is below 50 mL/min/1.73 m2, prescribe spironolactone 12.5 mg daily instead.
CONDITION: potassium above 4.8
CLAIMS: s = 'Prescribe spironolactone 25 mg daily.' | s' = 'Prescribe spironolactone 12.5 mg daily.'

BASE (answer s):
67 years old, female.
Heart failure with reduced ejection fraction (ejection fraction 32%).
Vaccinations up to date.
Speaks English and Spanish.
Enjoys cooking.
Grows tomatoes in the garden.
Enjoys gardening.
Reads most evenings.
Her coworker is nearsighted.
Drinks plenty of water.
Her coworker has a chipped front tooth.
Collects postcards.
Eats a varied diet.
Albumin 4.1 g/dL in 2012 (routine blood test).
Vitamin B12 450 pg/mL in 2010.
Potassium measured at this assessment is 4.2 mmol/L.
Hearing normal to conversation.
Watches football on weekends.
Her cousin has a stutter.
Nails normal.
eGFR today: 30 mL/min/1.73 m2.
Sings in a weekly choir.
Wears glasses when driving.

FLIP (answer s'): -Potassium measured at this assessment is 4.2 mmol/L. | +Potassium measured at this assessment is 5.0 mmol/L.

NEAR (answer s): -Potassium measured at this assessment is 4.2 mmol/L. | +Potassium measured at this assessment is 4.8 mmol/L.

MISSING (answer neither (undetermined)): -Potassium measured at this assessment is 4.2 mmol/L.

PRES (answer s): full text
Female, 67 years.
Heart failure with reduced ejection fraction (ejection fraction 32%).
Potassium 4.2 mmol/L on today's blood work.
Watches football on weekends.
Her coworker is nearsighted.
Reads most evenings.
This morning's blood test shows an eGFR of 30 mL/min/1.73 m2.
Eats a varied diet.
Speaks English and Spanish.
Vitamin B12 450 pg/mL in 2010.
Hearing normal to conversation.
Vaccinations up to date.
Drinks plenty of water.
Sings in a weekly choir.
Albumin 4.1 g/dL in 2012 (routine blood test).
Collects postcards.
Wears glasses when driving.
Enjoys gardening.
Grows tomatoes in the garden.
Enjoys cooking.
Her cousin has a stutter.
Nails normal.
Her coworker has a chipped front tooth.


## 1.22 ('c3_nice_step1', 'diabetes', 'negation', 'easy') templates=test

RULE: For newly diagnosed hypertension, prescribe amlodipine. If the patient's current age is below 55 years or the patient has ever had diabetes (current or past), prescribe ramipril instead.
CONDITION: diabetes at any time
CLAIMS: s = 'Prescribe amlodipine.' | s' = 'Prescribe ramipril.'

BASE (answer s):
Man, adult.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Current age 71 years.
HbA1c 5.3% at a routine check.
Paints watercolors as a hobby.
Has two cats.
Prefers morning appointments.
Photographs local wildlife.

FLIP (answer s'): -HbA1c 5.3% at a routine check. | +Has type 2 diabetes on metformin.

NEAR (answer s): -HbA1c 5.3% at a routine check. | +Never diagnosed with diabetes.

MISSING (answer neither (undetermined)): -HbA1c 5.3% at a routine check. | +Diabetes at any time: unknown.

PRES (answer s): full text
An adult man.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
HbA1c 5.3% at a routine check.
Currently aged 71 years.
Photographs local wildlife.
Paints watercolors as a hobby.
Has two cats.
Prefers morning appointments.


## 1.23 ('any_gout', 'egfr', 'numeric', 'long') templates=train

RULE: For an acute gout flare, prescribe naproxen. If the patient has an active peptic ulcer or the current eGFR is below 30 mL/min/1.73 m2, prescribe colchicine instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe colchicine.'

BASE (answer s):
Female, 58 years.
Acute gout flare of the left knee.
Height 170 cm.
TSH 1.6 mIU/L in 2009.
Her brother-in-law has a fear of heights.
Wears a seat belt when driving.
Collects postcards.
Her aunt had a splinter removed from a finger.
Listens to podcasts.
Plays chess online.
Albumin 4.1 g/dL in 2013 (routine blood test).
Wears glasses when driving.
Uses a smartphone for reminders.
Grows tomatoes in the garden.
Bicarbonate 26 mmol/L in 2006 (annual physical).
Reads most evenings.
Ferritin 60 ng/mL in 2022.
Has a pet dog.
Keeps houseplants.
Her husband has a chipped front tooth.
eGFR today: 64 mL/min/1.73 m2.
Vaccinations up to date.
Keeps a step counter.

FLIP (answer s'): -eGFR today: 64 mL/min/1.73 m2. | +eGFR today: 18 mL/min/1.73 m2.

NEAR (answer s): -eGFR today: 64 mL/min/1.73 m2. | +eGFR today: 32 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -eGFR today: 64 mL/min/1.73 m2.

PRES (answer s): full text
58 years old, female.
Acute gout flare of the left knee.
Collects postcards.
Her aunt had a splinter removed from a finger.
Grows tomatoes in the garden.
eGFR 64 mL/min/1.73 m2 on today's labs.
TSH 1.6 mIU/L in 2009.
Uses a smartphone for reminders.
Wears a seat belt when driving.
Has a pet dog.
Wears glasses when driving.
Reads most evenings.
Listens to podcasts.
Ferritin 60 ng/mL in 2022.
Her husband has a chipped front tooth.
Albumin 4.1 g/dL in 2013 (routine blood test).
Plays chess online.
Keeps a step counter.
Height 170 cm.
Vaccinations up to date.
Her brother-in-law has a fear of heights.
Keeps houseplants.
Bicarbonate 26 mmol/L in 2006 (annual physical).


## 1.24 ('gs193', 'c1', 'subject', 'long') templates=test

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient has an active peptic ulcer and the patient currently has a mechanical heart valve, prescribe azithromycin instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Man of 53 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Owns a bicycle.
Lives with a mechanical aortic valve prosthesis.
Paints watercolors as a hobby.
Sees a dentist yearly.
His roommate wears contact lenses.
Abdomen soft and non-tender.
During a checkup in 2011, free T3 was 3.2 pg/mL.
His roommate burned a hand on a stove years ago.
Prefers to be addressed by first name.
Has two cats.
His roommate has recovered from a dislocated finger.
Drives a car.
Uses sunscreen in summer.
Photographs local wildlife.
In 2020, lipase was 30 U/L.
Prefers morning appointments.
During a checkup in 2013, total protein was 7.0 g/dL.
Enjoys board games.
Knits as a hobby.
Plays the piano.

FLIP (answer s'): -Abdomen soft and non-tender. | +Has an active duodenal ulcer.

NEAR (answer s): -Abdomen soft and non-tender. | +His wife has peptic ulcer disease.

MISSING (answer neither (undetermined)): -Abdomen soft and non-tender. | +Active peptic ulcer: unknown.

PRES (answer s): full text
Male patient of 53 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Abdomen soft and non-tender.
Sees a dentist yearly.
Photographs local wildlife.
Lives with a mechanical aortic valve prosthesis.
Knits as a hobby.
Owns a bicycle.
Drives a car.
Uses sunscreen in summer.
Prefers morning appointments.
Enjoys board games.
His roommate has recovered from a dislocated finger.
Prefers to be addressed by first name.
His roommate wears contact lenses.
During a checkup in 2011, free T3 was 3.2 pg/mL.
Has two cats.
Plays the piano.
During a checkup in 2013, total protein was 7.0 g/dL.
His roommate burned a hand on a stove years ago.
Paints watercolors as a hobby.
In 2020, lipase was 30 U/L.


## 1.25 ('gs017', 'c2', 'time', 'superseded') templates=train

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient has ever had a venous thromboembolism (current or past) or the current blood urea nitrogen is above 19 mg/dL, prescribe nitrofurantoin instead.
CONDITION: blood urea nitrogen above 19
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Female, 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Lives on a quiet street.
Blood urea nitrogen of 14 mg/dL measured yesterday was replaced by a repeat measurement.
Height 170 cm.
BUN 9 mg/dL this morning.

FLIP (answer s'): -BUN 9 mg/dL this morning. | +BUN 27 mg/dL this morning.

NEAR (answer s): -Blood urea nitrogen of 14 mg/dL measured yesterday was replaced by a repeat measurement. | +Blood urea nitrogen of 37 mg/dL measured yesterday was replaced by a repeat measurement.

MISSING (answer neither (undetermined)): -Blood urea nitrogen of 14 mg/dL measured yesterday was replaced by a repeat measurement. | -BUN 9 mg/dL this morning.

PRES (answer s): full text
22 years old, female.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Blood urea nitrogen of 14 mg/dL measured yesterday was replaced by a repeat measurement.
Lives on a quiet street.
Height 170 cm.
BUN on today's chemistry panel: 9 mg/dL.


## 1.26 ('gs058', 'c1', 'boundary', 'easy') templates=test

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the current ALT is above 120 U/L and the patient is allergic to penicillin, prescribe azithromycin instead.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Male patient of 23 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Known penicillin allergy with angioedema.
Paints watercolors as a hobby.
Current ALT 44 U/L.
Lives in a second-floor apartment.

FLIP (answer s'): -Current ALT 44 U/L. | +Current ALT 348 U/L.

NEAR (answer s): -Current ALT 44 U/L. | +Current ALT 120 U/L.

MISSING (answer neither (undetermined)): -Current ALT 44 U/L.

PRES (answer s): full text
Man of 23 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Known penicillin allergy with angioedema.
ALT now 44 U/L.


## 1.27 ('gs107', 'c3', 'negation', 'easy') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current systolic blood pressure is above 160 mmHg; the patient is currently taking clarithromycin.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
43 years old, female.
Productive cough and fever; consolidation on chest radiograph.
Speaks English and Spanish.
Her mother completed radiation for colorectal cancer in 2020.
Systolic blood pressure 140 mmHg at this assessment.

FLIP (answer s'): +Takes clarithromycin as part of Helicobacter pylori treatment.

NEAR (answer s): +Denies taking clarithromycin.

MISSING (answer neither (undetermined)): +Clarithromycin: could not be determined from the information available.

PRES (answer s): full text
Female, 43 years.
Productive cough and fever; consolidation on chest radiograph.
Her mother completed radiation for colorectal cancer in 2020.
Blood pressure 140/88 mmHg this morning.
Speaks English and Spanish.


## 1.28 ('s3_blatchford', 'bun', 'numeric', 'long') templates=test

RULE: Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.
CONDITION: blood urea nitrogen above 18
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 2 points.'

BASE (answer s):
Woman of 55 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Blood urea nitrogen 12 mg/dL on the current labs.
Her uncle burned a hand on a stove years ago.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Sleeps flat on one pillow.
Photographs local wildlife.
Drives a car.
Owns a bicycle.
Has two cats.
Sees a dentist yearly.
Her uncle wears contact lenses.
Plays the piano.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2005.
Heart rate now 74/min on a pulse check.
Prefers morning appointments.
Sleeps seven hours a night.
Uses sunscreen in summer.
Paints watercolors as a hobby.
During a checkup in 2011, free T3 was 3.2 pg/mL.
Current systolic blood pressure 123 mmHg.
Teeth in good repair.

FLIP (answer s'): -Blood urea nitrogen 12 mg/dL on the current labs. | +Blood urea nitrogen 19 mg/dL on the current labs.

NEAR (answer s): -Blood urea nitrogen 12 mg/dL on the current labs. | +Blood urea nitrogen 16 mg/dL on the current labs.

MISSING (answer neither (undetermined)): -Blood urea nitrogen 12 mg/dL on the current labs.

PRES (answer s): full text
Female patient of 55 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Owns a bicycle.
Photographs local wildlife.
Plays the piano.
Her uncle wears contact lenses.
Her uncle burned a hand on a stove years ago.
Teeth in good repair.
Sleeps seven hours a night.
Sleeps flat on one pillow.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2005.
Observations now: blood pressure 123/78 mmHg.
Has two cats.
Current heart rate 74/min.
Sees a dentist yearly.
Drives a car.
Lives in a second-floor apartment.
Blood urea nitrogen now: 12 mg/dL.
During a checkup in 2011, free T3 was 3.2 pg/mL.
Prefers morning appointments.


## 1.29 ('s3_hctci', 'cad', 'subject', 'easy') templates=train

RULE: Hematopoietic Cell Transplantation-specific Comorbidity Index (as used here, partial): 1 point for coronary artery disease at any time (current or past); 1 point for a stroke or TIA at any time (current or past); 2 points for a current peptic ulcer; 1 point for a current ALT above 40 U/L. Other items of the index are not part of this question.
CONDITION: coronary artery disease
CLAIMS: s = 'The coronary artery disease criterion contributes 0 points.' | s' = 'The coronary artery disease criterion contributes 1 point.'

BASE (answer s):
55-year-old man.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Drinks alcohol occasionally.
Watches football on weekends.
Cranial nerves intact.
No angina symptoms reported.
ALT today: 30 U/L.
No dyspepsia or melena.

FLIP (answer s'): -No angina symptoms reported. | +Coronary artery disease, with angina when walking uphill.

NEAR (answer s): -No angina symptoms reported. | +His neighbor carries a nitroglycerin spray for coronary artery disease.

MISSING (answer neither (undetermined)): -No angina symptoms reported. | +Information on coronary artery disease was not obtained.

PRES (answer s): full text
Patient: male, 55 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
No dyspepsia or melena.
ALT 30 U/L on today's labs.
Drinks alcohol occasionally.
Cranial nerves intact.
Watches football on weekends.
No angina symptoms reported.


## 1.30 ('gs065', 'c2', 'time', 'long') templates=test

RULE: For acute sore throat, prescribe ibuprofen. If the patient has an active peptic ulcer and the patient currently has asthma, prescribe penicillin V instead.
CONDITION: asthma
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Female patient of 37 years.
Sore throat for two days.
Drives a car.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Teeth in good repair.
Her wife burned a hand on a stove years ago.
Prefers morning appointments.
Her father has recovered from a dislocated finger.
Lives in a second-floor apartment.
Her father wears contact lenses.
Lungs clear, without wheeze or prolonged expiration.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Enjoys board games.
Knits as a hobby.
Prefers to be addressed by first name.
Photographs local wildlife.
Has an active duodenal ulcer.
In 2020, folate was 12 ng/mL.

FLIP (answer s'): -Lungs clear, without wheeze or prolonged expiration. | +Persistent asthma, using a rescue inhaler most weeks.

NEAR (answer s): -Lungs clear, without wheeze or prolonged expiration. | +Formerly had asthma in elementary school; well for many years without inhalers.

MISSING (answer neither (undetermined)): -Lungs clear, without wheeze or prolonged expiration. | +Asthma: unknown.

PRES (answer s): full text
Woman of 37 years.
Sore throat for two days.
Her wife burned a hand on a stove years ago.
Drives a car.
Sleeps seven hours a night.
Knits as a hobby.
Prefers to be addressed by first name.
In 2020, folate was 12 ng/mL.
Prefers morning appointments.
Teeth in good repair.
Lungs clear, without wheeze or prolonged expiration.
Lives in a second-floor apartment.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Enjoys board games.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Has an active duodenal ulcer.
Photographs local wildlife.
Her father wears contact lenses.
Her father has recovered from a dislocated finger.


## 1.31 ('gs013', 'c1', 'boundary', 'easy') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the current heart rate is above 90/min, prescribe amlodipine instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Patient: male, 30 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Feeds birds in the backyard.
Pulse taken this morning: heart rate 72/min.
Keeps houseplants.
Height 170 cm.

FLIP (answer s'): -Pulse taken this morning: heart rate 72/min. | +Pulse taken this morning: heart rate 112/min.

NEAR (answer s): -Pulse taken this morning: heart rate 72/min. | +Pulse taken this morning: heart rate 90/min.

MISSING (answer neither (undetermined)): -Pulse taken this morning: heart rate 72/min.

PRES (answer s): full text
30-year-old man.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Feeds birds in the backyard.
Heart rate 72/min at rest this morning.
Height 170 cm.
Keeps houseplants.


## 1.32 ('gs005', 'c1', 'negation', 'easy') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient currently has heart failure, prescribe fondaparinux instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Male patient of 69 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Enjoys board games.
Prefers morning appointments.

FLIP (answer s'): +Current heart failure with ankle swelling.

NEAR (answer s): +Heart failure: never diagnosed.

MISSING (answer neither (undetermined)): +Current heart failure: unknown.

PRES (answer s): full text
Man of 69 years.
First day after elective total hip replacement.
Photographs local wildlife.
Prefers morning appointments.
Enjoys board games.
Sleeps seven hours a night.


## 1.33 ('gs086', 'c1', 'numeric', 'easy') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the current systolic blood pressure is above 160 mmHg and the current platelet count is below 50 x10^9/L, prescribe fondaparinux instead.
CONDITION: systolic blood pressure above 160
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
80-year-old man.
First day after elective total hip replacement.
Platelet count at this assessment: 24 x10^9/L.
Enjoys gardening.
Manual cuff blood pressure today: 144/90 mmHg.
Keeps houseplants.
Drinks plenty of water.

FLIP (answer s'): -Manual cuff blood pressure today: 144/90 mmHg. | +Manual cuff blood pressure today: 170/106 mmHg.

NEAR (answer s): -Manual cuff blood pressure today: 144/90 mmHg. | +Manual cuff blood pressure today: 155/97 mmHg.

MISSING (answer neither (undetermined)): -Manual cuff blood pressure today: 144/90 mmHg.

PRES (answer s): full text
Patient: male, 80 years.
First day after elective total hip replacement.
Drinks plenty of water.
Systolic blood pressure 144 mmHg at this assessment.
Platelet count today: 24 x10^9/L.
Keeps houseplants.
Enjoys gardening.


## 1.34 ('gs088', 'c1', 'subject', 'easy') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the patient has ever had asthma (current or past) or the current systolic blood pressure is 90 mmHg or less, prescribe sitagliptin instead.
CONDITION: asthma at any time
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Man of 49 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current systolic blood pressure 120 mmHg.
Lungs clear, without wheeze or prolonged expiration.
Photographs local wildlife.

FLIP (answer s'): -Lungs clear, without wheeze or prolonged expiration. | +Asthma, on a daily inhaled steroid.

NEAR (answer s): -Lungs clear, without wheeze or prolonged expiration. | +His uncle had asthma years ago.

MISSING (answer neither (undetermined)): -Lungs clear, without wheeze or prolonged expiration. | +Asthma at any time: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 49 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Observations now: blood pressure 120/76 mmHg.
Photographs local wildlife.
Lungs clear, without wheeze or prolonged expiration.


## 1.35 ('gs090', 'c1', 'time', 'long') templates=train

RULE: For an acute gout flare, prescribe colchicine. If the current serum creatinine is above 2.0 mg/dL, prescribe prednisone instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe colchicine.' | s' = 'Prescribe prednisone.'

BASE (answer s):
44 years old, female.
Acute gout flare of the right first metatarsophalangeal joint.
Keeps a step counter.
Non-smoker.
Her mother is being treated for eczema.
Writes with the right hand.
Her cousin broke a wrist, which has healed.
Kidney function today: creatinine 0.7 mg/dL.
Phosphate 3.6 mg/dL in 2009.
Uses public transport.
Magnesium 2.0 mg/dL in 2006.
In 2020, serum creatinine was 1.2 mg/dL.
Feeds birds in the backyard.
Vitamin B12 450 pg/mL in 2010.
Listens to podcasts.
Hearing normal to conversation.
Her neighbor had a splinter removed from a finger.
Drinks plenty of water.
Collects postcards.
Drinks two cups of coffee a day.
Chloride 103 mmol/L in 2022.
Lives on a quiet street.
Her neighbor previously wore dental braces.

FLIP (answer s'): -Kidney function today: creatinine 0.7 mg/dL. | +Kidney function today: creatinine 2.6 mg/dL.

NEAR (answer s): -In 2020, serum creatinine was 1.2 mg/dL. | +In 2020, serum creatinine was 2.9 mg/dL.

MISSING (answer neither (undetermined)): -Kidney function today: creatinine 0.7 mg/dL. | -In 2020, serum creatinine was 1.2 mg/dL.

PRES (answer s): full text
Female, 44 years.
Acute gout flare of the right first metatarsophalangeal joint.
Keeps a step counter.
Drinks two cups of coffee a day.
Blood panel at this assessment: creatinine 0.7 mg/dL.
Listens to podcasts.
Her neighbor previously wore dental braces.
Magnesium 2.0 mg/dL in 2006.
Non-smoker.
Hearing normal to conversation.
Chloride 103 mmol/L in 2022.
Collects postcards.
Lives on a quiet street.
Phosphate 3.6 mg/dL in 2009.
Writes with the right hand.
Her neighbor had a splinter removed from a finger.
Uses public transport.
Serum creatinine 1.2 mg/dL at a hospital visit in 2020.
Her mother is being treated for eczema.
Her cousin broke a wrist, which has healed.
Feeds birds in the backyard.
Vitamin B12 450 pg/mL in 2010.
Drinks plenty of water.


## 1.36 ('s1_sofa', 'map', 'boundary', 'long') templates=test

RULE: SOFA score (as used here, partial): 1 point each for a current platelet count below 150 x10^9/L; a current serum creatinine of 1.2 mg/dL or more; a current mean arterial pressure below 70 mmHg. Other SOFA items are not part of this question.
CONDITION: mean arterial pressure below 70
CLAIMS: s = 'The mean arterial pressure criterion contributes 0 points.' | s' = 'The mean arterial pressure criterion contributes 1 point.'

BASE (answer s):
Man of 47 years.
Sepsis from a chest infection; admitted to the intensive care unit.
Sleeps seven hours a night.
Drives a car.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2016.
Prefers morning appointments.
Enjoys board games.
Current serum creatinine 0.5 mg/dL.
His father wears contact lenses.
His father lives with psoriasis.
Platelet count now 293 x10^9/L.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Photographs local wildlife.
His wife burned a hand on a stove years ago.
Current mean arterial pressure 87 mmHg.
In 2007, folate was 12 ng/mL.
Plays the piano.
Knits as a hobby.

FLIP (answer s'): -Current mean arterial pressure 87 mmHg. | +Current mean arterial pressure 56 mmHg.

NEAR (answer s): -Current mean arterial pressure 87 mmHg. | +Current mean arterial pressure 70 mmHg.

MISSING (answer neither (undetermined)): -Current mean arterial pressure 87 mmHg.

PRES (answer s): full text
Male patient of 47 years.
Sepsis from a chest infection; admitted to the intensive care unit.
Prefers morning appointments.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Prefers to be addressed by first name.
Latest creatinine result: 0.5 mg/dL.
In 2007, folate was 12 ng/mL.
Free T4 of 1.2 ng/dL in 2016.
Latest mean arterial pressure reading: 87 mmHg.
Drives a car.
Plays the piano.
Knits as a hobby.
His father wears contact lenses.
Current platelet count 293 x10^9/L.
Sleeps seven hours a night.
Teeth in good repair.
His wife burned a hand on a stove years ago.
Pupils equal and reactive to light.
Enjoys board games.
Lives in a second-floor apartment.
His father lives with psoriasis.


## 1.37 ('gs236', 'c1', 'negation', 'long') templates=train

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. Score 3 points if the patient currently has asthma; 2 points if the current heart rate is above 90/min; 3 points if the patient is allergic to sulfonamide antibiotics. If the score is 5 or more, prescribe sitagliptin instead.
CONDITION: asthma
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Male, 35 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Enjoys gardening.
Reads most evenings.
Hearing normal to conversation.
Wears glasses when driving.
Vaccinations up to date.
Chloride 103 mmol/L in 2018.
Keeps houseplants.
Lives on a quiet street.
His neighbor completed physical therapy for a shoulder injury.
Watches football on weekends.
Drinks plenty of water.
Albumin 4.1 g/dL in 2015 (routine blood test).
No known antibiotic allergies.
Heart rate today: 139/min.
Volunteers at a library.
Keeps a step counter.
Grows tomatoes in the garden.
His cousin is left-handed.
No night cough or chest tightness.
Bakes bread at home.
Has a pet dog.

FLIP (answer s'): -No night cough or chest tightness. | +Has asthma and uses an albuterol inhaler for wheeze.

NEAR (answer s): -No night cough or chest tightness. | +Not asthmatic.

MISSING (answer neither (undetermined)): -No night cough or chest tightness. | +Asthma: not asked about.

PRES (answer s): full text
35 years old, male.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Watches football on weekends.
Hearing normal to conversation.
Lives on a quiet street.
Wears glasses when driving.
No night cough or chest tightness.
Has a pet dog.
Reads most evenings.
Bakes bread at home.
Enjoys gardening.
Volunteers at a library.
Albumin 4.1 g/dL in 2015 (routine blood test).
Heart rate counted over a full minute at this assessment: 139/min.
His cousin is left-handed.
His neighbor completed physical therapy for a shoulder injury.
Chloride 103 mmol/L in 2018.
Vaccinations up to date.
Keeps a step counter.
No known antibiotic allergies.
Grows tomatoes in the garden.
Drinks plenty of water.
Keeps houseplants.


## 1.38 ('gs146', 'c1', 'numeric', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Man of 81 years.
Hip osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Photographs local wildlife.
Current serum creatinine 0.9 mg/dL.
Enjoys board games.

FLIP (answer s'): -Current serum creatinine 0.9 mg/dL. | +Current serum creatinine 4.2 mg/dL.

NEAR (answer s): -Current serum creatinine 0.9 mg/dL. | +Current serum creatinine 1.9 mg/dL.

MISSING (answer neither (undetermined)): -Current serum creatinine 0.9 mg/dL.

PRES (answer s): full text
Male patient of 81 years.
Hip osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Enjoys board games.
Pupils equal and reactive to light.
Photographs local wildlife.
Latest creatinine result: 0.9 mg/dL.


## 1.39 ('gs059', 'c2', 'subject', 'easy') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient currently has a venous thromboembolism and the patient currently has tender anterior cervical lymph nodes, prescribe intermittent pneumatic compression instead.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
45 years old, male.
Admitted for community-acquired pneumonia; immobile.
Watches football on weekends.
Vaccinations up to date.
On treatment for a deep vein thrombosis in the left leg.
Writes with the right hand.
No tender swellings in the neck.

FLIP (answer s'): -No tender swellings in the neck. | +Tender anterior cervical lymph nodes on the left.

NEAR (answer s): -No tender swellings in the neck. | +His coworker's anterior cervical lymph nodes are tender this morning.

MISSING (answer neither (undetermined)): -No tender swellings in the neck. | +Tender cervical lymph nodes: could not be determined from the information available.

PRES (answer s): full text
Male, 45 years.
Admitted for community-acquired pneumonia; immobile.
No tender swellings in the neck.
On treatment for a deep vein thrombosis in the left leg.
Vaccinations up to date.
Watches football on weekends.
Writes with the right hand.


## 1.40 ('gs055', 'c1', 'time', 'superseded') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current heart rate is above 90/min or the current respiratory rate is 25/min or more, prescribe aspirin plus clopidogrel instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Male patient of 86 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Drives a car.
Current heart rate 82/min.
Last month, heart rate was 79/min; the newest measurement replaces it.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Current respiratory rate 18/min.

FLIP (answer s'): -Current heart rate 82/min. | +Current heart rate 116/min.

NEAR (answer s): -Last month, heart rate was 79/min; the newest measurement replaces it. | +Last month, heart rate was 132/min; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Current heart rate 82/min. | -Last month, heart rate was 79/min; the newest measurement replaces it.

PRES (answer s): full text
Man of 86 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Drives a car.
Uses sunscreen in summer.
Heart rate now 82/min on a pulse check.
Lives in a second-floor apartment.
Observations now: respiratory rate 18/min.
Last month, heart rate was 79/min; the newest measurement replaces it.


## 1.41 ('gs173', 'c2', 'boundary', 'long') templates=train

RULE: For acute migraine, prescribe sumatriptan. If the current calf swelling compared with the other leg is 3.0 cm or more or the current white cell count is above 12.0 x10^9/L, prescribe naproxen instead.
CONDITION: white cell count above 12.0
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
60 years old, female.
Acute migraine without aura, typical of prior attacks.
Enjoys cooking.
Collects postcards.
Keeps houseplants.
Serum calcium 9.4 mg/dL in 2008.
Her aunt wears hearing aids.
Enjoys gardening.
Nails normal.
Her brother has a broken finger in a splint.
Keeps a step counter.
Drinks plenty of water.
Hearing normal to conversation.
Wears a seat belt when driving.
Uses a smartphone for reminders.
Her cousin is left-handed.
Complete blood count this morning: white cell count 5.4 x10^9/L.
Phosphate 3.6 mg/dL in 2021.
Sodium 140 mmol/L in 2005.
Vaccinations up to date.
Difference in calf circumference today, side to side: 1.1 cm.

FLIP (answer s'): -Complete blood count this morning: white cell count 5.4 x10^9/L. | +Complete blood count this morning: white cell count 19.4 x10^9/L.

NEAR (answer s): -Complete blood count this morning: white cell count 5.4 x10^9/L. | +Complete blood count this morning: white cell count 12.0 x10^9/L.

MISSING (answer neither (undetermined)): -Complete blood count this morning: white cell count 5.4 x10^9/L.

PRES (answer s): full text
Female, 60 years.
Acute migraine without aura, typical of prior attacks.
Phosphate 3.6 mg/dL in 2021.
Vaccinations up to date.
Serum calcium 9.4 mg/dL in 2008.
Enjoys cooking.
Sodium 140 mmol/L in 2005.
Keeps a step counter.
Keeps houseplants.
Tape measurement today shows a calf circumference gap of 1.1 cm.
Her cousin is left-handed.
Nails normal.
White cell count today: 5.4 x10^9/L.
Uses a smartphone for reminders.
Hearing normal to conversation.
Drinks plenty of water.
Wears a seat belt when driving.
Enjoys gardening.
Her brother has a broken finger in a splint.
Her aunt wears hearing aids.
Collects postcards.


## 1.42 ('gs228', 'c2', 'negation', 'easy') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current ALT is above 120 U/L or the patient is currently taking aspirin, prescribe warfarin instead.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Woman of 49 years.
Atrial fibrillation; anticoagulation indicated.
Photographs local wildlife.
ALT now 55 U/L.
Antiplatelet therapy: none at present.
Prefers morning appointments.
Enjoys board games.

FLIP (answer s'): -Antiplatelet therapy: none at present. | +Currently on low-dose aspirin for heart protection.

NEAR (answer s): -Antiplatelet therapy: none at present. | +Has never taken aspirin.

MISSING (answer neither (undetermined)): -Antiplatelet therapy: none at present. | +Aspirin use: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 49 years.
Atrial fibrillation; anticoagulation indicated.
Enjoys board games.
Prefers morning appointments.
Photographs local wildlife.
Current ALT 55 U/L.
Antiplatelet therapy: none at present.


## 1.43 ('s1_mews', 'sbp', 'numeric', 'long') templates=train

RULE: Modified Early Warning Score (as used here, partial: only the stated band of each listed item): 3 points for a systolic blood pressure of 70 mmHg or less; 3 points for a heart rate of 130/min or more; 3 points for a respiratory rate of 30/min or more; 2 points for a temperature of 38.5 C or more. Any other value of these items scores 0 here, and the other MEWS items are not part of this question. Only current findings count.
CONDITION: systolic blood pressure at or below 70
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 3 points.'

BASE (answer s):
51 years old, male.
Abdominal pain and vomiting; assessed on the surgical admissions unit.
His partner is left-handed.
Uses public transport.
Vitamin D 38 ng/mL in 2016 (wellness visit).
Nails normal.
Writes with the right hand.
Respiratory rate 12/min this morning.
Feeds birds in the backyard.
Sodium 140 mmol/L in 2016.
Watches football on weekends.
Temperature checked with a digital thermometer today: 36.7 C.
Vaccinations up to date.
Uses a smartphone for reminders.
Systolic blood pressure 123 mmHg at this assessment.
Reads most evenings.
Non-smoker.
Total bilirubin 0.6 mg/dL in 2010.
Keeps a step counter.
Pulse taken this morning: heart rate 59/min.
Height 170 cm.
His coworker has a stutter.
His coworker has a fear of heights.

FLIP (answer s'): -Systolic blood pressure 123 mmHg at this assessment. | +Systolic blood pressure 70 mmHg at this assessment.

NEAR (answer s): -Systolic blood pressure 123 mmHg at this assessment. | +Systolic blood pressure 75 mmHg at this assessment.

MISSING (answer neither (undetermined)): -Systolic blood pressure 123 mmHg at this assessment.

PRES (answer s): full text
Patient: male, 51 years.
Abdominal pain and vomiting; assessed on the surgical admissions unit.
Total bilirubin 0.6 mg/dL in 2010.
Non-smoker.
Uses public transport.
Vaccinations up to date.
Nails normal.
Feeds birds in the backyard.
Height 170 cm.
Uses a smartphone for reminders.
Watches football on weekends.
Heart rate today: 59/min.
Blood pressure 123/78 mmHg this morning.
Writes with the right hand.
His coworker has a stutter.
Vitamin D 38 ng/mL in 2016 (wellness visit).
Sodium 140 mmol/L in 2016.
Temperature today: 36.7 C.
Reads most evenings.
His partner is left-handed.
Respiratory rate, counted over a full minute today, is 12/min.
Keeps a step counter.
His coworker has a fear of heights.


## 1.44 ('gs200', 'c1', 'subject', 'easy') templates=test

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. Score 2 points if the patient has had cancer at any time (active or in remission); 2 points if the current systolic blood pressure is below 90 mmHg; 3 points if the patient is currently taking clarithromycin; 3 points if the current serum potassium is above 5.0 mmol/L. If the score is 8 or more, prescribe doxycycline instead.
CONDITION: cancer at any time
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Male patient of 73 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
On clarithromycin for a chest infection, day 3 of 7.
Latest potassium result: 6.1 mmol/L.
Observations now: blood pressure 118/75 mmHg.

FLIP (answer s'): +Has melanoma skin cancer and is receiving treatment for it.

NEAR (answer s): +His friend had thyroid cancer years ago and recovered fully.

MISSING (answer neither (undetermined)): +Cancer at any time: unknown.

PRES (answer s): full text
Man of 73 years.
Productive cough and fever; consolidation on chest radiograph.
Current serum potassium 6.1 mmol/L.
On clarithromycin for a chest infection, day 3 of 7.
Uses sunscreen in summer.
Current systolic blood pressure 118 mmHg.


## 1.45 ('s3_childpugh', 'inr', 'time', 'easy') templates=train

RULE: Child-Pugh score (as used here, partial; each finding below adds 1 point, whatever its grade): 1 point each for a current international normalized ratio (INR) of 1.7 or more; current ascites; new confusion (encephalopathy). Bilirubin, albumin and other items are not part of this question.
CONDITION: international normalized ratio at least 1.7
CLAIMS: s = 'The international normalized ratio criterion contributes 0 points.' | s' = 'The international normalized ratio criterion contributes 1 point.'

BASE (answer s):
50-year-old man.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
International normalized ratio was 1.4 when measured in 2018.
Sings in a weekly choir.
International normalized ratio (INR) at this assessment: 1.3.
Nails normal.
Abdominal girth stable; no fluid felt on examination.
Feeds birds in the backyard.
Wears a seat belt when driving.

FLIP (answer s'): -International normalized ratio (INR) at this assessment: 1.3. | +International normalized ratio (INR) at this assessment: 2.3.

NEAR (answer s): -International normalized ratio was 1.4 when measured in 2018. | +International normalized ratio was 2.1 when measured in 2018.

MISSING (answer neither (undetermined)): -International normalized ratio was 1.4 when measured in 2018. | -International normalized ratio (INR) at this assessment: 1.3.

PRES (answer s): full text
50 years old, male.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Wears a seat belt when driving.
International normalized ratio today: 1.3.
Feeds birds in the backyard.
Nails normal.
Sings in a weekly choir.
Abdominal girth stable; no fluid felt on examination.
In 2018, international normalized ratio was 1.4.


## 1.46 ('c1_spironolactone', 'k', 'boundary', 'long') templates=test

RULE: For hypertension uncontrolled on amlodipine, ramipril and indapamide, prescribe spironolactone. If the current serum potassium is above 4.5 mmol/L, prescribe doxazosin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe doxazosin.'

BASE (answer s):
Male patient of 51 years.
Clinic blood pressure 158/96 mmHg on three visits despite full doses of amlodipine, ramipril and indapamide.
During a checkup in 2006, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
His wife sprained a thumb last month.
In 2006, lipase was 30 U/L.
Enjoys board games.
His sister wears contact lenses.
Prefers morning appointments.
His father lives with psoriasis.
Free T4 of 1.2 ng/dL in 2008.
Paints watercolors as a hobby.
His uncle has a lazy eye.
Latest potassium result: 3.8 mmol/L.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Knits as a hobby.

FLIP (answer s'): -Latest potassium result: 3.8 mmol/L. | +Latest potassium result: 5.2 mmol/L.

NEAR (answer s): -Latest potassium result: 3.8 mmol/L. | +Latest potassium result: 4.5 mmol/L.

MISSING (answer neither (undetermined)): -Latest potassium result: 3.8 mmol/L.

PRES (answer s): full text
Man of 51 years.
Clinic blood pressure 158/96 mmHg on three visits despite full doses of amlodipine, ramipril and indapamide.
Enjoys board games.
Current serum potassium 3.8 mmol/L.
Uses sunscreen in summer.
His father lives with psoriasis.
His uncle has a lazy eye.
Prefers morning appointments.
Knits as a hobby.
During a checkup in 2006, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
His wife sprained a thumb last month.
Pupils equal and reactive to light.
His sister wears contact lenses.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2008.
In 2006, lipase was 30 U/L.


## 1.47 ('gs044', 'c1', 'negation', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient is allergic to sulfonamide antibiotics, prescribe amlodipine instead.
CONDITION: colorectal cancer
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
35-year-old man.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
His neighbor previously wore dental braces.
Writes with the right hand.
Drinks alcohol occasionally.
Eats a varied diet.
His cousin had a splinter removed from a finger.
Chloride 103 mmol/L in 2018.
Reads most evenings.
Total bilirubin 0.6 mg/dL in 2024.
His coworker has a broken finger in a splint.
Sings in a weekly choir.
Drinks two cups of coffee a day.
His partner is being treated for eczema.
Vitamin D 38 ng/mL in 2020 (wellness visit).
Allergic to sulfa antibiotics (hives).
Volunteers at a library.
Albumin 4.1 g/dL in 2022 (routine blood test).
Has a pet dog.

FLIP (answer s'): +Bowel cancer, midway through a course of chemotherapy.

NEAR (answer s): +No colon cancer, past or present.

MISSING (answer neither (undetermined)): +Colorectal cancer: could not be determined from the information available.

PRES (answer s): full text
Patient: male, 35 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Total bilirubin 0.6 mg/dL in 2024.
Volunteers at a library.
His neighbor previously wore dental braces.
Albumin 4.1 g/dL in 2022 (routine blood test).
Eats a varied diet.
Writes with the right hand.
Reads most evenings.
Has a pet dog.
His cousin had a splinter removed from a finger.
Allergic to sulfa antibiotics (hives).
His partner is being treated for eczema.
Chloride 103 mmol/L in 2018.
Sings in a weekly choir.
His coworker has a broken finger in a splint.
Drinks two cups of coffee a day.
Drinks alcohol occasionally.
Vitamin D 38 ng/mL in 2020 (wellness visit).


## 1.48 ('gs151', 'c3', 'numeric', 'easy') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient has ever had asthma (current or past); the current calf swelling compared with the other leg is 3.0 cm or more.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male patient of 88 years.
Suspected chest infection; assessed on the medical ward.
Drives a car.
Current calf swelling 0.1 cm compared with the other leg.
Has two cats.
Prefers to be addressed by first name.
Has symptomatic peripheral artery disease of both legs.

FLIP (answer s'): -Current calf swelling 0.1 cm compared with the other leg. | +Current calf swelling 3.4 cm compared with the other leg.

NEAR (answer s): -Current calf swelling 0.1 cm compared with the other leg. | +Current calf swelling 2.3 cm compared with the other leg.

MISSING (answer neither (undetermined)): -Current calf swelling 0.1 cm compared with the other leg.

PRES (answer s): full text
Man of 88 years.
Suspected chest infection; assessed on the medical ward.
Prefers to be addressed by first name.
Difference in calf circumference now 0.1 cm.
Has two cats.
Drives a car.
Has symptomatic peripheral artery disease of both legs.


## 1.49 ('gs020', 'c1', 'subject', 'easy') templates=train

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient currently has tonsillar exudate or the current systolic blood pressure is above 160 mmHg, prescribe warfarin instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Patient: male, 49 years.
Atrial fibrillation; anticoagulation indicated.
Wears glasses when driving.
Wears a seat belt when driving.
Eats a varied diet.
Systolic blood pressure 148 mmHg at this assessment.
No pus or white patches on the tonsils.

FLIP (answer s'): -No pus or white patches on the tonsils. | +Spots of exudate on the left tonsil.

NEAR (answer s): -No pus or white patches on the tonsils. | +His husband has tonsillitis with white exudate on the tonsils.

MISSING (answer neither (undetermined)): -No pus or white patches on the tonsils. | +Tonsillar exudate: not asked about.

PRES (answer s): full text
49-year-old man.
Atrial fibrillation; anticoagulation indicated.
Wears glasses when driving.
Wears a seat belt when driving.
Eats a varied diet.
No pus or white patches on the tonsils.
Blood pressure 148/93 mmHg this morning.


## 1.50 ('gs184', 'c1', 'time', 'easy') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the current serum potassium is above 5.0 mmol/L; the patient is currently taking warfarin; the patient has ever had coronary artery disease (current or past).
CONDITION: serum potassium above 5.0
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female patient of 38 years.
Requests contraception.
Cardiac stress test unremarkable last year.
Records from 2012 list serum potassium at 4.6 mmol/L.
Current serum potassium 4.0 mmol/L.
Currently on warfarin, prescribed by the cardiology clinic.
Sleeps seven hours a night.

FLIP (answer s'): -Current serum potassium 4.0 mmol/L. | +Current serum potassium 5.4 mmol/L.

NEAR (answer s): -Records from 2012 list serum potassium at 4.6 mmol/L. | +Records from 2012 list serum potassium at 6.1 mmol/L.

MISSING (answer neither (undetermined)): -Records from 2012 list serum potassium at 4.6 mmol/L. | -Current serum potassium 4.0 mmol/L.

PRES (answer s): full text
Woman of 38 years.
Requests contraception.
Sleeps seven hours a night.
Cardiac stress test unremarkable last year.
Currently on warfarin, prescribed by the cardiology clinic.
Back in 2012, serum potassium stood at 4.6 mmol/L.
Latest potassium result: 4.0 mmol/L.


## 1.51 ('hasbled', 'sbp', 'boundary', 'easy') templates=train

RULE: HAS-BLED (as used here, partial): 1 point each for a current systolic blood pressure above 160 mmHg; a major bleeding event at any time; age above 65 years; current use of aspirin. Other HAS-BLED items are not part of this question.
CONDITION: systolic blood pressure above 160
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 1 point.'

BASE (answer s):
Male patient.
Atrial fibrillation; anticoagulation being considered.
Uses public transport.
Age as of today: 50 years.
Speaks English and Spanish.
Blood pressure 142/89 mmHg this morning.
No melena or hematemesis.
No platelet-inhibiting drugs on the medication list.

FLIP (answer s'): -Blood pressure 142/89 mmHg this morning. | +Blood pressure 170/106 mmHg this morning.

NEAR (answer s): -Blood pressure 142/89 mmHg this morning. | +Blood pressure 160/100 mmHg this morning.

MISSING (answer neither (undetermined)): -Blood pressure 142/89 mmHg this morning.

PRES (answer s): full text
Adult man.
Atrial fibrillation; anticoagulation being considered.
No melena or hematemesis.
Speaks English and Spanish.
Uses public transport.
Age today: 50 years.
Manual cuff blood pressure today: 142/89 mmHg.
No platelet-inhibiting drugs on the medication list.


## 1.52 ('gs026', 'c2', 'negation', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If at least two of the following apply, prescribe naproxen with omeprazole instead: the patient currently has tender anterior cervical lymph nodes; the patient has ever had asthma (current or past); the patient has active cancer.
CONDITION: asthma at any time
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Woman of 58 years.
Hip osteoarthritis with pain on walking.
Photographs local wildlife.
Teeth in good repair.
Inhaler use: none.
Has melanoma skin cancer and is receiving treatment for it.
Neck palpation unremarkable.

FLIP (answer s'): -Inhaler use: none. | +Persistent asthma, using a rescue inhaler most weeks.

NEAR (answer s): -Inhaler use: none. | +Has never had asthma.

MISSING (answer neither (undetermined)): -Inhaler use: none. | +Asthma at any time: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 58 years.
Hip osteoarthritis with pain on walking.
Photographs local wildlife.
Teeth in good repair.
Inhaler use: none.
Has melanoma skin cancer and is receiving treatment for it.
Neck palpation unremarkable.


## 1.53 ('gs094', 'c2', 'numeric', 'long') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current eGFR is below 50 mL/min/1.73 m2; the current ALT is above 120 U/L; the age of the patient is 75 years or more.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Patient: male.
Spreading redness and warmth of the right shin for two days.
Non-smoker.
Liver tests today: ALT 26 U/L.
Ferritin 60 ng/mL in 2011.
Speaks English and Spanish.
Vaccinations up to date.
Hearing normal to conversation.
Reads most evenings.
His neighbor is being treated for eczema.
Lives on a quiet street.
Volunteers at a library.
Age as of today: 66 years.
Eats a varied diet.
Drinks two cups of coffee a day.
His cousin broke a wrist, which has healed.
Collects postcards.
Drinks plenty of water.
TSH 1.6 mIU/L in 2022.
Drinks alcohol occasionally.
His husband completed physical therapy for a shoulder injury.
eGFR 36 mL/min/1.73 m2 on today's labs.

FLIP (answer s'): -Liver tests today: ALT 26 U/L. | +Liver tests today: ALT 260 U/L.

NEAR (answer s): -Liver tests today: ALT 26 U/L. | +Liver tests today: ALT 112 U/L.

MISSING (answer neither (undetermined)): -Liver tests today: ALT 26 U/L.

PRES (answer s): full text
Adult man.
Spreading redness and warmth of the right shin for two days.
His neighbor is being treated for eczema.
Ferritin 60 ng/mL in 2011.
eGFR today: 36 mL/min/1.73 m2.
Vaccinations up to date.
Drinks plenty of water.
His cousin broke a wrist, which has healed.
Hearing normal to conversation.
TSH 1.6 mIU/L in 2022.
Non-smoker.
His husband completed physical therapy for a shoulder injury.
Drinks two cups of coffee a day.
Volunteers at a library.
Eats a varied diet.
Collects postcards.
ALT today: 26 U/L.
Age today: 66 years.
Reads most evenings.
Drinks alcohol occasionally.
Speaks English and Spanish.
Lives on a quiet street.


## 1.54 ('gs062', 'c2', 'subject', 'long') templates=test

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If at least two of the following apply, prescribe dapagliflozin instead: the patient is currently taking aspirin; the patient has ever had angioedema (current or past); the patient currently has tender anterior cervical lymph nodes.
CONDITION: angioedema
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Male patient of 65 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Owns a bicycle.
Drives a car.
Has two cats.
His wife lives with psoriasis.
Lives in a second-floor apartment.
Photographs local wildlife.
In 2008, folate was 12 ng/mL.
Currently on low-dose aspirin for heart protection.
Zinc of 85 mcg/dL in 2016.
During a checkup in 2014, total protein was 7.0 g/dL.
Prefers morning appointments.
Neck palpation unremarkable.
His wife sprained a thumb last month.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Knits as a hobby.
Sleeps seven hours a night.
Uses sunscreen in summer.
Enjoys board games.
Teeth in good repair.
Prefers to be addressed by first name.
Face and neck without swelling on examination.
Plays the piano.

FLIP (answer s'): -Face and neck without swelling on examination. | +Formerly had recurrent angioedema, in remission for many years now.

NEAR (answer s): -Face and neck without swelling on examination. | +His roommate recovered from an episode of angioedema in 2016.

MISSING (answer neither (undetermined)): -Face and neck without swelling on examination. | +Angioedema: status unclear from the records at hand.

PRES (answer s): full text
Man of 65 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Owns a bicycle.
Photographs local wildlife.
Prefers morning appointments.
Knits as a hobby.
In 2008, folate was 12 ng/mL.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Face and neck without swelling on examination.
Uses sunscreen in summer.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Neck palpation unremarkable.
Zinc of 85 mcg/dL in 2016.
Plays the piano.
Teeth in good repair.
His wife lives with psoriasis.
Currently on low-dose aspirin for heart protection.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
Has two cats.
During a checkup in 2014, total protein was 7.0 g/dL.
Drives a car.
Enjoys board games.
Lives in a second-floor apartment.


## 1.55 ('gs208', 'c1', 'time', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient is currently taking warfarin and the patient has ever had coronary artery disease (current or past), prescribe azithromycin instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Male, 38 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Hearing normal to conversation.
Does crossword puzzles.
Keeps houseplants.
No INR monitoring in place.
Coronary artery disease on ongoing treatment.
Watches football on weekends.

FLIP (answer s'): -No INR monitoring in place. | +Takes warfarin daily, with the dose adjusted to the INR.

NEAR (answer s): -No INR monitoring in place. | +Warfarin, taken for six weeks after leg fracture surgery, has been stopped.

MISSING (answer neither (undetermined)): -No INR monitoring in place. | +Warfarin: not yet assessed.

PRES (answer s): full text
Patient: male, 38 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Does crossword puzzles.
Watches football on weekends.
Hearing normal to conversation.
No INR monitoring in place.
Keeps houseplants.
Coronary artery disease on ongoing treatment.


## 1.56 ('c3_nice_step1', 'age', 'boundary', 'long') templates=test

RULE: For newly diagnosed hypertension, prescribe amlodipine. If the patient's current age is below 55 years or the patient has ever had diabetes (current or past), prescribe ramipril instead.
CONDITION: age below 55
CLAIMS: s = 'Prescribe amlodipine.' | s' = 'Prescribe ramipril.'

BASE (answer s):
Woman, adult.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Current age 70 years.
Free T4 of 1.2 ng/dL in 2024.
Enjoys board games.
Teeth in good repair.
HbA1c 5.3% at a routine check.
Uses sunscreen in summer.
Her friend has a lazy eye.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Sees a dentist yearly.
Knits as a hobby.
Drives a car.
Photographs local wildlife.
Prefers morning appointments.
Her friend lives with psoriasis.
Owns a bicycle.
In 2006, folate was 12 ng/mL.
Plays the piano.

FLIP (answer s'): -Current age 70 years. | +Current age 44 years.

NEAR (answer s): -Current age 70 years. | +Current age 55 years.

MISSING (answer neither (undetermined)): -Current age 70 years.

PRES (answer s): full text
An adult woman.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Free T4 of 1.2 ng/dL in 2024.
Plays the piano.
Uses sunscreen in summer.
In 2006, folate was 12 ng/mL.
Teeth in good repair.
Her friend lives with psoriasis.
Owns a bicycle.
Prefers morning appointments.
Drives a car.
Her friend has a lazy eye.
Sees a dentist yearly.
HbA1c 5.3% at a routine check.
Currently aged 70 years.
Prefers to be addressed by first name.
Enjoys board games.
Photographs local wildlife.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Knits as a hobby.


## 1.57 ('gs196', 'c2', 'negation', 'long') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. If the patient is currently taking warfarin and the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe acetaminophen instead.
CONDITION: vascular disease
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: male, 51 years.
Knee osteoarthritis with pain on walking.
Does crossword puzzles.
His mother is being treated for eczema.
Has a pet dog.
Takes warfarin daily, with the dose adjusted to the INR.
Wears a seat belt when driving.
Sings in a weekly choir.
Chloride 103 mmol/L in 2012.
Wears glasses when driving.
Serum calcium 9.4 mg/dL in 2020.
Toes warm, with brisk capillary refill.
Bicarbonate 26 mmol/L in 2011 (annual physical).
His aunt is nearsighted.
His brother broke a wrist, which has healed.
Bakes bread at home.
Lives on a quiet street.
Keeps houseplants.
Reads most evenings.
Grows tomatoes in the garden.
Writes with the right hand.
His brother had a splinter removed from a finger.
Drinks plenty of water.
Vaccinations up to date.

FLIP (answer s'): -Toes warm, with brisk capillary refill. | +Has peripheral artery disease.

NEAR (answer s): -Toes warm, with brisk capillary refill. | +Denies ever having had a myocardial infarction or peripheral artery disease.

MISSING (answer neither (undetermined)): -Toes warm, with brisk capillary refill. | +Vascular disease: not asked about.

PRES (answer s): full text
Male, 51 years.
Knee osteoarthritis with pain on walking.
Does crossword puzzles.
Bicarbonate 26 mmol/L in 2011 (annual physical).
Sings in a weekly choir.
Wears a seat belt when driving.
Writes with the right hand.
Has a pet dog.
Vaccinations up to date.
Reads most evenings.
Lives on a quiet street.
His brother broke a wrist, which has healed.
Grows tomatoes in the garden.
Bakes bread at home.
His mother is being treated for eczema.
Toes warm, with brisk capillary refill.
Takes warfarin daily, with the dose adjusted to the INR.
Serum calcium 9.4 mg/dL in 2020.
Drinks plenty of water.
His aunt is nearsighted.
His brother had a splinter removed from a finger.
Chloride 103 mmol/L in 2012.
Keeps houseplants.
Wears glasses when driving.


## 1.58 ('s2_hemorr2hages', 'age', 'numeric', 'long') templates=test

RULE: HEMORR2HAGES score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for active cancer, a current age above 75 years, and current use of aspirin. Other HEMORR2HAGES items are not part of this question.
CONDITION: age above 75
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Atrial fibrillation; warfarin therapy under consideration.
Her friend burned a hand on a stove years ago.
Her roommate lives with psoriasis.
Plays the piano.
During a checkup in 2021, free T3 was 3.2 pg/mL.
In 2009, folate was 12 ng/mL.
Enjoys board games.
Sees a dentist yearly.
Oncology follow-up: none.
Sleeps seven hours a night.
Free T4 of 1.2 ng/dL in 2013.
Current age 69 years.
Drives a car.
Teeth in good repair.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Her roommate has a lazy eye.
Owns a bicycle.

FLIP (answer s'): -Current age 69 years. | +Current age 81 years.

NEAR (answer s): -Current age 69 years. | +Current age 74 years.

MISSING (answer neither (undetermined)): -Current age 69 years.

PRES (answer s): full text
An adult woman.
Atrial fibrillation; warfarin therapy under consideration.
Sees a dentist yearly.
Prefers to be addressed by first name.
Enjoys board games.
Sleeps seven hours a night.
Oncology follow-up: none.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Teeth in good repair.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2013.
In 2009, folate was 12 ng/mL.
Owns a bicycle.
Plays the piano.
Her roommate lives with psoriasis.
Her roommate has a lazy eye.
Currently aged 69 years.
Her friend burned a hand on a stove years ago.
Drives a car.


## 1.59 ('gs026', 'c1', 'subject', 'long') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If at least two of the following apply, prescribe naproxen with omeprazole instead: the patient currently has tender anterior cervical lymph nodes; the patient has ever had asthma (current or past); the patient has active cancer.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Male, 56 years.
Hip osteoarthritis with pain on walking.
Takes oral targeted therapy for active chronic myeloid leukemia.
Drinks two cups of coffee a day.
His coworker has a broken finger in a splint.
Speaks English and Spanish.
Does crossword puzzles.
No tender swellings in the neck.
Vaccinations up to date.
Enjoys cooking.
Has a pet dog.
Eats a varied diet.
Chloride 103 mmol/L in 2015.
Height 170 cm.
Takes no inhaled medicines.
Listens to podcasts.
Magnesium 2.0 mg/dL in 2009.
His partner has a chipped front tooth.
Phosphate 3.6 mg/dL in 2020.
Ferritin 60 ng/mL in 2009.

FLIP (answer s'): -No tender swellings in the neck. | +The anterior cervical lymph nodes are tender today, more so on the right.

NEAR (answer s): -No tender swellings in the neck. | +His housemate has tender lymph nodes at the front of the neck.

MISSING (answer neither (undetermined)): -No tender swellings in the neck. | +Information on tender cervical lymph nodes was not obtained.

PRES (answer s): full text
56-year-old man.
Hip osteoarthritis with pain on walking.
Takes oral targeted therapy for active chronic myeloid leukemia.
Speaks English and Spanish.
Does crossword puzzles.
Listens to podcasts.
Drinks two cups of coffee a day.
Ferritin 60 ng/mL in 2009.
Magnesium 2.0 mg/dL in 2009.
No tender swellings in the neck.
Enjoys cooking.
His coworker has a broken finger in a splint.
Phosphate 3.6 mg/dL in 2020.
Takes no inhaled medicines.
Eats a varied diet.
Chloride 103 mmol/L in 2015.
Vaccinations up to date.
His partner has a chipped front tooth.
Height 170 cm.
Has a pet dog.


## 1.60 ('gs222', 'c1', 'time', 'long') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the current calf swelling compared with the other leg is 3.0 cm or more; the patient currently has tonsillar exudate; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Man of 84 years.
First day after elective total hip replacement.
During a checkup in 2012, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2020.
Records from 2021 list calf swelling at 0.4 cm.
His friend burned a hand on a stove years ago.
Owns a bicycle.
Zinc of 85 mcg/dL in 2021.
Difference in calf circumference now 0.9 cm.
Enjoys board games.
Uses sunscreen in summer.
Sees a dentist yearly.
His sister had a DVT years ago.
Prefers to be addressed by first name.
In 2009, folate was 12 ng/mL.
Paints watercolors as a hobby.
His sister wears contact lenses.
Pupils equal and reactive to light.
Drives a car.
His wife lives with psoriasis.
Photographs local wildlife.
Teeth in good repair.
Lives in a second-floor apartment.
His roommate sprained a thumb last month.

FLIP (answer s'): -Difference in calf circumference now 0.9 cm. | +Difference in calf circumference now 4.8 cm.

NEAR (answer s): -Records from 2021 list calf swelling at 0.4 cm. | +Records from 2021 list calf swelling at 3.7 cm.

MISSING (answer neither (undetermined)): -Records from 2021 list calf swelling at 0.4 cm. | -Difference in calf circumference now 0.9 cm.

PRES (answer s): full text
Male patient of 84 years.
First day after elective total hip replacement.
Uses sunscreen in summer.
Drives a car.
His sister had a DVT years ago.
Pupils equal and reactive to light.
His sister wears contact lenses.
Current calf swelling 0.9 cm compared with the other leg.
Lives in a second-floor apartment.
Owns a bicycle.
Teeth in good repair.
Zinc of 85 mcg/dL in 2021.
In 2009, folate was 12 ng/mL.
His friend burned a hand on a stove years ago.
His wife lives with psoriasis.
During a checkup in 2012, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
His roommate sprained a thumb last month.
Back in 2021, calf swelling stood at 0.4 cm.
Enjoys board games.
Sees a dentist yearly.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2020.
Prefers to be addressed by first name.


## 1.61 ('c1_methimazole', 'alt', 'boundary', 'alt') templates=train

RULE: For Graves' hyperthyroidism, prescribe methimazole. If the current ALT is above 120 U/L, prescribe radioactive iodine instead.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe methimazole.' | s' = 'Prescribe radioactive iodine.'

BASE (answer s):
Patient: male, 36 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Plays chess online.
Bakes bread at home.
Grows tomatoes in the garden.
Uses public transport.
Liver tests today: ALT 78 U/L.

FLIP (answer s'): -Liver tests today: ALT 78 U/L. | +Liver tests today: ALT 199 U/L.

NEAR (answer s): -Liver tests today: ALT 78 U/L. | +Liver tests today: ALT 120 U/L.

MISSING (answer neither (undetermined)): -Liver tests today: ALT 78 U/L.

PRES (answer s): full text
36-year-old man.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Uses public transport.
Plays chess online.
Bakes bread at home.
ALT on blood drawn this morning: 78 U/L.
Grows tomatoes in the garden.


## 1.62 ('padua', 'hf', 'negation', 'easy') templates=test

RULE: Padua prediction score (as used here, partial): 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. Other Padua items are not part of this question.
CONDITION: heart failure
CLAIMS: s = 'The heart failure criterion contributes 0 points.' | s' = 'The heart failure criterion contributes 1 point.'

BASE (answer s):
Man, adult.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Prefers to be addressed by first name.
Sleeps flat on one pillow.
Uses sunscreen in summer.
Varicose veins: none seen.
Photographs local wildlife.
Currently aged 50 years.

FLIP (answer s'): -Sleeps flat on one pillow. | +Current heart failure with ankle swelling.

NEAR (answer s): -Sleeps flat on one pillow. | +Has never had heart failure.

MISSING (answer neither (undetermined)): -Sleeps flat on one pillow. | +Heart failure: status unclear from the records at hand.

PRES (answer s): full text
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Photographs local wildlife.
Uses sunscreen in summer.
Sleeps flat on one pillow.
Prefers to be addressed by first name.
Current age 50 years.
Varicose veins: none seen.


## 1.63 ('gs218', 'c1', 'numeric', 'long') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the current serum creatinine is above 2.0 mg/dL or the patient currently has a mechanical heart valve, prescribe clindamycin instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Female, 53 years.
Spreading redness and warmth of the right shin for two days.
Magnesium 2.0 mg/dL in 2016.
Speaks English and Spanish.
TSH 1.6 mIU/L in 2015.
Vitamin B12 450 pg/mL in 2020.
Height 170 cm.
Grows tomatoes in the garden.
Plays chess online.
Not on anticoagulation at present.
Blood panel at this assessment: creatinine 0.9 mg/dL.
Non-smoker.
Her neighbor had a splinter removed from a finger.
Collects postcards.
Total bilirubin 0.6 mg/dL in 2008.
Wears a seat belt when driving.
Writes with the right hand.
Her coworker has a chipped front tooth.
Vaccinations up to date.
Drinks two cups of coffee a day.

FLIP (answer s'): -Blood panel at this assessment: creatinine 0.9 mg/dL. | +Blood panel at this assessment: creatinine 3.6 mg/dL.

NEAR (answer s): -Blood panel at this assessment: creatinine 0.9 mg/dL. | +Blood panel at this assessment: creatinine 1.8 mg/dL.

MISSING (answer neither (undetermined)): -Blood panel at this assessment: creatinine 0.9 mg/dL.

PRES (answer s): full text
53 years old, female.
Spreading redness and warmth of the right shin for two days.
Grows tomatoes in the garden.
Writes with the right hand.
Vitamin B12 450 pg/mL in 2020.
Non-smoker.
Speaks English and Spanish.
Height 170 cm.
Total bilirubin 0.6 mg/dL in 2008.
Plays chess online.
Drinks two cups of coffee a day.
Her neighbor had a splinter removed from a finger.
Magnesium 2.0 mg/dL in 2016.
TSH 1.6 mIU/L in 2015.
Wears a seat belt when driving.
Serum creatinine today: 0.9 mg/dL.
Collects postcards.
Her coworker has a chipped front tooth.
Vaccinations up to date.
Not on anticoagulation at present.


## 1.64 ('gs191', 'c2', 'subject', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the current eGFR is below 30 mL/min/1.73 m2 and the patient is currently taking warfarin, prescribe acetaminophen instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Female patient of 67 years.
Acute low back pain after lifting.
Zinc of 85 mcg/dL in 2013.
Photographs local wildlife.
Prefers to be addressed by first name.
During a checkup in 2012, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Plays the piano.
Prefers morning appointments.
Teeth in good repair.
eGFR now 23 mL/min/1.73 m2.
Enjoys board games.
Lives in a second-floor apartment.
In 2020, lipase was 30 U/L.
Sees a dentist yearly.
Her friend sprained a thumb last month.
Knits as a hobby.
Her sister burned a hand on a stove years ago.

FLIP (answer s'): +Anticoagulated with warfarin; INR checked monthly at the clinic.

NEAR (answer s): +Her sister is anticoagulated with warfarin.

MISSING (answer neither (undetermined)): +Warfarin: status unclear from the records at hand.

PRES (answer s): full text
Woman of 67 years.
Acute low back pain after lifting.
In 2020, lipase was 30 U/L.
Knits as a hobby.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
During a checkup in 2012, total protein was 7.0 g/dL.
Prefers morning appointments.
Enjoys board games.
Current eGFR 23 mL/min/1.73 m2.
Teeth in good repair.
Zinc of 85 mcg/dL in 2013.
Sees a dentist yearly.
Photographs local wildlife.
Her sister burned a hand on a stove years ago.
Prefers to be addressed by first name.
Plays the piano.
Her friend sprained a thumb last month.


## 1.65 ('gs172', 'c1', 'time', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient currently has tonsillar exudate or the age of the patient is 75 years or more, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Adult woman.
Suspected chest infection; assessed on the medical ward.
Drinks plenty of water.
Vaccinations up to date.
Listens to podcasts.
Age at this assessment: 61 years.

FLIP (answer s'): +Spots of exudate on the left tonsil.

NEAR (answer s): +Tonsillar exudate during tonsillitis in 2022, resolved with antibiotics.

MISSING (answer neither (undetermined)): +Tonsillar exudate: not asked about.

PRES (answer s): full text
Patient: female.
Suspected chest infection; assessed on the medical ward.
Listens to podcasts.
Drinks plenty of water.
Vaccinations up to date.
Age today: 61 years.


## 1.66 ('gs055', 'c1', 'boundary', 'long') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current heart rate is above 90/min or the current respiratory rate is 25/min or more, prescribe aspirin plus clopidogrel instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Man of 48 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Observations now: respiratory rate 19/min.
Free T4 of 1.2 ng/dL in 2021.
His roommate burned a hand on a stove years ago.
His wife lives with psoriasis.
Prefers to be addressed by first name.
In 2009, folate was 12 ng/mL.
Drives a car.
Prefers morning appointments.
His sister has recovered from a dislocated finger.
During a checkup in 2005, total protein was 7.0 g/dL.
Teeth in good repair.
Enjoys board games.
Owns a bicycle.
Sleeps seven hours a night.
Heart rate now 71/min on a pulse check.
Paints watercolors as a hobby.
His father sprained a thumb last month.

FLIP (answer s'): -Heart rate now 71/min on a pulse check. | +Heart rate now 101/min on a pulse check.

NEAR (answer s): -Heart rate now 71/min on a pulse check. | +Heart rate now 90/min on a pulse check.

MISSING (answer neither (undetermined)): -Heart rate now 71/min on a pulse check.

PRES (answer s): full text
Male patient of 48 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current heart rate 71/min.
Sleeps seven hours a night.
Drives a car.
During a checkup in 2005, total protein was 7.0 g/dL.
In 2009, folate was 12 ng/mL.
His wife lives with psoriasis.
Free T4 of 1.2 ng/dL in 2021.
Prefers morning appointments.
Teeth in good repair.
His roommate burned a hand on a stove years ago.
Enjoys board games.
His sister has recovered from a dislocated finger.
Owns a bicycle.
His father sprained a thumb last month.
Current respiratory rate 19/min.
Paints watercolors as a hobby.
Prefers to be addressed by first name.


## 1.67 ('c3_nice_step1', 'diabetes', 'negation', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe amlodipine. If the patient's current age is below 55 years or the patient has ever had diabetes (current or past), prescribe ramipril instead.
CONDITION: diabetes at any time
CLAIMS: s = 'Prescribe amlodipine.' | s' = 'Prescribe ramipril.'

BASE (answer s):
Sex: female.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Age today: 73 years.
Collects postcards.
Reads most evenings.
Her brother had a splinter removed from a finger.
Lives on a quiet street.
Her brother broke a wrist, which has healed.
Wears glasses when driving.
Volunteers at a library.
Vaccinations up to date.
TSH 1.6 mIU/L in 2006.
Eats a varied diet.
Her cousin is left-handed.
Listens to podcasts.
Uses public transport.
Vitamin D 38 ng/mL in 2022 (wellness visit).
Magnesium 2.0 mg/dL in 2017.
Her cousin wears hearing aids.
No excessive thirst or urination.
Keeps houseplants.

FLIP (answer s'): -No excessive thirst or urination. | +Type 2 diabetes diagnosed in 2012, resolved after weight loss.

NEAR (answer s): -No excessive thirst or urination. | +No diabetes at any time.

MISSING (answer neither (undetermined)): -No excessive thirst or urination. | +Diabetes at any time: not yet assessed.

PRES (answer s): full text
Adult woman.
Newly diagnosed hypertension (clinic blood pressure 158/98 mmHg, confirmed by home readings).
Listens to podcasts.
Her cousin is left-handed.
Volunteers at a library.
Uses public transport.
Vitamin D 38 ng/mL in 2022 (wellness visit).
Reads most evenings.
Vaccinations up to date.
Magnesium 2.0 mg/dL in 2017.
Her cousin wears hearing aids.
No excessive thirst or urination.
Age 73 years, calculated today from the date of birth.
Wears glasses when driving.
Her brother broke a wrist, which has healed.
Collects postcards.
Keeps houseplants.
Eats a varied diet.
Her brother had a splinter removed from a finger.
Lives on a quiet street.
TSH 1.6 mIU/L in 2006.


## 1.68 ('gs163', 'c1', 'numeric', 'long') templates=test

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the current heart rate is above 90/min, prescribe doxycycline instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Man of 56 years.
Productive cough and fever; consolidation on chest radiograph.
Pupils equal and reactive to light.
In 2005, lipase was 30 U/L.
His uncle has a lazy eye.
Paints watercolors as a hobby.
Teeth in good repair.
His father has recovered from a dislocated finger.
Drives a car.
Plays the piano.
Has two cats.
Uses sunscreen in summer.
Prefers to be addressed by first name.
His roommate sprained a thumb last month.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Prefers morning appointments.
Owns a bicycle.
His roommate burned a hand on a stove years ago.
Sleeps seven hours a night.
Enjoys board games.
Current heart rate 78/min.

FLIP (answer s'): -Current heart rate 78/min. | +Current heart rate 119/min.

NEAR (answer s): -Current heart rate 78/min. | +Current heart rate 88/min.

MISSING (answer neither (undetermined)): -Current heart rate 78/min.

PRES (answer s): full text
Male patient of 56 years.
Productive cough and fever; consolidation on chest radiograph.
In 2005, lipase was 30 U/L.
His father has recovered from a dislocated finger.
His roommate burned a hand on a stove years ago.
His uncle has a lazy eye.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Plays the piano.
Prefers to be addressed by first name.
Heart rate now 78/min on a pulse check.
Drives a car.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Owns a bicycle.
Teeth in good repair.
Prefers morning appointments.
Enjoys board games.
Sleeps seven hours a night.
His roommate sprained a thumb last month.
Has two cats.
Uses sunscreen in summer.


## 1.69 ('gs009', 'c2', 'subject', 'long') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the current temperature is above 38.0 C and the patient has ever had heart failure (current or past), prescribe azithromycin instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
67-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Total bilirubin 0.6 mg/dL in 2005.
Speaks English and Spanish.
Non-smoker.
Temperature checked with a digital thermometer today: 39.3 C.
Enjoys cooking.
Feeds birds in the backyard.
Phosphate 3.6 mg/dL in 2008.
Uses a smartphone for reminders.
Jugular venous pressure not raised.
His brother-in-law is left-handed.
Drinks two cups of coffee a day.
His cousin completed physical therapy for a shoulder injury.
Drinks alcohol occasionally.
His cousin wears hearing aids.
Height 170 cm.
His brother previously wore dental braces.
Uses public transport.
Hearing normal to conversation.

FLIP (answer s'): -Jugular venous pressure not raised. | +Previously treated for heart failure, which resolved; heart function is normal on follow-up.

NEAR (answer s): -Jugular venous pressure not raised. | +His coworker previously took diuretics for heart failure.

MISSING (answer neither (undetermined)): -Jugular venous pressure not raised. | +Information on heart failure was not obtained.

PRES (answer s): full text
Male, 67 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Uses a smartphone for reminders.
His cousin wears hearing aids.
Temperature today: 39.3 C.
Drinks alcohol occasionally.
His cousin completed physical therapy for a shoulder injury.
Height 170 cm.
Hearing normal to conversation.
Speaks English and Spanish.
Phosphate 3.6 mg/dL in 2008.
Uses public transport.
Jugular venous pressure not raised.
His brother-in-law is left-handed.
Drinks two cups of coffee a day.
Feeds birds in the backyard.
Total bilirubin 0.6 mg/dL in 2005.
Enjoys cooking.
Non-smoker.
His brother previously wore dental braces.


## 1.70 ('two_throat', 'temp', 'time', 'long') templates=test

RULE: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the current temperature is above 38.0 C; the patient currently has tonsillar exudate; the patient currently has tender anterior cervical lymph nodes.
CONDITION: temperature above 38.0
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Man of 35 years.
Sore throat for two days.
Lives in a second-floor apartment.
Owns a bicycle.
Back in 2019, temperature stood at 37.3 C.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2017.
Teeth in good repair.
Paints watercolors as a hobby.
His friend wears contact lenses.
Uses sunscreen in summer.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Photographs local wildlife.
Drives a car.
Tonsils swollen and coated with yellow exudate.
Has two cats.
Neck palpation unremarkable.
Enjoys board games.
Current temperature 36.8 C.
Prefers morning appointments.
His uncle burned a hand on a stove years ago.
Plays the piano.
Knits as a hobby.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.

FLIP (answer s'): -Current temperature 36.8 C. | +Current temperature 39.1 C.

NEAR (answer s): -Back in 2019, temperature stood at 37.3 C. | +Back in 2019, temperature stood at 39.7 C.

MISSING (answer neither (undetermined)): -Back in 2019, temperature stood at 37.3 C. | -Current temperature 36.8 C.

PRES (answer s): full text
Male patient of 35 years.
Sore throat for two days.
Has two cats.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Owns a bicycle.
Prefers morning appointments.
Drives a car.
Free T4 of 1.2 ng/dL in 2017.
Temperature now 36.8 C (tympanic).
His uncle burned a hand on a stove years ago.
Photographs local wildlife.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Teeth in good repair.
Neck palpation unremarkable.
Records from 2019 list temperature at 37.3 C.
Enjoys board games.
During a checkup in 2009, free T3 was 3.2 pg/mL.
His friend wears contact lenses.
Knits as a hobby.
Tonsils swollen and coated with yellow exudate.
Plays the piano.
Sees a dentist yearly.
Uses sunscreen in summer.


## 1.71 ('hf_spironolactone', 'k', 'boundary', 'long') templates=train

RULE: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 5.0 mmol/L, add dapagliflozin instead.
CONDITION: potassium above 5.0
CLAIMS: s = 'Add spironolactone.' | s' = 'Add dapagliflozin.'

BASE (answer s):
68-year-old woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Keeps a step counter.
Ferritin 60 ng/mL in 2022.
Magnesium 2.0 mg/dL in 2017.
Her cousin had a splinter removed from a finger.
Sodium 140 mmol/L in 2017.
Potassium 4.4 mmol/L on today's blood work.
Writes with the right hand.
Her husband completed physical therapy for a shoulder injury.
Her brother-in-law wears hearing aids.
Hearing normal to conversation.
Her husband previously wore dental braces.
Reads most evenings.
Volunteers at a library.
Grows tomatoes in the garden.
Feeds birds in the backyard.
Enjoys gardening.

FLIP (answer s'): -Potassium 4.4 mmol/L on today's blood work. | +Potassium 6.4 mmol/L on today's blood work.

NEAR (answer s): -Potassium 4.4 mmol/L on today's blood work. | +Potassium 5.0 mmol/L on today's blood work.

MISSING (answer neither (undetermined)): -Potassium 4.4 mmol/L on today's blood work.

PRES (answer s): full text
Female, 68 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Her cousin had a splinter removed from a finger.
Grows tomatoes in the garden.
Serum potassium today: 4.4 mmol/L.
Her brother-in-law wears hearing aids.
Keeps a step counter.
Hearing normal to conversation.
Feeds birds in the backyard.
Enjoys gardening.
Sodium 140 mmol/L in 2017.
Her husband completed physical therapy for a shoulder injury.
Ferritin 60 ng/mL in 2022.
Magnesium 2.0 mg/dL in 2017.
Her husband previously wore dental braces.
Reads most evenings.
Volunteers at a library.
Writes with the right hand.


## 1.72 ('s2_chads2', 'htn', 'negation', 'easy') templates=test

RULE: CHADS2 (as used here): 2 points for a stroke or TIA at any time; 1 point each for heart failure at any time, hypertension at any time, diabetes at any time, and a current age of 75 years or more.
CONDITION: hypertension
CLAIMS: s = 'The hypertension criterion contributes 0 points.' | s' = 'The hypertension criterion contributes 1 point.'

BASE (answer s):
An adult man.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Currently aged 58 years.
Teeth in good repair.
Plays the piano.
Prefers to be addressed by first name.
Retinal examination shows healthy vessels.
Gait normal; no focal weakness.

FLIP (answer s'): -Retinal examination shows healthy vessels. | +Currently treated for hypertension with losartan.

NEAR (answer s): -Retinal examination shows healthy vessels. | +Never diagnosed with hypertension.

MISSING (answer neither (undetermined)): -Retinal examination shows healthy vessels. | +Hypertension: status unclear from the records at hand.

PRES (answer s): full text
Man, adult.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Gait normal; no focal weakness.
Current age 58 years.
Teeth in good repair.
Plays the piano.
Prefers to be addressed by first name.
Retinal examination shows healthy vessels.


## 1.73 ('gs011', 'c3', 'numeric', 'long') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the patient currently has a major bleed; the current white cell count is above 12.0 x10^9/L.
CONDITION: white cell count above 12.0
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Patient: male, 84 years.
First day after elective total hip replacement.
Lives on a quiet street.
WBC on the blood count drawn at this assessment: 8.8 x10^9/L.
Height 170 cm.
Coronary artery disease treated with a stent in 2024.
His neighbor has a chipped front tooth.
Sings in a weekly choir.
Keeps houseplants.
Total bilirubin 0.6 mg/dL in 2012.
Nails normal.
His neighbor is nearsighted.
His cousin had a splinter removed from a finger.
Sodium 140 mmol/L in 2017.
Feeds birds in the backyard.
Bakes bread at home.
Plays chess online.
His housemate completed physical therapy for a shoulder injury.
Hearing normal to conversation.
Watches football on weekends.
Drinks plenty of water.
Has a pet dog.

FLIP (answer s'): -WBC on the blood count drawn at this assessment: 8.8 x10^9/L. | +WBC on the blood count drawn at this assessment: 12.8 x10^9/L.

NEAR (answer s): -WBC on the blood count drawn at this assessment: 8.8 x10^9/L. | +WBC on the blood count drawn at this assessment: 11.9 x10^9/L.

MISSING (answer neither (undetermined)): -WBC on the blood count drawn at this assessment: 8.8 x10^9/L.

PRES (answer s): full text
84 years old, male.
First day after elective total hip replacement.
His cousin had a splinter removed from a finger.
Feeds birds in the backyard.
Keeps houseplants.
Sings in a weekly choir.
Plays chess online.
Bakes bread at home.
Height 170 cm.
Nails normal.
Has a pet dog.
Lives on a quiet street.
His neighbor has a chipped front tooth.
Complete blood count this morning: white cell count 8.8 x10^9/L.
Drinks plenty of water.
Coronary artery disease treated with a stent in 2024.
Total bilirubin 0.6 mg/dL in 2012.
Sodium 140 mmol/L in 2017.
His housemate completed physical therapy for a shoulder injury.
Watches football on weekends.
His neighbor is nearsighted.
Hearing normal to conversation.


## 1.74 ('gs133', 'c1', 'subject', 'long') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current systolic blood pressure is 100 mmHg or less; the patient is currently taking aspirin.
CONDITION: colorectal cancer
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Male patient of 62 years.
Spreading redness and warmth of the right shin for two days.
Sees a dentist yearly.
Plays the piano.
Observations now: blood pressure 121/77 mmHg.
Currently on low-dose aspirin for heart protection.
Zinc of 85 mcg/dL in 2014.
In 2016, lipase was 30 U/L.
During a checkup in 2021, total protein was 7.0 g/dL.
His sister has a lazy eye.
Lives in a second-floor apartment.
Has two cats.
His uncle sprained a thumb last month.
Enjoys board games.
Teeth in good repair.
Hemoglobin within the normal range on recent blood tests.
Owns a bicycle.
His sister wears contact lenses.
During a checkup in 2013, free T3 was 3.2 pg/mL.
His friend burned a hand on a stove years ago.

FLIP (answer s'): -Hemoglobin within the normal range on recent blood tests. | +Lives with colon cancer and attends an oncology clinic.

NEAR (answer s): -Hemoglobin within the normal range on recent blood tests. | +His uncle has advanced colorectal cancer.

MISSING (answer neither (undetermined)): -Hemoglobin within the normal range on recent blood tests. | +Colorectal cancer: unknown.

PRES (answer s): full text
Man of 62 years.
Spreading redness and warmth of the right shin for two days.
His uncle sprained a thumb last month.
Enjoys board games.
Plays the piano.
Zinc of 85 mcg/dL in 2014.
Teeth in good repair.
Hemoglobin within the normal range on recent blood tests.
Currently on low-dose aspirin for heart protection.
Owns a bicycle.
During a checkup in 2013, free T3 was 3.2 pg/mL.
His sister has a lazy eye.
His friend burned a hand on a stove years ago.
His sister wears contact lenses.
Current systolic blood pressure 121 mmHg.
Lives in a second-floor apartment.
During a checkup in 2021, total protein was 7.0 g/dL.
Has two cats.
Sees a dentist yearly.
In 2016, lipase was 30 U/L.


## 1.75 ('gs245', 'c3', 'time', 'easy') templates=train

RULE: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has a mechanical heart valve; the current white cell count is above 12.0 x10^9/L; the patient currently has tonsillar exudate.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
23 years old, male.
Sore throat for two days.
Complete blood count this morning: white cell count 20.5 x10^9/L.
Height 170 cm.
Throat mildly red; tonsils not coated.
Auscultation: no clicks or added sounds.

FLIP (answer s'): -Throat mildly red; tonsils not coated. | +Spots of exudate on the left tonsil.

NEAR (answer s): -Throat mildly red; tonsils not coated. | +Previously had white exudate on the tonsils in 2021, since resolved.

MISSING (answer neither (undetermined)): -Throat mildly red; tonsils not coated. | +Tonsillar exudate: not asked about.

PRES (answer s): full text
Patient: male, 23 years.
Sore throat for two days.
Auscultation: no clicks or added sounds.
Height 170 cm.
Throat mildly red; tonsils not coated.
WBC on the blood count drawn at this assessment: 20.5 x10^9/L.
