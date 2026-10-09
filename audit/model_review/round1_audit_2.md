# Audit sample 2


## 2.1 ('centor', 'temp', 'boundary', 'long') templates=train

RULE: Centor score (as used here, partial): 1 point each for temperature above 38.0 C; tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.
CONDITION: temperature above 38.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
A 34-year-old man.
Sore throat for three days.
Uses reading glasses for small print.
TSH 1.6 mIU/L in 2010.
Eats a varied diet.
Feeds birds in the backyard.
Writes with the right hand.
Temperature today: 36.8 C.
Vitamin D 38 ng/mL in 2018 (wellness visit).
Hearing normal to conversation.
His coworker completed physical therapy for a shoulder injury.
Sings in a weekly choir.
Volunteers at a library.
Plays chess online.
Keeps a step counter.
Reads most evenings.
Listens to podcasts.
His brother-in-law has a broken finger in a splint.
His cousin is left-handed.
Grows tomatoes in the garden.
Drinks plenty of water.

FLIP (answer s'): -Temperature today: 36.8 C. | +Temperature today: 39.4 C.

NEAR (answer s): -Temperature today: 36.8 C. | +Temperature today: 38.0 C.

MISSING (answer neither (undetermined)): -Temperature today: 36.8 C.

PRES (answer s): full text
Patient: male, 34 years.
Sore throat for three days.
Writes with the right hand.
Temperature 36.8 C at this assessment.
His coworker completed physical therapy for a shoulder injury.
Hearing normal to conversation.
His brother-in-law has a broken finger in a splint.
Sings in a weekly choir.
Volunteers at a library.
Vitamin D 38 ng/mL in 2018 (wellness visit).
Listens to podcasts.
Grows tomatoes in the garden.
Reads most evenings.
Keeps a step counter.
Drinks plenty of water.
Plays chess online.
His cousin is left-handed.
Feeds birds in the backyard.
TSH 1.6 mIU/L in 2010.
Uses reading glasses for small print.
Eats a varied diet.


## 2.2 ('gs225', 'c1', 'negation', 'long') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. If at least two of the following apply, prescribe diltiazem instead: the patient has ever had angioedema (current or past); the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the current systolic blood pressure is below 100 mmHg.
CONDITION: angioedema
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Woman of 52 years.
Atrial fibrillation with a ventricular rate of 128/min.
Current systolic blood pressure 159 mmHg.
Her father lives with psoriasis.
Had coronary artery disease, treated with bypass surgery in 2017; recovered well.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her roommate wears contact lenses.
Prefers morning appointments.
Sees a dentist yearly.
During a checkup in 2005, total protein was 7.0 g/dL.
Drives a car.
Teeth in good repair.
Has two cats.
Owns a bicycle.
Lives in a second-floor apartment.
Plays the piano.
Free of facial or oropharyngeal edema.

FLIP (answer s'): -Free of facial or oropharyngeal edema. | +Formerly had recurrent angioedema, in remission for many years now.

NEAR (answer s): -Free of facial or oropharyngeal edema. | +Has never had angioedema.

MISSING (answer neither (undetermined)): -Free of facial or oropharyngeal edema. | +Angioedema: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 52 years.
Atrial fibrillation with a ventricular rate of 128/min.
Sees a dentist yearly.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Plays the piano.
Owns a bicycle.
Observations now: blood pressure 159/99 mmHg.
Has two cats.
Her roommate wears contact lenses.
During a checkup in 2005, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Drives a car.
Her father lives with psoriasis.
Teeth in good repair.
Face and neck without swelling on examination.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Had coronary artery disease, treated with bypass surgery in 2017; recovered well.
Prefers morning appointments.


## 2.3 ('c1_neutropenia', 'anc', 'numeric', 'alt') templates=train

RULE: For a chest infection during chemotherapy, prescribe oral co-amoxiclav. If the current neutrophil count is 1.0 x10^9/L or less, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: neutrophil count at or below 1.0
CLAIMS: s = 'Prescribe oral co-amoxiclav.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
A 53-year-old woman.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Enjoys cooking.
Uses a smartphone for reminders.
Hearing normal to conversation.
Blood count today: neutrophil count 2.6 x10^9/L.
Nails normal.

FLIP (answer s'): -Blood count today: neutrophil count 2.6 x10^9/L. | +Blood count today: neutrophil count 0.7 x10^9/L.

NEAR (answer s): -Blood count today: neutrophil count 2.6 x10^9/L. | +Blood count today: neutrophil count 1.2 x10^9/L.

MISSING (answer neither (undetermined)): -Blood count today: neutrophil count 2.6 x10^9/L.

PRES (answer s): full text
53-year-old woman.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Neutrophil count at this assessment: 2.6 x10^9/L.
Uses a smartphone for reminders.
Enjoys cooking.
Hearing normal to conversation.
Nails normal.


## 2.4 ('gs176', 'c4', 'subject', 'long') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. Score 2 points if the patient has ever had a stroke or TIA (current or past); 3 points if the patient is currently taking clarithromycin; 2 points if the patient is currently taking warfarin; 2 points if the patient is allergic to sulfonamide antibiotics. If the score is 6 or more, prescribe fondaparinux instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Woman of 58 years.
First day after elective total hip replacement.
Enjoys board games.
Pupils equal and reactive to light.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Transient ischemic attack this week; carotid imaging is pending.
Zinc of 85 mcg/dL in 2008.
In 2016, lipase was 30 U/L.
Her roommate has a lazy eye.
Prefers morning appointments.
Knits as a hobby.
Sleeps seven hours a night.
Sees a dentist yearly.
Currently taking clarithromycin for an ear infection.
Plays the piano.
Medication allergies: none at present.
During a checkup in 2007, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
Her sister wears contact lenses.
Has two cats.

FLIP (answer s'): -Medication allergies: none at present. | +Develops hives whenever given sulfonamide antibiotics.

NEAR (answer s): -Medication allergies: none at present. | +Her wife has a sulfonamide antibiotic allergy.

MISSING (answer neither (undetermined)): -Medication allergies: none at present. | +Sulfonamide allergy: unknown.

PRES (answer s): full text
Female patient of 58 years.
First day after elective total hip replacement.
Her sister wears contact lenses.
Prefers morning appointments.
In 2016, lipase was 30 U/L.
Her roommate has a lazy eye.
Enjoys board games.
Zinc of 85 mcg/dL in 2008.
Has weakness of the left arm from a stroke this month.
Sleeps seven hours a night.
On clarithromycin for a chest infection, day 3 of 7.
Current drug allergies: none.
Has two cats.
During a checkup in 2007, total protein was 7.0 g/dL.
Plays the piano.
Sees a dentist yearly.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Knits as a hobby.
Pupils equal and reactive to light.


## 2.5 ('gs196', 'c1', 'time', 'easy') templates=train

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient currently has tonsillar exudate or the patient currently has tender anterior cervical lymph nodes, prescribe acetaminophen instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Female, 44 years.
Acute low back pain after lifting.
Wears a seat belt when driving.
Collects postcards.
Nails normal.

FLIP (answer s'): +Creamy exudate in the tonsillar crypts today.

NEAR (answer s): +Previously had white exudate on the tonsils in 2020, since resolved.

MISSING (answer neither (undetermined)): +Tonsillar exudate: not asked about.

PRES (answer s): full text
A 44-year-old woman.
Acute low back pain after lifting.
Collects postcards.
Nails normal.
Wears a seat belt when driving.


## 2.6 ('hasbled', 'age', 'boundary', 'easy') templates=test

RULE: HAS-BLED (as used here, partial): 1 point each for a current systolic blood pressure above 160 mmHg; a major bleeding event at any time; age above 65 years; current use of aspirin. Other HAS-BLED items are not part of this question.
CONDITION: age above 65
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Atrial fibrillation; anticoagulation being considered.
Antiplatelet therapy: none at present.
Observations now: blood pressure 139/87 mmHg.
Prefers to be addressed by first name.
Currently aged 58 years.

FLIP (answer s'): -Currently aged 58 years. | +Currently aged 75 years.

NEAR (answer s): -Currently aged 58 years. | +Currently aged 65 years.

MISSING (answer neither (undetermined)): -Currently aged 58 years.

PRES (answer s): full text
An adult woman.
Atrial fibrillation; anticoagulation being considered.
Current systolic blood pressure 139 mmHg.
Current age 58 years.
Prefers to be addressed by first name.
Current antiplatelet drugs: none.


## 2.7 ('gs183', 'c2', 'negation', 'easy') templates=train

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient currently has tender anterior cervical lymph nodes or the patient has had a major bleeding event at any time, prescribe acetaminophen instead.
CONDITION: bleeding history
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: male, 23 years.
Acute low back pain after lifting.
Writes with the right hand.
Collects postcards.
No hematuria or hemoptysis.
Hearing normal to conversation.
No tender swellings in the neck.

FLIP (answer s'): -No hematuria or hemoptysis. | +Previously transfused for a major bleed from a stomach ulcer, which healed in 2022.

NEAR (answer s): -No hematuria or hemoptysis. | +Bleeding history: no major bleeds.

MISSING (answer neither (undetermined)): -No hematuria or hemoptysis. | +Information on bleeding history was not obtained.

PRES (answer s): full text
A 23-year-old man.
Acute low back pain after lifting.
Neck glands cannot be felt.
Conjunctivae pink, with no pallor.
Writes with the right hand.
Collects postcards.
Hearing normal to conversation.


## 2.8 ('gs139', 'c2', 'numeric', 'long') templates=test

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient currently has tonsillar exudate or the current heart rate is 131/min or more, prescribe intermittent pneumatic compression instead.
CONDITION: heart rate at least 131
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Female patient of 72 years.
Admitted for community-acquired pneumonia; immobile.
Her friend lives with psoriasis.
Sees a dentist yearly.
Tonsils slightly red but clean, without pus.
Her wife burned a hand on a stove years ago.
Current heart rate 81/min.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
In 2009, folate was 12 ng/mL.
Drives a car.
Prefers morning appointments.
Her sister has recovered from a dislocated finger.
Enjoys board games.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2021.
Knits as a hobby.
Has two cats.
During a checkup in 2005, total protein was 7.0 g/dL.

FLIP (answer s'): -Current heart rate 81/min. | +Current heart rate 160/min.

NEAR (answer s): -Current heart rate 81/min. | +Current heart rate 129/min.

MISSING (answer neither (undetermined)): -Current heart rate 81/min.

PRES (answer s): full text
Woman of 72 years.
Admitted for community-acquired pneumonia; immobile.
In 2009, folate was 12 ng/mL.
Pupils equal and reactive to light.
Her friend lives with psoriasis.
Drives a car.
Her wife burned a hand on a stove years ago.
Enjoys board games.
Tonsils pink and clean on inspection.
Has two cats.
Heart rate now 81/min on the monitor.
During a checkup in 2005, total protein was 7.0 g/dL.
Her sister has recovered from a dislocated finger.
Sees a dentist yearly.
Knits as a hobby.
Zinc of 85 mcg/dL in 2021.
Prefers morning appointments.
Lives in a second-floor apartment.
Prefers to be addressed by first name.


## 2.9 ('gs100', 'c1', 'subject', 'long') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. If the patient has ever had a stroke or TIA (current or past) or the patient is currently taking aspirin, prescribe acetaminophen instead.
CONDITION: stroke/TIA
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Female, 85 years.
Knee osteoarthritis with pain on walking.
Volunteers at a library.
Uses reading glasses for small print.
Drinks plenty of water.
Visual fields full to confrontation.
No platelet-inhibiting drugs on the medication list.
Her cousin has a broken finger in a splint.
Vaccinations up to date.
Her coworker had a splinter removed from a finger.
Enjoys cooking.
Does crossword puzzles.
Wears a seat belt when driving.
Non-smoker.
Her coworker is nearsighted.
Writes with the right hand.
Eats a varied diet.
Chloride 103 mmol/L in 2018.
Bicarbonate 26 mmol/L in 2008 (annual physical).
Uses a smartphone for reminders.
Bakes bread at home.
Keeps houseplants.

FLIP (answer s'): -Visual fields full to confrontation. | +Brain MRI today shows a new ischemic stroke.

NEAR (answer s): -Visual fields full to confrontation. | +Her husband is recovering from a stroke this month.

MISSING (answer neither (undetermined)): -Visual fields full to confrontation. | +Information on stroke/TIA was not obtained.

PRES (answer s): full text
Patient: female, 85 years.
Knee osteoarthritis with pain on walking.
Bakes bread at home.
Drinks plenty of water.
Enjoys cooking.
Takes no daily pill to stop platelets from clumping.
Non-smoker.
Writes with the right hand.
Keeps houseplants.
Wears a seat belt when driving.
Her cousin has a broken finger in a splint.
Eats a varied diet.
Uses reading glasses for small print.
Uses a smartphone for reminders.
Chloride 103 mmol/L in 2018.
Cranial nerves intact.
Her coworker had a splinter removed from a finger.
Bicarbonate 26 mmol/L in 2008 (annual physical).
Vaccinations up to date.
Her coworker is nearsighted.
Does crossword puzzles.
Volunteers at a library.


## 2.10 ('s2_khorana', 'hgb', 'time', 'long') templates=test

RULE: Khorana score (as used here, partial): 1 point each for a current platelet count of 350 x10^9/L or more; a current hemoglobin below 10.0 g/dL; a current white cell count above 11.0 x10^9/L; a current body mass index of 35.0 kg/m2 or more. Other Khorana items, including the cancer site, are not part of this question.
CONDITION: hemoglobin below 10.0
CLAIMS: s = 'The hemoglobin criterion contributes 0 points.' | s' = 'The hemoglobin criterion contributes 1 point.'

BASE (answer s):
Man of 61 years.
Newly diagnosed colon cancer; first chemotherapy cycle planned for next week.
Plays the piano.
Sleeps seven hours a night.
Back in 2012, Hgb measured 13.4 g/dL.
Enjoys board games.
Paints watercolors as a hobby.
In 2005, folate was 12 ng/mL.
His father wears contact lenses.
Photographs local wildlife.
Prefers to be addressed by first name.
Owns a bicycle.
Prefers morning appointments.
Has two cats.
Platelet count now 208 x10^9/L.
Latest BMI is 30.5 kg/m2.
During a checkup in 2008, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
Drives a car.
Current white cell count 6.9 x10^9/L.
Latest Hgb result: 14.9 g/dL.
Teeth in good repair.
Pupils equal and reactive to light.
His sister lives with psoriasis.

FLIP (answer s'): -Latest Hgb result: 14.9 g/dL. | +Latest Hgb result: 8.1 g/dL.

NEAR (answer s): -Back in 2012, Hgb measured 13.4 g/dL. | +Back in 2012, Hgb measured 8.0 g/dL.

MISSING (answer neither (undetermined)): -Back in 2012, Hgb measured 13.4 g/dL. | -Latest Hgb result: 14.9 g/dL.

PRES (answer s): full text
Male patient of 61 years.
Newly diagnosed colon cancer; first chemotherapy cycle planned for next week.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2008, total protein was 7.0 g/dL.
His sister lives with psoriasis.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Drives a car.
Current platelet count 208 x10^9/L.
His father wears contact lenses.
Photographs local wildlife.
Plays the piano.
Latest WBC is 6.9 x10^9/L.
Teeth in good repair.
In 2005, folate was 12 ng/mL.
Prefers to be addressed by first name.
Owns a bicycle.
Records from 2012 list Hgb at 13.4 g/dL.
Lives in a second-floor apartment.
Current body mass index 30.5 kg/m2.
Has two cats.
Current Hgb 14.9 g/dL.
Enjoys board games.


## 2.11 ('gs150', 'c1', 'boundary', 'long') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If the current ALT is above 120 U/L or the patient currently has heart failure, prescribe a progestin-only pill instead.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Patient: female, 21 years.
Requests contraception.
Sings in a weekly choir.
ALT 60 U/L on today's labs.
Lives on a quiet street.
Has a pet dog.
Heart size normal on chest radiograph.
Serum calcium 9.4 mg/dL in 2023.
Hearing normal to conversation.
Watches football on weekends.
Volunteers at a library.
Feeds birds in the backyard.
Vitamin B12 450 pg/mL in 2024.
Height 170 cm.
Chloride 103 mmol/L in 2024.
Reads most evenings.
Her grandfather wears hearing aids.
Her grandfather is being treated for eczema.
Vitamin D 38 ng/mL in 2023 (wellness visit).
Uses public transport.
Uses reading glasses for small print.
Uses a smartphone for reminders.

FLIP (answer s'): -ALT 60 U/L on today's labs. | +ALT 250 U/L on today's labs.

NEAR (answer s): -ALT 60 U/L on today's labs. | +ALT 120 U/L on today's labs.

MISSING (answer neither (undetermined)): -ALT 60 U/L on today's labs.

PRES (answer s): full text
A 21-year-old woman.
Requests contraception.
Hearing normal to conversation.
Vitamin B12 450 pg/mL in 2024.
Chloride 103 mmol/L in 2024.
Uses a smartphone for reminders.
Her grandfather wears hearing aids.
Jugular venous pressure not raised.
Feeds birds in the backyard.
Watches football on weekends.
Reads most evenings.
Volunteers at a library.
Vitamin D 38 ng/mL in 2023 (wellness visit).
ALT today: 60 U/L.
Sings in a weekly choir.
Uses reading glasses for small print.
Her grandfather is being treated for eczema.
Has a pet dog.
Uses public transport.
Height 170 cm.
Lives on a quiet street.
Serum calcium 9.4 mg/dL in 2023.


## 2.12 ('gs244', 'c1', 'negation', 'long') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient has ever had coronary artery disease (current or past) or the patient currently has tonsillar exudate, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: coronary artery disease
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male patient of 42 years.
Suspected chest infection; assessed on the medical ward.
Zinc of 85 mcg/dL in 2007.
During a checkup in 2022, total protein was 7.0 g/dL.
Owns a bicycle.
Sees a dentist yearly.
Prefers to be addressed by first name.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Teeth in good repair.
Sleeps seven hours a night.
Has two cats.
In 2022, folate was 12 ng/mL.
His father has recovered from a dislocated finger.
Tonsils slightly red but clean, without pus.
Climbs two flights of stairs without symptoms.
His roommate sprained a thumb last month.
Prefers morning appointments.
Lives in a second-floor apartment.

FLIP (answer s'): -Climbs two flights of stairs without symptoms. | +Known coronary artery disease (two-vessel disease on angiography).

NEAR (answer s): -Climbs two flights of stairs without symptoms. | +Never diagnosed with coronary artery disease.

MISSING (answer neither (undetermined)): -Climbs two flights of stairs without symptoms. | +Coronary artery disease: unknown.

PRES (answer s): full text
Man of 42 years.
Suspected chest infection; assessed on the medical ward.
Teeth in good repair.
Has two cats.
His father has recovered from a dislocated finger.
Tonsils pink and clean on inspection.
During a checkup in 2022, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
His roommate sprained a thumb last month.
Sleeps seven hours a night.
In 2022, folate was 12 ng/mL.
Paints watercolors as a hobby.
Sees a dentist yearly.
Owns a bicycle.
Prefers morning appointments.
Chest pain on exertion: none reported.
Zinc of 85 mcg/dL in 2007.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.


## 2.13 ('all_spiro', 'egfr', 'numeric', 'easy') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone 25 mg daily. If the current serum potassium is above 4.8 mmol/L and the current eGFR is below 50 mL/min/1.73 m2, prescribe spironolactone 12.5 mg daily instead.
CONDITION: eGFR below 50
CLAIMS: s = 'Prescribe spironolactone 25 mg daily.' | s' = 'Prescribe spironolactone 12.5 mg daily.'

BASE (answer s):
Patient: female, 56 years.
Heart failure with reduced ejection fraction (ejection fraction 32%).
Serum potassium today: 5.0 mmol/L.
This morning's blood test shows an eGFR of 79 mL/min/1.73 m2.
Wears a seat belt when driving.
Hearing normal to conversation.

FLIP (answer s'): -This morning's blood test shows an eGFR of 79 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 35 mL/min/1.73 m2.

NEAR (answer s): -This morning's blood test shows an eGFR of 79 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 52 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -This morning's blood test shows an eGFR of 79 mL/min/1.73 m2.

PRES (answer s): full text
A 56-year-old woman.
Heart failure with reduced ejection fraction (ejection fraction 32%).
Labs this morning: potassium 5.0 mmol/L.
eGFR 79 mL/min/1.73 m2 on today's labs.
Hearing normal to conversation.
Wears a seat belt when driving.


## 2.14 ('gs236', 'c1', 'subject', 'easy') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the patient is currently taking warfarin or the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe clindamycin instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Female patient of 64 years.
Spreading redness and warmth of the right shin for two days.
Current anticoagulants: none.
Teeth in good repair.
Pupils equal and reactive to light.
Plays the piano.

FLIP (answer s'): -Current anticoagulants: none. | +Anticoagulated with warfarin; INR checked monthly at the clinic.

NEAR (answer s): -Current anticoagulants: none. | +Her friend is anticoagulated with warfarin.

MISSING (answer neither (undetermined)): -Current anticoagulants: none. | +Warfarin: status unclear from the records at hand.

PRES (answer s): full text
Woman of 64 years.
Spreading redness and warmth of the right shin for two days.
Plays the piano.
Pupils equal and reactive to light.
Teeth in good repair.
Anticoagulant therapy: none at present.


## 2.15 ('s1_sofa', 'map', 'time', 'easy') templates=train

RULE: SOFA score (as used here, partial): 1 point each for a current platelet count below 150 x10^9/L; a current serum creatinine of 1.2 mg/dL or more; a current mean arterial pressure below 70 mmHg. Other SOFA items are not part of this question.
CONDITION: mean arterial pressure below 70
CLAIMS: s = 'The mean arterial pressure criterion contributes 0 points.' | s' = 'The mean arterial pressure criterion contributes 1 point.'

BASE (answer s):
A 75-year-old woman.
Sepsis from a chest infection; admitted to the intensive care unit.
Mean arterial pressure 100 mmHg at a clinic visit in 2014.
Platelet count at this assessment: 227 x10^9/L.
Keeps houseplants.
Serum creatinine today: 0.7 mg/dL.
Uses a smartphone for reminders.
Nails normal.
Mean arterial pressure on the bedside monitor today: 85 mmHg.
Wears a seat belt when driving.

FLIP (answer s'): -Mean arterial pressure on the bedside monitor today: 85 mmHg. | +Mean arterial pressure on the bedside monitor today: 61 mmHg.

NEAR (answer s): -Mean arterial pressure 100 mmHg at a clinic visit in 2014. | +Mean arterial pressure 55 mmHg at a clinic visit in 2014.

MISSING (answer neither (undetermined)): -Mean arterial pressure 100 mmHg at a clinic visit in 2014. | -Mean arterial pressure on the bedside monitor today: 85 mmHg.

PRES (answer s): full text
Female, 75 years.
Sepsis from a chest infection; admitted to the intensive care unit.
Creatinine 0.7 mg/dL on this morning's labs.
In 2014, mean arterial pressure was 100 mmHg.
Uses a smartphone for reminders.
Wears a seat belt when driving.
Nails normal.
Complete blood count today: platelets 227 x10^9/L.
Mean arterial pressure today: 85 mmHg.
Keeps houseplants.


## 2.16 ('gs234', 'c1', 'boundary', 'long') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the age of the patient is above 60 years or the patient currently has tender anterior cervical lymph nodes, prescribe aspirin plus clopidogrel instead.
CONDITION: age above 60
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Woman, adult.
Recovering on the ward after a myocardial infarction treated with a stent.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2017.
Sleeps seven hours a night.
Teeth in good repair.
Lives in a second-floor apartment.
Drives a car.
Her sister has recovered from a dislocated finger.
Photographs local wildlife.
During a checkup in 2019, free T3 was 3.2 pg/mL.
During a checkup in 2008, total protein was 7.0 g/dL.
Has two cats.
Currently aged 37 years.
Her father lives with psoriasis.
Zinc of 85 mcg/dL in 2010.
Plays the piano.
Her uncle wears contact lenses.

FLIP (answer s'): -Currently aged 37 years. | +Currently aged 80 years.

NEAR (answer s): -Currently aged 37 years. | +Currently aged 60 years.

MISSING (answer neither (undetermined)): -Currently aged 37 years.

PRES (answer s): full text
An adult woman.
Recovering on the ward after a myocardial infarction treated with a stent.
Zinc of 85 mcg/dL in 2010.
Her father lives with psoriasis.
Drives a car.
Current age 37 years.
Her uncle wears contact lenses.
Uses sunscreen in summer.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Teeth in good repair.
During a checkup in 2008, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
Her sister has recovered from a dislocated finger.
Photographs local wildlife.
Sleeps seven hours a night.
Plays the piano.
Has two cats.
Free T4 of 1.2 ng/dL in 2017.


## 2.17 ('gs176', 'c2', 'negation', 'long') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. Score 2 points if the patient has ever had a stroke or TIA (current or past); 3 points if the patient is currently taking clarithromycin; 2 points if the patient is currently taking warfarin; 2 points if the patient is allergic to sulfonamide antibiotics. If the score is 6 or more, prescribe fondaparinux instead.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
67-year-old man.
First day after elective total hip replacement.
Uses public transport.
Has a sulfa allergy that causes skin blistering.
Total bilirubin 0.6 mg/dL in 2013.
Keeps houseplants.
Listens to podcasts.
Enjoys cooking.
Uses reading glasses for small print.
Vitamin B12 450 pg/mL in 2015.
Height 170 cm.
His brother had a splinter removed from a finger.
Lives on a quiet street.
Feeds birds in the backyard.
Nails normal.
Previously had a transient ischemic attack; the arm numbness resolved within an hour.
Wears a seat belt when driving.
Vitamin D 38 ng/mL in 2012 (wellness visit).
Drinks alcohol occasionally.
Not taking any antibiotics.
His cousin completed physical therapy for a shoulder injury.

FLIP (answer s'): -Not taking any antibiotics. | +Takes clarithromycin 500 mg twice daily.

NEAR (answer s): -Not taking any antibiotics. | +No clarithromycin on the medication list.

MISSING (answer neither (undetermined)): -Not taking any antibiotics. | +Clarithromycin: not asked about.

PRES (answer s): full text
A 67-year-old man.
First day after elective total hip replacement.
His brother had a splinter removed from a finger.
Listens to podcasts.
Allergic to sulfa antibiotics (hives).
Vitamin B12 450 pg/mL in 2015.
Uses public transport.
Drinks alcohol occasionally.
Vitamin D 38 ng/mL in 2012 (wellness visit).
Feeds birds in the backyard.
Total bilirubin 0.6 mg/dL in 2013.
Wears a seat belt when driving.
Enjoys cooking.
His cousin completed physical therapy for a shoulder injury.
Nails normal.
Antibiotics: none.
Previously had a transient ischemic attack; the arm numbness resolved within an hour.
Uses reading glasses for small print.
Height 170 cm.
Keeps houseplants.
Lives on a quiet street.


## 2.18 ('gs155', 'c3', 'numeric', 'long') templates=test

RULE: For early Lyme disease, prescribe doxycycline. If at least two of the following apply, prescribe amoxicillin instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the patient has ever had heart failure (current or past); the current oxygen saturation is below 90%.
CONDITION: oxygen saturation below 90
CLAIMS: s = 'Prescribe doxycycline.' | s' = 'Prescribe amoxicillin.'

BASE (answer s):
Man of 69 years.
Erythema migrans rash ten days after a tick bite.
Teeth in good repair.
Plays the piano.
Pupils equal and reactive to light.
Owns a bicycle.
Latest oxygen saturation reading: 96%.
Photographs local wildlife.
Has two cats.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Has coronary artery disease, managed medically.
Knits as a hobby.
Lives in a second-floor apartment.
His roommate burned a hand on a stove years ago.
His friend has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2011.
Enjoys board games.
In 2005, folate was 12 ng/mL.
Sleeps seven hours a night.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Sees a dentist yearly.

FLIP (answer s'): -Latest oxygen saturation reading: 96%. | +Latest oxygen saturation reading: 89%.

NEAR (answer s): -Latest oxygen saturation reading: 96%. | +Latest oxygen saturation reading: 91%.

MISSING (answer neither (undetermined)): -Latest oxygen saturation reading: 96%.

PRES (answer s): full text
Male patient of 69 years.
Erythema migrans rash ten days after a tick bite.
His roommate burned a hand on a stove years ago.
Sees a dentist yearly.
His friend has recovered from a dislocated finger.
Pupils equal and reactive to light.
Known coronary artery disease (two-vessel disease on angiography).
During a checkup in 2019, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Photographs local wildlife.
Has two cats.
Zinc of 85 mcg/dL in 2011.
Teeth in good repair.
Current oxygen saturation 96%.
Owns a bicycle.
Enjoys board games.
Plays the piano.
Uses sunscreen in summer.
Sleeps seven hours a night.
Lives in a second-floor apartment.
In 2005, folate was 12 ng/mL.
Knits as a hobby.


## 2.19 ('gs167', 'c1', 'subject', 'easy') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current platelet count is below 150 x10^9/L, prescribe fondaparinux instead.
CONDITION: vascular disease
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
55-year-old man.
First day after elective total hip replacement.
Complete blood count today: platelets 90 x10^9/L.
Has a pet dog.
Plays chess online.
Nails normal.
Watches football on weekends.
Peripheral pulses palpable.

FLIP (answer s'): -Peripheral pulses palpable. | +Myocardial infarction confirmed by troponin and ECG today.

NEAR (answer s): -Peripheral pulses palpable. | +His housemate had peripheral artery disease in 2024, resolved after leg artery surgery.

MISSING (answer neither (undetermined)): -Peripheral pulses palpable. | +Vascular disease: not recorded.

PRES (answer s): full text
Patient: male, 55 years.
First day after elective total hip replacement.
Watches football on weekends.
Nails normal.
Plays chess online.
Has a pet dog.
Foot pulses easily felt.
Platelets 90 x10^9/L on this morning's blood count.


## 2.20 ('gs162', 'c2', 'time', 'long') templates=test

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient is allergic to penicillin and the current serum potassium is above 4.5 mmol/L, prescribe azithromycin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Male patient of 56 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
His uncle burned a hand on a stove years ago.
His roommate has a lazy eye.
Teeth in good repair.
His wife lives with psoriasis.
Prefers morning appointments.
Drives a car.
Paints watercolors as a hobby.
Has two cats.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Back in 2011, serum potassium measured 4.0 mmol/L.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Latest potassium result: 3.8 mmol/L.
During a checkup in 2013, total protein was 7.0 g/dL.
Photographs local wildlife.
Sleeps seven hours a night.
Knits as a hobby.
Sees a dentist yearly.
Owns a bicycle.
Penicillin allergy: anaphylaxis.
Enjoys board games.

FLIP (answer s'): -Latest potassium result: 3.8 mmol/L. | +Latest potassium result: 5.2 mmol/L.

NEAR (answer s): -Back in 2011, serum potassium measured 4.0 mmol/L. | +Back in 2011, serum potassium measured 5.2 mmol/L.

MISSING (answer neither (undetermined)): -Back in 2011, serum potassium measured 4.0 mmol/L. | -Latest potassium result: 3.8 mmol/L.

PRES (answer s): full text
Man of 56 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
During a checkup in 2013, total protein was 7.0 g/dL.
Sees a dentist yearly.
Teeth in good repair.
His roommate has a lazy eye.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Owns a bicycle.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Photographs local wildlife.
Paints watercolors as a hobby.
Drives a car.
His wife lives with psoriasis.
Uses sunscreen in summer.
Current serum potassium 3.8 mmol/L.
Sleeps seven hours a night.
Has two cats.
Records from 2011 list serum potassium at 4.0 mmol/L.
Known penicillin allergy with angioedema.
Knits as a hobby.
His uncle burned a hand on a stove years ago.
Enjoys board games.
Prefers morning appointments.


## 2.21 ('gs186', 'c1', 'boundary', 'easy') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the current serum creatinine is above 2.0 mg/dL; 2 points if the patient currently has heart failure; 1 point if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe acetaminophen instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
A 70-year-old man.
Knee osteoarthritis with pain on walking.
Sings in a weekly choir.
Has a mechanical aortic valve.
Serum creatinine today: 1.2 mg/dL.
Breathless on mild exertion because of heart failure.
Drinks alcohol occasionally.

FLIP (answer s'): -Serum creatinine today: 1.2 mg/dL. | +Serum creatinine today: 3.8 mg/dL.

NEAR (answer s): -Serum creatinine today: 1.2 mg/dL. | +Serum creatinine today: 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Serum creatinine today: 1.2 mg/dL.

PRES (answer s): full text
Male, 70 years.
Knee osteoarthritis with pain on walking.
Sings in a weekly choir.
Blood panel at this assessment: creatinine 1.2 mg/dL.
Mechanical aortic valve, functioning normally on echocardiography today.
Heart failure, under regular review in a cardiology clinic.
Drinks alcohol occasionally.


## 2.22 ('gs025', 'c1', 'negation', 'long') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient currently has a major bleed; the current weight is below 67 kg; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Female patient of 84 years.
First day after elective total hip replacement.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Latest weight 65 kg.
Coagulation tests normal on recent bloodwork.
Plays the piano.
Drives a car.
Her sister burned a hand on a stove years ago.
Her roommate has a lazy eye.
Examination shows no signs of blood loss.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2019.
In 2007, folate was 12 ng/mL.
Has two cats.
Lives in a second-floor apartment.
Teeth in good repair.
Uses sunscreen in summer.
Her roommate has recovered from a dislocated finger.
Enjoys board games.
Owns a bicycle.
Prefers to be addressed by first name.

FLIP (answer s'): -Examination shows no signs of blood loss. | +Currently has a major bleed from a duodenal ulcer, with transfusion under way.

NEAR (answer s): -Examination shows no signs of blood loss. | +Medical records negative for major bleeding at any time.

MISSING (answer neither (undetermined)): -Examination shows no signs of blood loss. | +Active major bleeding: unknown.

PRES (answer s): full text
Woman of 84 years.
First day after elective total hip replacement.
Enjoys board games.
Pupils equal and reactive to light.
Has two cats.
Her roommate has a lazy eye.
Drives a car.
Varicose veins: none seen.
Her roommate has recovered from a dislocated finger.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Teeth in good repair.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Uses sunscreen in summer.
Zinc of 85 mcg/dL in 2019.
Sees a dentist yearly.
Plays the piano.
In 2007, folate was 12 ng/mL.
Bowel habit normal, without any blood in the stool.
Current weight 65 kg.
Owns a bicycle.


## 2.23 ('gs227', 'c1', 'numeric', 'long') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the current weight is 60 kg or less or the patient is currently taking aspirin, prescribe clindamycin instead.
CONDITION: weight at or below 60
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Patient: female, 81 years.
Spreading redness and warmth of the right shin for two days.
Grows tomatoes in the garden.
Speaks English and Spanish.
Ferritin 60 ng/mL in 2007.
Collects postcards.
Drinks plenty of water.
Watches football on weekends.
Height 170 cm.
Her brother-in-law broke a wrist, which has healed.
Uses reading glasses for small print.
Does crossword puzzles.
Vaccinations up to date.
Writes with the right hand.
Enjoys cooking.
Her brother-in-law completed physical therapy for a shoulder injury.
Drinks two cups of coffee a day.
Lives on a quiet street.
Nails normal.
Sodium 140 mmol/L in 2006.
Magnesium 2.0 mg/dL in 2007.
Weight 67 kg at this assessment.
Her husband wears hearing aids.

FLIP (answer s'): -Weight 67 kg at this assessment. | +Weight 55 kg at this assessment.

NEAR (answer s): -Weight 67 kg at this assessment. | +Weight 63 kg at this assessment.

MISSING (answer neither (undetermined)): -Weight 67 kg at this assessment.

PRES (answer s): full text
81-year-old woman.
Spreading redness and warmth of the right shin for two days.
Lives on a quiet street.
Enjoys cooking.
Grows tomatoes in the garden.
Collects postcards.
Sodium 140 mmol/L in 2006.
Ferritin 60 ng/mL in 2007.
Does crossword puzzles.
Watches football on weekends.
Speaks English and Spanish.
Nails normal.
Height 170 cm.
Vaccinations up to date.
Her brother-in-law completed physical therapy for a shoulder injury.
Writes with the right hand.
Magnesium 2.0 mg/dL in 2007.
Her husband wears hearing aids.
Uses reading glasses for small print.
Weight checked today on a calibrated scale: 67 kg.
Drinks plenty of water.
Her brother-in-law broke a wrist, which has healed.
Drinks two cups of coffee a day.


## 2.24 ('gs080', 'c3', 'subject', 'long') templates=test

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. Score 3 points if the patient is currently taking warfarin; 1 point if the patient currently has tender anterior cervical lymph nodes; 3 points if the patient has ever had a peptic ulcer (current or past). If the score is 7 or more, prescribe doxycycline instead.
CONDITION: peptic ulcer at any time
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Male patient of 38 years.
Productive cough and fever; consolidation on chest radiograph.
Anterior cervical lymph nodes enlarged and tender to touch.
Enjoys board games.
Sees a dentist yearly.
His friend sprained a thumb last month.
His father burned a hand on a stove years ago.
His father has recovered from a dislocated finger.
His father has a lazy eye.
In 2020, lipase was 30 U/L.
Prefers morning appointments.
Abdomen soft and non-tender.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Prefers to be addressed by first name.
During a checkup in 2022, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2023.
Photographs local wildlife.
Teeth in good repair.
Plays the piano.
Uses sunscreen in summer.
Paints watercolors as a hobby.

FLIP (answer s'): -Abdomen soft and non-tender. | +Duodenal ulcer years ago; recovered fully with treatment.

NEAR (answer s): -Abdomen soft and non-tender. | +His uncle recovered from a stomach ulcer years ago.

MISSING (answer neither (undetermined)): -Abdomen soft and non-tender. | +Peptic ulcer at any time: unknown.

PRES (answer s): full text
Man of 38 years.
Productive cough and fever; consolidation on chest radiograph.
Teeth in good repair.
Photographs local wildlife.
Tender, swollen lymph nodes in the front of the neck.
His friend sprained a thumb last month.
Plays the piano.
Uses sunscreen in summer.
His father has recovered from a dislocated finger.
Paints watercolors as a hobby.
His father has a lazy eye.
His father burned a hand on a stove years ago.
Appetite good; no indigestion.
Prefers to be addressed by first name.
Currently on warfarin, prescribed by the cardiology clinic.
Prefers morning appointments.
Sees a dentist yearly.
Sleeps seven hours a night.
Enjoys board games.
During a checkup in 2022, total protein was 7.0 g/dL.
Zinc of 85 mcg/dL in 2023.
In 2020, lipase was 30 U/L.


## 2.25 ('gs062', 'c1', 'time', 'superseded') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. Score 1 point if the current eGFR is below 30 mL/min/1.73 m2; 3 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 1 point if the patient is allergic to sulfonamide antibiotics; 3 points if the current platelet count is 350 x10^9/L or more. If the score is 7 or more, prescribe clindamycin instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Patient: female, 77 years.
Spreading redness and warmth of the right shin for two days.
Complete blood count today: platelets 498 x10^9/L.
Height 170 cm.
Myocardial infarction in 2019, treated with a stent.
EGFR of 98 mL/min/1.73 m2 measured yesterday was replaced by a repeat measurement.
This morning's blood test shows an eGFR of 63 mL/min/1.73 m2.
Drinks alcohol occasionally.
Plays chess online.
Keeps a step counter.

FLIP (answer s'): -This morning's blood test shows an eGFR of 63 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 28 mL/min/1.73 m2.

NEAR (answer s): -EGFR of 98 mL/min/1.73 m2 measured yesterday was replaced by a repeat measurement. | +EGFR of 25 mL/min/1.73 m2 measured yesterday was replaced by a repeat measurement.

MISSING (answer neither (undetermined)): -EGFR of 98 mL/min/1.73 m2 measured yesterday was replaced by a repeat measurement. | -This morning's blood test shows an eGFR of 63 mL/min/1.73 m2.

PRES (answer s): full text
Female, 77 years.
Spreading redness and warmth of the right shin for two days.
eGFR 63 mL/min/1.73 m2 on today's labs.
Keeps a step counter.
Platelet count at this assessment: 498 x10^9/L.
Myocardial infarction in 2019; completed cardiac rehabilitation and has had no symptoms since.
Drinks alcohol occasionally.
Plays chess online.
Height 170 cm.
Yesterday, eGFR was 98 mL/min/1.73 m2; today's value replaces it.


## 2.26 ('gs186', 'c1', 'boundary', 'long') templates=test

RULE: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the current serum creatinine is above 2.0 mg/dL; 2 points if the patient currently has heart failure; 1 point if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe acetaminophen instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Woman of 62 years.
Knee osteoarthritis with pain on walking.
Lives with a mechanical aortic valve prosthesis.
Current heart failure with ankle swelling.
Uses sunscreen in summer.
Sees a dentist yearly.
Prefers to be addressed by first name.
Sleeps seven hours a night.
In 2009, lipase was 30 U/L.
Lives in a second-floor apartment.
Enjoys board games.
Her friend sprained a thumb last month.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Latest creatinine result: 0.9 mg/dL.
Teeth in good repair.
Her father burned a hand on a stove years ago.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
Paints watercolors as a hobby.
During a checkup in 2006, total protein was 7.0 g/dL.

FLIP (answer s'): -Latest creatinine result: 0.9 mg/dL. | +Latest creatinine result: 2.6 mg/dL.

NEAR (answer s): -Latest creatinine result: 0.9 mg/dL. | +Latest creatinine result: 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Latest creatinine result: 0.9 mg/dL.

PRES (answer s): full text
Female patient of 62 years.
Knee osteoarthritis with pain on walking.
Prefers to be addressed by first name.
Current serum creatinine 0.9 mg/dL.
In 2009, lipase was 30 U/L.
Paints watercolors as a hobby.
Sleeps seven hours a night.
During a checkup in 2006, total protein was 7.0 g/dL.
Mechanical mitral valve in place; metallic closing clicks audible.
Teeth in good repair.
Uses sunscreen in summer.
Enjoys board games.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Her friend sprained a thumb last month.
Owns a bicycle.
Her father burned a hand on a stove years ago.
Lives in a second-floor apartment.
Sees a dentist yearly.
Photographs local wildlife.
Has heart failure, treated with diuretics.


## 2.27 ('gs215', 'c1', 'negation', 'easy') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If at least two of the following apply, prescribe naproxen with omeprazole instead: the patient has ever had heparin-induced thrombocytopenia (current or past); the current platelet count is below 150 x10^9/L; the patient is currently taking clarithromycin.
CONDITION: heparin-induced thrombocytopenia
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Female, 46 years.
Hip osteoarthritis with pain on walking.
Not taking any antibiotics.
Sings in a weekly choir.
Grows tomatoes in the garden.
Not on any blood thinner at present.
Complete blood count today: platelets 100 x10^9/L.
Drinks alcohol occasionally.
Bakes bread at home.

FLIP (answer s'): -Not on any blood thinner at present. | +Has heparin-induced thrombocytopenia, confirmed by antibody testing.

NEAR (answer s): -Not on any blood thinner at present. | +Denies ever having heparin-induced thrombocytopenia.

MISSING (answer neither (undetermined)): -Not on any blood thinner at present. | +Heparin-induced thrombocytopenia: not documented in the records available.

PRES (answer s): full text
A 46-year-old woman.
Hip osteoarthritis with pain on walking.
Platelets 100 x10^9/L on this morning's blood count.
Drinks alcohol occasionally.
Bakes bread at home.
Grows tomatoes in the garden.
No heparin given so far during this admission.
Sings in a weekly choir.
No macrolide antibiotics on the medication list.


## 2.28 ('gs192', 'c2', 'numeric', 'long') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has an active peptic ulcer and the current respiratory rate is 50/min or more, prescribe naproxen with omeprazole instead.
CONDITION: respiratory rate at least 50
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Woman of 72 years.
Hip osteoarthritis with pain on walking.
Prefers to be addressed by first name.
Teeth in good repair.
Enjoys board games.
During a checkup in 2015, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Her wife has recovered from a dislocated finger.
Has an active duodenal ulcer.
Pupils equal and reactive to light.
In 2006, folate was 12 ng/mL.
Her wife wears contact lenses.
Observations now: respiratory rate 36/min.
Sleeps seven hours a night.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2010.
Owns a bicycle.
Knits as a hobby.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2010.
Plays the piano.

FLIP (answer s'): -Observations now: respiratory rate 36/min. | +Observations now: respiratory rate 56/min.

NEAR (answer s): -Observations now: respiratory rate 36/min. | +Observations now: respiratory rate 47/min.

MISSING (answer neither (undetermined)): -Observations now: respiratory rate 36/min.

PRES (answer s): full text
Female patient of 72 years.
Hip osteoarthritis with pain on walking.
Owns a bicycle.
Active peptic ulcer disease.
Current respiratory rate 36/min.
Prefers morning appointments.
Sees a dentist yearly.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Plays the piano.
In 2006, folate was 12 ng/mL.
Sleeps seven hours a night.
Teeth in good repair.
Uses sunscreen in summer.
Zinc of 85 mcg/dL in 2010.
Her wife has recovered from a dislocated finger.
Her wife wears contact lenses.
Free T4 of 1.2 ng/dL in 2010.
During a checkup in 2015, total protein was 7.0 g/dL.
Enjoys board games.
Knits as a hobby.


## 2.29 ('gs176', 'c1', 'subject', 'long') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. Score 2 points if the patient has ever had a stroke or TIA (current or past); 3 points if the patient is currently taking clarithromycin; 2 points if the patient is currently taking warfarin; 2 points if the patient is allergic to sulfonamide antibiotics. If the score is 6 or more, prescribe fondaparinux instead.
CONDITION: stroke/TIA
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Patient: female, 76 years.
First day after elective total hip replacement.
Keeps houseplants.
Writes with the right hand.
Takes warfarin for atrial fibrillation.
Her neighbor had a splinter removed from a finger.
Lives on a quiet street.
Allergies: sulfa drugs (rash).
Eats a varied diet.
Bakes bread at home.
Speaks English and Spanish.
Her coworker wears hearing aids.
Ferritin 60 ng/mL in 2013.
Does crossword puzzles.
Volunteers at a library.
Vitamin B12 450 pg/mL in 2013.
Her husband has a chipped front tooth.
Her partner previously wore dental braces.
Enjoys gardening.

FLIP (answer s'): +Ongoing symptoms from a stroke this week.

NEAR (answer s): +Her cousin has a new stroke that affects speech.

MISSING (answer neither (undetermined)): +Information on stroke/TIA was not obtained.

PRES (answer s): full text
Female, 76 years.
First day after elective total hip replacement.
Her partner previously wore dental braces.
Lives on a quiet street.
Her husband has a chipped front tooth.
Keeps houseplants.
Bakes bread at home.
Allergic to sulfa antibiotics (hives).
Her neighbor had a splinter removed from a finger.
Her coworker wears hearing aids.
Speaks English and Spanish.
Takes warfarin daily, with the dose adjusted to the INR.
Vitamin B12 450 pg/mL in 2013.
Eats a varied diet.
Enjoys gardening.
Volunteers at a library.
Ferritin 60 ng/mL in 2013.
Writes with the right hand.
Does crossword puzzles.


## 2.30 ('gs167', 'c2', 'time', 'superseded') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current platelet count is below 150 x10^9/L, prescribe fondaparinux instead.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Woman of 70 years.
First day after elective total hip replacement.
Current platelet count 311 x10^9/L.
Heart attack years ago, with full recovery.
Last month, platelet count was 378 x10^9/L; the newest measurement replaces it.
Sleeps seven hours a night.

FLIP (answer s'): -Current platelet count 311 x10^9/L. | +Current platelet count 93 x10^9/L.

NEAR (answer s): -Last month, platelet count was 378 x10^9/L; the newest measurement replaces it. | +Last month, platelet count was 81 x10^9/L; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Current platelet count 311 x10^9/L. | -Last month, platelet count was 378 x10^9/L; the newest measurement replaces it.

PRES (answer s): full text
Female patient of 70 years.
First day after elective total hip replacement.
Earlier this week, platelet count was 378 x10^9/L; a newer reading supersedes it.
Sleeps seven hours a night.
Platelet count now 311 x10^9/L.
Recovered from a heart attack in None.


## 2.31 ('gs071', 'c1', 'boundary', 'easy') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the current weight is below 67 kg or the patient has ever had angioedema (current or past), prescribe intermittent pneumatic compression instead.
CONDITION: weight below 67
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Patient: male, 55 years.
Admitted for community-acquired pneumonia; immobile.
Speaks and swallows normally, with no hoarseness.
Weight 72 kg at this assessment.
Has a pet dog.
Keeps houseplants.
Collects postcards.

FLIP (answer s'): -Weight 72 kg at this assessment. | +Weight 66 kg at this assessment.

NEAR (answer s): -Weight 72 kg at this assessment. | +Weight 67 kg at this assessment.

MISSING (answer neither (undetermined)): -Weight 72 kg at this assessment.

PRES (answer s): full text
A 55-year-old man.
Admitted for community-acquired pneumonia; immobile.
Has a pet dog.
Lips and tongue normal in size at this assessment.
Weight today: 72 kg.
Collects postcards.
Keeps houseplants.


## 2.32 ('gs090', 'c2', 'negation', 'long') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current heart rate is 125/min or more or the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe warfarin instead.
CONDITION: venous thromboembolism in the family
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Man of 85 years.
Atrial fibrillation; anticoagulation indicated.
Zinc of 85 mcg/dL in 2021.
Prefers to be addressed by first name.
His friend sprained a thumb last month.
Plays the piano.
Heart rate now 82/min on the monitor.
His friend lives with psoriasis.
Uses sunscreen in summer.
Teeth in good repair.
His friend burned a hand on a stove years ago.
His friend wears contact lenses.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Photographs local wildlife.
In 2019, lipase was 30 U/L.
Coagulation tests normal on recent bloodwork.
Pupils equal and reactive to light.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2012.
Knits as a hobby.
Paints watercolors as a hobby.

FLIP (answer s'): -Coagulation tests normal on recent bloodwork. | +His sister is being treated for a pulmonary embolism.

NEAR (answer s): -Coagulation tests normal on recent bloodwork. | +Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.

MISSING (answer neither (undetermined)): -Coagulation tests normal on recent bloodwork. | +Venous thromboembolism in the family: unknown.

PRES (answer s): full text
Male patient of 85 years.
Atrial fibrillation; anticoagulation indicated.
His friend wears contact lenses.
Paints watercolors as a hobby.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2012.
Pupils equal and reactive to light.
His friend lives with psoriasis.
His friend burned a hand on a stove years ago.
Teeth in good repair.
Prefers to be addressed by first name.
During a checkup in 2023, free T3 was 3.2 pg/mL.
His friend sprained a thumb last month.
Zinc of 85 mcg/dL in 2021.
Sleeps seven hours a night.
In 2019, lipase was 30 U/L.
Plays the piano.
Prefers morning appointments.
Uses sunscreen in summer.
Photographs local wildlife.
Varicose veins: none seen.
Knits as a hobby.
Current heart rate 82/min.


## 2.33 ('s4_apache', 'temp', 'numeric', 'long') templates=train

RULE: APACHE II (as used here, partial: only the stated band of each item): 4 points for a current temperature of 41.0 C or more; 4 points for a current heart rate of 180/min or more; 4 points for a current respiratory rate of 50/min or more; 6 points for age 75 years or more. Any other value of these items scores 0 here, and the other APACHE II items are not part of this question.
CONDITION: temperature at least 41.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 4 points.'

BASE (answer s):
Patient: male.
Admitted to the intensive care unit for monitoring.
Oral temperature this morning: 37.0 C.
His partner has a stutter.
Keeps houseplants.
Age on arrival: 61 years.
Watches football on weekends.
Drinks two cups of coffee a day.
Respiratory rate, counted over a full minute today, is 13/min.
His mother has a fear of heights.
His aunt previously wore dental braces.
Speaks English and Spanish.
Has a pet dog.
His husband broke a wrist, which has healed.
Sodium 140 mmol/L in 2011.
Eats a varied diet.
Vitamin D 38 ng/mL in 2008 (wellness visit).
Uses reading glasses for small print.
Plays chess online.
Height 170 cm.
Grows tomatoes in the garden.
Heart rate today: 106/min.

FLIP (answer s'): -Oral temperature this morning: 37.0 C. | +Oral temperature this morning: 41.2 C.

NEAR (answer s): -Oral temperature this morning: 37.0 C. | +Oral temperature this morning: 40.9 C.

MISSING (answer neither (undetermined)): -Oral temperature this morning: 37.0 C.

PRES (answer s): full text
Sex: male.
Admitted to the intensive care unit for monitoring.
Temperature checked with a digital thermometer today: 37.0 C.
His husband broke a wrist, which has healed.
Plays chess online.
Keeps houseplants.
Drinks two cups of coffee a day.
His mother has a fear of heights.
Has a pet dog.
Age 61 years, calculated today from the date of birth.
Vitamin D 38 ng/mL in 2008 (wellness visit).
His aunt previously wore dental braces.
Eats a varied diet.
Heart rate counted over a full minute at this assessment: 106/min.
Uses reading glasses for small print.
Speaks English and Spanish.
Respiratory rate 13/min at this assessment.
His partner has a stutter.
Sodium 140 mmol/L in 2011.
Height 170 cm.
Grows tomatoes in the garden.
Watches football on weekends.


## 2.34 ('gs039', 'c1', 'subject', 'long') templates=test

RULE: For vaginal candidiasis, prescribe oral fluconazole. If the patient has active cancer or the patient currently has heart failure, prescribe clotrimazole pessaries instead.
CONDITION: active cancer
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
In 2016, folate was 12 ng/mL.
Her roommate lives with psoriasis.
Knits as a hobby.
Zinc of 85 mcg/dL in 2013.
In 2022, lipase was 30 U/L.
Malignant disease: none at present.
Pupils equal and reactive to light.
Plays the piano.
Enjoys board games.
Her wife wears contact lenses.
Teeth in good repair.
Drives a car.
Has two cats.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2013.
Sees a dentist yearly.

FLIP (answer s'): -Malignant disease: none at present. | +Has melanoma skin cancer and is receiving treatment for it.

NEAR (answer s): -Malignant disease: none at present. | +Her wife is being treated for leukemia.

MISSING (answer neither (undetermined)): -Malignant disease: none at present. | +Active cancer: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
In 2016, folate was 12 ng/mL.
Plays the piano.
Her wife wears contact lenses.
Pupils equal and reactive to light.
Photographs local wildlife.
In 2022, lipase was 30 U/L.
Her roommate lives with psoriasis.
Weight steady over the past year.
Knits as a hobby.
Has two cats.
Zinc of 85 mcg/dL in 2013.
Drives a car.
Sees a dentist yearly.
Teeth in good repair.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2013.


## 2.35 ('gs039', 'c2', 'time', 'easy') templates=train

RULE: For vaginal candidiasis, prescribe oral fluconazole. If the patient has active cancer or the patient currently has heart failure, prescribe clotrimazole pessaries instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
31-year-old woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Keeps houseplants.
No active malignancy.
Takes no diuretics.
Enjoys cooking.

FLIP (answer s'): -Takes no diuretics. | +Heart failure with reduced ejection fraction.

NEAR (answer s): -Takes no diuretics. | +Previously had heart failure from a thyroid problem in 2014, resolved with treatment.

MISSING (answer neither (undetermined)): -Takes no diuretics. | +Current heart failure: not recorded.

PRES (answer s): full text
Patient: female, 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
No evidence of active neoplasia.
Enjoys cooking.
Recent echocardiogram normal.
Keeps houseplants.


## 2.36 ('vte_platelets', 'plt', 'boundary', 'long') templates=test

RULE: For inpatient VTE prophylaxis, give enoxaparin. If the current platelet count is below 50 x10^9/L, use intermittent pneumatic compression instead.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Male patient of 48 years.
Admitted for community-acquired pneumonia; immobile.
Prefers to be addressed by first name.
His friend burned a hand on a stove years ago.
Paints watercolors as a hobby.
Plays the piano.
During a checkup in 2009, total protein was 7.0 g/dL.
Owns a bicycle.
His wife has a lazy eye.
Knits as a hobby.
Sleeps seven hours a night.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2021.
Sees a dentist yearly.
Photographs local wildlife.
Current platelet count 269 x10^9/L.
Lives in a second-floor apartment.
Uses sunscreen in summer.
His wife sprained a thumb last month.

FLIP (answer s'): -Current platelet count 269 x10^9/L. | +Current platelet count 40 x10^9/L.

NEAR (answer s): -Current platelet count 269 x10^9/L. | +Current platelet count 50 x10^9/L.

MISSING (answer neither (undetermined)): -Current platelet count 269 x10^9/L.

PRES (answer s): full text
Man of 48 years.
Admitted for community-acquired pneumonia; immobile.
His friend burned a hand on a stove years ago.
Uses sunscreen in summer.
Lives in a second-floor apartment.
His wife has a lazy eye.
During a checkup in 2009, total protein was 7.0 g/dL.
Sees a dentist yearly.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Owns a bicycle.
Platelet count now 269 x10^9/L.
Plays the piano.
His wife sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2021.
Sleeps seven hours a night.
Knits as a hobby.
Enjoys board games.
Photographs local wildlife.


## 2.37 ('crc_screen', 'crc', 'negation', 'long') templates=train

RULE: For colorectal cancer screening, order a fecal immunochemical test. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time, order a colonoscopy instead.
CONDITION: colorectal cancer
CLAIMS: s = 'Order a fecal immunochemical test.' | s' = 'Order a colonoscopy.'

BASE (answer s):
46-year-old man.
Primary care visit; asks about screening tests.
Lives on a quiet street.
Weight stable and appetite good.
His brother-in-law has a fear of heights.
Bakes bread at home.
Reads most evenings.
Drinks plenty of water.
His aunt has a stutter.
His coworker has a chipped front tooth.
Chloride 103 mmol/L in 2005.
Bicarbonate 26 mmol/L in 2023 (annual physical).
Sings in a weekly choir.
TSH 1.6 mIU/L in 2021.
Wears a seat belt when driving.
Uses public transport.
Albumin 4.1 g/dL in 2013 (routine blood test).
His mother previously wore dental braces.
Collects postcards.

FLIP (answer s'): -Weight stable and appetite good. | +Bowel cancer in 2023; all treatment completed and the patient was declared cancer-free.

NEAR (answer s): -Weight stable and appetite good. | +Denies ever having colon cancer.

MISSING (answer neither (undetermined)): -Weight stable and appetite good. | +Colorectal cancer: not asked about.

PRES (answer s): full text
A 46-year-old man.
Primary care visit; asks about screening tests.
TSH 1.6 mIU/L in 2021.
Albumin 4.1 g/dL in 2013 (routine blood test).
Chloride 103 mmol/L in 2005.
His coworker has a chipped front tooth.
Sings in a weekly choir.
Abdomen soft, with no masses on examination.
Collects postcards.
His brother-in-law has a fear of heights.
Bicarbonate 26 mmol/L in 2023 (annual physical).
His mother previously wore dental braces.
His aunt has a stutter.
Wears a seat belt when driving.
Uses public transport.
Lives on a quiet street.
Drinks plenty of water.
Reads most evenings.
Bakes bread at home.


## 2.38 ('s1_bap65', 'hr', 'numeric', 'long') templates=test

RULE: BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of 25 mg/dL or more; current altered mental status (confusion or disorientation); a current heart rate of 109/min or more. Age is scored separately and is not part of this question.
CONDITION: heart rate at least 109
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 1 point.'

BASE (answer s):
Male patient of 49 years.
Acute exacerbation of COPD; assessed in the emergency department.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Prefers morning appointments.
Enjoys board games.
Plays the piano.
Knits as a hobby.
Teeth in good repair.
Has two cats.
Drives a car.
Current heart rate 63/min.
Owns a bicycle.
Blood urea nitrogen 16 mg/dL on the current labs.
His wife wears contact lenses.
Speech clear; follows commands.
In 2018, folate was 12 ng/mL.
His wife burned a hand on a stove years ago.
His roommate lives with psoriasis.
His sister has recovered from a dislocated finger.
Lives in a second-floor apartment.

FLIP (answer s'): -Current heart rate 63/min. | +Current heart rate 109/min.

NEAR (answer s): -Current heart rate 63/min. | +Current heart rate 107/min.

MISSING (answer neither (undetermined)): -Current heart rate 63/min.

PRES (answer s): full text
Man of 49 years.
Acute exacerbation of COPD; assessed in the emergency department.
His wife wears contact lenses.
Drives a car.
His roommate lives with psoriasis.
Plays the piano.
His sister has recovered from a dislocated finger.
Heart rate now 63/min on the monitor.
During a checkup in 2022, free T3 was 3.2 pg/mL.
In 2018, folate was 12 ng/mL.
Blood urea nitrogen now: 16 mg/dL.
Teeth in good repair.
Sleeps seven hours a night.
Enjoys board games.
Knits as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Has two cats.
Prefers morning appointments.
Gives a clear account of the illness.
His wife burned a hand on a stove years ago.


## 2.39 ('gs158', 'c1', 'subject', 'long') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time or the current white cell count is above 15.0 x10^9/L, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: coronary artery disease in the family
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Female, 41 years.
Suspected chest infection; assessed on the medical ward.
Uses reading glasses for small print.
Does crossword puzzles.
Wears a seat belt when driving.
No exertional chest discomfort.
Albumin 4.1 g/dL in 2005 (routine blood test).
Plays chess online.
Hearing normal to conversation.
Non-smoker.
Watches football on weekends.
Her husband completed physical therapy for a shoulder injury.
Collects postcards.
Keeps houseplants.
Sings in a weekly choir.
Her aunt is left-handed.
TSH 1.6 mIU/L in 2013.
Ferritin 60 ng/mL in 2012.
Vaccinations up to date.
Enjoys gardening.
WBC 9.1 x10^9/L on today's sample.

FLIP (answer s'): -No exertional chest discomfort. | +Previously treated for coronary artery disease (stent, 2009).

NEAR (answer s): -No exertional chest discomfort. | +Her aunt had coronary artery disease found on a stress test in 2012.

MISSING (answer neither (undetermined)): -No exertional chest discomfort. | +Coronary artery disease in the family: not documented in the records available.

PRES (answer s): full text
41-year-old woman.
Suspected chest infection; assessed on the medical ward.
Uses reading glasses for small print.
Her husband completed physical therapy for a shoulder injury.
Plays chess online.
Her aunt is left-handed.
TSH 1.6 mIU/L in 2013.
Does crossword puzzles.
Ferritin 60 ng/mL in 2012.
Vaccinations up to date.
Watches football on weekends.
Exercises regularly without chest pain.
Keeps houseplants.
Non-smoker.
Albumin 4.1 g/dL in 2005 (routine blood test).
Collects postcards.
Enjoys gardening.
Sings in a weekly choir.
Complete blood count this morning: white cell count 9.1 x10^9/L.
Hearing normal to conversation.
Wears a seat belt when driving.


## 2.40 ('gs236', 'c1', 'time', 'easy') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the patient is currently taking warfarin or the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe clindamycin instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Man of 39 years.
Spreading redness and warmth of the right shin for two days.
Sleeps seven hours a night.

FLIP (answer s'): +Currently on warfarin, prescribed by the cardiology clinic.

NEAR (answer s): +Came off warfarin years ago after a heart rhythm problem settled.

MISSING (answer neither (undetermined)): +Warfarin: unknown.

PRES (answer s): full text
Male patient of 39 years.
Spreading redness and warmth of the right shin for two days.
Sleeps seven hours a night.


## 2.41 ('gs133', 'c2', 'boundary', 'long') templates=train

RULE: For primary prevention, prescribe atorvastatin. If the patient is currently taking clarithromycin and the age of the patient is above 55 years, prescribe ezetimibe instead.
CONDITION: age above 55
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Collects postcards.
Vaccinations up to date.
Reads most evenings.
Her aunt has a fear of heights.
Takes clarithromycin as part of Helicobacter pylori treatment.
Keeps a step counter.
Sings in a weekly choir.
Writes with the right hand.
Plays chess online.
Eats a varied diet.
Age at this assessment: 30 years.
Her grandfather has a stutter.
Uses a smartphone for reminders.
Does crossword puzzles.
Vitamin B12 450 pg/mL in 2018.
Bicarbonate 26 mmol/L in 2016 (annual physical).
Wears a seat belt when driving.
Vitamin D 38 ng/mL in 2021 (wellness visit).
Feeds birds in the backyard.
Her neighbor is being treated for eczema.

FLIP (answer s'): -Age at this assessment: 30 years. | +Age at this assessment: 87 years.

NEAR (answer s): -Age at this assessment: 30 years. | +Age at this assessment: 55 years.

MISSING (answer neither (undetermined)): -Age at this assessment: 30 years.

PRES (answer s): full text
Patient: female.
Primary prevention; LDL cholesterol 182 mg/dL.
Plays chess online.
Collects postcards.
Vitamin B12 450 pg/mL in 2018.
Reads most evenings.
Vitamin D 38 ng/mL in 2021 (wellness visit).
Wears a seat belt when driving.
Bicarbonate 26 mmol/L in 2016 (annual physical).
Keeps a step counter.
Her aunt has a fear of heights.
Her neighbor is being treated for eczema.
Age on arrival: 30 years.
Feeds birds in the backyard.
Eats a varied diet.
Vaccinations up to date.
Writes with the right hand.
Uses a smartphone for reminders.
Started clarithromycin this morning for sinusitis.
Does crossword puzzles.
Her grandfather has a stutter.
Sings in a weekly choir.


## 2.42 ('gs216', 'c2', 'negation', 'easy') templates=test

RULE: For acute migraine, prescribe sumatriptan. If the current blood urea nitrogen is 21 mg/dL or more or the patient currently has a mechanical heart valve, prescribe naproxen instead.
CONDITION: mechanical heart valve
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Male patient of 60 years.
Acute migraine without aura, typical of prior attacks.
Enjoys board games.
Irregularly irregular pulse; heart sounds free of clicks.
Pupils equal and reactive to light.
Blood urea nitrogen 8 mg/dL on the current labs.

FLIP (answer s'): -Irregularly irregular pulse; heart sounds free of clicks. | +Mechanical mitral valve in place; metallic closing clicks audible.

NEAR (answer s): -Irregularly irregular pulse; heart sounds free of clicks. | +Has never had a mechanical heart valve.

MISSING (answer neither (undetermined)): -Irregularly irregular pulse; heart sounds free of clicks. | +Mechanical heart valve: unknown.

PRES (answer s): full text
Man of 60 years.
Acute migraine without aura, typical of prior attacks.
Blood urea nitrogen now: 8 mg/dL.
Enjoys board games.
Heart sounds irregular, without a metallic click.
Pupils equal and reactive to light.


## 2.43 ('gs205', 'c2', 'numeric', 'long') templates=train

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient has had a major bleeding event at any time and the current temperature is below 36.0 C, prescribe nitrofurantoin instead.
CONDITION: temperature below 36.0
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
Patient: female, 18 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Major postoperative bleed from a knee wound in 2024, resolved with a repeat procedure.
Sings in a weekly choir.
Enjoys cooking.
Speaks English and Spanish.
Collects postcards.
Drinks alcohol occasionally.
Non-smoker.
TSH 1.6 mIU/L in 2024.
Temperature today: 38.9 C.
Lives on a quiet street.
Wears a seat belt when driving.
Uses reading glasses for small print.
Phosphate 3.6 mg/dL in 2024.
Eats a varied diet.
Drinks two cups of coffee a day.
Her cousin broke a wrist, which has healed.
Height 170 cm.
Has a pet dog.
Vaccinations up to date.
Her neighbor has a chipped front tooth.

FLIP (answer s'): -Temperature today: 38.9 C. | +Temperature today: 34.1 C.

NEAR (answer s): -Temperature today: 38.9 C. | +Temperature today: 36.2 C.

MISSING (answer neither (undetermined)): -Temperature today: 38.9 C.

PRES (answer s): full text
A 18-year-old woman.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Enjoys cooking.
Height 170 cm.
Phosphate 3.6 mg/dL in 2024.
TSH 1.6 mIU/L in 2024.
Temperature 38.9 C at this assessment.
Collects postcards.
Speaks English and Spanish.
Her cousin broke a wrist, which has healed.
Vaccinations up to date.
Lives on a quiet street.
Has a pet dog.
Non-smoker.
Wears a seat belt when driving.
Sings in a weekly choir.
Drinks alcohol occasionally.
Previously transfused for a major bleed from a stomach ulcer, which healed in 2024.
Her neighbor has a chipped front tooth.
Eats a varied diet.
Uses reading glasses for small print.
Drinks two cups of coffee a day.


## 2.44 ('gs106', 'c1', 'subject', 'long') templates=test

RULE: For vaginal candidiasis, prescribe oral fluconazole. Score 2 points if the patient has ever had a venous thromboembolism (current or past); 2 points if the current blood urea nitrogen is 20 mg/dL or more; 1 point if the patient currently has tonsillar exudate; 1 point if the patient is currently taking clarithromycin. If the score is 3 or more, prescribe clotrimazole pessaries instead.
CONDITION: venous thromboembolism
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Drives a car.
Her uncle burned a hand on a stove years ago.
Has two cats.
Teeth in good repair.
In 2014, folate was 12 ng/mL.
Sees a dentist yearly.
Blood urea nitrogen 8 mg/dL on the current labs.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Tonsils pink and clean on inspection.
Zinc of 85 mcg/dL in 2015.
Prefers morning appointments.
Her father has a lazy eye.
Enjoys board games.
Owns a bicycle.
Her father wears contact lenses.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Sleeps seven hours a night.
Photographs local wildlife.
Currently taking clarithromycin for an ear infection.
Paints watercolors as a hobby.

FLIP (answer s'): +Ongoing treatment for venous thrombosis of the left arm.

NEAR (answer s): +Her sister is being treated for a pulmonary embolism.

MISSING (answer neither (undetermined)): +Venous thromboembolism: status unclear from the records at hand.

PRES (answer s): full text
Woman of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
On clarithromycin for a chest infection, day 3 of 7.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Teeth in good repair.
Enjoys board games.
Sees a dentist yearly.
Blood urea nitrogen now: 8 mg/dL.
Owns a bicycle.
Zinc of 85 mcg/dL in 2015.
Prefers morning appointments.
In 2014, folate was 12 ng/mL.
Photographs local wildlife.
Lives in a second-floor apartment.
Drives a car.
Has two cats.
Paints watercolors as a hobby.
Her uncle burned a hand on a stove years ago.
Knits as a hobby.
Her father wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Tonsils slightly red but clean, without pus.
Her father has a lazy eye.


## 2.45 ('gs094', 'c3', 'time', 'long') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 1 point if the age of the patient is 65 years or more; 3 points if the current serum potassium is above 4.5 mmol/L; 1 point if the patient is allergic to penicillin. If the score is 7 or more, prescribe clindamycin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Adult man.
Spreading redness and warmth of the right shin for two days.
Serum calcium 9.4 mg/dL in 2011.
His cousin previously wore dental braces.
Vitamin D 38 ng/mL in 2021 (wellness visit).
Keeps a step counter.
Diabetic; tests blood sugar at home twice a day.
Serum potassium 4.2 mmol/L at a clinic visit in 2019.
Feeds birds in the backyard.
Reports an allergy to penicillin that causes hives.
Sings in a weekly choir.
Volunteers at a library.
Height 170 cm.
His coworker had a splinter removed from a finger.
Potassium measured at this assessment is 3.6 mmol/L.
His brother has a broken finger in a splint.
Enjoys cooking.
Has a pet dog.
Hearing normal to conversation.
Keeps houseplants.
Uses a smartphone for reminders.
Age at this assessment: 78 years.
Does crossword puzzles.
Lives on a quiet street.
Bakes bread at home.
Drinks two cups of coffee a day.

FLIP (answer s'): -Potassium measured at this assessment is 3.6 mmol/L. | +Potassium measured at this assessment is 4.9 mmol/L.

NEAR (answer s): -Serum potassium 4.2 mmol/L at a clinic visit in 2019. | +Serum potassium 4.9 mmol/L at a clinic visit in 2019.

MISSING (answer neither (undetermined)): -Serum potassium 4.2 mmol/L at a clinic visit in 2019. | -Potassium measured at this assessment is 3.6 mmol/L.

PRES (answer s): full text
Patient: male.
Spreading redness and warmth of the right shin for two days.
Vitamin D 38 ng/mL in 2021 (wellness visit).
Bakes bread at home.
Keeps houseplants.
Keeps a step counter.
Labs this morning: potassium 3.6 mmol/L.
Diabetes mellitus type 1.
Allergies: penicillin (rash).
Enjoys cooking.
Serum potassium of 4.2 mmol/L recorded in 2019.
Uses a smartphone for reminders.
Volunteers at a library.
Serum calcium 9.4 mg/dL in 2011.
Drinks two cups of coffee a day.
Does crossword puzzles.
Has a pet dog.
His cousin previously wore dental braces.
Age today: 78 years.
Feeds birds in the backyard.
Height 170 cm.
His coworker had a splinter removed from a finger.
Sings in a weekly choir.
Hearing normal to conversation.
Lives on a quiet street.
His brother has a broken finger in a splint.


## 2.46 ('s2_khorana', 'hgb', 'boundary', 'alt') templates=test

RULE: Khorana score (as used here, partial): 1 point each for a current platelet count of 350 x10^9/L or more; a current hemoglobin below 11.0 g/dL; a current white cell count above 11.0 x10^9/L; a current body mass index of 35.0 kg/m2 or more. Other Khorana items, including the cancer site, are not part of this question.
CONDITION: hemoglobin below 11.0
CLAIMS: s = 'The hemoglobin criterion contributes 0 points.' | s' = 'The hemoglobin criterion contributes 1 point.'

BASE (answer s):
Man of 68 years.
Newly diagnosed colon cancer; first chemotherapy cycle planned for next week.
Current body mass index 27.4 kg/m2.
Sleeps seven hours a night.
Current platelet count 233 x10^9/L.
Current white cell count 8.6 x10^9/L.
Photographs local wildlife.
Lives in a second-floor apartment.
Current Hgb 14.4 g/dL.
Pupils equal and reactive to light.

FLIP (answer s'): -Current Hgb 14.4 g/dL. | +Current Hgb 10.3 g/dL.

NEAR (answer s): -Current Hgb 14.4 g/dL. | +Current Hgb 11.0 g/dL.

MISSING (answer neither (undetermined)): -Current Hgb 14.4 g/dL.

PRES (answer s): full text
Male patient of 68 years.
Newly diagnosed colon cancer; first chemotherapy cycle planned for next week.
Lives in a second-floor apartment.
Photographs local wildlife.
Pupils equal and reactive to light.
Latest Hgb result: 14.4 g/dL.
Platelet count now 233 x10^9/L.
Latest WBC is 8.6 x10^9/L.
Sleeps seven hours a night.
Latest BMI is 27.4 kg/m2.


## 2.47 ('gs027', 'c1', 'negation', 'easy') templates=train

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If at least two of the following apply, prescribe nitrofurantoin instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the current weight is below 67 kg; the patient is allergic to penicillin.
CONDITION: coronary artery disease in the family
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
A 53-year-old woman.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Drinks alcohol occasionally.
Collects postcards.
Weighs 84 kg on the scale this morning.
Lives on a quiet street.
Allergic to penicillin (urticaria).

FLIP (answer s'): +Coronary artery disease, followed in cardiology clinic every six months.

NEAR (answer s): +Medical records show no coronary artery disease, past or present.

MISSING (answer neither (undetermined)): +Coronary artery disease in the family: not asked about.

PRES (answer s): full text
Female, 53 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Penicillin triggers an allergic reaction with wheezing in this patient.
Weight today: 84 kg.
Collects postcards.
Lives on a quiet street.
Drinks alcohol occasionally.


## 2.48 ('gs179', 'c2', 'numeric', 'long') templates=test

RULE: For acute migraine, prescribe sumatriptan. If the patient has ever had angioedema (current or past) or the current respiratory rate is 25/min or more, prescribe naproxen instead.
CONDITION: respiratory rate at least 25
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Female patient of 39 years.
Acute migraine without aura, typical of prior attacks.
Her roommate has recovered from a dislocated finger.
Drives a car.
In 2018, lipase was 30 U/L.
During a checkup in 2022, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2020.
Current respiratory rate 12/min.
Prefers to be addressed by first name.
Her wife sprained a thumb last month.
Lives in a second-floor apartment.
In 2010, folate was 12 ng/mL.
Uses sunscreen in summer.
Her wife lives with psoriasis.
Enjoys board games.
Her friend wears contact lenses.
Face and neck without swelling on examination.
Photographs local wildlife.
Prefers morning appointments.

FLIP (answer s'): -Current respiratory rate 12/min. | +Current respiratory rate 28/min.

NEAR (answer s): -Current respiratory rate 12/min. | +Current respiratory rate 24/min.

MISSING (answer neither (undetermined)): -Current respiratory rate 12/min.

PRES (answer s): full text
Woman of 39 years.
Acute migraine without aura, typical of prior attacks.
Enjoys board games.
Her roommate has recovered from a dislocated finger.
Free T4 of 1.2 ng/dL in 2020.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Prefers morning appointments.
Drives a car.
Photographs local wildlife.
During a checkup in 2022, total protein was 7.0 g/dL.
Free of facial or oropharyngeal edema.
Observations now: respiratory rate 12/min.
In 2018, lipase was 30 U/L.
Her wife lives with psoriasis.
Uses sunscreen in summer.
Her wife sprained a thumb last month.
In 2010, folate was 12 ng/mL.
Her friend wears contact lenses.


## 2.49 ('gs098', 'c3', 'subject', 'long') templates=train

RULE: For an acute gout flare, prescribe colchicine. Score 3 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 1 point if the patient is currently taking warfarin; 2 points if the patient currently has heart failure. If the score is 4 or more, prescribe prednisone instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe colchicine.' | s' = 'Prescribe prednisone.'

BASE (answer s):
Patient: male, 45 years.
Acute gout flare of the right first metatarsophalangeal joint.
Non-smoker.
Myocardial infarction in 2017, treated with a stent.
Enjoys cooking.
Has a pet dog.
Reads most evenings.
Volunteers at a library.
Hearing normal to conversation.
His aunt had a splinter removed from a finger.
Height 170 cm.
No INR monitoring in place.
His mother is being treated for eczema.
Writes with the right hand.
His brother-in-law has a broken finger in a splint.
Listens to podcasts.
Nails normal.
Phosphate 3.6 mg/dL in 2023.
Total bilirubin 0.6 mg/dL in 2006.
His mother has a stutter.
Drinks alcohol occasionally.

FLIP (answer s'): +Heart failure, under regular review in a cardiology clinic.

NEAR (answer s): +His aunt was admitted this morning with heart failure.

MISSING (answer neither (undetermined)): +Current heart failure: not recorded.

PRES (answer s): full text
A 45-year-old man.
Acute gout flare of the right first metatarsophalangeal joint.
Reads most evenings.
Total bilirubin 0.6 mg/dL in 2006.
Nails normal.
Enjoys cooking.
His brother-in-law has a broken finger in a splint.
Myocardial infarction in 2017; completed cardiac rehabilitation and has had no symptoms since.
Listens to podcasts.
Phosphate 3.6 mg/dL in 2023.
His mother has a stutter.
Non-smoker.
His aunt had a splinter removed from a finger.
Drinks alcohol occasionally.
Volunteers at a library.
Hearing normal to conversation.
Has a pet dog.
His mother is being treated for eczema.
Writes with the right hand.
Not taking any anticoagulants.
Height 170 cm.


## 2.50 ('gs190', 'c1', 'time', 'easy') templates=test

RULE: For acute sore throat, prescribe ibuprofen. If the patient is allergic to penicillin and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe penicillin V instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Man of 29 years.
Sore throat for two days.
Reports no allergies to medicines.
Plays the piano.
His father recovered from a pulmonary embolism in 2023.
Teeth in good repair.

FLIP (answer s'): -Reports no allergies to medicines. | +Known penicillin allergy with angioedema.

NEAR (answer s): -Reports no allergies to medicines. | +Outgrew a penicillin allergy by 2020.

MISSING (answer neither (undetermined)): -Reports no allergies to medicines. | +Penicillin allergy: unknown.

PRES (answer s): full text
Male patient of 29 years.
Sore throat for two days.
Drug allergies: none known.
Plays the piano.
Teeth in good repair.
His father had a DVT years ago.


## 2.51 ('gs160', 'c1', 'boundary', 'long') templates=train

RULE: For acute migraine, prescribe sumatriptan. If the current heart rate is above 90/min, prescribe naproxen instead.
CONDITION: heart rate above 90
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Patient: male, 34 years.
Acute migraine without aura, typical of prior attacks.
Pulse taken this morning: heart rate 75/min.
Total bilirubin 0.6 mg/dL in 2024.
Feeds birds in the backyard.
Serum calcium 9.4 mg/dL in 2014.
Hearing normal to conversation.
Lives on a quiet street.
His partner previously wore dental braces.
Uses a smartphone for reminders.
His housemate has a chipped front tooth.
Bicarbonate 26 mmol/L in 2020 (annual physical).
Height 170 cm.
Grows tomatoes in the garden.
His partner is nearsighted.
Ferritin 60 ng/mL in 2017.
Uses reading glasses for small print.
Watches football on weekends.
Reads most evenings.
His husband is left-handed.
Keeps houseplants.
Bakes bread at home.
Drinks plenty of water.

FLIP (answer s'): -Pulse taken this morning: heart rate 75/min. | +Pulse taken this morning: heart rate 122/min.

NEAR (answer s): -Pulse taken this morning: heart rate 75/min. | +Pulse taken this morning: heart rate 90/min.

MISSING (answer neither (undetermined)): -Pulse taken this morning: heart rate 75/min.

PRES (answer s): full text
Male, 34 years.
Acute migraine without aura, typical of prior attacks.
Uses reading glasses for small print.
His partner previously wore dental braces.
Keeps houseplants.
His husband is left-handed.
Uses a smartphone for reminders.
Drinks plenty of water.
Reads most evenings.
His housemate has a chipped front tooth.
Feeds birds in the backyard.
Grows tomatoes in the garden.
Heart rate today: 75/min.
Watches football on weekends.
Lives on a quiet street.
Serum calcium 9.4 mg/dL in 2014.
Total bilirubin 0.6 mg/dL in 2024.
Bakes bread at home.
Height 170 cm.
His partner is nearsighted.
Bicarbonate 26 mmol/L in 2020 (annual physical).
Ferritin 60 ng/mL in 2017.
Hearing normal to conversation.


## 2.52 ('gs218', 'c1', 'negation', 'long') templates=test

RULE: For primary prevention, prescribe atorvastatin. If the patient is allergic to sulfonamide antibiotics, prescribe ezetimibe instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Female patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Prefers to be addressed by first name.
Her friend has recovered from a dislocated finger.
Knits as a hobby.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Medication allergies: none at present.
Enjoys board games.
Zinc of 85 mcg/dL in 2020.
Her sister wears contact lenses.
Plays the piano.
Uses sunscreen in summer.
Sees a dentist yearly.
In 2010, folate was 12 ng/mL.
Prefers morning appointments.
Photographs local wildlife.
Her friend burned a hand on a stove years ago.

FLIP (answer s'): -Medication allergies: none at present. | +Develops hives whenever given sulfonamide antibiotics.

NEAR (answer s): -Medication allergies: none at present. | +Allergy history negative for sulfa drugs.

MISSING (answer neither (undetermined)): -Medication allergies: none at present. | +Sulfonamide allergy: status unclear from the records at hand.

PRES (answer s): full text
Woman of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Uses sunscreen in summer.
Current drug allergies: none.
Sees a dentist yearly.
Photographs local wildlife.
Prefers morning appointments.
Plays the piano.
Her friend has recovered from a dislocated finger.
Knits as a hobby.
Pupils equal and reactive to light.
In 2010, folate was 12 ng/mL.
Her sister wears contact lenses.
Enjoys board games.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2020.
Her friend burned a hand on a stove years ago.
Prefers to be addressed by first name.
Sleeps seven hours a night.


## 2.53 ('gs142', 'c2', 'numeric', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 3 points if the patient has ever had asthma (current or past); 1 point if the current serum creatinine is above 2.0 mg/dL; 3 points if the patient has had cancer at any time (active or in remission); 2 points if the current temperature is above 38.0 C. If the score is 6 or more, prescribe azithromycin instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Female, 60 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Blood panel at this assessment: creatinine 1.5 mg/dL.
Temperature checked with a digital thermometer today: 39.3 C.
Reads most evenings.
Uses a smartphone for reminders.
Has asthma and wakes at night with wheeze.

FLIP (answer s'): -Blood panel at this assessment: creatinine 1.5 mg/dL. | +Blood panel at this assessment: creatinine 2.8 mg/dL.

NEAR (answer s): -Blood panel at this assessment: creatinine 1.5 mg/dL. | +Blood panel at this assessment: creatinine 1.9 mg/dL.

MISSING (answer neither (undetermined)): -Blood panel at this assessment: creatinine 1.5 mg/dL.

PRES (answer s): full text
A 60-year-old woman.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Asthmatic; wheezes on exertion and in cold air.
Reads most evenings.
Serum creatinine today: 1.5 mg/dL.
Temperature 39.3 C at this assessment.
Uses a smartphone for reminders.


## 2.54 ('gs129', 'c1', 'subject', 'long') templates=test

RULE: For primary prevention, prescribe atorvastatin. If the patient has ever had angioedema (current or past) or the patient is currently taking clarithromycin, prescribe ezetimibe instead.
CONDITION: angioedema
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Woman of 73 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Uses sunscreen in summer.
During a checkup in 2009, total protein was 7.0 g/dL.
Prefers morning appointments.
Photographs local wildlife.
Teeth in good repair.
Her wife has recovered from a dislocated finger.
In 2008, folate was 12 ng/mL.
Lives in a second-floor apartment.
Sees a dentist yearly.
Plays the piano.
Enjoys board games.
Knits as a hobby.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2015.
Owns a bicycle.
Drives a car.
Free of facial or oropharyngeal edema.
Her friend wears contact lenses.
In 2021, lipase was 30 U/L.
Has two cats.
Prefers to be addressed by first name.

FLIP (answer s'): -Free of facial or oropharyngeal edema. | +Formerly had recurrent angioedema, in remission for many years now.

NEAR (answer s): -Free of facial or oropharyngeal edema. | +Her roommate has active angioedema of the face.

MISSING (answer neither (undetermined)): -Free of facial or oropharyngeal edema. | +Angioedema: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 73 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Teeth in good repair.
Enjoys board games.
In 2008, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2015.
Face and neck without swelling on examination.
Plays the piano.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Sees a dentist yearly.
Sleeps seven hours a night.
Drives a car.
Owns a bicycle.
During a checkup in 2009, total protein was 7.0 g/dL.
Her wife has recovered from a dislocated finger.
Prefers morning appointments.
Has two cats.
In 2021, lipase was 30 U/L.
Photographs local wildlife.
Her friend wears contact lenses.
Knits as a hobby.
Lives in a second-floor apartment.


## 2.55 ('c1_spironolactone', 'k', 'time', 'superseded') templates=train

RULE: For hypertension uncontrolled on amlodipine, ramipril and indapamide, prescribe spironolactone. If the current serum potassium is above 4.5 mmol/L, prescribe doxazosin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe doxazosin.'

BASE (answer s):
Male, 75 years.
Clinic blood pressure 158/96 mmHg on three visits despite full doses of amlodipine, ramipril and indapamide.
Potassium 4.1 mmol/L on today's blood work.
Uses a smartphone for reminders.
Lives on a quiet street.
Serum potassium was 4.0 mmol/L yesterday, before today's repeat.

FLIP (answer s'): -Potassium 4.1 mmol/L on today's blood work. | +Potassium 5.4 mmol/L on today's blood work.

NEAR (answer s): -Serum potassium was 4.0 mmol/L yesterday, before today's repeat. | +Serum potassium was 5.3 mmol/L yesterday, before today's repeat.

MISSING (answer neither (undetermined)): -Potassium 4.1 mmol/L on today's blood work. | -Serum potassium was 4.0 mmol/L yesterday, before today's repeat.

PRES (answer s): full text
A 75-year-old man.
Clinic blood pressure 158/96 mmHg on three visits despite full doses of amlodipine, ramipril and indapamide.
Uses a smartphone for reminders.
Lives on a quiet street.
On admission, serum potassium was 4.0 mmol/L; it has since been repeated.
Potassium measured at this assessment is 4.1 mmol/L.


## 2.56 ('gs000', 'c2', 'boundary', 'long') templates=test

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. Score 2 points if the patient is allergic to penicillin; 2 points if the current white cell count is below 4.0 x10^9/L; 3 points if the patient has ever had asthma (current or past). If the score is 4 or more, prescribe intermittent pneumatic compression instead.
CONDITION: white cell count below 4.0
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Female patient of 85 years.
Admitted for community-acquired pneumonia; immobile.
During a checkup in 2011, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Current white cell count 6.4 x10^9/L.
Plays the piano.
In 2008, lipase was 30 U/L.
Photographs local wildlife.
Inhaler use: none.
Sees a dentist yearly.
Her friend has recovered from a dislocated finger.
Teeth in good repair.
Sleeps seven hours a night.
Penicillin allergy: anaphylaxis.
Her roommate burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2013.
Paints watercolors as a hobby.
Her wife lives with psoriasis.
Prefers morning appointments.
In 2023, folate was 12 ng/mL.
Uses sunscreen in summer.
Lives in a second-floor apartment.

FLIP (answer s'): -Current white cell count 6.4 x10^9/L. | +Current white cell count 1.5 x10^9/L.

NEAR (answer s): -Current white cell count 6.4 x10^9/L. | +Current white cell count 4.0 x10^9/L.

MISSING (answer neither (undetermined)): -Current white cell count 6.4 x10^9/L.

PRES (answer s): full text
Woman of 85 years.
Admitted for community-acquired pneumonia; immobile.
Her friend has recovered from a dislocated finger.
Free T4 of 1.2 ng/dL in 2013.
During a checkup in 2011, total protein was 7.0 g/dL.
In 2008, lipase was 30 U/L.
Plays the piano.
Lungs clear, without wheeze or prolonged expiration.
Teeth in good repair.
In 2023, folate was 12 ng/mL.
Paints watercolors as a hobby.
Photographs local wildlife.
Lives in a second-floor apartment.
Sees a dentist yearly.
Her wife lives with psoriasis.
Known penicillin allergy with angioedema.
Prefers morning appointments.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Latest WBC is 6.4 x10^9/L.
Sleeps seven hours a night.
Her roommate burned a hand on a stove years ago.


## 2.57 ('gs047', 'c1', 'negation', 'easy') templates=train

RULE: For rate control in atrial fibrillation, prescribe metoprolol. If the patient is currently taking aspirin and the patient currently has tonsillar exudate, prescribe diltiazem instead.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Patient: male, 55 years.
Atrial fibrillation with a ventricular rate of 128/min.
Keeps a step counter.
Patchy exudate over the right tonsil.

FLIP (answer s'): +Medication list: aspirin 81 mg, taken each morning.

NEAR (answer s): +Reports no aspirin use, prescribed or over the counter.

MISSING (answer neither (undetermined)): +Aspirin use: not documented in the records available.

PRES (answer s): full text
Male, 55 years.
Atrial fibrillation with a ventricular rate of 128/min.
Keeps a step counter.
Creamy exudate in the tonsillar crypts today.


## 2.58 ('gs158', 'c2', 'numeric', 'easy') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time or the current white cell count is above 15.0 x10^9/L, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: white cell count above 15.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Female patient of 75 years.
Suspected chest infection; assessed on the medical ward.
Has two cats.
Climbs two flights of stairs without symptoms.
Latest WBC is 10.3 x10^9/L.
Owns a bicycle.

FLIP (answer s'): -Latest WBC is 10.3 x10^9/L. | +Latest WBC is 16.1 x10^9/L.

NEAR (answer s): -Latest WBC is 10.3 x10^9/L. | +Latest WBC is 14.4 x10^9/L.

MISSING (answer neither (undetermined)): -Latest WBC is 10.3 x10^9/L.

PRES (answer s): full text
Woman of 75 years.
Suspected chest infection; assessed on the medical ward.
Chest pain on exertion: none reported.
Owns a bicycle.
Has two cats.
Current white cell count 10.3 x10^9/L.


## 2.59 ('gs219', 'c2', 'subject', 'long') templates=train

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient has had a major bleeding event at any time or the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe warfarin instead.
CONDITION: vascular disease
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Male, 60 years.
Atrial fibrillation; anticoagulation indicated.
Drinks alcohol occasionally.
TSH 1.6 mIU/L in 2016.
Total bilirubin 0.6 mg/dL in 2024.
Keeps a step counter.
Hemoglobin normal on today's blood count.
Enjoys gardening.
Eats a varied diet.
Writes with the right hand.
His housemate previously wore dental braces.
Serum calcium 9.4 mg/dL in 2024.
Plays chess online.
Vaccinations up to date.
His cousin is being treated for eczema.
His mother has a chipped front tooth.
Enjoys cooking.
Nails normal.
Drinks plenty of water.
Bicarbonate 26 mmol/L in 2017 (annual physical).
Keeps houseplants.
His brother-in-law has a stutter.

FLIP (answer s'): +Peripheral artery disease, on cilostazol for pain on walking.

NEAR (answer s): +His cousin had a myocardial infarction in 2021.

MISSING (answer neither (undetermined)): +Vascular disease: not documented in the records available.

PRES (answer s): full text
Patient: male, 60 years.
Atrial fibrillation; anticoagulation indicated.
Nails normal.
His cousin is being treated for eczema.
Keeps a step counter.
Writes with the right hand.
Enjoys gardening.
Vaccinations up to date.
His housemate previously wore dental braces.
Drinks alcohol occasionally.
Keeps houseplants.
Bicarbonate 26 mmol/L in 2017 (annual physical).
Eats a varied diet.
Drinks plenty of water.
Serum calcium 9.4 mg/dL in 2024.
No hematuria or hemoptysis.
His mother has a chipped front tooth.
Enjoys cooking.
His brother-in-law has a stutter.
TSH 1.6 mIU/L in 2016.
Plays chess online.
Total bilirubin 0.6 mg/dL in 2024.


## 2.60 ('s1_smartcop', 'ph', 'time', 'superseded') templates=test

RULE: SMART-COP (as used here, partial, for patients older than 50 years): 2 points for a current systolic blood pressure below 90 mmHg; 1 point for a current respiratory rate of 30/min or more; 1 point for a current heart rate of 125/min or more; 2 points for a current oxygen saturation of 90% or less; 2 points for a current arterial pH below 7.35. Other SMART-COP items are not part of this question.
CONDITION: arterial pH below 7.35
CLAIMS: s = 'The arterial pH criterion contributes 0 points.' | s' = 'The arterial pH criterion contributes 2 points.'

BASE (answer s):
Man of 54 years.
Admitted with community-acquired pneumonia; reviewed by the medical team.
Last month, arterial pH was 7.39; the newest measurement replaces it.
Observations now: respiratory rate 22/min.
Current arterial pH 7.40.
Latest oxygen saturation reading: 98%.
Current systolic blood pressure 138 mmHg.
Prefers to be addressed by first name.
Current heart rate 72/min.

FLIP (answer s'): -Current arterial pH 7.40. | +Current arterial pH 7.26.

NEAR (answer s): -Last month, arterial pH was 7.39; the newest measurement replaces it. | +Last month, arterial pH was 7.29; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Last month, arterial pH was 7.39; the newest measurement replaces it. | -Current arterial pH 7.40.

PRES (answer s): full text
Male patient of 54 years.
Admitted with community-acquired pneumonia; reviewed by the medical team.
Current oxygen saturation 98%.
Prefers to be addressed by first name.
Heart rate now 72/min on the monitor.
Earlier this week, arterial pH was 7.39; a newer reading supersedes it.
Current respiratory rate 22/min.
Latest arterial blood gas shows a pH of 7.40.
Observations now: blood pressure 138/87 mmHg.


## 2.61 ('gs112', 'c3', 'boundary', 'long') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the patient is currently taking aspirin; 2 points if the current ALT is above 200 U/L. If the score is 5 or more, prescribe dapagliflozin instead.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
73-year-old man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
His coworker previously wore dental braces.
Takes one enteric-coated aspirin with breakfast every day.
Uses a smartphone for reminders.
Writes with the right hand.
His husband has a broken finger in a splint.
Sodium 140 mmol/L in 2009.
Feeds birds in the backyard.
Serum calcium 9.4 mg/dL in 2012.
ALT today: 37 U/L.
Listens to podcasts.
Keeps a step counter.
Drinks alcohol occasionally.
Plays chess online.
Uses public transport.
Reads most evenings.
His neighbor is left-handed.
Watches football on weekends.
Has a pet dog.
Non-smoker.
Angioplasty for coronary artery disease in 2006, after which all symptoms resolved.
Albumin 4.1 g/dL in 2006 (routine blood test).
Chloride 103 mmol/L in 2009.

FLIP (answer s'): -ALT today: 37 U/L. | +ALT today: 219 U/L.

NEAR (answer s): -ALT today: 37 U/L. | +ALT today: 200 U/L.

MISSING (answer neither (undetermined)): -ALT today: 37 U/L.

PRES (answer s): full text
Patient: male, 73 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Watches football on weekends.
Non-smoker.
Keeps a step counter.
Takes aspirin 81 mg daily.
His coworker previously wore dental braces.
Coronary artery disease was treated with a stent, and cardiology follow-up was completed in 2006 with no remaining symptoms.
Plays chess online.
Listens to podcasts.
His neighbor is left-handed.
Has a pet dog.
Serum calcium 9.4 mg/dL in 2012.
Drinks alcohol occasionally.
Uses a smartphone for reminders.
Uses public transport.
Sodium 140 mmol/L in 2009.
Feeds birds in the backyard.
Writes with the right hand.
Reads most evenings.
Chloride 103 mmol/L in 2009.
ALT 37 U/L on today's labs.
Albumin 4.1 g/dL in 2006 (routine blood test).
His husband has a broken finger in a splint.


## 2.62 ('gs172', 'c2', 'negation', 'long') templates=test

RULE: For an acute gout flare, prescribe colchicine. If the patient has ever had asthma (current or past) or the patient has ever had diabetes (current or past), prescribe prednisone instead.
CONDITION: diabetes
CLAIMS: s = 'Prescribe colchicine.' | s' = 'Prescribe prednisone.'

BASE (answer s):
Man of 69 years.
Acute gout flare of the right first metatarsophalangeal joint.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Photographs local wildlife.
Has two cats.
In 2005, folate was 12 ng/mL.
Prefers morning appointments.
Enjoys board games.
Random glucose 92 mg/dL.
Zinc of 85 mcg/dL in 2014.
Sees a dentist yearly.
During a checkup in 2024, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Plays the piano.
His wife burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
His wife has a lazy eye.
Teeth in good repair.
Lungs clear, without wheeze or prolonged expiration.
Prefers to be addressed by first name.

FLIP (answer s'): -Random glucose 92 mg/dL. | +Had diabetes years ago that went into remission on a low-calorie diet.

NEAR (answer s): -Random glucose 92 mg/dL. | +Has never had diabetes.

MISSING (answer neither (undetermined)): -Random glucose 92 mg/dL. | +Diabetes: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 69 years.
Acute gout flare of the right first metatarsophalangeal joint.
Inhaler use: none.
His wife burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2014.
Paints watercolors as a hobby.
Knits as a hobby.
Pupils equal and reactive to light.
During a checkup in 2024, total protein was 7.0 g/dL.
Prefers morning appointments.
Plays the piano.
HbA1c 5.3% at a routine check.
Sleeps seven hours a night.
Uses sunscreen in summer.
Sees a dentist yearly.
Enjoys board games.
Teeth in good repair.
His wife has a lazy eye.
Photographs local wildlife.
In 2005, folate was 12 ng/mL.
Prefers to be addressed by first name.
Has two cats.


## 2.63 ('gs200', 'c1', 'numeric', 'long') templates=train

RULE: For vaginal candidiasis, prescribe oral fluconazole. Score 2 points if the current blood urea nitrogen is above 45 mg/dL; 3 points if the patient has ever had angioedema (current or past); 1 point if the patient currently has asthma; 2 points if the age of the patient is 80 years or more. If the score is 5 or more, prescribe clotrimazole pessaries instead.
CONDITION: blood urea nitrogen above 45
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Female patient.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Nails normal.
Wears a seat belt when driving.
Her aunt has a chipped front tooth.
Her partner has a fear of heights.
Writes with the right hand.
Sings in a weekly choir.
Magnesium 2.0 mg/dL in 2013.
Ferritin 60 ng/mL in 2007.
Angioedema after a wasp sting in 2007, which resolved within a day.
Chest clear on auscultation, with no wheeze.
Eats a varied diet.
Phosphate 3.6 mg/dL in 2018.
Bakes bread at home.
Does crossword puzzles.
BUN on today's chemistry panel: 16 mg/dL.
Speaks English and Spanish.
Drinks two cups of coffee a day.
Age 62 years, calculated today from the date of birth.
Has a pet dog.
Hearing normal to conversation.
Her cousin has a broken finger in a splint.

FLIP (answer s'): -BUN on today's chemistry panel: 16 mg/dL. | +BUN on today's chemistry panel: 47 mg/dL.

NEAR (answer s): -BUN on today's chemistry panel: 16 mg/dL. | +BUN on today's chemistry panel: 44 mg/dL.

MISSING (answer neither (undetermined)): -BUN on today's chemistry panel: 16 mg/dL.

PRES (answer s): full text
Adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Has a pet dog.
Bakes bread at home.
Her cousin has a broken finger in a splint.
Wears a seat belt when driving.
Phosphate 3.6 mg/dL in 2018.
Ferritin 60 ng/mL in 2007.
Speaks English and Spanish.
Previously had angioedema of the tongue in 2007, which settled within hours.
BUN 16 mg/dL this morning.
Eats a varied diet.
Hearing normal to conversation.
Nails normal.
Does crossword puzzles.
Sings in a weekly choir.
Her partner has a fear of heights.
Magnesium 2.0 mg/dL in 2013.
No night cough or chest tightness.
Age today: 62 years.
Writes with the right hand.
Drinks two cups of coffee a day.
Her aunt has a chipped front tooth.


## 2.64 ('gs026', 'c4', 'subject', 'long') templates=test

RULE: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current heart rate is 109/min or more; 2 points if the patient has ever had a stroke or TIA (current or past); 3 points if the patient is allergic to penicillin; 3 points if the patient currently has tender anterior cervical lymph nodes. If the score is 4 or more, prescribe clotrimazole pessaries instead.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Woman of 64 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drug allergies: none known.
Plays the piano.
Her uncle has a lazy eye.
Her roommate lives with psoriasis.
Drives a car.
Knits as a hobby.
During a checkup in 2005, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Her father sprained a thumb last month.
Teeth in good repair.
In 2020, lipase was 30 U/L.
Sees a dentist yearly.
In 2013, folate was 12 ng/mL.
Free T4 of 1.2 ng/dL in 2012.
Heart rate now 126/min on the monitor.
Power and sensation normal in all limbs.

FLIP (answer s'): +Tender, swollen lymph nodes in the front of the neck.

NEAR (answer s): +Her roommate has a throat infection with tender anterior cervical lymph nodes.

MISSING (answer neither (undetermined)): +Tender cervical lymph nodes: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 64 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her father sprained a thumb last month.
Her roommate lives with psoriasis.
Knits as a hobby.
Drives a car.
Teeth in good repair.
Lives in a second-floor apartment.
During a checkup in 2005, total protein was 7.0 g/dL.
Sees a dentist yearly.
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Her uncle has a lazy eye.
Reports no allergies to medicines.
Free T4 of 1.2 ng/dL in 2012.
Plays the piano.
Gait normal; no focal weakness.
In 2013, folate was 12 ng/mL.
Current heart rate 126/min.
Uses sunscreen in summer.


## 2.65 ('gs152', 'c2', 'time', 'long') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the current heart rate is 180/min or more or the patient is allergic to sulfonamide antibiotics, prescribe intermittent pneumatic compression instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
A 79-year-old woman.
Admitted for community-acquired pneumonia; immobile.
Drinks two cups of coffee a day.
Albumin 4.1 g/dL in 2022 (routine blood test).
Keeps houseplants.
Bakes bread at home.
Vaccinations up to date.
Height 170 cm.
Her brother has a fear of heights.
Uses a smartphone for reminders.
Sings in a weekly choir.
Heart rate counted over a full minute at this assessment: 105/min.
Reads most evenings.
Uses public transport.
Total bilirubin 0.6 mg/dL in 2022.
Does crossword puzzles.
Listens to podcasts.
Uses reading glasses for small print.
Her husband previously wore dental braces.
Her housemate has a stutter.
Drinks plenty of water.
Keeps a step counter.
No known antibiotic allergies.
Her husband is being treated for eczema.

FLIP (answer s'): -No known antibiotic allergies. | +Sulfa antibiotics cause an itchy allergic rash in this patient.

NEAR (answer s): -No known antibiotic allergies. | +Sulfa antibiotic allergy in childhood, resolved; tolerated trimethoprim-sulfamethoxazole in 2020.

MISSING (answer neither (undetermined)): -No known antibiotic allergies. | +Information on sulfonamide allergy was not obtained.

PRES (answer s): full text
79-year-old woman.
Admitted for community-acquired pneumonia; immobile.
Her brother has a fear of heights.
Uses reading glasses for small print.
Albumin 4.1 g/dL in 2022 (routine blood test).
Height 170 cm.
Her husband is being treated for eczema.
Her husband previously wore dental braces.
Drinks two cups of coffee a day.
Listens to podcasts.
Total bilirubin 0.6 mg/dL in 2022.
Her housemate has a stutter.
Uses a smartphone for reminders.
Keeps a step counter.
Pulse taken this morning: heart rate 105/min.
Uses public transport.
Reads most evenings.
Vaccinations up to date.
No known medication allergies.
Keeps houseplants.
Does crossword puzzles.
Drinks plenty of water.
Sings in a weekly choir.
Bakes bread at home.


## 2.66 ('s1_spesi', 'age', 'boundary', 'long') templates=test

RULE: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.
CONDITION: age above 80
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Weight steady over the past year.
Plays the piano.
Lives in a second-floor apartment.
Heart rate now 93/min on the monitor.
Pupils equal and reactive to light.
During a checkup in 2018, total protein was 7.0 g/dL.
Observations now: blood pressure 138/87 mmHg.
Her uncle sprained a thumb last month.
Teeth in good repair.
Owns a bicycle.
Her roommate lives with psoriasis.
In 2011, lipase was 30 U/L.
In 2010, folate was 12 ng/mL.
Photographs local wildlife.
Drives a car.
Knits as a hobby.
Enjoys board games.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Has two cats.
Her wife has a lazy eye.
Uses sunscreen in summer.
Latest oxygen saturation reading: 95%.
Current age 63 years.

FLIP (answer s'): -Current age 63 years. | +Current age 81 years.

NEAR (answer s): -Current age 63 years. | +Current age 80 years.

MISSING (answer neither (undetermined)): -Current age 63 years.

PRES (answer s): full text
An adult woman.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Sleeps seven hours a night.
In 2011, lipase was 30 U/L.
Currently aged 63 years.
Teeth in good repair.
Uses sunscreen in summer.
In 2010, folate was 12 ng/mL.
Her wife has a lazy eye.
Owns a bicycle.
Has two cats.
Enjoys board games.
Current heart rate 93/min.
Lives in a second-floor apartment.
Her roommate lives with psoriasis.
Pupils equal and reactive to light.
Current systolic blood pressure 138 mmHg.
Current oxygen saturation 95%.
Her uncle sprained a thumb last month.
Photographs local wildlife.
Plays the piano.
Malignant disease: none at present.
Knits as a hobby.
Drives a car.
Paints watercolors as a hobby.
During a checkup in 2018, total protein was 7.0 g/dL.


## 2.67 ('gs088', 'c2', 'negation', 'long') templates=train

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. Score 1 point if the patient is currently taking warfarin; 3 points if the patient has ever had asthma (current or past); 1 point if the patient has new confusion. If the score is 4 or more, prescribe sitagliptin instead.
CONDITION: asthma at any time
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
A 76-year-old woman.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Nails normal.
Non-smoker.
Grows tomatoes in the garden.
Her neighbor is left-handed.
Her cousin had a splinter removed from a finger.
Bakes bread at home.
Her cousin has a stutter.
Listens to podcasts.
Enjoys gardening.
Uses public transport.
Drinks plenty of water.
On long-term warfarin, with an INR of 2.6 this morning.
Writes with the right hand.
Does crossword puzzles.
Vaccinations up to date.
Magnesium 2.0 mg/dL in 2007.
Uses a smartphone for reminders.
Keeps houseplants.
Chloride 103 mmol/L in 2011.
Hearing normal to conversation.

FLIP (answer s'): +Asthma attack this month needing nebulizers; still wheezy at this assessment.

NEAR (answer s): +No asthma or other airway disease.

MISSING (answer neither (undetermined)): +Asthma at any time: not recorded.

PRES (answer s): full text
76-year-old woman.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Drinks plenty of water.
Vaccinations up to date.
Medications: warfarin 5 mg once daily.
Chloride 103 mmol/L in 2011.
Nails normal.
Hearing normal to conversation.
Listens to podcasts.
Her cousin had a splinter removed from a finger.
Her neighbor is left-handed.
Writes with the right hand.
Magnesium 2.0 mg/dL in 2007.
Does crossword puzzles.
Non-smoker.
Her cousin has a stutter.
Enjoys gardening.
Keeps houseplants.
Uses a smartphone for reminders.
Uses public transport.
Bakes bread at home.
Grows tomatoes in the garden.


## 2.68 ('gs174', 'c1', 'numeric', 'easy') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient currently has asthma, prescribe aspirin plus clopidogrel instead.
CONDITION: serum potassium above 5.0
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Male patient of 58 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Prefers to be addressed by first name.
Current serum potassium 3.6 mmol/L.
Asthma, on a daily inhaled steroid.
Paints watercolors as a hobby.
Lives in a second-floor apartment.

FLIP (answer s'): -Current serum potassium 3.6 mmol/L. | +Current serum potassium 6.0 mmol/L.

NEAR (answer s): -Current serum potassium 3.6 mmol/L. | +Current serum potassium 4.9 mmol/L.

MISSING (answer neither (undetermined)): -Current serum potassium 3.6 mmol/L.

PRES (answer s): full text
Man of 58 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Persistent asthma, using a rescue inhaler most weeks.
Latest potassium result: 3.6 mmol/L.


## 2.69 ('c3_hmb_vte', 'vte', 'subject', 'long') templates=train

RULE: For heavy menstrual bleeding, prescribe tranexamic acid. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe a levonorgestrel intrauterine system instead.
CONDITION: venous thromboembolism at any time in the patient or a first-degree relative
CLAIMS: s = 'Prescribe tranexamic acid.' | s' = 'Prescribe a levonorgestrel intrauterine system.'

BASE (answer s):
35-year-old woman.
Heavy menstrual bleeding for six months; pelvic ultrasound normal.
Her grandfather is left-handed.
Feeds birds in the backyard.
Volunteers at a library.
Nails normal.
Uses public transport.
Her brother-in-law wears hearing aids.
Her neighbor completed physical therapy for a shoulder injury.
Non-smoker.
Sings in a weekly choir.
Enjoys gardening.
Enjoys cooking.
Chloride 103 mmol/L in 2017.
Her aunt has a broken finger in a splint.
Vaccinations up to date.
Keeps houseplants.
Serum calcium 9.4 mg/dL in 2010.

FLIP (answer s'): +On treatment for a deep vein thrombosis in the left leg.

NEAR (answer s): +Her grandmother has a DVT in one leg.

MISSING (answer neither (undetermined)): +Venous thromboembolism at any time in the patient or a first-degree relative: not documented in the records available.

PRES (answer s): full text
Patient: female, 35 years.
Heavy menstrual bleeding for six months; pelvic ultrasound normal.
Uses public transport.
Sings in a weekly choir.
Nails normal.
Feeds birds in the backyard.
Keeps houseplants.
Vaccinations up to date.
Her neighbor completed physical therapy for a shoulder injury.
Serum calcium 9.4 mg/dL in 2010.
Her aunt has a broken finger in a splint.
Her grandfather is left-handed.
Enjoys gardening.
Volunteers at a library.
Non-smoker.
Chloride 103 mmol/L in 2017.
Her brother-in-law wears hearing aids.
Enjoys cooking.


## 2.70 ('gs038', 'c1', 'time', 'long') templates=test

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the patient has an active peptic ulcer and the patient has new confusion, prescribe intravenous co-amoxiclav instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
Female patient of 60 years.
Community-acquired pneumonia confirmed on chest radiograph.
Her sister wears contact lenses.
Lives in a second-floor apartment.
Photographs local wildlife.
Paints watercolors as a hobby.
Her sister has recovered from a dislocated finger.
During a checkup in 2014, total protein was 7.0 g/dL.
Sees a dentist yearly.
Drives a car.
Pupils equal and reactive to light.
Plays the piano.
Disoriented to time and place, which is new for the patient.
Has two cats.
Owns a bicycle.
In 2023, folate was 12 ng/mL.
Appetite good; no indigestion.
Sleeps seven hours a night.
Prefers morning appointments.

FLIP (answer s'): -Appetite good; no indigestion. | +Active peptic ulcer disease.

NEAR (answer s): -Appetite good; no indigestion. | +Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.

MISSING (answer neither (undetermined)): -Appetite good; no indigestion. | +Active peptic ulcer: status unclear from the records at hand.

PRES (answer s): full text
Woman of 60 years.
Community-acquired pneumonia confirmed on chest radiograph.
Lives in a second-floor apartment.
Abdomen soft and non-tender.
Plays the piano.
Newly disoriented and unable to give a clear history.
Drives a car.
Owns a bicycle.
Her sister wears contact lenses.
Paints watercolors as a hobby.
Has two cats.
During a checkup in 2014, total protein was 7.0 g/dL.
Photographs local wildlife.
In 2023, folate was 12 ng/mL.
Her sister has recovered from a dislocated finger.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Prefers morning appointments.
Sees a dentist yearly.


## 2.71 ('gs162', 'c2', 'boundary', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient is allergic to penicillin and the current serum potassium is above 4.5 mmol/L, prescribe azithromycin instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
A 59-year-old woman.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Labs this morning: potassium 3.9 mmol/L.
Allergies: penicillin (rash).
Drinks two cups of coffee a day.

FLIP (answer s'): -Labs this morning: potassium 3.9 mmol/L. | +Labs this morning: potassium 5.4 mmol/L.

NEAR (answer s): -Labs this morning: potassium 3.9 mmol/L. | +Labs this morning: potassium 4.5 mmol/L.

MISSING (answer neither (undetermined)): -Labs this morning: potassium 3.9 mmol/L.

PRES (answer s): full text
Female, 59 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Allergic to penicillin (urticaria).
Potassium measured at this assessment is 3.9 mmol/L.
Drinks two cups of coffee a day.


## 2.72 ('gs069', 'c2', 'negation', 'long') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the patient is currently taking aspirin and the patient currently has a major bleed, prescribe sitagliptin instead.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Man of 78 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
In 2008, lipase was 30 U/L.
Prefers to be addressed by first name.
His wife wears contact lenses.
Owns a bicycle.
Enjoys board games.
Teeth in good repair.
Zinc of 85 mcg/dL in 2022.
Bowel habit normal, without any blood in the stool.
Lives in a second-floor apartment.
Sees a dentist yearly.
Has two cats.
Free T4 of 1.2 ng/dL in 2014.
Paints watercolors as a hobby.
His sister burned a hand on a stove years ago.
Photographs local wildlife.
Currently on low-dose aspirin for heart protection.
Uses sunscreen in summer.

FLIP (answer s'): -Bowel habit normal, without any blood in the stool. | +Major bleed from the stomach at present, with hemoglobin falling.

NEAR (answer s): -Bowel habit normal, without any blood in the stool. | +Medical records negative for major bleeding at any time.

MISSING (answer neither (undetermined)): -Bowel habit normal, without any blood in the stool. | +Active major bleeding: unknown.

PRES (answer s): full text
Male patient of 78 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2022.
Examination shows no signs of blood loss.
His wife wears contact lenses.
Has two cats.
Free T4 of 1.2 ng/dL in 2014.
Sees a dentist yearly.
His sister burned a hand on a stove years ago.
Uses a daily aspirin on a cardiologist's recommendation.
Uses sunscreen in summer.
Teeth in good repair.
Prefers to be addressed by first name.
Owns a bicycle.
Enjoys board games.
In 2008, lipase was 30 U/L.
Photographs local wildlife.
Lives in a second-floor apartment.


## 2.73 ('s1_psi', 'bun', 'numeric', 'easy') templates=train

RULE: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 30 mg/dL or more. Age, sex and other items of the index are not part of this question.
CONDITION: blood urea nitrogen at least 30
CLAIMS: s = 'The blood urea nitrogen criterion contributes 0 points.' | s' = 'The blood urea nitrogen criterion contributes 20 points.'

BASE (answer s):
61-year-old man.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
BUN at this assessment: 15 mg/dL.
No evidence of active neoplasia.
Enjoys gardening.
Arterial pH 7.45 on the blood gas taken at this assessment.
Heart size normal on chest radiograph.

FLIP (answer s'): -BUN at this assessment: 15 mg/dL. | +BUN at this assessment: 38 mg/dL.

NEAR (answer s): -BUN at this assessment: 15 mg/dL. | +BUN at this assessment: 28 mg/dL.

MISSING (answer neither (undetermined)): -BUN at this assessment: 15 mg/dL.

PRES (answer s): full text
Male, 61 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Enjoys gardening.
BUN on today's chemistry panel: 15 mg/dL.
Recent echocardiogram normal.
No unexplained weight loss or new lumps.
Arterial blood gas this morning: pH 7.45.


## 2.74 ('gs006', 'c1', 'subject', 'long') templates=test

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 3 points if the patient has had cancer at any time (active or in remission); 2 points if the current blood urea nitrogen is 20 mg/dL or more; 1 point if the patient has ever had diabetes (current or past). If the score is 4 or more, prescribe dapagliflozin instead.
CONDITION: cancer at any time
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Man of 54 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
In 2013, lipase was 30 U/L.
Has two cats.
Lives in a second-floor apartment.
Has type 2 diabetes on metformin.
His uncle lives with psoriasis.
Knits as a hobby.
Malignant disease: none at present.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Blood urea nitrogen now: 34 mg/dL.
Sees a dentist yearly.
Prefers morning appointments.
Drives a car.
Zinc of 85 mcg/dL in 2019.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Enjoys board games.
His sister sprained a thumb last month.
His father burned a hand on a stove years ago.

FLIP (answer s'): -Malignant disease: none at present. | +Has metastatic lung cancer, receiving palliative treatment.

NEAR (answer s): -Malignant disease: none at present. | +His sister is being treated for leukemia.

MISSING (answer neither (undetermined)): -Malignant disease: none at present. | +Cancer at any time: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 54 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Zinc of 85 mcg/dL in 2019.
Weight steady over the past year.
Prefers morning appointments.
Paints watercolors as a hobby.
Insulin-treated diabetes.
Blood urea nitrogen 34 mg/dL on the current labs.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
In 2013, lipase was 30 U/L.
His sister sprained a thumb last month.
Knits as a hobby.
Has two cats.
Drives a car.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Sees a dentist yearly.
His uncle lives with psoriasis.
His father burned a hand on a stove years ago.
Enjoys board games.


## 2.75 ('gs127', 'c1', 'time', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current calf swelling compared with the other leg is 3.0 cm or more or the patient currently has asthma, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
63-year-old man.
Suspected chest infection; assessed on the medical ward.
Height 170 cm.
Takes no inhaled medicines.
Difference in calf circumference today, side to side: 0.2 cm.
Calf swelling 1.0 cm at a clinic visit in 2022.

FLIP (answer s'): -Difference in calf circumference today, side to side: 0.2 cm. | +Difference in calf circumference today, side to side: 3.7 cm.

NEAR (answer s): -Calf swelling 1.0 cm at a clinic visit in 2022. | +Calf swelling 5.6 cm at a clinic visit in 2022.

MISSING (answer neither (undetermined)): -Difference in calf circumference today, side to side: 0.2 cm. | -Calf swelling 1.0 cm at a clinic visit in 2022.

PRES (answer s): full text
Patient: male, 63 years.
Suspected chest infection; assessed on the medical ward.
Height 170 cm.
Chest clear on auscultation, with no wheeze.
Calf swelling at this assessment: 0.2 cm more than the opposite calf.
A routine check in 2022 gave calf swelling 1.0 cm.
