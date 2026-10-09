# Audit sample 2


## 2.1 ('gs247', 'c1', 'boundary', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current serum potassium is above 4.8 mmol/L or the current oxygen saturation is 91% or less, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: serum potassium above 4.8
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Patient: female, 43 years.
Suspected chest infection; assessed on the medical ward.
Grows tomatoes in the garden.
Potassium measured at this assessment is 3.9 mmol/L.
Oxygen saturation by finger probe today: 98%.

FLIP (answer s'): -Potassium measured at this assessment is 3.9 mmol/L. | +Potassium measured at this assessment is 5.4 mmol/L.

NEAR (answer s): -Potassium measured at this assessment is 3.9 mmol/L. | +Potassium measured at this assessment is 4.8 mmol/L.

MISSING (answer neither (undetermined)): -Potassium measured at this assessment is 3.9 mmol/L.

PRES (answer s): full text
Female, 43 years.
Suspected chest infection; assessed on the medical ward.
Oxygen saturation 98% at rest today.
Grows tomatoes in the garden.
Labs this morning: potassium 3.9 mmol/L.


## 2.2 ('gs107', 'c3', 'negation', 'long') templates=test

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current systolic blood pressure is above 160 mmHg; the patient is currently taking clarithromycin.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Man of 52 years.
Productive cough and fever; consolidation on chest radiograph.
Knits as a hobby.
Bowel cancer cured by surgery years ago, without recurrence.
Photographs local wildlife.
Lives in a second-floor apartment.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2015.
Observations now: blood pressure 118/75 mmHg.
His father wears contact lenses.
Paints watercolors as a hobby.
Teeth in good repair.
His sister lives with psoriasis.
Uses sunscreen in summer.
During a checkup in 2017, total protein was 7.0 g/dL.
Current antibiotic therapy: none.
Drives a car.
Plays the piano.
Prefers to be addressed by first name.
Enjoys board games.
His friend has a lazy eye.
Prefers morning appointments.
Pupils equal and reactive to light.
His friend burned a hand on a stove years ago.
During a checkup in 2018, free T3 was 3.2 pg/mL.

FLIP (answer s'): -Current antibiotic therapy: none. | +Currently taking clarithromycin for an ear infection.

NEAR (answer s): -Current antibiotic therapy: none. | +Has never taken clarithromycin.

MISSING (answer neither (undetermined)): -Current antibiotic therapy: none. | +Clarithromycin: unknown.

PRES (answer s): full text
Male patient of 52 years.
Productive cough and fever; consolidation on chest radiograph.
Prefers morning appointments.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
Current antibiotic therapy: none.
Drives a car.
During a checkup in 2018, free T3 was 3.2 pg/mL.
His father wears contact lenses.
During a checkup in 2017, total protein was 7.0 g/dL.
Enjoys board games.
Plays the piano.
Knits as a hobby.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
His friend has a lazy eye.
Owns a bicycle.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2015.
His sister lives with psoriasis.
Bowel cancer cured by surgery years ago, without recurrence.
Current systolic blood pressure 118 mmHg.
Photographs local wildlife.
His friend burned a hand on a stove years ago.


## 2.3 ('news2_red', 'spo2', 'numeric', 'easy') templates=train

RULE: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.
CONDITION: oxygen saturation at or below 91
CLAIMS: s = 'The oxygen saturation criterion contributes 0 points.' | s' = 'The oxygen saturation criterion contributes 3 points.'

BASE (answer s):
35-year-old woman.
Shortness of breath and fever; assessed on the medical ward.
Lives on a quiet street.
Respiratory rate 15/min at this assessment.
Oxygen saturation at this assessment is 99%.
Systolic blood pressure 140 mmHg at this assessment.
Memory and concentration normal on bedside testing.

FLIP (answer s'): -Oxygen saturation at this assessment is 99%. | +Oxygen saturation at this assessment is 91%.

NEAR (answer s): -Oxygen saturation at this assessment is 99%. | +Oxygen saturation at this assessment is 92%.

MISSING (answer neither (undetermined)): -Oxygen saturation at this assessment is 99%.

PRES (answer s): full text
Patient: female, 35 years.
Shortness of breath and fever; assessed on the medical ward.
Blood pressure 140/88 mmHg this morning.
Memory and concentration normal on bedside testing.
Respiratory rate today: 15/min.
Lives on a quiet street.
Pulse oximetry this morning: oxygen saturation 99%.


## 2.4 ('gs116', 'c1', 'subject', 'easy') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the patient currently has asthma and the patient has had cancer at any time (active or in remission), prescribe aspirin plus clopidogrel instead.
CONDITION: asthma
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Woman of 88 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Knits as a hobby.
Has metastatic lung cancer, receiving palliative treatment.
Plays the piano.
Inhaler use: none.

FLIP (answer s'): -Inhaler use: none. | +Persistent asthma, using a rescue inhaler most weeks.

NEAR (answer s): -Inhaler use: none. | +Her roommate uses an inhaler for asthma.

MISSING (answer neither (undetermined)): -Inhaler use: none. | +Asthma: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 88 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Knits as a hobby.
Plays the piano.
Inhaler use: none.
Has metastatic lung cancer, receiving palliative treatment.


## 2.5 ('c1_allopurinol', 'egfr', 'time', 'long') templates=train

RULE: For urate-lowering therapy in gout, prescribe allopurinol 100 mg daily. If the current eGFR is below 30 mL/min/1.73 m2, prescribe allopurinol 50 mg daily instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe allopurinol 100 mg daily.' | s' = 'Prescribe allopurinol 50 mg daily.'

BASE (answer s):
Patient: male, 77 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Vitamin B12 450 pg/mL in 2018.
Keeps houseplants.
Reads most evenings.
Albumin 4.1 g/dL in 2010 (routine blood test).
Renal function today: eGFR 70 mL/min/1.73 m2.
Bicarbonate 26 mmol/L in 2012 (annual physical).
Keeps a step counter.
Enjoys gardening.
Total bilirubin 0.6 mg/dL in 2006.
In 2018, eGFR was 67 mL/min/1.73 m2.
Wears a seat belt when driving.
Feeds birds in the backyard.
Plays chess online.
Collects postcards.
His husband has a fear of heights.
His husband completed physical therapy for a shoulder injury.
Eats a varied diet.

FLIP (answer s'): -Renal function today: eGFR 70 mL/min/1.73 m2. | +Renal function today: eGFR 20 mL/min/1.73 m2.

NEAR (answer s): -In 2018, eGFR was 67 mL/min/1.73 m2. | +In 2018, eGFR was 27 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Renal function today: eGFR 70 mL/min/1.73 m2. | -In 2018, eGFR was 67 mL/min/1.73 m2.

PRES (answer s): full text
Male, 77 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Feeds birds in the backyard.
Total bilirubin 0.6 mg/dL in 2006.
Enjoys gardening.
Reads most evenings.
Collects postcards.
Plays chess online.
Keeps a step counter.
His husband completed physical therapy for a shoulder injury.
Keeps houseplants.
Bicarbonate 26 mmol/L in 2012 (annual physical).
His husband has a fear of heights.
Eats a varied diet.
Wears a seat belt when driving.
eGFR 67 mL/min/1.73 m2 at a hospital visit in 2018.
eGFR today: 70 mL/min/1.73 m2.
Albumin 4.1 g/dL in 2010 (routine blood test).
Vitamin B12 450 pg/mL in 2018.


## 2.6 ('gs146', 'c1', 'boundary', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Man of 64 years.
Hip osteoarthritis with pain on walking.
Prefers to be addressed by first name.
Knits as a hobby.
Uses sunscreen in summer.
Latest creatinine result: 1.5 mg/dL.

FLIP (answer s'): -Latest creatinine result: 1.5 mg/dL. | +Latest creatinine result: 3.3 mg/dL.

NEAR (answer s): -Latest creatinine result: 1.5 mg/dL. | +Latest creatinine result: 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Latest creatinine result: 1.5 mg/dL.

PRES (answer s): full text
Male patient of 64 years.
Hip osteoarthritis with pain on walking.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Current serum creatinine 1.5 mg/dL.
Knits as a hobby.


## 2.7 ('gs143', 'c3', 'negation', 'long') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient has ever had heparin-induced thrombocytopenia (current or past); the current ALT is above 120 U/L; the patient currently has tonsillar exudate.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
76 years old, male.
First day after elective total hip replacement.
Magnesium 2.0 mg/dL in 2015.
Hearing normal to conversation.
Volunteers at a library.
Heparin-induced thrombocytopenia in 2007, treated with argatroban and resolved within two weeks.
Has a pet dog.
Reads most evenings.
Throat mildly red; tonsils not coated.
Drinks alcohol occasionally.
Bicarbonate 26 mmol/L in 2015 (annual physical).
Eats a varied diet.
Uses public transport.
His cousin is nearsighted.
Does crossword puzzles.
Enjoys gardening.
His husband has a chipped front tooth.
Uses a smartphone for reminders.
Vitamin B12 450 pg/mL in 2009.
Height 170 cm.
Speaks English and Spanish.
Keeps a step counter.
Bakes bread at home.
Plays chess online.
ALT 48 U/L on today's labs.

FLIP (answer s'): -Throat mildly red; tonsils not coated. | +Patchy exudate over the right tonsil.

NEAR (answer s): -Throat mildly red; tonsils not coated. | +Exudate not seen on either tonsil.

MISSING (answer neither (undetermined)): -Throat mildly red; tonsils not coated. | +Tonsillar exudate: not yet assessed.

PRES (answer s): full text
Male, 76 years.
First day after elective total hip replacement.
Does crossword puzzles.
Vitamin B12 450 pg/mL in 2009.
His husband has a chipped front tooth.
Bicarbonate 26 mmol/L in 2015 (annual physical).
Speaks English and Spanish.
Throat mildly red; tonsils not coated.
Magnesium 2.0 mg/dL in 2015.
Drinks alcohol occasionally.
ALT today: 48 U/L.
Hearing normal to conversation.
Reads most evenings.
Height 170 cm.
Eats a varied diet.
Bakes bread at home.
His cousin is nearsighted.
Heparin-induced thrombocytopenia in 2007, treated with argatroban and resolved within two weeks.
Keeps a step counter.
Volunteers at a library.
Has a pet dog.
Plays chess online.
Enjoys gardening.
Uses a smartphone for reminders.
Uses public transport.


## 2.8 ('s1_idsa_minor', 'temp', 'numeric', 'long') templates=test

RULE: IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): 1 point each for a current white cell count below 4.0 x10^9/L; a current platelet count below 100 x10^9/L; a current temperature below 36.0 C; a current blood urea nitrogen of 20 mg/dL or more. Other criteria are not part of this question.
CONDITION: temperature below 36.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
Female patient of 52 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Sees a dentist yearly.
Her father burned a hand on a stove years ago.
Knits as a hobby.
Current temperature 38.2 C.
Paints watercolors as a hobby.
Her friend has a lazy eye.
Platelet count now 169 x10^9/L.
Drives a car.
Prefers to be addressed by first name.
Prefers morning appointments.
Her sister has recovered from a dislocated finger.
Lives in a second-floor apartment.
Has two cats.
Pupils equal and reactive to light.
Teeth in good repair.
Plays the piano.
Photographs local wildlife.
During a checkup in 2013, free T3 was 3.2 pg/mL.
During a checkup in 2005, total protein was 7.0 g/dL.
Owns a bicycle.
Blood urea nitrogen now: 9 mg/dL.
Current white cell count 10.3 x10^9/L.
Sleeps seven hours a night.

FLIP (answer s'): -Current temperature 38.2 C. | +Current temperature 34.5 C.

NEAR (answer s): -Current temperature 38.2 C. | +Current temperature 36.1 C.

MISSING (answer neither (undetermined)): -Current temperature 38.2 C.

PRES (answer s): full text
Woman of 52 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Has two cats.
Pupils equal and reactive to light.
Owns a bicycle.
Knits as a hobby.
Teeth in good repair.
Temperature now 38.2 C (tympanic).
Blood urea nitrogen 9 mg/dL on the current labs.
Prefers morning appointments.
Drives a car.
Her sister has recovered from a dislocated finger.
Latest WBC is 10.3 x10^9/L.
Her friend has a lazy eye.
Sees a dentist yearly.
During a checkup in 2005, total protein was 7.0 g/dL.
Her father burned a hand on a stove years ago.
Photographs local wildlife.
Plays the piano.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Current platelet count 169 x10^9/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Sleeps seven hours a night.


## 2.9 ('gs138', 'c1', 'subject', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the patient currently has heart failure and the current serum potassium is above 5.0 mmol/L, prescribe a progestin-only pill instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female, 21 years.
Requests contraception.
Sings in a weekly choir.
Serum potassium today: 5.7 mmol/L.
Hearing normal to conversation.
Wears glasses when driving.
Jugular venous pressure not raised.

FLIP (answer s'): -Jugular venous pressure not raised. | +Heart failure, under regular review in a cardiology clinic.

NEAR (answer s): -Jugular venous pressure not raised. | +Her grandfather was admitted this morning with heart failure.

MISSING (answer neither (undetermined)): -Jugular venous pressure not raised. | +Current heart failure: could not be determined from the information available.

PRES (answer s): full text
21-year-old woman.
Requests contraception.
Potassium measured at this assessment is 5.7 mmol/L.
Wears glasses when driving.
Sings in a weekly choir.
Jugular venous pressure not raised.
Hearing normal to conversation.


## 2.10 ('s1_spesi', 'cancer', 'time', 'easy') templates=test

RULE: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.
CONDITION: active cancer
CLAIMS: s = 'The active cancer criterion contributes 0 points.' | s' = 'The active cancer criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Current systolic blood pressure 117 mmHg.
Oncology follow-up: none.
Current age 65 years.
Current oxygen saturation 98%.
Owns a bicycle.
Current heart rate 75/min.

FLIP (answer s'): -Oncology follow-up: none. | +Has melanoma skin cancer and is receiving treatment for it.

NEAR (answer s): -Oncology follow-up: none. | +Had thyroid cancer years ago and is now cured.

MISSING (answer neither (undetermined)): -Oncology follow-up: none. | +Active cancer: unknown.

PRES (answer s): full text
An adult woman.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Latest oxygen saturation reading: 98%.
Observations now: blood pressure 117/74 mmHg.
Heart rate now 75/min on a pulse check.
Currently aged 65 years.
Owns a bicycle.
Oncology follow-up: none.


## 2.11 ('gs006', 'c1', 'boundary', 'long') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the current heart rate is above 90/min and the patient has ever had a venous thromboembolism (current or past), prescribe doxycycline instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Patient: female, 42 years.
Productive cough and fever; consolidation on chest radiograph.
Her neighbor completed physical therapy for a shoulder injury.
Sodium 140 mmol/L in 2023.
Heart rate today: 81/min.
Enjoys cooking.
Writes with the right hand.
Volunteers at a library.
Serum calcium 9.4 mg/dL in 2023.
Active DVT of the right calf on anticoagulation.
Vitamin B12 450 pg/mL in 2008.
Her coworker is being treated for eczema.
Magnesium 2.0 mg/dL in 2019.
Has a pet dog.
Wears glasses when driving.
Height 170 cm.
Plays chess online.
Her brother-in-law wears hearing aids.
Wears a seat belt when driving.

FLIP (answer s'): -Heart rate today: 81/min. | +Heart rate today: 124/min.

NEAR (answer s): -Heart rate today: 81/min. | +Heart rate today: 90/min.

MISSING (answer neither (undetermined)): -Heart rate today: 81/min.

PRES (answer s): full text
Female, 42 years.
Productive cough and fever; consolidation on chest radiograph.
Vitamin B12 450 pg/mL in 2008.
Active DVT of the right calf on anticoagulation.
Her neighbor completed physical therapy for a shoulder injury.
Sodium 140 mmol/L in 2023.
Writes with the right hand.
Has a pet dog.
Wears a seat belt when driving.
Her coworker is being treated for eczema.
Serum calcium 9.4 mg/dL in 2023.
Enjoys cooking.
Her brother-in-law wears hearing aids.
Wears glasses when driving.
Height 170 cm.
Heart rate 81/min at rest this morning.
Plays chess online.
Magnesium 2.0 mg/dL in 2019.
Volunteers at a library.


## 2.12 ('gs087', 'c2', 'negation', 'long') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the patient currently has tonsillar exudate and the patient is allergic to penicillin, prescribe clindamycin instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Woman of 61 years.
Spreading redness and warmth of the right shin for two days.
Her father has a lazy eye.
Knits as a hobby.
Zinc of 85 mcg/dL in 2017.
Enjoys board games.
Teeth in good repair.
Paints watercolors as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
Tonsils swollen and coated with yellow exudate.
Prefers to be addressed by first name.
Her father sprained a thumb last month.
Has two cats.
Drives a car.
Sees a dentist yearly.
Plays the piano.
Owns a bicycle.
Sleeps seven hours a night.
Pupils equal and reactive to light.
During a checkup in 2012, free T3 was 3.2 pg/mL.

FLIP (answer s'): +Penicillin allergy: anaphylaxis.

NEAR (answer s): +Has never been allergic to penicillin.

MISSING (answer neither (undetermined)): +Penicillin allergy: unknown.

PRES (answer s): full text
Female patient of 61 years.
Spreading redness and warmth of the right shin for two days.
Her father sprained a thumb last month.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Knits as a hobby.
Uses sunscreen in summer.
Has two cats.
Tonsils swollen and coated with yellow exudate.
Pupils equal and reactive to light.
Her father has a lazy eye.
Prefers to be addressed by first name.
Teeth in good repair.
Owns a bicycle.
Sleeps seven hours a night.
Sees a dentist yearly.
Paints watercolors as a hobby.
Drives a car.
Enjoys board games.
Plays the piano.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2017.


## 2.13 ('curb65', 'sbp', 'numeric', 'easy') templates=train

RULE: CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
CONDITION: blood pressure below 90
CLAIMS: s = 'The blood pressure criterion contributes 0 points.' | s' = 'The blood pressure criterion contributes 1 point.'

BASE (answer s):
Patient: male.
Community-acquired pneumonia confirmed on chest radiograph.
Enjoys cooking.
Volunteers at a library.
Reads most evenings.
Blood pressure today: 129/81 mmHg.
Age today: 53 years.
Non-smoker.
BUN 16 mg/dL this morning.
Respiratory rate 23/min at this assessment.

FLIP (answer s'): -Blood pressure today: 129/81 mmHg. | +Blood pressure today: 71/47 mmHg.

NEAR (answer s): -Blood pressure today: 129/81 mmHg. | +Blood pressure today: 97/62 mmHg.

MISSING (answer neither (undetermined)): -Blood pressure today: 129/81 mmHg.

PRES (answer s): full text
Adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Volunteers at a library.
Reads most evenings.
Respiratory rate today: 23/min.
Age 53 years, calculated today from the date of birth.
Enjoys cooking.
Today's BUN is 16 mg/dL.
Non-smoker.
Blood pressure 129/81 mmHg this morning.


## 2.14 ('s2_caprini', 'cancer', 'subject', 'easy') templates=test

RULE: Caprini score (as used here, partial): 3 points for a venous thromboembolism of the patient or a first-degree relative (parent, sibling or child) at any time; 2 points for cancer at any time (active or previous); 1 point for a current body mass index above 25.0 kg/m2. Other Caprini items, including age, are not part of this question.
CONDITION: cancer
CLAIMS: s = 'The cancer criterion contributes 0 points.' | s' = 'The cancer criterion contributes 2 points.'

BASE (answer s):
Male patient of 71 years.
Admitted for an emergency bowel resection.
Pupils equal and reactive to light.
Owns a bicycle.
Oncology follow-up: none.
Varicose veins: none seen.
Prefers morning appointments.
Current body mass index 23.9 kg/m2.

FLIP (answer s'): -Oncology follow-up: none. | +Had thyroid cancer years ago and is now cured.

NEAR (answer s): -Oncology follow-up: none. | +His friend has lung cancer that has spread to the liver.

MISSING (answer neither (undetermined)): -Oncology follow-up: none. | +Cancer: status unclear from the records at hand.

PRES (answer s): full text
Man of 71 years.
Admitted for an emergency bowel resection.
Oncology follow-up: none.
Owns a bicycle.
Prefers morning appointments.
Varicose veins: none seen.
Latest BMI is 23.9 kg/m2.
Pupils equal and reactive to light.


## 2.15 ('c1_allopurinol', 'egfr', 'time', 'superseded') templates=train

RULE: For urate-lowering therapy in gout, prescribe allopurinol 100 mg daily. If the current eGFR is below 30 mL/min/1.73 m2, prescribe allopurinol 50 mg daily instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe allopurinol 100 mg daily.' | s' = 'Prescribe allopurinol 50 mg daily.'

BASE (answer s):
Patient: male, 43 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Previously, eGFR was 79 mL/min/1.73 m2; it has since been repeated.
Writes with the right hand.
Renal function today: eGFR 83 mL/min/1.73 m2.
Non-smoker.
Speaks English and Spanish.

FLIP (answer s'): -Renal function today: eGFR 83 mL/min/1.73 m2. | +Renal function today: eGFR 28 mL/min/1.73 m2.

NEAR (answer s): -Previously, eGFR was 79 mL/min/1.73 m2; it has since been repeated. | +Previously, eGFR was 24 mL/min/1.73 m2; it has since been repeated.

MISSING (answer neither (undetermined)): -Previously, eGFR was 79 mL/min/1.73 m2; it has since been repeated. | -Renal function today: eGFR 83 mL/min/1.73 m2.

PRES (answer s): full text
43-year-old man.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Non-smoker.
Previously, eGFR was 79 mL/min/1.73 m2; it has since been repeated.
Writes with the right hand.
Speaks English and Spanish.
eGFR today: 83 mL/min/1.73 m2.


## 2.16 ('t2d_metformin', 'egfr', 'boundary', 'alt') templates=test

RULE: For newly diagnosed type 2 diabetes, start metformin. If the patient's current eGFR is below 45 mL/min/1.73 m2, start sitagliptin instead.
CONDITION: eGFR below 45
CLAIMS: s = 'Start metformin.' | s' = 'Start sitagliptin.'

BASE (answer s):
Woman of 38 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current eGFR 56 mL/min/1.73 m2.
Owns a bicycle.
Prefers morning appointments.
Sleeps seven hours a night.
Paints watercolors as a hobby.

FLIP (answer s'): -Current eGFR 56 mL/min/1.73 m2. | +Current eGFR 34 mL/min/1.73 m2.

NEAR (answer s): -Current eGFR 56 mL/min/1.73 m2. | +Current eGFR 45 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Current eGFR 56 mL/min/1.73 m2.

PRES (answer s): full text
Female patient of 38 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Prefers morning appointments.
Owns a bicycle.
Paints watercolors as a hobby.
eGFR now 56 mL/min/1.73 m2.


## 2.17 ('gs144', 'c2', 'negation', 'long') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the current blood urea nitrogen is above 19 mg/dL and the patient has had cancer at any time (active or in remission), prescribe a progestin-only pill instead.
CONDITION: cancer at any time
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
20-year-old woman.
Requests contraception.
Reads most evenings.
Ferritin 60 ng/mL in 2024.
Bakes bread at home.
Uses a smartphone for reminders.
Does crossword puzzles.
Her brother-in-law has a stutter.
Nails normal.
Grows tomatoes in the garden.
Her brother has a fear of heights.
Lives on a quiet street.
Listens to podcasts.
Eats a varied diet.
Feeds birds in the backyard.
Collects postcards.
Magnesium 2.0 mg/dL in 2024.
Non-smoker.
No unexplained weight loss or new lumps.
Drinks plenty of water.
Drinks alcohol occasionally.
BUN 22 mg/dL this morning.
Drinks two cups of coffee a day.
Phosphate 3.6 mg/dL in 2024.

FLIP (answer s'): -No unexplained weight loss or new lumps. | +Non-Hodgkin lymphoma diagnosed this year, on active treatment.

NEAR (answer s): -No unexplained weight loss or new lumps. | +No leukemia, lymphoma or other cancer at any time.

MISSING (answer neither (undetermined)): -No unexplained weight loss or new lumps. | +Cancer at any time: could not be determined from the information available.

PRES (answer s): full text
Patient: female, 20 years.
Requests contraception.
Magnesium 2.0 mg/dL in 2024.
Drinks two cups of coffee a day.
Uses a smartphone for reminders.
Drinks alcohol occasionally.
Bakes bread at home.
Her brother has a fear of heights.
Eats a varied diet.
Collects postcards.
Ferritin 60 ng/mL in 2024.
Lives on a quiet street.
Drinks plenty of water.
Feeds birds in the backyard.
Grows tomatoes in the garden.
Listens to podcasts.
Non-smoker.
No unexplained weight loss or new lumps.
BUN on today's chemistry panel: 22 mg/dL.
Nails normal.
Her brother-in-law has a stutter.
Phosphate 3.6 mg/dL in 2024.
Reads most evenings.
Does crossword puzzles.


## 2.18 ('gs040', 'c2', 'numeric', 'easy') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has a mechanical heart valve; the current serum creatinine is above 2.0 mg/dL; the patient has ever had a peptic ulcer (current or past).
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Woman of 39 years.
Requests contraception.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Heart sounds free of clicks.
Active peptic ulcer disease.
Latest creatinine result: 1.4 mg/dL.

FLIP (answer s'): -Latest creatinine result: 1.4 mg/dL. | +Latest creatinine result: 4.1 mg/dL.

NEAR (answer s): -Latest creatinine result: 1.4 mg/dL. | +Latest creatinine result: 1.9 mg/dL.

MISSING (answer neither (undetermined)): -Latest creatinine result: 1.4 mg/dL.

PRES (answer s): full text
Female patient of 39 years.
Requests contraception.
Heart sounds free of clicks.
Active peptic ulcer disease.
Current serum creatinine 1.4 mg/dL.
Lives in a second-floor apartment.
Sleeps seven hours a night.


## 2.19 ('gs149', 'c2', 'subject', 'long') templates=train

RULE: For rate control in atrial fibrillation, prescribe metoprolol. If the current blood urea nitrogen is above 19 mg/dL or the patient has ever had heart failure (current or past), prescribe diltiazem instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
79-year-old man.
Atrial fibrillation with a ventricular rate of 128/min.
Listens to podcasts.
Vitamin B12 450 pg/mL in 2011.
Ferritin 60 ng/mL in 2012.
Uses a smartphone for reminders.
Grows tomatoes in the garden.
Bakes bread at home.
His housemate has a stutter.
Eats a varied diet.
Phosphate 3.6 mg/dL in 2006.
His cousin is left-handed.
Enjoys gardening.
Lives on a quiet street.
His neighbor has a fear of heights.
Nails normal.
BUN at this assessment: 17 mg/dL.
His neighbor broke a wrist, which has healed.
Speaks English and Spanish.
Watches football on weekends.
Writes with the right hand.
Chloride 103 mmol/L in 2007.

FLIP (answer s'): +Heart failure with reduced ejection fraction.

NEAR (answer s): +His cousin attends a heart failure clinic.

MISSING (answer neither (undetermined)): +Information on heart failure was not obtained.

PRES (answer s): full text
79 years old, male.
Atrial fibrillation with a ventricular rate of 128/min.
Grows tomatoes in the garden.
Vitamin B12 450 pg/mL in 2011.
Lives on a quiet street.
Eats a varied diet.
Ferritin 60 ng/mL in 2012.
Writes with the right hand.
His housemate has a stutter.
Bakes bread at home.
Speaks English and Spanish.
Uses a smartphone for reminders.
His cousin is left-handed.
Watches football on weekends.
Phosphate 3.6 mg/dL in 2006.
His neighbor has a fear of heights.
His neighbor broke a wrist, which has healed.
Nails normal.
Listens to podcasts.
Chloride 103 mmol/L in 2007.
Today's BUN is 17 mg/dL.
Enjoys gardening.


## 2.20 ('gs083', 'c1', 'time', 'superseded') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current temperature is above 38.0 C and the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe intravenous piperacillin-tazobactam instead.
CONDITION: temperature above 38.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Woman of 74 years.
Suspected chest infection; assessed on the medical ward.
Photographs local wildlife.
Temperature now 36.3 C (tympanic).
Recovered from a heart attack in 2017.
Last month, temperature was 36.2 C; the newest measurement replaces it.
Prefers to be addressed by first name.

FLIP (answer s'): -Temperature now 36.3 C (tympanic). | +Temperature now 39.3 C (tympanic).

NEAR (answer s): -Last month, temperature was 36.2 C; the newest measurement replaces it. | +Last month, temperature was 39.8 C; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Temperature now 36.3 C (tympanic). | -Last month, temperature was 36.2 C; the newest measurement replaces it.

PRES (answer s): full text
Female patient of 74 years.
Suspected chest infection; assessed on the medical ward.
Photographs local wildlife.
Recovered from a heart attack in 2017.
Current temperature 36.3 C.
Prefers to be addressed by first name.
Last month, temperature was 36.2 C; the newest measurement replaces it.


## 2.21 ('gs107', 'c2', 'boundary', 'long') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current systolic blood pressure is above 160 mmHg; the patient is currently taking clarithromycin.
CONDITION: systolic blood pressure above 160
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
56-year-old man.
Productive cough and fever; consolidation on chest radiograph.
Uses public transport.
Watches football on weekends.
Lives on a quiet street.
Drinks two cups of coffee a day.
Bakes bread at home.
Wears a seat belt when driving.
Speaks English and Spanish.
His partner is being treated for eczema.
His brother has colon cancer.
Wears glasses when driving.
Bicarbonate 26 mmol/L in 2020 (annual physical).
Vitamin B12 450 pg/mL in 2019.
Total bilirubin 0.6 mg/dL in 2008.
Volunteers at a library.
His partner is nearsighted.
His housemate has a broken finger in a splint.
Enjoys cooking.
Blood pressure today: 117/74 mmHg.
Keeps houseplants.
Sodium 140 mmol/L in 2022.

FLIP (answer s'): -Blood pressure today: 117/74 mmHg. | +Blood pressure today: 172/107 mmHg.

NEAR (answer s): -Blood pressure today: 117/74 mmHg. | +Blood pressure today: 160/100 mmHg.

MISSING (answer neither (undetermined)): -Blood pressure today: 117/74 mmHg.

PRES (answer s): full text
56 years old, male.
Productive cough and fever; consolidation on chest radiograph.
Lives on a quiet street.
Bakes bread at home.
Wears a seat belt when driving.
Speaks English and Spanish.
His partner is being treated for eczema.
Drinks two cups of coffee a day.
Uses public transport.
Bicarbonate 26 mmol/L in 2020 (annual physical).
His partner is nearsighted.
Watches football on weekends.
Enjoys cooking.
Total bilirubin 0.6 mg/dL in 2008.
His housemate has a broken finger in a splint.
His brother has colon cancer.
Volunteers at a library.
Sodium 140 mmol/L in 2022.
Vitamin B12 450 pg/mL in 2019.
Blood pressure 117/74 mmHg this morning.
Wears glasses when driving.
Keeps houseplants.


## 2.22 ('gs029', 'c1', 'negation', 'easy') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient currently has tender anterior cervical lymph nodes or the current ALT is above 120 U/L, prescribe warfarin instead.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Male patient of 45 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Uses sunscreen in summer.
Sees a dentist yearly.
Lives in a second-floor apartment.
ALT now 57 U/L.

FLIP (answer s'): +Tender, swollen lymph nodes in the front of the neck.

NEAR (answer s): +Neck supple, without tender lymph nodes.

MISSING (answer neither (undetermined)): +Tender cervical lymph nodes: status unclear from the records at hand.

PRES (answer s): full text
Man of 45 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Lives in a second-floor apartment.
Current ALT 57 U/L.
Uses sunscreen in summer.
Teeth in good repair.


## 2.23 ('gs173', 'c1', 'numeric', 'easy') templates=train

RULE: For acute migraine, prescribe sumatriptan. If the current calf swelling compared with the other leg is 3.0 cm or more or the current white cell count is above 12.0 x10^9/L, prescribe naproxen instead.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Patient: female, 18 years.
Acute migraine without aura, typical of prior attacks.
Tape measurement today shows a calf circumference gap of 1.2 cm.
Enjoys cooking.
Keeps houseplants.
Complete blood count this morning: white cell count 9.7 x10^9/L.

FLIP (answer s'): -Tape measurement today shows a calf circumference gap of 1.2 cm. | +Tape measurement today shows a calf circumference gap of 3.0 cm.

NEAR (answer s): -Tape measurement today shows a calf circumference gap of 1.2 cm. | +Tape measurement today shows a calf circumference gap of 2.7 cm.

MISSING (answer neither (undetermined)): -Tape measurement today shows a calf circumference gap of 1.2 cm.

PRES (answer s): full text
18 years old, female.
Acute migraine without aura, typical of prior attacks.
White cell count today: 9.7 x10^9/L.
Keeps houseplants.
Enjoys cooking.
Difference in calf circumference today, side to side: 1.2 cm.


## 2.24 ('gs062', 'c1', 'subject', 'long') templates=test

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If at least two of the following apply, prescribe dapagliflozin instead: the patient is currently taking aspirin; the patient has ever had angioedema (current or past); the patient currently has tender anterior cervical lymph nodes.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Man of 57 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Teeth in good repair.
Pupils equal and reactive to light.
His sister wears contact lenses.
Enjoys board games.
Sleeps seven hours a night.
Has two cats.
Sees a dentist yearly.
Knits as a hobby.
Uses sunscreen in summer.
Prefers to be addressed by first name.
His sister burned a hand on a stove years ago.
Photographs local wildlife.
His roommate lives with psoriasis.
Lives in a second-floor apartment.
During a checkup in 2021, free T3 was 3.2 pg/mL.
His father has recovered from a dislocated finger.
Lives with chronic angioedema that flares several times a year.
During a checkup in 2008, total protein was 7.0 g/dL.
Neck palpation unremarkable.
Plays the piano.

FLIP (answer s'): +Currently on low-dose aspirin for heart protection.

NEAR (answer s): +His roommate is on low-dose aspirin.

MISSING (answer neither (undetermined)): +Aspirin use: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 57 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Knits as a hobby.
Uses sunscreen in summer.
Teeth in good repair.
Sleeps seven hours a night.
Has two cats.
Pupils equal and reactive to light.
His roommate lives with psoriasis.
Sees a dentist yearly.
His sister burned a hand on a stove years ago.
His father has recovered from a dislocated finger.
Drives a car.
Lives in a second-floor apartment.
Enjoys board games.
During a checkup in 2008, total protein was 7.0 g/dL.
Lives with chronic angioedema that flares several times a year.
His sister wears contact lenses.
Prefers to be addressed by first name.
Photographs local wildlife.
Neck palpation unremarkable.
Plays the piano.
During a checkup in 2021, free T3 was 3.2 pg/mL.


## 2.25 ('gs159', 'c1', 'time', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient is allergic to sulfonamide antibiotics, prescribe amlodipine instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Patient: male, 38 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
His mother has a chipped front tooth.
Writes with the right hand.
Reads most evenings.
Denies allergies to any drug or food.
Enjoys cooking.
Grows tomatoes in the garden.
TSH 1.6 mIU/L in 2012.
Albumin 4.1 g/dL in 2016 (routine blood test).
Height 170 cm.
Plays chess online.
His housemate broke a wrist, which has healed.
Enjoys gardening.
Speaks English and Spanish.
Wears a seat belt when driving.
Uses public transport.
His neighbor had a splinter removed from a finger.

FLIP (answer s'): -Denies allergies to any drug or food. | +Sulfa antibiotics cause an itchy allergic rash in this patient.

NEAR (answer s): -Denies allergies to any drug or food. | +Sulfa antibiotic allergy in childhood, resolved; tolerated trimethoprim-sulfamethoxazole in 2010.

MISSING (answer neither (undetermined)): -Denies allergies to any drug or food. | +Sulfonamide allergy: not asked about.

PRES (answer s): full text
38 years old, male.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
His neighbor had a splinter removed from a finger.
Enjoys cooking.
Writes with the right hand.
Speaks English and Spanish.
Reads most evenings.
Grows tomatoes in the garden.
Plays chess online.
Wears a seat belt when driving.
Enjoys gardening.
His mother has a chipped front tooth.
Denies allergies to any drug or food.
Height 170 cm.
His housemate broke a wrist, which has healed.
Albumin 4.1 g/dL in 2016 (routine blood test).
Uses public transport.
TSH 1.6 mIU/L in 2012.


## 2.26 ('gs076', 'c3', 'boundary', 'long') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. Score 2 points if the patient currently has tonsillar exudate; 3 points if the current white cell count is above 12.0 x10^9/L; 2 points if the current serum creatinine is above 2.0 mg/dL. If the score is 4 or more, prescribe diltiazem instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Male patient of 47 years.
Atrial fibrillation with a ventricular rate of 128/min.
Drives a car.
Tonsils slightly red but clean, without pus.
His uncle wears contact lenses.
Latest creatinine result: 1.4 mg/dL.
Owns a bicycle.
Prefers to be addressed by first name.
Prefers morning appointments.
Enjoys board games.
Sleeps seven hours a night.
Latest WBC is 16.4 x10^9/L.
His roommate burned a hand on a stove years ago.
Teeth in good repair.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Has two cats.
Knits as a hobby.
In 2014, folate was 12 ng/mL.
Sees a dentist yearly.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2009.

FLIP (answer s'): -Latest creatinine result: 1.4 mg/dL. | +Latest creatinine result: 3.0 mg/dL.

NEAR (answer s): -Latest creatinine result: 1.4 mg/dL. | +Latest creatinine result: 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Latest creatinine result: 1.4 mg/dL.

PRES (answer s): full text
Man of 47 years.
Atrial fibrillation with a ventricular rate of 128/min.
Enjoys board games.
Knits as a hobby.
Zinc of 85 mcg/dL in 2009.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Teeth in good repair.
Drives a car.
Lives in a second-floor apartment.
In 2014, folate was 12 ng/mL.
Owns a bicycle.
Sees a dentist yearly.
Current white cell count 16.4 x10^9/L.
Has two cats.
His uncle wears contact lenses.
Prefers to be addressed by first name.
Prefers morning appointments.
Tonsils slightly red but clean, without pus.
Current serum creatinine 1.4 mg/dL.
Paints watercolors as a hobby.
His roommate burned a hand on a stove years ago.


## 2.27 ('cut_bleed', 'bleed', 'negation', 'easy') templates=train

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. Score 2 points for a major bleeding event at any time; 1 point for age 75 years or more; 1 point for a current eGFR below 30 mL/min/1.73 m2. If the score is 2 or more, prescribe aspirin plus clopidogrel instead.
CONDITION: bleeding history
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Patient: male.
Recovering on the ward after a myocardial infarction treated with a stent.
Drinks alcohol occasionally.
Renal function today: eGFR 21 mL/min/1.73 m2.
Non-smoker.
Age as of today: 62 years.

FLIP (answer s'): +Major postoperative bleed from a knee wound in 2017, resolved with a repeat procedure.

NEAR (answer s): +Denies any major bleeding, past or present.

MISSING (answer neither (undetermined)): +Information on bleeding history was not obtained.

PRES (answer s): full text
Sex: male.
Recovering on the ward after a myocardial infarction treated with a stent.
This morning's blood test shows an eGFR of 21 mL/min/1.73 m2.
Drinks alcohol occasionally.
Age today: 62 years.
Non-smoker.


## 2.28 ('gs076', 'c3', 'numeric', 'easy') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. Score 2 points if the patient currently has tonsillar exudate; 3 points if the current white cell count is above 12.0 x10^9/L; 2 points if the current serum creatinine is above 2.0 mg/dL. If the score is 4 or more, prescribe diltiazem instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Man of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Tonsils pink and clean on inspection.
Has two cats.
Uses sunscreen in summer.
Current serum creatinine 1.1 mg/dL.
Latest WBC is 14.3 x10^9/L.
Prefers morning appointments.
Pupils equal and reactive to light.

FLIP (answer s'): -Current serum creatinine 1.1 mg/dL. | +Current serum creatinine 2.6 mg/dL.

NEAR (answer s): -Current serum creatinine 1.1 mg/dL. | +Current serum creatinine 1.8 mg/dL.

MISSING (answer neither (undetermined)): -Current serum creatinine 1.1 mg/dL.

PRES (answer s): full text
Male patient of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Tonsils pink and clean on inspection.
Pupils equal and reactive to light.
Current white cell count 14.3 x10^9/L.
Uses sunscreen in summer.
Prefers morning appointments.
Has two cats.
Latest creatinine result: 1.1 mg/dL.


## 2.29 ('gs093', 'c2', 'subject', 'easy') templates=train

RULE: For vaginal candidiasis, prescribe oral fluconazole. Score 3 points if the current systolic blood pressure is below 90 mmHg; 1 point if the patient is currently taking clarithromycin; 1 point if the current serum creatinine is 1.5 mg/dL or more. If the score is 4 or more, prescribe clotrimazole pessaries instead.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Female, 58 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drinks alcohol occasionally.
Antibiotics: none.
Manual cuff blood pressure today: 76/50 mmHg.
Serum creatinine today: 0.9 mg/dL.
Non-smoker.
Grows tomatoes in the garden.

FLIP (answer s'): -Antibiotics: none. | +Takes clarithromycin as part of Helicobacter pylori treatment.

NEAR (answer s): -Antibiotics: none. | +Her cousin is taking clarithromycin.

MISSING (answer neither (undetermined)): -Antibiotics: none. | +Clarithromycin: not yet assessed.

PRES (answer s): full text
58 years old, female.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drinks alcohol occasionally.
Blood panel at this assessment: creatinine 0.9 mg/dL.
Systolic blood pressure 76 mmHg at this assessment.
Non-smoker.
Grows tomatoes in the garden.
Antibiotics: none.


## 2.30 ('s3_rockall', 'sbp', 'time', 'long') templates=test

RULE: Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.
CONDITION: systolic blood pressure below 100
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 2 points.'

BASE (answer s):
Man, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Zinc of 85 mcg/dL in 2024.
In 2005, folate was 12 ng/mL.
His wife has a lazy eye.
His roommate wears contact lenses.
His roommate has recovered from a dislocated finger.
Uses sunscreen in summer.
Owns a bicycle.
Plays the piano.
In 2014, lipase was 30 U/L.
Has two cats.
Paints watercolors as a hobby.
Prefers morning appointments.
His wife burned a hand on a stove years ago.
Drives a car.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Currently aged 52 years.
Lives in a second-floor apartment.
Current systolic blood pressure 146 mmHg.
Sleeps flat on one pillow.
Teeth in good repair.
Knits as a hobby.
Records from 2020 list systolic blood pressure at 152 mmHg.

FLIP (answer s'): -Current systolic blood pressure 146 mmHg. | +Current systolic blood pressure 77 mmHg.

NEAR (answer s): -Records from 2020 list systolic blood pressure at 152 mmHg. | +Records from 2020 list systolic blood pressure at 83 mmHg.

MISSING (answer neither (undetermined)): -Current systolic blood pressure 146 mmHg. | -Records from 2020 list systolic blood pressure at 152 mmHg.

PRES (answer s): full text
An adult man.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Prefers morning appointments.
In 2014, lipase was 30 U/L.
Observations now: blood pressure 146/92 mmHg.
Owns a bicycle.
Lives in a second-floor apartment.
Drives a car.
His roommate wears contact lenses.
His wife burned a hand on a stove years ago.
Knits as a hobby.
Sleeps flat on one pillow.
In 2005, folate was 12 ng/mL.
Has two cats.
Zinc of 85 mcg/dL in 2024.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Back in 2020, systolic blood pressure stood at 152 mmHg.
Current age 52 years.
Plays the piano.
His roommate has recovered from a dislocated finger.
Teeth in good repair.
Uses sunscreen in summer.
His wife has a lazy eye.
Paints watercolors as a hobby.


## 2.31 ('gs083', 'c1', 'boundary', 'long') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current temperature is above 38.0 C and the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe intravenous piperacillin-tazobactam instead.
CONDITION: temperature above 38.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
57-year-old woman.
Suspected chest infection; assessed on the medical ward.
Nails normal.
Vitamin D 38 ng/mL in 2009 (wellness visit).
Watches football on weekends.
Listens to podcasts.
Reads most evenings.
Drinks two cups of coffee a day.
Enjoys gardening.
Does crossword puzzles.
Keeps houseplants.
Peripheral artery disease in 2021, with leg pain that resolved after an artery stent.
Her aunt has a broken finger in a splint.
Volunteers at a library.
Temperature 36.4 C at this assessment.
Serum calcium 9.4 mg/dL in 2015.
Non-smoker.
Sodium 140 mmol/L in 2023.
Her brother-in-law is being treated for eczema.

FLIP (answer s'): -Temperature 36.4 C at this assessment. | +Temperature 38.7 C at this assessment.

NEAR (answer s): -Temperature 36.4 C at this assessment. | +Temperature 38.0 C at this assessment.

MISSING (answer neither (undetermined)): -Temperature 36.4 C at this assessment.

PRES (answer s): full text
Patient: female, 57 years.
Suspected chest infection; assessed on the medical ward.
Keeps houseplants.
Serum calcium 9.4 mg/dL in 2015.
Vitamin D 38 ng/mL in 2009 (wellness visit).
Drinks two cups of coffee a day.
Volunteers at a library.
Peripheral artery disease in 2021, with leg pain that resolved after an artery stent.
Her aunt has a broken finger in a splint.
Reads most evenings.
Enjoys gardening.
Nails normal.
Non-smoker.
Temperature checked with a digital thermometer today: 36.4 C.
Watches football on weekends.
Her brother-in-law is being treated for eczema.
Listens to podcasts.
Does crossword puzzles.
Sodium 140 mmol/L in 2023.


## 2.32 ('gs024', 'c1', 'negation', 'long') templates=test

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the patient is allergic to penicillin or the current white cell count is above 12.0 x10^9/L, prescribe intravenous co-amoxiclav instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
Female patient of 74 years.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Enjoys board games.
Zinc of 85 mcg/dL in 2019.
Her sister lives with psoriasis.
Plays the piano.
Paints watercolors as a hobby.
During a checkup in 2005, total protein was 7.0 g/dL.
Teeth in good repair.
Knits as a hobby.
Pupils equal and reactive to light.
Latest WBC is 8.7 x10^9/L.
Sleeps seven hours a night.
Her roommate sprained a thumb last month.
Her roommate burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2015.
Lives in a second-floor apartment.

FLIP (answer s'): +Known penicillin allergy with angioedema.

NEAR (answer s): +Has never been allergic to penicillin.

MISSING (answer neither (undetermined)): +Penicillin allergy: status unclear from the records at hand.

PRES (answer s): full text
Woman of 74 years.
Community-acquired pneumonia confirmed on chest radiograph.
Free T4 of 1.2 ng/dL in 2015.
Her roommate sprained a thumb last month.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
During a checkup in 2005, total protein was 7.0 g/dL.
Her sister lives with psoriasis.
Enjoys board games.
Sleeps seven hours a night.
Knits as a hobby.
Uses sunscreen in summer.
Plays the piano.
Her roommate burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2019.
Teeth in good repair.
Current white cell count 8.7 x10^9/L.
Prefers to be addressed by first name.


## 2.33 ('s3_aims65', 'age', 'numeric', 'easy') templates=train

RULE: AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.
CONDITION: age at least 65
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Patient: male.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Enjoys cooking.
Blood pressure today: 132/83 mmHg.
Age today: 52 years.
Coagulation screen this morning: international normalized ratio 1.2.
Plays chess online.
Alert and attentive.

FLIP (answer s'): -Age today: 52 years. | +Age today: 65 years.

NEAR (answer s): -Age today: 52 years. | +Age today: 62 years.

MISSING (answer neither (undetermined)): -Age today: 52 years.

PRES (answer s): full text
Male patient.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Systolic blood pressure 132 mmHg at this assessment.
Alert and attentive.
Age 52 years, calculated today from the date of birth.
Plays chess online.
Enjoys cooking.
International normalized ratio (INR) at this assessment: 1.2.


## 2.34 ('gs137', 'c1', 'subject', 'long') templates=test

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient has ever had asthma (current or past) and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe nitrofurantoin instead.
CONDITION: asthma at any time
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Female patient of 43 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Her friend wears contact lenses.
Inhaler use: none.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Plays the piano.
Owns a bicycle.
Recovered from a pulmonary embolism in 2016.
In 2009, folate was 12 ng/mL.
During a checkup in 2022, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2008.
Photographs local wildlife.
Teeth in good repair.
Her uncle has a lazy eye.

FLIP (answer s'): -Inhaler use: none. | +Asthma, on a daily inhaled steroid.

NEAR (answer s): -Inhaler use: none. | +Her wife is asthmatic.

MISSING (answer neither (undetermined)): -Inhaler use: none. | +Asthma at any time: unknown.

PRES (answer s): full text
Woman of 43 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Recovered from a pulmonary embolism in 2016.
During a checkup in 2022, total protein was 7.0 g/dL.
In 2009, folate was 12 ng/mL.
Photographs local wildlife.
Her friend wears contact lenses.
Sleeps seven hours a night.
Inhaler use: none.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Teeth in good repair.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2008.
Plays the piano.
Sees a dentist yearly.
Her uncle has a lazy eye.
Owns a bicycle.


## 2.35 ('uti_sulfa', 'sulfa', 'time', 'delabelled') templates=train

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient is allergic to sulfonamide antibiotics, prescribe nitrofurantoin instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
46 years old, female.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
No known antibiotic allergies.
Enjoys gardening.

FLIP (answer s'): -No known antibiotic allergies. | +Allergic to sulfa antibiotics (hives).

NEAR (answer s): -No known antibiotic allergies. | +An oral challenge in 2015 disproved the sulfa allergy, and the label was removed.

MISSING (answer neither (undetermined)): -No known antibiotic allergies. | +Sulfonamide allergy: not yet assessed.

PRES (answer s): full text
46-year-old woman.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Enjoys gardening.
No known antibiotic allergies.


## 2.36 ('gs086', 'c1', 'boundary', 'long') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the current systolic blood pressure is above 160 mmHg and the current platelet count is below 50 x10^9/L, prescribe fondaparinux instead.
CONDITION: systolic blood pressure above 160
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Man of 74 years.
First day after elective total hip replacement.
His sister has a lazy eye.
Knits as a hobby.
Pupils equal and reactive to light.
In 2010, lipase was 30 U/L.
His roommate lives with psoriasis.
Current platelet count 22 x10^9/L.
His friend sprained a thumb last month.
Enjoys board games.
Sleeps seven hours a night.
Plays the piano.
In 2014, folate was 12 ng/mL.
Photographs local wildlife.
Prefers to be addressed by first name.
Current systolic blood pressure 123 mmHg.
Lives in a second-floor apartment.
During a checkup in 2012, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Prefers morning appointments.
Owns a bicycle.

FLIP (answer s'): -Current systolic blood pressure 123 mmHg. | +Current systolic blood pressure 190 mmHg.

NEAR (answer s): -Current systolic blood pressure 123 mmHg. | +Current systolic blood pressure 160 mmHg.

MISSING (answer neither (undetermined)): -Current systolic blood pressure 123 mmHg.

PRES (answer s): full text
Male patient of 74 years.
First day after elective total hip replacement.
Platelet count now 22 x10^9/L.
Enjoys board games.
In 2010, lipase was 30 U/L.
His roommate lives with psoriasis.
Photographs local wildlife.
During a checkup in 2012, total protein was 7.0 g/dL.
His sister has a lazy eye.
Uses sunscreen in summer.
In 2014, folate was 12 ng/mL.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Plays the piano.
His friend sprained a thumb last month.
Observations now: blood pressure 123/78 mmHg.
Lives in a second-floor apartment.
Knits as a hobby.
Owns a bicycle.
Prefers to be addressed by first name.
Prefers morning appointments.


## 2.37 ('gs177', 'c1', 'negation', 'long') templates=train

RULE: For acute migraine, prescribe sumatriptan. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time, prescribe naproxen instead.
CONDITION: coronary artery disease in the patient or a first-degree relative
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
59 years old, male.
Acute migraine without aura, typical of prior attacks.
His housemate had a splinter removed from a finger.
Uses a smartphone for reminders.
Sodium 140 mmol/L in 2013.
Drinks plenty of water.
Reads most evenings.
Sings in a weekly choir.
TSH 1.6 mIU/L in 2006.
His aunt has a chipped front tooth.
Takes no medicines for angina.
Eats a varied diet.
Speaks English and Spanish.
Keeps a step counter.
Drinks alcohol occasionally.
Collects postcards.
His neighbor has a stutter.
Non-smoker.

FLIP (answer s'): -Takes no medicines for angina. | +Coronary artery disease, followed in cardiology clinic every six months.

NEAR (answer s): -Takes no medicines for angina. | +Denies coronary artery disease, past or present.

MISSING (answer neither (undetermined)): -Takes no medicines for angina. | +Coronary artery disease in the patient or a first-degree relative: could not be determined from the information available.

PRES (answer s): full text
Male, 59 years.
Acute migraine without aura, typical of prior attacks.
Keeps a step counter.
TSH 1.6 mIU/L in 2006.
His neighbor has a stutter.
Eats a varied diet.
His housemate had a splinter removed from a finger.
Non-smoker.
His aunt has a chipped front tooth.
Speaks English and Spanish.
Uses a smartphone for reminders.
Collects postcards.
Sodium 140 mmol/L in 2013.
Drinks plenty of water.
Takes no medicines for angina.
Drinks alcohol occasionally.
Sings in a weekly choir.
Reads most evenings.


## 2.38 ('all_gastro', 'age', 'numeric', 'long') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient is aged 65 years or more and the patient is currently taking aspirin, prescribe naproxen with omeprazole instead.
CONDITION: age at least 65
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Man, adult.
Hip osteoarthritis with pain on walking.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Prefers morning appointments.
Current age 56 years.
Owns a bicycle.
In 2020, folate was 12 ng/mL.
Teeth in good repair.
Sleeps seven hours a night.
Knits as a hobby.
Enjoys board games.
Zinc of 85 mcg/dL in 2013.
Sees a dentist yearly.
Paints watercolors as a hobby.
In 2022, lipase was 30 U/L.
Photographs local wildlife.
Uses a daily aspirin on a cardiologist's recommendation.
His wife has recovered from a dislocated finger.
Drives a car.
Prefers to be addressed by first name.
His wife has a lazy eye.

FLIP (answer s'): -Current age 56 years. | +Current age 81 years.

NEAR (answer s): -Current age 56 years. | +Current age 63 years.

MISSING (answer neither (undetermined)): -Current age 56 years.

PRES (answer s): full text
An adult man.
Hip osteoarthritis with pain on walking.
His wife has recovered from a dislocated finger.
Uses a daily aspirin on a cardiologist's recommendation.
Uses sunscreen in summer.
Enjoys board games.
His wife has a lazy eye.
Zinc of 85 mcg/dL in 2013.
In 2022, lipase was 30 U/L.
Sees a dentist yearly.
Currently aged 56 years.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Knits as a hobby.
Owns a bicycle.
Teeth in good repair.
Prefers morning appointments.
In 2020, folate was 12 ng/mL.
Photographs local wildlife.
Drives a car.
Pupils equal and reactive to light.


## 2.39 ('gs151', 'c2', 'subject', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient has ever had asthma (current or past); the current calf swelling compared with the other leg is 3.0 cm or more.
CONDITION: asthma at any time
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
46 years old, male.
Suspected chest infection; assessed on the medical ward.
Plays chess online.
Bakes bread at home.
No night cough or chest tightness.
Calf swelling at this assessment: 0.5 cm more than the opposite calf.
Keeps houseplants.
Peripheral artery disease with calf claudication.

FLIP (answer s'): -No night cough or chest tightness. | +Previously had asthma in childhood; symptom-free and off inhalers for decades.

NEAR (answer s): -No night cough or chest tightness. | +His brother had occupational asthma in 2005 that resolved after a change of job.

MISSING (answer neither (undetermined)): -No night cough or chest tightness. | +Asthma at any time: not yet assessed.

PRES (answer s): full text
Male, 46 years.
Suspected chest infection; assessed on the medical ward.
Plays chess online.
No night cough or chest tightness.
Bakes bread at home.
Keeps houseplants.
Peripheral artery disease with calf claudication.
Tape measurement today shows a calf circumference gap of 0.5 cm.


## 2.40 ('gs222', 'c1', 'time', 'long') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the current calf swelling compared with the other leg is 3.0 cm or more; the patient currently has tonsillar exudate; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Male patient of 61 years.
First day after elective total hip replacement.
His father burned a hand on a stove years ago.
Drives a car.
Photographs local wildlife.
His uncle lives with psoriasis.
During a checkup in 2020, total protein was 7.0 g/dL.
Current calf swelling 1.1 cm compared with the other leg.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
His roommate wears contact lenses.
Zinc of 85 mcg/dL in 2021.
In 2011, folate was 12 ng/mL.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Tonsils slightly red but clean, without pus.
His father is being treated for a pulmonary embolism.
Records from 2009 list calf swelling at 0.8 cm.
Teeth in good repair.
Has two cats.
Sleeps seven hours a night.
His wife sprained a thumb last month.
Sees a dentist yearly.

FLIP (answer s'): -Current calf swelling 1.1 cm compared with the other leg. | +Current calf swelling 3.0 cm compared with the other leg.

NEAR (answer s): -Records from 2009 list calf swelling at 0.8 cm. | +Records from 2009 list calf swelling at 4.8 cm.

MISSING (answer neither (undetermined)): -Current calf swelling 1.1 cm compared with the other leg. | -Records from 2009 list calf swelling at 0.8 cm.

PRES (answer s): full text
Man of 61 years.
First day after elective total hip replacement.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Drives a car.
Has two cats.
Tonsils slightly red but clean, without pus.
His father is being treated for a pulmonary embolism.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2021.
Sees a dentist yearly.
During a checkup in 2020, total protein was 7.0 g/dL.
Photographs local wildlife.
Teeth in good repair.
His uncle lives with psoriasis.
His father burned a hand on a stove years ago.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Back in 2009, calf swelling stood at 0.8 cm.
In 2011, folate was 12 ng/mL.
His wife sprained a thumb last month.
Difference in calf circumference now 1.1 cm.
His roommate wears contact lenses.


## 2.41 ('gs130', 'c3', 'boundary', 'easy') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient currently has tender anterior cervical lymph nodes; the current platelet count is below 50 x10^9/L.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Male, 63 years.
Productive cough and fever; consolidation on chest radiograph.
Platelet count at this assessment: 338 x10^9/L.
Myocardial infarction confirmed by troponin and ECG today.
No tender swellings in the neck.
Uses public transport.
Feeds birds in the backyard.
Listens to podcasts.
Wears glasses when driving.

FLIP (answer s'): -Platelet count at this assessment: 338 x10^9/L. | +Platelet count at this assessment: 34 x10^9/L.

NEAR (answer s): -Platelet count at this assessment: 338 x10^9/L. | +Platelet count at this assessment: 50 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count at this assessment: 338 x10^9/L.

PRES (answer s): full text
63 years old, male.
Productive cough and fever; consolidation on chest radiograph.
Complete blood count today: platelets 338 x10^9/L.
Uses public transport.
Myocardial infarction confirmed by troponin and ECG today.
No tender swellings in the neck.
Listens to podcasts.
Feeds birds in the backyard.
Wears glasses when driving.


## 2.42 ('s3_charlson', 'vasc', 'negation', 'easy') templates=test

RULE: Charlson Comorbidity Index (as used here, partial): 1 point for heart failure at any time (current or past); 1 point for a myocardial infarction or peripheral artery disease at any time (current or past); 1 point for current asthma; 2 points for a current serum creatinine above 3.0 mg/dL. Age and other Charlson items are not part of this question.
CONDITION: myocardial infarction or peripheral artery disease
CLAIMS: s = 'The myocardial infarction or peripheral artery disease criterion contributes 0 points.' | s' = 'The myocardial infarction or peripheral artery disease criterion contributes 1 point.'

BASE (answer s):
Male patient of 81 years.
Inpatient on the medical ward; comorbidity review.
Lives in a second-floor apartment.
Has two cats.
Photographs local wildlife.
Latest creatinine result: 0.7 mg/dL.

FLIP (answer s'): +Has symptomatic peripheral artery disease of both legs.

NEAR (answer s): +Has never had a heart attack or peripheral artery disease.

MISSING (answer neither (undetermined)): +Myocardial infarction or peripheral artery disease: unknown.

PRES (answer s): full text
Man of 81 years.
Inpatient on the medical ward; comorbidity review.
Has two cats.
Lives in a second-floor apartment.
Photographs local wildlife.
Current serum creatinine 0.7 mg/dL.


## 2.43 ('s4_glasgow_imrie', 'bun', 'numeric', 'long') templates=train

RULE: Glasgow-Imrie score for acute pancreatitis (as used here, partial): 1 point each for age above 55 years; a current white cell count above 15.0 x10^9/L; a current blood urea nitrogen above 45 mg/dL. Other Glasgow-Imrie items are not part of this question.
CONDITION: blood urea nitrogen above 45
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 1 point.'

BASE (answer s):
Adult woman.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Sodium 140 mmol/L in 2016.
Non-smoker.
Her aunt is left-handed.
Enjoys gardening.
Keeps houseplants.
Her brother-in-law wears hearing aids.
Age at this assessment: 34 years.
Collects postcards.
Uses a smartphone for reminders.
Uses public transport.
Has a pet dog.
Reads most evenings.
Drinks plenty of water.
Writes with the right hand.
Volunteers at a library.
Feeds birds in the backyard.
Complete blood count this morning: white cell count 9.9 x10^9/L.
Vitamin B12 450 pg/mL in 2019.
BUN on today's chemistry panel: 33 mg/dL.
Chloride 103 mmol/L in 2019.
Albumin 4.1 g/dL in 2023 (routine blood test).

FLIP (answer s'): -BUN on today's chemistry panel: 33 mg/dL. | +BUN on today's chemistry panel: 71 mg/dL.

NEAR (answer s): -BUN on today's chemistry panel: 33 mg/dL. | +BUN on today's chemistry panel: 41 mg/dL.

MISSING (answer neither (undetermined)): -BUN on today's chemistry panel: 33 mg/dL.

PRES (answer s): full text
Female patient.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Her aunt is left-handed.
Reads most evenings.
Vitamin B12 450 pg/mL in 2019.
Collects postcards.
Volunteers at a library.
Chloride 103 mmol/L in 2019.
BUN 33 mg/dL this morning.
Albumin 4.1 g/dL in 2023 (routine blood test).
Uses a smartphone for reminders.
Keeps houseplants.
Enjoys gardening.
Feeds birds in the backyard.
WBC 9.9 x10^9/L on today's sample.
Uses public transport.
Writes with the right hand.
Has a pet dog.
Her brother-in-law wears hearing aids.
Non-smoker.
Age 34 years, calculated today from the date of birth.
Drinks plenty of water.
Sodium 140 mmol/L in 2016.


## 2.44 ('gs056', 'c1', 'subject', 'easy') templates=test

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If at least two of the following apply, prescribe nitrofurantoin instead: the patient currently has asthma; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current serum potassium is above 4.8 mmol/L.
CONDITION: asthma
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Female patient of 68 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Hemoglobin within the normal range on recent blood tests.
Inhaler use: none.
Latest potassium result: 5.0 mmol/L.
Sees a dentist yearly.

FLIP (answer s'): -Inhaler use: none. | +Persistent asthma, using a rescue inhaler most weeks.

NEAR (answer s): -Inhaler use: none. | +Her friend uses an inhaler for asthma.

MISSING (answer neither (undetermined)): -Inhaler use: none. | +Asthma: unknown.

PRES (answer s): full text
Woman of 68 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Current serum potassium 5.0 mmol/L.
Hemoglobin within the normal range on recent blood tests.
Inhaler use: none.
Sees a dentist yearly.


## 2.45 ('gs001', 'c1', 'time', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the current white cell count is above 12.0 x10^9/L and the current serum creatinine is 1.5 mg/dL or more, prescribe a progestin-only pill instead.
CONDITION: white cell count above 12.0
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
33-year-old woman.
Requests contraception.
Feeds birds in the backyard.
White cell count of 4.8 x10^9/L recorded in 2019.
Creatinine 2.4 mg/dL on this morning's labs.
Listens to podcasts.
Bakes bread at home.
WBC 8.1 x10^9/L on today's sample.
Drinks alcohol occasionally.

FLIP (answer s'): -WBC 8.1 x10^9/L on today's sample. | +WBC 14.9 x10^9/L on today's sample.

NEAR (answer s): -White cell count of 4.8 x10^9/L recorded in 2019. | +White cell count of 14.3 x10^9/L recorded in 2019.

MISSING (answer neither (undetermined)): -White cell count of 4.8 x10^9/L recorded in 2019. | -WBC 8.1 x10^9/L on today's sample.

PRES (answer s): full text
Patient: female, 33 years.
Requests contraception.
Listens to podcasts.
Feeds birds in the backyard.
Blood panel at this assessment: creatinine 2.4 mg/dL.
In 2019, white cell count was 4.8 x10^9/L.
Complete blood count this morning: white cell count 8.1 x10^9/L.
Bakes bread at home.
Drinks alcohol occasionally.


## 2.46 ('c3_cellulitis_sirs', 'wbc', 'boundary', 'long') templates=test

RULE: For cellulitis of the lower leg, prescribe oral cephalexin. If the current temperature is above 38.0 C and the current white cell count is above 12.0 x10^9/L, prescribe intravenous cefazolin instead.
CONDITION: white cell count above 12.0
CLAIMS: s = 'Prescribe oral cephalexin.' | s' = 'Prescribe intravenous cefazolin.'

BASE (answer s):
Male patient of 73 years.
Spreading redness, warmth and swelling of the left lower leg for two days.
Owns a bicycle.
Teeth in good repair.
His friend sprained a thumb last month.
His sister wears contact lenses.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Temperature now 38.9 C (tympanic).
Drives a car.
Sleeps seven hours a night.
His wife burned a hand on a stove years ago.
His wife lives with psoriasis.
Uses sunscreen in summer.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2020.
Free T4 of 1.2 ng/dL in 2012.
Enjoys board games.
Prefers to be addressed by first name.
During a checkup in 2018, total protein was 7.0 g/dL.
Sees a dentist yearly.
Current white cell count 6.0 x10^9/L.
Pupils equal and reactive to light.
Paints watercolors as a hobby.

FLIP (answer s'): -Current white cell count 6.0 x10^9/L. | +Current white cell count 20.1 x10^9/L.

NEAR (answer s): -Current white cell count 6.0 x10^9/L. | +Current white cell count 12.0 x10^9/L.

MISSING (answer neither (undetermined)): -Current white cell count 6.0 x10^9/L.

PRES (answer s): full text
Man of 73 years.
Spreading redness, warmth and swelling of the left lower leg for two days.
His friend sprained a thumb last month.
Enjoys board games.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
His wife lives with psoriasis.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2020.
Owns a bicycle.
Latest WBC is 6.0 x10^9/L.
His wife burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2012.
Teeth in good repair.
Sees a dentist yearly.
During a checkup in 2018, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Current temperature 38.9 C.
Drives a car.
His sister wears contact lenses.


## 2.47 ('gs205', 'c1', 'negation', 'long') templates=train

RULE: For primary prevention, prescribe atorvastatin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe ezetimibe instead.
CONDITION: venous thromboembolism in the patient or a first-degree relative
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Male, 60 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Volunteers at a library.
Uses public transport.
Writes with the right hand.
Grows tomatoes in the garden.
Bakes bread at home.
TSH 1.6 mIU/L in 2017.
Non-smoker.
Hearing normal to conversation.
His brother-in-law is being treated for eczema.
Feeds birds in the backyard.
Phosphate 3.6 mg/dL in 2023.
Keeps a step counter.
Watches football on weekends.
His coworker completed physical therapy for a shoulder injury.
Wears glasses when driving.
No known blood clotting disorder.
Drinks alcohol occasionally.
Enjoys gardening.

FLIP (answer s'): -No known blood clotting disorder. | +His brother had a pulmonary embolism in 2020.

NEAR (answer s): -No known blood clotting disorder. | +Medical records show no venous thromboembolism, and none is reported in first-degree relatives.

MISSING (answer neither (undetermined)): -No known blood clotting disorder. | +Venous thromboembolism in the patient or a first-degree relative: not asked about.

PRES (answer s): full text
Patient: male, 60 years.
Primary prevention; LDL cholesterol 182 mg/dL.
His coworker completed physical therapy for a shoulder injury.
Phosphate 3.6 mg/dL in 2023.
Keeps a step counter.
Writes with the right hand.
Feeds birds in the backyard.
TSH 1.6 mIU/L in 2017.
Hearing normal to conversation.
Drinks alcohol occasionally.
Grows tomatoes in the garden.
Bakes bread at home.
Enjoys gardening.
Wears glasses when driving.
Watches football on weekends.
Non-smoker.
Volunteers at a library.
No known blood clotting disorder.
Uses public transport.
His brother-in-law is being treated for eczema.


## 2.48 ('news2_red', 'spo2', 'numeric', 'easy') templates=test

RULE: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.
CONDITION: oxygen saturation at or below 91
CLAIMS: s = 'The oxygen saturation criterion contributes 0 points.' | s' = 'The oxygen saturation criterion contributes 3 points.'

BASE (answer s):
Male patient of 36 years.
Shortness of breath and fever; assessed on the medical ward.
Latest oxygen saturation reading: 100%.
Speech clear; follows commands.
Observations now: respiratory rate 14/min.
Knits as a hobby.
Has two cats.
Pupils equal and reactive to light.
Observations now: blood pressure 134/84 mmHg.

FLIP (answer s'): -Latest oxygen saturation reading: 100%. | +Latest oxygen saturation reading: 83%.

NEAR (answer s): -Latest oxygen saturation reading: 100%. | +Latest oxygen saturation reading: 93%.

MISSING (answer neither (undetermined)): -Latest oxygen saturation reading: 100%.

PRES (answer s): full text
Man of 36 years.
Shortness of breath and fever; assessed on the medical ward.
Knits as a hobby.
Current respiratory rate 14/min.
Has two cats.
Current systolic blood pressure 134 mmHg.
Pupils equal and reactive to light.
Speech clear; follows commands.
Current oxygen saturation 100%.


## 2.49 ('gs037', 'c3', 'subject', 'long') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. Score 3 points if the patient is currently taking aspirin; 1 point if the current weight is 60 kg or less; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 4 or more, prescribe a progestin-only pill instead.
CONDITION: coronary artery disease
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female, 39 years.
Requests contraception.
Vitamin B12 450 pg/mL in 2007.
Non-smoker.
Her grandmother is nearsighted.
Chloride 103 mmol/L in 2017.
Albumin 4.1 g/dL in 2019 (routine blood test).
Plays chess online.
Collects postcards.
Enjoys cooking.
Drinks alcohol occasionally.
Has a pet dog.
Listens to podcasts.
Feeds birds in the backyard.
Resting ECG shows no ischemic changes.
TSH 1.6 mIU/L in 2011.
Nails normal.
Weight 87 kg at this assessment.
Grows tomatoes in the garden.
Drinks two cups of coffee a day.
Wears a seat belt when driving.
Her aunt is being treated for eczema.
Medication list: aspirin 81 mg, taken each morning.

FLIP (answer s'): -Resting ECG shows no ischemic changes. | +Coronary artery disease, followed in cardiology clinic every six months.

NEAR (answer s): -Resting ECG shows no ischemic changes. | +Her grandmother previously had coronary artery disease, treated with angioplasty.

MISSING (answer neither (undetermined)): -Resting ECG shows no ischemic changes. | +Coronary artery disease: could not be determined from the information available.

PRES (answer s): full text
39-year-old woman.
Requests contraception.
Nails normal.
Chloride 103 mmol/L in 2017.
Albumin 4.1 g/dL in 2019 (routine blood test).
Resting ECG shows no ischemic changes.
Medication list: aspirin 81 mg, taken each morning.
Drinks two cups of coffee a day.
Drinks alcohol occasionally.
Wears a seat belt when driving.
Vitamin B12 450 pg/mL in 2007.
Her aunt is being treated for eczema.
Her grandmother is nearsighted.
TSH 1.6 mIU/L in 2011.
Feeds birds in the backyard.
Collects postcards.
Listens to podcasts.
Weight today: 87 kg.
Non-smoker.
Plays chess online.
Has a pet dog.
Grows tomatoes in the garden.
Enjoys cooking.


## 2.50 ('gs168', 'c1', 'time', 'superseded') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. If the current temperature is above 38.0 C or the patient has ever had diabetes (current or past), prescribe a progestin-only pill instead.
CONDITION: temperature above 38.0
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female patient of 33 years.
Requests contraception.
Current temperature 37.4 C.
HbA1c 5.3% at a routine check.
Last month, temperature was 36.9 C; the newest measurement replaces it.
Pupils equal and reactive to light.

FLIP (answer s'): -Current temperature 37.4 C. | +Current temperature 39.5 C.

NEAR (answer s): -Last month, temperature was 36.9 C; the newest measurement replaces it. | +Last month, temperature was 38.6 C; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Current temperature 37.4 C. | -Last month, temperature was 36.9 C; the newest measurement replaces it.

PRES (answer s): full text
Woman of 33 years.
Requests contraception.
Last month, temperature was 36.9 C; the newest measurement replaces it.
HbA1c 5.3% at a routine check.
Temperature now 37.4 C (tympanic).
Pupils equal and reactive to light.


## 2.51 ('gs064', 'c1', 'boundary', 'easy') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the current platelet count is below 50 x10^9/L; the patient currently has a mechanical heart valve; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
48-year-old man.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Not on anticoagulation at present.
Does crossword puzzles.
Complete blood count today: platelets 360 x10^9/L.
His brother completed cardiac rehabilitation for coronary artery disease in 2007.
Uses a smartphone for reminders.

FLIP (answer s'): -Complete blood count today: platelets 360 x10^9/L. | +Complete blood count today: platelets 44 x10^9/L.

NEAR (answer s): -Complete blood count today: platelets 360 x10^9/L. | +Complete blood count today: platelets 50 x10^9/L.

MISSING (answer neither (undetermined)): -Complete blood count today: platelets 360 x10^9/L.

PRES (answer s): full text
Male, 48 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Platelets 360 x10^9/L on this morning's blood count.
Uses a smartphone for reminders.
Does crossword puzzles.
Not on anticoagulation at present.
His brother completed cardiac rehabilitation for coronary artery disease in 2007.


## 2.52 ('s2_orbit', 'aspirin', 'negation', 'easy') templates=test

RULE: ORBIT bleeding score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for a current age of 75 years or more, a current eGFR below 60 mL/min/1.73 m2, and current use of aspirin. Other ORBIT items are not part of this question.
CONDITION: aspirin use
CLAIMS: s = 'The aspirin use criterion contributes 0 points.' | s' = 'The aspirin use criterion contributes 1 point.'

BASE (answer s):
An adult woman.
Atrial fibrillation; starting apixaban is being considered.
Current antiplatelet drugs: none.
eGFR now 68 mL/min/1.73 m2.
Current age 62 years.
Examination shows no signs of blood loss.
Prefers to be addressed by first name.
Prefers morning appointments.

FLIP (answer s'): -Current antiplatelet drugs: none. | +Uses a daily aspirin on a cardiologist's recommendation.

NEAR (answer s): -Current antiplatelet drugs: none. | +Has never taken aspirin.

MISSING (answer neither (undetermined)): -Current antiplatelet drugs: none. | +Aspirin use: status unclear from the records at hand.

PRES (answer s): full text
Woman, adult.
Atrial fibrillation; starting apixaban is being considered.
Examination shows no signs of blood loss.
Current antiplatelet drugs: none.
Prefers to be addressed by first name.
Prefers morning appointments.
Current eGFR 68 mL/min/1.73 m2.
Currently aged 62 years.


## 2.53 ('all_metformin', 'egfr', 'numeric', 'easy') templates=train

RULE: For type 2 diabetes, prescribe metformin 1000 mg twice daily. If the current eGFR is below 45 mL/min/1.73 m2 and the patient is aged 75 years or more, prescribe metformin 500 mg twice daily instead.
CONDITION: eGFR below 45
CLAIMS: s = 'Prescribe metformin 1000 mg twice daily.' | s' = 'Prescribe metformin 500 mg twice daily.'

BASE (answer s):
Female patient.
Type 2 diabetes on metformin; annual medication review.
Uses public transport.
Keeps a step counter.
Sings in a weekly choir.
Age today: 81 years.
Nails normal.
eGFR today: 65 mL/min/1.73 m2.

FLIP (answer s'): -eGFR today: 65 mL/min/1.73 m2. | +eGFR today: 32 mL/min/1.73 m2.

NEAR (answer s): -eGFR today: 65 mL/min/1.73 m2. | +eGFR today: 47 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -eGFR today: 65 mL/min/1.73 m2.

PRES (answer s): full text
Adult woman.
Type 2 diabetes on metformin; annual medication review.
Age 81 years, calculated today from the date of birth.
eGFR 65 mL/min/1.73 m2 on today's labs.
Keeps a step counter.
Uses public transport.
Sings in a weekly choir.
Nails normal.


## 2.54 ('gs084', 'c1', 'subject', 'easy') templates=test

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient has ever had heart failure (current or past) or the patient currently has tonsillar exudate, prescribe nitrofurantoin instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Female patient of 61 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Heart sounds without a gallop.
Photographs local wildlife.
Pupils equal and reactive to light.
Prefers to be addressed by first name.

FLIP (answer s'): -Heart sounds without a gallop. | +Has heart failure, treated with diuretics.

NEAR (answer s): -Heart sounds without a gallop. | +Her father is treated for heart failure.

MISSING (answer neither (undetermined)): -Heart sounds without a gallop. | +Heart failure: status unclear from the records at hand.

PRES (answer s): full text
Woman of 61 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Heart sounds without a gallop.


## 2.55 ('s2_wells_pe', 'hr', 'time', 'long') templates=train

RULE: Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.
CONDITION: heart rate above 100
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 1.5 points.'

BASE (answer s):
48-year-old man.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
His mother has a chipped front tooth.
Lives on a quiet street.
Drinks plenty of water.
Enjoys cooking.
Vitamin B12 450 pg/mL in 2009.
Watches football on weekends.
Bakes bread at home.
Feeds birds in the backyard.
Vitamin D 38 ng/mL in 2017 (wellness visit).
His brother has a stutter.
Reads most evenings.
Heart rate was 90/min when measured in 2016.
Enjoys gardening.
Ferritin 60 ng/mL in 2020.
Heart rate counted over a full minute at this assessment: 86/min.
His brother wears hearing aids.
Eats a varied diet.
His aunt is nearsighted.
Sputum clear.

FLIP (answer s'): -Heart rate counted over a full minute at this assessment: 86/min. | +Heart rate counted over a full minute at this assessment: 122/min.

NEAR (answer s): -Heart rate was 90/min when measured in 2016. | +Heart rate was 108/min when measured in 2016.

MISSING (answer neither (undetermined)): -Heart rate was 90/min when measured in 2016. | -Heart rate counted over a full minute at this assessment: 86/min.

PRES (answer s): full text
48 years old, male.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Enjoys gardening.
Heart rate today: 86/min.
Enjoys cooking.
Lives on a quiet street.
Ferritin 60 ng/mL in 2020.
His mother has a chipped front tooth.
Vitamin D 38 ng/mL in 2017 (wellness visit).
Feeds birds in the backyard.
Bakes bread at home.
Reads most evenings.
His brother has a stutter.
His brother wears hearing aids.
Drinks plenty of water.
Sputum clear.
Heart rate 90/min at a hospital visit in 2016.
Watches football on weekends.
Eats a varied diet.
His aunt is nearsighted.
Vitamin B12 450 pg/mL in 2009.


## 2.56 ('s4_glasgow_imrie', 'bun', 'boundary', 'long') templates=test

RULE: Glasgow-Imrie score for acute pancreatitis (as used here, partial): 1 point each for age above 55 years; a current white cell count above 15.0 x10^9/L; a current blood urea nitrogen above 45 mg/dL. Other Glasgow-Imrie items are not part of this question.
CONDITION: blood urea nitrogen above 45
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 1 point.'

BASE (answer s):
An adult man.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Owns a bicycle.
Uses sunscreen in summer.
Knits as a hobby.
Sleeps seven hours a night.
Enjoys board games.
His friend burned a hand on a stove years ago.
Photographs local wildlife.
Latest WBC is 10.6 x10^9/L.
His father wears contact lenses.
Prefers morning appointments.
Paints watercolors as a hobby.
Has two cats.
Sees a dentist yearly.
Plays the piano.
Blood urea nitrogen 31 mg/dL on the current labs.
Drives a car.
Lives in a second-floor apartment.
In 2012, folate was 12 ng/mL.
Current age 35 years.
His sister has recovered from a dislocated finger.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Teeth in good repair.

FLIP (answer s'): -Blood urea nitrogen 31 mg/dL on the current labs. | +Blood urea nitrogen 64 mg/dL on the current labs.

NEAR (answer s): -Blood urea nitrogen 31 mg/dL on the current labs. | +Blood urea nitrogen 45 mg/dL on the current labs.

MISSING (answer neither (undetermined)): -Blood urea nitrogen 31 mg/dL on the current labs.

PRES (answer s): full text
Man, adult.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Sees a dentist yearly.
Uses sunscreen in summer.
In 2012, folate was 12 ng/mL.
Sleeps seven hours a night.
Drives a car.
Enjoys board games.
Blood urea nitrogen now: 31 mg/dL.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
His father wears contact lenses.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Has two cats.
Prefers morning appointments.
Plays the piano.
Currently aged 35 years.
Owns a bicycle.
Knits as a hobby.
Photographs local wildlife.
Current white cell count 10.6 x10^9/L.
His sister has recovered from a dislocated finger.
His friend burned a hand on a stove years ago.
Teeth in good repair.
Lives in a second-floor apartment.


## 2.57 ('gs181', 'c1', 'negation', 'long') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the patient has ever had heart failure (current or past) or the patient is currently taking aspirin, prescribe a progestin-only pill instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female, 20 years.
Requests contraception.
Drinks alcohol occasionally.
Albumin 4.1 g/dL in 2024 (routine blood test).
Nails normal.
Volunteers at a library.
Her neighbor has a stutter.
Ferritin 60 ng/mL in 2024.
Sings in a weekly choir.
Does crossword puzzles.
Uses public transport.
Drinks two cups of coffee a day.
Serum calcium 9.4 mg/dL in 2024.
Collects postcards.
Her aunt completed physical therapy for a shoulder injury.
Hearing normal to conversation.
Chloride 103 mmol/L in 2024.
Her brother broke a wrist, which has healed.
Heart size normal on chest radiograph.
No platelet-inhibiting drugs on the medication list.
Wears a seat belt when driving.
Her housemate wears hearing aids.
Writes with the right hand.
Bakes bread at home.

FLIP (answer s'): -Heart size normal on chest radiograph. | +Heart failure during sepsis in 2024, resolved as the infection cleared.

NEAR (answer s): -Heart size normal on chest radiograph. | +No history of heart failure.

MISSING (answer neither (undetermined)): -Heart size normal on chest radiograph. | +Heart failure: not asked about.

PRES (answer s): full text
Patient: female, 20 years.
Requests contraception.
Drinks alcohol occasionally.
Her aunt completed physical therapy for a shoulder injury.
Drinks two cups of coffee a day.
No platelet-inhibiting drugs on the medication list.
Sings in a weekly choir.
Nails normal.
Her neighbor has a stutter.
Heart size normal on chest radiograph.
Wears a seat belt when driving.
Uses public transport.
Chloride 103 mmol/L in 2024.
Her housemate wears hearing aids.
Collects postcards.
Does crossword puzzles.
Hearing normal to conversation.
Albumin 4.1 g/dL in 2024 (routine blood test).
Ferritin 60 ng/mL in 2024.
Serum calcium 9.4 mg/dL in 2024.
Volunteers at a library.
Bakes bread at home.
Writes with the right hand.
Her brother broke a wrist, which has healed.


## 2.58 ('gs109', 'c1', 'numeric', 'long') templates=test

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the current heart rate is above 90/min or the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time, prescribe amlodipine instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Male patient of 39 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Has two cats.
His friend sprained a thumb last month.
Prefers to be addressed by first name.
Sees a dentist yearly.
Paints watercolors as a hobby.
Teeth in good repair.
In 2009, folate was 12 ng/mL.
Enjoys board games.
Cardiac stress test unremarkable last year.
His roommate burned a hand on a stove years ago.
Knits as a hobby.
His wife wears contact lenses.
Pupils equal and reactive to light.
During a checkup in 2019, free T3 was 3.2 pg/mL.
In 2018, lipase was 30 U/L.
Current heart rate 58/min.
Owns a bicycle.
His uncle has a lazy eye.
Plays the piano.

FLIP (answer s'): -Current heart rate 58/min. | +Current heart rate 108/min.

NEAR (answer s): -Current heart rate 58/min. | +Current heart rate 86/min.

MISSING (answer neither (undetermined)): -Current heart rate 58/min.

PRES (answer s): full text
Man of 39 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Cardiac stress test unremarkable last year.
In 2018, lipase was 30 U/L.
Enjoys board games.
In 2009, folate was 12 ng/mL.
Sees a dentist yearly.
Pupils equal and reactive to light.
Knits as a hobby.
Heart rate now 58/min on a pulse check.
His roommate burned a hand on a stove years ago.
His wife wears contact lenses.
His friend sprained a thumb last month.
Has two cats.
Prefers to be addressed by first name.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Teeth in good repair.
Owns a bicycle.
Plays the piano.
His uncle has a lazy eye.


## 2.59 ('gs025', 'c2', 'subject', 'long') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the current eGFR is below 30 mL/min/1.73 m2 or the patient is allergic to penicillin, prescribe naproxen with omeprazole instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
64 years old, female.
Hip osteoarthritis with pain on walking.
Her mother previously wore dental braces.
Uses public transport.
Vitamin D 38 ng/mL in 2021 (wellness visit).
Her coworker wears hearing aids.
Bakes bread at home.
Her brother is left-handed.
Feeds birds in the backyard.
Speaks English and Spanish.
Volunteers at a library.
Drinks plenty of water.
eGFR 77 mL/min/1.73 m2 on today's labs.
No known drug allergies.
Uses a smartphone for reminders.
Her housemate broke a wrist, which has healed.
Chloride 103 mmol/L in 2014.
Enjoys gardening.
Has a pet dog.
Nails normal.
Wears glasses when driving.
Height 170 cm.

FLIP (answer s'): -No known drug allergies. | +Allergies: penicillin (rash).

NEAR (answer s): -No known drug allergies. | +Her cousin carries an allergy alert card for penicillin.

MISSING (answer neither (undetermined)): -No known drug allergies. | +Penicillin allergy: not asked about.

PRES (answer s): full text
Patient: female, 64 years.
Hip osteoarthritis with pain on walking.
Feeds birds in the backyard.
Drinks plenty of water.
Volunteers at a library.
This morning's blood test shows an eGFR of 77 mL/min/1.73 m2.
Uses a smartphone for reminders.
Chloride 103 mmol/L in 2014.
Her brother is left-handed.
Wears glasses when driving.
Has a pet dog.
No known drug allergies.
Enjoys gardening.
Speaks English and Spanish.
Her mother previously wore dental braces.
Uses public transport.
Bakes bread at home.
Her coworker wears hearing aids.
Height 170 cm.
Her housemate broke a wrist, which has healed.
Nails normal.
Vitamin D 38 ng/mL in 2021 (wellness visit).


## 2.60 ('gs076', 'c2', 'time', 'easy') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. Score 2 points if the patient currently has tonsillar exudate; 3 points if the current white cell count is above 12.0 x10^9/L; 2 points if the current serum creatinine is above 2.0 mg/dL. If the score is 4 or more, prescribe diltiazem instead.
CONDITION: white cell count above 12.0
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Male patient of 58 years.
Atrial fibrillation with a ventricular rate of 128/min.
Back in 2014, white cell count stood at 7.1 x10^9/L.
Latest creatinine result: 0.6 mg/dL.
Owns a bicycle.
Has two cats.
Latest WBC is 7.6 x10^9/L.
Lives in a second-floor apartment.
Enjoys board games.
Tonsillar exudate visible on both sides.

FLIP (answer s'): -Latest WBC is 7.6 x10^9/L. | +Latest WBC is 13.7 x10^9/L.

NEAR (answer s): -Back in 2014, white cell count stood at 7.1 x10^9/L. | +Back in 2014, white cell count stood at 15.7 x10^9/L.

MISSING (answer neither (undetermined)): -Back in 2014, white cell count stood at 7.1 x10^9/L. | -Latest WBC is 7.6 x10^9/L.

PRES (answer s): full text
Man of 58 years.
Atrial fibrillation with a ventricular rate of 128/min.
Current white cell count 7.6 x10^9/L.
Current serum creatinine 0.6 mg/dL.
Owns a bicycle.
Tonsillar exudate visible on both sides.
Enjoys board games.
Has two cats.
Records from 2014 list white cell count at 7.1 x10^9/L.
Lives in a second-floor apartment.


## 2.61 ('s4_glasgow_imrie', 'age', 'boundary', 'easy') templates=train

RULE: Glasgow-Imrie score for acute pancreatitis (as used here, partial): 1 point each for age above 55 years; a current white cell count above 15.0 x10^9/L; a current blood urea nitrogen above 45 mg/dL. Other Glasgow-Imrie items are not part of this question.
CONDITION: age above 55
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Adult woman.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Height 170 cm.
Today's BUN is 36 mg/dL.
Hearing normal to conversation.
WBC 10.0 x10^9/L on today's sample.
Drinks plenty of water.
Age as of today: 47 years.

FLIP (answer s'): -Age as of today: 47 years. | +Age as of today: 82 years.

NEAR (answer s): -Age as of today: 47 years. | +Age as of today: 55 years.

MISSING (answer neither (undetermined)): -Age as of today: 47 years.

PRES (answer s): full text
Patient: female.
Acute pancreatitis confirmed by lipase and imaging; admitted for supportive care.
Age at this assessment: 47 years.
Height 170 cm.
Drinks plenty of water.
White cell count today: 10.0 x10^9/L.
Hearing normal to conversation.
BUN at this assessment: 36 mg/dL.


## 2.62 ('gs126', 'c2', 'negation', 'long') templates=test

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient has ever had asthma (current or past) or the patient is currently taking clarithromycin, prescribe azithromycin instead.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Woman of 68 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Paints watercolors as a hobby.
In 2020, lipase was 30 U/L.
Her friend lives with psoriasis.
Sees a dentist yearly.
Lungs clear, without wheeze or prolonged expiration.
Prefers morning appointments.
Photographs local wildlife.
Sleeps seven hours a night.
Owns a bicycle.
Her friend sprained a thumb last month.
Enjoys board games.
Lives in a second-floor apartment.
Has two cats.
Teeth in good repair.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2009.
Plays the piano.
Uses sunscreen in summer.
Current antibiotic therapy: none.
Knits as a hobby.
Drives a car.

FLIP (answer s'): -Current antibiotic therapy: none. | +Currently taking clarithromycin for an ear infection.

NEAR (answer s): -Current antibiotic therapy: none. | +Clarithromycin absent from the pharmacy dispensing record.

MISSING (answer neither (undetermined)): -Current antibiotic therapy: none. | +Clarithromycin: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 68 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Sleeps seven hours a night.
Teeth in good repair.
Has two cats.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Drives a car.
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Knits as a hobby.
Her friend sprained a thumb last month.
Photographs local wildlife.
Enjoys board games.
Lungs clear, without wheeze or prolonged expiration.
Her friend lives with psoriasis.
Owns a bicycle.
Sees a dentist yearly.
Prefers morning appointments.
Plays the piano.
Free T4 of 1.2 ng/dL in 2009.
Current antibiotic therapy: none.
Lives in a second-floor apartment.


## 2.63 ('gs191', 'c1', 'numeric', 'easy') templates=train

RULE: For musculoskeletal pain, prescribe ibuprofen. If the current eGFR is below 30 mL/min/1.73 m2 and the patient is currently taking warfarin, prescribe acetaminophen instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: female, 27 years.
Acute low back pain after lifting.
Medications: warfarin 5 mg once daily.
This morning's blood test shows an eGFR of 52 mL/min/1.73 m2.
Writes with the right hand.
Wears glasses when driving.
Wears a seat belt when driving.

FLIP (answer s'): -This morning's blood test shows an eGFR of 52 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 26 mL/min/1.73 m2.

NEAR (answer s): -This morning's blood test shows an eGFR of 52 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 33 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -This morning's blood test shows an eGFR of 52 mL/min/1.73 m2.

PRES (answer s): full text
27 years old, female.
Acute low back pain after lifting.
Renal function today: eGFR 52 mL/min/1.73 m2.
Wears glasses when driving.
Wears a seat belt when driving.
Writes with the right hand.
Medications: warfarin 5 mg once daily.


## 2.64 ('gs070', 'c1', 'subject', 'long') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current temperature is above 38.0 C; the patient has an active peptic ulcer.
CONDITION: vascular disease
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Female patient of 41 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Photographs local wildlife.
Her father has recovered from a dislocated finger.
Sleeps seven hours a night.
Temperature now 36.6 C (tympanic).
Active peptic ulcer disease.
Pupils equal and reactive to light.
In 2015, folate was 12 ng/mL.
Drives a car.
Zinc of 85 mcg/dL in 2017.
Her father sprained a thumb last month.
Knits as a hobby.
Enjoys board games.
Lives in a second-floor apartment.
Prefers morning appointments.
Uses sunscreen in summer.
Has two cats.
Her father lives with psoriasis.
Sees a dentist yearly.
Owns a bicycle.
Teeth in good repair.
Paints watercolors as a hobby.

FLIP (answer s'): +Has symptomatic peripheral artery disease of both legs.

NEAR (answer s): +Her uncle is in the hospital with a heart attack.

MISSING (answer neither (undetermined)): +Vascular disease: unknown.

PRES (answer s): full text
Woman of 41 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Current temperature 36.6 C.
Lives in a second-floor apartment.
Her father lives with psoriasis.
Her father sprained a thumb last month.
Active peptic ulcer disease.
Photographs local wildlife.
Sees a dentist yearly.
Her father has recovered from a dislocated finger.
Owns a bicycle.
Enjoys board games.
Uses sunscreen in summer.
Has two cats.
Zinc of 85 mcg/dL in 2017.
Knits as a hobby.
Prefers morning appointments.
In 2015, folate was 12 ng/mL.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Drives a car.


## 2.65 ('gs182', 'c1', 'time', 'long') templates=train

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. Score 1 point if the patient is currently taking clarithromycin; 1 point if the patient has ever had heparin-induced thrombocytopenia (current or past); 2 points if the patient currently has a major bleed; 2 points if the patient has ever had angioedema (current or past). If the score is 4 or more, prescribe intravenous co-amoxiclav instead.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
54 years old, female.
Community-acquired pneumonia confirmed on chest radiograph.
Speaks English and Spanish.
Drinks plenty of water.
Her housemate had a splinter removed from a finger.
Uses public transport.
Vaccinations up to date.
Lives on a quiet street.
Phosphate 3.6 mg/dL in 2021.
Sodium 140 mmol/L in 2011.
Writes with the right hand.
Wears a seat belt when driving.
Major retroperitoneal bleed seen on a CT scan this morning, needing urgent treatment.
Grows tomatoes in the garden.
Vitamin B12 450 pg/mL in 2024.
Keeps houseplants.
Collects postcards.
Nails normal.
Does crossword puzzles.
Heparin-induced thrombocytopenia in 2011 that resolved, with heparin avoided ever since.
Serum calcium 9.4 mg/dL in 2010.
Her housemate wears hearing aids.
Volunteers at a library.
Drinks alcohol occasionally.

FLIP (answer s'): +Started clarithromycin this morning for sinusitis.

NEAR (answer s): +Completed a course of clarithromycin in 2018.

MISSING (answer neither (undetermined)): +Clarithromycin: not yet assessed.

PRES (answer s): full text
Patient: female, 54 years.
Community-acquired pneumonia confirmed on chest radiograph.
Sodium 140 mmol/L in 2011.
Drinks plenty of water.
Heparin-induced thrombocytopenia in 2011 that resolved, with heparin avoided ever since.
Vaccinations up to date.
Keeps houseplants.
Volunteers at a library.
Lives on a quiet street.
Major retroperitoneal bleed seen on a CT scan this morning, needing urgent treatment.
Collects postcards.
Does crossword puzzles.
Nails normal.
Writes with the right hand.
Uses public transport.
Her housemate had a splinter removed from a finger.
Drinks alcohol occasionally.
Her housemate wears hearing aids.
Grows tomatoes in the garden.
Vitamin B12 450 pg/mL in 2024.
Phosphate 3.6 mg/dL in 2021.
Serum calcium 9.4 mg/dL in 2010.
Wears a seat belt when driving.
Speaks English and Spanish.


## 2.66 ('curb65', 'sbp', 'boundary', 'long') templates=test

RULE: CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
CONDITION: blood pressure below 90
CLAIMS: s = 'The blood pressure criterion contributes 0 points.' | s' = 'The blood pressure criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Teeth in good repair.
Sleeps seven hours a night.
Drives a car.
Prefers morning appointments.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2015.
Owns a bicycle.
Observations now: blood pressure 139/87 mmHg.
Photographs local wildlife.
Enjoys board games.
Her sister has a lazy eye.
In 2017, folate was 12 ng/mL.
Has two cats.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2018.
Sees a dentist yearly.
Currently aged 55 years.
Plays the piano.
Her father burned a hand on a stove years ago.
Current respiratory rate 22/min.
Blood urea nitrogen now: 14 mg/dL.
Prefers to be addressed by first name.

FLIP (answer s'): -Observations now: blood pressure 139/87 mmHg. | +Observations now: blood pressure 84/54 mmHg.

NEAR (answer s): -Observations now: blood pressure 139/87 mmHg. | +Observations now: blood pressure 90/58 mmHg.

MISSING (answer neither (undetermined)): -Observations now: blood pressure 139/87 mmHg.

PRES (answer s): full text
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Zinc of 85 mcg/dL in 2015.
Observations now: respiratory rate 22/min.
Pupils equal and reactive to light.
Prefers morning appointments.
Plays the piano.
Sleeps seven hours a night.
In 2017, folate was 12 ng/mL.
Owns a bicycle.
Blood urea nitrogen 14 mg/dL on the current labs.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2018.
Lives in a second-floor apartment.
Current age 55 years.
Photographs local wildlife.
Current systolic blood pressure 139 mmHg.
Her sister has a lazy eye.
Has two cats.
Teeth in good repair.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Drives a car.
Her father burned a hand on a stove years ago.
Enjoys board games.


## 2.67 ('gs189', 'c2', 'negation', 'easy') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient currently has a venous thromboembolism, prescribe fondaparinux instead.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Patient: male, 80 years.
First day after elective total hip replacement.
Non-smoker.
Speaks English and Spanish.
Not on any blood thinners.
His brother is being treated for colorectal cancer.

FLIP (answer s'): -Not on any blood thinners. | +On treatment for a deep vein thrombosis in the left leg.

NEAR (answer s): -Not on any blood thinners. | +Medical records show no venous thromboembolism, and none is reported in first-degree relatives.

MISSING (answer neither (undetermined)): -Not on any blood thinners. | +Current venous thromboembolism: could not be determined from the information available.

PRES (answer s): full text
Male, 80 years.
First day after elective total hip replacement.
His brother is being treated for colorectal cancer.
Not on any blood thinners.
Speaks English and Spanish.
Non-smoker.


## 2.68 ('s4_abcd2', 'age', 'numeric', 'easy') templates=test

RULE: ABCD2 score (as used here, partial): 1 point each for age 60 years or more; a current systolic blood pressure of 140 mmHg or more; diabetes at any time. Clinical features and duration of symptoms are not part of this question.
CONDITION: age at least 60
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
An adult man.
Transient weakness of the left arm lasting 20 minutes; assessed in a rapid-access clinic.
Lives in a second-floor apartment.
Photographs local wildlife.
Current systolic blood pressure 131 mmHg.
Currently aged 39 years.
HbA1c 5.3% at a routine check.

FLIP (answer s'): -Currently aged 39 years. | +Currently aged 77 years.

NEAR (answer s): -Currently aged 39 years. | +Currently aged 58 years.

MISSING (answer neither (undetermined)): -Currently aged 39 years.

PRES (answer s): full text
Man, adult.
Transient weakness of the left arm lasting 20 minutes; assessed in a rapid-access clinic.
Lives in a second-floor apartment.
Current age 39 years.
HbA1c 5.3% at a routine check.
Photographs local wildlife.
Observations now: blood pressure 131/83 mmHg.


## 2.69 ('gs095', 'c1', 'subject', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time or the current white cell count is above 12.0 x10^9/L, prescribe amlodipine instead.
CONDITION: coronary artery disease in the patient or a first-degree relative
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Male, 56 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
His coworker broke a wrist, which has healed.
Listens to podcasts.
Non-smoker.
Enjoys cooking.
Vaccinations up to date.
Uses a smartphone for reminders.
Wears a seat belt when driving.
Total bilirubin 0.6 mg/dL in 2024.
Complete blood count this morning: white cell count 5.4 x10^9/L.
Hearing normal to conversation.
Plays chess online.
His cousin has a stutter.
Resting ECG shows no ischemic changes.
Bakes bread at home.
Drinks alcohol occasionally.
Ferritin 60 ng/mL in 2008.
Feeds birds in the backyard.
His housemate completed physical therapy for a shoulder injury.
Lives on a quiet street.

FLIP (answer s'): -Resting ECG shows no ischemic changes. | +His mother previously had coronary artery disease, treated with angioplasty.

NEAR (answer s): -Resting ECG shows no ischemic changes. | +His neighbor had coronary artery disease found on a stress test in 2020.

MISSING (answer neither (undetermined)): -Resting ECG shows no ischemic changes. | +Coronary artery disease in the patient or a first-degree relative: could not be determined from the information available.

PRES (answer s): full text
56 years old, male.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Enjoys cooking.
WBC on the blood count drawn at this assessment: 5.4 x10^9/L.
Wears a seat belt when driving.
Plays chess online.
Drinks alcohol occasionally.
His coworker broke a wrist, which has healed.
Ferritin 60 ng/mL in 2008.
Vaccinations up to date.
Resting ECG shows no ischemic changes.
Hearing normal to conversation.
Non-smoker.
Total bilirubin 0.6 mg/dL in 2024.
His cousin has a stutter.
His housemate completed physical therapy for a shoulder injury.
Bakes bread at home.
Listens to podcasts.
Lives on a quiet street.
Feeds birds in the backyard.
Uses a smartphone for reminders.


## 2.70 ('s2_geneva', 'cancer', 'time', 'long') templates=test

RULE: Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.
CONDITION: active cancer
CLAIMS: s = 'The active cancer criterion contributes 0 points.' | s' = 'The active cancer criterion contributes 2 points.'

BASE (answer s):
An adult woman.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Drives a car.
Uses sunscreen in summer.
Her sister sprained a thumb last month.
Currently aged 48 years.
Prefers to be addressed by first name.
Teeth in good repair.
Sees a dentist yearly.
Her roommate has recovered from a dislocated finger.
Pupils equal and reactive to light.
In 2006, lipase was 30 U/L.
Photographs local wildlife.
In 2019, folate was 12 ng/mL.
Dry cough, with nothing brought up.
Her uncle wears contact lenses.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Plays the piano.
Owns a bicycle.

FLIP (answer s'): +Has metastatic lung cancer, receiving palliative treatment.

NEAR (answer s): +Had thyroid cancer years ago and is now cured.

MISSING (answer neither (undetermined)): +Active cancer: status unclear from the records at hand.

PRES (answer s): full text
Woman, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Sees a dentist yearly.
Prefers to be addressed by first name.
Dry cough, with nothing brought up.
In 2019, folate was 12 ng/mL.
Teeth in good repair.
Plays the piano.
Her uncle wears contact lenses.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Her friend burned a hand on a stove years ago.
Knits as a hobby.
Her sister sprained a thumb last month.
Owns a bicycle.
Drives a car.
Her roommate has recovered from a dislocated finger.
Photographs local wildlife.
In 2006, lipase was 30 U/L.
Current age 48 years.


## 2.71 ('gs186', 'c2', 'boundary', 'long') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient is allergic to sulfonamide antibiotics or the current ALT is above 120 U/L, prescribe intermittent pneumatic compression instead.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Female, 76 years.
Admitted for community-acquired pneumonia; immobile.
Watches football on weekends.
Drinks plenty of water.
Albumin 4.1 g/dL in 2017 (routine blood test).
Collects postcards.
Sings in a weekly choir.
Phosphate 3.6 mg/dL in 2023.
Bicarbonate 26 mmol/L in 2023 (annual physical).
Her brother-in-law previously wore dental braces.
Her partner broke a wrist, which has healed.
Feeds birds in the backyard.
Her brother had a splinter removed from a finger.
Does crossword puzzles.
Ferritin 60 ng/mL in 2020.
Denies allergies to any drug or food.
Lives on a quiet street.
ALT 39 U/L on today's labs.
Enjoys gardening.

FLIP (answer s'): -ALT 39 U/L on today's labs. | +ALT 391 U/L on today's labs.

NEAR (answer s): -ALT 39 U/L on today's labs. | +ALT 120 U/L on today's labs.

MISSING (answer neither (undetermined)): -ALT 39 U/L on today's labs.

PRES (answer s): full text
76 years old, female.
Admitted for community-acquired pneumonia; immobile.
Sings in a weekly choir.
Ferritin 60 ng/mL in 2020.
Collects postcards.
Phosphate 3.6 mg/dL in 2023.
Feeds birds in the backyard.
Watches football on weekends.
Her brother-in-law previously wore dental braces.
Denies allergies to any drug or food.
Bicarbonate 26 mmol/L in 2023 (annual physical).
ALT today: 39 U/L.
Albumin 4.1 g/dL in 2017 (routine blood test).
Does crossword puzzles.
Drinks plenty of water.
Her partner broke a wrist, which has healed.
Her brother had a splinter removed from a finger.
Enjoys gardening.
Lives on a quiet street.


## 2.72 ('gs219', 'c2', 'negation', 'long') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current serum creatinine is 1.5 mg/dL or more or the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: venous thromboembolism in the patient or a first-degree relative
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Woman of 41 years.
Suspected chest infection; assessed on the medical ward.
Drives a car.
Prefers morning appointments.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Latest creatinine result: 0.7 mg/dL.
In 2015, lipase was 30 U/L.
Her uncle has a lazy eye.
Owns a bicycle.
Her friend sprained a thumb last month.
Enjoys board games.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Teeth in good repair.
Photographs local wildlife.
During a checkup in 2023, free T3 was 3.2 pg/mL.
In 2009, folate was 12 ng/mL.
Has two cats.
Zinc of 85 mcg/dL in 2023.
Her roommate wears contact lenses.

FLIP (answer s'): +Her sister recovered from a pulmonary embolism in 2018.

NEAR (answer s): +Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.

MISSING (answer neither (undetermined)): +Venous thromboembolism in the patient or a first-degree relative: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 41 years.
Suspected chest infection; assessed on the medical ward.
Prefers to be addressed by first name.
Current serum creatinine 0.7 mg/dL.
Teeth in good repair.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2023, free T3 was 3.2 pg/mL.
In 2015, lipase was 30 U/L.
Paints watercolors as a hobby.
Enjoys board games.
Her roommate wears contact lenses.
Owns a bicycle.
Drives a car.
In 2009, folate was 12 ng/mL.
Her uncle has a lazy eye.
Photographs local wildlife.
Uses sunscreen in summer.
Zinc of 85 mcg/dL in 2023.
Has two cats.
Her friend sprained a thumb last month.


## 2.73 ('gs001', 'c2', 'numeric', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the current white cell count is above 12.0 x10^9/L and the current serum creatinine is 1.5 mg/dL or more, prescribe a progestin-only pill instead.
CONDITION: serum creatinine at least 1.5
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
28-year-old woman.
Requests contraception.
Kidney function today: creatinine 0.9 mg/dL.
Uses public transport.
WBC 17.8 x10^9/L on today's sample.
Plays chess online.

FLIP (answer s'): -Kidney function today: creatinine 0.9 mg/dL. | +Kidney function today: creatinine 1.8 mg/dL.

NEAR (answer s): -Kidney function today: creatinine 0.9 mg/dL. | +Kidney function today: creatinine 1.4 mg/dL.

MISSING (answer neither (undetermined)): -Kidney function today: creatinine 0.9 mg/dL.

PRES (answer s): full text
Female, 28 years.
Requests contraception.
White cell count today: 17.8 x10^9/L.
Plays chess online.
Uses public transport.
Blood panel at this assessment: creatinine 0.9 mg/dL.


## 2.74 ('gs234', 'c1', 'subject', 'easy') templates=test

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the patient currently has heart failure, prescribe intravenous co-amoxiclav instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
Man of 51 years.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Photographs local wildlife.
Lives in a second-floor apartment.

FLIP (answer s'): +Has heart failure, treated with diuretics.

NEAR (answer s): +His uncle is treated for heart failure.

MISSING (answer neither (undetermined)): +Current heart failure: unknown.

PRES (answer s): full text
Male patient of 51 years.
Community-acquired pneumonia confirmed on chest radiograph.
Owns a bicycle.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Photographs local wildlife.


## 2.75 ('s3_charlson', 'cr', 'time', 'alt') templates=train

RULE: Charlson Comorbidity Index (as used here, partial): 1 point for heart failure at any time (current or past); 1 point for a myocardial infarction or peripheral artery disease at any time (current or past); 1 point for current asthma; 2 points for a current serum creatinine above 2.0 mg/dL. Age and other Charlson items are not part of this question.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'The serum creatinine criterion contributes 0 points.' | s' = 'The serum creatinine criterion contributes 2 points.'

BASE (answer s):
Female, 68 years.
Inpatient on the medical ward; comorbidity review.
No night cough or chest tightness.
Takes no diuretics.
Serum creatinine 1.7 mg/dL at a hospital visit in 2016.
Vaccinations up to date.
Creatinine 2.0 mg/dL on this morning's labs.
Enjoys gardening.

FLIP (answer s'): -Creatinine 2.0 mg/dL on this morning's labs. | +Creatinine 2.5 mg/dL on this morning's labs.

NEAR (answer s): -Serum creatinine 1.7 mg/dL at a hospital visit in 2016. | +Serum creatinine 3.4 mg/dL at a hospital visit in 2016.

MISSING (answer neither (undetermined)): -Serum creatinine 1.7 mg/dL at a hospital visit in 2016. | -Creatinine 2.0 mg/dL on this morning's labs.

PRES (answer s): full text
68 years old, female.
Inpatient on the medical ward; comorbidity review.
No night cough or chest tightness.
Kidney function today: creatinine 2.0 mg/dL.
Serum creatinine was 1.7 mg/dL when measured in 2016.
Vaccinations up to date.
Takes no diuretics.
Enjoys gardening.
