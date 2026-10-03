# Rendering-fidelity sheets (H1): 300 groups, 75 per author

Read each case against the facts listed under it. (1) Does the text state exactly these facts, no more and no fewer? (2) Is the correct claim unambiguous under the rule text? Record y/n in your CSV, with a problem type (dropped negation, wrong subject, ambiguous time, conflicting measurement, omitted exception, wording, other) and a note. Save it as `audit/fidelity_<name>.csv`.


## author1 / group 1: `rule_v1.test.inv012.c1.time.easy.721`

Rule: For Quorin syndrome, prescribe ostravin. If the patient has active cancer or the patient has ever had heart failure (current or past), prescribe dalmerol instead.

**base** (program answer: s; facts: patient: heart failure; absent; current | patient: active cancer; absent; current)
```
Male patient of 29 years.
Referred with Quorin syndrome.
Sleeps flat on one pillow.
Teeth in good repair.
Weight steady over the past year.
```

**flip** (program answer: s'; facts: patient: heart failure; absent; current | patient: active cancer; present; current)
```
Male patient of 29 years.
Referred with Quorin syndrome.
Sleeps flat on one pillow.
Teeth in good repair.
Has melanoma skin cancer and is receiving treatment for it.
```

**near** (program answer: s; facts: patient: heart failure; absent; current | patient: active cancer; present; past (2017))
```
Male patient of 29 years.
Referred with Quorin syndrome.
Sleeps flat on one pillow.
Teeth in good repair.
Formerly had kidney cancer, cured by surgery in 2017.
```

**pres** (program answer: s; facts: patient: active cancer; absent; current | patient: heart failure; absent; current)
```
Man of 29 years.
Referred with Quorin syndrome.
Weight steady over the past year.
Teeth in good repair.
Sleeps flat on one pillow.
```


## author2 / group 2: `rule_v1.test.gs147.c3.negation.easy.1300`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 1 point if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 1 point if the patient has had cancer at any time (active or in remission); 2 points if the patient has ever had heart failure (current or past). If the score is 3 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; past | patient: systolic blood pressure = 127; present; current)
```
Female patient of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Had diabetes years ago that went into remission on a low-calorie diet.
Uses sunscreen in summer.
Observations now: blood pressure 127/85 mmHg.
```

**flip** (program answer: s'; facts: patient: diabetes (patient or first-degree relative); present; past | patient: cancer at any time; present; current | patient: systolic blood pressure = 127; present; current)
```
Female patient of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Had diabetes years ago that went into remission on a low-calorie diet.
Uses sunscreen in summer.
Has metastatic lung cancer, receiving palliative treatment.
Observations now: blood pressure 127/85 mmHg.
```

**near** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; past | patient: cancer at any time; absent; current | patient: systolic blood pressure = 127; present; current)
```
Female patient of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Had diabetes years ago that went into remission on a low-calorie diet.
Uses sunscreen in summer.
Free of cancer throughout life.
Observations now: blood pressure 127/85 mmHg.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; past | patient: systolic blood pressure = 127; present; current)
```
Woman of 22 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Uses sunscreen in summer.
Had diabetes years ago that went into remission on a low-calorie diet.
Current systolic blood pressure 127 mmHg.
```


## author3 / group 3: `rule_v1.test.gs196.c2.time.easy.309`

Rule: For musculoskeletal pain, prescribe ibuprofen. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time and the patient is allergic to penicillin, prescribe acetaminophen instead.

**base** (program answer: s; facts: father: coronary artery disease (patient or first-degree relative); present; current)
```
Female patient of 56 years.
Acute low back pain after lifting.
Lives in a second-floor apartment.
Drives a car.
Her father has known coronary artery disease.
Knits as a hobby.
Prefers to be addressed by first name.
```

**flip** (program answer: s'; facts: father: coronary artery disease (patient or first-degree relative); present; current | patient: penicillin allergy; present; current)
```
Female patient of 56 years.
Acute low back pain after lifting.
Lives in a second-floor apartment.
Drives a car.
Her father has known coronary artery disease.
Knits as a hobby.
Prefers to be addressed by first name.
Known penicillin allergy with angioedema.
```

**near** (program answer: s; facts: father: coronary artery disease (patient or first-degree relative); present; current | patient: penicillin allergy; present; past (2021))
```
Female patient of 56 years.
Acute low back pain after lifting.
Lives in a second-floor apartment.
Drives a car.
Her father has known coronary artery disease.
Knits as a hobby.
Prefers to be addressed by first name.
Outgrew a penicillin allergy by 2021.
```

**pres** (program answer: s; facts: father: coronary artery disease (patient or first-degree relative); present; current)
```
Woman of 56 years.
Acute low back pain after lifting.
Drives a car.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Knits as a hobby.
Her father has known coronary artery disease.
```

**missing** (program answer: neither; facts: father: coronary artery disease (patient or first-degree relative); present; current | patient: penicillin allergy; unknown; current)
```
Female patient of 56 years.
Acute low back pain after lifting.
Lives in a second-floor apartment.
Drives a car.
Her father has known coronary artery disease.
Knits as a hobby.
Prefers to be addressed by first name.
Penicillin allergy: status unclear from the records at hand.
```


## author4 / group 4: `rule_v1.test.gs137.c1.subject.long.128`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: serum creatinine = 1.5; present; current)
```
Female patient of 53 years.
Hip osteoarthritis with pain on walking.
Her roommate has recovered from a dislocated finger.
Prefers morning appointments.
During a checkup in 2013, total protein was 7.0 g/dL.
Teeth in good repair.
Owns a bicycle.
Sleeps seven hours a night.
Free T4 of 1.2 ng/dL in 2005.
Her sister wears contact lenses.
Lives in a second-floor apartment.
Her roommate lives with psoriasis.
In 2009, lipase was 30 U/L.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Current serum creatinine 1.5 mg/dL.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Her friend has a lazy eye.
```

**flip** (program answer: s'; facts: patient: diabetes; present; past | patient: serum creatinine = 1.5; present; current)
```
Female patient of 53 years.
Hip osteoarthritis with pain on walking.
Her roommate has recovered from a dislocated finger.
Prefers morning appointments.
During a checkup in 2013, total protein was 7.0 g/dL.
Teeth in good repair.
Owns a bicycle.
Sleeps seven hours a night.
Had diabetes years ago that went into remission on a low-calorie diet.
Free T4 of 1.2 ng/dL in 2005.
Her sister wears contact lenses.
Lives in a second-floor apartment.
Her roommate lives with psoriasis.
In 2009, lipase was 30 U/L.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Current serum creatinine 1.5 mg/dL.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Her friend has a lazy eye.
```

**near** (program answer: s; facts: friend: diabetes; present; past | patient: serum creatinine = 1.5; present; current)
```
Female patient of 53 years.
Hip osteoarthritis with pain on walking.
Her roommate has recovered from a dislocated finger.
Prefers morning appointments.
During a checkup in 2013, total protein was 7.0 g/dL.
Teeth in good repair.
Owns a bicycle.
Sleeps seven hours a night.
Her friend was diabetic until bariatric surgery several years ago.
Free T4 of 1.2 ng/dL in 2005.
Her sister wears contact lenses.
Lives in a second-floor apartment.
Her roommate lives with psoriasis.
In 2009, lipase was 30 U/L.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Current serum creatinine 1.5 mg/dL.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Her friend has a lazy eye.
```

**pres** (program answer: s; facts: patient: serum creatinine = 1.5; present; current)
```
Woman of 53 years.
Hip osteoarthritis with pain on walking.
Teeth in good repair.
In 2009, lipase was 30 U/L.
Her sister wears contact lenses.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Her friend has a lazy eye.
Her roommate lives with psoriasis.
Owns a bicycle.
Her roommate has recovered from a dislocated finger.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2005.
Latest creatinine result: 1.5 mg/dL.
Prefers morning appointments.
During a checkup in 2013, total protein was 7.0 g/dL.
```


## author1 / group 5: `rule_v1.test.inv030.c1.boundary.easy.303`

Rule: For Hestin disease, prescribe melcadine. If the current white cell count is above 12.0 x10^9/L, prescribe orvitrex instead.

**base** (program answer: s; facts: patient: white cell count = 7.8; present; current)
```
Man of 43 years.
Referred with Hestin disease.
Owns a bicycle.
Latest WBC is 7.8 x10^9/L.
Drives a car.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: white cell count = 13.4; present; current)
```
Man of 43 years.
Referred with Hestin disease.
Owns a bicycle.
Latest WBC is 13.4 x10^9/L.
Drives a car.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: patient: white cell count = 12.0; present; current)
```
Man of 43 years.
Referred with Hestin disease.
Owns a bicycle.
Latest WBC is 12.0 x10^9/L.
Drives a car.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: white cell count = 7.8; present; current)
```
Male patient of 43 years.
Referred with Hestin disease.
Owns a bicycle.
Uses sunscreen in summer.
Current white cell count 7.8 x10^9/L.
Drives a car.
```


## author2 / group 6: `rule_v1.test.gs080.c1.time.long.248`

Rule: For an acute gout flare, prescribe colchicine. If the patient is currently taking warfarin, prescribe prednisone instead.

**base** (program answer: s; facts: patient: warfarin; absent; current)
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

**flip** (program answer: s'; facts: patient: warfarin; present; current)
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

**near** (program answer: s; facts: patient: warfarin; present; past)
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

**pres** (program answer: s; facts: patient: warfarin; absent; current)
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


## author3 / group 7: `rule_v1.test.gs209.c3.boundary.long.1886`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**base** (program answer: s; facts: patient: heart rate = 82; present; current | patient: peptic ulcer at any time; present; current | patient: age = 60; present; current)
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Knits as a hobby.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her sister wears contact lenses.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Her sister has recovered from a dislocated finger.
Heart rate now 82/min on a pulse check.
Drives a car.
Enjoys board games.
Active peptic ulcer disease.
Teeth in good repair.
Uses sunscreen in summer.
Currently aged 60 years.
Her roommate has a lazy eye.
Plays the piano.
Her wife sprained a thumb last month.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Owns a bicycle.
In 2014, lipase was 30 U/L.
```

**flip** (program answer: s'; facts: patient: heart rate = 97; present; current | patient: peptic ulcer at any time; present; current | patient: age = 60; present; current)
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Knits as a hobby.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her sister wears contact lenses.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Her sister has recovered from a dislocated finger.
Heart rate now 97/min on a pulse check.
Drives a car.
Enjoys board games.
Active peptic ulcer disease.
Teeth in good repair.
Uses sunscreen in summer.
Currently aged 60 years.
Her roommate has a lazy eye.
Plays the piano.
Her wife sprained a thumb last month.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Owns a bicycle.
In 2014, lipase was 30 U/L.
```

**near** (program answer: s; facts: patient: heart rate = 90; present; current | patient: peptic ulcer at any time; present; current | patient: age = 60; present; current)
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Knits as a hobby.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her sister wears contact lenses.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Her sister has recovered from a dislocated finger.
Heart rate now 90/min on a pulse check.
Drives a car.
Enjoys board games.
Active peptic ulcer disease.
Teeth in good repair.
Uses sunscreen in summer.
Currently aged 60 years.
Her roommate has a lazy eye.
Plays the piano.
Her wife sprained a thumb last month.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Owns a bicycle.
In 2014, lipase was 30 U/L.
```

**pres** (program answer: s; facts: patient: heart rate = 82; present; current | patient: peptic ulcer at any time; present; current | patient: age = 60; present; current)
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sleeps seven hours a night.
Her sister wears contact lenses.
Teeth in good repair.
Lives in a second-floor apartment.
Enjoys board games.
In 2014, lipase was 30 U/L.
Current heart rate 82/min.
Paints watercolors as a hobby.
Drives a car.
Photographs local wildlife.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Active peptic ulcer disease.
Plays the piano.
Owns a bicycle.
Knits as a hobby.
Her roommate has a lazy eye.
Her wife sprained a thumb last month.
Her sister has recovered from a dislocated finger.
Current age 60 years.
Pupils equal and reactive to light.
Sees a dentist yearly.
```


## author4 / group 8: `rule_v1.test.gs123.c2.negation.long.268`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

**base** (program answer: s; facts: patient: serum potassium = 5.4; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Female patient of 43 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sees a dentist yearly.
Paints watercolors as a hobby.
Drives a car.
Latest potassium result: 5.4 mmol/L.
Zinc of 85 mcg/dL in 2007.
Pupils equal and reactive to light.
Her roommate has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Owns a bicycle.
Her friend has recovered from a dislocated finger.
Her wife lives with psoriasis.
Random glucose 92 mg/dL.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2012.
In 2023, folate was 12 ng/mL.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her uncle wears contact lenses.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: serum potassium = 5.4; present; current | patient: diabetes (patient or first-degree relative); present; past (2014))
```
Female patient of 43 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sees a dentist yearly.
Paints watercolors as a hobby.
Drives a car.
Latest potassium result: 5.4 mmol/L.
Zinc of 85 mcg/dL in 2007.
Pupils equal and reactive to light.
Her roommate has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Owns a bicycle.
Her friend has recovered from a dislocated finger.
Her wife lives with psoriasis.
Formerly diabetic; in remission since 2014.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2012.
In 2023, folate was 12 ng/mL.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her uncle wears contact lenses.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: serum potassium = 5.4; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Female patient of 43 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sees a dentist yearly.
Paints watercolors as a hobby.
Drives a car.
Latest potassium result: 5.4 mmol/L.
Zinc of 85 mcg/dL in 2007.
Pupils equal and reactive to light.
Her roommate has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Owns a bicycle.
Her friend has recovered from a dislocated finger.
Her wife lives with psoriasis.
Has never had diabetes.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2012.
In 2023, folate was 12 ng/mL.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her uncle wears contact lenses.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: serum potassium = 5.4; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 43 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Zinc of 85 mcg/dL in 2007.
Current serum potassium 5.4 mmol/L.
In 2023, folate was 12 ng/mL.
Drives a car.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Her wife lives with psoriasis.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Her uncle wears contact lenses.
Sleeps seven hours a night.
Random glucose 92 mg/dL.
During a checkup in 2005, total protein was 7.0 g/dL.
Owns a bicycle.
Prefers morning appointments.
Her roommate has a lazy eye.
Sees a dentist yearly.
Her friend has recovered from a dislocated finger.
Free T4 of 1.2 ng/dL in 2012.
```


## author1 / group 9: `rule_v1.test.inv053.c1.boundary.easy.180`

Rule: For Varnell syndrome, prescribe lorvatide. If the current temperature is above 38.0 C and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe pemraxin instead.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; past (2014) | patient: temperature = 37.4; present; current)
```
Female patient of 71 years.
Referred with Varnell syndrome.
Recovered from a pulmonary embolism in 2014.
Temperature now 37.4 C (tympanic).
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); present; past (2014) | patient: temperature = 38.8; present; current)
```
Female patient of 71 years.
Referred with Varnell syndrome.
Recovered from a pulmonary embolism in 2014.
Temperature now 38.8 C (tympanic).
Teeth in good repair.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; past (2014) | patient: temperature = 38.0; present; current)
```
Female patient of 71 years.
Referred with Varnell syndrome.
Recovered from a pulmonary embolism in 2014.
Temperature now 38.0 C (tympanic).
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: temperature = 37.4; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2014))
```
Woman of 71 years.
Referred with Varnell syndrome.
Current temperature 37.4 C.
Recovered from a pulmonary embolism in 2014.
Teeth in good repair.
```


## author2 / group 10: `rule_v1.test.inv058.c1.time.easy.217`

Rule: For Quorin syndrome, prescribe ostravin. If at least two of the following apply, prescribe dalmerol instead: the current weight is 60 kg or less; the current eGFR is below 50 mL/min/1.73 m2; the current ALT is above 120 U/L.

**base** (program answer: s; facts: patient: eGFR = 76; present; current | patient: weight = 90; present; past (2019) | patient: ALT = 143; present; current | patient: weight = 85; present; current)
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

**flip** (program answer: s'; facts: patient: eGFR = 76; present; current | patient: weight = 90; present; past (2019) | patient: ALT = 143; present; current | patient: weight = 57; present; current)
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

**near** (program answer: s; facts: patient: eGFR = 76; present; current | patient: weight = 49; present; past (2019) | patient: ALT = 143; present; current | patient: weight = 85; present; current)
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

**pres** (program answer: s; facts: patient: ALT = 143; present; current | patient: eGFR = 76; present; current | patient: weight = 85; present; current | patient: weight = 90; present; past (2019))
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


## author3 / group 11: `rule_v1.test.statin_alt.alt.numeric.alt.136`

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**base** (program answer: s; facts: patient: ALT = 37; present; current)
```
Man of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Current ALT 37 U/L.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: ALT = 116; present; current)
```
Man of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Current ALT 116 U/L.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: ALT = 73; present; current)
```
Man of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Current ALT 73 U/L.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: ALT = 37; present; current)
```
Male patient of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Lives in a second-floor apartment.
ALT now 37 U/L.
```


## author4 / group 12: `rule_v1.test.inv000.c2.numeric.easy.796`

Rule: For Pallis disease, prescribe brexadol. Score 2 points if the patient has ever had heparin-induced thrombocytopenia (current or past); 1 point if the current calf swelling compared with the other leg is 3.0 cm or more; 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time. If the score is 5 or more, prescribe corlitane instead.

**base** (program answer: s; facts: patient: calf swelling = 0.3; present; current | patient: diabetes (patient or first-degree relative); present; past | patient: heparin-induced thrombocytopenia; present; past (2019))
```
Female patient of 47 years.
Referred with Pallis disease.
Photographs local wildlife.
Paints watercolors as a hobby.
Difference in calf circumference now 0.3 cm.
Owns a bicycle.
Had diabetes years ago that went into remission on a low-calorie diet.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2019; blood counts recovered afterward.
```

**flip** (program answer: s'; facts: patient: calf swelling = 5.2; present; current | patient: diabetes (patient or first-degree relative); present; past | patient: heparin-induced thrombocytopenia; present; past (2019))
```
Female patient of 47 years.
Referred with Pallis disease.
Photographs local wildlife.
Paints watercolors as a hobby.
Difference in calf circumference now 5.2 cm.
Owns a bicycle.
Had diabetes years ago that went into remission on a low-calorie diet.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2019; blood counts recovered afterward.
```

**near** (program answer: s; facts: patient: calf swelling = 2.6; present; current | patient: diabetes (patient or first-degree relative); present; past | patient: heparin-induced thrombocytopenia; present; past (2019))
```
Female patient of 47 years.
Referred with Pallis disease.
Photographs local wildlife.
Paints watercolors as a hobby.
Difference in calf circumference now 2.6 cm.
Owns a bicycle.
Had diabetes years ago that went into remission on a low-calorie diet.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2019; blood counts recovered afterward.
```

**pres** (program answer: s; facts: patient: calf swelling = 0.3; present; current | patient: heparin-induced thrombocytopenia; present; past (2019) | patient: diabetes (patient or first-degree relative); present; past)
```
Woman of 47 years.
Referred with Pallis disease.
Photographs local wildlife.
Current calf swelling 0.3 cm compared with the other leg.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2019; blood counts recovered afterward.
Owns a bicycle.
Had diabetes years ago that went into remission on a low-calorie diet.
Paints watercolors as a hobby.
```


## author1 / group 13: `rule_v1.test.gs150.c1.boundary.long.614`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current blood urea nitrogen is above 19 mg/dL or the patient has active cancer, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: blood urea nitrogen = 10; present; current)
```
Woman of 79 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Prefers morning appointments.
Owns a bicycle.
Oncology follow-up: none.
Photographs local wildlife.
Plays the piano.
Drives a car.
Lives in a second-floor apartment.
Teeth in good repair.
Her sister has a lazy eye.
Her sister wears contact lenses.
Zinc of 85 mcg/dL in 2017.
Blood urea nitrogen 10 mg/dL on the current labs.
Has two cats.
```

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: blood urea nitrogen = 29; present; current)
```
Woman of 79 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Prefers morning appointments.
Owns a bicycle.
Oncology follow-up: none.
Photographs local wildlife.
Plays the piano.
Drives a car.
Lives in a second-floor apartment.
Teeth in good repair.
Her sister has a lazy eye.
Her sister wears contact lenses.
Zinc of 85 mcg/dL in 2017.
Blood urea nitrogen 29 mg/dL on the current labs.
Has two cats.
```

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: blood urea nitrogen = 19; present; current)
```
Woman of 79 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Prefers morning appointments.
Owns a bicycle.
Oncology follow-up: none.
Photographs local wildlife.
Plays the piano.
Drives a car.
Lives in a second-floor apartment.
Teeth in good repair.
Her sister has a lazy eye.
Her sister wears contact lenses.
Zinc of 85 mcg/dL in 2017.
Blood urea nitrogen 19 mg/dL on the current labs.
Has two cats.
```

**pres** (program answer: s; facts: patient: blood urea nitrogen = 10; present; current | patient: active cancer; absent; current)
```
Female patient of 79 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Knits as a hobby.
Blood urea nitrogen now: 10 mg/dL.
Owns a bicycle.
Teeth in good repair.
Zinc of 85 mcg/dL in 2017.
Photographs local wildlife.
Oncology follow-up: none.
Her sister has a lazy eye.
Lives in a second-floor apartment.
Her sister wears contact lenses.
Sleeps seven hours a night.
Free T4 of 1.2 ng/dL in 2013.
Prefers morning appointments.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Drives a car.
Plays the piano.
Has two cats.
```


## author2 / group 14: `rule_v1.test.gs022.c1.numeric.easy.686`

Rule: For an acute gout flare, prescribe colchicine. If the current eGFR is below 45 mL/min/1.73 m2, prescribe prednisone instead.

**base** (program answer: s; facts: patient: eGFR = 71; present; current)
```
Female patient of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Photographs local wildlife.
Enjoys board games.
Prefers to be addressed by first name.
eGFR now 71 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: eGFR = 36; present; current)
```
Female patient of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Photographs local wildlife.
Enjoys board games.
Prefers to be addressed by first name.
eGFR now 36 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: eGFR = 47; present; current)
```
Female patient of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Photographs local wildlife.
Enjoys board games.
Prefers to be addressed by first name.
eGFR now 47 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: eGFR = 71; present; current)
```
Woman of 85 years.
Acute gout flare of the right first metatarsophalangeal joint.
Enjoys board games.
Current eGFR 71 mL/min/1.73 m2.
Prefers to be addressed by first name.
Photographs local wildlife.
```


## author3 / group 15: `rule_v1.test.gs157.c2.boundary.long.73`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has ever had heart failure (current or past); the current platelet count is below 50 x10^9/L; the current temperature is above 38.0 C.

**base** (program answer: s; facts: patient: heart failure; present; current | patient: temperature = 36.5; present; current | patient: platelet count = 245; present; current)
```
Man of 30 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current heart failure with ankle swelling.
His father burned a hand on a stove years ago.
During a checkup in 2019, total protein was 7.0 g/dL.
Current temperature 36.5 C.
Prefers to be addressed by first name.
Photographs local wildlife.
Drives a car.
Sleeps seven hours a night.
Sees a dentist yearly.
Uses sunscreen in summer.
In 2014, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2014.
Teeth in good repair.
His friend sprained a thumb last month.
Prefers morning appointments.
Platelet count now 245 x10^9/L.
Zinc of 85 mcg/dL in 2024.
Owns a bicycle.
His uncle has a lazy eye.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: heart failure; present; current | patient: temperature = 36.5; present; current | patient: platelet count = 41; present; current)
```
Man of 30 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current heart failure with ankle swelling.
His father burned a hand on a stove years ago.
During a checkup in 2019, total protein was 7.0 g/dL.
Current temperature 36.5 C.
Prefers to be addressed by first name.
Photographs local wildlife.
Drives a car.
Sleeps seven hours a night.
Sees a dentist yearly.
Uses sunscreen in summer.
In 2014, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2014.
Teeth in good repair.
His friend sprained a thumb last month.
Prefers morning appointments.
Platelet count now 41 x10^9/L.
Zinc of 85 mcg/dL in 2024.
Owns a bicycle.
His uncle has a lazy eye.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: heart failure; present; current | patient: temperature = 36.5; present; current | patient: platelet count = 50; present; current)
```
Man of 30 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current heart failure with ankle swelling.
His father burned a hand on a stove years ago.
During a checkup in 2019, total protein was 7.0 g/dL.
Current temperature 36.5 C.
Prefers to be addressed by first name.
Photographs local wildlife.
Drives a car.
Sleeps seven hours a night.
Sees a dentist yearly.
Uses sunscreen in summer.
In 2014, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2014.
Teeth in good repair.
His friend sprained a thumb last month.
Prefers morning appointments.
Platelet count now 50 x10^9/L.
Zinc of 85 mcg/dL in 2024.
Owns a bicycle.
His uncle has a lazy eye.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: heart failure; present; current | patient: platelet count = 245; present; current | patient: temperature = 36.5; present; current)
```
Male patient of 30 years.
Community-acquired pneumonia confirmed on chest radiograph.
Uses sunscreen in summer.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Owns a bicycle.
Prefers morning appointments.
In 2014, lipase was 30 U/L.
Knits as a hobby.
Prefers to be addressed by first name.
His uncle has a lazy eye.
Drives a car.
Current heart failure with ankle swelling.
His father burned a hand on a stove years ago.
Sees a dentist yearly.
Teeth in good repair.
Zinc of 85 mcg/dL in 2024.
Current platelet count 245 x10^9/L.
Temperature now 36.5 C (tympanic).
Free T4 of 1.2 ng/dL in 2014.
Photographs local wildlife.
During a checkup in 2019, total protein was 7.0 g/dL.
```

**missing** (program answer: neither; facts: patient: heart failure; present; current | patient: temperature = 36.5; present; current)
```
Man of 30 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current heart failure with ankle swelling.
His father burned a hand on a stove years ago.
During a checkup in 2019, total protein was 7.0 g/dL.
Current temperature 36.5 C.
Prefers to be addressed by first name.
Photographs local wildlife.
Drives a car.
Sleeps seven hours a night.
Sees a dentist yearly.
Uses sunscreen in summer.
In 2014, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2014.
Teeth in good repair.
His friend sprained a thumb last month.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2024.
Owns a bicycle.
His uncle has a lazy eye.
Knits as a hobby.
```


## author4 / group 16: `rule_v1.test.gs209.c3.numeric.easy.1864`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**base** (program answer: s; facts: patient: heart rate = 65; present; current | patient: peptic ulcer at any time; present; past | patient: age = 61; present; current)
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Heart rate now 65/min on a pulse check.
Duodenal ulcer years ago; recovered fully with treatment.
Currently aged 61 years.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: heart rate = 101; present; current | patient: peptic ulcer at any time; present; past | patient: age = 61; present; current)
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Heart rate now 101/min on a pulse check.
Duodenal ulcer years ago; recovered fully with treatment.
Currently aged 61 years.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: heart rate = 87; present; current | patient: peptic ulcer at any time; present; past | patient: age = 61; present; current)
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Heart rate now 87/min on a pulse check.
Duodenal ulcer years ago; recovered fully with treatment.
Currently aged 61 years.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: heart rate = 65; present; current | patient: peptic ulcer at any time; present; past | patient: age = 61; present; current)
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current heart rate 65/min.
Prefers morning appointments.
Duodenal ulcer years ago; recovered fully with treatment.
Current age 61 years.
```


## author1 / group 17: `rule_v1.test.gs188.c1.subject.long.396`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: ALT = 136; present; current | patient: peptic ulcer at any time; absent; current | patient: venous thromboembolism; absent; current)
```
Female patient of 18 years.
Spreading redness and warmth of the right shin for two days.
Her sister has recovered from a dislocated finger.
ALT now 136 U/L.
Enjoys board games.
Prefers to be addressed by first name.
Drives a car.
Paints watercolors as a hobby.
Plays the piano.
Owns a bicycle.
Appetite good; no indigestion.
Knits as a hobby.
Pupils equal and reactive to light.
During a checkup in 2024, total protein was 7.0 g/dL.
Her father lives with psoriasis.
In 2024, folate was 12 ng/mL.
Prefers morning appointments.
In 2024, lipase was 30 U/L.
Lives in a second-floor apartment.
Photographs local wildlife.
Coagulation tests normal on recent bloodwork.
Zinc of 85 mcg/dL in 2024.
Sleeps seven hours a night.
Has two cats.
```

**flip** (program answer: s'; facts: patient: ALT = 136; present; current | patient: peptic ulcer at any time; present; current | patient: venous thromboembolism; absent; current)
```
Female patient of 18 years.
Spreading redness and warmth of the right shin for two days.
Her sister has recovered from a dislocated finger.
ALT now 136 U/L.
Enjoys board games.
Prefers to be addressed by first name.
Drives a car.
Paints watercolors as a hobby.
Plays the piano.
Owns a bicycle.
Active peptic ulcer disease.
Knits as a hobby.
Pupils equal and reactive to light.
During a checkup in 2024, total protein was 7.0 g/dL.
Her father lives with psoriasis.
In 2024, folate was 12 ng/mL.
Prefers morning appointments.
In 2024, lipase was 30 U/L.
Lives in a second-floor apartment.
Photographs local wildlife.
Coagulation tests normal on recent bloodwork.
Zinc of 85 mcg/dL in 2024.
Sleeps seven hours a night.
Has two cats.
```

**near** (program answer: s; facts: patient: ALT = 136; present; current | sister: peptic ulcer at any time; present; current | patient: venous thromboembolism; absent; current)
```
Female patient of 18 years.
Spreading redness and warmth of the right shin for two days.
Her sister has recovered from a dislocated finger.
ALT now 136 U/L.
Enjoys board games.
Prefers to be addressed by first name.
Drives a car.
Paints watercolors as a hobby.
Plays the piano.
Owns a bicycle.
Her sister has peptic ulcer disease.
Knits as a hobby.
Pupils equal and reactive to light.
During a checkup in 2024, total protein was 7.0 g/dL.
Her father lives with psoriasis.
In 2024, folate was 12 ng/mL.
Prefers morning appointments.
In 2024, lipase was 30 U/L.
Lives in a second-floor apartment.
Photographs local wildlife.
Coagulation tests normal on recent bloodwork.
Zinc of 85 mcg/dL in 2024.
Sleeps seven hours a night.
Has two cats.
```

**pres** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: peptic ulcer at any time; absent; current | patient: ALT = 136; present; current)
```
Woman of 18 years.
Spreading redness and warmth of the right shin for two days.
Has two cats.
In 2024, lipase was 30 U/L.
Zinc of 85 mcg/dL in 2024.
Owns a bicycle.
In 2024, folate was 12 ng/mL.
Coagulation tests normal on recent bloodwork.
Enjoys board games.
Appetite good; no indigestion.
Photographs local wildlife.
Plays the piano.
Her father lives with psoriasis.
Lives in a second-floor apartment.
Drives a car.
During a checkup in 2024, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Her sister has recovered from a dislocated finger.
Current ALT 136 U/L.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Prefers morning appointments.
Knits as a hobby.
Sleeps seven hours a night.
```


## author2 / group 18: `rule_v1.test.gs021.c1.boundary.easy.605`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the current systolic blood pressure is above 160 mmHg or the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 142; present; current | patient: serum creatinine = 1.5; present; current)
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Observations now: blood pressure 142/93 mmHg.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 167; present; current | patient: serum creatinine = 1.5; present; current)
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Observations now: blood pressure 167/107 mmHg.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 160; present; current | patient: serum creatinine = 1.5; present; current)
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Observations now: blood pressure 160/103 mmHg.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 142; present; current | patient: serum creatinine = 1.5; present; current)
```
Man of 65 years.
Hip osteoarthritis with pain on walking.
Current systolic blood pressure 142 mmHg.
Current serum creatinine 1.5 mg/dL.
Knits as a hobby.
Lives in a second-floor apartment.
```

**missing** (program answer: neither; facts: patient: serum creatinine = 1.5; present; current)
```
Male patient of 65 years.
Hip osteoarthritis with pain on walking.
Lives in a second-floor apartment.
Latest creatinine result: 1.5 mg/dL.
Knits as a hobby.
```


## author3 / group 19: `rule_v1.test.gs249.c1.negation.easy.1667`

Rule: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient has an active peptic ulcer, prescribe doxycycline instead.

**base** (program answer: s; facts: patient: active peptic ulcer; present; current)
```
Man of 76 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Owns a bicycle.
Sleeps seven hours a night.
Has two cats.
Active peptic ulcer disease.
```

**flip** (program answer: s'; facts: patient: colorectal cancer (patient or first-degree relative); present; current | patient: active peptic ulcer; present; current)
```
Man of 76 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Colorectal cancer under active treatment.
Owns a bicycle.
Sleeps seven hours a night.
Has two cats.
Active peptic ulcer disease.
```

**near** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: active peptic ulcer; present; current)
```
Man of 76 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Has never had bowel cancer.
Owns a bicycle.
Sleeps seven hours a night.
Has two cats.
Active peptic ulcer disease.
```

**pres** (program answer: s; facts: patient: active peptic ulcer; present; current)
```
Male patient of 76 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Active peptic ulcer disease.
Has two cats.
Sleeps seven hours a night.
Owns a bicycle.
```


## author4 / group 20: `rule_v1.test.s3_aims65.ams.negation.easy.1763`

Rule: AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.

**base** (program answer: s; facts: patient: age = 42; present; current | patient: systolic blood pressure = 118; present; current | patient: international normalized ratio = 1.0; present; current)
```
An adult man.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Owns a bicycle.
Current age 42 years.
Current systolic blood pressure 118 mmHg.
Latest international normalized ratio (INR): 1.0.
```

**flip** (program answer: s'; facts: patient: age = 42; present; current | patient: systolic blood pressure = 118; present; current | patient: international normalized ratio = 1.0; present; current | patient: altered mental status; present; current)
```
An adult man.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Owns a bicycle.
Current age 42 years.
Current systolic blood pressure 118 mmHg.
Latest international normalized ratio (INR): 1.0.
Newly disoriented and unable to give a clear history.
```

**near** (program answer: s; facts: patient: age = 42; present; current | patient: systolic blood pressure = 118; present; current | patient: international normalized ratio = 1.0; present; current | patient: altered mental status; absent; current)
```
An adult man.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Owns a bicycle.
Current age 42 years.
Current systolic blood pressure 118 mmHg.
Latest international normalized ratio (INR): 1.0.
Confusion absent; answers questions appropriately.
```

**pres** (program answer: s; facts: patient: international normalized ratio = 1.0; present; current | patient: age = 42; present; current | patient: systolic blood pressure = 118; present; current)
```
Man, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Current international normalized ratio 1.0.
Owns a bicycle.
Currently aged 42 years.
Observations now: blood pressure 118/80 mmHg.
```


## author1 / group 21: `rule_v1.test.all_gastro.age.numeric.easy.973`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient is aged 65 years or more and the patient is currently taking aspirin, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: aspirin use; present; current | patient: age = 45; present; current)
```
Woman, adult.
Hip osteoarthritis with pain on walking.
Plays the piano.
Currently on low-dose aspirin each day.
Current age 45 years.
```

**flip** (program answer: s'; facts: patient: aspirin use; present; current | patient: age = 65; present; current)
```
Woman, adult.
Hip osteoarthritis with pain on walking.
Plays the piano.
Currently on low-dose aspirin each day.
Current age 65 years.
```

**near** (program answer: s; facts: patient: aspirin use; present; current | patient: age = 62; present; current)
```
Woman, adult.
Hip osteoarthritis with pain on walking.
Plays the piano.
Currently on low-dose aspirin each day.
Current age 62 years.
```

**pres** (program answer: s; facts: patient: aspirin use; present; current | patient: age = 45; present; current)
```
An adult woman.
Hip osteoarthritis with pain on walking.
Currently on low-dose aspirin each day.
Plays the piano.
Currently aged 45 years.
```


## author2 / group 22: `rule_v1.test.gs246.c1.boundary.long.82`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: angioedema; present; past | patient: white cell count = 4.8; present; current)
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

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: angioedema; present; past | patient: white cell count = 13.6; present; current)
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

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: angioedema; present; past | patient: white cell count = 12.0; present; current)
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

**pres** (program answer: s; facts: patient: angioedema; present; past | patient: active cancer; absent; current | patient: white cell count = 4.8; present; current)
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


## author3 / group 23: `rule_v1.test.gs073.c1.time.easy.129`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the current eGFR is below 50 mL/min/1.73 m2, prescribe fondaparinux instead.

**base** (program answer: s; facts: patient: eGFR = 68; present; past (2016) | patient: eGFR = 55; present; current)
```
Woman of 85 years.
First day after elective total hip replacement.
Paints watercolors as a hobby.
Back in 2016, eGFR stood at 68 mL/min/1.73 m2.
Teeth in good repair.
eGFR now 55 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: eGFR = 68; present; past (2016) | patient: eGFR = 49; present; current)
```
Woman of 85 years.
First day after elective total hip replacement.
Paints watercolors as a hobby.
Back in 2016, eGFR stood at 68 mL/min/1.73 m2.
Teeth in good repair.
eGFR now 49 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: eGFR = 41; present; past (2016) | patient: eGFR = 55; present; current)
```
Woman of 85 years.
First day after elective total hip replacement.
Paints watercolors as a hobby.
Back in 2016, eGFR stood at 41 mL/min/1.73 m2.
Teeth in good repair.
eGFR now 55 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: eGFR = 55; present; current | patient: eGFR = 68; present; past (2016))
```
Female patient of 85 years.
First day after elective total hip replacement.
Current eGFR 55 mL/min/1.73 m2.
Paints watercolors as a hobby.
Records from 2016 list eGFR at 68 mL/min/1.73 m2.
Teeth in good repair.
```


## author4 / group 24: `rule_v1.test.cut_bleed.bleed.subject.long.789`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. Score 2 points for a major bleeding event at any time; 1 point for age 75 years or more; 1 point for a current eGFR below 30 mL/min/1.73 m2. If the score is 2 or more, prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: age = 79; present; current | patient: bleeding history; absent; current | patient: eGFR = 64; present; current)
```
Woman, adult.
Recovering on the ward after a myocardial infarction treated with a stent.
Currently aged 79 years.
Plays the piano.
Her sister sprained a thumb last month.
Her wife has recovered from a dislocated finger.
In 2011, folate was 12 ng/mL.
Paints watercolors as a hobby.
Prefers morning appointments.
Owns a bicycle.
Drives a car.
Examination shows no signs of blood loss.
Free T4 of 1.2 ng/dL in 2016.
Uses sunscreen in summer.
Current eGFR 64 mL/min/1.73 m2.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Knits as a hobby.
Sees a dentist yearly.
During a checkup in 2020, total protein was 7.0 g/dL.
```

**flip** (program answer: s'; facts: patient: age = 79; present; current | patient: bleeding history; present; current | patient: eGFR = 64; present; current)
```
Woman, adult.
Recovering on the ward after a myocardial infarction treated with a stent.
Currently aged 79 years.
Plays the piano.
Her sister sprained a thumb last month.
Her wife has recovered from a dislocated finger.
In 2011, folate was 12 ng/mL.
Paints watercolors as a hobby.
Prefers morning appointments.
Owns a bicycle.
Drives a car.
Currently has a major bleed from a duodenal ulcer, with transfusion under way.
Free T4 of 1.2 ng/dL in 2016.
Uses sunscreen in summer.
Current eGFR 64 mL/min/1.73 m2.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Knits as a hobby.
Sees a dentist yearly.
During a checkup in 2020, total protein was 7.0 g/dL.
```

**near** (program answer: s; facts: patient: age = 79; present; current | friend: bleeding history; present; current | patient: eGFR = 64; present; current)
```
Woman, adult.
Recovering on the ward after a myocardial infarction treated with a stent.
Currently aged 79 years.
Plays the piano.
Her sister sprained a thumb last month.
Her wife has recovered from a dislocated finger.
In 2011, folate was 12 ng/mL.
Paints watercolors as a hobby.
Prefers morning appointments.
Owns a bicycle.
Drives a car.
Her friend has major bleeding from the bowel at present.
Free T4 of 1.2 ng/dL in 2016.
Uses sunscreen in summer.
Current eGFR 64 mL/min/1.73 m2.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Knits as a hobby.
Sees a dentist yearly.
During a checkup in 2020, total protein was 7.0 g/dL.
```

**pres** (program answer: s; facts: patient: bleeding history; absent; current | patient: age = 79; present; current | patient: eGFR = 64; present; current)
```
An adult woman.
Recovering on the ward after a myocardial infarction treated with a stent.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Sees a dentist yearly.
Drives a car.
Sleeps seven hours a night.
Examination shows no signs of blood loss.
Her sister sprained a thumb last month.
Prefers morning appointments.
During a checkup in 2020, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2016.
Prefers to be addressed by first name.
Current age 79 years.
Plays the piano.
Owns a bicycle.
In 2011, folate was 12 ng/mL.
Knits as a hobby.
eGFR now 64 mL/min/1.73 m2.
Her wife has recovered from a dislocated finger.
```


## author1 / group 25: `rule_v1.test.c1_allopurinol.egfr.numeric.alt.402`

Rule: For urate-lowering therapy in gout, prescribe allopurinol 100 mg daily. If the current eGFR is below 60 mL/min/1.73 m2, prescribe allopurinol 50 mg daily instead.

**base** (program answer: s; facts: patient: eGFR = 68; present; current)
```
Male patient of 77 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Plays the piano.
eGFR now 68 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: eGFR = 36; present; current)
```
Male patient of 77 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Plays the piano.
eGFR now 36 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: eGFR = 62; present; current)
```
Male patient of 77 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Plays the piano.
eGFR now 62 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: eGFR = 68; present; current)
```
Man of 77 years.
Three gout flares in the past year; serum urate 9.2 mg/dL.
Current eGFR 68 mL/min/1.73 m2.
Plays the piano.
```


## author2 / group 26: `rule_v1.test.gs025.c2.time.superseded.1607`

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**base** (program answer: s; facts: patient: temperature = 37.4; present; current | patient: temperature = 36.6; present; past | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 29 years.
Sore throat for two days.
Prefers to be addressed by first name.
Current temperature 37.4 C.
Owns a bicycle.
Last month, temperature was 36.6 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
```

**flip** (program answer: s'; facts: patient: temperature = 39.1; present; current | patient: temperature = 36.6; present; past | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 29 years.
Sore throat for two days.
Prefers to be addressed by first name.
Current temperature 39.1 C.
Owns a bicycle.
Last month, temperature was 36.6 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
```

**near** (program answer: s; facts: patient: temperature = 37.4; present; current | patient: temperature = 39.2; present; past | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 29 years.
Sore throat for two days.
Prefers to be addressed by first name.
Current temperature 37.4 C.
Owns a bicycle.
Last month, temperature was 39.2 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
```

**pres** (program answer: s; facts: patient: temperature = 37.4; present; current | patient: temperature = 36.6; present; past | patient: myocardial infarction or peripheral artery disease; present; current)
```
Man of 29 years.
Sore throat for two days.
Temperature now 37.4 C (tympanic).
Owns a bicycle.
Last month, temperature was 36.6 C; the newest measurement replaces it.
Lives with peripheral artery disease affecting the left leg.
Prefers to be addressed by first name.
```


## author3 / group 27: `rule_v1.test.gs137.c2.time.long.889`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: serum creatinine = 0.6; present; current | patient: diabetes; present; past | patient: serum creatinine = 1.1; present; past (2021))
```
Woman of 60 years.
Hip osteoarthritis with pain on walking.
Her father sprained a thumb last month.
Zinc of 85 mcg/dL in 2020.
Her friend lives with psoriasis.
In 2020, lipase was 30 U/L.
Teeth in good repair.
Sees a dentist yearly.
Current serum creatinine 0.6 mg/dL.
Prefers morning appointments.
Owns a bicycle.
During a checkup in 2009, total protein was 7.0 g/dL.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Sleeps seven hours a night.
Had diabetes years ago that went into remission on a low-calorie diet.
Has two cats.
Photographs local wildlife.
Uses sunscreen in summer.
Back in 2021, serum creatinine stood at 1.1 mg/dL.
Her friend wears contact lenses.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 1.7; present; current | patient: diabetes; present; past | patient: serum creatinine = 1.1; present; past (2021))
```
Woman of 60 years.
Hip osteoarthritis with pain on walking.
Her father sprained a thumb last month.
Zinc of 85 mcg/dL in 2020.
Her friend lives with psoriasis.
In 2020, lipase was 30 U/L.
Teeth in good repair.
Sees a dentist yearly.
Current serum creatinine 1.7 mg/dL.
Prefers morning appointments.
Owns a bicycle.
During a checkup in 2009, total protein was 7.0 g/dL.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Sleeps seven hours a night.
Had diabetes years ago that went into remission on a low-calorie diet.
Has two cats.
Photographs local wildlife.
Uses sunscreen in summer.
Back in 2021, serum creatinine stood at 1.1 mg/dL.
Her friend wears contact lenses.
```

**near** (program answer: s; facts: patient: serum creatinine = 0.6; present; current | patient: diabetes; present; past | patient: serum creatinine = 1.9; present; past (2021))
```
Woman of 60 years.
Hip osteoarthritis with pain on walking.
Her father sprained a thumb last month.
Zinc of 85 mcg/dL in 2020.
Her friend lives with psoriasis.
In 2020, lipase was 30 U/L.
Teeth in good repair.
Sees a dentist yearly.
Current serum creatinine 0.6 mg/dL.
Prefers morning appointments.
Owns a bicycle.
During a checkup in 2009, total protein was 7.0 g/dL.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Sleeps seven hours a night.
Had diabetes years ago that went into remission on a low-calorie diet.
Has two cats.
Photographs local wildlife.
Uses sunscreen in summer.
Back in 2021, serum creatinine stood at 1.9 mg/dL.
Her friend wears contact lenses.
```

**pres** (program answer: s; facts: patient: diabetes; present; past | patient: serum creatinine = 1.1; present; past (2021) | patient: serum creatinine = 0.6; present; current)
```
Female patient of 60 years.
Hip osteoarthritis with pain on walking.
Lives in a second-floor apartment.
Had diabetes years ago that went into remission on a low-calorie diet.
Sees a dentist yearly.
Her father sprained a thumb last month.
Teeth in good repair.
Has two cats.
Zinc of 85 mcg/dL in 2020.
Her friend wears contact lenses.
Knits as a hobby.
Sleeps seven hours a night.
Photographs local wildlife.
Plays the piano.
Records from 2021 list serum creatinine at 1.1 mg/dL.
Uses sunscreen in summer.
In 2020, lipase was 30 U/L.
During a checkup in 2009, total protein was 7.0 g/dL.
Her friend lives with psoriasis.
Owns a bicycle.
Latest creatinine result: 0.6 mg/dL.
Prefers morning appointments.
```

**missing** (program answer: neither; facts: patient: diabetes; present; past)
```
Woman of 60 years.
Hip osteoarthritis with pain on walking.
Her father sprained a thumb last month.
Zinc of 85 mcg/dL in 2020.
Her friend lives with psoriasis.
In 2020, lipase was 30 U/L.
Teeth in good repair.
Sees a dentist yearly.
Prefers morning appointments.
Owns a bicycle.
During a checkup in 2009, total protein was 7.0 g/dL.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Sleeps seven hours a night.
Had diabetes years ago that went into remission on a low-calorie diet.
Has two cats.
Photographs local wildlife.
Uses sunscreen in summer.
Her friend wears contact lenses.
```


## author4 / group 28: `rule_v1.test.gs157.c2.time.superseded.891`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has ever had heart failure (current or past); the current platelet count is below 50 x10^9/L; the current temperature is above 38.0 C.

**base** (program answer: s; facts: patient: temperature = 38.7; present; current | patient: platelet count = 181; present; current | patient: heart failure; absent; current | patient: platelet count = 207; present; past)
```
Man of 77 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current temperature 38.7 C.
Current platelet count 181 x10^9/L.
Uses sunscreen in summer.
Heart sounds without a gallop.
Pupils equal and reactive to light.
Earlier this week, platelet count was 207 x10^9/L; a newer reading supersedes it.
```

**flip** (program answer: s'; facts: patient: temperature = 38.7; present; current | patient: platelet count = 31; present; current | patient: heart failure; absent; current | patient: platelet count = 207; present; past)
```
Man of 77 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current temperature 38.7 C.
Current platelet count 31 x10^9/L.
Uses sunscreen in summer.
Heart sounds without a gallop.
Pupils equal and reactive to light.
Earlier this week, platelet count was 207 x10^9/L; a newer reading supersedes it.
```

**near** (program answer: s; facts: patient: temperature = 38.7; present; current | patient: platelet count = 181; present; current | patient: heart failure; absent; current | patient: platelet count = 44; present; past)
```
Man of 77 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current temperature 38.7 C.
Current platelet count 181 x10^9/L.
Uses sunscreen in summer.
Heart sounds without a gallop.
Pupils equal and reactive to light.
Earlier this week, platelet count was 44 x10^9/L; a newer reading supersedes it.
```

**pres** (program answer: s; facts: patient: temperature = 38.7; present; current | patient: heart failure; absent; current | patient: platelet count = 181; present; current | patient: platelet count = 207; present; past)
```
Male patient of 77 years.
Community-acquired pneumonia confirmed on chest radiograph.
Pupils equal and reactive to light.
Temperature now 38.7 C (tympanic).
Uses sunscreen in summer.
Heart sounds without a gallop.
Platelet count now 181 x10^9/L.
Earlier this week, platelet count was 207 x10^9/L; a newer reading supersedes it.
```


## author1 / group 29: `rule_v1.test.gs120.c3.time.long.226`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the patient has ever had a peptic ulcer (current or past); the current weight is 60 kg or less.

**base** (program answer: s; facts: patient: weight = 69; present; past (2008) | patient: peptic ulcer at any time; present; current | patient: weight = 86; present; current)
```
Man of 65 years.
First day after elective total hip replacement.
His wife burned a hand on a stove years ago.
Back in 2008, weight stood at 69 kg.
Drives a car.
In 2010, folate was 12 ng/mL.
Prefers to be addressed by first name.
Photographs local wildlife.
His wife wears contact lenses.
Sleeps seven hours a night.
Teeth in good repair.
Active peptic ulcer disease.
Prefers morning appointments.
His wife sprained a thumb last month.
Knits as a hobby.
Current weight 86 kg.
Uses sunscreen in summer.
His friend has a lazy eye.
During a checkup in 2010, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Enjoys board games.
Lives in a second-floor apartment.
Owns a bicycle.
```

**flip** (program answer: s'; facts: patient: weight = 69; present; past (2008) | patient: peptic ulcer at any time; present; current | patient: weight = 60; present; current)
```
Man of 65 years.
First day after elective total hip replacement.
His wife burned a hand on a stove years ago.
Back in 2008, weight stood at 69 kg.
Drives a car.
In 2010, folate was 12 ng/mL.
Prefers to be addressed by first name.
Photographs local wildlife.
His wife wears contact lenses.
Sleeps seven hours a night.
Teeth in good repair.
Active peptic ulcer disease.
Prefers morning appointments.
His wife sprained a thumb last month.
Knits as a hobby.
Current weight 60 kg.
Uses sunscreen in summer.
His friend has a lazy eye.
During a checkup in 2010, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Enjoys board games.
Lives in a second-floor apartment.
Owns a bicycle.
```

**near** (program answer: s; facts: patient: weight = 58; present; past (2008) | patient: peptic ulcer at any time; present; current | patient: weight = 86; present; current)
```
Man of 65 years.
First day after elective total hip replacement.
His wife burned a hand on a stove years ago.
Back in 2008, weight stood at 58 kg.
Drives a car.
In 2010, folate was 12 ng/mL.
Prefers to be addressed by first name.
Photographs local wildlife.
His wife wears contact lenses.
Sleeps seven hours a night.
Teeth in good repair.
Active peptic ulcer disease.
Prefers morning appointments.
His wife sprained a thumb last month.
Knits as a hobby.
Current weight 86 kg.
Uses sunscreen in summer.
His friend has a lazy eye.
During a checkup in 2010, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Enjoys board games.
Lives in a second-floor apartment.
Owns a bicycle.
```

**pres** (program answer: s; facts: patient: weight = 86; present; current | patient: weight = 69; present; past (2008) | patient: peptic ulcer at any time; present; current)
```
Male patient of 65 years.
First day after elective total hip replacement.
His wife wears contact lenses.
During a checkup in 2010, total protein was 7.0 g/dL.
In 2010, folate was 12 ng/mL.
Photographs local wildlife.
Lives in a second-floor apartment.
Knits as a hobby.
Latest weight 86 kg.
Enjoys board games.
Records from 2008 list weight at 69 kg.
His friend has a lazy eye.
Teeth in good repair.
Sleeps seven hours a night.
Pupils equal and reactive to light.
His wife burned a hand on a stove years ago.
His wife sprained a thumb last month.
Prefers morning appointments.
Drives a car.
Active peptic ulcer disease.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Owns a bicycle.
```

**missing** (program answer: neither; facts: patient: peptic ulcer at any time; present; current)
```
Man of 65 years.
First day after elective total hip replacement.
His wife burned a hand on a stove years ago.
Drives a car.
In 2010, folate was 12 ng/mL.
Prefers to be addressed by first name.
Photographs local wildlife.
His wife wears contact lenses.
Sleeps seven hours a night.
Teeth in good repair.
Active peptic ulcer disease.
Prefers morning appointments.
His wife sprained a thumb last month.
Knits as a hobby.
Uses sunscreen in summer.
His friend has a lazy eye.
During a checkup in 2010, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Enjoys board games.
Lives in a second-floor apartment.
Owns a bicycle.
```


## author2 / group 30: `rule_v1.test.gs075.c2.negation.easy.87`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.

**base** (program answer: s; facts: patient: warfarin; absent; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current)
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Anticoagulant therapy: none at present.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: warfarin; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current)
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```

**near** (program answer: s; facts: patient: warfarin; absent; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current)
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Has never been prescribed warfarin.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: warfarin; absent; current)
```
Male patient of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Teeth in good repair.
Rectal exam unremarkable.
Current calf swelling 3.6 cm compared with the other leg.
Uses sunscreen in summer.
Anticoagulant therapy: none at present.
```

**missing** (program answer: neither; facts: patient: warfarin; unknown; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current)
```
Man of 69 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Uses sunscreen in summer.
Warfarin: status unclear from the records at hand.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Teeth in good repair.
```


## author3 / group 31: `rule_v1.test.gs148.c1.negation.easy.922`

Rule: For early Lyme disease, prescribe doxycycline. If the patient has ever had coronary artery disease (current or past) and the patient has an active peptic ulcer, prescribe amoxicillin instead.

**base** (program answer: s; facts: patient: active peptic ulcer; present; current | patient: coronary artery disease; absent; current)
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Cardiac stress test unremarkable last year.
Knits as a hobby.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: active peptic ulcer; present; current | patient: coronary artery disease; present; current)
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Known coronary artery disease (two-vessel disease on angiography).
Knits as a hobby.
Plays the piano.
```

**near** (program answer: s; facts: patient: active peptic ulcer; present; current | patient: coronary artery disease; absent; current)
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Has never had coronary artery disease.
Knits as a hobby.
Plays the piano.
```

**pres** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: active peptic ulcer; present; current)
```
Man of 53 years.
Erythema migrans rash ten days after a tick bite.
Plays the piano.
Knits as a hobby.
Cardiac stress test unremarkable last year.
Has an active duodenal ulcer.
Prefers to be addressed by first name.
```

**missing** (program answer: neither; facts: patient: active peptic ulcer; present; current | patient: coronary artery disease; unknown; current)
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Coronary artery disease: unknown.
Knits as a hobby.
Plays the piano.
```


## author4 / group 32: `rule_v1.test.hf_spironolactone.k.time.alt.1`

Rule: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 4.5 mmol/L, add dapagliflozin instead.

**base** (program answer: s; facts: patient: potassium = 4.2; present; past (2017) | patient: potassium = 4.1; present; current)
```
Woman of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Prefers to be addressed by first name.
Back in 2017, serum potassium stood at 4.2 mmol/L.
Prefers morning appointments.
Current serum potassium 4.1 mmol/L.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: potassium = 4.2; present; past (2017) | patient: potassium = 5.0; present; current)
```
Woman of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Prefers to be addressed by first name.
Back in 2017, serum potassium stood at 4.2 mmol/L.
Prefers morning appointments.
Current serum potassium 5.0 mmol/L.
Enjoys board games.
```

**near** (program answer: s; facts: patient: potassium = 5.3; present; past (2017) | patient: potassium = 4.1; present; current)
```
Woman of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Prefers to be addressed by first name.
Back in 2017, serum potassium stood at 5.3 mmol/L.
Prefers morning appointments.
Current serum potassium 4.1 mmol/L.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: potassium = 4.2; present; past (2017) | patient: potassium = 4.1; present; current)
```
Female patient of 46 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Prefers to be addressed by first name.
Prefers morning appointments.
Records from 2017 list serum potassium at 4.2 mmol/L.
Latest potassium result: 4.1 mmol/L.
Drives a car.
Enjoys board games.
```


## author1 / group 33: `rule_v1.test.s3_blatchford.bun.boundary.long.730`

Rule: Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.

**base** (program answer: s; facts: patient: heart rate = 79; present; current | patient: blood urea nitrogen = 12; present; current | patient: systolic blood pressure = 136; present; current | patient: heart failure; absent; current)
```
Male patient of 30 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Lives in a second-floor apartment.
Enjoys board games.
In 2018, folate was 12 ng/mL.
In 2020, lipase was 30 U/L.
Current heart rate 79/min.
Knits as a hobby.
During a checkup in 2021, free T3 was 3.2 pg/mL.
His uncle burned a hand on a stove years ago.
Drives a car.
Sees a dentist yearly.
Blood urea nitrogen 12 mg/dL on the current labs.
His roommate sprained a thumb last month.
Sleeps seven hours a night.
Current systolic blood pressure 136 mmHg.
Prefers morning appointments.
Heart sounds without a gallop.
Has two cats.
Paints watercolors as a hobby.
His sister has recovered from a dislocated finger.
```

**flip** (program answer: s'; facts: patient: heart rate = 79; present; current | patient: blood urea nitrogen = 19; present; current | patient: systolic blood pressure = 136; present; current | patient: heart failure; absent; current)
```
Male patient of 30 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Lives in a second-floor apartment.
Enjoys board games.
In 2018, folate was 12 ng/mL.
In 2020, lipase was 30 U/L.
Current heart rate 79/min.
Knits as a hobby.
During a checkup in 2021, free T3 was 3.2 pg/mL.
His uncle burned a hand on a stove years ago.
Drives a car.
Sees a dentist yearly.
Blood urea nitrogen 19 mg/dL on the current labs.
His roommate sprained a thumb last month.
Sleeps seven hours a night.
Current systolic blood pressure 136 mmHg.
Prefers morning appointments.
Heart sounds without a gallop.
Has two cats.
Paints watercolors as a hobby.
His sister has recovered from a dislocated finger.
```

**near** (program answer: s; facts: patient: heart rate = 79; present; current | patient: blood urea nitrogen = 18; present; current | patient: systolic blood pressure = 136; present; current | patient: heart failure; absent; current)
```
Male patient of 30 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Lives in a second-floor apartment.
Enjoys board games.
In 2018, folate was 12 ng/mL.
In 2020, lipase was 30 U/L.
Current heart rate 79/min.
Knits as a hobby.
During a checkup in 2021, free T3 was 3.2 pg/mL.
His uncle burned a hand on a stove years ago.
Drives a car.
Sees a dentist yearly.
Blood urea nitrogen 18 mg/dL on the current labs.
His roommate sprained a thumb last month.
Sleeps seven hours a night.
Current systolic blood pressure 136 mmHg.
Prefers morning appointments.
Heart sounds without a gallop.
Has two cats.
Paints watercolors as a hobby.
His sister has recovered from a dislocated finger.
```

**pres** (program answer: s; facts: patient: blood urea nitrogen = 12; present; current | patient: heart failure; absent; current | patient: heart rate = 79; present; current | patient: systolic blood pressure = 136; present; current)
```
Man of 30 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
His uncle burned a hand on a stove years ago.
His sister has recovered from a dislocated finger.
In 2020, lipase was 30 U/L.
Has two cats.
Prefers morning appointments.
Blood urea nitrogen now: 12 mg/dL.
Sleeps seven hours a night.
During a checkup in 2021, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Heart sounds without a gallop.
His roommate sprained a thumb last month.
Paints watercolors as a hobby.
Drives a car.
Knits as a hobby.
Heart rate now 79/min on a pulse check.
Observations now: blood pressure 136/90 mmHg.
Enjoys board games.
In 2018, folate was 12 ng/mL.
Lives in a second-floor apartment.
```

**missing** (program answer: neither; facts: patient: heart rate = 79; present; current | patient: systolic blood pressure = 136; present; current | patient: heart failure; absent; current)
```
Male patient of 30 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Lives in a second-floor apartment.
Enjoys board games.
In 2018, folate was 12 ng/mL.
In 2020, lipase was 30 U/L.
Current heart rate 79/min.
Knits as a hobby.
During a checkup in 2021, free T3 was 3.2 pg/mL.
His uncle burned a hand on a stove years ago.
Drives a car.
Sees a dentist yearly.
His roommate sprained a thumb last month.
Sleeps seven hours a night.
Current systolic blood pressure 136 mmHg.
Prefers morning appointments.
Heart sounds without a gallop.
Has two cats.
Paints watercolors as a hobby.
His sister has recovered from a dislocated finger.
```


## author2 / group 34: `rule_v1.test.gs118.c1.time.superseded.997`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: heart rate = 99; present; current | patient: white cell count = 10.8; present; past | patient: white cell count = 9.0; present; current | patient: eGFR = 37; present; current | patient: angioedema; absent; current)
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

**flip** (program answer: s'; facts: patient: heart rate = 99; present; current | patient: white cell count = 10.8; present; past | patient: white cell count = 13.8; present; current | patient: eGFR = 37; present; current | patient: angioedema; absent; current)
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

**near** (program answer: s; facts: patient: heart rate = 99; present; current | patient: white cell count = 14.3; present; past | patient: white cell count = 9.0; present; current | patient: eGFR = 37; present; current | patient: angioedema; absent; current)
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

**pres** (program answer: s; facts: patient: heart rate = 99; present; current | patient: white cell count = 9.0; present; current | patient: eGFR = 37; present; current | patient: angioedema; absent; current | patient: white cell count = 10.8; present; past)
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


## author3 / group 35: `rule_v1.test.gs010.c2.subject.easy.1863`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

**base** (program answer: s; facts: patient: white cell count = 13.3; present; current | patient: coronary artery disease; present; past)
```
Male patient of 85 years.
Atrial fibrillation; anticoagulation indicated.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Plays the piano.
Latest WBC is 13.3 x10^9/L.
Coronary artery disease years ago, with angina that went away after bypass surgery.
```

**flip** (program answer: s'; facts: patient: white cell count = 13.3; present; current | patient: colorectal cancer (patient or first-degree relative); present; current | patient: coronary artery disease; present; past)
```
Male patient of 85 years.
Atrial fibrillation; anticoagulation indicated.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Plays the piano.
Latest WBC is 13.3 x10^9/L.
Colorectal cancer under active treatment.
Coronary artery disease years ago, with angina that went away after bypass surgery.
```

**near** (program answer: s; facts: patient: white cell count = 13.3; present; current | wife: colorectal cancer (patient or first-degree relative); present; current | patient: coronary artery disease; present; past)
```
Male patient of 85 years.
Atrial fibrillation; anticoagulation indicated.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Plays the piano.
Latest WBC is 13.3 x10^9/L.
His wife is undergoing surgery for bowel cancer.
Coronary artery disease years ago, with angina that went away after bypass surgery.
```

**pres** (program answer: s; facts: patient: coronary artery disease; present; past | patient: white cell count = 13.3; present; current)
```
Man of 85 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Plays the piano.
Sleeps seven hours a night.
Current white cell count 13.3 x10^9/L.
```


## author4 / group 36: `rule_v1.test.gs118.c3.time.easy.1067`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: eGFR = 52; present; past (2017) | patient: angioedema; absent; current | patient: white cell count = 12.6; present; current | patient: eGFR = 69; present; current | patient: heart rate = 63; present; current)
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

**flip** (program answer: s'; facts: patient: eGFR = 52; present; past (2017) | patient: angioedema; absent; current | patient: white cell count = 12.6; present; current | patient: eGFR = 40; present; current | patient: heart rate = 63; present; current)
```
Man of 51 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Records from 2017 list eGFR at 52 mL/min/1.73 m2.
Has two cats.
Face and neck without swelling on examination.
Latest WBC is 12.6 x10^9/L.
Pupils equal and reactive to light.
Current eGFR 40 mL/min/1.73 m2.
Uses sunscreen in summer.
Sees a dentist yearly.
Heart rate now 63/min on a pulse check.
```

**near** (program answer: s; facts: patient: eGFR = 35; present; past (2017) | patient: angioedema; absent; current | patient: white cell count = 12.6; present; current | patient: eGFR = 69; present; current | patient: heart rate = 63; present; current)
```
Man of 51 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Records from 2017 list eGFR at 35 mL/min/1.73 m2.
Has two cats.
Face and neck without swelling on examination.
Latest WBC is 12.6 x10^9/L.
Pupils equal and reactive to light.
Current eGFR 69 mL/min/1.73 m2.
Uses sunscreen in summer.
Sees a dentist yearly.
Heart rate now 63/min on a pulse check.
```

**pres** (program answer: s; facts: patient: heart rate = 63; present; current | patient: eGFR = 69; present; current | patient: eGFR = 52; present; past (2017) | patient: white cell count = 12.6; present; current | patient: angioedema; absent; current)
```
Male patient of 51 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Pupils equal and reactive to light.
Current heart rate 63/min.
Uses sunscreen in summer.
Has two cats.
eGFR now 69 mL/min/1.73 m2.
Back in 2017, eGFR stood at 52 mL/min/1.73 m2.
Current white cell count 12.6 x10^9/L.
Face and neck without swelling on examination.
Sees a dentist yearly.
```


## author1 / group 37: `rule_v1.test.s2_caprini.vte.subject.long.959`

Rule: Caprini score (as used here, partial): 3 points for a venous thromboembolism of the patient or a first-degree relative (parent, sibling or child) at any time; 2 points for cancer at any time (active or previous); 1 point for a current body mass index above 25.0 kg/m2. Other Caprini items, including age, are not part of this question.

**base** (program answer: s; facts: patient: cancer; absent; current | patient: body mass index = 20.4; present; current)
```
Woman of 79 years.
Admitted for an emergency bowel resection.
Zinc of 85 mcg/dL in 2017.
Has two cats.
Oncology follow-up: none.
Her sister has a lazy eye.
Lives in a second-floor apartment.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Prefers morning appointments.
Paints watercolors as a hobby.
Her roommate has recovered from a dislocated finger.
Drives a car.
Prefers to be addressed by first name.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
In 2016, folate was 12 ng/mL.
Teeth in good repair.
Current body mass index 20.4 kg/m2.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; present; current | patient: cancer; absent; current | patient: body mass index = 20.4; present; current)
```
Woman of 79 years.
Admitted for an emergency bowel resection.
Zinc of 85 mcg/dL in 2017.
Ongoing treatment for a deep vein thrombosis of the left arm.
Has two cats.
Oncology follow-up: none.
Her sister has a lazy eye.
Lives in a second-floor apartment.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Prefers morning appointments.
Paints watercolors as a hobby.
Her roommate has recovered from a dislocated finger.
Drives a car.
Prefers to be addressed by first name.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
In 2016, folate was 12 ng/mL.
Teeth in good repair.
Current body mass index 20.4 kg/m2.
```

**near** (program answer: s; facts: wife: venous thromboembolism; present; current | patient: cancer; absent; current | patient: body mass index = 20.4; present; current)
```
Woman of 79 years.
Admitted for an emergency bowel resection.
Zinc of 85 mcg/dL in 2017.
Her wife is on anticoagulation for venous thrombosis.
Has two cats.
Oncology follow-up: none.
Her sister has a lazy eye.
Lives in a second-floor apartment.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Prefers morning appointments.
Paints watercolors as a hobby.
Her roommate has recovered from a dislocated finger.
Drives a car.
Prefers to be addressed by first name.
Knits as a hobby.
During a checkup in 2017, free T3 was 3.2 pg/mL.
In 2016, folate was 12 ng/mL.
Teeth in good repair.
Current body mass index 20.4 kg/m2.
```

**pres** (program answer: s; facts: patient: body mass index = 20.4; present; current | patient: cancer; absent; current)
```
Female patient of 79 years.
Admitted for an emergency bowel resection.
Has two cats.
Prefers to be addressed by first name.
Prefers morning appointments.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Teeth in good repair.
Lives in a second-floor apartment.
Her sister wears contact lenses.
In 2016, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2017.
Latest BMI is 20.4 kg/m2.
Oncology follow-up: none.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Knits as a hobby.
Her sister has a lazy eye.
Drives a car.
Her roommate has recovered from a dislocated finger.
```


## author2 / group 38: `rule_v1.test.s3_hctci.stroke.negation.easy.839`

Rule: Hematopoietic Cell Transplantation-specific Comorbidity Index (as used here, partial): 1 point for coronary artery disease at any time (current or past); 1 point for a stroke or TIA at any time (current or past); 2 points for a current peptic ulcer; 1 point for a current ALT above 40 U/L. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: active peptic ulcer; absent; current | patient: stroke/TIA; absent; current | patient: coronary artery disease; absent; current | patient: ALT = 12; present; current)
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

**flip** (program answer: s'; facts: patient: active peptic ulcer; absent; current | patient: stroke/TIA; present; past (2007) | patient: coronary artery disease; absent; current | patient: ALT = 12; present; current)
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

**near** (program answer: s; facts: patient: active peptic ulcer; absent; current | patient: stroke/TIA; absent; current | patient: coronary artery disease; absent; current | patient: ALT = 12; present; current)
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

**pres** (program answer: s; facts: patient: stroke/TIA; absent; current | patient: active peptic ulcer; absent; current | patient: ALT = 12; present; current | patient: coronary artery disease; absent; current)
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


## author3 / group 39: `rule_v1.test.gs113.c1.time.easy.64`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum creatinine is above 2.0 mg/dL and the patient has ever had heart failure (current or past), prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: heart failure; present; current | patient: serum creatinine = 1.2; present; past (2018) | patient: serum creatinine = 0.7; present; current)
```
Woman of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Photographs local wildlife.
Current heart failure with ankle swelling.
Paints watercolors as a hobby.
Back in 2018, serum creatinine stood at 1.2 mg/dL.
Uses sunscreen in summer.
Current serum creatinine 0.7 mg/dL.
```

**flip** (program answer: s'; facts: patient: heart failure; present; current | patient: serum creatinine = 1.2; present; past (2018) | patient: serum creatinine = 2.2; present; current)
```
Woman of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Photographs local wildlife.
Current heart failure with ankle swelling.
Paints watercolors as a hobby.
Back in 2018, serum creatinine stood at 1.2 mg/dL.
Uses sunscreen in summer.
Current serum creatinine 2.2 mg/dL.
```

**near** (program answer: s; facts: patient: heart failure; present; current | patient: serum creatinine = 2.4; present; past (2018) | patient: serum creatinine = 0.7; present; current)
```
Woman of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Photographs local wildlife.
Current heart failure with ankle swelling.
Paints watercolors as a hobby.
Back in 2018, serum creatinine stood at 2.4 mg/dL.
Uses sunscreen in summer.
Current serum creatinine 0.7 mg/dL.
```

**pres** (program answer: s; facts: patient: serum creatinine = 1.2; present; past (2018) | patient: heart failure; present; current | patient: serum creatinine = 0.7; present; current)
```
Female patient of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Records from 2018 list serum creatinine at 1.2 mg/dL.
Photographs local wildlife.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Current heart failure with ankle swelling.
Latest creatinine result: 0.7 mg/dL.
```

**missing** (program answer: neither; facts: patient: heart failure; present; current)
```
Woman of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Photographs local wildlife.
Current heart failure with ankle swelling.
Paints watercolors as a hobby.
Uses sunscreen in summer.
```


## author4 / group 40: `rule_v1.test.gs124.c3.boundary.easy.731`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**base** (program answer: s; facts: patient: calf swelling = 3.5; present; current | patient: age = 47; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 3.5 cm.
Sees a dentist yearly.
Currently aged 47 years.
Pupils equal and reactive to light.
Hemoglobin within the normal range on recent blood tests.
Photographs local wildlife.
```

**flip** (program answer: s'; facts: patient: calf swelling = 3.5; present; current | patient: age = 72; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 3.5 cm.
Sees a dentist yearly.
Currently aged 72 years.
Pupils equal and reactive to light.
Hemoglobin within the normal range on recent blood tests.
Photographs local wildlife.
```

**near** (program answer: s; facts: patient: calf swelling = 3.5; present; current | patient: age = 65; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 3.5 cm.
Sees a dentist yearly.
Currently aged 65 years.
Pupils equal and reactive to light.
Hemoglobin within the normal range on recent blood tests.
Photographs local wildlife.
```

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.5; present; current | patient: age = 47; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Hemoglobin within the normal range on recent blood tests.
Pupils equal and reactive to light.
Current calf swelling 3.5 cm compared with the other leg.
Photographs local wildlife.
Sees a dentist yearly.
Current age 47 years.
```

**missing** (program answer: neither; facts: patient: calf swelling = 3.5; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 3.5 cm.
Sees a dentist yearly.
Pupils equal and reactive to light.
Hemoglobin within the normal range on recent blood tests.
Photographs local wildlife.
```


## author1 / group 41: `rule_v1.test.gs074.c3.boundary.long.505`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. Score 3 points if the age of the patient is 65 years or more; 2 points if the current systolic blood pressure is below 90 mmHg; 1 point if the current blood urea nitrogen is above 19 mg/dL; 3 points if the patient has ever had diabetes (current or past). If the score is 6 or more, prescribe intravenous piperacillin-tazobactam instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 75; present; current | patient: age = 75; present; current | patient: diabetes; absent; current | patient: blood urea nitrogen = 13; present; current)
```
An adult man.
Suspected chest infection; assessed on the medical ward.
His friend lives with psoriasis.
His roommate has recovered from a dislocated finger.
Owns a bicycle.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister has a lazy eye.
In 2020, lipase was 30 U/L.
Observations now: blood pressure 75/56 mmHg.
Prefers morning appointments.
Teeth in good repair.
Current age 75 years.
During a checkup in 2005, free T3 was 3.2 pg/mL.
During a checkup in 2017, total protein was 7.0 g/dL.
His friend wears contact lenses.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2007.
HbA1c 5.3% at a routine check.
Enjoys board games.
Blood urea nitrogen now: 13 mg/dL.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 75; present; current | patient: age = 75; present; current | patient: diabetes; absent; current | patient: blood urea nitrogen = 21; present; current)
```
An adult man.
Suspected chest infection; assessed on the medical ward.
His friend lives with psoriasis.
His roommate has recovered from a dislocated finger.
Owns a bicycle.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister has a lazy eye.
In 2020, lipase was 30 U/L.
Observations now: blood pressure 75/56 mmHg.
Prefers morning appointments.
Teeth in good repair.
Current age 75 years.
During a checkup in 2005, free T3 was 3.2 pg/mL.
During a checkup in 2017, total protein was 7.0 g/dL.
His friend wears contact lenses.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2007.
HbA1c 5.3% at a routine check.
Enjoys board games.
Blood urea nitrogen now: 21 mg/dL.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 75; present; current | patient: age = 75; present; current | patient: diabetes; absent; current | patient: blood urea nitrogen = 19; present; current)
```
An adult man.
Suspected chest infection; assessed on the medical ward.
His friend lives with psoriasis.
His roommate has recovered from a dislocated finger.
Owns a bicycle.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister has a lazy eye.
In 2020, lipase was 30 U/L.
Observations now: blood pressure 75/56 mmHg.
Prefers morning appointments.
Teeth in good repair.
Current age 75 years.
During a checkup in 2005, free T3 was 3.2 pg/mL.
During a checkup in 2017, total protein was 7.0 g/dL.
His friend wears contact lenses.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2007.
HbA1c 5.3% at a routine check.
Enjoys board games.
Blood urea nitrogen now: 19 mg/dL.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 75; present; current | patient: diabetes; absent; current | patient: blood urea nitrogen = 13; present; current | patient: age = 75; present; current)
```
Man, adult.
Suspected chest infection; assessed on the medical ward.
His sister has a lazy eye.
His roommate has recovered from a dislocated finger.
Photographs local wildlife.
Current systolic blood pressure 75 mmHg.
In 2020, lipase was 30 U/L.
HbA1c 5.3% at a routine check.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Owns a bicycle.
Zinc of 85 mcg/dL in 2007.
Blood urea nitrogen 13 mg/dL on the current labs.
Pupils equal and reactive to light.
Enjoys board games.
Sees a dentist yearly.
Currently aged 75 years.
His friend lives with psoriasis.
Teeth in good repair.
Sleeps seven hours a night.
During a checkup in 2017, total protein was 7.0 g/dL.
Prefers morning appointments.
His friend wears contact lenses.
```


## author2 / group 42: `rule_v1.test.qsofa.rr.numeric.easy.1432`

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**base** (program answer: s; facts: patient: respiratory rate = 16; present; current | patient: systolic blood pressure = 111; present; current)
```
Male patient of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Paints watercolors as a hobby.
Current respiratory rate 16/min.
Observations now: blood pressure 111/76 mmHg.
```

**flip** (program answer: s'; facts: patient: respiratory rate = 22; present; current | patient: systolic blood pressure = 111; present; current)
```
Male patient of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Paints watercolors as a hobby.
Current respiratory rate 22/min.
Observations now: blood pressure 111/76 mmHg.
```

**near** (program answer: s; facts: patient: respiratory rate = 21; present; current | patient: systolic blood pressure = 111; present; current)
```
Male patient of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Paints watercolors as a hobby.
Current respiratory rate 21/min.
Observations now: blood pressure 111/76 mmHg.
```

**pres** (program answer: s; facts: patient: respiratory rate = 16; present; current | patient: systolic blood pressure = 111; present; current)
```
Man of 33 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 16/min.
Current systolic blood pressure 111 mmHg.
Paints watercolors as a hobby.
```


## author3 / group 43: `rule_v1.test.gs134.c4.subject.long.929`

Rule: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: platelet count = 42; present; current | patient: weight = 56; present; current | father: coronary artery disease (patient or first-degree relative); present; current | patient: tender cervical lymph nodes; absent; current)
```
Woman of 20 years.
Requests contraception.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Owns a bicycle.
In 2024, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Current platelet count 42 x10^9/L.
Current weight 56 kg.
Drives a car.
Her father has angina from coronary artery disease.
Has two cats.
Teeth in good repair.
Her sister has a lazy eye.
Plays the piano.
Neck palpation unremarkable.
Knits as a hobby.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: platelet count = 42; present; current | patient: weight = 56; present; current | father: coronary artery disease (patient or first-degree relative); present; current | patient: tender cervical lymph nodes; present; current)
```
Woman of 20 years.
Requests contraception.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Owns a bicycle.
In 2024, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Current platelet count 42 x10^9/L.
Current weight 56 kg.
Drives a car.
Her father has angina from coronary artery disease.
Has two cats.
Teeth in good repair.
Her sister has a lazy eye.
Plays the piano.
Tender, swollen lymph nodes in the front of the neck.
Knits as a hobby.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: platelet count = 42; present; current | patient: weight = 56; present; current | father: coronary artery disease (patient or first-degree relative); present; current | sister: tender cervical lymph nodes; present; current)
```
Woman of 20 years.
Requests contraception.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Owns a bicycle.
In 2024, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Current platelet count 42 x10^9/L.
Current weight 56 kg.
Drives a car.
Her father has angina from coronary artery disease.
Has two cats.
Teeth in good repair.
Her sister has a lazy eye.
Plays the piano.
Her sister currently has tender anterior cervical lymphadenopathy.
Knits as a hobby.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: tender cervical lymph nodes; absent; current | patient: platelet count = 42; present; current | father: coronary artery disease (patient or first-degree relative); present; current | patient: weight = 56; present; current)
```
Female patient of 20 years.
Requests contraception.
Teeth in good repair.
Neck palpation unremarkable.
In 2024, folate was 12 ng/mL.
Has two cats.
Her sister has a lazy eye.
Her sister sprained a thumb last month.
Platelet count now 42 x10^9/L.
Prefers morning appointments.
Plays the piano.
Her father has angina from coronary artery disease.
Knits as a hobby.
In 2024, lipase was 30 U/L.
Drives a car.
Paints watercolors as a hobby.
Latest weight 56 kg.
Owns a bicycle.
Sleeps seven hours a night.
Sees a dentist yearly.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
```

**missing** (program answer: neither; facts: patient: platelet count = 42; present; current | patient: weight = 56; present; current | father: coronary artery disease (patient or first-degree relative); present; current | patient: tender cervical lymph nodes; unknown; current)
```
Woman of 20 years.
Requests contraception.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Owns a bicycle.
In 2024, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Current platelet count 42 x10^9/L.
Current weight 56 kg.
Drives a car.
Her father has angina from coronary artery disease.
Has two cats.
Teeth in good repair.
Her sister has a lazy eye.
Plays the piano.
Tender cervical lymph nodes: unknown.
Knits as a hobby.
Sleeps seven hours a night.
```


## author4 / group 44: `rule_v1.test.gs245.c3.numeric.easy.1772`

Rule: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had heart failure (current or past); the patient has an active peptic ulcer; the age of the patient is 65 years or more.

**base** (program answer: s; facts: patient: age = 58; present; current | patient: active peptic ulcer; absent; current | patient: heart failure; present; current)
```
An adult woman.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Current age 58 years.
Photographs local wildlife.
Appetite good; no indigestion.
Has heart failure, treated with diuretics.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: age = 68; present; current | patient: active peptic ulcer; absent; current | patient: heart failure; present; current)
```
An adult woman.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Current age 68 years.
Photographs local wildlife.
Appetite good; no indigestion.
Has heart failure, treated with diuretics.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: age = 63; present; current | patient: active peptic ulcer; absent; current | patient: heart failure; present; current)
```
An adult woman.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Current age 63 years.
Photographs local wildlife.
Appetite good; no indigestion.
Has heart failure, treated with diuretics.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: age = 58; present; current | patient: heart failure; present; current | patient: active peptic ulcer; absent; current)
```
Woman, adult.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Currently aged 58 years.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Has heart failure, treated with diuretics.
Photographs local wildlife.
Appetite good; no indigestion.
```


## author1 / group 45: `rule_v1.test.gs134.c4.negation.easy.1859`

Rule: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: sister: coronary artery disease (patient or first-degree relative); present; past | patient: tender cervical lymph nodes; absent; current | patient: platelet count = 48; present; current | patient: weight = 55; present; current)
```
Female patient of 20 years.
Requests contraception.
Her sister had bypass surgery for coronary artery disease years ago.
Drives a car.
Enjoys board games.
Owns a bicycle.
Front of the neck without tenderness or swelling.
Prefers morning appointments.
Current platelet count 48 x10^9/L.
Latest weight 55 kg.
```

**flip** (program answer: s'; facts: sister: coronary artery disease (patient or first-degree relative); present; past | patient: tender cervical lymph nodes; present; current | patient: platelet count = 48; present; current | patient: weight = 55; present; current)
```
Female patient of 20 years.
Requests contraception.
Her sister had bypass surgery for coronary artery disease years ago.
Drives a car.
Enjoys board games.
Owns a bicycle.
Tender, swollen lymph nodes in the front of the neck.
Prefers morning appointments.
Current platelet count 48 x10^9/L.
Latest weight 55 kg.
```

**near** (program answer: s; facts: sister: coronary artery disease (patient or first-degree relative); present; past | patient: tender cervical lymph nodes; absent; current | patient: platelet count = 48; present; current | patient: weight = 55; present; current)
```
Female patient of 20 years.
Requests contraception.
Her sister had bypass surgery for coronary artery disease years ago.
Drives a car.
Enjoys board games.
Owns a bicycle.
Neck supple, without tender lymph nodes.
Prefers morning appointments.
Current platelet count 48 x10^9/L.
Latest weight 55 kg.
```

**pres** (program answer: s; facts: patient: tender cervical lymph nodes; absent; current | patient: platelet count = 48; present; current | sister: coronary artery disease (patient or first-degree relative); present; past | patient: weight = 55; present; current)
```
Woman of 20 years.
Requests contraception.
Owns a bicycle.
Front of the neck without tenderness or swelling.
Platelet count now 48 x10^9/L.
Enjoys board games.
Her sister had bypass surgery for coronary artery disease years ago.
Current weight 55 kg.
Prefers morning appointments.
Drives a car.
```


## author2 / group 46: `rule_v1.test.s1_idsa_minor.bun.time.easy.141`

Rule: IDSA/ATS minor criteria for severe community-acquired pneumonia (as used here, partial): 1 point each for a current white cell count below 4.0 x10^9/L; a current platelet count below 100 x10^9/L; a current temperature below 36.0 C; a current blood urea nitrogen of 20 mg/dL or more. Other criteria are not part of this question.

**base** (program answer: s; facts: patient: temperature = 37.1; present; current | patient: white cell count = 5.4; present; current | patient: platelet count = 168; present; current | patient: blood urea nitrogen = 15; present; current | patient: blood urea nitrogen = 13; present; past (2022))
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

**flip** (program answer: s'; facts: patient: temperature = 37.1; present; current | patient: white cell count = 5.4; present; current | patient: platelet count = 168; present; current | patient: blood urea nitrogen = 31; present; current | patient: blood urea nitrogen = 13; present; past (2022))
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

**near** (program answer: s; facts: patient: temperature = 37.1; present; current | patient: white cell count = 5.4; present; current | patient: platelet count = 168; present; current | patient: blood urea nitrogen = 15; present; current | patient: blood urea nitrogen = 22; present; past (2022))
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

**pres** (program answer: s; facts: patient: platelet count = 168; present; current | patient: temperature = 37.1; present; current | patient: blood urea nitrogen = 15; present; current | patient: white cell count = 5.4; present; current | patient: blood urea nitrogen = 13; present; past (2022))
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


## author3 / group 47: `rule_v1.test.gs188.c2.boundary.long.622`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: ALT = 36; present; current | patient: peptic ulcer at any time; present; current | patient: venous thromboembolism; absent; current)
```
Male patient of 74 years.
Spreading redness and warmth of the right shin for two days.
His friend lives with psoriasis.
Plays the piano.
Lives in a second-floor apartment.
Photographs local wildlife.
Prefers morning appointments.
ALT now 36 U/L.
Drives a car.
Prefers to be addressed by first name.
Owns a bicycle.
Enjoys board games.
Has an active duodenal ulcer.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Teeth in good repair.
Coagulation tests normal on recent bloodwork.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
His wife has a lazy eye.
Uses sunscreen in summer.
During a checkup in 2010, total protein was 7.0 g/dL.
In 2007, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: ALT = 143; present; current | patient: peptic ulcer at any time; present; current | patient: venous thromboembolism; absent; current)
```
Male patient of 74 years.
Spreading redness and warmth of the right shin for two days.
His friend lives with psoriasis.
Plays the piano.
Lives in a second-floor apartment.
Photographs local wildlife.
Prefers morning appointments.
ALT now 143 U/L.
Drives a car.
Prefers to be addressed by first name.
Owns a bicycle.
Enjoys board games.
Has an active duodenal ulcer.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Teeth in good repair.
Coagulation tests normal on recent bloodwork.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
His wife has a lazy eye.
Uses sunscreen in summer.
During a checkup in 2010, total protein was 7.0 g/dL.
In 2007, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: ALT = 120; present; current | patient: peptic ulcer at any time; present; current | patient: venous thromboembolism; absent; current)
```
Male patient of 74 years.
Spreading redness and warmth of the right shin for two days.
His friend lives with psoriasis.
Plays the piano.
Lives in a second-floor apartment.
Photographs local wildlife.
Prefers morning appointments.
ALT now 120 U/L.
Drives a car.
Prefers to be addressed by first name.
Owns a bicycle.
Enjoys board games.
Has an active duodenal ulcer.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Teeth in good repair.
Coagulation tests normal on recent bloodwork.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
His wife has a lazy eye.
Uses sunscreen in summer.
During a checkup in 2010, total protein was 7.0 g/dL.
In 2007, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: peptic ulcer at any time; present; current | patient: ALT = 36; present; current)
```
Man of 74 years.
Spreading redness and warmth of the right shin for two days.
Knits as a hobby.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Coagulation tests normal on recent bloodwork.
Pupils equal and reactive to light.
Sees a dentist yearly.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Has an active duodenal ulcer.
Plays the piano.
Photographs local wildlife.
Lives in a second-floor apartment.
Drives a car.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Prefers morning appointments.
His friend lives with psoriasis.
Current ALT 36 U/L.
Enjoys board games.
Teeth in good repair.
His wife has a lazy eye.
In 2007, lipase was 30 U/L.
Owns a bicycle.
During a checkup in 2010, total protein was 7.0 g/dL.
```

**missing** (program answer: neither; facts: patient: peptic ulcer at any time; present; current | patient: venous thromboembolism; absent; current)
```
Male patient of 74 years.
Spreading redness and warmth of the right shin for two days.
His friend lives with psoriasis.
Plays the piano.
Lives in a second-floor apartment.
Photographs local wildlife.
Prefers morning appointments.
Drives a car.
Prefers to be addressed by first name.
Owns a bicycle.
Enjoys board games.
Has an active duodenal ulcer.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Teeth in good repair.
Coagulation tests normal on recent bloodwork.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
His wife has a lazy eye.
Uses sunscreen in summer.
During a checkup in 2010, total protein was 7.0 g/dL.
In 2007, lipase was 30 U/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```


## author4 / group 48: `rule_v1.test.gs246.c1.boundary.long.758`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: angioedema; present; past | patient: white cell count = 4.5; present; current)
```
Man of 61 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2011.
His wife burned a hand on a stove years ago.
His sister sprained a thumb last month.
In 2012, folate was 12 ng/mL.
His friend lives with psoriasis.
Drives a car.
Paints watercolors as a hobby.
Uses sunscreen in summer.
His father wears contact lenses.
Teeth in good repair.
Oncology follow-up: none.
An episode of angioedema years ago, with full recovery.
Owns a bicycle.
Knits as a hobby.
Plays the piano.
Latest WBC is 4.5 x10^9/L.
Sleeps seven hours a night.
During a checkup in 2010, total protein was 7.0 g/dL.
```

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: angioedema; present; past | patient: white cell count = 12.7; present; current)
```
Man of 61 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2011.
His wife burned a hand on a stove years ago.
His sister sprained a thumb last month.
In 2012, folate was 12 ng/mL.
His friend lives with psoriasis.
Drives a car.
Paints watercolors as a hobby.
Uses sunscreen in summer.
His father wears contact lenses.
Teeth in good repair.
Oncology follow-up: none.
An episode of angioedema years ago, with full recovery.
Owns a bicycle.
Knits as a hobby.
Plays the piano.
Latest WBC is 12.7 x10^9/L.
Sleeps seven hours a night.
During a checkup in 2010, total protein was 7.0 g/dL.
```

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: angioedema; present; past | patient: white cell count = 12.0; present; current)
```
Man of 61 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2011.
His wife burned a hand on a stove years ago.
His sister sprained a thumb last month.
In 2012, folate was 12 ng/mL.
His friend lives with psoriasis.
Drives a car.
Paints watercolors as a hobby.
Uses sunscreen in summer.
His father wears contact lenses.
Teeth in good repair.
Oncology follow-up: none.
An episode of angioedema years ago, with full recovery.
Owns a bicycle.
Knits as a hobby.
Plays the piano.
Latest WBC is 12.0 x10^9/L.
Sleeps seven hours a night.
During a checkup in 2010, total protein was 7.0 g/dL.
```

**pres** (program answer: s; facts: patient: angioedema; present; past | patient: white cell count = 4.5; present; current | patient: active cancer; absent; current)
```
Male patient of 61 years.
Acute low back pain after lifting.
His sister sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2011.
Sleeps seven hours a night.
Drives a car.
His friend lives with psoriasis.
Plays the piano.
His father wears contact lenses.
Owns a bicycle.
Uses sunscreen in summer.
An episode of angioedema years ago, with full recovery.
Knits as a hobby.
Current white cell count 4.5 x10^9/L.
During a checkup in 2010, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
His wife burned a hand on a stove years ago.
In 2012, folate was 12 ng/mL.
Oncology follow-up: none.
Teeth in good repair.
```

**missing** (program answer: neither; facts: patient: active cancer; absent; current | patient: angioedema; present; past)
```
Man of 61 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2011.
His wife burned a hand on a stove years ago.
His sister sprained a thumb last month.
In 2012, folate was 12 ng/mL.
His friend lives with psoriasis.
Drives a car.
Paints watercolors as a hobby.
Uses sunscreen in summer.
His father wears contact lenses.
Teeth in good repair.
Oncology follow-up: none.
An episode of angioedema years ago, with full recovery.
Owns a bicycle.
Knits as a hobby.
Plays the piano.
Sleeps seven hours a night.
During a checkup in 2010, total protein was 7.0 g/dL.
```


## author1 / group 49: `rule_v1.test.gs039.c1.subject.long.910`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient currently has a major bleed, prescribe intermittent pneumatic compression instead.

**base** (program answer: s; facts: patient: active major bleeding; absent; current)
```
Woman of 67 years.
Admitted for community-acquired pneumonia; immobile.
Zinc of 85 mcg/dL in 2010.
Her roommate burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Teeth in good repair.
Uses sunscreen in summer.
Plays the piano.
Photographs local wildlife.
Bowel habit normal, without any blood in the stool.
Has two cats.
Drives a car.
Her wife has recovered from a dislocated finger.
Paints watercolors as a hobby.
Her sister sprained a thumb last month.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: active major bleeding; present; current)
```
Woman of 67 years.
Admitted for community-acquired pneumonia; immobile.
Zinc of 85 mcg/dL in 2010.
Her roommate burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Teeth in good repair.
Uses sunscreen in summer.
Plays the piano.
Photographs local wildlife.
Currently has a major bleed from a duodenal ulcer, with transfusion under way.
Has two cats.
Drives a car.
Her wife has recovered from a dislocated finger.
Paints watercolors as a hobby.
Her sister sprained a thumb last month.
Prefers morning appointments.
```

**near** (program answer: s; facts: wife: active major bleeding; present; current)
```
Woman of 67 years.
Admitted for community-acquired pneumonia; immobile.
Zinc of 85 mcg/dL in 2010.
Her roommate burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Knits as a hobby.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Teeth in good repair.
Uses sunscreen in summer.
Plays the piano.
Photographs local wildlife.
Her wife is currently being transfused for a major bleed.
Has two cats.
Drives a car.
Her wife has recovered from a dislocated finger.
Paints watercolors as a hobby.
Her sister sprained a thumb last month.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: active major bleeding; absent; current)
```
Female patient of 67 years.
Admitted for community-acquired pneumonia; immobile.
Has two cats.
Drives a car.
Photographs local wildlife.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Her sister sprained a thumb last month.
Knits as a hobby.
Her wife has recovered from a dislocated finger.
Bowel habit normal, without any blood in the stool.
Zinc of 85 mcg/dL in 2010.
Plays the piano.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Her roommate burned a hand on a stove years ago.
Prefers morning appointments.
Teeth in good repair.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
```


## author2 / group 50: `rule_v1.test.gs094.c1.negation.easy.243`

Rule: For primary prevention, prescribe atorvastatin. If the patient has ever had heart failure (current or past) and the age of the patient is 75 years or more, prescribe ezetimibe instead.

**base** (program answer: s; facts: patient: age = 83; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Sees a dentist yearly.
Currently aged 83 years.
```

**flip** (program answer: s'; facts: patient: heart failure; present; past (2014) | patient: age = 83; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2014 and off all heart medicines since.
Sees a dentist yearly.
Currently aged 83 years.
```

**near** (program answer: s; facts: patient: heart failure; absent; current | patient: age = 83; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Has never had heart failure.
Sees a dentist yearly.
Currently aged 83 years.
```

**pres** (program answer: s; facts: patient: age = 83; present; current)
```
An adult man.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Current age 83 years.
Sees a dentist yearly.
```

**missing** (program answer: neither; facts: patient: heart failure; unknown; current | patient: age = 83; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Heart failure: status unclear from the records at hand.
Sees a dentist yearly.
Currently aged 83 years.
```


## author3 / group 51: `rule_v1.test.s2_orbit.egfr.numeric.alt.144`

Rule: ORBIT bleeding score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for a current age of 75 years or more, a current eGFR below 75 mL/min/1.73 m2, and current use of aspirin. Other ORBIT items are not part of this question.

**base** (program answer: s; facts: patient: aspirin use; absent; current | patient: bleeding history; absent; current | patient: age = 56; present; current | patient: eGFR = 96; present; current)
```
Woman, adult.
Atrial fibrillation; starting apixaban is being considered.
Antiplatelet therapy: none at present.
Examination shows no signs of blood loss.
Plays the piano.
Current age 56 years.
Owns a bicycle.
Current eGFR 96 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: aspirin use; absent; current | patient: bleeding history; absent; current | patient: age = 56; present; current | patient: eGFR = 73; present; current)
```
Woman, adult.
Atrial fibrillation; starting apixaban is being considered.
Antiplatelet therapy: none at present.
Examination shows no signs of blood loss.
Plays the piano.
Current age 56 years.
Owns a bicycle.
Current eGFR 73 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: aspirin use; absent; current | patient: bleeding history; absent; current | patient: age = 56; present; current | patient: eGFR = 77; present; current)
```
Woman, adult.
Atrial fibrillation; starting apixaban is being considered.
Antiplatelet therapy: none at present.
Examination shows no signs of blood loss.
Plays the piano.
Current age 56 years.
Owns a bicycle.
Current eGFR 77 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: age = 56; present; current | patient: eGFR = 96; present; current | patient: aspirin use; absent; current | patient: bleeding history; absent; current)
```
An adult woman.
Atrial fibrillation; starting apixaban is being considered.
Currently aged 56 years.
eGFR now 96 mL/min/1.73 m2.
Owns a bicycle.
Plays the piano.
Antiplatelet therapy: none at present.
Examination shows no signs of blood loss.
```


## author4 / group 52: `rule_v1.test.t2d_metformin.egfr.numeric.alt.939`

Rule: For newly diagnosed type 2 diabetes, start metformin. If the patient's current eGFR is below 45 mL/min/1.73 m2, start sitagliptin instead.

**base** (program answer: s; facts: patient: eGFR = 58; present; current)
```
Male patient of 47 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current eGFR 58 mL/min/1.73 m2.
Sleeps seven hours a night.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: eGFR = 34; present; current)
```
Male patient of 47 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current eGFR 34 mL/min/1.73 m2.
Sleeps seven hours a night.
Sees a dentist yearly.
```

**near** (program answer: s; facts: patient: eGFR = 50; present; current)
```
Male patient of 47 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current eGFR 50 mL/min/1.73 m2.
Sleeps seven hours a night.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: patient: eGFR = 58; present; current)
```
Man of 47 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sees a dentist yearly.
Sleeps seven hours a night.
eGFR now 58 mL/min/1.73 m2.
```


## author1 / group 53: `rule_v1.test.gs188.c2.time.easy.627`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: venous thromboembolism; present; current | patient: peptic ulcer at any time; absent; current | patient: ALT = 38; present; current | patient: ALT = 33; present; past (2022))
```
Female patient of 81 years.
Spreading redness and warmth of the right shin for two days.
Sees a dentist yearly.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Appetite good; no indigestion.
Current ALT 38 U/L.
Drives a car.
Records from 2022 list ALT at 33 U/L.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; present; current | patient: peptic ulcer at any time; absent; current | patient: ALT = 143; present; current | patient: ALT = 33; present; past (2022))
```
Female patient of 81 years.
Spreading redness and warmth of the right shin for two days.
Sees a dentist yearly.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Appetite good; no indigestion.
Current ALT 143 U/L.
Drives a car.
Records from 2022 list ALT at 33 U/L.
```

**near** (program answer: s; facts: patient: venous thromboembolism; present; current | patient: peptic ulcer at any time; absent; current | patient: ALT = 38; present; current | patient: ALT = 126; present; past (2022))
```
Female patient of 81 years.
Spreading redness and warmth of the right shin for two days.
Sees a dentist yearly.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Appetite good; no indigestion.
Current ALT 38 U/L.
Drives a car.
Records from 2022 list ALT at 126 U/L.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: ALT = 33; present; past (2022) | patient: venous thromboembolism; present; current | patient: ALT = 38; present; current)
```
Woman of 81 years.
Spreading redness and warmth of the right shin for two days.
Appetite good; no indigestion.
Drives a car.
Back in 2022, ALT stood at 33 U/L.
Sees a dentist yearly.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
ALT now 38 U/L.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism; present; current | patient: peptic ulcer at any time; absent; current)
```
Female patient of 81 years.
Spreading redness and warmth of the right shin for two days.
Sees a dentist yearly.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
Appetite good; no indigestion.
Drives a car.
```


## author2 / group 54: `rule_v1.test.gs048.c1.numeric.long.155`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: weight = 73; present; current | patient: age = 60; present; current)
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

**flip** (program answer: s'; facts: patient: weight = 60; present; current | patient: age = 60; present; current)
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

**near** (program answer: s; facts: patient: weight = 61; present; current | patient: age = 60; present; current)
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

**pres** (program answer: s; facts: patient: age = 60; present; current | patient: weight = 73; present; current)
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


## author3 / group 55: `rule_v1.test.gs118.c4.numeric.easy.1445`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: eGFR = 80; present; current | patient: angioedema; present; current | patient: white cell count = 5.1; present; current | patient: heart rate = 63; present; current)
```
Woman of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current eGFR 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Prefers to be addressed by first name.
Latest WBC is 5.1 x10^9/L.
Heart rate now 63/min on a pulse check.
```

**flip** (program answer: s'; facts: patient: eGFR = 80; present; current | patient: angioedema; present; current | patient: white cell count = 5.1; present; current | patient: heart rate = 99; present; current)
```
Woman of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current eGFR 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Prefers to be addressed by first name.
Latest WBC is 5.1 x10^9/L.
Heart rate now 99/min on a pulse check.
```

**near** (program answer: s; facts: patient: eGFR = 80; present; current | patient: angioedema; present; current | patient: white cell count = 5.1; present; current | patient: heart rate = 89; present; current)
```
Woman of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current eGFR 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Prefers to be addressed by first name.
Latest WBC is 5.1 x10^9/L.
Heart rate now 89/min on a pulse check.
```

**pres** (program answer: s; facts: patient: eGFR = 80; present; current | patient: angioedema; present; current | patient: white cell count = 5.1; present; current | patient: heart rate = 63; present; current)
```
Female patient of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Prefers to be addressed by first name.
eGFR now 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Current white cell count 5.1 x10^9/L.
Current heart rate 63/min.
```


## author4 / group 56: `rule_v1.test.gs216.c2.negation.easy.1337`

Rule: For primary prevention, prescribe atorvastatin. If the age of the patient is 75 years or more and the patient has ever had a venous thromboembolism (current or past), prescribe ezetimibe instead.

**base** (program answer: s; facts: patient: age = 80; present; current | patient: venous thromboembolism; absent; current)
```
An adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 80 years.
Varicose veins: none seen.
Drives a car.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: age = 80; present; current | patient: venous thromboembolism; present; current)
```
An adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 80 years.
Has an acute pulmonary embolism, diagnosed this week.
Drives a car.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: age = 80; present; current | patient: venous thromboembolism; absent; current)
```
An adult woman.
Primary prevention; LDL cholesterol 182 mg/dL.
Current age 80 years.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
Drives a car.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: age = 80; present; current)
```
Woman, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Varicose veins: none seen.
Currently aged 80 years.
Pupils equal and reactive to light.
Drives a car.
Lives in a second-floor apartment.
```


## author1 / group 57: `rule_v1.test.gs047.c1.time.easy.494`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: serum potassium = 4.1; present; current | father: venous thromboembolism (patient or first-degree relative); present; past (2019) | patient: serum potassium = 3.9; present; past (2014))
```
Woman of 41 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Latest potassium result: 4.1 mmol/L.
Her father recovered from a pulmonary embolism in 2019.
Knits as a hobby.
Back in 2014, serum potassium stood at 3.9 mmol/L.
```

**flip** (program answer: s'; facts: patient: serum potassium = 5.6; present; current | father: venous thromboembolism (patient or first-degree relative); present; past (2019) | patient: serum potassium = 3.9; present; past (2014))
```
Woman of 41 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Latest potassium result: 5.6 mmol/L.
Her father recovered from a pulmonary embolism in 2019.
Knits as a hobby.
Back in 2014, serum potassium stood at 3.9 mmol/L.
```

**near** (program answer: s; facts: patient: serum potassium = 4.1; present; current | father: venous thromboembolism (patient or first-degree relative); present; past (2019) | patient: serum potassium = 5.8; present; past (2014))
```
Woman of 41 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Latest potassium result: 4.1 mmol/L.
Her father recovered from a pulmonary embolism in 2019.
Knits as a hobby.
Back in 2014, serum potassium stood at 5.8 mmol/L.
```

**pres** (program answer: s; facts: patient: serum potassium = 3.9; present; past (2014) | father: venous thromboembolism (patient or first-degree relative); present; past (2019) | patient: serum potassium = 4.1; present; current)
```
Female patient of 41 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Records from 2014 list serum potassium at 3.9 mmol/L.
Her father recovered from a pulmonary embolism in 2019.
Knits as a hobby.
Current serum potassium 4.1 mmol/L.
```

**missing** (program answer: neither; facts: father: venous thromboembolism (patient or first-degree relative); present; past (2019))
```
Woman of 41 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Her father recovered from a pulmonary embolism in 2019.
Knits as a hobby.
```


## author2 / group 58: `rule_v1.test.gs011.c1.subject.long.87`

Rule: For acute streptococcal pharyngitis, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time and the current ALT is above 120 U/L, prescribe azithromycin instead.

**base** (program answer: s; facts: patient: ALT = 138; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current)
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

**flip** (program answer: s'; facts: patient: ALT = 138; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
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

**near** (program answer: s; facts: patient: ALT = 138; present; current | uncle: venous thromboembolism (patient or first-degree relative); present; current)
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

**pres** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: ALT = 138; present; current)
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


## author3 / group 59: `rule_v1.test.gs044.c1.numeric.easy.734`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

**base** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: peptic ulcer at any time; present; past (2010) | patient: age = 53; present; current)
```
Woman, adult.
Suspected chest infection; assessed on the medical ward.
Walks without calf pain.
Prefers morning appointments.
Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.
Teeth in good repair.
Has two cats.
Current age 53 years.
```

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: peptic ulcer at any time; present; past (2010) | patient: age = 65; present; current)
```
Woman, adult.
Suspected chest infection; assessed on the medical ward.
Walks without calf pain.
Prefers morning appointments.
Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.
Teeth in good repair.
Has two cats.
Current age 65 years.
```

**near** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: peptic ulcer at any time; present; past (2010) | patient: age = 62; present; current)
```
Woman, adult.
Suspected chest infection; assessed on the medical ward.
Walks without calf pain.
Prefers morning appointments.
Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.
Teeth in good repair.
Has two cats.
Current age 62 years.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; present; past (2010) | patient: myocardial infarction or peripheral artery disease; absent; current | patient: age = 53; present; current)
```
An adult woman.
Suspected chest infection; assessed on the medical ward.
Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.
Has two cats.
Prefers morning appointments.
Walks without calf pain.
Currently aged 53 years.
Teeth in good repair.
```

**missing** (program answer: neither; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: peptic ulcer at any time; present; past (2010))
```
Woman, adult.
Suspected chest infection; assessed on the medical ward.
Walks without calf pain.
Prefers morning appointments.
Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.
Teeth in good repair.
Has two cats.
```


## author4 / group 60: `rule_v1.test.gs001.c1.numeric.long.631`

Rule: For contraception, prescribe a combined oral contraceptive. Score 1 point if the current platelet count is below 50 x10^9/L; 1 point if the patient is currently taking warfarin; 1 point if the patient has ever had diabetes (current or past); 3 points if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: mechanical heart valve; present; current | patient: platelet count = 315; present; current | patient: warfarin; present; current | patient: diabetes; absent; current)
```
Woman of 35 years.
Requests contraception.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Plays the piano.
During a checkup in 2016, total protein was 7.0 g/dL.
Photographs local wildlife.
Lives in a second-floor apartment.
Lives with a mechanical aortic valve prosthesis.
Teeth in good repair.
Platelet count now 315 x10^9/L.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2022.
Pupils equal and reactive to light.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Knits as a hobby.
Her roommate has a lazy eye.
Her father sprained a thumb last month.
Her wife lives with psoriasis.
In 2009, lipase was 30 U/L.
HbA1c 5.3% at a routine check.
Prefers to be addressed by first name.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: mechanical heart valve; present; current | patient: platelet count = 40; present; current | patient: warfarin; present; current | patient: diabetes; absent; current)
```
Woman of 35 years.
Requests contraception.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Plays the piano.
During a checkup in 2016, total protein was 7.0 g/dL.
Photographs local wildlife.
Lives in a second-floor apartment.
Lives with a mechanical aortic valve prosthesis.
Teeth in good repair.
Platelet count now 40 x10^9/L.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2022.
Pupils equal and reactive to light.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Knits as a hobby.
Her roommate has a lazy eye.
Her father sprained a thumb last month.
Her wife lives with psoriasis.
In 2009, lipase was 30 U/L.
HbA1c 5.3% at a routine check.
Prefers to be addressed by first name.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: mechanical heart valve; present; current | patient: platelet count = 55; present; current | patient: warfarin; present; current | patient: diabetes; absent; current)
```
Woman of 35 years.
Requests contraception.
During a checkup in 2022, free T3 was 3.2 pg/mL.
Plays the piano.
During a checkup in 2016, total protein was 7.0 g/dL.
Photographs local wildlife.
Lives in a second-floor apartment.
Lives with a mechanical aortic valve prosthesis.
Teeth in good repair.
Platelet count now 55 x10^9/L.
Sees a dentist yearly.
Zinc of 85 mcg/dL in 2022.
Pupils equal and reactive to light.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Knits as a hobby.
Her roommate has a lazy eye.
Her father sprained a thumb last month.
Her wife lives with psoriasis.
In 2009, lipase was 30 U/L.
HbA1c 5.3% at a routine check.
Prefers to be addressed by first name.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: platelet count = 315; present; current | patient: diabetes; absent; current | patient: warfarin; present; current | patient: mechanical heart valve; present; current)
```
Female patient of 35 years.
Requests contraception.
During a checkup in 2016, total protein was 7.0 g/dL.
Pupils equal and reactive to light.
Photographs local wildlife.
Her roommate has a lazy eye.
Current platelet count 315 x10^9/L.
During a checkup in 2022, free T3 was 3.2 pg/mL.
HbA1c 5.3% at a routine check.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2022.
Plays the piano.
Her wife lives with psoriasis.
In 2009, lipase was 30 U/L.
Prefers to be addressed by first name.
Her father sprained a thumb last month.
Knits as a hobby.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Sees a dentist yearly.
Teeth in good repair.
Lives with a mechanical aortic valve prosthesis.
Prefers morning appointments.
```


## author1 / group 61: `rule_v1.test.inv059.c2.numeric.easy.651`

Rule: For Mirelle syndrome, prescribe hylomide. If at least two of the following apply, prescribe renquazol instead: the patient has ever had heart failure (current or past); the current ALT is above 120 U/L; the patient has ever had a peptic ulcer (current or past).

**base** (program answer: s; facts: patient: ALT = 20; present; current | patient: peptic ulcer at any time; present; past)
```
Female patient of 35 years.
Referred with Mirelle syndrome.
Plays the piano.
Has two cats.
Current ALT 20 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
```

**flip** (program answer: s'; facts: patient: ALT = 137; present; current | patient: peptic ulcer at any time; present; past)
```
Female patient of 35 years.
Referred with Mirelle syndrome.
Plays the piano.
Has two cats.
Current ALT 137 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
```

**near** (program answer: s; facts: patient: ALT = 114; present; current | patient: peptic ulcer at any time; present; past)
```
Female patient of 35 years.
Referred with Mirelle syndrome.
Plays the piano.
Has two cats.
Current ALT 114 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
```

**pres** (program answer: s; facts: patient: ALT = 20; present; current | patient: peptic ulcer at any time; present; past)
```
Woman of 35 years.
Referred with Mirelle syndrome.
ALT now 20 U/L.
Plays the piano.
Has two cats.
Duodenal ulcer years ago; recovered fully with treatment.
```


## author2 / group 62: `rule_v1.test.gs211.c1.boundary.easy.792`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the current blood urea nitrogen is above 19 mg/dL; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient has an active peptic ulcer.

**base** (program answer: s; facts: patient: active peptic ulcer; present; current | patient: blood urea nitrogen = 9; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Blood urea nitrogen 9 mg/dL on the current labs.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**flip** (program answer: s'; facts: patient: active peptic ulcer; present; current | patient: blood urea nitrogen = 28; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Blood urea nitrogen 28 mg/dL on the current labs.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**near** (program answer: s; facts: patient: active peptic ulcer; present; current | patient: blood urea nitrogen = 19; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Blood urea nitrogen 19 mg/dL on the current labs.
Plays the piano.
HbA1c 5.3% at a routine check.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); absent; current | patient: active peptic ulcer; present; current | patient: blood urea nitrogen = 9; present; current)
```
Female patient of 54 years.
Atrial fibrillation; anticoagulation indicated.
HbA1c 5.3% at a routine check.
Has an active duodenal ulcer.
Blood urea nitrogen now: 9 mg/dL.
Plays the piano.
```

**missing** (program answer: neither; facts: patient: active peptic ulcer; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 54 years.
Atrial fibrillation; anticoagulation indicated.
Has an active duodenal ulcer.
Plays the piano.
HbA1c 5.3% at a routine check.
```


## author3 / group 63: `rule_v1.test.qsofa.mentation.time.easy.1609`

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**base** (program answer: s; facts: patient: respiratory rate = 15; present; current | patient: altered mentation; absent; current | patient: systolic blood pressure = 128; present; current)
```
Man of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 15/min.
Gives a clear account of the illness.
Current systolic blood pressure 128 mmHg.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: respiratory rate = 15; present; current | patient: altered mentation; present; current | patient: systolic blood pressure = 128; present; current)
```
Man of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 15/min.
Newly disoriented and unable to give a clear history.
Current systolic blood pressure 128 mmHg.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: respiratory rate = 15; present; current | patient: altered mentation; present; past | patient: systolic blood pressure = 128; present; current)
```
Man of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 15/min.
Was confused for a day after surgery years ago; recovered fully.
Current systolic blood pressure 128 mmHg.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 128; present; current | patient: altered mentation; absent; current | patient: respiratory rate = 15; present; current)
```
Male patient of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: blood pressure 128/85 mmHg.
Gives a clear account of the illness.
Paints watercolors as a hobby.
Current respiratory rate 15/min.
```


## author4 / group 64: `rule_v1.test.s1_spesi.cancer.negation.long.1209`

Rule: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: age = 62; present; current | patient: oxygen saturation = 100; present; current | patient: heart rate = 90; present; current | patient: systolic blood pressure = 121; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
His uncle has recovered from a dislocated finger.
In 2010, folate was 12 ng/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
Plays the piano.
Weight steady over the past year.
Currently aged 62 years.
His father wears contact lenses.
Pupils equal and reactive to light.
Has two cats.
Current oxygen saturation 100%.
Heart rate now 90/min on a pulse check.
Sees a dentist yearly.
Enjoys board games.
Observations now: blood pressure 121/82 mmHg.
Photographs local wildlife.
In 2016, lipase was 30 U/L.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Owns a bicycle.
Paints watercolors as a hobby.
His wife lives with psoriasis.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: active cancer; present; current | patient: age = 62; present; current | patient: oxygen saturation = 100; present; current | patient: heart rate = 90; present; current | patient: systolic blood pressure = 121; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
His uncle has recovered from a dislocated finger.
In 2010, folate was 12 ng/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
Plays the piano.
Has melanoma skin cancer and is receiving treatment for it.
Currently aged 62 years.
His father wears contact lenses.
Pupils equal and reactive to light.
Has two cats.
Current oxygen saturation 100%.
Heart rate now 90/min on a pulse check.
Sees a dentist yearly.
Enjoys board games.
Observations now: blood pressure 121/82 mmHg.
Photographs local wildlife.
In 2016, lipase was 30 U/L.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Owns a bicycle.
Paints watercolors as a hobby.
His wife lives with psoriasis.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: age = 62; present; current | patient: oxygen saturation = 100; present; current | patient: heart rate = 90; present; current | patient: systolic blood pressure = 121; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
His uncle has recovered from a dislocated finger.
In 2010, folate was 12 ng/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
Plays the piano.
Free of cancer throughout life.
Currently aged 62 years.
His father wears contact lenses.
Pupils equal and reactive to light.
Has two cats.
Current oxygen saturation 100%.
Heart rate now 90/min on a pulse check.
Sees a dentist yearly.
Enjoys board games.
Observations now: blood pressure 121/82 mmHg.
Photographs local wildlife.
In 2016, lipase was 30 U/L.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Owns a bicycle.
Paints watercolors as a hobby.
His wife lives with psoriasis.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: age = 62; present; current | patient: heart rate = 90; present; current | patient: active cancer; absent; current | patient: systolic blood pressure = 121; present; current | patient: oxygen saturation = 100; present; current)
```
An adult man.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Has two cats.
In 2016, lipase was 30 U/L.
Current age 62 years.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
Current heart rate 90/min.
Weight steady over the past year.
Sleeps seven hours a night.
Plays the piano.
Current systolic blood pressure 121 mmHg.
His father wears contact lenses.
Prefers morning appointments.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Photographs local wildlife.
Latest oxygen saturation reading: 100%.
His wife lives with psoriasis.
Enjoys board games.
His friend sprained a thumb last month.
Owns a bicycle.
His uncle has recovered from a dislocated finger.
In 2010, folate was 12 ng/mL.
```


## author1 / group 65: `rule_v1.test.inv020.c2.boundary.easy.570`

Rule: For Hestin disease, prescribe melcadine. If the current systolic blood pressure is 100 mmHg or less or the current temperature is above 38.0 C, prescribe orvitrex instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 133; present; current | patient: temperature = 37.2; present; current)
```
Man of 25 years.
Referred with Hestin disease.
Observations now: blood pressure 133/88 mmHg.
Current temperature 37.2 C.
Sleeps seven hours a night.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 133; present; current | patient: temperature = 38.6; present; current)
```
Man of 25 years.
Referred with Hestin disease.
Observations now: blood pressure 133/88 mmHg.
Current temperature 38.6 C.
Sleeps seven hours a night.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 133; present; current | patient: temperature = 38.0; present; current)
```
Man of 25 years.
Referred with Hestin disease.
Observations now: blood pressure 133/88 mmHg.
Current temperature 38.0 C.
Sleeps seven hours a night.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 133; present; current | patient: temperature = 37.2; present; current)
```
Male patient of 25 years.
Referred with Hestin disease.
Current systolic blood pressure 133 mmHg.
Knits as a hobby.
Sleeps seven hours a night.
Temperature now 37.2 C (tympanic).
```


## author2 / group 66: `rule_v1.test.gs139.c1.time.easy.1320`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: tender cervical lymph nodes; absent; current | patient: angioedema; present; past)
```
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Front of the neck without tenderness or swelling.
An episode of angioedema years ago, with full recovery.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: tender cervical lymph nodes; present; current | patient: angioedema; present; past)
```
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Tender, swollen lymph nodes in the front of the neck.
An episode of angioedema years ago, with full recovery.
Enjoys board games.
```

**near** (program answer: s; facts: patient: tender cervical lymph nodes; present; past | patient: angioedema; present; past)
```
Woman of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Tender anterior cervical lymph nodes with a throat infection years ago, which went down within two weeks.
An episode of angioedema years ago, with full recovery.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: angioedema; present; past | patient: tender cervical lymph nodes; absent; current)
```
Female patient of 35 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Enjoys board games.
An episode of angioedema years ago, with full recovery.
Front of the neck without tenderness or swelling.
```


## author3 / group 67: `rule_v1.test.gs118.c2.subject.easy.142`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: heart rate = 68; present; current | patient: angioedema; absent; current | patient: white cell count = 9.8; present; current | patient: eGFR = 41; present; current)
```
Man of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Has two cats.
Current heart rate 68/min.
Free of facial or oropharyngeal edema.
Current white cell count 9.8 x10^9/L.
eGFR now 41 mL/min/1.73 m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: heart rate = 68; present; current | patient: angioedema; present; past | patient: white cell count = 9.8; present; current | patient: eGFR = 41; present; current)
```
Man of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Has two cats.
Current heart rate 68/min.
Formerly had recurrent angioedema, in remission for many years now.
Current white cell count 9.8 x10^9/L.
eGFR now 41 mL/min/1.73 m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: heart rate = 68; present; current | father: angioedema; present; past | patient: white cell count = 9.8; present; current | patient: eGFR = 41; present; current)
```
Man of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Has two cats.
Current heart rate 68/min.
His father had an attack of angioedema years ago.
Current white cell count 9.8 x10^9/L.
eGFR now 41 mL/min/1.73 m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: angioedema; absent; current | patient: heart rate = 68; present; current | patient: white cell count = 9.8; present; current | patient: eGFR = 41; present; current)
```
Male patient of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Free of facial or oropharyngeal edema.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Has two cats.
Heart rate now 68/min on a pulse check.
Drives a car.
Latest WBC is 9.8 x10^9/L.
Current eGFR 41 mL/min/1.73 m2.
```

**missing** (program answer: neither; facts: patient: heart rate = 68; present; current | patient: angioedema; unknown; current | patient: white cell count = 9.8; present; current | patient: eGFR = 41; present; current)
```
Man of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
Has two cats.
Current heart rate 68/min.
Angioedema: unknown.
Current white cell count 9.8 x10^9/L.
eGFR now 41 mL/min/1.73 m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```


## author4 / group 68: `rule_v1.test.c1_neutropenia.anc.numeric.alt.395`

Rule: For a chest infection during chemotherapy, prescribe oral co-amoxiclav. If the current neutrophil count is 1.0 x10^9/L or less, prescribe intravenous piperacillin-tazobactam instead.

**base** (program answer: s; facts: patient: neutrophil count = 2.0; present; current)
```
Man of 60 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Has two cats.
Current neutrophil count 2.0 x10^9/L.
```

**flip** (program answer: s'; facts: patient: neutrophil count = 0.8; present; current)
```
Man of 60 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Has two cats.
Current neutrophil count 0.8 x10^9/L.
```

**near** (program answer: s; facts: patient: neutrophil count = 1.1; present; current)
```
Man of 60 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Has two cats.
Current neutrophil count 1.1 x10^9/L.
```

**pres** (program answer: s; facts: patient: neutrophil count = 2.0; present; current)
```
Male patient of 60 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Latest neutrophil count: 2.0 x10^9/L.
Has two cats.
```


## author1 / group 69: `rule_v1.test.gs071.c1.time.superseded.697`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**base** (program answer: s; facts: patient: temperature = 36.9; present; past | patient: temperature = 37.3; present; current | patient: peptic ulcer at any time; present; current)
```
Woman of 59 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Earlier this week, temperature was 36.9 C; a newer reading supersedes it.
Temperature now 37.3 C (tympanic).
Pupils equal and reactive to light.
Has an active duodenal ulcer.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: temperature = 36.9; present; past | patient: temperature = 38.7; present; current | patient: peptic ulcer at any time; present; current)
```
Woman of 59 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Earlier this week, temperature was 36.9 C; a newer reading supersedes it.
Temperature now 38.7 C (tympanic).
Pupils equal and reactive to light.
Has an active duodenal ulcer.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: temperature = 38.4; present; past | patient: temperature = 37.3; present; current | patient: peptic ulcer at any time; present; current)
```
Woman of 59 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Earlier this week, temperature was 38.4 C; a newer reading supersedes it.
Temperature now 37.3 C (tympanic).
Pupils equal and reactive to light.
Has an active duodenal ulcer.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: temperature = 37.3; present; current | patient: peptic ulcer at any time; present; current | patient: temperature = 36.9; present; past)
```
Female patient of 59 years.
Atrial fibrillation; anticoagulation indicated.
Knits as a hobby.
Pupils equal and reactive to light.
Current temperature 37.3 C.
Has an active duodenal ulcer.
Sees a dentist yearly.
Earlier this week, temperature was 36.9 C; a newer reading supersedes it.
```

**missing** (program answer: neither; facts: patient: peptic ulcer at any time; present; current)
```
Woman of 59 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Pupils equal and reactive to light.
Has an active duodenal ulcer.
Knits as a hobby.
```


## author2 / group 70: `rule_v1.test.gs124.c2.numeric.long.949`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**base** (program answer: s; facts: father: colorectal cancer (patient or first-degree relative); present; current | patient: age = 54; present; current | patient: calf swelling = 0.4; present; current)
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

**flip** (program answer: s'; facts: father: colorectal cancer (patient or first-degree relative); present; current | patient: age = 54; present; current | patient: calf swelling = 3.0; present; current)
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

**near** (program answer: s; facts: father: colorectal cancer (patient or first-degree relative); present; current | patient: age = 54; present; current | patient: calf swelling = 2.7; present; current)
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

**pres** (program answer: s; facts: patient: calf swelling = 0.4; present; current | patient: age = 54; present; current | father: colorectal cancer (patient or first-degree relative); present; current)
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


## author3 / group 71: `rule_v1.test.statin_alt.alt.numeric.alt.103`

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**base** (program answer: s; facts: patient: ALT = 25; present; current)
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Photographs local wildlife.
Current ALT 25 U/L.
```

**flip** (program answer: s'; facts: patient: ALT = 94; present; current)
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Photographs local wildlife.
Current ALT 94 U/L.
```

**near** (program answer: s; facts: patient: ALT = 77; present; current)
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Photographs local wildlife.
Current ALT 77 U/L.
```

**pres** (program answer: s; facts: patient: ALT = 25; present; current)
```
Female patient of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
ALT now 25 U/L.
Photographs local wildlife.
```


## author4 / group 72: `rule_v1.test.gs088.c3.numeric.long.1124`

Rule: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: myocardial infarction or peripheral artery disease; present; past | patient: white cell count = 7.1; present; current)
```
Male patient of 54 years.
Sore throat for two days.
Plays the piano.
Sleeps seven hours a night.
In 2009, folate was 12 ng/mL.
His uncle wears contact lenses.
Prefers morning appointments.
Tonsils pink and clean on inspection.
Prefers to be addressed by first name.
Owns a bicycle.
Photographs local wildlife.
Knits as a hobby.
Heart attack years ago, with full recovery.
Current white cell count 7.1 x10^9/L.
His wife has recovered from a dislocated finger.
During a checkup in 2018, total protein was 7.0 g/dL.
Has two cats.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
His friend has a lazy eye.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; absent; current | patient: myocardial infarction or peripheral artery disease; present; past | patient: white cell count = 13.7; present; current)
```
Male patient of 54 years.
Sore throat for two days.
Plays the piano.
Sleeps seven hours a night.
In 2009, folate was 12 ng/mL.
His uncle wears contact lenses.
Prefers morning appointments.
Tonsils pink and clean on inspection.
Prefers to be addressed by first name.
Owns a bicycle.
Photographs local wildlife.
Knits as a hobby.
Heart attack years ago, with full recovery.
Current white cell count 13.7 x10^9/L.
His wife has recovered from a dislocated finger.
During a checkup in 2018, total protein was 7.0 g/dL.
Has two cats.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
His friend has a lazy eye.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: myocardial infarction or peripheral artery disease; present; past | patient: white cell count = 11.6; present; current)
```
Male patient of 54 years.
Sore throat for two days.
Plays the piano.
Sleeps seven hours a night.
In 2009, folate was 12 ng/mL.
His uncle wears contact lenses.
Prefers morning appointments.
Tonsils pink and clean on inspection.
Prefers to be addressed by first name.
Owns a bicycle.
Photographs local wildlife.
Knits as a hobby.
Heart attack years ago, with full recovery.
Current white cell count 11.6 x10^9/L.
His wife has recovered from a dislocated finger.
During a checkup in 2018, total protein was 7.0 g/dL.
Has two cats.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
His friend has a lazy eye.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; present; past | patient: tonsillar exudate; absent; current | patient: white cell count = 7.1; present; current)
```
Man of 54 years.
Sore throat for two days.
Prefers to be addressed by first name.
Has two cats.
His wife has recovered from a dislocated finger.
Sees a dentist yearly.
Paints watercolors as a hobby.
His friend has a lazy eye.
Plays the piano.
Heart attack years ago, with full recovery.
Enjoys board games.
Sleeps seven hours a night.
Prefers morning appointments.
Pupils equal and reactive to light.
Knits as a hobby.
Tonsils pink and clean on inspection.
Lives in a second-floor apartment.
Latest WBC is 7.1 x10^9/L.
Drives a car.
His uncle wears contact lenses.
During a checkup in 2018, total protein was 7.0 g/dL.
In 2009, folate was 12 ng/mL.
Owns a bicycle.
Photographs local wildlife.
```


## author1 / group 73: `rule_v1.test.gs033.c1.time.easy.1770`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.

**base** (program answer: s; facts: patient: weight = 80; present; current | patient: penicillin allergy; absent; current | patient: weight = 67; present; past (2014) | sister: coronary artery disease (patient or first-degree relative); present; past)
```
Man of 80 years.
Spreading redness and warmth of the right shin for two days.
Prefers to be addressed by first name.
Owns a bicycle.
Latest weight 80 kg.
Reports no allergies to medicines.
Photographs local wildlife.
Records from 2014 list weight at 67 kg.
His sister had bypass surgery for coronary artery disease years ago.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: weight = 53; present; current | patient: penicillin allergy; absent; current | patient: weight = 67; present; past (2014) | sister: coronary artery disease (patient or first-degree relative); present; past)
```
Man of 80 years.
Spreading redness and warmth of the right shin for two days.
Prefers to be addressed by first name.
Owns a bicycle.
Latest weight 53 kg.
Reports no allergies to medicines.
Photographs local wildlife.
Records from 2014 list weight at 67 kg.
His sister had bypass surgery for coronary artery disease years ago.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: weight = 80; present; current | patient: penicillin allergy; absent; current | patient: weight = 52; present; past (2014) | sister: coronary artery disease (patient or first-degree relative); present; past)
```
Man of 80 years.
Spreading redness and warmth of the right shin for two days.
Prefers to be addressed by first name.
Owns a bicycle.
Latest weight 80 kg.
Reports no allergies to medicines.
Photographs local wildlife.
Records from 2014 list weight at 52 kg.
His sister had bypass surgery for coronary artery disease years ago.
Knits as a hobby.
```

**pres** (program answer: s; facts: sister: coronary artery disease (patient or first-degree relative); present; past | patient: penicillin allergy; absent; current | patient: weight = 67; present; past (2014) | patient: weight = 80; present; current)
```
Male patient of 80 years.
Spreading redness and warmth of the right shin for two days.
His sister had bypass surgery for coronary artery disease years ago.
Photographs local wildlife.
Knits as a hobby.
Reports no allergies to medicines.
Back in 2014, weight stood at 67 kg.
Current weight 80 kg.
Owns a bicycle.
Prefers to be addressed by first name.
```


## author2 / group 74: `rule_v1.test.s3_hctci.ulcer.subject.easy.643`

Rule: Hematopoietic Cell Transplantation-specific Comorbidity Index (as used here, partial): 1 point for coronary artery disease at any time (current or past); 1 point for a stroke or TIA at any time (current or past); 2 points for a current peptic ulcer; 1 point for a current ALT above 40 U/L. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: active peptic ulcer; absent; current | patient: stroke/TIA; absent; current | patient: ALT = 13; present; current | patient: coronary artery disease; absent; current)
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

**flip** (program answer: s'; facts: patient: active peptic ulcer; present; current | patient: stroke/TIA; absent; current | patient: ALT = 13; present; current | patient: coronary artery disease; absent; current)
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

**near** (program answer: s; facts: wife: active peptic ulcer; present; current | patient: stroke/TIA; absent; current | patient: ALT = 13; present; current | patient: coronary artery disease; absent; current)
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

**pres** (program answer: s; facts: patient: stroke/TIA; absent; current | patient: coronary artery disease; absent; current | patient: active peptic ulcer; absent; current | patient: ALT = 13; present; current)
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


## author3 / group 75: `rule_v1.test.gs220.c1.boundary.easy.273`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: father: diabetes (patient or first-degree relative); present; past | patient: eGFR = 89; present; current)
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
eGFR now 89 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: father: diabetes (patient or first-degree relative); present; past | patient: eGFR = 17; present; current)
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
eGFR now 17 mL/min/1.73 m2.
```

**near** (program answer: s; facts: father: diabetes (patient or first-degree relative); present; past | patient: eGFR = 30; present; current)
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
eGFR now 30 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: father: diabetes (patient or first-degree relative); present; past | patient: eGFR = 89; present; current)
```
Female patient of 19 years.
Requests contraception.
Her father had diabetes years ago that went away after a change in diet.
Has two cats.
Current eGFR 89 mL/min/1.73 m2.
```

**missing** (program answer: neither; facts: father: diabetes (patient or first-degree relative); present; past)
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
```


## author4 / group 76: `rule_v1.test.c3_glaucoma_asthma.asthma.negation.easy.589`

Rule: For primary open-angle glaucoma, prescribe timolol eye drops. If the patient has ever had asthma (current or past), prescribe latanoprost eye drops instead.

**base** (program answer: s; facts: )
```
Female patient of 49 years.
Newly diagnosed primary open-angle glaucoma (intraocular pressure 27 mmHg in both eyes).
Drives a car.
Lives in a second-floor apartment.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: asthma at any time; present; past)
```
Female patient of 49 years.
Newly diagnosed primary open-angle glaucoma (intraocular pressure 27 mmHg in both eyes).
Drives a car.
Lives in a second-floor apartment.
Asthma in the early school years, outgrown long ago.
Plays the piano.
```

**near** (program answer: s; facts: patient: asthma at any time; absent; current)
```
Female patient of 49 years.
Newly diagnosed primary open-angle glaucoma (intraocular pressure 27 mmHg in both eyes).
Drives a car.
Lives in a second-floor apartment.
Asthma ruled out on lung function testing.
Plays the piano.
```

**pres** (program answer: s; facts: )
```
Woman of 49 years.
Newly diagnosed primary open-angle glaucoma (intraocular pressure 27 mmHg in both eyes).
Plays the piano.
Drives a car.
Lives in a second-floor apartment.
```


## author1 / group 77: `rule_v1.test.gs001.c4.time.easy.1215`

Rule: For contraception, prescribe a combined oral contraceptive. Score 1 point if the current platelet count is below 50 x10^9/L; 1 point if the patient is currently taking warfarin; 1 point if the patient has ever had diabetes (current or past); 3 points if the patient currently has a mechanical heart valve. If the score is 5 or more, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: warfarin; present; current | patient: platelet count = 35; present; current | patient: diabetes; absent; current)
```
Female patient of 39 years.
Requests contraception.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Pupils equal and reactive to light.
Knits as a hobby.
Current platelet count 35 x10^9/L.
HbA1c 5.3% at a routine check.
```

**flip** (program answer: s'; facts: patient: warfarin; present; current | patient: platelet count = 35; present; current | patient: mechanical heart valve; present; current | patient: diabetes; absent; current)
```
Female patient of 39 years.
Requests contraception.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Pupils equal and reactive to light.
Knits as a hobby.
Current platelet count 35 x10^9/L.
Mechanical mitral valve in place; metallic closing clicks audible.
HbA1c 5.3% at a routine check.
```

**near** (program answer: s; facts: patient: warfarin; present; current | patient: platelet count = 35; present; current | patient: mechanical heart valve; present; past | patient: diabetes; absent; current)
```
Female patient of 39 years.
Requests contraception.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Pupils equal and reactive to light.
Knits as a hobby.
Current platelet count 35 x10^9/L.
Mechanical aortic valve explanted years ago for valve thrombosis; a bioprosthesis now sits in its place.
HbA1c 5.3% at a routine check.
```

**pres** (program answer: s; facts: patient: platelet count = 35; present; current | patient: warfarin; present; current | patient: diabetes; absent; current)
```
Woman of 39 years.
Requests contraception.
Platelet count now 35 x10^9/L.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Knits as a hobby.
Pupils equal and reactive to light.
HbA1c 5.3% at a routine check.
```


## author2 / group 78: `rule_v1.test.gs143.c2.numeric.long.190`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has active cancer; the age of the patient is 65 years or more; the current ALT is above 120 U/L.

**base** (program answer: s; facts: patient: active cancer; present; current | patient: age = 49; present; current | patient: ALT = 24; present; current)
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

**flip** (program answer: s'; facts: patient: active cancer; present; current | patient: age = 70; present; current | patient: ALT = 24; present; current)
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

**near** (program answer: s; facts: patient: active cancer; present; current | patient: age = 64; present; current | patient: ALT = 24; present; current)
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

**pres** (program answer: s; facts: patient: age = 49; present; current | patient: ALT = 24; present; current | patient: active cancer; present; current)
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


## author3 / group 79: `rule_v1.test.gs037.c3.numeric.easy.1155`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. Score 1 point if the patient has ever had angioedema (current or past); 1 point if the patient has new confusion; 2 points if the current temperature is above 38.0 C; 2 points if the age of the patient is 65 years or more. If the score is 5 or more, prescribe intermittent pneumatic compression instead.

**base** (program answer: s; facts: patient: temperature = 37.4; present; current | patient: age = 68; present; current | patient: new confusion; absent; current | patient: angioedema; present; past)
```
An adult man.
Admitted for community-acquired pneumonia; immobile.
Current temperature 37.4 C.
Currently aged 68 years.
Prefers morning appointments.
Speech clear; follows commands.
An episode of angioedema years ago, with full recovery.
```

**flip** (program answer: s'; facts: patient: temperature = 39.1; present; current | patient: age = 68; present; current | patient: new confusion; absent; current | patient: angioedema; present; past)
```
An adult man.
Admitted for community-acquired pneumonia; immobile.
Current temperature 39.1 C.
Currently aged 68 years.
Prefers morning appointments.
Speech clear; follows commands.
An episode of angioedema years ago, with full recovery.
```

**near** (program answer: s; facts: patient: temperature = 37.8; present; current | patient: age = 68; present; current | patient: new confusion; absent; current | patient: angioedema; present; past)
```
An adult man.
Admitted for community-acquired pneumonia; immobile.
Current temperature 37.8 C.
Currently aged 68 years.
Prefers morning appointments.
Speech clear; follows commands.
An episode of angioedema years ago, with full recovery.
```

**pres** (program answer: s; facts: patient: angioedema; present; past | patient: new confusion; absent; current | patient: temperature = 37.4; present; current | patient: age = 68; present; current)
```
Man, adult.
Admitted for community-acquired pneumonia; immobile.
An episode of angioedema years ago, with full recovery.
Speech clear; follows commands.
Temperature now 37.4 C (tympanic).
Prefers morning appointments.
Current age 68 years.
```


## author4 / group 80: `rule_v1.test.hf_spironolactone.k.boundary.alt.828`

Rule: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 4.5 mmol/L, add dapagliflozin instead.

**base** (program answer: s; facts: patient: potassium = 3.8; present; current)
```
Woman of 69 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Prefers morning appointments.
Sleeps seven hours a night.
Latest potassium result: 3.8 mmol/L.
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: potassium = 5.0; present; current)
```
Woman of 69 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Prefers morning appointments.
Sleeps seven hours a night.
Latest potassium result: 5.0 mmol/L.
Teeth in good repair.
```

**near** (program answer: s; facts: patient: potassium = 4.5; present; current)
```
Woman of 69 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Prefers morning appointments.
Sleeps seven hours a night.
Latest potassium result: 4.5 mmol/L.
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: potassium = 3.8; present; current)
```
Female patient of 69 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 3.8 mmol/L.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Teeth in good repair.
Prefers morning appointments.
```


## author1 / group 81: `rule_v1.test.inv039.c3.numeric.easy.227`

Rule: For Pallis disease, prescribe brexadol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 2 points if the current ALT is above 120 U/L; 3 points if the current eGFR is below 30 mL/min/1.73 m2. If the score is 4 or more, prescribe corlitane instead.

**base** (program answer: s; facts: patient: eGFR = 81; present; current | patient: ALT = 15; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
```
Woman of 26 years.
Referred with Pallis disease.
Owns a bicycle.
Teeth in good repair.
eGFR now 81 mL/min/1.73 m2.
ALT now 15 U/L.
Prefers to be addressed by first name.
Has an acute pulmonary embolism, diagnosed this week.
```

**flip** (program answer: s'; facts: patient: eGFR = 15; present; current | patient: ALT = 15; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
```
Woman of 26 years.
Referred with Pallis disease.
Owns a bicycle.
Teeth in good repair.
eGFR now 15 mL/min/1.73 m2.
ALT now 15 U/L.
Prefers to be addressed by first name.
Has an acute pulmonary embolism, diagnosed this week.
```

**near** (program answer: s; facts: patient: eGFR = 33; present; current | patient: ALT = 15; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
```
Woman of 26 years.
Referred with Pallis disease.
Owns a bicycle.
Teeth in good repair.
eGFR now 33 mL/min/1.73 m2.
ALT now 15 U/L.
Prefers to be addressed by first name.
Has an acute pulmonary embolism, diagnosed this week.
```

**pres** (program answer: s; facts: patient: ALT = 15; present; current | patient: eGFR = 81; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
```
Female patient of 26 years.
Referred with Pallis disease.
Current ALT 15 U/L.
Prefers to be addressed by first name.
Current eGFR 81 mL/min/1.73 m2.
Teeth in good repair.
Has an acute pulmonary embolism, diagnosed this week.
Owns a bicycle.
```


## author2 / group 82: `rule_v1.test.gs033.c1.numeric.easy.1182`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the current weight is 60 kg or less; the patient is allergic to penicillin; the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time.

**base** (program answer: s; facts: sister: coronary artery disease (patient or first-degree relative); present; current | patient: weight = 92; present; current)
```
Female patient of 80 years.
Spreading redness and warmth of the right shin for two days.
Teeth in good repair.
Prefers to be addressed by first name.
Her sister has known coronary artery disease.
Current weight 92 kg.
```

**flip** (program answer: s'; facts: sister: coronary artery disease (patient or first-degree relative); present; current | patient: weight = 60; present; current)
```
Female patient of 80 years.
Spreading redness and warmth of the right shin for two days.
Teeth in good repair.
Prefers to be addressed by first name.
Her sister has known coronary artery disease.
Current weight 60 kg.
```

**near** (program answer: s; facts: sister: coronary artery disease (patient or first-degree relative); present; current | patient: weight = 61; present; current)
```
Female patient of 80 years.
Spreading redness and warmth of the right shin for two days.
Teeth in good repair.
Prefers to be addressed by first name.
Her sister has known coronary artery disease.
Current weight 61 kg.
```

**pres** (program answer: s; facts: sister: coronary artery disease (patient or first-degree relative); present; current | patient: weight = 92; present; current)
```
Woman of 80 years.
Spreading redness and warmth of the right shin for two days.
Prefers to be addressed by first name.
Teeth in good repair.
Her sister has known coronary artery disease.
Latest weight 92 kg.
```


## author3 / group 83: `rule_v1.test.inv032.c1.subject.long.336`

Rule: For Zentha disease, prescribe valtimide. If the patient has ever had a stroke or TIA (current or past) and the current temperature is above 38.0 C, prescribe isomarin instead.

**base** (program answer: s; facts: patient: temperature = 38.4; present; current)
```
Woman of 59 years.
Referred with Zentha disease.
Her roommate has a lazy eye.
Enjoys board games.
Photographs local wildlife.
Prefers morning appointments.
Temperature now 38.4 C (tympanic).
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Knits as a hobby.
Her father wears contact lenses.
Lives in a second-floor apartment.
Her friend burned a hand on a stove years ago.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2021.
Owns a bicycle.
Her roommate lives with psoriasis.
During a checkup in 2006, total protein was 7.0 g/dL.
```

**flip** (program answer: s'; facts: patient: stroke/TIA; present; past | patient: temperature = 38.4; present; current)
```
Woman of 59 years.
Referred with Zentha disease.
Her roommate has a lazy eye.
Enjoys board games.
TIA years ago, with full recovery.
Photographs local wildlife.
Prefers morning appointments.
Temperature now 38.4 C (tympanic).
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Knits as a hobby.
Her father wears contact lenses.
Lives in a second-floor apartment.
Her friend burned a hand on a stove years ago.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2021.
Owns a bicycle.
Her roommate lives with psoriasis.
During a checkup in 2006, total protein was 7.0 g/dL.
```

**near** (program answer: s; facts: roommate: stroke/TIA; present; past | patient: temperature = 38.4; present; current)
```
Woman of 59 years.
Referred with Zentha disease.
Her roommate has a lazy eye.
Enjoys board games.
Her roommate had a TIA years ago.
Photographs local wildlife.
Prefers morning appointments.
Temperature now 38.4 C (tympanic).
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Knits as a hobby.
Her father wears contact lenses.
Lives in a second-floor apartment.
Her friend burned a hand on a stove years ago.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2021.
Owns a bicycle.
Her roommate lives with psoriasis.
During a checkup in 2006, total protein was 7.0 g/dL.
```

**pres** (program answer: s; facts: patient: temperature = 38.4; present; current)
```
Female patient of 59 years.
Referred with Zentha disease.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2021.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Her roommate has a lazy eye.
Her roommate lives with psoriasis.
Prefers morning appointments.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Enjoys board games.
In 2020, lipase was 30 U/L.
During a checkup in 2006, total protein was 7.0 g/dL.
Owns a bicycle.
Current temperature 38.4 C.
Lives in a second-floor apartment.
Her father wears contact lenses.
```


## author4 / group 84: `rule_v1.test.gs113.c1.numeric.long.630`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum creatinine is above 2.0 mg/dL and the patient has ever had heart failure (current or past), prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: serum creatinine = 1.1; present; current | patient: heart failure; present; past (2005))
```
Female patient of 83 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum creatinine 1.1 mg/dL.
Teeth in good repair.
Prefers to be addressed by first name.
Her friend has a lazy eye.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Paints watercolors as a hobby.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Lives in a second-floor apartment.
Photographs local wildlife.
Uses sunscreen in summer.
Prefers morning appointments.
Drives a car.
Has two cats.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2005 and off all heart medicines since.
In 2020, lipase was 30 U/L.
Pupils equal and reactive to light.
Her friend lives with psoriasis.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 2.5; present; current | patient: heart failure; present; past (2005))
```
Female patient of 83 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum creatinine 2.5 mg/dL.
Teeth in good repair.
Prefers to be addressed by first name.
Her friend has a lazy eye.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Paints watercolors as a hobby.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Lives in a second-floor apartment.
Photographs local wildlife.
Uses sunscreen in summer.
Prefers morning appointments.
Drives a car.
Has two cats.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2005 and off all heart medicines since.
In 2020, lipase was 30 U/L.
Pupils equal and reactive to light.
Her friend lives with psoriasis.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: serum creatinine = 1.8; present; current | patient: heart failure; present; past (2005))
```
Female patient of 83 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum creatinine 1.8 mg/dL.
Teeth in good repair.
Prefers to be addressed by first name.
Her friend has a lazy eye.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Paints watercolors as a hobby.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Lives in a second-floor apartment.
Photographs local wildlife.
Uses sunscreen in summer.
Prefers morning appointments.
Drives a car.
Has two cats.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2005 and off all heart medicines since.
In 2020, lipase was 30 U/L.
Pupils equal and reactive to light.
Her friend lives with psoriasis.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: heart failure; present; past (2005) | patient: serum creatinine = 1.1; present; current)
```
Woman of 83 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Paints watercolors as a hobby.
Her friend lives with psoriasis.
Prefers to be addressed by first name.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Teeth in good repair.
Photographs local wildlife.
Prefers morning appointments.
In 2020, lipase was 30 U/L.
Has two cats.
Her wife has recovered from a dislocated finger.
Sees a dentist yearly.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2005 and off all heart medicines since.
Drives a car.
Enjoys board games.
Uses sunscreen in summer.
Latest creatinine result: 1.1 mg/dL.
Her friend has a lazy eye.
Knits as a hobby.
Lives in a second-floor apartment.
```


## author1 / group 85: `rule_v1.test.gs025.c2.numeric.long.1550`

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**base** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; present; current | patient: temperature = 36.8; present; current)
```
Female patient of 56 years.
Sore throat for two days.
Prefers morning appointments.
Her friend lives with psoriasis.
During a checkup in 2010, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2008.
Lives with peripheral artery disease affecting the left leg.
Her roommate has recovered from a dislocated finger.
Teeth in good repair.
Her roommate has a lazy eye.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Photographs local wildlife.
Sees a dentist yearly.
Temperature now 36.8 C (tympanic).
Free T4 of 1.2 ng/dL in 2008.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; present; current | patient: temperature = 38.5; present; current)
```
Female patient of 56 years.
Sore throat for two days.
Prefers morning appointments.
Her friend lives with psoriasis.
During a checkup in 2010, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2008.
Lives with peripheral artery disease affecting the left leg.
Her roommate has recovered from a dislocated finger.
Teeth in good repair.
Her roommate has a lazy eye.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Photographs local wildlife.
Sees a dentist yearly.
Temperature now 38.5 C (tympanic).
Free T4 of 1.2 ng/dL in 2008.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; present; current | patient: temperature = 37.8; present; current)
```
Female patient of 56 years.
Sore throat for two days.
Prefers morning appointments.
Her friend lives with psoriasis.
During a checkup in 2010, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2008.
Lives with peripheral artery disease affecting the left leg.
Her roommate has recovered from a dislocated finger.
Teeth in good repair.
Her roommate has a lazy eye.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Photographs local wildlife.
Sees a dentist yearly.
Temperature now 37.8 C (tympanic).
Free T4 of 1.2 ng/dL in 2008.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; present; current | patient: temperature = 36.8; present; current)
```
Woman of 56 years.
Sore throat for two days.
Photographs local wildlife.
Lives with peripheral artery disease affecting the left leg.
Free T4 of 1.2 ng/dL in 2008.
Her roommate has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2008.
Sees a dentist yearly.
Her friend lives with psoriasis.
During a checkup in 2010, total protein was 7.0 g/dL.
Uses sunscreen in summer.
Prefers morning appointments.
Her roommate has a lazy eye.
Paints watercolors as a hobby.
Teeth in good repair.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Current temperature 36.8 C.
```


## author2 / group 86: `rule_v1.test.gs230.c1.subject.easy.1625`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 2 points if the patient currently has tonsillar exudate; 3 points if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past). If the score is 8 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: tonsillar exudate; present; current | patient: calf swelling = 3.6; present; current | patient: peptic ulcer at any time; present; past)
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

**flip** (program answer: s'; facts: patient: tonsillar exudate; present; current | patient: myocardial infarction or peripheral artery disease; present; current | patient: calf swelling = 3.6; present; current | patient: peptic ulcer at any time; present; past)
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

**near** (program answer: s; facts: patient: tonsillar exudate; present; current | roommate: myocardial infarction or peripheral artery disease; present; current | patient: calf swelling = 3.6; present; current | patient: peptic ulcer at any time; present; past)
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

**pres** (program answer: s; facts: patient: peptic ulcer at any time; present; past | patient: tonsillar exudate; present; current | patient: calf swelling = 3.6; present; current)
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


## author3 / group 87: `rule_v1.test.gs071.c2.subject.long.633`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**base** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: temperature = 38.7; present; current)
```
Man of 55 years.
Atrial fibrillation; anticoagulation indicated.
Abdomen soft and non-tender.
Lives in a second-floor apartment.
Knits as a hobby.
Uses sunscreen in summer.
Sleeps seven hours a night.
Plays the piano.
Prefers morning appointments.
Has two cats.
Owns a bicycle.
Teeth in good repair.
His wife sprained a thumb last month.
Current temperature 38.7 C.
Photographs local wildlife.
His friend has a lazy eye.
Enjoys board games.
Sees a dentist yearly.
Pupils equal and reactive to light.
In 2005, folate was 12 ng/mL.
Paints watercolors as a hobby.
Drives a car.
Free T4 of 1.2 ng/dL in 2019.
```

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; current | patient: temperature = 38.7; present; current)
```
Man of 55 years.
Atrial fibrillation; anticoagulation indicated.
Active peptic ulcer disease.
Lives in a second-floor apartment.
Knits as a hobby.
Uses sunscreen in summer.
Sleeps seven hours a night.
Plays the piano.
Prefers morning appointments.
Has two cats.
Owns a bicycle.
Teeth in good repair.
His wife sprained a thumb last month.
Current temperature 38.7 C.
Photographs local wildlife.
His friend has a lazy eye.
Enjoys board games.
Sees a dentist yearly.
Pupils equal and reactive to light.
In 2005, folate was 12 ng/mL.
Paints watercolors as a hobby.
Drives a car.
Free T4 of 1.2 ng/dL in 2019.
```

**near** (program answer: s; facts: friend: peptic ulcer at any time; present; current | patient: temperature = 38.7; present; current)
```
Man of 55 years.
Atrial fibrillation; anticoagulation indicated.
His friend has peptic ulcer disease.
Lives in a second-floor apartment.
Knits as a hobby.
Uses sunscreen in summer.
Sleeps seven hours a night.
Plays the piano.
Prefers morning appointments.
Has two cats.
Owns a bicycle.
Teeth in good repair.
His wife sprained a thumb last month.
Current temperature 38.7 C.
Photographs local wildlife.
His friend has a lazy eye.
Enjoys board games.
Sees a dentist yearly.
Pupils equal and reactive to light.
In 2005, folate was 12 ng/mL.
Paints watercolors as a hobby.
Drives a car.
Free T4 of 1.2 ng/dL in 2019.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: temperature = 38.7; present; current)
```
Male patient of 55 years.
Atrial fibrillation; anticoagulation indicated.
His wife sprained a thumb last month.
His friend has a lazy eye.
Owns a bicycle.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Free T4 of 1.2 ng/dL in 2019.
Prefers morning appointments.
Sleeps seven hours a night.
Enjoys board games.
Uses sunscreen in summer.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
Drives a car.
Abdomen soft and non-tender.
Temperature now 38.7 C (tympanic).
Knits as a hobby.
Pupils equal and reactive to light.
Has two cats.
In 2005, folate was 12 ng/mL.
Photographs local wildlife.
```


## author4 / group 88: `rule_v1.test.gs138.c3.time.long.40`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the current weight is 60 kg or less; the patient currently has heart failure.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: current heart failure; absent; current | patient: weight = 58; present; current)
```
Man of 80 years.
Atrial fibrillation; anticoagulation indicated.
Enjoys board games.
Prefers morning appointments.
In 2021, lipase was 30 U/L.
Varicose veins: none seen.
Knits as a hobby.
Owns a bicycle.
His friend lives with psoriasis.
Sleeps flat on one pillow.
In 2017, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2011.
Pupils equal and reactive to light.
Current weight 58 kg.
Uses sunscreen in summer.
Drives a car.
Photographs local wildlife.
Prefers to be addressed by first name.
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: current heart failure; present; current | patient: weight = 58; present; current)
```
Man of 80 years.
Atrial fibrillation; anticoagulation indicated.
Enjoys board games.
Prefers morning appointments.
In 2021, lipase was 30 U/L.
Varicose veins: none seen.
Knits as a hobby.
Owns a bicycle.
His friend lives with psoriasis.
Current heart failure with ankle swelling.
In 2017, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2011.
Pupils equal and reactive to light.
Current weight 58 kg.
Uses sunscreen in summer.
Drives a car.
Photographs local wildlife.
Prefers to be addressed by first name.
Teeth in good repair.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: current heart failure; present; past (2005) | patient: weight = 58; present; current)
```
Man of 80 years.
Atrial fibrillation; anticoagulation indicated.
Enjoys board games.
Prefers morning appointments.
In 2021, lipase was 30 U/L.
Varicose veins: none seen.
Knits as a hobby.
Owns a bicycle.
His friend lives with psoriasis.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2005 and off all heart medicines since.
In 2017, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2011.
Pupils equal and reactive to light.
Current weight 58 kg.
Uses sunscreen in summer.
Drives a car.
Photographs local wildlife.
Prefers to be addressed by first name.
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: current heart failure; absent; current | patient: weight = 58; present; current)
```
Male patient of 80 years.
Atrial fibrillation; anticoagulation indicated.
In 2017, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2011.
Drives a car.
Varicose veins: none seen.
During a checkup in 2009, free T3 was 3.2 pg/mL.
His roommate has recovered from a dislocated finger.
Pupils equal and reactive to light.
Sleeps flat on one pillow.
Prefers to be addressed by first name.
Enjoys board games.
His friend lives with psoriasis.
Knits as a hobby.
Latest weight 58 kg.
Owns a bicycle.
Uses sunscreen in summer.
Prefers morning appointments.
Photographs local wildlife.
Teeth in good repair.
In 2021, lipase was 30 U/L.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: current heart failure; unknown; current | patient: weight = 58; present; current)
```
Man of 80 years.
Atrial fibrillation; anticoagulation indicated.
Enjoys board games.
Prefers morning appointments.
In 2021, lipase was 30 U/L.
Varicose veins: none seen.
Knits as a hobby.
Owns a bicycle.
His friend lives with psoriasis.
Current heart failure: status unclear from the records at hand.
In 2017, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2011.
Pupils equal and reactive to light.
Current weight 58 kg.
Uses sunscreen in summer.
Drives a car.
Photographs local wildlife.
Prefers to be addressed by first name.
Teeth in good repair.
```


## author1 / group 89: `rule_v1.test.gs221.c1.negation.long.559`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the patient has had cancer at any time (active or in remission), prescribe fondaparinux instead.

**base** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: cancer at any time; present; past (2010))
```
Man of 72 years.
First day after elective total hip replacement.
Knits as a hobby.
In 2005, lipase was 30 U/L.
Paints watercolors as a hobby.
Sees a dentist yearly.
Lives in a second-floor apartment.
Has two cats.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Walks without calf pain.
During a checkup in 2014, total protein was 7.0 g/dL.
Formerly had kidney cancer, cured by surgery in 2010.
Photographs local wildlife.
His sister has a lazy eye.
His friend sprained a thumb last month.
In 2024, folate was 12 ng/mL.
Teeth in good repair.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; present; current | patient: cancer at any time; present; past (2010))
```
Man of 72 years.
First day after elective total hip replacement.
Knits as a hobby.
In 2005, lipase was 30 U/L.
Paints watercolors as a hobby.
Sees a dentist yearly.
Lives in a second-floor apartment.
Has two cats.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Has symptomatic peripheral artery disease of both legs.
During a checkup in 2014, total protein was 7.0 g/dL.
Formerly had kidney cancer, cured by surgery in 2010.
Photographs local wildlife.
His sister has a lazy eye.
His friend sprained a thumb last month.
In 2024, folate was 12 ng/mL.
Teeth in good repair.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: cancer at any time; present; past (2010))
```
Man of 72 years.
First day after elective total hip replacement.
Knits as a hobby.
In 2005, lipase was 30 U/L.
Paints watercolors as a hobby.
Sees a dentist yearly.
Lives in a second-floor apartment.
Has two cats.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Has never had a heart attack or peripheral artery disease.
During a checkup in 2014, total protein was 7.0 g/dL.
Formerly had kidney cancer, cured by surgery in 2010.
Photographs local wildlife.
His sister has a lazy eye.
His friend sprained a thumb last month.
In 2024, folate was 12 ng/mL.
Teeth in good repair.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: cancer at any time; present; past (2010) | patient: myocardial infarction or peripheral artery disease; absent; current)
```
Male patient of 72 years.
First day after elective total hip replacement.
Formerly had kidney cancer, cured by surgery in 2010.
In 2024, folate was 12 ng/mL.
Paints watercolors as a hobby.
Walks without calf pain.
Sees a dentist yearly.
Enjoys board games.
Photographs local wildlife.
His sister has a lazy eye.
Has two cats.
His friend sprained a thumb last month.
Uses sunscreen in summer.
In 2005, lipase was 30 U/L.
Owns a bicycle.
During a checkup in 2024, free T3 was 3.2 pg/mL.
During a checkup in 2014, total protein was 7.0 g/dL.
Plays the piano.
Prefers morning appointments.
Lives in a second-floor apartment.
Teeth in good repair.
Knits as a hobby.
Sleeps seven hours a night.
```

**missing** (program answer: neither; facts: patient: myocardial infarction or peripheral artery disease; unknown; current | patient: cancer at any time; present; past (2010))
```
Man of 72 years.
First day after elective total hip replacement.
Knits as a hobby.
In 2005, lipase was 30 U/L.
Paints watercolors as a hobby.
Sees a dentist yearly.
Lives in a second-floor apartment.
Has two cats.
During a checkup in 2024, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
Owns a bicycle.
Myocardial infarction or peripheral artery disease: unknown.
During a checkup in 2014, total protein was 7.0 g/dL.
Formerly had kidney cancer, cured by surgery in 2010.
Photographs local wildlife.
His sister has a lazy eye.
His friend sprained a thumb last month.
In 2024, folate was 12 ng/mL.
Teeth in good repair.
Sleeps seven hours a night.
```


## author2 / group 90: `rule_v1.test.c1_neutropenia.anc.time.alt.197`

Rule: For a chest infection during chemotherapy, prescribe oral co-amoxiclav. If the current neutrophil count is 1.0 x10^9/L or less, prescribe intravenous piperacillin-tazobactam instead.

**base** (program answer: s; facts: patient: neutrophil count = 4.7; present; past (2015) | patient: neutrophil count = 2.3; present; current)
```
Man of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Back in 2015, neutrophil count stood at 4.7 x10^9/L.
Paints watercolors as a hobby.
Current neutrophil count 2.3 x10^9/L.
```

**flip** (program answer: s'; facts: patient: neutrophil count = 4.7; present; past (2015) | patient: neutrophil count = 0.8; present; current)
```
Man of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Back in 2015, neutrophil count stood at 4.7 x10^9/L.
Paints watercolors as a hobby.
Current neutrophil count 0.8 x10^9/L.
```

**near** (program answer: s; facts: patient: neutrophil count = 0.5; present; past (2015) | patient: neutrophil count = 2.3; present; current)
```
Man of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Back in 2015, neutrophil count stood at 0.5 x10^9/L.
Paints watercolors as a hobby.
Current neutrophil count 2.3 x10^9/L.
```

**pres** (program answer: s; facts: patient: neutrophil count = 2.3; present; current | patient: neutrophil count = 4.7; present; past (2015))
```
Male patient of 72 years.
Productive cough and fever, three weeks after the most recent cycle of chemotherapy for lymphoma.
Latest neutrophil count: 2.3 x10^9/L.
Records from 2015 list neutrophil count at 4.7 x10^9/L.
Paints watercolors as a hobby.
```


## author3 / group 91: `rule_v1.test.inv037.c1.negation.long.772`

Rule: For Pallis disease, prescribe brexadol. If the patient has had cancer at any time (active or in remission) or the current white cell count is above 12.0 x10^9/L, prescribe corlitane instead.

**base** (program answer: s; facts: patient: cancer at any time; absent; current | patient: white cell count = 5.7; present; current)
```
Woman of 75 years.
Referred with Pallis disease.
Sleeps seven hours a night.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Weight steady over the past year.
Has two cats.
Her roommate burned a hand on a stove years ago.
Latest WBC is 5.7 x10^9/L.
Her wife wears contact lenses.
Her wife sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2020.
In 2022, folate was 12 ng/mL.
Photographs local wildlife.
Drives a car.
Lives in a second-floor apartment.
In 2018, lipase was 30 U/L.
Plays the piano.
During a checkup in 2007, free T3 was 3.2 pg/mL.
```

**flip** (program answer: s'; facts: patient: cancer at any time; present; current | patient: white cell count = 5.7; present; current)
```
Woman of 75 years.
Referred with Pallis disease.
Sleeps seven hours a night.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Has melanoma skin cancer and is receiving treatment for it.
Has two cats.
Her roommate burned a hand on a stove years ago.
Latest WBC is 5.7 x10^9/L.
Her wife wears contact lenses.
Her wife sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2020.
In 2022, folate was 12 ng/mL.
Photographs local wildlife.
Drives a car.
Lives in a second-floor apartment.
In 2018, lipase was 30 U/L.
Plays the piano.
During a checkup in 2007, free T3 was 3.2 pg/mL.
```

**near** (program answer: s; facts: patient: cancer at any time; absent; current | patient: white cell count = 5.7; present; current)
```
Woman of 75 years.
Referred with Pallis disease.
Sleeps seven hours a night.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Free of cancer throughout life.
Has two cats.
Her roommate burned a hand on a stove years ago.
Latest WBC is 5.7 x10^9/L.
Her wife wears contact lenses.
Her wife sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2020.
In 2022, folate was 12 ng/mL.
Photographs local wildlife.
Drives a car.
Lives in a second-floor apartment.
In 2018, lipase was 30 U/L.
Plays the piano.
During a checkup in 2007, free T3 was 3.2 pg/mL.
```

**pres** (program answer: s; facts: patient: cancer at any time; absent; current | patient: white cell count = 5.7; present; current)
```
Female patient of 75 years.
Referred with Pallis disease.
Has two cats.
Teeth in good repair.
Photographs local wildlife.
Her roommate burned a hand on a stove years ago.
Weight steady over the past year.
Plays the piano.
Her wife sprained a thumb last month.
During a checkup in 2007, free T3 was 3.2 pg/mL.
In 2022, folate was 12 ng/mL.
Drives a car.
Sees a dentist yearly.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2020.
Enjoys board games.
Current white cell count 5.7 x10^9/L.
Sleeps seven hours a night.
In 2018, lipase was 30 U/L.
Her wife wears contact lenses.
```


## author4 / group 92: `rule_v1.test.gs086.c3.subject.easy.1114`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: heart failure; absent; current | patient: heart rate = 100; present; current)
```
Female patient of 70 years.
Admitted for community-acquired pneumonia; immobile.
Plays the piano.
Owns a bicycle.
Sees a dentist yearly.
Sleeps flat on one pillow.
Current heart rate 100/min.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; present; past (2018) | patient: heart failure; absent; current | patient: heart rate = 100; present; current)
```
Female patient of 70 years.
Admitted for community-acquired pneumonia; immobile.
Plays the piano.
Owns a bicycle.
Sees a dentist yearly.
Recovered from a pulmonary embolism in 2018.
Sleeps flat on one pillow.
Current heart rate 100/min.
```

**near** (program answer: s; facts: wife: venous thromboembolism; present; past | patient: heart failure; absent; current | patient: heart rate = 100; present; current)
```
Female patient of 70 years.
Admitted for community-acquired pneumonia; immobile.
Plays the piano.
Owns a bicycle.
Sees a dentist yearly.
Her wife had a DVT years ago.
Sleeps flat on one pillow.
Current heart rate 100/min.
```

**pres** (program answer: s; facts: patient: heart failure; absent; current | patient: heart rate = 100; present; current)
```
Woman of 70 years.
Admitted for community-acquired pneumonia; immobile.
Sees a dentist yearly.
Plays the piano.
Sleeps flat on one pillow.
Heart rate now 100/min on a pulse check.
Owns a bicycle.
```


## author1 / group 93: `rule_v1.test.gs157.c1.subject.easy.1000`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has ever had heart failure (current or past); the current platelet count is below 50 x10^9/L; the current temperature is above 38.0 C.

**base** (program answer: s; facts: patient: temperature = 38.6; present; current | patient: platelet count = 356; present; current)
```
Female patient of 43 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current temperature 38.6 C.
Paints watercolors as a hobby.
Photographs local wildlife.
Platelet count now 356 x10^9/L.
```

**flip** (program answer: s'; facts: patient: heart failure; present; current | patient: temperature = 38.6; present; current | patient: platelet count = 356; present; current)
```
Female patient of 43 years.
Community-acquired pneumonia confirmed on chest radiograph.
Current heart failure with ankle swelling.
Current temperature 38.6 C.
Paints watercolors as a hobby.
Photographs local wildlife.
Platelet count now 356 x10^9/L.
```

**near** (program answer: s; facts: sister: heart failure; present; current | patient: temperature = 38.6; present; current | patient: platelet count = 356; present; current)
```
Female patient of 43 years.
Community-acquired pneumonia confirmed on chest radiograph.
Her sister has advanced heart failure.
Current temperature 38.6 C.
Paints watercolors as a hobby.
Photographs local wildlife.
Platelet count now 356 x10^9/L.
```

**pres** (program answer: s; facts: patient: platelet count = 356; present; current | patient: temperature = 38.6; present; current)
```
Woman of 43 years.
Community-acquired pneumonia confirmed on chest radiograph.
Photographs local wildlife.
Current platelet count 356 x10^9/L.
Temperature now 38.6 C (tympanic).
Paints watercolors as a hobby.
```


## author2 / group 94: `rule_v1.test.gs139.c2.subject.long.925`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: angioedema; absent; current | patient: tender cervical lymph nodes; present; current)
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

**flip** (program answer: s'; facts: patient: angioedema; present; current | patient: tender cervical lymph nodes; present; current)
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

**near** (program answer: s; facts: wife: angioedema; present; current | patient: tender cervical lymph nodes; present; current)
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

**pres** (program answer: s; facts: patient: angioedema; absent; current | patient: tender cervical lymph nodes; present; current)
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

**missing** (program answer: neither; facts: patient: angioedema; unknown; current | patient: tender cervical lymph nodes; present; current)
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


## author3 / group 95: `rule_v1.test.gs071.c1.time.superseded.1234`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**base** (program answer: s; facts: patient: temperature = 37.3; present; current | patient: peptic ulcer at any time; present; current | patient: temperature = 37.2; present; past)
```
Female patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Current temperature 37.3 C.
Has an active duodenal ulcer.
Last month, temperature was 37.2 C; the newest measurement replaces it.
Has two cats.
```

**flip** (program answer: s'; facts: patient: temperature = 39.1; present; current | patient: peptic ulcer at any time; present; current | patient: temperature = 37.2; present; past)
```
Female patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Current temperature 39.1 C.
Has an active duodenal ulcer.
Last month, temperature was 37.2 C; the newest measurement replaces it.
Has two cats.
```

**near** (program answer: s; facts: patient: temperature = 37.3; present; current | patient: peptic ulcer at any time; present; current | patient: temperature = 39.2; present; past)
```
Female patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Current temperature 37.3 C.
Has an active duodenal ulcer.
Last month, temperature was 39.2 C; the newest measurement replaces it.
Has two cats.
```

**pres** (program answer: s; facts: patient: temperature = 37.2; present; past | patient: peptic ulcer at any time; present; current | patient: temperature = 37.3; present; current)
```
Woman of 50 years.
Atrial fibrillation; anticoagulation indicated.
Last month, temperature was 37.2 C; the newest measurement replaces it.
Has an active duodenal ulcer.
Temperature now 37.3 C (tympanic).
Has two cats.
Teeth in good repair.
```


## author4 / group 96: `rule_v1.test.gs024.c1.boundary.easy.405`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 3 points if the current ALT is above 120 U/L; 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 3 points if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 4 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: ALT = 50; present; current | patient: systolic blood pressure = 115; present; current | sister: diabetes (patient or first-degree relative); present; current)
```
Woman of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Varicose veins: none seen.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
ALT now 50 U/L.
Current systolic blood pressure 115 mmHg.
Photographs local wildlife.
Her sister lives with type 1 diabetes.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: ALT = 144; present; current | patient: systolic blood pressure = 115; present; current | sister: diabetes (patient or first-degree relative); present; current)
```
Woman of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Varicose veins: none seen.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
ALT now 144 U/L.
Current systolic blood pressure 115 mmHg.
Photographs local wildlife.
Her sister lives with type 1 diabetes.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: ALT = 120; present; current | patient: systolic blood pressure = 115; present; current | sister: diabetes (patient or first-degree relative); present; current)
```
Woman of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Varicose veins: none seen.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
ALT now 120 U/L.
Current systolic blood pressure 115 mmHg.
Photographs local wildlife.
Her sister lives with type 1 diabetes.
```

**pres** (program answer: s; facts: sister: diabetes (patient or first-degree relative); present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: systolic blood pressure = 115; present; current | patient: ALT = 50; present; current)
```
Female patient of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Her sister lives with type 1 diabetes.
Varicose veins: none seen.
Lives in a second-floor apartment.
Observations now: blood pressure 115/78 mmHg.
Pupils equal and reactive to light.
Current ALT 50 U/L.
Has two cats.
Photographs local wildlife.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: systolic blood pressure = 115; present; current | sister: diabetes (patient or first-degree relative); present; current)
```
Woman of 37 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Varicose veins: none seen.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Current systolic blood pressure 115 mmHg.
Photographs local wildlife.
Her sister lives with type 1 diabetes.
```


## author1 / group 97: `rule_v1.test.gs194.c1.numeric.easy.1636`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: weight = 84; present; current | patient: heart rate = 62; present; current)
```
Female patient of 36 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Current weight 84 kg.
Heart rate now 62/min on a pulse check.
Has two cats.
```

**flip** (program answer: s'; facts: patient: weight = 84; present; current | patient: heart rate = 98; present; current)
```
Female patient of 36 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Current weight 84 kg.
Heart rate now 98/min on a pulse check.
Has two cats.
```

**near** (program answer: s; facts: patient: weight = 84; present; current | patient: heart rate = 89; present; current)
```
Female patient of 36 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Current weight 84 kg.
Heart rate now 89/min on a pulse check.
Has two cats.
```

**pres** (program answer: s; facts: patient: heart rate = 62; present; current | patient: weight = 84; present; current)
```
Woman of 36 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers to be addressed by first name.
Has two cats.
Current heart rate 62/min.
Latest weight 84 kg.
```


## author2 / group 98: `rule_v1.test.gs223.c3.boundary.long.458`

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current blood urea nitrogen is above 19 mg/dL.

**base** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: blood urea nitrogen = 11; present; current | father: diabetes (patient or first-degree relative); present; current)
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

**flip** (program answer: s'; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: blood urea nitrogen = 25; present; current | father: diabetes (patient or first-degree relative); present; current)
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

**near** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: blood urea nitrogen = 19; present; current | father: diabetes (patient or first-degree relative); present; current)
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

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | father: diabetes (patient or first-degree relative); present; current | patient: blood urea nitrogen = 11; present; current)
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

**missing** (program answer: neither; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | father: diabetes (patient or first-degree relative); present; current)
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


## author3 / group 99: `rule_v1.test.gs131.c1.boundary.easy.954`

Rule: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: coronary artery disease; present; past | patient: heart rate = 96; present; current | patient: eGFR = 55; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Uses sunscreen in summer.
Plays the piano.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Heart rate now 96/min on a pulse check.
Current eGFR 55 mL/min/1.73 m2.
Enjoys board games.
Has two cats.
```

**flip** (program answer: s'; facts: patient: coronary artery disease; present; past | patient: heart rate = 96; present; current | patient: eGFR = 42; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Uses sunscreen in summer.
Plays the piano.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Heart rate now 96/min on a pulse check.
Current eGFR 42 mL/min/1.73 m2.
Enjoys board games.
Has two cats.
```

**near** (program answer: s; facts: patient: coronary artery disease; present; past | patient: heart rate = 96; present; current | patient: eGFR = 45; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Uses sunscreen in summer.
Plays the piano.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Heart rate now 96/min on a pulse check.
Current eGFR 45 mL/min/1.73 m2.
Enjoys board games.
Has two cats.
```

**pres** (program answer: s; facts: patient: coronary artery disease; present; past | patient: eGFR = 55; present; current | patient: heart rate = 96; present; current)
```
Woman of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Enjoys board games.
Plays the piano.
Coronary artery disease years ago, with angina that went away after bypass surgery.
eGFR now 55 mL/min/1.73 m2.
Uses sunscreen in summer.
Current heart rate 96/min.
Has two cats.
```

**missing** (program answer: neither; facts: patient: coronary artery disease; present; past | patient: heart rate = 96; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Uses sunscreen in summer.
Plays the piano.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Heart rate now 96/min on a pulse check.
Enjoys board games.
Has two cats.
```


## author4 / group 100: `rule_v1.test.gs139.c2.negation.long.1559`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: angioedema; absent; current | patient: tender cervical lymph nodes; present; current)
```
Woman of 26 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Face and neck without swelling on examination.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Teeth in good repair.
During a checkup in 2023, total protein was 7.0 g/dL.
Sees a dentist yearly.
Drives a car.
In 2018, lipase was 30 U/L.
Her sister burned a hand on a stove years ago.
Tender, swollen lymph nodes in the front of the neck.
Sleeps seven hours a night.
Her uncle sprained a thumb last month.
Zinc of 85 mcg/dL in 2022.
Her wife has a lazy eye.
Her father wears contact lenses.
Photographs local wildlife.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: patient: angioedema; present; past | patient: tender cervical lymph nodes; present; current)
```
Woman of 26 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Formerly had recurrent angioedema, in remission for many years now.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Teeth in good repair.
During a checkup in 2023, total protein was 7.0 g/dL.
Sees a dentist yearly.
Drives a car.
In 2018, lipase was 30 U/L.
Her sister burned a hand on a stove years ago.
Tender, swollen lymph nodes in the front of the neck.
Sleeps seven hours a night.
Her uncle sprained a thumb last month.
Zinc of 85 mcg/dL in 2022.
Her wife has a lazy eye.
Her father wears contact lenses.
Photographs local wildlife.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: patient: angioedema; absent; current | patient: tender cervical lymph nodes; present; current)
```
Woman of 26 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Has never had angioedema.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Teeth in good repair.
During a checkup in 2023, total protein was 7.0 g/dL.
Sees a dentist yearly.
Drives a car.
In 2018, lipase was 30 U/L.
Her sister burned a hand on a stove years ago.
Tender, swollen lymph nodes in the front of the neck.
Sleeps seven hours a night.
Her uncle sprained a thumb last month.
Zinc of 85 mcg/dL in 2022.
Her wife has a lazy eye.
Her father wears contact lenses.
Photographs local wildlife.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: tender cervical lymph nodes; present; current | patient: angioedema; absent; current)
```
Female patient of 26 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sees a dentist yearly.
Knits as a hobby.
Her wife has a lazy eye.
Tender, swollen lymph nodes in the front of the neck.
Zinc of 85 mcg/dL in 2022.
Her sister burned a hand on a stove years ago.
Pupils equal and reactive to light.
Her uncle sprained a thumb last month.
Her father wears contact lenses.
Teeth in good repair.
Photographs local wildlife.
During a checkup in 2023, total protein was 7.0 g/dL.
Face and neck without swelling on examination.
Sleeps seven hours a night.
In 2018, lipase was 30 U/L.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Drives a car.
```


## author1 / group 101: `rule_v1.test.gs134.c1.subject.easy.617`

Rule: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: platelet count = 37; present; current | patient: weight = 55; present; current | patient: tender cervical lymph nodes; present; current | patient: coronary artery disease (patient or first-degree relative); absent; current)
```
Woman of 29 years.
Requests contraception.
Current platelet count 37 x10^9/L.
Prefers morning appointments.
Teeth in good repair.
Current weight 55 kg.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
Chest pain on exertion: none reported.
```

**flip** (program answer: s'; facts: patient: platelet count = 37; present; current | patient: weight = 55; present; current | patient: tender cervical lymph nodes; present; current | father: coronary artery disease (patient or first-degree relative); present; current)
```
Woman of 29 years.
Requests contraception.
Current platelet count 37 x10^9/L.
Prefers morning appointments.
Teeth in good repair.
Current weight 55 kg.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
Her father has known coronary artery disease.
```

**near** (program answer: s; facts: patient: platelet count = 37; present; current | patient: weight = 55; present; current | patient: tender cervical lymph nodes; present; current | wife: coronary artery disease (patient or first-degree relative); present; current)
```
Woman of 29 years.
Requests contraception.
Current platelet count 37 x10^9/L.
Prefers morning appointments.
Teeth in good repair.
Current weight 55 kg.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
Her wife has angina from coronary artery disease.
```

**pres** (program answer: s; facts: patient: platelet count = 37; present; current | patient: weight = 55; present; current | patient: tender cervical lymph nodes; present; current | patient: coronary artery disease (patient or first-degree relative); absent; current)
```
Female patient of 29 years.
Requests contraception.
Platelet count now 37 x10^9/L.
Latest weight 55 kg.
Tender, swollen lymph nodes in the front of the neck.
Chest pain on exertion: none reported.
Prefers morning appointments.
Teeth in good repair.
Lives in a second-floor apartment.
```

**missing** (program answer: neither; facts: patient: platelet count = 37; present; current | patient: weight = 55; present; current | patient: tender cervical lymph nodes; present; current | patient: coronary artery disease (patient or first-degree relative); unknown; current)
```
Woman of 29 years.
Requests contraception.
Current platelet count 37 x10^9/L.
Prefers morning appointments.
Teeth in good repair.
Current weight 55 kg.
Lives in a second-floor apartment.
Tender, swollen lymph nodes in the front of the neck.
Coronary artery disease (patient or first-degree relative): unknown.
```


## author2 / group 102: `rule_v1.test.c3_dronedarone_hf.hf.negation.easy.482`

Rule: For rhythm control of paroxysmal atrial fibrillation, prescribe dronedarone. If the patient has ever had heart failure (current or past), prescribe amiodarone instead.

**base** (program answer: s; facts: patient: heart failure at any time; absent; current)
```
Male patient of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Heart sounds without a gallop.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: heart failure at any time; present; current)
```
Male patient of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Current heart failure with ankle swelling.
Plays the piano.
```

**near** (program answer: s; facts: patient: heart failure at any time; absent; current)
```
Male patient of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Has never had heart failure.
Plays the piano.
```

**pres** (program answer: s; facts: patient: heart failure at any time; absent; current)
```
Man of 62 years.
Paroxysmal atrial fibrillation with frequent symptomatic episodes; rhythm control chosen.
Plays the piano.
Heart sounds without a gallop.
```


## author3 / group 103: `rule_v1.test.s3_aims65.inr.numeric.easy.1024`

Rule: AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.

**base** (program answer: s; facts: patient: international normalized ratio = 1.2; present; current | patient: systolic blood pressure = 105; present; current | patient: age = 46; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Paints watercolors as a hobby.
Current international normalized ratio 1.2.
Observations now: blood pressure 105/73 mmHg.
Current age 46 years.
```

**flip** (program answer: s'; facts: patient: international normalized ratio = 2.3; present; current | patient: systolic blood pressure = 105; present; current | patient: age = 46; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Paints watercolors as a hobby.
Current international normalized ratio 2.3.
Observations now: blood pressure 105/73 mmHg.
Current age 46 years.
```

**near** (program answer: s; facts: patient: international normalized ratio = 1.4; present; current | patient: systolic blood pressure = 105; present; current | patient: age = 46; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Paints watercolors as a hobby.
Current international normalized ratio 1.4.
Observations now: blood pressure 105/73 mmHg.
Current age 46 years.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 105; present; current | patient: international normalized ratio = 1.2; present; current | patient: age = 46; present; current)
```
An adult woman.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Current systolic blood pressure 105 mmHg.
Latest international normalized ratio (INR): 1.2.
Paints watercolors as a hobby.
Currently aged 46 years.
```


## author4 / group 104: `rule_v1.test.gs036.c2.subject.long.442`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current weight is 60 kg or less or the patient has ever had coronary artery disease (current or past), prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: weight = 97; present; current)
```
Woman of 69 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Free T4 of 1.2 ng/dL in 2021.
Knits as a hobby.
Sleeps seven hours a night.
Enjoys board games.
Her friend has recovered from a dislocated finger.
In 2020, lipase was 30 U/L.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
Her sister has a lazy eye.
Zinc of 85 mcg/dL in 2023.
In 2018, folate was 12 ng/mL.
Prefers morning appointments.
Her roommate lives with psoriasis.
Cardiac stress test unremarkable last year.
Paints watercolors as a hobby.
Drives a car.
Pupils equal and reactive to light.
Photographs local wildlife.
Current weight 97 kg.
Her sister wears contact lenses.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: coronary artery disease; present; current | patient: weight = 97; present; current)
```
Woman of 69 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Free T4 of 1.2 ng/dL in 2021.
Knits as a hobby.
Sleeps seven hours a night.
Enjoys board games.
Her friend has recovered from a dislocated finger.
In 2020, lipase was 30 U/L.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
Her sister has a lazy eye.
Zinc of 85 mcg/dL in 2023.
In 2018, folate was 12 ng/mL.
Prefers morning appointments.
Her roommate lives with psoriasis.
Has coronary artery disease, managed medically.
Paints watercolors as a hobby.
Drives a car.
Pupils equal and reactive to light.
Photographs local wildlife.
Current weight 97 kg.
Her sister wears contact lenses.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: roommate: coronary artery disease; present; current | patient: weight = 97; present; current)
```
Woman of 69 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Free T4 of 1.2 ng/dL in 2021.
Knits as a hobby.
Sleeps seven hours a night.
Enjoys board games.
Her friend has recovered from a dislocated finger.
In 2020, lipase was 30 U/L.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
Her sister has a lazy eye.
Zinc of 85 mcg/dL in 2023.
In 2018, folate was 12 ng/mL.
Prefers morning appointments.
Her roommate lives with psoriasis.
Her roommate has known coronary artery disease.
Paints watercolors as a hobby.
Drives a car.
Pupils equal and reactive to light.
Photographs local wildlife.
Current weight 97 kg.
Her sister wears contact lenses.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: weight = 97; present; current)
```
Female patient of 69 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Free T4 of 1.2 ng/dL in 2021.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
In 2020, lipase was 30 U/L.
Plays the piano.
Her friend has recovered from a dislocated finger.
Sleeps seven hours a night.
Enjoys board games.
Her sister wears contact lenses.
Her sister has a lazy eye.
Owns a bicycle.
Photographs local wildlife.
Cardiac stress test unremarkable last year.
Zinc of 85 mcg/dL in 2023.
Prefers morning appointments.
Drives a car.
Latest weight 97 kg.
In 2018, folate was 12 ng/mL.
Teeth in good repair.
Her roommate lives with psoriasis.
Knits as a hobby.
```


## author1 / group 105: `rule_v1.test.s3_aims65.sbp.numeric.easy.332`

Rule: AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.

**base** (program answer: s; facts: patient: altered mental status; absent; current | patient: age = 44; present; current | patient: international normalized ratio = 1.0; present; current | patient: systolic blood pressure = 135; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Speech clear; follows commands.
Current age 44 years.
Latest international normalized ratio (INR): 1.0.
Teeth in good repair.
Observations now: blood pressure 135/89 mmHg.
```

**flip** (program answer: s'; facts: patient: altered mental status; absent; current | patient: age = 44; present; current | patient: international normalized ratio = 1.0; present; current | patient: systolic blood pressure = 90; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Speech clear; follows commands.
Current age 44 years.
Latest international normalized ratio (INR): 1.0.
Teeth in good repair.
Observations now: blood pressure 90/64 mmHg.
```

**near** (program answer: s; facts: patient: altered mental status; absent; current | patient: age = 44; present; current | patient: international normalized ratio = 1.0; present; current | patient: systolic blood pressure = 95; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Speech clear; follows commands.
Current age 44 years.
Latest international normalized ratio (INR): 1.0.
Teeth in good repair.
Observations now: blood pressure 95/67 mmHg.
```

**pres** (program answer: s; facts: patient: international normalized ratio = 1.0; present; current | patient: altered mental status; absent; current | patient: systolic blood pressure = 135; present; current | patient: age = 44; present; current)
```
An adult woman.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Teeth in good repair.
Current international normalized ratio 1.0.
Speech clear; follows commands.
Current systolic blood pressure 135 mmHg.
Currently aged 44 years.
```

**missing** (program answer: neither; facts: patient: altered mental status; absent; current | patient: age = 44; present; current | patient: international normalized ratio = 1.0; present; current)
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Speech clear; follows commands.
Current age 44 years.
Latest international normalized ratio (INR): 1.0.
Teeth in good repair.
```


## author2 / group 106: `rule_v1.test.gs137.c1.negation.long.208`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: serum creatinine = 1.7; present; current | patient: diabetes; absent; current)
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

**flip** (program answer: s'; facts: patient: serum creatinine = 1.7; present; current | patient: diabetes; present; past)
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

**near** (program answer: s; facts: patient: serum creatinine = 1.7; present; current | patient: diabetes; absent; current)
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

**pres** (program answer: s; facts: patient: diabetes; absent; current | patient: serum creatinine = 1.7; present; current)
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


## author3 / group 107: `rule_v1.test.s2_chads2.diabetes.subject.easy.367`

Rule: CHADS2 (as used here): 2 points for a stroke or TIA at any time; 1 point each for heart failure at any time, hypertension at any time, diabetes at any time, and a current age of 75 years or more.

**base** (program answer: s; facts: patient: age = 51; present; current | patient: stroke/TIA; absent; current)
```
An adult woman.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Sleeps seven hours a night.
Current age 51 years.
Prefers morning appointments.
Power and sensation normal in all limbs.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: age = 51; present; current | patient: diabetes; present; past (2019) | patient: stroke/TIA; absent; current)
```
An adult woman.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Sleeps seven hours a night.
Current age 51 years.
Prefers morning appointments.
Formerly diabetic; in remission since 2019.
Power and sensation normal in all limbs.
Sees a dentist yearly.
```

**near** (program answer: s; facts: patient: age = 51; present; current | father: diabetes; present; past | patient: stroke/TIA; absent; current)
```
An adult woman.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Sleeps seven hours a night.
Current age 51 years.
Prefers morning appointments.
Her father had diabetes years ago that went away after a change in diet.
Power and sensation normal in all limbs.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: patient: age = 51; present; current | patient: stroke/TIA; absent; current)
```
Woman, adult.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Prefers morning appointments.
Sleeps seven hours a night.
Currently aged 51 years.
Power and sensation normal in all limbs.
Sees a dentist yearly.
```


## author4 / group 108: `rule_v1.test.gs246.c2.negation.easy.949`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

**base** (program answer: s; facts: patient: active cancer; present; current | patient: angioedema; absent; current | patient: white cell count = 7.6; present; current)
```
Man of 45 years.
Acute low back pain after lifting.
Has metastatic lung cancer, receiving palliative treatment.
Free of facial or oropharyngeal edema.
Owns a bicycle.
Latest WBC is 7.6 x10^9/L.
```

**flip** (program answer: s'; facts: patient: active cancer; present; current | patient: angioedema; present; current | patient: white cell count = 7.6; present; current)
```
Man of 45 years.
Acute low back pain after lifting.
Has metastatic lung cancer, receiving palliative treatment.
Recurrent angioedema, under allergy follow-up.
Owns a bicycle.
Latest WBC is 7.6 x10^9/L.
```

**near** (program answer: s; facts: patient: active cancer; present; current | patient: angioedema; absent; current | patient: white cell count = 7.6; present; current)
```
Man of 45 years.
Acute low back pain after lifting.
Has metastatic lung cancer, receiving palliative treatment.
Has never had angioedema.
Owns a bicycle.
Latest WBC is 7.6 x10^9/L.
```

**pres** (program answer: s; facts: patient: active cancer; present; current | patient: angioedema; absent; current | patient: white cell count = 7.6; present; current)
```
Male patient of 45 years.
Acute low back pain after lifting.
Owns a bicycle.
Has metastatic lung cancer, receiving palliative treatment.
Free of facial or oropharyngeal edema.
Current white cell count 7.6 x10^9/L.
```

**missing** (program answer: neither; facts: patient: active cancer; present; current | patient: angioedema; unknown; current | patient: white cell count = 7.6; present; current)
```
Man of 45 years.
Acute low back pain after lifting.
Has metastatic lung cancer, receiving palliative treatment.
Angioedema: status unclear from the records at hand.
Owns a bicycle.
Latest WBC is 7.6 x10^9/L.
```


## author1 / group 109: `rule_v1.test.s1_meds.ams.subject.long.1436`

Rule: Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.

**base** (program answer: s; facts: patient: altered mental status; absent; current | patient: platelet count = 160; present; current | patient: age = 55; present; current)
```
An adult man.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Uses sunscreen in summer.
Gives a clear account of the illness.
Platelet count now 160 x10^9/L.
Prefers to be addressed by first name.
Current age 55 years.
Photographs local wildlife.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Knits as a hobby.
Paints watercolors as a hobby.
His father sprained a thumb last month.
Plays the piano.
Enjoys board games.
His friend burned a hand on a stove years ago.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2020.
Sees a dentist yearly.
Drives a car.
Pupils equal and reactive to light.
In 2009, lipase was 30 U/L.
```

**flip** (program answer: s'; facts: patient: altered mental status; present; current | patient: platelet count = 160; present; current | patient: age = 55; present; current)
```
An adult man.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Uses sunscreen in summer.
Disoriented to time and place, which is new for the patient.
Platelet count now 160 x10^9/L.
Prefers to be addressed by first name.
Current age 55 years.
Photographs local wildlife.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Knits as a hobby.
Paints watercolors as a hobby.
His father sprained a thumb last month.
Plays the piano.
Enjoys board games.
His friend burned a hand on a stove years ago.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2020.
Sees a dentist yearly.
Drives a car.
Pupils equal and reactive to light.
In 2009, lipase was 30 U/L.
```

**near** (program answer: s; facts: father: altered mental status; present; current | patient: platelet count = 160; present; current | patient: age = 55; present; current)
```
An adult man.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Uses sunscreen in summer.
His father is newly disoriented.
Platelet count now 160 x10^9/L.
Prefers to be addressed by first name.
Current age 55 years.
Photographs local wildlife.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Knits as a hobby.
Paints watercolors as a hobby.
His father sprained a thumb last month.
Plays the piano.
Enjoys board games.
His friend burned a hand on a stove years ago.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2020.
Sees a dentist yearly.
Drives a car.
Pupils equal and reactive to light.
In 2009, lipase was 30 U/L.
```

**pres** (program answer: s; facts: patient: platelet count = 160; present; current | patient: altered mental status; absent; current | patient: age = 55; present; current)
```
Man, adult.
Suspected sepsis; admitted from the emergency department.
Sees a dentist yearly.
Sleeps seven hours a night.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2020.
Drives a car.
Paints watercolors as a hobby.
Current platelet count 160 x10^9/L.
Gives a clear account of the illness.
His father sprained a thumb last month.
Photographs local wildlife.
Currently aged 55 years.
Plays the piano.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Prefers morning appointments.
Prefers to be addressed by first name.
In 2009, lipase was 30 U/L.
Uses sunscreen in summer.
His friend burned a hand on a stove years ago.
Knits as a hobby.
```


## author2 / group 110: `rule_v1.test.cut_bleed.egfr.numeric.long.1595`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. Score 2 points for a major bleeding event at any time; 1 point for age 75 years or more; 1 point for a current eGFR below 30 mL/min/1.73 m2. If the score is 2 or more, prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: age = 79; present; current | patient: eGFR = 83; present; current | patient: bleeding history; absent; current)
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

**flip** (program answer: s'; facts: patient: age = 79; present; current | patient: eGFR = 26; present; current | patient: bleeding history; absent; current)
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

**near** (program answer: s; facts: patient: age = 79; present; current | patient: eGFR = 35; present; current | patient: bleeding history; absent; current)
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

**pres** (program answer: s; facts: patient: age = 79; present; current | patient: eGFR = 83; present; current | patient: bleeding history; absent; current)
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


## author3 / group 111: `rule_v1.test.gs086.c1.numeric.long.367`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: heart rate = 78; present; current | patient: venous thromboembolism; present; current | patient: heart failure; absent; current)
```
Woman of 71 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Heart rate now 78/min on a pulse check.
Enjoys board games.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2013.
Knits as a hobby.
Photographs local wildlife.
Has two cats.
Her friend burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2016.
Owns a bicycle.
Has an acute pulmonary embolism, diagnosed this week.
Drives a car.
Pupils equal and reactive to light.
Plays the piano.
Her sister wears contact lenses.
Teeth in good repair.
Heart sounds without a gallop.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: heart rate = 104; present; current | patient: venous thromboembolism; present; current | patient: heart failure; absent; current)
```
Woman of 71 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Heart rate now 104/min on a pulse check.
Enjoys board games.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2013.
Knits as a hobby.
Photographs local wildlife.
Has two cats.
Her friend burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2016.
Owns a bicycle.
Has an acute pulmonary embolism, diagnosed this week.
Drives a car.
Pupils equal and reactive to light.
Plays the piano.
Her sister wears contact lenses.
Teeth in good repair.
Heart sounds without a gallop.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: heart rate = 87; present; current | patient: venous thromboembolism; present; current | patient: heart failure; absent; current)
```
Woman of 71 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Heart rate now 87/min on a pulse check.
Enjoys board games.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2013.
Knits as a hobby.
Photographs local wildlife.
Has two cats.
Her friend burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2016.
Owns a bicycle.
Has an acute pulmonary embolism, diagnosed this week.
Drives a car.
Pupils equal and reactive to light.
Plays the piano.
Her sister wears contact lenses.
Teeth in good repair.
Heart sounds without a gallop.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: heart rate = 78; present; current | patient: venous thromboembolism; present; current | patient: heart failure; absent; current)
```
Female patient of 71 years.
Admitted for community-acquired pneumonia; immobile.
Lives in a second-floor apartment.
Plays the piano.
Drives a car.
Current heart rate 78/min.
Prefers morning appointments.
Owns a bicycle.
Pupils equal and reactive to light.
Sees a dentist yearly.
Her sister wears contact lenses.
Has an acute pulmonary embolism, diagnosed this week.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2016.
Her friend burned a hand on a stove years ago.
Heart sounds without a gallop.
Teeth in good repair.
Sleeps seven hours a night.
Enjoys board games.
Zinc of 85 mcg/dL in 2013.
Has two cats.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism; present; current | patient: heart failure; absent; current)
```
Woman of 71 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Enjoys board games.
Paints watercolors as a hobby.
Zinc of 85 mcg/dL in 2013.
Knits as a hobby.
Photographs local wildlife.
Has two cats.
Her friend burned a hand on a stove years ago.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2016.
Owns a bicycle.
Has an acute pulmonary embolism, diagnosed this week.
Drives a car.
Pupils equal and reactive to light.
Plays the piano.
Her sister wears contact lenses.
Teeth in good repair.
Heart sounds without a gallop.
Lives in a second-floor apartment.
```


## author4 / group 112: `rule_v1.test.s2_geneva.hemoptysis.subject.long.1580`

Rule: Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: hemoptysis; absent; current | patient: age = 52; present; current)
```
Man, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Photographs local wildlife.
Sleeps seven hours a night.
Weight steady over the past year.
Lives in a second-floor apartment.
Has two cats.
In 2014, folate was 12 ng/mL.
Sputum colorless on inspection.
Enjoys board games.
His sister sprained a thumb last month.
Knits as a hobby.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Current age 52 years.
Pupils equal and reactive to light.
During a checkup in 2015, total protein was 7.0 g/dL.
Drives a car.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
His uncle has a lazy eye.
Zinc of 85 mcg/dL in 2009.
Prefers morning appointments.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: hemoptysis; present; current | patient: age = 52; present; current)
```
Man, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Photographs local wildlife.
Sleeps seven hours a night.
Weight steady over the past year.
Lives in a second-floor apartment.
Has two cats.
In 2014, folate was 12 ng/mL.
Currently coughing up blood with each bout of coughing.
Enjoys board games.
His sister sprained a thumb last month.
Knits as a hobby.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Current age 52 years.
Pupils equal and reactive to light.
During a checkup in 2015, total protein was 7.0 g/dL.
Drives a car.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
His uncle has a lazy eye.
Zinc of 85 mcg/dL in 2009.
Prefers morning appointments.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: patient: active cancer; absent; current | sister: hemoptysis; present; current | patient: age = 52; present; current)
```
Man, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Photographs local wildlife.
Sleeps seven hours a night.
Weight steady over the past year.
Lives in a second-floor apartment.
Has two cats.
In 2014, folate was 12 ng/mL.
His sister coughs up blood and is awaiting a chest scan.
Enjoys board games.
His sister sprained a thumb last month.
Knits as a hobby.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Current age 52 years.
Pupils equal and reactive to light.
During a checkup in 2015, total protein was 7.0 g/dL.
Drives a car.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
His uncle has a lazy eye.
Zinc of 85 mcg/dL in 2009.
Prefers morning appointments.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: active cancer; absent; current | patient: hemoptysis; absent; current | patient: age = 52; present; current)
```
An adult man.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Enjoys board games.
Weight steady over the past year.
Lives in a second-floor apartment.
Has two cats.
Uses sunscreen in summer.
Pupils equal and reactive to light.
His sister sprained a thumb last month.
Prefers morning appointments.
Knits as a hobby.
Drives a car.
His uncle has a lazy eye.
Plays the piano.
Sputum colorless on inspection.
Zinc of 85 mcg/dL in 2009.
Photographs local wildlife.
Sees a dentist yearly.
During a checkup in 2016, free T3 was 3.2 pg/mL.
During a checkup in 2015, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Currently aged 52 years.
In 2014, folate was 12 ng/mL.
Teeth in good repair.
```


## author1 / group 113: `rule_v1.test.gs079.c3.negation.easy.1365`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the current blood urea nitrogen is above 19 mg/dL; the patient has had a major bleeding event at any time; the patient currently has heart failure.

**base** (program answer: s; facts: patient: blood urea nitrogen = 10; present; current | patient: bleeding history; present; current)
```
Female patient of 65 years.
Suspected chest infection; assessed on the medical ward.
Blood urea nitrogen now: 10 mg/dL.
Major bleed from the stomach at present, with hemoglobin falling.
Teeth in good repair.
Drives a car.
Knits as a hobby.
Prefers to be addressed by first name.
```

**flip** (program answer: s'; facts: patient: current heart failure; present; current | patient: blood urea nitrogen = 10; present; current | patient: bleeding history; present; current)
```
Female patient of 65 years.
Suspected chest infection; assessed on the medical ward.
Current heart failure with ankle swelling.
Blood urea nitrogen now: 10 mg/dL.
Major bleed from the stomach at present, with hemoglobin falling.
Teeth in good repair.
Drives a car.
Knits as a hobby.
Prefers to be addressed by first name.
```

**near** (program answer: s; facts: patient: current heart failure; absent; current | patient: blood urea nitrogen = 10; present; current | patient: bleeding history; present; current)
```
Female patient of 65 years.
Suspected chest infection; assessed on the medical ward.
Heart failure: never diagnosed.
Blood urea nitrogen now: 10 mg/dL.
Major bleed from the stomach at present, with hemoglobin falling.
Teeth in good repair.
Drives a car.
Knits as a hobby.
Prefers to be addressed by first name.
```

**pres** (program answer: s; facts: patient: bleeding history; present; current | patient: blood urea nitrogen = 10; present; current)
```
Woman of 65 years.
Suspected chest infection; assessed on the medical ward.
Prefers to be addressed by first name.
Teeth in good repair.
Major bleed from the stomach at present, with hemoglobin falling.
Blood urea nitrogen 10 mg/dL on the current labs.
Drives a car.
Knits as a hobby.
```


## author2 / group 114: `rule_v1.test.inv018.c1.numeric.long.908`

Rule: For Delmar fever, prescribe fenrastat. If the current serum potassium is above 4.8 mmol/L, prescribe kivolane instead.

**base** (program answer: s; facts: patient: serum potassium = 4.4; present; current)
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

**flip** (program answer: s'; facts: patient: serum potassium = 5.4; present; current)
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

**near** (program answer: s; facts: patient: serum potassium = 4.7; present; current)
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

**pres** (program answer: s; facts: patient: serum potassium = 4.4; present; current)
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


## author3 / group 115: `rule_v1.test.gs179.c2.boundary.long.491`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the patient has ever had diabetes (current or past) and the current white cell count is above 12.0 x10^9/L, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: diabetes; present; past | patient: white cell count = 5.4; present; current)
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

**flip** (program answer: s'; facts: patient: diabetes; present; past | patient: white cell count = 13.9; present; current)
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
Latest WBC is 13.9 x10^9/L.
Free T4 of 1.2 ng/dL in 2005.
```

**near** (program answer: s; facts: patient: diabetes; present; past | patient: white cell count = 12.0; present; current)
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
Latest WBC is 12.0 x10^9/L.
Free T4 of 1.2 ng/dL in 2005.
```

**pres** (program answer: s; facts: patient: diabetes; present; past | patient: white cell count = 5.4; present; current)
```
Male patient of 72 years.
Atrial fibrillation with a ventricular rate of 128/min.
His friend wears contact lenses.
Drives a car.
Lives in a second-floor apartment.
Sees a dentist yearly.
Has two cats.
Paints watercolors as a hobby.
In 2016, lipase was 30 U/L.
Owns a bicycle.
His roommate has recovered from a dislocated finger.
Had diabetes years ago that went into remission on a low-calorie diet.
His sister burned a hand on a stove years ago.
Current white cell count 5.4 x10^9/L.
Pupils equal and reactive to light.
Teeth in good repair.
Photographs local wildlife.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2005.
Plays the piano.
Uses sunscreen in summer.
His friend has a lazy eye.
Zinc of 85 mcg/dL in 2010.
```

**missing** (program answer: neither; facts: patient: diabetes; present; past)
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
Free T4 of 1.2 ng/dL in 2005.
```


## author4 / group 116: `rule_v1.test.gs078.c1.boundary.easy.988`

Rule: For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the current serum potassium is above 5.0 mmol/L; the patient currently has a mechanical heart valve; the patient has ever had coronary artery disease (current or past).

**base** (program answer: s; facts: patient: coronary artery disease; present; current | patient: serum potassium = 3.9; present; current)
```
Female patient of 67 years.
Productive cough and fever; consolidation on chest radiograph.
Has coronary artery disease, managed medically.
Owns a bicycle.
Current serum potassium 3.9 mmol/L.
Plays the piano.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: coronary artery disease; present; current | patient: serum potassium = 5.8; present; current)
```
Female patient of 67 years.
Productive cough and fever; consolidation on chest radiograph.
Has coronary artery disease, managed medically.
Owns a bicycle.
Current serum potassium 5.8 mmol/L.
Plays the piano.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: coronary artery disease; present; current | patient: serum potassium = 5.0; present; current)
```
Female patient of 67 years.
Productive cough and fever; consolidation on chest radiograph.
Has coronary artery disease, managed medically.
Owns a bicycle.
Current serum potassium 5.0 mmol/L.
Plays the piano.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: serum potassium = 3.9; present; current | patient: coronary artery disease; present; current)
```
Woman of 67 years.
Productive cough and fever; consolidation on chest radiograph.
Lives in a second-floor apartment.
Owns a bicycle.
Latest potassium result: 3.9 mmol/L.
Plays the piano.
Has coronary artery disease, managed medically.
```

**missing** (program answer: neither; facts: patient: coronary artery disease; present; current)
```
Female patient of 67 years.
Productive cough and fever; consolidation on chest radiograph.
Has coronary artery disease, managed medically.
Owns a bicycle.
Plays the piano.
Lives in a second-floor apartment.
```


## author1 / group 117: `rule_v1.test.gs083.c1.numeric.easy.1998`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If the current serum creatinine is 1.5 mg/dL or more and the patient has ever had heart failure (current or past), prescribe intravenous co-amoxiclav instead.

**base** (program answer: s; facts: patient: heart failure; present; past (2009) | patient: serum creatinine = 0.6; present; current)
```
Female patient of 45 years.
Community-acquired pneumonia confirmed on chest radiograph.
Photographs local wildlife.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2009 and off all heart medicines since.
Latest creatinine result: 0.6 mg/dL.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: heart failure; present; past (2009) | patient: serum creatinine = 2.0; present; current)
```
Female patient of 45 years.
Community-acquired pneumonia confirmed on chest radiograph.
Photographs local wildlife.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2009 and off all heart medicines since.
Latest creatinine result: 2.0 mg/dL.
Plays the piano.
```

**near** (program answer: s; facts: patient: heart failure; present; past (2009) | patient: serum creatinine = 1.4; present; current)
```
Female patient of 45 years.
Community-acquired pneumonia confirmed on chest radiograph.
Photographs local wildlife.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2009 and off all heart medicines since.
Latest creatinine result: 1.4 mg/dL.
Plays the piano.
```

**pres** (program answer: s; facts: patient: heart failure; present; past (2009) | patient: serum creatinine = 0.6; present; current)
```
Woman of 45 years.
Community-acquired pneumonia confirmed on chest radiograph.
Plays the piano.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2009 and off all heart medicines since.
Photographs local wildlife.
Current serum creatinine 0.6 mg/dL.
```


## author2 / group 118: `rule_v1.test.two_throat.temp.time.easy.494`

Rule: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the current temperature is above 38.0 C; the patient currently has tonsillar exudate; the patient currently has tender anterior cervical lymph nodes.

**base** (program answer: s; facts: patient: temperature = 37.3; present; past (2013) | patient: temperature = 37.2; present; current | patient: tender cervical lymph nodes; present; current)
```
Male patient of 44 years.
Sore throat for two days.
Back in 2013, temperature stood at 37.3 C.
Current temperature 37.2 C.
Anterior cervical lymph nodes enlarged and tender to touch.
Teeth in good repair.
Drives a car.
```

**flip** (program answer: s'; facts: patient: temperature = 37.3; present; past (2013) | patient: temperature = 38.8; present; current | patient: tender cervical lymph nodes; present; current)
```
Male patient of 44 years.
Sore throat for two days.
Back in 2013, temperature stood at 37.3 C.
Current temperature 38.8 C.
Anterior cervical lymph nodes enlarged and tender to touch.
Teeth in good repair.
Drives a car.
```

**near** (program answer: s; facts: patient: temperature = 38.9; present; past (2013) | patient: temperature = 37.2; present; current | patient: tender cervical lymph nodes; present; current)
```
Male patient of 44 years.
Sore throat for two days.
Back in 2013, temperature stood at 38.9 C.
Current temperature 37.2 C.
Anterior cervical lymph nodes enlarged and tender to touch.
Teeth in good repair.
Drives a car.
```

**pres** (program answer: s; facts: patient: temperature = 37.3; present; past (2013) | patient: temperature = 37.2; present; current | patient: tender cervical lymph nodes; present; current)
```
Man of 44 years.
Sore throat for two days.
Teeth in good repair.
Records from 2013 list temperature at 37.3 C.
Drives a car.
Temperature now 37.2 C (tympanic).
Anterior cervical lymph nodes enlarged and tender to touch.
```


## author3 / group 119: `rule_v1.test.gs188.c2.boundary.easy.1918`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: ALT = 25; present; current | patient: peptic ulcer at any time; present; past)
```
Man of 30 years.
Spreading redness and warmth of the right shin for two days.
Current ALT 25 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
Photographs local wildlife.
```

**flip** (program answer: s'; facts: patient: ALT = 155; present; current | patient: peptic ulcer at any time; present; past)
```
Man of 30 years.
Spreading redness and warmth of the right shin for two days.
Current ALT 155 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
Photographs local wildlife.
```

**near** (program answer: s; facts: patient: ALT = 120; present; current | patient: peptic ulcer at any time; present; past)
```
Man of 30 years.
Spreading redness and warmth of the right shin for two days.
Current ALT 120 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
Photographs local wildlife.
```

**pres** (program answer: s; facts: patient: ALT = 25; present; current | patient: peptic ulcer at any time; present; past)
```
Male patient of 30 years.
Spreading redness and warmth of the right shin for two days.
ALT now 25 U/L.
Photographs local wildlife.
Duodenal ulcer years ago; recovered fully with treatment.
```


## author4 / group 120: `rule_v1.test.inv017.c3.negation.easy.593`

Rule: For Quorin syndrome, prescribe ostravin. If at least two of the following apply, prescribe dalmerol instead: the current serum creatinine is 1.5 mg/dL or more; the current ALT is above 120 U/L; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time.

**base** (program answer: s; facts: patient: serum creatinine = 0.8; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: ALT = 129; present; current)
```
Man of 50 years.
Referred with Quorin syndrome.
Latest creatinine result: 0.8 mg/dL.
Photographs local wildlife.
Prefers morning appointments.
Rectal exam unremarkable.
Current ALT 129 U/L.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 0.8; present; current | patient: colorectal cancer (patient or first-degree relative); present; current | patient: ALT = 129; present; current)
```
Man of 50 years.
Referred with Quorin syndrome.
Latest creatinine result: 0.8 mg/dL.
Photographs local wildlife.
Prefers morning appointments.
Lives with colon cancer and attends an oncology clinic.
Current ALT 129 U/L.
```

**near** (program answer: s; facts: patient: serum creatinine = 0.8; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: ALT = 129; present; current)
```
Man of 50 years.
Referred with Quorin syndrome.
Latest creatinine result: 0.8 mg/dL.
Photographs local wildlife.
Prefers morning appointments.
Has never had bowel cancer.
Current ALT 129 U/L.
```

**pres** (program answer: s; facts: patient: ALT = 129; present; current | patient: serum creatinine = 0.8; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current)
```
Male patient of 50 years.
Referred with Quorin syndrome.
Prefers morning appointments.
ALT now 129 U/L.
Current serum creatinine 0.8 mg/dL.
Rectal exam unremarkable.
Photographs local wildlife.
```


## author1 / group 121: `rule_v1.test.gs220.c2.negation.long.754`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: eGFR = 24; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Female patient of 19 years.
Requests contraception.
During a checkup in 2024, total protein was 7.0 g/dL.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
Her roommate sprained a thumb last month.
Plays the piano.
Zinc of 85 mcg/dL in 2024.
Teeth in good repair.
In 2024, folate was 12 ng/mL.
Pupils equal and reactive to light.
Her sister burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Enjoys board games.
eGFR now 24 mL/min/1.73 m2.
Prefers to be addressed by first name.
Owns a bicycle.
HbA1c 5.3% at a routine check.
Photographs local wildlife.
```

**flip** (program answer: s'; facts: patient: eGFR = 24; present; current | sister: diabetes (patient or first-degree relative); present; past)
```
Female patient of 19 years.
Requests contraception.
During a checkup in 2024, total protein was 7.0 g/dL.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
Her roommate sprained a thumb last month.
Plays the piano.
Zinc of 85 mcg/dL in 2024.
Teeth in good repair.
In 2024, folate was 12 ng/mL.
Pupils equal and reactive to light.
Her sister burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Enjoys board games.
eGFR now 24 mL/min/1.73 m2.
Prefers to be addressed by first name.
Owns a bicycle.
Her sister had diabetes years ago that went away after a change in diet.
Photographs local wildlife.
```

**near** (program answer: s; facts: patient: eGFR = 24; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Female patient of 19 years.
Requests contraception.
During a checkup in 2024, total protein was 7.0 g/dL.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
Her roommate sprained a thumb last month.
Plays the piano.
Zinc of 85 mcg/dL in 2024.
Teeth in good repair.
In 2024, folate was 12 ng/mL.
Pupils equal and reactive to light.
Her sister burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Enjoys board games.
eGFR now 24 mL/min/1.73 m2.
Prefers to be addressed by first name.
Owns a bicycle.
Has never had diabetes.
Photographs local wildlife.
```

**pres** (program answer: s; facts: patient: eGFR = 24; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 19 years.
Requests contraception.
Her roommate sprained a thumb last month.
Current eGFR 24 mL/min/1.73 m2.
HbA1c 5.3% at a routine check.
Prefers to be addressed by first name.
Owns a bicycle.
Sees a dentist yearly.
During a checkup in 2024, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Has two cats.
Knits as a hobby.
Lives in a second-floor apartment.
Enjoys board games.
Her sister burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2024.
In 2024, folate was 12 ng/mL.
Plays the piano.
Photographs local wildlife.
Pupils equal and reactive to light.
Teeth in good repair.
```

**missing** (program answer: neither; facts: patient: eGFR = 24; present; current | patient: diabetes (patient or first-degree relative); unknown; current)
```
Female patient of 19 years.
Requests contraception.
During a checkup in 2024, total protein was 7.0 g/dL.
Has two cats.
Lives in a second-floor apartment.
Sees a dentist yearly.
Her roommate sprained a thumb last month.
Plays the piano.
Zinc of 85 mcg/dL in 2024.
Teeth in good repair.
In 2024, folate was 12 ng/mL.
Pupils equal and reactive to light.
Her sister burned a hand on a stove years ago.
Knits as a hobby.
Paints watercolors as a hobby.
Enjoys board games.
eGFR now 24 mL/min/1.73 m2.
Prefers to be addressed by first name.
Owns a bicycle.
Diabetes (patient or first-degree relative): status unclear from the records at hand.
Photographs local wildlife.
```


## author2 / group 122: `rule_v1.test.gs209.c2.negation.long.1389`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**base** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: heart rate = 68; present; current | patient: age = 77; present; current)
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

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; past (2023) | patient: heart rate = 68; present; current | patient: age = 77; present; current)
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

**near** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: heart rate = 68; present; current | patient: age = 77; present; current)
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

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: heart rate = 68; present; current | patient: age = 77; present; current)
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


## author3 / group 123: `rule_v1.test.gs038.c2.time.easy.508`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.

**base** (program answer: s; facts: patient: blood urea nitrogen = 15; present; past (2011) | patient: blood urea nitrogen = 13; present; current | patient: peptic ulcer at any time; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Records from 2011 list blood urea nitrogen at 15 mg/dL.
Blood urea nitrogen now: 13 mg/dL.
Active peptic ulcer disease.
```

**flip** (program answer: s'; facts: patient: blood urea nitrogen = 15; present; past (2011) | patient: blood urea nitrogen = 30; present; current | patient: peptic ulcer at any time; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Records from 2011 list blood urea nitrogen at 15 mg/dL.
Blood urea nitrogen now: 30 mg/dL.
Active peptic ulcer disease.
```

**near** (program answer: s; facts: patient: blood urea nitrogen = 29; present; past (2011) | patient: blood urea nitrogen = 13; present; current | patient: peptic ulcer at any time; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Records from 2011 list blood urea nitrogen at 29 mg/dL.
Blood urea nitrogen now: 13 mg/dL.
Active peptic ulcer disease.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; present; current | patient: blood urea nitrogen = 13; present; current | patient: blood urea nitrogen = 15; present; past (2011))
```
Man of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Active peptic ulcer disease.
Blood urea nitrogen 13 mg/dL on the current labs.
Sees a dentist yearly.
Back in 2011, blood urea nitrogen stood at 15 mg/dL.
Paints watercolors as a hobby.
```

**missing** (program answer: neither; facts: patient: peptic ulcer at any time; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Active peptic ulcer disease.
```


## author4 / group 124: `rule_v1.test.c2_sprain_warfarin.warfarin.time.long.898`

Rule: For an acute ankle sprain, prescribe naproxen. If the patient is currently taking warfarin, prescribe acetaminophen instead.

**base** (program answer: s; facts: )
```
Female patient of 76 years.
Right ankle sprain after a fall on uneven ground; radiograph normal.
Prefers morning appointments.
Teeth in good repair.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Free T4 of 1.2 ng/dL in 2005.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Her friend lives with psoriasis.
Her friend wears contact lenses.
Her wife sprained a thumb last month.
Photographs local wildlife.
Sleeps seven hours a night.
Plays the piano.
Her friend has a lazy eye.
Owns a bicycle.
In 2012, lipase was 30 U/L.
Pupils equal and reactive to light.
Has two cats.
During a checkup in 2017, total protein was 7.0 g/dL.
```

**flip** (program answer: s'; facts: patient: warfarin use; present; current)
```
Female patient of 76 years.
Right ankle sprain after a fall on uneven ground; radiograph normal.
Prefers morning appointments.
Teeth in good repair.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Free T4 of 1.2 ng/dL in 2005.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Her friend lives with psoriasis.
Her friend wears contact lenses.
Her wife sprained a thumb last month.
Photographs local wildlife.
Sleeps seven hours a night.
Currently on warfarin, prescribed by the cardiology clinic.
Plays the piano.
Her friend has a lazy eye.
Owns a bicycle.
In 2012, lipase was 30 U/L.
Pupils equal and reactive to light.
Has two cats.
During a checkup in 2017, total protein was 7.0 g/dL.
```

**near** (program answer: s; facts: patient: warfarin use; present; past)
```
Female patient of 76 years.
Right ankle sprain after a fall on uneven ground; radiograph normal.
Prefers morning appointments.
Teeth in good repair.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Free T4 of 1.2 ng/dL in 2005.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Her friend lives with psoriasis.
Her friend wears contact lenses.
Her wife sprained a thumb last month.
Photographs local wildlife.
Sleeps seven hours a night.
Came off warfarin years ago after a heart rhythm problem settled.
Plays the piano.
Her friend has a lazy eye.
Owns a bicycle.
In 2012, lipase was 30 U/L.
Pupils equal and reactive to light.
Has two cats.
During a checkup in 2017, total protein was 7.0 g/dL.
```

**pres** (program answer: s; facts: )
```
Woman of 76 years.
Right ankle sprain after a fall on uneven ground; radiograph normal.
Her friend lives with psoriasis.
Prefers to be addressed by first name.
Her friend has a lazy eye.
Her friend wears contact lenses.
Teeth in good repair.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2017, free T3 was 3.2 pg/mL.
In 2012, lipase was 30 U/L.
Plays the piano.
Owns a bicycle.
Paints watercolors as a hobby.
Has two cats.
Photographs local wildlife.
Pupils equal and reactive to light.
During a checkup in 2017, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2005.
Her wife sprained a thumb last month.
Sleeps seven hours a night.
```


## author1 / group 125: `rule_v1.test.gs066.c2.subject.long.56`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient currently has tonsillar exudate, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | sister: colorectal cancer (patient or first-degree relative); present; past (2013))
```
Man of 82 years.
Atrial fibrillation with a ventricular rate of 128/min.
Prefers morning appointments.
Paints watercolors as a hobby.
Has two cats.
His roommate sprained a thumb last month.
Enjoys board games.
Uses sunscreen in summer.
His friend wears contact lenses.
In 2014, lipase was 30 U/L.
In 2007, folate was 12 ng/mL.
Photographs local wildlife.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2024.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Tonsils pink and clean on inspection.
His sister recovered from colon cancer after an operation in 2013.
Knits as a hobby.
His friend lives with psoriasis.
Drives a car.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; present; current | sister: colorectal cancer (patient or first-degree relative); present; past (2013))
```
Man of 82 years.
Atrial fibrillation with a ventricular rate of 128/min.
Prefers morning appointments.
Paints watercolors as a hobby.
Has two cats.
His roommate sprained a thumb last month.
Enjoys board games.
Uses sunscreen in summer.
His friend wears contact lenses.
In 2014, lipase was 30 U/L.
In 2007, folate was 12 ng/mL.
Photographs local wildlife.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2024.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Tonsils swollen and coated with yellow exudate.
His sister recovered from colon cancer after an operation in 2013.
Knits as a hobby.
His friend lives with psoriasis.
Drives a car.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: sister: tonsillar exudate; present; current | sister: colorectal cancer (patient or first-degree relative); present; past (2013))
```
Man of 82 years.
Atrial fibrillation with a ventricular rate of 128/min.
Prefers morning appointments.
Paints watercolors as a hobby.
Has two cats.
His roommate sprained a thumb last month.
Enjoys board games.
Uses sunscreen in summer.
His friend wears contact lenses.
In 2014, lipase was 30 U/L.
In 2007, folate was 12 ng/mL.
Photographs local wildlife.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2024.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
His sister has a sore throat with tonsillar exudate.
His sister recovered from colon cancer after an operation in 2013.
Knits as a hobby.
His friend lives with psoriasis.
Drives a car.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; absent; current | sister: colorectal cancer (patient or first-degree relative); present; past (2013))
```
Male patient of 82 years.
Atrial fibrillation with a ventricular rate of 128/min.
Lives in a second-floor apartment.
His friend wears contact lenses.
Sees a dentist yearly.
Teeth in good repair.
Enjoys board games.
Has two cats.
His roommate sprained a thumb last month.
Drives a car.
Free T4 of 1.2 ng/dL in 2024.
Sleeps seven hours a night.
Owns a bicycle.
Pupils equal and reactive to light.
Tonsils pink and clean on inspection.
His sister recovered from colon cancer after an operation in 2013.
His friend lives with psoriasis.
Photographs local wildlife.
Paints watercolors as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
In 2014, lipase was 30 U/L.
In 2007, folate was 12 ng/mL.
Knits as a hobby.
```

**missing** (program answer: neither; facts: patient: tonsillar exudate; unknown; current | sister: colorectal cancer (patient or first-degree relative); present; past (2013))
```
Man of 82 years.
Atrial fibrillation with a ventricular rate of 128/min.
Prefers morning appointments.
Paints watercolors as a hobby.
Has two cats.
His roommate sprained a thumb last month.
Enjoys board games.
Uses sunscreen in summer.
His friend wears contact lenses.
In 2014, lipase was 30 U/L.
In 2007, folate was 12 ng/mL.
Photographs local wildlife.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2024.
Sleeps seven hours a night.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Tonsillar exudate: unknown.
His sister recovered from colon cancer after an operation in 2013.
Knits as a hobby.
His friend lives with psoriasis.
Drives a car.
Lives in a second-floor apartment.
```


## author2 / group 126: `rule_v1.test.gs197.c1.negation.long.390`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current systolic blood pressure is 90 mmHg or less, prescribe fondaparinux instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 86; present; current | patient: myocardial infarction or peripheral artery disease; absent; current)
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

**flip** (program answer: s'; facts: patient: systolic blood pressure = 86; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
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

**near** (program answer: s; facts: patient: systolic blood pressure = 86; present; current | patient: myocardial infarction or peripheral artery disease; absent; current)
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

**pres** (program answer: s; facts: patient: systolic blood pressure = 86; present; current | patient: myocardial infarction or peripheral artery disease; absent; current)
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

**missing** (program answer: neither; facts: patient: systolic blood pressure = 86; present; current | patient: myocardial infarction or peripheral artery disease; unknown; current)
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


## author3 / group 127: `rule_v1.test.s1_bap65.ams.negation.long.421`

Rule: BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of 25 mg/dL or more; current altered mental status (confusion or disorientation); a current heart rate of 109/min or more. Age is scored separately and is not part of this question.

**base** (program answer: s; facts: patient: heart rate = 80; present; current | patient: altered mental status; absent; current | patient: blood urea nitrogen = 8; present; current)
```
Female patient of 89 years.
Acute exacerbation of COPD; assessed in the emergency department.
In 2006, lipase was 30 U/L.
Uses sunscreen in summer.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Her friend sprained a thumb last month.
Has two cats.
Prefers morning appointments.
Current heart rate 80/min.
Prefers to be addressed by first name.
Photographs local wildlife.
Her roommate lives with psoriasis.
Pupils equal and reactive to light.
Speech clear; follows commands.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her sister has a lazy eye.
Drives a car.
Blood urea nitrogen 8 mg/dL on the current labs.
Owns a bicycle.
During a checkup in 2007, total protein was 7.0 g/dL.
```

**flip** (program answer: s'; facts: patient: heart rate = 80; present; current | patient: altered mental status; present; current | patient: blood urea nitrogen = 8; present; current)
```
Female patient of 89 years.
Acute exacerbation of COPD; assessed in the emergency department.
In 2006, lipase was 30 U/L.
Uses sunscreen in summer.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Her friend sprained a thumb last month.
Has two cats.
Prefers morning appointments.
Current heart rate 80/min.
Prefers to be addressed by first name.
Photographs local wildlife.
Her roommate lives with psoriasis.
Pupils equal and reactive to light.
Newly disoriented and unable to give a clear history.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her sister has a lazy eye.
Drives a car.
Blood urea nitrogen 8 mg/dL on the current labs.
Owns a bicycle.
During a checkup in 2007, total protein was 7.0 g/dL.
```

**near** (program answer: s; facts: patient: heart rate = 80; present; current | patient: altered mental status; absent; current | patient: blood urea nitrogen = 8; present; current)
```
Female patient of 89 years.
Acute exacerbation of COPD; assessed in the emergency department.
In 2006, lipase was 30 U/L.
Uses sunscreen in summer.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Her friend sprained a thumb last month.
Has two cats.
Prefers morning appointments.
Current heart rate 80/min.
Prefers to be addressed by first name.
Photographs local wildlife.
Her roommate lives with psoriasis.
Pupils equal and reactive to light.
Confusion absent; answers questions appropriately.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her sister has a lazy eye.
Drives a car.
Blood urea nitrogen 8 mg/dL on the current labs.
Owns a bicycle.
During a checkup in 2007, total protein was 7.0 g/dL.
```

**pres** (program answer: s; facts: patient: blood urea nitrogen = 8; present; current | patient: altered mental status; absent; current | patient: heart rate = 80; present; current)
```
Woman of 89 years.
Acute exacerbation of COPD; assessed in the emergency department.
In 2006, lipase was 30 U/L.
Her sister has a lazy eye.
Drives a car.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her wife has recovered from a dislocated finger.
Prefers to be addressed by first name.
Owns a bicycle.
Prefers morning appointments.
Has two cats.
During a checkup in 2007, total protein was 7.0 g/dL.
Photographs local wildlife.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Blood urea nitrogen now: 8 mg/dL.
Speech clear; follows commands.
Her roommate lives with psoriasis.
Enjoys board games.
Her friend sprained a thumb last month.
Heart rate now 80/min on a pulse check.
```


## author4 / group 128: `rule_v1.test.two_pneumonia.rr.numeric.easy.711`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has new confusion; the current respiratory rate is 30/min or more; the current systolic blood pressure is below 90 mmHg.

**base** (program answer: s; facts: patient: new confusion; present; current | patient: systolic blood pressure = 142; present; current | patient: respiratory rate = 14; present; current)
```
Male patient of 78 years.
Community-acquired pneumonia confirmed on chest radiograph.
Disoriented to time and place, which is new for the patient.
Observations now: blood pressure 142/93 mmHg.
Current respiratory rate 14/min.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: new confusion; present; current | patient: systolic blood pressure = 142; present; current | patient: respiratory rate = 30; present; current)
```
Male patient of 78 years.
Community-acquired pneumonia confirmed on chest radiograph.
Disoriented to time and place, which is new for the patient.
Observations now: blood pressure 142/93 mmHg.
Current respiratory rate 30/min.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: new confusion; present; current | patient: systolic blood pressure = 142; present; current | patient: respiratory rate = 28; present; current)
```
Male patient of 78 years.
Community-acquired pneumonia confirmed on chest radiograph.
Disoriented to time and place, which is new for the patient.
Observations now: blood pressure 142/93 mmHg.
Current respiratory rate 28/min.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: respiratory rate = 14; present; current | patient: new confusion; present; current | patient: systolic blood pressure = 142; present; current)
```
Man of 78 years.
Community-acquired pneumonia confirmed on chest radiograph.
Observations now: respiratory rate 14/min.
Sleeps seven hours a night.
Disoriented to time and place, which is new for the patient.
Current systolic blood pressure 142 mmHg.
```


## author1 / group 129: `rule_v1.test.inv008.c1.negation.long.109`

Rule: For Okata fever, prescribe solvadine. If the patient currently has a venous thromboembolism and the current eGFR is below 50 mL/min/1.73 m2, prescribe tarnicept instead.

**base** (program answer: s; facts: patient: eGFR = 44; present; current)
```
Man of 60 years.
Referred with Okata fever.
Drives a car.
In 2024, lipase was 30 U/L.
Paints watercolors as a hobby.
eGFR now 44 mL/min/1.73 m2.
His wife has a lazy eye.
During a checkup in 2024, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2005.
His friend burned a hand on a stove years ago.
Sleeps seven hours a night.
Photographs local wildlife.
Prefers morning appointments.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Teeth in good repair.
His friend has recovered from a dislocated finger.
His roommate wears contact lenses.
```

**flip** (program answer: s'; facts: patient: eGFR = 44; present; current | patient: current venous thromboembolism; present; current)
```
Man of 60 years.
Referred with Okata fever.
Drives a car.
In 2024, lipase was 30 U/L.
Paints watercolors as a hobby.
eGFR now 44 mL/min/1.73 m2.
His wife has a lazy eye.
Has an acute pulmonary embolism, diagnosed this week.
During a checkup in 2024, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2005.
His friend burned a hand on a stove years ago.
Sleeps seven hours a night.
Photographs local wildlife.
Prefers morning appointments.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Teeth in good repair.
His friend has recovered from a dislocated finger.
His roommate wears contact lenses.
```

**near** (program answer: s; facts: patient: eGFR = 44; present; current | patient: current venous thromboembolism; absent; current)
```
Man of 60 years.
Referred with Okata fever.
Drives a car.
In 2024, lipase was 30 U/L.
Paints watercolors as a hobby.
eGFR now 44 mL/min/1.73 m2.
His wife has a lazy eye.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
During a checkup in 2024, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2005.
His friend burned a hand on a stove years ago.
Sleeps seven hours a night.
Photographs local wildlife.
Prefers morning appointments.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Teeth in good repair.
His friend has recovered from a dislocated finger.
His roommate wears contact lenses.
```

**pres** (program answer: s; facts: patient: eGFR = 44; present; current)
```
Male patient of 60 years.
Referred with Okata fever.
Photographs local wildlife.
His roommate wears contact lenses.
Uses sunscreen in summer.
During a checkup in 2024, total protein was 7.0 g/dL.
In 2024, lipase was 30 U/L.
His friend has recovered from a dislocated finger.
Free T4 of 1.2 ng/dL in 2005.
Teeth in good repair.
Current eGFR 44 mL/min/1.73 m2.
His friend burned a hand on a stove years ago.
Drives a car.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2019, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
His wife has a lazy eye.
Sleeps seven hours a night.
```


## author2 / group 130: `rule_v1.test.gs140.c3.boundary.long.770`

Rule: For primary prevention, prescribe atorvastatin. Score 2 points if the patient has ever had a venous thromboembolism (current or past); 1 point if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current temperature is above 38.0 C. If the score is 3 or more, prescribe ezetimibe instead.

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: temperature = 36.4; present; current | patient: colorectal cancer (patient or first-degree relative); present; past (2014))
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

**flip** (program answer: s'; facts: patient: venous thromboembolism; absent; current | patient: temperature = 38.6; present; current | patient: colorectal cancer (patient or first-degree relative); present; past (2014))
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

**near** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: temperature = 38.0; present; current | patient: colorectal cancer (patient or first-degree relative); present; past (2014))
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

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); present; past (2014) | patient: temperature = 36.4; present; current | patient: venous thromboembolism; absent; current)
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


## author3 / group 131: `rule_v1.test.gs172.c1.numeric.long.169`

Rule: For an acute gout flare, prescribe colchicine. If the current serum creatinine is above 2.0 mg/dL and the current heart rate is above 90/min, prescribe prednisone instead.

**base** (program answer: s; facts: patient: serum creatinine = 1.4; present; current | patient: heart rate = 99; present; current)
```
Male patient of 59 years.
Acute gout flare of the right first metatarsophalangeal joint.
His sister wears contact lenses.
His uncle burned a hand on a stove years ago.
Current serum creatinine 1.4 mg/dL.
Knits as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
Photographs local wildlife.
His uncle has a lazy eye.
Sees a dentist yearly.
Drives a car.
Owns a bicycle.
His friend lives with psoriasis.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
In 2019, folate was 12 ng/mL.
Has two cats.
Heart rate now 99/min on a pulse check.
Prefers to be addressed by first name.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 2.9; present; current | patient: heart rate = 99; present; current)
```
Male patient of 59 years.
Acute gout flare of the right first metatarsophalangeal joint.
His sister wears contact lenses.
His uncle burned a hand on a stove years ago.
Current serum creatinine 2.9 mg/dL.
Knits as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
Photographs local wildlife.
His uncle has a lazy eye.
Sees a dentist yearly.
Drives a car.
Owns a bicycle.
His friend lives with psoriasis.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
In 2019, folate was 12 ng/mL.
Has two cats.
Heart rate now 99/min on a pulse check.
Prefers to be addressed by first name.
Enjoys board games.
```

**near** (program answer: s; facts: patient: serum creatinine = 1.8; present; current | patient: heart rate = 99; present; current)
```
Male patient of 59 years.
Acute gout flare of the right first metatarsophalangeal joint.
His sister wears contact lenses.
His uncle burned a hand on a stove years ago.
Current serum creatinine 1.8 mg/dL.
Knits as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
Photographs local wildlife.
His uncle has a lazy eye.
Sees a dentist yearly.
Drives a car.
Owns a bicycle.
His friend lives with psoriasis.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
In 2019, folate was 12 ng/mL.
Has two cats.
Heart rate now 99/min on a pulse check.
Prefers to be addressed by first name.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: heart rate = 99; present; current | patient: serum creatinine = 1.4; present; current)
```
Man of 59 years.
Acute gout flare of the right first metatarsophalangeal joint.
Current heart rate 99/min.
Enjoys board games.
Prefers morning appointments.
His friend lives with psoriasis.
Owns a bicycle.
Drives a car.
Has two cats.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
In 2019, folate was 12 ng/mL.
Latest creatinine result: 1.4 mg/dL.
Photographs local wildlife.
His sister wears contact lenses.
Knits as a hobby.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Pupils equal and reactive to light.
His uncle burned a hand on a stove years ago.
His uncle has a lazy eye.
```


## author4 / group 132: `rule_v1.test.gs078.c2.time.long.1433`

Rule: For community-acquired pneumonia treated at home, prescribe amoxicillin. If at least two of the following apply, prescribe doxycycline instead: the current serum potassium is above 5.0 mmol/L; the patient currently has a mechanical heart valve; the patient has ever had coronary artery disease (current or past).

**base** (program answer: s; facts: patient: serum potassium = 5.5; present; current | patient: coronary artery disease; absent; current | patient: mechanical heart valve; absent; current)
```
Male patient of 78 years.
Productive cough and fever; consolidation on chest radiograph.
His wife has a lazy eye.
Prefers to be addressed by first name.
Owns a bicycle.
His wife has recovered from a dislocated finger.
Current serum potassium 5.5 mmol/L.
Photographs local wildlife.
Teeth in good repair.
Uses sunscreen in summer.
Chest pain on exertion: none reported.
Plays the piano.
Enjoys board games.
In 2014, lipase was 30 U/L.
Sees a dentist yearly.
Drives a car.
During a checkup in 2013, total protein was 7.0 g/dL.
Has two cats.
Heart sounds without a metallic click.
Pupils equal and reactive to light.
Knits as a hobby.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2023.
Paints watercolors as a hobby.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: serum potassium = 5.5; present; current | patient: coronary artery disease; absent; current | patient: mechanical heart valve; present; current)
```
Male patient of 78 years.
Productive cough and fever; consolidation on chest radiograph.
His wife has a lazy eye.
Prefers to be addressed by first name.
Owns a bicycle.
His wife has recovered from a dislocated finger.
Current serum potassium 5.5 mmol/L.
Photographs local wildlife.
Teeth in good repair.
Uses sunscreen in summer.
Chest pain on exertion: none reported.
Plays the piano.
Enjoys board games.
In 2014, lipase was 30 U/L.
Sees a dentist yearly.
Drives a car.
During a checkup in 2013, total protein was 7.0 g/dL.
Has two cats.
Lives with a mechanical aortic valve prosthesis.
Pupils equal and reactive to light.
Knits as a hobby.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2023.
Paints watercolors as a hobby.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: serum potassium = 5.5; present; current | patient: coronary artery disease; absent; current | patient: mechanical heart valve; present; past)
```
Male patient of 78 years.
Productive cough and fever; consolidation on chest radiograph.
His wife has a lazy eye.
Prefers to be addressed by first name.
Owns a bicycle.
His wife has recovered from a dislocated finger.
Current serum potassium 5.5 mmol/L.
Photographs local wildlife.
Teeth in good repair.
Uses sunscreen in summer.
Chest pain on exertion: none reported.
Plays the piano.
Enjoys board games.
In 2014, lipase was 30 U/L.
Sees a dentist yearly.
Drives a car.
During a checkup in 2013, total protein was 7.0 g/dL.
Has two cats.
Mechanical aortic valve explanted years ago for valve thrombosis; a bioprosthesis now sits in its place.
Pupils equal and reactive to light.
Knits as a hobby.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2023.
Paints watercolors as a hobby.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: mechanical heart valve; absent; current | patient: serum potassium = 5.5; present; current | patient: coronary artery disease; absent; current)
```
Man of 78 years.
Productive cough and fever; consolidation on chest radiograph.
His wife has recovered from a dislocated finger.
Plays the piano.
Lives in a second-floor apartment.
During a checkup in 2013, total protein was 7.0 g/dL.
Drives a car.
Paints watercolors as a hobby.
Heart sounds without a metallic click.
Enjoys board games.
His wife has a lazy eye.
Owns a bicycle.
Latest potassium result: 5.5 mmol/L.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Zinc of 85 mcg/dL in 2023.
In 2014, lipase was 30 U/L.
Photographs local wildlife.
Knits as a hobby.
Chest pain on exertion: none reported.
Sleeps seven hours a night.
Teeth in good repair.
Has two cats.
Sees a dentist yearly.
Pupils equal and reactive to light.
```


## author1 / group 133: `rule_v1.test.s1_psi.bun.time.alt.225`

Rule: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 20 mg/dL or more. Age, sex and other items of the index are not part of this question.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: arterial pH = 7.42; present; current | patient: blood urea nitrogen = 13; present; past (2012) | patient: blood urea nitrogen = 13; present; current)
```
Woman of 45 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Oncology follow-up: none.
Latest arterial blood gas shows a pH of 7.42.
Back in 2012, blood urea nitrogen stood at 13 mg/dL.
Blood urea nitrogen 13 mg/dL on the current labs.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: arterial pH = 7.42; present; current | patient: blood urea nitrogen = 13; present; past (2012) | patient: blood urea nitrogen = 24; present; current)
```
Woman of 45 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Oncology follow-up: none.
Latest arterial blood gas shows a pH of 7.42.
Back in 2012, blood urea nitrogen stood at 13 mg/dL.
Blood urea nitrogen 24 mg/dL on the current labs.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: arterial pH = 7.42; present; current | patient: blood urea nitrogen = 31; present; past (2012) | patient: blood urea nitrogen = 13; present; current)
```
Woman of 45 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Oncology follow-up: none.
Latest arterial blood gas shows a pH of 7.42.
Back in 2012, blood urea nitrogen stood at 31 mg/dL.
Blood urea nitrogen 13 mg/dL on the current labs.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: active cancer; absent; current | patient: arterial pH = 7.42; present; current | patient: blood urea nitrogen = 13; present; current | patient: blood urea nitrogen = 13; present; past (2012))
```
Female patient of 45 years.
Community-acquired pneumonia confirmed on chest radiograph; admitted to the medical ward.
Oncology follow-up: none.
Prefers morning appointments.
Current arterial pH 7.42.
Blood urea nitrogen now: 13 mg/dL.
Records from 2012 list blood urea nitrogen at 13 mg/dL.
```


## author2 / group 134: `rule_v1.test.gs123.c3.boundary.easy.666`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

**base** (program answer: s; facts: patient: aspirin use; present; current | patient: serum potassium = 4.0; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Latest potassium result: 4.0 mmol/L.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: patient: aspirin use; present; current | patient: serum potassium = 5.3; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Latest potassium result: 5.3 mmol/L.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: patient: aspirin use; present; current | patient: serum potassium = 5.0; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Latest potassium result: 5.0 mmol/L.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: aspirin use; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: serum potassium = 4.0; present; current)
```
Female patient of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Pupils equal and reactive to light.
Random glucose 92 mg/dL.
Current serum potassium 4.0 mmol/L.
```

**missing** (program answer: neither; facts: patient: aspirin use; present; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 46 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Swallows one low-dose aspirin each night.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
```


## author3 / group 135: `rule_v1.test.gs122.c1.numeric.long.130`

Rule: For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the current systolic blood pressure is above 160 mmHg; the age of the patient is 75 years or more; the patient has ever had asthma (current or past).

**base** (program answer: s; facts: patient: asthma at any time; absent; current | patient: systolic blood pressure = 137; present; current | patient: age = 78; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Drives a car.
Owns a bicycle.
Prefers morning appointments.
Knits as a hobby.
Lungs clear, without wheeze or prolonged expiration.
Sleeps seven hours a night.
Current systolic blood pressure 137 mmHg.
Zinc of 85 mcg/dL in 2009.
Current age 78 years.
His roommate wears contact lenses.
Sees a dentist yearly.
Paints watercolors as a hobby.
His sister sprained a thumb last month.
His wife lives with psoriasis.
His friend burned a hand on a stove years ago.
Enjoys board games.
Photographs local wildlife.
Has two cats.
Plays the piano.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Teeth in good repair.
In 2019, lipase was 30 U/L.
```

**flip** (program answer: s'; facts: patient: asthma at any time; absent; current | patient: systolic blood pressure = 168; present; current | patient: age = 78; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Drives a car.
Owns a bicycle.
Prefers morning appointments.
Knits as a hobby.
Lungs clear, without wheeze or prolonged expiration.
Sleeps seven hours a night.
Current systolic blood pressure 168 mmHg.
Zinc of 85 mcg/dL in 2009.
Current age 78 years.
His roommate wears contact lenses.
Sees a dentist yearly.
Paints watercolors as a hobby.
His sister sprained a thumb last month.
His wife lives with psoriasis.
His friend burned a hand on a stove years ago.
Enjoys board games.
Photographs local wildlife.
Has two cats.
Plays the piano.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Teeth in good repair.
In 2019, lipase was 30 U/L.
```

**near** (program answer: s; facts: patient: asthma at any time; absent; current | patient: systolic blood pressure = 153; present; current | patient: age = 78; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Drives a car.
Owns a bicycle.
Prefers morning appointments.
Knits as a hobby.
Lungs clear, without wheeze or prolonged expiration.
Sleeps seven hours a night.
Current systolic blood pressure 153 mmHg.
Zinc of 85 mcg/dL in 2009.
Current age 78 years.
His roommate wears contact lenses.
Sees a dentist yearly.
Paints watercolors as a hobby.
His sister sprained a thumb last month.
His wife lives with psoriasis.
His friend burned a hand on a stove years ago.
Enjoys board games.
Photographs local wildlife.
Has two cats.
Plays the piano.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Teeth in good repair.
In 2019, lipase was 30 U/L.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 137; present; current | patient: age = 78; present; current | patient: asthma at any time; absent; current)
```
An adult man.
Primary prevention; LDL cholesterol 182 mg/dL.
Observations now: blood pressure 137/90 mmHg.
Drives a car.
Knits as a hobby.
Plays the piano.
Sees a dentist yearly.
Has two cats.
Enjoys board games.
His wife lives with psoriasis.
Paints watercolors as a hobby.
His sister sprained a thumb last month.
His friend burned a hand on a stove years ago.
Photographs local wildlife.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Teeth in good repair.
Currently aged 78 years.
Owns a bicycle.
Lungs clear, without wheeze or prolonged expiration.
In 2019, lipase was 30 U/L.
Prefers morning appointments.
His roommate wears contact lenses.
Zinc of 85 mcg/dL in 2009.
Sleeps seven hours a night.
```

**missing** (program answer: neither; facts: patient: asthma at any time; absent; current | patient: age = 78; present; current)
```
Man, adult.
Primary prevention; LDL cholesterol 182 mg/dL.
Drives a car.
Owns a bicycle.
Prefers morning appointments.
Knits as a hobby.
Lungs clear, without wheeze or prolonged expiration.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2009.
Current age 78 years.
His roommate wears contact lenses.
Sees a dentist yearly.
Paints watercolors as a hobby.
His sister sprained a thumb last month.
His wife lives with psoriasis.
His friend burned a hand on a stove years ago.
Enjoys board games.
Photographs local wildlife.
Has two cats.
Plays the piano.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Teeth in good repair.
In 2019, lipase was 30 U/L.
```


## author4 / group 136: `rule_v1.test.inv049.c2.numeric.long.578`

Rule: For Corvane syndrome, prescribe zephalin. If at least two of the following apply, prescribe trivosan instead: the current systolic blood pressure is 90 mmHg or less; the current weight is 60 kg or less; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: systolic blood pressure = 139; present; current | patient: weight = 74; present; current)
```
Male patient of 30 years.
Referred with Corvane syndrome.
His father sprained a thumb last month.
Owns a bicycle.
Paints watercolors as a hobby.
Has an acute pulmonary embolism, diagnosed this week.
Observations now: blood pressure 139/91 mmHg.
Knits as a hobby.
In 2019, lipase was 30 U/L.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister wears contact lenses.
Teeth in good repair.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Lives in a second-floor apartment.
Photographs local wildlife.
Drives a car.
His uncle has recovered from a dislocated finger.
Has two cats.
Prefers morning appointments.
His friend lives with psoriasis.
Plays the piano.
Latest weight 74 kg.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: systolic blood pressure = 139; present; current | patient: weight = 50; present; current)
```
Male patient of 30 years.
Referred with Corvane syndrome.
His father sprained a thumb last month.
Owns a bicycle.
Paints watercolors as a hobby.
Has an acute pulmonary embolism, diagnosed this week.
Observations now: blood pressure 139/91 mmHg.
Knits as a hobby.
In 2019, lipase was 30 U/L.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister wears contact lenses.
Teeth in good repair.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Lives in a second-floor apartment.
Photographs local wildlife.
Drives a car.
His uncle has recovered from a dislocated finger.
Has two cats.
Prefers morning appointments.
His friend lives with psoriasis.
Plays the piano.
Latest weight 50 kg.
Enjoys board games.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: systolic blood pressure = 139; present; current | patient: weight = 63; present; current)
```
Male patient of 30 years.
Referred with Corvane syndrome.
His father sprained a thumb last month.
Owns a bicycle.
Paints watercolors as a hobby.
Has an acute pulmonary embolism, diagnosed this week.
Observations now: blood pressure 139/91 mmHg.
Knits as a hobby.
In 2019, lipase was 30 U/L.
Sees a dentist yearly.
Pupils equal and reactive to light.
His sister wears contact lenses.
Teeth in good repair.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Lives in a second-floor apartment.
Photographs local wildlife.
Drives a car.
His uncle has recovered from a dislocated finger.
Has two cats.
Prefers morning appointments.
His friend lives with psoriasis.
Plays the piano.
Latest weight 63 kg.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 139; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current | patient: weight = 74; present; current)
```
Man of 30 years.
Referred with Corvane syndrome.
Sees a dentist yearly.
Current systolic blood pressure 139 mmHg.
Owns a bicycle.
Has an acute pulmonary embolism, diagnosed this week.
His sister wears contact lenses.
Prefers morning appointments.
His father sprained a thumb last month.
In 2019, lipase was 30 U/L.
Knits as a hobby.
Has two cats.
Lives in a second-floor apartment.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2024.
His uncle has recovered from a dislocated finger.
Drives a car.
Current weight 74 kg.
His friend lives with psoriasis.
Paints watercolors as a hobby.
Photographs local wildlife.
Enjoys board games.
Plays the piano.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
```


## author1 / group 137: `rule_v1.test.gs219.c2.boundary.long.691`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: serum potassium = 4.4; present; current | patient: coronary artery disease; present; current)
```
Woman of 55 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2014.
Owns a bicycle.
Teeth in good repair.
Lives in a second-floor apartment.
In 2023, lipase was 30 U/L.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Tonsils pink and clean on inspection.
Photographs local wildlife.
Drives a car.
Current serum potassium 4.4 mmol/L.
Her wife lives with psoriasis.
Enjoys board games.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Her sister wears contact lenses.
Has two cats.
Uses sunscreen in summer.
Prefers to be addressed by first name.
During a checkup in 2010, total protein was 7.0 g/dL.
Sees a dentist yearly.
Paints watercolors as a hobby.
Has coronary artery disease, managed medically.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; absent; current | patient: serum potassium = 5.7; present; current | patient: coronary artery disease; present; current)
```
Woman of 55 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2014.
Owns a bicycle.
Teeth in good repair.
Lives in a second-floor apartment.
In 2023, lipase was 30 U/L.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Tonsils pink and clean on inspection.
Photographs local wildlife.
Drives a car.
Current serum potassium 5.7 mmol/L.
Her wife lives with psoriasis.
Enjoys board games.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Her sister wears contact lenses.
Has two cats.
Uses sunscreen in summer.
Prefers to be addressed by first name.
During a checkup in 2010, total protein was 7.0 g/dL.
Sees a dentist yearly.
Paints watercolors as a hobby.
Has coronary artery disease, managed medically.
```

**near** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: serum potassium = 5.0; present; current | patient: coronary artery disease; present; current)
```
Woman of 55 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2014.
Owns a bicycle.
Teeth in good repair.
Lives in a second-floor apartment.
In 2023, lipase was 30 U/L.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Tonsils pink and clean on inspection.
Photographs local wildlife.
Drives a car.
Current serum potassium 5.0 mmol/L.
Her wife lives with psoriasis.
Enjoys board games.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Her sister wears contact lenses.
Has two cats.
Uses sunscreen in summer.
Prefers to be addressed by first name.
During a checkup in 2010, total protein was 7.0 g/dL.
Sees a dentist yearly.
Paints watercolors as a hobby.
Has coronary artery disease, managed medically.
```

**pres** (program answer: s; facts: patient: coronary artery disease; present; current | patient: tonsillar exudate; absent; current | patient: serum potassium = 4.4; present; current)
```
Female patient of 55 years.
Acute low back pain after lifting.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Owns a bicycle.
Pupils equal and reactive to light.
In 2023, lipase was 30 U/L.
Lives in a second-floor apartment.
During a checkup in 2010, total protein was 7.0 g/dL.
Has coronary artery disease, managed medically.
Enjoys board games.
Prefers to be addressed by first name.
Tonsils pink and clean on inspection.
Drives a car.
Latest potassium result: 4.4 mmol/L.
Her sister wears contact lenses.
Knits as a hobby.
Photographs local wildlife.
Uses sunscreen in summer.
Her friend burned a hand on a stove years ago.
Her wife lives with psoriasis.
Sees a dentist yearly.
Teeth in good repair.
Has two cats.
Free T4 of 1.2 ng/dL in 2014.
```

**missing** (program answer: neither; facts: patient: tonsillar exudate; absent; current | patient: coronary artery disease; present; current)
```
Woman of 55 years.
Acute low back pain after lifting.
Free T4 of 1.2 ng/dL in 2014.
Owns a bicycle.
Teeth in good repair.
Lives in a second-floor apartment.
In 2023, lipase was 30 U/L.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Tonsils pink and clean on inspection.
Photographs local wildlife.
Drives a car.
Her wife lives with psoriasis.
Enjoys board games.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Her sister wears contact lenses.
Has two cats.
Uses sunscreen in summer.
Prefers to be addressed by first name.
During a checkup in 2010, total protein was 7.0 g/dL.
Sees a dentist yearly.
Paints watercolors as a hobby.
Has coronary artery disease, managed medically.
```


## author2 / group 138: `rule_v1.test.gs010.c3.time.superseded.892`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

**base** (program answer: s; facts: patient: white cell count = 10.5; present; current | patient: colorectal cancer (patient or first-degree relative); present; past (2007) | patient: white cell count = 9.1; present; past | patient: coronary artery disease; present; current)
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

**flip** (program answer: s'; facts: patient: white cell count = 13.2; present; current | patient: colorectal cancer (patient or first-degree relative); present; past (2007) | patient: white cell count = 9.1; present; past | patient: coronary artery disease; present; current)
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

**near** (program answer: s; facts: patient: white cell count = 10.5; present; current | patient: colorectal cancer (patient or first-degree relative); present; past (2007) | patient: white cell count = 13.5; present; past | patient: coronary artery disease; present; current)
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

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); present; past (2007) | patient: coronary artery disease; present; current | patient: white cell count = 10.5; present; current | patient: white cell count = 9.1; present; past)
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

**missing** (program answer: neither; facts: patient: colorectal cancer (patient or first-degree relative); present; past (2007) | patient: coronary artery disease; present; current)
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


## author3 / group 139: `rule_v1.test.gs120.c3.time.superseded.816`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the patient has ever had a peptic ulcer (current or past); the current weight is 60 kg or less.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: weight = 68; present; past | patient: weight = 73; present; current | patient: peptic ulcer at any time; absent; current)
```
Female patient of 56 years.
First day after elective total hip replacement.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 68 kg; the newest measurement replaces it.
Latest weight 73 kg.
Appetite good; no indigestion.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: weight = 68; present; past | patient: weight = 60; present; current | patient: peptic ulcer at any time; absent; current)
```
Female patient of 56 years.
First day after elective total hip replacement.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 68 kg; the newest measurement replaces it.
Latest weight 60 kg.
Appetite good; no indigestion.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: weight = 55; present; past | patient: weight = 73; present; current | patient: peptic ulcer at any time; absent; current)
```
Female patient of 56 years.
First day after elective total hip replacement.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 55 kg; the newest measurement replaces it.
Latest weight 73 kg.
Appetite good; no indigestion.
```

**pres** (program answer: s; facts: patient: weight = 73; present; current | patient: peptic ulcer at any time; absent; current | patient: venous thromboembolism (patient or first-degree relative); present; current | patient: weight = 68; present; past)
```
Woman of 56 years.
First day after elective total hip replacement.
Current weight 73 kg.
Appetite good; no indigestion.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 68 kg; the newest measurement replaces it.
```


## author4 / group 140: `rule_v1.test.s3_blatchford.bun.boundary.long.599`

Rule: Glasgow-Blatchford score (as used here, partial): 2 points for a current blood urea nitrogen above 18 mg/dL; 1 point for a current systolic blood pressure below 110 mmHg; 1 point for a current heart rate of 100/min or more; 2 points for current heart failure. Other Glasgow-Blatchford items are not part of this question.

**base** (program answer: s; facts: patient: blood urea nitrogen = 10; present; current | patient: heart rate = 84; present; current | patient: heart failure; absent; current | patient: systolic blood pressure = 136; present; current)
```
Woman of 63 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Uses sunscreen in summer.
Knits as a hobby.
Her father has recovered from a dislocated finger.
Blood urea nitrogen 10 mg/dL on the current labs.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Heart rate now 84/min on a pulse check.
Prefers to be addressed by first name.
Drives a car.
Teeth in good repair.
During a checkup in 2024, total protein was 7.0 g/dL.
Heart sounds without a gallop.
Enjoys board games.
Sleeps seven hours a night.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
Paints watercolors as a hobby.
Plays the piano.
Her sister has a lazy eye.
Photographs local wildlife.
Observations now: blood pressure 136/90 mmHg.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: blood urea nitrogen = 20; present; current | patient: heart rate = 84; present; current | patient: heart failure; absent; current | patient: systolic blood pressure = 136; present; current)
```
Woman of 63 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Uses sunscreen in summer.
Knits as a hobby.
Her father has recovered from a dislocated finger.
Blood urea nitrogen 20 mg/dL on the current labs.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Heart rate now 84/min on a pulse check.
Prefers to be addressed by first name.
Drives a car.
Teeth in good repair.
During a checkup in 2024, total protein was 7.0 g/dL.
Heart sounds without a gallop.
Enjoys board games.
Sleeps seven hours a night.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
Paints watercolors as a hobby.
Plays the piano.
Her sister has a lazy eye.
Photographs local wildlife.
Observations now: blood pressure 136/90 mmHg.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: blood urea nitrogen = 18; present; current | patient: heart rate = 84; present; current | patient: heart failure; absent; current | patient: systolic blood pressure = 136; present; current)
```
Woman of 63 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Uses sunscreen in summer.
Knits as a hobby.
Her father has recovered from a dislocated finger.
Blood urea nitrogen 18 mg/dL on the current labs.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Heart rate now 84/min on a pulse check.
Prefers to be addressed by first name.
Drives a car.
Teeth in good repair.
During a checkup in 2024, total protein was 7.0 g/dL.
Heart sounds without a gallop.
Enjoys board games.
Sleeps seven hours a night.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
Paints watercolors as a hobby.
Plays the piano.
Her sister has a lazy eye.
Photographs local wildlife.
Observations now: blood pressure 136/90 mmHg.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: heart rate = 84; present; current | patient: systolic blood pressure = 136; present; current | patient: heart failure; absent; current | patient: blood urea nitrogen = 10; present; current)
```
Female patient of 63 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Her sister has a lazy eye.
Lives in a second-floor apartment.
Drives a car.
Sees a dentist yearly.
Current heart rate 84/min.
Current systolic blood pressure 136 mmHg.
Paints watercolors as a hobby.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Uses sunscreen in summer.
Photographs local wildlife.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Plays the piano.
Her father has recovered from a dislocated finger.
Owns a bicycle.
Prefers morning appointments.
Has two cats.
Enjoys board games.
Heart sounds without a gallop.
Blood urea nitrogen now: 10 mg/dL.
Knits as a hobby.
Prefers to be addressed by first name.
Teeth in good repair.
During a checkup in 2024, total protein was 7.0 g/dL.
```

**missing** (program answer: neither; facts: patient: heart rate = 84; present; current | patient: heart failure; absent; current | patient: systolic blood pressure = 136; present; current)
```
Woman of 63 years.
Vomited fresh blood twice; admitted with upper gastrointestinal bleeding.
Uses sunscreen in summer.
Knits as a hobby.
Her father has recovered from a dislocated finger.
During a checkup in 2015, free T3 was 3.2 pg/mL.
Heart rate now 84/min on a pulse check.
Prefers to be addressed by first name.
Drives a car.
Teeth in good repair.
During a checkup in 2024, total protein was 7.0 g/dL.
Heart sounds without a gallop.
Enjoys board games.
Sleeps seven hours a night.
Has two cats.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
Paints watercolors as a hobby.
Plays the piano.
Her sister has a lazy eye.
Photographs local wildlife.
Observations now: blood pressure 136/90 mmHg.
Prefers morning appointments.
```


## author1 / group 141: `rule_v1.test.gs087.c3.boundary.easy.474`

Rule: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the patient is allergic to penicillin; 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe acetaminophen instead.

**base** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 63; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2018))
```
Man of 81 years.
Knee osteoarthritis with pain on walking.
Penicillin allergy: anaphylaxis.
Pupils equal and reactive to light.
Owns a bicycle.
Heart rate now 63/min on a pulse check.
Recovered from a pulmonary embolism in 2018.
```

**flip** (program answer: s'; facts: patient: penicillin allergy; present; current | patient: heart rate = 96; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2018))
```
Man of 81 years.
Knee osteoarthritis with pain on walking.
Penicillin allergy: anaphylaxis.
Pupils equal and reactive to light.
Owns a bicycle.
Heart rate now 96/min on a pulse check.
Recovered from a pulmonary embolism in 2018.
```

**near** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 90; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2018))
```
Man of 81 years.
Knee osteoarthritis with pain on walking.
Penicillin allergy: anaphylaxis.
Pupils equal and reactive to light.
Owns a bicycle.
Heart rate now 90/min on a pulse check.
Recovered from a pulmonary embolism in 2018.
```

**pres** (program answer: s; facts: patient: heart rate = 63; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2018) | patient: penicillin allergy; present; current)
```
Male patient of 81 years.
Knee osteoarthritis with pain on walking.
Current heart rate 63/min.
Pupils equal and reactive to light.
Recovered from a pulmonary embolism in 2018.
Owns a bicycle.
Penicillin allergy: anaphylaxis.
```

**missing** (program answer: neither; facts: patient: penicillin allergy; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2018))
```
Man of 81 years.
Knee osteoarthritis with pain on walking.
Penicillin allergy: anaphylaxis.
Pupils equal and reactive to light.
Owns a bicycle.
Recovered from a pulmonary embolism in 2018.
```


## author2 / group 142: `rule_v1.test.gs188.c2.time.long.840`

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: ALT = 32; present; past (2024) | patient: peptic ulcer at any time; present; past | patient: ALT = 26; present; current)
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

**flip** (program answer: s'; facts: patient: venous thromboembolism; absent; current | patient: ALT = 32; present; past (2024) | patient: peptic ulcer at any time; present; past | patient: ALT = 141; present; current)
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

**near** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: ALT = 137; present; past (2024) | patient: peptic ulcer at any time; present; past | patient: ALT = 26; present; current)
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

**pres** (program answer: s; facts: patient: ALT = 32; present; past (2024) | patient: peptic ulcer at any time; present; past | patient: venous thromboembolism; absent; current | patient: ALT = 26; present; current)
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


## author3 / group 143: `rule_v1.test.s1_spesi.cancer.subject.easy.977`

Rule: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: heart rate = 92; present; current | patient: age = 57; present; current | patient: oxygen saturation = 100; present; current | patient: active cancer; absent; current | patient: systolic blood pressure = 118; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Current heart rate 92/min.
Owns a bicycle.
Uses sunscreen in summer.
Current age 57 years.
Paints watercolors as a hobby.
Current oxygen saturation 100%.
Weight steady over the past year.
Drives a car.
Observations now: blood pressure 118/80 mmHg.
```

**flip** (program answer: s'; facts: patient: heart rate = 92; present; current | patient: age = 57; present; current | patient: oxygen saturation = 100; present; current | patient: active cancer; present; current | patient: systolic blood pressure = 118; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Current heart rate 92/min.
Owns a bicycle.
Uses sunscreen in summer.
Current age 57 years.
Paints watercolors as a hobby.
Current oxygen saturation 100%.
Has metastatic lung cancer, receiving palliative treatment.
Drives a car.
Observations now: blood pressure 118/80 mmHg.
```

**near** (program answer: s; facts: patient: heart rate = 92; present; current | patient: age = 57; present; current | patient: oxygen saturation = 100; present; current | friend: active cancer; present; current | patient: systolic blood pressure = 118; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Current heart rate 92/min.
Owns a bicycle.
Uses sunscreen in summer.
Current age 57 years.
Paints watercolors as a hobby.
Current oxygen saturation 100%.
His friend has lung cancer that has spread to the liver.
Drives a car.
Observations now: blood pressure 118/80 mmHg.
```

**pres** (program answer: s; facts: patient: heart rate = 92; present; current | patient: age = 57; present; current | patient: active cancer; absent; current | patient: oxygen saturation = 100; present; current | patient: systolic blood pressure = 118; present; current)
```
An adult man.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Uses sunscreen in summer.
Heart rate now 92/min on a pulse check.
Owns a bicycle.
Currently aged 57 years.
Paints watercolors as a hobby.
Drives a car.
Weight steady over the past year.
Latest oxygen saturation reading: 100%.
Current systolic blood pressure 118 mmHg.
```

**missing** (program answer: neither; facts: patient: heart rate = 92; present; current | patient: age = 57; present; current | patient: oxygen saturation = 100; present; current | patient: active cancer; unknown; current | patient: systolic blood pressure = 118; present; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Current heart rate 92/min.
Owns a bicycle.
Uses sunscreen in summer.
Current age 57 years.
Paints watercolors as a hobby.
Current oxygen saturation 100%.
Active cancer: status unclear from the records at hand.
Drives a car.
Observations now: blood pressure 118/80 mmHg.
```


## author4 / group 144: `rule_v1.test.inv013.c2.time.easy.774`

Rule: For Hestin disease, prescribe melcadine. If the patient has ever had a peptic ulcer (current or past) or the patient currently has asthma, prescribe orvitrex instead.

**base** (program answer: s; facts: patient: asthma; absent; current | patient: peptic ulcer at any time; absent; current)
```
Male patient of 35 years.
Referred with Hestin disease.
Uses sunscreen in summer.
Lungs clear, without wheeze or prolonged expiration.
Knits as a hobby.
Sees a dentist yearly.
Appetite good; no indigestion.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: asthma; present; current | patient: peptic ulcer at any time; absent; current)
```
Male patient of 35 years.
Referred with Hestin disease.
Uses sunscreen in summer.
Asthma, on a daily inhaled steroid.
Knits as a hobby.
Sees a dentist yearly.
Appetite good; no indigestion.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: asthma; present; past | patient: peptic ulcer at any time; absent; current)
```
Male patient of 35 years.
Referred with Hestin disease.
Uses sunscreen in summer.
Formerly had asthma in elementary school; well for many years without inhalers.
Knits as a hobby.
Sees a dentist yearly.
Appetite good; no indigestion.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: asthma; absent; current | patient: peptic ulcer at any time; absent; current)
```
Man of 35 years.
Referred with Hestin disease.
Lungs clear, without wheeze or prolonged expiration.
Uses sunscreen in summer.
Knits as a hobby.
Prefers morning appointments.
Sees a dentist yearly.
Appetite good; no indigestion.
```


## author1 / group 145: `rule_v1.test.gs079.c2.subject.long.967`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the current blood urea nitrogen is above 19 mg/dL; the patient has had a major bleeding event at any time; the patient currently has heart failure.

**base** (program answer: s; facts: patient: current heart failure; present; current | patient: blood urea nitrogen = 14; present; current | patient: bleeding history; absent; current)
```
Man of 61 years.
Suspected chest infection; assessed on the medical ward.
Paints watercolors as a hobby.
His uncle has a lazy eye.
During a checkup in 2011, total protein was 7.0 g/dL.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Current heart failure with ankle swelling.
Knits as a hobby.
Blood urea nitrogen 14 mg/dL on the current labs.
Photographs local wildlife.
Plays the piano.
Prefers morning appointments.
Owns a bicycle.
Has two cats.
Prefers to be addressed by first name.
Examination shows no signs of blood loss.
In 2020, folate was 12 ng/mL.
Uses sunscreen in summer.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2018.
His uncle lives with psoriasis.
```

**flip** (program answer: s'; facts: patient: current heart failure; present; current | patient: blood urea nitrogen = 14; present; current | patient: bleeding history; present; past)
```
Man of 61 years.
Suspected chest infection; assessed on the medical ward.
Paints watercolors as a hobby.
His uncle has a lazy eye.
During a checkup in 2011, total protein was 7.0 g/dL.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Current heart failure with ankle swelling.
Knits as a hobby.
Blood urea nitrogen 14 mg/dL on the current labs.
Photographs local wildlife.
Plays the piano.
Prefers morning appointments.
Owns a bicycle.
Has two cats.
Prefers to be addressed by first name.
Major intracranial bleed after a fall years ago, with full recovery.
In 2020, folate was 12 ng/mL.
Uses sunscreen in summer.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2018.
His uncle lives with psoriasis.
```

**near** (program answer: s; facts: patient: current heart failure; present; current | patient: blood urea nitrogen = 14; present; current | sister: bleeding history; present; past)
```
Man of 61 years.
Suspected chest infection; assessed on the medical ward.
Paints watercolors as a hobby.
His uncle has a lazy eye.
During a checkup in 2011, total protein was 7.0 g/dL.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Sees a dentist yearly.
Current heart failure with ankle swelling.
Knits as a hobby.
Blood urea nitrogen 14 mg/dL on the current labs.
Photographs local wildlife.
Plays the piano.
Prefers morning appointments.
Owns a bicycle.
Has two cats.
Prefers to be addressed by first name.
His sister needed a blood transfusion for a major bleed years ago.
In 2020, folate was 12 ng/mL.
Uses sunscreen in summer.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2018.
His uncle lives with psoriasis.
```

**pres** (program answer: s; facts: patient: bleeding history; absent; current | patient: current heart failure; present; current | patient: blood urea nitrogen = 14; present; current)
```
Male patient of 61 years.
Suspected chest infection; assessed on the medical ward.
During a checkup in 2008, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Has two cats.
Free T4 of 1.2 ng/dL in 2018.
Prefers to be addressed by first name.
Examination shows no signs of blood loss.
Sees a dentist yearly.
Photographs local wildlife.
Lives in a second-floor apartment.
Plays the piano.
Prefers morning appointments.
Knits as a hobby.
His uncle has a lazy eye.
Enjoys board games.
Current heart failure with ankle swelling.
Owns a bicycle.
His uncle lives with psoriasis.
Teeth in good repair.
Uses sunscreen in summer.
In 2020, folate was 12 ng/mL.
During a checkup in 2011, total protein was 7.0 g/dL.
Blood urea nitrogen now: 14 mg/dL.
```


## author2 / group 146: `rule_v1.test.s1_spesi.hr.numeric.long.645`

Rule: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: oxygen saturation = 95; present; current | patient: age = 72; present; current | patient: systolic blood pressure = 140; present; current | patient: heart rate = 61; present; current | patient: active cancer; absent; current)
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

**flip** (program answer: s'; facts: patient: oxygen saturation = 95; present; current | patient: age = 72; present; current | patient: systolic blood pressure = 140; present; current | patient: heart rate = 125; present; current | patient: active cancer; absent; current)
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

**near** (program answer: s; facts: patient: oxygen saturation = 95; present; current | patient: age = 72; present; current | patient: systolic blood pressure = 140; present; current | patient: heart rate = 107; present; current | patient: active cancer; absent; current)
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

**pres** (program answer: s; facts: patient: systolic blood pressure = 140; present; current | patient: heart rate = 61; present; current | patient: age = 72; present; current | patient: oxygen saturation = 95; present; current | patient: active cancer; absent; current)
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


## author3 / group 147: `rule_v1.test.gs118.c2.subject.long.855`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: heart rate = 80; present; current | patient: white cell count = 13.1; present; current | patient: eGFR = 87; present; current | patient: angioedema; absent; current)
```
Male patient of 65 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Heart rate now 80/min on a pulse check.
During a checkup in 2005, total protein was 7.0 g/dL.
His friend has a lazy eye.
Drives a car.
Photographs local wildlife.
Prefers morning appointments.
Latest WBC is 13.1 x10^9/L.
Paints watercolors as a hobby.
His sister wears contact lenses.
Lives in a second-floor apartment.
eGFR now 87 mL/min/1.73 m2.
Enjoys board games.
Sleeps seven hours a night.
Knits as a hobby.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2012.
In 2012, lipase was 30 U/L.
His sister lives with psoriasis.
His wife has recovered from a dislocated finger.
Teeth in good repair.
Free of facial or oropharyngeal edema.
Prefers to be addressed by first name.
Plays the piano.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: patient: heart rate = 80; present; current | patient: white cell count = 13.1; present; current | patient: eGFR = 87; present; current | patient: angioedema; present; past)
```
Male patient of 65 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Heart rate now 80/min on a pulse check.
During a checkup in 2005, total protein was 7.0 g/dL.
His friend has a lazy eye.
Drives a car.
Photographs local wildlife.
Prefers morning appointments.
Latest WBC is 13.1 x10^9/L.
Paints watercolors as a hobby.
His sister wears contact lenses.
Lives in a second-floor apartment.
eGFR now 87 mL/min/1.73 m2.
Enjoys board games.
Sleeps seven hours a night.
Knits as a hobby.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2012.
In 2012, lipase was 30 U/L.
His sister lives with psoriasis.
His wife has recovered from a dislocated finger.
Teeth in good repair.
An episode of angioedema years ago, with full recovery.
Prefers to be addressed by first name.
Plays the piano.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: patient: heart rate = 80; present; current | patient: white cell count = 13.1; present; current | patient: eGFR = 87; present; current | sister: angioedema; present; past (2006))
```
Male patient of 65 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Heart rate now 80/min on a pulse check.
During a checkup in 2005, total protein was 7.0 g/dL.
His friend has a lazy eye.
Drives a car.
Photographs local wildlife.
Prefers morning appointments.
Latest WBC is 13.1 x10^9/L.
Paints watercolors as a hobby.
His sister wears contact lenses.
Lives in a second-floor apartment.
eGFR now 87 mL/min/1.73 m2.
Enjoys board games.
Sleeps seven hours a night.
Knits as a hobby.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2012.
In 2012, lipase was 30 U/L.
His sister lives with psoriasis.
His wife has recovered from a dislocated finger.
Teeth in good repair.
His sister recovered from an episode of angioedema in 2006.
Prefers to be addressed by first name.
Plays the piano.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: eGFR = 87; present; current | patient: heart rate = 80; present; current | patient: angioedema; absent; current | patient: white cell count = 13.1; present; current)
```
Man of 65 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Drives a car.
His wife has recovered from a dislocated finger.
Sees a dentist yearly.
Pupils equal and reactive to light.
Current eGFR 87 mL/min/1.73 m2.
Free T4 of 1.2 ng/dL in 2012.
Teeth in good repair.
Paints watercolors as a hobby.
Current heart rate 80/min.
Plays the piano.
Free of facial or oropharyngeal edema.
Current white cell count 13.1 x10^9/L.
Lives in a second-floor apartment.
His sister lives with psoriasis.
In 2012, lipase was 30 U/L.
Photographs local wildlife.
Sleeps seven hours a night.
Prefers to be addressed by first name.
During a checkup in 2005, total protein was 7.0 g/dL.
His friend has a lazy eye.
Knits as a hobby.
Enjoys board games.
His sister wears contact lenses.
Prefers morning appointments.
```


## author4 / group 148: `rule_v1.test.cut_vte.vte.negation.long.1602`

Rule: For thromboprophylaxis in a medical inpatient, prescribe compression stockings. Score 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. If the score is 4 or more, prescribe enoxaparin instead.

**base** (program answer: s; facts: patient: age = 49; present; current | patient: active cancer; absent; current | patient: venous thromboembolism; absent; current | patient: heart failure; present; current)
```
Woman, adult.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Plays the piano.
Her sister has a lazy eye.
Drives a car.
Pupils equal and reactive to light.
Her friend wears contact lenses.
During a checkup in 2022, total protein was 7.0 g/dL.
Currently aged 49 years.
Zinc of 85 mcg/dL in 2014.
Prefers morning appointments.
Has two cats.
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Weight steady over the past year.
Lives in a second-floor apartment.
In 2015, folate was 12 ng/mL.
Knits as a hobby.
Varicose veins: none seen.
Has heart failure, treated with diuretics.
Her uncle lives with psoriasis.
```

**flip** (program answer: s'; facts: patient: age = 49; present; current | patient: active cancer; absent; current | patient: venous thromboembolism; present; current | patient: heart failure; present; current)
```
Woman, adult.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Plays the piano.
Her sister has a lazy eye.
Drives a car.
Pupils equal and reactive to light.
Her friend wears contact lenses.
During a checkup in 2022, total protein was 7.0 g/dL.
Currently aged 49 years.
Zinc of 85 mcg/dL in 2014.
Prefers morning appointments.
Has two cats.
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Weight steady over the past year.
Lives in a second-floor apartment.
In 2015, folate was 12 ng/mL.
Knits as a hobby.
Has an acute pulmonary embolism, diagnosed this week.
Has heart failure, treated with diuretics.
Her uncle lives with psoriasis.
```

**near** (program answer: s; facts: patient: age = 49; present; current | patient: active cancer; absent; current | patient: venous thromboembolism; absent; current | patient: heart failure; present; current)
```
Woman, adult.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Plays the piano.
Her sister has a lazy eye.
Drives a car.
Pupils equal and reactive to light.
Her friend wears contact lenses.
During a checkup in 2022, total protein was 7.0 g/dL.
Currently aged 49 years.
Zinc of 85 mcg/dL in 2014.
Prefers morning appointments.
Has two cats.
In 2020, lipase was 30 U/L.
Paints watercolors as a hobby.
Weight steady over the past year.
Lives in a second-floor apartment.
In 2015, folate was 12 ng/mL.
Knits as a hobby.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
Has heart failure, treated with diuretics.
Her uncle lives with psoriasis.
```

**pres** (program answer: s; facts: patient: age = 49; present; current | patient: heart failure; present; current | patient: venous thromboembolism; absent; current | patient: active cancer; absent; current)
```
An adult woman.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Prefers morning appointments.
Knits as a hobby.
Her sister has a lazy eye.
Current age 49 years.
Has heart failure, treated with diuretics.
In 2020, lipase was 30 U/L.
Her friend wears contact lenses.
Pupils equal and reactive to light.
Varicose veins: none seen.
Has two cats.
Weight steady over the past year.
Lives in a second-floor apartment.
During a checkup in 2022, total protein was 7.0 g/dL.
Drives a car.
Plays the piano.
Paints watercolors as a hobby.
Her uncle lives with psoriasis.
In 2015, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2014.
```


## author1 / group 149: `rule_v1.test.gs067.c2.negation.easy.604`

Rule: For knee osteoarthritis pain, prescribe naproxen. If the patient is allergic to penicillin and the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time, prescribe acetaminophen instead.

**base** (program answer: s; facts: patient: coronary artery disease (patient or first-degree relative); absent; current | patient: penicillin allergy; present; current)
```
Female patient of 75 years.
Knee osteoarthritis with pain on walking.
Owns a bicycle.
Chest pain on exertion: none reported.
Known penicillin allergy with angioedema.
```

**flip** (program answer: s'; facts: patient: coronary artery disease (patient or first-degree relative); present; past | patient: penicillin allergy; present; current)
```
Female patient of 75 years.
Knee osteoarthritis with pain on walking.
Owns a bicycle.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Known penicillin allergy with angioedema.
```

**near** (program answer: s; facts: patient: coronary artery disease (patient or first-degree relative); absent; current | patient: penicillin allergy; present; current)
```
Female patient of 75 years.
Knee osteoarthritis with pain on walking.
Owns a bicycle.
Has never had coronary artery disease.
Known penicillin allergy with angioedema.
```

**pres** (program answer: s; facts: patient: penicillin allergy; present; current | patient: coronary artery disease (patient or first-degree relative); absent; current)
```
Woman of 75 years.
Knee osteoarthritis with pain on walking.
Known penicillin allergy with angioedema.
Chest pain on exertion: none reported.
Owns a bicycle.
```

**missing** (program answer: neither; facts: patient: coronary artery disease (patient or first-degree relative); unknown; current | patient: penicillin allergy; present; current)
```
Female patient of 75 years.
Knee osteoarthritis with pain on walking.
Owns a bicycle.
Coronary artery disease (patient or first-degree relative): unknown.
Known penicillin allergy with angioedema.
```


## author2 / group 150: `rule_v1.test.news2_red.rr.numeric.easy.1313`

Rule: NEWS2 (as used here, single-parameter red items only): 3 points each for a respiratory rate of 25/min or more; oxygen saturation of 91% or less; systolic blood pressure of 90 mmHg or less; new confusion. Only current findings count.

**base** (program answer: s; facts: patient: systolic blood pressure = 143; present; current | patient: respiratory rate = 15; present; current | patient: oxygen saturation = 96; present; current)
```
Female patient of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current systolic blood pressure 143 mmHg.
Current respiratory rate 15/min.
Latest oxygen saturation reading: 96%.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 143; present; current | patient: respiratory rate = 34; present; current | patient: oxygen saturation = 96; present; current)
```
Female patient of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current systolic blood pressure 143 mmHg.
Current respiratory rate 34/min.
Latest oxygen saturation reading: 96%.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 143; present; current | patient: respiratory rate = 23; present; current | patient: oxygen saturation = 96; present; current)
```
Female patient of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current systolic blood pressure 143 mmHg.
Current respiratory rate 23/min.
Latest oxygen saturation reading: 96%.
```

**pres** (program answer: s; facts: patient: oxygen saturation = 96; present; current | patient: systolic blood pressure = 143; present; current | patient: respiratory rate = 15; present; current)
```
Woman of 54 years.
Shortness of breath and fever; assessed on the medical ward.
Drives a car.
Current oxygen saturation 96%.
Observations now: blood pressure 143/94 mmHg.
Observations now: respiratory rate 15/min.
```


## author3 / group 151: `rule_v1.test.s1_meds.ams.negation.long.449`

Rule: Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.

**base** (program answer: s; facts: patient: age = 48; present; current | patient: platelet count = 195; present; current | patient: altered mental status; absent; current)
```
An adult woman.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Plays the piano.
Paints watercolors as a hobby.
Current age 48 years.
During a checkup in 2007, total protein was 7.0 g/dL.
Owns a bicycle.
Teeth in good repair.
Her friend has a lazy eye.
Platelet count now 195 x10^9/L.
Photographs local wildlife.
Prefers morning appointments.
Her friend sprained a thumb last month.
Prefers to be addressed by first name.
Knits as a hobby.
Speech clear; follows commands.
Pupils equal and reactive to light.
Sees a dentist yearly.
In 2012, lipase was 30 U/L.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: age = 48; present; current | patient: platelet count = 195; present; current | patient: altered mental status; present; current)
```
An adult woman.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Plays the piano.
Paints watercolors as a hobby.
Current age 48 years.
During a checkup in 2007, total protein was 7.0 g/dL.
Owns a bicycle.
Teeth in good repair.
Her friend has a lazy eye.
Platelet count now 195 x10^9/L.
Photographs local wildlife.
Prefers morning appointments.
Her friend sprained a thumb last month.
Prefers to be addressed by first name.
Knits as a hobby.
Disoriented to time and place, which is new for the patient.
Pupils equal and reactive to light.
Sees a dentist yearly.
In 2012, lipase was 30 U/L.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: age = 48; present; current | patient: platelet count = 195; present; current | patient: altered mental status; absent; current)
```
An adult woman.
Suspected sepsis; admitted from the emergency department.
Has two cats.
Plays the piano.
Paints watercolors as a hobby.
Current age 48 years.
During a checkup in 2007, total protein was 7.0 g/dL.
Owns a bicycle.
Teeth in good repair.
Her friend has a lazy eye.
Platelet count now 195 x10^9/L.
Photographs local wildlife.
Prefers morning appointments.
Her friend sprained a thumb last month.
Prefers to be addressed by first name.
Knits as a hobby.
Confusion absent; answers questions appropriately.
Pupils equal and reactive to light.
Sees a dentist yearly.
In 2012, lipase was 30 U/L.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: altered mental status; absent; current | patient: age = 48; present; current | patient: platelet count = 195; present; current)
```
Woman, adult.
Suspected sepsis; admitted from the emergency department.
Knits as a hobby.
Speech clear; follows commands.
Her friend sprained a thumb last month.
During a checkup in 2007, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Currently aged 48 years.
Prefers morning appointments.
Owns a bicycle.
Teeth in good repair.
Current platelet count 195 x10^9/L.
Sees a dentist yearly.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Has two cats.
Her friend has a lazy eye.
Photographs local wildlife.
Plays the piano.
In 2012, lipase was 30 U/L.
```


## author4 / group 152: `rule_v1.test.c1_transfusion.hgb.time.alt.692`

Rule: For anemia after hip fracture surgery, prescribe oral iron. If the current hemoglobin is below 10.0 g/dL, prescribe a red cell transfusion instead.

**base** (program answer: s; facts: patient: hemoglobin = 11.3; present; current | patient: hemoglobin = 10.6; present; past (2007))
```
Female patient of 89 years.
Second day after surgical repair of a hip fracture; hemodynamically stable.
Latest Hgb result: 11.3 g/dL.
Enjoys board games.
Records from 2007 list Hgb at 10.6 g/dL.
```

**flip** (program answer: s'; facts: patient: hemoglobin = 9.2; present; current | patient: hemoglobin = 10.6; present; past (2007))
```
Female patient of 89 years.
Second day after surgical repair of a hip fracture; hemodynamically stable.
Latest Hgb result: 9.2 g/dL.
Enjoys board games.
Records from 2007 list Hgb at 10.6 g/dL.
```

**near** (program answer: s; facts: patient: hemoglobin = 11.3; present; current | patient: hemoglobin = 7.3; present; past (2007))
```
Female patient of 89 years.
Second day after surgical repair of a hip fracture; hemodynamically stable.
Latest Hgb result: 11.3 g/dL.
Enjoys board games.
Records from 2007 list Hgb at 7.3 g/dL.
```

**pres** (program answer: s; facts: patient: hemoglobin = 10.6; present; past (2007) | patient: hemoglobin = 11.3; present; current)
```
Woman of 89 years.
Second day after surgical repair of a hip fracture; hemodynamically stable.
Back in 2007, Hgb stood at 10.6 g/dL.
Current Hgb 11.3 g/dL.
Enjoys board games.
```


## author1 / group 153: `rule_v1.test.s1_meds.plt.boundary.easy.1554`

Rule: Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.

**base** (program answer: s; facts: patient: platelet count = 332; present; current | patient: altered mental status; absent; current | patient: age = 47; present; current)
```
Woman, adult.
Suspected sepsis; admitted from the emergency department.
Enjoys board games.
Platelet count now 332 x10^9/L.
Speech clear; follows commands.
Photographs local wildlife.
Sleeps seven hours a night.
Currently aged 47 years.
```

**flip** (program answer: s'; facts: patient: platelet count = 130; present; current | patient: altered mental status; absent; current | patient: age = 47; present; current)
```
Woman, adult.
Suspected sepsis; admitted from the emergency department.
Enjoys board games.
Platelet count now 130 x10^9/L.
Speech clear; follows commands.
Photographs local wildlife.
Sleeps seven hours a night.
Currently aged 47 years.
```

**near** (program answer: s; facts: patient: platelet count = 150; present; current | patient: altered mental status; absent; current | patient: age = 47; present; current)
```
Woman, adult.
Suspected sepsis; admitted from the emergency department.
Enjoys board games.
Platelet count now 150 x10^9/L.
Speech clear; follows commands.
Photographs local wildlife.
Sleeps seven hours a night.
Currently aged 47 years.
```

**pres** (program answer: s; facts: patient: altered mental status; absent; current | patient: age = 47; present; current | patient: platelet count = 332; present; current)
```
An adult woman.
Suspected sepsis; admitted from the emergency department.
Sleeps seven hours a night.
Speech clear; follows commands.
Current age 47 years.
Enjoys board games.
Current platelet count 332 x10^9/L.
Photographs local wildlife.
```


## author2 / group 154: `rule_v1.test.gs224.c1.subject.easy.1033`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had a venous thromboembolism (current or past) and the current serum creatinine is above 2.0 mg/dL, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: serum creatinine = 2.4; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Coagulation tests normal on recent bloodwork.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; present; past | patient: serum creatinine = 2.4; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Pulmonary embolism years ago, treated for six months.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```

**near** (program answer: s; facts: roommate: venous thromboembolism; present; past | patient: serum creatinine = 2.4; present; current)
```
Female patient of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her roommate had a DVT years ago.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```

**pres** (program answer: s; facts: patient: serum creatinine = 2.4; present; current | patient: venous thromboembolism; absent; current)
```
Woman of 22 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current serum creatinine 2.4 mg/dL.
Coagulation tests normal on recent bloodwork.
Plays the piano.
```


## author3 / group 155: `rule_v1.test.gs230.c3.numeric.long.1163`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 2 points if the patient currently has tonsillar exudate; 3 points if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past). If the score is 8 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; present; past | patient: peptic ulcer at any time; present; past | patient: tonsillar exudate; present; current | patient: calf swelling = 1.4; present; current)
```
Woman of 51 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Heart attack years ago, with full recovery.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Duodenal ulcer years ago; recovered fully with treatment.
In 2006, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2020.
Prefers morning appointments.
Teeth in good repair.
During a checkup in 2020, total protein was 7.0 g/dL.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Uses sunscreen in summer.
Has two cats.
Tonsils swollen and coated with yellow exudate.
Knits as a hobby.
Paints watercolors as a hobby.
Photographs local wildlife.
Drives a car.
Pupils equal and reactive to light.
Enjoys board games.
Plays the piano.
Current calf swelling 1.4 cm compared with the other leg.
Her friend lives with psoriasis.
```

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; present; past | patient: peptic ulcer at any time; present; past | patient: tonsillar exudate; present; current | patient: calf swelling = 3.0; present; current)
```
Woman of 51 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Heart attack years ago, with full recovery.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Duodenal ulcer years ago; recovered fully with treatment.
In 2006, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2020.
Prefers morning appointments.
Teeth in good repair.
During a checkup in 2020, total protein was 7.0 g/dL.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Uses sunscreen in summer.
Has two cats.
Tonsils swollen and coated with yellow exudate.
Knits as a hobby.
Paints watercolors as a hobby.
Photographs local wildlife.
Drives a car.
Pupils equal and reactive to light.
Enjoys board games.
Plays the piano.
Current calf swelling 3.0 cm compared with the other leg.
Her friend lives with psoriasis.
```

**near** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; present; past | patient: peptic ulcer at any time; present; past | patient: tonsillar exudate; present; current | patient: calf swelling = 2.8; present; current)
```
Woman of 51 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Heart attack years ago, with full recovery.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Duodenal ulcer years ago; recovered fully with treatment.
In 2006, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2020.
Prefers morning appointments.
Teeth in good repair.
During a checkup in 2020, total protein was 7.0 g/dL.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Uses sunscreen in summer.
Has two cats.
Tonsils swollen and coated with yellow exudate.
Knits as a hobby.
Paints watercolors as a hobby.
Photographs local wildlife.
Drives a car.
Pupils equal and reactive to light.
Enjoys board games.
Plays the piano.
Current calf swelling 2.8 cm compared with the other leg.
Her friend lives with psoriasis.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; present; current | patient: peptic ulcer at any time; present; past | patient: myocardial infarction or peripheral artery disease; present; past | patient: calf swelling = 1.4; present; current)
```
Female patient of 51 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
During a checkup in 2020, total protein was 7.0 g/dL.
Her sister burned a hand on a stove years ago.
In 2006, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2020.
Uses sunscreen in summer.
Tonsils swollen and coated with yellow exudate.
Knits as a hobby.
Duodenal ulcer years ago; recovered fully with treatment.
Enjoys board games.
Pupils equal and reactive to light.
Drives a car.
Prefers morning appointments.
Sleeps seven hours a night.
Her friend lives with psoriasis.
Photographs local wildlife.
Plays the piano.
Heart attack years ago, with full recovery.
Has two cats.
Teeth in good repair.
Difference in calf circumference now 1.4 cm.
During a checkup in 2020, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
```


## author4 / group 156: `rule_v1.test.gs124.c3.boundary.long.705`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**base** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 49; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Hemoglobin within the normal range on recent blood tests.
Has two cats.
Plays the piano.
Uses sunscreen in summer.
Knits as a hobby.
His sister wears contact lenses.
His friend has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2015.
Owns a bicycle.
Teeth in good repair.
Photographs local wildlife.
Sleeps seven hours a night.
His friend burned a hand on a stove years ago.
Prefers morning appointments.
Enjoys board games.
Difference in calf circumference now 3.6 cm.
In 2014, folate was 12 ng/mL.
During a checkup in 2008, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Currently aged 49 years.
Drives a car.
```

**flip** (program answer: s'; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 71; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Hemoglobin within the normal range on recent blood tests.
Has two cats.
Plays the piano.
Uses sunscreen in summer.
Knits as a hobby.
His sister wears contact lenses.
His friend has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2015.
Owns a bicycle.
Teeth in good repair.
Photographs local wildlife.
Sleeps seven hours a night.
His friend burned a hand on a stove years ago.
Prefers morning appointments.
Enjoys board games.
Difference in calf circumference now 3.6 cm.
In 2014, folate was 12 ng/mL.
During a checkup in 2008, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Currently aged 71 years.
Drives a car.
```

**near** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 65; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Hemoglobin within the normal range on recent blood tests.
Has two cats.
Plays the piano.
Uses sunscreen in summer.
Knits as a hobby.
His sister wears contact lenses.
His friend has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2015.
Owns a bicycle.
Teeth in good repair.
Photographs local wildlife.
Sleeps seven hours a night.
His friend burned a hand on a stove years ago.
Prefers morning appointments.
Enjoys board games.
Difference in calf circumference now 3.6 cm.
In 2014, folate was 12 ng/mL.
During a checkup in 2008, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Currently aged 65 years.
Drives a car.
```

**pres** (program answer: s; facts: patient: age = 49; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Current age 49 years.
Has two cats.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2015.
His friend has recovered from a dislocated finger.
Sleeps seven hours a night.
His friend burned a hand on a stove years ago.
Hemoglobin within the normal range on recent blood tests.
Owns a bicycle.
Uses sunscreen in summer.
Teeth in good repair.
His sister wears contact lenses.
Plays the piano.
Drives a car.
During a checkup in 2008, total protein was 7.0 g/dL.
Prefers to be addressed by first name.
Knits as a hobby.
Photographs local wildlife.
Enjoys board games.
In 2014, folate was 12 ng/mL.
Current calf swelling 3.6 cm compared with the other leg.
```


## author1 / group 157: `rule_v1.test.inv045.c1.boundary.easy.100`

Rule: For Pallis disease, prescribe brexadol. If the current white cell count is above 12.0 x10^9/L, prescribe corlitane instead.

**base** (program answer: s; facts: patient: white cell count = 8.6; present; current)
```
Man of 38 years.
Referred with Pallis disease.
Owns a bicycle.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest WBC is 8.6 x10^9/L.
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: white cell count = 14.3; present; current)
```
Man of 38 years.
Referred with Pallis disease.
Owns a bicycle.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest WBC is 14.3 x10^9/L.
Teeth in good repair.
```

**near** (program answer: s; facts: patient: white cell count = 12.0; present; current)
```
Man of 38 years.
Referred with Pallis disease.
Owns a bicycle.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest WBC is 12.0 x10^9/L.
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: white cell count = 8.6; present; current)
```
Male patient of 38 years.
Referred with Pallis disease.
Owns a bicycle.
Lives in a second-floor apartment.
Current white cell count 8.6 x10^9/L.
Teeth in good repair.
Sees a dentist yearly.
```


## author2 / group 158: `rule_v1.test.gs052.c2.boundary.easy.1349`

Rule: For primary prevention, prescribe atorvastatin. If the current heart rate is above 90/min or the current serum potassium is above 5.0 mmol/L, prescribe ezetimibe instead.

**base** (program answer: s; facts: patient: heart rate = 83; present; current | patient: serum potassium = 4.1; present; current)
```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 4.1 mmol/L.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: heart rate = 83; present; current | patient: serum potassium = 5.2; present; current)
```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 5.2 mmol/L.
Plays the piano.
```

**near** (program answer: s; facts: patient: heart rate = 83; present; current | patient: serum potassium = 5.0; present; current)
```
Male patient of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Sees a dentist yearly.
Heart rate now 83/min on a pulse check.
Paints watercolors as a hobby.
Current serum potassium 5.0 mmol/L.
Plays the piano.
```

**pres** (program answer: s; facts: patient: serum potassium = 4.1; present; current | patient: heart rate = 83; present; current)
```
Man of 55 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Latest potassium result: 4.1 mmol/L.
Sees a dentist yearly.
Plays the piano.
Current heart rate 83/min.
Paints watercolors as a hobby.
```


## author3 / group 159: `rule_v1.test.gs194.c1.boundary.long.360`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: heart rate = 68; present; current | patient: weight = 97; present; current)
```
Female patient of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current heart rate 68/min.
Drives a car.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Enjoys board games.
Sees a dentist yearly.
In 2016, lipase was 30 U/L.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
Owns a bicycle.
Current weight 97 kg.
Zinc of 85 mcg/dL in 2022.
Uses sunscreen in summer.
Her uncle lives with psoriasis.
Her roommate has recovered from a dislocated finger.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
```

**flip** (program answer: s'; facts: patient: heart rate = 101; present; current | patient: weight = 97; present; current)
```
Female patient of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current heart rate 101/min.
Drives a car.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Enjoys board games.
Sees a dentist yearly.
In 2016, lipase was 30 U/L.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
Owns a bicycle.
Current weight 97 kg.
Zinc of 85 mcg/dL in 2022.
Uses sunscreen in summer.
Her uncle lives with psoriasis.
Her roommate has recovered from a dislocated finger.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
```

**near** (program answer: s; facts: patient: heart rate = 90; present; current | patient: weight = 97; present; current)
```
Female patient of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current heart rate 90/min.
Drives a car.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Enjoys board games.
Sees a dentist yearly.
In 2016, lipase was 30 U/L.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
Owns a bicycle.
Current weight 97 kg.
Zinc of 85 mcg/dL in 2022.
Uses sunscreen in summer.
Her uncle lives with psoriasis.
Her roommate has recovered from a dislocated finger.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
```

**pres** (program answer: s; facts: patient: weight = 97; present; current | patient: heart rate = 68; present; current)
```
Woman of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drives a car.
Prefers to be addressed by first name.
Her uncle lives with psoriasis.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2022.
Knits as a hobby.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2013.
Uses sunscreen in summer.
Sleeps seven hours a night.
Latest weight 97 kg.
Enjoys board games.
Sees a dentist yearly.
Pupils equal and reactive to light.
Owns a bicycle.
In 2016, lipase was 30 U/L.
Paints watercolors as a hobby.
Heart rate now 68/min on a pulse check.
Her roommate has recovered from a dislocated finger.
```

**missing** (program answer: neither; facts: patient: weight = 97; present; current)
```
Female patient of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drives a car.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Enjoys board games.
Sees a dentist yearly.
In 2016, lipase was 30 U/L.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
Owns a bicycle.
Current weight 97 kg.
Zinc of 85 mcg/dL in 2022.
Uses sunscreen in summer.
Her uncle lives with psoriasis.
Her roommate has recovered from a dislocated finger.
Paints watercolors as a hobby.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2013.
```


## author4 / group 160: `rule_v1.test.s3_aims65.inr.boundary.long.51`

Rule: AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.

**base** (program answer: s; facts: patient: age = 60; present; current | patient: systolic blood pressure = 123; present; current | patient: international normalized ratio = 0.9; present; current)
```
An adult man.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Uses sunscreen in summer.
Has two cats.
His friend burned a hand on a stove years ago.
Currently aged 60 years.
Enjoys board games.
His father wears contact lenses.
Sees a dentist yearly.
Photographs local wildlife.
During a checkup in 2009, total protein was 7.0 g/dL.
Drives a car.
His roommate sprained a thumb last month.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2005.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Current systolic blood pressure 123 mmHg.
Plays the piano.
His uncle has a lazy eye.
Zinc of 85 mcg/dL in 2021.
Current international normalized ratio 0.9.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: age = 60; present; current | patient: systolic blood pressure = 123; present; current | patient: international normalized ratio = 2.1; present; current)
```
An adult man.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Uses sunscreen in summer.
Has two cats.
His friend burned a hand on a stove years ago.
Currently aged 60 years.
Enjoys board games.
His father wears contact lenses.
Sees a dentist yearly.
Photographs local wildlife.
During a checkup in 2009, total protein was 7.0 g/dL.
Drives a car.
His roommate sprained a thumb last month.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2005.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Current systolic blood pressure 123 mmHg.
Plays the piano.
His uncle has a lazy eye.
Zinc of 85 mcg/dL in 2021.
Current international normalized ratio 2.1.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: age = 60; present; current | patient: systolic blood pressure = 123; present; current | patient: international normalized ratio = 1.5; present; current)
```
An adult man.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Prefers morning appointments.
Uses sunscreen in summer.
Has two cats.
His friend burned a hand on a stove years ago.
Currently aged 60 years.
Enjoys board games.
His father wears contact lenses.
Sees a dentist yearly.
Photographs local wildlife.
During a checkup in 2009, total protein was 7.0 g/dL.
Drives a car.
His roommate sprained a thumb last month.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2005.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Current systolic blood pressure 123 mmHg.
Plays the piano.
His uncle has a lazy eye.
Zinc of 85 mcg/dL in 2021.
Current international normalized ratio 1.5.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: age = 60; present; current | patient: international normalized ratio = 0.9; present; current | patient: systolic blood pressure = 123; present; current)
```
Man, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Free T4 of 1.2 ng/dL in 2005.
Current age 60 years.
Prefers morning appointments.
Drives a car.
His father wears contact lenses.
Photographs local wildlife.
His friend burned a hand on a stove years ago.
Teeth in good repair.
His uncle has a lazy eye.
Uses sunscreen in summer.
Knits as a hobby.
Plays the piano.
Has two cats.
Latest international normalized ratio (INR): 0.9.
Paints watercolors as a hobby.
During a checkup in 2009, total protein was 7.0 g/dL.
Sees a dentist yearly.
Pupils equal and reactive to light.
His roommate sprained a thumb last month.
Observations now: blood pressure 123/83 mmHg.
Enjoys board games.
Zinc of 85 mcg/dL in 2021.
```


## author1 / group 161: `rule_v1.test.gs079.c2.negation.long.738`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the current blood urea nitrogen is above 19 mg/dL; the patient has had a major bleeding event at any time; the patient currently has heart failure.

**base** (program answer: s; facts: patient: blood urea nitrogen = 27; present; current | patient: current heart failure; absent; current)
```
Male patient of 57 years.
Suspected chest infection; assessed on the medical ward.
In 2015, lipase was 30 U/L.
Enjoys board games.
Pupils equal and reactive to light.
Sees a dentist yearly.
Prefers morning appointments.
Blood urea nitrogen 27 mg/dL on the current labs.
Uses sunscreen in summer.
Sleeps seven hours a night.
Teeth in good repair.
Drives a car.
Heart sounds without a gallop.
His father lives with psoriasis.
His father wears contact lenses.
Owns a bicycle.
Photographs local wildlife.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2015.
During a checkup in 2006, total protein was 7.0 g/dL.
His roommate burned a hand on a stove years ago.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: blood urea nitrogen = 27; present; current | patient: current heart failure; absent; current | patient: bleeding history; present; past (2022))
```
Male patient of 57 years.
Suspected chest infection; assessed on the medical ward.
In 2015, lipase was 30 U/L.
Enjoys board games.
Pupils equal and reactive to light.
Sees a dentist yearly.
Prefers morning appointments.
Blood urea nitrogen 27 mg/dL on the current labs.
Uses sunscreen in summer.
Sleeps seven hours a night.
Teeth in good repair.
Drives a car.
Heart sounds without a gallop.
His father lives with psoriasis.
His father wears contact lenses.
Owns a bicycle.
Photographs local wildlife.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Recovered from a major lower gastrointestinal bleed in 2022 that required transfusion.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2015.
During a checkup in 2006, total protein was 7.0 g/dL.
His roommate burned a hand on a stove years ago.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: blood urea nitrogen = 27; present; current | patient: current heart failure; absent; current | patient: bleeding history; absent; current)
```
Male patient of 57 years.
Suspected chest infection; assessed on the medical ward.
In 2015, lipase was 30 U/L.
Enjoys board games.
Pupils equal and reactive to light.
Sees a dentist yearly.
Prefers morning appointments.
Blood urea nitrogen 27 mg/dL on the current labs.
Uses sunscreen in summer.
Sleeps seven hours a night.
Teeth in good repair.
Drives a car.
Heart sounds without a gallop.
His father lives with psoriasis.
His father wears contact lenses.
Owns a bicycle.
Photographs local wildlife.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Medical records negative for major bleeding at any time.
Prefers to be addressed by first name.
Zinc of 85 mcg/dL in 2015.
During a checkup in 2006, total protein was 7.0 g/dL.
His roommate burned a hand on a stove years ago.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: current heart failure; absent; current | patient: blood urea nitrogen = 27; present; current)
```
Man of 57 years.
Suspected chest infection; assessed on the medical ward.
During a checkup in 2005, free T3 was 3.2 pg/mL.
His father wears contact lenses.
Drives a car.
In 2015, lipase was 30 U/L.
Zinc of 85 mcg/dL in 2015.
Prefers morning appointments.
Pupils equal and reactive to light.
Heart sounds without a gallop.
Teeth in good repair.
Paints watercolors as a hobby.
Blood urea nitrogen now: 27 mg/dL.
Owns a bicycle.
His roommate burned a hand on a stove years ago.
Sees a dentist yearly.
Uses sunscreen in summer.
Photographs local wildlife.
His father lives with psoriasis.
During a checkup in 2006, total protein was 7.0 g/dL.
Enjoys board games.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```


## author2 / group 162: `rule_v1.test.gs118.c3.time.easy.1228`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: eGFR = 52; present; past (2018) | patient: white cell count = 13.5; present; current | patient: angioedema; absent; current | patient: heart rate = 70; present; current | patient: eGFR = 80; present; current)
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

**flip** (program answer: s'; facts: patient: eGFR = 52; present; past (2018) | patient: white cell count = 13.5; present; current | patient: angioedema; absent; current | patient: heart rate = 70; present; current | patient: eGFR = 37; present; current)
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

**near** (program answer: s; facts: patient: eGFR = 39; present; past (2018) | patient: white cell count = 13.5; present; current | patient: angioedema; absent; current | patient: heart rate = 70; present; current | patient: eGFR = 80; present; current)
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

**pres** (program answer: s; facts: patient: angioedema; absent; current | patient: white cell count = 13.5; present; current | patient: eGFR = 52; present; past (2018) | patient: heart rate = 70; present; current | patient: eGFR = 80; present; current)
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


## author3 / group 163: `rule_v1.test.gs136.c2.negation.easy.165`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 50 mL/min/1.73 m2 or the patient currently has tonsillar exudate, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: eGFR = 58; present; current)
```
Woman of 31 years.
Requests contraception.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: eGFR = 58; present; current | patient: tonsillar exudate; present; current)
```
Woman of 31 years.
Requests contraception.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Tonsillar exudate visible on both sides.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: eGFR = 58; present; current | patient: tonsillar exudate; absent; current)
```
Woman of 31 years.
Requests contraception.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Tonsils free of exudate.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: eGFR = 58; present; current)
```
Female patient of 31 years.
Requests contraception.
Has two cats.
Paints watercolors as a hobby.
Current eGFR 58 mL/min/1.73 m2.
```


## author4 / group 164: `rule_v1.test.gs087.c3.time.superseded.109`

Rule: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the patient is allergic to penicillin; 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe acetaminophen instead.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: heart rate = 72; present; past | patient: heart rate = 81; present; current | patient: penicillin allergy; present; current)
```
Woman of 64 years.
Knee osteoarthritis with pain on walking.
Prefers morning appointments.
Has an acute pulmonary embolism, diagnosed this week.
Earlier this week, heart rate was 72/min; a newer reading supersedes it.
Current heart rate 81/min.
Known penicillin allergy with angioedema.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: heart rate = 72; present; past | patient: heart rate = 99; present; current | patient: penicillin allergy; present; current)
```
Woman of 64 years.
Knee osteoarthritis with pain on walking.
Prefers morning appointments.
Has an acute pulmonary embolism, diagnosed this week.
Earlier this week, heart rate was 72/min; a newer reading supersedes it.
Current heart rate 99/min.
Known penicillin allergy with angioedema.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; current | patient: heart rate = 101; present; past | patient: heart rate = 81; present; current | patient: penicillin allergy; present; current)
```
Woman of 64 years.
Knee osteoarthritis with pain on walking.
Prefers morning appointments.
Has an acute pulmonary embolism, diagnosed this week.
Earlier this week, heart rate was 101/min; a newer reading supersedes it.
Current heart rate 81/min.
Known penicillin allergy with angioedema.
```

**pres** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 72; present; past | patient: venous thromboembolism (patient or first-degree relative); present; current | patient: heart rate = 81; present; current)
```
Female patient of 64 years.
Knee osteoarthritis with pain on walking.
Known penicillin allergy with angioedema.
Earlier this week, heart rate was 72/min; a newer reading supersedes it.
Prefers morning appointments.
Has an acute pulmonary embolism, diagnosed this week.
Heart rate now 81/min on a pulse check.
```


## author1 / group 165: `rule_v1.test.s2_geneva.cancer.subject.long.763`

Rule: Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: age = 46; present; current | patient: hemoptysis; absent; current)
```
Woman, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2017.
Owns a bicycle.
Her wife has a lazy eye.
Prefers morning appointments.
Teeth in good repair.
Her sister wears contact lenses.
In 2013, folate was 12 ng/mL.
Weight steady over the past year.
Current age 46 years.
Photographs local wildlife.
Sleeps seven hours a night.
Her uncle burned a hand on a stove years ago.
In 2023, lipase was 30 U/L.
Plays the piano.
Her uncle lives with psoriasis.
Drives a car.
Sees a dentist yearly.
Dry cough, with nothing brought up.
Has two cats.
```

**flip** (program answer: s'; facts: patient: active cancer; present; current | patient: age = 46; present; current | patient: hemoptysis; absent; current)
```
Woman, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2017.
Owns a bicycle.
Her wife has a lazy eye.
Prefers morning appointments.
Teeth in good repair.
Her sister wears contact lenses.
In 2013, folate was 12 ng/mL.
Has melanoma skin cancer and is receiving treatment for it.
Current age 46 years.
Photographs local wildlife.
Sleeps seven hours a night.
Her uncle burned a hand on a stove years ago.
In 2023, lipase was 30 U/L.
Plays the piano.
Her uncle lives with psoriasis.
Drives a car.
Sees a dentist yearly.
Dry cough, with nothing brought up.
Has two cats.
```

**near** (program answer: s; facts: sister: active cancer; present; current | patient: age = 46; present; current | patient: hemoptysis; absent; current)
```
Woman, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2017.
Owns a bicycle.
Her wife has a lazy eye.
Prefers morning appointments.
Teeth in good repair.
Her sister wears contact lenses.
In 2013, folate was 12 ng/mL.
Her sister is being treated for leukemia.
Current age 46 years.
Photographs local wildlife.
Sleeps seven hours a night.
Her uncle burned a hand on a stove years ago.
In 2023, lipase was 30 U/L.
Plays the piano.
Her uncle lives with psoriasis.
Drives a car.
Sees a dentist yearly.
Dry cough, with nothing brought up.
Has two cats.
```

**pres** (program answer: s; facts: patient: hemoptysis; absent; current | patient: active cancer; absent; current | patient: age = 46; present; current)
```
An adult woman.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Her uncle lives with psoriasis.
In 2023, lipase was 30 U/L.
Pupils equal and reactive to light.
Her uncle burned a hand on a stove years ago.
Dry cough, with nothing brought up.
Her wife has a lazy eye.
Sees a dentist yearly.
Photographs local wildlife.
Drives a car.
Teeth in good repair.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2017.
Prefers to be addressed by first name.
Weight steady over the past year.
Owns a bicycle.
Has two cats.
Lives in a second-floor apartment.
Her sister wears contact lenses.
In 2013, folate was 12 ng/mL.
Plays the piano.
Currently aged 46 years.
Sleeps seven hours a night.
```


## author2 / group 166: `rule_v1.test.gs219.c2.numeric.long.287`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

**base** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: tonsillar exudate; present; current | patient: serum potassium = 4.2; present; current)
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

**flip** (program answer: s'; facts: patient: coronary artery disease; absent; current | patient: tonsillar exudate; present; current | patient: serum potassium = 5.3; present; current)
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

**near** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: tonsillar exudate; present; current | patient: serum potassium = 4.8; present; current)
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

**pres** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: serum potassium = 4.2; present; current | patient: tonsillar exudate; present; current)
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

**missing** (program answer: neither; facts: patient: coronary artery disease; absent; current | patient: tonsillar exudate; present; current)
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


## author3 / group 167: `rule_v1.test.gs213.c1.negation.easy.679`

Rule: For contraception, prescribe a combined oral contraceptive. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time or the patient has ever had asthma (current or past), prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: asthma at any time; absent; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 36 years.
Requests contraception.
Lungs clear, without wheeze or prolonged expiration.
Has two cats.
Prefers morning appointments.
Random glucose 92 mg/dL.
```

**flip** (program answer: s'; facts: patient: asthma at any time; absent; current | patient: diabetes (patient or first-degree relative); present; current)
```
Woman of 36 years.
Requests contraception.
Lungs clear, without wheeze or prolonged expiration.
Has two cats.
Prefers morning appointments.
Has type 2 diabetes on metformin.
```

**near** (program answer: s; facts: patient: asthma at any time; absent; current | patient: diabetes (patient or first-degree relative); absent; current)
```
Woman of 36 years.
Requests contraception.
Lungs clear, without wheeze or prolonged expiration.
Has two cats.
Prefers morning appointments.
Has never had diabetes.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); absent; current | patient: asthma at any time; absent; current)
```
Female patient of 36 years.
Requests contraception.
Has two cats.
Random glucose 92 mg/dL.
Prefers morning appointments.
Lungs clear, without wheeze or prolonged expiration.
```


## author4 / group 168: `rule_v1.test.gs086.c1.boundary.long.934`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: heart failure; present; past | patient: heart rate = 75; present; current | patient: venous thromboembolism; absent; current)
```
Female patient of 82 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2013.
Her friend lives with psoriasis.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Enjoys board games.
Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected.
In 2016, folate was 12 ng/mL.
Has two cats.
Plays the piano.
Drives a car.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Owns a bicycle.
Her roommate sprained a thumb last month.
During a checkup in 2006, total protein was 7.0 g/dL.
Current heart rate 75/min.
Her friend has a lazy eye.
Sleeps seven hours a night.
Varicose veins: none seen.
```

**flip** (program answer: s'; facts: patient: heart failure; present; past | patient: heart rate = 99; present; current | patient: venous thromboembolism; absent; current)
```
Female patient of 82 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2013.
Her friend lives with psoriasis.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Enjoys board games.
Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected.
In 2016, folate was 12 ng/mL.
Has two cats.
Plays the piano.
Drives a car.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Owns a bicycle.
Her roommate sprained a thumb last month.
During a checkup in 2006, total protein was 7.0 g/dL.
Current heart rate 99/min.
Her friend has a lazy eye.
Sleeps seven hours a night.
Varicose veins: none seen.
```

**near** (program answer: s; facts: patient: heart failure; present; past | patient: heart rate = 90; present; current | patient: venous thromboembolism; absent; current)
```
Female patient of 82 years.
Admitted for community-acquired pneumonia; immobile.
Prefers morning appointments.
Free T4 of 1.2 ng/dL in 2013.
Her friend lives with psoriasis.
Sees a dentist yearly.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Enjoys board games.
Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected.
In 2016, folate was 12 ng/mL.
Has two cats.
Plays the piano.
Drives a car.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Owns a bicycle.
Her roommate sprained a thumb last month.
During a checkup in 2006, total protein was 7.0 g/dL.
Current heart rate 90/min.
Her friend has a lazy eye.
Sleeps seven hours a night.
Varicose veins: none seen.
```

**pres** (program answer: s; facts: patient: heart failure; present; past | patient: venous thromboembolism; absent; current | patient: heart rate = 75; present; current)
```
Woman of 82 years.
Admitted for community-acquired pneumonia; immobile.
Free T4 of 1.2 ng/dL in 2013.
Sees a dentist yearly.
Has two cats.
Owns a bicycle.
Her roommate sprained a thumb last month.
Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected.
In 2016, folate was 12 ng/mL.
Sleeps seven hours a night.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Drives a car.
Varicose veins: none seen.
Enjoys board games.
Heart rate now 75/min on a pulse check.
Prefers morning appointments.
Her friend has a lazy eye.
During a checkup in 2006, total protein was 7.0 g/dL.
Plays the piano.
Teeth in good repair.
Her friend lives with psoriasis.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```


## author1 / group 169: `rule_v1.test.s2_atria_bleed.egfr.time.alt.160`

Rule: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 45 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.

**base** (program answer: s; facts: patient: eGFR = 66; present; past (2024) | patient: age = 68; present; current | patient: hypertension; absent; current | patient: eGFR = 74; present; current | patient: hemoglobin = 14.2; present; current)
```
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Teeth in good repair.
Drives a car.
Photographs local wildlife.
Records from 2024 list eGFR at 66 mL/min/1.73 m2.
Current age 68 years.
Echocardiogram shows normal left ventricular wall thickness.
eGFR now 74 mL/min/1.73 m2.
Latest Hgb result: 14.2 g/dL.
```

**flip** (program answer: s'; facts: patient: eGFR = 66; present; past (2024) | patient: age = 68; present; current | patient: hypertension; absent; current | patient: eGFR = 34; present; current | patient: hemoglobin = 14.2; present; current)
```
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Teeth in good repair.
Drives a car.
Photographs local wildlife.
Records from 2024 list eGFR at 66 mL/min/1.73 m2.
Current age 68 years.
Echocardiogram shows normal left ventricular wall thickness.
eGFR now 34 mL/min/1.73 m2.
Latest Hgb result: 14.2 g/dL.
```

**near** (program answer: s; facts: patient: eGFR = 27; present; past (2024) | patient: age = 68; present; current | patient: hypertension; absent; current | patient: eGFR = 74; present; current | patient: hemoglobin = 14.2; present; current)
```
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Teeth in good repair.
Drives a car.
Photographs local wildlife.
Records from 2024 list eGFR at 27 mL/min/1.73 m2.
Current age 68 years.
Echocardiogram shows normal left ventricular wall thickness.
eGFR now 74 mL/min/1.73 m2.
Latest Hgb result: 14.2 g/dL.
```

**pres** (program answer: s; facts: patient: hypertension; absent; current | patient: eGFR = 74; present; current | patient: age = 68; present; current | patient: eGFR = 66; present; past (2024) | patient: hemoglobin = 14.2; present; current)
```
An adult man.
Atrial fibrillation; a decision on warfarin is pending.
Teeth in good repair.
Echocardiogram shows normal left ventricular wall thickness.
Current eGFR 74 mL/min/1.73 m2.
Currently aged 68 years.
Back in 2024, eGFR stood at 66 mL/min/1.73 m2.
Drives a car.
Current Hgb 14.2 g/dL.
Photographs local wildlife.
```


## author2 / group 170: `rule_v1.test.gs124.c1.negation.easy.278`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**base** (program answer: s; facts: patient: calf swelling = 4.1; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: age = 46; present; current)
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Rectal exam unremarkable.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```

**flip** (program answer: s'; facts: patient: calf swelling = 4.1; present; current | patient: colorectal cancer (patient or first-degree relative); present; current | patient: age = 46; present; current)
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Colorectal cancer under active treatment.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```

**near** (program answer: s; facts: patient: calf swelling = 4.1; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: age = 46; present; current)
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Has never had bowel cancer.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```

**pres** (program answer: s; facts: patient: calf swelling = 4.1; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current | patient: age = 46; present; current)
```
Woman, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Current calf swelling 4.1 cm compared with the other leg.
Rectal exam unremarkable.
Has two cats.
Owns a bicycle.
Current age 46 years.
```

**missing** (program answer: neither; facts: patient: calf swelling = 4.1; present; current | patient: colorectal cancer (patient or first-degree relative); unknown; current | patient: age = 46; present; current)
```
An adult woman.
Community-acquired pneumonia confirmed on chest radiograph.
Difference in calf circumference now 4.1 cm.
Colorectal cancer (patient or first-degree relative): unknown.
Has two cats.
Currently aged 46 years.
Owns a bicycle.
```


## author3 / group 171: `rule_v1.test.gs025.c1.subject.easy.238`

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**base** (program answer: s; facts: patient: temperature = 38.3; present; current)
```
Woman of 42 years.
Sore throat for two days.
Plays the piano.
Drives a car.
Knits as a hobby.
Temperature now 38.3 C (tympanic).
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; present; past (2016) | patient: temperature = 38.3; present; current)
```
Woman of 42 years.
Sore throat for two days.
Plays the piano.
Recovered from a heart attack in 2016.
Drives a car.
Knits as a hobby.
Temperature now 38.3 C (tympanic).
Enjoys board games.
```

**near** (program answer: s; facts: sister: myocardial infarction or peripheral artery disease; present; past | patient: temperature = 38.3; present; current)
```
Woman of 42 years.
Sore throat for two days.
Plays the piano.
Her sister had a heart attack years ago.
Drives a car.
Knits as a hobby.
Temperature now 38.3 C (tympanic).
Enjoys board games.
```

**pres** (program answer: s; facts: patient: temperature = 38.3; present; current)
```
Female patient of 42 years.
Sore throat for two days.
Plays the piano.
Current temperature 38.3 C.
Drives a car.
Knits as a hobby.
Enjoys board games.
```

**missing** (program answer: neither; facts: patient: myocardial infarction or peripheral artery disease; unknown; current | patient: temperature = 38.3; present; current)
```
Woman of 42 years.
Sore throat for two days.
Plays the piano.
Myocardial infarction or peripheral artery disease: status unclear from the records at hand.
Drives a car.
Knits as a hobby.
Temperature now 38.3 C (tympanic).
Enjoys board games.
```


## author4 / group 172: `rule_v1.test.gs024.c3.numeric.long.795`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 3 points if the current ALT is above 120 U/L; 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 3 points if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 4 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: ALT = 136; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: systolic blood pressure = 112; present; current)
```
Female patient of 49 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Owns a bicycle.
ALT now 136 U/L.
HbA1c 5.3% at a routine check.
Her wife has recovered from a dislocated finger.
Uses sunscreen in summer.
Prefers morning appointments.
Her father lives with psoriasis.
During a checkup in 2012, total protein was 7.0 g/dL.
Her sister sprained a thumb last month.
Has two cats.
Zinc of 85 mcg/dL in 2021.
Drives a car.
Plays the piano.
Observations now: blood pressure 112/77 mmHg.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
```

**flip** (program answer: s'; facts: patient: ALT = 136; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: systolic blood pressure = 182; present; current)
```
Female patient of 49 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Owns a bicycle.
ALT now 136 U/L.
HbA1c 5.3% at a routine check.
Her wife has recovered from a dislocated finger.
Uses sunscreen in summer.
Prefers morning appointments.
Her father lives with psoriasis.
During a checkup in 2012, total protein was 7.0 g/dL.
Her sister sprained a thumb last month.
Has two cats.
Zinc of 85 mcg/dL in 2021.
Drives a car.
Plays the piano.
Observations now: blood pressure 182/115 mmHg.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
```

**near** (program answer: s; facts: patient: ALT = 136; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: systolic blood pressure = 156; present; current)
```
Female patient of 49 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Owns a bicycle.
ALT now 136 U/L.
HbA1c 5.3% at a routine check.
Her wife has recovered from a dislocated finger.
Uses sunscreen in summer.
Prefers morning appointments.
Her father lives with psoriasis.
During a checkup in 2012, total protein was 7.0 g/dL.
Her sister sprained a thumb last month.
Has two cats.
Zinc of 85 mcg/dL in 2021.
Drives a car.
Plays the piano.
Observations now: blood pressure 156/101 mmHg.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
```

**pres** (program answer: s; facts: patient: ALT = 136; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: systolic blood pressure = 112; present; current)
```
Woman of 49 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Has two cats.
Her sister sprained a thumb last month.
Plays the piano.
Photographs local wildlife.
Current ALT 136 U/L.
Owns a bicycle.
Pupils equal and reactive to light.
HbA1c 5.3% at a routine check.
Zinc of 85 mcg/dL in 2021.
Uses sunscreen in summer.
Lives in a second-floor apartment.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Her father lives with psoriasis.
Current systolic blood pressure 112 mmHg.
Drives a car.
During a checkup in 2012, total protein was 7.0 g/dL.
Her wife burned a hand on a stove years ago.
Her wife has recovered from a dislocated finger.
Prefers morning appointments.
```


## author1 / group 173: `rule_v1.test.gs225.c2.boundary.long.422`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has an active peptic ulcer and the current white cell count is above 12.0 x10^9/L, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: white cell count = 8.0; present; current | patient: active peptic ulcer; present; current)
```
Man of 49 years.
Hip osteoarthritis with pain on walking.
Latest WBC is 8.0 x10^9/L.
His sister lives with psoriasis.
Owns a bicycle.
Drives a car.
His friend sprained a thumb last month.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Teeth in good repair.
Has an active duodenal ulcer.
Knits as a hobby.
Enjoys board games.
Prefers to be addressed by first name.
In 2017, lipase was 30 U/L.
Sees a dentist yearly.
Prefers morning appointments.
Uses sunscreen in summer.
His roommate has recovered from a dislocated finger.
Pupils equal and reactive to light.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2009.
```

**flip** (program answer: s'; facts: patient: white cell count = 12.7; present; current | patient: active peptic ulcer; present; current)
```
Man of 49 years.
Hip osteoarthritis with pain on walking.
Latest WBC is 12.7 x10^9/L.
His sister lives with psoriasis.
Owns a bicycle.
Drives a car.
His friend sprained a thumb last month.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Teeth in good repair.
Has an active duodenal ulcer.
Knits as a hobby.
Enjoys board games.
Prefers to be addressed by first name.
In 2017, lipase was 30 U/L.
Sees a dentist yearly.
Prefers morning appointments.
Uses sunscreen in summer.
His roommate has recovered from a dislocated finger.
Pupils equal and reactive to light.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2009.
```

**near** (program answer: s; facts: patient: white cell count = 12.0; present; current | patient: active peptic ulcer; present; current)
```
Man of 49 years.
Hip osteoarthritis with pain on walking.
Latest WBC is 12.0 x10^9/L.
His sister lives with psoriasis.
Owns a bicycle.
Drives a car.
His friend sprained a thumb last month.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Teeth in good repair.
Has an active duodenal ulcer.
Knits as a hobby.
Enjoys board games.
Prefers to be addressed by first name.
In 2017, lipase was 30 U/L.
Sees a dentist yearly.
Prefers morning appointments.
Uses sunscreen in summer.
His roommate has recovered from a dislocated finger.
Pupils equal and reactive to light.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2009.
```

**pres** (program answer: s; facts: patient: white cell count = 8.0; present; current | patient: active peptic ulcer; present; current)
```
Male patient of 49 years.
Hip osteoarthritis with pain on walking.
Current white cell count 8.0 x10^9/L.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Knits as a hobby.
Sees a dentist yearly.
In 2017, lipase was 30 U/L.
Free T4 of 1.2 ng/dL in 2009.
Enjoys board games.
Owns a bicycle.
His friend sprained a thumb last month.
His sister lives with psoriasis.
Photographs local wildlife.
Pupils equal and reactive to light.
Teeth in good repair.
His roommate has recovered from a dislocated finger.
Has an active duodenal ulcer.
Drives a car.
Prefers to be addressed by first name.
Prefers morning appointments.
```


## author2 / group 174: `rule_v1.test.gs056.c4.boundary.easy.725`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 2 points if the patient has ever had a venous thromboembolism (current or past); 3 points if the patient has ever had coronary artery disease (current or past); 1 point if the current white cell count is above 12.0 x10^9/L. If the score is 4 or more, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: white cell count = 6.9; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: coronary artery disease; present; past (2006))
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

**flip** (program answer: s'; facts: patient: venous thromboembolism; absent; current | patient: white cell count = 13.1; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: coronary artery disease; present; past (2006))
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

**near** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: white cell count = 12.0; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: coronary artery disease; present; past (2006))
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

**pres** (program answer: s; facts: patient: coronary artery disease; present; past (2006) | patient: white cell count = 6.9; present; current | patient: diabetes (patient or first-degree relative); absent; current | patient: venous thromboembolism; absent; current)
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

**missing** (program answer: neither; facts: patient: venous thromboembolism; absent; current | patient: diabetes (patient or first-degree relative); absent; current | patient: coronary artery disease; present; past (2006))
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


## author3 / group 175: `rule_v1.test.gs155.c2.boundary.easy.375`

Rule: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had a peptic ulcer (current or past); the current serum potassium is above 5.0 mmol/L; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.

**base** (program answer: s; facts: patient: peptic ulcer at any time; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: serum potassium = 3.9; present; current)
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest potassium result: 3.9 mmol/L.
```

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: serum potassium = 5.2; present; current)
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest potassium result: 5.2 mmol/L.
```

**near** (program answer: s; facts: patient: peptic ulcer at any time; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: serum potassium = 5.0; present; current)
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest potassium result: 5.0 mmol/L.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; present; current | patient: serum potassium = 3.9; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current)
```
Male patient of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Lives in a second-floor apartment.
Current serum potassium 3.9 mmol/L.
Varicose veins: none seen.
```

**missing** (program answer: neither; facts: patient: peptic ulcer at any time; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current)
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
```


## author4 / group 176: `rule_v1.test.wells_dvt.cancer.negation.long.944`

Rule: Wells DVT score (as used here, partial): 1 point each for active cancer; a venous thromboembolism of the patient, current or previous; current calf swelling of 3.0 cm or more compared with the other leg. Other Wells items are not part of this question.

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: calf swelling = 0.8; present; current | patient: active cancer; absent; current)
```
Woman of 41 years.
Left leg pain for two days after a long-haul flight.
Her roommate has a lazy eye.
Plays the piano.
Prefers morning appointments.
Prefers to be addressed by first name.
Drives a car.
Sees a dentist yearly.
Her sister sprained a thumb last month.
Owns a bicycle.
Her father has recovered from a dislocated finger.
Uses sunscreen in summer.
Knits as a hobby.
Paints watercolors as a hobby.
In 2017, folate was 12 ng/mL.
Lives in a second-floor apartment.
Enjoys board games.
Coagulation tests normal on recent bloodwork.
Has two cats.
Sleeps seven hours a night.
Her father burned a hand on a stove years ago.
Difference in calf circumference now 0.8 cm.
Zinc of 85 mcg/dL in 2024.
Pupils equal and reactive to light.
Oncology follow-up: none.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; absent; current | patient: calf swelling = 0.8; present; current | patient: active cancer; present; current)
```
Woman of 41 years.
Left leg pain for two days after a long-haul flight.
Her roommate has a lazy eye.
Plays the piano.
Prefers morning appointments.
Prefers to be addressed by first name.
Drives a car.
Sees a dentist yearly.
Her sister sprained a thumb last month.
Owns a bicycle.
Her father has recovered from a dislocated finger.
Uses sunscreen in summer.
Knits as a hobby.
Paints watercolors as a hobby.
In 2017, folate was 12 ng/mL.
Lives in a second-floor apartment.
Enjoys board games.
Coagulation tests normal on recent bloodwork.
Has two cats.
Sleeps seven hours a night.
Her father burned a hand on a stove years ago.
Difference in calf circumference now 0.8 cm.
Zinc of 85 mcg/dL in 2024.
Pupils equal and reactive to light.
Has metastatic lung cancer, receiving palliative treatment.
```

**near** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: calf swelling = 0.8; present; current | patient: active cancer; absent; current)
```
Woman of 41 years.
Left leg pain for two days after a long-haul flight.
Her roommate has a lazy eye.
Plays the piano.
Prefers morning appointments.
Prefers to be addressed by first name.
Drives a car.
Sees a dentist yearly.
Her sister sprained a thumb last month.
Owns a bicycle.
Her father has recovered from a dislocated finger.
Uses sunscreen in summer.
Knits as a hobby.
Paints watercolors as a hobby.
In 2017, folate was 12 ng/mL.
Lives in a second-floor apartment.
Enjoys board games.
Coagulation tests normal on recent bloodwork.
Has two cats.
Sleeps seven hours a night.
Her father burned a hand on a stove years ago.
Difference in calf circumference now 0.8 cm.
Zinc of 85 mcg/dL in 2024.
Pupils equal and reactive to light.
Free of cancer throughout life.
```

**pres** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: calf swelling = 0.8; present; current | patient: active cancer; absent; current)
```
Female patient of 41 years.
Left leg pain for two days after a long-haul flight.
Pupils equal and reactive to light.
Her father has recovered from a dislocated finger.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Plays the piano.
Coagulation tests normal on recent bloodwork.
Uses sunscreen in summer.
In 2017, folate was 12 ng/mL.
Her father burned a hand on a stove years ago.
Her roommate has a lazy eye.
Prefers to be addressed by first name.
Has two cats.
Enjoys board games.
Her sister sprained a thumb last month.
Drives a car.
Current calf swelling 0.8 cm compared with the other leg.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2024.
Sleeps seven hours a night.
Oncology follow-up: none.
Sees a dentist yearly.
Knits as a hobby.
```


## author1 / group 177: `rule_v1.test.gs155.c2.time.superseded.783`

Rule: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had a peptic ulcer (current or past); the current serum potassium is above 5.0 mmol/L; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.

**base** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; past (2010) | patient: serum potassium = 4.4; present; past | patient: serum potassium = 4.3; present; current)
```
Woman of 75 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Drives a car.
Recovered from a pulmonary embolism in 2010.
Last month, serum potassium was 4.4 mmol/L; the newest measurement replaces it.
Latest potassium result: 4.3 mmol/L.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism (patient or first-degree relative); present; past (2010) | patient: serum potassium = 4.4; present; past | patient: serum potassium = 5.8; present; current)
```
Woman of 75 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Drives a car.
Recovered from a pulmonary embolism in 2010.
Last month, serum potassium was 4.4 mmol/L; the newest measurement replaces it.
Latest potassium result: 5.8 mmol/L.
```

**near** (program answer: s; facts: patient: venous thromboembolism (patient or first-degree relative); present; past (2010) | patient: serum potassium = 5.6; present; past | patient: serum potassium = 4.3; present; current)
```
Woman of 75 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Drives a car.
Recovered from a pulmonary embolism in 2010.
Last month, serum potassium was 5.6 mmol/L; the newest measurement replaces it.
Latest potassium result: 4.3 mmol/L.
```

**pres** (program answer: s; facts: patient: serum potassium = 4.3; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2010) | patient: serum potassium = 4.4; present; past)
```
Female patient of 75 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Current serum potassium 4.3 mmol/L.
Recovered from a pulmonary embolism in 2010.
Last month, serum potassium was 4.4 mmol/L; the newest measurement replaces it.
Drives a car.
```


## author2 / group 178: `rule_v1.test.gs163.c2.time.easy.548`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. Score 2 points if the current blood urea nitrogen is above 19 mg/dL; 1 point if the current calf swelling compared with the other leg is 3.0 cm or more; 3 points if the current serum creatinine is above 2.0 mg/dL. If the score is 4 or more, prescribe intravenous piperacillin-tazobactam instead.

**base** (program answer: s; facts: patient: serum creatinine = 2.5; present; current | patient: calf swelling = 1.3; present; past (2009) | patient: calf swelling = 0.5; present; current | patient: blood urea nitrogen = 15; present; current)
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

**flip** (program answer: s'; facts: patient: serum creatinine = 2.5; present; current | patient: calf swelling = 1.3; present; past (2009) | patient: calf swelling = 4.7; present; current | patient: blood urea nitrogen = 15; present; current)
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

**near** (program answer: s; facts: patient: serum creatinine = 2.5; present; current | patient: calf swelling = 5.0; present; past (2009) | patient: calf swelling = 0.5; present; current | patient: blood urea nitrogen = 15; present; current)
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

**pres** (program answer: s; facts: patient: serum creatinine = 2.5; present; current | patient: calf swelling = 1.3; present; past (2009) | patient: calf swelling = 0.5; present; current | patient: blood urea nitrogen = 15; present; current)
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


## author3 / group 179: `rule_v1.test.centor.temp.boundary.easy.1303`

Rule: Centor score (as used here, partial): 1 point each for temperature above 38.0 C; tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: temperature = 37.2; present; current | patient: tender cervical lymph nodes; absent; current)
```
Male patient of 37 years.
Sore throat for three days.
Tonsils pink and clean on inspection.
Temperature now 37.2 C (tympanic).
Neck palpation unremarkable.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; absent; current | patient: temperature = 39.0; present; current | patient: tender cervical lymph nodes; absent; current)
```
Male patient of 37 years.
Sore throat for three days.
Tonsils pink and clean on inspection.
Temperature now 39.0 C (tympanic).
Neck palpation unremarkable.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: temperature = 38.0; present; current | patient: tender cervical lymph nodes; absent; current)
```
Male patient of 37 years.
Sore throat for three days.
Tonsils pink and clean on inspection.
Temperature now 38.0 C (tympanic).
Neck palpation unremarkable.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: temperature = 37.2; present; current | patient: tonsillar exudate; absent; current | patient: tender cervical lymph nodes; absent; current)
```
Man of 37 years.
Sore throat for three days.
Current temperature 37.2 C.
Lives in a second-floor apartment.
Tonsils pink and clean on inspection.
Prefers morning appointments.
Prefers to be addressed by first name.
Neck palpation unremarkable.
```


## author4 / group 180: `rule_v1.test.inv026.c2.time.easy.432`

Rule: For Corvane syndrome, prescribe zephalin. If the patient is allergic to penicillin or the patient is currently taking clarithromycin, prescribe trivosan instead.

**base** (program answer: s; facts: patient: penicillin allergy; absent; current | patient: clarithromycin; absent; current)
```
Man of 58 years.
Referred with Corvane syndrome.
Drug allergies: none known.
Has no antibiotic course under way.
Prefers morning appointments.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: penicillin allergy; absent; current | patient: clarithromycin; present; current)
```
Man of 58 years.
Referred with Corvane syndrome.
Drug allergies: none known.
Currently taking clarithromycin for an ear infection.
Prefers morning appointments.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: penicillin allergy; absent; current | patient: clarithromycin; present; past (2009))
```
Man of 58 years.
Referred with Corvane syndrome.
Drug allergies: none known.
Formerly took clarithromycin for a chest infection in 2009.
Prefers morning appointments.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: clarithromycin; absent; current | patient: penicillin allergy; absent; current)
```
Male patient of 58 years.
Referred with Corvane syndrome.
Lives in a second-floor apartment.
Has no antibiotic course under way.
Prefers morning appointments.
Drug allergies: none known.
Pupils equal and reactive to light.
```


## author1 / group 181: `rule_v1.test.gs088.c1.subject.long.707`

Rule: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: white cell count = 4.9; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 23 years.
Sore throat for two days.
Prefers to be addressed by first name.
Enjoys board games.
Tonsils pink and clean on inspection.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Has two cats.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2023.
Latest WBC is 4.9 x10^9/L.
Plays the piano.
His wife has a lazy eye.
Prefers morning appointments.
Lives with peripheral artery disease affecting the left leg.
In 2024, folate was 12 ng/mL.
Drives a car.
Owns a bicycle.
Sleeps seven hours a night.
His wife has recovered from a dislocated finger.
Photographs local wildlife.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; present; current | patient: white cell count = 4.9; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 23 years.
Sore throat for two days.
Prefers to be addressed by first name.
Enjoys board games.
Tonsils swollen and coated with yellow exudate.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Has two cats.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2023.
Latest WBC is 4.9 x10^9/L.
Plays the piano.
His wife has a lazy eye.
Prefers morning appointments.
Lives with peripheral artery disease affecting the left leg.
In 2024, folate was 12 ng/mL.
Drives a car.
Owns a bicycle.
Sleeps seven hours a night.
His wife has recovered from a dislocated finger.
Photographs local wildlife.
```

**near** (program answer: s; facts: wife: tonsillar exudate; present; current | patient: white cell count = 4.9; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 23 years.
Sore throat for two days.
Prefers to be addressed by first name.
Enjoys board games.
His wife currently has a throat infection with tonsillar exudate.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Has two cats.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2023.
Latest WBC is 4.9 x10^9/L.
Plays the piano.
His wife has a lazy eye.
Prefers morning appointments.
Lives with peripheral artery disease affecting the left leg.
In 2024, folate was 12 ng/mL.
Drives a car.
Owns a bicycle.
Sleeps seven hours a night.
His wife has recovered from a dislocated finger.
Photographs local wildlife.
```

**pres** (program answer: s; facts: patient: white cell count = 4.9; present; current | patient: myocardial infarction or peripheral artery disease; present; current | patient: tonsillar exudate; absent; current)
```
Man of 23 years.
Sore throat for two days.
Current white cell count 4.9 x10^9/L.
Enjoys board games.
His wife has a lazy eye.
Knits as a hobby.
Paints watercolors as a hobby.
In 2024, folate was 12 ng/mL.
Prefers to be addressed by first name.
Has two cats.
Prefers morning appointments.
Owns a bicycle.
Drives a car.
Lives in a second-floor apartment.
Free T4 of 1.2 ng/dL in 2023.
Teeth in good repair.
Lives with peripheral artery disease affecting the left leg.
His wife has recovered from a dislocated finger.
Plays the piano.
Tonsils pink and clean on inspection.
Photographs local wildlife.
Sleeps seven hours a night.
```

**missing** (program answer: neither; facts: patient: tonsillar exudate; unknown; current | patient: white cell count = 4.9; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Male patient of 23 years.
Sore throat for two days.
Prefers to be addressed by first name.
Enjoys board games.
Tonsillar exudate: unknown.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Has two cats.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2023.
Latest WBC is 4.9 x10^9/L.
Plays the piano.
His wife has a lazy eye.
Prefers morning appointments.
Lives with peripheral artery disease affecting the left leg.
In 2024, folate was 12 ng/mL.
Drives a car.
Owns a bicycle.
Sleeps seven hours a night.
His wife has recovered from a dislocated finger.
Photographs local wildlife.
```


## author2 / group 182: `rule_v1.test.centor.temp.boundary.easy.540`

Rule: Centor score (as used here, partial): 1 point each for temperature above 38.0 C; tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.

**base** (program answer: s; facts: patient: tender cervical lymph nodes; absent; current | patient: temperature = 37.0; present; current)
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

**flip** (program answer: s'; facts: patient: tender cervical lymph nodes; absent; current | patient: temperature = 38.4; present; current)
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

**near** (program answer: s; facts: patient: tender cervical lymph nodes; absent; current | patient: temperature = 38.0; present; current)
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

**pres** (program answer: s; facts: patient: temperature = 37.0; present; current | patient: tender cervical lymph nodes; absent; current)
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

**missing** (program answer: neither; facts: patient: tender cervical lymph nodes; absent; current)
```
Woman of 47 years.
Sore throat for three days.
Front of the neck without tenderness or swelling.
Teeth in good repair.
Photographs local wildlife.
Paints watercolors as a hobby.
Knits as a hobby.
```


## author3 / group 183: `rule_v1.test.gs010.c3.time.superseded.302`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

**base** (program answer: s; facts: patient: white cell count = 9.5; present; past | patient: colorectal cancer (patient or first-degree relative); present; current | patient: coronary artery disease; present; past | patient: white cell count = 8.8; present; current)
```
Man of 62 years.
Atrial fibrillation; anticoagulation indicated.
Last month, white cell count was 9.5 x10^9/L; the newest measurement replaces it.
Photographs local wildlife.
Lives with colon cancer and attends an oncology clinic.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Current white cell count 8.8 x10^9/L.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: white cell count = 9.5; present; past | patient: colorectal cancer (patient or first-degree relative); present; current | patient: coronary artery disease; present; past | patient: white cell count = 14.0; present; current)
```
Man of 62 years.
Atrial fibrillation; anticoagulation indicated.
Last month, white cell count was 9.5 x10^9/L; the newest measurement replaces it.
Photographs local wildlife.
Lives with colon cancer and attends an oncology clinic.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Current white cell count 14.0 x10^9/L.
Plays the piano.
```

**near** (program answer: s; facts: patient: white cell count = 14.0; present; past | patient: colorectal cancer (patient or first-degree relative); present; current | patient: coronary artery disease; present; past | patient: white cell count = 8.8; present; current)
```
Man of 62 years.
Atrial fibrillation; anticoagulation indicated.
Last month, white cell count was 14.0 x10^9/L; the newest measurement replaces it.
Photographs local wildlife.
Lives with colon cancer and attends an oncology clinic.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Current white cell count 8.8 x10^9/L.
Plays the piano.
```

**pres** (program answer: s; facts: patient: white cell count = 9.5; present; past | patient: white cell count = 8.8; present; current | patient: coronary artery disease; present; past | patient: colorectal cancer (patient or first-degree relative); present; current)
```
Male patient of 62 years.
Atrial fibrillation; anticoagulation indicated.
Last month, white cell count was 9.5 x10^9/L; the newest measurement replaces it.
Photographs local wildlife.
Plays the piano.
Latest WBC is 8.8 x10^9/L.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Lives with colon cancer and attends an oncology clinic.
```


## author4 / group 184: `rule_v1.test.s1_spesi.sbp.boundary.long.146`

Rule: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: systolic blood pressure = 152; present; current | patient: heart rate = 79; present; current | patient: oxygen saturation = 94; present; current | patient: age = 53; present; current | patient: active cancer; absent; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
During a checkup in 2015, total protein was 7.0 g/dL.
Sees a dentist yearly.
Observations now: blood pressure 152/99 mmHg.
His wife burned a hand on a stove years ago.
Prefers morning appointments.
Current heart rate 79/min.
Lives in a second-floor apartment.
Enjoys board games.
His sister wears contact lenses.
His wife has a lazy eye.
Uses sunscreen in summer.
Current oxygen saturation 94%.
Free T4 of 1.2 ng/dL in 2023.
Plays the piano.
In 2011, lipase was 30 U/L.
Owns a bicycle.
Current age 53 years.
Paints watercolors as a hobby.
Knits as a hobby.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Teeth in good repair.
Weight steady over the past year.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 94; present; current | patient: heart rate = 79; present; current | patient: oxygen saturation = 94; present; current | patient: age = 53; present; current | patient: active cancer; absent; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
During a checkup in 2015, total protein was 7.0 g/dL.
Sees a dentist yearly.
Observations now: blood pressure 94/67 mmHg.
His wife burned a hand on a stove years ago.
Prefers morning appointments.
Current heart rate 79/min.
Lives in a second-floor apartment.
Enjoys board games.
His sister wears contact lenses.
His wife has a lazy eye.
Uses sunscreen in summer.
Current oxygen saturation 94%.
Free T4 of 1.2 ng/dL in 2023.
Plays the piano.
In 2011, lipase was 30 U/L.
Owns a bicycle.
Current age 53 years.
Paints watercolors as a hobby.
Knits as a hobby.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Teeth in good repair.
Weight steady over the past year.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 100; present; current | patient: heart rate = 79; present; current | patient: oxygen saturation = 94; present; current | patient: age = 53; present; current | patient: active cancer; absent; current)
```
Man, adult.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
During a checkup in 2015, total protein was 7.0 g/dL.
Sees a dentist yearly.
Observations now: blood pressure 100/70 mmHg.
His wife burned a hand on a stove years ago.
Prefers morning appointments.
Current heart rate 79/min.
Lives in a second-floor apartment.
Enjoys board games.
His sister wears contact lenses.
His wife has a lazy eye.
Uses sunscreen in summer.
Current oxygen saturation 94%.
Free T4 of 1.2 ng/dL in 2023.
Plays the piano.
In 2011, lipase was 30 U/L.
Owns a bicycle.
Current age 53 years.
Paints watercolors as a hobby.
Knits as a hobby.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Teeth in good repair.
Weight steady over the past year.
```

**pres** (program answer: s; facts: patient: heart rate = 79; present; current | patient: oxygen saturation = 94; present; current | patient: systolic blood pressure = 152; present; current | patient: age = 53; present; current | patient: active cancer; absent; current)
```
An adult man.
Acute pulmonary embolism confirmed on CT pulmonary angiography.
Heart rate now 79/min on a pulse check.
Paints watercolors as a hobby.
Prefers morning appointments.
Latest oxygen saturation reading: 94%.
In 2011, lipase was 30 U/L.
Enjoys board games.
His wife has a lazy eye.
His wife burned a hand on a stove years ago.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Current systolic blood pressure 152 mmHg.
Knits as a hobby.
During a checkup in 2015, total protein was 7.0 g/dL.
His sister wears contact lenses.
Sees a dentist yearly.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Currently aged 53 years.
Owns a bicycle.
Plays the piano.
Weight steady over the past year.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2023.
```


## author1 / group 185: `rule_v1.test.gs147.c4.negation.easy.100`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 1 point if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 1 point if the patient has had cancer at any time (active or in remission); 2 points if the patient has ever had heart failure (current or past). If the score is 3 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; current | patient: cancer at any time; absent; current | patient: systolic blood pressure = 118; present; current | patient: heart failure; absent; current)
```
Woman of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Insulin-treated diabetes.
Weight steady over the past year.
Plays the piano.
Observations now: blood pressure 118/80 mmHg.
Sleeps flat on one pillow.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: diabetes (patient or first-degree relative); present; current | patient: cancer at any time; absent; current | patient: systolic blood pressure = 118; present; current | patient: heart failure; present; past (2007))
```
Woman of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Insulin-treated diabetes.
Weight steady over the past year.
Plays the piano.
Observations now: blood pressure 118/80 mmHg.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2007 and off all heart medicines since.
Enjoys board games.
```

**near** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; current | patient: cancer at any time; absent; current | patient: systolic blood pressure = 118; present; current | patient: heart failure; absent; current)
```
Woman of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Insulin-treated diabetes.
Weight steady over the past year.
Plays the piano.
Observations now: blood pressure 118/80 mmHg.
Heart failure: never diagnosed.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 118; present; current | patient: diabetes (patient or first-degree relative); present; current | patient: cancer at any time; absent; current | patient: heart failure; absent; current)
```
Female patient of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Plays the piano.
Current systolic blood pressure 118 mmHg.
Insulin-treated diabetes.
Weight steady over the past year.
Sleeps flat on one pillow.
Enjoys board games.
```

**missing** (program answer: neither; facts: patient: diabetes (patient or first-degree relative); present; current | patient: cancer at any time; absent; current | patient: systolic blood pressure = 118; present; current | patient: heart failure; unknown; current)
```
Woman of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Insulin-treated diabetes.
Weight steady over the past year.
Plays the piano.
Observations now: blood pressure 118/80 mmHg.
Heart failure: unknown.
Enjoys board games.
```


## author2 / group 186: `rule_v1.test.any_gout.egfr.boundary.easy.872`

Rule: For an acute gout flare, prescribe naproxen. If the patient has an active peptic ulcer or the current eGFR is below 30 mL/min/1.73 m2, prescribe colchicine instead.

**base** (program answer: s; facts: patient: eGFR = 80; present; current)
```
Man of 30 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Teeth in good repair.
Current eGFR 80 mL/min/1.73 m2.
Owns a bicycle.
```

**flip** (program answer: s'; facts: patient: eGFR = 13; present; current)
```
Man of 30 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Teeth in good repair.
Current eGFR 13 mL/min/1.73 m2.
Owns a bicycle.
```

**near** (program answer: s; facts: patient: eGFR = 30; present; current)
```
Man of 30 years.
Acute gout flare of the left knee.
Sees a dentist yearly.
Teeth in good repair.
Current eGFR 30 mL/min/1.73 m2.
Owns a bicycle.
```

**pres** (program answer: s; facts: patient: eGFR = 80; present; current)
```
Male patient of 30 years.
Acute gout flare of the left knee.
eGFR now 80 mL/min/1.73 m2.
Owns a bicycle.
Sees a dentist yearly.
Teeth in good repair.
```


## author3 / group 187: `rule_v1.test.inv052.c3.time.easy.864`

Rule: For Tessaly disease, prescribe velimor. Score 2 points if the patient has had cancer at any time (active or in remission); 2 points if the patient has ever had diabetes (current or past); 2 points if the patient currently has a major bleed; 3 points if the patient has ever had angioedema (current or past). If the score is 6 or more, prescribe quantrel instead.

**base** (program answer: s; facts: patient: diabetes; absent; current | patient: angioedema; present; current | patient: cancer at any time; present; current)
```
Male patient of 41 years.
Referred with Tessaly disease.
Drives a car.
Random glucose 92 mg/dL.
Sees a dentist yearly.
Recurrent angioedema, under allergy follow-up.
Uses sunscreen in summer.
Has metastatic lung cancer, receiving palliative treatment.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: diabetes; absent; current | patient: active major bleeding; present; current | patient: angioedema; present; current | patient: cancer at any time; present; current)
```
Male patient of 41 years.
Referred with Tessaly disease.
Drives a car.
Random glucose 92 mg/dL.
Currently has a major bleed from a duodenal ulcer, with transfusion under way.
Sees a dentist yearly.
Recurrent angioedema, under allergy follow-up.
Uses sunscreen in summer.
Has metastatic lung cancer, receiving palliative treatment.
Plays the piano.
```

**near** (program answer: s; facts: patient: diabetes; absent; current | patient: active major bleeding; present; past (2006) | patient: angioedema; present; current | patient: cancer at any time; present; current)
```
Male patient of 41 years.
Referred with Tessaly disease.
Drives a car.
Random glucose 92 mg/dL.
Recovered from a major lower gastrointestinal bleed in 2006 that required transfusion.
Sees a dentist yearly.
Recurrent angioedema, under allergy follow-up.
Uses sunscreen in summer.
Has metastatic lung cancer, receiving palliative treatment.
Plays the piano.
```

**pres** (program answer: s; facts: patient: cancer at any time; present; current | patient: diabetes; absent; current | patient: angioedema; present; current)
```
Man of 41 years.
Referred with Tessaly disease.
Drives a car.
Has metastatic lung cancer, receiving palliative treatment.
Sees a dentist yearly.
Random glucose 92 mg/dL.
Recurrent angioedema, under allergy follow-up.
Uses sunscreen in summer.
Plays the piano.
```


## author4 / group 188: `rule_v1.test.rcri.cr.numeric.alt.72`

Rule: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.

**base** (program answer: s; facts: patient: creatinine = 0.8; present; current | patient: stroke/TIA; absent; current)
```
Man of 50 years.
Preoperative assessment before elective colectomy.
Teeth in good repair.
Latest creatinine result: 0.8 mg/dL.
Prefers to be addressed by first name.
Gait normal; no focal weakness.
Drives a car.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: creatinine = 1.9; present; current | patient: stroke/TIA; absent; current)
```
Man of 50 years.
Preoperative assessment before elective colectomy.
Teeth in good repair.
Latest creatinine result: 1.9 mg/dL.
Prefers to be addressed by first name.
Gait normal; no focal weakness.
Drives a car.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: creatinine = 1.4; present; current | patient: stroke/TIA; absent; current)
```
Man of 50 years.
Preoperative assessment before elective colectomy.
Teeth in good repair.
Latest creatinine result: 1.4 mg/dL.
Prefers to be addressed by first name.
Gait normal; no focal weakness.
Drives a car.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: creatinine = 0.8; present; current | patient: stroke/TIA; absent; current)
```
Male patient of 50 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 0.8 mg/dL.
Drives a car.
Teeth in good repair.
Gait normal; no focal weakness.
Knits as a hobby.
Prefers to be addressed by first name.
```


## author1 / group 189: `rule_v1.test.ckd_nsaid.egfr.boundary.alt.740`

Rule: For knee osteoarthritis pain, prescribe naproxen. If the patient's current eGFR is below 75 mL/min/1.73 m2, prescribe acetaminophen instead.

**base** (program answer: s; facts: patient: eGFR = 83; present; current)
```
Man of 54 years.
Knee osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Enjoys board games.
eGFR now 83 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: eGFR = 72; present; current)
```
Man of 54 years.
Knee osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Enjoys board games.
eGFR now 72 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: eGFR = 75; present; current)
```
Man of 54 years.
Knee osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Enjoys board games.
eGFR now 75 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: eGFR = 83; present; current)
```
Male patient of 54 years.
Knee osteoarthritis with pain on walking.
Current eGFR 83 mL/min/1.73 m2.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Enjoys board games.
Pupils equal and reactive to light.
```


## author2 / group 190: `rule_v1.test.gs209.c2.subject.easy.1090`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**base** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: age = 74; present; current | patient: heart rate = 76; present; current)
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

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; past | patient: age = 74; present; current | patient: heart rate = 76; present; current)
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

**near** (program answer: s; facts: friend: peptic ulcer at any time; present; past | patient: age = 74; present; current | patient: heart rate = 76; present; current)
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

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: age = 74; present; current | patient: heart rate = 76; present; current)
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


## author3 / group 191: `rule_v1.test.s3_rockall.hf.subject.easy.1295`

Rule: Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

**base** (program answer: s; facts: patient: heart failure; absent; current | patient: systolic blood pressure = 129; present; current | patient: age = 47; present; current)
```
Man, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Sleeps flat on one pillow.
Prefers morning appointments.
Sleeps seven hours a night.
Current systolic blood pressure 129 mmHg.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Currently aged 47 years.
```

**flip** (program answer: s'; facts: patient: heart failure; present; current | patient: systolic blood pressure = 129; present; current | patient: age = 47; present; current)
```
Man, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Current heart failure with ankle swelling.
Prefers morning appointments.
Sleeps seven hours a night.
Current systolic blood pressure 129 mmHg.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Currently aged 47 years.
```

**near** (program answer: s; facts: sister: heart failure; present; current | patient: systolic blood pressure = 129; present; current | patient: age = 47; present; current)
```
Man, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
His sister is treated for heart failure.
Prefers morning appointments.
Sleeps seven hours a night.
Current systolic blood pressure 129 mmHg.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Currently aged 47 years.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 129; present; current | patient: heart failure; absent; current | patient: age = 47; present; current)
```
An adult man.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Sleeps seven hours a night.
Observations now: blood pressure 129/86 mmHg.
Pupils equal and reactive to light.
Prefers morning appointments.
Sleeps flat on one pillow.
Paints watercolors as a hobby.
Current age 47 years.
```


## author4 / group 192: `rule_v1.test.inv014.c2.numeric.long.744`

Rule: For Pallis disease, prescribe brexadol. If the current oxygen saturation is 91% or less and the age of the patient is 75 years or more, prescribe corlitane instead.

**base** (program answer: s; facts: patient: age = 65; present; current | patient: oxygen saturation = 88; present; current)
```
An adult man.
Referred with Pallis disease.
His roommate has recovered from a dislocated finger.
Prefers morning appointments.
Lives in a second-floor apartment.
Enjoys board games.
Paints watercolors as a hobby.
Uses sunscreen in summer.
In 2020, lipase was 30 U/L.
Currently aged 65 years.
Photographs local wildlife.
His sister has a lazy eye.
Owns a bicycle.
Prefers to be addressed by first name.
Latest oxygen saturation reading: 88%.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2010.
During a checkup in 2017, free T3 was 3.2 pg/mL.
During a checkup in 2006, total protein was 7.0 g/dL.
Plays the piano.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: age = 80; present; current | patient: oxygen saturation = 88; present; current)
```
An adult man.
Referred with Pallis disease.
His roommate has recovered from a dislocated finger.
Prefers morning appointments.
Lives in a second-floor apartment.
Enjoys board games.
Paints watercolors as a hobby.
Uses sunscreen in summer.
In 2020, lipase was 30 U/L.
Currently aged 80 years.
Photographs local wildlife.
His sister has a lazy eye.
Owns a bicycle.
Prefers to be addressed by first name.
Latest oxygen saturation reading: 88%.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2010.
During a checkup in 2017, free T3 was 3.2 pg/mL.
During a checkup in 2006, total protein was 7.0 g/dL.
Plays the piano.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: age = 72; present; current | patient: oxygen saturation = 88; present; current)
```
An adult man.
Referred with Pallis disease.
His roommate has recovered from a dislocated finger.
Prefers morning appointments.
Lives in a second-floor apartment.
Enjoys board games.
Paints watercolors as a hobby.
Uses sunscreen in summer.
In 2020, lipase was 30 U/L.
Currently aged 72 years.
Photographs local wildlife.
His sister has a lazy eye.
Owns a bicycle.
Prefers to be addressed by first name.
Latest oxygen saturation reading: 88%.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2010.
During a checkup in 2017, free T3 was 3.2 pg/mL.
During a checkup in 2006, total protein was 7.0 g/dL.
Plays the piano.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: oxygen saturation = 88; present; current | patient: age = 65; present; current)
```
Man, adult.
Referred with Pallis disease.
During a checkup in 2017, free T3 was 3.2 pg/mL.
In 2020, lipase was 30 U/L.
Enjoys board games.
Lives in a second-floor apartment.
His roommate has recovered from a dislocated finger.
Owns a bicycle.
Plays the piano.
Prefers morning appointments.
His sister has a lazy eye.
Sleeps seven hours a night.
Current oxygen saturation 88%.
During a checkup in 2006, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2010.
Prefers to be addressed by first name.
Current age 65 years.
Paints watercolors as a hobby.
Photographs local wildlife.
Uses sunscreen in summer.
Sees a dentist yearly.
```


## author1 / group 193: `rule_v1.test.s2_wells_pe.hr.numeric.long.833`

Rule: Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.

**base** (program answer: s; facts: patient: hemoptysis; absent; current | patient: active cancer; absent; current | patient: heart rate = 83; present; current)
```
Man of 74 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Drives a car.
Lives in a second-floor apartment.
Owns a bicycle.
His wife has recovered from a dislocated finger.
In 2006, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2008.
Teeth in good repair.
Sputum colorless on inspection.
His sister has a lazy eye.
Sleeps seven hours a night.
Sees a dentist yearly.
Plays the piano.
Oncology follow-up: none.
Current heart rate 83/min.
Prefers morning appointments.
Uses sunscreen in summer.
In 2018, lipase was 30 U/L.
Enjoys board games.
Photographs local wildlife.
```

**flip** (program answer: s'; facts: patient: hemoptysis; absent; current | patient: active cancer; absent; current | patient: heart rate = 108; present; current)
```
Man of 74 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Drives a car.
Lives in a second-floor apartment.
Owns a bicycle.
His wife has recovered from a dislocated finger.
In 2006, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2008.
Teeth in good repair.
Sputum colorless on inspection.
His sister has a lazy eye.
Sleeps seven hours a night.
Sees a dentist yearly.
Plays the piano.
Oncology follow-up: none.
Current heart rate 108/min.
Prefers morning appointments.
Uses sunscreen in summer.
In 2018, lipase was 30 U/L.
Enjoys board games.
Photographs local wildlife.
```

**near** (program answer: s; facts: patient: hemoptysis; absent; current | patient: active cancer; absent; current | patient: heart rate = 97; present; current)
```
Man of 74 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Drives a car.
Lives in a second-floor apartment.
Owns a bicycle.
His wife has recovered from a dislocated finger.
In 2006, folate was 12 ng/mL.
Zinc of 85 mcg/dL in 2008.
Teeth in good repair.
Sputum colorless on inspection.
His sister has a lazy eye.
Sleeps seven hours a night.
Sees a dentist yearly.
Plays the piano.
Oncology follow-up: none.
Current heart rate 97/min.
Prefers morning appointments.
Uses sunscreen in summer.
In 2018, lipase was 30 U/L.
Enjoys board games.
Photographs local wildlife.
```

**pres** (program answer: s; facts: patient: heart rate = 83; present; current | patient: hemoptysis; absent; current | patient: active cancer; absent; current)
```
Male patient of 74 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
His sister has a lazy eye.
Photographs local wildlife.
Teeth in good repair.
Heart rate now 83/min on a pulse check.
Sputum colorless on inspection.
Drives a car.
Prefers morning appointments.
In 2018, lipase was 30 U/L.
His wife has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2008.
Owns a bicycle.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Enjoys board games.
Plays the piano.
In 2006, folate was 12 ng/mL.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Sees a dentist yearly.
Oncology follow-up: none.
Uses sunscreen in summer.
```


## author2 / group 194: `rule_v1.test.gs061.c2.time.delabelled.533`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a peptic ulcer (current or past) or the patient is allergic to penicillin, prescribe fondaparinux instead.

**base** (program answer: s; facts: patient: penicillin allergy; absent; current)
```
Female patient of 74 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
Drug allergies: none known.
```

**flip** (program answer: s'; facts: patient: penicillin allergy; present; current)
```
Female patient of 74 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
Penicillin allergy: anaphylaxis.
```

**near** (program answer: s; facts: patient: penicillin allergy; present; past (2007))
```
Female patient of 74 years.
First day after elective total hip replacement.
Photographs local wildlife.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Plays the piano.
Formerly recorded as penicillin-allergic; de-labeled in 2007 by an allergy clinic.
```

**pres** (program answer: s; facts: patient: penicillin allergy; absent; current)
```
Woman of 74 years.
First day after elective total hip replacement.
Drug allergies: none known.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Plays the piano.
Photographs local wildlife.
```


## author3 / group 195: `rule_v1.test.hf_spironolactone.k.numeric.alt.633`

Rule: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 4.5 mmol/L, add dapagliflozin instead.

**base** (program answer: s; facts: patient: potassium = 4.2; present; current)
```
Man of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 4.2 mmol/L.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: potassium = 4.8; present; current)
```
Man of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 4.8 mmol/L.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: potassium = 4.3; present; current)
```
Man of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 4.3 mmol/L.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: potassium = 4.2; present; current)
```
Male patient of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Latest potassium result: 4.2 mmol/L.
```


## author4 / group 196: `rule_v1.test.gs139.c2.subject.easy.1231`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: tender cervical lymph nodes; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Tender, swollen lymph nodes in the front of the neck.
Drives a car.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: tender cervical lymph nodes; present; current | patient: angioedema; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Tender, swollen lymph nodes in the front of the neck.
Drives a car.
Prefers morning appointments.
Recurrent angioedema, under allergy follow-up.
```

**near** (program answer: s; facts: patient: tender cervical lymph nodes; present; current | sister: angioedema; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Tender, swollen lymph nodes in the front of the neck.
Drives a car.
Prefers morning appointments.
Her sister has active angioedema of the face.
```

**pres** (program answer: s; facts: patient: tender cervical lymph nodes; present; current)
```
Woman of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Photographs local wildlife.
Prefers morning appointments.
Drives a car.
Tender, swollen lymph nodes in the front of the neck.
```


## author1 / group 197: `rule_v1.test.inv042.c1.subject.easy.512`

Rule: For Zentha disease, prescribe valtimide. If the patient currently has asthma or the patient has had cancer at any time (active or in remission), prescribe isomarin instead.

**base** (program answer: s; facts: patient: asthma; absent; current | patient: cancer at any time; absent; current)
```
Woman of 63 years.
Referred with Zentha disease.
Sleeps seven hours a night.
Inhaler use: none.
Weight steady over the past year.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: asthma; present; current | patient: cancer at any time; absent; current)
```
Woman of 63 years.
Referred with Zentha disease.
Sleeps seven hours a night.
Persistent asthma, using a rescue inhaler most weeks.
Weight steady over the past year.
Prefers morning appointments.
```

**near** (program answer: s; facts: father: asthma; present; current | patient: cancer at any time; absent; current)
```
Woman of 63 years.
Referred with Zentha disease.
Sleeps seven hours a night.
Her father uses an inhaler for asthma.
Weight steady over the past year.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: asthma; absent; current | patient: cancer at any time; absent; current)
```
Female patient of 63 years.
Referred with Zentha disease.
Prefers morning appointments.
Sleeps seven hours a night.
Inhaler use: none.
Weight steady over the past year.
```


## author2 / group 198: `rule_v1.test.gs048.c1.time.easy.32`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: age = 63; present; current | patient: weight = 80; present; current | patient: weight = 69; present; past (2007))
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
Current weight 80 kg.
Records from 2007 list weight at 69 kg.
```

**flip** (program answer: s'; facts: patient: age = 63; present; current | patient: weight = 49; present; current | patient: weight = 69; present; past (2007))
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
Current weight 49 kg.
Records from 2007 list weight at 69 kg.
```

**near** (program answer: s; facts: patient: age = 63; present; current | patient: weight = 80; present; current | patient: weight = 51; present; past (2007))
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
Current weight 80 kg.
Records from 2007 list weight at 51 kg.
```

**pres** (program answer: s; facts: patient: weight = 69; present; past (2007) | patient: age = 63; present; current | patient: weight = 80; present; current)
```
An adult woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Sees a dentist yearly.
Back in 2007, weight stood at 69 kg.
Currently aged 63 years.
Latest weight 80 kg.
```

**missing** (program answer: neither; facts: patient: age = 63; present; current)
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current age 63 years.
Sees a dentist yearly.
```


## author3 / group 199: `rule_v1.test.gs124.c3.numeric.easy.1136`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**base** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 49; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Currently aged 49 years.
```

**flip** (program answer: s'; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 67; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Currently aged 67 years.
```

**near** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 63; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Currently aged 63 years.
```

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: calf swelling = 3.6; present; current | patient: age = 49; present; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Rectal exam unremarkable.
Current calf swelling 3.6 cm compared with the other leg.
Current age 49 years.
Owns a bicycle.
```


## author4 / group 200: `rule_v1.test.gs209.c2.negation.long.956`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**base** (program answer: s; facts: patient: age = 42; present; current | patient: heart rate = 98; present; current | patient: peptic ulcer at any time; absent; current)
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
In 2024, folate was 12 ng/mL.
Paints watercolors as a hobby.
Her sister wears contact lenses.
Her friend sprained a thumb last month.
Pupils equal and reactive to light.
Photographs local wildlife.
Plays the piano.
In 2009, lipase was 30 U/L.
Her friend has a lazy eye.
Drives a car.
Current age 42 years.
Heart rate now 98/min on a pulse check.
During a checkup in 2012, total protein was 7.0 g/dL.
Her wife burned a hand on a stove years ago.
Sleeps seven hours a night.
Appetite good; no indigestion.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2024.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: age = 42; present; current | patient: heart rate = 98; present; current | patient: peptic ulcer at any time; present; past (2009))
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
In 2024, folate was 12 ng/mL.
Paints watercolors as a hobby.
Her sister wears contact lenses.
Her friend sprained a thumb last month.
Pupils equal and reactive to light.
Photographs local wildlife.
Plays the piano.
In 2009, lipase was 30 U/L.
Her friend has a lazy eye.
Drives a car.
Current age 42 years.
Heart rate now 98/min on a pulse check.
During a checkup in 2012, total protein was 7.0 g/dL.
Her wife burned a hand on a stove years ago.
Sleeps seven hours a night.
Formerly treated for a peptic ulcer; endoscopy in 2009 showed it had gone.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2024.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: age = 42; present; current | patient: heart rate = 98; present; current | patient: peptic ulcer at any time; absent; current)
```
Woman, adult.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
In 2024, folate was 12 ng/mL.
Paints watercolors as a hobby.
Her sister wears contact lenses.
Her friend sprained a thumb last month.
Pupils equal and reactive to light.
Photographs local wildlife.
Plays the piano.
In 2009, lipase was 30 U/L.
Her friend has a lazy eye.
Drives a car.
Current age 42 years.
Heart rate now 98/min on a pulse check.
During a checkup in 2012, total protein was 7.0 g/dL.
Her wife burned a hand on a stove years ago.
Sleeps seven hours a night.
Medical record negative for peptic ulcer, current or past.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2024.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: age = 42; present; current | patient: peptic ulcer at any time; absent; current | patient: heart rate = 98; present; current)
```
An adult woman.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Currently aged 42 years.
During a checkup in 2012, total protein was 7.0 g/dL.
Sleeps seven hours a night.
Her wife burned a hand on a stove years ago.
Drives a car.
In 2024, folate was 12 ng/mL.
Appetite good; no indigestion.
Her friend has a lazy eye.
Her friend sprained a thumb last month.
Photographs local wildlife.
Plays the piano.
Current heart rate 98/min.
Her sister wears contact lenses.
Free T4 of 1.2 ng/dL in 2024.
In 2009, lipase was 30 U/L.
Enjoys board games.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Prefers morning appointments.
```


## author1 / group 201: `rule_v1.test.gs038.c2.numeric.long.948`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.

**base** (program answer: s; facts: patient: blood urea nitrogen = 15; present; current | patient: peptic ulcer at any time; present; current)
```
Woman of 75 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sleeps seven hours a night.
Owns a bicycle.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Enjoys board games.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2007.
Plays the piano.
Uses sunscreen in summer.
Her sister wears contact lenses.
Her sister has recovered from a dislocated finger.
In 2016, lipase was 30 U/L.
Teeth in good repair.
Prefers to be addressed by first name.
Has two cats.
Zinc of 85 mcg/dL in 2022.
Blood urea nitrogen now: 15 mg/dL.
Her wife sprained a thumb last month.
Prefers morning appointments.
Knits as a hobby.
Active peptic ulcer disease.
```

**flip** (program answer: s'; facts: patient: blood urea nitrogen = 28; present; current | patient: peptic ulcer at any time; present; current)
```
Woman of 75 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sleeps seven hours a night.
Owns a bicycle.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Enjoys board games.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2007.
Plays the piano.
Uses sunscreen in summer.
Her sister wears contact lenses.
Her sister has recovered from a dislocated finger.
In 2016, lipase was 30 U/L.
Teeth in good repair.
Prefers to be addressed by first name.
Has two cats.
Zinc of 85 mcg/dL in 2022.
Blood urea nitrogen now: 28 mg/dL.
Her wife sprained a thumb last month.
Prefers morning appointments.
Knits as a hobby.
Active peptic ulcer disease.
```

**near** (program answer: s; facts: patient: blood urea nitrogen = 16; present; current | patient: peptic ulcer at any time; present; current)
```
Woman of 75 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sleeps seven hours a night.
Owns a bicycle.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Enjoys board games.
Pupils equal and reactive to light.
Her wife burned a hand on a stove years ago.
Free T4 of 1.2 ng/dL in 2007.
Plays the piano.
Uses sunscreen in summer.
Her sister wears contact lenses.
Her sister has recovered from a dislocated finger.
In 2016, lipase was 30 U/L.
Teeth in good repair.
Prefers to be addressed by first name.
Has two cats.
Zinc of 85 mcg/dL in 2022.
Blood urea nitrogen now: 16 mg/dL.
Her wife sprained a thumb last month.
Prefers morning appointments.
Knits as a hobby.
Active peptic ulcer disease.
```

**pres** (program answer: s; facts: patient: blood urea nitrogen = 15; present; current | patient: peptic ulcer at any time; present; current)
```
Female patient of 75 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Enjoys board games.
Owns a bicycle.
Blood urea nitrogen 15 mg/dL on the current labs.
Her wife sprained a thumb last month.
In 2016, lipase was 30 U/L.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2007.
Knits as a hobby.
Her sister wears contact lenses.
Pupils equal and reactive to light.
Plays the piano.
Teeth in good repair.
During a checkup in 2017, free T3 was 3.2 pg/mL.
Sleeps seven hours a night.
Has two cats.
Active peptic ulcer disease.
Her wife burned a hand on a stove years ago.
Zinc of 85 mcg/dL in 2022.
Her sister has recovered from a dislocated finger.
Prefers morning appointments.
```


## author2 / group 202: `rule_v1.test.gs197.c2.time.long.207`

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current systolic blood pressure is 90 mmHg or less, prescribe fondaparinux instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 129; present; past (2023) | patient: systolic blood pressure = 124; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
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

**flip** (program answer: s'; facts: patient: systolic blood pressure = 129; present; past (2023) | patient: systolic blood pressure = 90; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
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

**near** (program answer: s; facts: patient: systolic blood pressure = 74; present; past (2023) | patient: systolic blood pressure = 124; present; current | patient: myocardial infarction or peripheral artery disease; present; current)
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

**pres** (program answer: s; facts: patient: systolic blood pressure = 129; present; past (2023) | patient: myocardial infarction or peripheral artery disease; present; current | patient: systolic blood pressure = 124; present; current)
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

**missing** (program answer: neither; facts: patient: myocardial infarction or peripheral artery disease; present; current)
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


## author3 / group 203: `rule_v1.test.gs136.c1.numeric.easy.429`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 50 mL/min/1.73 m2 or the patient currently has tonsillar exudate, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 62; present; current)
```
Woman of 31 years.
Requests contraception.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Tonsils pink and clean on inspection.
eGFR now 62 mL/min/1.73 m2.
Sees a dentist yearly.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 46; present; current)
```
Woman of 31 years.
Requests contraception.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Tonsils pink and clean on inspection.
eGFR now 46 mL/min/1.73 m2.
Sees a dentist yearly.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 51; present; current)
```
Woman of 31 years.
Requests contraception.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Tonsils pink and clean on inspection.
eGFR now 51 mL/min/1.73 m2.
Sees a dentist yearly.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 62; present; current)
```
Female patient of 31 years.
Requests contraception.
Tonsils pink and clean on inspection.
Sees a dentist yearly.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Current eGFR 62 mL/min/1.73 m2.
```


## author4 / group 204: `rule_v1.test.s3_hctci.alt.numeric.easy.412`

Rule: Hematopoietic Cell Transplantation-specific Comorbidity Index (as used here, partial): 1 point for coronary artery disease at any time (current or past); 1 point for a stroke or TIA at any time (current or past); 2 points for a current peptic ulcer; 1 point for a current ALT above 40 U/L. Other items of the index are not part of this question.

**base** (program answer: s; facts: patient: ALT = 21; present; current | patient: active peptic ulcer; absent; current | patient: stroke/TIA; absent; current)
```
Man of 54 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
ALT now 21 U/L.
Plays the piano.
Abdomen soft and non-tender.
Sleeps seven hours a night.
Power and sensation normal in all limbs.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: patient: ALT = 46; present; current | patient: active peptic ulcer; absent; current | patient: stroke/TIA; absent; current)
```
Man of 54 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
ALT now 46 U/L.
Plays the piano.
Abdomen soft and non-tender.
Sleeps seven hours a night.
Power and sensation normal in all limbs.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: patient: ALT = 39; present; current | patient: active peptic ulcer; absent; current | patient: stroke/TIA; absent; current)
```
Man of 54 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
ALT now 39 U/L.
Plays the piano.
Abdomen soft and non-tender.
Sleeps seven hours a night.
Power and sensation normal in all limbs.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: stroke/TIA; absent; current | patient: active peptic ulcer; absent; current | patient: ALT = 21; present; current)
```
Male patient of 54 years.
Assessment before allogeneic stem cell transplantation for acute myeloid leukemia in remission.
Power and sensation normal in all limbs.
Abdomen soft and non-tender.
Pupils equal and reactive to light.
Current ALT 21 U/L.
Plays the piano.
Sleeps seven hours a night.
```


## author1 / group 205: `rule_v1.test.inv003.c2.subject.long.182`

Rule: For Brask fever, prescribe gendrotil. If the patient has ever had diabetes (current or past) or the patient is currently taking warfarin, prescribe lumacept instead.

**base** (program answer: s; facts: )
```
Male patient of 68 years.
Referred with Brask fever.
Teeth in good repair.
Pupils equal and reactive to light.
In 2015, lipase was 30 U/L.
His wife has a lazy eye.
Has two cats.
Prefers to be addressed by first name.
His wife sprained a thumb last month.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2016.
His roommate wears contact lenses.
Sleeps seven hours a night.
Owns a bicycle.
Sees a dentist yearly.
Photographs local wildlife.
Knits as a hobby.
His sister burned a hand on a stove years ago.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: warfarin; present; current)
```
Male patient of 68 years.
Referred with Brask fever.
Teeth in good repair.
Pupils equal and reactive to light.
In 2015, lipase was 30 U/L.
His wife has a lazy eye.
Has two cats.
Prefers to be addressed by first name.
His wife sprained a thumb last month.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2016.
His roommate wears contact lenses.
Sleeps seven hours a night.
Owns a bicycle.
Sees a dentist yearly.
Currently on warfarin, prescribed by the cardiology clinic.
Photographs local wildlife.
Knits as a hobby.
His sister burned a hand on a stove years ago.
Enjoys board games.
```

**near** (program answer: s; facts: friend: warfarin; present; current)
```
Male patient of 68 years.
Referred with Brask fever.
Teeth in good repair.
Pupils equal and reactive to light.
In 2015, lipase was 30 U/L.
His wife has a lazy eye.
Has two cats.
Prefers to be addressed by first name.
His wife sprained a thumb last month.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2016.
His roommate wears contact lenses.
Sleeps seven hours a night.
Owns a bicycle.
Sees a dentist yearly.
His friend is on warfarin with monthly INR checks.
Photographs local wildlife.
Knits as a hobby.
His sister burned a hand on a stove years ago.
Enjoys board games.
```

**pres** (program answer: s; facts: )
```
Man of 68 years.
Referred with Brask fever.
His wife sprained a thumb last month.
Teeth in good repair.
Knits as a hobby.
Photographs local wildlife.
Sleeps seven hours a night.
His roommate wears contact lenses.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2016.
In 2015, lipase was 30 U/L.
Pupils equal and reactive to light.
Has two cats.
His wife has a lazy eye.
His sister burned a hand on a stove years ago.
Sees a dentist yearly.
Prefers to be addressed by first name.
Owns a bicycle.
Enjoys board games.
```


## author2 / group 206: `rule_v1.test.gs047.c1.boundary.long.34`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: serum potassium = 4.5; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
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

**flip** (program answer: s'; facts: patient: serum potassium = 5.8; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
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

**near** (program answer: s; facts: patient: serum potassium = 5.0; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
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

**pres** (program answer: s; facts: patient: serum potassium = 4.5; present; current | patient: venous thromboembolism (patient or first-degree relative); present; current)
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


## author3 / group 207: `rule_v1.test.rcri.cr.boundary.alt.490`

Rule: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.

**base** (program answer: s; facts: patient: creatinine = 1.3; present; current | patient: heart failure; absent; current | patient: coronary artery disease; absent; current)
```
Female patient of 62 years.
Preoperative assessment before elective colectomy.
Pupils equal and reactive to light.
Current serum creatinine 1.3 mg/dL.
Heart sounds without a gallop.
Chest pain on exertion: none reported.
```

**flip** (program answer: s'; facts: patient: creatinine = 1.9; present; current | patient: heart failure; absent; current | patient: coronary artery disease; absent; current)
```
Female patient of 62 years.
Preoperative assessment before elective colectomy.
Pupils equal and reactive to light.
Current serum creatinine 1.9 mg/dL.
Heart sounds without a gallop.
Chest pain on exertion: none reported.
```

**near** (program answer: s; facts: patient: creatinine = 1.5; present; current | patient: heart failure; absent; current | patient: coronary artery disease; absent; current)
```
Female patient of 62 years.
Preoperative assessment before elective colectomy.
Pupils equal and reactive to light.
Current serum creatinine 1.5 mg/dL.
Heart sounds without a gallop.
Chest pain on exertion: none reported.
```

**pres** (program answer: s; facts: patient: heart failure; absent; current | patient: creatinine = 1.3; present; current | patient: coronary artery disease; absent; current)
```
Woman of 62 years.
Preoperative assessment before elective colectomy.
Heart sounds without a gallop.
Latest creatinine result: 1.3 mg/dL.
Pupils equal and reactive to light.
Chest pain on exertion: none reported.
```


## author4 / group 208: `rule_v1.test.s3_jhfrat.age.numeric.long.1601`

Rule: Johns Hopkins Fall Risk Assessment Tool (as used here, partial): 1 point for age 60 years or more; 5 points for one fall in the six months before this admission; 1 point for new confusion (altered awareness of the surroundings). Other items are not part of this question.

**base** (program answer: s; facts: patient: age = 51; present; current | patient: recent fall; absent; current)
```
An adult man.
Admitted to the medical ward with a urinary infection.
Paints watercolors as a hobby.
Owns a bicycle.
Photographs local wildlife.
His wife lives with psoriasis.
Has two cats.
Sleeps seven hours a night.
His wife burned a hand on a stove years ago.
Uses sunscreen in summer.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2011.
Current age 51 years.
Sees a dentist yearly.
His friend has a lazy eye.
Walks independently, with no recent trips or slips.
Plays the piano.
In 2019, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: age = 69; present; current | patient: recent fall; absent; current)
```
An adult man.
Admitted to the medical ward with a urinary infection.
Paints watercolors as a hobby.
Owns a bicycle.
Photographs local wildlife.
His wife lives with psoriasis.
Has two cats.
Sleeps seven hours a night.
His wife burned a hand on a stove years ago.
Uses sunscreen in summer.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2011.
Current age 69 years.
Sees a dentist yearly.
His friend has a lazy eye.
Walks independently, with no recent trips or slips.
Plays the piano.
In 2019, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
Enjoys board games.
```

**near** (program answer: s; facts: patient: age = 58; present; current | patient: recent fall; absent; current)
```
An adult man.
Admitted to the medical ward with a urinary infection.
Paints watercolors as a hobby.
Owns a bicycle.
Photographs local wildlife.
His wife lives with psoriasis.
Has two cats.
Sleeps seven hours a night.
His wife burned a hand on a stove years ago.
Uses sunscreen in summer.
Teeth in good repair.
Knits as a hobby.
Free T4 of 1.2 ng/dL in 2011.
Current age 58 years.
Sees a dentist yearly.
His friend has a lazy eye.
Walks independently, with no recent trips or slips.
Plays the piano.
In 2019, folate was 12 ng/mL.
His roommate has recovered from a dislocated finger.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: age = 51; present; current | patient: recent fall; absent; current)
```
Man, adult.
Admitted to the medical ward with a urinary infection.
Owns a bicycle.
Sleeps seven hours a night.
Has two cats.
His friend has a lazy eye.
Enjoys board games.
His wife lives with psoriasis.
Currently aged 51 years.
Knits as a hobby.
In 2019, folate was 12 ng/mL.
Teeth in good repair.
Walks independently, with no recent trips or slips.
His roommate has recovered from a dislocated finger.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2011.
His wife burned a hand on a stove years ago.
Paints watercolors as a hobby.
Plays the piano.
Uses sunscreen in summer.
Photographs local wildlife.
```


## author1 / group 209: `rule_v1.test.gs124.c1.negation.easy.1911`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**base** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: age = 48; present; current | patient: calf swelling = 3.8; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Owns a bicycle.
Hemoglobin within the normal range on recent blood tests.
Currently aged 48 years.
Photographs local wildlife.
Enjoys board games.
Difference in calf circumference now 3.8 cm.
```

**flip** (program answer: s'; facts: patient: colorectal cancer (patient or first-degree relative); present; current | patient: age = 48; present; current | patient: calf swelling = 3.8; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Owns a bicycle.
Colorectal cancer under active treatment.
Currently aged 48 years.
Photographs local wildlife.
Enjoys board games.
Difference in calf circumference now 3.8 cm.
```

**near** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: age = 48; present; current | patient: calf swelling = 3.8; present; current)
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Owns a bicycle.
Never diagnosed with colorectal cancer.
Currently aged 48 years.
Photographs local wildlife.
Enjoys board games.
Difference in calf circumference now 3.8 cm.
```

**pres** (program answer: s; facts: patient: calf swelling = 3.8; present; current | patient: age = 48; present; current | patient: colorectal cancer (patient or first-degree relative); absent; current)
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Owns a bicycle.
Photographs local wildlife.
Current calf swelling 3.8 cm compared with the other leg.
Current age 48 years.
Hemoglobin within the normal range on recent blood tests.
Enjoys board games.
```


## author2 / group 210: `rule_v1.test.gs047.c1.time.easy.1779`

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum potassium is above 5.0 mmol/L and the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time, prescribe aspirin plus clopidogrel instead.

**base** (program answer: s; facts: patient: serum potassium = 3.8; present; current | patient: serum potassium = 4.4; present; past (2005) | patient: venous thromboembolism (patient or first-degree relative); present; past (2024))
```
Woman of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum potassium 3.8 mmol/L.
Back in 2005, serum potassium stood at 4.4 mmol/L.
Teeth in good repair.
Recovered from a pulmonary embolism in 2024.
```

**flip** (program answer: s'; facts: patient: serum potassium = 5.5; present; current | patient: serum potassium = 4.4; present; past (2005) | patient: venous thromboembolism (patient or first-degree relative); present; past (2024))
```
Woman of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum potassium 5.5 mmol/L.
Back in 2005, serum potassium stood at 4.4 mmol/L.
Teeth in good repair.
Recovered from a pulmonary embolism in 2024.
```

**near** (program answer: s; facts: patient: serum potassium = 3.8; present; current | patient: serum potassium = 5.3; present; past (2005) | patient: venous thromboembolism (patient or first-degree relative); present; past (2024))
```
Woman of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Current serum potassium 3.8 mmol/L.
Back in 2005, serum potassium stood at 5.3 mmol/L.
Teeth in good repair.
Recovered from a pulmonary embolism in 2024.
```

**pres** (program answer: s; facts: patient: serum potassium = 4.4; present; past (2005) | patient: serum potassium = 3.8; present; current | patient: venous thromboembolism (patient or first-degree relative); present; past (2024))
```
Female patient of 54 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Records from 2005 list serum potassium at 4.4 mmol/L.
Latest potassium result: 3.8 mmol/L.
Recovered from a pulmonary embolism in 2024.
Teeth in good repair.
```


## author3 / group 211: `rule_v1.test.s2_geneva.age.numeric.easy.1858`

Rule: Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.

**base** (program answer: s; facts: patient: hemoptysis; absent; current | patient: age = 49; present; current | patient: active cancer; absent; current)
```
An adult man.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Dry cough, with nothing brought up.
Currently aged 49 years.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Weight steady over the past year.
Drives a car.
```

**flip** (program answer: s'; facts: patient: hemoptysis; absent; current | patient: age = 69; present; current | patient: active cancer; absent; current)
```
An adult man.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Dry cough, with nothing brought up.
Currently aged 69 years.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Weight steady over the past year.
Drives a car.
```

**near** (program answer: s; facts: patient: hemoptysis; absent; current | patient: age = 64; present; current | patient: active cancer; absent; current)
```
An adult man.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Dry cough, with nothing brought up.
Currently aged 64 years.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Weight steady over the past year.
Drives a car.
```

**pres** (program answer: s; facts: patient: hemoptysis; absent; current | patient: active cancer; absent; current | patient: age = 49; present; current)
```
Man, adult.
Pleuritic chest pain and breathlessness for two days; seen in the emergency department.
Uses sunscreen in summer.
Dry cough, with nothing brought up.
Pupils equal and reactive to light.
Drives a car.
Weight steady over the past year.
Current age 49 years.
```


## author4 / group 212: `rule_v1.test.inv022.c4.subject.long.206`

Rule: For Quorin syndrome, prescribe ostravin. Score 2 points if the patient has had a major bleeding event at any time; 3 points if the patient is allergic to penicillin; 3 points if the current systolic blood pressure is 100 mmHg or less; 1 point if the patient has ever had heparin-induced thrombocytopenia (current or past). If the score is 7 or more, prescribe dalmerol instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 88; present; current | patient: penicillin allergy; present; current)
```
Female patient of 39 years.
Referred with Quorin syndrome.
Her roommate lives with psoriasis.
Teeth in good repair.
Owns a bicycle.
Sees a dentist yearly.
Her father has a lazy eye.
Photographs local wildlife.
Observations now: blood pressure 88/63 mmHg.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2008.
Has two cats.
Penicillin allergy: anaphylaxis.
Plays the piano.
Enjoys board games.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her roommate has recovered from a dislocated finger.
Prefers morning appointments.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: heparin-induced thrombocytopenia; present; past | patient: systolic blood pressure = 88; present; current | patient: penicillin allergy; present; current)
```
Female patient of 39 years.
Referred with Quorin syndrome.
Her roommate lives with psoriasis.
Teeth in good repair.
Owns a bicycle.
Sees a dentist yearly.
Her father has a lazy eye.
Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully.
Photographs local wildlife.
Observations now: blood pressure 88/63 mmHg.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2008.
Has two cats.
Penicillin allergy: anaphylaxis.
Plays the piano.
Enjoys board games.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her roommate has recovered from a dislocated finger.
Prefers morning appointments.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: wife: heparin-induced thrombocytopenia; present; past | patient: systolic blood pressure = 88; present; current | patient: penicillin allergy; present; current)
```
Female patient of 39 years.
Referred with Quorin syndrome.
Her roommate lives with psoriasis.
Teeth in good repair.
Owns a bicycle.
Sees a dentist yearly.
Her father has a lazy eye.
Her wife developed heparin-induced thrombocytopenia years ago.
Photographs local wildlife.
Observations now: blood pressure 88/63 mmHg.
Pupils equal and reactive to light.
Free T4 of 1.2 ng/dL in 2008.
Has two cats.
Penicillin allergy: anaphylaxis.
Plays the piano.
Enjoys board games.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Her roommate has recovered from a dislocated finger.
Prefers morning appointments.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: penicillin allergy; present; current | patient: systolic blood pressure = 88; present; current)
```
Woman of 39 years.
Referred with Quorin syndrome.
Penicillin allergy: anaphylaxis.
Has two cats.
Plays the piano.
Her father has a lazy eye.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Prefers morning appointments.
Photographs local wildlife.
Teeth in good repair.
Uses sunscreen in summer.
Her roommate lives with psoriasis.
Current systolic blood pressure 88 mmHg.
Free T4 of 1.2 ng/dL in 2008.
Enjoys board games.
Pupils equal and reactive to light.
Her roommate has recovered from a dislocated finger.
Sees a dentist yearly.
Owns a bicycle.
```


## author1 / group 213: `rule_v1.test.gs035.c1.time.easy.1899`

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).

**base** (program answer: s; facts: patient: current heart failure; absent; current | patient: cancer at any time; present; current | patient: age = 61; present; current)
```
An adult woman.
Requests contraception.
Drives a car.
Heart sounds without a gallop.
Has melanoma skin cancer and is receiving treatment for it.
Currently aged 61 years.
```

**flip** (program answer: s'; facts: patient: current heart failure; present; current | patient: cancer at any time; present; current | patient: age = 61; present; current)
```
An adult woman.
Requests contraception.
Drives a car.
Current heart failure with ankle swelling.
Has melanoma skin cancer and is receiving treatment for it.
Currently aged 61 years.
```

**near** (program answer: s; facts: patient: current heart failure; present; past (2023) | patient: cancer at any time; present; current | patient: age = 61; present; current)
```
An adult woman.
Requests contraception.
Drives a car.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2023 and off all heart medicines since.
Has melanoma skin cancer and is receiving treatment for it.
Currently aged 61 years.
```

**pres** (program answer: s; facts: patient: current heart failure; absent; current | patient: age = 61; present; current | patient: cancer at any time; present; current)
```
Woman, adult.
Requests contraception.
Heart sounds without a gallop.
Current age 61 years.
Has melanoma skin cancer and is receiving treatment for it.
Drives a car.
```


## author2 / group 214: `rule_v1.test.two_pneumonia.sbp.time.superseded.507`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has new confusion; the current respiratory rate is 30/min or more; the current systolic blood pressure is below 90 mmHg.

**base** (program answer: s; facts: patient: systolic blood pressure = 122; present; past | patient: new confusion; absent; current | patient: systolic blood pressure = 119; present; current | patient: respiratory rate = 36; present; current)
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

**flip** (program answer: s'; facts: patient: systolic blood pressure = 122; present; past | patient: new confusion; absent; current | patient: systolic blood pressure = 77; present; current | patient: respiratory rate = 36; present; current)
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

**near** (program answer: s; facts: patient: systolic blood pressure = 79; present; past | patient: new confusion; absent; current | patient: systolic blood pressure = 119; present; current | patient: respiratory rate = 36; present; current)
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

**pres** (program answer: s; facts: patient: systolic blood pressure = 119; present; current | patient: respiratory rate = 36; present; current | patient: systolic blood pressure = 122; present; past | patient: new confusion; absent; current)
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


## author3 / group 215: `rule_v1.test.gs032.c1.boundary.long.830`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the current eGFR is below 30 mL/min/1.73 m2 and the current calf swelling compared with the other leg is 3.0 cm or more, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: calf swelling = 3.9; present; current | patient: eGFR = 73; present; current)
```
Man of 78 years.
Atrial fibrillation with a ventricular rate of 128/min.
Pupils equal and reactive to light.
His sister burned a hand on a stove years ago.
His wife lives with psoriasis.
Enjoys board games.
Difference in calf circumference now 3.9 cm.
Prefers to be addressed by first name.
Owns a bicycle.
eGFR now 73 mL/min/1.73 m2.
His wife has recovered from a dislocated finger.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Free T4 of 1.2 ng/dL in 2015.
Knits as a hobby.
Has two cats.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: calf swelling = 3.9; present; current | patient: eGFR = 17; present; current)
```
Man of 78 years.
Atrial fibrillation with a ventricular rate of 128/min.
Pupils equal and reactive to light.
His sister burned a hand on a stove years ago.
His wife lives with psoriasis.
Enjoys board games.
Difference in calf circumference now 3.9 cm.
Prefers to be addressed by first name.
Owns a bicycle.
eGFR now 17 mL/min/1.73 m2.
His wife has recovered from a dislocated finger.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Free T4 of 1.2 ng/dL in 2015.
Knits as a hobby.
Has two cats.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Plays the piano.
```

**near** (program answer: s; facts: patient: calf swelling = 3.9; present; current | patient: eGFR = 30; present; current)
```
Man of 78 years.
Atrial fibrillation with a ventricular rate of 128/min.
Pupils equal and reactive to light.
His sister burned a hand on a stove years ago.
His wife lives with psoriasis.
Enjoys board games.
Difference in calf circumference now 3.9 cm.
Prefers to be addressed by first name.
Owns a bicycle.
eGFR now 30 mL/min/1.73 m2.
His wife has recovered from a dislocated finger.
Prefers morning appointments.
In 2024, folate was 12 ng/mL.
Free T4 of 1.2 ng/dL in 2015.
Knits as a hobby.
Has two cats.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Plays the piano.
```

**pres** (program answer: s; facts: patient: calf swelling = 3.9; present; current | patient: eGFR = 73; present; current)
```
Male patient of 78 years.
Atrial fibrillation with a ventricular rate of 128/min.
Free T4 of 1.2 ng/dL in 2015.
Paints watercolors as a hobby.
Current calf swelling 3.9 cm compared with the other leg.
His wife has recovered from a dislocated finger.
In 2024, folate was 12 ng/mL.
Knits as a hobby.
Enjoys board games.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Owns a bicycle.
His sister burned a hand on a stove years ago.
His wife lives with psoriasis.
Has two cats.
Current eGFR 73 mL/min/1.73 m2.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
```


## author4 / group 216: `rule_v1.test.gs224.c2.time.easy.742`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient has ever had a venous thromboembolism (current or past) and the current serum creatinine is above 2.0 mg/dL, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: serum creatinine = 0.9; present; current | patient: venous thromboembolism; present; past (2024) | patient: serum creatinine = 1.0; present; past (2021))
```
Female patient of 25 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current serum creatinine 0.9 mg/dL.
Recovered from a pulmonary embolism in 2024.
Back in 2021, serum creatinine stood at 1.0 mg/dL.
Sees a dentist yearly.
Uses sunscreen in summer.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 2.8; present; current | patient: venous thromboembolism; present; past (2024) | patient: serum creatinine = 1.0; present; past (2021))
```
Female patient of 25 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current serum creatinine 2.8 mg/dL.
Recovered from a pulmonary embolism in 2024.
Back in 2021, serum creatinine stood at 1.0 mg/dL.
Sees a dentist yearly.
Uses sunscreen in summer.
Enjoys board games.
```

**near** (program answer: s; facts: patient: serum creatinine = 0.9; present; current | patient: venous thromboembolism; present; past (2024) | patient: serum creatinine = 2.7; present; past (2021))
```
Female patient of 25 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Current serum creatinine 0.9 mg/dL.
Recovered from a pulmonary embolism in 2024.
Back in 2021, serum creatinine stood at 2.7 mg/dL.
Sees a dentist yearly.
Uses sunscreen in summer.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: serum creatinine = 0.9; present; current | patient: venous thromboembolism; present; past (2024) | patient: serum creatinine = 1.0; present; past (2021))
```
Woman of 25 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Sees a dentist yearly.
Latest creatinine result: 0.9 mg/dL.
Recovered from a pulmonary embolism in 2024.
Records from 2021 list serum creatinine at 1.0 mg/dL.
Enjoys board games.
Uses sunscreen in summer.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism; present; past (2024))
```
Female patient of 25 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Recovered from a pulmonary embolism in 2024.
Sees a dentist yearly.
Uses sunscreen in summer.
Enjoys board games.
```


## author1 / group 217: `rule_v1.test.gs021.c1.boundary.easy.1207`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the current systolic blood pressure is above 160 mmHg or the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: serum creatinine = 0.7; present; current | patient: systolic blood pressure = 135; present; current)
```
Male patient of 51 years.
Hip osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Current serum creatinine 0.7 mg/dL.
Owns a bicycle.
Observations now: blood pressure 135/89 mmHg.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 0.7; present; current | patient: systolic blood pressure = 172; present; current)
```
Male patient of 51 years.
Hip osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Current serum creatinine 0.7 mg/dL.
Owns a bicycle.
Observations now: blood pressure 172/110 mmHg.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: patient: serum creatinine = 0.7; present; current | patient: systolic blood pressure = 160; present; current)
```
Male patient of 51 years.
Hip osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Current serum creatinine 0.7 mg/dL.
Owns a bicycle.
Observations now: blood pressure 160/103 mmHg.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 135; present; current | patient: serum creatinine = 0.7; present; current)
```
Man of 51 years.
Hip osteoarthritis with pain on walking.
Paints watercolors as a hobby.
Current systolic blood pressure 135 mmHg.
Owns a bicycle.
Pupils equal and reactive to light.
Latest creatinine result: 0.7 mg/dL.
```


## author2 / group 218: `rule_v1.test.s1_news2_other.sbp.numeric.long.729`

Rule: NEWS2 (as used here, partial: only the stated band of each listed item): 3 points for a heart rate of 131/min or more; 3 points for a systolic blood pressure of 220 mmHg or more; 2 points for a temperature of 39.1 C or more; 2 points for current use of supplemental oxygen. Any other value of these items scores 0 here, and the other NEWS2 items are not part of this question. Only current findings count.

**base** (program answer: s; facts: patient: heart rate = 67; present; current | patient: systolic blood pressure = 133; present; current | patient: temperature = 36.8; present; current)
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

**flip** (program answer: s'; facts: patient: heart rate = 67; present; current | patient: systolic blood pressure = 220; present; current | patient: temperature = 36.8; present; current)
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

**near** (program answer: s; facts: patient: heart rate = 67; present; current | patient: systolic blood pressure = 215; present; current | patient: temperature = 36.8; present; current)
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

**pres** (program answer: s; facts: patient: systolic blood pressure = 133; present; current | patient: temperature = 36.8; present; current | patient: heart rate = 67; present; current)
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

**missing** (program answer: neither; facts: patient: heart rate = 67; present; current | patient: temperature = 36.8; present; current)
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


## author3 / group 219: `rule_v1.test.gs024.c3.numeric.long.1134`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 3 points if the current ALT is above 120 U/L; 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 3 points if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 4 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: systolic blood pressure = 148; present; current | patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 34; present; current)
```
Female patient of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Has two cats.
Her father sprained a thumb last month.
Lives in a second-floor apartment.
Sees a dentist yearly.
Knits as a hobby.
Sleeps seven hours a night.
Current systolic blood pressure 148 mmHg.
Zinc of 85 mcg/dL in 2010.
Has type 2 diabetes on metformin.
Prefers to be addressed by first name.
Her father has a lazy eye.
ALT now 34 U/L.
Paints watercolors as a hobby.
Her friend wears contact lenses.
Free T4 of 1.2 ng/dL in 2022.
Uses sunscreen in summer.
Her uncle has recovered from a dislocated finger.
Photographs local wildlife.
Owns a bicycle.
Drives a car.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 184; present; current | patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 34; present; current)
```
Female patient of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Has two cats.
Her father sprained a thumb last month.
Lives in a second-floor apartment.
Sees a dentist yearly.
Knits as a hobby.
Sleeps seven hours a night.
Current systolic blood pressure 184 mmHg.
Zinc of 85 mcg/dL in 2010.
Has type 2 diabetes on metformin.
Prefers to be addressed by first name.
Her father has a lazy eye.
ALT now 34 U/L.
Paints watercolors as a hobby.
Her friend wears contact lenses.
Free T4 of 1.2 ng/dL in 2022.
Uses sunscreen in summer.
Her uncle has recovered from a dislocated finger.
Photographs local wildlife.
Owns a bicycle.
Drives a car.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 153; present; current | patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 34; present; current)
```
Female patient of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Has two cats.
Her father sprained a thumb last month.
Lives in a second-floor apartment.
Sees a dentist yearly.
Knits as a hobby.
Sleeps seven hours a night.
Current systolic blood pressure 153 mmHg.
Zinc of 85 mcg/dL in 2010.
Has type 2 diabetes on metformin.
Prefers to be addressed by first name.
Her father has a lazy eye.
ALT now 34 U/L.
Paints watercolors as a hobby.
Her friend wears contact lenses.
Free T4 of 1.2 ng/dL in 2022.
Uses sunscreen in summer.
Her uncle has recovered from a dislocated finger.
Photographs local wildlife.
Owns a bicycle.
Drives a car.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 34; present; current | patient: systolic blood pressure = 148; present; current)
```
Woman of 50 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Sleeps seven hours a night.
Her father has a lazy eye.
Her friend wears contact lenses.
Her father sprained a thumb last month.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Drives a car.
Paints watercolors as a hobby.
Photographs local wildlife.
Knits as a hobby.
Has type 2 diabetes on metformin.
Owns a bicycle.
Current ALT 34 U/L.
Has two cats.
Her uncle has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2010.
Prefers to be addressed by first name.
Observations now: blood pressure 148/96 mmHg.
Sees a dentist yearly.
Free T4 of 1.2 ng/dL in 2022.
```


## author4 / group 220: `rule_v1.test.gs190.c1.time.easy.27`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If the current weight is 60 kg or less and the patient has ever had a venous thromboembolism (current or past), prescribe intravenous piperacillin-tazobactam instead.

**base** (program answer: s; facts: patient: weight = 76; present; current | patient: weight = 94; present; past (2024) | patient: venous thromboembolism; present; current)
```
Man of 69 years.
Suspected chest infection; assessed on the medical ward.
Prefers morning appointments.
Prefers to be addressed by first name.
Teeth in good repair.
Current weight 76 kg.
Enjoys board games.
Records from 2024 list weight at 94 kg.
Has an acute pulmonary embolism, diagnosed this week.
```

**flip** (program answer: s'; facts: patient: weight = 59; present; current | patient: weight = 94; present; past (2024) | patient: venous thromboembolism; present; current)
```
Man of 69 years.
Suspected chest infection; assessed on the medical ward.
Prefers morning appointments.
Prefers to be addressed by first name.
Teeth in good repair.
Current weight 59 kg.
Enjoys board games.
Records from 2024 list weight at 94 kg.
Has an acute pulmonary embolism, diagnosed this week.
```

**near** (program answer: s; facts: patient: weight = 76; present; current | patient: weight = 48; present; past (2024) | patient: venous thromboembolism; present; current)
```
Man of 69 years.
Suspected chest infection; assessed on the medical ward.
Prefers morning appointments.
Prefers to be addressed by first name.
Teeth in good repair.
Current weight 76 kg.
Enjoys board games.
Records from 2024 list weight at 48 kg.
Has an acute pulmonary embolism, diagnosed this week.
```

**pres** (program answer: s; facts: patient: weight = 76; present; current | patient: weight = 94; present; past (2024) | patient: venous thromboembolism; present; current)
```
Male patient of 69 years.
Suspected chest infection; assessed on the medical ward.
Prefers morning appointments.
Prefers to be addressed by first name.
Latest weight 76 kg.
Enjoys board games.
Back in 2024, weight stood at 94 kg.
Teeth in good repair.
Has an acute pulmonary embolism, diagnosed this week.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism; present; current)
```
Man of 69 years.
Suspected chest infection; assessed on the medical ward.
Prefers morning appointments.
Prefers to be addressed by first name.
Teeth in good repair.
Enjoys board games.
Has an acute pulmonary embolism, diagnosed this week.
```


## author1 / group 221: `rule_v1.test.gs066.c1.subject.easy.1271`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient currently has tonsillar exudate, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: tonsillar exudate; present; current)
```
Man of 42 years.
Atrial fibrillation with a ventricular rate of 128/min.
Rectal exam unremarkable.
Drives a car.
Tonsillar exudate visible on both sides.
Pupils equal and reactive to light.
```

**flip** (program answer: s'; facts: sister: colorectal cancer (patient or first-degree relative); present; past (2017) | patient: tonsillar exudate; present; current)
```
Man of 42 years.
Atrial fibrillation with a ventricular rate of 128/min.
His sister recovered from colon cancer after an operation in 2017.
Drives a car.
Tonsillar exudate visible on both sides.
Pupils equal and reactive to light.
```

**near** (program answer: s; facts: friend: colorectal cancer (patient or first-degree relative); present; past | patient: tonsillar exudate; present; current)
```
Man of 42 years.
Atrial fibrillation with a ventricular rate of 128/min.
His friend was treated for bowel cancer years ago.
Drives a car.
Tonsillar exudate visible on both sides.
Pupils equal and reactive to light.
```

**pres** (program answer: s; facts: patient: colorectal cancer (patient or first-degree relative); absent; current | patient: tonsillar exudate; present; current)
```
Male patient of 42 years.
Atrial fibrillation with a ventricular rate of 128/min.
Pupils equal and reactive to light.
Rectal exam unremarkable.
Drives a car.
Tonsillar exudate visible on both sides.
```


## author2 / group 222: `rule_v1.test.gs071.c2.subject.long.1413`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**base** (program answer: s; facts: patient: temperature = 38.5; present; current | patient: peptic ulcer at any time; absent; current)
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

**flip** (program answer: s'; facts: patient: temperature = 38.5; present; current | patient: peptic ulcer at any time; present; past (2014))
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

**near** (program answer: s; facts: patient: temperature = 38.5; present; current | roommate: peptic ulcer at any time; present; past)
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

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: temperature = 38.5; present; current)
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


## author3 / group 223: `rule_v1.test.s3_rockall.hf.negation.long.89`

Rule: Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

**base** (program answer: s; facts: patient: systolic blood pressure = 137; present; current | patient: heart failure; absent; current | patient: age = 46; present; current)
```
Woman, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Observations now: blood pressure 137/90 mmHg.
Heart sounds without a gallop.
During a checkup in 2023, total protein was 7.0 g/dL.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Owns a bicycle.
Zinc of 85 mcg/dL in 2021.
Prefers morning appointments.
Prefers to be addressed by first name.
Sees a dentist yearly.
Her roommate has a lazy eye.
Uses sunscreen in summer.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2018, lipase was 30 U/L.
Lives in a second-floor apartment.
Currently aged 46 years.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 137; present; current | patient: heart failure; present; current | patient: age = 46; present; current)
```
Woman, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Observations now: blood pressure 137/90 mmHg.
Has heart failure, treated with diuretics.
During a checkup in 2023, total protein was 7.0 g/dL.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Owns a bicycle.
Zinc of 85 mcg/dL in 2021.
Prefers morning appointments.
Prefers to be addressed by first name.
Sees a dentist yearly.
Her roommate has a lazy eye.
Uses sunscreen in summer.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2018, lipase was 30 U/L.
Lives in a second-floor apartment.
Currently aged 46 years.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 137; present; current | patient: heart failure; absent; current | patient: age = 46; present; current)
```
Woman, adult.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Observations now: blood pressure 137/90 mmHg.
Heart failure: never diagnosed.
During a checkup in 2023, total protein was 7.0 g/dL.
Her roommate wears contact lenses.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Owns a bicycle.
Zinc of 85 mcg/dL in 2021.
Prefers morning appointments.
Prefers to be addressed by first name.
Sees a dentist yearly.
Her roommate has a lazy eye.
Uses sunscreen in summer.
Photographs local wildlife.
Paints watercolors as a hobby.
In 2018, lipase was 30 U/L.
Lives in a second-floor apartment.
Currently aged 46 years.
```

**pres** (program answer: s; facts: patient: systolic blood pressure = 137; present; current | patient: age = 46; present; current | patient: heart failure; absent; current)
```
An adult woman.
Coffee-ground vomiting since the early hours; assessed in the emergency department.
Sleeps seven hours a night.
Zinc of 85 mcg/dL in 2021.
Prefers to be addressed by first name.
Owns a bicycle.
Her roommate wears contact lenses.
Paints watercolors as a hobby.
Current systolic blood pressure 137 mmHg.
Photographs local wildlife.
Current age 46 years.
Pupils equal and reactive to light.
Her roommate has a lazy eye.
Lives in a second-floor apartment.
During a checkup in 2023, total protein was 7.0 g/dL.
Heart sounds without a gallop.
In 2018, lipase was 30 U/L.
Uses sunscreen in summer.
Sees a dentist yearly.
Prefers morning appointments.
```


## author4 / group 224: `rule_v1.test.rcri.cr.boundary.alt.74`

Rule: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.

**base** (program answer: s; facts: patient: creatinine = 1.4; present; current | patient: heart failure; absent; current)
```
Female patient of 76 years.
Preoperative assessment before elective colectomy.
Latest creatinine result: 1.4 mg/dL.
Paints watercolors as a hobby.
Has two cats.
Photographs local wildlife.
Heart sounds without a gallop.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: creatinine = 1.9; present; current | patient: heart failure; absent; current)
```
Female patient of 76 years.
Preoperative assessment before elective colectomy.
Latest creatinine result: 1.9 mg/dL.
Paints watercolors as a hobby.
Has two cats.
Photographs local wildlife.
Heart sounds without a gallop.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: creatinine = 1.5; present; current | patient: heart failure; absent; current)
```
Female patient of 76 years.
Preoperative assessment before elective colectomy.
Latest creatinine result: 1.5 mg/dL.
Paints watercolors as a hobby.
Has two cats.
Photographs local wildlife.
Heart sounds without a gallop.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: heart failure; absent; current | patient: creatinine = 1.4; present; current)
```
Woman of 76 years.
Preoperative assessment before elective colectomy.
Photographs local wildlife.
Paints watercolors as a hobby.
Has two cats.
Heart sounds without a gallop.
Current serum creatinine 1.4 mg/dL.
Sleeps seven hours a night.
```


## author1 / group 225: `rule_v1.test.inv021.c1.negation.easy.61`

Rule: For Varnell syndrome, prescribe lorvatide. If the patient has ever had angioedema (current or past), prescribe pemraxin instead.

**base** (program answer: s; facts: )
```
Woman of 43 years.
Referred with Varnell syndrome.
Has two cats.
Photographs local wildlife.
Owns a bicycle.
```

**flip** (program answer: s'; facts: patient: angioedema; present; current)
```
Woman of 43 years.
Referred with Varnell syndrome.
Has two cats.
Photographs local wildlife.
Owns a bicycle.
Recurrent angioedema, under allergy follow-up.
```

**near** (program answer: s; facts: patient: angioedema; absent; current)
```
Woman of 43 years.
Referred with Varnell syndrome.
Has two cats.
Photographs local wildlife.
Owns a bicycle.
Never diagnosed with angioedema.
```

**pres** (program answer: s; facts: )
```
Female patient of 43 years.
Referred with Varnell syndrome.
Owns a bicycle.
Photographs local wildlife.
Has two cats.
```


## author2 / group 226: `rule_v1.test.gs044.c3.negation.long.758`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

**base** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: age = 66; present; current | patient: peptic ulcer at any time; absent; current)
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

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; present; past | patient: age = 66; present; current | patient: peptic ulcer at any time; absent; current)
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

**near** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: age = 66; present; current | patient: peptic ulcer at any time; absent; current)
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

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: myocardial infarction or peripheral artery disease; absent; current | patient: age = 66; present; current)
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


## author3 / group 227: `rule_v1.test.cut_vte.cancer.time.easy.689`

Rule: For thromboprophylaxis in a medical inpatient, prescribe compression stockings. Score 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. If the score is 4 or more, prescribe enoxaparin instead.

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: heart failure; absent; current | patient: age = 76; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Coagulation tests normal on recent bloodwork.
Prefers morning appointments.
Heart sounds without a gallop.
Current age 76 years.
Prefers to be addressed by first name.
Owns a bicycle.
Has two cats.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; absent; current | patient: heart failure; absent; current | patient: active cancer; present; current | patient: age = 76; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Coagulation tests normal on recent bloodwork.
Prefers morning appointments.
Heart sounds without a gallop.
Has metastatic lung cancer, receiving palliative treatment.
Current age 76 years.
Prefers to be addressed by first name.
Owns a bicycle.
Has two cats.
```

**near** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: heart failure; absent; current | patient: active cancer; present; past | patient: age = 76; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Coagulation tests normal on recent bloodwork.
Prefers morning appointments.
Heart sounds without a gallop.
Had thyroid cancer years ago and is now cured.
Current age 76 years.
Prefers to be addressed by first name.
Owns a bicycle.
Has two cats.
```

**pres** (program answer: s; facts: patient: heart failure; absent; current | patient: age = 76; present; current | patient: venous thromboembolism; absent; current)
```
Man, adult.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Prefers to be addressed by first name.
Heart sounds without a gallop.
Has two cats.
Owns a bicycle.
Currently aged 76 years.
Prefers morning appointments.
Coagulation tests normal on recent bloodwork.
```

**missing** (program answer: neither; facts: patient: venous thromboembolism; absent; current | patient: heart failure; absent; current | patient: active cancer; unknown; current | patient: age = 76; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Coagulation tests normal on recent bloodwork.
Prefers morning appointments.
Heart sounds without a gallop.
Active cancer: status unclear from the records at hand.
Current age 76 years.
Prefers to be addressed by first name.
Owns a bicycle.
Has two cats.
```


## author4 / group 228: `rule_v1.test.gs077.c1.subject.easy.260`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient currently has tonsillar exudate, prescribe amlodipine instead.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current)
```
Woman of 31 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Knits as a hobby.
Uses sunscreen in summer.
Owns a bicycle.
Tonsils pink and clean on inspection.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; present; current)
```
Woman of 31 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Knits as a hobby.
Uses sunscreen in summer.
Owns a bicycle.
Tonsils swollen and coated with yellow exudate.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: father: tonsillar exudate; present; current)
```
Woman of 31 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Knits as a hobby.
Uses sunscreen in summer.
Owns a bicycle.
Her father has a sore throat with tonsillar exudate.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; absent; current)
```
Female patient of 31 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Paints watercolors as a hobby.
Knits as a hobby.
Owns a bicycle.
Tonsils pink and clean on inspection.
Uses sunscreen in summer.
```


## author1 / group 229: `rule_v1.test.gs054.c2.subject.easy.1935`

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. Score 3 points if the patient currently has a venous thromboembolism; 2 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current respiratory rate is 22/min or more; 1 point if the current oxygen saturation is 91% or less. If the score is 6 or more, prescribe intravenous co-amoxiclav instead.

**base** (program answer: s; facts: patient: oxygen saturation = 85; present; current | patient: current venous thromboembolism; present; current | patient: respiratory rate = 14; present; current)
```
Woman of 56 years.
Community-acquired pneumonia confirmed on chest radiograph.
Drives a car.
Prefers to be addressed by first name.
Teeth in good repair.
Current oxygen saturation 85%.
Has an acute pulmonary embolism, diagnosed this week.
Current respiratory rate 14/min.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: oxygen saturation = 85; present; current | patient: current venous thromboembolism; present; current | patient: respiratory rate = 14; present; current | sister: colorectal cancer (patient or first-degree relative); present; current)
```
Woman of 56 years.
Community-acquired pneumonia confirmed on chest radiograph.
Drives a car.
Prefers to be addressed by first name.
Teeth in good repair.
Current oxygen saturation 85%.
Has an acute pulmonary embolism, diagnosed this week.
Current respiratory rate 14/min.
Sees a dentist yearly.
Her sister is undergoing surgery for bowel cancer.
```

**near** (program answer: s; facts: patient: oxygen saturation = 85; present; current | patient: current venous thromboembolism; present; current | patient: respiratory rate = 14; present; current | uncle: colorectal cancer (patient or first-degree relative); present; current)
```
Woman of 56 years.
Community-acquired pneumonia confirmed on chest radiograph.
Drives a car.
Prefers to be addressed by first name.
Teeth in good repair.
Current oxygen saturation 85%.
Has an acute pulmonary embolism, diagnosed this week.
Current respiratory rate 14/min.
Sees a dentist yearly.
Her uncle is undergoing surgery for bowel cancer.
```

**pres** (program answer: s; facts: patient: respiratory rate = 14; present; current | patient: current venous thromboembolism; present; current | patient: oxygen saturation = 85; present; current)
```
Female patient of 56 years.
Community-acquired pneumonia confirmed on chest radiograph.
Observations now: respiratory rate 14/min.
Drives a car.
Has an acute pulmonary embolism, diagnosed this week.
Sees a dentist yearly.
Latest oxygen saturation reading: 85%.
Prefers to be addressed by first name.
Teeth in good repair.
```


## author2 / group 230: `rule_v1.test.gs131.c3.subject.long.22`

Rule: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: heart rate = 100; present; current | patient: coronary artery disease; absent; current | patient: eGFR = 41; present; current)
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

**flip** (program answer: s'; facts: patient: heart rate = 100; present; current | patient: coronary artery disease; present; current | patient: eGFR = 41; present; current)
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

**near** (program answer: s; facts: patient: heart rate = 100; present; current | roommate: coronary artery disease; present; current | patient: eGFR = 41; present; current)
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

**pres** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: heart rate = 100; present; current | patient: eGFR = 41; present; current)
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


## author3 / group 231: `rule_v1.test.s2_wells_pe.hemoptysis.subject.easy.738`

Rule: Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: heart rate = 67; present; current | patient: hemoptysis; absent; current)
```
Female patient of 56 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Oncology follow-up: none.
Current heart rate 67/min.
Sputum colorless on inspection.
Prefers to be addressed by first name.
Prefers morning appointments.
Owns a bicycle.
```

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: heart rate = 67; present; current | patient: hemoptysis; present; current)
```
Female patient of 56 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Oncology follow-up: none.
Current heart rate 67/min.
Currently coughing up blood with each bout of coughing.
Prefers to be addressed by first name.
Prefers morning appointments.
Owns a bicycle.
```

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: heart rate = 67; present; current | uncle: hemoptysis; present; current)
```
Female patient of 56 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Oncology follow-up: none.
Current heart rate 67/min.
Her uncle is currently coughing up blood.
Prefers to be addressed by first name.
Prefers morning appointments.
Owns a bicycle.
```

**pres** (program answer: s; facts: patient: heart rate = 67; present; current | patient: hemoptysis; absent; current | patient: active cancer; absent; current)
```
Woman of 56 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Prefers to be addressed by first name.
Heart rate now 67/min on a pulse check.
Sputum colorless on inspection.
Owns a bicycle.
Oncology follow-up: none.
Prefers morning appointments.
```

**missing** (program answer: neither; facts: patient: active cancer; absent; current | patient: heart rate = 67; present; current | patient: hemoptysis; unknown; current)
```
Female patient of 56 years.
Sudden breathlessness and pleuritic chest pain; assessed in the emergency department.
Oncology follow-up: none.
Current heart rate 67/min.
Hemoptysis: status unclear from the records at hand.
Prefers to be addressed by first name.
Prefers morning appointments.
Owns a bicycle.
```


## author4 / group 232: `rule_v1.test.statin_alt.alt.time.alt.582`

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**base** (program answer: s; facts: patient: ALT = 32; present; past (2007) | patient: ALT = 14; present; current)
```
Female patient of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Owns a bicycle.
Back in 2007, ALT stood at 32 U/L.
ALT now 14 U/L.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: ALT = 32; present; past (2007) | patient: ALT = 113; present; current)
```
Female patient of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Owns a bicycle.
Back in 2007, ALT stood at 32 U/L.
ALT now 113 U/L.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: ALT = 294; present; past (2007) | patient: ALT = 14; present; current)
```
Female patient of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Owns a bicycle.
Back in 2007, ALT stood at 294 U/L.
ALT now 14 U/L.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: ALT = 32; present; past (2007) | patient: ALT = 14; present; current)
```
Woman of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Records from 2007 list ALT at 32 U/L.
Current ALT 14 U/L.
Owns a bicycle.
Knits as a hobby.
```


## author1 / group 233: `rule_v1.test.gs246.c1.boundary.long.752`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

**base** (program answer: s; facts: patient: angioedema; absent; current | patient: white cell count = 9.5; present; current | patient: active cancer; present; current)
```
Male patient of 47 years.
Acute low back pain after lifting.
Enjoys board games.
Drives a car.
His uncle wears contact lenses.
Sleeps seven hours a night.
His roommate sprained a thumb last month.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Face and neck without swelling on examination.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Teeth in good repair.
Prefers morning appointments.
Current white cell count 9.5 x10^9/L.
Has two cats.
In 2012, folate was 12 ng/mL.
Paints watercolors as a hobby.
Has melanoma skin cancer and is receiving treatment for it.
```

**flip** (program answer: s'; facts: patient: angioedema; absent; current | patient: white cell count = 13.4; present; current | patient: active cancer; present; current)
```
Male patient of 47 years.
Acute low back pain after lifting.
Enjoys board games.
Drives a car.
His uncle wears contact lenses.
Sleeps seven hours a night.
His roommate sprained a thumb last month.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Face and neck without swelling on examination.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Teeth in good repair.
Prefers morning appointments.
Current white cell count 13.4 x10^9/L.
Has two cats.
In 2012, folate was 12 ng/mL.
Paints watercolors as a hobby.
Has melanoma skin cancer and is receiving treatment for it.
```

**near** (program answer: s; facts: patient: angioedema; absent; current | patient: white cell count = 12.0; present; current | patient: active cancer; present; current)
```
Male patient of 47 years.
Acute low back pain after lifting.
Enjoys board games.
Drives a car.
His uncle wears contact lenses.
Sleeps seven hours a night.
His roommate sprained a thumb last month.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Prefers to be addressed by first name.
Plays the piano.
Lives in a second-floor apartment.
Knits as a hobby.
Face and neck without swelling on examination.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Teeth in good repair.
Prefers morning appointments.
Current white cell count 12.0 x10^9/L.
Has two cats.
In 2012, folate was 12 ng/mL.
Paints watercolors as a hobby.
Has melanoma skin cancer and is receiving treatment for it.
```

**pres** (program answer: s; facts: patient: active cancer; present; current | patient: white cell count = 9.5; present; current | patient: angioedema; absent; current)
```
Man of 47 years.
Acute low back pain after lifting.
Has two cats.
His roommate sprained a thumb last month.
Teeth in good repair.
Pupils equal and reactive to light.
Has melanoma skin cancer and is receiving treatment for it.
Lives in a second-floor apartment.
During a checkup in 2013, free T3 was 3.2 pg/mL.
In 2012, folate was 12 ng/mL.
Knits as a hobby.
Prefers to be addressed by first name.
Drives a car.
Uses sunscreen in summer.
His uncle wears contact lenses.
Latest WBC is 9.5 x10^9/L.
Sleeps seven hours a night.
Plays the piano.
Face and neck without swelling on examination.
Paints watercolors as a hobby.
Prefers morning appointments.
Enjoys board games.
```


## author2 / group 234: `rule_v1.test.t2d_metformin.egfr.boundary.alt.299`

Rule: For newly diagnosed type 2 diabetes, start metformin. If the patient's current eGFR is below 45 mL/min/1.73 m2, start sitagliptin instead.

**base** (program answer: s; facts: patient: eGFR = 70; present; current)
```
Woman of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Uses sunscreen in summer.
Current eGFR 70 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: eGFR = 36; present; current)
```
Woman of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Uses sunscreen in summer.
Current eGFR 36 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: eGFR = 45; present; current)
```
Woman of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Sleeps seven hours a night.
Uses sunscreen in summer.
Current eGFR 45 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: eGFR = 70; present; current)
```
Female patient of 32 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
eGFR now 70 mL/min/1.73 m2.
Sleeps seven hours a night.
Uses sunscreen in summer.
```


## author3 / group 235: `rule_v1.test.gs021.c2.boundary.easy.225`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the current systolic blood pressure is above 160 mmHg or the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: serum creatinine = 0.7; present; current | patient: systolic blood pressure = 139; present; current)
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Latest creatinine result: 0.7 mg/dL.
Current systolic blood pressure 139 mmHg.
```

**flip** (program answer: s'; facts: patient: serum creatinine = 2.7; present; current | patient: systolic blood pressure = 139; present; current)
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Latest creatinine result: 2.7 mg/dL.
Current systolic blood pressure 139 mmHg.
```

**near** (program answer: s; facts: patient: serum creatinine = 2.0; present; current | patient: systolic blood pressure = 139; present; current)
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Latest creatinine result: 2.0 mg/dL.
Current systolic blood pressure 139 mmHg.
```

**pres** (program answer: s; facts: patient: serum creatinine = 0.7; present; current | patient: systolic blood pressure = 139; present; current)
```
Male patient of 54 years.
Hip osteoarthritis with pain on walking.
Current serum creatinine 0.7 mg/dL.
Sleeps seven hours a night.
Observations now: blood pressure 139/91 mmHg.
```

**missing** (program answer: neither; facts: patient: systolic blood pressure = 139; present; current)
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Current systolic blood pressure 139 mmHg.
```


## author4 / group 236: `rule_v1.test.s2_atria_bleed.egfr.boundary.alt.987`

Rule: ATRIA bleeding score for men (as used here, partial): 3 points each for a current hemoglobin below 13.0 g/dL and a current eGFR below 45 mL/min/1.73 m2; 2 points for a current age of 75 years or more; 1 point for hypertension at any time. Other ATRIA items are not part of this question.

**base** (program answer: s; facts: patient: hemoglobin = 14.7; present; current | patient: age = 66; present; current | patient: eGFR = 62; present; current)
```
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Current Hgb 14.7 g/dL.
Currently aged 66 years.
eGFR now 62 mL/min/1.73 m2.
Owns a bicycle.
```

**flip** (program answer: s'; facts: patient: hemoglobin = 14.7; present; current | patient: age = 66; present; current | patient: eGFR = 31; present; current)
```
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Current Hgb 14.7 g/dL.
Currently aged 66 years.
eGFR now 31 mL/min/1.73 m2.
Owns a bicycle.
```

**near** (program answer: s; facts: patient: hemoglobin = 14.7; present; current | patient: age = 66; present; current | patient: eGFR = 45; present; current)
```
Man, adult.
Atrial fibrillation; a decision on warfarin is pending.
Current Hgb 14.7 g/dL.
Currently aged 66 years.
eGFR now 45 mL/min/1.73 m2.
Owns a bicycle.
```

**pres** (program answer: s; facts: patient: age = 66; present; current | patient: eGFR = 62; present; current | patient: hemoglobin = 14.7; present; current)
```
An adult man.
Atrial fibrillation; a decision on warfarin is pending.
Owns a bicycle.
Current age 66 years.
Current eGFR 62 mL/min/1.73 m2.
Latest Hgb result: 14.7 g/dL.
```


## author1 / group 237: `rule_v1.test.gs075.c2.subject.long.170`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If at least two of the following apply, prescribe amlodipine instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the patient is currently taking warfarin; the current calf swelling compared with the other leg is 3.0 cm or more.

**base** (program answer: s; facts: father: colorectal cancer (patient or first-degree relative); present; current | patient: calf swelling = 0.3; present; current)
```
Female patient of 46 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Her father is undergoing surgery for bowel cancer.
Teeth in good repair.
Sleeps seven hours a night.
Her father sprained a thumb last month.
Paints watercolors as a hobby.
Sees a dentist yearly.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Plays the piano.
Drives a car.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2007, total protein was 7.0 g/dL.
Current calf swelling 0.3 cm compared with the other leg.
In 2009, folate was 12 ng/mL.
Knits as a hobby.
Owns a bicycle.
```

**flip** (program answer: s'; facts: father: colorectal cancer (patient or first-degree relative); present; current | patient: warfarin; present; current | patient: calf swelling = 0.3; present; current)
```
Female patient of 46 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Her father is undergoing surgery for bowel cancer.
Teeth in good repair.
Sleeps seven hours a night.
Her father sprained a thumb last month.
Paints watercolors as a hobby.
Sees a dentist yearly.
Anticoagulated with warfarin; INR checked monthly at the clinic.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Plays the piano.
Drives a car.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2007, total protein was 7.0 g/dL.
Current calf swelling 0.3 cm compared with the other leg.
In 2009, folate was 12 ng/mL.
Knits as a hobby.
Owns a bicycle.
```

**near** (program answer: s; facts: father: colorectal cancer (patient or first-degree relative); present; current | wife: warfarin; present; current | patient: calf swelling = 0.3; present; current)
```
Female patient of 46 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Her father is undergoing surgery for bowel cancer.
Teeth in good repair.
Sleeps seven hours a night.
Her father sprained a thumb last month.
Paints watercolors as a hobby.
Sees a dentist yearly.
Her wife is on warfarin with monthly INR checks.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Plays the piano.
Drives a car.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2007, total protein was 7.0 g/dL.
Current calf swelling 0.3 cm compared with the other leg.
In 2009, folate was 12 ng/mL.
Knits as a hobby.
Owns a bicycle.
```

**pres** (program answer: s; facts: patient: calf swelling = 0.3; present; current | father: colorectal cancer (patient or first-degree relative); present; current)
```
Woman of 46 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
In 2009, folate was 12 ng/mL.
Has two cats.
Difference in calf circumference now 0.3 cm.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Drives a car.
Her father is undergoing surgery for bowel cancer.
Enjoys board games.
Owns a bicycle.
Knits as a hobby.
Her wife has recovered from a dislocated finger.
Teeth in good repair.
Plays the piano.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Uses sunscreen in summer.
Her father sprained a thumb last month.
Sees a dentist yearly.
Prefers to be addressed by first name.
During a checkup in 2007, total protein was 7.0 g/dL.
Paints watercolors as a hobby.
Prefers morning appointments.
```

**missing** (program answer: neither; facts: father: colorectal cancer (patient or first-degree relative); present; current | patient: warfarin; unknown; current | patient: calf swelling = 0.3; present; current)
```
Female patient of 46 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Her father is undergoing surgery for bowel cancer.
Teeth in good repair.
Sleeps seven hours a night.
Her father sprained a thumb last month.
Paints watercolors as a hobby.
Sees a dentist yearly.
Warfarin: status unclear from the records at hand.
Her wife has recovered from a dislocated finger.
Enjoys board games.
Uses sunscreen in summer.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Plays the piano.
Drives a car.
During a checkup in 2016, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Prefers morning appointments.
During a checkup in 2007, total protein was 7.0 g/dL.
Current calf swelling 0.3 cm compared with the other leg.
In 2009, folate was 12 ng/mL.
Knits as a hobby.
Owns a bicycle.
```


## author2 / group 238: `rule_v1.test.gs025.c1.subject.long.432`

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**base** (program answer: s; facts: patient: myocardial infarction or peripheral artery disease; absent; current | patient: temperature = 38.2; present; current)
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

**flip** (program answer: s'; facts: patient: myocardial infarction or peripheral artery disease; present; current | patient: temperature = 38.2; present; current)
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

**near** (program answer: s; facts: friend: myocardial infarction or peripheral artery disease; present; current | patient: temperature = 38.2; present; current)
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

**pres** (program answer: s; facts: patient: temperature = 38.2; present; current | patient: myocardial infarction or peripheral artery disease; absent; current)
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

**missing** (program answer: neither; facts: patient: myocardial infarction or peripheral artery disease; unknown; current | patient: temperature = 38.2; present; current)
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


## author3 / group 239: `rule_v1.test.inv027.c1.subject.easy.246`

Rule: For Tessaly disease, prescribe velimor. If the patient is allergic to penicillin, prescribe quantrel instead.

**base** (program answer: s; facts: )
```
Male patient of 28 years.
Referred with Tessaly disease.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: penicillin allergy; present; current)
```
Male patient of 28 years.
Referred with Tessaly disease.
Known penicillin allergy with angioedema.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

**near** (program answer: s; facts: roommate: penicillin allergy; present; current)
```
Male patient of 28 years.
Referred with Tessaly disease.
His roommate has a penicillin allergy.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: )
```
Man of 28 years.
Referred with Tessaly disease.
Sees a dentist yearly.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
```


## author4 / group 240: `rule_v1.test.inv054.c3.negation.easy.587`

Rule: For Brask fever, prescribe gendrotil. If at least two of the following apply, prescribe lumacept instead: the patient has ever had asthma (current or past); the patient has an active peptic ulcer; the patient currently has a mechanical heart valve.

**base** (program answer: s; facts: patient: active peptic ulcer; absent; current | patient: mechanical heart valve; absent; current | patient: asthma at any time; present; past)
```
Woman of 51 years.
Referred with Brask fever.
Appetite good; no indigestion.
Lives in a second-floor apartment.
Plays the piano.
Heart sounds without a metallic click.
Formerly had asthma in elementary school; well for many years without inhalers.
```

**flip** (program answer: s'; facts: patient: active peptic ulcer; absent; current | patient: mechanical heart valve; present; current | patient: asthma at any time; present; past)
```
Woman of 51 years.
Referred with Brask fever.
Appetite good; no indigestion.
Lives in a second-floor apartment.
Plays the piano.
Lives with a mechanical aortic valve prosthesis.
Formerly had asthma in elementary school; well for many years without inhalers.
```

**near** (program answer: s; facts: patient: active peptic ulcer; absent; current | patient: mechanical heart valve; absent; current | patient: asthma at any time; present; past)
```
Woman of 51 years.
Referred with Brask fever.
Appetite good; no indigestion.
Lives in a second-floor apartment.
Plays the piano.
Never received a mechanical heart valve.
Formerly had asthma in elementary school; well for many years without inhalers.
```

**pres** (program answer: s; facts: patient: mechanical heart valve; absent; current | patient: active peptic ulcer; absent; current | patient: asthma at any time; present; past)
```
Female patient of 51 years.
Referred with Brask fever.
Heart sounds without a metallic click.
Appetite good; no indigestion.
Formerly had asthma in elementary school; well for many years without inhalers.
Plays the piano.
Lives in a second-floor apartment.
```


## author1 / group 241: `rule_v1.test.gs179.c2.time.easy.563`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the patient has ever had diabetes (current or past) and the current white cell count is above 12.0 x10^9/L, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: white cell count = 7.8; present; current | patient: white cell count = 10.3; present; past (2006) | patient: diabetes; present; current)
```
Woman of 83 years.
Atrial fibrillation with a ventricular rate of 128/min.
Latest WBC is 7.8 x10^9/L.
Drives a car.
Paints watercolors as a hobby.
Back in 2006, white cell count stood at 10.3 x10^9/L.
Has type 2 diabetes on metformin.
Owns a bicycle.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: white cell count = 13.4; present; current | patient: white cell count = 10.3; present; past (2006) | patient: diabetes; present; current)
```
Woman of 83 years.
Atrial fibrillation with a ventricular rate of 128/min.
Latest WBC is 13.4 x10^9/L.
Drives a car.
Paints watercolors as a hobby.
Back in 2006, white cell count stood at 10.3 x10^9/L.
Has type 2 diabetes on metformin.
Owns a bicycle.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: white cell count = 7.8; present; current | patient: white cell count = 12.8; present; past (2006) | patient: diabetes; present; current)
```
Woman of 83 years.
Atrial fibrillation with a ventricular rate of 128/min.
Latest WBC is 7.8 x10^9/L.
Drives a car.
Paints watercolors as a hobby.
Back in 2006, white cell count stood at 12.8 x10^9/L.
Has type 2 diabetes on metformin.
Owns a bicycle.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: diabetes; present; current | patient: white cell count = 7.8; present; current | patient: white cell count = 10.3; present; past (2006))
```
Female patient of 83 years.
Atrial fibrillation with a ventricular rate of 128/min.
Owns a bicycle.
Prefers morning appointments.
Has type 2 diabetes on metformin.
Drives a car.
Current white cell count 7.8 x10^9/L.
Records from 2006 list white cell count at 10.3 x10^9/L.
Paints watercolors as a hobby.
```

**missing** (program answer: neither; facts: patient: diabetes; present; current)
```
Woman of 83 years.
Atrial fibrillation with a ventricular rate of 128/min.
Drives a car.
Paints watercolors as a hobby.
Has type 2 diabetes on metformin.
Owns a bicycle.
Prefers morning appointments.
```


## author2 / group 242: `rule_v1.test.c1_methotrexate.alt.time.alt.824`

Rule: For newly diagnosed rheumatoid arthritis, prescribe methotrexate. If the current ALT is above 40 U/L, prescribe hydroxychloroquine instead.

**base** (program answer: s; facts: patient: ALT = 10; present; past (2005) | patient: ALT = 17; present; current)
```
Female patient of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Teeth in good repair.
Sleeps seven hours a night.
Owns a bicycle.
Records from 2005 list ALT at 10 U/L.
Current ALT 17 U/L.
```

**flip** (program answer: s'; facts: patient: ALT = 10; present; past (2005) | patient: ALT = 47; present; current)
```
Female patient of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Teeth in good repair.
Sleeps seven hours a night.
Owns a bicycle.
Records from 2005 list ALT at 10 U/L.
Current ALT 47 U/L.
```

**near** (program answer: s; facts: patient: ALT = 201; present; past (2005) | patient: ALT = 17; present; current)
```
Female patient of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Teeth in good repair.
Sleeps seven hours a night.
Owns a bicycle.
Records from 2005 list ALT at 201 U/L.
Current ALT 17 U/L.
```

**pres** (program answer: s; facts: patient: ALT = 10; present; past (2005) | patient: ALT = 17; present; current)
```
Woman of 44 years.
Newly diagnosed rheumatoid arthritis with swollen, tender wrists and finger joints for three months.
Owns a bicycle.
Back in 2005, ALT stood at 10 U/L.
ALT now 17 U/L.
Sleeps seven hours a night.
Teeth in good repair.
```


## author3 / group 243: `rule_v1.test.gs056.c2.negation.easy.1332`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 2 points if the patient has ever had a venous thromboembolism (current or past); 3 points if the patient has ever had coronary artery disease (current or past); 1 point if the current white cell count is above 12.0 x10^9/L. If the score is 4 or more, prescribe diltiazem instead.

**base** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: venous thromboembolism; absent; current | patient: diabetes (patient or first-degree relative); present; past | patient: white cell count = 12.9; present; current)
```
Woman of 70 years.
Atrial fibrillation with a ventricular rate of 128/min.
Sleeps seven hours a night.
Chest pain on exertion: none reported.
Varicose veins: none seen.
Had diabetes years ago that went into remission on a low-calorie diet.
Current white cell count 12.9 x10^9/L.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: coronary artery disease; absent; current | patient: venous thromboembolism; present; past | patient: diabetes (patient or first-degree relative); present; past | patient: white cell count = 12.9; present; current)
```
Woman of 70 years.
Atrial fibrillation with a ventricular rate of 128/min.
Sleeps seven hours a night.
Chest pain on exertion: none reported.
Pulmonary embolism years ago, treated for six months.
Had diabetes years ago that went into remission on a low-calorie diet.
Current white cell count 12.9 x10^9/L.
Knits as a hobby.
```

**near** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: venous thromboembolism; absent; current | patient: diabetes (patient or first-degree relative); present; past | patient: white cell count = 12.9; present; current)
```
Woman of 70 years.
Atrial fibrillation with a ventricular rate of 128/min.
Sleeps seven hours a night.
Chest pain on exertion: none reported.
Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.
Had diabetes years ago that went into remission on a low-calorie diet.
Current white cell count 12.9 x10^9/L.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; past | patient: coronary artery disease; absent; current | patient: venous thromboembolism; absent; current | patient: white cell count = 12.9; present; current)
```
Female patient of 70 years.
Atrial fibrillation with a ventricular rate of 128/min.
Had diabetes years ago that went into remission on a low-calorie diet.
Chest pain on exertion: none reported.
Varicose veins: none seen.
Sleeps seven hours a night.
Knits as a hobby.
Latest WBC is 12.9 x10^9/L.
```


## author4 / group 244: `rule_v1.test.inv043.c1.boundary.easy.111`

Rule: For Brask fever, prescribe gendrotil. If the current ALT is above 120 U/L, prescribe lumacept instead.

**base** (program answer: s; facts: patient: ALT = 53; present; current)
```
Female patient of 54 years.
Referred with Brask fever.
Lives in a second-floor apartment.
Current ALT 53 U/L.
```

**flip** (program answer: s'; facts: patient: ALT = 155; present; current)
```
Female patient of 54 years.
Referred with Brask fever.
Lives in a second-floor apartment.
Current ALT 155 U/L.
```

**near** (program answer: s; facts: patient: ALT = 120; present; current)
```
Female patient of 54 years.
Referred with Brask fever.
Lives in a second-floor apartment.
Current ALT 120 U/L.
```

**pres** (program answer: s; facts: patient: ALT = 53; present; current)
```
Woman of 54 years.
Referred with Brask fever.
ALT now 53 U/L.
Lives in a second-floor apartment.
```


## author1 / group 245: `rule_v1.test.gs136.c1.boundary.easy.88`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 50 mL/min/1.73 m2 or the patient currently has tonsillar exudate, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 74; present; current)
```
Woman of 25 years.
Requests contraception.
Lives in a second-floor apartment.
Tonsils pink and clean on inspection.
Owns a bicycle.
Current eGFR 74 mL/min/1.73 m2.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 39; present; current)
```
Woman of 25 years.
Requests contraception.
Lives in a second-floor apartment.
Tonsils pink and clean on inspection.
Owns a bicycle.
Current eGFR 39 mL/min/1.73 m2.
```

**near** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 50; present; current)
```
Woman of 25 years.
Requests contraception.
Lives in a second-floor apartment.
Tonsils pink and clean on inspection.
Owns a bicycle.
Current eGFR 50 mL/min/1.73 m2.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 74; present; current)
```
Female patient of 25 years.
Requests contraception.
Owns a bicycle.
Lives in a second-floor apartment.
Tonsils pink and clean on inspection.
eGFR now 74 mL/min/1.73 m2.
```


## author2 / group 246: `rule_v1.test.gs002.c1.time.long.259`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: heart rate = 77; present; current | patient: heart rate = 76; present; past (2016) | patient: serum potassium = 3.9; present; current)
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

**flip** (program answer: s'; facts: patient: heart rate = 103; present; current | patient: heart rate = 76; present; past (2016) | patient: serum potassium = 3.9; present; current)
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

**near** (program answer: s; facts: patient: heart rate = 77; present; current | patient: heart rate = 98; present; past (2016) | patient: serum potassium = 3.9; present; current)
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

**pres** (program answer: s; facts: patient: heart rate = 77; present; current | patient: serum potassium = 3.9; present; current | patient: heart rate = 76; present; past (2016))
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


## author3 / group 247: `rule_v1.test.qsofa.mentation.subject.long.447`

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**base** (program answer: s; facts: patient: systolic blood pressure = 139; present; current | patient: respiratory rate = 15; present; current | patient: altered mentation; absent; current)
```
Male patient of 64 years.
Suspected urinary sepsis, assessed in the emergency department.
Has two cats.
His friend has recovered from a dislocated finger.
Paints watercolors as a hobby.
His roommate lives with psoriasis.
Owns a bicycle.
His friend burned a hand on a stove years ago.
Observations now: blood pressure 139/91 mmHg.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
In 2023, lipase was 30 U/L.
Photographs local wildlife.
Current respiratory rate 15/min.
Sees a dentist yearly.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
Plays the piano.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2017.
Gives a clear account of the illness.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 139; present; current | patient: respiratory rate = 15; present; current | patient: altered mentation; present; current)
```
Male patient of 64 years.
Suspected urinary sepsis, assessed in the emergency department.
Has two cats.
His friend has recovered from a dislocated finger.
Paints watercolors as a hobby.
His roommate lives with psoriasis.
Owns a bicycle.
His friend burned a hand on a stove years ago.
Observations now: blood pressure 139/91 mmHg.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
In 2023, lipase was 30 U/L.
Photographs local wildlife.
Current respiratory rate 15/min.
Sees a dentist yearly.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
Plays the piano.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2017.
Disoriented to time and place, which is new for the patient.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 139; present; current | patient: respiratory rate = 15; present; current | father: altered mentation; present; current)
```
Male patient of 64 years.
Suspected urinary sepsis, assessed in the emergency department.
Has two cats.
His friend has recovered from a dislocated finger.
Paints watercolors as a hobby.
His roommate lives with psoriasis.
Owns a bicycle.
His friend burned a hand on a stove years ago.
Observations now: blood pressure 139/91 mmHg.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
In 2023, lipase was 30 U/L.
Photographs local wildlife.
Current respiratory rate 15/min.
Sees a dentist yearly.
Teeth in good repair.
Enjoys board games.
Lives in a second-floor apartment.
Plays the piano.
Pupils equal and reactive to light.
Zinc of 85 mcg/dL in 2017.
His father is newly disoriented.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: altered mentation; absent; current | patient: systolic blood pressure = 139; present; current | patient: respiratory rate = 15; present; current)
```
Man of 64 years.
Suspected urinary sepsis, assessed in the emergency department.
Gives a clear account of the illness.
Paints watercolors as a hobby.
Current systolic blood pressure 139 mmHg.
Sleeps seven hours a night.
Observations now: respiratory rate 15/min.
Prefers morning appointments.
Zinc of 85 mcg/dL in 2017.
His friend sprained a thumb last month.
Lives in a second-floor apartment.
Has two cats.
Photographs local wildlife.
Teeth in good repair.
In 2023, lipase was 30 U/L.
Sees a dentist yearly.
Plays the piano.
His roommate lives with psoriasis.
Knits as a hobby.
Enjoys board games.
Pupils equal and reactive to light.
His friend burned a hand on a stove years ago.
Owns a bicycle.
His friend has recovered from a dislocated finger.
```


## author4 / group 248: `rule_v1.test.gs155.c2.numeric.long.983`

Rule: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had a peptic ulcer (current or past); the current serum potassium is above 5.0 mmol/L; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.

**base** (program answer: s; facts: patient: serum potassium = 3.9; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: peptic ulcer at any time; present; current)
```
Female patient of 61 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Pupils equal and reactive to light.
Drives a car.
Her roommate sprained a thumb last month.
Her father has a lazy eye.
Paints watercolors as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
In 2018, folate was 12 ng/mL.
Her uncle lives with psoriasis.
Teeth in good repair.
Current serum potassium 3.9 mmol/L.
Coagulation tests normal on recent bloodwork.
Has an active duodenal ulcer.
During a checkup in 2018, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2020.
Has two cats.
Prefers morning appointments.
Sees a dentist yearly.
Plays the piano.
Owns a bicycle.
Knits as a hobby.
Her uncle wears contact lenses.
```

**flip** (program answer: s'; facts: patient: serum potassium = 5.5; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: peptic ulcer at any time; present; current)
```
Female patient of 61 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Pupils equal and reactive to light.
Drives a car.
Her roommate sprained a thumb last month.
Her father has a lazy eye.
Paints watercolors as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
In 2018, folate was 12 ng/mL.
Her uncle lives with psoriasis.
Teeth in good repair.
Current serum potassium 5.5 mmol/L.
Coagulation tests normal on recent bloodwork.
Has an active duodenal ulcer.
During a checkup in 2018, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2020.
Has two cats.
Prefers morning appointments.
Sees a dentist yearly.
Plays the piano.
Owns a bicycle.
Knits as a hobby.
Her uncle wears contact lenses.
```

**near** (program answer: s; facts: patient: serum potassium = 4.8; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: peptic ulcer at any time; present; current)
```
Female patient of 61 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Pupils equal and reactive to light.
Drives a car.
Her roommate sprained a thumb last month.
Her father has a lazy eye.
Paints watercolors as a hobby.
Photographs local wildlife.
Prefers to be addressed by first name.
In 2018, folate was 12 ng/mL.
Her uncle lives with psoriasis.
Teeth in good repair.
Current serum potassium 4.8 mmol/L.
Coagulation tests normal on recent bloodwork.
Has an active duodenal ulcer.
During a checkup in 2018, total protein was 7.0 g/dL.
Free T4 of 1.2 ng/dL in 2020.
Has two cats.
Prefers morning appointments.
Sees a dentist yearly.
Plays the piano.
Owns a bicycle.
Knits as a hobby.
Her uncle wears contact lenses.
```

**pres** (program answer: s; facts: patient: serum potassium = 3.9; present; current | patient: peptic ulcer at any time; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current)
```
Woman of 61 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Free T4 of 1.2 ng/dL in 2020.
Her roommate sprained a thumb last month.
Prefers morning appointments.
Pupils equal and reactive to light.
Owns a bicycle.
Plays the piano.
Drives a car.
Prefers to be addressed by first name.
During a checkup in 2018, total protein was 7.0 g/dL.
Latest potassium result: 3.9 mmol/L.
Her uncle wears contact lenses.
In 2018, folate was 12 ng/mL.
Has an active duodenal ulcer.
Photographs local wildlife.
Her uncle lives with psoriasis.
Teeth in good repair.
Has two cats.
Sees a dentist yearly.
Knits as a hobby.
Paints watercolors as a hobby.
Coagulation tests normal on recent bloodwork.
Her father has a lazy eye.
```


## author1 / group 249: `rule_v1.test.gs044.c2.negation.easy.1540`

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

**base** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: age = 67; present; current)
```
An adult woman.
Suspected chest infection; assessed on the medical ward.
Abdomen soft and non-tender.
Prefers morning appointments.
Current age 67 years.
Paints watercolors as a hobby.
Has two cats.
```

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; past | patient: age = 67; present; current)
```
An adult woman.
Suspected chest infection; assessed on the medical ward.
Duodenal ulcer years ago; recovered fully with treatment.
Prefers morning appointments.
Current age 67 years.
Paints watercolors as a hobby.
Has two cats.
```

**near** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: age = 67; present; current)
```
An adult woman.
Suspected chest infection; assessed on the medical ward.
Has never had a peptic ulcer.
Prefers morning appointments.
Current age 67 years.
Paints watercolors as a hobby.
Has two cats.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: age = 67; present; current)
```
Woman, adult.
Suspected chest infection; assessed on the medical ward.
Has two cats.
Abdomen soft and non-tender.
Prefers morning appointments.
Paints watercolors as a hobby.
Currently aged 67 years.
```


## author2 / group 250: `rule_v1.test.gs035.c3.negation.long.351`

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).

**base** (program answer: s; facts: patient: cancer at any time; absent; current | patient: age = 78; present; current)
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

**flip** (program answer: s'; facts: patient: cancer at any time; present; current | patient: age = 78; present; current)
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

**near** (program answer: s; facts: patient: cancer at any time; absent; current | patient: age = 78; present; current)
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

**pres** (program answer: s; facts: patient: age = 78; present; current | patient: cancer at any time; absent; current)
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

**missing** (program answer: neither; facts: patient: cancer at any time; unknown; current | patient: age = 78; present; current)
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


## author3 / group 251: `rule_v1.test.inv039.c1.subject.easy.337`

Rule: For Pallis disease, prescribe brexadol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 2 points if the current ALT is above 120 U/L; 3 points if the current eGFR is below 30 mL/min/1.73 m2. If the score is 4 or more, prescribe corlitane instead.

**base** (program answer: s; facts: patient: eGFR = 20; present; current | patient: ALT = 12; present; current)
```
Female patient of 46 years.
Referred with Pallis disease.
eGFR now 20 mL/min/1.73 m2.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Uses sunscreen in summer.
Current ALT 12 U/L.
Enjoys board games.
```

**flip** (program answer: s'; facts: patient: eGFR = 20; present; current | father: venous thromboembolism (patient or first-degree relative); present; past (2013) | patient: ALT = 12; present; current)
```
Female patient of 46 years.
Referred with Pallis disease.
eGFR now 20 mL/min/1.73 m2.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her father recovered from a pulmonary embolism in 2013.
Uses sunscreen in summer.
Current ALT 12 U/L.
Enjoys board games.
```

**near** (program answer: s; facts: patient: eGFR = 20; present; current | uncle: venous thromboembolism (patient or first-degree relative); present; past | patient: ALT = 12; present; current)
```
Female patient of 46 years.
Referred with Pallis disease.
eGFR now 20 mL/min/1.73 m2.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Her uncle had a DVT years ago.
Uses sunscreen in summer.
Current ALT 12 U/L.
Enjoys board games.
```

**pres** (program answer: s; facts: patient: ALT = 12; present; current | patient: eGFR = 20; present; current)
```
Woman of 46 years.
Referred with Pallis disease.
Prefers to be addressed by first name.
Uses sunscreen in summer.
ALT now 12 U/L.
Enjoys board games.
Current eGFR 20 mL/min/1.73 m2.
Sleeps seven hours a night.
```


## author4 / group 252: `rule_v1.test.hf_spironolactone.k.time.alt.65`

Rule: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 4.5 mmol/L, add dapagliflozin instead.

**base** (program answer: s; facts: patient: potassium = 3.7; present; current | patient: potassium = 3.6; present; past (2006))
```
Female patient of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Pupils equal and reactive to light.
Current serum potassium 3.7 mmol/L.
Drives a car.
Teeth in good repair.
Records from 2006 list serum potassium at 3.6 mmol/L.
```

**flip** (program answer: s'; facts: patient: potassium = 4.7; present; current | patient: potassium = 3.6; present; past (2006))
```
Female patient of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Pupils equal and reactive to light.
Current serum potassium 4.7 mmol/L.
Drives a car.
Teeth in good repair.
Records from 2006 list serum potassium at 3.6 mmol/L.
```

**near** (program answer: s; facts: patient: potassium = 3.7; present; current | patient: potassium = 5.2; present; past (2006))
```
Female patient of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Pupils equal and reactive to light.
Current serum potassium 3.7 mmol/L.
Drives a car.
Teeth in good repair.
Records from 2006 list serum potassium at 5.2 mmol/L.
```

**pres** (program answer: s; facts: patient: potassium = 3.6; present; past (2006) | patient: potassium = 3.7; present; current)
```
Woman of 52 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Teeth in good repair.
Back in 2006, serum potassium stood at 3.6 mmol/L.
Latest potassium result: 3.7 mmol/L.
Pupils equal and reactive to light.
Drives a car.
```


## author1 / group 253: `rule_v1.test.gs087.c2.subject.long.860`

Rule: For knee osteoarthritis pain, prescribe naproxen. Score 2 points if the patient is allergic to penicillin; 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 3 points if the current heart rate is above 90/min. If the score is 6 or more, prescribe acetaminophen instead.

**base** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 98; present; current)
```
Woman of 58 years.
Knee osteoarthritis with pain on walking.
Known penicillin allergy with angioedema.
Free T4 of 1.2 ng/dL in 2019.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Photographs local wildlife.
In 2008, lipase was 30 U/L.
Enjoys board games.
Lives in a second-floor apartment.
Prefers morning appointments.
Her sister lives with psoriasis.
Teeth in good repair.
Heart rate now 98/min on a pulse check.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Drives a car.
Owns a bicycle.
Plays the piano.
Her friend sprained a thumb last month.
Sees a dentist yearly.
Her wife has recovered from a dislocated finger.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**flip** (program answer: s'; facts: patient: penicillin allergy; present; current | father: venous thromboembolism (patient or first-degree relative); present; current | patient: heart rate = 98; present; current)
```
Woman of 58 years.
Knee osteoarthritis with pain on walking.
Known penicillin allergy with angioedema.
Free T4 of 1.2 ng/dL in 2019.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Photographs local wildlife.
In 2008, lipase was 30 U/L.
Enjoys board games.
Lives in a second-floor apartment.
Her father is being treated for a pulmonary embolism.
Prefers morning appointments.
Her sister lives with psoriasis.
Teeth in good repair.
Heart rate now 98/min on a pulse check.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Drives a car.
Owns a bicycle.
Plays the piano.
Her friend sprained a thumb last month.
Sees a dentist yearly.
Her wife has recovered from a dislocated finger.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**near** (program answer: s; facts: patient: penicillin allergy; present; current | friend: venous thromboembolism (patient or first-degree relative); present; current | patient: heart rate = 98; present; current)
```
Woman of 58 years.
Knee osteoarthritis with pain on walking.
Known penicillin allergy with angioedema.
Free T4 of 1.2 ng/dL in 2019.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Photographs local wildlife.
In 2008, lipase was 30 U/L.
Enjoys board games.
Lives in a second-floor apartment.
Her friend is being treated for a pulmonary embolism.
Prefers morning appointments.
Her sister lives with psoriasis.
Teeth in good repair.
Heart rate now 98/min on a pulse check.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Drives a car.
Owns a bicycle.
Plays the piano.
Her friend sprained a thumb last month.
Sees a dentist yearly.
Her wife has recovered from a dislocated finger.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**pres** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 98; present; current)
```
Female patient of 58 years.
Knee osteoarthritis with pain on walking.
Teeth in good repair.
Free T4 of 1.2 ng/dL in 2019.
Her friend sprained a thumb last month.
Her wife has recovered from a dislocated finger.
Lives in a second-floor apartment.
Enjoys board games.
In 2008, lipase was 30 U/L.
Her sister lives with psoriasis.
Photographs local wildlife.
Plays the piano.
Her friend burned a hand on a stove years ago.
Sees a dentist yearly.
Owns a bicycle.
Knits as a hobby.
Known penicillin allergy with angioedema.
Prefers morning appointments.
Current heart rate 98/min.
Drives a car.
During a checkup in 2009, free T3 was 3.2 pg/mL.
During a checkup in 2011, total protein was 7.0 g/dL.
```

**missing** (program answer: neither; facts: patient: penicillin allergy; present; current | patient: venous thromboembolism (patient or first-degree relative); unknown; current | patient: heart rate = 98; present; current)
```
Woman of 58 years.
Knee osteoarthritis with pain on walking.
Known penicillin allergy with angioedema.
Free T4 of 1.2 ng/dL in 2019.
Knits as a hobby.
Her friend burned a hand on a stove years ago.
Photographs local wildlife.
In 2008, lipase was 30 U/L.
Enjoys board games.
Lives in a second-floor apartment.
Venous thromboembolism (patient or first-degree relative): unknown.
Prefers morning appointments.
Her sister lives with psoriasis.
Teeth in good repair.
Heart rate now 98/min on a pulse check.
During a checkup in 2009, free T3 was 3.2 pg/mL.
Drives a car.
Owns a bicycle.
Plays the piano.
Her friend sprained a thumb last month.
Sees a dentist yearly.
Her wife has recovered from a dislocated finger.
During a checkup in 2011, total protein was 7.0 g/dL.
```


## author2 / group 254: `rule_v1.test.c2_t2d_hf.hf.negation.easy.466`

Rule: For type 2 diabetes above target on metformin, prescribe pioglitazone. If the patient has ever had heart failure (current or past), prescribe empagliflozin instead.

**base** (program answer: s; facts: patient: heart failure; absent; current)
```
Male patient of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Drives a car.
Uses sunscreen in summer.
Has two cats.
Sleeps flat on one pillow.
```

**flip** (program answer: s'; facts: patient: heart failure; present; current)
```
Male patient of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Drives a car.
Uses sunscreen in summer.
Has two cats.
Has heart failure, treated with diuretics.
```

**near** (program answer: s; facts: patient: heart failure; absent; current)
```
Male patient of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Drives a car.
Uses sunscreen in summer.
Has two cats.
Has never had heart failure.
```

**pres** (program answer: s; facts: patient: heart failure; absent; current)
```
Man of 47 years.
Type 2 diabetes above target despite metformin (HbA1c 8.4%).
Pupils equal and reactive to light.
Sleeps flat on one pillow.
Has two cats.
Drives a car.
Uses sunscreen in summer.
```


## author3 / group 255: `rule_v1.test.s3_childpugh.ascites.negation.easy.1791`

Rule: Child-Pugh score (as used here, partial; each finding below adds 1 point, whatever its grade): 1 point each for a current international normalized ratio (INR) of 1.7 or more; current ascites; new confusion (encephalopathy). Bilirubin, albumin and other items are not part of this question.

**base** (program answer: s; facts: patient: international normalized ratio = 1.1; present; current | patient: new confusion; absent; current | patient: ascites; absent; current)
```
Woman of 54 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Latest international normalized ratio (INR): 1.1.
Speech clear; follows commands.
Knits as a hobby.
Pupils equal and reactive to light.
Abdomen soft, without distension or fluid.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: international normalized ratio = 1.1; present; current | patient: new confusion; absent; current | patient: ascites; present; current)
```
Woman of 54 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Latest international normalized ratio (INR): 1.1.
Speech clear; follows commands.
Knits as a hobby.
Pupils equal and reactive to light.
Mild ascites seen on the current ultrasound scan.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: international normalized ratio = 1.1; present; current | patient: new confusion; absent; current | patient: ascites; absent; current)
```
Woman of 54 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Latest international normalized ratio (INR): 1.1.
Speech clear; follows commands.
Knits as a hobby.
Pupils equal and reactive to light.
Ultrasound negative for ascites at this visit.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: new confusion; absent; current | patient: ascites; absent; current | patient: international normalized ratio = 1.1; present; current)
```
Female patient of 54 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Knits as a hobby.
Speech clear; follows commands.
Abdomen soft, without distension or fluid.
Current international normalized ratio 1.1.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
```


## author4 / group 256: `rule_v1.test.gs139.c2.subject.long.188`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the patient currently has tender anterior cervical lymph nodes and the patient has ever had angioedema (current or past), prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: angioedema; absent; current | patient: tender cervical lymph nodes; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Free of facial or oropharyngeal edema.
Owns a bicycle.
Enjoys board games.
Uses sunscreen in summer.
Her wife burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Her uncle lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Anterior cervical lymph nodes enlarged and tender to touch.
Her sister sprained a thumb last month.
Knits as a hobby.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2019, total protein was 7.0 g/dL.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: angioedema; present; past | patient: tender cervical lymph nodes; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
An episode of angioedema years ago, with full recovery.
Owns a bicycle.
Enjoys board games.
Uses sunscreen in summer.
Her wife burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Her uncle lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Anterior cervical lymph nodes enlarged and tender to touch.
Her sister sprained a thumb last month.
Knits as a hobby.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2019, total protein was 7.0 g/dL.
Sees a dentist yearly.
```

**near** (program answer: s; facts: wife: angioedema; present; past (2010) | patient: tender cervical lymph nodes; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Her wife recovered from an episode of angioedema in 2010.
Owns a bicycle.
Enjoys board games.
Uses sunscreen in summer.
Her wife burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Her uncle lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Anterior cervical lymph nodes enlarged and tender to touch.
Her sister sprained a thumb last month.
Knits as a hobby.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2019, total protein was 7.0 g/dL.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: patient: angioedema; absent; current | patient: tender cervical lymph nodes; present; current)
```
Woman of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Enjoys board games.
Pupils equal and reactive to light.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Has two cats.
Her uncle lives with psoriasis.
Knits as a hobby.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Owns a bicycle.
Her wife burned a hand on a stove years ago.
Prefers morning appointments.
Free of facial or oropharyngeal edema.
Her wife has a lazy eye.
Sleeps seven hours a night.
Anterior cervical lymph nodes enlarged and tender to touch.
Sees a dentist yearly.
During a checkup in 2019, total protein was 7.0 g/dL.
Her sister sprained a thumb last month.
```

**missing** (program answer: neither; facts: patient: angioedema; unknown; current | patient: tender cervical lymph nodes; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Angioedema: status unclear from the records at hand.
Owns a bicycle.
Enjoys board games.
Uses sunscreen in summer.
Her wife burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2012, free T3 was 3.2 pg/mL.
Her uncle lives with psoriasis.
Has two cats.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Anterior cervical lymph nodes enlarged and tender to touch.
Her sister sprained a thumb last month.
Knits as a hobby.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Prefers morning appointments.
During a checkup in 2019, total protein was 7.0 g/dL.
Sees a dentist yearly.
```


## author1 / group 257: `rule_v1.test.gs117.c2.boundary.long.329`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If the patient has new confusion and the current eGFR is below 45 mL/min/1.73 m2, prescribe intermittent pneumatic compression instead.

**base** (program answer: s; facts: patient: eGFR = 69; present; current | patient: new confusion; present; current)
```
Woman of 57 years.
Admitted for community-acquired pneumonia; immobile.
Her sister wears contact lenses.
Sleeps seven hours a night.
Her friend has recovered from a dislocated finger.
Prefers morning appointments.
During a checkup in 2016, total protein was 7.0 g/dL.
In 2023, lipase was 30 U/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Her wife has a lazy eye.
Drives a car.
Current eGFR 69 mL/min/1.73 m2.
Enjoys board games.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Knits as a hobby.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
Sees a dentist yearly.
Newly disoriented and unable to give a clear history.
Paints watercolors as a hobby.
```

**flip** (program answer: s'; facts: patient: eGFR = 38; present; current | patient: new confusion; present; current)
```
Woman of 57 years.
Admitted for community-acquired pneumonia; immobile.
Her sister wears contact lenses.
Sleeps seven hours a night.
Her friend has recovered from a dislocated finger.
Prefers morning appointments.
During a checkup in 2016, total protein was 7.0 g/dL.
In 2023, lipase was 30 U/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Her wife has a lazy eye.
Drives a car.
Current eGFR 38 mL/min/1.73 m2.
Enjoys board games.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Knits as a hobby.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
Sees a dentist yearly.
Newly disoriented and unable to give a clear history.
Paints watercolors as a hobby.
```

**near** (program answer: s; facts: patient: eGFR = 45; present; current | patient: new confusion; present; current)
```
Woman of 57 years.
Admitted for community-acquired pneumonia; immobile.
Her sister wears contact lenses.
Sleeps seven hours a night.
Her friend has recovered from a dislocated finger.
Prefers morning appointments.
During a checkup in 2016, total protein was 7.0 g/dL.
In 2023, lipase was 30 U/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Her wife has a lazy eye.
Drives a car.
Current eGFR 45 mL/min/1.73 m2.
Enjoys board games.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Knits as a hobby.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
Sees a dentist yearly.
Newly disoriented and unable to give a clear history.
Paints watercolors as a hobby.
```

**pres** (program answer: s; facts: patient: new confusion; present; current | patient: eGFR = 69; present; current)
```
Female patient of 57 years.
Admitted for community-acquired pneumonia; immobile.
Newly disoriented and unable to give a clear history.
Drives a car.
In 2023, lipase was 30 U/L.
Sleeps seven hours a night.
Sees a dentist yearly.
Owns a bicycle.
Her sister wears contact lenses.
Uses sunscreen in summer.
During a checkup in 2016, total protein was 7.0 g/dL.
Her wife has a lazy eye.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Knits as a hobby.
Prefers to be addressed by first name.
Prefers morning appointments.
Her friend has recovered from a dislocated finger.
Photographs local wildlife.
eGFR now 69 mL/min/1.73 m2.
Enjoys board games.
Pupils equal and reactive to light.
During a checkup in 2014, free T3 was 3.2 pg/mL.
```


## author2 / group 258: `rule_v1.test.gs135.c2.boundary.long.926`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the patient is allergic to penicillin and the current heart rate is above 90/min, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 80; present; current)
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

**flip** (program answer: s'; facts: patient: penicillin allergy; present; current | patient: heart rate = 104; present; current)
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

**near** (program answer: s; facts: patient: penicillin allergy; present; current | patient: heart rate = 90; present; current)
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

**pres** (program answer: s; facts: patient: heart rate = 80; present; current | patient: penicillin allergy; present; current)
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


## author3 / group 259: `rule_v1.test.s3_childpugh.enceph.negation.easy.382`

Rule: Child-Pugh score (as used here, partial; each finding below adds 1 point, whatever its grade): 1 point each for a current international normalized ratio (INR) of 1.7 or more; current ascites; new confusion (encephalopathy). Bilirubin, albumin and other items are not part of this question.

**base** (program answer: s; facts: patient: international normalized ratio = 1.0; present; current | patient: ascites; absent; current)
```
Male patient of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Pupils equal and reactive to light.
Teeth in good repair.
Sees a dentist yearly.
Current international normalized ratio 1.0.
Abdomen soft, without distension or fluid.
```

**flip** (program answer: s'; facts: patient: international normalized ratio = 1.0; present; current | patient: new confusion; present; current | patient: ascites; absent; current)
```
Male patient of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Pupils equal and reactive to light.
Teeth in good repair.
Sees a dentist yearly.
Current international normalized ratio 1.0.
Disoriented to time and place, which is new for the patient.
Abdomen soft, without distension or fluid.
```

**near** (program answer: s; facts: patient: international normalized ratio = 1.0; present; current | patient: new confusion; absent; current | patient: ascites; absent; current)
```
Male patient of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Pupils equal and reactive to light.
Teeth in good repair.
Sees a dentist yearly.
Current international normalized ratio 1.0.
Confusion absent; answers questions appropriately.
Abdomen soft, without distension or fluid.
```

**pres** (program answer: s; facts: patient: international normalized ratio = 1.0; present; current | patient: ascites; absent; current)
```
Man of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Latest international normalized ratio (INR): 1.0.
Sees a dentist yearly.
Pupils equal and reactive to light.
Abdomen soft, without distension or fluid.
Teeth in good repair.
```

**missing** (program answer: neither; facts: patient: international normalized ratio = 1.0; present; current | patient: new confusion; unknown; current | patient: ascites; absent; current)
```
Male patient of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Pupils equal and reactive to light.
Teeth in good repair.
Sees a dentist yearly.
Current international normalized ratio 1.0.
New confusion: status unclear from the records at hand.
Abdomen soft, without distension or fluid.
```


## author4 / group 260: `rule_v1.test.gs002.c1.numeric.easy.1400`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: serum potassium = 4.5; present; current | patient: heart rate = 65; present; current)
```
Female patient of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Current serum potassium 4.5 mmol/L.
Current heart rate 65/min.
Has two cats.
```

**flip** (program answer: s'; facts: patient: serum potassium = 4.5; present; current | patient: heart rate = 103; present; current)
```
Female patient of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Current serum potassium 4.5 mmol/L.
Current heart rate 103/min.
Has two cats.
```

**near** (program answer: s; facts: patient: serum potassium = 4.5; present; current | patient: heart rate = 88; present; current)
```
Female patient of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Current serum potassium 4.5 mmol/L.
Current heart rate 88/min.
Has two cats.
```

**pres** (program answer: s; facts: patient: serum potassium = 4.5; present; current | patient: heart rate = 65; present; current)
```
Woman of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Latest potassium result: 4.5 mmol/L.
Has two cats.
Heart rate now 65/min on a pulse check.
```


## author1 / group 261: `rule_v1.test.gs048.c2.numeric.long.814`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: age = 67; present; current | patient: weight = 87; present; current)
```
An adult woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
In 2013, lipase was 30 U/L.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
Her sister burned a hand on a stove years ago.
Drives a car.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2012.
Paints watercolors as a hobby.
Knits as a hobby.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Prefers morning appointments.
Pupils equal and reactive to light.
Her wife wears contact lenses.
Current age 67 years.
Has two cats.
Sleeps seven hours a night.
Her wife has recovered from a dislocated finger.
Latest weight 87 kg.
```

**flip** (program answer: s'; facts: patient: age = 84; present; current | patient: weight = 87; present; current)
```
An adult woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
In 2013, lipase was 30 U/L.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
Her sister burned a hand on a stove years ago.
Drives a car.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2012.
Paints watercolors as a hobby.
Knits as a hobby.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Prefers morning appointments.
Pupils equal and reactive to light.
Her wife wears contact lenses.
Current age 84 years.
Has two cats.
Sleeps seven hours a night.
Her wife has recovered from a dislocated finger.
Latest weight 87 kg.
```

**near** (program answer: s; facts: patient: age = 73; present; current | patient: weight = 87; present; current)
```
An adult woman.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
In 2013, lipase was 30 U/L.
Sees a dentist yearly.
Teeth in good repair.
Plays the piano.
Her sister burned a hand on a stove years ago.
Drives a car.
Owns a bicycle.
Free T4 of 1.2 ng/dL in 2012.
Paints watercolors as a hobby.
Knits as a hobby.
Her sister sprained a thumb last month.
Prefers to be addressed by first name.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Prefers morning appointments.
Pupils equal and reactive to light.
Her wife wears contact lenses.
Current age 73 years.
Has two cats.
Sleeps seven hours a night.
Her wife has recovered from a dislocated finger.
Latest weight 87 kg.
```

**pres** (program answer: s; facts: patient: age = 67; present; current | patient: weight = 87; present; current)
```
Woman, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Teeth in good repair.
Her wife has recovered from a dislocated finger.
Drives a car.
Currently aged 67 years.
Her wife wears contact lenses.
Her sister burned a hand on a stove years ago.
Prefers to be addressed by first name.
In 2013, lipase was 30 U/L.
Sleeps seven hours a night.
Owns a bicycle.
Current weight 87 kg.
Sees a dentist yearly.
Has two cats.
Her sister sprained a thumb last month.
Free T4 of 1.2 ng/dL in 2012.
Uses sunscreen in summer.
Plays the piano.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Knits as a hobby.
Lives in a second-floor apartment.
Prefers morning appointments.
```


## author2 / group 262: `rule_v1.test.gs048.c1.numeric.easy.1614`

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. If the current weight is 60 kg or less or the age of the patient is 75 years or more, prescribe dapagliflozin instead.

**base** (program answer: s; facts: patient: weight = 89; present; current | patient: age = 70; present; current)
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current weight 89 kg.
Plays the piano.
Lives in a second-floor apartment.
Currently aged 70 years.
```

**flip** (program answer: s'; facts: patient: weight = 60; present; current | patient: age = 70; present; current)
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current weight 60 kg.
Plays the piano.
Lives in a second-floor apartment.
Currently aged 70 years.
```

**near** (program answer: s; facts: patient: weight = 61; present; current | patient: age = 70; present; current)
```
Man, adult.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current weight 61 kg.
Plays the piano.
Lives in a second-floor apartment.
Currently aged 70 years.
```

**pres** (program answer: s; facts: patient: weight = 89; present; current | patient: age = 70; present; current)
```
An adult man.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Latest weight 89 kg.
Lives in a second-floor apartment.
Current age 70 years.
Plays the piano.
```


## author3 / group 263: `rule_v1.test.gs130.c1.subject.long.500`

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If at least two of the following apply, prescribe diltiazem instead: the patient currently has tender anterior cervical lymph nodes; the patient currently has a venous thromboembolism; the patient has ever had angioedema (current or past).

**base** (program answer: s; facts: patient: angioedema; present; current)
```
Man of 44 years.
Atrial fibrillation with a ventricular rate of 128/min.
Free T4 of 1.2 ng/dL in 2021.
Enjoys board games.
Lives with chronic angioedema that flares several times a year.
Teeth in good repair.
His father has a lazy eye.
Plays the piano.
Knits as a hobby.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Drives a car.
His roommate lives with psoriasis.
During a checkup in 2017, total protein was 7.0 g/dL.
Has two cats.
His roommate burned a hand on a stove years ago.
Lives in a second-floor apartment.
His sister sprained a thumb last month.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
In 2022, lipase was 30 U/L.
Owns a bicycle.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: angioedema; present; current | patient: tender cervical lymph nodes; present; current)
```
Man of 44 years.
Atrial fibrillation with a ventricular rate of 128/min.
Free T4 of 1.2 ng/dL in 2021.
Enjoys board games.
Lives with chronic angioedema that flares several times a year.
Teeth in good repair.
His father has a lazy eye.
Plays the piano.
Anterior cervical lymph nodes enlarged and tender to touch.
Knits as a hobby.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Drives a car.
His roommate lives with psoriasis.
During a checkup in 2017, total protein was 7.0 g/dL.
Has two cats.
His roommate burned a hand on a stove years ago.
Lives in a second-floor apartment.
His sister sprained a thumb last month.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
In 2022, lipase was 30 U/L.
Owns a bicycle.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: angioedema; present; current | roommate: tender cervical lymph nodes; present; current)
```
Man of 44 years.
Atrial fibrillation with a ventricular rate of 128/min.
Free T4 of 1.2 ng/dL in 2021.
Enjoys board games.
Lives with chronic angioedema that flares several times a year.
Teeth in good repair.
His father has a lazy eye.
Plays the piano.
His roommate currently has tender anterior cervical lymphadenopathy.
Knits as a hobby.
During a checkup in 2018, free T3 was 3.2 pg/mL.
Photographs local wildlife.
Drives a car.
His roommate lives with psoriasis.
During a checkup in 2017, total protein was 7.0 g/dL.
Has two cats.
His roommate burned a hand on a stove years ago.
Lives in a second-floor apartment.
His sister sprained a thumb last month.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
In 2022, lipase was 30 U/L.
Owns a bicycle.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: angioedema; present; current)
```
Male patient of 44 years.
Atrial fibrillation with a ventricular rate of 128/min.
His sister sprained a thumb last month.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Owns a bicycle.
Plays the piano.
In 2022, lipase was 30 U/L.
Drives a car.
Lives with chronic angioedema that flares several times a year.
During a checkup in 2017, total protein was 7.0 g/dL.
Photographs local wildlife.
His roommate burned a hand on a stove years ago.
Teeth in good repair.
His roommate lives with psoriasis.
His father has a lazy eye.
Paints watercolors as a hobby.
Knits as a hobby.
Has two cats.
Enjoys board games.
Sleeps seven hours a night.
Free T4 of 1.2 ng/dL in 2021.
During a checkup in 2018, free T3 was 3.2 pg/mL.
```


## author4 / group 264: `rule_v1.test.gs014.c2.negation.long.481`

Rule: For primary prevention, prescribe atorvastatin. If the current serum creatinine is above 2.0 mg/dL or the patient has ever had a peptic ulcer (current or past), prescribe ezetimibe instead.

**base** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: serum creatinine = 0.6; present; current)
```
Female patient of 45 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Abdomen soft and non-tender.
Owns a bicycle.
Her roommate lives with psoriasis.
Drives a car.
Has two cats.
Free T4 of 1.2 ng/dL in 2014.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Her uncle has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2019.
Plays the piano.
Knits as a hobby.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her uncle sprained a thumb last month.
Current serum creatinine 0.6 mg/dL.
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; current | patient: serum creatinine = 0.6; present; current)
```
Female patient of 45 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Active peptic ulcer disease.
Owns a bicycle.
Her roommate lives with psoriasis.
Drives a car.
Has two cats.
Free T4 of 1.2 ng/dL in 2014.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Her uncle has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2019.
Plays the piano.
Knits as a hobby.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her uncle sprained a thumb last month.
Current serum creatinine 0.6 mg/dL.
Teeth in good repair.
```

**near** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: serum creatinine = 0.6; present; current)
```
Female patient of 45 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Medical record negative for peptic ulcer, current or past.
Owns a bicycle.
Her roommate lives with psoriasis.
Drives a car.
Has two cats.
Free T4 of 1.2 ng/dL in 2014.
In 2009, lipase was 30 U/L.
Photographs local wildlife.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Lives in a second-floor apartment.
Her uncle has recovered from a dislocated finger.
Zinc of 85 mcg/dL in 2019.
Plays the piano.
Knits as a hobby.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her uncle sprained a thumb last month.
Current serum creatinine 0.6 mg/dL.
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: serum creatinine = 0.6; present; current)
```
Woman of 45 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Has two cats.
Photographs local wildlife.
Knits as a hobby.
In 2009, lipase was 30 U/L.
Owns a bicycle.
Sees a dentist yearly.
Pupils equal and reactive to light.
Plays the piano.
Lives in a second-floor apartment.
Zinc of 85 mcg/dL in 2019.
Free T4 of 1.2 ng/dL in 2014.
Abdomen soft and non-tender.
Latest creatinine result: 0.6 mg/dL.
Her uncle sprained a thumb last month.
Drives a car.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Her roommate lives with psoriasis.
Her uncle has recovered from a dislocated finger.
Teeth in good repair.
```


## author1 / group 265: `rule_v1.test.gs136.c1.numeric.long.386`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 50 mL/min/1.73 m2 or the patient currently has tonsillar exudate, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 90; present; current)
```
Woman of 24 years.
Requests contraception.
Paints watercolors as a hobby.
Prefers morning appointments.
Tonsils a little red, surfaces clear.
Her friend has a lazy eye.
During a checkup in 2023, free T3 was 3.2 pg/mL.
In 2020, folate was 12 ng/mL.
Owns a bicycle.
Her roommate burned a hand on a stove years ago.
Drives a car.
Plays the piano.
Her father has recovered from a dislocated finger.
Uses sunscreen in summer.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Her roommate wears contact lenses.
Current eGFR 90 mL/min/1.73 m2.
Enjoys board games.
Photographs local wildlife.
Teeth in good repair.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 49; present; current)
```
Woman of 24 years.
Requests contraception.
Paints watercolors as a hobby.
Prefers morning appointments.
Tonsils a little red, surfaces clear.
Her friend has a lazy eye.
During a checkup in 2023, free T3 was 3.2 pg/mL.
In 2020, folate was 12 ng/mL.
Owns a bicycle.
Her roommate burned a hand on a stove years ago.
Drives a car.
Plays the piano.
Her father has recovered from a dislocated finger.
Uses sunscreen in summer.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Her roommate wears contact lenses.
Current eGFR 49 mL/min/1.73 m2.
Enjoys board games.
Photographs local wildlife.
Teeth in good repair.
Sees a dentist yearly.
```

**near** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 53; present; current)
```
Woman of 24 years.
Requests contraception.
Paints watercolors as a hobby.
Prefers morning appointments.
Tonsils a little red, surfaces clear.
Her friend has a lazy eye.
During a checkup in 2023, free T3 was 3.2 pg/mL.
In 2020, folate was 12 ng/mL.
Owns a bicycle.
Her roommate burned a hand on a stove years ago.
Drives a car.
Plays the piano.
Her father has recovered from a dislocated finger.
Uses sunscreen in summer.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2024.
Her roommate wears contact lenses.
Current eGFR 53 mL/min/1.73 m2.
Enjoys board games.
Photographs local wildlife.
Teeth in good repair.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; absent; current | patient: eGFR = 90; present; current)
```
Female patient of 24 years.
Requests contraception.
Sleeps seven hours a night.
Drives a car.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2024.
Teeth in good repair.
Sees a dentist yearly.
Her roommate wears contact lenses.
Tonsils a little red, surfaces clear.
Prefers morning appointments.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Her father has recovered from a dislocated finger.
Enjoys board games.
Photographs local wildlife.
Owns a bicycle.
Plays the piano.
Her friend has a lazy eye.
In 2020, folate was 12 ng/mL.
Paints watercolors as a hobby.
Uses sunscreen in summer.
eGFR now 90 mL/min/1.73 m2.
Her roommate burned a hand on a stove years ago.
```


## author2 / group 266: `rule_v1.test.vte_platelets.plt.numeric.alt.653`

Rule: For inpatient VTE prophylaxis, use enoxaparin. If the current platelet count is below 100 x10^9/L, use intermittent pneumatic compression instead.

**base** (program answer: s; facts: patient: platelet count = 173; present; current)
```
Male patient of 42 years.
Admitted for community-acquired pneumonia; immobile.
Uses sunscreen in summer.
Current platelet count 173 x10^9/L.
```

**flip** (program answer: s'; facts: patient: platelet count = 58; present; current)
```
Male patient of 42 years.
Admitted for community-acquired pneumonia; immobile.
Uses sunscreen in summer.
Current platelet count 58 x10^9/L.
```

**near** (program answer: s; facts: patient: platelet count = 106; present; current)
```
Male patient of 42 years.
Admitted for community-acquired pneumonia; immobile.
Uses sunscreen in summer.
Current platelet count 106 x10^9/L.
```

**pres** (program answer: s; facts: patient: platelet count = 173; present; current)
```
Man of 42 years.
Admitted for community-acquired pneumonia; immobile.
Platelet count now 173 x10^9/L.
Uses sunscreen in summer.
```


## author3 / group 267: `rule_v1.test.gs086.c2.negation.long.439`

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).

**base** (program answer: s; facts: patient: heart failure; absent; current | patient: heart rate = 98; present; current | patient: venous thromboembolism; absent; current)
```
Woman of 62 years.
Admitted for community-acquired pneumonia; immobile.
Sleeps flat on one pillow.
Heart rate now 98/min on a pulse check.
Pupils equal and reactive to light.
During a checkup in 2007, total protein was 7.0 g/dL.
Her uncle wears contact lenses.
Prefers to be addressed by first name.
Prefers morning appointments.
Her sister sprained a thumb last month.
Sleeps seven hours a night.
In 2018, lipase was 30 U/L.
Varicose veins: none seen.
Teeth in good repair.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2021.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Her father has a lazy eye.
```

**flip** (program answer: s'; facts: patient: heart failure; present; current | patient: heart rate = 98; present; current | patient: venous thromboembolism; absent; current)
```
Woman of 62 years.
Admitted for community-acquired pneumonia; immobile.
Current heart failure with ankle swelling.
Heart rate now 98/min on a pulse check.
Pupils equal and reactive to light.
During a checkup in 2007, total protein was 7.0 g/dL.
Her uncle wears contact lenses.
Prefers to be addressed by first name.
Prefers morning appointments.
Her sister sprained a thumb last month.
Sleeps seven hours a night.
In 2018, lipase was 30 U/L.
Varicose veins: none seen.
Teeth in good repair.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2021.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Her father has a lazy eye.
```

**near** (program answer: s; facts: patient: heart failure; absent; current | patient: heart rate = 98; present; current | patient: venous thromboembolism; absent; current)
```
Woman of 62 years.
Admitted for community-acquired pneumonia; immobile.
Heart failure: never diagnosed.
Heart rate now 98/min on a pulse check.
Pupils equal and reactive to light.
During a checkup in 2007, total protein was 7.0 g/dL.
Her uncle wears contact lenses.
Prefers to be addressed by first name.
Prefers morning appointments.
Her sister sprained a thumb last month.
Sleeps seven hours a night.
In 2018, lipase was 30 U/L.
Varicose veins: none seen.
Teeth in good repair.
Uses sunscreen in summer.
Free T4 of 1.2 ng/dL in 2021.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
Owns a bicycle.
Her father has a lazy eye.
```

**pres** (program answer: s; facts: patient: heart rate = 98; present; current | patient: venous thromboembolism; absent; current | patient: heart failure; absent; current)
```
Female patient of 62 years.
Admitted for community-acquired pneumonia; immobile.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Uses sunscreen in summer.
Her uncle wears contact lenses.
In 2018, lipase was 30 U/L.
Current heart rate 98/min.
Free T4 of 1.2 ng/dL in 2021.
Her sister sprained a thumb last month.
Her father has a lazy eye.
Prefers morning appointments.
Teeth in good repair.
Varicose veins: none seen.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
Sleeps flat on one pillow.
Sleeps seven hours a night.
During a checkup in 2007, total protein was 7.0 g/dL.
Owns a bicycle.
```


## author4 / group 268: `rule_v1.test.inv005.c1.boundary.long.49`

Rule: For Okata fever, prescribe solvadine. If the current platelet count is below 50 x10^9/L, prescribe tarnicept instead.

**base** (program answer: s; facts: patient: platelet count = 373; present; current)
```
Man of 52 years.
Referred with Okata fever.
Current platelet count 373 x10^9/L.
Knits as a hobby.
Paints watercolors as a hobby.
Prefers morning appointments.
His wife has recovered from a dislocated finger.
Prefers to be addressed by first name.
During a checkup in 2016, total protein was 7.0 g/dL.
Drives a car.
Sees a dentist yearly.
Plays the piano.
His father burned a hand on a stove years ago.
Photographs local wildlife.
His friend lives with psoriasis.
Owns a bicycle.
Lives in a second-floor apartment.
Enjoys board games.
Pupils equal and reactive to light.
Teeth in good repair.
In 2022, lipase was 30 U/L.
In 2014, folate was 12 ng/mL.
```

**flip** (program answer: s'; facts: patient: platelet count = 36; present; current)
```
Man of 52 years.
Referred with Okata fever.
Current platelet count 36 x10^9/L.
Knits as a hobby.
Paints watercolors as a hobby.
Prefers morning appointments.
His wife has recovered from a dislocated finger.
Prefers to be addressed by first name.
During a checkup in 2016, total protein was 7.0 g/dL.
Drives a car.
Sees a dentist yearly.
Plays the piano.
His father burned a hand on a stove years ago.
Photographs local wildlife.
His friend lives with psoriasis.
Owns a bicycle.
Lives in a second-floor apartment.
Enjoys board games.
Pupils equal and reactive to light.
Teeth in good repair.
In 2022, lipase was 30 U/L.
In 2014, folate was 12 ng/mL.
```

**near** (program answer: s; facts: patient: platelet count = 50; present; current)
```
Man of 52 years.
Referred with Okata fever.
Current platelet count 50 x10^9/L.
Knits as a hobby.
Paints watercolors as a hobby.
Prefers morning appointments.
His wife has recovered from a dislocated finger.
Prefers to be addressed by first name.
During a checkup in 2016, total protein was 7.0 g/dL.
Drives a car.
Sees a dentist yearly.
Plays the piano.
His father burned a hand on a stove years ago.
Photographs local wildlife.
His friend lives with psoriasis.
Owns a bicycle.
Lives in a second-floor apartment.
Enjoys board games.
Pupils equal and reactive to light.
Teeth in good repair.
In 2022, lipase was 30 U/L.
In 2014, folate was 12 ng/mL.
```

**pres** (program answer: s; facts: patient: platelet count = 373; present; current)
```
Male patient of 52 years.
Referred with Okata fever.
Teeth in good repair.
His wife has recovered from a dislocated finger.
Prefers to be addressed by first name.
In 2022, lipase was 30 U/L.
Plays the piano.
Prefers morning appointments.
Knits as a hobby.
Lives in a second-floor apartment.
Enjoys board games.
Platelet count now 373 x10^9/L.
His friend lives with psoriasis.
In 2014, folate was 12 ng/mL.
Pupils equal and reactive to light.
His father burned a hand on a stove years ago.
During a checkup in 2016, total protein was 7.0 g/dL.
Owns a bicycle.
Photographs local wildlife.
Sees a dentist yearly.
Paints watercolors as a hobby.
Drives a car.
```


## author1 / group 269: `rule_v1.test.gs246.c3.negation.easy.235`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the current white cell count is above 12.0 x10^9/L; the patient has ever had angioedema (current or past); the patient has active cancer.

**base** (program answer: s; facts: patient: white cell count = 4.6; present; current | patient: angioedema; present; past | patient: active cancer; absent; current)
```
Woman of 20 years.
Acute low back pain after lifting.
Latest WBC is 4.6 x10^9/L.
Has two cats.
Prefers morning appointments.
An episode of angioedema years ago, with full recovery.
Plays the piano.
Weight steady over the past year.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: white cell count = 4.6; present; current | patient: angioedema; present; past | patient: active cancer; present; current)
```
Woman of 20 years.
Acute low back pain after lifting.
Latest WBC is 4.6 x10^9/L.
Has two cats.
Prefers morning appointments.
An episode of angioedema years ago, with full recovery.
Plays the piano.
Has metastatic lung cancer, receiving palliative treatment.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: white cell count = 4.6; present; current | patient: angioedema; present; past | patient: active cancer; absent; current)
```
Woman of 20 years.
Acute low back pain after lifting.
Latest WBC is 4.6 x10^9/L.
Has two cats.
Prefers morning appointments.
An episode of angioedema years ago, with full recovery.
Plays the piano.
Free of cancer throughout life.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: white cell count = 4.6; present; current | patient: angioedema; present; past | patient: active cancer; absent; current)
```
Female patient of 20 years.
Acute low back pain after lifting.
Prefers morning appointments.
Current white cell count 4.6 x10^9/L.
Plays the piano.
An episode of angioedema years ago, with full recovery.
Has two cats.
Lives in a second-floor apartment.
Weight steady over the past year.
```

**missing** (program answer: neither; facts: patient: white cell count = 4.6; present; current | patient: angioedema; present; past | patient: active cancer; unknown; current)
```
Woman of 20 years.
Acute low back pain after lifting.
Latest WBC is 4.6 x10^9/L.
Has two cats.
Prefers morning appointments.
An episode of angioedema years ago, with full recovery.
Plays the piano.
Active cancer: status unclear from the records at hand.
Lives in a second-floor apartment.
```


## author2 / group 270: `rule_v1.test.s3_alvarado.wbc.boundary.easy.1760`

Rule: Alvarado score (as used here, partial): 2 points for current tenderness in the right lower quadrant (right iliac fossa); 2 points for a current white cell count above 10.0 x10^9/L; 1 point for a current temperature of 37.3 C or more. Other Alvarado items are not part of this question.

**base** (program answer: s; facts: patient: temperature = 36.8; present; current | patient: white cell count = 8.0; present; current | patient: right lower quadrant tenderness; absent; current)
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

**flip** (program answer: s'; facts: patient: temperature = 36.8; present; current | patient: white cell count = 11.7; present; current | patient: right lower quadrant tenderness; absent; current)
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

**near** (program answer: s; facts: patient: temperature = 36.8; present; current | patient: white cell count = 10.0; present; current | patient: right lower quadrant tenderness; absent; current)
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

**pres** (program answer: s; facts: patient: white cell count = 8.0; present; current | patient: right lower quadrant tenderness; absent; current | patient: temperature = 36.8; present; current)
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


## author3 / group 271: `rule_v1.test.c1_methimazole.alt.numeric.alt.441`

Rule: For Graves' hyperthyroidism, prescribe methimazole. If the current ALT is above 120 U/L, prescribe radioactive iodine instead.

**base** (program answer: s; facts: patient: ALT = 83; present; current)
```
Male patient of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Current ALT 83 U/L.
Plays the piano.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: ALT = 178; present; current)
```
Male patient of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Current ALT 178 U/L.
Plays the piano.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: ALT = 119; present; current)
```
Male patient of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Current ALT 119 U/L.
Plays the piano.
Lives in a second-floor apartment.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: ALT = 83; present; current)
```
Man of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Plays the piano.
ALT now 83 U/L.
Lives in a second-floor apartment.
Prefers morning appointments.
```


## author4 / group 272: `rule_v1.test.gs220.c1.time.easy.1659`

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

**base** (program answer: s; facts: patient: eGFR = 61; present; current | patient: eGFR = 78; present; past (2008) | sister: diabetes (patient or first-degree relative); present; current)
```
Female patient of 37 years.
Requests contraception.
Current eGFR 61 mL/min/1.73 m2.
Plays the piano.
Back in 2008, eGFR stood at 78 mL/min/1.73 m2.
Paints watercolors as a hobby.
Her sister is diabetic.
```

**flip** (program answer: s'; facts: patient: eGFR = 18; present; current | patient: eGFR = 78; present; past (2008) | sister: diabetes (patient or first-degree relative); present; current)
```
Female patient of 37 years.
Requests contraception.
Current eGFR 18 mL/min/1.73 m2.
Plays the piano.
Back in 2008, eGFR stood at 78 mL/min/1.73 m2.
Paints watercolors as a hobby.
Her sister is diabetic.
```

**near** (program answer: s; facts: patient: eGFR = 61; present; current | patient: eGFR = 26; present; past (2008) | sister: diabetes (patient or first-degree relative); present; current)
```
Female patient of 37 years.
Requests contraception.
Current eGFR 61 mL/min/1.73 m2.
Plays the piano.
Back in 2008, eGFR stood at 26 mL/min/1.73 m2.
Paints watercolors as a hobby.
Her sister is diabetic.
```

**pres** (program answer: s; facts: patient: eGFR = 61; present; current | sister: diabetes (patient or first-degree relative); present; current | patient: eGFR = 78; present; past (2008))
```
Woman of 37 years.
Requests contraception.
eGFR now 61 mL/min/1.73 m2.
Her sister is diabetic.
Paints watercolors as a hobby.
Records from 2008 list eGFR at 78 mL/min/1.73 m2.
Plays the piano.
```


## author1 / group 273: `rule_v1.test.s1_bap65.ams.time.long.442`

Rule: BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of 25 mg/dL or more; current altered mental status (confusion or disorientation); a current heart rate of 109/min or more. Age is scored separately and is not part of this question.

**base** (program answer: s; facts: patient: heart rate = 82; present; current | patient: blood urea nitrogen = 20; present; current | patient: altered mental status; absent; current)
```
Woman of 70 years.
Acute exacerbation of COPD; assessed in the emergency department.
Enjoys board games.
Owns a bicycle.
In 2013, lipase was 30 U/L.
Sees a dentist yearly.
Her sister has recovered from a dislocated finger.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
In 2012, folate was 12 ng/mL.
Lives in a second-floor apartment.
Teeth in good repair.
Current heart rate 82/min.
Paints watercolors as a hobby.
Her wife lives with psoriasis.
Photographs local wildlife.
Has two cats.
Drives a car.
Her wife burned a hand on a stove years ago.
Blood urea nitrogen 20 mg/dL on the current labs.
Her friend has a lazy eye.
Sleeps seven hours a night.
Gives a clear account of the illness.
```

**flip** (program answer: s'; facts: patient: heart rate = 82; present; current | patient: blood urea nitrogen = 20; present; current | patient: altered mental status; present; current)
```
Woman of 70 years.
Acute exacerbation of COPD; assessed in the emergency department.
Enjoys board games.
Owns a bicycle.
In 2013, lipase was 30 U/L.
Sees a dentist yearly.
Her sister has recovered from a dislocated finger.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
In 2012, folate was 12 ng/mL.
Lives in a second-floor apartment.
Teeth in good repair.
Current heart rate 82/min.
Paints watercolors as a hobby.
Her wife lives with psoriasis.
Photographs local wildlife.
Has two cats.
Drives a car.
Her wife burned a hand on a stove years ago.
Blood urea nitrogen 20 mg/dL on the current labs.
Her friend has a lazy eye.
Sleeps seven hours a night.
Disoriented to time and place, which is new for the patient.
```

**near** (program answer: s; facts: patient: heart rate = 82; present; current | patient: blood urea nitrogen = 20; present; current | patient: altered mental status; present; past (2022))
```
Woman of 70 years.
Acute exacerbation of COPD; assessed in the emergency department.
Enjoys board games.
Owns a bicycle.
In 2013, lipase was 30 U/L.
Sees a dentist yearly.
Her sister has recovered from a dislocated finger.
Prefers morning appointments.
Plays the piano.
Prefers to be addressed by first name.
In 2012, folate was 12 ng/mL.
Lives in a second-floor apartment.
Teeth in good repair.
Current heart rate 82/min.
Paints watercolors as a hobby.
Her wife lives with psoriasis.
Photographs local wildlife.
Has two cats.
Drives a car.
Her wife burned a hand on a stove years ago.
Blood urea nitrogen 20 mg/dL on the current labs.
Her friend has a lazy eye.
Sleeps seven hours a night.
Formerly had an episode of confusion with dehydration in 2022.
```

**pres** (program answer: s; facts: patient: altered mental status; absent; current | patient: blood urea nitrogen = 20; present; current | patient: heart rate = 82; present; current)
```
Female patient of 70 years.
Acute exacerbation of COPD; assessed in the emergency department.
Gives a clear account of the illness.
Has two cats.
Her wife burned a hand on a stove years ago.
Prefers to be addressed by first name.
Photographs local wildlife.
Owns a bicycle.
Enjoys board games.
In 2012, folate was 12 ng/mL.
Blood urea nitrogen now: 20 mg/dL.
Her sister has recovered from a dislocated finger.
Lives in a second-floor apartment.
Her friend has a lazy eye.
Heart rate now 82/min on a pulse check.
Plays the piano.
Prefers morning appointments.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Sees a dentist yearly.
Teeth in good repair.
Her wife lives with psoriasis.
In 2013, lipase was 30 U/L.
Drives a car.
```


## author2 / group 274: `rule_v1.test.gs194.c2.numeric.easy.866`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: heart rate = 71; present; current | patient: weight = 94; present; current)
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
Latest weight 94 kg.
```

**flip** (program answer: s'; facts: patient: heart rate = 71; present; current | patient: weight = 56; present; current)
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
Latest weight 56 kg.
```

**near** (program answer: s; facts: patient: heart rate = 71; present; current | patient: weight = 61; present; current)
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
Latest weight 61 kg.
```

**pres** (program answer: s; facts: patient: weight = 94; present; current | patient: heart rate = 71; present; current)
```
Woman of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Knits as a hobby.
Teeth in good repair.
Current weight 94 kg.
Paints watercolors as a hobby.
Heart rate now 71/min on a pulse check.
```

**missing** (program answer: neither; facts: patient: heart rate = 71; present; current)
```
Female patient of 31 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Paints watercolors as a hobby.
Teeth in good repair.
Knits as a hobby.
Current heart rate 71/min.
```


## author3 / group 275: `rule_v1.test.gs002.c2.boundary.long.854`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: serum potassium = 4.3; present; current | patient: heart rate = 82; present; current)
```
Female patient of 65 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Latest potassium result: 4.3 mmol/L.
Prefers to be addressed by first name.
Her friend has recovered from a dislocated finger.
Pupils equal and reactive to light.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Heart rate now 82/min on a pulse check.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
Has two cats.
Free T4 of 1.2 ng/dL in 2020.
Uses sunscreen in summer.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```

**flip** (program answer: s'; facts: patient: serum potassium = 5.1; present; current | patient: heart rate = 82; present; current)
```
Female patient of 65 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Latest potassium result: 5.1 mmol/L.
Prefers to be addressed by first name.
Her friend has recovered from a dislocated finger.
Pupils equal and reactive to light.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Heart rate now 82/min on a pulse check.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
Has two cats.
Free T4 of 1.2 ng/dL in 2020.
Uses sunscreen in summer.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```

**near** (program answer: s; facts: patient: serum potassium = 4.8; present; current | patient: heart rate = 82; present; current)
```
Female patient of 65 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Latest potassium result: 4.8 mmol/L.
Prefers to be addressed by first name.
Her friend has recovered from a dislocated finger.
Pupils equal and reactive to light.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Heart rate now 82/min on a pulse check.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
Has two cats.
Free T4 of 1.2 ng/dL in 2020.
Uses sunscreen in summer.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```

**pres** (program answer: s; facts: patient: heart rate = 82; present; current | patient: serum potassium = 4.3; present; current)
```
Woman of 65 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Sees a dentist yearly.
Her friend has recovered from a dislocated finger.
Drives a car.
Has two cats.
Photographs local wildlife.
Free T4 of 1.2 ng/dL in 2020.
Pupils equal and reactive to light.
Owns a bicycle.
Current heart rate 82/min.
During a checkup in 2005, total protein was 7.0 g/dL.
Current serum potassium 4.3 mmol/L.
Her wife has a lazy eye.
Prefers to be addressed by first name.
Enjoys board games.
Uses sunscreen in summer.
Her friend burned a hand on a stove years ago.
Knits as a hobby.
Prefers morning appointments.
Teeth in good repair.
Lives in a second-floor apartment.
```

**missing** (program answer: neither; facts: patient: heart rate = 82; present; current)
```
Female patient of 65 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Photographs local wildlife.
Prefers to be addressed by first name.
Her friend has recovered from a dislocated finger.
Pupils equal and reactive to light.
Sees a dentist yearly.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
Owns a bicycle.
Her friend burned a hand on a stove years ago.
Her wife has a lazy eye.
During a checkup in 2005, total protein was 7.0 g/dL.
Heart rate now 82/min on a pulse check.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
Has two cats.
Free T4 of 1.2 ng/dL in 2020.
Uses sunscreen in summer.
Sleeps seven hours a night.
Lives in a second-floor apartment.
```


## author4 / group 276: `rule_v1.test.gs225.c2.boundary.long.251`

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has an active peptic ulcer and the current white cell count is above 12.0 x10^9/L, prescribe naproxen with omeprazole instead.

**base** (program answer: s; facts: patient: white cell count = 8.8; present; current | patient: active peptic ulcer; present; current)
```
Woman of 80 years.
Hip osteoarthritis with pain on walking.
Her roommate lives with psoriasis.
Latest WBC is 8.8 x10^9/L.
Her wife wears contact lenses.
During a checkup in 2013, total protein was 7.0 g/dL.
Owns a bicycle.
Plays the piano.
Prefers to be addressed by first name.
Teeth in good repair.
Pupils equal and reactive to light.
Prefers morning appointments.
Has two cats.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2010.
Active peptic ulcer disease.
In 2011, folate was 12 ng/mL.
Drives a car.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: white cell count = 12.8; present; current | patient: active peptic ulcer; present; current)
```
Woman of 80 years.
Hip osteoarthritis with pain on walking.
Her roommate lives with psoriasis.
Latest WBC is 12.8 x10^9/L.
Her wife wears contact lenses.
During a checkup in 2013, total protein was 7.0 g/dL.
Owns a bicycle.
Plays the piano.
Prefers to be addressed by first name.
Teeth in good repair.
Pupils equal and reactive to light.
Prefers morning appointments.
Has two cats.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2010.
Active peptic ulcer disease.
In 2011, folate was 12 ng/mL.
Drives a car.
Sees a dentist yearly.
```

**near** (program answer: s; facts: patient: white cell count = 12.0; present; current | patient: active peptic ulcer; present; current)
```
Woman of 80 years.
Hip osteoarthritis with pain on walking.
Her roommate lives with psoriasis.
Latest WBC is 12.0 x10^9/L.
Her wife wears contact lenses.
During a checkup in 2013, total protein was 7.0 g/dL.
Owns a bicycle.
Plays the piano.
Prefers to be addressed by first name.
Teeth in good repair.
Pupils equal and reactive to light.
Prefers morning appointments.
Has two cats.
Photographs local wildlife.
Enjoys board games.
Zinc of 85 mcg/dL in 2010.
Active peptic ulcer disease.
In 2011, folate was 12 ng/mL.
Drives a car.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: patient: white cell count = 8.8; present; current | patient: active peptic ulcer; present; current)
```
Female patient of 80 years.
Hip osteoarthritis with pain on walking.
Prefers to be addressed by first name.
Owns a bicycle.
Current white cell count 8.8 x10^9/L.
Enjoys board games.
During a checkup in 2013, total protein was 7.0 g/dL.
Plays the piano.
Sees a dentist yearly.
Prefers morning appointments.
Active peptic ulcer disease.
Has two cats.
Drives a car.
Her roommate lives with psoriasis.
In 2011, folate was 12 ng/mL.
Photographs local wildlife.
Zinc of 85 mcg/dL in 2010.
Pupils equal and reactive to light.
Teeth in good repair.
Her wife wears contact lenses.
```


## author1 / group 277: `rule_v1.test.qsofa.sbp.numeric.easy.257`

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**base** (program answer: s; facts: patient: systolic blood pressure = 131; present; current | patient: altered mentation; absent; current | patient: respiratory rate = 15; present; current)
```
Male patient of 57 years.
Suspected urinary sepsis, assessed in the emergency department.
Current systolic blood pressure 131 mmHg.
Speech clear; follows commands.
Has two cats.
Current respiratory rate 15/min.
```

**flip** (program answer: s'; facts: patient: systolic blood pressure = 97; present; current | patient: altered mentation; absent; current | patient: respiratory rate = 15; present; current)
```
Male patient of 57 years.
Suspected urinary sepsis, assessed in the emergency department.
Current systolic blood pressure 97 mmHg.
Speech clear; follows commands.
Has two cats.
Current respiratory rate 15/min.
```

**near** (program answer: s; facts: patient: systolic blood pressure = 101; present; current | patient: altered mentation; absent; current | patient: respiratory rate = 15; present; current)
```
Male patient of 57 years.
Suspected urinary sepsis, assessed in the emergency department.
Current systolic blood pressure 101 mmHg.
Speech clear; follows commands.
Has two cats.
Current respiratory rate 15/min.
```

**pres** (program answer: s; facts: patient: altered mentation; absent; current | patient: respiratory rate = 15; present; current | patient: systolic blood pressure = 131; present; current)
```
Man of 57 years.
Suspected urinary sepsis, assessed in the emergency department.
Has two cats.
Speech clear; follows commands.
Observations now: respiratory rate 15/min.
Observations now: blood pressure 131/87 mmHg.
```

**missing** (program answer: neither; facts: patient: altered mentation; absent; current | patient: respiratory rate = 15; present; current)
```
Male patient of 57 years.
Suspected urinary sepsis, assessed in the emergency department.
Speech clear; follows commands.
Has two cats.
Current respiratory rate 15/min.
```


## author2 / group 278: `rule_v1.test.statin_alt.alt.time.alt.7`

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**base** (program answer: s; facts: patient: ALT = 29; present; current | patient: ALT = 27; present; past (2008))
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

**flip** (program answer: s'; facts: patient: ALT = 101; present; current | patient: ALT = 27; present; past (2008))
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

**near** (program answer: s; facts: patient: ALT = 29; present; current | patient: ALT = 223; present; past (2008))
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

**pres** (program answer: s; facts: patient: ALT = 27; present; past (2008) | patient: ALT = 29; present; current)
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


## author3 / group 279: `rule_v1.test.gs088.c2.subject.easy.1669`

Rule: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.

**base** (program answer: s; facts: patient: white cell count = 12.9; present; current)
```
Male patient of 20 years.
Sore throat for two days.
Photographs local wildlife.
Latest WBC is 12.9 x10^9/L.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: white cell count = 12.9; present; current | patient: myocardial infarction or peripheral artery disease; present; past (2024))
```
Male patient of 20 years.
Sore throat for two days.
Photographs local wildlife.
Latest WBC is 12.9 x10^9/L.
Recovered from a heart attack in 2024.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: patient: white cell count = 12.9; present; current | uncle: myocardial infarction or peripheral artery disease; present; past)
```
Male patient of 20 years.
Sore throat for two days.
Photographs local wildlife.
Latest WBC is 12.9 x10^9/L.
His uncle had a heart attack years ago.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: white cell count = 12.9; present; current)
```
Man of 20 years.
Sore throat for two days.
Uses sunscreen in summer.
Plays the piano.
Photographs local wildlife.
Sleeps seven hours a night.
Current white cell count 12.9 x10^9/L.
```


## author4 / group 280: `rule_v1.test.gs024.c3.numeric.easy.1162`

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 3 points if the current ALT is above 120 U/L; 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 3 points if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 4 or more, prescribe nitrofurantoin instead.

**base** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 32; present; current | patient: systolic blood pressure = 126; present; current)
```
Female patient of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Lives in a second-floor apartment.
Has type 2 diabetes on metformin.
ALT now 32 U/L.
Has two cats.
Sleeps seven hours a night.
Observations now: blood pressure 126/84 mmHg.
```

**flip** (program answer: s'; facts: patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 32; present; current | patient: systolic blood pressure = 172; present; current)
```
Female patient of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Lives in a second-floor apartment.
Has type 2 diabetes on metformin.
ALT now 32 U/L.
Has two cats.
Sleeps seven hours a night.
Observations now: blood pressure 172/110 mmHg.
```

**near** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; current | patient: ALT = 32; present; current | patient: systolic blood pressure = 158; present; current)
```
Female patient of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Lives in a second-floor apartment.
Has type 2 diabetes on metformin.
ALT now 32 U/L.
Has two cats.
Sleeps seven hours a night.
Observations now: blood pressure 158/102 mmHg.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); present; current | patient: systolic blood pressure = 126; present; current | patient: ALT = 32; present; current)
```
Woman of 42 years.
Dysuria and urinary frequency for two days; urine dipstick positive for nitrites.
Has type 2 diabetes on metformin.
Current systolic blood pressure 126 mmHg.
Lives in a second-floor apartment.
Has two cats.
Current ALT 32 U/L.
Sleeps seven hours a night.
```


## author1 / group 281: `rule_v1.test.hf_spironolactone.k.boundary.alt.487`

Rule: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 4.5 mmol/L, add dapagliflozin instead.

**base** (program answer: s; facts: patient: potassium = 4.0; present; current)
```
Woman of 60 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Plays the piano.
Owns a bicycle.
Current serum potassium 4.0 mmol/L.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: patient: potassium = 4.8; present; current)
```
Woman of 60 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Plays the piano.
Owns a bicycle.
Current serum potassium 4.8 mmol/L.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: patient: potassium = 4.5; present; current)
```
Woman of 60 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Plays the piano.
Owns a bicycle.
Current serum potassium 4.5 mmol/L.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: patient: potassium = 4.0; present; current)
```
Female patient of 60 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Plays the piano.
Uses sunscreen in summer.
Owns a bicycle.
Latest potassium result: 4.0 mmol/L.
```


## author2 / group 282: `rule_v1.test.s3_charlson.cr.boundary.alt.872`

Rule: Charlson Comorbidity Index (as used here, partial): 1 point for heart failure at any time (current or past); 1 point for a myocardial infarction or peripheral artery disease at any time (current or past); 1 point for current asthma; 2 points for a current serum creatinine above 2.0 mg/dL. Age and other Charlson items are not part of this question.

**base** (program answer: s; facts: patient: asthma; absent; current | patient: serum creatinine = 0.8; present; current | patient: heart failure; absent; current)
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

**flip** (program answer: s'; facts: patient: asthma; absent; current | patient: serum creatinine = 2.4; present; current | patient: heart failure; absent; current)
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

**near** (program answer: s; facts: patient: asthma; absent; current | patient: serum creatinine = 2.0; present; current | patient: heart failure; absent; current)
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

**pres** (program answer: s; facts: patient: asthma; absent; current | patient: serum creatinine = 0.8; present; current | patient: heart failure; absent; current)
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


## author3 / group 283: `rule_v1.test.gs131.c3.subject.easy.1913`

Rule: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

**base** (program answer: s; facts: patient: eGFR = 43; present; current | patient: heart rate = 98; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers morning appointments.
Current eGFR 43 mL/min/1.73 m2.
Heart rate now 98/min on a pulse check.
Has two cats.
Knits as a hobby.
```

**flip** (program answer: s'; facts: patient: eGFR = 43; present; current | patient: heart rate = 98; present; current | patient: coronary artery disease; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers morning appointments.
Current eGFR 43 mL/min/1.73 m2.
Heart rate now 98/min on a pulse check.
Has two cats.
Known coronary artery disease (two-vessel disease on angiography).
Knits as a hobby.
```

**near** (program answer: s; facts: patient: eGFR = 43; present; current | patient: heart rate = 98; present; current | sister: coronary artery disease; present; current)
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers morning appointments.
Current eGFR 43 mL/min/1.73 m2.
Heart rate now 98/min on a pulse check.
Has two cats.
Her sister has angina from coronary artery disease.
Knits as a hobby.
```

**pres** (program answer: s; facts: patient: eGFR = 43; present; current | patient: heart rate = 98; present; current)
```
Woman of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
eGFR now 43 mL/min/1.73 m2.
Knits as a hobby.
Prefers morning appointments.
Has two cats.
Current heart rate 98/min.
```


## author4 / group 284: `rule_v1.test.gs096.c1.subject.easy.772`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 2 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient currently has tonsillar exudate; 2 points if the current ALT is above 120 U/L; 2 points if the current weight is 60 kg or less. If the score is 6 or more, prescribe warfarin instead.

**base** (program answer: s; facts: patient: weight = 68; present; current | patient: tonsillar exudate; present; current | patient: coronary artery disease; absent; current | patient: ALT = 125; present; current)
```
Female patient of 80 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest weight 68 kg.
Drives a car.
Sleeps seven hours a night.
Tonsils swollen and coated with yellow exudate.
Cardiac stress test unremarkable last year.
ALT now 125 U/L.
```

**flip** (program answer: s'; facts: patient: weight = 68; present; current | patient: tonsillar exudate; present; current | patient: coronary artery disease; present; current | patient: ALT = 125; present; current)
```
Female patient of 80 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest weight 68 kg.
Drives a car.
Sleeps seven hours a night.
Tonsils swollen and coated with yellow exudate.
Has coronary artery disease, managed medically.
ALT now 125 U/L.
```

**near** (program answer: s; facts: patient: weight = 68; present; current | patient: tonsillar exudate; present; current | wife: coronary artery disease; present; current | patient: ALT = 125; present; current)
```
Female patient of 80 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest weight 68 kg.
Drives a car.
Sleeps seven hours a night.
Tonsils swollen and coated with yellow exudate.
Her wife has angina from coronary artery disease.
ALT now 125 U/L.
```

**pres** (program answer: s; facts: patient: ALT = 125; present; current | patient: coronary artery disease; absent; current | patient: weight = 68; present; current | patient: tonsillar exudate; present; current)
```
Woman of 80 years.
Atrial fibrillation; anticoagulation indicated.
Current ALT 125 U/L.
Drives a car.
Sees a dentist yearly.
Sleeps seven hours a night.
Cardiac stress test unremarkable last year.
Current weight 68 kg.
Tonsils swollen and coated with yellow exudate.
Lives in a second-floor apartment.
```

**missing** (program answer: neither; facts: patient: weight = 68; present; current | patient: tonsillar exudate; present; current | patient: coronary artery disease; unknown; current | patient: ALT = 125; present; current)
```
Female patient of 80 years.
Atrial fibrillation; anticoagulation indicated.
Sees a dentist yearly.
Lives in a second-floor apartment.
Latest weight 68 kg.
Drives a car.
Sleeps seven hours a night.
Tonsils swollen and coated with yellow exudate.
Coronary artery disease: status unclear from the records at hand.
ALT now 125 U/L.
```


## author1 / group 285: `rule_v1.test.cut_vte.vte.subject.easy.1305`

Rule: For thromboprophylaxis in a medical inpatient, prescribe compression stockings. Score 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. If the score is 4 or more, prescribe enoxaparin instead.

**base** (program answer: s; facts: patient: venous thromboembolism; absent; current | patient: heart failure; absent; current | patient: age = 41; present; current | patient: active cancer; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Coagulation tests normal on recent bloodwork.
Heart sounds without a gallop.
Owns a bicycle.
Current age 41 years.
Teeth in good repair.
Has metastatic lung cancer, receiving palliative treatment.
Sees a dentist yearly.
```

**flip** (program answer: s'; facts: patient: venous thromboembolism; present; current | patient: heart failure; absent; current | patient: age = 41; present; current | patient: active cancer; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Has an acute pulmonary embolism, diagnosed this week.
Heart sounds without a gallop.
Owns a bicycle.
Current age 41 years.
Teeth in good repair.
Has metastatic lung cancer, receiving palliative treatment.
Sees a dentist yearly.
```

**near** (program answer: s; facts: sister: venous thromboembolism; present; current | patient: heart failure; absent; current | patient: age = 41; present; current | patient: active cancer; present; current)
```
An adult man.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
His sister is being treated for a pulmonary embolism.
Heart sounds without a gallop.
Owns a bicycle.
Current age 41 years.
Teeth in good repair.
Has metastatic lung cancer, receiving palliative treatment.
Sees a dentist yearly.
```

**pres** (program answer: s; facts: patient: age = 41; present; current | patient: active cancer; present; current | patient: heart failure; absent; current | patient: venous thromboembolism; absent; current)
```
Man, adult.
Admitted with community-acquired pneumonia; expected to stay in bed for several days.
Currently aged 41 years.
Teeth in good repair.
Has metastatic lung cancer, receiving palliative treatment.
Owns a bicycle.
Heart sounds without a gallop.
Coagulation tests normal on recent bloodwork.
Sees a dentist yearly.
```


## author2 / group 286: `rule_v1.test.gs138.c1.negation.easy.1612`

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If at least two of the following apply, prescribe warfarin instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the current weight is 60 kg or less; the patient currently has heart failure.

**base** (program answer: s; facts: patient: weight = 80; present; current | patient: current heart failure; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current)
```
Male patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Latest weight 80 kg.
Has heart failure, treated with diuretics.
Coagulation tests normal on recent bloodwork.
```

**flip** (program answer: s'; facts: patient: weight = 80; present; current | patient: current heart failure; present; current | father: venous thromboembolism (patient or first-degree relative); present; past)
```
Male patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Latest weight 80 kg.
Has heart failure, treated with diuretics.
His father had a DVT years ago.
```

**near** (program answer: s; facts: patient: weight = 80; present; current | patient: current heart failure; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current)
```
Male patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Latest weight 80 kg.
Has heart failure, treated with diuretics.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**pres** (program answer: s; facts: patient: current heart failure; present; current | patient: venous thromboembolism (patient or first-degree relative); absent; current | patient: weight = 80; present; current)
```
Man of 50 years.
Atrial fibrillation; anticoagulation indicated.
Has heart failure, treated with diuretics.
Coagulation tests normal on recent bloodwork.
Prefers to be addressed by first name.
Current weight 80 kg.
```


## author3 / group 287: `rule_v1.test.ckd_nsaid.egfr.boundary.alt.625`

Rule: For knee osteoarthritis pain, prescribe naproxen. If the patient's current eGFR is below 75 mL/min/1.73 m2, prescribe acetaminophen instead.

**base** (program answer: s; facts: patient: eGFR = 100; present; current)
```
Male patient of 55 years.
Knee osteoarthritis with pain on walking.
Current eGFR 100 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
Sleeps seven hours a night.
```

**flip** (program answer: s'; facts: patient: eGFR = 63; present; current)
```
Male patient of 55 years.
Knee osteoarthritis with pain on walking.
Current eGFR 63 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
Sleeps seven hours a night.
```

**near** (program answer: s; facts: patient: eGFR = 75; present; current)
```
Male patient of 55 years.
Knee osteoarthritis with pain on walking.
Current eGFR 75 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
Sleeps seven hours a night.
```

**pres** (program answer: s; facts: patient: eGFR = 100; present; current)
```
Man of 55 years.
Knee osteoarthritis with pain on walking.
Sleeps seven hours a night.
eGFR now 100 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
```


## author4 / group 288: `rule_v1.test.gs245.c2.negation.easy.1392`

Rule: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had heart failure (current or past); the patient has an active peptic ulcer; the age of the patient is 65 years or more.

**base** (program answer: s; facts: patient: heart failure; present; past (2016) | patient: age = 42; present; current | patient: active peptic ulcer; absent; current)
```
Man, adult.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2016 and off all heart medicines since.
Plays the piano.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current age 42 years.
Abdomen soft and non-tender.
Prefers morning appointments.
```

**flip** (program answer: s'; facts: patient: heart failure; present; past (2016) | patient: age = 42; present; current | patient: active peptic ulcer; present; current)
```
Man, adult.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2016 and off all heart medicines since.
Plays the piano.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current age 42 years.
Active peptic ulcer disease.
Prefers morning appointments.
```

**near** (program answer: s; facts: patient: heart failure; present; past (2016) | patient: age = 42; present; current | patient: active peptic ulcer; absent; current)
```
Man, adult.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2016 and off all heart medicines since.
Plays the piano.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current age 42 years.
Medical record negative for peptic ulcer, current or past.
Prefers morning appointments.
```

**pres** (program answer: s; facts: patient: active peptic ulcer; absent; current | patient: heart failure; present; past (2016) | patient: age = 42; present; current)
```
An adult man.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Abdomen soft and non-tender.
Paints watercolors as a hobby.
Prefers morning appointments.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2016 and off all heart medicines since.
Prefers to be addressed by first name.
Plays the piano.
Currently aged 42 years.
```


## author1 / group 289: `rule_v1.test.gs123.c3.boundary.long.337`

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the patient is currently taking aspirin; the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the current serum potassium is above 5.0 mmol/L.

**base** (program answer: s; facts: sister: diabetes (patient or first-degree relative); present; past | patient: serum potassium = 3.8; present; current)
```
Woman of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drives a car.
Knits as a hobby.
Lives in a second-floor apartment.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her sister had diabetes years ago that went away after a change in diet.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2019.
Her uncle has a lazy eye.
Photographs local wildlife.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Enjoys board games.
Paints watercolors as a hobby.
Teeth in good repair.
Latest potassium result: 3.8 mmol/L.
Her father wears contact lenses.
Uses sunscreen in summer.
```

**flip** (program answer: s'; facts: sister: diabetes (patient or first-degree relative); present; past | patient: serum potassium = 5.5; present; current)
```
Woman of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drives a car.
Knits as a hobby.
Lives in a second-floor apartment.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her sister had diabetes years ago that went away after a change in diet.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2019.
Her uncle has a lazy eye.
Photographs local wildlife.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Enjoys board games.
Paints watercolors as a hobby.
Teeth in good repair.
Latest potassium result: 5.5 mmol/L.
Her father wears contact lenses.
Uses sunscreen in summer.
```

**near** (program answer: s; facts: sister: diabetes (patient or first-degree relative); present; past | patient: serum potassium = 5.0; present; current)
```
Woman of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Drives a car.
Knits as a hobby.
Lives in a second-floor apartment.
Sees a dentist yearly.
Pupils equal and reactive to light.
Her sister had diabetes years ago that went away after a change in diet.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Free T4 of 1.2 ng/dL in 2019.
Her uncle has a lazy eye.
Photographs local wildlife.
Her sister burned a hand on a stove years ago.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Enjoys board games.
Paints watercolors as a hobby.
Teeth in good repair.
Latest potassium result: 5.0 mmol/L.
Her father wears contact lenses.
Uses sunscreen in summer.
```

**pres** (program answer: s; facts: sister: diabetes (patient or first-degree relative); present; past | patient: serum potassium = 3.8; present; current)
```
Female patient of 52 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Enjoys board games.
Uses sunscreen in summer.
Her father wears contact lenses.
Her uncle has a lazy eye.
Sleeps seven hours a night.
Photographs local wildlife.
Knits as a hobby.
Her sister had diabetes years ago that went away after a change in diet.
Free T4 of 1.2 ng/dL in 2019.
Her sister burned a hand on a stove years ago.
Prefers to be addressed by first name.
Drives a car.
Current serum potassium 3.8 mmol/L.
Lives in a second-floor apartment.
During a checkup in 2023, free T3 was 3.2 pg/mL.
Teeth in good repair.
Paints watercolors as a hobby.
Sees a dentist yearly.
Pupils equal and reactive to light.
```


## author2 / group 290: `rule_v1.test.s1_psi.bun.time.alt.242`

Rule: Pneumonia Severity Index (as used here, partial): 30 points for active cancer; 10 points for current heart failure; 10 points for a stroke or TIA at any time; 30 points for a current arterial pH below 7.35; 20 points for a current blood urea nitrogen of 20 mg/dL or more. Age, sex and other items of the index are not part of this question.

**base** (program answer: s; facts: patient: active cancer; absent; current | patient: blood urea nitrogen = 15; present; current | patient: stroke/TIA; absent; current | patient: arterial pH = 7.4; present; current | patient: blood urea nitrogen = 13; present; past (2018))
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

**flip** (program answer: s'; facts: patient: active cancer; absent; current | patient: blood urea nitrogen = 21; present; current | patient: stroke/TIA; absent; current | patient: arterial pH = 7.4; present; current | patient: blood urea nitrogen = 13; present; past (2018))
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

**near** (program answer: s; facts: patient: active cancer; absent; current | patient: blood urea nitrogen = 15; present; current | patient: stroke/TIA; absent; current | patient: arterial pH = 7.4; present; current | patient: blood urea nitrogen = 32; present; past (2018))
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

**pres** (program answer: s; facts: patient: stroke/TIA; absent; current | patient: active cancer; absent; current | patient: blood urea nitrogen = 15; present; current | patient: blood urea nitrogen = 13; present; past (2018) | patient: arterial pH = 7.4; present; current)
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


## author3 / group 291: `rule_v1.test.gs038.c2.time.long.465`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.

**base** (program answer: s; facts: patient: blood urea nitrogen = 10; present; past (2023) | patient: peptic ulcer at any time; present; past | patient: blood urea nitrogen = 10; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Back in 2023, blood urea nitrogen stood at 10 mg/dL.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
Drives a car.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Teeth in good repair.
Prefers morning appointments.
Blood urea nitrogen now: 10 mg/dL.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
Has two cats.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2012.
Owns a bicycle.
His wife has a lazy eye.
Photographs local wildlife.
Prefers to be addressed by first name.
```

**flip** (program answer: s'; facts: patient: blood urea nitrogen = 10; present; past (2023) | patient: peptic ulcer at any time; present; past | patient: blood urea nitrogen = 28; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Back in 2023, blood urea nitrogen stood at 10 mg/dL.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
Drives a car.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Teeth in good repair.
Prefers morning appointments.
Blood urea nitrogen now: 28 mg/dL.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
Has two cats.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2012.
Owns a bicycle.
His wife has a lazy eye.
Photographs local wildlife.
Prefers to be addressed by first name.
```

**near** (program answer: s; facts: patient: blood urea nitrogen = 23; present; past (2023) | patient: peptic ulcer at any time; present; past | patient: blood urea nitrogen = 10; present; current)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Back in 2023, blood urea nitrogen stood at 23 mg/dL.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
Drives a car.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Teeth in good repair.
Prefers morning appointments.
Blood urea nitrogen now: 10 mg/dL.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
Has two cats.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2012.
Owns a bicycle.
His wife has a lazy eye.
Photographs local wildlife.
Prefers to be addressed by first name.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; present; past | patient: blood urea nitrogen = 10; present; past (2023) | patient: blood urea nitrogen = 10; present; current)
```
Man of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
His friend sprained a thumb last month.
Duodenal ulcer years ago; recovered fully with treatment.
Drives a car.
Lives in a second-floor apartment.
Has two cats.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Free T4 of 1.2 ng/dL in 2012.
Knits as a hobby.
His wife has a lazy eye.
Photographs local wildlife.
Records from 2023 list blood urea nitrogen at 10 mg/dL.
Prefers morning appointments.
Teeth in good repair.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Pupils equal and reactive to light.
Blood urea nitrogen 10 mg/dL on the current labs.
Enjoys board games.
Owns a bicycle.
Uses sunscreen in summer.
Paints watercolors as a hobby.
```

**missing** (program answer: neither; facts: patient: peptic ulcer at any time; present; past)
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Duodenal ulcer years ago; recovered fully with treatment.
Uses sunscreen in summer.
Drives a car.
During a checkup in 2014, free T3 was 3.2 pg/mL.
Teeth in good repair.
Prefers morning appointments.
Sleeps seven hours a night.
His friend sprained a thumb last month.
Knits as a hobby.
Has two cats.
Enjoys board games.
Free T4 of 1.2 ng/dL in 2012.
Owns a bicycle.
His wife has a lazy eye.
Photographs local wildlife.
Prefers to be addressed by first name.
```


## author4 / group 292: `rule_v1.test.gs223.c3.time.superseded.1640`

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current blood urea nitrogen is above 19 mg/dL.

**base** (program answer: s; facts: patient: diabetes (patient or first-degree relative); absent; current | patient: blood urea nitrogen = 13; present; past | patient: colorectal cancer (patient or first-degree relative); present; current | patient: blood urea nitrogen = 10; present; current)
```
Woman of 20 years.
Requests contraception.
HbA1c 5.3% at a routine check.
Earlier this week, blood urea nitrogen was 13 mg/dL; a newer reading supersedes it.
Colorectal cancer under active treatment.
Blood urea nitrogen now: 10 mg/dL.
Prefers to be addressed by first name.
```

**flip** (program answer: s'; facts: patient: diabetes (patient or first-degree relative); absent; current | patient: blood urea nitrogen = 13; present; past | patient: colorectal cancer (patient or first-degree relative); present; current | patient: blood urea nitrogen = 27; present; current)
```
Woman of 20 years.
Requests contraception.
HbA1c 5.3% at a routine check.
Earlier this week, blood urea nitrogen was 13 mg/dL; a newer reading supersedes it.
Colorectal cancer under active treatment.
Blood urea nitrogen now: 27 mg/dL.
Prefers to be addressed by first name.
```

**near** (program answer: s; facts: patient: diabetes (patient or first-degree relative); absent; current | patient: blood urea nitrogen = 25; present; past | patient: colorectal cancer (patient or first-degree relative); present; current | patient: blood urea nitrogen = 10; present; current)
```
Woman of 20 years.
Requests contraception.
HbA1c 5.3% at a routine check.
Earlier this week, blood urea nitrogen was 25 mg/dL; a newer reading supersedes it.
Colorectal cancer under active treatment.
Blood urea nitrogen now: 10 mg/dL.
Prefers to be addressed by first name.
```

**pres** (program answer: s; facts: patient: diabetes (patient or first-degree relative); absent; current | patient: colorectal cancer (patient or first-degree relative); present; current | patient: blood urea nitrogen = 13; present; past | patient: blood urea nitrogen = 10; present; current)
```
Female patient of 20 years.
Requests contraception.
HbA1c 5.3% at a routine check.
Colorectal cancer under active treatment.
Prefers to be addressed by first name.
Earlier this week, blood urea nitrogen was 13 mg/dL; a newer reading supersedes it.
Blood urea nitrogen 10 mg/dL on the current labs.
```


## author1 / group 293: `rule_v1.test.gs046.c1.subject.long.248`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient currently has heart failure or the current heart rate is above 90/min, prescribe amlodipine instead.

**base** (program answer: s; facts: patient: current heart failure; absent; current | patient: heart rate = 79; present; current)
```
Male patient of 72 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Drives a car.
Sleeps seven hours a night.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Photographs local wildlife.
His sister sprained a thumb last month.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Sees a dentist yearly.
His roommate has a lazy eye.
Heart sounds without a gallop.
Heart rate now 79/min on a pulse check.
During a checkup in 2008, total protein was 7.0 g/dL.
Enjoys board games.
In 2024, lipase was 30 U/L.
His friend lives with psoriasis.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
```

**flip** (program answer: s'; facts: patient: current heart failure; present; current | patient: heart rate = 79; present; current)
```
Male patient of 72 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Drives a car.
Sleeps seven hours a night.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Photographs local wildlife.
His sister sprained a thumb last month.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Sees a dentist yearly.
His roommate has a lazy eye.
Has heart failure, treated with diuretics.
Heart rate now 79/min on a pulse check.
During a checkup in 2008, total protein was 7.0 g/dL.
Enjoys board games.
In 2024, lipase was 30 U/L.
His friend lives with psoriasis.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
```

**near** (program answer: s; facts: roommate: current heart failure; present; current | patient: heart rate = 79; present; current)
```
Male patient of 72 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Drives a car.
Sleeps seven hours a night.
Prefers to be addressed by first name.
His roommate burned a hand on a stove years ago.
Photographs local wildlife.
His sister sprained a thumb last month.
During a checkup in 2013, free T3 was 3.2 pg/mL.
Paints watercolors as a hobby.
Sees a dentist yearly.
His roommate has a lazy eye.
His roommate is treated for heart failure.
Heart rate now 79/min on a pulse check.
During a checkup in 2008, total protein was 7.0 g/dL.
Enjoys board games.
In 2024, lipase was 30 U/L.
His friend lives with psoriasis.
Prefers morning appointments.
Knits as a hobby.
Teeth in good repair.
```

**pres** (program answer: s; facts: patient: heart rate = 79; present; current | patient: current heart failure; absent; current)
```
Man of 72 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
During a checkup in 2008, total protein was 7.0 g/dL.
Sees a dentist yearly.
Knits as a hobby.
Enjoys board games.
Prefers to be addressed by first name.
Prefers morning appointments.
His roommate burned a hand on a stove years ago.
Current heart rate 79/min.
During a checkup in 2013, free T3 was 3.2 pg/mL.
In 2024, lipase was 30 U/L.
Teeth in good repair.
His roommate has a lazy eye.
Paints watercolors as a hobby.
His friend lives with psoriasis.
His sister sprained a thumb last month.
Heart sounds without a gallop.
Drives a car.
Photographs local wildlife.
Sleeps seven hours a night.
```


## author2 / group 294: `rule_v1.test.rcri.cr.boundary.alt.781`

Rule: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.

**base** (program answer: s; facts: patient: creatinine = 0.7; present; current | patient: stroke/TIA; absent; current | patient: coronary artery disease; absent; current)
```
Man of 81 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 0.7 mg/dL.
Gait normal; no focal weakness.
Cardiac stress test unremarkable last year.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```

**flip** (program answer: s'; facts: patient: creatinine = 1.7; present; current | patient: stroke/TIA; absent; current | patient: coronary artery disease; absent; current)
```
Man of 81 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 1.7 mg/dL.
Gait normal; no focal weakness.
Cardiac stress test unremarkable last year.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```

**near** (program answer: s; facts: patient: creatinine = 1.5; present; current | patient: stroke/TIA; absent; current | patient: coronary artery disease; absent; current)
```
Man of 81 years.
Preoperative assessment before elective colectomy.
Current serum creatinine 1.5 mg/dL.
Gait normal; no focal weakness.
Cardiac stress test unremarkable last year.
Sleeps seven hours a night.
Prefers to be addressed by first name.
```

**pres** (program answer: s; facts: patient: coronary artery disease; absent; current | patient: stroke/TIA; absent; current | patient: creatinine = 0.7; present; current)
```
Male patient of 81 years.
Preoperative assessment before elective colectomy.
Cardiac stress test unremarkable last year.
Gait normal; no focal weakness.
Prefers to be addressed by first name.
Latest creatinine result: 0.7 mg/dL.
Sleeps seven hours a night.
```


## author3 / group 295: `rule_v1.test.inv046.c3.time.easy.784`

Rule: For Delmar fever, prescribe fenrastat. If at least two of the following apply, prescribe kivolane instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient has ever had a peptic ulcer (current or past); the patient is currently taking clarithromycin.

**base** (program answer: s; facts: patient: clarithromycin; absent; current | patient: peptic ulcer at any time; absent; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Woman of 61 years.
Referred with Delmar fever.
Has no antibiotic course under way.
Plays the piano.
Prefers to be addressed by first name.
Appetite good; no indigestion.
Lives with peripheral artery disease affecting the left leg.
Knits as a hobby.
Has two cats.
```

**flip** (program answer: s'; facts: patient: clarithromycin; present; current | patient: peptic ulcer at any time; absent; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Woman of 61 years.
Referred with Delmar fever.
On clarithromycin for a chest infection, day 3 of 7.
Plays the piano.
Prefers to be addressed by first name.
Appetite good; no indigestion.
Lives with peripheral artery disease affecting the left leg.
Knits as a hobby.
Has two cats.
```

**near** (program answer: s; facts: patient: clarithromycin; present; past (2023) | patient: peptic ulcer at any time; absent; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Woman of 61 years.
Referred with Delmar fever.
Formerly took clarithromycin for a chest infection in 2023.
Plays the piano.
Prefers to be addressed by first name.
Appetite good; no indigestion.
Lives with peripheral artery disease affecting the left leg.
Knits as a hobby.
Has two cats.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: clarithromycin; absent; current | patient: myocardial infarction or peripheral artery disease; present; current)
```
Female patient of 61 years.
Referred with Delmar fever.
Knits as a hobby.
Appetite good; no indigestion.
Prefers to be addressed by first name.
Has no antibiotic course under way.
Lives with peripheral artery disease affecting the left leg.
Has two cats.
Plays the piano.
```


## author4 / group 296: `rule_v1.test.inv027.c1.negation.easy.795`

Rule: For Tessaly disease, prescribe velimor. If the patient is allergic to penicillin, prescribe quantrel instead.

**base** (program answer: s; facts: patient: penicillin allergy; absent; current)
```
Man of 33 years.
Referred with Tessaly disease.
Sleeps seven hours a night.
Reports no allergies to medicines.
Sees a dentist yearly.
Plays the piano.
```

**flip** (program answer: s'; facts: patient: penicillin allergy; present; current)
```
Man of 33 years.
Referred with Tessaly disease.
Sleeps seven hours a night.
Penicillin allergy: anaphylaxis.
Sees a dentist yearly.
Plays the piano.
```

**near** (program answer: s; facts: patient: penicillin allergy; absent; current)
```
Man of 33 years.
Referred with Tessaly disease.
Sleeps seven hours a night.
Has never been allergic to penicillin.
Sees a dentist yearly.
Plays the piano.
```

**pres** (program answer: s; facts: patient: penicillin allergy; absent; current)
```
Male patient of 33 years.
Referred with Tessaly disease.
Plays the piano.
Reports no allergies to medicines.
Sees a dentist yearly.
Sleeps seven hours a night.
```


## author1 / group 297: `rule_v1.test.gs038.c1.negation.long.667`

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.

**base** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: blood urea nitrogen = 24; present; current)
```
Man of 79 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
In 2011, folate was 12 ng/mL.
Prefers morning appointments.
Teeth in good repair.
Sleeps seven hours a night.
His friend has recovered from a dislocated finger.
Appetite good; no indigestion.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2021.
Plays the piano.
Enjoys board games.
Photographs local wildlife.
Uses sunscreen in summer.
Sees a dentist yearly.
Blood urea nitrogen now: 24 mg/dL.
Has two cats.
Pupils equal and reactive to light.
Drives a car.
His friend wears contact lenses.
```

**flip** (program answer: s'; facts: patient: peptic ulcer at any time; present; current | patient: blood urea nitrogen = 24; present; current)
```
Man of 79 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
In 2011, folate was 12 ng/mL.
Prefers morning appointments.
Teeth in good repair.
Sleeps seven hours a night.
His friend has recovered from a dislocated finger.
Has an active duodenal ulcer.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2021.
Plays the piano.
Enjoys board games.
Photographs local wildlife.
Uses sunscreen in summer.
Sees a dentist yearly.
Blood urea nitrogen now: 24 mg/dL.
Has two cats.
Pupils equal and reactive to light.
Drives a car.
His friend wears contact lenses.
```

**near** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: blood urea nitrogen = 24; present; current)
```
Man of 79 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
In 2011, folate was 12 ng/mL.
Prefers morning appointments.
Teeth in good repair.
Sleeps seven hours a night.
His friend has recovered from a dislocated finger.
Has never had a peptic ulcer.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Zinc of 85 mcg/dL in 2021.
Plays the piano.
Enjoys board games.
Photographs local wildlife.
Uses sunscreen in summer.
Sees a dentist yearly.
Blood urea nitrogen now: 24 mg/dL.
Has two cats.
Pupils equal and reactive to light.
Drives a car.
His friend wears contact lenses.
```

**pres** (program answer: s; facts: patient: peptic ulcer at any time; absent; current | patient: blood urea nitrogen = 24; present; current)
```
Male patient of 79 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
His friend has recovered from a dislocated finger.
Prefers morning appointments.
Plays the piano.
In 2011, folate was 12 ng/mL.
Sleeps seven hours a night.
Has two cats.
During a checkup in 2005, free T3 was 3.2 pg/mL.
Appetite good; no indigestion.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Pupils equal and reactive to light.
Blood urea nitrogen 24 mg/dL on the current labs.
Drives a car.
Zinc of 85 mcg/dL in 2021.
His friend wears contact lenses.
Photographs local wildlife.
Uses sunscreen in summer.
```


## author2 / group 298: `rule_v1.test.gs035.c2.numeric.long.543`

Rule: For contraception, prescribe a combined oral contraceptive. If at least two of the following apply, prescribe a progestin-only pill instead: the patient currently has heart failure; the age of the patient is 75 years or more; the patient has had cancer at any time (active or in remission).

**base** (program answer: s; facts: patient: cancer at any time; present; current | patient: age = 61; present; current)
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

**flip** (program answer: s'; facts: patient: cancer at any time; present; current | patient: age = 87; present; current)
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

**near** (program answer: s; facts: patient: cancer at any time; present; current | patient: age = 74; present; current)
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

**pres** (program answer: s; facts: patient: cancer at any time; present; current | patient: age = 61; present; current)
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

**missing** (program answer: neither; facts: patient: cancer at any time; present; current)
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


## author3 / group 299: `rule_v1.test.gs219.c2.time.superseded.199`

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

**base** (program answer: s; facts: patient: tonsillar exudate; present; current | patient: serum potassium = 4.5; present; past | patient: serum potassium = 4.3; present; current)
```
Man of 48 years.
Acute low back pain after lifting.
Tonsils swollen and coated with yellow exudate.
Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it.
Latest potassium result: 4.3 mmol/L.
Plays the piano.
Prefers to be addressed by first name.
```

**flip** (program answer: s'; facts: patient: tonsillar exudate; present; current | patient: serum potassium = 4.5; present; past | patient: serum potassium = 5.3; present; current)
```
Man of 48 years.
Acute low back pain after lifting.
Tonsils swollen and coated with yellow exudate.
Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it.
Latest potassium result: 5.3 mmol/L.
Plays the piano.
Prefers to be addressed by first name.
```

**near** (program answer: s; facts: patient: tonsillar exudate; present; current | patient: serum potassium = 5.6; present; past | patient: serum potassium = 4.3; present; current)
```
Man of 48 years.
Acute low back pain after lifting.
Tonsils swollen and coated with yellow exudate.
Last month, serum potassium was 5.6 mmol/L; the newest measurement replaces it.
Latest potassium result: 4.3 mmol/L.
Plays the piano.
Prefers to be addressed by first name.
```

**pres** (program answer: s; facts: patient: tonsillar exudate; present; current | patient: serum potassium = 4.5; present; past | patient: serum potassium = 4.3; present; current)
```
Male patient of 48 years.
Acute low back pain after lifting.
Prefers to be addressed by first name.
Tonsils swollen and coated with yellow exudate.
Plays the piano.
Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it.
Current serum potassium 4.3 mmol/L.
```


## author4 / group 300: `rule_v1.test.s1_adrop.confusion.negation.easy.1988`

Rule: A-DROP (as used here, partial): 1 point each for a current blood urea nitrogen of 21 mg/dL or more; a current oxygen saturation of 90% or less; new confusion or disorientation; a current systolic blood pressure of 90 mmHg or less. Age is scored separately and is not part of this question.

**base** (program answer: s; facts: patient: blood urea nitrogen = 13; present; current | patient: new confusion; absent; current | patient: systolic blood pressure = 105; present; current | patient: oxygen saturation = 99; present; current)
```
Male patient of 74 years.
Fever and cough with new consolidation on chest radiograph.
Blood urea nitrogen now: 13 mg/dL.
Gives a clear account of the illness.
Photographs local wildlife.
Observations now: blood pressure 105/73 mmHg.
Current oxygen saturation 99%.
```

**flip** (program answer: s'; facts: patient: blood urea nitrogen = 13; present; current | patient: new confusion; present; current | patient: systolic blood pressure = 105; present; current | patient: oxygen saturation = 99; present; current)
```
Male patient of 74 years.
Fever and cough with new consolidation on chest radiograph.
Blood urea nitrogen now: 13 mg/dL.
Disoriented to time and place, which is new for the patient.
Photographs local wildlife.
Observations now: blood pressure 105/73 mmHg.
Current oxygen saturation 99%.
```

**near** (program answer: s; facts: patient: blood urea nitrogen = 13; present; current | patient: new confusion; absent; current | patient: systolic blood pressure = 105; present; current | patient: oxygen saturation = 99; present; current)
```
Male patient of 74 years.
Fever and cough with new consolidation on chest radiograph.
Blood urea nitrogen now: 13 mg/dL.
Confusion absent; answers questions appropriately.
Photographs local wildlife.
Observations now: blood pressure 105/73 mmHg.
Current oxygen saturation 99%.
```

**pres** (program answer: s; facts: patient: oxygen saturation = 99; present; current | patient: new confusion; absent; current | patient: blood urea nitrogen = 13; present; current | patient: systolic blood pressure = 105; present; current)
```
Man of 74 years.
Fever and cough with new consolidation on chest radiograph.
Latest oxygen saturation reading: 99%.
Gives a clear account of the illness.
Blood urea nitrogen 13 mg/dL on the current labs.
Current systolic blood pressure 105 mmHg.
Photographs local wildlife.
```
