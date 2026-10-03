# H1 sheet author2 (75 groups)

Read `README.md` first.

## G01

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 1 point if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 1 point if the patient has had cancer at any time (active or in remission); 2 points if the patient has ever had heart failure (current or past). If the score is 3 or more, prescribe nitrofurantoin instead.

**A2-G01-C1**

Facts: patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]; patient: systolic blood pressure = 127 (current) [line: "Current systolic blood pressure 127 mmHg."]; cancer: not mentioned (counts as absent); heart failure: not mentioned (counts as absent)

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Woman of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Uses sunscreen in summer.
Had diabetes years ago that went into remission on a low-calorie diet.
Current systolic blood pressure 127 mmHg.
```

**A2-G01-C2**

Facts: patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]; patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]; patient: systolic blood pressure = 127 (current) [line: "Observations now: blood pressure 127/85 mmHg."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Female patient of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Had diabetes years ago that went into remission on a low-calorie diet.
Uses sunscreen in summer.
Has metastatic lung cancer, receiving palliative treatment.
Observations now: blood pressure 127/85 mmHg.
```

**A2-G01-C3**

Facts: patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]; patient: cancer denied by name (current) [line: "Free of cancer throughout life."]; patient: systolic blood pressure = 127 (current) [line: "Observations now: blood pressure 127/85 mmHg."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Female patient of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Had diabetes years ago that went into remission on a low-calorie diet.
Uses sunscreen in summer.
Free of cancer throughout life.
Observations now: blood pressure 127/85 mmHg.
```

**A2-G01-C4**

Facts: patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]; patient: systolic blood pressure = 127 (current) [line: "Observations now: blood pressure 127/85 mmHg."]; cancer: not mentioned (counts as absent); heart failure: not mentioned (counts as absent)

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Female patient of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Had diabetes years ago that went into remission on a low-calorie diet.
Uses sunscreen in summer.
Observations now: blood pressure 127/85 mmHg.
```


## G02

Rule: For an acute gout flare, prescribe colchicine. If the patient is currently taking warfarin, prescribe prednisone instead.

**A2-G02-C1**

Facts: warfarin: not named; a general line implies absence (counts as absent) [line: "Anticoagulant therapy: none at present."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Female patient of 69 years.
Acute gout flare of the right first metatarsophalangeal joint.
Prefers morning appointments.
Photographs local wildlife.
Enjoys board games.
During a checkup in 2009, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Has two cats.
Pupils equal and reactive to light.
Her friend has recovered from a dislocated finger.
In 2005, lipase was 30 U/L.
Knits as a hobby.
Sleeps seven hours a night.
Anticoagulant therapy: none at present.
Drives a car.
Lives in a second-floor apartment.
Plays the piano.
Owns a bicycle.
Uses sunscreen in summer.
Sees a dentist yearly.
Prefers to be addressed by first name.
Her wife wears contact lenses.
```

**A2-G02-C2**

Facts: warfarin: not named; a general line implies absence (counts as absent) [line: "Anticoagulant therapy: none at present."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Woman of 69 years.
Acute gout flare of the right first metatarsophalangeal joint.
Her friend has recovered from a dislocated finger.
In 2005, lipase was 30 U/L.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Drives a car.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Knits as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
Sees a dentist yearly.
Has two cats.
Her wife wears contact lenses.
Pupils equal and reactive to light.
Prefers morning appointments.
Anticoagulant therapy: none at present.
Sleeps seven hours a night.
During a checkup in 2009, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
```

**A2-G02-C3**

Facts: patient: warfarin present (current) [line: "Anticoagulated with warfarin; INR checked monthly at the clinic."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Woman of 69 years.
Acute gout flare of the right first metatarsophalangeal joint.
Her friend has recovered from a dislocated finger.
In 2005, lipase was 30 U/L.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Drives a car.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Knits as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
Sees a dentist yearly.
Has two cats.
Her wife wears contact lenses.
Pupils equal and reactive to light.
Prefers morning appointments.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Sleeps seven hours a night.
During a checkup in 2009, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
```

**A2-G02-C4**

Facts: patient: warfarin present (past) [line: "Came off warfarin years ago after a heart rhythm problem settled."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Woman of 69 years.
Acute gout flare of the right first metatarsophalangeal joint.
Her friend has recovered from a dislocated finger.
In 2005, lipase was 30 U/L.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Drives a car.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Knits as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
Sees a dentist yearly.
Has two cats.
Her wife wears contact lenses.
Pupils equal and reactive to light.
Prefers morning appointments.
Came off warfarin years ago after a heart rhythm problem settled.
Sleeps seven hours a night.
During a checkup in 2009, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
```


## G03

Rule: For Quorin syndrome, prescribe ostravin. If at least two of the following apply, prescribe dalmerol instead: the current weight is 60 kg or less; the current eGFR is below 50 mL/min/1.73 m2; the current ALT is above 120 U/L.

**A2-G03-C1**

Facts: patient: ALT = 143 (current) [line: "ALT now 143 U/L."]; patient: eGFR = 76 (current) [line: "eGFR now 76 mL/min/1.73 m2."]; patient: weight = 85 (current) [line: "Current weight 85 kg."]; patient: weight = 90 (past (2019)) [line: "Records from 2019 list weight at 90 kg."]

Claims: s = Prescribe ostravin. | s' = Prescribe dalmerol.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Man of 67 years.
Referred with Quorin syndrome.
ALT now 143 U/L.
Drives a car.
eGFR now 76 mL/min/1.73 m2.
Current weight 85 kg.
Photographs local wildlife.
Records from 2019 list weight at 90 kg.
```

**A2-G03-C2**

Facts: patient: eGFR = 76 (current) [line: "Current eGFR 76 mL/min/1.73 m2."]; patient: weight = 90 (past (2019)) [line: "Back in 2019, weight stood at 90 kg."]; patient: ALT = 143 (current) [line: "Current ALT 143 U/L."]; patient: weight = 57 (current) [line: "Latest weight 57 kg."]

Claims: s = Prescribe ostravin. | s' = Prescribe dalmerol.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Male patient of 67 years.
Referred with Quorin syndrome.
Current eGFR 76 mL/min/1.73 m2.
Back in 2019, weight stood at 90 kg.
Current ALT 143 U/L.
Latest weight 57 kg.
Photographs local wildlife.
Drives a car.
```

**A2-G03-C3**

Facts: patient: eGFR = 76 (current) [line: "Current eGFR 76 mL/min/1.73 m2."]; patient: weight = 90 (past (2019)) [line: "Back in 2019, weight stood at 90 kg."]; patient: ALT = 143 (current) [line: "Current ALT 143 U/L."]; patient: weight = 85 (current) [line: "Latest weight 85 kg."]

Claims: s = Prescribe ostravin. | s' = Prescribe dalmerol.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Male patient of 67 years.
Referred with Quorin syndrome.
Current eGFR 76 mL/min/1.73 m2.
Back in 2019, weight stood at 90 kg.
Current ALT 143 U/L.
Latest weight 85 kg.
Photographs local wildlife.
Drives a car.
```

**A2-G03-C4**

Facts: patient: eGFR = 76 (current) [line: "Current eGFR 76 mL/min/1.73 m2."]; patient: weight = 49 (past (2019)) [line: "Back in 2019, weight stood at 49 kg."]; patient: ALT = 143 (current) [line: "Current ALT 143 U/L."]; patient: weight = 85 (current) [line: "Latest weight 85 kg."]

Claims: s = Prescribe ostravin. | s' = Prescribe dalmerol.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Male patient of 67 years.
Referred with Quorin syndrome.
Current eGFR 76 mL/min/1.73 m2.
Back in 2019, weight stood at 49 kg.
Current ALT 143 U/L.
Latest weight 85 kg.
Photographs local wildlife.
Drives a car.
```


## G04

Rule: For an acute gout flare, prescribe colchicine. If the current eGFR is below 45 mL/min/1.73 m2, prescribe prednisone instead.

**A2-G04-C1**

Facts: patient: eGFR = 71 (current) [line: "eGFR now 71 mL/min/1.73 m2."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Female patient of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Photographs local wildlife.
Enjoys board games.
Prefers to be addressed by first name.
eGFR now 71 mL/min/1.73 m2.
```

**A2-G04-C2**

Facts: patient: eGFR = 71 (current) [line: "Current eGFR 71 mL/min/1.73 m2."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Enjoys board games.
Current eGFR 71 mL/min/1.73 m2.
Prefers to be addressed by first name.
Photographs local wildlife.
```

**A2-G04-C3**

Facts: patient: eGFR = 36 (current) [line: "eGFR now 36 mL/min/1.73 m2."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Female patient of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Photographs local wildlife.
Enjoys board games.
Prefers to be addressed by first name.
eGFR now 36 mL/min/1.73 m2.
```

**A2-G04-C4**

Facts: patient: eGFR = 47 (current) [line: "eGFR now 47 mL/min/1.73 m2."]

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Female patient of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Photographs local wildlife.
Enjoys board games.
Prefers to be addressed by first name.
eGFR now 47 mL/min/1.73 m2.
```


## G05

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the current systolic blood pressure is above 160 mmHg or the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.

**A2-G05-C1**

Facts: patient: systolic blood pressure = 160 (current) [line: "Observations now: blood pressure 160/103 mmHg."]; patient: serum creatinine = 1.5 (current) [line: "Latest creatinine result: 1.5 mg/dL."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Observations now: blood pressure 160/103 mmHg.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```

**A2-G05-C2**

Facts: patient: systolic blood pressure = 167 (current) [line: "Observations now: blood pressure 167/107 mmHg."]; patient: serum creatinine = 1.5 (current) [line: "Latest creatinine result: 1.5 mg/dL."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Observations now: blood pressure 167/107 mmHg.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```

**A2-G05-C3**

Facts: patient: serum creatinine = 1.5 (current) [line: "Latest creatinine result: 1.5 mg/dL."]; systolic blood pressure: not mentioned (unknown)

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```

**A2-G05-C4**

Facts: patient: systolic blood pressure = 142 (current) [line: "Current systolic blood pressure 142 mmHg."]; patient: serum creatinine = 1.5 (current) [line: "Current serum creatinine 1.5 mg/dL."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
```
Man of 65 years.
Hip osteoarthritis with pain on walking.
Current systolic blood pressure 142 mmHg.
Current serum creatinine 1.5 mg/dL.
Knits as a hobby.
Lives in a second-floor apartment.
```

**A2-G05-C5**

Facts: patient: systolic blood pressure = 142 (current) [line: "Observations now: blood pressure 142/93 mmHg."]; patient: serum creatinine = 1.5 (current) [line: "Latest creatinine result: 1.5 mg/dL."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Observations now: blood pressure 142/93 mmHg.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```


## G06

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

**A2-G06-C1**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]; patient: white cell count = 4.8 (current) [line: "Latest WBC is 4.8 x10^9/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 45 years.
Acute low back pain after lifting.
Drives a car.
Has two cats.
Weight steady over the past year.
Her sister has a lazy eye.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2017.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Photographs local wildlife.
An episode of angioedema years ago, with full recovery.
Her father lives with psoriasis.
Owns a bicycle.
Her friend has recovered from a dislocated finger.
Prefers to be addressed by first name.
Knits as a hobby.
Teeth in good repair.
Lives in a second-floor apartment.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Latest WBC is 4.8 x10^9/L.
```

**A2-G06-C2**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]; patient: white cell count = 12.0 (current) [line: "Latest WBC is 12.0 x10^9/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 45 years.
Acute low back pain after lifting.
Drives a car.
Has two cats.
Weight steady over the past year.
Her sister has a lazy eye.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2017.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Photographs local wildlife.
An episode of angioedema years ago, with full recovery.
Her father lives with psoriasis.
Owns a bicycle.
Her friend has recovered from a dislocated finger.
Prefers to be addressed by first name.
Knits as a hobby.
Teeth in good repair.
Lives in a second-floor apartment.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Latest WBC is 12.0 x10^9/L.
```

**A2-G06-C3**

Facts: patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]; cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: white cell count = 4.8 (current) [line: "Current white cell count 4.8 x10^9/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Woman of 45 years.
Acute low back pain after lifting.
Drives a car.
An episode of angioedema years ago, with full recovery.
Lives in a second-floor apartment.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Photographs local wildlife.
Weight steady over the past year.
Prefers morning appointments.
Teeth in good repair.
Paints watercolors as a hobby.
Owns a bicycle.
Her sister has a lazy eye.
Prefers to be addressed by first name.
Her friend has recovered from a dislocated finger.
Pupils equal and reactive to light.
Has two cats.
Her father lives with psoriasis.
Current white cell count 4.8 x10^9/L.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2017.
```

**A2-G06-C4**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]; patient: white cell count = 13.6 (current) [line: "Latest WBC is 13.6 x10^9/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 45 years.
Acute low back pain after lifting.
Drives a car.
Has two cats.
Weight steady over the past year.
Her sister has a lazy eye.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2017.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Photographs local wildlife.
An episode of angioedema years ago, with full recovery.
Her father lives with psoriasis.
Owns a bicycle.
Her friend has recovered from a dislocated finger.
Prefers to be addressed by first name.
Knits as a hobby.
Teeth in good repair.
Lives in a second-floor apartment.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Latest WBC is 13.6 x10^9/L.
```


## G07

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**A2-G07-C1**

Facts: patient: temperature = 37.4 (current) [line: "Current temperature 37.4 C."]; patient: temperature = 36.6 (past) [line: "Last month, temperature was 36.6 C; the newest measurement replaces it."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Male patient of 29 years.
Sore throat for two days.
Prefers to be addressed by first name.
Current temperature 37.4 C.
Owns a bicycle.
Last month, temperature was 36.6 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
```

**A2-G07-C2**

Facts: patient: temperature = 37.4 (current) [line: "Current temperature 37.4 C."]; patient: temperature = 39.2 (past) [line: "Last month, temperature was 39.2 C; the newest measurement replaces it."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Male patient of 29 years.
Sore throat for two days.
Prefers to be addressed by first name.
Current temperature 37.4 C.
Owns a bicycle.
Last month, temperature was 39.2 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
```

**A2-G07-C3**

Facts: patient: temperature = 39.1 (current) [line: "Current temperature 39.1 C."]; patient: temperature = 36.6 (past) [line: "Last month, temperature was 36.6 C; the newest measurement replaces it."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Male patient of 29 years.
Sore throat for two days.
Prefers to be addressed by first name.
Current temperature 39.1 C.
Owns a bicycle.
Last month, temperature was 36.6 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
```

**A2-G07-C4**

Facts: patient: temperature = 37.4 (current) [line: "Temperature now 37.4 C (tympanic)."]; patient: temperature = 36.6 (past) [line: "Last month, temperature was 36.6 C; the newest measurement replaces it."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Man of 29 years.
Sore throat for two days.
Temperature now 37.4 C (tympanic).
Owns a bicycle.
Last month, temperature was 36.6 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
Prefers to be addressed by first name.
```


## G08

Rule: For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.

**A2-G08-C1**

Facts: patient: warfarin denied by name (current) [line: "Has never been prescribed warfarin."]; colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Has never been prescribed warfarin.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```

**A2-G08-C2**

Facts: colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: calf swelling = 3.6 (current) [line: "Current calf swelling 3.6 cm compared with the other leg."]; warfarin: not named; a general line implies absence (counts as absent) [line: "Anticoagulant therapy: none at present."]

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Male patient of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Teeth in good repair.
Rectal exam unremarkable.
Current calf swelling 3.6 cm compared with the other leg.
Uses sunscreen in summer.
Anticoagulant therapy: none at present.
```

**A2-G08-C3**

Facts: warfarin: not named; a general line implies absence (counts as absent) [line: "Anticoagulant therapy: none at present."]; colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Anticoagulant therapy: none at present.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```

**A2-G08-C4**

Facts: patient: warfarin present (current) [line: "Anticoagulated with warfarin; INR checked monthly at the clinic."]; colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```

**A2-G08-C5**

Facts: warfarin: stated as unknown [line: "Warfarin: status unclear from the records at hand."]; colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "warfarin" does not hold for this patient. | s' = Under the rule, the condition "warfarin" holds for this patient.
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Warfarin: status unclear from the records at hand.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```


## G09

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**A2-G09-C1**

Facts: patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]; patient: white cell count = 10.8 (past) [line: "Earlier this week, white cell count was 10.8 x10^9/L; a newer reading supersedes it."]; patient: white cell count = 9.0 (current) [line: "Current white cell count 9.0 x10^9/L."]; patient: eGFR = 37 (current) [line: "eGFR now 37 mL/min/1.73 m2."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Man of 64 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Heart rate now 99/min on a pulse check.
Paints watercolors as a hobby.
Earlier this week, white cell count was 10.8 x10^9/L; a newer reading supersedes it.
Uses sunscreen in summer.
Owns a bicycle.
Prefers to be addressed by first name.
Current white cell count 9.0 x10^9/L.
eGFR now 37 mL/min/1.73 m2.
Face and neck without swelling on examination.
```

**A2-G09-C2**

Facts: patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]; patient: white cell count = 10.8 (past) [line: "Earlier this week, white cell count was 10.8 x10^9/L; a newer reading supersedes it."]; patient: white cell count = 13.8 (current) [line: "Current white cell count 13.8 x10^9/L."]; patient: eGFR = 37 (current) [line: "eGFR now 37 mL/min/1.73 m2."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Man of 64 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Heart rate now 99/min on a pulse check.
Paints watercolors as a hobby.
Earlier this week, white cell count was 10.8 x10^9/L; a newer reading supersedes it.
Uses sunscreen in summer.
Owns a bicycle.
Prefers to be addressed by first name.
Current white cell count 13.8 x10^9/L.
eGFR now 37 mL/min/1.73 m2.
Face and neck without swelling on examination.
```

**A2-G09-C3**

Facts: patient: heart rate = 99 (current) [line: "Current heart rate 99/min."]; patient: white cell count = 9.0 (current) [line: "Latest WBC is 9.0 x10^9/L."]; patient: eGFR = 37 (current) [line: "Current eGFR 37 mL/min/1.73 m2."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]; patient: white cell count = 10.8 (past) [line: "Earlier this week, white cell count was 10.8 x10^9/L; a newer reading supersedes it."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Male patient of 64 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current heart rate 99/min.
Owns a bicycle.
Latest WBC is 9.0 x10^9/L.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Current eGFR 37 mL/min/1.73 m2.
Paints watercolors as a hobby.
Face and neck without swelling on examination.
Earlier this week, white cell count was 10.8 x10^9/L; a newer reading supersedes it.
```

**A2-G09-C4**

Facts: patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]; patient: white cell count = 14.3 (past) [line: "Earlier this week, white cell count was 14.3 x10^9/L; a newer reading supersedes it."]; patient: white cell count = 9.0 (current) [line: "Current white cell count 9.0 x10^9/L."]; patient: eGFR = 37 (current) [line: "eGFR now 37 mL/min/1.73 m2."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Man of 64 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Heart rate now 99/min on a pulse check.
Paints watercolors as a hobby.
Earlier this week, white cell count was 14.3 x10^9/L; a newer reading supersedes it.
Uses sunscreen in summer.
Owns a bicycle.
Prefers to be addressed by first name.
Current white cell count 9.0 x10^9/L.
eGFR now 37 mL/min/1.73 m2.
Face and neck without swelling on examination.
```


## G10

Rule: Hematopoietic Cell Transplantation-specific Comorbidity Index (as used here, partial): 1 point for coronary artery disease at any time (current or past); 1 point for a stroke or TIA at any time (current or past); 2 points for a current peptic ulcer; 1 point for a current ALT above 40 U/L. Other items of the index are not part of this question.

**A2-G10-C1**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: stroke/TIA present (past (2007)) [line: "Recovered from a stroke in 2007."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: ALT = 12 (current) [line: "Current ALT 12 U/L."]

Claims: s = The stroke/TIA criterion contributes 0 points. | s' = The stroke/TIA criterion contributes 1 point.
```
Female patient of 45 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Appetite good; no indigestion.
Recovered from a stroke in 2007.
Cardiac stress test unremarkable last year.
Current ALT 12 U/L.
Enjoys board games.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Drives a car.
```

**A2-G10-C2**

Facts: stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]; peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: ALT = 12 (current) [line: "ALT now 12 U/L."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]

Claims: s = The stroke/TIA criterion contributes 0 points. | s' = The stroke/TIA criterion contributes 1 point.
```
Woman of 45 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Power and sensation normal in all limbs.
Enjoys board games.
Appetite good; no indigestion.
Lives in a second-floor apartment.
ALT now 12 U/L.
Drives a car.
Paints watercolors as a hobby.
Cardiac stress test unremarkable last year.
```

**A2-G10-C3**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: ALT = 12 (current) [line: "Current ALT 12 U/L."]

Claims: s = The stroke/TIA criterion contributes 0 points. | s' = The stroke/TIA criterion contributes 1 point.
```
Female patient of 45 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Appetite good; no indigestion.
Power and sensation normal in all limbs.
Cardiac stress test unremarkable last year.
Current ALT 12 U/L.
Enjoys board games.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Drives a car.
```

**A2-G10-C4**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: stroke/TIA denied by name (current) [line: "Has never had a stroke or TIA."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: ALT = 12 (current) [line: "Current ALT 12 U/L."]

Claims: s = The stroke/TIA criterion contributes 0 points. | s' = The stroke/TIA criterion contributes 1 point.
```
Female patient of 45 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Appetite good; no indigestion.
Has never had a stroke or TIA.
Cardiac stress test unremarkable last year.
Current ALT 12 U/L.
Enjoys board games.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Drives a car.
```


## G11

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**A2-G11-C1**

Facts: patient: respiratory rate = 22 (current) [line: "Current respiratory rate 22/min."]; patient: systolic blood pressure = 111 (current) [line: "Observations now: blood pressure 111/76 mmHg."]; altered mentation: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 1 point.
```
Male patient of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Paints watercolors as a hobby.
Current respiratory rate 22/min.
Observations now: blood pressure 111/76 mmHg.
```

**A2-G11-C2**

Facts: patient: respiratory rate = 16 (current) [line: "Observations now: respiratory rate 16/min."]; patient: systolic blood pressure = 111 (current) [line: "Current systolic blood pressure 111 mmHg."]; altered mentation: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 1 point.
```
Man of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 16/min.
Current systolic blood pressure 111 mmHg.
Paints watercolors as a hobby.
```

**A2-G11-C3**

Facts: patient: respiratory rate = 16 (current) [line: "Current respiratory rate 16/min."]; patient: systolic blood pressure = 111 (current) [line: "Observations now: blood pressure 111/76 mmHg."]; altered mentation: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 1 point.
```
Male patient of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Paints watercolors as a hobby.
Current respiratory rate 16/min.
Observations now: blood pressure 111/76 mmHg.
```

**A2-G11-C4**

Facts: patient: respiratory rate = 21 (current) [line: "Current respiratory rate 21/min."]; patient: systolic blood pressure = 111 (current) [line: "Observations now: blood pressure 111/76 mmHg."]; altered mentation: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 1 point.
```
Male patient of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Paints watercolors as a hobby.
Current respiratory rate 21/min.
Observations now: blood pressure 111/76 mmHg.
```


## G12

Rule: IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): 1 point each for a current white cell count below 4.0 x10^9/L; a current platelet count below 100 x10^9/L; a current temperature below 36.0 C; a current blood urea nitrogen of 20 mg/dL or more. Other criteria are not part of this question.

**A2-G12-C1**

Facts: patient: temperature = 37.1 (current) [line: "Temperature now 37.1 C (tympanic)."]; patient: white cell count = 5.4 (current) [line: "Latest WBC is 5.4 x10^9/L."]; patient: platelet count = 168 (current) [line: "Platelet count now 168 x10^9/L."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen now: 15 mg/dL."]; patient: blood urea nitrogen = 22 (past (2022)) [line: "Records from 2022 list blood urea nitrogen at 22 mg/dL."]

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 1 point.
```
Female patient of 70 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Temperature now 37.1 C (tympanic).
Latest WBC is 5.4 x10^9/L.
Platelet count now 168 x10^9/L.
Blood urea nitrogen now: 15 mg/dL.
Prefers to be addressed by first name.
Records from 2022 list blood urea nitrogen at 22 mg/dL.
```

**A2-G12-C2**

Facts: patient: platelet count = 168 (current) [line: "Current platelet count 168 x10^9/L."]; patient: temperature = 37.1 (current) [line: "Current temperature 37.1 C."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen 15 mg/dL on the current labs."]; patient: white cell count = 5.4 (current) [line: "Current white cell count 5.4 x10^9/L."]; patient: blood urea nitrogen = 13 (past (2022)) [line: "Back in 2022, blood urea nitrogen stood at 13 mg/dL."]

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 1 point.
```
Woman of 70 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Prefers to be addressed by first name.
Current platelet count 168 x10^9/L.
Current temperature 37.1 C.
Blood urea nitrogen 15 mg/dL on the current labs.
Current white cell count 5.4 x10^9/L.
Back in 2022, blood urea nitrogen stood at 13 mg/dL.
```

**A2-G12-C3**

Facts: patient: temperature = 37.1 (current) [line: "Temperature now 37.1 C (tympanic)."]; patient: white cell count = 5.4 (current) [line: "Latest WBC is 5.4 x10^9/L."]; patient: platelet count = 168 (current) [line: "Platelet count now 168 x10^9/L."]; patient: blood urea nitrogen = 31 (current) [line: "Blood urea nitrogen now: 31 mg/dL."]; patient: blood urea nitrogen = 13 (past (2022)) [line: "Records from 2022 list blood urea nitrogen at 13 mg/dL."]

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 1 point.
```
Female patient of 70 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Temperature now 37.1 C (tympanic).
Latest WBC is 5.4 x10^9/L.
Platelet count now 168 x10^9/L.
Blood urea nitrogen now: 31 mg/dL.
Prefers to be addressed by first name.
Records from 2022 list blood urea nitrogen at 13 mg/dL.
```

**A2-G12-C4**

Facts: patient: temperature = 37.1 (current) [line: "Temperature now 37.1 C (tympanic)."]; patient: white cell count = 5.4 (current) [line: "Latest WBC is 5.4 x10^9/L."]; patient: platelet count = 168 (current) [line: "Platelet count now 168 x10^9/L."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen now: 15 mg/dL."]; patient: blood urea nitrogen = 13 (past (2022)) [line: "Records from 2022 list blood urea nitrogen at 13 mg/dL."]

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 1 point.
```
Female patient of 70 years.
Community-acquired pneumonia on chest radiograph; admitted to the medical ward.
Temperature now 37.1 C (tympanic).
Latest WBC is 5.4 x10^9/L.
Platelet count now 168 x10^9/L.
Blood urea nitrogen now: 15 mg/dL.
Prefers to be addressed by first name.
Records from 2022 list blood urea nitrogen at 13 mg/dL.
```


## G13

Rule: For primary prevention, prescribe atorvastatin. If the patient has ever had heart failure (current or past) and the age of the patient is 75 years or more, prescribe ezetimibe instead.

**A2-G13-C1**

Facts: patient: heart failure present (past (2014)) [line: "Formerly had heart failure from stress cardiomyopathy; recovered fully in 2014 and off all heart medicines since."]; patient: age = 83 (current) [line: "Currently aged 83 years."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2014 and off all heart medicines since.
Sees a dentist yearly.
Currently aged 83 years.
```

**A2-G13-C2**

Facts: patient: age = 83 (current) [line: "Currently aged 83 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Sees a dentist yearly.
Currently aged 83 years.
```

**A2-G13-C3**

Facts: heart failure: stated as unknown [line: "Heart failure: status unclear from the records at hand."]; patient: age = 83 (current) [line: "Currently aged 83 years."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Heart failure: status unclear from the records at hand.
Sees a dentist yearly.
Currently aged 83 years.
```

**A2-G13-C4**

Facts: patient: heart failure denied by name (current) [line: "Has never had heart failure."]; patient: age = 83 (current) [line: "Currently aged 83 years."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Has never had heart failure.
Sees a dentist yearly.
Currently aged 83 years.
```

**A2-G13-C5**

Facts: patient: age = 83 (current) [line: "Current age 83 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
An adult man.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Current age 83 years.
Sees a dentist yearly.
```


## G14

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**A2-G14-C1**

Facts: patient: weight = 73 (current) [line: "Current weight 73 kg."]; patient: age = 60 (current) [line: "Currently aged 60 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Zinc of 85 mcg/dL in 2019.
Current weight 73 kg.
Owns a bicycle.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
Knits as a hobby.
In 2017, folate was 12 ng/mL.
Drives a car.
His uncle has a lazy eye.
Currently aged 60 years.
Teeth in good repair.
His uncle lives with psoriasis.
Prefers morning appointments.
His roommate sprained a thumb last month.
His sister burned a hand on a stove years ago.
During a checkup in 2007, total protein was 7.0 g/dL.
```

**A2-G14-C2**

Facts: patient: weight = 60 (current) [line: "Current weight 60 kg."]; patient: age = 60 (current) [line: "Currently aged 60 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Zinc of 85 mcg/dL in 2019.
Current weight 60 kg.
Owns a bicycle.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
Knits as a hobby.
In 2017, folate was 12 ng/mL.
Drives a car.
His uncle has a lazy eye.
Currently aged 60 years.
Teeth in good repair.
His uncle lives with psoriasis.
Prefers morning appointments.
His roommate sprained a thumb last month.
His sister burned a hand on a stove years ago.
During a checkup in 2007, total protein was 7.0 g/dL.
```

**A2-G14-C3**

Facts: patient: weight = 61 (current) [line: "Current weight 61 kg."]; patient: age = 60 (current) [line: "Currently aged 60 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Zinc of 85 mcg/dL in 2019.
Current weight 61 kg.
Owns a bicycle.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
Knits as a hobby.
In 2017, folate was 12 ng/mL.
Drives a car.
His uncle has a lazy eye.
Currently aged 60 years.
Teeth in good repair.
His uncle lives with psoriasis.
Prefers morning appointments.
His roommate sprained a thumb last month.
His sister burned a hand on a stove years ago.
During a checkup in 2007, total protein was 7.0 g/dL.
```

**A2-G14-C4**

Facts: patient: age = 60 (current) [line: "Current age 60 years."]; patient: weight = 73 (current) [line: "Latest weight 73 kg."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Lives in a second-floor apartment.
His roommate sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
His uncle lives with psoriasis.
Drives a car.
Owns a bicycle.
In 2017, folate was 12 ng/mL.
His uncle has a lazy eye.
Current age 60 years.
Zinc of 85 mcg/dL in 2019.
Prefers morning appointments.
Latest weight 73 kg.
His sister burned a hand on a stove years ago.
Paints watercolors as a hobby.
During a checkup in 2007, total protein was 7.0 g/dL.
Teeth in good repair.
Knits as a hobby.
```


## G15

Rule: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the current ALT is above 120 U/L, prescribe azithromycin instead.

**A2-G15-C1**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: ALT = 138 (current) [line: "ALT now 138 U/L."]

Claims: s = Prescribe amoxicillin. | s' = Prescribe azithromycin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Female patient of 36 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Owns a bicycle.
Varicose veins: none seen.
Her uncle has a lazy eye.
Plays the piano.
In 2023, lipase was 30 U/L.
Her uncle burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2024.
Her father wears contact lenses.
ALT now 138 U/L.
Photographs local wildlife.
Lives in a second-floor apartment.
Knits as a hobby.
In 2017, folate was 12 ng/mL.
Teeth in good repair.
Enjoys board games.
Her uncle sprained a thumb last month.
Has two cats.
```

**A2-G15-C2**

Facts: patient: ALT = 138 (current) [line: "Current ALT 138 U/L."]; uncle: venous thromboembolism present (current) [line: "Her uncle is on anticoagulation for venous thrombosis."]

Claims: s = Prescribe amoxicillin. | s' = Prescribe azithromycin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Woman of 36 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Lives in a second-floor apartment.
Her uncle burned a hand on a stove years ago.
Enjoys board games.
Current ALT 138 U/L.
Owns a bicycle.
In 2023, lipase was 30 U/L.
Her uncle is on anticoagulation for venous thrombosis.
In 2017, folate was 12 ng/mL.
Photographs local wildlife.
Her father wears contact lenses.
Plays the piano.
Teeth in good repair.
Her uncle sprained a thumb last month.
Her uncle has a lazy eye.
Knits as a hobby.
Zinc of 85 mcg/dL in 2024.
Has two cats.
```

**A2-G15-C3**

Facts: patient: ALT = 138 (current) [line: "Current ALT 138 U/L."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]

Claims: s = Prescribe amoxicillin. | s' = Prescribe azithromycin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Woman of 36 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Lives in a second-floor apartment.
Her uncle burned a hand on a stove years ago.
Enjoys board games.
Current ALT 138 U/L.
Owns a bicycle.
In 2023, lipase was 30 U/L.
Varicose veins: none seen.
In 2017, folate was 12 ng/mL.
Photographs local wildlife.
Her father wears contact lenses.
Plays the piano.
Teeth in good repair.
Her uncle sprained a thumb last month.
Her uncle has a lazy eye.
Knits as a hobby.
Zinc of 85 mcg/dL in 2024.
Has two cats.
```

**A2-G15-C4**

Facts: patient: ALT = 138 (current) [line: "Current ALT 138 U/L."]; patient: venous thromboembolism present (current) [line: "Ongoing treatment for a deep vein thrombosis of the left arm."]

Claims: s = Prescribe amoxicillin. | s' = Prescribe azithromycin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Woman of 36 years.
Presents with acute streptococcal pharyngitis (rapid antigen test positive).
Lives in a second-floor apartment.
Her uncle burned a hand on a stove years ago.
Enjoys board games.
Current ALT 138 U/L.
Owns a bicycle.
In 2023, lipase was 30 U/L.
Ongoing treatment for a deep vein thrombosis of the left arm.
In 2017, folate was 12 ng/mL.
Photographs local wildlife.
Her father wears contact lenses.
Plays the piano.
Teeth in good repair.
Her uncle sprained a thumb last month.
Her uncle has a lazy eye.
Knits as a hobby.
Zinc of 85 mcg/dL in 2024.
Has two cats.
```


## G16

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the current blood urea nitrogen is above 19 mg/dL; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient has an active peptic ulcer.

**A2-G16-C1**

Facts: patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]; patient: blood urea nitrogen = 19 (current) [line: "Blood urea nitrogen 19 mg/dL on the current labs."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Blood urea nitrogen 19 mg/dL on the current labs.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**A2-G16-C2**

Facts: patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; blood urea nitrogen: not mentioned (unknown)

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**A2-G16-C3**

Facts: patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]; patient: blood urea nitrogen = 9 (current) [line: "Blood urea nitrogen 9 mg/dL on the current labs."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Blood urea nitrogen 9 mg/dL on the current labs.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**A2-G16-C4**

Facts: patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]; patient: blood urea nitrogen = 28 (current) [line: "Blood urea nitrogen 28 mg/dL on the current labs."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Blood urea nitrogen 28 mg/dL on the current labs.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**A2-G16-C5**

Facts: diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]; patient: blood urea nitrogen = 9 (current) [line: "Blood urea nitrogen now: 9 mg/dL."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Female patient of 54 years.
Atrial fibrillation; anticoagulation indicated.
HbA1c 5.3% at a routine check.
Has an active duodenal ulcer.
Blood urea nitrogen now: 9 mg/dL.
Plays the piano.
```


## G17

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**A2-G17-C1**

Facts: patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]; patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
```
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Tender, swollen lymph nodes in the front of the neck.
An episode of angioedema years ago, with full recovery.
Enjoys board games.
```

**A2-G17-C2**

Facts: patient: tender cervical lymph nodes present (past) [line: "Tender anterior cervical lymph nodes with a throat infection years ago, which went down within two weeks."]; patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
```
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Tender anterior cervical lymph nodes with a throat infection years ago, which went down within two weeks.
An episode of angioedema years ago, with full recovery.
Enjoys board games.
```

**A2-G17-C3**

Facts: tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]; patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
```
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Front of the neck without tenderness or swelling.
An episode of angioedema years ago, with full recovery.
Enjoys board games.
```

**A2-G17-C4**

Facts: patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]; tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
```
Female patient of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Enjoys board games.
An episode of angioedema years ago, with full recovery.
Front of the neck without tenderness or swelling.
```


## G18

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**A2-G18-C1**

Facts: patient: calf swelling = 0.4 (current) [line: "Current calf swelling 0.4 cm compared with the other leg."]; patient: age = 54 (current) [line: "Current age 54 years."]; father: colorectal cancer present (current) [line: "His father is undergoing surgery for bowel cancer."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Photographs local wildlife.
Pupils equal and reactive to light.
Owns a bicycle.
Teeth in good repair.
Sleeps seven hours a night.
His sister sprained a thumb last month.
Uses sunscreen in summer.
His father burned a hand on a stove years ago.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2016.
His roommate has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Current calf swelling 0.4 cm compared with the other leg.
Current age 54 years.
Drives a car.
Has two cats.
His father is undergoing surgery for bowel cancer.
```

**A2-G18-C2**

Facts: father: colorectal cancer present (current) [line: "His father is undergoing surgery for bowel cancer."]; patient: age = 54 (current) [line: "Currently aged 54 years."]; patient: calf swelling = 3.0 (current) [line: "Difference in calf circumference now 3.0 cm."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
His father is undergoing surgery for bowel cancer.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Photographs local wildlife.
Sleeps seven hours a night.
His sister sprained a thumb last month.
Zinc of 85 mcg/dL in 2016.
During a checkup in 2005, total protein was 7.0 g/dL.
His father burned a hand on a stove years ago.
Currently aged 54 years.
Drives a car.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Owns a bicycle.
Teeth in good repair.
Difference in calf circumference now 3.0 cm.
His roommate has a lazy eye.
```

**A2-G18-C3**

Facts: father: colorectal cancer present (current) [line: "His father is undergoing surgery for bowel cancer."]; patient: age = 54 (current) [line: "Currently aged 54 years."]; patient: calf swelling = 0.4 (current) [line: "Difference in calf circumference now 0.4 cm."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
His father is undergoing surgery for bowel cancer.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Photographs local wildlife.
Sleeps seven hours a night.
His sister sprained a thumb last month.
Zinc of 85 mcg/dL in 2016.
During a checkup in 2005, total protein was 7.0 g/dL.
His father burned a hand on a stove years ago.
Currently aged 54 years.
Drives a car.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Owns a bicycle.
Teeth in good repair.
Difference in calf circumference now 0.4 cm.
His roommate has a lazy eye.
```

**A2-G18-C4**

Facts: father: colorectal cancer present (current) [line: "His father is undergoing surgery for bowel cancer."]; patient: age = 54 (current) [line: "Currently aged 54 years."]; patient: calf swelling = 2.7 (current) [line: "Difference in calf circumference now 2.7 cm."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
His father is undergoing surgery for bowel cancer.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Photographs local wildlife.
Sleeps seven hours a night.
His sister sprained a thumb last month.
Zinc of 85 mcg/dL in 2016.
During a checkup in 2005, total protein was 7.0 g/dL.
His father burned a hand on a stove years ago.
Currently aged 54 years.
Drives a car.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
During a checkup in 2007, free T3 was 3.2 pg/mL.
Owns a bicycle.
Teeth in good repair.
Difference in calf circumference now 2.7 cm.
His roommate has a lazy eye.
```


## G19

Rule: Hematopoietic Cell Transplantation-specific Comorbidity Index (as used here, partial): 1 point for coronary artery disease at any time (current or past); 1 point for a stroke or TIA at any time (current or past); 2 points for a current peptic ulcer; 1 point for a current ALT above 40 U/L. Other items of the index are not part of this question.

**A2-G19-C1**

Facts: stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]; peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: ALT = 13 (current) [line: "ALT now 13 U/L."]

Claims: s = The active peptic ulcer criterion contributes 0 points. | s' = The active peptic ulcer criterion contributes 2 points.
```
Female patient of 40 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Power and sensation normal in all limbs.
Knits as a hobby.
Has two cats.
Photographs local wildlife.
Chest pain on exertion: none reported.
Appetite good; no indigestion.
ALT now 13 U/L.
Prefers morning appointments.
```

**A2-G19-C2**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]; patient: ALT = 13 (current) [line: "Current ALT 13 U/L."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]

Claims: s = The active peptic ulcer criterion contributes 0 points. | s' = The active peptic ulcer criterion contributes 2 points.
```
Woman of 40 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Has two cats.
Prefers morning appointments.
Photographs local wildlife.
Appetite good; no indigestion.
Power and sensation normal in all limbs.
Knits as a hobby.
Current ALT 13 U/L.
Chest pain on exertion: none reported.
```

**A2-G19-C3**

Facts: wife: peptic ulcer present (current) [line: "Her wife has peptic ulcer disease."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]; patient: ALT = 13 (current) [line: "Current ALT 13 U/L."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]

Claims: s = The active peptic ulcer criterion contributes 0 points. | s' = The active peptic ulcer criterion contributes 2 points.
```
Woman of 40 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Has two cats.
Prefers morning appointments.
Photographs local wildlife.
Her wife has peptic ulcer disease.
Power and sensation normal in all limbs.
Knits as a hobby.
Current ALT 13 U/L.
Chest pain on exertion: none reported.
```

**A2-G19-C4**

Facts: patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]; patient: ALT = 13 (current) [line: "Current ALT 13 U/L."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]

Claims: s = The active peptic ulcer criterion contributes 0 points. | s' = The active peptic ulcer criterion contributes 2 points.
```
Woman of 40 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Has two cats.
Prefers morning appointments.
Photographs local wildlife.
Active peptic ulcer disease.
Power and sensation normal in all limbs.
Knits as a hobby.
Current ALT 13 U/L.
Chest pain on exertion: none reported.
```


## G20

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has active cancer; the age of the patient is 65 years or more; the current ALT is above 120 U/L.

**A2-G20-C1**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 70 (current) [line: "Currently aged 70 years."]; patient: ALT = 24 (current) [line: "Current ALT 24 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
```
Man, adult.
Spreading redness and warmth of the right shin for two days.
Has melanoma skin cancer and is receiving treatment for it.
Sleeps seven hours a night.
In 2017, folate was 12 ng/mL.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2022.
Has two cats.
Teeth in good repair.
His wife wears contact lenses.
Prefers to be addressed by first name.
Knits as a hobby.
Enjoys board games.
His roommate has a lazy eye.
Paints watercolors as a hobby.
His wife lives with psoriasis.
Currently aged 70 years.
Plays the piano.
Owns a bicycle.
Current ALT 24 U/L.
Sees a dentist yearly.
Photographs local wildlife.
```

**A2-G20-C2**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 49 (current) [line: "Currently aged 49 years."]; patient: ALT = 24 (current) [line: "Current ALT 24 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
```
Man, adult.
Spreading redness and warmth of the right shin for two days.
Has melanoma skin cancer and is receiving treatment for it.
Sleeps seven hours a night.
In 2017, folate was 12 ng/mL.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2022.
Has two cats.
Teeth in good repair.
His wife wears contact lenses.
Prefers to be addressed by first name.
Knits as a hobby.
Enjoys board games.
His roommate has a lazy eye.
Paints watercolors as a hobby.
His wife lives with psoriasis.
Currently aged 49 years.
Plays the piano.
Owns a bicycle.
Current ALT 24 U/L.
Sees a dentist yearly.
Photographs local wildlife.
```

**A2-G20-C3**

Facts: patient: age = 49 (current) [line: "Current age 49 years."]; patient: ALT = 24 (current) [line: "ALT now 24 U/L."]; patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
```
An adult man.
Spreading redness and warmth of the right shin for two days.
His wife wears contact lenses.
Knits as a hobby.
Prefers to be addressed by first name.
Sees a dentist yearly.
Pupils equal and reactive to light.
Photographs local wildlife.
Current age 49 years.
Zinc of 85 mcg/dL in 2022.
Has two cats.
In 2017, folate was 12 ng/mL.
ALT now 24 U/L.
Paints watercolors as a hobby.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
Has melanoma skin cancer and is receiving treatment for it.
His wife lives with psoriasis.
His roommate has a lazy eye.
Sleeps seven hours a night.
Enjoys board games.
```

**A2-G20-C4**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 64 (current) [line: "Currently aged 64 years."]; patient: ALT = 24 (current) [line: "Current ALT 24 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
```
Man, adult.
Spreading redness and warmth of the right shin for two days.
Has melanoma skin cancer and is receiving treatment for it.
Sleeps seven hours a night.
In 2017, folate was 12 ng/mL.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2022.
Has two cats.
Teeth in good repair.
His wife wears contact lenses.
Prefers to be addressed by first name.
Knits as a hobby.
Enjoys board games.
His roommate has a lazy eye.
Paints watercolors as a hobby.
His wife lives with psoriasis.
Currently aged 64 years.
Plays the piano.
Owns a bicycle.
Current ALT 24 U/L.
Sees a dentist yearly.
Photographs local wildlife.
```


## G21

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.

**A2-G21-C1**

Facts: sister: coronary artery disease present (current) [line: "Her sister has known coronary artery disease."]; patient: weight = 92 (current) [line: "Current weight 92 kg."]; penicillin allergy: not mentioned (counts as absent)

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 80 years.
Spreading redness and warmth of the right shin for two days.
Teeth in good repair.
Prefers to be addressed by first name.
Her sister has known coronary artery disease.
Current weight 92 kg.
```

**A2-G21-C2**

Facts: sister: coronary artery disease present (current) [line: "Her sister has known coronary artery disease."]; patient: weight = 92 (current) [line: "Latest weight 92 kg."]; penicillin allergy: not mentioned (counts as absent)

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman of 80 years.
Spreading redness and warmth of the right shin for two days.
Prefers to be addressed by first name.
Teeth in good repair.
Her sister has known coronary artery disease.
Latest weight 92 kg.
```

**A2-G21-C3**

Facts: sister: coronary artery disease present (current) [line: "Her sister has known coronary artery disease."]; patient: weight = 60 (current) [line: "Current weight 60 kg."]; penicillin allergy: not mentioned (counts as absent)

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 80 years.
Spreading redness and warmth of the right shin for two days.
Teeth in good repair.
Prefers to be addressed by first name.
Her sister has known coronary artery disease.
Current weight 60 kg.
```

**A2-G21-C4**

Facts: sister: coronary artery disease present (current) [line: "Her sister has known coronary artery disease."]; patient: weight = 61 (current) [line: "Current weight 61 kg."]; penicillin allergy: not mentioned (counts as absent)

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 80 years.
Spreading redness and warmth of the right shin for two days.
Teeth in good repair.
Prefers to be addressed by first name.
Her sister has known coronary artery disease.
Current weight 61 kg.
```


## G22

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 2 points if the patient currently has tonsillar exudate; 3 points if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past). If the score is 8 or more, prescribe nitrofurantoin instead.

**A2-G22-C1**

Facts: patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Female patient of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Prefers to be addressed by first name.
Tonsillar exudate visible on both sides.
Difference in calf circumference now 3.6 cm.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
```

**A2-G22-C2**

Facts: patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Female patient of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Prefers to be addressed by first name.
Tonsillar exudate visible on both sides.
Lives with peripheral artery disease affecting the left leg.
Difference in calf circumference now 3.6 cm.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
```

**A2-G22-C3**

Facts: patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; roommate: myocardial infarction or peripheral artery disease present (current) [line: "Her roommate has peripheral artery disease with leg pain."]; patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Female patient of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Prefers to be addressed by first name.
Tonsillar exudate visible on both sides.
Her roommate has peripheral artery disease with leg pain.
Difference in calf circumference now 3.6 cm.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
```

**A2-G22-C4**

Facts: patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; patient: calf swelling = 3.6 (current) [line: "Current calf swelling 3.6 cm compared with the other leg."]; myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Woman of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Duodenal ulcer years ago; recovered fully with treatment.
Tonsillar exudate visible on both sides.
Plays the piano.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Current calf swelling 3.6 cm compared with the other leg.
```


## G23

Rule: For a chest infection during chemotherapy, prescribe oral co-amoxiclav. If the current neutrophil count is 1.0 x10^9/L or less, prescribe intravenous piperacillin-tazobactam instead.

**A2-G23-C1**

Facts: patient: neutrophil count = 0.5 (past (2015)) [line: "Back in 2015, neutrophil count stood at 0.5 x10^9/L."]; patient: neutrophil count = 2.3 (current) [line: "Current neutrophil count 2.3 x10^9/L."]

Claims: s = Prescribe oral co-amoxiclav. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "neutrophil count at or below 1.0" does not hold for this patient. | s' = Under the rule, the condition "neutrophil count at or below 1.0" holds for this patient.
```
Man of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Back in 2015, neutrophil count stood at 0.5 x10^9/L.
Paints watercolors as a hobby.
Current neutrophil count 2.3 x10^9/L.
```

**A2-G23-C2**

Facts: patient: neutrophil count = 4.7 (past (2015)) [line: "Back in 2015, neutrophil count stood at 4.7 x10^9/L."]; patient: neutrophil count = 2.3 (current) [line: "Current neutrophil count 2.3 x10^9/L."]

Claims: s = Prescribe oral co-amoxiclav. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "neutrophil count at or below 1.0" does not hold for this patient. | s' = Under the rule, the condition "neutrophil count at or below 1.0" holds for this patient.
```
Man of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Back in 2015, neutrophil count stood at 4.7 x10^9/L.
Paints watercolors as a hobby.
Current neutrophil count 2.3 x10^9/L.
```

**A2-G23-C3**

Facts: patient: neutrophil count = 4.7 (past (2015)) [line: "Back in 2015, neutrophil count stood at 4.7 x10^9/L."]; patient: neutrophil count = 0.8 (current) [line: "Current neutrophil count 0.8 x10^9/L."]

Claims: s = Prescribe oral co-amoxiclav. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "neutrophil count at or below 1.0" does not hold for this patient. | s' = Under the rule, the condition "neutrophil count at or below 1.0" holds for this patient.
```
Man of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Back in 2015, neutrophil count stood at 4.7 x10^9/L.
Paints watercolors as a hobby.
Current neutrophil count 0.8 x10^9/L.
```

**A2-G23-C4**

Facts: patient: neutrophil count = 2.3 (current) [line: "Latest neutrophil count: 2.3 x10^9/L."]; patient: neutrophil count = 4.7 (past (2015)) [line: "Records from 2015 list neutrophil count at 4.7 x10^9/L."]

Claims: s = Prescribe oral co-amoxiclav. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "neutrophil count at or below 1.0" does not hold for this patient. | s' = Under the rule, the condition "neutrophil count at or below 1.0" holds for this patient.
```
Male patient of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Latest neutrophil count: 2.3 x10^9/L.
Records from 2015 list neutrophil count at 4.7 x10^9/L.
Paints watercolors as a hobby.
```


## G24

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**A2-G24-C1**

Facts: angioedema: not named; a general line implies absence (counts as absent) [line: "Free of facial or oropharyngeal edema."]; patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her sister lives with psoriasis.
Owns a bicycle.
Drives a car.
Her wife burned a hand on a stove years ago.
Her friend has a lazy eye.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2022.
During a checkup in 2021, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Her uncle has recovered from a dislocated finger.
Pupils equal and reactive to light.
Free of facial or oropharyngeal edema.
Knits as a hobby.
Prefers morning appointments.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
```

**A2-G24-C2**

Facts: angioedema: stated as unknown [line: "Angioedema: unknown."]; patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her sister lives with psoriasis.
Owns a bicycle.
Drives a car.
Her wife burned a hand on a stove years ago.
Her friend has a lazy eye.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2022.
During a checkup in 2021, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Her uncle has recovered from a dislocated finger.
Pupils equal and reactive to light.
Angioedema: unknown.
Knits as a hobby.
Prefers morning appointments.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
```

**A2-G24-C3**

Facts: patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]; patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her sister lives with psoriasis.
Owns a bicycle.
Drives a car.
Her wife burned a hand on a stove years ago.
Her friend has a lazy eye.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2022.
During a checkup in 2021, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Her uncle has recovered from a dislocated finger.
Pupils equal and reactive to light.
Recurrent angioedema, under allergy follow-up.
Knits as a hobby.
Prefers morning appointments.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
```

**A2-G24-C4**

Facts: wife: angioedema present (current) [line: "Her wife is being treated for angioedema."]; patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her sister lives with psoriasis.
Owns a bicycle.
Drives a car.
Her wife burned a hand on a stove years ago.
Her friend has a lazy eye.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2022.
During a checkup in 2021, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Her uncle has recovered from a dislocated finger.
Pupils equal and reactive to light.
Her wife is being treated for angioedema.
Knits as a hobby.
Prefers morning appointments.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
```

**A2-G24-C5**

Facts: angioedema: not named; a general line implies absence (counts as absent) [line: "Free of facial or oropharyngeal edema."]; patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
```
Female patient of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her uncle has recovered from a dislocated finger.
Knits as a hobby.
Her friend has a lazy eye.
Free of facial or oropharyngeal edema.
Her wife burned a hand on a stove years ago.
Paints watercolors as a hobby.
Tender, swollen lymph nodes in the front of the neck.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2022.
Enjoys board games.
Drives a car.
Owns a bicycle.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Photographs local wildlife.
Her sister lives with psoriasis.
During a checkup in 2016, free T3 was 3.2 pg/mL.
During a checkup in 2021, total protein was 7.0 g/dL.
```


## G25

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current blood urea nitrogen is above 19 mg/dL.

**A2-G25-C1**

Facts: colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Hemoglobin within the normal range on recent blood tests."]; father: diabetes present (current) [line: "Her father is diabetic."]; blood urea nitrogen: not mentioned (unknown)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Female patient of 31 years.
Requests contraception.
Hemoglobin within the normal range on recent blood tests.
In 2023, lipase was 30 U/L.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Teeth in good repair.
Prefers morning appointments.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
Enjoys board games.
Her roommate burned a hand on a stove years ago.
Her uncle lives with psoriasis.
Owns a bicycle.
Plays the piano.
Her father is diabetic.
Free T4 of 1.2 ng/dL in 2024.
```

**A2-G25-C2**

Facts: colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Hemoglobin within the normal range on recent blood tests."]; father: diabetes present (current) [line: "Her father is diabetic."]; patient: blood urea nitrogen = 11 (current) [line: "Blood urea nitrogen now: 11 mg/dL."]

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Woman of 31 years.
Requests contraception.
Lives in a second-floor apartment.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2024.
Enjoys board games.
Her uncle lives with psoriasis.
Has two cats.
Hemoglobin within the normal range on recent blood tests.
Sees a dentist yearly.
Drives a car.
Owns a bicycle.
Pupils equal and reactive to light.
Her father is diabetic.
Teeth in good repair.
Blood urea nitrogen now: 11 mg/dL.
In 2023, lipase was 30 U/L.
Knits as a hobby.
Prefers to be addressed by first name.
Her roommate burned a hand on a stove years ago.
Plays the piano.
```

**A2-G25-C3**

Facts: colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Hemoglobin within the normal range on recent blood tests."]; patient: blood urea nitrogen = 25 (current) [line: "Blood urea nitrogen 25 mg/dL on the current labs."]; father: diabetes present (current) [line: "Her father is diabetic."]

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Female patient of 31 years.
Requests contraception.
Hemoglobin within the normal range on recent blood tests.
In 2023, lipase was 30 U/L.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Teeth in good repair.
Prefers morning appointments.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
Blood urea nitrogen 25 mg/dL on the current labs.
Enjoys board games.
Her roommate burned a hand on a stove years ago.
Her uncle lives with psoriasis.
Owns a bicycle.
Plays the piano.
Her father is diabetic.
Free T4 of 1.2 ng/dL in 2024.
```

**A2-G25-C4**

Facts: colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Hemoglobin within the normal range on recent blood tests."]; patient: blood urea nitrogen = 11 (current) [line: "Blood urea nitrogen 11 mg/dL on the current labs."]; father: diabetes present (current) [line: "Her father is diabetic."]

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Female patient of 31 years.
Requests contraception.
Hemoglobin within the normal range on recent blood tests.
In 2023, lipase was 30 U/L.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Teeth in good repair.
Prefers morning appointments.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
Blood urea nitrogen 11 mg/dL on the current labs.
Enjoys board games.
Her roommate burned a hand on a stove years ago.
Her uncle lives with psoriasis.
Owns a bicycle.
Plays the piano.
Her father is diabetic.
Free T4 of 1.2 ng/dL in 2024.
```

**A2-G25-C5**

Facts: colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Hemoglobin within the normal range on recent blood tests."]; patient: blood urea nitrogen = 19 (current) [line: "Blood urea nitrogen 19 mg/dL on the current labs."]; father: diabetes present (current) [line: "Her father is diabetic."]

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Female patient of 31 years.
Requests contraception.
Hemoglobin within the normal range on recent blood tests.
In 2023, lipase was 30 U/L.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Teeth in good repair.
Prefers morning appointments.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
Blood urea nitrogen 19 mg/dL on the current labs.
Enjoys board games.
Her roommate burned a hand on a stove years ago.
Her uncle lives with psoriasis.
Owns a bicycle.
Plays the piano.
Her father is diabetic.
Free T4 of 1.2 ng/dL in 2024.
```


## G26

Rule: For rhythm control of paroxysmal atrial fibrillation, prescribe dronedarone. If the patient has ever had heart failure (current or past), prescribe amiodarone instead.

**A2-G26-C1**

Facts: patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]

Claims: s = Prescribe dronedarone. | s' = Prescribe amiodarone.

Criterion claims: s = Under the rule, the condition "heart failure at any time" does not hold for this patient. | s' = Under the rule, the condition "heart failure at any time" holds for this patient.
```
Male patient of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Current heart failure with ankle swelling.
Plays the piano.
```

**A2-G26-C2**

Facts: heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

Claims: s = Prescribe dronedarone. | s' = Prescribe amiodarone.

Criterion claims: s = Under the rule, the condition "heart failure at any time" does not hold for this patient. | s' = Under the rule, the condition "heart failure at any time" holds for this patient.
```
Male patient of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Heart sounds without a gallop.
Plays the piano.
```

**A2-G26-C3**

Facts: patient: heart failure denied by name (current) [line: "Has never had heart failure."]

Claims: s = Prescribe dronedarone. | s' = Prescribe amiodarone.

Criterion claims: s = Under the rule, the condition "heart failure at any time" does not hold for this patient. | s' = Under the rule, the condition "heart failure at any time" holds for this patient.
```
Male patient of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Has never had heart failure.
Plays the piano.
```

**A2-G26-C4**

Facts: heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

Claims: s = Prescribe dronedarone. | s' = Prescribe amiodarone.

Criterion claims: s = Under the rule, the condition "heart failure at any time" does not hold for this patient. | s' = Under the rule, the condition "heart failure at any time" holds for this patient.
```
Man of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Plays the piano.
Heart sounds without a gallop.
```


## G27

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

**A2-G27-C1**

Facts: patient: serum creatinine = 1.7 (current) [line: "Current serum creatinine 1.7 mg/dL."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "diabetes" does not hold for this patient. | s' = Under the rule, the condition "diabetes" holds for this patient.
```
Male patient of 81 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Plays the piano.
Prefers morning appointments.
Has two cats.
His roommate burned a hand on a stove years ago.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
In 2009, folate was 12 ng/mL.
Drives a car.
Uses sunscreen in summer.
Sees a dentist yearly.
During a checkup in 2019, total protein was 7.0 g/dL.
In 2017, lipase was 30 U/L.
Teeth in good repair.
Knits as a hobby.
Current serum creatinine 1.7 mg/dL.
Zinc of 85 mcg/dL in 2010.
HbA1c 5.3% at a routine check.
Pupils equal and reactive to light.
Photographs local wildlife.
```

**A2-G27-C2**

Facts: patient: serum creatinine = 1.7 (current) [line: "Current serum creatinine 1.7 mg/dL."]; patient: diabetes denied by name (current) [line: "Never diagnosed with diabetes."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "diabetes" does not hold for this patient. | s' = Under the rule, the condition "diabetes" holds for this patient.
```
Male patient of 81 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Plays the piano.
Prefers morning appointments.
Has two cats.
His roommate burned a hand on a stove years ago.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
In 2009, folate was 12 ng/mL.
Drives a car.
Uses sunscreen in summer.
Sees a dentist yearly.
During a checkup in 2019, total protein was 7.0 g/dL.
In 2017, lipase was 30 U/L.
Teeth in good repair.
Knits as a hobby.
Current serum creatinine 1.7 mg/dL.
Zinc of 85 mcg/dL in 2010.
Never diagnosed with diabetes.
Pupils equal and reactive to light.
Photographs local wildlife.
```

**A2-G27-C3**

Facts: diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; patient: serum creatinine = 1.7 (current) [line: "Latest creatinine result: 1.7 mg/dL."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "diabetes" does not hold for this patient. | s' = Under the rule, the condition "diabetes" holds for this patient.
```
Man of 81 years.
Hip osteoarthritis with pain on walking.
His wife sprained a thumb last month.
Prefers morning appointments.
Enjoys board games.
Plays the piano.
Teeth in good repair.
His roommate burned a hand on a stove years ago.
In 2009, folate was 12 ng/mL.
Uses sunscreen in summer.
Pupils equal and reactive to light.
HbA1c 5.3% at a routine check.
Sees a dentist yearly.
Prefers to be addressed by first name.
In 2017, lipase was 30 U/L.
Has two cats.
Knits as a hobby.
Drives a car.
Zinc of 85 mcg/dL in 2010.
During a checkup in 2019, total protein was 7.0 g/dL.
Photographs local wildlife.
Latest creatinine result: 1.7 mg/dL.
```

**A2-G27-C4**

Facts: patient: serum creatinine = 1.7 (current) [line: "Current serum creatinine 1.7 mg/dL."]; patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "diabetes" does not hold for this patient. | s' = Under the rule, the condition "diabetes" holds for this patient.
```
Male patient of 81 years.
Hip osteoarthritis with pain on walking.
Enjoys board games.
Plays the piano.
Prefers morning appointments.
Has two cats.
His roommate burned a hand on a stove years ago.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
In 2009, folate was 12 ng/mL.
Drives a car.
Uses sunscreen in summer.
Sees a dentist yearly.
During a checkup in 2019, total protein was 7.0 g/dL.
In 2017, lipase was 30 U/L.
Teeth in good repair.
Knits as a hobby.
Current serum creatinine 1.7 mg/dL.
Zinc of 85 mcg/dL in 2010.
Had diabetes years ago that went into remission on a low-calorie diet.
Pupils equal and reactive to light.
Photographs local wildlife.
```


## G28

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. Score 2 points for a major bleeding event at any time; 1 point for age 75 years or more; 1 point for a current eGFR below 30 mL/min/1.73 m2. If the score is 2 or more, prescribe aspirin plus clopidogrel instead.

**A2-G28-C1**

Facts: patient: age = 79 (current) [line: "Current age 79 years."]; patient: eGFR = 83 (current) [line: "Current eGFR 83 mL/min/1.73 m2."]; bleeding history: not named; a general line implies absence (counts as absent) [line: "Bowel habit normal, without any blood in the stool."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Woman, adult.
Recovering on the ward after a myocardial infarction treated with a stent.
Sees a dentist yearly.
During a checkup in 2013, total protein was 7.0 g/dL.
Has two cats.
Enjoys board games.
Owns a bicycle.
Prefers morning appointments.
Knits as a hobby.
Uses sunscreen in summer.
Current age 79 years.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Current eGFR 83 mL/min/1.73 m2.
Teeth in good repair.
Her sister has a lazy eye.
Her friend burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2016.
Lives in a second-floor apartment.
Bowel habit normal, without any blood in the stool.
Plays the piano.
Drives a car.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**A2-G28-C2**

Facts: patient: age = 79 (current) [line: "Currently aged 79 years."]; patient: eGFR = 35 (current) [line: "eGFR now 35 mL/min/1.73 m2."]; bleeding history: not named; a general line implies absence (counts as absent) [line: "Bowel habit normal, without any blood in the stool."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
An adult woman.
Recovering on the ward after a myocardial infarction treated with a stent.
Enjoys board games.
Owns a bicycle.
Drives a car.
Her sister has a lazy eye.
Prefers morning appointments.
Currently aged 79 years.
Has two cats.
Zinc of 85 mcg/dL in 2016.
Her friend burned a hand on a stove years ago.
eGFR now 35 mL/min/1.73 m2.
Teeth in good repair.
Plays the piano.
Photographs local wildlife.
During a checkup in 2013, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Knits as a hobby.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Bowel habit normal, without any blood in the stool.
Sees a dentist yearly.
```

**A2-G28-C3**

Facts: patient: age = 79 (current) [line: "Currently aged 79 years."]; patient: eGFR = 26 (current) [line: "eGFR now 26 mL/min/1.73 m2."]; bleeding history: not named; a general line implies absence (counts as absent) [line: "Bowel habit normal, without any blood in the stool."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
An adult woman.
Recovering on the ward after a myocardial infarction treated with a stent.
Enjoys board games.
Owns a bicycle.
Drives a car.
Her sister has a lazy eye.
Prefers morning appointments.
Currently aged 79 years.
Has two cats.
Zinc of 85 mcg/dL in 2016.
Her friend burned a hand on a stove years ago.
eGFR now 26 mL/min/1.73 m2.
Teeth in good repair.
Plays the piano.
Photographs local wildlife.
During a checkup in 2013, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Knits as a hobby.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Bowel habit normal, without any blood in the stool.
Sees a dentist yearly.
```

**A2-G28-C4**

Facts: patient: age = 79 (current) [line: "Currently aged 79 years."]; patient: eGFR = 83 (current) [line: "eGFR now 83 mL/min/1.73 m2."]; bleeding history: not named; a general line implies absence (counts as absent) [line: "Bowel habit normal, without any blood in the stool."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
An adult woman.
Recovering on the ward after a myocardial infarction treated with a stent.
Enjoys board games.
Owns a bicycle.
Drives a car.
Her sister has a lazy eye.
Prefers morning appointments.
Currently aged 79 years.
Has two cats.
Zinc of 85 mcg/dL in 2016.
Her friend burned a hand on a stove years ago.
eGFR now 83 mL/min/1.73 m2.
Teeth in good repair.
Plays the piano.
Photographs local wildlife.
During a checkup in 2013, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Knits as a hobby.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Bowel habit normal, without any blood in the stool.
Sees a dentist yearly.
```


## G29

Rule: For Delmar fever, prescribe fenrastat. If the current serum potassium is above 4.8 mmol/L, prescribe kivolane instead.

**A2-G29-C1**

Facts: patient: serum potassium = 5.4 (current) [line: "Latest potassium result: 5.4 mmol/L."]

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
```
Man of 32 years.
Referred with Delmar fever.
His roommate has a lazy eye.
Plays the piano.
Knits as a hobby.
Sleeps seven hours a night.
Uses sunscreen in summer.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Latest potassium result: 5.4 mmol/L.
Prefers morning appointments.
Has two cats.
Sees a dentist yearly.
His sister has recovered from a dislocated finger.
Owns a bicycle.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2024.
Photographs local wildlife.
Drives a car.
His roommate lives with psoriasis.
Lives in a second-floor apartment.
During a checkup in 2016, total protein was 7.0 g/dL.
```

**A2-G29-C2**

Facts: patient: serum potassium = 4.4 (current) [line: "Current serum potassium 4.4 mmol/L."]

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
```
Male patient of 32 years.
Referred with Delmar fever.
Teeth in good repair.
Knits as a hobby.
His roommate has a lazy eye.
Prefers morning appointments.
Owns a bicycle.
Has two cats.
Pupils equal and reactive to light.
During a checkup in 2016, total protein was 7.0 g/dL.
Drives a car.
His wife sprained a thumb last month.
Photographs local wildlife.
Plays the piano.
His roommate lives with psoriasis.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Sees a dentist yearly.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Current serum potassium 4.4 mmol/L.
His sister has recovered from a dislocated finger.
Sleeps seven hours a night.
```

**A2-G29-C3**

Facts: patient: serum potassium = 4.7 (current) [line: "Latest potassium result: 4.7 mmol/L."]

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
```
Man of 32 years.
Referred with Delmar fever.
His roommate has a lazy eye.
Plays the piano.
Knits as a hobby.
Sleeps seven hours a night.
Uses sunscreen in summer.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Latest potassium result: 4.7 mmol/L.
Prefers morning appointments.
Has two cats.
Sees a dentist yearly.
His sister has recovered from a dislocated finger.
Owns a bicycle.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2024.
Photographs local wildlife.
Drives a car.
His roommate lives with psoriasis.
Lives in a second-floor apartment.
During a checkup in 2016, total protein was 7.0 g/dL.
```

**A2-G29-C4**

Facts: patient: serum potassium = 4.4 (current) [line: "Latest potassium result: 4.4 mmol/L."]

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
```
Man of 32 years.
Referred with Delmar fever.
His roommate has a lazy eye.
Plays the piano.
Knits as a hobby.
Sleeps seven hours a night.
Uses sunscreen in summer.
His wife sprained a thumb last month.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Latest potassium result: 4.4 mmol/L.
Prefers morning appointments.
Has two cats.
Sees a dentist yearly.
His sister has recovered from a dislocated finger.
Owns a bicycle.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2024.
Photographs local wildlife.
Drives a car.
His roommate lives with psoriasis.
Lives in a second-floor apartment.
During a checkup in 2016, total protein was 7.0 g/dL.
```


## G30

Rule: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the current temperature is above 38.0 C; the patient currently has tonsillar exudate; the patient currently has tender anterior cervical lymph nodes.

**A2-G30-C1**

Facts: patient: temperature = 37.3 (past (2013)) [line: "Back in 2013, temperature stood at 37.3 C."]; patient: temperature = 37.2 (current) [line: "Current temperature 37.2 C."]; patient: tender cervical lymph nodes present (current) [line: "Anterior cervical lymph nodes enlarged and tender to touch."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Male patient of 44 years.
Sore throat for two days.
Back in 2013, temperature stood at 37.3 C.
Current temperature 37.2 C.
Anterior cervical lymph nodes enlarged and tender to touch.
Teeth in good repair.
Drives a car.
```

**A2-G30-C2**

Facts: patient: temperature = 37.3 (past (2013)) [line: "Back in 2013, temperature stood at 37.3 C."]; patient: temperature = 38.8 (current) [line: "Current temperature 38.8 C."]; patient: tender cervical lymph nodes present (current) [line: "Anterior cervical lymph nodes enlarged and tender to touch."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Male patient of 44 years.
Sore throat for two days.
Back in 2013, temperature stood at 37.3 C.
Current temperature 38.8 C.
Anterior cervical lymph nodes enlarged and tender to touch.
Teeth in good repair.
Drives a car.
```

**A2-G30-C3**

Facts: patient: temperature = 38.9 (past (2013)) [line: "Back in 2013, temperature stood at 38.9 C."]; patient: temperature = 37.2 (current) [line: "Current temperature 37.2 C."]; patient: tender cervical lymph nodes present (current) [line: "Anterior cervical lymph nodes enlarged and tender to touch."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Male patient of 44 years.
Sore throat for two days.
Back in 2013, temperature stood at 38.9 C.
Current temperature 37.2 C.
Anterior cervical lymph nodes enlarged and tender to touch.
Teeth in good repair.
Drives a car.
```

**A2-G30-C4**

Facts: patient: temperature = 37.3 (past (2013)) [line: "Records from 2013 list temperature at 37.3 C."]; patient: temperature = 37.2 (current) [line: "Temperature now 37.2 C (tympanic)."]; patient: tender cervical lymph nodes present (current) [line: "Anterior cervical lymph nodes enlarged and tender to touch."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Man of 44 years.
Sore throat for two days.
Teeth in good repair.
Records from 2013 list temperature at 37.3 C.
Drives a car.
Temperature now 37.2 C (tympanic).
Anterior cervical lymph nodes enlarged and tender to touch.
```


## G31

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**A2-G31-C1**

Facts: patient: peptic ulcer present (past (2023)) [line: "Formerly treated for a peptic ulcer; endoscopy in 2023 showed it had gone."]; patient: heart rate = 68 (current) [line: "Heart rate now 68/min on a pulse check."]; patient: age = 77 (current) [line: "Currently aged 77 years."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Her sister has a lazy eye.
Pupils equal and reactive to light.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2011.
Sees a dentist yearly.
Lives in a second-floor apartment.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Formerly treated for a peptic ulcer; endoscopy in 2023 showed it had gone.
Zinc of 85 mcg/dL in 2011.
Heart rate now 68/min on a pulse check.
Sleeps seven hours a night.
Currently aged 77 years.
Her wife lives with psoriasis.
Uses sunscreen in summer.
Photographs local wildlife.
Her sister wears contact lenses.
Has two cats.
Drives a car.
Enjoys board games.
Her sister burned a hand on a stove years ago.
```

**A2-G31-C2**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: heart rate = 68 (current) [line: "Heart rate now 68/min on a pulse check."]; patient: age = 77 (current) [line: "Currently aged 77 years."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Her sister has a lazy eye.
Pupils equal and reactive to light.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2011.
Sees a dentist yearly.
Lives in a second-floor apartment.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Appetite good; no indigestion.
Zinc of 85 mcg/dL in 2011.
Heart rate now 68/min on a pulse check.
Sleeps seven hours a night.
Currently aged 77 years.
Her wife lives with psoriasis.
Uses sunscreen in summer.
Photographs local wildlife.
Her sister wears contact lenses.
Has two cats.
Drives a car.
Enjoys board games.
Her sister burned a hand on a stove years ago.
```

**A2-G31-C3**

Facts: patient: peptic ulcer denied by name (current) [line: "Has never had a peptic ulcer."]; patient: heart rate = 68 (current) [line: "Heart rate now 68/min on a pulse check."]; patient: age = 77 (current) [line: "Currently aged 77 years."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Her sister has a lazy eye.
Pupils equal and reactive to light.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2011.
Sees a dentist yearly.
Lives in a second-floor apartment.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Has never had a peptic ulcer.
Zinc of 85 mcg/dL in 2011.
Heart rate now 68/min on a pulse check.
Sleeps seven hours a night.
Currently aged 77 years.
Her wife lives with psoriasis.
Uses sunscreen in summer.
Photographs local wildlife.
Her sister wears contact lenses.
Has two cats.
Drives a car.
Enjoys board games.
Her sister burned a hand on a stove years ago.
```

**A2-G31-C4**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: heart rate = 68 (current) [line: "Current heart rate 68/min."]; patient: age = 77 (current) [line: "Current age 77 years."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Her sister has a lazy eye.
Drives a car.
Zinc of 85 mcg/dL in 2011.
Free T4 of 1.2 ng/dL in 2011.
Uses sunscreen in summer.
Knits as a hobby.
Appetite good; no indigestion.
Her wife lives with psoriasis.
Enjoys board games.
Has two cats.
Current heart rate 68/min.
Pupils equal and reactive to light.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Current age 77 years.
Sleeps seven hours a night.
Sees a dentist yearly.
Photographs local wildlife.
Owns a bicycle.
Her sister burned a hand on a stove years ago.
Her sister wears contact lenses.
```


## G32

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current systolic blood pressure is 90 mmHg or less, prescribe fondaparinux instead.

**A2-G32-C1**

Facts: patient: systolic blood pressure = 86 (current) [line: "Observations now: blood pressure 86/62 mmHg."]; patient: myocardial infarction or peripheral artery disease denied by name (current) [line: "Has never had a heart attack or peripheral artery disease."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Man of 71 years.
First day after elective total hip replacement.
Sleeps seven hours a night.
Prefers to be addressed by first name.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Plays the piano.
His roommate has a lazy eye.
His friend has recovered from a dislocated finger.
Knits as a hobby.
In 2012, folate was 12 ng/mL.
Owns a bicycle.
Enjoys board games.
Paints watercolors as a hobby.
Prefers morning appointments.
His sister lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Observations now: blood pressure 86/62 mmHg.
Has never had a heart attack or peripheral artery disease.
His wife sprained a thumb last month.
Drives a car.
```

**A2-G32-C2**

Facts: patient: systolic blood pressure = 86 (current) [line: "Observations now: blood pressure 86/62 mmHg."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Man of 71 years.
First day after elective total hip replacement.
Sleeps seven hours a night.
Prefers to be addressed by first name.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Plays the piano.
His roommate has a lazy eye.
His friend has recovered from a dislocated finger.
Knits as a hobby.
In 2012, folate was 12 ng/mL.
Owns a bicycle.
Enjoys board games.
Paints watercolors as a hobby.
Prefers morning appointments.
His sister lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Observations now: blood pressure 86/62 mmHg.
Lives with peripheral artery disease affecting the left leg.
His wife sprained a thumb last month.
Drives a car.
```

**A2-G32-C3**

Facts: patient: systolic blood pressure = 86 (current) [line: "Current systolic blood pressure 86 mmHg."]; myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Male patient of 71 years.
First day after elective total hip replacement.
His friend has recovered from a dislocated finger.
Knits as a hobby.
Enjoys board games.
His sister lives with psoriasis.
Has two cats.
Sees a dentist yearly.
Sleeps seven hours a night.
Prefers morning appointments.
Current systolic blood pressure 86 mmHg.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Drives a car.
Plays the piano.
Owns a bicycle.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
In 2012, folate was 12 ng/mL.
Walks without calf pain.
His roommate has a lazy eye.
His wife sprained a thumb last month.
```

**A2-G32-C4**

Facts: patient: systolic blood pressure = 86 (current) [line: "Observations now: blood pressure 86/62 mmHg."]; myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Man of 71 years.
First day after elective total hip replacement.
Sleeps seven hours a night.
Prefers to be addressed by first name.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Plays the piano.
His roommate has a lazy eye.
His friend has recovered from a dislocated finger.
Knits as a hobby.
In 2012, folate was 12 ng/mL.
Owns a bicycle.
Enjoys board games.
Paints watercolors as a hobby.
Prefers morning appointments.
His sister lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Observations now: blood pressure 86/62 mmHg.
Walks without calf pain.
His wife sprained a thumb last month.
Drives a car.
```

**A2-G32-C5**

Facts: patient: systolic blood pressure = 86 (current) [line: "Observations now: blood pressure 86/62 mmHg."]; myocardial infarction or peripheral artery disease: stated as unknown [line: "Myocardial infarction or peripheral artery disease: unknown."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Man of 71 years.
First day after elective total hip replacement.
Sleeps seven hours a night.
Prefers to be addressed by first name.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Plays the piano.
His roommate has a lazy eye.
His friend has recovered from a dislocated finger.
Knits as a hobby.
In 2012, folate was 12 ng/mL.
Owns a bicycle.
Enjoys board games.
Paints watercolors as a hobby.
Prefers morning appointments.
His sister lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Sees a dentist yearly.
Observations now: blood pressure 86/62 mmHg.
Myocardial infarction or peripheral artery disease: unknown.
His wife sprained a thumb last month.
Drives a car.
```


## G33

Rule: For primary prevention, prescribe atorvastatin. Score 2 points if the patient has ever had a venous thromboembolism (current or past); 1 point if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current temperature is above 38.0 C. If the score is 3 or more, prescribe ezetimibe instead.

**A2-G33-C1**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: temperature = 36.4 (current) [line: "Current temperature 36.4 C."]; patient: colorectal cancer present (past (2014)) [line: "Formerly had colon cancer; recovered fully after an operation in 2014."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Knits as a hobby.
Zinc of 85 mcg/dL in 2007.
Paints watercolors as a hobby.
Has two cats.
Prefers morning appointments.
Sleeps seven hours a night.
Her friend has a lazy eye.
Sees a dentist yearly.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Varicose veins: none seen.
Current temperature 36.4 C.
Drives a car.
Formerly had colon cancer; recovered fully after an operation in 2014.
In 2006, lipase was 30 U/L.
Owns a bicycle.
Photographs local wildlife.
Teeth in good repair.
Her roommate lives with psoriasis.
```

**A2-G33-C2**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: temperature = 38.6 (current) [line: "Current temperature 38.6 C."]; patient: colorectal cancer present (past (2014)) [line: "Formerly had colon cancer; recovered fully after an operation in 2014."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Knits as a hobby.
Zinc of 85 mcg/dL in 2007.
Paints watercolors as a hobby.
Has two cats.
Prefers morning appointments.
Sleeps seven hours a night.
Her friend has a lazy eye.
Sees a dentist yearly.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Varicose veins: none seen.
Current temperature 38.6 C.
Drives a car.
Formerly had colon cancer; recovered fully after an operation in 2014.
In 2006, lipase was 30 U/L.
Owns a bicycle.
Photographs local wildlife.
Teeth in good repair.
Her roommate lives with psoriasis.
```

**A2-G33-C3**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: temperature = 38.0 (current) [line: "Current temperature 38.0 C."]; patient: colorectal cancer present (past (2014)) [line: "Formerly had colon cancer; recovered fully after an operation in 2014."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Knits as a hobby.
Zinc of 85 mcg/dL in 2007.
Paints watercolors as a hobby.
Has two cats.
Prefers morning appointments.
Sleeps seven hours a night.
Her friend has a lazy eye.
Sees a dentist yearly.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Varicose veins: none seen.
Current temperature 38.0 C.
Drives a car.
Formerly had colon cancer; recovered fully after an operation in 2014.
In 2006, lipase was 30 U/L.
Owns a bicycle.
Photographs local wildlife.
Teeth in good repair.
Her roommate lives with psoriasis.
```

**A2-G33-C4**

Facts: patient: colorectal cancer present (past (2014)) [line: "Formerly had colon cancer; recovered fully after an operation in 2014."]; patient: temperature = 36.4 (current) [line: "Temperature now 36.4 C (tympanic)."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Female patient of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Knits as a hobby.
Her roommate lives with psoriasis.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2007.
In 2006, lipase was 30 U/L.
Formerly had colon cancer; recovered fully after an operation in 2014.
Prefers morning appointments.
Temperature now 36.4 C (tympanic).
Has two cats.
Paints watercolors as a hobby.
Her friend has a lazy eye.
Drives a car.
Teeth in good repair.
Photographs local wildlife.
Varicose veins: none seen.
Sees a dentist yearly.
Owns a bicycle.
Sleeps seven hours a night.
```


## G34

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

**A2-G34-C1**

Facts: patient: aspirin use present (current) [line: "Swallows one low-dose aspirin each night."]; diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]; patient: serum potassium = 4.0 (current) [line: "Current serum potassium 4.0 mmol/L."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Pupils equal and reactive to light.
Random glucose 92 mg/dL.
Current serum potassium 4.0 mmol/L.
```

**A2-G34-C2**

Facts: patient: aspirin use present (current) [line: "Swallows one low-dose aspirin each night."]; patient: serum potassium = 5.3 (current) [line: "Latest potassium result: 5.3 mmol/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Latest potassium result: 5.3 mmol/L.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```

**A2-G34-C3**

Facts: patient: aspirin use present (current) [line: "Swallows one low-dose aspirin each night."]; patient: serum potassium = 4.0 (current) [line: "Latest potassium result: 4.0 mmol/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Latest potassium result: 4.0 mmol/L.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```

**A2-G34-C4**

Facts: patient: aspirin use present (current) [line: "Swallows one low-dose aspirin each night."]; patient: serum potassium = 5.0 (current) [line: "Latest potassium result: 5.0 mmol/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Latest potassium result: 5.0 mmol/L.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```

**A2-G34-C5**

Facts: patient: aspirin use present (current) [line: "Swallows one low-dose aspirin each night."]; diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]; serum potassium: not mentioned (unknown)

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```


## G35

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

**A2-G35-C1**

Facts: patient: white cell count = 10.5 (current) [line: "Current white cell count 10.5 x10^9/L."]; patient: colorectal cancer present (past (2007)) [line: "Formerly had colon cancer; recovered fully after an operation in 2007."]; patient: white cell count = 13.5 (past) [line: "Last month, white cell count was 13.5 x10^9/L; the newest measurement replaces it."]; patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 48 years.
Atrial fibrillation; anticoagulation indicated.
Current white cell count 10.5 x10^9/L.
Photographs local wildlife.
Knits as a hobby.
Teeth in good repair.
Formerly had colon cancer; recovered fully after an operation in 2007.
Prefers morning appointments.
Last month, white cell count was 13.5 x10^9/L; the newest measurement replaces it.
Known coronary artery disease (two-vessel disease on angiography).
```

**A2-G35-C2**

Facts: patient: colorectal cancer present (past (2007)) [line: "Formerly had colon cancer; recovered fully after an operation in 2007."]; patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]; patient: white cell count = 10.5 (current) [line: "Latest WBC is 10.5 x10^9/L."]; patient: white cell count = 9.1 (past) [line: "Last month, white cell count was 9.1 x10^9/L; the newest measurement replaces it."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Woman of 48 years.
Atrial fibrillation; anticoagulation indicated.
Formerly had colon cancer; recovered fully after an operation in 2007.
Knits as a hobby.
Known coronary artery disease (two-vessel disease on angiography).
Teeth in good repair.
Latest WBC is 10.5 x10^9/L.
Last month, white cell count was 9.1 x10^9/L; the newest measurement replaces it.
Photographs local wildlife.
Prefers morning appointments.
```

**A2-G35-C3**

Facts: patient: colorectal cancer present (past (2007)) [line: "Formerly had colon cancer; recovered fully after an operation in 2007."]; patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]; white cell count: not mentioned (unknown)

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 48 years.
Atrial fibrillation; anticoagulation indicated.
Photographs local wildlife.
Knits as a hobby.
Teeth in good repair.
Formerly had colon cancer; recovered fully after an operation in 2007.
Prefers morning appointments.
Known coronary artery disease (two-vessel disease on angiography).
```

**A2-G35-C4**

Facts: patient: white cell count = 10.5 (current) [line: "Current white cell count 10.5 x10^9/L."]; patient: colorectal cancer present (past (2007)) [line: "Formerly had colon cancer; recovered fully after an operation in 2007."]; patient: white cell count = 9.1 (past) [line: "Last month, white cell count was 9.1 x10^9/L; the newest measurement replaces it."]; patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 48 years.
Atrial fibrillation; anticoagulation indicated.
Current white cell count 10.5 x10^9/L.
Photographs local wildlife.
Knits as a hobby.
Teeth in good repair.
Formerly had colon cancer; recovered fully after an operation in 2007.
Prefers morning appointments.
Last month, white cell count was 9.1 x10^9/L; the newest measurement replaces it.
Known coronary artery disease (two-vessel disease on angiography).
```

**A2-G35-C5**

Facts: patient: white cell count = 13.2 (current) [line: "Current white cell count 13.2 x10^9/L."]; patient: colorectal cancer present (past (2007)) [line: "Formerly had colon cancer; recovered fully after an operation in 2007."]; patient: white cell count = 9.1 (past) [line: "Last month, white cell count was 9.1 x10^9/L; the newest measurement replaces it."]; patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 48 years.
Atrial fibrillation; anticoagulation indicated.
Current white cell count 13.2 x10^9/L.
Photographs local wildlife.
Knits as a hobby.
Teeth in good repair.
Formerly had colon cancer; recovered fully after an operation in 2007.
Prefers morning appointments.
Last month, white cell count was 9.1 x10^9/L; the newest measurement replaces it.
Known coronary artery disease (two-vessel disease on angiography).
```


## G36

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**A2-G36-C1**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: ALT = 32 (past (2024)) [line: "Back in 2024, ALT stood at 32 U/L."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; patient: ALT = 26 (current) [line: "Current ALT 26 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 42 years.
Spreading redness and warmth of the right shin for two days.
Varicose veins: none seen.
Owns a bicycle.
Has two cats.
Paints watercolors as a hobby.
His roommate burned a hand on a stove years ago.
Drives a car.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2022.
Knits as a hobby.
In 2006, lipase was 30 U/L.
Back in 2024, ALT stood at 32 U/L.
Prefers to be addressed by first name.
His friend has a lazy eye.
Zinc of 85 mcg/dL in 2009.
Duodenal ulcer years ago; recovered fully with treatment.
Prefers morning appointments.
His wife lives with psoriasis.
Current ALT 26 U/L.
His roommate wears contact lenses.
Teeth in good repair.
Plays the piano.
During a checkup in 2006, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
```

**A2-G36-C2**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: ALT = 137 (past (2024)) [line: "Back in 2024, ALT stood at 137 U/L."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; patient: ALT = 26 (current) [line: "Current ALT 26 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 42 years.
Spreading redness and warmth of the right shin for two days.
Varicose veins: none seen.
Owns a bicycle.
Has two cats.
Paints watercolors as a hobby.
His roommate burned a hand on a stove years ago.
Drives a car.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2022.
Knits as a hobby.
In 2006, lipase was 30 U/L.
Back in 2024, ALT stood at 137 U/L.
Prefers to be addressed by first name.
His friend has a lazy eye.
Zinc of 85 mcg/dL in 2009.
Duodenal ulcer years ago; recovered fully with treatment.
Prefers morning appointments.
His wife lives with psoriasis.
Current ALT 26 U/L.
His roommate wears contact lenses.
Teeth in good repair.
Plays the piano.
During a checkup in 2006, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
```

**A2-G36-C3**

Facts: patient: ALT = 32 (past (2024)) [line: "Records from 2024 list ALT at 32 U/L."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: ALT = 26 (current) [line: "ALT now 26 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Male patient of 42 years.
Spreading redness and warmth of the right shin for two days.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Has two cats.
Records from 2024 list ALT at 32 U/L.
Teeth in good repair.
Drives a car.
Owns a bicycle.
His roommate burned a hand on a stove years ago.
His friend has a lazy eye.
Duodenal ulcer years ago; recovered fully with treatment.
Free T4 of 1.2 ng/dL in 2022.
Prefers morning appointments.
Plays the piano.
Paints watercolors as a hobby.
Varicose veins: none seen.
Zinc of 85 mcg/dL in 2009.
In 2006, lipase was 30 U/L.
His wife lives with psoriasis.
During a checkup in 2006, total protein was 7.0 g/dL.
ALT now 26 U/L.
His roommate wears contact lenses.
Photographs local wildlife.
Knits as a hobby.
```

**A2-G36-C4**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: ALT = 32 (past (2024)) [line: "Back in 2024, ALT stood at 32 U/L."]; patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; patient: ALT = 141 (current) [line: "Current ALT 141 U/L."]

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 42 years.
Spreading redness and warmth of the right shin for two days.
Varicose veins: none seen.
Owns a bicycle.
Has two cats.
Paints watercolors as a hobby.
His roommate burned a hand on a stove years ago.
Drives a car.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2022.
Knits as a hobby.
In 2006, lipase was 30 U/L.
Back in 2024, ALT stood at 32 U/L.
Prefers to be addressed by first name.
His friend has a lazy eye.
Zinc of 85 mcg/dL in 2009.
Duodenal ulcer years ago; recovered fully with treatment.
Prefers morning appointments.
His wife lives with psoriasis.
Current ALT 141 U/L.
His roommate wears contact lenses.
Teeth in good repair.
Plays the piano.
During a checkup in 2006, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
```


## G37

Rule: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

**A2-G37-C1**

Facts: patient: oxygen saturation = 95 (current) [line: "Latest oxygen saturation reading: 95%."]; patient: age = 72 (current) [line: "Currently aged 72 years."]; patient: systolic blood pressure = 140 (current) [line: "Observations now: blood pressure 140/92 mmHg."]; patient: heart rate = 107 (current) [line: "Heart rate now 107/min on a pulse check."]; cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]

Claims: s = The heart rate criterion contributes 0 points. | s' = The heart rate criterion contributes 1 point.
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Prefers morning appointments.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Latest oxygen saturation reading: 95%.
His sister has recovered from a dislocated finger.
His friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2014.
Currently aged 72 years.
His wife wears contact lenses.
Enjoys board games.
His roommate sprained a thumb last month.
Has two cats.
Lives in a second-floor apartment.
Observations now: blood pressure 140/92 mmHg.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2009, lipase was 30 U/L.
Heart rate now 107/min on a pulse check.
Sees a dentist yearly.
Oncology follow-up: none.
```

**A2-G37-C2**

Facts: patient: oxygen saturation = 95 (current) [line: "Latest oxygen saturation reading: 95%."]; patient: age = 72 (current) [line: "Currently aged 72 years."]; patient: systolic blood pressure = 140 (current) [line: "Observations now: blood pressure 140/92 mmHg."]; patient: heart rate = 61 (current) [line: "Heart rate now 61/min on a pulse check."]; cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]

Claims: s = The heart rate criterion contributes 0 points. | s' = The heart rate criterion contributes 1 point.
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Prefers morning appointments.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Latest oxygen saturation reading: 95%.
His sister has recovered from a dislocated finger.
His friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2014.
Currently aged 72 years.
His wife wears contact lenses.
Enjoys board games.
His roommate sprained a thumb last month.
Has two cats.
Lives in a second-floor apartment.
Observations now: blood pressure 140/92 mmHg.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2009, lipase was 30 U/L.
Heart rate now 61/min on a pulse check.
Sees a dentist yearly.
Oncology follow-up: none.
```

**A2-G37-C3**

Facts: patient: oxygen saturation = 95 (current) [line: "Latest oxygen saturation reading: 95%."]; patient: age = 72 (current) [line: "Currently aged 72 years."]; patient: systolic blood pressure = 140 (current) [line: "Observations now: blood pressure 140/92 mmHg."]; patient: heart rate = 125 (current) [line: "Heart rate now 125/min on a pulse check."]; cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]

Claims: s = The heart rate criterion contributes 0 points. | s' = The heart rate criterion contributes 1 point.
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Prefers morning appointments.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Latest oxygen saturation reading: 95%.
His sister has recovered from a dislocated finger.
His friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2014.
Currently aged 72 years.
His wife wears contact lenses.
Enjoys board games.
His roommate sprained a thumb last month.
Has two cats.
Lives in a second-floor apartment.
Observations now: blood pressure 140/92 mmHg.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2009, lipase was 30 U/L.
Heart rate now 125/min on a pulse check.
Sees a dentist yearly.
Oncology follow-up: none.
```

**A2-G37-C4**

Facts: patient: systolic blood pressure = 140 (current) [line: "Current systolic blood pressure 140 mmHg."]; patient: heart rate = 61 (current) [line: "Current heart rate 61/min."]; patient: age = 72 (current) [line: "Current age 72 years."]; patient: oxygen saturation = 95 (current) [line: "Current oxygen saturation 95%."]; cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]

Claims: s = The heart rate criterion contributes 0 points. | s' = The heart rate criterion contributes 1 point.
```
An adult man.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Free T4 of 1.2 ng/dL in 2014.
Sees a dentist yearly.
His roommate sprained a thumb last month.
Lives in a second-floor apartment.
Photographs local wildlife.
Current systolic blood pressure 140 mmHg.
Current heart rate 61/min.
Paints watercolors as a hobby.
Current age 72 years.
Has two cats.
Enjoys board games.
His friend lives with psoriasis.
Prefers to be addressed by first name.
His wife wears contact lenses.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Current oxygen saturation 95%.
Oncology follow-up: none.
Prefers morning appointments.
His sister has recovered from a dislocated finger.
In 2009, lipase was 30 U/L.
```


## G38

Rule: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.

**A2-G38-C1**

Facts: patient: systolic blood pressure = 143 (current) [line: "Current systolic blood pressure 143 mmHg."]; patient: respiratory rate = 15 (current) [line: "Current respiratory rate 15/min."]; patient: oxygen saturation = 96 (current) [line: "Latest oxygen saturation reading: 96%."]; new confusion: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 3 points.
```
Female patient of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current systolic blood pressure 143 mmHg.
Current respiratory rate 15/min.
Latest oxygen saturation reading: 96%.
```

**A2-G38-C2**

Facts: patient: systolic blood pressure = 143 (current) [line: "Current systolic blood pressure 143 mmHg."]; patient: respiratory rate = 34 (current) [line: "Current respiratory rate 34/min."]; patient: oxygen saturation = 96 (current) [line: "Latest oxygen saturation reading: 96%."]; new confusion: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 3 points.
```
Female patient of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current systolic blood pressure 143 mmHg.
Current respiratory rate 34/min.
Latest oxygen saturation reading: 96%.
```

**A2-G38-C3**

Facts: patient: oxygen saturation = 96 (current) [line: "Current oxygen saturation 96%."]; patient: systolic blood pressure = 143 (current) [line: "Observations now: blood pressure 143/94 mmHg."]; patient: respiratory rate = 15 (current) [line: "Observations now: respiratory rate 15/min."]; new confusion: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 3 points.
```
Woman of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current oxygen saturation 96%.
Observations now: blood pressure 143/94 mmHg.
Observations now: respiratory rate 15/min.
```

**A2-G38-C4**

Facts: patient: systolic blood pressure = 143 (current) [line: "Current systolic blood pressure 143 mmHg."]; patient: respiratory rate = 23 (current) [line: "Current respiratory rate 23/min."]; patient: oxygen saturation = 96 (current) [line: "Latest oxygen saturation reading: 96%."]; new confusion: not mentioned (counts as absent)

Claims: s = The respiratory rate criterion contributes 0 points. | s' = The respiratory rate criterion contributes 3 points.
```
Female patient of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current systolic blood pressure 143 mmHg.
Current respiratory rate 23/min.
Latest oxygen saturation reading: 96%.
```


## G39

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had a venous thromboembolism (current or past) and the current serum creatinine is above 2.0 mg/dL, prescribe clotrimazole pessaries instead.

**A2-G39-C1**

Facts: patient: venous thromboembolism present (past) [line: "Pulmonary embolism years ago, treated for six months."]; patient: serum creatinine = 2.4 (current) [line: "Latest creatinine result: 2.4 mg/dL."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Pulmonary embolism years ago, treated for six months.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```

**A2-G39-C2**

Facts: roommate: venous thromboembolism present (past) [line: "Her roommate had a DVT years ago."]; patient: serum creatinine = 2.4 (current) [line: "Latest creatinine result: 2.4 mg/dL."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her roommate had a DVT years ago.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```

**A2-G39-C3**

Facts: patient: serum creatinine = 2.4 (current) [line: "Current serum creatinine 2.4 mg/dL."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
```
Woman of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current serum creatinine 2.4 mg/dL.
Coagulation tests normal on recent bloodwork.
Plays the piano.
```

**A2-G39-C4**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]; patient: serum creatinine = 2.4 (current) [line: "Latest creatinine result: 2.4 mg/dL."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Coagulation tests normal on recent bloodwork.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```


## G40

Rule: For primary prevention, prescribe atorvastatin. If the current heart rate is above 90/min or the current serum potassium is above 5.0 mmol/L, prescribe ezetimibe instead.

**A2-G40-C1**

Facts: patient: heart rate = 83 (current) [line: "Heart rate now 83/min on a pulse check."]; patient: serum potassium = 5.0 (current) [line: "Current serum potassium 5.0 mmol/L."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 5.0 mmol/L.
Plays the piano.
```

**A2-G40-C2**

Facts: patient: heart rate = 83 (current) [line: "Heart rate now 83/min on a pulse check."]; patient: serum potassium = 5.2 (current) [line: "Current serum potassium 5.2 mmol/L."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 5.2 mmol/L.
Plays the piano.
```

**A2-G40-C3**

Facts: patient: serum potassium = 4.1 (current) [line: "Latest potassium result: 4.1 mmol/L."]; patient: heart rate = 83 (current) [line: "Current heart rate 83/min."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Latest potassium result: 4.1 mmol/L.
Sees a dentist yearly.
Plays the piano.
Current heart rate 83/min.
Paints watercolors as a hobby.
```

**A2-G40-C4**

Facts: patient: heart rate = 83 (current) [line: "Heart rate now 83/min on a pulse check."]; patient: serum potassium = 4.1 (current) [line: "Current serum potassium 4.1 mmol/L."]

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 4.1 mmol/L.
Plays the piano.
```


## G41

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**A2-G41-C1**

Facts: patient: eGFR = 52 (past (2018)) [line: "Records from 2018 list eGFR at 52 mL/min/1.73 m2."]; patient: white cell count = 13.5 (current) [line: "Latest WBC is 13.5 x10^9/L."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]; patient: heart rate = 70 (current) [line: "Current heart rate 70/min."]; patient: eGFR = 80 (current) [line: "eGFR now 80 mL/min/1.73 m2."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 81 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Records from 2018 list eGFR at 52 mL/min/1.73 m2.
Plays the piano.
Photographs local wildlife.
Latest WBC is 13.5 x10^9/L.
Face and neck without swelling on examination.
Lives in a second-floor apartment.
Current heart rate 70/min.
eGFR now 80 mL/min/1.73 m2.
```

**A2-G41-C2**

Facts: angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]; patient: white cell count = 13.5 (current) [line: "Current white cell count 13.5 x10^9/L."]; patient: eGFR = 52 (past (2018)) [line: "Back in 2018, eGFR stood at 52 mL/min/1.73 m2."]; patient: heart rate = 70 (current) [line: "Heart rate now 70/min on a pulse check."]; patient: eGFR = 80 (current) [line: "Current eGFR 80 mL/min/1.73 m2."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Female patient of 81 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Plays the piano.
Face and neck without swelling on examination.
Current white cell count 13.5 x10^9/L.
Photographs local wildlife.
Back in 2018, eGFR stood at 52 mL/min/1.73 m2.
Heart rate now 70/min on a pulse check.
Lives in a second-floor apartment.
Current eGFR 80 mL/min/1.73 m2.
```

**A2-G41-C3**

Facts: patient: eGFR = 52 (past (2018)) [line: "Records from 2018 list eGFR at 52 mL/min/1.73 m2."]; patient: white cell count = 13.5 (current) [line: "Latest WBC is 13.5 x10^9/L."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]; patient: heart rate = 70 (current) [line: "Current heart rate 70/min."]; patient: eGFR = 37 (current) [line: "eGFR now 37 mL/min/1.73 m2."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 81 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Records from 2018 list eGFR at 52 mL/min/1.73 m2.
Plays the piano.
Photographs local wildlife.
Latest WBC is 13.5 x10^9/L.
Face and neck without swelling on examination.
Lives in a second-floor apartment.
Current heart rate 70/min.
eGFR now 37 mL/min/1.73 m2.
```

**A2-G41-C4**

Facts: patient: eGFR = 39 (past (2018)) [line: "Records from 2018 list eGFR at 39 mL/min/1.73 m2."]; patient: white cell count = 13.5 (current) [line: "Latest WBC is 13.5 x10^9/L."]; angioedema: not named; a general line implies absence (counts as absent) [line: "Face and neck without swelling on examination."]; patient: heart rate = 70 (current) [line: "Current heart rate 70/min."]; patient: eGFR = 80 (current) [line: "eGFR now 80 mL/min/1.73 m2."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 81 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Records from 2018 list eGFR at 39 mL/min/1.73 m2.
Plays the piano.
Photographs local wildlife.
Latest WBC is 13.5 x10^9/L.
Face and neck without swelling on examination.
Lives in a second-floor apartment.
Current heart rate 70/min.
eGFR now 80 mL/min/1.73 m2.
```


## G42

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

**A2-G42-C1**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; patient: serum potassium = 5.3 (current) [line: "Latest potassium result: 5.3 mmol/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 66 years.
Acute low back pain after lifting.
Uses sunscreen in summer.
Enjoys board games.
Owns a bicycle.
Prefers to be addressed by first name.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Her sister has a lazy eye.
Her friend burned a hand on a stove years ago.
During a checkup in 2005, total protein was 7.0 g/dL.
Cardiac stress test unremarkable last year.
Lives in a second-floor apartment.
Has two cats.
Tonsillar exudate visible on both sides.
Her sister has recovered from a dislocated finger.
Drives a car.
Sees a dentist yearly.
Latest potassium result: 5.3 mmol/L.
Prefers morning appointments.
```

**A2-G42-C2**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; patient: serum potassium = 4.2 (current) [line: "Latest potassium result: 4.2 mmol/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 66 years.
Acute low back pain after lifting.
Uses sunscreen in summer.
Enjoys board games.
Owns a bicycle.
Prefers to be addressed by first name.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Her sister has a lazy eye.
Her friend burned a hand on a stove years ago.
During a checkup in 2005, total protein was 7.0 g/dL.
Cardiac stress test unremarkable last year.
Lives in a second-floor apartment.
Has two cats.
Tonsillar exudate visible on both sides.
Her sister has recovered from a dislocated finger.
Drives a car.
Sees a dentist yearly.
Latest potassium result: 4.2 mmol/L.
Prefers morning appointments.
```

**A2-G42-C3**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; serum potassium: not mentioned (unknown)

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 66 years.
Acute low back pain after lifting.
Uses sunscreen in summer.
Enjoys board games.
Owns a bicycle.
Prefers to be addressed by first name.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Her sister has a lazy eye.
Her friend burned a hand on a stove years ago.
During a checkup in 2005, total protein was 7.0 g/dL.
Cardiac stress test unremarkable last year.
Lives in a second-floor apartment.
Has two cats.
Tonsillar exudate visible on both sides.
Her sister has recovered from a dislocated finger.
Drives a car.
Sees a dentist yearly.
Prefers morning appointments.
```

**A2-G42-C4**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]; patient: serum potassium = 4.8 (current) [line: "Latest potassium result: 4.8 mmol/L."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 66 years.
Acute low back pain after lifting.
Uses sunscreen in summer.
Enjoys board games.
Owns a bicycle.
Prefers to be addressed by first name.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Her sister has a lazy eye.
Her friend burned a hand on a stove years ago.
During a checkup in 2005, total protein was 7.0 g/dL.
Cardiac stress test unremarkable last year.
Lives in a second-floor apartment.
Has two cats.
Tonsillar exudate visible on both sides.
Her sister has recovered from a dislocated finger.
Drives a car.
Sees a dentist yearly.
Latest potassium result: 4.8 mmol/L.
Prefers morning appointments.
```

**A2-G42-C5**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: serum potassium = 4.2 (current) [line: "Current serum potassium 4.2 mmol/L."]; patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 66 years.
Acute low back pain after lifting.
In 2009, lipase was 30 U/L.
During a checkup in 2005, total protein was 7.0 g/dL.
Photographs local wildlife.
Sees a dentist yearly.
Her sister has a lazy eye.
Her friend burned a hand on a stove years ago.
Has two cats.
Lives in a second-floor apartment.
Owns a bicycle.
Enjoys board games.
Uses sunscreen in summer.
Her sister wears contact lenses.
Cardiac stress test unremarkable last year.
Drives a car.
Current serum potassium 4.2 mmol/L.
Her sister has recovered from a dislocated finger.
Tonsillar exudate visible on both sides.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Prefers morning appointments.
```


## G43

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**A2-G43-C1**

Facts: patient: calf swelling = 4.1 (current) [line: "Difference in calf circumference now 4.1 cm."]; colorectal cancer: stated as unknown [line: "Colorectal cancer (patient or first-degree relative): unknown."]; patient: age = 46 (current) [line: "Currently aged 46 years."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Colorectal cancer (patient or first-degree relative): unknown.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```

**A2-G43-C2**

Facts: patient: calf swelling = 4.1 (current) [line: "Difference in calf circumference now 4.1 cm."]; patient: colorectal cancer denied by name (current) [line: "Has never had bowel cancer."]; patient: age = 46 (current) [line: "Currently aged 46 years."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Has never had bowel cancer.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```

**A2-G43-C3**

Facts: patient: calf swelling = 4.1 (current) [line: "Current calf swelling 4.1 cm compared with the other leg."]; colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: age = 46 (current) [line: "Current age 46 years."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
Woman, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Current calf swelling 4.1 cm compared with the other leg.
Rectal exam unremarkable.
Has two cats.
Owns a bicycle.
Current age 46 years.
```

**A2-G43-C4**

Facts: patient: calf swelling = 4.1 (current) [line: "Difference in calf circumference now 4.1 cm."]; patient: colorectal cancer present (current) [line: "Colorectal cancer under active treatment."]; patient: age = 46 (current) [line: "Currently aged 46 years."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Colorectal cancer under active treatment.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```

**A2-G43-C5**

Facts: patient: calf swelling = 4.1 (current) [line: "Difference in calf circumference now 4.1 cm."]; colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]; patient: age = 46 (current) [line: "Currently aged 46 years."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Rectal exam unremarkable.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```


## G44

Rule: For rate control in atrial fibrillation, prescribe metoprolol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 2 points if the patient has ever had a venous thromboembolism (current or past); 3 points if the patient has ever had coronary artery disease (current or past); 1 point if the current white cell count is above 12.0 x10^9/L. If the score is 4 or more, prescribe diltiazem instead.

**A2-G44-C1**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: white cell count = 6.9 (current) [line: "Latest WBC is 6.9 x10^9/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; patient: coronary artery disease present (past (2006)) [line: "Had coronary artery disease, treated with bypass surgery in 2006; recovered well."]

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Has two cats.
Enjoys board games.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest WBC is 6.9 x10^9/L.
HbA1c 5.3% at a routine check.
Had coronary artery disease, treated with bypass surgery in 2006; recovered well.
Pupils equal and reactive to light.
```

**A2-G44-C2**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: white cell count = 13.1 (current) [line: "Latest WBC is 13.1 x10^9/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; patient: coronary artery disease present (past (2006)) [line: "Had coronary artery disease, treated with bypass surgery in 2006; recovered well."]

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Has two cats.
Enjoys board games.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest WBC is 13.1 x10^9/L.
HbA1c 5.3% at a routine check.
Had coronary artery disease, treated with bypass surgery in 2006; recovered well.
Pupils equal and reactive to light.
```

**A2-G44-C3**

Facts: patient: coronary artery disease present (past (2006)) [line: "Had coronary artery disease, treated with bypass surgery in 2006; recovered well."]; patient: white cell count = 6.9 (current) [line: "Current white cell count 6.9 x10^9/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Woman of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Lives in a second-floor apartment.
Had coronary artery disease, treated with bypass surgery in 2006; recovered well.
Current white cell count 6.9 x10^9/L.
HbA1c 5.3% at a routine check.
Pupils equal and reactive to light.
Varicose veins: none seen.
Enjoys board games.
Has two cats.
```

**A2-G44-C4**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; patient: white cell count = 12.0 (current) [line: "Latest WBC is 12.0 x10^9/L."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; patient: coronary artery disease present (past (2006)) [line: "Had coronary artery disease, treated with bypass surgery in 2006; recovered well."]

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Has two cats.
Enjoys board games.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest WBC is 12.0 x10^9/L.
HbA1c 5.3% at a routine check.
Had coronary artery disease, treated with bypass surgery in 2006; recovered well.
Pupils equal and reactive to light.
```

**A2-G44-C5**

Facts: venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]; diabetes: not named; a general line implies absence (counts as absent) [line: "HbA1c 5.3% at a routine check."]; patient: coronary artery disease present (past (2006)) [line: "Had coronary artery disease, treated with bypass surgery in 2006; recovered well."]; white cell count: not mentioned (unknown)

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
```
Female patient of 75 years.
Atrial fibrillation with a ventricular rate of 128/min.
Has two cats.
Enjoys board games.
Varicose veins: none seen.
Lives in a second-floor apartment.
HbA1c 5.3% at a routine check.
Had coronary artery disease, treated with bypass surgery in 2006; recovered well.
Pupils equal and reactive to light.
```


## G45

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. Score 2 points if the current blood urea nitrogen is above 19 mg/dL; 1 point if the current calf swelling compared with the other leg is 3.0 cm or more; 3 points if the current serum creatinine is above 2.0 mg/dL. If the score is 4 or more, prescribe intravenous piperacillin-tazobactam instead.

**A2-G45-C1**

Facts: patient: serum creatinine = 2.5 (current) [line: "Latest creatinine result: 2.5 mg/dL."]; patient: calf swelling = 1.3 (past (2009)) [line: "Records from 2009 list calf swelling at 1.3 cm."]; patient: calf swelling = 4.7 (current) [line: "Difference in calf circumference now 4.7 cm."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen 15 mg/dL on the current labs."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
Man of 75 years.
Suspected chest infection; assessed on the medical ward.
Drives a car.
Latest creatinine result: 2.5 mg/dL.
Records from 2009 list calf swelling at 1.3 cm.
Owns a bicycle.
Difference in calf circumference now 4.7 cm.
Blood urea nitrogen 15 mg/dL on the current labs.
Prefers morning appointments.
```

**A2-G45-C2**

Facts: patient: serum creatinine = 2.5 (current) [line: "Current serum creatinine 2.5 mg/dL."]; patient: calf swelling = 1.3 (past (2009)) [line: "Back in 2009, calf swelling stood at 1.3 cm."]; patient: calf swelling = 0.5 (current) [line: "Current calf swelling 0.5 cm compared with the other leg."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen now: 15 mg/dL."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
Male patient of 75 years.
Suspected chest infection; assessed on the medical ward.
Current serum creatinine 2.5 mg/dL.
Back in 2009, calf swelling stood at 1.3 cm.
Drives a car.
Owns a bicycle.
Current calf swelling 0.5 cm compared with the other leg.
Prefers morning appointments.
Blood urea nitrogen now: 15 mg/dL.
```

**A2-G45-C3**

Facts: patient: serum creatinine = 2.5 (current) [line: "Latest creatinine result: 2.5 mg/dL."]; patient: calf swelling = 5.0 (past (2009)) [line: "Records from 2009 list calf swelling at 5.0 cm."]; patient: calf swelling = 0.5 (current) [line: "Difference in calf circumference now 0.5 cm."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen 15 mg/dL on the current labs."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
Man of 75 years.
Suspected chest infection; assessed on the medical ward.
Drives a car.
Latest creatinine result: 2.5 mg/dL.
Records from 2009 list calf swelling at 5.0 cm.
Owns a bicycle.
Difference in calf circumference now 0.5 cm.
Blood urea nitrogen 15 mg/dL on the current labs.
Prefers morning appointments.
```

**A2-G45-C4**

Facts: patient: serum creatinine = 2.5 (current) [line: "Latest creatinine result: 2.5 mg/dL."]; patient: calf swelling = 1.3 (past (2009)) [line: "Records from 2009 list calf swelling at 1.3 cm."]; patient: calf swelling = 0.5 (current) [line: "Difference in calf circumference now 0.5 cm."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen 15 mg/dL on the current labs."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
```
Man of 75 years.
Suspected chest infection; assessed on the medical ward.
Drives a car.
Latest creatinine result: 2.5 mg/dL.
Records from 2009 list calf swelling at 1.3 cm.
Owns a bicycle.
Difference in calf circumference now 0.5 cm.
Blood urea nitrogen 15 mg/dL on the current labs.
Prefers morning appointments.
```


## G46

Rule: Centor score (as used here, partial): 1 point each for temperature above 38.0 C; tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.

**A2-G46-C1**

Facts: tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]; temperature: not mentioned (unknown); tonsillar exudate: not mentioned (counts as absent)

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
```
Woman of 47 years.
Sore throat for three days.
Front of the neck without tenderness or swelling.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
```

**A2-G46-C2**

Facts: tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]; patient: temperature = 37.0 (current) [line: "Current temperature 37.0 C."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
```
Woman of 47 years.
Sore throat for three days.
Front of the neck without tenderness or swelling.
Current temperature 37.0 C.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
```

**A2-G46-C3**

Facts: patient: temperature = 37.0 (current) [line: "Temperature now 37.0 C (tympanic)."]; tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
```
Female patient of 47 years.
Sore throat for three days.
Temperature now 37.0 C (tympanic).
Photographs local wildlife.
Front of the neck without tenderness or swelling.
Teeth in good repair.
Paints watercolors as a hobby.
Knits as a hobby.
```

**A2-G46-C4**

Facts: tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]; patient: temperature = 38.0 (current) [line: "Current temperature 38.0 C."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
```
Woman of 47 years.
Sore throat for three days.
Front of the neck without tenderness or swelling.
Current temperature 38.0 C.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
```

**A2-G46-C5**

Facts: tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Front of the neck without tenderness or swelling."]; patient: temperature = 38.4 (current) [line: "Current temperature 38.4 C."]; tonsillar exudate: not mentioned (counts as absent)

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
```
Woman of 47 years.
Sore throat for three days.
Front of the neck without tenderness or swelling.
Current temperature 38.4 C.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
```


## G47

Rule: For an acute gout flare, prescribe naproxen. If the patient has an active peptic ulcer or the current eGFR is below 30 mL/min/1.73 m2, prescribe colchicine instead.

**A2-G47-C1**

Facts: patient: eGFR = 80 (current) [line: "Current eGFR 80 mL/min/1.73 m2."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe naproxen. | s' = Prescribe colchicine.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Man of 30 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Teeth in good repair.
Current eGFR 80 mL/min/1.73 m2.
Owns a bicycle.
```

**A2-G47-C2**

Facts: patient: eGFR = 80 (current) [line: "eGFR now 80 mL/min/1.73 m2."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe naproxen. | s' = Prescribe colchicine.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Male patient of 30 years.
Acute gout flare of the left knee.
eGFR now 80 mL/min/1.73 m2.
Owns a bicycle.
Sees a dentist yearly.
Teeth in good repair.
```

**A2-G47-C3**

Facts: patient: eGFR = 30 (current) [line: "Current eGFR 30 mL/min/1.73 m2."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe naproxen. | s' = Prescribe colchicine.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Man of 30 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Teeth in good repair.
Current eGFR 30 mL/min/1.73 m2.
Owns a bicycle.
```

**A2-G47-C4**

Facts: patient: eGFR = 13 (current) [line: "Current eGFR 13 mL/min/1.73 m2."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe naproxen. | s' = Prescribe colchicine.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Man of 30 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Teeth in good repair.
Current eGFR 13 mL/min/1.73 m2.
Owns a bicycle.
```


## G48

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**A2-G48-C1**

Facts: friend: peptic ulcer present (past) [line: "Her friend formerly had peptic ulcer disease."]; patient: age = 74 (current) [line: "Current age 74 years."]; patient: heart rate = 76 (current) [line: "Heart rate now 76/min on a pulse check."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Owns a bicycle.
Teeth in good repair.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Her friend formerly had peptic ulcer disease.
Current age 74 years.
Heart rate now 76/min on a pulse check.
```

**A2-G48-C2**

Facts: patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]; patient: age = 74 (current) [line: "Current age 74 years."]; patient: heart rate = 76 (current) [line: "Heart rate now 76/min on a pulse check."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Owns a bicycle.
Teeth in good repair.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Duodenal ulcer years ago; recovered fully with treatment.
Current age 74 years.
Heart rate now 76/min on a pulse check.
```

**A2-G48-C3**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Abdomen soft and non-tender."]; patient: age = 74 (current) [line: "Currently aged 74 years."]; patient: heart rate = 76 (current) [line: "Current heart rate 76/min."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Owns a bicycle.
Abdomen soft and non-tender.
Sleeps seven hours a night.
Currently aged 74 years.
Teeth in good repair.
Paints watercolors as a hobby.
Current heart rate 76/min.
```

**A2-G48-C4**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Abdomen soft and non-tender."]; patient: age = 74 (current) [line: "Current age 74 years."]; patient: heart rate = 76 (current) [line: "Heart rate now 76/min on a pulse check."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Owns a bicycle.
Teeth in good repair.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Abdomen soft and non-tender.
Current age 74 years.
Heart rate now 76/min on a pulse check.
```


## G49

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a peptic ulcer (current or past) or the patient is allergic to penicillin, prescribe fondaparinux instead.

**A2-G49-C1**

Facts: patient: penicillin allergy present (current) [line: "Penicillin allergy: anaphylaxis."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Female patient of 74 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
Penicillin allergy: anaphylaxis.
```

**A2-G49-C2**

Facts: penicillin allergy: not named; a general line implies absence (counts as absent) [line: "Drug allergies: none known."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Female patient of 74 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
Drug allergies: none known.
```

**A2-G49-C3**

Facts: penicillin allergy: not named; a general line implies absence (counts as absent) [line: "Drug allergies: none known."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Woman of 74 years.
First day after elective total hip replacement.
Drug allergies: none known.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Plays the piano.
Photographs local wildlife.
```

**A2-G49-C4**

Facts: patient: penicillin allergy present (past (2007)) [line: "Formerly recorded as penicillin-allergic; de-labeled in 2007 by an allergy clinic."]; peptic ulcer: not mentioned (counts as absent)

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Female patient of 74 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
Formerly recorded as penicillin-allergic; de-labeled in 2007 by an allergy clinic.
```


## G50

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**A2-G50-C1**

Facts: patient: age = 63 (current) [line: "Current age 63 years."]; weight: not mentioned (unknown)

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
```

**A2-G50-C2**

Facts: patient: weight = 69 (past (2007)) [line: "Back in 2007, weight stood at 69 kg."]; patient: age = 63 (current) [line: "Currently aged 63 years."]; patient: weight = 80 (current) [line: "Latest weight 80 kg."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
An adult woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Sees a dentist yearly.
Back in 2007, weight stood at 69 kg.
Currently aged 63 years.
Latest weight 80 kg.
```

**A2-G50-C3**

Facts: patient: age = 63 (current) [line: "Current age 63 years."]; patient: weight = 80 (current) [line: "Current weight 80 kg."]; patient: weight = 51 (past (2007)) [line: "Records from 2007 list weight at 51 kg."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
Current weight 80 kg.
Records from 2007 list weight at 51 kg.
```

**A2-G50-C4**

Facts: patient: age = 63 (current) [line: "Current age 63 years."]; patient: weight = 80 (current) [line: "Current weight 80 kg."]; patient: weight = 69 (past (2007)) [line: "Records from 2007 list weight at 69 kg."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
Current weight 80 kg.
Records from 2007 list weight at 69 kg.
```

**A2-G50-C5**

Facts: patient: age = 63 (current) [line: "Current age 63 years."]; patient: weight = 49 (current) [line: "Current weight 49 kg."]; patient: weight = 69 (past (2007)) [line: "Records from 2007 list weight at 69 kg."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
Current weight 49 kg.
Records from 2007 list weight at 69 kg.
```


## G51

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current systolic blood pressure is 90 mmHg or less, prescribe fondaparinux instead.

**A2-G51-C1**

Facts: patient: systolic blood pressure = 129 (past (2023)) [line: "Records from 2023 list systolic blood pressure at 129 mmHg."]; patient: systolic blood pressure = 124 (current) [line: "Observations now: blood pressure 124/83 mmHg."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "systolic blood pressure at or below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure at or below 90" holds for this patient.
```
Woman of 72 years.
First day after elective total hip replacement.
Records from 2023 list systolic blood pressure at 129 mmHg.
Zinc of 85 mcg/dL in 2021.
During a checkup in 2007, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Her friend wears contact lenses.
Pupils equal and reactive to light.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Observations now: blood pressure 124/83 mmHg.
Sees a dentist yearly.
Lives with peripheral artery disease affecting the left leg.
Has two cats.
Owns a bicycle.
Sleeps seven hours a night.
Her friend burned a hand on a stove years ago.
Lives in a second-floor apartment.
Enjoys board games.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
Knits as a hobby.
```

**A2-G51-C2**

Facts: patient: systolic blood pressure = 129 (past (2023)) [line: "Records from 2023 list systolic blood pressure at 129 mmHg."]; patient: systolic blood pressure = 90 (current) [line: "Observations now: blood pressure 90/64 mmHg."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "systolic blood pressure at or below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure at or below 90" holds for this patient.
```
Woman of 72 years.
First day after elective total hip replacement.
Records from 2023 list systolic blood pressure at 129 mmHg.
Zinc of 85 mcg/dL in 2021.
During a checkup in 2007, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Her friend wears contact lenses.
Pupils equal and reactive to light.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Observations now: blood pressure 90/64 mmHg.
Sees a dentist yearly.
Lives with peripheral artery disease affecting the left leg.
Has two cats.
Owns a bicycle.
Sleeps seven hours a night.
Her friend burned a hand on a stove years ago.
Lives in a second-floor apartment.
Enjoys board games.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
Knits as a hobby.
```

**A2-G51-C3**

Facts: patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]; systolic blood pressure: not mentioned (unknown)

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "systolic blood pressure at or below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure at or below 90" holds for this patient.
```
Woman of 72 years.
First day after elective total hip replacement.
Zinc of 85 mcg/dL in 2021.
During a checkup in 2007, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Her friend wears contact lenses.
Pupils equal and reactive to light.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Lives with peripheral artery disease affecting the left leg.
Has two cats.
Owns a bicycle.
Sleeps seven hours a night.
Her friend burned a hand on a stove years ago.
Lives in a second-floor apartment.
Enjoys board games.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
Knits as a hobby.
```

**A2-G51-C4**

Facts: patient: systolic blood pressure = 74 (past (2023)) [line: "Records from 2023 list systolic blood pressure at 74 mmHg."]; patient: systolic blood pressure = 124 (current) [line: "Observations now: blood pressure 124/83 mmHg."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "systolic blood pressure at or below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure at or below 90" holds for this patient.
```
Woman of 72 years.
First day after elective total hip replacement.
Records from 2023 list systolic blood pressure at 74 mmHg.
Zinc of 85 mcg/dL in 2021.
During a checkup in 2007, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Her friend wears contact lenses.
Pupils equal and reactive to light.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Observations now: blood pressure 124/83 mmHg.
Sees a dentist yearly.
Lives with peripheral artery disease affecting the left leg.
Has two cats.
Owns a bicycle.
Sleeps seven hours a night.
Her friend burned a hand on a stove years ago.
Lives in a second-floor apartment.
Enjoys board games.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
Knits as a hobby.
```

**A2-G51-C5**

Facts: patient: systolic blood pressure = 129 (past (2023)) [line: "Back in 2023, systolic blood pressure stood at 129 mmHg."]; patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]; patient: systolic blood pressure = 124 (current) [line: "Current systolic blood pressure 124 mmHg."]

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "systolic blood pressure at or below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure at or below 90" holds for this patient.
```
Female patient of 72 years.
First day after elective total hip replacement.
Sees a dentist yearly.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Back in 2023, systolic blood pressure stood at 129 mmHg.
Plays the piano.
Enjoys board games.
During a checkup in 2007, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Sleeps seven hours a night.
Her friend wears contact lenses.
Paints watercolors as a hobby.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Lives with peripheral artery disease affecting the left leg.
Owns a bicycle.
Knits as a hobby.
Zinc of 85 mcg/dL in 2021.
Teeth in good repair.
Has two cats.
Pupils equal and reactive to light.
Prefers morning appointments.
Her friend burned a hand on a stove years ago.
Current systolic blood pressure 124 mmHg.
```


## G52

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.

**A2-G52-C1**

Facts: patient: serum potassium = 4.5 (current) [line: "Latest potassium result: 4.5 mmol/L."]; patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 52 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Latest potassium result: 4.5 mmol/L.
Pupils equal and reactive to light.
In 2006, folate was 12 ng/mL.
Sees a dentist yearly.
Has two cats.
Knits as a hobby.
Plays the piano.
Free T4 of 1.2 ng/dL in 2014.
Her sister has recovered from a dislocated finger.
Paints watercolors as a hobby.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Her roommate lives with psoriasis.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Teeth in good repair.
Prefers to be addressed by first name.
Photographs local wildlife.
Enjoys board games.
Lives in a second-floor apartment.
```

**A2-G52-C2**

Facts: patient: serum potassium = 5.0 (current) [line: "Latest potassium result: 5.0 mmol/L."]; patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 52 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Latest potassium result: 5.0 mmol/L.
Pupils equal and reactive to light.
In 2006, folate was 12 ng/mL.
Sees a dentist yearly.
Has two cats.
Knits as a hobby.
Plays the piano.
Free T4 of 1.2 ng/dL in 2014.
Her sister has recovered from a dislocated finger.
Paints watercolors as a hobby.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Her roommate lives with psoriasis.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Teeth in good repair.
Prefers to be addressed by first name.
Photographs local wildlife.
Enjoys board games.
Lives in a second-floor apartment.
```

**A2-G52-C3**

Facts: patient: serum potassium = 4.5 (current) [line: "Current serum potassium 4.5 mmol/L."]; patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 52 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Teeth in good repair.
Photographs local wildlife.
Sees a dentist yearly.
Current serum potassium 4.5 mmol/L.
Plays the piano.
Her sister has recovered from a dislocated finger.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Owns a bicycle.
Has an acute pulmonary embolism, diagnosed this week.
Free T4 of 1.2 ng/dL in 2014.
In 2006, folate was 12 ng/mL.
Has two cats.
Knits as a hobby.
Her roommate lives with psoriasis.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Enjoys board games.
During a checkup in 2020, free T3 was 3.2 pg/mL.
```

**A2-G52-C4**

Facts: patient: serum potassium = 5.8 (current) [line: "Latest potassium result: 5.8 mmol/L."]; patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 52 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Latest potassium result: 5.8 mmol/L.
Pupils equal and reactive to light.
In 2006, folate was 12 ng/mL.
Sees a dentist yearly.
Has two cats.
Knits as a hobby.
Plays the piano.
Free T4 of 1.2 ng/dL in 2014.
Her sister has recovered from a dislocated finger.
Paints watercolors as a hobby.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Her roommate lives with psoriasis.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Teeth in good repair.
Prefers to be addressed by first name.
Photographs local wildlife.
Enjoys board games.
Lives in a second-floor apartment.
```


## G53

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.

**A2-G53-C1**

Facts: patient: serum potassium = 3.8 (current) [line: "Current serum potassium 3.8 mmol/L."]; patient: serum potassium = 4.4 (past (2005)) [line: "Back in 2005, serum potassium stood at 4.4 mmol/L."]; patient: venous thromboembolism present (past (2024)) [line: "Recovered from a pulmonary embolism in 2024."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum potassium 3.8 mmol/L.
Back in 2005, serum potassium stood at 4.4 mmol/L.
Teeth in good repair.
Recovered from a pulmonary embolism in 2024.
```

**A2-G53-C2**

Facts: patient: serum potassium = 5.5 (current) [line: "Current serum potassium 5.5 mmol/L."]; patient: serum potassium = 4.4 (past (2005)) [line: "Back in 2005, serum potassium stood at 4.4 mmol/L."]; patient: venous thromboembolism present (past (2024)) [line: "Recovered from a pulmonary embolism in 2024."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum potassium 5.5 mmol/L.
Back in 2005, serum potassium stood at 4.4 mmol/L.
Teeth in good repair.
Recovered from a pulmonary embolism in 2024.
```

**A2-G53-C3**

Facts: patient: serum potassium = 4.4 (past (2005)) [line: "Records from 2005 list serum potassium at 4.4 mmol/L."]; patient: serum potassium = 3.8 (current) [line: "Latest potassium result: 3.8 mmol/L."]; patient: venous thromboembolism present (past (2024)) [line: "Recovered from a pulmonary embolism in 2024."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Female patient of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Records from 2005 list serum potassium at 4.4 mmol/L.
Latest potassium result: 3.8 mmol/L.
Recovered from a pulmonary embolism in 2024.
Teeth in good repair.
```

**A2-G53-C4**

Facts: patient: serum potassium = 3.8 (current) [line: "Current serum potassium 3.8 mmol/L."]; patient: serum potassium = 5.3 (past (2005)) [line: "Back in 2005, serum potassium stood at 5.3 mmol/L."]; patient: venous thromboembolism present (past (2024)) [line: "Recovered from a pulmonary embolism in 2024."]

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Woman of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum potassium 3.8 mmol/L.
Back in 2005, serum potassium stood at 5.3 mmol/L.
Teeth in good repair.
Recovered from a pulmonary embolism in 2024.
```


## G54

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has new confusion; the current respiratory rate is 30/min or more; the current systolic blood pressure is below 90 mmHg.

**A2-G54-C1**

Facts: patient: systolic blood pressure = 79 (past) [line: "Last month, systolic blood pressure was 79 mmHg; the newest measurement replaces it."]; new confusion: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]; patient: systolic blood pressure = 119 (current) [line: "Current systolic blood pressure 119 mmHg."]; patient: respiratory rate = 36 (current) [line: "Current respiratory rate 36/min."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "systolic blood pressure below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure below 90" holds for this patient.
```
Woman of 52 years.
Community-acquired pneumonia confirmed on chest radiograph.
Pupils equal and reactive to light.
Last month, systolic blood pressure was 79 mmHg; the newest measurement replaces it.
Gives a clear account of the illness.
Current systolic blood pressure 119 mmHg.
Lives in a second-floor apartment.
Current respiratory rate 36/min.
Paints watercolors as a hobby.
```

**A2-G54-C2**

Facts: patient: systolic blood pressure = 119 (current) [line: "Observations now: blood pressure 119/80 mmHg."]; patient: respiratory rate = 36 (current) [line: "Observations now: respiratory rate 36/min."]; patient: systolic blood pressure = 122 (past) [line: "Last month, systolic blood pressure was 122 mmHg; the newest measurement replaces it."]; new confusion: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "systolic blood pressure below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure below 90" holds for this patient.
```
Female patient of 52 years.
Community-acquired pneumonia confirmed on chest radiograph.
Lives in a second-floor apartment.
Observations now: blood pressure 119/80 mmHg.
Observations now: respiratory rate 36/min.
Pupils equal and reactive to light.
Last month, systolic blood pressure was 122 mmHg; the newest measurement replaces it.
Gives a clear account of the illness.
Paints watercolors as a hobby.
```

**A2-G54-C3**

Facts: patient: systolic blood pressure = 122 (past) [line: "Last month, systolic blood pressure was 122 mmHg; the newest measurement replaces it."]; new confusion: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]; patient: systolic blood pressure = 119 (current) [line: "Current systolic blood pressure 119 mmHg."]; patient: respiratory rate = 36 (current) [line: "Current respiratory rate 36/min."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "systolic blood pressure below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure below 90" holds for this patient.
```
Woman of 52 years.
Community-acquired pneumonia confirmed on chest radiograph.
Pupils equal and reactive to light.
Last month, systolic blood pressure was 122 mmHg; the newest measurement replaces it.
Gives a clear account of the illness.
Current systolic blood pressure 119 mmHg.
Lives in a second-floor apartment.
Current respiratory rate 36/min.
Paints watercolors as a hobby.
```

**A2-G54-C4**

Facts: patient: systolic blood pressure = 122 (past) [line: "Last month, systolic blood pressure was 122 mmHg; the newest measurement replaces it."]; new confusion: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]; patient: systolic blood pressure = 77 (current) [line: "Current systolic blood pressure 77 mmHg."]; patient: respiratory rate = 36 (current) [line: "Current respiratory rate 36/min."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "systolic blood pressure below 90" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure below 90" holds for this patient.
```
Woman of 52 years.
Community-acquired pneumonia confirmed on chest radiograph.
Pupils equal and reactive to light.
Last month, systolic blood pressure was 122 mmHg; the newest measurement replaces it.
Gives a clear account of the illness.
Current systolic blood pressure 77 mmHg.
Lives in a second-floor apartment.
Current respiratory rate 36/min.
Paints watercolors as a hobby.
```


## G55

Rule: NEWS2 (as used here, partial: only the stated band of each listed item): 3 points for a heart rate of 131/min or more; 3 points for a systolic blood pressure of 220 mmHg or more; 2 points for a temperature of 39.1 C or more; 2 points for current use of supplemental oxygen. Any other value of these items scores 0 here, and the other NEWS2 items are not part of this question. Only current findings count.

**A2-G55-C1**

Facts: patient: systolic blood pressure = 133 (current) [line: "Current systolic blood pressure 133 mmHg."]; patient: temperature = 36.8 (current) [line: "Temperature now 36.8 C (tympanic)."]; patient: heart rate = 67 (current) [line: "Heart rate now 67/min on a pulse check."]; supplemental oxygen: not mentioned (counts as absent)

Claims: s = The systolic blood pressure criterion contributes 0 points. | s' = The systolic blood pressure criterion contributes 3 points.
```
Man of 52 years.
Newly admitted to the medical ward with a chest infection.
Current systolic blood pressure 133 mmHg.
During a checkup in 2017, total protein was 7.0 g/dL.
His roommate burned a hand on a stove years ago.
Enjoys board games.
Paints watercolors as a hobby.
His uncle sprained a thumb last month.
Drives a car.
Prefers to be addressed by first name.
Photographs local wildlife.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Zinc of 85 mcg/dL in 2015.
Has two cats.
Temperature now 36.8 C (tympanic).
Knits as a hobby.
Heart rate now 67/min on a pulse check.
Free T4 of 1.2 ng/dL in 2014.
```

**A2-G55-C2**

Facts: patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]; patient: systolic blood pressure = 215 (current) [line: "Observations now: blood pressure 215/133 mmHg."]; patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; supplemental oxygen: not mentioned (counts as absent)

Claims: s = The systolic blood pressure criterion contributes 0 points. | s' = The systolic blood pressure criterion contributes 3 points.
```
Male patient of 52 years.
Newly admitted to the medical ward with a chest infection.
Current heart rate 67/min.
Observations now: blood pressure 215/133 mmHg.
Current temperature 36.8 C.
His uncle sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2014.
Lives in a second-floor apartment.
Enjoys board games.
Uses sunscreen in summer.
Has two cats.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2015.
Photographs local wildlife.
Drives a car.
During a checkup in 2017, total protein was 7.0 g/dL.
```

**A2-G55-C3**

Facts: patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]; patient: systolic blood pressure = 133 (current) [line: "Observations now: blood pressure 133/88 mmHg."]; patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; supplemental oxygen: not mentioned (counts as absent)

Claims: s = The systolic blood pressure criterion contributes 0 points. | s' = The systolic blood pressure criterion contributes 3 points.
```
Male patient of 52 years.
Newly admitted to the medical ward with a chest infection.
Current heart rate 67/min.
Observations now: blood pressure 133/88 mmHg.
Current temperature 36.8 C.
His uncle sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2014.
Lives in a second-floor apartment.
Enjoys board games.
Uses sunscreen in summer.
Has two cats.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2015.
Photographs local wildlife.
Drives a car.
During a checkup in 2017, total protein was 7.0 g/dL.
```

**A2-G55-C4**

Facts: patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]; patient: systolic blood pressure = 220 (current) [line: "Observations now: blood pressure 220/136 mmHg."]; patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; supplemental oxygen: not mentioned (counts as absent)

Claims: s = The systolic blood pressure criterion contributes 0 points. | s' = The systolic blood pressure criterion contributes 3 points.
```
Male patient of 52 years.
Newly admitted to the medical ward with a chest infection.
Current heart rate 67/min.
Observations now: blood pressure 220/136 mmHg.
Current temperature 36.8 C.
His uncle sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2014.
Lives in a second-floor apartment.
Enjoys board games.
Uses sunscreen in summer.
Has two cats.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2015.
Photographs local wildlife.
Drives a car.
During a checkup in 2017, total protein was 7.0 g/dL.
```

**A2-G55-C5**

Facts: patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]; patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; systolic blood pressure: not mentioned (unknown); supplemental oxygen: not mentioned (counts as absent)

Claims: s = The systolic blood pressure criterion contributes 0 points. | s' = The systolic blood pressure criterion contributes 3 points.
```
Male patient of 52 years.
Newly admitted to the medical ward with a chest infection.
Current heart rate 67/min.
Current temperature 36.8 C.
His uncle sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2014.
Lives in a second-floor apartment.
Enjoys board games.
Uses sunscreen in summer.
Has two cats.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2015.
Photographs local wildlife.
Drives a car.
During a checkup in 2017, total protein was 7.0 g/dL.
```


## G56

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**A2-G56-C1**

Facts: patient: temperature = 38.5 (current) [line: "Current temperature 38.5 C."]; peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Female patient of 53 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
Her uncle burned a hand on a stove years ago.
Pupils equal and reactive to light.
Her wife lives with psoriasis.
Enjoys board games.
Prefers morning appointments.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
In 2021, lipase was 30 U/L.
Owns a bicycle.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Current temperature 38.5 C.
Lives in a second-floor apartment.
Drives a car.
During a checkup in 2018, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2010.
Sees a dentist yearly.
Sleeps seven hours a night.
Photographs local wildlife.
Has two cats.
Appetite good; no indigestion.
Plays the piano.
```

**A2-G56-C2**

Facts: patient: temperature = 38.5 (current) [line: "Current temperature 38.5 C."]; patient: peptic ulcer present (past (2014)) [line: "Formerly treated for a peptic ulcer; endoscopy in 2014 showed it had gone."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Female patient of 53 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
Her uncle burned a hand on a stove years ago.
Pupils equal and reactive to light.
Her wife lives with psoriasis.
Enjoys board games.
Prefers morning appointments.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
In 2021, lipase was 30 U/L.
Owns a bicycle.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Current temperature 38.5 C.
Lives in a second-floor apartment.
Drives a car.
During a checkup in 2018, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2010.
Sees a dentist yearly.
Sleeps seven hours a night.
Photographs local wildlife.
Has two cats.
Formerly treated for a peptic ulcer; endoscopy in 2014 showed it had gone.
Plays the piano.
```

**A2-G56-C3**

Facts: patient: temperature = 38.5 (current) [line: "Current temperature 38.5 C."]; roommate: peptic ulcer present (past) [line: "Her roommate recovered from a stomach ulcer years ago."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Female patient of 53 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
Her uncle burned a hand on a stove years ago.
Pupils equal and reactive to light.
Her wife lives with psoriasis.
Enjoys board games.
Prefers morning appointments.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
In 2021, lipase was 30 U/L.
Owns a bicycle.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Current temperature 38.5 C.
Lives in a second-floor apartment.
Drives a car.
During a checkup in 2018, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2010.
Sees a dentist yearly.
Sleeps seven hours a night.
Photographs local wildlife.
Has two cats.
Her roommate recovered from a stomach ulcer years ago.
Plays the piano.
```

**A2-G56-C4**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; patient: temperature = 38.5 (current) [line: "Temperature now 38.5 C (tympanic)."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
```
Woman of 53 years.
Atrial fibrillation; anticoagulation indicated.
Prefers morning appointments.
Sees a dentist yearly.
Prefers to be addressed by first name.
Her uncle burned a hand on a stove years ago.
Drives a car.
Has two cats.
Sleeps seven hours a night.
During a checkup in 2018, total protein was 7.0 g/dL.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Owns a bicycle.
Appetite good; no indigestion.
Her wife lives with psoriasis.
Enjoys board games.
In 2021, lipase was 30 U/L.
Plays the piano.
Pupils equal and reactive to light.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2010.
Temperature now 38.5 C (tympanic).
Lives in a second-floor apartment.
```


## G57

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

**A2-G57-C1**

Facts: myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]; patient: age = 66 (current) [line: "Currently aged 66 years."]; peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
An adult man.
Suspected chest infection; assessed on the medical ward.
Plays the piano.
Sees a dentist yearly.
Walks without calf pain.
Prefers morning appointments.
Teeth in good repair.
Lives in a second-floor apartment.
His friend has recovered from a dislocated finger.
Uses sunscreen in summer.
Sleeps seven hours a night.
In 2024, lipase was 30 U/L.
Prefers to be addressed by first name.
Has two cats.
Knits as a hobby.
In 2021, folate was 12 ng/mL.
His roommate has a lazy eye.
Currently aged 66 years.
Photographs local wildlife.
Enjoys board games.
Appetite good; no indigestion.
Drives a car.
His roommate lives with psoriasis.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2005.
```

**A2-G57-C2**

Facts: patient: myocardial infarction or peripheral artery disease present (past) [line: "Heart attack years ago, with full recovery."]; patient: age = 66 (current) [line: "Currently aged 66 years."]; peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
An adult man.
Suspected chest infection; assessed on the medical ward.
Plays the piano.
Sees a dentist yearly.
Heart attack years ago, with full recovery.
Prefers morning appointments.
Teeth in good repair.
Lives in a second-floor apartment.
His friend has recovered from a dislocated finger.
Uses sunscreen in summer.
Sleeps seven hours a night.
In 2024, lipase was 30 U/L.
Prefers to be addressed by first name.
Has two cats.
Knits as a hobby.
In 2021, folate was 12 ng/mL.
His roommate has a lazy eye.
Currently aged 66 years.
Photographs local wildlife.
Enjoys board games.
Appetite good; no indigestion.
Drives a car.
His roommate lives with psoriasis.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2005.
```

**A2-G57-C3**

Facts: patient: myocardial infarction or peripheral artery disease denied by name (current) [line: "Has never had a heart attack or peripheral artery disease."]; patient: age = 66 (current) [line: "Currently aged 66 years."]; peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
An adult man.
Suspected chest infection; assessed on the medical ward.
Plays the piano.
Sees a dentist yearly.
Has never had a heart attack or peripheral artery disease.
Prefers morning appointments.
Teeth in good repair.
Lives in a second-floor apartment.
His friend has recovered from a dislocated finger.
Uses sunscreen in summer.
Sleeps seven hours a night.
In 2024, lipase was 30 U/L.
Prefers to be addressed by first name.
Has two cats.
Knits as a hobby.
In 2021, folate was 12 ng/mL.
His roommate has a lazy eye.
Currently aged 66 years.
Photographs local wildlife.
Enjoys board games.
Appetite good; no indigestion.
Drives a car.
His roommate lives with psoriasis.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2005.
```

**A2-G57-C4**

Facts: peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]; myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]; patient: age = 66 (current) [line: "Current age 66 years."]

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Man, adult.
Suspected chest infection; assessed on the medical ward.
Drives a car.
Owns a bicycle.
Enjoys board games.
His roommate has a lazy eye.
Lives in a second-floor apartment.
Appetite good; no indigestion.
His roommate lives with psoriasis.
His friend has recovered from a dislocated finger.
Sleeps seven hours a night.
Photographs local wildlife.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Walks without calf pain.
Knits as a hobby.
In 2021, folate was 12 ng/mL.
In 2024, lipase was 30 U/L.
Has two cats.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2005.
Plays the piano.
Prefers morning appointments.
Sees a dentist yearly.
Current age 66 years.
```


## G58

Rule: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

**A2-G58-C1**

Facts: patient: heart rate = 100 (current) [line: "Heart rate now 100/min on a pulse check."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: eGFR = 41 (current) [line: "Current eGFR 41 mL/min/1.73 m2."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her friend has a lazy eye.
Lives in a second-floor apartment.
In 2012, folate was 12 ng/mL.
Heart rate now 100/min on a pulse check.
Teeth in good repair.
Plays the piano.
Knits as a hobby.
Cardiac stress test unremarkable last year.
Photographs local wildlife.
Her father wears contact lenses.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2012.
Enjoys board games.
Her friend has recovered from a dislocated finger.
Sleeps seven hours a night.
Prefers morning appointments.
Her father sprained a thumb last month.
Has two cats.
Pupils equal and reactive to light.
Current eGFR 41 mL/min/1.73 m2.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**A2-G58-C2**

Facts: patient: heart rate = 100 (current) [line: "Heart rate now 100/min on a pulse check."]; patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]; patient: eGFR = 41 (current) [line: "Current eGFR 41 mL/min/1.73 m2."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her friend has a lazy eye.
Lives in a second-floor apartment.
In 2012, folate was 12 ng/mL.
Heart rate now 100/min on a pulse check.
Teeth in good repair.
Plays the piano.
Knits as a hobby.
Known coronary artery disease (two-vessel disease on angiography).
Photographs local wildlife.
Her father wears contact lenses.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2012.
Enjoys board games.
Her friend has recovered from a dislocated finger.
Sleeps seven hours a night.
Prefers morning appointments.
Her father sprained a thumb last month.
Has two cats.
Pupils equal and reactive to light.
Current eGFR 41 mL/min/1.73 m2.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**A2-G58-C3**

Facts: patient: heart rate = 100 (current) [line: "Heart rate now 100/min on a pulse check."]; roommate: coronary artery disease present (current) [line: "Her roommate has known coronary artery disease."]; patient: eGFR = 41 (current) [line: "Current eGFR 41 mL/min/1.73 m2."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Woman of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her friend has a lazy eye.
Lives in a second-floor apartment.
In 2012, folate was 12 ng/mL.
Heart rate now 100/min on a pulse check.
Teeth in good repair.
Plays the piano.
Knits as a hobby.
Her roommate has known coronary artery disease.
Photographs local wildlife.
Her father wears contact lenses.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2012.
Enjoys board games.
Her friend has recovered from a dislocated finger.
Sleeps seven hours a night.
Prefers morning appointments.
Her father sprained a thumb last month.
Has two cats.
Pupils equal and reactive to light.
Current eGFR 41 mL/min/1.73 m2.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**A2-G58-C4**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; patient: heart rate = 100 (current) [line: "Current heart rate 100/min."]; patient: eGFR = 41 (current) [line: "eGFR now 41 mL/min/1.73 m2."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Female patient of 33 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Cardiac stress test unremarkable last year.
Her friend has recovered from a dislocated finger.
During a checkup in 2011, total protein was 7.0 g/dL.
Current heart rate 100/min.
Photographs local wildlife.
Prefers morning appointments.
Lives in a second-floor apartment.
Her friend has a lazy eye.
Has two cats.
Her father wears contact lenses.
eGFR now 41 mL/min/1.73 m2.
In 2012, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2012.
Her father sprained a thumb last month.
Sleeps seven hours a night.
Teeth in good repair.
Knits as a hobby.
Sees a dentist yearly.
Plays the piano.
Enjoys board games.
Pupils equal and reactive to light.
```


## G59

Rule: For newly diagnosed type 2 diabetes, start metformin. If the patient's current eGFR is below 45 mL/min/1.73 m2, start sitagliptin instead.

**A2-G59-C1**

Facts: patient: eGFR = 70 (current) [line: "Current eGFR 70 mL/min/1.73 m2."]

Claims: s = Start metformin. | s' = Start sitagliptin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Uses sunscreen in summer.
Current eGFR 70 mL/min/1.73 m2.
```

**A2-G59-C2**

Facts: patient: eGFR = 70 (current) [line: "eGFR now 70 mL/min/1.73 m2."]

Claims: s = Start metformin. | s' = Start sitagliptin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Female patient of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
eGFR now 70 mL/min/1.73 m2.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

**A2-G59-C3**

Facts: patient: eGFR = 36 (current) [line: "Current eGFR 36 mL/min/1.73 m2."]

Claims: s = Start metformin. | s' = Start sitagliptin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Uses sunscreen in summer.
Current eGFR 36 mL/min/1.73 m2.
```

**A2-G59-C4**

Facts: patient: eGFR = 45 (current) [line: "Current eGFR 45 mL/min/1.73 m2."]

Claims: s = Start metformin. | s' = Start sitagliptin.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
```
Woman of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Uses sunscreen in summer.
Current eGFR 45 mL/min/1.73 m2.
```


## G60

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**A2-G60-C1**

Facts: friend: myocardial infarction or peripheral artery disease present (current) [line: "Her friend has peripheral artery disease with leg pain."]; patient: temperature = 38.2 (current) [line: "Current temperature 38.2 C."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Woman of 33 years.
Sore throat for two days.
Prefers morning appointments.
Her friend has peripheral artery disease with leg pain.
Current temperature 38.2 C.
Her roommate burned a hand on a stove years ago.
Teeth in good repair.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
In 2020, lipase was 30 U/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Sees a dentist yearly.
Photographs local wildlife.
Her friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2023.
Her roommate sprained a thumb last month.
Drives a car.
Knits as a hobby.
Her friend has a lazy eye.
```

**A2-G60-C2**

Facts: myocardial infarction or peripheral artery disease: stated as unknown [line: "Myocardial infarction or peripheral artery disease: unknown."]; patient: temperature = 38.2 (current) [line: "Current temperature 38.2 C."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Woman of 33 years.
Sore throat for two days.
Prefers morning appointments.
Myocardial infarction or peripheral artery disease: unknown.
Current temperature 38.2 C.
Her roommate burned a hand on a stove years ago.
Teeth in good repair.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
In 2020, lipase was 30 U/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Sees a dentist yearly.
Photographs local wildlife.
Her friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2023.
Her roommate sprained a thumb last month.
Drives a car.
Knits as a hobby.
Her friend has a lazy eye.
```

**A2-G60-C3**

Facts: myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]; patient: temperature = 38.2 (current) [line: "Current temperature 38.2 C."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Woman of 33 years.
Sore throat for two days.
Prefers morning appointments.
Walks without calf pain.
Current temperature 38.2 C.
Her roommate burned a hand on a stove years ago.
Teeth in good repair.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
In 2020, lipase was 30 U/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Sees a dentist yearly.
Photographs local wildlife.
Her friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2023.
Her roommate sprained a thumb last month.
Drives a car.
Knits as a hobby.
Her friend has a lazy eye.
```

**A2-G60-C4**

Facts: patient: myocardial infarction or peripheral artery disease present (current) [line: "Has symptomatic peripheral artery disease of both legs."]; patient: temperature = 38.2 (current) [line: "Current temperature 38.2 C."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Woman of 33 years.
Sore throat for two days.
Prefers morning appointments.
Has symptomatic peripheral artery disease of both legs.
Current temperature 38.2 C.
Her roommate burned a hand on a stove years ago.
Teeth in good repair.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
In 2020, lipase was 30 U/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Sees a dentist yearly.
Photographs local wildlife.
Her friend lives with psoriasis.
Free T4 of 1.2 ng/dL in 2023.
Her roommate sprained a thumb last month.
Drives a car.
Knits as a hobby.
Her friend has a lazy eye.
```

**A2-G60-C5**

Facts: patient: temperature = 38.2 (current) [line: "Temperature now 38.2 C (tympanic)."]; myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Female patient of 33 years.
Sore throat for two days.
In 2020, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2023.
Sees a dentist yearly.
Her friend has a lazy eye.
Temperature now 38.2 C (tympanic).
Her friend lives with psoriasis.
Her roommate burned a hand on a stove years ago.
Teeth in good repair.
Her roommate sprained a thumb last month.
Walks without calf pain.
Drives a car.
Photographs local wildlife.
Prefers morning appointments.
Knits as a hobby.
Pupils equal and reactive to light.
During a checkup in 2012, total protein was 7.0 g/dL.
Lives in a second-floor apartment.
```


## G61

Rule: For newly diagnosed rheumatoid arthritis, prescribe methotrexate. If the current ALT is above 40 U/L, prescribe hydroxychloroquine instead.

**A2-G61-C1**

Facts: patient: ALT = 201 (past (2005)) [line: "Records from 2005 list ALT at 201 U/L."]; patient: ALT = 17 (current) [line: "Current ALT 17 U/L."]

Claims: s = Prescribe methotrexate. | s' = Prescribe hydroxychloroquine.

Criterion claims: s = Under the rule, the condition "ALT above 40" does not hold for this patient. | s' = Under the rule, the condition "ALT above 40" holds for this patient.
```
Female patient of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Teeth in good repair.
Sleeps seven hours a night.
Owns a bicycle.
Records from 2005 list ALT at 201 U/L.
Current ALT 17 U/L.
```

**A2-G61-C2**

Facts: patient: ALT = 10 (past (2005)) [line: "Records from 2005 list ALT at 10 U/L."]; patient: ALT = 47 (current) [line: "Current ALT 47 U/L."]

Claims: s = Prescribe methotrexate. | s' = Prescribe hydroxychloroquine.

Criterion claims: s = Under the rule, the condition "ALT above 40" does not hold for this patient. | s' = Under the rule, the condition "ALT above 40" holds for this patient.
```
Female patient of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Teeth in good repair.
Sleeps seven hours a night.
Owns a bicycle.
Records from 2005 list ALT at 10 U/L.
Current ALT 47 U/L.
```

**A2-G61-C3**

Facts: patient: ALT = 10 (past (2005)) [line: "Records from 2005 list ALT at 10 U/L."]; patient: ALT = 17 (current) [line: "Current ALT 17 U/L."]

Claims: s = Prescribe methotrexate. | s' = Prescribe hydroxychloroquine.

Criterion claims: s = Under the rule, the condition "ALT above 40" does not hold for this patient. | s' = Under the rule, the condition "ALT above 40" holds for this patient.
```
Female patient of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Teeth in good repair.
Sleeps seven hours a night.
Owns a bicycle.
Records from 2005 list ALT at 10 U/L.
Current ALT 17 U/L.
```

**A2-G61-C4**

Facts: patient: ALT = 10 (past (2005)) [line: "Back in 2005, ALT stood at 10 U/L."]; patient: ALT = 17 (current) [line: "ALT now 17 U/L."]

Claims: s = Prescribe methotrexate. | s' = Prescribe hydroxychloroquine.

Criterion claims: s = Under the rule, the condition "ALT above 40" does not hold for this patient. | s' = Under the rule, the condition "ALT above 40" holds for this patient.
```
Woman of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Owns a bicycle.
Back in 2005, ALT stood at 10 U/L.
ALT now 17 U/L.
Sleeps seven hours a night.
Teeth in good repair.
```


## G62

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

**A2-G62-C1**

Facts: patient: heart rate = 103 (current) [line: "Current heart rate 103/min."]; patient: heart rate = 76 (past (2016)) [line: "Records from 2016 list heart rate at 76/min."]; patient: serum potassium = 3.9 (current) [line: "Latest potassium result: 3.9 mmol/L."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 67 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Prefers morning appointments.
Her roommate burned a hand on a stove years ago.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Current heart rate 103/min.
Records from 2016 list heart rate at 76/min.
Sleeps seven hours a night.
Sees a dentist yearly.
Teeth in good repair.
Her roommate has a lazy eye.
Knits as a hobby.
Her sister has recovered from a dislocated finger.
In 2013, folate was 12 ng/mL.
Latest potassium result: 3.9 mmol/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Her sister lives with psoriasis.
```

**A2-G62-C2**

Facts: patient: heart rate = 77 (current) [line: "Current heart rate 77/min."]; patient: heart rate = 76 (past (2016)) [line: "Records from 2016 list heart rate at 76/min."]; patient: serum potassium = 3.9 (current) [line: "Latest potassium result: 3.9 mmol/L."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 67 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Prefers morning appointments.
Her roommate burned a hand on a stove years ago.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Current heart rate 77/min.
Records from 2016 list heart rate at 76/min.
Sleeps seven hours a night.
Sees a dentist yearly.
Teeth in good repair.
Her roommate has a lazy eye.
Knits as a hobby.
Her sister has recovered from a dislocated finger.
In 2013, folate was 12 ng/mL.
Latest potassium result: 3.9 mmol/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Her sister lives with psoriasis.
```

**A2-G62-C3**

Facts: patient: heart rate = 77 (current) [line: "Current heart rate 77/min."]; patient: heart rate = 98 (past (2016)) [line: "Records from 2016 list heart rate at 98/min."]; patient: serum potassium = 3.9 (current) [line: "Latest potassium result: 3.9 mmol/L."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 67 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Prefers morning appointments.
Her roommate burned a hand on a stove years ago.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Current heart rate 77/min.
Records from 2016 list heart rate at 98/min.
Sleeps seven hours a night.
Sees a dentist yearly.
Teeth in good repair.
Her roommate has a lazy eye.
Knits as a hobby.
Her sister has recovered from a dislocated finger.
In 2013, folate was 12 ng/mL.
Latest potassium result: 3.9 mmol/L.
During a checkup in 2012, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Her sister lives with psoriasis.
```

**A2-G62-C4**

Facts: patient: heart rate = 77 (current) [line: "Heart rate now 77/min on a pulse check."]; patient: serum potassium = 3.9 (current) [line: "Current serum potassium 3.9 mmol/L."]; patient: heart rate = 76 (past (2016)) [line: "Back in 2016, heart rate stood at 76/min."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Female patient of 67 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
During a checkup in 2022, free T3 was 3.2 pg/mL.
In 2013, folate was 12 ng/mL.
Prefers morning appointments.
Her sister lives with psoriasis.
Heart rate now 77/min on a pulse check.
Current serum potassium 3.9 mmol/L.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
During a checkup in 2012, total protein was 7.0 g/dL.
Her roommate has a lazy eye.
Back in 2016, heart rate stood at 76/min.
Teeth in good repair.
Her sister has recovered from a dislocated finger.
Knits as a hobby.
Lives in a second-floor apartment.
Her roommate burned a hand on a stove years ago.
Sees a dentist yearly.
```


## G63

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).

**A2-G63-C1**

Facts: patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]; patient: age = 78 (current) [line: "Currently aged 78 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Woman, adult.
Requests contraception.
Teeth in good repair.
Zinc of 85 mcg/dL in 2011.
Free T4 of 1.2 ng/dL in 2011.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Has metastatic lung cancer, receiving palliative treatment.
Her wife has recovered from a dislocated finger.
In 2009, folate was 12 ng/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Enjoys board games.
Sleeps seven hours a night.
In 2006, lipase was 30 U/L.
Drives a car.
Her friend sprained a thumb last month.
Currently aged 78 years.
Has two cats.
Her friend wears contact lenses.
```

**A2-G63-C2**

Facts: patient: cancer denied by name (current) [line: "Free of cancer throughout life."]; patient: age = 78 (current) [line: "Currently aged 78 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Woman, adult.
Requests contraception.
Teeth in good repair.
Zinc of 85 mcg/dL in 2011.
Free T4 of 1.2 ng/dL in 2011.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Free of cancer throughout life.
Her wife has recovered from a dislocated finger.
In 2009, folate was 12 ng/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Enjoys board games.
Sleeps seven hours a night.
In 2006, lipase was 30 U/L.
Drives a car.
Her friend sprained a thumb last month.
Currently aged 78 years.
Has two cats.
Her friend wears contact lenses.
```

**A2-G63-C3**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]; patient: age = 78 (current) [line: "Currently aged 78 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Woman, adult.
Requests contraception.
Teeth in good repair.
Zinc of 85 mcg/dL in 2011.
Free T4 of 1.2 ng/dL in 2011.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Oncology follow-up: none.
Her wife has recovered from a dislocated finger.
In 2009, folate was 12 ng/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Enjoys board games.
Sleeps seven hours a night.
In 2006, lipase was 30 U/L.
Drives a car.
Her friend sprained a thumb last month.
Currently aged 78 years.
Has two cats.
Her friend wears contact lenses.
```

**A2-G63-C4**

Facts: cancer: stated as unknown [line: "Cancer at any time: status unclear from the records at hand."]; patient: age = 78 (current) [line: "Currently aged 78 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
Woman, adult.
Requests contraception.
Teeth in good repair.
Zinc of 85 mcg/dL in 2011.
Free T4 of 1.2 ng/dL in 2011.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Cancer at any time: status unclear from the records at hand.
Her wife has recovered from a dislocated finger.
In 2009, folate was 12 ng/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Enjoys board games.
Sleeps seven hours a night.
In 2006, lipase was 30 U/L.
Drives a car.
Her friend sprained a thumb last month.
Currently aged 78 years.
Has two cats.
Her friend wears contact lenses.
```

**A2-G63-C5**

Facts: patient: age = 78 (current) [line: "Current age 78 years."]; cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
```
An adult woman.
Requests contraception.
Sleeps seven hours a night.
Her wife has recovered from a dislocated finger.
Current age 78 years.
In 2006, lipase was 30 U/L.
Teeth in good repair.
Her friend sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2011.
Uses sunscreen in summer.
Oncology follow-up: none.
Her friend wears contact lenses.
Enjoys board games.
Drives a car.
In 2009, folate was 12 ng/mL.
Has two cats.
Paints watercolors as a hobby.
Owns a bicycle.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2011.
Her friend burned a hand on a stove years ago.
```


## G64

Rule: For type 2 diabetes above target on metformin, prescribe pioglitazone. If the patient has ever had heart failure (current or past), prescribe empagliflozin instead.

**A2-G64-C1**

Facts: heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]

Claims: s = Prescribe pioglitazone. | s' = Prescribe empagliflozin.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Male patient of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Drives a car.
Uses sunscreen in summer.
Has two cats.
Sleeps flat on one pillow.
```

**A2-G64-C2**

Facts: patient: heart failure present (current) [line: "Has heart failure, treated with diuretics."]

Claims: s = Prescribe pioglitazone. | s' = Prescribe empagliflozin.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Male patient of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Drives a car.
Uses sunscreen in summer.
Has two cats.
Has heart failure, treated with diuretics.
```

**A2-G64-C3**

Facts: patient: heart failure denied by name (current) [line: "Has never had heart failure."]

Claims: s = Prescribe pioglitazone. | s' = Prescribe empagliflozin.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Male patient of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Drives a car.
Uses sunscreen in summer.
Has two cats.
Has never had heart failure.
```

**A2-G64-C4**

Facts: heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]

Claims: s = Prescribe pioglitazone. | s' = Prescribe empagliflozin.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
```
Man of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Sleeps flat on one pillow.
Has two cats.
Drives a car.
Uses sunscreen in summer.
```


## G65

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient is allergic to penicillin and the current heart rate is above 90/min, prescribe nitrofurantoin instead.

**A2-G65-C1**

Facts: patient: penicillin allergy present (current) [line: "Known penicillin allergy with angioedema."]; patient: heart rate = 90 (current) [line: "Heart rate now 90/min on a pulse check."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Female patient of 41 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Known penicillin allergy with angioedema.
Has two cats.
Her wife has a lazy eye.
Free T4 of 1.2 ng/dL in 2021.
During a checkup in 2005, total protein was 7.0 g/dL.
Zinc of 85 mcg/dL in 2018.
Enjoys board games.
Pupils equal and reactive to light.
Sees a dentist yearly.
Drives a car.
Heart rate now 90/min on a pulse check.
Her wife sprained a thumb last month.
Lives in a second-floor apartment.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Owns a bicycle.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
```

**A2-G65-C2**

Facts: patient: penicillin allergy present (current) [line: "Known penicillin allergy with angioedema."]; patient: heart rate = 80 (current) [line: "Heart rate now 80/min on a pulse check."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Female patient of 41 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Known penicillin allergy with angioedema.
Has two cats.
Her wife has a lazy eye.
Free T4 of 1.2 ng/dL in 2021.
During a checkup in 2005, total protein was 7.0 g/dL.
Zinc of 85 mcg/dL in 2018.
Enjoys board games.
Pupils equal and reactive to light.
Sees a dentist yearly.
Drives a car.
Heart rate now 80/min on a pulse check.
Her wife sprained a thumb last month.
Lives in a second-floor apartment.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Owns a bicycle.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
```

**A2-G65-C3**

Facts: patient: heart rate = 80 (current) [line: "Current heart rate 80/min."]; patient: penicillin allergy present (current) [line: "Known penicillin allergy with angioedema."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 41 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Prefers morning appointments.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2021.
Her wife has a lazy eye.
Enjoys board games.
Has two cats.
During a checkup in 2005, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Current heart rate 80/min.
Drives a car.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2018.
Her wife sprained a thumb last month.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Known penicillin allergy with angioedema.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Plays the piano.
```

**A2-G65-C4**

Facts: patient: penicillin allergy present (current) [line: "Known penicillin allergy with angioedema."]; patient: heart rate = 104 (current) [line: "Heart rate now 104/min on a pulse check."]

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Female patient of 41 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Known penicillin allergy with angioedema.
Has two cats.
Her wife has a lazy eye.
Free T4 of 1.2 ng/dL in 2021.
During a checkup in 2005, total protein was 7.0 g/dL.
Zinc of 85 mcg/dL in 2018.
Enjoys board games.
Pupils equal and reactive to light.
Sees a dentist yearly.
Drives a car.
Heart rate now 104/min on a pulse check.
Her wife sprained a thumb last month.
Lives in a second-floor apartment.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
Owns a bicycle.
Paints watercolors as a hobby.
Prefers morning appointments.
Plays the piano.
```


## G66

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**A2-G66-C1**

Facts: patient: weight = 89 (current) [line: "Latest weight 89 kg."]; patient: age = 70 (current) [line: "Current age 70 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Latest weight 89 kg.
Lives in a second-floor apartment.
Current age 70 years.
Plays the piano.
```

**A2-G66-C2**

Facts: patient: weight = 89 (current) [line: "Current weight 89 kg."]; patient: age = 70 (current) [line: "Currently aged 70 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current weight 89 kg.
Plays the piano.
Lives in a second-floor apartment.
Currently aged 70 years.
```

**A2-G66-C3**

Facts: patient: weight = 61 (current) [line: "Current weight 61 kg."]; patient: age = 70 (current) [line: "Currently aged 70 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current weight 61 kg.
Plays the piano.
Lives in a second-floor apartment.
Currently aged 70 years.
```

**A2-G66-C4**

Facts: patient: weight = 60 (current) [line: "Current weight 60 kg."]; patient: age = 70 (current) [line: "Currently aged 70 years."]

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current weight 60 kg.
Plays the piano.
Lives in a second-floor apartment.
Currently aged 70 years.
```


## G67

Rule: For inpatient VTE prophylaxis, use enoxaparin. If the current platelet count is below 100 x10^9/L, use intermittent pneumatic compression instead.

**A2-G67-C1**

Facts: patient: platelet count = 106 (current) [line: "Current platelet count 106 x10^9/L."]

Claims: s = Use enoxaparin. | s' = Use intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "platelet count below 100" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 100" holds for this patient.
```
Male patient of 42 years.
Admitted for community-acquired pneumonia; immobile.
Uses sunscreen in summer.
Current platelet count 106 x10^9/L.
```

**A2-G67-C2**

Facts: patient: platelet count = 173 (current) [line: "Current platelet count 173 x10^9/L."]

Claims: s = Use enoxaparin. | s' = Use intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "platelet count below 100" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 100" holds for this patient.
```
Male patient of 42 years.
Admitted for community-acquired pneumonia; immobile.
Uses sunscreen in summer.
Current platelet count 173 x10^9/L.
```

**A2-G67-C3**

Facts: patient: platelet count = 58 (current) [line: "Current platelet count 58 x10^9/L."]

Claims: s = Use enoxaparin. | s' = Use intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "platelet count below 100" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 100" holds for this patient.
```
Male patient of 42 years.
Admitted for community-acquired pneumonia; immobile.
Uses sunscreen in summer.
Current platelet count 58 x10^9/L.
```

**A2-G67-C4**

Facts: patient: platelet count = 173 (current) [line: "Platelet count now 173 x10^9/L."]

Claims: s = Use enoxaparin. | s' = Use intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "platelet count below 100" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 100" holds for this patient.
```
Man of 42 years.
Admitted for community-acquired pneumonia; immobile.
Platelet count now 173 x10^9/L.
Uses sunscreen in summer.
```


## G68

Rule: Alvarado score (as used here, partial): 2 points for current tenderness in the right lower quadrant (right iliac fossa); 2 points for a current white cell count above 10.0 x10^9/L; 1 point for a current temperature of 37.3 C or more. Other Alvarado items are not part of this question.

**A2-G68-C1**

Facts: patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; patient: white cell count = 8.0 (current) [line: "Latest WBC is 8.0 x10^9/L."]; right lower quadrant tenderness: not named; a general line implies absence (counts as absent) [line: "Abdominal examination unremarkable, without tenderness."]

Claims: s = The white cell count criterion contributes 0 points. | s' = The white cell count criterion contributes 2 points.
```
Woman of 27 years.
Abdominal pain for one day; assessed in the emergency department.
Current temperature 36.8 C.
Latest WBC is 8.0 x10^9/L.
Abdominal examination unremarkable, without tenderness.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

**A2-G68-C2**

Facts: patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; patient: white cell count = 11.7 (current) [line: "Latest WBC is 11.7 x10^9/L."]; right lower quadrant tenderness: not named; a general line implies absence (counts as absent) [line: "Abdominal examination unremarkable, without tenderness."]

Claims: s = The white cell count criterion contributes 0 points. | s' = The white cell count criterion contributes 2 points.
```
Woman of 27 years.
Abdominal pain for one day; assessed in the emergency department.
Current temperature 36.8 C.
Latest WBC is 11.7 x10^9/L.
Abdominal examination unremarkable, without tenderness.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

**A2-G68-C3**

Facts: patient: white cell count = 8.0 (current) [line: "Current white cell count 8.0 x10^9/L."]; right lower quadrant tenderness: not named; a general line implies absence (counts as absent) [line: "Abdominal examination unremarkable, without tenderness."]; patient: temperature = 36.8 (current) [line: "Temperature now 36.8 C (tympanic)."]

Claims: s = The white cell count criterion contributes 0 points. | s' = The white cell count criterion contributes 2 points.
```
Female patient of 27 years.
Abdominal pain for one day; assessed in the emergency department.
Sleeps seven hours a night.
Plays the piano.
Current white cell count 8.0 x10^9/L.
Abdominal examination unremarkable, without tenderness.
Temperature now 36.8 C (tympanic).
Uses sunscreen in summer.
```

**A2-G68-C4**

Facts: patient: temperature = 36.8 (current) [line: "Current temperature 36.8 C."]; patient: white cell count = 10.0 (current) [line: "Latest WBC is 10.0 x10^9/L."]; right lower quadrant tenderness: not named; a general line implies absence (counts as absent) [line: "Abdominal examination unremarkable, without tenderness."]

Claims: s = The white cell count criterion contributes 0 points. | s' = The white cell count criterion contributes 2 points.
```
Woman of 27 years.
Abdominal pain for one day; assessed in the emergency department.
Current temperature 36.8 C.
Latest WBC is 10.0 x10^9/L.
Abdominal examination unremarkable, without tenderness.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```


## G69

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.

**A2-G69-C1**

Facts: patient: heart rate = 71 (current) [line: "Current heart rate 71/min."]; patient: weight = 61 (current) [line: "Latest weight 61 kg."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
Latest weight 61 kg.
```

**A2-G69-C2**

Facts: patient: heart rate = 71 (current) [line: "Current heart rate 71/min."]; weight: not mentioned (unknown)

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
```

**A2-G69-C3**

Facts: patient: heart rate = 71 (current) [line: "Current heart rate 71/min."]; patient: weight = 94 (current) [line: "Latest weight 94 kg."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
Latest weight 94 kg.
```

**A2-G69-C4**

Facts: patient: heart rate = 71 (current) [line: "Current heart rate 71/min."]; patient: weight = 56 (current) [line: "Latest weight 56 kg."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
Latest weight 56 kg.
```

**A2-G69-C5**

Facts: patient: weight = 94 (current) [line: "Current weight 94 kg."]; patient: heart rate = 71 (current) [line: "Heart rate now 71/min on a pulse check."]

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Teeth in good repair.
Current weight 94 kg.
Paints watercolors as a hobby.
Heart rate now 71/min on a pulse check.
```


## G70

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**A2-G70-C1**

Facts: patient: ALT = 29 (current) [line: "Current ALT 29 U/L."]; patient: ALT = 223 (past (2008)) [line: "Back in 2008, ALT stood at 223 U/L."]

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Female patient of 62 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Current ALT 29 U/L.
Knits as a hobby.
Paints watercolors as a hobby.
Back in 2008, ALT stood at 223 U/L.
```

**A2-G70-C2**

Facts: patient: ALT = 29 (current) [line: "Current ALT 29 U/L."]; patient: ALT = 27 (past (2008)) [line: "Back in 2008, ALT stood at 27 U/L."]

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Female patient of 62 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Current ALT 29 U/L.
Knits as a hobby.
Paints watercolors as a hobby.
Back in 2008, ALT stood at 27 U/L.
```

**A2-G70-C3**

Facts: patient: ALT = 27 (past (2008)) [line: "Records from 2008 list ALT at 27 U/L."]; patient: ALT = 29 (current) [line: "ALT now 29 U/L."]

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Woman of 62 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Records from 2008 list ALT at 27 U/L.
ALT now 29 U/L.
Lives in a second-floor apartment.
Knits as a hobby.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
```

**A2-G70-C4**

Facts: patient: ALT = 101 (current) [line: "Current ALT 101 U/L."]; patient: ALT = 27 (past (2008)) [line: "Back in 2008, ALT stood at 27 U/L."]

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Female patient of 62 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Current ALT 101 U/L.
Knits as a hobby.
Paints watercolors as a hobby.
Back in 2008, ALT stood at 27 U/L.
```


## G71

Rule: Charlson Comorbidity Index (as used here, partial): 1 point for heart failure at any time (current or past); 1 point for a myocardial infarction or peripheral artery disease at any time (current or past); 1 point for current asthma; 2 points for a current serum creatinine above 2.0 mg/dL. Age and other Charlson items are not part of this question.

**A2-G71-C1**

Facts: asthma: not named; a general line implies absence (counts as absent) [line: "Inhaler use: none."]; patient: serum creatinine = 0.8 (current) [line: "Current serum creatinine 0.8 mg/dL."]; heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]; myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

Claims: s = The serum creatinine criterion contributes 0 points. | s' = The serum creatinine criterion contributes 2 points.
```
Man of 70 years.
Inpatient on the medical ward; comorbidity review.
Inhaler use: none.
Current serum creatinine 0.8 mg/dL.
Has two cats.
Sleeps seven hours a night.
Drives a car.
Owns a bicycle.
Sleeps flat on one pillow.
```

**A2-G71-C2**

Facts: asthma: not named; a general line implies absence (counts as absent) [line: "Inhaler use: none."]; patient: serum creatinine = 2.0 (current) [line: "Current serum creatinine 2.0 mg/dL."]; heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]; myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

Claims: s = The serum creatinine criterion contributes 0 points. | s' = The serum creatinine criterion contributes 2 points.
```
Man of 70 years.
Inpatient on the medical ward; comorbidity review.
Inhaler use: none.
Current serum creatinine 2.0 mg/dL.
Has two cats.
Sleeps seven hours a night.
Drives a car.
Owns a bicycle.
Sleeps flat on one pillow.
```

**A2-G71-C3**

Facts: asthma: not named; a general line implies absence (counts as absent) [line: "Inhaler use: none."]; patient: serum creatinine = 0.8 (current) [line: "Latest creatinine result: 0.8 mg/dL."]; heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]; myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

Claims: s = The serum creatinine criterion contributes 0 points. | s' = The serum creatinine criterion contributes 2 points.
```
Male patient of 70 years.
Inpatient on the medical ward; comorbidity review.
Has two cats.
Inhaler use: none.
Latest creatinine result: 0.8 mg/dL.
Owns a bicycle.
Sleeps seven hours a night.
Drives a car.
Sleeps flat on one pillow.
```

**A2-G71-C4**

Facts: asthma: not named; a general line implies absence (counts as absent) [line: "Inhaler use: none."]; patient: serum creatinine = 2.4 (current) [line: "Current serum creatinine 2.4 mg/dL."]; heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]; myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

Claims: s = The serum creatinine criterion contributes 0 points. | s' = The serum creatinine criterion contributes 2 points.
```
Man of 70 years.
Inpatient on the medical ward; comorbidity review.
Inhaler use: none.
Current serum creatinine 2.4 mg/dL.
Has two cats.
Sleeps seven hours a night.
Drives a car.
Owns a bicycle.
Sleeps flat on one pillow.
```


## G72

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the current weight is 60 kg or less; the patient currently has heart failure.

**A2-G72-C1**

Facts: patient: weight = 80 (current) [line: "Latest weight 80 kg."]; patient: heart failure present (current) [line: "Has heart failure, treated with diuretics."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Male patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Latest weight 80 kg.
Has heart failure, treated with diuretics.
Coagulation tests normal on recent bloodwork.
```

**A2-G72-C2**

Facts: patient: heart failure present (current) [line: "Has heart failure, treated with diuretics."]; venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]; patient: weight = 80 (current) [line: "Current weight 80 kg."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Man of 50 years.
Atrial fibrillation; anticoagulation indicated.
Has heart failure, treated with diuretics.
Coagulation tests normal on recent bloodwork.
Prefers to be addressed by first name.
Current weight 80 kg.
```

**A2-G72-C3**

Facts: patient: weight = 80 (current) [line: "Latest weight 80 kg."]; patient: heart failure present (current) [line: "Has heart failure, treated with diuretics."]; patient: venous thromboembolism denied by name (current) [line: "Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Male patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Latest weight 80 kg.
Has heart failure, treated with diuretics.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**A2-G72-C4**

Facts: patient: weight = 80 (current) [line: "Latest weight 80 kg."]; patient: heart failure present (current) [line: "Has heart failure, treated with diuretics."]; father: venous thromboembolism present (past) [line: "His father had a DVT years ago."]

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
```
Male patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Latest weight 80 kg.
Has heart failure, treated with diuretics.
His father had a DVT years ago.
```


## G73

Rule: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 20 mg/dL or more. Age, sex and other items of the index are not part of this question.

**A2-G73-C1**

Facts: stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen 15 mg/dL on the current labs."]; patient: blood urea nitrogen = 13 (past (2018)) [line: "Back in 2018, blood urea nitrogen stood at 13 mg/dL."]; patient: arterial pH = 7.40 (current) [line: "Latest arterial blood gas shows a pH of 7.40."]; heart failure: not mentioned (counts as absent)

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 20 points.
```
Man of 59 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Prefers to be addressed by first name.
Gait normal; no focal weakness.
Weight steady over the past year.
Blood urea nitrogen 15 mg/dL on the current labs.
Sleeps seven hours a night.
Back in 2018, blood urea nitrogen stood at 13 mg/dL.
Latest arterial blood gas shows a pH of 7.40.
```

**A2-G73-C2**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen now: 15 mg/dL."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; patient: arterial pH = 7.40 (current) [line: "Current arterial pH 7.40."]; patient: blood urea nitrogen = 13 (past (2018)) [line: "Records from 2018 list blood urea nitrogen at 13 mg/dL."]; heart failure: not mentioned (counts as absent)

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 20 points.
```
Male patient of 59 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Weight steady over the past year.
Sleeps seven hours a night.
Blood urea nitrogen now: 15 mg/dL.
Gait normal; no focal weakness.
Current arterial pH 7.40.
Prefers to be addressed by first name.
Records from 2018 list blood urea nitrogen at 13 mg/dL.
```

**A2-G73-C3**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: blood urea nitrogen = 15 (current) [line: "Blood urea nitrogen now: 15 mg/dL."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; patient: arterial pH = 7.40 (current) [line: "Current arterial pH 7.40."]; patient: blood urea nitrogen = 32 (past (2018)) [line: "Records from 2018 list blood urea nitrogen at 32 mg/dL."]; heart failure: not mentioned (counts as absent)

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 20 points.
```
Male patient of 59 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Weight steady over the past year.
Sleeps seven hours a night.
Blood urea nitrogen now: 15 mg/dL.
Gait normal; no focal weakness.
Current arterial pH 7.40.
Prefers to be addressed by first name.
Records from 2018 list blood urea nitrogen at 32 mg/dL.
```

**A2-G73-C4**

Facts: cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]; patient: blood urea nitrogen = 21 (current) [line: "Blood urea nitrogen now: 21 mg/dL."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; patient: arterial pH = 7.40 (current) [line: "Current arterial pH 7.40."]; patient: blood urea nitrogen = 13 (past (2018)) [line: "Records from 2018 list blood urea nitrogen at 13 mg/dL."]; heart failure: not mentioned (counts as absent)

Claims: s = The blood urea nitrogen criterion contributes 0 points. | s' = The blood urea nitrogen criterion contributes 20 points.
```
Male patient of 59 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Weight steady over the past year.
Sleeps seven hours a night.
Blood urea nitrogen now: 21 mg/dL.
Gait normal; no focal weakness.
Current arterial pH 7.40.
Prefers to be addressed by first name.
Records from 2018 list blood urea nitrogen at 13 mg/dL.
```


## G74

Rule: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.

**A2-G74-C1**

Facts: patient: creatinine = 0.7 (current) [line: "Current serum creatinine 0.7 mg/dL."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; heart failure: not mentioned (counts as absent)

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Man of 81 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 0.7 mg/dL.
Gait normal; no focal weakness.
Cardiac stress test unremarkable last year.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```

**A2-G74-C2**

Facts: patient: creatinine = 1.7 (current) [line: "Current serum creatinine 1.7 mg/dL."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; heart failure: not mentioned (counts as absent)

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Man of 81 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 1.7 mg/dL.
Gait normal; no focal weakness.
Cardiac stress test unremarkable last year.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```

**A2-G74-C3**

Facts: coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; patient: creatinine = 0.7 (current) [line: "Latest creatinine result: 0.7 mg/dL."]; heart failure: not mentioned (counts as absent)

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Male patient of 81 years.
Preoperative assessment before elective colectomy.
Cardiac stress test unremarkable last year.
Gait normal; no focal weakness.
Prefers to be addressed by first name.
Latest creatinine result: 0.7 mg/dL.
Sleeps seven hours a night.
```

**A2-G74-C4**

Facts: patient: creatinine = 1.5 (current) [line: "Current serum creatinine 1.5 mg/dL."]; stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Gait normal; no focal weakness."]; coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]; heart failure: not mentioned (counts as absent)

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Man of 81 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 1.5 mg/dL.
Gait normal; no focal weakness.
Cardiac stress test unremarkable last year.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```


## G75

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).

**A2-G75-C1**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 87 (current) [line: "Current age 87 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "age at least 75" does not hold for this patient. | s' = Under the rule, the condition "age at least 75" holds for this patient.
```
An adult woman.
Requests contraception.
Prefers morning appointments.
Sees a dentist yearly.
Has two cats.
Drives a car.
Photographs local wildlife.
Uses sunscreen in summer.
In 2007, lipase was 30 U/L.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Has melanoma skin cancer and is receiving treatment for it.
Her friend burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2008.
Owns a bicycle.
Her wife has recovered from a dislocated finger.
Knits as a hobby.
Pupils equal and reactive to light.
Current age 87 years.
Her wife has a lazy eye.
Teeth in good repair.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```

**A2-G75-C2**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; heart failure: not mentioned (counts as absent); age: not mentioned (unknown)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "age at least 75" does not hold for this patient. | s' = Under the rule, the condition "age at least 75" holds for this patient.
```
An adult woman.
Requests contraception.
Prefers morning appointments.
Sees a dentist yearly.
Has two cats.
Drives a car.
Photographs local wildlife.
Uses sunscreen in summer.
In 2007, lipase was 30 U/L.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Has melanoma skin cancer and is receiving treatment for it.
Her friend burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2008.
Owns a bicycle.
Her wife has recovered from a dislocated finger.
Knits as a hobby.
Pupils equal and reactive to light.
Her wife has a lazy eye.
Teeth in good repair.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```

**A2-G75-C3**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 61 (current) [line: "Current age 61 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "age at least 75" does not hold for this patient. | s' = Under the rule, the condition "age at least 75" holds for this patient.
```
An adult woman.
Requests contraception.
Prefers morning appointments.
Sees a dentist yearly.
Has two cats.
Drives a car.
Photographs local wildlife.
Uses sunscreen in summer.
In 2007, lipase was 30 U/L.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Has melanoma skin cancer and is receiving treatment for it.
Her friend burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2008.
Owns a bicycle.
Her wife has recovered from a dislocated finger.
Knits as a hobby.
Pupils equal and reactive to light.
Current age 61 years.
Her wife has a lazy eye.
Teeth in good repair.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```

**A2-G75-C4**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 61 (current) [line: "Currently aged 61 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "age at least 75" does not hold for this patient. | s' = Under the rule, the condition "age at least 75" holds for this patient.
```
Woman, adult.
Requests contraception.
Zinc of 85 mcg/dL in 2008.
Lives in a second-floor apartment.
Has melanoma skin cancer and is receiving treatment for it.
Sleeps seven hours a night.
Sees a dentist yearly.
Currently aged 61 years.
Prefers morning appointments.
Uses sunscreen in summer.
Has two cats.
Her wife has a lazy eye.
Teeth in good repair.
Her friend burned a hand on a stove years ago.
Photographs local wildlife.
In 2007, lipase was 30 U/L.
Her wife has recovered from a dislocated finger.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Owns a bicycle.
Drives a car.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Knits as a hobby.
```

**A2-G75-C5**

Facts: patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]; patient: age = 74 (current) [line: "Current age 74 years."]; heart failure: not mentioned (counts as absent)

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "age at least 75" does not hold for this patient. | s' = Under the rule, the condition "age at least 75" holds for this patient.
```
An adult woman.
Requests contraception.
Prefers morning appointments.
Sees a dentist yearly.
Has two cats.
Drives a car.
Photographs local wildlife.
Uses sunscreen in summer.
In 2007, lipase was 30 U/L.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Has melanoma skin cancer and is receiving treatment for it.
Her friend burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2008.
Owns a bicycle.
Her wife has recovered from a dislocated finger.
Knits as a hobby.
Pupils equal and reactive to light.
Current age 74 years.
Her wife has a lazy eye.
Teeth in good repair.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```
