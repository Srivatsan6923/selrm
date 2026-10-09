# Sample triplets

100 triplets from `data/rule_v1/test_L2/records.jsonl`, stratified by near-miss kind (seed 0). Lines starting with `-` are removed from the base case and lines starting with `+` are added to it. **Answer** is the claim the program marks correct.


## 1. `rule_v1.test.gs118.c1.boundary.long.1986`

- **Rule** (gs118, g_score_cutoff): For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.
- **Condition**: white cell count above 12.0 | near-miss: boundary | tier: long
- **Claims**: s = "Prescribe spironolactone." | s' = "Prescribe dapagliflozin."

```
Male patient of 47 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
His father lives with psoriasis.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Current eGFR 69 mL/min/1.73 m2.
His wife wears contact lenses.
His roommate has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2022.
Enjoys board games.
Pupils equal and reactive to light.
Heart rate now 61/min on a pulse check.
Owns a bicycle.
Photographs local wildlife.
Prefers morning appointments.
An episode of angioedema years ago, with full recovery.
Sleeps seven hours a night.
Drives a car.
Knits as a hobby.
Sees a dentist yearly.
Teeth in good repair.
His sister burned a hand on a stove years ago.
Current white cell count 5.7 x10^9/L.
Plays the piano.
During a checkup in 2022, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
```

**flip** (answer: s')
```
-Current white cell count 5.7 x10^9/L.
+Current white cell count 14.2 x10^9/L.
```

**near** (answer: s)
```
-Current white cell count 5.7 x10^9/L.
+Current white cell count 12.0 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 26 lines, same state)
```


## 2. `rule_v1.test.s3_blatchford.hf.negation.easy.1902`

- **Rule** (s3_blatchford, additive_score): Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.
- **Condition**: heart failure | near-miss: negation | tier: easy
- **Claims**: s = "The heart failure criterion contributes 0 points." | s' = "The heart failure criterion contributes 2 points."

```
Female patient of 53 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Has two cats.
Photographs local wildlife.
Paints watercolors as a hobby.
Heart rate now 77/min on a pulse check.
Observations now: blood pressure 143/94 mmHg.
Sleeps seven hours a night.
Blood urea nitrogen now: 12 mg/dL.
```

**flip** (answer: s')
```
+Current heart failure with ankle swelling.
```

**near** (answer: s)
```
+Has never had heart failure.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 3. `rule_v1.test.gs137.c2.numeric.easy.299`

- **Rule** (gs137, g_all_of): For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.
- **Condition**: serum creatinine at least 1.5 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe naproxen alone." | s' = "Prescribe naproxen with omeprazole."

```
Female patient of 65 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Owns a bicycle.
Current serum creatinine 1.2 mg/dL.
Insulin-treated diabetes.
Paints watercolors as a hobby.
Sleeps seven hours a night.
```

**flip** (answer: s')
```
-Current serum creatinine 1.2 mg/dL.
+Current serum creatinine 2.0 mg/dL.
```

**near** (answer: s)
```
-Current serum creatinine 1.2 mg/dL.
+Current serum creatinine 1.4 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 4. `rule_v1.test.gs001.c4.subject.easy.1547`

- **Rule** (gs001, g_score_cutoff): For contraception, prescribe a combined oral contraceptive. Score 1 point if the current platelet count is below 50 x10^9/L; 1 point if the patient is currently taking warfarin; 1 point if the patient has ever had diabetes (current or past); 3 points if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe a progestin-only pill instead.
- **Condition**: mechanical heart valve | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Woman of 38 years.
Requests contraception.
Formerly diabetic; in remission since 2011.
Prefers to be addressed by first name.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Has two cats.
Current platelet count 45 x10^9/L.
Sleeps seven hours a night.
```

**flip** (answer: s')
```
+Lives with a mechanical aortic valve prosthesis.
```

**near** (answer: s)
```
+Her sister attends a valve clinic for a mechanical mitral valve.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 5. `rule_v1.test.gs072.c1.time.easy.1799`

- **Rule** (gs072, g_two_of_three): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has a mechanical heart valve; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the age of the patient is 65 years or more.
- **Condition**: mechanical heart valve | near-miss: time | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
An adult woman.
Acute low back pain after lifting.
Recovered from a heart attack in 2011.
Currently aged 41 years.
Sleeps seven hours a night.
Heart sounds without a metallic click.
Teeth in good repair.
Prefers to be addressed by first name.
```

**flip** (answer: s')
```
-Heart sounds without a metallic click.
+Mechanical mitral valve in place; metallic closing clicks audible.
```

**near** (answer: s)
```
-Heart sounds without a metallic click.
+Mechanical aortic valve explanted years ago for valve thrombosis; a bioprosthesis now sits in its place.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 6. `rule_v1.test.gs179.c2.boundary.long.491`

- **Rule** (gs179, g_all_of): For rate control in atrial fibrillation, prescribe metoprolol. If the patient has ever had diabetes (current or past) and the current white cell count is above 12.0 x10^9/L, prescribe diltiazem instead.
- **Condition**: white cell count above 12.0 | near-miss: boundary | tier: long
- **Claims**: s = "Prescribe metoprolol." | s' = "Prescribe diltiazem."

```
Man of 72 years.
Atrial fibrillation with a ventricular rate of 128/min.
Drives a car.
Sees a dentist yearly.
Has two cats.
Pupils equal and reactive to light.
Prefers morning appointments.
In 2016, lipase was 30 U/L.
Had diabetes years ago that went into remission on a low-calorie diet.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
His roommate has recovered from a dislocated finger.
Lives in a second-floor apartment.
Plays the piano.
Uses sunscreen in summer.
His friend wears contact lenses.
His sister burned a hand on a stove years ago.
His friend has a lazy eye.
Zinc of 85 mcg/dL in 2010.
Owns a bicycle.
Latest WBC is 5.4 x10^9/L.
Free T4 of 1.2 ng/dL in 2005.
```

**flip** (answer: s')
```
-Latest WBC is 5.4 x10^9/L.
+Latest WBC is 13.9 x10^9/L.
```

**near** (answer: s)
```
-Latest WBC is 5.4 x10^9/L.
+Latest WBC is 12.0 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 23 lines, same state)
```


## 7. `rule_v1.test.gs188.c3.negation.easy.855`

- **Rule** (gs188, g_two_of_three): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).
- **Condition**: venous thromboembolism | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe cephalexin." | s' = "Prescribe clindamycin."

```
Man of 84 years.
Spreading redness and warmth of the right shin for two days.
Varicose veins: none seen.
Abdomen soft and non-tender.
Photographs local wildlife.
Owns a bicycle.
ALT now 143 U/L.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**flip** (answer: s')
```
-Varicose veins: none seen.
+Ongoing treatment for a deep vein thrombosis of the left arm.
```

**near** (answer: s)
```
-Varicose veins: none seen.
+Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 8. `rule_v1.test.gs134.c2.numeric.easy.312`

- **Rule** (gs134, g_score_cutoff): For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.
- **Condition**: weight at or below 60 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Woman of 33 years.
Requests contraception.
Owns a bicycle.
Latest weight 70 kg.
Has two cats.
Prefers morning appointments.
Tender, swollen lymph nodes in the front of the neck.
Platelet count now 40 x10^9/L.
Paints watercolors as a hobby.
Known coronary artery disease (two-vessel disease on angiography).
```

**flip** (answer: s')
```
-Latest weight 70 kg.
+Latest weight 60 kg.
```

**near** (answer: s)
```
-Latest weight 70 kg.
+Latest weight 62 kg.
```

**pres** (answer: s)
```
(re-rendered: 10 lines, same state)
```


## 9. `rule_v1.test.gs094.c1.subject.easy.1674`

- **Rule** (gs094, g_all_of): For primary prevention, prescribe atorvastatin. If the patient has ever had heart failure (current or past) and the age of the patient is 75 years or more, prescribe ezetimibe instead.
- **Condition**: heart failure | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
An adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 83 years.
Drives a car.
Prefers morning appointments.
```

**flip** (answer: s')
```
+Current heart failure with ankle swelling.
```

**near** (answer: s)
```
+Her roommate is treated for heart failure.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 10. `rule_v1.test.gs139.c1.time.easy.1836`

- **Rule** (gs139, g_all_of): For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.
- **Condition**: tender cervical lymph nodes | near-miss: time | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
Female patient of 20 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Owns a bicycle.
Recurrent angioedema, under allergy follow-up.
Teeth in good repair.
Prefers to be addressed by first name.
Neck palpation unremarkable.
Has two cats.
```

**flip** (answer: s')
```
-Neck palpation unremarkable.
+Tender, swollen lymph nodes in the front of the neck.
```

**near** (answer: s)
```
-Neck palpation unremarkable.
+Tender anterior cervical lymph nodes with a throat infection years ago, which went down within two weeks.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 11. `rule_v1.test.gs108.c1.boundary.easy.1936`

- **Rule** (gs108, g_any_of): For heart failure with reduced ejection fraction, prescribe spironolactone. If the current white cell count is above 12.0 x10^9/L or the current temperature is above 38.0 C, prescribe dapagliflozin instead.
- **Condition**: white cell count above 12.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe spironolactone." | s' = "Prescribe dapagliflozin."

```
Woman of 80 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Teeth in good repair.
Has two cats.
Current temperature 36.4 C.
Prefers to be addressed by first name.
Current white cell count 5.1 x10^9/L.
```

**flip** (answer: s')
```
-Current white cell count 5.1 x10^9/L.
+Current white cell count 13.9 x10^9/L.
```

**near** (answer: s)
```
-Current white cell count 5.1 x10^9/L.
+Current white cell count 12.0 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 12. `rule_v1.test.gs221.c1.negation.easy.1888`

- **Rule** (gs221, g_all_of): For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the patient has had cancer at any time (active or in remission), prescribe fondaparinux instead.
- **Condition**: myocardial infarction or peripheral artery disease | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe enoxaparin." | s' = "Prescribe fondaparinux."

```
Female patient of 84 years.
First day after elective total hip replacement.
Uses sunscreen in summer.
Walks without calf pain.
Knits as a hobby.
Enjoys board games.
Has metastatic lung cancer, receiving palliative treatment.
```

**flip** (answer: s')
```
-Walks without calf pain.
+Heart attack years ago, with full recovery.
```

**near** (answer: s)
```
-Walks without calf pain.
+Never diagnosed with a myocardial infarction or peripheral artery disease.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 13. `rule_v1.test.gs056.c4.numeric.long.1158`

- **Rule** (gs056, g_score_cutoff): For rate control in atrial fibrillation, prescribe metoprolol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 2 points if the patient has ever had a venous thromboembolism (current or past); 3 points if the patient has ever had coronary artery disease (current or past); 1 point if the current white cell count is above 12.0 x10^9/L. If the score is 4 or more, prescribe diltiazem instead.
- **Condition**: white cell count above 12.0 | near-miss: numeric | tier: long
- **Claims**: s = "Prescribe metoprolol." | s' = "Prescribe diltiazem."

```
Man of 57 years.
Atrial fibrillation with a ventricular rate of 128/min.
Knits as a hobby.
Sleeps seven hours a night.
Chest pain on exertion: none reported.
His friend burned a hand on a stove years ago.
His sister has a lazy eye.
Current white cell count 8.2 x10^9/L.
Has type 2 diabetes on metformin.
Lives in a second-floor apartment.
Plays the piano.
Zinc of 85 mcg/dL in 2013.
Enjoys board games.
Paints watercolors as a hobby.
Owns a bicycle.
Has two cats.
In 2011, folate was 12 ng/mL.
Prefers to be addressed by first name.
Teeth in good repair.
During a checkup in 2014, total protein was 7.0 g/dL.
Drives a car.
Pulmonary embolism years ago, treated for six months.
```

**flip** (answer: s')
```
-Current white cell count 8.2 x10^9/L.
+Current white cell count 14.3 x10^9/L.
```

**near** (answer: s)
```
-Current white cell count 8.2 x10^9/L.
+Current white cell count 11.6 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 22 lines, same state)
```


## 14. `rule_v1.test.gs192.c1.subject.long.1473`

- **Rule** (gs192, g_score_cutoff): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had asthma (current or past); 1 point if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past); 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time. If the score is 6 or more, prescribe nitrofurantoin instead.
- **Condition**: asthma at any time | near-miss: subject | tier: long
- **Claims**: s = "Prescribe trimethoprim-sulfamethoxazole." | s' = "Prescribe nitrofurantoin."

```
Female patient of 55 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Her friend has a lazy eye.
Teeth in good repair.
Formerly diabetic; in remission since 2015.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2007.
Paints watercolors as a hobby.
During a checkup in 2010, total protein was 7.0 g/dL.
Her roommate sprained a thumb last month.
Drives a car.
Formerly treated for a peptic ulcer; endoscopy in 2011 showed it had gone.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Has two cats.
Uses sunscreen in summer.
Her uncle wears contact lenses.
Prefers to be addressed by first name.
Plays the piano.
Knits as a hobby.
Difference in calf circumference now 3.0 cm.
Sleeps seven hours a night.
Prefers morning appointments.
Lungs clear, without wheeze or prolonged expiration.
Her sister burned a hand on a stove years ago.
```

**flip** (answer: s')
```
-Lungs clear, without wheeze or prolonged expiration.
+Persistent asthma, using a rescue inhaler most weeks.
```

**near** (answer: s)
```
-Lungs clear, without wheeze or prolonged expiration.
+Her sister is asthmatic.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 15. `rule_v1.test.gs033.c1.time.easy.1875`

- **Rule** (gs033, g_two_of_three): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
- **Condition**: weight at or below 60 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe cephalexin." | s' = "Prescribe clindamycin."

```
Woman of 85 years.
Spreading redness and warmth of the right shin for two days.
Prefers morning appointments.
Teeth in good repair.
Current weight 97 kg.
Known penicillin allergy with angioedema.
Sleeps seven hours a night.
Has two cats.
Back in 2014, weight stood at 80 kg.
Cardiac stress test unremarkable last year.
```

**flip** (answer: s')
```
-Current weight 97 kg.
+Current weight 60 kg.
```

**near** (answer: s)
```
-Back in 2014, weight stood at 80 kg.
+Back in 2014, weight stood at 49 kg.
```

**pres** (answer: s)
```
(re-rendered: 10 lines, same state)
```


## 16. `rule_v1.test.gs078.c1.boundary.easy.455`

- **Rule** (gs078, g_two_of_three): For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the current serum potassium is above 5.0 mmol/L; the patient currently has a mechanical heart valve; the patient has ever had coronary artery disease (current or past).
- **Condition**: serum potassium above 5.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe amoxicillin." | s' = "Prescribe doxycycline."

```
Man of 61 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Latest potassium result: 4.5 mmol/L.
Lives in a second-floor apartment.
Lives with a mechanical aortic valve prosthesis.
```

**flip** (answer: s')
```
-Latest potassium result: 4.5 mmol/L.
+Latest potassium result: 5.8 mmol/L.
```

**near** (answer: s)
```
-Latest potassium result: 4.5 mmol/L.
+Latest potassium result: 5.0 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 17. `rule_v1.test.gs038.c1.negation.easy.70`

- **Rule** (gs038, g_all_of): For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.
- **Condition**: peptic ulcer at any time | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe lisinopril." | s' = "Prescribe amlodipine."

```
Woman of 30 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Blood urea nitrogen now: 24 mg/dL.
Knits as a hobby.
Appetite good; no indigestion.
```

**flip** (answer: s')
```
-Appetite good; no indigestion.
+Formerly treated for a peptic ulcer; endoscopy in 2024 showed it had gone.
```

**near** (answer: s)
```
-Appetite good; no indigestion.
+Medical record negative for peptic ulcer, current or past.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 18. `rule_v1.test.s3_childpugh.inr.numeric.easy.577`

- **Rule** (s3_childpugh, additive_score): Child-Pugh score (as used here, partial; each finding below adds 1 point, whatever its grade): 1 point each for a current international normalized ratio (INR) of 1.7 or more; current ascites; new confusion (encephalopathy). Bilirubin, albumin and other items are not part of this question.
- **Condition**: international normalized ratio at least 1.7 | near-miss: numeric | tier: easy
- **Claims**: s = "The international normalized ratio criterion contributes 0 points." | s' = "The international normalized ratio criterion contributes 1 point."

```
Woman of 58 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Current international normalized ratio 1.0.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Speech clear; follows commands.
Flat abdomen, resonant to percussion throughout.
```

**flip** (answer: s')
```
-Current international normalized ratio 1.0.
+Current international normalized ratio 1.7.
```

**near** (answer: s)
```
-Current international normalized ratio 1.0.
+Current international normalized ratio 1.5.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 19. `rule_v1.test.gs025.c1.subject.easy.238`

- **Rule** (gs025, g_all_of): For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.
- **Condition**: myocardial infarction or peripheral artery disease | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe penicillin V."

```
Woman of 42 years.
Sore throat for two days.
Plays the piano.
Drives a car.
Knits as a hobby.
Temperature now 38.3 C (tympanic).
Enjoys board games.
```

**flip** (answer: s')
```
+Recovered from a heart attack in 2016.
```

**near** (answer: s)
```
+Her sister had a heart attack years ago.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 20. `rule_v1.test.gs220.c1.time.easy.1659`

- **Rule** (gs220, g_all_of): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.
- **Condition**: eGFR below 30 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Female patient of 37 years.
Requests contraception.
Current eGFR 61 mL/min/1.73 m2.
Plays the piano.
Back in 2008, eGFR stood at 78 mL/min/1.73 m2.
Paints watercolors as a hobby.
Her sister is diabetic.
```

**flip** (answer: s')
```
-Current eGFR 61 mL/min/1.73 m2.
+Current eGFR 18 mL/min/1.73 m2.
```

**near** (answer: s)
```
-Back in 2008, eGFR stood at 78 mL/min/1.73 m2.
+Back in 2008, eGFR stood at 26 mL/min/1.73 m2.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 21. `rule_v1.test.gs071.c1.boundary.easy.1380`

- **Rule** (gs071, g_all_of): For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.
- **Condition**: temperature above 38.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe apixaban." | s' = "Prescribe warfarin."

```
Male patient of 65 years.
Atrial fibrillation; anticoagulation indicated.
Active peptic ulcer disease.
Paints watercolors as a hobby.
Temperature now 36.5 C (tympanic).
```

**flip** (answer: s')
```
-Temperature now 36.5 C (tympanic).
+Temperature now 38.7 C (tympanic).
```

**near** (answer: s)
```
-Temperature now 36.5 C (tympanic).
+Temperature now 38.0 C (tympanic).
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 22. `rule_v1.test.gs209.c2.negation.easy.1015`

- **Rule** (gs209, g_two_of_three): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.
- **Condition**: peptic ulcer at any time | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current heart rate 77/min.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Appetite good; no indigestion.
Currently aged 78 years.
```

**flip** (answer: s')
```
-Appetite good; no indigestion.
+Duodenal ulcer years ago; recovered fully with treatment.
```

**near** (answer: s)
```
-Appetite good; no indigestion.
+Has never had a peptic ulcer.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 23. `rule_v1.test.s2_wells_pe.hr.numeric.easy.15`

- **Rule** (s2_wells_pe, additive_score): Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.
- **Condition**: heart rate above 100 | near-miss: numeric | tier: easy
- **Claims**: s = "The heart rate criterion contributes 0 points." | s' = "The heart rate criterion contributes 1.5 points."

```
Man of 76 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Dry cough, with nothing brought up.
Weight steady over the past year.
Pupils equal and reactive to light.
Heart rate now 75/min on a pulse check.
Prefers morning appointments.
```

**flip** (answer: s')
```
-Heart rate now 75/min on a pulse check.
+Heart rate now 111/min on a pulse check.
```

**near** (answer: s)
```
-Heart rate now 75/min on a pulse check.
+Heart rate now 96/min on a pulse check.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 24. `rule_v1.test.gs224.c1.subject.easy.1001`

- **Rule** (gs224, g_all_of): For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had a venous thromboembolism (current or past) and the current serum creatinine is above 2.0 mg/dL, prescribe clotrimazole pessaries instead.
- **Condition**: venous thromboembolism | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
Female patient of 20 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Plays the piano.
Paints watercolors as a hobby.
Latest creatinine result: 2.5 mg/dL.
```

**flip** (answer: s')
```
+Recovered from a pulmonary embolism in 2024.
```

**near** (answer: s)
```
+Her sister had a DVT years ago.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 25. `rule_v1.test.gs035.c1.time.easy.1899`

- **Rule** (gs035, g_two_of_three): For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).
- **Condition**: current heart failure | near-miss: time | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
An adult woman.
Requests contraception.
Drives a car.
Heart sounds without a gallop.
Has melanoma skin cancer and is receiving treatment for it.
Currently aged 61 years.
```

**flip** (answer: s')
```
-Heart sounds without a gallop.
+Current heart failure with ankle swelling.
```

**near** (answer: s)
```
-Heart sounds without a gallop.
+Formerly had heart failure from stress cardiomyopathy; recovered fully in 2023 and off all heart medicines since.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 26. `rule_v1.test.gs086.c1.boundary.easy.8`

- **Rule** (gs086, g_two_of_three): For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).
- **Condition**: heart rate above 90 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe enoxaparin." | s' = "Prescribe intermittent pneumatic compression."

```
Male patient of 64 years.
Admitted for community-acquired pneumonia; immobile.
Recovered from a pulmonary embolism in 2007.
Heart rate now 68/min on a pulse check.
Enjoys board games.
Sleeps seven hours a night.
Sleeps flat on one pillow.
```

**flip** (answer: s')
```
-Heart rate now 68/min on a pulse check.
+Heart rate now 105/min on a pulse check.
```

**near** (answer: s)
```
-Heart rate now 68/min on a pulse check.
+Heart rate now 90/min on a pulse check.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 27. `rule_v1.test.gs023.c2.negation.easy.1450`

- **Rule** (gs023, g_all_of): For hip osteoarthritis pain, prescribe naproxen alone. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time, prescribe naproxen with omeprazole instead.
- **Condition**: coronary artery disease (patient or first-degree relative) | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe naproxen alone." | s' = "Prescribe naproxen with omeprazole."

```
Male patient of 76 years.
Hip osteoarthritis with pain on walking.
Cardiac stress test unremarkable last year.
Recovered from a pulmonary embolism in 2016.
Owns a bicycle.
```

**flip** (answer: s')
```
-Cardiac stress test unremarkable last year.
+Known coronary artery disease (two-vessel disease on angiography).
```

**near** (answer: s)
```
-Cardiac stress test unremarkable last year.
+Has never had coronary artery disease.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 28. `rule_v1.test.s3_alvarado.temp.numeric.long.1691`

- **Rule** (s3_alvarado, additive_score): Alvarado score (as used here, partial): 2 points for current tenderness in the right lower quadrant (right iliac fossa); 2 points for a current white cell count above 10.0 x10^9/L; 1 point for a current temperature of 37.3 C or more. Other Alvarado items are not part of this question.
- **Condition**: temperature at least 37.3 | near-miss: numeric | tier: long
- **Claims**: s = "The temperature criterion contributes 0 points." | s' = "The temperature criterion contributes 1 point."

```
Female patient of 58 years.
Abdominal pain for one day; assessed in the emergency department.
Lives in a second-floor apartment.
In 2007, lipase was 30 U/L.
Her uncle lives with psoriasis.
Enjoys board games.
Her friend has recovered from a dislocated finger.
Sees a dentist yearly.
Has two cats.
Uses sunscreen in summer.
Her father burned a hand on a stove years ago.
Temperature now 36.5 C (tympanic).
Free T4 of 1.2 ng/dL in 2017.
Plays the piano.
Photographs local wildlife.
Owns a bicycle.
Prefers morning appointments.
Abdominal examination unremarkable, without tenderness.
Pupils equal and reactive to light.
Latest WBC is 5.6 x10^9/L.
```

**flip** (answer: s')
```
-Temperature now 36.5 C (tympanic).
+Temperature now 37.3 C (tympanic).
```

**near** (answer: s)
```
-Temperature now 36.5 C (tympanic).
+Temperature now 37.2 C (tympanic).
```

**pres** (answer: s)
```
(re-rendered: 20 lines, same state)
```


## 29. `rule_v1.test.gs011.c1.subject.easy.7`

- **Rule** (gs011, g_all_of): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the current ALT is above 120 U/L, prescribe azithromycin instead.
- **Condition**: venous thromboembolism (patient or first-degree relative) | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe amoxicillin." | s' = "Prescribe azithromycin."

```
Woman of 70 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Has two cats.
ALT now 143 U/L.
```

**flip** (answer: s')
```
+Has an acute pulmonary embolism, diagnosed this week.
```

**near** (answer: s)
```
+Her friend is on anticoagulation for venous thrombosis.
```

**pres** (answer: s)
```
(re-rendered: 4 lines, same state)
```


## 30. `rule_v1.test.s1_bap65.bun.time.easy.126`

- **Rule** (s1_bap65, additive_score): BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of 25 mg/dL or more; current altered mental status (confusion or disorientation); a current heart rate of 109/min or more. Age is scored separately and is not part of this question.
- **Condition**: blood urea nitrogen at least 25 | near-miss: time | tier: easy
- **Claims**: s = "The blood urea nitrogen criterion contributes 0 points." | s' = "The blood urea nitrogen criterion contributes 1 point."

```
Woman of 67 years.
Acute exacerbation of COPD; assessed in the emergency department.
Back in 2017, blood urea nitrogen stood at 10 mg/dL.
Sleeps seven hours a night.
Blood urea nitrogen 15 mg/dL on the current labs.
Heart rate now 91/min on a pulse check.
Teeth in good repair.
Prefers morning appointments.
```

**flip** (answer: s')
```
-Blood urea nitrogen 15 mg/dL on the current labs.
+Blood urea nitrogen 25 mg/dL on the current labs.
```

**near** (answer: s)
```
-Back in 2017, blood urea nitrogen stood at 10 mg/dL.
+Back in 2017, blood urea nitrogen stood at 36 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 31. `rule_v1.test.gs088.c3.boundary.easy.851`

- **Rule** (gs088, g_two_of_three): For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.
- **Condition**: white cell count above 12.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe penicillin V."

```
Female patient of 37 years.
Sore throat for two days.
Current white cell count 6.9 x10^9/L.
Heart attack years ago, with full recovery.
Has two cats.
Tonsils pink and clean on inspection.
```

**flip** (answer: s')
```
-Current white cell count 6.9 x10^9/L.
+Current white cell count 13.8 x10^9/L.
```

**near** (answer: s)
```
-Current white cell count 6.9 x10^9/L.
+Current white cell count 12.0 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 32. `rule_v1.test.gs188.c1.negation.easy.1498`

- **Rule** (gs188, g_two_of_three): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).
- **Condition**: peptic ulcer at any time | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe cephalexin." | s' = "Prescribe clindamycin."

```
Woman of 44 years.
Spreading redness and warmth of the right shin for two days.
Coagulation tests normal on recent bloodwork.
Sleeps seven hours a night.
ALT now 140 U/L.
Photographs local wildlife.
Drives a car.
```

**flip** (answer: s')
```
+Duodenal ulcer years ago; recovered fully with treatment.
```

**near** (answer: s)
```
+Has never had a peptic ulcer.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 33. `rule_v1.test.gs216.c1.numeric.easy.1767`

- **Rule** (gs216, g_all_of): For primary prevention, prescribe atorvastatin. If the age of the patient is 75 years or more and the patient has ever had a venous thromboembolism (current or past), prescribe ezetimibe instead.
- **Condition**: age at least 75 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
An adult man.
Primary prevention; LDL cholesterol 182 mg/dL.
Prefers morning appointments.
Owns a bicycle.
Knits as a hobby.
Pupils equal and reactive to light.
Recovered from a pulmonary embolism in 2020.
Currently aged 64 years.
```

**flip** (answer: s')
```
-Currently aged 64 years.
+Currently aged 85 years.
```

**near** (answer: s)
```
-Currently aged 64 years.
+Currently aged 73 years.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 34. `rule_v1.test.gs033.c2.subject.easy.1865`

- **Rule** (gs033, g_two_of_three): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
- **Condition**: penicillin allergy | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe cephalexin." | s' = "Prescribe clindamycin."

```
Male patient of 83 years.
Spreading redness and warmth of the right shin for two days.
Chest pain on exertion: none reported.
Current weight 56 kg.
Prefers to be addressed by first name.
Teeth in good repair.
Photographs local wildlife.
Drug allergies: none known.
```

**flip** (answer: s')
```
-Drug allergies: none known.
+Known penicillin allergy with angioedema.
```

**near** (answer: s)
```
-Drug allergies: none known.
+His friend cannot take penicillin because of an allergy.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 35. `rule_v1.test.gs118.c3.time.easy.1067`

- **Rule** (gs118, g_score_cutoff): For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.
- **Condition**: eGFR below 45 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe spironolactone." | s' = "Prescribe dapagliflozin."

```
Man of 51 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Records from 2017 list eGFR at 52 mL/min/1.73 m2.
Has two cats.
Face and neck without swelling on examination.
Latest WBC is 12.6 x10^9/L.
Pupils equal and reactive to light.
Current eGFR 69 mL/min/1.73 m2.
Uses sunscreen in summer.
Sees a dentist yearly.
Heart rate now 63/min on a pulse check.
```

**flip** (answer: s')
```
-Current eGFR 69 mL/min/1.73 m2.
+Current eGFR 40 mL/min/1.73 m2.
```

**near** (answer: s)
```
-Records from 2017 list eGFR at 52 mL/min/1.73 m2.
+Records from 2017 list eGFR at 35 mL/min/1.73 m2.
```

**pres** (answer: s)
```
(re-rendered: 11 lines, same state)
```


## 36. `rule_v1.test.gs124.c3.boundary.long.1302`

- **Rule** (gs124, g_two_of_three): For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.
- **Condition**: age above 65 | near-miss: boundary | tier: long
- **Claims**: s = "Prescribe oral amoxicillin." | s' = "Prescribe intravenous co-amoxiclav."

```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Knits as a hobby.
Plays the piano.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Uses sunscreen in summer.
His sister wears contact lenses.
Has two cats.
Prefers morning appointments.
Current age 54 years.
Lives in a second-floor apartment.
Teeth in good repair.
Sleeps seven hours a night.
His friend lives with psoriasis.
Drives a car.
Owns a bicycle.
Lives with colon cancer and attends an oncology clinic.
In 2016, lipase was 30 U/L.
Photographs local wildlife.
Sees a dentist yearly.
Current calf swelling 1.4 cm compared with the other leg.
Enjoys board games.
During a checkup in 2005, free T3 was 3.2 pg/mL.
```

**flip** (answer: s')
```
-Current age 54 years.
+Current age 68 years.
```

**near** (answer: s)
```
-Current age 54 years.
+Current age 65 years.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 37. `rule_v1.test.gs113.c2.negation.easy.1974`

- **Rule** (gs113, g_all_of): For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum creatinine is above 2.0 mg/dL and the patient has ever had heart failure (current or past), prescribe aspirin plus clopidogrel instead.
- **Condition**: heart failure | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe aspirin plus ticagrelor." | s' = "Prescribe aspirin plus clopidogrel."

```
Man of 61 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Paints watercolors as a hobby.
Sleeps flat on one pillow.
Enjoys board games.
Plays the piano.
Current serum creatinine 2.4 mg/dL.
```

**flip** (answer: s')
```
-Sleeps flat on one pillow.
+Current heart failure with ankle swelling.
```

**near** (answer: s)
```
-Sleeps flat on one pillow.
+Heart failure: never diagnosed.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 38. `rule_v1.test.gs245.c3.numeric.easy.1968`

- **Rule** (gs245, g_two_of_three): For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had heart failure (current or past); the patient has an active peptic ulcer; the age of the patient is 65 years or more.
- **Condition**: age at least 65 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe metformin." | s' = "Prescribe sitagliptin."

```
Man, adult.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected.
Prefers to be addressed by first name.
Currently aged 48 years.
Abdomen soft and non-tender.
```

**flip** (answer: s')
```
-Currently aged 48 years.
+Currently aged 65 years.
```

**near** (answer: s)
```
-Currently aged 48 years.
+Currently aged 63 years.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 39. `rule_v1.test.gs249.c1.subject.easy.1517`

- **Rule** (gs249, g_all_of): For community-acquired pneumonia treated at home, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient has an active peptic ulcer, prescribe doxycycline instead.
- **Condition**: colorectal cancer (patient or first-degree relative) | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe amoxicillin." | s' = "Prescribe doxycycline."

```
Woman of 57 years.
Productive cough and fever; consolidation on chest radiograph.
Active peptic ulcer disease.
Paints watercolors as a hobby.
Knits as a hobby.
```

**flip** (answer: s')
```
+Her father is undergoing surgery for bowel cancer.
```

**near** (answer: s)
```
+Her friend has advanced colorectal cancer.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 40. `rule_v1.test.gs052.c1.time.long.236`

- **Rule** (gs052, g_any_of): For primary prevention, prescribe atorvastatin. If the current heart rate is above 90/min or the current serum potassium is above 5.0 mmol/L, prescribe ezetimibe instead.
- **Condition**: heart rate above 90 | near-miss: time | tier: long
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
Woman of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Drives a car.
Pupils equal and reactive to light.
In 2015, folate was 12 ng/mL.
Has two cats.
Sees a dentist yearly.
Heart rate now 59/min on a pulse check.
Knits as a hobby.
Latest potassium result: 4.3 mmol/L.
Plays the piano.
Prefers morning appointments.
Uses sunscreen in summer.
Teeth in good repair.
Owns a bicycle.
Photographs local wildlife.
Her wife wears contact lenses.
Enjoys board games.
Her uncle has a lazy eye.
Records from 2012 list heart rate at 64/min.
During a checkup in 2009, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
```

**flip** (answer: s')
```
-Heart rate now 59/min on a pulse check.
+Heart rate now 103/min on a pulse check.
```

**near** (answer: s)
```
-Records from 2012 list heart rate at 64/min.
+Records from 2012 list heart rate at 96/min.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 41. `rule_v1.test.gs194.c1.boundary.easy.898`

- **Rule** (gs194, g_any_of): For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.
- **Condition**: heart rate above 90 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
Female patient of 44 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Heart rate now 62/min on a pulse check.
Plays the piano.
Current weight 82 kg.
```

**flip** (answer: s')
```
-Heart rate now 62/min on a pulse check.
+Heart rate now 96/min on a pulse check.
```

**near** (answer: s)
```
-Heart rate now 62/min on a pulse check.
+Heart rate now 90/min on a pulse check.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 42. `rule_v1.test.gs190.c2.negation.easy.536`

- **Rule** (gs190, g_all_of): For suspected infection on the medical ward, prescribe oral amoxicillin. If the current weight is 60 kg or less and the patient has ever had a venous thromboembolism (current or past), prescribe intravenous piperacillin-tazobactam instead.
- **Condition**: venous thromboembolism | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe oral amoxicillin." | s' = "Prescribe intravenous piperacillin-tazobactam."

```
Man of 72 years.
Suspected chest infection; assessed on the medical ward.
Current weight 52 kg.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Varicose veins: none seen.
Knits as a hobby.
Owns a bicycle.
```

**flip** (answer: s')
```
-Varicose veins: none seen.
+Recovered from a pulmonary embolism in 2013.
```

**near** (answer: s)
```
-Varicose veins: none seen.
+Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 43. `rule_v1.test.gs140.c3.numeric.easy.919`

- **Rule** (gs140, g_score_cutoff): For primary prevention, prescribe atorvastatin. Score 2 points if the patient has ever had a venous thromboembolism (current or past); 1 point if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current temperature is above 38.0 C. If the score is 3 or more, prescribe ezetimibe instead.
- **Condition**: temperature above 38.0 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
Man of 42 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Enjoys board games.
Plays the piano.
Has two cats.
Colorectal cancer under active treatment.
Temperature now 36.5 C (tympanic).
Prefers to be addressed by first name.
```

**flip** (answer: s')
```
-Temperature now 36.5 C (tympanic).
+Temperature now 38.8 C (tympanic).
```

**near** (answer: s)
```
-Temperature now 36.5 C (tympanic).
+Temperature now 37.9 C (tympanic).
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 44. `rule_v1.test.gs196.c1.subject.long.937`

- **Rule** (gs196, g_all_of): For musculoskeletal pain, prescribe ibuprofen. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time and the patient is allergic to penicillin, prescribe acetaminophen instead.
- **Condition**: coronary artery disease (patient or first-degree relative) | near-miss: subject | tier: long
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
Man of 43 years.
Acute low back pain after lifting.
Knits as a hobby.
Enjoys board games.
His friend has a lazy eye.
Drives a car.
Plays the piano.
Prefers morning appointments.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Uses sunscreen in summer.
Sees a dentist yearly.
His sister wears contact lenses.
Paints watercolors as a hobby.
Penicillin allergy: anaphylaxis.
Sleeps seven hours a night.
Teeth in good repair.
Photographs local wildlife.
During a checkup in 2007, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
```

**flip** (answer: s')
```
+Known coronary artery disease (two-vessel disease on angiography).
```

**near** (answer: s)
```
+His uncle has angina from coronary artery disease.
```

**pres** (answer: s)
```
(re-rendered: 19 lines, same state)
```


## 45. `rule_v1.test.gs074.c2.time.easy.1833`

- **Rule** (gs074, g_score_cutoff): For suspected infection on the medical ward, prescribe oral amoxicillin. Score 3 points if the age of the patient is 65 years or more; 2 points if the current systolic blood pressure is below 90 mmHg; 1 point if the current blood urea nitrogen is above 19 mg/dL; 3 points if the patient has ever had diabetes (current or past). If the score is 6 or more, prescribe intravenous piperacillin-tazobactam instead.
- **Condition**: systolic blood pressure below 90 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe oral amoxicillin." | s' = "Prescribe intravenous piperacillin-tazobactam."

```
An adult woman.
Suspected chest infection; assessed on the medical ward.
Uses sunscreen in summer.
Current age 52 years.
Knits as a hobby.
Pupils equal and reactive to light.
Records from 2023 list systolic blood pressure at 140 mmHg.
Blood urea nitrogen now: 25 mg/dL.
Formerly diabetic; in remission since 2008.
Observations now: blood pressure 112/77 mmHg.
```

**flip** (answer: s')
```
-Observations now: blood pressure 112/77 mmHg.
+Observations now: blood pressure 73/55 mmHg.
```

**near** (answer: s)
```
-Records from 2023 list systolic blood pressure at 140 mmHg.
+Records from 2023 list systolic blood pressure at 75 mmHg.
```

**pres** (answer: s)
```
(re-rendered: 10 lines, same state)
```


## 46. `rule_v1.test.gs001.c1.boundary.long.1255`

- **Rule** (gs001, g_score_cutoff): For contraception, prescribe a combined oral contraceptive. Score 1 point if the current platelet count is below 50 x10^9/L; 1 point if the patient is currently taking warfarin; 1 point if the patient has ever had diabetes (current or past); 3 points if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe a progestin-only pill instead.
- **Condition**: platelet count below 50 | near-miss: boundary | tier: long
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Female patient of 40 years.
Requests contraception.
Enjoys board games.
Owns a bicycle.
Teeth in good repair.
Her uncle lives with psoriasis.
Current platelet count 315 x10^9/L.
Uses sunscreen in summer.
Knits as a hobby.
In 2005, lipase was 30 U/L.
Pupils equal and reactive to light.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Her friend has a lazy eye.
Lives in a second-floor apartment.
HbA1c 5.3% at a routine check.
During a checkup in 2023, total protein was 7.0 g/dL.
Lives with a mechanical aortic valve prosthesis.
Prefers to be addressed by first name.
Her roommate wears contact lenses.
Drives a car.
Free T4 of 1.2 ng/dL in 2018.
Sleeps seven hours a night.
Sees a dentist yearly.
Her uncle has recovered from a dislocated finger.
In 2015, folate was 12 ng/mL.
Has two cats.
```

**flip** (answer: s')
```
-Current platelet count 315 x10^9/L.
+Current platelet count 47 x10^9/L.
```

**near** (answer: s)
```
-Current platelet count 315 x10^9/L.
+Current platelet count 50 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 26 lines, same state)
```


## 47. `rule_v1.test.gs216.c2.negation.easy.274`

- **Rule** (gs216, g_all_of): For primary prevention, prescribe atorvastatin. If the age of the patient is 75 years or more and the patient has ever had a venous thromboembolism (current or past), prescribe ezetimibe instead.
- **Condition**: venous thromboembolism | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
Woman, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 79 years.
Uses sunscreen in summer.
Coagulation tests normal on recent bloodwork.
```

**flip** (answer: s')
```
-Coagulation tests normal on recent bloodwork.
+Has an acute pulmonary embolism, diagnosed this week.
```

**near** (answer: s)
```
-Coagulation tests normal on recent bloodwork.
+Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 48. `rule_v1.test.curb65.age.numeric.easy.435`

- **Rule** (curb65, additive_score): CURB-65 (as used here): 1 point each for new confusion; blood urea nitrogen above 19 mg/dL; respiratory rate of 30/min or more; systolic blood pressure below 90 mmHg; age 65 years or more. Only current findings count.
- **Condition**: age at least 65 | near-miss: numeric | tier: easy
- **Claims**: s = "The age criterion contributes 0 points." | s' = "The age criterion contributes 1 point."

```
Woman, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Current systolic blood pressure 106 mmHg.
Pupils equal and reactive to light.
Observations now: respiratory rate 14/min.
Blood urea nitrogen now: 16 mg/dL.
Currently aged 59 years.
Photographs local wildlife.
Sleeps seven hours a night.
```

**flip** (answer: s')
```
-Currently aged 59 years.
+Currently aged 72 years.
```

**near** (answer: s)
```
-Currently aged 59 years.
+Currently aged 63 years.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 49. `rule_v1.test.gs025.c1.subject.easy.953`

- **Rule** (gs025, g_all_of): For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.
- **Condition**: myocardial infarction or peripheral artery disease | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe penicillin V."

```
Male patient of 32 years.
Sore throat for two days.
Temperature now 38.2 C (tympanic).
Prefers morning appointments.
Ankle-brachial index normal today.
Paints watercolors as a hobby.
```

**flip** (answer: s')
```
-Ankle-brachial index normal today.
+Lives with peripheral artery disease affecting the left leg.
```

**near** (answer: s)
```
-Ankle-brachial index normal today.
+His friend has peripheral artery disease with leg pain.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 50. `rule_v1.test.s3_aims65.ams.time.easy.1971`

- **Rule** (s3_aims65, additive_score): AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.
- **Condition**: altered mental status | near-miss: time | tier: easy
- **Claims**: s = "The altered mental status criterion contributes 0 points." | s' = "The altered mental status criterion contributes 1 point."

```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Current systolic blood pressure 113 mmHg.
Currently aged 43 years.
Latest international normalized ratio (INR): 1.2.
Gives a clear account of the illness.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Knits as a hobby.
```

**flip** (answer: s')
```
-Gives a clear account of the illness.
+Newly disoriented and unable to give a clear history.
```

**near** (answer: s)
```
-Gives a clear account of the illness.
+Formerly had an episode of confusion with dehydration in 2014.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 51. `rule_v1.test.gs123.c3.boundary.easy.1309`

- **Rule** (gs123, g_two_of_three): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.
- **Condition**: serum potassium above 5.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
Woman of 39 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Current antiplatelet drugs: none.
Insulin-treated diabetes.
Current serum potassium 4.5 mmol/L.
Paints watercolors as a hobby.
```

**flip** (answer: s')
```
-Current serum potassium 4.5 mmol/L.
+Current serum potassium 5.5 mmol/L.
```

**near** (answer: s)
```
-Current serum potassium 4.5 mmol/L.
+Current serum potassium 5.0 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 52. `rule_v1.test.s2_geneva.hemoptysis.negation.easy.1288`

- **Rule** (s2_geneva, additive_score): Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.
- **Condition**: hemoptysis | near-miss: negation | tier: easy
- **Claims**: s = "The hemoptysis criterion contributes 0 points." | s' = "The hemoptysis criterion contributes 2 points."

```
Man, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Weight steady over the past year.
Pupils equal and reactive to light.
Sputum colorless on inspection.
Current age 57 years.
Enjoys board games.
```

**flip** (answer: s')
```
-Sputum colorless on inspection.
+Currently coughing up blood with each bout of coughing.
```

**near** (answer: s)
```
-Sputum colorless on inspection.
+Has never coughed up blood.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 53. `rule_v1.test.s1_meds.age.numeric.easy.1036`

- **Rule** (s1_meds, additive_score): Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.
- **Condition**: age above 65 | near-miss: numeric | tier: easy
- **Claims**: s = "The age criterion contributes 0 points." | s' = "The age criterion contributes 3 points."

```
An adult woman.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Currently aged 58 years.
Speech clear; follows commands.
Sees a dentist yearly.
Platelet count now 295 x10^9/L.
Teeth in good repair.
Owns a bicycle.
```

**flip** (answer: s')
```
-Currently aged 58 years.
+Currently aged 73 years.
```

**near** (answer: s)
```
-Currently aged 58 years.
+Currently aged 64 years.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 54. `rule_v1.test.gs246.c2.subject.long.586`

- **Rule** (gs246, g_two_of_three): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.
- **Condition**: angioedema | near-miss: subject | tier: long
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
Woman of 59 years.
Acute low back pain after lifting.
Has melanoma skin cancer and is receiving treatment for it.
Has two cats.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Latest WBC is 7.8 x10^9/L.
Her father wears contact lenses.
Zinc of 85 mcg/dL in 2018.
Uses sunscreen in summer.
Her sister sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2009.
During a checkup in 2014, total protein was 7.0 g/dL.
Her uncle lives with psoriasis.
```

**flip** (answer: s')
```
+Lives with chronic angioedema that flares several times a year.
```

**near** (answer: s)
```
+Her sister has active angioedema of the face.
```

**pres** (answer: s)
```
(re-rendered: 19 lines, same state)
```


## 55. `rule_v1.test.c3_edoxaban_dose.egfr.time.superseded.219`

- **Rule** (c3_edoxaban_dose, any_of): For stroke prevention in atrial fibrillation, prescribe edoxaban 60 mg daily. If the current eGFR is 50 mL/min/1.73 m2 or less or the current weight is 60 kg or less, prescribe edoxaban 30 mg daily instead.
- **Condition**: eGFR at or below 50 | near-miss: time | tier: superseded
- **Claims**: s = "Prescribe edoxaban 60 mg daily." | s' = "Prescribe edoxaban 30 mg daily."

```
Woman of 58 years.
Atrial fibrillation without valve disease; starting an oral anticoagulant.
Plays the piano.
Latest weight 97 kg.
eGFR now 64 mL/min/1.73 m2.
Last month, eGFR was 62 mL/min/1.73 m2; the newest measurement replaces it.
Paints watercolors as a hobby.
Owns a bicycle.
```

**flip** (answer: s')
```
-eGFR now 64 mL/min/1.73 m2.
+eGFR now 50 mL/min/1.73 m2.
```

**near** (answer: s)
```
-Last month, eGFR was 62 mL/min/1.73 m2; the newest measurement replaces it.
+Last month, eGFR was 39 mL/min/1.73 m2; the newest measurement replaces it.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 56. `rule_v1.test.gs223.c3.boundary.easy.1496`

- **Rule** (gs223, g_two_of_three): For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current blood urea nitrogen is above 19 mg/dL.
- **Condition**: blood urea nitrogen above 19 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Female patient of 19 years.
Requests contraception.
Blood urea nitrogen 11 mg/dL on the current labs.
Lives in a second-floor apartment.
Lives with colon cancer and attends an oncology clinic.
```

**flip** (answer: s')
```
-Blood urea nitrogen 11 mg/dL on the current labs.
+Blood urea nitrogen 26 mg/dL on the current labs.
```

**near** (answer: s)
```
-Blood urea nitrogen 11 mg/dL on the current labs.
+Blood urea nitrogen 19 mg/dL on the current labs.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 57. `rule_v1.test.gs195.c1.negation.long.771`

- **Rule** (gs195, g_all_of): For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the patient has ever had a myocardial infarction or peripheral artery disease (current or past), prescribe fondaparinux instead.
- **Condition**: venous thromboembolism (patient or first-degree relative) | near-miss: negation | tier: long
- **Claims**: s = "Prescribe enoxaparin." | s' = "Prescribe fondaparinux."

```
Male patient of 63 years.
First day after elective total hip replacement.
Knits as a hobby.
During a checkup in 2015, total protein was 7.0 g/dL.
Uses sunscreen in summer.
His friend sprained a thumb last month.
Teeth in good repair.
In 2018, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2019.
Prefers morning appointments.
Photographs local wildlife.
Plays the piano.
Recovered from a heart attack in 2012.
Sleeps seven hours a night.
Has two cats.
Pupils equal and reactive to light.
Owns a bicycle.
Enjoys board games.
His roommate burned a hand on a stove years ago.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Sees a dentist yearly.
During a checkup in 2009, free T3 was 3.2 pg/mL.
```

**flip** (answer: s')
```
+Has an acute pulmonary embolism, diagnosed this week.
```

**near** (answer: s)
```
+Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.
```

**pres** (answer: s)
```
(re-rendered: 23 lines, same state)
```


## 58. `rule_v1.test.gs108.c2.numeric.easy.1147`

- **Rule** (gs108, g_any_of): For heart failure with reduced ejection fraction, prescribe spironolactone. If the current white cell count is above 12.0 x10^9/L or the current temperature is above 38.0 C, prescribe dapagliflozin instead.
- **Condition**: temperature above 38.0 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe spironolactone." | s' = "Prescribe dapagliflozin."

```
Female patient of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Temperature now 37.2 C (tympanic).
Latest WBC is 5.9 x10^9/L.
```

**flip** (answer: s')
```
-Temperature now 37.2 C (tympanic).
+Temperature now 38.3 C (tympanic).
```

**near** (answer: s)
```
-Temperature now 37.2 C (tympanic).
+Temperature now 37.8 C (tympanic).
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 59. `rule_v1.test.gs075.c2.subject.long.1841`

- **Rule** (gs075, g_two_of_three): For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.
- **Condition**: warfarin | near-miss: subject | tier: long
- **Claims**: s = "Prescribe lisinopril." | s' = "Prescribe amlodipine."

```
Woman of 62 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Prefers morning appointments.
Her father burned a hand on a stove years ago.
Her sister has a lazy eye.
Has two cats.
Plays the piano.
Zinc of 85 mcg/dL in 2022.
Photographs local wildlife.
In 2016, folate was 12 ng/mL.
Her father recovered from colon cancer after an operation in 2018.
Paints watercolors as a hobby.
Her uncle sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2009.
Uses sunscreen in summer.
Current calf swelling 0.5 cm compared with the other leg.
Sleeps seven hours a night.
Enjoys board games.
Knits as a hobby.
Prefers to be addressed by first name.
```

**flip** (answer: s')
```
+Anticoagulated with warfarin; INR checked monthly at the clinic.
```

**near** (answer: s)
```
+Her wife is on warfarin with monthly INR checks.
```

**pres** (answer: s)
```
(re-rendered: 20 lines, same state)
```


## 60. `rule_v1.test.s3_alvarado.temp.time.easy.38`

- **Rule** (s3_alvarado, additive_score): Alvarado score (as used here, partial): 2 points for current tenderness in the right lower quadrant (right iliac fossa); 2 points for a current white cell count above 10.0 x10^9/L; 1 point for a current temperature of 37.3 C or more. Other Alvarado items are not part of this question.
- **Condition**: temperature at least 37.3 | near-miss: time | tier: easy
- **Claims**: s = "The temperature criterion contributes 0 points." | s' = "The temperature criterion contributes 1 point."

```
Female patient of 56 years.
Abdominal pain for one day; assessed in the emergency department.
Pupils equal and reactive to light.
Abdominal examination unremarkable, without tenderness.
Temperature now 36.3 C (tympanic).
Records from 2014 list temperature at 36.5 C.
Teeth in good repair.
Latest WBC is 7.0 x10^9/L.
```

**flip** (answer: s')
```
-Temperature now 36.3 C (tympanic).
+Temperature now 38.1 C (tympanic).
```

**near** (answer: s)
```
-Records from 2014 list temperature at 36.5 C.
+Records from 2014 list temperature at 38.2 C.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 61. `rule_v1.test.gs088.c3.boundary.easy.1525`

- **Rule** (gs088, g_two_of_three): For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.
- **Condition**: white cell count above 12.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe penicillin V."

```
Male patient of 56 years.
Sore throat for two days.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Latest WBC is 7.8 x10^9/L.
Has symptomatic peripheral artery disease of both legs.
Tonsils pink and clean on inspection.
Enjoys board games.
Knits as a hobby.
```

**flip** (answer: s')
```
-Latest WBC is 7.8 x10^9/L.
+Latest WBC is 12.9 x10^9/L.
```

**near** (answer: s)
```
-Latest WBC is 7.8 x10^9/L.
+Latest WBC is 12.0 x10^9/L.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 62. `rule_v1.test.s2_geneva.cancer.negation.long.1241`

- **Rule** (s2_geneva, additive_score): Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.
- **Condition**: active cancer | near-miss: negation | tier: long
- **Claims**: s = "The active cancer criterion contributes 0 points." | s' = "The active cancer criterion contributes 2 points."

```
Man, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Zinc of 85 mcg/dL in 2024.
In 2016, folate was 12 ng/mL.
Lives in a second-floor apartment.
Owns a bicycle.
Pupils equal and reactive to light.
His father has recovered from a dislocated finger.
Teeth in good repair.
Photographs local wildlife.
Has two cats.
His wife burned a hand on a stove years ago.
Dry cough, with nothing brought up.
His uncle wears contact lenses.
His father lives with psoriasis.
Prefers morning appointments.
Prefers to be addressed by first name.
Oncology follow-up: none.
Knits as a hobby.
Paints watercolors as a hobby.
Drives a car.
Current age 58 years.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Plays the piano.
```

**flip** (answer: s')
```
-Oncology follow-up: none.
+Has melanoma skin cancer and is receiving treatment for it.
```

**near** (answer: s)
```
-Oncology follow-up: none.
+Free of cancer throughout life.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 63. `rule_v1.test.gs002.c2.numeric.easy.1004`

- **Rule** (gs002, g_any_of): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.
- **Condition**: serum potassium above 4.8 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe trimethoprim-sulfamethoxazole." | s' = "Prescribe nitrofurantoin."

```
Female patient of 67 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Lives in a second-floor apartment.
Heart rate now 76/min on a pulse check.
Current serum potassium 4.0 mmol/L.
```

**flip** (answer: s')
```
-Current serum potassium 4.0 mmol/L.
+Current serum potassium 5.1 mmol/L.
```

**near** (answer: s)
```
-Current serum potassium 4.0 mmol/L.
+Current serum potassium 4.7 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 64. `rule_v1.test.gs065.c3.subject.easy.1251`

- **Rule** (gs065, g_two_of_three): For knee osteoarthritis pain, prescribe naproxen. If at least two of the following apply, prescribe acetaminophen instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the patient has ever had angioedema (current or past).
- **Condition**: angioedema | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe naproxen." | s' = "Prescribe acetaminophen."

```
Man of 83 years.
Knee osteoarthritis with pain on walking.
Free of facial or oropharyngeal edema.
Knits as a hobby.
Plays the piano.
His sister has angina from coronary artery disease.
Sleeps seven hours a night.
Current calf swelling 0.6 cm compared with the other leg.
```

**flip** (answer: s')
```
-Free of facial or oropharyngeal edema.
+An episode of angioedema years ago, with full recovery.
```

**near** (answer: s)
```
-Free of facial or oropharyngeal edema.
+His wife recovered from an episode of angioedema in 2016.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 65. `rule_v1.test.gs196.c2.time.delabelled.681`

- **Rule** (gs196, g_all_of): For musculoskeletal pain, prescribe ibuprofen. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time and the patient is allergic to penicillin, prescribe acetaminophen instead.
- **Condition**: penicillin allergy | near-miss: time | tier: delabelled
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
Male patient of 55 years.
Acute low back pain after lifting.
His father was formerly under the care of a cardiologist for coronary artery disease.
Prefers morning appointments.
```

**flip** (answer: s')
```
+Known penicillin allergy with angioedema.
```

**near** (answer: s)
```
+Formerly recorded as penicillin-allergic; de-labeled in 2013 by an allergy clinic.
```

**pres** (answer: s)
```
(re-rendered: 4 lines, same state)
```


## 66. `rule_v1.test.gs052.c2.boundary.easy.1349`

- **Rule** (gs052, g_any_of): For primary prevention, prescribe atorvastatin. If the current heart rate is above 90/min or the current serum potassium is above 5.0 mmol/L, prescribe ezetimibe instead.
- **Condition**: serum potassium above 5.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 4.1 mmol/L.
Plays the piano.
```

**flip** (answer: s')
```
-Current serum potassium 4.1 mmol/L.
+Current serum potassium 5.2 mmol/L.
```

**near** (answer: s)
```
-Current serum potassium 4.1 mmol/L.
+Current serum potassium 5.0 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 67. `rule_v1.test.gs075.c2.negation.long.379`

- **Rule** (gs075, g_two_of_three): For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.
- **Condition**: warfarin | near-miss: negation | tier: long
- **Claims**: s = "Prescribe lisinopril." | s' = "Prescribe amlodipine."

```
Male patient of 34 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
During a checkup in 2018, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Owns a bicycle.
His friend lives with psoriasis.
Prefers morning appointments.
Has two cats.
Zinc of 85 mcg/dL in 2013.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Sees a dentist yearly.
His wife wears contact lenses.
His sister has a lazy eye.
Free T4 of 1.2 ng/dL in 2015.
His sister recovered from colon cancer after an operation in 2024.
Photographs local wildlife.
Current calf swelling 0.8 cm compared with the other leg.
Lives in a second-floor apartment.
His uncle has recovered from a dislocated finger.
```

**flip** (answer: s')
```
+Currently on warfarin, prescribed by the cardiology clinic.
```

**near** (answer: s)
```
+Warfarin is absent from the current medication list.
```

**pres** (answer: s)
```
(re-rendered: 20 lines, same state)
```


## 68. `rule_v1.test.gs033.c1.numeric.easy.61`

- **Rule** (gs033, g_two_of_three): For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.
- **Condition**: weight at or below 60 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe cephalexin." | s' = "Prescribe clindamycin."

```
Female patient of 35 years.
Spreading redness and warmth of the right shin for two days.
Drug allergies: none known.
Paints watercolors as a hobby.
Plays the piano.
Her sister was formerly under the care of a cardiologist for coronary artery disease.
Teeth in good repair.
Latest weight 75 kg.
Enjoys board games.
```

**flip** (answer: s')
```
-Latest weight 75 kg.
+Latest weight 50 kg.
```

**near** (answer: s)
```
-Latest weight 75 kg.
+Latest weight 61 kg.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 69. `rule_v1.test.gs211.c3.subject.easy.1356`

- **Rule** (gs211, g_two_of_three): For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the current blood urea nitrogen is above 19 mg/dL; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient has an active peptic ulcer.
- **Condition**: active peptic ulcer | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe apixaban." | s' = "Prescribe warfarin."

```
Man of 74 years.
Atrial fibrillation; anticoagulation indicated.
His sister lives with type 1 diabetes.
Prefers to be addressed by first name.
Blood urea nitrogen now: 12 mg/dL.
Appetite good; no indigestion.
Knits as a hobby.
```

**flip** (answer: s')
```
-Appetite good; no indigestion.
+Has an active duodenal ulcer.
```

**near** (answer: s)
```
-Appetite good; no indigestion.
+His sister has peptic ulcer disease.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 70. `rule_v1.test.gs137.c2.time.long.55`

- **Rule** (gs137, g_all_of): For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.
- **Condition**: serum creatinine at least 1.5 | near-miss: time | tier: long
- **Claims**: s = "Prescribe naproxen alone." | s' = "Prescribe naproxen with omeprazole."

```
Male patient of 59 years.
Hip osteoarthritis with pain on walking.
Uses sunscreen in summer.
Plays the piano.
Back in 2009, serum creatinine stood at 1.0 mg/dL.
Sees a dentist yearly.
Drives a car.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Knits as a hobby.
Has two cats.
Free T4 of 1.2 ng/dL in 2017.
In 2007, folate was 12 ng/mL.
His uncle has recovered from a dislocated finger.
Latest creatinine result: 0.8 mg/dL.
Paints watercolors as a hobby.
His uncle lives with psoriasis.
Photographs local wildlife.
Had diabetes years ago that went into remission on a low-calorie diet.
His roommate wears contact lenses.
His father has a lazy eye.
Enjoys board games.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
```

**flip** (answer: s')
```
-Latest creatinine result: 0.8 mg/dL.
+Latest creatinine result: 1.7 mg/dL.
```

**near** (answer: s)
```
-Back in 2009, serum creatinine stood at 1.0 mg/dL.
+Back in 2009, serum creatinine stood at 1.6 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 71. `rule_v1.test.gs011.c2.boundary.easy.102`

- **Rule** (gs011, g_all_of): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the current ALT is above 120 U/L, prescribe azithromycin instead.
- **Condition**: ALT above 120 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe amoxicillin." | s' = "Prescribe azithromycin."

```
Male patient of 54 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Paints watercolors as a hobby.
Recovered from a pulmonary embolism in 2011.
Current ALT 26 U/L.
Prefers morning appointments.
Drives a car.
```

**flip** (answer: s')
```
-Current ALT 26 U/L.
+Current ALT 132 U/L.
```

**near** (answer: s)
```
-Current ALT 26 U/L.
+Current ALT 120 U/L.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 72. `rule_v1.test.gs011.c1.negation.easy.1164`

- **Rule** (gs011, g_all_of): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the current ALT is above 120 U/L, prescribe azithromycin instead.
- **Condition**: venous thromboembolism (patient or first-degree relative) | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe amoxicillin." | s' = "Prescribe azithromycin."

```
Female patient of 70 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Current ALT 126 U/L.
Varicose veins: none seen.
Paints watercolors as a hobby.
Teeth in good repair.
```

**flip** (answer: s')
```
-Varicose veins: none seen.
+Ongoing treatment for a deep vein thrombosis of the left arm.
```

**near** (answer: s)
```
-Varicose veins: none seen.
+Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 73. `rule_v1.test.gs096.c4.numeric.long.1965`

- **Rule** (gs096, g_score_cutoff): For stroke prevention in atrial fibrillation, prescribe apixaban. Score 2 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient currently has tonsillar exudate; 2 points if the current ALT is above 120 U/L; 2 points if the current weight is 60 kg or less. If the score is 6 or more, prescribe warfarin instead.
- **Condition**: weight at or below 60 | near-miss: numeric | tier: long
- **Claims**: s = "Prescribe apixaban." | s' = "Prescribe warfarin."

```
Woman of 71 years.
Atrial fibrillation; anticoagulation indicated.
Owns a bicycle.
Paints watercolors as a hobby.
Her sister has a lazy eye.
Sees a dentist yearly.
Uses sunscreen in summer.
Had coronary artery disease, treated with bypass surgery in 2007; recovered well.
During a checkup in 2010, free T3 was 3.2 pg/mL.
Latest weight 68 kg.
Photographs local wildlife.
Her sister wears contact lenses.
Prefers to be addressed by first name.
ALT now 142 U/L.
Tonsils a little red, surfaces clear.
Knits as a hobby.
Has two cats.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2021.
Her friend burned a hand on a stove years ago.
Plays the piano.
Her roommate sprained a thumb last month.
Lives in a second-floor apartment.
In 2007, lipase was 30 U/L.
```

**flip** (answer: s')
```
-Latest weight 68 kg.
+Latest weight 54 kg.
```

**near** (answer: s)
```
-Latest weight 68 kg.
+Latest weight 61 kg.
```

**pres** (answer: s)
```
(re-rendered: 25 lines, same state)
```


## 74. `rule_v1.test.gs196.c1.subject.easy.1995`

- **Rule** (gs196, g_all_of): For musculoskeletal pain, prescribe ibuprofen. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time and the patient is allergic to penicillin, prescribe acetaminophen instead.
- **Condition**: coronary artery disease (patient or first-degree relative) | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
Male patient of 65 years.
Acute low back pain after lifting.
Has two cats.
Lives in a second-floor apartment.
Penicillin allergy: anaphylaxis.
```

**flip** (answer: s')
```
+Has coronary artery disease, managed medically.
```

**near** (answer: s)
```
+His wife has angina from coronary artery disease.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 75. `rule_v1.test.gs155.c2.time.long.567`

- **Rule** (gs155, g_two_of_three): For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had a peptic ulcer (current or past); the current serum potassium is above 5.0 mmol/L; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.
- **Condition**: serum potassium above 5.0 | near-miss: time | tier: long
- **Claims**: s = "Prescribe metformin." | s' = "Prescribe sitagliptin."

```
Male patient of 54 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has two cats.
Pupils equal and reactive to light.
Coagulation tests normal on recent bloodwork.
In 2023, lipase was 30 U/L.
Prefers morning appointments.
In 2020, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2020.
Latest potassium result: 4.4 mmol/L.
His father wears contact lenses.
Records from 2015 list serum potassium at 4.0 mmol/L.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
Photographs local wildlife.
His wife has recovered from a dislocated finger.
Teeth in good repair.
Uses sunscreen in summer.
Plays the piano.
Active peptic ulcer disease.
During a checkup in 2019, total protein was 7.0 g/dL.
Owns a bicycle.
```

**flip** (answer: s')
```
-Latest potassium result: 4.4 mmol/L.
+Latest potassium result: 5.5 mmol/L.
```

**near** (answer: s)
```
-Records from 2015 list serum potassium at 4.0 mmol/L.
+Records from 2015 list serum potassium at 5.9 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 76. `rule_v1.test.gs021.c2.boundary.easy.502`

- **Rule** (gs021, g_any_of): For hip osteoarthritis pain, prescribe naproxen alone. If the current systolic blood pressure is above 160 mmHg or the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.
- **Condition**: serum creatinine above 2.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe naproxen alone." | s' = "Prescribe naproxen with omeprazole."

```
Man of 50 years.
Hip osteoarthritis with pain on walking.
Current systolic blood pressure 122 mmHg.
Latest creatinine result: 0.9 mg/dL.
Owns a bicycle.
```

**flip** (answer: s')
```
-Latest creatinine result: 0.9 mg/dL.
+Latest creatinine result: 2.6 mg/dL.
```

**near** (answer: s)
```
-Latest creatinine result: 0.9 mg/dL.
+Latest creatinine result: 2.0 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 77. `rule_v1.test.gs096.c1.negation.easy.366`

- **Rule** (gs096, g_score_cutoff): For stroke prevention in atrial fibrillation, prescribe apixaban. Score 2 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient currently has tonsillar exudate; 2 points if the current ALT is above 120 U/L; 2 points if the current weight is 60 kg or less. If the score is 6 or more, prescribe warfarin instead.
- **Condition**: coronary artery disease | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe apixaban." | s' = "Prescribe warfarin."

```
Man of 66 years.
Atrial fibrillation; anticoagulation indicated.
Tonsils swollen and coated with yellow exudate.
Cardiac stress test unremarkable last year.
Sees a dentist yearly.
Teeth in good repair.
Current ALT 31 U/L.
Latest weight 60 kg.
Lives in a second-floor apartment.
```

**flip** (answer: s')
```
-Cardiac stress test unremarkable last year.
+Has coronary artery disease, managed medically.
```

**near** (answer: s)
```
-Cardiac stress test unremarkable last year.
+Never diagnosed with coronary artery disease.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 78. `rule_v1.test.gs219.c2.numeric.easy.785`

- **Rule** (gs219, g_two_of_three): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).
- **Condition**: serum potassium above 5.0 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
Female patient of 55 years.
Acute low back pain after lifting.
Current serum potassium 4.1 mmol/L.
Pupils equal and reactive to light.
Tonsils swollen and coated with yellow exudate.
```

**flip** (answer: s')
```
-Current serum potassium 4.1 mmol/L.
+Current serum potassium 5.8 mmol/L.
```

**near** (answer: s)
```
-Current serum potassium 4.1 mmol/L.
+Current serum potassium 4.8 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 79. `rule_v1.test.gs094.c1.subject.easy.591`

- **Rule** (gs094, g_all_of): For primary prevention, prescribe atorvastatin. If the patient has ever had heart failure (current or past) and the age of the patient is 75 years or more, prescribe ezetimibe instead.
- **Condition**: heart failure | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Currently aged 78 years.
Sleeps flat on one pillow.
Pupils equal and reactive to light.
```

**flip** (answer: s')
```
-Sleeps flat on one pillow.
+Current heart failure with ankle swelling.
```

**near** (answer: s)
```
-Sleeps flat on one pillow.
+His roommate has advanced heart failure.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 80. `rule_v1.test.s2_wells_pe.hemoptysis.time.easy.447`

- **Rule** (s2_wells_pe, additive_score): Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.
- **Condition**: hemoptysis | near-miss: time | tier: easy
- **Claims**: s = "The hemoptysis criterion contributes 0 points." | s' = "The hemoptysis criterion contributes 1 point."

```
Man of 58 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Pupils equal and reactive to light.
Sputum colorless on inspection.
Heart rate now 88/min on a pulse check.
Oncology follow-up: none.
Paints watercolors as a hobby.
Photographs local wildlife.
Teeth in good repair.
```

**flip** (answer: s')
```
-Sputum colorless on inspection.
+Coughing up blood now, mixed with the sputum.
```

**near** (answer: s)
```
-Sputum colorless on inspection.
+Formerly coughed up blood from bronchiectasis, which settled after surgery in 2008.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 81. `rule_v1.test.gs024.c3.boundary.easy.1885`

- **Rule** (gs024, g_score_cutoff): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 3 points if the current ALT is above 120 U/L; 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 3 points if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 4 or more, prescribe nitrofurantoin instead.
- **Condition**: systolic blood pressure above 160 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe trimethoprim-sulfamethoxazole." | s' = "Prescribe nitrofurantoin."

```
Woman of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Insulin-treated diabetes.
Has two cats.
ALT now 37 U/L.
Enjoys board games.
Paints watercolors as a hobby.
Current systolic blood pressure 120 mmHg.
```

**flip** (answer: s')
```
-Current systolic blood pressure 120 mmHg.
+Current systolic blood pressure 173 mmHg.
```

**near** (answer: s)
```
-Current systolic blood pressure 120 mmHg.
+Current systolic blood pressure 160 mmHg.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 82. `rule_v1.test.gs219.c3.negation.long.348`

- **Rule** (gs219, g_two_of_three): For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).
- **Condition**: coronary artery disease | near-miss: negation | tier: long
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe acetaminophen."

```
Female patient of 61 years.
Acute low back pain after lifting.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Has two cats.
Photographs local wildlife.
Owns a bicycle.
Tonsillar exudate visible on both sides.
Sees a dentist yearly.
Her father burned a hand on a stove years ago.
In 2018, folate was 12 ng/mL.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Plays the piano.
Her friend has recovered from a dislocated finger.
Enjoys board games.
Pupils equal and reactive to light.
Teeth in good repair.
Drives a car.
Her wife wears contact lenses.
Cardiac stress test unremarkable last year.
Latest potassium result: 4.2 mmol/L.
```

**flip** (answer: s')
```
-Cardiac stress test unremarkable last year.
+Known coronary artery disease (two-vessel disease on angiography).
```

**near** (answer: s)
```
-Cardiac stress test unremarkable last year.
+Has never had coronary artery disease.
```

**pres** (answer: s)
```
(re-rendered: 21 lines, same state)
```


## 83. `rule_v1.test.gs113.c1.numeric.easy.195`

- **Rule** (gs113, g_all_of): For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum creatinine is above 2.0 mg/dL and the patient has ever had heart failure (current or past), prescribe aspirin plus clopidogrel instead.
- **Condition**: serum creatinine above 2.0 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe aspirin plus ticagrelor." | s' = "Prescribe aspirin plus clopidogrel."

```
Female patient of 48 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Has two cats.
Latest creatinine result: 1.0 mg/dL.
Has heart failure, treated with diuretics.
```

**flip** (answer: s')
```
-Latest creatinine result: 1.0 mg/dL.
+Latest creatinine result: 2.6 mg/dL.
```

**near** (answer: s)
```
-Latest creatinine result: 1.0 mg/dL.
+Latest creatinine result: 1.9 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 84. `rule_v1.test.gs211.c3.subject.long.445`

- **Rule** (gs211, g_two_of_three): For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the current blood urea nitrogen is above 19 mg/dL; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient has an active peptic ulcer.
- **Condition**: active peptic ulcer | near-miss: subject | tier: long
- **Claims**: s = "Prescribe apixaban." | s' = "Prescribe warfarin."

```
Woman of 50 years.
Atrial fibrillation; anticoagulation indicated.
Enjoys board games.
Blood urea nitrogen 26 mg/dL on the current labs.
Prefers to be addressed by first name.
Has two cats.
Knits as a hobby.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Prefers morning appointments.
Teeth in good repair.
Her roommate burned a hand on a stove years ago.
Paints watercolors as a hobby.
Appetite good; no indigestion.
Owns a bicycle.
Plays the piano.
Zinc of 85 mcg/dL in 2023.
Drives a car.
In 2008, lipase was 30 U/L.
Her friend has a lazy eye.
Sees a dentist yearly.
Photographs local wildlife.
Pupils equal and reactive to light.
```

**flip** (answer: s')
```
-Appetite good; no indigestion.
+Has an active duodenal ulcer.
```

**near** (answer: s)
```
-Appetite good; no indigestion.
+Her wife has peptic ulcer disease.
```

**pres** (answer: s)
```
(re-rendered: 23 lines, same state)
```


## 85. `rule_v1.test.gs054.c1.time.long.597`

- **Rule** (gs054, g_score_cutoff): For community-acquired pneumonia, prescribe oral amoxicillin. Score 3 points if the patient currently has a venous thromboembolism; 2 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current respiratory rate is 22/min or more; 1 point if the current oxygen saturation is 91% or less. If the score is 6 or more, prescribe intravenous co-amoxiclav instead.
- **Condition**: current venous thromboembolism | near-miss: time | tier: long
- **Claims**: s = "Prescribe oral amoxicillin." | s' = "Prescribe intravenous co-amoxiclav."

```
Woman of 87 years.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers morning appointments.
Pupils equal and reactive to light.
During a checkup in 2018, total protein was 7.0 g/dL.
In 2013, folate was 12 ng/mL.
Uses sunscreen in summer.
Teeth in good repair.
Coagulation tests normal on recent bloodwork.
Latest oxygen saturation reading: 85%.
Enjoys board games.
Knits as a hobby.
Prefers to be addressed by first name.
Owns a bicycle.
Has two cats.
Paints watercolors as a hobby.
Current respiratory rate 27/min.
Formerly had colon cancer; recovered fully after an operation in 2020.
Free T4 of 1.2 ng/dL in 2005.
In 2008, lipase was 30 U/L.
Her sister lives with psoriasis.
Her sister sprained a thumb last month.
Her friend burned a hand on a stove years ago.
```

**flip** (answer: s')
```
-Coagulation tests normal on recent bloodwork.
+Has an acute pulmonary embolism, diagnosed this week.
```

**near** (answer: s)
```
-Coagulation tests normal on recent bloodwork.
+Recovered from a pulmonary embolism in 2006.
```

**pres** (answer: s)
```
(re-rendered: 23 lines, same state)
```


## 86. `rule_v1.test.gs223.c3.boundary.easy.1574`

- **Rule** (gs223, g_two_of_three): For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current blood urea nitrogen is above 19 mg/dL.
- **Condition**: blood urea nitrogen above 19 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Woman of 32 years.
Requests contraception.
Hemoglobin within the normal range on recent blood tests.
Insulin-treated diabetes.
Teeth in good repair.
Plays the piano.
Blood urea nitrogen now: 13 mg/dL.
Has two cats.
```

**flip** (answer: s')
```
-Blood urea nitrogen now: 13 mg/dL.
+Blood urea nitrogen now: 26 mg/dL.
```

**near** (answer: s)
```
-Blood urea nitrogen now: 13 mg/dL.
+Blood urea nitrogen now: 19 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 87. `rule_v1.test.gs220.c2.negation.easy.1873`

- **Rule** (gs220, g_all_of): For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.
- **Condition**: diabetes (patient or first-degree relative) | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe a combined oral contraceptive." | s' = "Prescribe a progestin-only pill."

```
Female patient of 35 years.
Requests contraception.
Prefers morning appointments.
eGFR now 18 mL/min/1.73 m2.
HbA1c 5.3% at a routine check.
```

**flip** (answer: s')
```
-HbA1c 5.3% at a routine check.
+Her sister was diabetic until bariatric surgery several years ago.
```

**near** (answer: s)
```
-HbA1c 5.3% at a routine check.
+Never diagnosed with diabetes.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 88. `rule_v1.test.gs245.c3.numeric.easy.1126`

- **Rule** (gs245, g_two_of_three): For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had heart failure (current or past); the patient has an active peptic ulcer; the age of the patient is 65 years or more.
- **Condition**: age at least 65 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe metformin." | s' = "Prescribe sitagliptin."

```
An adult man.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Paints watercolors as a hobby.
Uses sunscreen in summer.
Has heart failure, treated with diuretics.
Lives in a second-floor apartment.
Currently aged 43 years.
```

**flip** (answer: s')
```
-Currently aged 43 years.
+Currently aged 65 years.
```

**near** (answer: s)
```
-Currently aged 43 years.
+Currently aged 62 years.
```

**pres** (answer: s)
```
(re-rendered: 7 lines, same state)
```


## 89. `rule_v1.test.gs088.c2.subject.long.864`

- **Rule** (gs088, g_two_of_three): For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.
- **Condition**: myocardial infarction or peripheral artery disease | near-miss: subject | tier: long
- **Claims**: s = "Prescribe ibuprofen." | s' = "Prescribe penicillin V."

```
Woman of 17 years.
Sore throat for two days.
Zinc of 85 mcg/dL in 2024.
During a checkup in 2024, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Drives a car.
Her roommate lives with psoriasis.
Pupils equal and reactive to light.
Knits as a hobby.
Plays the piano.
Latest WBC is 13.2 x10^9/L.
Owns a bicycle.
Enjoys board games.
Prefers morning appointments.
Walks without calf pain.
Her uncle has a lazy eye.
Her uncle has recovered from a dislocated finger.
Uses sunscreen in summer.
Her father burned a hand on a stove years ago.
Tonsils pink and clean on inspection.
Has two cats.
In 2024, folate was 12 ng/mL.
```

**flip** (answer: s')
```
-Walks without calf pain.
+Recovered from a heart attack in 2024.
```

**near** (answer: s)
```
-Walks without calf pain.
+Her friend had a heart attack years ago.
```

**pres** (answer: s)
```
(re-rendered: 22 lines, same state)
```


## 90. `rule_v1.test.gs137.c2.time.easy.1984`

- **Rule** (gs137, g_all_of): For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.
- **Condition**: serum creatinine at least 1.5 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe naproxen alone." | s' = "Prescribe naproxen with omeprazole."

```
Man of 71 years.
Hip osteoarthritis with pain on walking.
Prefers morning appointments.
Latest creatinine result: 1.2 mg/dL.
Records from 2011 list serum creatinine at 1.0 mg/dL.
Has type 2 diabetes on metformin.
```

**flip** (answer: s')
```
-Latest creatinine result: 1.2 mg/dL.
+Latest creatinine result: 2.0 mg/dL.
```

**near** (answer: s)
```
-Records from 2011 list serum creatinine at 1.0 mg/dL.
+Records from 2011 list serum creatinine at 1.6 mg/dL.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 91. `rule_v1.test.gs011.c2.boundary.easy.185`

- **Rule** (gs011, g_all_of): For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the current ALT is above 120 U/L, prescribe azithromycin instead.
- **Condition**: ALT above 120 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe amoxicillin." | s' = "Prescribe azithromycin."

```
Male patient of 56 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Paints watercolors as a hobby.
Current ALT 51 U/L.
Has an acute pulmonary embolism, diagnosed this week.
```

**flip** (answer: s')
```
-Current ALT 51 U/L.
+Current ALT 147 U/L.
```

**near** (answer: s)
```
-Current ALT 51 U/L.
+Current ALT 120 U/L.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 92. `rule_v1.test.gs230.c4.negation.long.916`

- **Rule** (gs230, g_score_cutoff): For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 2 points if the patient currently has tonsillar exudate; 3 points if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past). If the score is 8 or more, prescribe nitrofurantoin instead.
- **Condition**: peptic ulcer at any time | near-miss: negation | tier: long
- **Claims**: s = "Prescribe trimethoprim-sulfamethoxazole." | s' = "Prescribe nitrofurantoin."

```
Female patient of 39 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Recovered from a heart attack in 2007.
Owns a bicycle.
Teeth in good repair.
Photographs local wildlife.
Drives a car.
Paints watercolors as a hobby.
Sees a dentist yearly.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Appetite good; no indigestion.
Free T4 of 1.2 ng/dL in 2013.
Zinc of 85 mcg/dL in 2011.
Knits as a hobby.
Tonsillar exudate visible on both sides.
Plays the piano.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Her roommate has recovered from a dislocated finger.
Difference in calf circumference now 3.5 cm.
Enjoys board games.
In 2016, lipase was 30 U/L.
Pupils equal and reactive to light.
Her sister lives with psoriasis.
```

**flip** (answer: s')
```
-Appetite good; no indigestion.
+Formerly treated for a peptic ulcer; endoscopy in 2018 showed it had gone.
```

**near** (answer: s)
```
-Appetite good; no indigestion.
+Has never had a peptic ulcer.
```

**pres** (answer: s)
```
(re-rendered: 24 lines, same state)
```


## 93. `rule_v1.test.gs131.c1.numeric.easy.374`

- **Rule** (gs131, g_score_cutoff): For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.
- **Condition**: eGFR below 45 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
Woman of 28 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sleeps seven hours a night.
eGFR now 62 mL/min/1.73 m2.
Has two cats.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Heart rate now 98/min on a pulse check.
Sees a dentist yearly.
```

**flip** (answer: s')
```
-eGFR now 62 mL/min/1.73 m2.
+eGFR now 42 mL/min/1.73 m2.
```

**near** (answer: s)
```
-eGFR now 62 mL/min/1.73 m2.
+eGFR now 47 mL/min/1.73 m2.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 94. `rule_v1.test.gs118.c2.subject.long.1933`

- **Rule** (gs118, g_score_cutoff): For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.
- **Condition**: angioedema | near-miss: subject | tier: long
- **Claims**: s = "Prescribe spironolactone." | s' = "Prescribe dapagliflozin."

```
Man of 79 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Knits as a hobby.
Has two cats.
His roommate has recovered from a dislocated finger.
Current white cell count 9.3 x10^9/L.
Free of facial or oropharyngeal edema.
His friend lives with psoriasis.
Owns a bicycle.
His friend sprained a thumb last month.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Photographs local wildlife.
During a checkup in 2010, free T3 was 3.2 pg/mL.
Current heart rate 96/min.
During a checkup in 2009, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
Enjoys board games.
Sleeps seven hours a night.
eGFR now 44 mL/min/1.73 m2.
His wife wears contact lenses.
Drives a car.
```

**flip** (answer: s')
```
-Free of facial or oropharyngeal edema.
+Formerly had recurrent angioedema, in remission for many years now.
```

**near** (answer: s)
```
-Free of facial or oropharyngeal edema.
+His sister recovered from an episode of angioedema in 2023.
```

**pres** (answer: s)
```
(re-rendered: 22 lines, same state)
```


## 95. `rule_v1.test.gs209.c3.time.easy.1061`

- **Rule** (gs209, g_two_of_three): For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.
- **Condition**: heart rate above 90 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe oral fluconazole." | s' = "Prescribe clotrimazole pessaries."

```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Has an active duodenal ulcer.
Prefers morning appointments.
Currently aged 43 years.
Back in 2007, heart rate stood at 71/min.
Heart rate now 58/min on a pulse check.
Plays the piano.
```

**flip** (answer: s')
```
-Heart rate now 58/min on a pulse check.
+Heart rate now 99/min on a pulse check.
```

**near** (answer: s)
```
-Back in 2007, heart rate stood at 71/min.
+Back in 2007, heart rate stood at 100/min.
```

**pres** (answer: s)
```
(re-rendered: 9 lines, same state)
```


## 96. `rule_v1.test.gs071.c1.boundary.easy.1695`

- **Rule** (gs071, g_all_of): For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.
- **Condition**: temperature above 38.0 | near-miss: boundary | tier: easy
- **Claims**: s = "Prescribe apixaban." | s' = "Prescribe warfarin."

```
Man of 57 years.
Atrial fibrillation; anticoagulation indicated.
Prefers morning appointments.
Formerly treated for a peptic ulcer; endoscopy in 2018 showed it had gone.
Current temperature 36.7 C.
```

**flip** (answer: s')
```
-Current temperature 36.7 C.
+Current temperature 38.6 C.
```

**near** (answer: s)
```
-Current temperature 36.7 C.
+Current temperature 38.0 C.
```

**pres** (answer: s)
```
(re-rendered: 5 lines, same state)
```


## 97. `rule_v1.test.gs094.c1.negation.easy.1184`

- **Rule** (gs094, g_all_of): For primary prevention, prescribe atorvastatin. If the patient has ever had heart failure (current or past) and the age of the patient is 75 years or more, prescribe ezetimibe instead.
- **Condition**: heart failure | near-miss: negation | tier: easy
- **Claims**: s = "Prescribe atorvastatin." | s' = "Prescribe ezetimibe."

```
An adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 79 years.
Photographs local wildlife.
Has two cats.
Heart sounds without a gallop.
```

**flip** (answer: s')
```
-Heart sounds without a gallop.
+Formerly had heart failure from stress cardiomyopathy; recovered fully in 2022 and off all heart medicines since.
```

**near** (answer: s)
```
-Heart sounds without a gallop.
+Heart failure: never diagnosed.
```

**pres** (answer: s)
```
(re-rendered: 6 lines, same state)
```


## 98. `rule_v1.test.gs048.c2.numeric.easy.324`

- **Rule** (gs048, g_any_of): For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.
- **Condition**: age at least 75 | near-miss: numeric | tier: easy
- **Claims**: s = "Prescribe spironolactone." | s' = "Prescribe dapagliflozin."

```
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Sleeps seven hours a night.
Currently aged 58 years.
Current weight 68 kg.
Drives a car.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

**flip** (answer: s')
```
-Currently aged 58 years.
+Currently aged 87 years.
```

**near** (answer: s)
```
-Currently aged 58 years.
+Currently aged 72 years.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 99. `rule_v1.test.gs065.c3.subject.easy.1034`

- **Rule** (gs065, g_two_of_three): For knee osteoarthritis pain, prescribe naproxen. If at least two of the following apply, prescribe acetaminophen instead: the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the patient has ever had angioedema (current or past).
- **Condition**: angioedema | near-miss: subject | tier: easy
- **Claims**: s = "Prescribe naproxen." | s' = "Prescribe acetaminophen."

```
Female patient of 70 years.
Knee osteoarthritis with pain on walking.
Owns a bicycle.
Teeth in good repair.
Prefers morning appointments.
Free of facial or oropharyngeal edema.
Current calf swelling 3.4 cm compared with the other leg.
Cardiac stress test unremarkable last year.
```

**flip** (answer: s')
```
-Free of facial or oropharyngeal edema.
+Recurrent angioedema, under allergy follow-up.
```

**near** (answer: s)
```
-Free of facial or oropharyngeal edema.
+Her wife is being treated for angioedema.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```


## 100. `rule_v1.test.gs047.c1.time.easy.705`

- **Rule** (gs047, g_all_of): For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.
- **Condition**: serum potassium above 5.0 | near-miss: time | tier: easy
- **Claims**: s = "Prescribe aspirin plus ticagrelor." | s' = "Prescribe aspirin plus clopidogrel."

```
Man of 55 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Teeth in good repair.
Lives in a second-floor apartment.
Pulmonary embolism years ago, treated for six months.
Latest potassium result: 3.7 mmol/L.
Records from 2014 list serum potassium at 4.5 mmol/L.
Photographs local wildlife.
```

**flip** (answer: s')
```
-Latest potassium result: 3.7 mmol/L.
+Latest potassium result: 5.4 mmol/L.
```

**near** (answer: s)
```
-Records from 2014 list serum potassium at 4.5 mmol/L.
+Records from 2014 list serum potassium at 5.6 mmol/L.
```

**pres** (answer: s)
```
(re-rendered: 8 lines, same state)
```

