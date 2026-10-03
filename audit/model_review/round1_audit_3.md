# Audit sample 3


## 3.1 ('s1_idsa_minor', 'wbc', 'boundary', 'long') templates=train

RULE: IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): 1 point each for a current white cell count below 4.0 x10^9/L; a current platelet count below 100 x10^9/L; a current temperature below 36.0 C; a current blood urea nitrogen of 20 mg/dL or more. Other criteria are not part of this question.
CONDITION: white cell count below 4.0
CLAIMS: s = 'The white cell count criterion contributes 0 points.' | s' = 'The white cell count criterion contributes 1 point.'

BASE (answer s):
Female, 68 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Watches football on weekends.
Keeps houseplants.
Her housemate previously wore dental braces.
Her cousin is nearsighted.
Bakes bread at home.
Complete blood count today: platelets 328 x10^9/L.
Listens to podcasts.
Chloride 103 mmol/L in 2009.
Uses a smartphone for reminders.
Collects postcards.
BUN at this assessment: 13 mg/dL.
Drinks alcohol occasionally.
Volunteers at a library.
Speaks English and Spanish.
Temperature today: 38.2 C.
Ferritin 60 ng/mL in 2023.
Drinks two cups of coffee a day.
Sodium 140 mmol/L in 2018.
WBC on the blood count drawn at this assessment: 11.1 x10^9/L.

FLIP (answer s'): -WBC on the blood count drawn at this assessment: 11.1 x10^9/L. | +WBC on the blood count drawn at this assessment: 2.6 x10^9/L.

NEAR (answer s): -WBC on the blood count drawn at this assessment: 11.1 x10^9/L. | +WBC on the blood count drawn at this assessment: 4.0 x10^9/L.

MISSING (answer neither (undetermined)): -WBC on the blood count drawn at this assessment: 11.1 x10^9/L.

PRES (answer s): full text
A 68-year-old woman.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Platelet count today: 328 x10^9/L.
Speaks English and Spanish.
White cell count today: 11.1 x10^9/L.
Listens to podcasts.
Sodium 140 mmol/L in 2018.
Keeps houseplants.
Chloride 103 mmol/L in 2009.
Collects postcards.
Her cousin is nearsighted.
Drinks two cups of coffee a day.
Bakes bread at home.
Volunteers at a library.
Temperature checked with a digital thermometer today: 38.2 C.
Ferritin 60 ng/mL in 2023.
Drinks alcohol occasionally.
Watches football on weekends.
Uses a smartphone for reminders.
BUN on today's chemistry panel: 13 mg/dL.
Her housemate previously wore dental braces.


## 3.2 ('gs096', 'c1', 'negation', 'easy') templates=test

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 2 points if the patient currently has a major bleed; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 1 point if the patient has ever had angioedema (current or past); 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past). If the score is 3 or more, prescribe azithromycin instead.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Female patient of 51 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Varicose veins: none seen.
Sees a dentist yearly.
Has symptomatic peripheral artery disease of both legs.
Photographs local wildlife.

FLIP (answer s'): +Major bleed from the stomach at present, with hemoglobin falling.

NEAR (answer s): +Medical records negative for major bleeding at any time.

MISSING (answer neither (undetermined)): +Active major bleeding: unknown.

PRES (answer s): full text
Woman of 51 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Coagulation tests normal on recent bloodwork.
Sees a dentist yearly.
Photographs local wildlife.
Admitted with a myocardial infarction this week.


## 3.3 ('curb65', 'sbp', 'numeric', 'easy') templates=train

RULE: CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
CONDITION: blood pressure below 90
CLAIMS: s = 'The blood pressure criterion contributes 0 points.' | s' = 'The blood pressure criterion contributes 1 point.'

BASE (answer s):
Adult man.
Community-acquired pneumonia confirmed on chest radiograph.
BUN on today's chemistry panel: 15 mg/dL.
Vaccinations up to date.
Volunteers at a library.
Writes with the right hand.
Respiratory rate 17/min at this assessment.
Systolic blood pressure 112 mmHg at this assessment.
Age on arrival: 54 years.
Uses public transport.
Answers questions appropriately.

FLIP (answer s'): -Systolic blood pressure 112 mmHg at this assessment. | +Systolic blood pressure 73 mmHg at this assessment.

NEAR (answer s): -Systolic blood pressure 112 mmHg at this assessment. | +Systolic blood pressure 92 mmHg at this assessment.

MISSING (answer neither (undetermined)): -Systolic blood pressure 112 mmHg at this assessment.

PRES (answer s): full text
Male patient.
Community-acquired pneumonia confirmed on chest radiograph.
Writes with the right hand.
Age 54 years, calculated today from the date of birth.
Today's BUN is 15 mg/dL.
Volunteers at a library.
Manual cuff blood pressure today: 112/71 mmHg.
Memory and concentration normal on bedside testing.
Respiratory rate 17/min this morning.
Vaccinations up to date.
Uses public transport.


## 3.4 ('wells_dvt', 'vte', 'subject', 'easy') templates=test

RULE: Wells DVT score (as used here, partial): 1 point each for active cancer; a venous thromboembolism of the patient, current or previous; current calf swelling of 3.0 cm or more compared with the other leg. Other Wells items are not part of this question.
CONDITION: venous thromboembolism
CLAIMS: s = 'The venous thromboembolism criterion contributes 0 points.' | s' = 'The venous thromboembolism criterion contributes 1 point.'

BASE (answer s):
Man of 31 years.
Left leg pain for two days after a long-haul flight.
Pupils equal and reactive to light.
Calf swelling now amounts to 0.0 cm of extra girth in the larger calf.
Paints watercolors as a hobby.

FLIP (answer s'): +Has an acute pulmonary embolism, diagnosed this week.

NEAR (answer s): +His uncle is on anticoagulation for venous thrombosis.

MISSING (answer neither (undetermined)): +Venous thromboembolism: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 31 years.
Left leg pain for two days after a long-haul flight.
Current calf swelling 0.0 cm compared with the other leg.
Pupils equal and reactive to light.
Paints watercolors as a hobby.


## 3.5 ('strep_amox', 'pen_allergy', 'time', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient is allergic to penicillin, prescribe azithromycin instead.
CONDITION: penicillin allergy
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
A 40-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Denies any drug allergies.
Reads most evenings.

FLIP (answer s'): -Denies any drug allergies. | +Allergic to penicillin (urticaria).

NEAR (answer s): -Denies any drug allergies. | +An old penicillin allergy has resolved; penicillin given for a dental abscess in 2023 was well tolerated.

MISSING (answer neither (undetermined)): -Denies any drug allergies. | +Penicillin allergy: not documented in the records available.

PRES (answer s): full text
40-year-old man.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
No beta-lactam allergy.
Reads most evenings.


## 3.6 ('gs132', 'c1', 'boundary', 'easy') templates=test

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the current eGFR is below 45 mL/min/1.73 m2, prescribe intermittent pneumatic compression instead.
CONDITION: eGFR below 45
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Male patient of 40 years.
Admitted for community-acquired pneumonia; immobile.
Drives a car.
Uses sunscreen in summer.
Teeth in good repair.
Photographs local wildlife.
eGFR now 82 mL/min/1.73 m2.

FLIP (answer s'): -eGFR now 82 mL/min/1.73 m2. | +eGFR now 30 mL/min/1.73 m2.

NEAR (answer s): -eGFR now 82 mL/min/1.73 m2. | +eGFR now 45 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -eGFR now 82 mL/min/1.73 m2.

PRES (answer s): full text
Man of 40 years.
Admitted for community-acquired pneumonia; immobile.
Current eGFR 82 mL/min/1.73 m2.
Uses sunscreen in summer.
Photographs local wildlife.
Teeth in good repair.
Drives a car.


## 3.7 ('gs136', 'c2', 'negation', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient has an active peptic ulcer; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient has ever had asthma (current or past).
CONDITION: vascular disease
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
A 37-year-old woman.
Requests contraception.
Collects postcards.
Peripheral pulses palpable.
Enjoys gardening.
No dyspepsia or melena.
Nails normal.
Asthmatic; wheezes on exertion and in cold air.

FLIP (answer s'): -Peripheral pulses palpable. | +Myocardial infarction in 2021; completed cardiac rehabilitation and has had no symptoms since.

NEAR (answer s): -Peripheral pulses palpable. | +Denies ever having had a myocardial infarction or peripheral artery disease.

MISSING (answer neither (undetermined)): -Peripheral pulses palpable. | +Vascular disease: not documented in the records available.

PRES (answer s): full text
37-year-old woman.
Requests contraception.
Nails normal.
Collects postcards.
Toes warm, with brisk capillary refill.
Enjoys gardening.
No black or bloody stools.
Has asthma and uses an albuterol inhaler for wheeze.


## 3.8 ('gs221', 'c1', 'numeric', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the current eGFR is below 30 mL/min/1.73 m2 and the patient currently has asthma, prescribe acetaminophen instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Man of 39 years.
Acute low back pain after lifting.
Plays the piano.
Paints watercolors as a hobby.
Prefers morning appointments.
Asthma, on a daily inhaled steroid.
His father sprained a thumb last month.
Photographs local wildlife.
Sleeps seven hours a night.
Enjoys board games.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2019.
Owns a bicycle.
His uncle lives with psoriasis.
Teeth in good repair.
Pupils equal and reactive to light.
Knits as a hobby.
Drives a car.
Current eGFR 67 mL/min/1.73 m2.
Prefers to be addressed by first name.
During a checkup in 2012, total protein was 7.0 g/dL.
Uses sunscreen in summer.

FLIP (answer s'): -Current eGFR 67 mL/min/1.73 m2. | +Current eGFR 21 mL/min/1.73 m2.

NEAR (answer s): -Current eGFR 67 mL/min/1.73 m2. | +Current eGFR 35 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Current eGFR 67 mL/min/1.73 m2.

PRES (answer s): full text
Male patient of 39 years.
Acute low back pain after lifting.
Pupils equal and reactive to light.
Sees a dentist yearly.
His father sprained a thumb last month.
Photographs local wildlife.
Prefers morning appointments.
Paints watercolors as a hobby.
Enjoys board games.
Owns a bicycle.
Sleeps seven hours a night.
During a checkup in 2012, total protein was 7.0 g/dL.
His uncle lives with psoriasis.
Teeth in good repair.
Drives a car.
Prefers to be addressed by first name.
Plays the piano.
eGFR now 67 mL/min/1.73 m2.
Free T4 of 1.2 ng/dL in 2019.
Uses sunscreen in summer.
Persistent asthma, using a rescue inhaler most weeks.
Knits as a hobby.


## 3.9 ('gs232', 'c2', 'subject', 'easy') templates=train

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the patient is allergic to penicillin or the patient currently has a mechanical heart valve, prescribe sitagliptin instead.
CONDITION: mechanical heart valve
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Patient: female, 76 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Volunteers at a library.
Not allergic to any antibiotics.

FLIP (answer s'): +Has a mechanical aortic valve.

NEAR (answer s): +Her brother-in-law has a mechanical heart valve.

MISSING (answer neither (undetermined)): +Mechanical heart valve: not asked about.

PRES (answer s): full text
Female, 76 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Volunteers at a library.
Denies any drug allergies.


## 3.10 ('news2_red', 'spo2', 'time', 'superseded') templates=test

RULE: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.
CONDITION: oxygen saturation at or below 91
CLAIMS: s = 'The oxygen saturation criterion contributes 0 points.' | s' = 'The oxygen saturation criterion contributes 3 points.'

BASE (answer s):
Man of 46 years.
Shortness of breath and fever; assessed on the medical ward.
Last month, oxygen saturation was 97%; the newest measurement replaces it.
Has two cats.
Observations now: blood pressure 129/81 mmHg.
Current respiratory rate 18/min.
Gives a clear account of the illness.
Latest oxygen saturation reading: 98%.
Sees a dentist yearly.

FLIP (answer s'): -Latest oxygen saturation reading: 98%. | +Latest oxygen saturation reading: 88%.

NEAR (answer s): -Last month, oxygen saturation was 97%; the newest measurement replaces it. | +Last month, oxygen saturation was 78%; the newest measurement replaces it.

MISSING (answer neither (undetermined)): -Last month, oxygen saturation was 97%; the newest measurement replaces it. | -Latest oxygen saturation reading: 98%.

PRES (answer s): full text
Male patient of 46 years.
Shortness of breath and fever; assessed on the medical ward.
Sees a dentist yearly.
Current systolic blood pressure 129 mmHg.
Earlier this week, oxygen saturation was 97%; a newer reading supersedes it.
Current oxygen saturation 98%.
Observations now: respiratory rate 18/min.
Has two cats.
Speech clear; follows commands.


## 3.11 ('gs230', 'c1', 'boundary', 'long') templates=train

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current platelet count is below 50 x10^9/L, prescribe aspirin plus clopidogrel instead.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Patient: male, 89 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Collects postcards.
Sings in a weekly choir.
Grows tomatoes in the garden.
TSH 1.6 mIU/L in 2023.
Magnesium 2.0 mg/dL in 2019.
Platelets 369 x10^9/L on this morning's blood count.
Albumin 4.1 g/dL in 2016 (routine blood test).
Writes with the right hand.
Chloride 103 mmol/L in 2008.
Plays chess online.
Vaccinations up to date.
Does crossword puzzles.
Uses a smartphone for reminders.
His brother-in-law broke a wrist, which has healed.
Drinks two cups of coffee a day.
Nails normal.
His brother-in-law is nearsighted.

FLIP (answer s'): -Platelets 369 x10^9/L on this morning's blood count. | +Platelets 24 x10^9/L on this morning's blood count.

NEAR (answer s): -Platelets 369 x10^9/L on this morning's blood count. | +Platelets 50 x10^9/L on this morning's blood count.

MISSING (answer neither (undetermined)): -Platelets 369 x10^9/L on this morning's blood count.

PRES (answer s): full text
A 89-year-old man.
Recovering on the ward after a myocardial infarction treated with a stent.
Albumin 4.1 g/dL in 2016 (routine blood test).
TSH 1.6 mIU/L in 2023.
Magnesium 2.0 mg/dL in 2019.
Chloride 103 mmol/L in 2008.
Sings in a weekly choir.
Grows tomatoes in the garden.
Platelet count at this assessment: 369 x10^9/L.
Nails normal.
His brother-in-law broke a wrist, which has healed.
Writes with the right hand.
Drinks two cups of coffee a day.
His brother-in-law is nearsighted.
Plays chess online.
Vaccinations up to date.
Does crossword puzzles.
Uses a smartphone for reminders.
Collects postcards.


## 3.12 ('gs213', 'c1', 'negation', 'easy') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. If at least two of the following apply, prescribe diltiazem instead: the patient has an active peptic ulcer; the current weight is below 67 kg; the patient is currently taking clarithromycin.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Female patient of 46 years.
Atrial fibrillation with a ventricular rate of 128/min.
Abdomen soft and non-tender.
Prefers to be addressed by first name.
Teeth in good repair.
Drives a car.
Latest weight 45 kg.

FLIP (answer s'): -Abdomen soft and non-tender. | +Active peptic ulcer disease.

NEAR (answer s): -Abdomen soft and non-tender. | +Medical record negative for peptic ulcer, current or past.

MISSING (answer neither (undetermined)): -Abdomen soft and non-tender. | +Active peptic ulcer: unknown.

PRES (answer s): full text
Woman of 46 years.
Atrial fibrillation with a ventricular rate of 128/min.
Teeth in good repair.
Drives a car.
Appetite good; no indigestion.
Prefers to be addressed by first name.
Current weight 45 kg.


## 3.13 ('s4_abcd2', 'age', 'numeric', 'long') templates=train

RULE: ABCD2 score (as used here, partial): 1 point each for age 60 years or more; a current systolic blood pressure of 140 mmHg or more; diabetes at any time. Clinical features and duration of symptoms are not part of this question.
CONDITION: age at least 60
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Female patient.
Transient weakness of the left arm lasting 20 minutes; assessed in a rapid-access clinic.
Lives on a quiet street.
TSH 1.6 mIU/L in 2020.
Vaccinations up to date.
Her aunt is left-handed.
Bicarbonate 26 mmol/L in 2021 (annual physical).
Non-smoker.
Grows tomatoes in the garden.
Her brother wears hearing aids.
Enjoys cooking.
Plays chess online.
Manual cuff blood pressure today: 104/66 mmHg.
Volunteers at a library.
Uses public transport.
Collects postcards.
Age at this assessment: 43 years.
Eats a varied diet.
Urine dipstick shows no sugar.
Ferritin 60 ng/mL in 2014.
Her cousin is being treated for eczema.
Chloride 103 mmol/L in 2005.

FLIP (answer s'): -Age at this assessment: 43 years. | +Age at this assessment: 88 years.

NEAR (answer s): -Age at this assessment: 43 years. | +Age at this assessment: 57 years.

MISSING (answer neither (undetermined)): -Age at this assessment: 43 years.

PRES (answer s): full text
Adult woman.
Transient weakness of the left arm lasting 20 minutes; assessed in a rapid-access clinic.
Plays chess online.
Bicarbonate 26 mmol/L in 2021 (annual physical).
Volunteers at a library.
Lives on a quiet street.
Grows tomatoes in the garden.
Her cousin is being treated for eczema.
Collects postcards.
Eats a varied diet.
Uses public transport.
Enjoys cooking.
Systolic blood pressure 104 mmHg at this assessment.
TSH 1.6 mIU/L in 2020.
Her aunt is left-handed.
Non-smoker.
Vaccinations up to date.
Ferritin 60 ng/mL in 2014.
Age on arrival: 43 years.
Chloride 103 mmol/L in 2005.
Takes no medicines to lower blood sugar.
Her brother wears hearing aids.


## 3.14 ('gs023', 'c2', 'subject', 'long') templates=test

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the patient currently has a major bleed or the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time, prescribe aspirin plus clopidogrel instead.
CONDITION: colorectal cancer
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
Female patient of 74 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Has two cats.
Teeth in good repair.
Lives in a second-floor apartment.
In 2015, lipase was 30 U/L.
Uses sunscreen in summer.
Sleeps seven hours a night.
Rectal exam unremarkable.
Prefers to be addressed by first name.
Her friend wears contact lenses.
Her sister burned a hand on a stove years ago.
In 2023, folate was 12 ng/mL.
Sees a dentist yearly.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Enjoys board games.
During a checkup in 2019, total protein was 7.0 g/dL.
Plays the piano.
Prefers morning appointments.
Her friend has a lazy eye.
Owns a bicycle.

FLIP (answer s'): -Rectal exam unremarkable. | +Colorectal cancer under active treatment.

NEAR (answer s): -Rectal exam unremarkable. | +Her roommate was treated for bowel cancer years ago.

MISSING (answer neither (undetermined)): -Rectal exam unremarkable. | +Colorectal cancer: unknown.

PRES (answer s): full text
Woman of 74 years.
Recovering on the ward after a myocardial infarction treated with a stent.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Hemoglobin within the normal range on recent blood tests.
Uses sunscreen in summer.
Sleeps seven hours a night.
In 2015, lipase was 30 U/L.
Her friend wears contact lenses.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Plays the piano.
Teeth in good repair.
Her friend has a lazy eye.
Sees a dentist yearly.
During a checkup in 2019, total protein was 7.0 g/dL.
Enjoys board games.
Owns a bicycle.
In 2023, folate was 12 ng/mL.
Her sister burned a hand on a stove years ago.
Prefers morning appointments.
Has two cats.


## 3.15 ('s1_sofa', 'cr', 'time', 'long') templates=train

RULE: SOFA score (as used here, partial): 1 point each for a current platelet count below 150 x10^9/L; a current serum creatinine of 1.2 mg/dL or more; a current mean arterial pressure below 70 mmHg. Other SOFA items are not part of this question.
CONDITION: creatinine at least 1.2
CLAIMS: s = 'The creatinine criterion contributes 0 points.' | s' = 'The creatinine criterion contributes 1 point.'

BASE (answer s):
Patient: male, 57 years.
Sepsis from a chest infection; admitted to the intensive care unit.
Keeps a step counter.
Uses reading glasses for small print.
Watches football on weekends.
Uses public transport.
Platelets 273 x10^9/L on this morning's blood count.
Eats a varied diet.
Mean arterial pressure on the bedside monitor today: 91 mmHg.
Drinks alcohol occasionally.
Uses a smartphone for reminders.
Vaccinations up to date.
His aunt is nearsighted.
In 2018, serum creatinine was 0.7 mg/dL.
His partner is left-handed.
Kidney function today: creatinine 0.7 mg/dL.
Sodium 140 mmol/L in 2006.
Enjoys gardening.
Sings in a weekly choir.
Listens to podcasts.
His housemate broke a wrist, which has healed.
Plays chess online.
Total bilirubin 0.6 mg/dL in 2022.
His brother had a splinter removed from a finger.
Vitamin B12 450 pg/mL in 2008.
Writes with the right hand.

FLIP (answer s'): -Kidney function today: creatinine 0.7 mg/dL. | +Kidney function today: creatinine 1.7 mg/dL.

NEAR (answer s): -In 2018, serum creatinine was 0.7 mg/dL. | +In 2018, serum creatinine was 1.4 mg/dL.

MISSING (answer neither (undetermined)): -In 2018, serum creatinine was 0.7 mg/dL. | -Kidney function today: creatinine 0.7 mg/dL.

PRES (answer s): full text
Male, 57 years.
Sepsis from a chest infection; admitted to the intensive care unit.
Platelet count today: 273 x10^9/L.
Mean arterial pressure 91 mmHg on the monitor this morning.
Sodium 140 mmol/L in 2006.
His aunt is nearsighted.
Sings in a weekly choir.
Enjoys gardening.
Uses public transport.
Drinks alcohol occasionally.
Eats a varied diet.
His housemate broke a wrist, which has healed.
Uses reading glasses for small print.
Vitamin B12 450 pg/mL in 2008.
Total bilirubin 0.6 mg/dL in 2022.
Uses a smartphone for reminders.
His brother had a splinter removed from a finger.
Plays chess online.
His partner is left-handed.
Watches football on weekends.
Vaccinations up to date.
Keeps a step counter.
A routine check in 2018 gave serum creatinine 0.7 mg/dL.
Listens to podcasts.
Writes with the right hand.
Serum creatinine today: 0.7 mg/dL.


## 3.16 ('gs233', 'c2', 'boundary', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had heparin-induced thrombocytopenia (current or past) and the current weight is below 67 kg, prescribe naproxen with omeprazole instead.
CONDITION: weight below 67
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Female patient of 57 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2007; blood counts recovered afterward.
Has two cats.
Sees a dentist yearly.
Current weight 94 kg.

FLIP (answer s'): -Current weight 94 kg. | +Current weight 57 kg.

NEAR (answer s): -Current weight 94 kg. | +Current weight 67 kg.

MISSING (answer neither (undetermined)): -Current weight 94 kg.

PRES (answer s): full text
Woman of 57 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Latest weight 94 kg.
Sees a dentist yearly.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2007; blood counts recovered afterward.
Has two cats.


## 3.17 ('c2_statin_clarith', 'clarith', 'negation', 'long') templates=train

RULE: For primary prevention of cardiovascular disease, prescribe simvastatin. If the patient is currently taking clarithromycin, prescribe pravastatin instead.
CONDITION: clarithromycin use
CLAIMS: s = 'Prescribe simvastatin.' | s' = 'Prescribe pravastatin.'

BASE (answer s):
Patient: male, 47 years.
Primary prevention; LDL cholesterol 172 mg/dL, 10-year cardiovascular risk 11%.
Bakes bread at home.
Has a pet dog.
Drinks alcohol occasionally.
Magnesium 2.0 mg/dL in 2007.
Keeps houseplants.
Plays chess online.
Hearing normal to conversation.
His brother-in-law broke a wrist, which has healed.
Serum calcium 9.4 mg/dL in 2021.
Non-smoker.
No macrolide antibiotics on the medication list.
Drinks plenty of water.
Height 170 cm.
Grows tomatoes in the garden.
Watches football on weekends.
Albumin 4.1 g/dL in 2010 (routine blood test).
His brother-in-law has a stutter.

FLIP (answer s'): -No macrolide antibiotics on the medication list. | +Started clarithromycin this morning for sinusitis.

NEAR (answer s): -No macrolide antibiotics on the medication list. | +No antibiotics are being taken, including clarithromycin.

MISSING (answer neither (undetermined)): -No macrolide antibiotics on the medication list. | +Information on clarithromycin use was not obtained.

PRES (answer s): full text
47-year-old man.
Primary prevention; LDL cholesterol 172 mg/dL, 10-year cardiovascular risk 11%.
Bakes bread at home.
Plays chess online.
Drinks plenty of water.
Height 170 cm.
Serum calcium 9.4 mg/dL in 2021.
Grows tomatoes in the garden.
Non-smoker.
His brother-in-law has a stutter.
Albumin 4.1 g/dL in 2010 (routine blood test).
Magnesium 2.0 mg/dL in 2007.
Hearing normal to conversation.
Drinks alcohol occasionally.
Antibiotics: none.
His brother-in-law broke a wrist, which has healed.
Keeps houseplants.
Has a pet dog.
Watches football on weekends.


## 3.18 ('gs221', 'c1', 'numeric', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the current eGFR is below 30 mL/min/1.73 m2 and the patient currently has asthma, prescribe acetaminophen instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Woman of 54 years.
Acute low back pain after lifting.
In 2006, folate was 12 ng/mL.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
During a checkup in 2009, total protein was 7.0 g/dL.
Sees a dentist yearly.
Pupils equal and reactive to light.
Owns a bicycle.
Sleeps seven hours a night.
Asthma, on a daily inhaled steroid.
Uses sunscreen in summer.
In 2014, lipase was 30 U/L.
Has two cats.
Enjoys board games.
Her roommate lives with psoriasis.
Drives a car.
eGFR now 86 mL/min/1.73 m2.
Prefers morning appointments.
Knits as a hobby.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2015.
Her uncle wears contact lenses.

FLIP (answer s'): -eGFR now 86 mL/min/1.73 m2. | +eGFR now 19 mL/min/1.73 m2.

NEAR (answer s): -eGFR now 86 mL/min/1.73 m2. | +eGFR now 31 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -eGFR now 86 mL/min/1.73 m2.

PRES (answer s): full text
Female patient of 54 years.
Acute low back pain after lifting.
Drives a car.
In 2006, folate was 12 ng/mL.
Paints watercolors as a hobby.
Her uncle wears contact lenses.
Sleeps seven hours a night.
Knits as a hobby.
Persistent asthma, using a rescue inhaler most weeks.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Sees a dentist yearly.
Her roommate lives with psoriasis.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2015.
Owns a bicycle.
Prefers morning appointments.
Has two cats.
In 2014, lipase was 30 U/L.
Current eGFR 86 mL/min/1.73 m2.
Lives in a second-floor apartment.
During a checkup in 2009, total protein was 7.0 g/dL.
Prefers to be addressed by first name.


## 3.19 ('gs028', 'c3', 'subject', 'easy') templates=train

RULE: For contraception, prescribe a combined oral contraceptive. Score 1 point if the patient has ever had coronary artery disease (current or past); 1 point if the patient has ever had angioedema (current or past); 2 points if the patient currently has a venous thromboembolism. If the score is 4 or more, prescribe a progestin-only pill instead.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe a combined oral contraceptive.' | s' = 'Prescribe a progestin-only pill.'

BASE (answer s):
40-year-old woman.
Requests contraception.
Has hereditary angioedema, with attacks every few months.
Collects postcards.
Coronary artery disease on ongoing treatment.

FLIP (answer s'): +On treatment for a deep vein thrombosis in the left leg.

NEAR (answer s): +Her brother has a DVT confirmed on ultrasound today.

MISSING (answer neither (undetermined)): +Current venous thromboembolism: not recorded.

PRES (answer s): full text
Patient: female, 40 years.
Requests contraception.
Coronary artery disease, followed in cardiology clinic every six months.
Collects postcards.
Idiopathic angioedema, treated with daily antihistamines.


## 3.20 ('gs092', 'c1', 'time', 'easy') templates=test

RULE: For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the patient currently has heart failure; the patient has ever had angioedema (current or past); the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time.
CONDITION: current heart failure
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Man of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Heart sounds without a gallop.
Sees a dentist yearly.
His sister had diabetes years ago that went away after a change in diet.
Face and neck without swelling on examination.
Drives a car.

FLIP (answer s'): -Heart sounds without a gallop. | +Current heart failure with ankle swelling.

NEAR (answer s): -Heart sounds without a gallop. | +Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected.

MISSING (answer neither (undetermined)): -Heart sounds without a gallop. | +Current heart failure: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Free of facial or oropharyngeal edema.
Sees a dentist yearly.
Drives a car.
His sister was diabetic until bariatric surgery several years ago.
Sleeps flat on one pillow.


## 3.21 ('s1_idsa_minor', 'temp', 'boundary', 'long') templates=train

RULE: IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): 1 point each for a current white cell count below 4.0 x10^9/L; a current platelet count below 100 x10^9/L; a current temperature below 36.0 C; a current blood urea nitrogen of 20 mg/dL or more. Other criteria are not part of this question.
CONDITION: temperature below 36.0
CLAIMS: s = 'The temperature criterion contributes 0 points.' | s' = 'The temperature criterion contributes 1 point.'

BASE (answer s):
Male, 81 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Height 170 cm.
His housemate has a broken finger in a splint.
Platelets 220 x10^9/L on this morning's blood count.
Uses reading glasses for small print.
Today's BUN is 14 mg/dL.
WBC 12.6 x10^9/L on today's sample.
Bakes bread at home.
His housemate is left-handed.
His brother has a stutter.
Hearing normal to conversation.
Temperature today: 37.7 C.
Has a pet dog.
Serum calcium 9.4 mg/dL in 2016.
Uses public transport.
His coworker wears hearing aids.
Magnesium 2.0 mg/dL in 2016.
Drinks plenty of water.
Drinks alcohol occasionally.
Vaccinations up to date.
Lives on a quiet street.
Volunteers at a library.

FLIP (answer s'): -Temperature today: 37.7 C. | +Temperature today: 35.0 C.

NEAR (answer s): -Temperature today: 37.7 C. | +Temperature today: 36.0 C.

MISSING (answer neither (undetermined)): -Temperature today: 37.7 C.

PRES (answer s): full text
81-year-old man.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Drinks alcohol occasionally.
BUN on today's chemistry panel: 14 mg/dL.
Lives on a quiet street.
Hearing normal to conversation.
Uses reading glasses for small print.
WBC on the blood count drawn at this assessment: 12.6 x10^9/L.
Has a pet dog.
Temperature 37.7 C at this assessment.
His housemate has a broken finger in a splint.
Serum calcium 9.4 mg/dL in 2016.
Volunteers at a library.
Height 170 cm.
His housemate is left-handed.
Uses public transport.
Drinks plenty of water.
His brother has a stutter.
Magnesium 2.0 mg/dL in 2016.
Vaccinations up to date.
His coworker wears hearing aids.
Bakes bread at home.
Complete blood count today: platelets 220 x10^9/L.


## 3.22 ('pain_ulcer', 'ulcer', 'negation', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the patient has an active peptic ulcer, prescribe acetaminophen instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Woman of 32 years.
Acute low back pain after lifting.
Knits as a hobby.
Abdomen soft and non-tender.
Prefers morning appointments.
Photographs local wildlife.
Sees a dentist yearly.
Teeth in good repair.
In 2024, folate was 12 ng/mL.
Her father sprained a thumb last month.
Enjoys board games.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Has two cats.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Drives a car.
Her sister has recovered from a dislocated finger.

FLIP (answer s'): -Abdomen soft and non-tender. | +Active peptic ulcer disease.

NEAR (answer s): -Abdomen soft and non-tender. | +Medical record negative for peptic ulcer, current or past.

MISSING (answer neither (undetermined)): -Abdomen soft and non-tender. | +Active peptic ulcer: status unclear from the records at hand.

PRES (answer s): full text
Female patient of 32 years.
Acute low back pain after lifting.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Knits as a hobby.
Uses sunscreen in summer.
Sees a dentist yearly.
Pupils equal and reactive to light.
Appetite good; no indigestion.
Lives in a second-floor apartment.
Enjoys board games.
Drives a car.
Photographs local wildlife.
Her father sprained a thumb last month.
Prefers to be addressed by first name.
In 2024, folate was 12 ng/mL.
Has two cats.
Her sister has recovered from a dislocated finger.
Teeth in good repair.


## 3.23 ('gs049', 'c1', 'numeric', 'easy') templates=train

RULE: For acute migraine, prescribe sumatriptan. If the current respiratory rate is 30/min or more or the current white cell count is above 12.0 x10^9/L, prescribe naproxen instead.
CONDITION: respiratory rate at least 30
CLAIMS: s = 'Prescribe sumatriptan.' | s' = 'Prescribe naproxen.'

BASE (answer s):
18-year-old man.
Acute migraine without aura, typical of prior attacks.
WBC 5.4 x10^9/L on today's sample.
Does crossword puzzles.
Bakes bread at home.
Respiratory rate 18/min this morning.
Collects postcards.

FLIP (answer s'): -Respiratory rate 18/min this morning. | +Respiratory rate 35/min this morning.

NEAR (answer s): -Respiratory rate 18/min this morning. | +Respiratory rate 27/min this morning.

MISSING (answer neither (undetermined)): -Respiratory rate 18/min this morning.

PRES (answer s): full text
A 18-year-old man.
Acute migraine without aura, typical of prior attacks.
Respiratory rate 18/min at this assessment.
Bakes bread at home.
Collects postcards.
White cell count today: 5.4 x10^9/L.
Does crossword puzzles.


## 3.24 ('gs163', 'c2', 'subject', 'easy') templates=test

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the current serum creatinine is above 2.0 mg/dL or the patient has ever had diabetes (current or past), prescribe doxycycline instead.
CONDITION: diabetes
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Man of 49 years.
Productive cough and fever; consolidation on chest radiograph.
Prefers morning appointments.
Latest creatinine result: 1.1 mg/dL.
Random glucose 92 mg/dL.

FLIP (answer s'): -Random glucose 92 mg/dL. | +Had diabetes years ago that went into remission on a low-calorie diet.

NEAR (answer s): -Random glucose 92 mg/dL. | +His wife lives with type 1 diabetes.

MISSING (answer neither (undetermined)): -Random glucose 92 mg/dL. | +Diabetes: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 49 years.
Productive cough and fever; consolidation on chest radiograph.
Prefers morning appointments.
Current serum creatinine 1.1 mg/dL.
HbA1c 5.3% at a routine check.


## 3.25 ('gs228', 'c1', 'time', 'long') templates=train

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the current respiratory rate is 22/min or more and the patient has ever had a peptic ulcer (current or past), prescribe intravenous co-amoxiclav instead.
CONDITION: respiratory rate at least 22
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
32-year-old woman.
Community-acquired pneumonia confirmed on chest radiograph.
Peptic ulcer in 2021, healed on repeat endoscopy.
Respiratory rate 17/min this morning.
Her grandfather wears hearing aids.
Has a pet dog.
Feeds birds in the backyard.
Nails normal.
Bicarbonate 26 mmol/L in 2013 (annual physical).
Drinks two cups of coffee a day.
Her neighbor had a splinter removed from a finger.
Does crossword puzzles.
Her housemate is left-handed.
Keeps a step counter.
Grows tomatoes in the garden.
Her aunt is nearsighted.
Respiratory rate 13/min at a clinic visit in 2017.
Uses public transport.
Volunteers at a library.
Sodium 140 mmol/L in 2022.

FLIP (answer s'): -Respiratory rate 17/min this morning. | +Respiratory rate 30/min this morning.

NEAR (answer s): -Respiratory rate 13/min at a clinic visit in 2017. | +Respiratory rate 24/min at a clinic visit in 2017.

MISSING (answer neither (undetermined)): -Respiratory rate 17/min this morning. | -Respiratory rate 13/min at a clinic visit in 2017.

PRES (answer s): full text
A 32-year-old woman.
Community-acquired pneumonia confirmed on chest radiograph.
Her housemate is left-handed.
Does crossword puzzles.
Sodium 140 mmol/L in 2022.
Treatment for Helicobacter pylori in 2021 resolved a stomach ulcer.
Keeps a step counter.
Has a pet dog.
Nails normal.
Her neighbor had a splinter removed from a finger.
Grows tomatoes in the garden.
Feeds birds in the backyard.
Bicarbonate 26 mmol/L in 2013 (annual physical).
Drinks two cups of coffee a day.
A routine check in 2017 gave respiratory rate 13/min.
Her grandfather wears hearing aids.
Uses public transport.
Her aunt is nearsighted.
Respiratory rate 17/min at this assessment.
Volunteers at a library.


## 3.26 ('gs208', 'c4', 'boundary', 'long') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. Score 1 point if the current platelet count is below 150 x10^9/L; 2 points if the patient has new confusion; 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 1 point if the current systolic blood pressure is below 100 mmHg. If the score is 4 or more, prescribe sitagliptin instead.
CONDITION: systolic blood pressure below 100
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Woman of 72 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
In 2018, folate was 12 ng/mL.
Current systolic blood pressure 114 mmHg.
Plays the piano.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2006, lipase was 30 U/L.
Platelet count now 112 x10^9/L.
Sees a dentist yearly.
Lives in a second-floor apartment.
Enjoys board games.
Owns a bicycle.
Her sister lives with psoriasis.
Newly disoriented and unable to give a clear history.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Prefers morning appointments.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2020.
Knits as a hobby.
Hemoglobin within the normal range on recent blood tests.
Teeth in good repair.
Prefers to be addressed by first name.

FLIP (answer s'): -Current systolic blood pressure 114 mmHg. | +Current systolic blood pressure 74 mmHg.

NEAR (answer s): -Current systolic blood pressure 114 mmHg. | +Current systolic blood pressure 100 mmHg.

MISSING (answer neither (undetermined)): -Current systolic blood pressure 114 mmHg.

PRES (answer s): full text
Female patient of 72 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Teeth in good repair.
Sleeps seven hours a night.
Prefers morning appointments.
Lives in a second-floor apartment.
Disoriented to time and place, which is new for the patient.
Photographs local wildlife.
Rectal exam unremarkable.
Prefers to be addressed by first name.
Knits as a hobby.
Observations now: blood pressure 114/72 mmHg.
Owns a bicycle.
Current platelet count 112 x10^9/L.
Plays the piano.
Enjoys board games.
In 2018, folate was 12 ng/mL.
Paints watercolors as a hobby.
Her sister lives with psoriasis.
Sees a dentist yearly.
Uses sunscreen in summer.
In 2006, lipase was 30 U/L.
Her roommate wears contact lenses.
Free T4 of 1.2 ng/dL in 2020.


## 3.27 ('gs202', 'c2', 'negation', 'long') templates=train

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient has ever had angioedema (current or past) or the patient has ever had a stroke or TIA (current or past), prescribe warfarin instead.
CONDITION: stroke/TIA
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
63-year-old man.
Atrial fibrillation; anticoagulation indicated.
Drinks alcohol occasionally.
His mother completed physical therapy for a shoulder injury.
Speech fluent and face symmetric.
Uses public transport.
His coworker wears hearing aids.
His brother-in-law has a fear of heights.
Phosphate 3.6 mg/dL in 2009.
Speaks English and Spanish.
His coworker has a stutter.
Ferritin 60 ng/mL in 2008.
Drinks two cups of coffee a day.
Has a pet dog.
Hearing normal to conversation.
Enjoys cooking.
Vaccinations up to date.
Chloride 103 mmol/L in 2007.
Uses reading glasses for small print.
No puffiness around the eyes or lips.
Albumin 4.1 g/dL in 2016 (routine blood test).

FLIP (answer s'): -Speech fluent and face symmetric. | +Previously had a stroke, in 2010.

NEAR (answer s): -Speech fluent and face symmetric. | +Denies ever having had a stroke or transient ischemic attack.

MISSING (answer neither (undetermined)): -Speech fluent and face symmetric. | +Stroke/TIA: not recorded.

PRES (answer s): full text
Patient: male, 63 years.
Atrial fibrillation; anticoagulation indicated.
Neurological examination unremarkable.
His coworker has a stutter.
Has a pet dog.
Enjoys cooking.
Albumin 4.1 g/dL in 2016 (routine blood test).
Speaks English and Spanish.
Hearing normal to conversation.
His mother completed physical therapy for a shoulder injury.
Chloride 103 mmol/L in 2007.
Phosphate 3.6 mg/dL in 2009.
Drinks two cups of coffee a day.
Lips and tongue normal in size at this assessment.
Drinks alcohol occasionally.
Ferritin 60 ng/mL in 2008.
Uses public transport.
Uses reading glasses for small print.
His coworker wears hearing aids.
Vaccinations up to date.
His brother-in-law has a fear of heights.


## 3.28 ('gs182', 'c1', 'numeric', 'long') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current weight is below 67 kg and the patient is allergic to sulfonamide antibiotics, prescribe warfarin instead.
CONDITION: weight below 67
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Male patient of 70 years.
Atrial fibrillation; anticoagulation indicated.
Sleeps seven hours a night.
Enjoys board games.
Sulfonamide antibiotic allergy: generalized rash.
Drives a car.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Photographs local wildlife.
His sister burned a hand on a stove years ago.
Prefers to be addressed by first name.
Owns a bicycle.
Current weight 78 kg.
Teeth in good repair.
Zinc of 85 mcg/dL in 2016.
In 2020, lipase was 30 U/L.
Plays the piano.
Sees a dentist yearly.
His sister wears contact lenses.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2007, total protein was 7.0 g/dL.
Has two cats.
Knits as a hobby.

FLIP (answer s'): -Current weight 78 kg. | +Current weight 47 kg.

NEAR (answer s): -Current weight 78 kg. | +Current weight 70 kg.

MISSING (answer neither (undetermined)): -Current weight 78 kg.

PRES (answer s): full text
Man of 70 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Has two cats.
Paints watercolors as a hobby.
Prefers morning appointments.
Develops hives whenever given sulfonamide antibiotics.
Drives a car.
Prefers to be addressed by first name.
In 2020, lipase was 30 U/L.
Enjoys board games.
Latest weight 78 kg.
Plays the piano.
During a checkup in 2007, total protein was 7.0 g/dL.
Zinc of 85 mcg/dL in 2016.
Knits as a hobby.
Owns a bicycle.
Sleeps seven hours a night.
Photographs local wildlife.
Lives in a second-floor apartment.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister burned a hand on a stove years ago.
His sister wears contact lenses.


## 3.29 ('gs173', 'c1', 'subject', 'easy') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the patient has had cancer at any time (active or in remission) or the patient has ever had angioedema (current or past), prescribe doxycycline instead.
CONDITION: cancer at any time
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
A 32-year-old woman.
Productive cough and fever; consolidation on chest radiograph.
Writes with the right hand.
Nails normal.
Not undergoing chemotherapy or radiotherapy.
Keeps houseplants.
Bakes bread at home.

FLIP (answer s'): -Not undergoing chemotherapy or radiotherapy. | +Non-Hodgkin lymphoma diagnosed this year, on active treatment.

NEAR (answer s): -Not undergoing chemotherapy or radiotherapy. | +Her brother completed chemotherapy for leukemia in 2019.

MISSING (answer neither (undetermined)): -Not undergoing chemotherapy or radiotherapy. | +Cancer at any time: not recorded.

PRES (answer s): full text
32-year-old woman.
Productive cough and fever; consolidation on chest radiograph.
Bakes bread at home.
Writes with the right hand.
Keeps houseplants.
Nails normal.
No active malignancy.


## 3.30 ('s2_wells_pe', 'hr', 'time', 'easy') templates=test

RULE: Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.
CONDITION: heart rate above 100
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 1.5 points.'

BASE (answer s):
Female patient of 36 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Weight steady over the past year.
Back in 2024, heart rate measured 65/min.
Current heart rate 71/min.
Dry cough, with nothing brought up.
Pupils equal and reactive to light.

FLIP (answer s'): -Current heart rate 71/min. | +Current heart rate 114/min.

NEAR (answer s): -Back in 2024, heart rate measured 65/min. | +Back in 2024, heart rate measured 125/min.

MISSING (answer neither (undetermined)): -Back in 2024, heart rate measured 65/min. | -Current heart rate 71/min.

PRES (answer s): full text
Woman of 36 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Records from 2024 list heart rate at 65/min.
Pupils equal and reactive to light.
Sputum colorless on inspection.
Malignant disease: none at present.
Heart rate now 71/min on the monitor.


## 3.31 ('gs186', 'c1', 'boundary', 'easy') templates=train

RULE: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the current serum creatinine is above 2.0 mg/dL; 2 points if the patient currently has heart failure; 1 point if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe acetaminophen instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe naproxen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Patient: male, 67 years.
Knee osteoarthritis with pain on walking.
Breathless on mild exertion because of heart failure.
Nails normal.
Has a mechanical aortic valve.
Creatinine 1.0 mg/dL on this morning's labs.

FLIP (answer s'): -Creatinine 1.0 mg/dL on this morning's labs. | +Creatinine 2.8 mg/dL on this morning's labs.

NEAR (answer s): -Creatinine 1.0 mg/dL on this morning's labs. | +Creatinine 2.0 mg/dL on this morning's labs.

MISSING (answer neither (undetermined)): -Creatinine 1.0 mg/dL on this morning's labs.

PRES (answer s): full text
67-year-old man.
Knee osteoarthritis with pain on walking.
Nails normal.
Chronic heart failure (NYHA class II).
Kidney function today: creatinine 1.0 mg/dL.
Mechanical aortic valve, functioning normally on echocardiography today.


## 3.32 ('gs016', 'c1', 'negation', 'easy') templates=test

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If the patient has ever had coronary artery disease (current or past), prescribe dapagliflozin instead.
CONDITION: coronary artery disease
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Female patient of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Teeth in good repair.
Climbs two flights of stairs without symptoms.
Lives in a second-floor apartment.

FLIP (answer s'): -Climbs two flights of stairs without symptoms. | +Had coronary artery disease, treated with bypass surgery in 2018; recovered well.

NEAR (answer s): -Climbs two flights of stairs without symptoms. | +Never diagnosed with coronary artery disease.

MISSING (answer neither (undetermined)): -Climbs two flights of stairs without symptoms. | +Coronary artery disease: status unclear from the records at hand.

PRES (answer s): full text
Woman of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Chest pain on exertion: none reported.
Teeth in good repair.
Lives in a second-floor apartment.


## 3.33 ('gs167', 'c2', 'numeric', 'easy') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current platelet count is below 150 x10^9/L, prescribe fondaparinux instead.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
86-year-old woman.
First day after elective total hip replacement.
Lives on a quiet street.
Platelet count today: 306 x10^9/L.
Reads most evenings.
Myocardial infarction in 2016; completed cardiac rehabilitation and has had no symptoms since.
Vaccinations up to date.

FLIP (answer s'): -Platelet count today: 306 x10^9/L. | +Platelet count today: 121 x10^9/L.

NEAR (answer s): -Platelet count today: 306 x10^9/L. | +Platelet count today: 157 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count today: 306 x10^9/L.

PRES (answer s): full text
Patient: female, 86 years.
First day after elective total hip replacement.
Lives on a quiet street.
Vaccinations up to date.
Reads most evenings.
Platelets 306 x10^9/L on this morning's blood count.
Myocardial infarction in 2016, treated with a stent.


## 3.34 ('gs138', 'c2', 'subject', 'easy') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the patient is currently taking warfarin or the patient currently has tonsillar exudate, prescribe intravenous piperacillin-tazobactam instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male patient of 83 years.
Suspected chest infection; assessed on the medical ward.
Anticoagulant therapy: none at present.
Tonsils pink and clean on inspection.
Teeth in good repair.
Lives in a second-floor apartment.

FLIP (answer s'): -Tonsils pink and clean on inspection. | +Tonsillar exudate visible on both sides.

NEAR (answer s): -Tonsils pink and clean on inspection. | +His wife currently has a throat infection with tonsillar exudate.

MISSING (answer neither (undetermined)): -Tonsils pink and clean on inspection. | +Tonsillar exudate: status unclear from the records at hand.

PRES (answer s): full text
Man of 83 years.
Suspected chest infection; assessed on the medical ward.
Teeth in good repair.
Tonsils slightly red but clean, without pus.
Lives in a second-floor apartment.
Current anticoagulants: none.


## 3.35 ('s1_spesi', 'hr', 'time', 'long') templates=train

RULE: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.
CONDITION: heart rate at least 110
CLAIMS: s = 'The heart rate criterion contributes 0 points.' | s' = 'The heart rate criterion contributes 1 point.'

BASE (answer s):
Patient: male.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Nails normal.
Bicarbonate 26 mmol/L in 2013 (annual physical).
No active malignancy.
Age today: 64 years.
Albumin 4.1 g/dL in 2010 (routine blood test).
Plays chess online.
Watches football on weekends.
His cousin completed physical therapy for a shoulder injury.
Blood pressure today: 156/98 mmHg.
Wears a seat belt when driving.
TSH 1.6 mIU/L in 2007.
Listens to podcasts.
A routine check in 2013 gave heart rate 73/min.
His neighbor broke a wrist, which has healed.
His coworker has a broken finger in a splint.
Heart rate 74/min at rest this morning.
Height 170 cm.
Grows tomatoes in the garden.
Oxygen saturation 95% at rest today.
Non-smoker.
His husband is nearsighted.

FLIP (answer s'): -Heart rate 74/min at rest this morning. | +Heart rate 130/min at rest this morning.

NEAR (answer s): -A routine check in 2013 gave heart rate 73/min. | +A routine check in 2013 gave heart rate 138/min.

MISSING (answer neither (undetermined)): -A routine check in 2013 gave heart rate 73/min. | -Heart rate 74/min at rest this morning.

PRES (answer s): full text
Male patient.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
His neighbor broke a wrist, which has healed.
Watches football on weekends.
His husband is nearsighted.
Nails normal.
Not undergoing chemotherapy or radiotherapy.
Plays chess online.
Listens to podcasts.
Oxygen saturation by finger probe today: 95%.
Grows tomatoes in the garden.
Heart rate of 73/min recorded in 2013.
Albumin 4.1 g/dL in 2010 (routine blood test).
Age on arrival: 64 years.
TSH 1.6 mIU/L in 2007.
Heart rate today: 74/min.
Wears a seat belt when driving.
His coworker has a broken finger in a splint.
Height 170 cm.
His cousin completed physical therapy for a shoulder injury.
Non-smoker.
Bicarbonate 26 mmol/L in 2013 (annual physical).
Systolic blood pressure 156 mmHg at this assessment.


## 3.36 ('gs221', 'c1', 'boundary', 'long') templates=test

RULE: For musculoskeletal pain, prescribe ibuprofen. If the current eGFR is below 30 mL/min/1.73 m2 and the patient currently has asthma, prescribe acetaminophen instead.
CONDITION: eGFR below 30
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe acetaminophen.'

BASE (answer s):
Woman of 46 years.
Acute low back pain after lifting.
Prefers morning appointments.
Paints watercolors as a hobby.
Current eGFR 48 mL/min/1.73 m2.
Persistent asthma, using a rescue inhaler most weeks.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2024.
Her roommate sprained a thumb last month.
Enjoys board games.
Her sister burned a hand on a stove years ago.
Has two cats.
Photographs local wildlife.
Sees a dentist yearly.
Uses sunscreen in summer.
Sleeps seven hours a night.
Owns a bicycle.
During a checkup in 2006, free T3 was 3.2 pg/mL.
Drives a car.
Plays the piano.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2018.

FLIP (answer s'): -Current eGFR 48 mL/min/1.73 m2. | +Current eGFR 26 mL/min/1.73 m2.

NEAR (answer s): -Current eGFR 48 mL/min/1.73 m2. | +Current eGFR 30 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Current eGFR 48 mL/min/1.73 m2.

PRES (answer s): full text
Female patient of 46 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2018.
Drives a car.
Owns a bicycle.
Asthma, on a daily inhaled steroid.
Pupils equal and reactive to light.
Her sister burned a hand on a stove years ago.
eGFR now 48 mL/min/1.73 m2.
Prefers morning appointments.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2024.
Uses sunscreen in summer.
Teeth in good repair.
Paints watercolors as a hobby.
During a checkup in 2006, free T3 was 3.2 pg/mL.
Enjoys board games.
Plays the piano.
Photographs local wildlife.
Sleeps seven hours a night.
Her roommate sprained a thumb last month.
Has two cats.


## 3.37 ('gs242', 'c1', 'negation', 'long') templates=train

RULE: For acute sore throat, prescribe ibuprofen. Score 3 points if the patient currently has tonsillar exudate; 3 points if the current heart rate is 110/min or more; 3 points if the patient currently has a major bleed; 2 points if the patient currently has asthma. If the score is 7 or more, prescribe penicillin V instead.
CONDITION: tonsillar exudate
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
19-year-old woman.
Sore throat for two days.
Drinks two cups of coffee a day.
Collects postcards.
Plays chess online.
Volunteers at a library.
Feeds birds in the backyard.
Vitamin B12 450 pg/mL in 2024.
Her husband broke a wrist, which has healed.
Wears a seat belt when driving.
Enjoys gardening.
No melena or hematemesis.
Speaks English and Spanish.
Uses a smartphone for reminders.
Heart rate counted over a full minute at this assessment: 139/min.
Magnesium 2.0 mg/dL in 2024.
Throat mildly red; tonsils not coated.
Has asthma and wakes at night with wheeze.
Listens to podcasts.
Lives on a quiet street.
TSH 1.6 mIU/L in 2024.
Her mother has a fear of heights.

FLIP (answer s'): -Throat mildly red; tonsils not coated. | +Patchy exudate over the right tonsil.

NEAR (answer s): -Throat mildly red; tonsils not coated. | +There is no exudate over the tonsils this morning.

MISSING (answer neither (undetermined)): -Throat mildly red; tonsils not coated. | +Tonsillar exudate: not documented in the records available.

PRES (answer s): full text
Female, 19 years.
Sore throat for two days.
Speaks English and Spanish.
No pus or white patches on the tonsils.
TSH 1.6 mIU/L in 2024.
Vitamin B12 450 pg/mL in 2024.
Volunteers at a library.
Wears a seat belt when driving.
Collects postcards.
Plays chess online.
Enjoys gardening.
Conjunctivae pink, with no pallor.
Uses a smartphone for reminders.
Her husband broke a wrist, which has healed.
Lives on a quiet street.
Asthma attack this month needing nebulizers; still wheezy at this assessment.
Her mother has a fear of heights.
Drinks two cups of coffee a day.
Listens to podcasts.
Heart rate 139/min at rest this morning.
Magnesium 2.0 mg/dL in 2024.
Feeds birds in the backyard.


## 3.38 ('gs194', 'c1', 'numeric', 'easy') templates=test

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the current white cell count is below 4.0 x10^9/L or the patient is currently taking clarithromycin, prescribe sitagliptin instead.
CONDITION: white cell count below 4.0
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Male patient of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Latest WBC is 10.2 x10^9/L.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Has two cats.

FLIP (answer s'): -Latest WBC is 10.2 x10^9/L. | +Latest WBC is 2.6 x10^9/L.

NEAR (answer s): -Latest WBC is 10.2 x10^9/L. | +Latest WBC is 4.7 x10^9/L.

MISSING (answer neither (undetermined)): -Latest WBC is 10.2 x10^9/L.

PRES (answer s): full text
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Uses sunscreen in summer.
Current white cell count 10.2 x10^9/L.
Has two cats.
Pupils equal and reactive to light.


## 3.39 ('gs038', 'c1', 'subject', 'long') templates=train

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the patient has an active peptic ulcer and the patient has new confusion, prescribe intravenous co-amoxiclav instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
Patient: female, 80 years.
Community-acquired pneumonia confirmed on chest radiograph.
Listens to podcasts.
Enjoys cooking.
Height 170 cm.
Uses public transport.
Drinks plenty of water.
Lives on a quiet street.
Reads most evenings.
Eats a varied diet.
Her neighbor has a chipped front tooth.
Sodium 140 mmol/L in 2006.
Watches football on weekends.
Her housemate is being treated for eczema.
Non-smoker.
Keeps houseplants.
Her housemate is left-handed.
Total bilirubin 0.6 mg/dL in 2013.
Has a pet dog.
Uses reading glasses for small print.
Acute confusional state at this assessment.
Nails normal.

FLIP (answer s'): +Taking omeprazole for a gastric ulcer diagnosed at endoscopy this week.

NEAR (answer s): +Her cousin was found to have a stomach ulcer this week.

MISSING (answer neither (undetermined)): +Active peptic ulcer: not asked about.

PRES (answer s): full text
Female, 80 years.
Community-acquired pneumonia confirmed on chest radiograph.
Her neighbor has a chipped front tooth.
Lives on a quiet street.
Total bilirubin 0.6 mg/dL in 2013.
Reads most evenings.
Watches football on weekends.
Keeps houseplants.
Enjoys cooking.
Non-smoker.
Uses public transport.
Has a pet dog.
Sodium 140 mmol/L in 2006.
Her housemate is left-handed.
Nails normal.
Uses reading glasses for small print.
Listens to podcasts.
Eats a varied diet.
Height 170 cm.
Acutely confused, per family.
Drinks plenty of water.
Her housemate is being treated for eczema.


## 3.40 ('news2_red', 'sbp', 'time', 'long') templates=test

RULE: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.
CONDITION: systolic blood pressure at or below 90
CLAIMS: s = 'The systolic blood pressure criterion contributes 0 points.' | s' = 'The systolic blood pressure criterion contributes 3 points.'

BASE (answer s):
Female patient of 43 years.
Shortness of breath and fever; assessed on the medical ward.
Sleeps seven hours a night.
Knits as a hobby.
Her father wears contact lenses.
Latest oxygen saturation reading: 98%.
Prefers morning appointments.
Her wife has a lazy eye.
Lives in a second-floor apartment.
Her friend sprained a thumb last month.
Current respiratory rate 18/min.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Records from 2012 list systolic blood pressure at 109 mmHg.
Teeth in good repair.
Speech clear; follows commands.
In 2014, folate was 12 ng/mL.
Uses sunscreen in summer.
Her uncle burned a hand on a stove years ago.
Enjoys board games.
Photographs local wildlife.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Current systolic blood pressure 142 mmHg.

FLIP (answer s'): -Current systolic blood pressure 142 mmHg. | +Current systolic blood pressure 70 mmHg.

NEAR (answer s): -Records from 2012 list systolic blood pressure at 109 mmHg. | +Records from 2012 list systolic blood pressure at 88 mmHg.

MISSING (answer neither (undetermined)): -Records from 2012 list systolic blood pressure at 109 mmHg. | -Current systolic blood pressure 142 mmHg.

PRES (answer s): full text
Woman of 43 years.
Shortness of breath and fever; assessed on the medical ward.
Lives in a second-floor apartment.
Knits as a hobby.
Her uncle burned a hand on a stove years ago.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Gives a clear account of the illness.
Back in 2012, systolic blood pressure measured 109 mmHg.
Prefers morning appointments.
Enjoys board games.
Teeth in good repair.
Paints watercolors as a hobby.
Her father wears contact lenses.
Observations now: respiratory rate 18/min.
Sleeps seven hours a night.
In 2014, folate was 12 ng/mL.
Her wife has a lazy eye.
Observations now: blood pressure 142/89 mmHg.
Uses sunscreen in summer.
Current oxygen saturation 98%.
Her friend sprained a thumb last month.
Photographs local wildlife.


## 3.41 ('gs082', 'c1', 'boundary', 'easy') templates=train

RULE: For primary prevention, prescribe atorvastatin. If the current white cell count is below 4.0 x10^9/L, prescribe ezetimibe instead.
CONDITION: white cell count below 4.0
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
50-year-old woman.
Primary prevention; LDL cholesterol 182 mg/dL.
White cell count today: 14.6 x10^9/L.
Watches football on weekends.

FLIP (answer s'): -White cell count today: 14.6 x10^9/L. | +White cell count today: 1.9 x10^9/L.

NEAR (answer s): -White cell count today: 14.6 x10^9/L. | +White cell count today: 4.0 x10^9/L.

MISSING (answer neither (undetermined)): -White cell count today: 14.6 x10^9/L.

PRES (answer s): full text
A 50-year-old woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Watches football on weekends.
Complete blood count this morning: white cell count 14.6 x10^9/L.


## 3.42 ('gs165', 'c1', 'negation', 'easy') templates=test

RULE: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe intermittent pneumatic compression instead.
CONDITION: venous thromboembolism in the family
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe intermittent pneumatic compression.'

BASE (answer s):
Female patient of 86 years.
Admitted for community-acquired pneumonia; immobile.
Prefers to be addressed by first name.
Coagulation tests normal on recent bloodwork.

FLIP (answer s'): -Coagulation tests normal on recent bloodwork. | +Ongoing treatment for venous thrombosis of the left arm.

NEAR (answer s): -Coagulation tests normal on recent bloodwork. | +Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.

MISSING (answer neither (undetermined)): -Coagulation tests normal on recent bloodwork. | +Venous thromboembolism in the family: status unclear from the records at hand.

PRES (answer s): full text
Woman of 86 years.
Admitted for community-acquired pneumonia; immobile.
Varicose veins: none seen.
Prefers to be addressed by first name.


## 3.43 ('s2_chads2', 'age', 'numeric', 'long') templates=train

RULE: CHADS2 (as used here): 2 points for a stroke or TIA at any time; 1 point each for heart failure at any time, hypertension at any time, diabetes at any time, and a current age of 75 years or more.
CONDITION: age at least 75
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Adult man.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Age at this assessment: 50 years.
Uses a smartphone for reminders.
Wears a seat belt when driving.
Vitamin D 38 ng/mL in 2023 (wellness visit).
Speaks English and Spanish.
Does crossword puzzles.
His housemate wears hearing aids.
Plays chess online.
Fasting glucose normal on today's blood tests.
Bicarbonate 26 mmol/L in 2019 (annual physical).
Vaccinations up to date.
Volunteers at a library.
Bakes bread at home.
His cousin is being treated for eczema.
Recent echocardiogram normal.
His cousin is nearsighted.
Drinks two cups of coffee a day.
His husband broke a wrist, which has healed.
Eats a varied diet.
Keeps a step counter.

FLIP (answer s'): -Age at this assessment: 50 years. | +Age at this assessment: 81 years.

NEAR (answer s): -Age at this assessment: 50 years. | +Age at this assessment: 74 years.

MISSING (answer neither (undetermined)): -Age at this assessment: 50 years.

PRES (answer s): full text
Patient: male.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Uses a smartphone for reminders.
Speaks English and Spanish.
His housemate wears hearing aids.
Drinks two cups of coffee a day.
Bicarbonate 26 mmol/L in 2019 (annual physical).
His cousin is being treated for eczema.
Keeps a step counter.
His cousin is nearsighted.
Wears a seat belt when driving.
Plays chess online.
Age 50 years, calculated today from the date of birth.
Vitamin D 38 ng/mL in 2023 (wellness visit).
Does crossword puzzles.
Volunteers at a library.
Jugular venous pressure not raised.
Bakes bread at home.
His husband broke a wrist, which has healed.
Urine dipstick shows no sugar.
Vaccinations up to date.
Eats a varied diet.


## 3.44 ('s2_hemorr2hages', 'aspirin', 'subject', 'easy') templates=test

RULE: HEMORR2HAGES score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for active cancer, a current age above 75 years, and current use of aspirin. Other HEMORR2HAGES items are not part of this question.
CONDITION: aspirin use
CLAIMS: s = 'The aspirin use criterion contributes 0 points.' | s' = 'The aspirin use criterion contributes 1 point.'

BASE (answer s):
An adult woman.
Atrial fibrillation; warfarin therapy under consideration.
Antiplatelet therapy: none at present.
Current age 55 years.
Knits as a hobby.
Malignant disease: none at present.
Pupils equal and reactive to light.
Enjoys board games.
Teeth in good repair.
Examination shows no signs of blood loss.

FLIP (answer s'): -Antiplatelet therapy: none at present. | +Currently on low-dose aspirin for heart protection.

NEAR (answer s): -Antiplatelet therapy: none at present. | +Her uncle uses a daily aspirin for heart protection.

MISSING (answer neither (undetermined)): -Antiplatelet therapy: none at present. | +Aspirin use: unknown.

PRES (answer s): full text
Woman, adult.
Atrial fibrillation; warfarin therapy under consideration.
Weight steady over the past year.
Teeth in good repair.
Bowel habit normal, without any blood in the stool.
Currently aged 55 years.
Knits as a hobby.
Pupils equal and reactive to light.
Current antiplatelet drugs: none.
Enjoys board games.


## 3.45 ('gs231', 'c1', 'time', 'long') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 2 points if the current respiratory rate is above 20/min; 2 points if the current serum potassium is above 4.5 mmol/L; 3 points if the patient has ever had heparin-induced thrombocytopenia (current or past); 2 points if the current blood urea nitrogen is 21 mg/dL or more. If the score is 6 or more, prescribe azithromycin instead.
CONDITION: respiratory rate above 20
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Female, 63 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Hearing normal to conversation.
Drinks two cups of coffee a day.
Her mother wears hearing aids.
Has a pet dog.
Speaks English and Spanish.
A routine check in 2019 gave respiratory rate 13/min.
Her housemate has a fear of heights.
Uses public transport.
Potassium 5.2 mmol/L on today's blood work.
Magnesium 2.0 mg/dL in 2007.
Vaccinations up to date.
BUN on today's chemistry panel: 24 mg/dL.
Uses reading glasses for small print.
Collects postcards.
Keeps a step counter.
Plays chess online.
Uses a smartphone for reminders.
Not on any blood thinner at present.
Total bilirubin 0.6 mg/dL in 2024.
Nails normal.
Respiratory rate 14/min this morning.
Grows tomatoes in the garden.

FLIP (answer s'): -Respiratory rate 14/min this morning. | +Respiratory rate 27/min this morning.

NEAR (answer s): -A routine check in 2019 gave respiratory rate 13/min. | +A routine check in 2019 gave respiratory rate 23/min.

MISSING (answer neither (undetermined)): -A routine check in 2019 gave respiratory rate 13/min. | -Respiratory rate 14/min this morning.

PRES (answer s): full text
63-year-old woman.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Uses public transport.
Her mother wears hearing aids.
Respiratory rate, counted over a full minute today, is 14/min.
Uses a smartphone for reminders.
Keeps a step counter.
BUN at this assessment: 24 mg/dL.
Plays chess online.
Nails normal.
Drinks two cups of coffee a day.
Grows tomatoes in the garden.
Her housemate has a fear of heights.
In 2019, respiratory rate was 13/min.
Serum potassium today: 5.2 mmol/L.
Total bilirubin 0.6 mg/dL in 2024.
Magnesium 2.0 mg/dL in 2007.
Collects postcards.
Speaks English and Spanish.
Uses reading glasses for small print.
Vaccinations up to date.
Has a pet dog.
Heparin has not been started.
Hearing normal to conversation.


## 3.46 ('gs015', 'c1', 'boundary', 'long') templates=test

RULE: For primary prevention, prescribe atorvastatin. Score 2 points if the current platelet count is below 50 x10^9/L; 3 points if the patient has ever had asthma (current or past); 3 points if the patient has ever had heart failure (current or past). If the score is 5 or more, prescribe ezetimibe instead.
CONDITION: platelet count below 50
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Female patient of 42 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Her wife has a lazy eye.
Sleeps seven hours a night.
Prefers morning appointments.
In 2022, lipase was 30 U/L.
Platelet count now 305 x10^9/L.
Her wife has recovered from a dislocated finger.
Lives in a second-floor apartment.
Enjoys board games.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2023.
Teeth in good repair.
During a checkup in 2023, total protein was 7.0 g/dL.
Her father sprained a thumb last month.
Prefers to be addressed by first name.
Drives a car.
Her roommate wears contact lenses.
In 2016, folate was 12 ng/mL.
Has heart failure, treated with diuretics.
Plays the piano.

FLIP (answer s'): -Platelet count now 305 x10^9/L. | +Platelet count now 29 x10^9/L.

NEAR (answer s): -Platelet count now 305 x10^9/L. | +Platelet count now 50 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count now 305 x10^9/L.

PRES (answer s): full text
Woman of 42 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Free T4 of 1.2 ng/dL in 2023.
Prefers morning appointments.
Sleeps seven hours a night.
Owns a bicycle.
Current heart failure with ankle swelling.
Her father sprained a thumb last month.
Her wife has recovered from a dislocated finger.
Current platelet count 305 x10^9/L.
Prefers to be addressed by first name.
Her wife has a lazy eye.
Lives in a second-floor apartment.
In 2016, folate was 12 ng/mL.
Plays the piano.
Drives a car.
Her roommate wears contact lenses.
In 2022, lipase was 30 U/L.
Enjoys board games.
Teeth in good repair.
During a checkup in 2023, total protein was 7.0 g/dL.


## 3.47 ('gs110', 'c1', 'negation', 'long') templates=train

RULE: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the patient has had a major bleeding event at any time, prescribe aspirin plus clopidogrel instead.
CONDITION: bleeding history
CLAIMS: s = 'Prescribe aspirin plus ticagrelor.' | s' = 'Prescribe aspirin plus clopidogrel.'

BASE (answer s):
A 49-year-old man.
Recovering on the ward after a myocardial infarction treated with a stent.
Watches football on weekends.
His aunt has a stutter.
Feeds birds in the backyard.
Albumin 4.1 g/dL in 2021 (routine blood test).
Lives on a quiet street.
His mother wears hearing aids.
His brother has a chipped front tooth.
Grows tomatoes in the garden.
Height 170 cm.
Chloride 103 mmol/L in 2015.
Speaks English and Spanish.
Phosphate 3.6 mg/dL in 2013.
Hearing normal to conversation.
Drinks alcohol occasionally.
Bicarbonate 26 mmol/L in 2015 (annual physical).

FLIP (answer s'): +Previously transfused for a major bleed from a stomach ulcer, which healed in 2005.

NEAR (answer s): +Denies any major bleeding, past or present.

MISSING (answer neither (undetermined)): +Information on bleeding history was not obtained.

PRES (answer s): full text
Male, 49 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Feeds birds in the backyard.
Phosphate 3.6 mg/dL in 2013.
Lives on a quiet street.
Bicarbonate 26 mmol/L in 2015 (annual physical).
Albumin 4.1 g/dL in 2021 (routine blood test).
His mother wears hearing aids.
Drinks alcohol occasionally.
Watches football on weekends.
His brother has a chipped front tooth.
His aunt has a stutter.
Hearing normal to conversation.
Grows tomatoes in the garden.
Chloride 103 mmol/L in 2015.
Height 170 cm.
Speaks English and Spanish.


## 3.48 ('gs121', 'c1', 'numeric', 'long') templates=test

RULE: For community-acquired pneumonia, prescribe oral amoxicillin. If the current calf swelling compared with the other leg is 3.0 cm or more or the patient has ever had a peptic ulcer (current or past), prescribe intravenous co-amoxiclav instead.
CONDITION: calf swelling at least 3.0
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous co-amoxiclav.'

BASE (answer s):
Woman of 41 years.
Community-acquired pneumonia confirmed on chest radiograph.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2015.
Zinc of 85 mcg/dL in 2006.
In 2024, folate was 12 ng/mL.
Her roommate wears contact lenses.
Prefers morning appointments.
Pupils equal and reactive to light.
Has two cats.
Her friend lives with psoriasis.
Enjoys board games.
Her uncle has a lazy eye.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Plays the piano.
Sees a dentist yearly.
Her roommate sprained a thumb last month.
Teeth in good repair.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
Drives a car.
Current calf swelling 1.3 cm compared with the other leg.

FLIP (answer s'): -Current calf swelling 1.3 cm compared with the other leg. | +Current calf swelling 3.0 cm compared with the other leg.

NEAR (answer s): -Current calf swelling 1.3 cm compared with the other leg. | +Current calf swelling 2.4 cm compared with the other leg.

MISSING (answer neither (undetermined)): -Current calf swelling 1.3 cm compared with the other leg.

PRES (answer s): full text
Female patient of 41 years.
Community-acquired pneumonia confirmed on chest radiograph.
Calf swelling now amounts to 1.3 cm of extra girth in the larger calf.
Has two cats.
Her roommate wears contact lenses.
Prefers to be addressed by first name.
Her friend lives with psoriasis.
Plays the piano.
Enjoys board games.
Pupils equal and reactive to light.
Her roommate sprained a thumb last month.
Zinc of 85 mcg/dL in 2006.
Free T4 of 1.2 ng/dL in 2015.
Photographs local wildlife.
In 2024, folate was 12 ng/mL.
Knits as a hobby.
Paints watercolors as a hobby.
Prefers morning appointments.
Drives a car.
Her uncle has a lazy eye.
Sees a dentist yearly.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Teeth in good repair.


## 3.49 ('gs078', 'c1', 'subject', 'long') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the patient currently has a venous thromboembolism; the patient currently has a major bleed; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
A 70-year-old woman.
Suspected chest infection; assessed on the medical ward.
Grows tomatoes in the garden.
Vitamin D 38 ng/mL in 2009 (wellness visit).
Collects postcards.
Drinks two cups of coffee a day.
Albumin 4.1 g/dL in 2016 (routine blood test).
Uses reading glasses for small print.
Her partner has a broken finger in a splint.
Hearing normal to conversation.
Drinks alcohol occasionally.
Keeps houseplants.
Her neighbor is being treated for eczema.
Coronary artery disease, with angina when walking uphill.
Uses public transport.
Her brother has a fear of heights.
Conjunctivae pink, with no pallor.
TSH 1.6 mIU/L in 2009.
Sings in a weekly choir.
Writes with the right hand.
Lives on a quiet street.
No known blood clotting disorder.
Phosphate 3.6 mg/dL in 2015.
Volunteers at a library.
Enjoys cooking.

FLIP (answer s'): -No known blood clotting disorder. | +Has a deep vein thrombosis and takes apixaban twice daily.

NEAR (answer s): -No known blood clotting disorder. | +Her neighbor has a DVT confirmed on ultrasound today.

MISSING (answer neither (undetermined)): -No known blood clotting disorder. | +Information on current venous thromboembolism was not obtained.

PRES (answer s): full text
Patient: female, 70 years.
Suspected chest infection; assessed on the medical ward.
Enjoys cooking.
Uses public transport.
Drinks alcohol occasionally.
TSH 1.6 mIU/L in 2009.
Grows tomatoes in the garden.
Volunteers at a library.
Uses reading glasses for small print.
Hearing normal to conversation.
Vitamin D 38 ng/mL in 2009 (wellness visit).
Coronary artery disease with stable angina.
Drinks two cups of coffee a day.
Lives on a quiet street.
Her partner has a broken finger in a splint.
Sings in a weekly choir.
Albumin 4.1 g/dL in 2016 (routine blood test).
Collects postcards.
Writes with the right hand.
Hemoglobin normal on today's blood count.
Takes no anticoagulant medicines.
Her brother has a fear of heights.
Her neighbor is being treated for eczema.
Phosphate 3.6 mg/dL in 2015.
Keeps houseplants.


## 3.50 ('s2_orbit', 'egfr', 'time', 'easy') templates=test

RULE: ORBIT bleeding score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for a current age of 75 years or more, a current eGFR below 60 mL/min/1.73 m2, and current use of aspirin. Other ORBIT items are not part of this question.
CONDITION: eGFR below 60
CLAIMS: s = 'The eGFR criterion contributes 0 points.' | s' = 'The eGFR criterion contributes 1 point.'

BASE (answer s):
Woman, adult.
Atrial fibrillation; starting apixaban is being considered.
Current eGFR 98 mL/min/1.73 m2.
Examination shows no signs of blood loss.
Back in 2019, eGFR measured 78 mL/min/1.73 m2.
Enjoys board games.
Current age 62 years.

FLIP (answer s'): -Current eGFR 98 mL/min/1.73 m2. | +Current eGFR 55 mL/min/1.73 m2.

NEAR (answer s): -Back in 2019, eGFR measured 78 mL/min/1.73 m2. | +Back in 2019, eGFR measured 53 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Current eGFR 98 mL/min/1.73 m2. | -Back in 2019, eGFR measured 78 mL/min/1.73 m2.

PRES (answer s): full text
An adult woman.
Atrial fibrillation; starting apixaban is being considered.
Enjoys board games.
Currently aged 62 years.
eGFR now 98 mL/min/1.73 m2.
Records from 2019 list eGFR at 78 mL/min/1.73 m2.
Bowel habit normal, without any blood in the stool.


## 3.51 ('gs167', 'c2', 'boundary', 'long') templates=train

RULE: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current platelet count is below 150 x10^9/L, prescribe fondaparinux instead.
CONDITION: platelet count below 150
CLAIMS: s = 'Prescribe enoxaparin.' | s' = 'Prescribe fondaparinux.'

BASE (answer s):
Male, 81 years.
First day after elective total hip replacement.
Height 170 cm.
Does crossword puzzles.
Lives on a quiet street.
His partner has a chipped front tooth.
Nails normal.
Hearing normal to conversation.
Platelet count at this assessment: 249 x10^9/L.
Enjoys gardening.
Listens to podcasts.
Drinks two cups of coffee a day.
Grows tomatoes in the garden.
Vaccinations up to date.
Peripheral artery disease with calf claudication.
Total bilirubin 0.6 mg/dL in 2017.
His neighbor previously wore dental braces.
Phosphate 3.6 mg/dL in 2017.
Has a pet dog.
Writes with the right hand.
Sings in a weekly choir.
Volunteers at a library.
Speaks English and Spanish.
Wears a seat belt when driving.

FLIP (answer s'): -Platelet count at this assessment: 249 x10^9/L. | +Platelet count at this assessment: 83 x10^9/L.

NEAR (answer s): -Platelet count at this assessment: 249 x10^9/L. | +Platelet count at this assessment: 150 x10^9/L.

MISSING (answer neither (undetermined)): -Platelet count at this assessment: 249 x10^9/L.

PRES (answer s): full text
81-year-old man.
First day after elective total hip replacement.
Nails normal.
Lives on a quiet street.
Hearing normal to conversation.
Listens to podcasts.
Vaccinations up to date.
Speaks English and Spanish.
Grows tomatoes in the garden.
Enjoys gardening.
Sings in a weekly choir.
Phosphate 3.6 mg/dL in 2017.
Platelet count today: 249 x10^9/L.
Has peripheral artery disease.
Volunteers at a library.
Has a pet dog.
Total bilirubin 0.6 mg/dL in 2017.
Drinks two cups of coffee a day.
Height 170 cm.
Does crossword puzzles.
Wears a seat belt when driving.
His neighbor previously wore dental braces.
Writes with the right hand.
His partner has a chipped front tooth.


## 3.52 ('gs218', 'c1', 'negation', 'easy') templates=test

RULE: For primary prevention, prescribe atorvastatin. If the patient is allergic to sulfonamide antibiotics, prescribe ezetimibe instead.
CONDITION: sulfonamide allergy
CLAIMS: s = 'Prescribe atorvastatin.' | s' = 'Prescribe ezetimibe.'

BASE (answer s):
Male patient of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Medication allergies: none at present.
Sees a dentist yearly.
Pupils equal and reactive to light.

FLIP (answer s'): -Medication allergies: none at present. | +Develops hives whenever given sulfonamide antibiotics.

NEAR (answer s): -Medication allergies: none at present. | +Has never been allergic to sulfonamide antibiotics.

MISSING (answer neither (undetermined)): -Medication allergies: none at present. | +Sulfonamide allergy: status unclear from the records at hand.

PRES (answer s): full text
Man of 44 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Current drug allergies: none.
Pupils equal and reactive to light.


## 3.53 ('s4_improve_vte', 'age', 'numeric', 'long') templates=train

RULE: IMPROVE VTE risk score (as used here, partial): 3 points for a venous thromboembolism of the patient at any time (current or previous); 2 points for active cancer; 1 point for age above 60 years. Other IMPROVE items are not part of this question.
CONDITION: age above 60
CLAIMS: s = 'The age criterion contributes 0 points.' | s' = 'The age criterion contributes 1 point.'

BASE (answer s):
Sex: male.
Admitted to the medical ward with cellulitis of the left leg; mostly in bed.
Collects postcards.
Feeds birds in the backyard.
Hearing normal to conversation.
No evidence of active neoplasia.
His cousin completed physical therapy for a shoulder injury.
Uses public transport.
Writes with the right hand.
Plays chess online.
Listens to podcasts.
Does crossword puzzles.
Speaks English and Spanish.
Not on any blood thinners.
Age at this assessment: 45 years.
Vitamin D 38 ng/mL in 2018 (wellness visit).
His mother previously wore dental braces.
Ferritin 60 ng/mL in 2008.
Uses a smartphone for reminders.
Vaccinations up to date.
Enjoys cooking.

FLIP (answer s'): -Age at this assessment: 45 years. | +Age at this assessment: 73 years.

NEAR (answer s): -Age at this assessment: 45 years. | +Age at this assessment: 59 years.

MISSING (answer neither (undetermined)): -Age at this assessment: 45 years.

PRES (answer s): full text
Patient: male.
Admitted to the medical ward with cellulitis of the left leg; mostly in bed.
Collects postcards.
Vaccinations up to date.
Does crossword puzzles.
Uses a smartphone for reminders.
Plays chess online.
His mother previously wore dental braces.
Uses public transport.
Speaks English and Spanish.
Vitamin D 38 ng/mL in 2018 (wellness visit).
Ferritin 60 ng/mL in 2008.
Not undergoing chemotherapy or radiotherapy.
Writes with the right hand.
Age today: 45 years.
His cousin completed physical therapy for a shoulder injury.
Listens to podcasts.
Hearing normal to conversation.
Enjoys cooking.
Takes no anticoagulant medicines.
Feeds birds in the backyard.


## 3.54 ('gs074', 'c2', 'subject', 'long') templates=test

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current temperature is above 38.0 C and the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe intravenous piperacillin-tazobactam instead.
CONDITION: vascular disease
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
Male patient of 43 years.
Suspected chest infection; assessed on the medical ward.
Plays the piano.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Has two cats.
His roommate sprained a thumb last month.
Enjoys board games.
His sister burned a hand on a stove years ago.
In 2023, folate was 12 ng/mL.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current temperature 38.6 C.
Knits as a hobby.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2018.
Photographs local wildlife.
Lives in a second-floor apartment.
During a checkup in 2014, free T3 was 3.2 pg/mL.
His friend has recovered from a dislocated finger.
Walks without calf pain.

FLIP (answer s'): -Walks without calf pain. | +Heart attack years ago, with full recovery.

NEAR (answer s): -Walks without calf pain. | +His friend has peripheral artery disease with leg pain.

MISSING (answer neither (undetermined)): -Walks without calf pain. | +Vascular disease: status unclear from the records at hand.

PRES (answer s): full text
Man of 43 years.
Suspected chest infection; assessed on the medical ward.
Pupils equal and reactive to light.
His sister burned a hand on a stove years ago.
His friend has recovered from a dislocated finger.
Prefers morning appointments.
Uses sunscreen in summer.
In 2023, folate was 12 ng/mL.
Photographs local wildlife.
Plays the piano.
Temperature now 38.6 C (tympanic).
Prefers to be addressed by first name.
Has two cats.
His roommate sprained a thumb last month.
Zinc of 85 mcg/dL in 2018.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Knits as a hobby.
Paints watercolors as a hobby.
Ankle-brachial index normal today.
Enjoys board games.
Lives in a second-floor apartment.


## 3.55 ('curb65', 'rr', 'time', 'long') templates=train

RULE: CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
CONDITION: respiratory rate at least 30
CLAIMS: s = 'The respiratory rate criterion contributes 0 points.' | s' = 'The respiratory rate criterion contributes 1 point.'

BASE (answer s):
Patient: male.
Community-acquired pneumonia confirmed on chest radiograph.
Nails normal.
Respiratory rate today: 17/min.
Vitamin B12 450 pg/mL in 2021.
Albumin 4.1 g/dL in 2017 (routine blood test).
Uses a smartphone for reminders.
Volunteers at a library.
Drinks alcohol occasionally.
His coworker has a stutter.
His neighbor has a fear of heights.
Listens to podcasts.
Wears a seat belt when driving.
Uses public transport.
A routine check in 2012 gave respiratory rate 22/min.
Alert and attentive.
Keeps a step counter.
Speaks English and Spanish.
His aunt has a chipped front tooth.
His husband wears hearing aids.
Lives on a quiet street.
Today's BUN is 17 mg/dL.
Watches football on weekends.
Age today: 46 years.
Manual cuff blood pressure today: 126/80 mmHg.
Magnesium 2.0 mg/dL in 2006.
Feeds birds in the backyard.
Hearing normal to conversation.

FLIP (answer s'): -Respiratory rate today: 17/min. | +Respiratory rate today: 35/min.

NEAR (answer s): -A routine check in 2012 gave respiratory rate 22/min. | +A routine check in 2012 gave respiratory rate 39/min.

MISSING (answer neither (undetermined)): -Respiratory rate today: 17/min. | -A routine check in 2012 gave respiratory rate 22/min.

PRES (answer s): full text
Adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Volunteers at a library.
Uses a smartphone for reminders.
Albumin 4.1 g/dL in 2017 (routine blood test).
His husband wears hearing aids.
Wears a seat belt when driving.
Feeds birds in the backyard.
BUN at this assessment: 17 mg/dL.
Watches football on weekends.
Hearing normal to conversation.
His coworker has a stutter.
Respiratory rate 22/min at a clinic visit in 2012.
Drinks alcohol occasionally.
Age 46 years, calculated today from the date of birth.
Blood pressure 126/80 mmHg this morning.
Nails normal.
His neighbor has a fear of heights.
Memory and concentration normal on bedside testing.
Uses public transport.
Vitamin B12 450 pg/mL in 2021.
Lives on a quiet street.
Magnesium 2.0 mg/dL in 2006.
Listens to podcasts.
Keeps a step counter.
Speaks English and Spanish.
His aunt has a chipped front tooth.
Respiratory rate 17/min this morning.


## 3.56 ('rcri', 'cr', 'boundary', 'easy') templates=test

RULE: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 2.0 mg/dL. Other items are not part of this question.
CONDITION: creatinine above 2.0
CLAIMS: s = 'The creatinine criterion contributes 0 points.' | s' = 'The creatinine criterion contributes 1 point.'

BASE (answer s):
Woman of 74 years.
Preoperative assessment before elective colectomy.
Climbs two flights of stairs without symptoms.
Latest creatinine result: 1.3 mg/dL.
Uses sunscreen in summer.
Plays the piano.
Sleeps flat on one pillow.
Has two cats.
Photographs local wildlife.

FLIP (answer s'): -Latest creatinine result: 1.3 mg/dL. | +Latest creatinine result: 3.6 mg/dL.

NEAR (answer s): -Latest creatinine result: 1.3 mg/dL. | +Latest creatinine result: 2.0 mg/dL.

MISSING (answer neither (undetermined)): -Latest creatinine result: 1.3 mg/dL.

PRES (answer s): full text
Female patient of 74 years.
Preoperative assessment before elective colectomy.
Has two cats.
Uses sunscreen in summer.
Current serum creatinine 1.3 mg/dL.
Heart sounds without a gallop.
Photographs local wildlife.
Chest pain on exertion: none reported.
Plays the piano.


## 3.57 ('gs078', 'c1', 'negation', 'easy') templates=train

RULE: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the patient currently has a venous thromboembolism; the patient currently has a major bleed; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
CONDITION: current venous thromboembolism
CLAIMS: s = 'Prescribe oral amoxicillin.' | s' = 'Prescribe intravenous piperacillin-tazobactam.'

BASE (answer s):
A 66-year-old woman.
Suspected chest infection; assessed on the medical ward.
No known blood clotting disorder.
Uses public transport.
Keeps houseplants.
Vomiting large amounts of blood today from a major bleed in the esophagus.

FLIP (answer s'): -No known blood clotting disorder. | +Has a deep vein thrombosis and takes apixaban twice daily.

NEAR (answer s): -No known blood clotting disorder. | +Medical records show no venous thromboembolism, and none is reported in first-degree relatives.

MISSING (answer neither (undetermined)): -No known blood clotting disorder. | +Current venous thromboembolism: not recorded.

PRES (answer s): full text
Patient: female, 66 years.
Suspected chest infection; assessed on the medical ward.
Not on any blood thinners.
Uses public transport.
Active major upper gastrointestinal bleed, requiring blood transfusion.
Keeps houseplants.


## 3.58 ('rcri', 'cr', 'numeric', 'easy') templates=test

RULE: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 2.0 mg/dL. Other items are not part of this question.
CONDITION: creatinine above 2.0
CLAIMS: s = 'The creatinine criterion contributes 0 points.' | s' = 'The creatinine criterion contributes 1 point.'

BASE (answer s):
Female patient of 79 years.
Preoperative assessment before elective colectomy.
Gait normal; no focal weakness.
Latest creatinine result: 0.7 mg/dL.
Chest pain on exertion: none reported.
Prefers morning appointments.

FLIP (answer s'): -Latest creatinine result: 0.7 mg/dL. | +Latest creatinine result: 4.1 mg/dL.

NEAR (answer s): -Latest creatinine result: 0.7 mg/dL. | +Latest creatinine result: 1.9 mg/dL.

MISSING (answer neither (undetermined)): -Latest creatinine result: 0.7 mg/dL.

PRES (answer s): full text
Woman of 79 years.
Preoperative assessment before elective colectomy.
Power and sensation normal in all limbs.
Current serum creatinine 0.7 mg/dL.
Climbs two flights of stairs without symptoms.
Prefers morning appointments.


## 3.59 ('c2_dvt_pregnancy', 'pregnancy', 'subject', 'easy') templates=train

RULE: For a deep vein thrombosis of the leg, prescribe apixaban. If the patient is currently pregnant, prescribe enoxaparin instead.
CONDITION: pregnancy
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe enoxaparin.'

BASE (answer s):
36-year-old woman.
Painful, swollen left calf; deep vein thrombosis confirmed on ultrasound.
Had a normal period last week.
Speaks English and Spanish.
Drinks alcohol occasionally.
Feeds birds in the backyard.
Enjoys gardening.

FLIP (answer s'): -Had a normal period last week. | +Pregnant, 12 weeks by dates.

NEAR (answer s): -Had a normal period last week. | +Her coworker is 30 weeks pregnant.

MISSING (answer neither (undetermined)): -Had a normal period last week. | +Pregnancy: not recorded.

PRES (answer s): full text
Female, 36 years.
Painful, swollen left calf; deep vein thrombosis confirmed on ultrasound.
Menstruating normally this week.
Drinks alcohol occasionally.
Feeds birds in the backyard.
Speaks English and Spanish.
Enjoys gardening.


## 3.60 ('gs087', 'c1', 'time', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the current temperature is above 38.0 C and the patient has ever had heart failure (current or past), prescribe naproxen with omeprazole instead.
CONDITION: temperature above 38.0
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Woman of 83 years.
Hip osteoarthritis with pain on walking.
Has two cats.
Teeth in good repair.
Temperature now 37.1 C (tympanic).
Sleeps seven hours a night.
Records from 2017 list temperature at 36.8 C.
Current heart failure with ankle swelling.

FLIP (answer s'): -Temperature now 37.1 C (tympanic). | +Temperature now 38.9 C (tympanic).

NEAR (answer s): -Records from 2017 list temperature at 36.8 C. | +Records from 2017 list temperature at 39.2 C.

MISSING (answer neither (undetermined)): -Temperature now 37.1 C (tympanic). | -Records from 2017 list temperature at 36.8 C.

PRES (answer s): full text
Female patient of 83 years.
Hip osteoarthritis with pain on walking.
Current temperature 37.1 C.
Back in 2017, temperature measured 36.8 C.
Has two cats.
Sleeps seven hours a night.
Has heart failure, treated with diuretics.
Teeth in good repair.


## 3.61 ('gs043', 'c1', 'boundary', 'long') templates=train

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the current serum potassium is above 4.5 mmol/L, prescribe amlodipine instead.
CONDITION: serum potassium above 4.5
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Male, 72 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Lives on a quiet street.
His housemate has a stutter.
Total bilirubin 0.6 mg/dL in 2013.
Potassium measured at this assessment is 4.0 mmol/L.
Bakes bread at home.
Vaccinations up to date.
Plays chess online.
TSH 1.6 mIU/L in 2006.
Albumin 4.1 g/dL in 2014 (routine blood test).
Hearing normal to conversation.
Writes with the right hand.
Grows tomatoes in the garden.
Eats a varied diet.
Drinks plenty of water.
His housemate had a splinter removed from a finger.
Serum calcium 9.4 mg/dL in 2016.

FLIP (answer s'): -Potassium measured at this assessment is 4.0 mmol/L. | +Potassium measured at this assessment is 4.7 mmol/L.

NEAR (answer s): -Potassium measured at this assessment is 4.0 mmol/L. | +Potassium measured at this assessment is 4.5 mmol/L.

MISSING (answer neither (undetermined)): -Potassium measured at this assessment is 4.0 mmol/L.

PRES (answer s): full text
A 72-year-old man.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Grows tomatoes in the garden.
Albumin 4.1 g/dL in 2014 (routine blood test).
Vaccinations up to date.
TSH 1.6 mIU/L in 2006.
Lives on a quiet street.
Bakes bread at home.
Serum calcium 9.4 mg/dL in 2016.
Plays chess online.
Hearing normal to conversation.
His housemate has a stutter.
Drinks plenty of water.
Labs this morning: potassium 4.0 mmol/L.
Eats a varied diet.
Writes with the right hand.
His housemate had a splinter removed from a finger.
Total bilirubin 0.6 mg/dL in 2013.


## 3.62 ('gs204', 'c1', 'negation', 'easy') templates=test

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient is currently taking warfarin or the patient has ever had asthma (current or past), prescribe amlodipine instead.
CONDITION: warfarin
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Female patient of 64 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Prefers to be addressed by first name.
Anticoagulant therapy: none at present.
Owns a bicycle.
Inhaler use: none.

FLIP (answer s'): -Anticoagulant therapy: none at present. | +Currently on warfarin, prescribed by the cardiology clinic.

NEAR (answer s): -Anticoagulant therapy: none at present. | +Has never been prescribed warfarin.

MISSING (answer neither (undetermined)): -Anticoagulant therapy: none at present. | +Warfarin: status unclear from the records at hand.

PRES (answer s): full text
Woman of 64 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Current anticoagulants: none.
Lungs clear, without wheeze or prolonged expiration.
Owns a bicycle.
Prefers to be addressed by first name.


## 3.63 ('c1_nitrofurantoin', 'egfr', 'numeric', 'alt') templates=train

RULE: For acute cystitis, prescribe nitrofurantoin. If the current eGFR is below 60 mL/min/1.73 m2, prescribe fosfomycin instead.
CONDITION: eGFR below 60
CLAIMS: s = 'Prescribe nitrofurantoin.' | s' = 'Prescribe fosfomycin.'

BASE (answer s):
Patient: female, 78 years.
Burning on passing urine and urinary frequency for three days; no fever or flank pain.
Renal function today: eGFR 88 mL/min/1.73 m2.
Uses reading glasses for small print.

FLIP (answer s'): -Renal function today: eGFR 88 mL/min/1.73 m2. | +Renal function today: eGFR 49 mL/min/1.73 m2.

NEAR (answer s): -Renal function today: eGFR 88 mL/min/1.73 m2. | +Renal function today: eGFR 61 mL/min/1.73 m2.

MISSING (answer neither (undetermined)): -Renal function today: eGFR 88 mL/min/1.73 m2.

PRES (answer s): full text
Female, 78 years.
Burning on passing urine and urinary frequency for three days; no fever or flank pain.
Uses reading glasses for small print.
This morning's blood test shows an eGFR of 88 mL/min/1.73 m2.


## 3.64 ('af_valve', 'valve', 'subject', 'easy') templates=test

RULE: For stroke prevention in atrial fibrillation, start apixaban. If the patient currently has a mechanical heart valve, start warfarin instead.
CONDITION: mechanical heart valve
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Female patient of 68 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
Pupils equal and reactive to light.
Photographs local wildlife.
Sleeps seven hours a night.

FLIP (answer s'): +Mechanical mitral valve in place; metallic closing clicks audible.

NEAR (answer s): +Her wife has an implanted mechanical aortic valve.

MISSING (answer neither (undetermined)): +Mechanical heart valve: unknown.

PRES (answer s): full text
Woman of 68 years.
Atrial fibrillation; anticoagulation indicated.
Sleeps seven hours a night.
Photographs local wildlife.
Pupils equal and reactive to light.
Knits as a hobby.


## 3.65 ('gs189', 'c1', 'time', 'long') templates=train

RULE: For newly diagnosed type 2 diabetes, prescribe metformin. If the current oxygen saturation is 91% or less, prescribe sitagliptin instead.
CONDITION: oxygen saturation at or below 91
CLAIMS: s = 'Prescribe metformin.' | s' = 'Prescribe sitagliptin.'

BASE (answer s):
Female, 43 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Drinks plenty of water.
Hearing normal to conversation.
Bakes bread at home.
Non-smoker.
Oxygen saturation at this assessment is 97%.
Nails normal.
Grows tomatoes in the garden.
Her husband wears hearing aids.
Feeds birds in the backyard.
Keeps a step counter.
Magnesium 2.0 mg/dL in 2024.
A routine check in 2011 gave oxygen saturation 96%.
Her cousin has a broken finger in a splint.
Drinks alcohol occasionally.
Listens to podcasts.
Her brother previously wore dental braces.
Phosphate 3.6 mg/dL in 2010.
Her mother completed physical therapy for a shoulder injury.
Height 170 cm.
Uses a smartphone for reminders.

FLIP (answer s'): -Oxygen saturation at this assessment is 97%. | +Oxygen saturation at this assessment is 80%.

NEAR (answer s): -A routine check in 2011 gave oxygen saturation 96%. | +A routine check in 2011 gave oxygen saturation 89%.

MISSING (answer neither (undetermined)): -Oxygen saturation at this assessment is 97%. | -A routine check in 2011 gave oxygen saturation 96%.

PRES (answer s): full text
43-year-old woman.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Drinks plenty of water.
Magnesium 2.0 mg/dL in 2024.
Her husband wears hearing aids.
Height 170 cm.
Phosphate 3.6 mg/dL in 2010.
Her mother completed physical therapy for a shoulder injury.
Hearing normal to conversation.
Feeds birds in the backyard.
Nails normal.
Non-smoker.
Listens to podcasts.
Drinks alcohol occasionally.
Grows tomatoes in the garden.
Keeps a step counter.
Uses a smartphone for reminders.
Oxygen saturation of 96% recorded in 2011.
Her cousin has a broken finger in a splint.
Bakes bread at home.
Pulse oximetry this morning: oxygen saturation 97%.
Her brother previously wore dental braces.


## 3.66 ('gs147', 'c3', 'boundary', 'easy') templates=test

RULE: For early Lyme disease, prescribe doxycycline. If at least two of the following apply, prescribe amoxicillin instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient currently has tonsillar exudate; the current ALT is above 200 U/L.
CONDITION: ALT above 200
CLAIMS: s = 'Prescribe doxycycline.' | s' = 'Prescribe amoxicillin.'

BASE (answer s):
Woman of 41 years.
Erythema migrans rash ten days after a tick bite.
Lives with colon cancer and attends an oncology clinic.
Current ALT 69 U/L.
Paints watercolors as a hobby.

FLIP (answer s'): -Current ALT 69 U/L. | +Current ALT 468 U/L.

NEAR (answer s): -Current ALT 69 U/L. | +Current ALT 200 U/L.

MISSING (answer neither (undetermined)): -Current ALT 69 U/L.

PRES (answer s): full text
Female patient of 41 years.
Erythema migrans rash ten days after a tick bite.
Colorectal cancer under active treatment.
Paints watercolors as a hobby.
ALT now 69 U/L.


## 3.67 ('gs052', 'c3', 'negation', 'long') templates=train

RULE: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the current temperature is 41.0 C or more; the current oxygen saturation is 91% or less; the patient has ever had a venous thromboembolism (current or past).
CONDITION: venous thromboembolism
CLAIMS: s = 'Prescribe ibuprofen.' | s' = 'Prescribe penicillin V.'

BASE (answer s):
17-year-old man.
Sore throat for two days.
Lives on a quiet street.
Temperature 41.1 C at this assessment.
His cousin has a fear of heights.
His neighbor is being treated for eczema.
Albumin 4.1 g/dL in 2024 (routine blood test).
Volunteers at a library.
His grandfather completed physical therapy for a shoulder injury.
Drinks alcohol occasionally.
Feeds birds in the backyard.
Uses reading glasses for small print.
Does crossword puzzles.
Wears a seat belt when driving.
Sings in a weekly choir.
Non-smoker.
Total bilirubin 0.6 mg/dL in 2024.
No known blood clotting disorder.
Oxygen saturation at this assessment is 98%.
Enjoys gardening.
Hearing normal to conversation.
Watches football on weekends.
Vitamin D 38 ng/mL in 2024 (wellness visit).
Writes with the right hand.
His grandmother has a chipped front tooth.

FLIP (answer s'): -No known blood clotting disorder. | +Active DVT of the right calf on anticoagulation.

NEAR (answer s): -No known blood clotting disorder. | +Denies any DVT or pulmonary embolism, past or present, personally or in parents, siblings or children.

MISSING (answer neither (undetermined)): -No known blood clotting disorder. | +Venous thromboembolism: not recorded.

PRES (answer s): full text
Male, 17 years.
Sore throat for two days.
His grandfather completed physical therapy for a shoulder injury.
Lives on a quiet street.
Total bilirubin 0.6 mg/dL in 2024.
Uses reading glasses for small print.
Hearing normal to conversation.
Enjoys gardening.
Watches football on weekends.
Feeds birds in the backyard.
Oxygen saturation 98% at rest today.
Vitamin D 38 ng/mL in 2024 (wellness visit).
Non-smoker.
His cousin has a fear of heights.
Wears a seat belt when driving.
Drinks alcohol occasionally.
His neighbor is being treated for eczema.
Volunteers at a library.
Sings in a weekly choir.
Not on any blood thinners.
Albumin 4.1 g/dL in 2024 (routine blood test).
His grandmother has a chipped front tooth.
Oral temperature this morning: 41.1 C.
Writes with the right hand.
Does crossword puzzles.


## 3.68 ('gs040', 'c1', 'numeric', 'easy') templates=test

RULE: For rate control in atrial fibrillation, prescribe metoprolol. Score 2 points if the current ALT is above 120 U/L; 3 points if the age of the patient is above 55 years; 3 points if the patient is currently taking aspirin; 1 point if the patient is allergic to penicillin. If the score is 6 or more, prescribe diltiazem instead.
CONDITION: ALT above 120
CLAIMS: s = 'Prescribe metoprolol.' | s' = 'Prescribe diltiazem.'

BASE (answer s):
Man, adult.
Atrial fibrillation with a ventricular rate of 128/min.
Current ALT 52 U/L.
Lives in a second-floor apartment.
Current age 50 years.
Known penicillin allergy with angioedema.
Currently on low-dose aspirin for heart protection.

FLIP (answer s'): -Current ALT 52 U/L. | +Current ALT 216 U/L.

NEAR (answer s): -Current ALT 52 U/L. | +Current ALT 113 U/L.

MISSING (answer neither (undetermined)): -Current ALT 52 U/L.

PRES (answer s): full text
An adult man.
Atrial fibrillation with a ventricular rate of 128/min.
Currently aged 50 years.
ALT now 52 U/L.
Uses a daily aspirin on a cardiologist's recommendation.
Lives in a second-floor apartment.
Penicillin allergy: anaphylaxis.


## 3.69 ('gs096', 'c1', 'subject', 'easy') templates=train

RULE: For acute streptococcal pharyngitis, prescribe amoxicillin. Score 2 points if the patient currently has a major bleed; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 1 point if the patient has ever had angioedema (current or past); 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past). If the score is 3 or more, prescribe azithromycin instead.
CONDITION: active major bleeding
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe azithromycin.'

BASE (answer s):
Patient: female, 67 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Keeps a step counter.
No hematuria or hemoptysis.
Troponin within the normal range.
Drinks plenty of water.
Not on any blood thinners.
Has hereditary angioedema, with attacks every few months.

FLIP (answer s'): -No hematuria or hemoptysis. | +Ongoing major bleeding from the lower bowel, receiving blood transfusion.

NEAR (answer s): -No hematuria or hemoptysis. | +Her brother-in-law is in the emergency room with a major bleed from a deep cut.

MISSING (answer neither (undetermined)): -No hematuria or hemoptysis. | +Active major bleeding: not documented in the records available.

PRES (answer s): full text
A 67-year-old woman.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Idiopathic angioedema, treated with daily antihistamines.
Drinks plenty of water.
No melena or hematemesis.
Foot pulses easily felt.
Keeps a step counter.
No inherited clotting condition such as factor V Leiden.


## 3.70 ('gs073', 'c2', 'time', 'easy') templates=test

RULE: For hip osteoarthritis pain, prescribe naproxen alone. If the age of the patient is 65 years or more and the current oxygen saturation is 91% or less, prescribe naproxen with omeprazole instead.
CONDITION: oxygen saturation at or below 91
CLAIMS: s = 'Prescribe naproxen alone.' | s' = 'Prescribe naproxen with omeprazole.'

BASE (answer s):
Man, adult.
Hip osteoarthritis with pain on walking.
Currently aged 69 years.
Current oxygen saturation 95%.
Owns a bicycle.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Back in 2007, oxygen saturation measured 100%.

FLIP (answer s'): -Current oxygen saturation 95%. | +Current oxygen saturation 78%.

NEAR (answer s): -Back in 2007, oxygen saturation measured 100%. | +Back in 2007, oxygen saturation measured 83%.

MISSING (answer neither (undetermined)): -Current oxygen saturation 95%. | -Back in 2007, oxygen saturation measured 100%.

PRES (answer s): full text
An adult man.
Hip osteoarthritis with pain on walking.
Latest oxygen saturation reading: 95%.
Records from 2007 list oxygen saturation at 100%.
Current age 69 years.
Prefers to be addressed by first name.
Owns a bicycle.
Pupils equal and reactive to light.


## 3.71 ('sirs', 'rr', 'boundary', 'long') templates=train

RULE: SIRS criteria (as used here, partial): 1 point each for temperature above 38.0 C; heart rate above 90/min; respiratory rate above 20/min; white cell count above 12.0 x10^9/L. Only current findings count.
CONDITION: respiratory rate above 20
CLAIMS: s = 'The respiratory rate criterion contributes 0 points.' | s' = 'The respiratory rate criterion contributes 1 point.'

BASE (answer s):
39-year-old man.
Productive cough for three days; assessed in the emergency department.
Feeds birds in the backyard.
Magnesium 2.0 mg/dL in 2010.
Watches football on weekends.
Keeps houseplants.
His partner is being treated for eczema.
Drinks two cups of coffee a day.
Hearing normal to conversation.
Nails normal.
Temperature today: 36.4 C.
Heart rate 78/min at rest this morning.
Bicarbonate 26 mmol/L in 2005 (annual physical).
Reads most evenings.
His cousin has a fear of heights.
Respiratory rate 12/min this morning.
His cousin has a stutter.
Volunteers at a library.
Albumin 4.1 g/dL in 2005 (routine blood test).
Non-smoker.
Serum calcium 9.4 mg/dL in 2017.
WBC on the blood count drawn at this assessment: 4.8 x10^9/L.
Eats a varied diet.
Speaks English and Spanish.

FLIP (answer s'): -Respiratory rate 12/min this morning. | +Respiratory rate 29/min this morning.

NEAR (answer s): -Respiratory rate 12/min this morning. | +Respiratory rate 20/min this morning.

MISSING (answer neither (undetermined)): -Respiratory rate 12/min this morning.

PRES (answer s): full text
A 39-year-old man.
Productive cough for three days; assessed in the emergency department.
His cousin has a stutter.
His cousin has a fear of heights.
His partner is being treated for eczema.
Speaks English and Spanish.
Non-smoker.
Bicarbonate 26 mmol/L in 2005 (annual physical).
Albumin 4.1 g/dL in 2005 (routine blood test).
Volunteers at a library.
Pulse taken this morning: heart rate 78/min.
Reads most evenings.
Drinks two cups of coffee a day.
Eats a varied diet.
Feeds birds in the backyard.
Keeps houseplants.
White cell count today: 4.8 x10^9/L.
Nails normal.
Serum calcium 9.4 mg/dL in 2017.
Respiratory rate 12/min at this assessment.
Hearing normal to conversation.
Magnesium 2.0 mg/dL in 2010.
Oral temperature this morning: 36.4 C.
Watches football on weekends.


## 3.72 ('gs108', 'c1', 'negation', 'long') templates=test

RULE: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had coronary artery disease (current or past) and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe amlodipine instead.
CONDITION: coronary artery disease
CLAIMS: s = 'Prescribe lisinopril.' | s' = 'Prescribe amlodipine.'

BASE (answer s):
Man of 38 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Paints watercolors as a hobby.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2008.
Enjoys board games.
Plays the piano.
Photographs local wildlife.
Prefers morning appointments.
Knits as a hobby.
Prefers to be addressed by first name.
Uses sunscreen in summer.
His uncle wears contact lenses.
His wife burned a hand on a stove years ago.
During a checkup in 2014, total protein was 7.0 g/dL.
Ongoing treatment for venous thrombosis of the left arm.
Chest pain on exertion: none reported.
Drives a car.
Owns a bicycle.
His friend has recovered from a dislocated finger.

FLIP (answer s'): -Chest pain on exertion: none reported. | +Coronary artery disease years ago, with angina that went away after bypass surgery.

NEAR (answer s): -Chest pain on exertion: none reported. | +Has never had coronary artery disease.

MISSING (answer neither (undetermined)): -Chest pain on exertion: none reported. | +Coronary artery disease: status unclear from the records at hand.

PRES (answer s): full text
Male patient of 38 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Knits as a hobby.
His wife burned a hand on a stove years ago.
Drives a car.
Enjoys board games.
Photographs local wildlife.
Climbs two flights of stairs without symptoms.
Plays the piano.
Prefers to be addressed by first name.
Prefers morning appointments.
Paints watercolors as a hobby.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Uses sunscreen in summer.
His uncle wears contact lenses.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2008.
Has an acute pulmonary embolism, diagnosed this week.
During a checkup in 2014, total protein was 7.0 g/dL.
His friend has recovered from a dislocated finger.


## 3.73 ('gs163', 'c1', 'numeric', 'long') templates=train

RULE: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the current serum creatinine is above 2.0 mg/dL or the patient has ever had diabetes (current or past), prescribe doxycycline instead.
CONDITION: serum creatinine above 2.0
CLAIMS: s = 'Prescribe amoxicillin.' | s' = 'Prescribe doxycycline.'

BASE (answer s):
Patient: male, 70 years.
Productive cough and fever; consolidation on chest radiograph.
His husband is nearsighted.
Uses reading glasses for small print.
His partner is being treated for eczema.
Keeps houseplants.
TSH 1.6 mIU/L in 2006.
Albumin 4.1 g/dL in 2007 (routine blood test).
His husband has a broken finger in a splint.
Urine dipstick shows no sugar.
Has a pet dog.
Feeds birds in the backyard.
His coworker completed physical therapy for a shoulder injury.
Total bilirubin 0.6 mg/dL in 2010.
Serum creatinine today: 0.8 mg/dL.
Uses a smartphone for reminders.
Height 170 cm.
Plays chess online.
Drinks two cups of coffee a day.

FLIP (answer s'): -Serum creatinine today: 0.8 mg/dL. | +Serum creatinine today: 4.2 mg/dL.

NEAR (answer s): -Serum creatinine today: 0.8 mg/dL. | +Serum creatinine today: 1.8 mg/dL.

MISSING (answer neither (undetermined)): -Serum creatinine today: 0.8 mg/dL.

PRES (answer s): full text
A 70-year-old man.
Productive cough and fever; consolidation on chest radiograph.
Blood panel at this assessment: creatinine 0.8 mg/dL.
TSH 1.6 mIU/L in 2006.
His husband has a broken finger in a splint.
Drinks two cups of coffee a day.
Feeds birds in the backyard.
His husband is nearsighted.
His partner is being treated for eczema.
His coworker completed physical therapy for a shoulder injury.
Uses a smartphone for reminders.
Albumin 4.1 g/dL in 2007 (routine blood test).
Has a pet dog.
Total bilirubin 0.6 mg/dL in 2010.
Uses reading glasses for small print.
Keeps houseplants.
Fasting glucose normal on today's blood tests.
Plays chess online.
Height 170 cm.


## 3.74 ('gs134', 'c1', 'subject', 'long') templates=test

RULE: For stroke prevention in atrial fibrillation, prescribe apixaban. If the patient has ever had heparin-induced thrombocytopenia (current or past) and the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe warfarin instead.
CONDITION: heparin-induced thrombocytopenia
CLAIMS: s = 'Prescribe apixaban.' | s' = 'Prescribe warfarin.'

BASE (answer s):
Male patient of 46 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
His uncle lives with psoriasis.
Has two cats.
Sees a dentist yearly.
Prefers morning appointments.
Pupils equal and reactive to light.
Photographs local wildlife.
During a checkup in 2011, free T3 was 3.2 pg/mL.
His roommate burned a hand on a stove years ago.
Owns a bicycle.
Sleeps seven hours a night.
Free T4 of 1.2 ng/dL in 2019.
In 2023, folate was 12 ng/mL.
Recovered from a heart attack in 2018.
Prefers to be addressed by first name.
Teeth in good repair.
Last received heparin more than a year ago.
Drives a car.
His wife sprained a thumb last month.
Uses sunscreen in summer.
His uncle has a lazy eye.

FLIP (answer s'): -Last received heparin more than a year ago. | +Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully.

NEAR (answer s): -Last received heparin more than a year ago. | +His friend has developed heparin-induced thrombocytopenia after surgery.

MISSING (answer neither (undetermined)): -Last received heparin more than a year ago. | +Heparin-induced thrombocytopenia: status unclear from the records at hand.

PRES (answer s): full text
Man of 46 years.
Atrial fibrillation; anticoagulation indicated.
Prefers morning appointments.
Knits as a hobby.
Owns a bicycle.
Pupils equal and reactive to light.
During a checkup in 2011, free T3 was 3.2 pg/mL.
Drives a car.
His uncle lives with psoriasis.
In 2023, folate was 12 ng/mL.
Has two cats.
Teeth in good repair.
Heparin exposure within the past 100 days: none.
His uncle has a lazy eye.
Photographs local wildlife.
His roommate burned a hand on a stove years ago.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2019.
Sees a dentist yearly.
Prefers to be addressed by first name.
Sleeps seven hours a night.
His wife sprained a thumb last month.
Heart attack years ago, with full recovery.


## 3.75 ('gs249', 'c2', 'time', 'long') templates=train

RULE: For heart failure with reduced ejection fraction, prescribe spironolactone. If the patient has ever had a venous thromboembolism (current or past) and the patient has an active peptic ulcer, prescribe dapagliflozin instead.
CONDITION: active peptic ulcer
CLAIMS: s = 'Prescribe spironolactone.' | s' = 'Prescribe dapagliflozin.'

BASE (answer s):
Female, 50 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Volunteers at a library.
Has a pet dog.
Phosphate 3.6 mg/dL in 2023.
Anticoagulation for a pulmonary embolism was completed in 2013, and the clot resolved.
Speaks English and Spanish.
Lives on a quiet street.
Total bilirubin 0.6 mg/dL in 2023.
Drinks alcohol occasionally.
No dyspepsia or melena.
Reads most evenings.
Enjoys cooking.
Bicarbonate 26 mmol/L in 2021 (annual physical).
Hearing normal to conversation.
Her brother-in-law is nearsighted.
Albumin 4.1 g/dL in 2008 (routine blood test).
Uses reading glasses for small print.
Her housemate wears hearing aids.
Her cousin has a broken finger in a splint.
Her cousin had a splinter removed from a finger.

FLIP (answer s'): -No dyspepsia or melena. | +A stomach ulcer is causing burning pain after meals.

NEAR (answer s): -No dyspepsia or melena. | +Gastric ulcer healed after eight weeks of omeprazole.

MISSING (answer neither (undetermined)): -No dyspepsia or melena. | +Active peptic ulcer: not asked about.

PRES (answer s): full text
50-year-old woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Previously had a DVT, in 2013.
Uses reading glasses for small print.
Drinks alcohol occasionally.
Phosphate 3.6 mg/dL in 2023.
Her brother-in-law is nearsighted.
Speaks English and Spanish.
Lives on a quiet street.
Hearing normal to conversation.
No black or bloody stools.
Bicarbonate 26 mmol/L in 2021 (annual physical).
Has a pet dog.
Albumin 4.1 g/dL in 2008 (routine blood test).
Reads most evenings.
Her housemate wears hearing aids.
Her cousin has a broken finger in a splint.
Volunteers at a library.
Total bilirubin 0.6 mg/dL in 2023.
Enjoys cooking.
Her cousin had a splinter removed from a finger.
