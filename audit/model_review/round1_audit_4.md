# Audit sample 4


## 4.1 ('s1_meds', 'age', 'boundary', 'long') templates=train

RULE: Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.
CONDITION: age above 65
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 3 points.'

BASE (answer s):
Sex: female.
Suspected sepsis; admitted from the emergency department.
Complete blood count today: platelets 255 x10^9/L.
Vitamin D 38 ng/mL in 2006 (wellness visit).
Speaks English and Spanish.
Listens to podcasts.
Enjoys gardening.
Albumin 4.1 g/dL in 2007 (routine blood test).
Age at this assessment: 51 years.
Chloride 103 mmol/L in 2020.
Bakes bread at home.
Her husband has a fear of heights.
Enjoys cooking.
Her husband is left-handed.
Height 170 cm.
Non-smoker.
Vitamin B12 450 pg/mL in 2018.
Keeps a step counter.
Watches football on weekends.
Her husband is nearsighted.
Wears a seat belt when driving.
Volunteers at a library.
Her housemate previously wore dental braces.

FLIP (answer s'): -Age at this assessment: 51 years. | +Age at this assessment: 87 years.

NEAR (answer s): -Age at this assessment: 51 years. | +Age at this assessment: 65 years.

MISSING (answer neither (undetermined)): -Age at this assessment: 51 years.

PRES (answer s): full text
Female patient.
Suspected sepsis; admitted from the emergency department.
Enjoys gardening.
Her husband is nearsighted.
Watches football on weekends.
Her husband has a fear of heights.
Listens to podcasts.
Age 51 years, calculated today from the date of birth.
Vitamin B12 450 pg/mL in 2018.
Vitamin D 38 ng/mL in 2006 (wellness visit).
Albumin 4.1 g/dL in 2007 (routine blood test).
Non-smoker.
Speaks English and Spanish.
Keeps a step counter.
Her husband is left-handed.
Volunteers at a library.
Height 170 cm.
Her housemate previously wore dental braces.
Wears a seat belt when driving.
Chloride 103 mmol/L in 2020.
Platelet count today: 255 x10^9/L.
Enjoys cooking.
Bakes bread at home.


## 4.2 ('any_gout', 'ulcer', 'negation', 'long') templates=test

RULE: For an acute gout flare, prescribe naproxen. If the patient has an active peptic ulcer or the current eGFR is below 30 mL/min/1.73 m2, prescribe colchicine instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe colchicine.'

BASE (answer s):
Male patient of 43 years.
Acute gout flare of the left knee.
Pupils equal and reactive to light.
Appetite good; no indigestion.
In 2009, lipase was 30 U/L.
Has two cats.
Sleeps seven hours a night.
Sees a dentist yearly.
Current eGFR 82 mL/min/1.73 m2.
Uses sunscreen in summer.
His sister lives with psoriasis.
Drives a car.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2019.
Lives in a second-floor apartment.
Enjoys board games.
Teeth in good repair.
Zinc of 85 mcg/dL in 2007.
His friend wears contact lenses.
His uncle has recovered from a dislocated finger.

FLIP (answer s'): -Appetite good; no indigestion. | +Active peptic ulcer disease.

NEAR (answer s): -Appetite good; no indigestion. | +Medical record negative for peptic ulcer, current or past.

MISSING (answer neither (undetermined)): -Appetite good; no indigestion. | +Active peptic ulcer: status unclear from the records at hand.

PRES (answer s): full text
Man of 43 years.
Acute gout flare of the left knee.
Teeth in good repair.
Has two cats.
Sees a dentist yearly.
Prefers to be addressed by first name.
Enjoys board games.
Lives in a second-floor apartment.
Drives a car.
Plays the piano.
Sleeps seven hours a night.
His friend wears contact lenses.
His uncle has recovered from a dislocated finger.
Uses sunscreen in summer.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2019.
His sister lives with psoriasis.
In 2009, lipase was 30 U/L.
Abdomen soft and non-tender.
eGFR now 82 mL/min/1.73 m2.
Zinc of 85 mcg/dL in 2007.
Pupils equal and reactive to light.


## 4.3 ('gs203', 'c1', 'numeric', 'easy') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current calf swelling compared with the other leg is 3.0 cm or more, prescribe dapagliflozin instead.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
51-year-old man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Difference in calf circumference today, side to side: 0.2 cm.
Bakes bread at home.

FLIP (answer s'): -Difference in calf circumference today, side to side: 0.2 cm. | +Difference in calf circumference today, side to side: 3.9 cm.

NEAR (answer s): -Difference in calf circumference today, side to side: 0.2 cm. | +Difference in calf circumference today, side to side: 2.5 cm.

MISSING (answer neither (undetermined)): -Difference in calf circumference today, side to side: 0.2 cm.

PRES (answer s): full text
Male, 51 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Calf swelling at this assessment: 0.2 cm more than the opposite calf.
Bakes bread at home.


## 4.4 ('gs010', 'c1', 'subject', 'long') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient is currently taking aspirin, prescribe naproxen with omeprazole instead.
CONDITION: aspirin use
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Female patient of 80 years.
Hip osteoarthritis with pain on walking.
Owns a bicycle.
Knits as a hobby.
Prefers morning appointments.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2007.
Her wife has recovered from a dislocated finger.
Drives a car.
Teeth in good repair.
Enjoys board games.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Her wife burned a hand on a stove years ago.
Has two cats.
During a checkup in 2008, total protein was 7.0 g/dL.
Photographs local wildlife.
Pupils equal and reactive to light.
Sees a dentist yearly.

FLIP (answer s'): +Uses a daily aspirin on a cardiologist's recommendation.

NEAR (answer s): +Her roommate uses a daily aspirin for heart protection.

MISSING (answer neither (undetermined)): +Aspirin use: unknown.

PRES (answer s): full text
Woman of 80 years.
Hip osteoarthritis with pain on walking.
Drives a car.
Pupils equal and reactive to light.
Enjoys board games.
Her wife burned a hand on a stove years ago.
Sleeps seven hours a night.
Her wife has recovered from a dislocated finger.
Teeth in good repair.
Owns a bicycle.
During a checkup in 2008, total protein was 7.0 g/dL.
Sees a dentist yearly.
Has two cats.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2007.
Photographs local wildlife.
Knits as a hobby.
Prefers morning appointments.


## 4.5 ('gs142', 'c2', 'time', 'long') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 3 points if the patient has ever had asthma (current or past); 1 point if the current serum creatinine is above 2.0 mg/dL; 3 points if the patient has had cancer at any time (active or in remission); 2 points if the current temperature is above 38.0 C. If the score is 6 or more, prescribe azithromycin instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
31-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Drinks two cups of coffee a day.
Bakes bread at home.
His grandmother is being treated for eczema.
Serum creatinine 1.2 mg/dL at a clinic visit in 2019.
His mother has a chipped front tooth.
Volunteers at a library.
TSH 1.6 mIU/L in 2023.
Temperature checked with a digital thermometer today: 39.2 C.
Kidney function today: creatinine 1.3 mg/dL.
Does crossword puzzles.
Plays chess online.
Nails normal.
Speaks English and Spanish.
Non-smoker.
Drinks plenty of water.
Keeps a step counter.
Albumin 4.1 g/dL in 2019 (routine blood test).
Takes no inhaled medicines.
Total bilirubin 0.6 mg/dL in 2023.
Wears a seat belt when driving.
Uses public transport.
Previously treated for Hodgkin lymphoma, with treatment completed in 2018; remains in remission.
Vitamin B12 450 pg/mL in 2022.

FLIP (answer s'): -Kidney function today: creatinine 1.3 mg/dL. | +Kidney function today: creatinine 3.6 mg/dL.

NEAR (answer s): -Serum creatinine 1.2 mg/dL at a clinic visit in 2019. | +Serum creatinine 2.9 mg/dL at a clinic visit in 2019.

MISSING (answer neither (undetermined)): -Serum creatinine 1.2 mg/dL at a clinic visit in 2019. | -Kidney function today: creatinine 1.3 mg/dL.

PRES (answer s): full text
Patient: male, 31 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Vitamin B12 450 pg/mL in 2022.
No night cough or chest tightness.
Volunteers at a library.
Speaks English and Spanish.
Plays chess online.
His grandmother is being treated for eczema.
Total bilirubin 0.6 mg/dL in 2023.
Drinks two cups of coffee a day.
Keeps a step counter.
Colon cancer removed surgically in 2018, in remission since.
TSH 1.6 mIU/L in 2023.
Drinks plenty of water.
Serum creatinine of 1.2 mg/dL recorded in 2019.
Temperature 39.2 C at this assessment.
Uses public transport.
His mother has a chipped front tooth.
Creatinine 1.3 mg/dL on this morning's labs.
Bakes bread at home.
Nails normal.
Does crossword puzzles.
Wears a seat belt when driving.
Non-smoker.
Albumin 4.1 g/dL in 2019 (routine blood test).


## 4.6 ('gs234', 'c1', 'boundary', 'easy') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the age of the patient is above 60 years or the patient currently has tender anterior cervical lymph nodes, prescribe aspirin plus clopidogrel instead.
CONDITION: age above 60
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
An adult woman.
Recovering on the ward after a myocardial infarction treated with a stent.
Prefers morning appointments.
Currently aged 41 years.
Sleeps seven hours a night.
Front of the neck without tenderness or swelling.

FLIP (answer s'): -Currently aged 41 years. | +Currently aged 86 years.

NEAR (answer s): -Currently aged 41 years. | +Currently aged 60 years.

MISSING (answer neither (undetermined)): -Currently aged 41 years.

PRES (answer s): full text
Woman, adult.
Recovering on the ward after a myocardial infarction treated with a stent.
Neck palpation unremarkable.
Prefers morning appointments.
Current age 41 years.
Sleeps seven hours a night.


## 4.7 ('gs057', 'c2', 'negation', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current ALT is above 200 U/L or the patient has an active peptic ulcer, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
A 61-year-old woman.
Suspected chest infection; assessed on the medical ward.
Uses a smartphone for reminders.
Bowel habit normal; no abdominal pain.
Does crossword puzzles.
Plays chess online.
ALT today: 42 U/L.

FLIP (answer s'): -Bowel habit normal; no abdominal pain. | +Bleeding gastric ulcer under active treatment.

NEAR (answer s): -Bowel habit normal; no abdominal pain. | +Denies any history of peptic ulcer.

MISSING (answer neither (undetermined)): -Bowel habit normal; no abdominal pain. | +Active peptic ulcer: not asked about.

PRES (answer s): full text
Patient: female, 61 years.
Suspected chest infection; assessed on the medical ward.
ALT 42 U/L on today's labs.
Plays chess online.
Uses a smartphone for reminders.
No dyspepsia or melena.
Does crossword puzzles.


## 4.8 ('gs158', 'c2', 'numeric', 'long') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time or the current white cell count is above 15.0 x10^9/L, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: white cell count above 15.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Female patient of 75 years.
Suspected chest infection; assessed on the medical ward.
Uses sunscreen in summer.
Enjoys board games.
During a checkup in 2014, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Her friend wears contact lenses.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2016.
Plays the piano.
Her sister has recovered from a dislocated finger.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2014.
Her wife burned a hand on a stove years ago.
In 2018, folate was 12 ng/mL.
Current white cell count 5.5 x10^9/L.
Has two cats.
Her wife lives with psoriasis.

FLIP (answer s'): -Current white cell count 5.5 x10^9/L. | +Current white cell count 19.1 x10^9/L.

NEAR (answer s): -Current white cell count 5.5 x10^9/L. | +Current white cell count 13.9 x10^9/L.

MISSING (answer neither (undetermined)): -Current white cell count 5.5 x10^9/L.

PRES (answer s): full text
Woman of 75 years.
Suspected chest infection; assessed on the medical ward.
Her sister has recovered from a dislocated finger.
During a checkup in 2014, total protein was 7.0 g/dL.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2014.
Sees a dentist yearly.
Plays the piano.
Latest WBC is 5.5 x10^9/L.
Sleeps seven hours a night.
Her friend wears contact lenses.
Her wife burned a hand on a stove years ago.
Her wife lives with psoriasis.
Zinc of 85 mcg/dL in 2016.
Uses sunscreen in summer.
Has two cats.
In 2018, folate was 12 ng/mL.
Enjoys board games.


## 4.9 ('gs142', 'c3', 'subject', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 3 points if the patient has ever had asthma (current or past); 1 point if the current serum creatinine is above 2.0 mg/dL; 3 points if the patient has had cancer at any time (active or in remission); 2 points if the current temperature is above 38.0 C. If the score is 6 or more, prescribe azithromycin instead.
CONDITION: cancer at any time
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Patient: male, 62 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Previously had asthma in childhood; symptom-free and off inhalers for decades.
Has a pet dog.
Uses reading glasses for small print.
Serum creatinine today: 1.1 mg/dL.
Oral temperature this morning: 36.5 C.
No unexplained weight loss or new lumps.
Plays chess online.

FLIP (answer s'): -No unexplained weight loss or new lumps. | +Active colon cancer under oncology treatment.

NEAR (answer s): -No unexplained weight loss or new lumps. | +His cousin has active colon cancer.

MISSING (answer neither (undetermined)): -No unexplained weight loss or new lumps. | +Cancer at any time: not documented in the records available.

PRES (answer s): full text
A 62-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Temperature today: 36.5 C.
Childhood asthma, resolved by adolescence.
Plays chess online.
Creatinine 1.1 mg/dL on this morning's labs.
Uses reading glasses for small print.
Has a pet dog.
No active malignancy.


## 4.10 ('gs022', 'c1', 'time', 'superseded') templates=test

RULE: For knee osteoarthritis pain, prescribe naproxen. If at least two of the following apply, prescribe acetaminophen instead: the current oxygen saturation is 90% or less; the patient has ever had angioedema (current or past); the patient currently has heart failure.
CONDITION: oxygen saturation at or below 90
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Woman of 55 years.
Knee osteoarthritis with pain on walking.
Prefers morning appointments.
Current heart failure with ankle swelling.
Free of facial or oropharyngeal edema.
Last month, oxygen saturation was 99%; the newest measurement replaces it.
Current oxygen saturation 94%.

FLIP (answer s'): -Current oxygen saturation 94%. | +Current oxygen saturation 84%.

NEAR (answer s): -Last month, oxygen saturation was 99%; the newest measurement replaces it. | +Last month, oxygen saturation was 83%; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Last month, oxygen saturation was 99%; the newest measurement replaces it. | -Current oxygen saturation 94%.

PRES (answer s): full text
Female patient of 55 years.
Knee osteoarthritis with pain on walking.
Earlier this week, oxygen saturation was 99%; a newer reading supersedes it.
Has heart failure, treated with diuretics.
Face and neck without swelling on examination.
Prefers morning appointments.
Latest oxygen saturation reading: 94%.


## 4.11 ('c1_methimazole', 'alt', 'boundary', 'easy') templates=train

RULE: For Graves' hyperthyroidism, prescribe methimazole. If the current ALT is above 200 U/L, prescribe radioactive iodine instead.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe methimazole.' | s' = 'Prescribe radioactive iodine.'

BASE (answer s):
Female, 26 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Reads most evenings.
Uses a smartphone for reminders.
ALT on blood drawn this morning: 71 U/L.
Writes with the right hand.
Has a pet dog.

FLIP (answer s'): -ALT on blood drawn this morning: 71 U/L. | +ALT on blood drawn this morning: 342 U/L.

NEAR (answer s): -ALT on blood drawn this morning: 71 U/L. | +ALT on blood drawn this morning: 200 U/L.

MISSING (answer neither (undetermined)): -ALT on blood drawn this morning: 71 U/L.

PRES (answer s): full text
Patient: female, 26 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Uses a smartphone for reminders.
Writes with the right hand.
Liver tests today: ALT 71 U/L.
Has a pet dog.
Reads most evenings.


## 4.12 ('gs126', 'c1', 'negation', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient is currently taking clarithromycin, prescribe naproxen with omeprazole instead.
CONDITION: clarithromycin
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Male patient of 69 years.
Hip osteoarthritis with pain on walking.
Prefers morning appointments.
Sleeps seven hours a night.
Drives a car.
Has two cats.
Has no antibiotic course under way.

FLIP (answer s'): -Has no antibiotic course under way. | +On clarithromycin for a chest infection, day 3 of 7.

NEAR (answer s): -Has no antibiotic course under way. | +Clarithromycin absent from the pharmacy dispensing record.

MISSING (answer neither (undetermined)): -Has no antibiotic course under way. | +Clarithromycin: status unclear from the records at hand.

PRES (answer s): full text
Man of 69 years.
Hip osteoarthritis with pain on walking.
Drives a car.
Current antibiotic therapy: none.
Sleeps seven hours a night.
Has two cats.
Prefers morning appointments.


## 4.13 ('gs106', 'c2', 'numeric', 'easy') templates=train

RULE: For vaginal candidiasis, prescribe oral fluconazole. Score 2 points if the patient has ever had a venous thromboembolism (current or past); 2 points if the current blood urea nitrogen is 20 mg/dL or more; 1 point if the patient currently has tonsillar exudate; 1 point if the patient is currently taking clarithromycin. If the score is 3 or more, prescribe clotrimazole pessaries instead.
CONDITION: blood urea nitrogen at least 20
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
37-year-old woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
No antibiotics or antifungals in use.
Grows tomatoes in the garden.
Anticoagulation for a pulmonary embolism was completed in 2012, and the clot resolved.
Lives on a quiet street.
Today's BUN is 13 mg/dL.
Drinks two cups of coffee a day.
Watches football on weekends.
No membrane, film or spots seen over the tonsils.

FLIP (answer s'): -Today's BUN is 13 mg/dL. | +Today's BUN is 32 mg/dL.

NEAR (answer s): -Today's BUN is 13 mg/dL. | +Today's BUN is 18 mg/dL.

MISSING (answer neither (undetermined)): -Today's BUN is 13 mg/dL.

PRES (answer s): full text
A 37-year-old woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Lives on a quiet street.
Grows tomatoes in the garden.
Antibiotics: none.
Watches football on weekends.
Previously had a DVT, in 2012.
Throat mildly red; tonsils not coated.
Drinks two cups of coffee a day.
BUN on today's chemistry panel: 13 mg/dL.


## 4.14 ('postop_hit', 'hit', 'subject', 'easy') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had heparin-induced thrombocytopenia (current or past), prescribe fondaparinux instead.
CONDITION: heparin-induced thrombocytopenia
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Man of 66 years.
First day after elective total hip replacement.
Owns a bicycle.
Photographs local wildlife.

FLIP (answer s'): +Heparin-induced thrombocytopenia, with heparin antibodies still positive.

NEAR (answer s): +His wife has developed heparin-induced thrombocytopenia after surgery.

MISSING (answer neither (undetermined)): +Heparin-induced thrombocytopenia: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 66 years.
First day after elective total hip replacement.
Photographs local wildlife.
Owns a bicycle.


## 4.15 ('cut_sepsis', 'sbp', 'time', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. Score 2 points for a current respiratory rate of 22/min or more; 1 point for current altered mentation; 1 point for a current systolic blood pressure of 100 mmHg or less. If the score is 3 or more, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: systolic blood pressure at or below 100
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
52-year-old woman.
Suspected chest infection; assessed on the medical ward.
Respiratory rate, counted over a full minute today, is 28/min.
Manual cuff blood pressure today: 133/84 mmHg.
Systolic blood pressure 111 mmHg at a clinic visit in 2015.
Lives on a quiet street.
Answers questions appropriately.
Vaccinations up to date.

FLIP (answer s'): -Manual cuff blood pressure today: 133/84 mmHg. | +Manual cuff blood pressure today: 99/63 mmHg.

NEAR (answer s): -Systolic blood pressure 111 mmHg at a clinic visit in 2015. | +Systolic blood pressure 94 mmHg at a clinic visit in 2015.

MISSING (answer neither (undetermined)): -Manual cuff blood pressure today: 133/84 mmHg. | -Systolic blood pressure 111 mmHg at a clinic visit in 2015.

PRES (answer s): full text
Female, 52 years.
Suspected chest infection; assessed on the medical ward.
Vaccinations up to date.
Systolic blood pressure 133 mmHg at this assessment.
Respiratory rate 28/min at this assessment.
Alert and attentive.
Lives on a quiet street.
A routine check in 2015 gave systolic blood pressure 111 mmHg.


## 4.16 ('s1_spesi', 'sbp', 'boundary', 'easy') templates=test

RULE: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.
CONDITION: systolic blood pressure below 100
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Malignant disease: none at present.
Current oxygen saturation 96%.
Heart rate now 98/min on the monitor.
Observations now: blood pressure 159/99 mmHg.
Currently aged 53 years.
Owns a bicycle.

FLIP (answer s'): -Observations now: blood pressure 159/99 mmHg. | +Observations now: blood pressure 91/59 mmHg.

NEAR (answer s): -Observations now: blood pressure 159/99 mmHg. | +Observations now: blood pressure 100/64 mmHg.

MISSING (answer neither (undetermined)): -Observations now: blood pressure 159/99 mmHg.

PRES (answer s): full text
An adult woman.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Current heart rate 98/min.
Latest oxygen saturation reading: 96%.
Weight steady over the past year.
Current age 53 years.
Current systolic blood pressure 159 mmHg.
Owns a bicycle.


## 4.17 ('c2_sprain_warfarin', 'warfarin', 'negation', 'easy') templates=train

RULE: For an acute ankle sprain, prescribe naproxen. If the patient is currently taking warfarin, prescribe acetaminophen instead.
CONDITION: warfarin use
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: male, 75 years.
Right ankle sprain after a fall on uneven ground; radiograph normal.
Drinks two cups of coffee a day.
Uses a smartphone for reminders.
Writes with the right hand.
No INR monitoring in place.

FLIP (answer s'): -No INR monitoring in place. | +Takes warfarin for atrial fibrillation.

NEAR (answer s): -No INR monitoring in place. | +Not on warfarin.

MISSING (answer neither (undetermined)): -No INR monitoring in place. | +Warfarin use: not recorded.

PRES (answer s): full text
Male, 75 years.
Right ankle sprain after a fall on uneven ground; radiograph normal.
Writes with the right hand.
No vitamin K antagonist on the medication list.
Uses a smartphone for reminders.
Drinks two cups of coffee a day.


## 4.18 ('gs220', 'c1', 'numeric', 'long') templates=test

RULE: For cellulitis of the lower leg, prescribe cephalexin. If the current respiratory rate is 22/min or more, prescribe clindamycin instead.
CONDITION: respiratory rate at least 22
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Female patient of 47 years.
Spreading redness and warmth of the right shin for two days.
Free T4 of 1.2 ng/dL in 2006.
Photographs local wildlife.
During a checkup in 2017, total protein was 7.0 g/dL.
Her sister has recovered from a dislocated finger.
Her wife wears contact lenses.
Drives a car.
Teeth in good repair.
Prefers morning appointments.
In 2013, folate was 12 ng/mL.
Her friend lives with psoriasis.
Paints watercolors as a hobby.
Owns a bicycle.
Plays the piano.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Current respiratory rate 14/min.
Sees a dentist yearly.
Uses sunscreen in summer.
Her uncle has a lazy eye.

FLIP (answer s'): -Current respiratory rate 14/min. | +Current respiratory rate 34/min.

NEAR (answer s): -Current respiratory rate 14/min. | +Current respiratory rate 21/min.

MISSING (answer neither (undetermined)): -Current respiratory rate 14/min.

PRES (answer s): full text
Woman of 47 years.
Spreading redness and warmth of the right shin for two days.
Her sister has recovered from a dislocated finger.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Observations now: respiratory rate 14/min.
Paints watercolors as a hobby.
In 2013, folate was 12 ng/mL.
Her uncle has a lazy eye.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2006.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
Her wife wears contact lenses.
Sees a dentist yearly.
Prefers morning appointments.
Drives a car.
Prefers to be addressed by first name.
Her friend lives with psoriasis.
Uses sunscreen in summer.
During a checkup in 2017, total protein was 7.0 g/dL.


## 4.19 ('gs233', 'c1', 'subject', 'long') templates=train

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had heparin-induced thrombocytopenia (current or past) and the current weight is below 67 kg, prescribe naproxen with omeprazole instead.
CONDITION: heparin-induced thrombocytopenia
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
77-year-old man.
Hip osteoarthritis with pain on walking.
Grows tomatoes in the garden.
No heparin products on the medication chart today.
Nails normal.
Bicarbonate 26 mmol/L in 2012 (annual physical).
Speaks English and Spanish.
Plays chess online.
Sodium 140 mmol/L in 2020.
Bakes bread at home.
Hearing normal to conversation.
His coworker has a stutter.
Phosphate 3.6 mg/dL in 2015.
Writes with the right hand.
His neighbor is being treated for eczema.
Uses reading glasses for small print.
Weight 56 kg at this assessment.
Height 170 cm.
His housemate has a chipped front tooth.
Volunteers at a library.
Sings in a weekly choir.
His partner is left-handed.

FLIP (answer s'): -No heparin products on the medication chart today. | +Heparin-induced thrombocytopenia diagnosed this week; all heparin is being avoided.

NEAR (answer s): -No heparin products on the medication chart today. | +His housemate is being treated for heparin-induced thrombocytopenia.

MISSING (answer neither (undetermined)): -No heparin products on the medication chart today. | +Heparin-induced thrombocytopenia: not recorded.

PRES (answer s): full text
A 77-year-old man.
Hip osteoarthritis with pain on walking.
Nails normal.
Speaks English and Spanish.
Volunteers at a library.
His neighbor is being treated for eczema.
Bicarbonate 26 mmol/L in 2012 (annual physical).
Phosphate 3.6 mg/dL in 2015.
Weight checked today on a calibrated scale: 56 kg.
Grows tomatoes in the garden.
Sings in a weekly choir.
His coworker has a stutter.
Bakes bread at home.
Not on any blood thinner at present.
Writes with the right hand.
Plays chess online.
Height 170 cm.
His partner is left-handed.
Hearing normal to conversation.
Sodium 140 mmol/L in 2020.
His housemate has a chipped front tooth.
Uses reading glasses for small print.


## 4.20 ('c2_statin_clarith', 'clarith', 'time', 'easy') templates=test

RULE: For primary prevention of cardiovascular disease, prescribe simvastatin. If the patient is currently taking clarithromycin, prescribe pravastatin instead.
CONDITION: clarithromycin use
CLAIMS: s = 'Prescribe simvastatin.' | s' = 'Prescribe pravastatin.'

BASE (answer s):
Woman of 69 years.
Primary prevention; LDL cholesterol 172 mg/dL, 10-year cardiovascular risk 11%.
Enjoys board games.
Has no antibiotic course under way.
Photographs local wildlife.
Prefers to be addressed by first name.
Prefers morning appointments.

FLIP (answer s'): -Has no antibiotic course under way. | +On clarithromycin for a chest infection, day 3 of 7.

NEAR (answer s): -Has no antibiotic course under way. | +Took clarithromycin for pneumonia years ago.

MISSING (answer neither (undetermined)): -Has no antibiotic course under way. | +Clarithromycin use: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 69 years.
Primary prevention; LDL cholesterol 172 mg/dL, 10-year cardiovascular risk 11%.
Current antibiotic therapy: none.
Enjoys board games.
Photographs local wildlife.
Prefers morning appointments.
Prefers to be addressed by first name.


## 4.21 ('gs132', 'c1', 'boundary', 'easy') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the current eGFR is below 45 mL/min/1.73 m2, prescribe intermittent pneumatic compression instead.
CONDITION: eGFR below 45
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
A 77-year-old man.
Admitted for community-acquired pneumonia; immobile.
Listens to podcasts.
Does crossword puzzles.
Grows tomatoes in the garden.
Renal function today: eGFR 85 mL/min/1.73 m2.

FLIP (answer s'): -Renal function today: eGFR 85 mL/min/1.73 m2. | +Renal function today: eGFR 29 mL/min/1.73 m2.

NEAR (answer s): -Renal function today: eGFR 85 mL/min/1.73 m2. | +Renal function today: eGFR 45 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Renal function today: eGFR 85 mL/min/1.73 m2.

PRES (answer s): full text
Patient: male, 77 years.
Admitted for community-acquired pneumonia; immobile.
Listens to podcasts.
Does crossword puzzles.
eGFR 85 mL/min/1.73 m2 on today's labs.
Grows tomatoes in the garden.


## 4.22 ('gs240', 'c1', 'negation', 'easy') templates=test

RULE: For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.
CONDITION: angioedema
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Female patient of 51 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sleeps seven hours a night.
Enjoys board games.

FLIP (answer s'): +Recurrent angioedema, under allergy follow-up.

NEAR (answer s): +Has never had angioedema.

MISSING (answer neither (undetermined)): +Angioedema: unknown.

PRES (answer s): full text
Woman of 51 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sleeps seven hours a night.
Enjoys board games.


## 4.23 ('s2_atria_bleed', 'age', 'numeric', 'long') templates=train

RULE: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 30 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.
CONDITION: age at least 75
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 2 points.'

BASE (answer s):
Sex: male.
Atrial fibrillation; a decision on warfarin is pending.
Uses a smartphone for reminders.
Enjoys cooking.
Hgb 14.7 g/dL on this morning's blood count.
Eats a varied diet.
Keeps houseplants.
Vitamin B12 450 pg/mL in 2008.
Drinks two cups of coffee a day.
Albumin 4.1 g/dL in 2018 (routine blood test).
eGFR 79 mL/min/1.73 m2 on today's labs.
Hearing normal to conversation.
Does crossword puzzles.
His aunt is left-handed.
Uses reading glasses for small print.
Age 63 years, calculated today from the date of birth.
Sings in a weekly choir.
Uses public transport.
His brother is being treated for eczema.
Total bilirubin 0.6 mg/dL in 2012.
Volunteers at a library.
Non-smoker.
Keeps a step counter.

FLIP (answer s'): -Age 63 years, calculated today from the date of birth. | +Age 88 years, calculated today from the date of birth.

NEAR (answer s): -Age 63 years, calculated today from the date of birth. | +Age 74 years, calculated today from the date of birth.

MISSING (answer neither (undetermined)): -Age 63 years, calculated today from the date of birth.

PRES (answer s): full text
Adult man.
Atrial fibrillation; a decision on warfarin is pending.
Drinks two cups of coffee a day.
Uses public transport.
Hearing normal to conversation.
Non-smoker.
Volunteers at a library.
Blood count today: Hgb 14.7 g/dL.
Keeps houseplants.
Albumin 4.1 g/dL in 2018 (routine blood test).
Uses a smartphone for reminders.
Keeps a step counter.
Eats a varied diet.
Enjoys cooking.
This morning's blood test shows an eGFR of 79 mL/min/1.73 m2.
Age on arrival: 63 years.
Vitamin B12 450 pg/mL in 2008.
Uses reading glasses for small print.
Total bilirubin 0.6 mg/dL in 2012.
Sings in a weekly choir.
His aunt is left-handed.
His brother is being treated for eczema.
Does crossword puzzles.


## 4.24 ('gs103', 'c4', 'subject', 'long') templates=test

RULE: For acute migraine, prescribe sumatriptan. Score 2 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient has an active peptic ulcer; 2 points if the patient is allergic to sulfonamide antibiotics; 2 points if the patient has new confusion. If the score is 7 or more, prescribe naproxen instead.
CONDITION: new confusion
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Female patient of 52 years.
Acute migraine without aura, typical of prior attacks.
Her roommate has a lazy eye.
Pupils equal and reactive to light.
Sees a dentist yearly.
Her roommate has recovered from a dislocated finger.
Teeth in good repair.
Her roommate sprained a thumb last month.
Her uncle lives with psoriasis.
Develops hives whenever given sulfonamide antibiotics.
Lives in a second-floor apartment.
In 2005, lipase was 30 U/L.
Photographs local wildlife.
Climbs two flights of stairs without symptoms.
Uses sunscreen in summer.
Prefers morning appointments.
Enjoys board games.
Zinc of 85 mcg/dL in 2015.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Drives a car.
Has an active duodenal ulcer.
Paints watercolors as a hobby.
Speech clear; follows commands.
Sleeps seven hours a night.

FLIP (answer s'): -Speech clear; follows commands. | +Disoriented to time and place, which is new for the patient.

NEAR (answer s): -Speech clear; follows commands. | +Her wife is newly disoriented.

MISSING (answer neither (undetermined)): -Speech clear; follows commands. | +New confusion: unknown.

PRES (answer s): full text
Woman of 52 years.
Acute migraine without aura, typical of prior attacks.
Zinc of 85 mcg/dL in 2015.
Her roommate sprained a thumb last month.
Her roommate has a lazy eye.
Active peptic ulcer disease.
Sleeps seven hours a night.
Prefers morning appointments.
Her uncle lives with psoriasis.
Photographs local wildlife.
Gives a clear account of the illness.
Sees a dentist yearly.
Sulfonamide antibiotic allergy: generalized rash.
In 2005, lipase was 30 U/L.
Uses sunscreen in summer.
Chest pain on exertion: none reported.
Drives a car.
Enjoys board games.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Her roommate has recovered from a dislocated finger.
Teeth in good repair.
During a checkup in 2018, free T3 was 3.2 pg/mL.


## 4.25 ('af_asthma', 'asthma', 'time', 'easy') templates=train

RULE: For rate control in atrial fibrillation, start metoprolol. If the patient currently has asthma, start diltiazem instead.
CONDITION: asthma
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Patient: female, 55 years.
Atrial fibrillation with a ventricular rate of 128/min.
Uses a smartphone for reminders.
Chest clear on auscultation, with no wheeze.
Height 170 cm.

FLIP (answer s'): -Chest clear on auscultation, with no wheeze. | +Asthmatic; wheezes on exertion and in cold air.

NEAR (answer s): -Chest clear on auscultation, with no wheeze. | +Asthma that began after a chest infection in 2007 and resolved within a year.

MISSING (answer neither (undetermined)): -Chest clear on auscultation, with no wheeze. | +Asthma: not documented in the records available.

PRES (answer s): full text
Female, 55 years.
Atrial fibrillation with a ventricular rate of 128/min.
Uses a smartphone for reminders.
Good air entry on both sides of the chest.
Height 170 cm.


## 4.26 ('centor', 'temp', 'boundary', 'long') templates=test

RULE: Centor score (as used here, partial): 1 point each for temperature above 38.0 C; tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.
CONDITION: temperature above 38.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
Male patient of 30 years.
Sore throat for three days.
His wife wears contact lenses.
Zinc of 85 mcg/dL in 2014.
Knits as a hobby.
Teeth in good repair.
His friend has recovered from a dislocated finger.
During a checkup in 2022, total protein was 7.0 g/dL.
Enjoys board games.
Owns a bicycle.
Uses sunscreen in summer.
Sees a dentist yearly.
Lives in a second-floor apartment.
Has two cats.
Tonsils slightly red but clean, without pus.
Sleeps seven hours a night.
His friend burned a hand on a stove years ago.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2020, folate was 12 ng/mL.
Temperature now 36.6 C (tympanic).
Drives a car.
Plays the piano.
Neck palpation unremarkable.

FLIP (answer s'): -Temperature now 36.6 C (tympanic). | +Temperature now 39.3 C (tympanic).

NEAR (answer s): -Temperature now 36.6 C (tympanic). | +Temperature now 38.0 C (tympanic).

MISSING (answer neither (undetermined)): -Temperature now 36.6 C (tympanic).

PRES (answer s): full text
Man of 30 years.
Sore throat for three days.
Knits as a hobby.
Current temperature 36.6 C.
Zinc of 85 mcg/dL in 2014.
Uses sunscreen in summer.
Owns a bicycle.
In 2020, folate was 12 ng/mL.
Enjoys board games.
Photographs local wildlife.
Plays the piano.
Sleeps seven hours a night.
Teeth in good repair.
Has two cats.
His friend has recovered from a dislocated finger.
Front of the neck without tenderness or swelling.
Sees a dentist yearly.
Lives in a second-floor apartment.
Tonsils pink and clean on inspection.
Drives a car.
His wife wears contact lenses.
Paints watercolors as a hobby.
His friend burned a hand on a stove years ago.
During a checkup in 2022, total protein was 7.0 g/dL.


## 4.27 ('gs156', 'c3', 'negation', 'long') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient has ever had a venous thromboembolism (current or past); the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time.
CONDITION: colorectal cancer
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
A 40-year-old woman.
Requests contraception.
Drinks alcohol occasionally.
Her partner previously wore dental braces.
Her coworker broke a wrist, which has healed.
Grows tomatoes in the garden.
Plays chess online.
Height 170 cm.
Abdomen soft, with no masses on examination.
Drinks plenty of water.
Allergies: penicillin (rash).
Chloride 103 mmol/L in 2007.
Enjoys gardening.
Wears a seat belt when driving.
Volunteers at a library.
Her coworker has a chipped front tooth.
Keeps a step counter.
Drinks two cups of coffee a day.
Her aunt completed physical therapy for a shoulder injury.
Total bilirubin 0.6 mg/dL in 2018.
Not on any blood thinners.

FLIP (answer s'): -Abdomen soft, with no masses on examination. | +Bowel cancer in 2014; all treatment completed and the patient was declared cancer-free.

NEAR (answer s): -Abdomen soft, with no masses on examination. | +No colon cancer, past or present.

MISSING (answer neither (undetermined)): -Abdomen soft, with no masses on examination. | +Colorectal cancer: not recorded.

PRES (answer s): full text
Female, 40 years.
Requests contraception.
Her partner previously wore dental braces.
Her coworker broke a wrist, which has healed.
Drinks plenty of water.
Her aunt completed physical therapy for a shoulder injury.
Plays chess online.
Drinks two cups of coffee a day.
Penicillin triggers an allergic reaction with wheezing in this patient.
Total bilirubin 0.6 mg/dL in 2018.
Keeps a step counter.
No known blood clotting disorder.
Her coworker has a chipped front tooth.
Grows tomatoes in the garden.
Wears a seat belt when driving.
Height 170 cm.
Weight stable and appetite good.
Volunteers at a library.
Chloride 103 mmol/L in 2007.
Enjoys gardening.
Drinks alcohol occasionally.


## 4.28 ('gs209', 'c1', 'numeric', 'easy') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current platelet count is below 50 x10^9/L or the patient has ever had angioedema (current or past), prescribe warfarin instead.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Man of 51 years.
Atrial fibrillation; anticoagulation indicated.
Platelet count now 253 x10^9/L.
Owns a bicycle.
Enjoys board games.
Pupils equal and reactive to light.
Prefers morning appointments.

FLIP (answer s'): -Platelet count now 253 x10^9/L. | +Platelet count now 43 x10^9/L.

NEAR (answer s): -Platelet count now 253 x10^9/L. | +Platelet count now 57 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count now 253 x10^9/L.

PRES (answer s): full text
Male patient of 51 years.
Atrial fibrillation; anticoagulation indicated.
Prefers morning appointments.
Owns a bicycle.
Pupils equal and reactive to light.
Current platelet count 253 x10^9/L.
Enjoys board games.


## 4.29 ('gs014', 'c2', 'subject', 'long') templates=train

RULE: For primary prevention, prescribe atorvastatin. If the current oxygen saturation is below 90% or the patient currently has heart failure, prescribe ezetimibe instead.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
41-year-old man.
Primary prevention; LDL cholesterol 182 mg/dL.
Speaks English and Spanish.
Vitamin B12 450 pg/mL in 2021.
Vaccinations up to date.
Pulse oximetry this morning: oxygen saturation 96%.
Writes with the right hand.
Keeps houseplants.
Hearing normal to conversation.
Wears a seat belt when driving.
His mother has a fear of heights.
His coworker has a chipped front tooth.
Uses public transport.
Enjoys gardening.
Ferritin 60 ng/mL in 2022.
Watches football on weekends.
Drinks two cups of coffee a day.
Takes no diuretics.
Drinks plenty of water.
Sodium 140 mmol/L in 2019.
His cousin wears hearing aids.

FLIP (answer s'): -Takes no diuretics. | +Chronic heart failure (NYHA class II).

NEAR (answer s): -Takes no diuretics. | +His husband was admitted this morning with heart failure.

MISSING (answer neither (undetermined)): -Takes no diuretics. | +Current heart failure: not recorded.

PRES (answer s): full text
Patient: male, 41 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Speaks English and Spanish.
His cousin wears hearing aids.
His coworker has a chipped front tooth.
Drinks two cups of coffee a day.
Vitamin B12 450 pg/mL in 2021.
Enjoys gardening.
Recent echocardiogram normal.
Wears a seat belt when driving.
Writes with the right hand.
Uses public transport.
Watches football on weekends.
Drinks plenty of water.
Keeps houseplants.
Vaccinations up to date.
His mother has a fear of heights.
Oxygen saturation at this assessment is 96%.
Sodium 140 mmol/L in 2019.
Hearing normal to conversation.
Ferritin 60 ng/mL in 2022.


## 4.30 ('gs192', 'c2', 'time', 'long') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has an active peptic ulcer and the current respiratory rate is 50/min or more, prescribe naproxen with omeprazole instead.
CONDITION: respiratory rate at least 50
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Man of 48 years.
Hip osteoarthritis with pain on walking.
His roommate has recovered from a dislocated finger.
Free T4 of 1.2 ng/dL in 2021.
Lives in a second-floor apartment.
Current respiratory rate 18/min.
During a checkup in 2014, total protein was 7.0 g/dL.
His roommate has a lazy eye.
Prefers to be addressed by first name.
Plays the piano.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Enjoys board games.
Active peptic ulcer disease.
Drives a car.
Uses sunscreen in summer.
In 2024, folate was 12 ng/mL.
Back in 2017, respiratory rate measured 12/min.
Paints watercolors as a hobby.
Has two cats.
Owns a bicycle.
Knits as a hobby.
Sees a dentist yearly.
His friend wears contact lenses.
Teeth in good repair.

FLIP (answer s'): -Current respiratory rate 18/min. | +Current respiratory rate 58/min.

NEAR (answer s): -Back in 2017, respiratory rate measured 12/min. | +Back in 2017, respiratory rate measured 51/min.

MISSING (answer neither (undetermined)): -Current respiratory rate 18/min. | -Back in 2017, respiratory rate measured 12/min.

PRES (answer s): full text
Male patient of 48 years.
Hip osteoarthritis with pain on walking.
His roommate has a lazy eye.
Pupils equal and reactive to light.
Enjoys board games.
Has two cats.
Paints watercolors as a hobby.
Knits as a hobby.
Sees a dentist yearly.
Teeth in good repair.
Observations now: respiratory rate 18/min.
His friend wears contact lenses.
Free T4 of 1.2 ng/dL in 2021.
Drives a car.
Has an active duodenal ulcer.
Lives in a second-floor apartment.
Records from 2017 list respiratory rate at 12/min.
In 2024, folate was 12 ng/mL.
Prefers to be addressed by first name.
Owns a bicycle.
His roommate has recovered from a dislocated finger.
During a checkup in 2014, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Plays the piano.
Uses sunscreen in summer.


## 4.31 ('s1_smartcop', 'sbp', 'boundary', 'long') templates=train

RULE: SMART-COP (as used here, partial, for patients older than 50 years): 2 points for a current systolic blood pressure below 90 mmHg; 1 point for a current respiratory rate of 30/min or more; 1 point for a current heart rate of 125/min or more; 2 points for a current oxygen saturation of 90% or less; 2 points for a current arterial pH below 7.35. Other SMART-COP items are not part of this question.
CONDITION: systolic blood pressure below 90
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 2 points.'

BASE (answer s):
51-year-old woman.
Admitted with community-acquired pneumonia; reviewed by the medical team.
Her cousin had a splinter removed from a finger.
Systolic blood pressure 138 mmHg at this assessment.
Volunteers at a library.
Speaks English and Spanish.
Non-smoker.
Respiratory rate today: 22/min.
Nails normal.
Lives on a quiet street.
Arterial pH on today's blood gas: 7.42.
Chloride 103 mmol/L in 2015.
Eats a varied diet.
Heart rate 69/min at rest this morning.
Enjoys gardening.
Writes with the right hand.
Her aunt completed physical therapy for a shoulder injury.
Keeps a step counter.
Has a pet dog.
Vaccinations up to date.
Hearing normal to conversation.
Plays chess online.
Sodium 140 mmol/L in 2005.
Feeds birds in the backyard.
Reads most evenings.
Pulse oximetry this morning: oxygen saturation 97%.
Uses public transport.

FLIP (answer s'): -Systolic blood pressure 138 mmHg at this assessment. | +Systolic blood pressure 89 mmHg at this assessment.

NEAR (answer s): -Systolic blood pressure 138 mmHg at this assessment. | +Systolic blood pressure 90 mmHg at this assessment.

MISSING (answer neither (undetermined)): -Systolic blood pressure 138 mmHg at this assessment.

PRES (answer s): full text
A 51-year-old woman.
Admitted with community-acquired pneumonia; reviewed by the medical team.
Pulse taken this morning: heart rate 69/min.
Non-smoker.
Keeps a step counter.
Volunteers at a library.
Nails normal.
Vaccinations up to date.
Her aunt completed physical therapy for a shoulder injury.
Uses public transport.
Manual cuff blood pressure today: 138/87 mmHg.
Oxygen saturation by finger probe today: 97%.
Lives on a quiet street.
Her cousin had a splinter removed from a finger.
Plays chess online.
Chloride 103 mmol/L in 2015.
Sodium 140 mmol/L in 2005.
Enjoys gardening.
Writes with the right hand.
Respiratory rate, counted over a full minute today, is 22/min.
Eats a varied diet.
Speaks English and Spanish.
Arterial blood gas this morning: pH 7.42.
Reads most evenings.
Has a pet dog.
Hearing normal to conversation.
Feeds birds in the backyard.


## 4.32 ('two_throat', 'exudate', 'negation', 'easy') templates=test

RULE: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the current temperature is above 38.0 C; the patient currently has tonsillar exudate; the patient currently has tender anterior cervical lymph nodes.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Man of 49 years.
Sore throat for two days.
Tonsils pink and clean on inspection.
Tender, swollen lymph nodes in the front of the neck.
Owns a bicycle.
Current temperature 37.2 C.

FLIP (answer s'): -Tonsils pink and clean on inspection. | +Tonsillar exudate visible on both sides.

NEAR (answer s): -Tonsils pink and clean on inspection. | +Tonsils free of exudate.

MISSING (answer neither (undetermined)): -Tonsils pink and clean on inspection. | +Tonsillar exudate: unknown.

PRES (answer s): full text
Male patient of 49 years.
Sore throat for two days.
Owns a bicycle.
Temperature now 37.2 C (tympanic).
Anterior cervical lymph nodes enlarged and tender to touch.
Tonsils slightly red but clean, without pus.


## 4.33 ('s2_atria_bleed', 'egfr', 'numeric', 'long') templates=train

RULE: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 30 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.
CONDITION: eGFR below 30
CLAIMS: s = 'The eGFR criterion contributes 0 points.' | s' = 'The eGFR criterion contributes 3 points.'

BASE (answer s):
Adult man.
Atrial fibrillation; a decision on warfarin is pending.
Retinal vessels look healthy on fundoscopy.
Grows tomatoes in the garden.
Total bilirubin 0.6 mg/dL in 2005.
Albumin 4.1 g/dL in 2023 (routine blood test).
Sings in a weekly choir.
Listens to podcasts.
Volunteers at a library.
Keeps a step counter.
Keeps houseplants.
Hgb 15.2 g/dL on this morning's blood count.
Uses a smartphone for reminders.
Uses public transport.
Sodium 140 mmol/L in 2011.
Reads most evenings.
Plays chess online.
Age 59 years, calculated today from the date of birth.
Writes with the right hand.
His aunt wears hearing aids.
Drinks plenty of water.
This morning's blood test shows an eGFR of 71 mL/min/1.73 m2.
His neighbor is being treated for eczema.
Feeds birds in the backyard.
Magnesium 2.0 mg/dL in 2023.

FLIP (answer s'): -This morning's blood test shows an eGFR of 71 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 19 mL/min/1.73 m2.

NEAR (answer s): -This morning's blood test shows an eGFR of 71 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 35 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -This morning's blood test shows an eGFR of 71 mL/min/1.73 m2.

PRES (answer s): full text
Male patient.
Atrial fibrillation; a decision on warfarin is pending.
Keeps a step counter.
Sings in a weekly choir.
Albumin 4.1 g/dL in 2023 (routine blood test).
No left ventricular hypertrophy on the echocardiogram.
Magnesium 2.0 mg/dL in 2023.
Listens to podcasts.
Drinks plenty of water.
Reads most evenings.
Sodium 140 mmol/L in 2011.
Hgb at this assessment: 15.2 g/dL.
Plays chess online.
His aunt wears hearing aids.
Uses a smartphone for reminders.
Writes with the right hand.
Age on arrival: 59 years.
Feeds birds in the backyard.
His neighbor is being treated for eczema.
Uses public transport.
Renal function today: eGFR 71 mL/min/1.73 m2.
Grows tomatoes in the garden.
Volunteers at a library.
Keeps houseplants.
Total bilirubin 0.6 mg/dL in 2005.


## 4.34 ('gs078', 'c1', 'subject', 'long') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the patient currently has a venous thromboembolism; the patient currently has a major bleed; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Female patient of 41 years.
Suspected chest infection; assessed on the medical ward.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Her sister has recovered from a dislocated finger.
Coagulation tests normal on recent bloodwork.
Prefers morning appointments.
Has two cats.
Teeth in good repair.
Owns a bicycle.
Sleeps seven hours a night.
Her roommate wears contact lenses.
Climbs two flights of stairs without symptoms.
Her father has a lazy eye.
Free T4 of 1.2 ng/dL in 2024.
During a checkup in 2007, total protein was 7.0 g/dL.
Currently has a major bleed from a duodenal ulcer, with transfusion under way.
Enjoys board games.
Sees a dentist yearly.
Her friend burned a hand on a stove years ago.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Plays the piano.
Lives in a second-floor apartment.
Paints watercolors as a hobby.

FLIP (answer s'): -Coagulation tests normal on recent bloodwork. | +Ongoing treatment for venous thrombosis of the left arm.

NEAR (answer s): -Coagulation tests normal on recent bloodwork. | +Her father is on anticoagulation for venous thrombosis.

MISSING (answer neither (undetermined)): -Coagulation tests normal on recent bloodwork. | +Current venous thromboembolism: status unclear from the records at hand.

PRES (answer s): full text
Woman of 41 years.
Suspected chest infection; assessed on the medical ward.
Owns a bicycle.
Chest pain on exertion: none reported.
During a checkup in 2007, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Her roommate wears contact lenses.
Her friend burned a hand on a stove years ago.
Sees a dentist yearly.
Prefers morning appointments.
Paints watercolors as a hobby.
Sleeps seven hours a night.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Enjoys board games.
Varicose veins: none seen.
Plays the piano.
Teeth in good repair.
Prefers to be addressed by first name.
Has two cats.
Major bleed from the stomach at present, with hemoglobin falling.
Free T4 of 1.2 ng/dL in 2024.
Her sister has recovered from a dislocated finger.
Her father has a lazy eye.


## 4.35 ('gs040', 'c4', 'time', 'long') templates=train

RULE: For rate control in atrial fibrillation, prescribe metoprolol. Score 2 points if the current ALT is above 120 U/L; 3 points if the age of the patient is above 55 years; 3 points if the patient is currently taking aspirin; 1 point if the patient is allergic to penicillin. If the score is 6 or more, prescribe diltiazem instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Sex: female.
Atrial fibrillation with a ventricular rate of 128/min.
Listens to podcasts.
Nails normal.
Enjoys gardening.
Her housemate had a splinter removed from a finger.
Denies any drug allergies.
Her brother-in-law has a chipped front tooth.
Age at this assessment: 85 years.
Watches football on weekends.
Uses a smartphone for reminders.
TSH 1.6 mIU/L in 2013.
Volunteers at a library.
Hearing normal to conversation.
Serum calcium 9.4 mg/dL in 2017.
Drinks two cups of coffee a day.
Lives on a quiet street.
ALT 231 U/L on today's labs.
Feeds birds in the backyard.
Uses reading glasses for small print.
Has a pet dog.

FLIP (answer s'): -Denies any drug allergies. | +Penicillin triggers an allergic reaction with wheezing in this patient.

NEAR (answer s): -Denies any drug allergies. | +Penicillin used to cause hives, but the allergy has resolved.

MISSING (answer neither (undetermined)): -Denies any drug allergies. | +Information on penicillin allergy was not obtained.

PRES (answer s): full text
Adult woman.
Atrial fibrillation with a ventricular rate of 128/min.
Her brother-in-law has a chipped front tooth.
Lives on a quiet street.
Drinks two cups of coffee a day.
Has a pet dog.
TSH 1.6 mIU/L in 2013.
No beta-lactam allergy.
Feeds birds in the backyard.
Volunteers at a library.
Hearing normal to conversation.
Uses a smartphone for reminders.
ALT on blood drawn this morning: 231 U/L.
Watches football on weekends.
Serum calcium 9.4 mg/dL in 2017.
Her housemate had a splinter removed from a finger.
Age 85 years, calculated today from the date of birth.
Uses reading glasses for small print.
Listens to podcasts.
Enjoys gardening.
Nails normal.


## 4.36 ('gs085', 'c2', 'boundary', 'easy') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had asthma (current or past) and the current ALT is above 200 U/L, prescribe fondaparinux instead.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Male patient of 73 years.
First day after elective total hip replacement.
Photographs local wildlife.
Plays the piano.
ALT now 67 U/L.
Persistent asthma, using a rescue inhaler most weeks.
Enjoys board games.
Drives a car.

FLIP (answer s'): -ALT now 67 U/L. | +ALT now 347 U/L.

NEAR (answer s): -ALT now 67 U/L. | +ALT now 200 U/L.

MISSING (answer neither (undetermined)): -ALT now 67 U/L.

PRES (answer s): full text
Man of 73 years.
First day after elective total hip replacement.
Asthma, on a daily inhaled steroid.
Current ALT 67 U/L.
Enjoys board games.
Plays the piano.
Drives a car.
Photographs local wildlife.


## 4.37 ('gs119', 'c1', 'negation', 'long') templates=train

RULE: For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had heart failure (current or past) and the patient is currently taking clarithromycin, prescribe clotrimazole pessaries instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
44-year-old woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Clarithromycin, prescribed last week for whooping cough, is being taken as directed.
Uses a smartphone for reminders.
Keeps houseplants.
Serum calcium 9.4 mg/dL in 2006.
Drinks plenty of water.
Has a pet dog.
Her brother previously wore dental braces.
Total bilirubin 0.6 mg/dL in 2014.
Volunteers at a library.
Enjoys gardening.
Sings in a weekly choir.
Vitamin D 38 ng/mL in 2011 (wellness visit).
Hearing normal to conversation.
Uses reading glasses for small print.
Her brother-in-law has a broken finger in a splint.
Feeds birds in the backyard.
Her mother is being treated for eczema.
Reads most evenings.
Collects postcards.
Albumin 4.1 g/dL in 2012 (routine blood test).
Lives on a quiet street.

FLIP (answer s'): +Chronic heart failure (NYHA class II).

NEAR (answer s): +No heart failure, past or present.

MISSING (answer neither (undetermined)): +Information on heart failure was not obtained.

PRES (answer s): full text
A 44-year-old woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Serum calcium 9.4 mg/dL in 2006.
Her brother previously wore dental braces.
Has a pet dog.
Volunteers at a library.
Albumin 4.1 g/dL in 2012 (routine blood test).
Enjoys gardening.
Her brother-in-law has a broken finger in a splint.
Lives on a quiet street.
Drinks plenty of water.
Hearing normal to conversation.
Collects postcards.
Keeps houseplants.
Uses reading glasses for small print.
Takes clarithromycin 500 mg twice daily.
Sings in a weekly choir.
Total bilirubin 0.6 mg/dL in 2014.
Uses a smartphone for reminders.
Feeds birds in the backyard.
Vitamin D 38 ng/mL in 2011 (wellness visit).
Reads most evenings.
Her mother is being treated for eczema.


## 4.38 ('gs123', 'c2', 'numeric', 'easy') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has a mechanical heart valve; the current calf swelling compared with the other leg is 3.0 cm or more; the current systolic blood pressure is 90 mmHg or less.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Female patient of 24 years.
Requests contraception.
Heart sounds irregular, without a metallic click.
Current systolic blood pressure 79 mmHg.
Current calf swelling 0.8 cm compared with the other leg.
Lives in a second-floor apartment.

FLIP (answer s'): -Current calf swelling 0.8 cm compared with the other leg. | +Current calf swelling 5.3 cm compared with the other leg.

NEAR (answer s): -Current calf swelling 0.8 cm compared with the other leg. | +Current calf swelling 2.6 cm compared with the other leg.

MISSING (answer neither (undetermined)): -Current calf swelling 0.8 cm compared with the other leg.

PRES (answer s): full text
Woman of 24 years.
Requests contraception.
Irregularly irregular pulse; heart sounds free of clicks.
Observations now: blood pressure 79/51 mmHg.
Lives in a second-floor apartment.
Calf swelling now amounts to 0.8 cm of extra girth in the larger calf.


## 4.39 ('gs240', 'c1', 'subject', 'easy') templates=train

RULE: For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.
CONDITION: angioedema
CLAIMS: s = 'Prescribe oral fluconazole.' | s' = 'Prescribe clotrimazole pessaries.'

BASE (answer s):
Female, 27 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drinks two cups of coffee a day.
Mouth and throat look normal; airway clear.
Vaccinations up to date.
Watches football on weekends.

FLIP (answer s'): -Mouth and throat look normal; airway clear. | +Has hereditary angioedema, with attacks every few months.

NEAR (answer s): -Mouth and throat look normal; airway clear. | +Her coworker has swelling of the tongue from angioedema today.

MISSING (answer neither (undetermined)): -Mouth and throat look normal; airway clear. | +Angioedema: not documented in the records available.

PRES (answer s): full text
Patient: female, 27 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Watches football on weekends.
Vaccinations up to date.
Drinks two cups of coffee a day.
Speaks and swallows normally, with no hoarseness.


## 4.40 ('wells_dvt', 'cancer', 'time', 'long') templates=test

RULE: Wells DVT score (as used here, partial): 1 point each for active cancer; a venous thromboembolism of the patient, current or previous; current calf swelling of 3.0 cm or more compared with the other leg. Other Wells items are not part of this question.
CONDITION: active cancer
CLAIMS: s = 'The active cancer criterion contributes 0 points.' | s' = 'The active cancer criterion contributes 1 point.'

BASE (answer s):
Man of 64 years.
Left leg pain for two days after a long-haul flight.
In 2018, lipase was 30 U/L.
Sees a dentist yearly.
His father wears contact lenses.
During a checkup in 2024, total protein was 7.0 g/dL.
Knits as a hobby.
Enjoys board games.
Pupils equal and reactive to light.
Prefers morning appointments.
Drives a car.
His father sprained a thumb last month.
In 2015, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2019.
Sleeps seven hours a night.
Calf swelling now amounts to 0.5 cm of extra girth in the larger calf.
Lives in a second-floor apartment.
Owns a bicycle.

FLIP (answer s'): +Has metastatic lung cancer, receiving palliative treatment.

NEAR (answer s): +Had thyroid cancer years ago and is now cured.

MISSING (answer neither (undetermined)): +Active cancer: unknown.

PRES (answer s): full text
Male patient of 64 years.
Left leg pain for two days after a long-haul flight.
Zinc of 85 mcg/dL in 2019.
Drives a car.
Pupils equal and reactive to light.
Current calf swelling 0.5 cm compared with the other leg.
Sleeps seven hours a night.
Prefers morning appointments.
His father sprained a thumb last month.
Owns a bicycle.
Sees a dentist yearly.
Lives in a second-floor apartment.
In 2018, lipase was 30 U/L.
During a checkup in 2024, total protein was 7.0 g/dL.
In 2015, folate was 12 ng/mL.
Enjoys board games.
His father wears contact lenses.
Knits as a hobby.


## 4.41 ('gs057', 'c1', 'boundary', 'long') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current ALT is above 200 U/L or the patient has an active peptic ulcer, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
45-year-old woman.
Suspected chest infection; assessed on the medical ward.
Enjoys cooking.
Sodium 140 mmol/L in 2024.
Reads most evenings.
Uses reading glasses for small print.
No dyspepsia or melena.
Albumin 4.1 g/dL in 2023 (routine blood test).
Height 170 cm.
Vitamin D 38 ng/mL in 2019 (wellness visit).
Her brother wears hearing aids.
Vaccinations up to date.
Uses public transport.
Her housemate has a stutter.
Keeps houseplants.
Drinks plenty of water.
Her cousin has a fear of heights.
TSH 1.6 mIU/L in 2010.
ALT on blood drawn this morning: 76 U/L.
Speaks English and Spanish.
Drinks alcohol occasionally.

FLIP (answer s'): -ALT on blood drawn this morning: 76 U/L. | +ALT on blood drawn this morning: 449 U/L.

NEAR (answer s): -ALT on blood drawn this morning: 76 U/L. | +ALT on blood drawn this morning: 200 U/L.

MISSING (answer neither (undetermined)): -ALT on blood drawn this morning: 76 U/L.

PRES (answer s): full text
Female, 45 years.
Suspected chest infection; assessed on the medical ward.
Height 170 cm.
Keeps houseplants.
Enjoys cooking.
Uses reading glasses for small print.
Her housemate has a stutter.
Her brother wears hearing aids.
Drinks plenty of water.
Sodium 140 mmol/L in 2024.
Speaks English and Spanish.
TSH 1.6 mIU/L in 2010.
No epigastric pain or heartburn.
Drinks alcohol occasionally.
Liver tests today: ALT 76 U/L.
Vaccinations up to date.
Her cousin has a fear of heights.
Reads most evenings.
Uses public transport.
Albumin 4.1 g/dL in 2023 (routine blood test).
Vitamin D 38 ng/mL in 2019 (wellness visit).


## 4.42 ('gs042', 'c1', 'negation', 'easy') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe warfarin instead.
CONDITION: diabetes in the family
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Male patient of 85 years.
Atrial fibrillation; anticoagulation indicated.
Owns a bicycle.
HbA1c 5.3% at a routine check.
Pupils equal and reactive to light.
Plays the piano.

FLIP (answer s'): -HbA1c 5.3% at a routine check. | +Insulin-treated diabetes.

NEAR (answer s): -HbA1c 5.3% at a routine check. | +Has never had diabetes.

MISSING (answer neither (undetermined)): -HbA1c 5.3% at a routine check. | +Diabetes in the family: unknown.

PRES (answer s): full text
Man of 85 years.
Atrial fibrillation; anticoagulation indicated.
Pupils equal and reactive to light.
Random glucose 92 mg/dL.
Owns a bicycle.
Plays the piano.


## 4.43 ('s2_atria_bleed', 'egfr', 'numeric', 'alt') templates=train

RULE: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 45 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.
CONDITION: eGFR below 45
CLAIMS: s = 'The eGFR criterion contributes 0 points.' | s' = 'The eGFR criterion contributes 3 points.'

BASE (answer s):
Patient: male.
Atrial fibrillation; a decision on warfarin is pending.
Age 61 years, calculated today from the date of birth.
Eats a varied diet.
Sings in a weekly choir.
Hearing normal to conversation.
Blood count today: Hgb 14.8 g/dL.
This morning's blood test shows an eGFR of 68 mL/min/1.73 m2.

FLIP (answer s'): -This morning's blood test shows an eGFR of 68 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 37 mL/min/1.73 m2.

NEAR (answer s): -This morning's blood test shows an eGFR of 68 mL/min/1.73 m2. | +This morning's blood test shows an eGFR of 48 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -This morning's blood test shows an eGFR of 68 mL/min/1.73 m2.

PRES (answer s): full text
Adult man.
Atrial fibrillation; a decision on warfarin is pending.
Eats a varied diet.
Age today: 61 years.
Hgb 14.8 g/dL on this morning's blood count.
Hearing normal to conversation.
eGFR 68 mL/min/1.73 m2 on today's labs.
Sings in a weekly choir.


## 4.44 ('gs061', 'c1', 'subject', 'easy') templates=test

RULE: For acute sore throat, prescribe ibuprofen. If the patient currently has a venous thromboembolism or the patient currently has tonsillar exudate, prescribe penicillin V instead.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Female patient of 46 years.
Sore throat for two days.
Tonsils pink and clean on inspection.
Varicose veins: none seen.
Paints watercolors as a hobby.

FLIP (answer s'): -Varicose veins: none seen. | +Has an acute pulmonary embolism, diagnosed this week.

NEAR (answer s): -Varicose veins: none seen. | +Her uncle is being treated for a pulmonary embolism.

MISSING (answer neither (undetermined)): -Varicose veins: none seen. | +Current venous thromboembolism: unknown.

PRES (answer s): full text
Woman of 46 years.
Sore throat for two days.
Coagulation tests normal on recent bloodwork.
Paints watercolors as a hobby.
Tonsils slightly red but clean, without pus.


## 4.45 ('any_ppx', 'plt', 'time', 'long') templates=train

RULE: For thromboprophylaxis in a medical inpatient, prescribe enoxaparin. If the current platelet count is below 50 x10^9/L or the patient has ever had heparin-induced thrombocytopenia (current or past), prescribe compression stockings instead.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe compression stockings.'

BASE (answer s):
Female, 51 years.
Admitted with a urinary tract infection; mobility reduced.
Drinks alcohol occasionally.
No heparin given so far during this admission.
Has a pet dog.
TSH 1.6 mIU/L in 2006.
Hearing normal to conversation.
Her neighbor is nearsighted.
Total bilirubin 0.6 mg/dL in 2005.
Eats a varied diet.
Sings in a weekly choir.
Non-smoker.
Complete blood count today: platelets 379 x10^9/L.
Drinks two cups of coffee a day.
Ferritin 60 ng/mL in 2020.
Uses reading glasses for small print.
Does crossword puzzles.
Phosphate 3.6 mg/dL in 2005.
Volunteers at a library.
Her brother-in-law has a stutter.
Writes with the right hand.
A routine check in 2006 gave platelet count 172 x10^9/L.

FLIP (answer s'): -Complete blood count today: platelets 379 x10^9/L. | +Complete blood count today: platelets 21 x10^9/L.

NEAR (answer s): -A routine check in 2006 gave platelet count 172 x10^9/L. | +A routine check in 2006 gave platelet count 13 x10^9/L.

MISSING (answer neither (undetermined)): -Complete blood count today: platelets 379 x10^9/L. | -A routine check in 2006 gave platelet count 172 x10^9/L.

PRES (answer s): full text
Patient: female, 51 years.
Admitted with a urinary tract infection; mobility reduced.
Phosphate 3.6 mg/dL in 2005.
No heparin products on the medication chart today.
Platelet count of 172 x10^9/L recorded in 2006.
Does crossword puzzles.
Platelet count today: 379 x10^9/L.
Her neighbor is nearsighted.
Her brother-in-law has a stutter.
Volunteers at a library.
Eats a varied diet.
Uses reading glasses for small print.
Drinks alcohol occasionally.
Drinks two cups of coffee a day.
Ferritin 60 ng/mL in 2020.
Hearing normal to conversation.
Non-smoker.
Total bilirubin 0.6 mg/dL in 2005.
Sings in a weekly choir.
Has a pet dog.
TSH 1.6 mIU/L in 2006.
Writes with the right hand.


## 4.46 ('any_ppx', 'plt', 'boundary', 'long') templates=test

RULE: For thromboprophylaxis in a medical inpatient, prescribe enoxaparin. If the current platelet count is below 50 x10^9/L or the patient has ever had heparin-induced thrombocytopenia (current or past), prescribe compression stockings instead.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe compression stockings.'

BASE (answer s):
Male patient of 77 years.
Admitted with a urinary tract infection; mobility reduced.
Platelet count now 263 x10^9/L.
During a checkup in 2006, free T3 was 3.2 pg/mL.
Uses sunscreen in summer.
Owns a bicycle.
Sees a dentist yearly.
Heparin exposure within the past 100 days: none.
His friend sprained a thumb last month.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2012.
His friend burned a hand on a stove years ago.
His sister wears contact lenses.
Knits as a hobby.
Sleeps seven hours a night.
His sister lives with psoriasis.
Plays the piano.
Enjoys board games.
Drives a car.

FLIP (answer s'): -Platelet count now 263 x10^9/L. | +Platelet count now 35 x10^9/L.

NEAR (answer s): -Platelet count now 263 x10^9/L. | +Platelet count now 50 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count now 263 x10^9/L.

PRES (answer s): full text
Man of 77 years.
Admitted with a urinary tract infection; mobility reduced.
Drives a car.
Sees a dentist yearly.
His sister wears contact lenses.
Uses sunscreen in summer.
His sister lives with psoriasis.
During a checkup in 2006, free T3 was 3.2 pg/mL.
His friend burned a hand on a stove years ago.
Knits as a hobby.
Current platelet count 263 x10^9/L.
His friend sprained a thumb last month.
Last received heparin more than a year ago.
Owns a bicycle.
Enjoys board games.
Plays the piano.
Sleeps seven hours a night.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2012.


## 4.47 ('gs098', 'c2', 'negation', 'long') templates=train

RULE: For an acute gout flare, prescribe colchicine. Score 3 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 1 point if the patient is currently taking warfarin; 2 points if the patient currently has heart failure. If the score is 4 or more, prescribe prednisone instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe colchicine.' | s' = 'Prescribe prednisone.'

BASE (answer s):
75-year-old woman.
Acute gout flare of the right first metatarsophalangeal joint.
Her partner is being treated for eczema.
Collects postcards.
Non-smoker.
Lives on a quiet street.
Peripheral artery disease with calf claudication.
Reads most evenings.
Grows tomatoes in the garden.
Feeds birds in the backyard.
No INR monitoring in place.
Has a pet dog.
Watches football on weekends.
Bicarbonate 26 mmol/L in 2013 (annual physical).
Height 170 cm.
Bakes bread at home.
Her brother had a splinter removed from a finger.
Uses a smartphone for reminders.
Wears a seat belt when driving.
Enjoys gardening.
TSH 1.6 mIU/L in 2016.

FLIP (answer s'): -No INR monitoring in place. | +Medications: warfarin 5 mg once daily.

NEAR (answer s): -No INR monitoring in place. | +Not on warfarin.

MISSING (answer neither (undetermined)): -No INR monitoring in place. | +Information on warfarin was not obtained.

PRES (answer s): full text
Female, 75 years.
Acute gout flare of the right first metatarsophalangeal joint.
Grows tomatoes in the garden.
Reads most evenings.
Wears a seat belt when driving.
TSH 1.6 mIU/L in 2016.
Her partner is being treated for eczema.
Peripheral artery disease, on cilostazol for pain on walking.
Feeds birds in the backyard.
Non-smoker.
Bakes bread at home.
Height 170 cm.
Not taking any anticoagulants.
Lives on a quiet street.
Bicarbonate 26 mmol/L in 2013 (annual physical).
Her brother had a splinter removed from a finger.
Has a pet dog.
Collects postcards.
Watches football on weekends.
Uses a smartphone for reminders.
Enjoys gardening.


## 4.48 ('gs189', 'c1', 'numeric', 'long') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the current oxygen saturation is 91% or less, prescribe sitagliptin instead.
CONDITION: oxygen saturation at or below 91
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Man of 49 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
In 2022, folate was 12 ng/mL.
Paints watercolors as a hobby.
Enjoys board games.
His uncle wears contact lenses.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Has two cats.
Sleeps seven hours a night.
Current oxygen saturation 100%.
His wife has recovered from a dislocated finger.
During a checkup in 2023, total protein was 7.0 g/dL.
Prefers morning appointments.
Sees a dentist yearly.
His sister has a lazy eye.
Teeth in good repair.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2014.
Drives a car.
Prefers to be addressed by first name.

FLIP (answer s'): -Current oxygen saturation 100%. | +Current oxygen saturation 91%.

NEAR (answer s): -Current oxygen saturation 100%. | +Current oxygen saturation 92%.

MISSING (answer neither (undetermined)): -Current oxygen saturation 100%.

PRES (answer s): full text
Male patient of 49 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
His wife has recovered from a dislocated finger.
Enjoys board games.
Uses sunscreen in summer.
His sister has a lazy eye.
Drives a car.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
During a checkup in 2023, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Teeth in good repair.
Pupils equal and reactive to light.
Latest oxygen saturation reading: 100%.
His uncle wears contact lenses.
In 2022, folate was 12 ng/mL.
Has two cats.
Zinc of 85 mcg/dL in 2014.


## 4.49 ('gs207', 'c1', 'subject', 'easy') templates=train

RULE: For primary prevention, prescribe atorvastatin. If the patient currently has a major bleed and the current systolic blood pressure is 220 mmHg or more, prescribe ezetimibe instead.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
63-year-old woman.
Primary prevention; LDL cholesterol 182 mg/dL.
No melena or hematemesis.
Lives on a quiet street.
Has a pet dog.
Does crossword puzzles.
Blood pressure 231/143 mmHg this morning.

FLIP (answer s'): -No melena or hematemesis. | +Ongoing major bleeding from the lower bowel, receiving blood transfusion.

NEAR (answer s): -No melena or hematemesis. | +Her brother is hospitalized with a major gastrointestinal bleed.

MISSING (answer neither (undetermined)): -No melena or hematemesis. | +Active major bleeding: not recorded.

PRES (answer s): full text
Female, 63 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Does crossword puzzles.
Lives on a quiet street.
Has a pet dog.
Manual cuff blood pressure today: 231/143 mmHg.
Hemoglobin normal on today's blood count.


## 4.50 ('gs130', 'c2', 'time', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient is allergic to penicillin, prescribe naproxen with omeprazole instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Woman of 49 years.
Hip osteoarthritis with pain on walking.
Prefers to be addressed by first name.
Reports no allergies to medicines.
Formerly had colon cancer; recovered fully after an operation in 2006.
Plays the piano.
Enjoys board games.
Owns a bicycle.

FLIP (answer s'): -Reports no allergies to medicines. | +Known penicillin allergy with angioedema.

NEAR (answer s): -Reports no allergies to medicines. | +Outgrew a penicillin allergy by 2007.

MISSING (answer neither (undetermined)): -Reports no allergies to medicines. | +Penicillin allergy: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 49 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Plays the piano.
Owns a bicycle.
Formerly had colon cancer; recovered fully after an operation in 2006.
Prefers to be addressed by first name.
Drug allergies: none known.


## 4.51 ('gs000', 'c2', 'boundary', 'easy') templates=train

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. Score 2 points if the patient is allergic to penicillin; 2 points if the current white cell count is below 4.0 x10^9/L; 3 points if the patient has ever had asthma (current or past). If the score is 4 or more, prescribe intermittent pneumatic compression instead.
CONDITION: white cell count below 4.0
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Patient: male, 57 years.
Admitted for community-acquired pneumonia; immobile.
Good air entry on both sides of the chest.
Nails normal.
Keeps a step counter.
Allergic to penicillin (urticaria).
Complete blood count this morning: white cell count 5.9 x10^9/L.

FLIP (answer s'): -Complete blood count this morning: white cell count 5.9 x10^9/L. | +Complete blood count this morning: white cell count 2.6 x10^9/L.

NEAR (answer s): -Complete blood count this morning: white cell count 5.9 x10^9/L. | +Complete blood count this morning: white cell count 4.0 x10^9/L.

MISSING (answer neither (undetermined)): -Complete blood count this morning: white cell count 5.9 x10^9/L.

PRES (answer s): full text
A 57-year-old man.
Admitted for community-acquired pneumonia; immobile.
White cell count today: 5.9 x10^9/L.
Keeps a step counter.
Reports an allergy to penicillin that causes hives.
Nails normal.
No night cough or chest tightness.


## 4.52 ('gs099', 'c2', 'negation', 'easy') templates=test

RULE: For acute sore throat, prescribe ibuprofen. If the current serum creatinine is 1.5 mg/dL or more or the patient has ever had heart failure (current or past), prescribe penicillin V instead.
CONDITION: heart failure
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Female patient of 57 years.
Sore throat for two days.
Teeth in good repair.
Pupils equal and reactive to light.
Plays the piano.
Prefers to be addressed by first name.
Current serum creatinine 1.0 mg/dL.
Heart sounds without a gallop.

FLIP (answer s'): -Heart sounds without a gallop. | +Current heart failure with ankle swelling.

NEAR (answer s): -Heart sounds without a gallop. | +Heart failure: never diagnosed.

MISSING (answer neither (undetermined)): -Heart sounds without a gallop. | +Heart failure: status unclear from the records at hand.

PRES (answer s): full text
Woman of 57 years.
Sore throat for two days.
Prefers to be addressed by first name.
Plays the piano.
Latest creatinine result: 1.0 mg/dL.
Teeth in good repair.
Pupils equal and reactive to light.
Sleeps flat on one pillow.


## 4.53 ('s2_hemorr2hages', 'age', 'numeric', 'long') templates=train

RULE: HEMORR2HAGES score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for active cancer, a current age above 75 years, and current use of aspirin. Other HEMORR2HAGES items are not part of this question.
CONDITION: age above 75
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Adult woman.
Atrial fibrillation; warfarin therapy under consideration.
Wears a seat belt when driving.
Drinks two cups of coffee a day.
Hemoglobin normal on today's blood count.
Eats a varied diet.
Chloride 103 mmol/L in 2009.
Bakes bread at home.
Lives on a quiet street.
Speaks English and Spanish.
Her coworker has a stutter.
Writes with the right hand.
Feeds birds in the backyard.
Sodium 140 mmol/L in 2024.
Enjoys cooking.
Uses a smartphone for reminders.
Plays chess online.
Drinks alcohol occasionally.
Has a pet dog.
No platelet-inhibiting drugs on the medication list.
Her husband previously wore dental braces.
Uses public transport.
Hearing normal to conversation.
Age today: 64 years.

FLIP (answer s'): -Age today: 64 years. | +Age today: 77 years.

NEAR (answer s): -Age today: 64 years. | +Age today: 72 years.

MISSING (answer neither (undetermined)): -Age today: 64 years.

PRES (answer s): full text
Sex: female.
Atrial fibrillation; warfarin therapy under consideration.
Hearing normal to conversation.
Not on any antiplatelet medication.
Plays chess online.
Has a pet dog.
Chloride 103 mmol/L in 2009.
Age 64 years, calculated today from the date of birth.
Uses a smartphone for reminders.
Uses public transport.
Wears a seat belt when driving.
Drinks two cups of coffee a day.
Her husband previously wore dental braces.
Speaks English and Spanish.
Sodium 140 mmol/L in 2024.
Her coworker has a stutter.
Eats a varied diet.
Writes with the right hand.
Drinks alcohol occasionally.
Lives on a quiet street.
Enjoys cooking.
Feeds birds in the backyard.
Conjunctivae pink, with no pallor.
Bakes bread at home.


## 4.54 ('gs050', 'c2', 'subject', 'long') templates=test

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a peptic ulcer (current or past) or the patient is allergic to penicillin, prescribe fondaparinux instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Male patient of 69 years.
First day after elective total hip replacement.
His friend wears contact lenses.
Zinc of 85 mcg/dL in 2023.
Photographs local wildlife.
Owns a bicycle.
His friend has recovered from a dislocated finger.
Free T4 of 1.2 ng/dL in 2011.
Prefers morning appointments.
Sees a dentist yearly.
His roommate has a lazy eye.
Appetite good; no indigestion.
Drives a car.
During a checkup in 2011, free T3 was 3.2 pg/mL.
Drug allergies: none known.
Sleeps seven hours a night.
His wife burned a hand on a stove years ago.
Prefers to be addressed by first name.
Plays the piano.

FLIP (answer s'): -Drug allergies: none known. | +Penicillin allergy: anaphylaxis.

NEAR (answer s): -Drug allergies: none known. | +His sister cannot take penicillin because of an allergy.

MISSING (answer neither (undetermined)): -Drug allergies: none known. | +Penicillin allergy: unknown.

PRES (answer s): full text
Man of 69 years.
First day after elective total hip replacement.
His wife burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2023.
Plays the piano.
His roommate has a lazy eye.
Drives a car.
Free T4 of 1.2 ng/dL in 2011.
Prefers morning appointments.
His friend wears contact lenses.
Abdomen soft and non-tender.
During a checkup in 2011, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Owns a bicycle.
His friend has recovered from a dislocated finger.
Sleeps seven hours a night.
Sees a dentist yearly.
Photographs local wildlife.
Reports no allergies to medicines.


## 4.55 ('gs194', 'c1', 'time', 'easy') templates=train

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the current white cell count is below 4.0 x10^9/L or the patient is currently taking clarithromycin, prescribe sitagliptin instead.
CONDITION: white cell count below 4.0
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Patient: male, 61 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Does crossword puzzles.
A routine check in 2018 gave white cell count 8.8 x10^9/L.
Vaccinations up to date.
WBC 5.2 x10^9/L on today's sample.

FLIP (answer s'): -WBC 5.2 x10^9/L on today's sample. | +WBC 2.6 x10^9/L on today's sample.

NEAR (answer s): -A routine check in 2018 gave white cell count 8.8 x10^9/L. | +A routine check in 2018 gave white cell count 2.9 x10^9/L.

MISSING (answer neither (undetermined)): -A routine check in 2018 gave white cell count 8.8 x10^9/L. | -WBC 5.2 x10^9/L on today's sample.

PRES (answer s): full text
A 61-year-old man.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Vaccinations up to date.
Does crossword puzzles.
White cell count 8.8 x10^9/L at a clinic visit in 2018.
Complete blood count this morning: white cell count 5.2 x10^9/L.


## 4.56 ('gs150', 'c1', 'boundary', 'long') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. If the current ALT is above 120 U/L or the patient currently has heart failure, prescribe a progestin-only pill instead.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Woman of 31 years.
Requests contraception.
Drives a car.
Free T4 of 1.2 ng/dL in 2016.
Has two cats.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Teeth in good repair.
Her wife has a lazy eye.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Owns a bicycle.
Her wife lives with psoriasis.
Sleeps flat on one pillow.
Photographs local wildlife.
Enjoys board games.
During a checkup in 2023, total protein was 7.0 g/dL.
ALT now 44 U/L.
Plays the piano.
Zinc of 85 mcg/dL in 2019.
Her roommate wears contact lenses.

FLIP (answer s'): -ALT now 44 U/L. | +ALT now 160 U/L.

NEAR (answer s): -ALT now 44 U/L. | +ALT now 120 U/L.

MISSING (answer neither (undetermined)): -ALT now 44 U/L.

PRES (answer s): full text
Female patient of 31 years.
Requests contraception.
Zinc of 85 mcg/dL in 2019.
Pupils equal and reactive to light.
Drives a car.
Her wife has a lazy eye.
Owns a bicycle.
Paints watercolors as a hobby.
Her wife lives with psoriasis.
During a checkup in 2023, total protein was 7.0 g/dL.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2016.
Photographs local wildlife.
Plays the piano.
Current ALT 44 U/L.
Has two cats.
Heart sounds without a gallop.
Lives in a second-floor apartment.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Enjoys board games.
Her roommate wears contact lenses.


## 4.57 ('gs094', 'c4', 'negation', 'long') templates=train

RULE: For cellulitis of the lower leg, prescribe cephalexin. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 1 point if the age of the patient is 65 years or more; 3 points if the current serum potassium is above 4.5 mmol/L; 1 point if the patient is allergic to penicillin. If the score is 7 or more, prescribe clindamycin instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe cephalexin.' | s' = 'Prescribe clindamycin.'

BASE (answer s):
Patient: female.
Spreading redness and warmth of the right shin for two days.
No beta-lactam allergy.
Her coworker has a fear of heights.
Nails normal.
Magnesium 2.0 mg/dL in 2020.
Potassium 4.9 mmol/L on today's blood work.
Has a pet dog.
Drinks alcohol occasionally.
Her partner is left-handed.
Writes with the right hand.
Her cousin has a broken finger in a splint.
Non-smoker.
Speaks English and Spanish.
Sodium 140 mmol/L in 2017.
Her coworker broke a wrist, which has healed.
Age on arrival: 77 years.
Lives on a quiet street.
Reads most evenings.
Grows tomatoes in the garden.
Vitamin B12 450 pg/mL in 2024.
Sings in a weekly choir.
Feeds birds in the backyard.
Wears a seat belt when driving.
Previously had type 2 diabetes (2013); resolved after bariatric surgery.

FLIP (answer s'): -No beta-lactam allergy. | +Allergic to penicillin (urticaria).

NEAR (answer s): -No beta-lactam allergy. | +No penicillin allergy.

MISSING (answer neither (undetermined)): -No beta-lactam allergy. | +Information on penicillin allergy was not obtained.

PRES (answer s): full text
Sex: female.
Spreading redness and warmth of the right shin for two days.
Writes with the right hand.
Her cousin has a broken finger in a splint.
Grows tomatoes in the garden.
Has a pet dog.
Vitamin B12 450 pg/mL in 2024.
Wears a seat belt when driving.
Reads most evenings.
Her coworker broke a wrist, which has healed.
Lives on a quiet street.
No known drug allergies.
Age 77 years, calculated today from the date of birth.
Steroid-induced diabetes in 2013, resolved once the steroids were stopped.
Non-smoker.
Her coworker has a fear of heights.
Feeds birds in the backyard.
Sings in a weekly choir.
Speaks English and Spanish.
Serum potassium today: 4.9 mmol/L.
Magnesium 2.0 mg/dL in 2020.
Drinks alcohol occasionally.
Her partner is left-handed.
Sodium 140 mmol/L in 2017.
Nails normal.


## 4.58 ('s1_idsa_minor', 'temp', 'numeric', 'easy') templates=test

RULE: IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): 1 point each for a current white cell count below 4.0 x10^9/L; a current platelet count below 100 x10^9/L; a current temperature below 36.0 C; a current blood urea nitrogen of 20 mg/dL or more. Other criteria are not part of this question.
CONDITION: temperature below 36.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
Man of 45 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Latest WBC is 7.4 x10^9/L.
Blood urea nitrogen 10 mg/dL on the current labs.
Photographs local wildlife.
Temperature now 36.8 C (tympanic).
Platelet count now 358 x10^9/L.

FLIP (answer s'): -Temperature now 36.8 C (tympanic). | +Temperature now 35.2 C (tympanic).

NEAR (answer s): -Temperature now 36.8 C (tympanic). | +Temperature now 36.1 C (tympanic).

MISSING (answer neither (undetermined)): -Temperature now 36.8 C (tympanic).

PRES (answer s): full text
Male patient of 45 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Current platelet count 358 x10^9/L.
Photographs local wildlife.
Blood urea nitrogen now: 10 mg/dL.
Current white cell count 7.4 x10^9/L.
Current temperature 36.8 C.


## 4.59 ('gs117', 'c2', 'subject', 'long') templates=train

RULE: For acute migraine, prescribe sumatriptan. If at least two of the following apply, prescribe naproxen instead: the current calf swelling compared with the other leg is 3.0 cm or more; the patient has active cancer; the patient has ever had heart failure (current or past).
CONDITION: active cancer
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
Male, 48 years.
Acute migraine without aura, typical of prior attacks.
Collects postcards.
Reads most evenings.
Keeps a step counter.
His mother is nearsighted.
His husband has a stutter.
Phosphate 3.6 mg/dL in 2022.
No evidence of active neoplasia.
His housemate had a splinter removed from a finger.
His neighbor is being treated for eczema.
Vaccinations up to date.
Chloride 103 mmol/L in 2017.
Enjoys cooking.
Eats a varied diet.
Hearing normal to conversation.
Difference in calf circumference today, side to side: 4.5 cm.
Enjoys gardening.
Drinks plenty of water.
Nails normal.
Vitamin B12 450 pg/mL in 2011.

FLIP (answer s'): -No evidence of active neoplasia. | +Active colon cancer under oncology treatment.

NEAR (answer s): -No evidence of active neoplasia. | +His brother-in-law has active colon cancer.

MISSING (answer neither (undetermined)): -No evidence of active neoplasia. | +Active cancer: not documented in the records available.

PRES (answer s): full text
A 48-year-old man.
Acute migraine without aura, typical of prior attacks.
No unexplained weight loss or new lumps.
Nails normal.
His mother is nearsighted.
Keeps a step counter.
Vitamin B12 450 pg/mL in 2011.
Chloride 103 mmol/L in 2017.
Reads most evenings.
His husband has a stutter.
Eats a varied diet.
Collects postcards.
His housemate had a splinter removed from a finger.
Vaccinations up to date.
Enjoys gardening.
His neighbor is being treated for eczema.
Phosphate 3.6 mg/dL in 2022.
Calf circumference measured this morning is 4.5 cm greater on one side.
Hearing normal to conversation.
Drinks plenty of water.
Enjoys cooking.


## 4.60 ('gs196', 'c2', 'time', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient currently has tonsillar exudate or the patient currently has tender anterior cervical lymph nodes, prescribe acetaminophen instead.
CONDITION: tender cervical lymph nodes
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Male patient of 53 years.
Acute low back pain after lifting.
Paints watercolors as a hobby.
Free T4 of 1.2 ng/dL in 2007.
Owns a bicycle.
Has two cats.
Teeth in good repair.
Lives in a second-floor apartment.
In 2014, lipase was 30 U/L.
Photographs local wildlife.
Drives a car.
His uncle wears contact lenses.
His wife lives with psoriasis.
His friend sprained a thumb last month.
Neck palpation unremarkable.
Prefers to be addressed by first name.
Prefers morning appointments.
Sees a dentist yearly.
Knits as a hobby.
Tonsils pink and clean on inspection.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.

FLIP (answer s'): -Neck palpation unremarkable. | +Tender, swollen lymph nodes in the front of the neck.

NEAR (answer s): -Neck palpation unremarkable. | +Formerly had tender anterior cervical lymphadenopathy in 2016, with full recovery.

MISSING (answer neither (undetermined)): -Neck palpation unremarkable. | +Tender cervical lymph nodes: unknown.

PRES (answer s): full text
Man of 53 years.
Acute low back pain after lifting.
Front of the neck without tenderness or swelling.
Prefers morning appointments.
Paints watercolors as a hobby.
His friend sprained a thumb last month.
His wife lives with psoriasis.
Sees a dentist yearly.
In 2014, lipase was 30 U/L.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Knits as a hobby.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Has two cats.
His uncle wears contact lenses.
Tonsils slightly red but clean, without pus.
Drives a car.
Photographs local wildlife.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2007.
Lives in a second-floor apartment.
Owns a bicycle.


## 4.61 ('all_spiro', 'egfr', 'boundary', 'long') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone 25 mg daily. If the current serum potassium is above 4.8 mmol/L and the current eGFR is below 50 mL/min/1.73 m2, prescribe spironolactone 12.5 mg daily instead.
CONDITION: eGFR below 50
CLAIMS: s = 'Prescribe spironolactone 25 mg daily.' | s' = 'Prescribe spironolactone 12.5 mg daily.'

BASE (answer s):
Female, 65 years.
Heart failure with reduced ejection fraction (ejection fraction 32%).
Phosphate 3.6 mg/dL in 2021.
Grows tomatoes in the garden.
Writes with the right hand.
Feeds birds in the backyard.
Bakes bread at home.
Speaks English and Spanish.
Uses reading glasses for small print.
eGFR today: 66 mL/min/1.73 m2.
Serum potassium today: 5.2 mmol/L.
TSH 1.6 mIU/L in 2012.
Uses a smartphone for reminders.
Her neighbor completed physical therapy for a shoulder injury.
Drinks plenty of water.
Collects postcards.
Total bilirubin 0.6 mg/dL in 2010.
Listens to podcasts.
Enjoys cooking.
Her cousin is being treated for eczema.
Keeps a step counter.

FLIP (answer s'): -eGFR today: 66 mL/min/1.73 m2. | +eGFR today: 42 mL/min/1.73 m2.

NEAR (answer s): -eGFR today: 66 mL/min/1.73 m2. | +eGFR today: 50 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -eGFR today: 66 mL/min/1.73 m2.

PRES (answer s): full text
65-year-old woman.
Heart failure with reduced ejection fraction (ejection fraction 32%).
Uses a smartphone for reminders.
Enjoys cooking.
Writes with the right hand.
Her neighbor completed physical therapy for a shoulder injury.
Renal function today: eGFR 66 mL/min/1.73 m2.
Bakes bread at home.
Feeds birds in the backyard.
Grows tomatoes in the garden.
Her cousin is being treated for eczema.
Total bilirubin 0.6 mg/dL in 2010.
Potassium measured at this assessment is 5.2 mmol/L.
Listens to podcasts.
Phosphate 3.6 mg/dL in 2021.
Uses reading glasses for small print.
Keeps a step counter.
TSH 1.6 mIU/L in 2012.
Collects postcards.
Speaks English and Spanish.
Drinks plenty of water.


## 4.62 ('gs224', 'c1', 'negation', 'long') templates=test

RULE: For knee osteoarthritis pain, prescribe naproxen. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time or the current platelet count is 350 x10^9/L or more, prescribe acetaminophen instead.
CONDITION: venous thromboembolism in the family
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Male patient of 85 years.
Knee osteoarthritis with pain on walking.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Drives a car.
Paints watercolors as a hobby.
His friend burned a hand on a stove years ago.
In 2015, folate was 12 ng/mL.
Has two cats.
Sees a dentist yearly.
His wife sprained a thumb last month.
Coagulation tests normal on recent bloodwork.
Knits as a hobby.
Zinc of 85 mcg/dL in 2007.
Free T4 of 1.2 ng/dL in 2020.
Plays the piano.
Platelet count now 242 x10^9/L.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
His sister has a lazy eye.
Uses sunscreen in summer.
Prefers to be addressed by first name.

FLIP (answer s'): -Coagulation tests normal on recent bloodwork. | +Pulmonary embolism years ago, treated for six months.

NEAR (answer s): -Coagulation tests normal on recent bloodwork. | +Has never had a DVT or pulmonary embolism, nor has any parent or sibling.

MISSING (answer neither (undetermined)): -Coagulation tests normal on recent bloodwork. | +Venous thromboembolism in the family: unknown.

PRES (answer s): full text
Man of 85 years.
Knee osteoarthritis with pain on walking.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Plays the piano.
Enjoys board games.
Zinc of 85 mcg/dL in 2007.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
Teeth in good repair.
Has two cats.
Varicose veins: none seen.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2020.
Lives in a second-floor apartment.
His sister has a lazy eye.
His wife sprained a thumb last month.
His friend burned a hand on a stove years ago.
In 2015, folate was 12 ng/mL.
Knits as a hobby.
Current platelet count 242 x10^9/L.
Drives a car.


## 4.63 ('s1_psi', 'ph', 'numeric', 'easy') templates=train

RULE: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 30 mg/dL or more. Age, sex and other items of the index are not part of this question.
CONDITION: arterial pH below 7.35
CLAIMS: s = 'The arterial pH criterion contributes 0 points.' | s' = 'The arterial pH criterion contributes 30 points.'

BASE (answer s):
68-year-old woman.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Uses a smartphone for reminders.
Arterial blood gas this morning: pH 7.39.
No evidence of active neoplasia.
BUN at this assessment: 18 mg/dL.
Recent echocardiogram normal.
Reads most evenings.
Visual fields full to confrontation.

FLIP (answer s'): -Arterial blood gas this morning: pH 7.39. | +Arterial blood gas this morning: pH 7.21.

NEAR (answer s): -Arterial blood gas this morning: pH 7.39. | +Arterial blood gas this morning: pH 7.37.

MISSING (answer neither (undetermined)): -Arterial blood gas this morning: pH 7.39.

PRES (answer s): full text
Patient: female, 68 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Jugular venous pressure not raised.
Not undergoing chemotherapy or radiotherapy.
Cranial nerves intact.
Reads most evenings.
BUN 18 mg/dL this morning.
Uses a smartphone for reminders.
Arterial pH today: 7.39.


## 4.64 ('gs235', 'c4', 'subject', 'easy') templates=test

RULE: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient has ever had diabetes (current or past); 3 points if the patient has new confusion; 2 points if the patient is allergic to penicillin; 2 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time. If the score is 6 or more, prescribe a progestin-only pill instead.
CONDITION: colorectal cancer
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
Woman of 19 years.
Requests contraception.
Sees a dentist yearly.
Hemoglobin within the normal range on recent blood tests.
Owns a bicycle.
Reports no allergies to medicines.
Disoriented to time and place, which is new for the patient.
Has type 2 diabetes on metformin.

FLIP (answer s'): -Hemoglobin within the normal range on recent blood tests. | +Colorectal cancer under active treatment.

NEAR (answer s): -Hemoglobin within the normal range on recent blood tests. | +Her roommate has advanced colorectal cancer.

MISSING (answer neither (undetermined)): -Hemoglobin within the normal range on recent blood tests. | +Colorectal cancer: unknown.

PRES (answer s): full text
Female patient of 19 years.
Requests contraception.
Sees a dentist yearly.
Owns a bicycle.
Drug allergies: none known.
Rectal exam unremarkable.
Newly disoriented and unable to give a clear history.
Insulin-treated diabetes.


## 4.65 ('gs008', 'c1', 'time', 'superseded') templates=train

RULE: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current systolic blood pressure is 90 mmHg or less and the patient currently has a major bleed, prescribe nitrofurantoin instead.
CONDITION: systolic blood pressure at or below 90
CLAIMS: s = 'Prescribe trimethoprim-sulfamethoxazole.' | s' = 'Prescribe nitrofurantoin.'

BASE (answer s):
60-year-old woman.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Grows tomatoes in the garden.
Nails normal.
Plays chess online.
Systolic blood pressure of 141 mmHg measured yesterday was replaced by a repeat measurement.
Manual cuff blood pressure today: 126/80 mmHg.
Height 170 cm.
Ongoing major bleeding from the lower bowel, receiving blood transfusion.

FLIP (answer s'): -Manual cuff blood pressure today: 126/80 mmHg. | +Manual cuff blood pressure today: 73/48 mmHg.

NEAR (answer s): -Systolic blood pressure of 141 mmHg measured yesterday was replaced by a repeat measurement. | +Systolic blood pressure of 79 mmHg measured yesterday was replaced by a repeat measurement.

MISSING (answer neither (undetermined)): -Systolic blood pressure of 141 mmHg measured yesterday was replaced by a repeat measurement. | -Manual cuff blood pressure today: 126/80 mmHg.

PRES (answer s): full text
Patient: female, 60 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Nails normal.
Systolic blood pressure 126 mmHg at this assessment.
Height 170 cm.
Major retroperitoneal bleed seen on a CT scan this morning, needing urgent treatment.
Systolic blood pressure was 141 mmHg yesterday, before today's repeat.
Grows tomatoes in the garden.
Plays chess online.


## 4.66 ('s2_timi_stemi', 'hr', 'boundary', 'long') templates=test

RULE: TIMI risk score for ST-elevation myocardial infarction (as used here, partial): 3 points for a current systolic blood pressure below 100 mmHg; 2 points for a current heart rate above 100/min; 1 point each for a current weight below 67 kg and hypertension at any time. Other TIMI items, including age, are not part of this question.
CONDITION: heart rate above 100
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 2 points.'

BASE (answer s):
Woman of 50 years.
Admitted with an acute ST-elevation myocardial infarction.
Drives a car.
Has two cats.
In 2022, lipase was 30 U/L.
Her friend has recovered from a dislocated finger.
Prefers morning appointments.
Her sister burned a hand on a stove years ago.
Lives in a second-floor apartment.
Photographs local wildlife.
Her friend has a lazy eye.
Sleeps seven hours a night.
Current systolic blood pressure 113 mmHg.
Uses sunscreen in summer.
Current heart rate 92/min.
Her uncle wears contact lenses.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2008.
Knits as a hobby.
Current weight 73 kg.
Enjoys board games.

FLIP (answer s'): -Current heart rate 92/min. | +Current heart rate 135/min.

NEAR (answer s): -Current heart rate 92/min. | +Current heart rate 100/min.

MISSING (answer neither (undetermined)): -Current heart rate 92/min.

PRES (answer s): full text
Female patient of 50 years.
Admitted with an acute ST-elevation myocardial infarction.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2008.
Her friend has a lazy eye.
Has two cats.
Drives a car.
Sleeps seven hours a night.
Knits as a hobby.
Enjoys board games.
Her sister burned a hand on a stove years ago.
In 2022, lipase was 30 U/L.
Prefers morning appointments.
Heart rate now 92/min on the monitor.
Latest weight 73 kg.
Her uncle wears contact lenses.
Observations now: blood pressure 113/72 mmHg.
Uses sunscreen in summer.
Her friend has recovered from a dislocated finger.
Photographs local wildlife.
Prefers to be addressed by first name.
Paints watercolors as a hobby.


## 4.67 ('pain_ulcer', 'ulcer', 'negation', 'long') templates=train

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient has an active peptic ulcer, prescribe acetaminophen instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
34-year-old woman.
Acute low back pain after lifting.
Total bilirubin 0.6 mg/dL in 2016.
Nails normal.
Her grandfather wears hearing aids.
Hearing normal to conversation.
Sings in a weekly choir.
Keeps a step counter.
Height 170 cm.
Drinks two cups of coffee a day.
Chloride 103 mmol/L in 2021.
Her brother-in-law has a broken finger in a splint.
Bakes bread at home.
Watches football on weekends.
Uses reading glasses for small print.
No epigastric pain or heartburn.
Has a pet dog.
Does crossword puzzles.
Non-smoker.
Her housemate is being treated for eczema.

FLIP (answer s'): -No epigastric pain or heartburn. | +Bleeding gastric ulcer under active treatment.

NEAR (answer s): -No epigastric pain or heartburn. | +No peptic ulcer, either active or healed.

MISSING (answer neither (undetermined)): -No epigastric pain or heartburn. | +Active peptic ulcer: not documented in the records available.

PRES (answer s): full text
Patient: female, 34 years.
Acute low back pain after lifting.
Keeps a step counter.
Her brother-in-law has a broken finger in a splint.
Nails normal.
Has a pet dog.
Bakes bread at home.
Hearing normal to conversation.
Chloride 103 mmol/L in 2021.
Her grandfather wears hearing aids.
Drinks two cups of coffee a day.
Her housemate is being treated for eczema.
Height 170 cm.
Non-smoker.
Does crossword puzzles.
Total bilirubin 0.6 mg/dL in 2016.
No black or bloody stools.
Watches football on weekends.
Sings in a weekly choir.
Uses reading glasses for small print.


## 4.68 ('news2_red', 'sbp', 'numeric', 'long') templates=test

RULE: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.
CONDITION: systolic blood pressure at or below 90
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 3 points.'

BASE (answer s):
Woman of 48 years.
Shortness of breath and fever; assessed on the medical ward.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Latest oxygen saturation reading: 96%.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2010.
Drives a car.
Observations now: respiratory rate 17/min.
During a checkup in 2008, free T3 was 3.2 pg/mL.
In 2023, folate was 12 ng/mL.
Her roommate has a lazy eye.
Has two cats.
Speech clear; follows commands.
Prefers to be addressed by first name.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2008.
Paints watercolors as a hobby.
Her sister burned a hand on a stove years ago.
Prefers morning appointments.
Knits as a hobby.
Photographs local wildlife.
Enjoys board games.
Current systolic blood pressure 117 mmHg.
Plays the piano.
Uses sunscreen in summer.

FLIP (answer s'): -Current systolic blood pressure 117 mmHg. | +Current systolic blood pressure 83 mmHg.

NEAR (answer s): -Current systolic blood pressure 117 mmHg. | +Current systolic blood pressure 91 mmHg.

MISSING (answer neither (undetermined)): -Current systolic blood pressure 117 mmHg.

PRES (answer s): full text
Female patient of 48 years.
Shortness of breath and fever; assessed on the medical ward.
Current oxygen saturation 96%.
Zinc of 85 mcg/dL in 2008.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Plays the piano.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
In 2023, folate was 12 ng/mL.
Has two cats.
Free T4 of 1.2 ng/dL in 2010.
Sees a dentist yearly.
Enjoys board games.
Owns a bicycle.
Paints watercolors as a hobby.
Gives a clear account of the illness.
Knits as a hobby.
Uses sunscreen in summer.
Drives a car.
Her sister burned a hand on a stove years ago.
Her roommate has a lazy eye.
Current respiratory rate 17/min.
Prefers morning appointments.
Photographs local wildlife.
Observations now: blood pressure 117/74 mmHg.
Pupils equal and reactive to light.


## 4.69 ('gs242', 'c3', 'subject', 'long') templates=train

RULE: For acute sore throat, prescribe ibuprofen. Score 3 points if the patient currently has tonsillar exudate; 3 points if the current heart rate is 110/min or more; 3 points if the patient currently has a major bleed; 2 points if the patient currently has asthma. If the score is 7 or more, prescribe penicillin V instead.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
A 40-year-old woman.
Sore throat for two days.
No hematuria or hemoptysis.
Ferritin 60 ng/mL in 2013.
Has a pet dog.
Keeps a step counter.
Vitamin B12 450 pg/mL in 2010.
Heart rate counted over a full minute at this assessment: 132/min.
Her mother is left-handed.
Sings in a weekly choir.
Chloride 103 mmol/L in 2022.
Her coworker completed physical therapy for a shoulder injury.
Volunteers at a library.
Collects postcards.
Eats a varied diet.
Creamy exudate in the tonsillar crypts today.
Drinks two cups of coffee a day.
Watches football on weekends.
Listens to podcasts.
Lives on a quiet street.

FLIP (answer s'): -No hematuria or hemoptysis. | +Vomiting large amounts of blood today from a major bleed in the esophagus.

NEAR (answer s): -No hematuria or hemoptysis. | +Her housemate has an active major bleed from a stomach ulcer.

MISSING (answer neither (undetermined)): -No hematuria or hemoptysis. | +Active major bleeding: not asked about.

PRES (answer s): full text
40-year-old woman.
Sore throat for two days.
Vitamin B12 450 pg/mL in 2010.
Chloride 103 mmol/L in 2022.
White exudate on both tonsils.
Volunteers at a library.
Lives on a quiet street.
Has a pet dog.
Keeps a step counter.
Heart rate 132/min at rest this morning.
Her coworker completed physical therapy for a shoulder injury.
Listens to podcasts.
Drinks two cups of coffee a day.
Sings in a weekly choir.
No melena or hematemesis.
Watches football on weekends.
Eats a varied diet.
Collects postcards.
Her mother is left-handed.
Ferritin 60 ng/mL in 2013.


## 4.70 ('gs153', 'c1', 'time', 'long') templates=test

RULE: For early Lyme disease, prescribe doxycycline. If the patient currently has a mechanical heart valve, prescribe amoxicillin instead.
CONDITION: mechanical heart valve
CLAIMS: s = 'Prescribe doxycycline.' | s' = 'Prescribe amoxicillin.'

BASE (answer s):
Woman of 62 years.
Erythema migrans rash ten days after a tick bite.
Free T4 of 1.2 ng/dL in 2008.
Has two cats.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Sees a dentist yearly.
Knits as a hobby.
Her father sprained a thumb last month.
Sleeps seven hours a night.
Photographs local wildlife.
Uses sunscreen in summer.
Heart sounds irregular, without a metallic click.
Plays the piano.
Teeth in good repair.
Owns a bicycle.
Prefers to be addressed by first name.
Drives a car.
Enjoys board games.
Pupils equal and reactive to light.
Prefers morning appointments.
In 2018, folate was 12 ng/mL.
Her friend has a lazy eye.

FLIP (answer s'): -Heart sounds irregular, without a metallic click. | +Mechanical mitral valve in place; metallic closing clicks audible.

NEAR (answer s): -Heart sounds irregular, without a metallic click. | +Formerly had a mechanical mitral valve, exchanged for a bioprosthetic valve in 2014.

MISSING (answer neither (undetermined)): -Heart sounds irregular, without a metallic click. | +Mechanical heart valve: unknown.

PRES (answer s): full text
Female patient of 62 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Lives in a second-floor apartment.
In 2018, folate was 12 ng/mL.
Enjoys board games.
Teeth in good repair.
Her friend has a lazy eye.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2008.
Has two cats.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Irregularly irregular pulse; heart sounds free of clicks.
Photographs local wildlife.
Her father sprained a thumb last month.
Owns a bicycle.
Prefers morning appointments.
Sees a dentist yearly.
Plays the piano.
Drives a car.
Pupils equal and reactive to light.


## 4.71 ('gs033', 'c2', 'boundary', 'easy') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current serum potassium is above 4.8 mmol/L; 2 points if the current white cell count is above 15.0 x10^9/L; 3 points if the current calf swelling compared with the other leg is 3.0 cm or more. If the score is 7 or more, prescribe doxycycline instead.
CONDITION: serum potassium above 4.8
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Male, 36 years.
Productive cough and fever; consolidation on chest radiograph.
WBC 11.1 x10^9/L on today's sample.
Writes with the right hand.
Bakes bread at home.
Coronary artery disease treated with a stent in 2018.
Difference in calf circumference today, side to side: 4.6 cm.
Potassium measured at this assessment is 3.9 mmol/L.

FLIP (answer s'): -Potassium measured at this assessment is 3.9 mmol/L. | +Potassium measured at this assessment is 5.0 mmol/L.

NEAR (answer s): -Potassium measured at this assessment is 3.9 mmol/L. | +Potassium measured at this assessment is 4.8 mmol/L.

MISSING (answer neither (undetermined)): -Potassium measured at this assessment is 3.9 mmol/L.

PRES (answer s): full text
A 36-year-old man.
Productive cough and fever; consolidation on chest radiograph.
Complete blood count this morning: white cell count 11.1 x10^9/L.
Bakes bread at home.
Labs this morning: potassium 3.9 mmol/L.
Writes with the right hand.
Coronary artery disease was treated with a stent, and cardiology follow-up was completed in 2018 with no remaining symptoms.
Tape measurement today shows a calf circumference gap of 4.6 cm.


## 4.72 ('gs081', 'c4', 'negation', 'long') templates=test

RULE: For acute sore throat, prescribe ibuprofen. Score 3 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 3 points if the patient currently has a major bleed; 2 points if the current systolic blood pressure is below 100 mmHg; 3 points if the patient is allergic to sulfonamide antibiotics. If the score is 7 or more, prescribe penicillin V instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
Female patient of 59 years.
Sore throat for two days.
Enjoys board games.
Prefers to be addressed by first name.
Her roommate wears contact lenses.
Major bleed from the stomach at present, with hemoglobin falling.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2009.
Knits as a hobby.
Owns a bicycle.
Prefers morning appointments.
Her sister has a lazy eye.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Observations now: blood pressure 115/73 mmHg.
Her wife sprained a thumb last month.
Drives a car.
Pupils equal and reactive to light.
Her roommate has recovered from a dislocated finger.
Photographs local wildlife.
Has symptomatic peripheral artery disease of both legs.
Has two cats.
In 2024, folate was 12 ng/mL.
Sees a dentist yearly.

FLIP (answer s'): +Develops hives whenever given sulfonamide antibiotics.

NEAR (answer s): +Has never been allergic to sulfonamide antibiotics.

MISSING (answer neither (undetermined)): +Sulfonamide allergy: unknown.

PRES (answer s): full text
Woman of 59 years.
Sore throat for two days.
Her roommate wears contact lenses.
Drives a car.
Her roommate has recovered from a dislocated finger.
Owns a bicycle.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2009.
Knits as a hobby.
Currently has a major bleed from a duodenal ulcer, with transfusion under way.
Has two cats.
Prefers morning appointments.
Her wife sprained a thumb last month.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Sees a dentist yearly.
Enjoys board games.
In 2024, folate was 12 ng/mL.
Current systolic blood pressure 115 mmHg.
Her sister has a lazy eye.
Admitted with a myocardial infarction this week.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.


## 4.73 ('gs221', 'c1', 'numeric', 'easy') templates=train

RULE: For musculoskeletal pain, prescribe ibuprofen. If the current eGFR is below 30 mL/min/1.73 m2 and the patient currently has asthma, prescribe acetaminophen instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: male, 49 years.
Acute low back pain after lifting.
Asthma attack this month needing nebulizers; still wheezy at this assessment.
Renal function today: eGFR 75 mL/min/1.73 m2.
Drinks two cups of coffee a day.
Enjoys cooking.

FLIP (answer s'): -Renal function today: eGFR 75 mL/min/1.73 m2. | +Renal function today: eGFR 27 mL/min/1.73 m2.

NEAR (answer s): -Renal function today: eGFR 75 mL/min/1.73 m2. | +Renal function today: eGFR 33 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Renal function today: eGFR 75 mL/min/1.73 m2.

PRES (answer s): full text
Male, 49 years.
Acute low back pain after lifting.
Enjoys cooking.
Has asthma and uses an albuterol inhaler for wheeze.
Drinks two cups of coffee a day.
eGFR 75 mL/min/1.73 m2 on today's labs.


## 4.74 ('gs208', 'c3', 'subject', 'easy') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. Score 1 point if the current platelet count is below 150 x10^9/L; 2 points if the patient has new confusion; 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 1 point if the current systolic blood pressure is below 100 mmHg. If the score is 4 or more, prescribe sitagliptin instead.
CONDITION: colorectal cancer
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Male patient of 68 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Platelet count now 118 x10^9/L.
Owns a bicycle.
Speech clear; follows commands.
Current systolic blood pressure 124 mmHg.

FLIP (answer s'): +His sister was treated for bowel cancer years ago.

NEAR (answer s): +His friend is undergoing surgery for bowel cancer.

MISSING (answer neither (undetermined)): +Colorectal cancer: unknown.

PRES (answer s): full text
Man of 68 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current platelet count 118 x10^9/L.
Owns a bicycle.
Gives a clear account of the illness.
Observations now: blood pressure 124/78 mmHg.


## 4.75 ('two_apixaban', 'cr', 'time', 'easy') templates=train

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban 5 mg twice daily. If at least two of the following apply, prescribe apixaban 2.5 mg twice daily instead: the patient is aged 80 years or more; the current weight is 60 kg or less; the current serum creatinine is 1.5 mg/dL or more.
CONDITION: creatinine at least 1.5
CLAIMS: s = 'Prescribe apixaban 5 mg twice daily.' | s' = 'Prescribe apixaban 2.5 mg twice daily.'

BASE (answer s):
Female patient.
Atrial fibrillation; anticoagulation indicated.
Age today: 66 years.
Drinks alcohol occasionally.
Serum creatinine today: 0.6 mg/dL.
Weighs 59 kg on the scale this morning.
In 2015, serum creatinine was 0.7 mg/dL.

FLIP (answer s'): -Serum creatinine today: 0.6 mg/dL. | +Serum creatinine today: 2.5 mg/dL.

NEAR (answer s): -In 2015, serum creatinine was 0.7 mg/dL. | +In 2015, serum creatinine was 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Serum creatinine today: 0.6 mg/dL. | -In 2015, serum creatinine was 0.7 mg/dL.

PRES (answer s): full text
Adult woman.
Atrial fibrillation; anticoagulation indicated.
A routine check in 2015 gave serum creatinine 0.7 mg/dL.
Creatinine 0.6 mg/dL on this morning's labs.
Weight today: 59 kg.
Drinks alcohol occasionally.
Age at this assessment: 66 years.
