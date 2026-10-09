# H1 sheet author3 (75 groups)

Read `README.md` first.

## G01

Rule: For musculoskeletal pain, prescribe ibuprofen. If the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time and the patient is allergic to penicillin, prescribe acetaminophen instead.

**A3-G01-C1**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
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

Facts (for q1, after q2 and q3):
- father: coronary artery disease present (current) [line: "Her father has known coronary artery disease."]
- patient: penicillin allergy present (past) [line: "Outgrew a penicillin allergy by 2021."]

**A3-G01-C2**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Female patient of 56 years.
Acute low back pain after lifting.
Lives in a second-floor apartment.
Drives a car.
Her father has known coronary artery disease.
Knits as a hobby.
Prefers to be addressed by first name.
```

Facts (for q1, after q2 and q3):
- father: coronary artery disease present (current) [line: "Her father has known coronary artery disease."]
- penicillin allergy: not mentioned (counts as absent)

**A3-G01-C3**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
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

Facts (for q1, after q2 and q3):
- father: coronary artery disease present (current) [line: "Her father has known coronary artery disease."]
- penicillin allergy: stated as unknown [line: "Penicillin allergy: status unclear from the records at hand."]

**A3-G01-C4**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
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

Facts (for q1, after q2 and q3):
- father: coronary artery disease present (current) [line: "Her father has known coronary artery disease."]
- patient: penicillin allergy present (current) [line: "Known penicillin allergy with angioedema."]

**A3-G01-C5**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Woman of 56 years.
Acute low back pain after lifting.
Drives a car.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Knits as a hobby.
Her father has known coronary artery disease.
```

Facts (for q1, after q2 and q3):
- father: coronary artery disease present (current) [line: "Her father has known coronary artery disease."]
- penicillin allergy: not mentioned (counts as absent)


## G02

Rule: For vaginal candidiasis, prescribe oral fluconazole. If at least two of the following apply, prescribe clotrimazole pessaries instead: the age of the patient is 70 years or more; the patient has ever had a peptic ulcer (current or past); the current heart rate is above 90/min.

**A3-G02-C1**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 82 (current) [line: "Heart rate now 82/min on a pulse check."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- patient: age = 60 (current) [line: "Currently aged 60 years."]

**A3-G02-C2**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 97 (current) [line: "Heart rate now 97/min on a pulse check."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- patient: age = 60 (current) [line: "Currently aged 60 years."]

**A3-G02-C3**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 82 (current) [line: "Current heart rate 82/min."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- patient: age = 60 (current) [line: "Current age 60 years."]

**A3-G02-C4**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 90 (current) [line: "Heart rate now 90/min on a pulse check."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- patient: age = 60 (current) [line: "Currently aged 60 years."]


## G03

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**A3-G03-C1**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Man of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Current ALT 73 U/L.
Lives in a second-floor apartment.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 73 (current) [line: "Current ALT 73 U/L."]

**A3-G03-C2**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Man of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Current ALT 37 U/L.
Lives in a second-floor apartment.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 37 (current) [line: "Current ALT 37 U/L."]

**A3-G03-C3**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Man of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Current ALT 116 U/L.
Lives in a second-floor apartment.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 116 (current) [line: "Current ALT 116 U/L."]

**A3-G03-C4**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Male patient of 37 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Lives in a second-floor apartment.
ALT now 37 U/L.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 37 (current) [line: "ALT now 37 U/L."]


## G04

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient has ever had heart failure (current or past); the current platelet count is below 50 x10^9/L; the current temperature is above 38.0 C.

**A3-G04-C1**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "platelet count below 50" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: platelet count = 245 (current) [line: "Current platelet count 245 x10^9/L."]
- patient: temperature = 36.5 (current) [line: "Temperature now 36.5 C (tympanic)."]

**A3-G04-C2**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "platelet count below 50" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: temperature = 36.5 (current) [line: "Current temperature 36.5 C."]
- patient: platelet count = 50 (current) [line: "Platelet count now 50 x10^9/L."]

**A3-G04-C3**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "platelet count below 50" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: temperature = 36.5 (current) [line: "Current temperature 36.5 C."]
- patient: platelet count = 41 (current) [line: "Platelet count now 41 x10^9/L."]

**A3-G04-C4**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "platelet count below 50" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: temperature = 36.5 (current) [line: "Current temperature 36.5 C."]
- patient: platelet count = 245 (current) [line: "Platelet count now 245 x10^9/L."]

**A3-G04-C5**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "platelet count below 50" does not hold for this patient. | s' = Under the rule, the condition "platelet count below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: temperature = 36.5 (current) [line: "Current temperature 36.5 C."]
- platelet count: not mentioned (unknown)


## G05

Rule: For community-acquired pneumonia treated at home, prescribe amoxicillin. If the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time and the patient has an active peptic ulcer, prescribe doxycycline instead.

**A3-G05-C1**

Claims: s = Prescribe amoxicillin. | s' = Prescribe doxycycline.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
Male patient of 76 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Active peptic ulcer disease.
Has two cats.
Sleeps seven hours a night.
Owns a bicycle.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- colorectal cancer: not mentioned (counts as absent)

**A3-G05-C2**

Claims: s = Prescribe amoxicillin. | s' = Prescribe doxycycline.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: colorectal cancer denied by name [line: "Has never had bowel cancer."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]

**A3-G05-C3**

Claims: s = Prescribe amoxicillin. | s' = Prescribe doxycycline.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
Man of 76 years.
Productive cough and fever; consolidation on chest radiograph.
Uses sunscreen in summer.
Owns a bicycle.
Sleeps seven hours a night.
Has two cats.
Active peptic ulcer disease.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- colorectal cancer: not mentioned (counts as absent)

**A3-G05-C4**

Claims: s = Prescribe amoxicillin. | s' = Prescribe doxycycline.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: colorectal cancer present (current) [line: "Colorectal cancer under active treatment."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]


## G06

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If the current eGFR is below 50 mL/min/1.73 m2, prescribe fondaparinux instead.

**A3-G06-C1**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
```
Woman of 85 years.
First day after elective total hip replacement.
Paints watercolors as a hobby.
Back in 2016, eGFR stood at 68 mL/min/1.73 m2.
Teeth in good repair.
eGFR now 49 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 68 (past) [line: "Back in 2016, eGFR stood at 68 mL/min/1.73 m2."]
- patient: eGFR = 49 (current) [line: "eGFR now 49 mL/min/1.73 m2."]

**A3-G06-C2**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
```
Woman of 85 years.
First day after elective total hip replacement.
Paints watercolors as a hobby.
Back in 2016, eGFR stood at 41 mL/min/1.73 m2.
Teeth in good repair.
eGFR now 55 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 41 (past) [line: "Back in 2016, eGFR stood at 41 mL/min/1.73 m2."]
- patient: eGFR = 55 (current) [line: "eGFR now 55 mL/min/1.73 m2."]

**A3-G06-C3**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
```
Female patient of 85 years.
First day after elective total hip replacement.
Current eGFR 55 mL/min/1.73 m2.
Paints watercolors as a hobby.
Records from 2016 list eGFR at 68 mL/min/1.73 m2.
Teeth in good repair.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 55 (current) [line: "Current eGFR 55 mL/min/1.73 m2."]
- patient: eGFR = 68 (past) [line: "Records from 2016 list eGFR at 68 mL/min/1.73 m2."]

**A3-G06-C4**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
```
Woman of 85 years.
First day after elective total hip replacement.
Paints watercolors as a hobby.
Back in 2016, eGFR stood at 68 mL/min/1.73 m2.
Teeth in good repair.
eGFR now 55 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 68 (past) [line: "Back in 2016, eGFR stood at 68 mL/min/1.73 m2."]
- patient: eGFR = 55 (current) [line: "eGFR now 55 mL/min/1.73 m2."]


## G07

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the patient has ever had diabetes (current or past) and the current serum creatinine is 1.5 mg/dL or more, prescribe naproxen with omeprazole instead.

**A3-G07-C1**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine at least 1.5" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine at least 1.5" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 0.6 (current) [line: "Current serum creatinine 0.6 mg/dL."]
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: serum creatinine = 1.9 (past) [line: "Back in 2021, serum creatinine stood at 1.9 mg/dL."]

**A3-G07-C2**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine at least 1.5" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine at least 1.5" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 0.6 (current) [line: "Current serum creatinine 0.6 mg/dL."]
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: serum creatinine = 1.1 (past) [line: "Back in 2021, serum creatinine stood at 1.1 mg/dL."]

**A3-G07-C3**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine at least 1.5" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine at least 1.5" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- serum creatinine: not mentioned (unknown)

**A3-G07-C4**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine at least 1.5" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine at least 1.5" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: serum creatinine = 1.1 (past) [line: "Records from 2021 list serum creatinine at 1.1 mg/dL."]
- patient: serum creatinine = 0.6 (current) [line: "Latest creatinine result: 0.6 mg/dL."]

**A3-G07-C5**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine at least 1.5" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine at least 1.5" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 1.7 (current) [line: "Current serum creatinine 1.7 mg/dL."]
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: serum creatinine = 1.1 (past) [line: "Back in 2021, serum creatinine stood at 1.1 mg/dL."]


## G08

Rule: For early Lyme disease, prescribe doxycycline. If the patient has ever had coronary artery disease (current or past) and the patient has an active peptic ulcer, prescribe amoxicillin instead.

**A3-G08-C1**

Claims: s = Prescribe doxycycline. | s' = Prescribe amoxicillin.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Has never had coronary artery disease.
Knits as a hobby.
Plays the piano.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: coronary artery disease denied by name [line: "Has never had coronary artery disease."]

**A3-G08-C2**

Claims: s = Prescribe doxycycline. | s' = Prescribe amoxicillin.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Coronary artery disease: unknown.
Knits as a hobby.
Plays the piano.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- coronary artery disease: stated as unknown [line: "Coronary artery disease: unknown."]

**A3-G08-C3**

Claims: s = Prescribe doxycycline. | s' = Prescribe amoxicillin.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Man of 53 years.
Erythema migrans rash ten days after a tick bite.
Plays the piano.
Knits as a hobby.
Cardiac stress test unremarkable last year.
Has an active duodenal ulcer.
Prefers to be addressed by first name.
```

Facts (for q1, after q2 and q3):
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]

**A3-G08-C4**

Claims: s = Prescribe doxycycline. | s' = Prescribe amoxicillin.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Cardiac stress test unremarkable last year.
Knits as a hobby.
Plays the piano.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Cardiac stress test unremarkable last year."]

**A3-G08-C5**

Claims: s = Prescribe doxycycline. | s' = Prescribe amoxicillin.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Male patient of 53 years.
Erythema migrans rash ten days after a tick bite.
Prefers to be addressed by first name.
Has an active duodenal ulcer.
Known coronary artery disease (two-vessel disease on angiography).
Knits as a hobby.
Plays the piano.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]


## G09

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

**A3-G09-C1**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
Man of 85 years.
Atrial fibrillation; anticoagulation indicated.
Prefers to be addressed by first name.
Coronary artery disease years ago, with angina that went away after bypass surgery.
Plays the piano.
Sleeps seven hours a night.
Current white cell count 13.3 x10^9/L.
```

Facts (for q1, after q2 and q3):
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: white cell count = 13.3 (current) [line: "Current white cell count 13.3 x10^9/L."]
- colorectal cancer: not mentioned (counts as absent)

**A3-G09-C2**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
```
Male patient of 85 years.
Atrial fibrillation; anticoagulation indicated.
Sleeps seven hours a night.
Prefers to be addressed by first name.
Plays the piano.
Latest WBC is 13.3 x10^9/L.
Coronary artery disease years ago, with angina that went away after bypass surgery.
```

Facts (for q1, after q2 and q3):
- patient: white cell count = 13.3 (current) [line: "Latest WBC is 13.3 x10^9/L."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- colorectal cancer: not mentioned (counts as absent)

**A3-G09-C3**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 13.3 (current) [line: "Latest WBC is 13.3 x10^9/L."]
- patient: colorectal cancer present (current) [line: "Colorectal cancer under active treatment."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]

**A3-G09-C4**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "colorectal cancer (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 13.3 (current) [line: "Latest WBC is 13.3 x10^9/L."]
- wife: colorectal cancer present (current) [line: "His wife is undergoing surgery for bowel cancer."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]


## G10

Rule: For dual antiplatelet therapy after a myocardial infarction, prescribe aspirin plus ticagrelor. If the current serum creatinine is above 2.0 mg/dL and the patient has ever had heart failure (current or past), prescribe aspirin plus clopidogrel instead.

**A3-G10-C1**

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
```
Woman of 45 years.
Recovering on the ward after a myocardial infarction treated with a stent.
Photographs local wildlife.
Current heart failure with ankle swelling.
Paints watercolors as a hobby.
Uses sunscreen in summer.
```

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- serum creatinine: not mentioned (unknown)

**A3-G10-C2**

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: serum creatinine = 1.2 (past) [line: "Back in 2018, serum creatinine stood at 1.2 mg/dL."]
- patient: serum creatinine = 2.2 (current) [line: "Current serum creatinine 2.2 mg/dL."]

**A3-G10-C3**

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: serum creatinine = 1.2 (past) [line: "Back in 2018, serum creatinine stood at 1.2 mg/dL."]
- patient: serum creatinine = 0.7 (current) [line: "Current serum creatinine 0.7 mg/dL."]

**A3-G10-C4**

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: serum creatinine = 2.4 (past) [line: "Back in 2018, serum creatinine stood at 2.4 mg/dL."]
- patient: serum creatinine = 0.7 (current) [line: "Current serum creatinine 0.7 mg/dL."]

**A3-G10-C5**

Claims: s = Prescribe aspirin plus ticagrelor. | s' = Prescribe aspirin plus clopidogrel.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 1.2 (past) [line: "Records from 2018 list serum creatinine at 1.2 mg/dL."]
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: serum creatinine = 0.7 (current) [line: "Latest creatinine result: 0.7 mg/dL."]


## G11

Rule: For contraception, prescribe a combined oral contraceptive. Score 2 points if the patient or a first-degree relative (parent, sibling or child) has had coronary artery disease at any time; 2 points if the current weight is 60 kg or less; 2 points if the current platelet count is below 50 x10^9/L; 1 point if the patient currently has tender anterior cervical lymph nodes. If the score is 7 or more, prescribe a progestin-only pill instead.

**A3-G11-C1**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: platelet count = 42 (current) [line: "Current platelet count 42 x10^9/L."]
- patient: weight = 56 (current) [line: "Current weight 56 kg."]
- father: coronary artery disease present (current) [line: "Her father has angina from coronary artery disease."]
- tender cervical lymph nodes: stated as unknown [line: "Tender cervical lymph nodes: unknown."]

**A3-G11-C2**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: platelet count = 42 (current) [line: "Current platelet count 42 x10^9/L."]
- patient: weight = 56 (current) [line: "Current weight 56 kg."]
- father: coronary artery disease present (current) [line: "Her father has angina from coronary artery disease."]
- sister: tender cervical lymph nodes present (current) [line: "Her sister currently has tender anterior cervical lymphadenopathy."]

**A3-G11-C3**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Neck palpation unremarkable."]
- patient: platelet count = 42 (current) [line: "Platelet count now 42 x10^9/L."]
- father: coronary artery disease present (current) [line: "Her father has angina from coronary artery disease."]
- patient: weight = 56 (current) [line: "Latest weight 56 kg."]

**A3-G11-C4**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: platelet count = 42 (current) [line: "Current platelet count 42 x10^9/L."]
- patient: weight = 56 (current) [line: "Current weight 56 kg."]
- father: coronary artery disease present (current) [line: "Her father has angina from coronary artery disease."]
- patient: tender cervical lymph nodes present (current) [line: "Tender, swollen lymph nodes in the front of the neck."]

**A3-G11-C5**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: platelet count = 42 (current) [line: "Current platelet count 42 x10^9/L."]
- patient: weight = 56 (current) [line: "Current weight 56 kg."]
- father: coronary artery disease present (current) [line: "Her father has angina from coronary artery disease."]
- tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Neck palpation unremarkable."]


## G12

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**A3-G12-C1**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: ALT = 36 (current) [line: "ALT now 36 U/L."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]

**A3-G12-C2**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: ALT = 143 (current) [line: "ALT now 143 U/L."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]

**A3-G12-C3**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
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

Facts (for q1, after q2 and q3):
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: ALT = 36 (current) [line: "Current ALT 36 U/L."]

**A3-G12-C4**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- ALT: not mentioned (unknown)

**A3-G12-C5**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: ALT = 120 (current) [line: "ALT now 120 U/L."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]


## G13

Rule: ORBIT bleeding score (as used here, partial): 2 points for a major bleeding event at any time; 1 point each for a current age of 75 years or more, a current eGFR below 75 mL/min/1.73 m2, and current use of aspirin. Other ORBIT items are not part of this question.

**A3-G13-C1**

Claims: s = The eGFR criterion contributes 0 points. | s' = The eGFR criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: age = 56 (current) [line: "Currently aged 56 years."]
- patient: eGFR = 96 (current) [line: "eGFR now 96 mL/min/1.73 m2."]
- aspirin use: not named; a general line implies absence (counts as absent) [line: "Antiplatelet therapy: none at present."]
- bleeding history: not named; a general line implies absence (counts as absent) [line: "Examination shows no signs of blood loss."]

**A3-G13-C2**

Claims: s = The eGFR criterion contributes 0 points. | s' = The eGFR criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- aspirin use: not named; a general line implies absence (counts as absent) [line: "Antiplatelet therapy: none at present."]
- bleeding history: not named; a general line implies absence (counts as absent) [line: "Examination shows no signs of blood loss."]
- patient: age = 56 (current) [line: "Current age 56 years."]
- patient: eGFR = 77 (current) [line: "Current eGFR 77 mL/min/1.73 m2."]

**A3-G13-C3**

Claims: s = The eGFR criterion contributes 0 points. | s' = The eGFR criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- aspirin use: not named; a general line implies absence (counts as absent) [line: "Antiplatelet therapy: none at present."]
- bleeding history: not named; a general line implies absence (counts as absent) [line: "Examination shows no signs of blood loss."]
- patient: age = 56 (current) [line: "Current age 56 years."]
- patient: eGFR = 96 (current) [line: "Current eGFR 96 mL/min/1.73 m2."]

**A3-G13-C4**

Claims: s = The eGFR criterion contributes 0 points. | s' = The eGFR criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- aspirin use: not named; a general line implies absence (counts as absent) [line: "Antiplatelet therapy: none at present."]
- bleeding history: not named; a general line implies absence (counts as absent) [line: "Examination shows no signs of blood loss."]
- patient: age = 56 (current) [line: "Current age 56 years."]
- patient: eGFR = 73 (current) [line: "Current eGFR 73 mL/min/1.73 m2."]


## G14

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**A3-G14-C1**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current eGFR 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Prefers to be addressed by first name.
Latest WBC is 5.1 x10^9/L.
Heart rate now 89/min on a pulse check.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 80 (current) [line: "Current eGFR 80 mL/min/1.73 m2."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: white cell count = 5.1 (current) [line: "Latest WBC is 5.1 x10^9/L."]
- patient: heart rate = 89 (current) [line: "Heart rate now 89/min on a pulse check."]

**A3-G14-C2**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Female patient of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Prefers to be addressed by first name.
eGFR now 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Current white cell count 5.1 x10^9/L.
Current heart rate 63/min.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 80 (current) [line: "eGFR now 80 mL/min/1.73 m2."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: white cell count = 5.1 (current) [line: "Current white cell count 5.1 x10^9/L."]
- patient: heart rate = 63 (current) [line: "Current heart rate 63/min."]

**A3-G14-C3**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current eGFR 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Prefers to be addressed by first name.
Latest WBC is 5.1 x10^9/L.
Heart rate now 63/min on a pulse check.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 80 (current) [line: "Current eGFR 80 mL/min/1.73 m2."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: white cell count = 5.1 (current) [line: "Latest WBC is 5.1 x10^9/L."]
- patient: heart rate = 63 (current) [line: "Heart rate now 63/min on a pulse check."]

**A3-G14-C4**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
```
Woman of 84 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current eGFR 80 mL/min/1.73 m2.
Recurrent angioedema, under allergy follow-up.
Prefers to be addressed by first name.
Latest WBC is 5.1 x10^9/L.
Heart rate now 99/min on a pulse check.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 80 (current) [line: "Current eGFR 80 mL/min/1.73 m2."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: white cell count = 5.1 (current) [line: "Latest WBC is 5.1 x10^9/L."]
- patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]


## G15

Rule: For suspected infection on the medical ward, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous piperacillin-tazobactam instead: the age of the patient is 65 years or more; the patient has ever had a peptic ulcer (current or past); the patient has ever had a myocardial infarction or peripheral artery disease (current or past).

**A3-G15-C1**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
```
Woman, adult.
Suspected chest infection; assessed on the medical ward.
Walks without calf pain.
Prefers morning appointments.
Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone.
Teeth in good repair.
Has two cats.
```

Facts (for q1, after q2 and q3):
- myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]
- patient: peptic ulcer present (past) [line: "Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone."]
- age: not mentioned (unknown)

**A3-G15-C2**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
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

Facts (for q1, after q2 and q3):
- myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]
- patient: peptic ulcer present (past) [line: "Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone."]
- patient: age = 53 (current) [line: "Current age 53 years."]

**A3-G15-C3**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
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

Facts (for q1, after q2 and q3):
- myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]
- patient: peptic ulcer present (past) [line: "Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone."]
- patient: age = 62 (current) [line: "Current age 62 years."]

**A3-G15-C4**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
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

Facts (for q1, after q2 and q3):
- myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]
- patient: peptic ulcer present (past) [line: "Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone."]
- patient: age = 65 (current) [line: "Current age 65 years."]

**A3-G15-C5**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous piperacillin-tazobactam.

Criterion claims: s = Under the rule, the condition "age at least 65" does not hold for this patient. | s' = Under the rule, the condition "age at least 65" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (past) [line: "Formerly treated for a peptic ulcer; endoscopy in 2010 showed it had gone."]
- myocardial infarction or peripheral artery disease: not named; a general line implies absence (counts as absent) [line: "Walks without calf pain."]
- patient: age = 53 (current) [line: "Currently aged 53 years."]


## G16

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**A3-G16-C1**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
```
Man of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 15/min.
Newly disoriented and unable to give a clear history.
Current systolic blood pressure 128 mmHg.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: respiratory rate = 15 (current) [line: "Observations now: respiratory rate 15/min."]
- patient: altered mentation present (current) [line: "Newly disoriented and unable to give a clear history."]
- patient: systolic blood pressure = 128 (current) [line: "Current systolic blood pressure 128 mmHg."]

**A3-G16-C2**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
```
Man of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 15/min.
Was confused for a day after surgery years ago; recovered fully.
Current systolic blood pressure 128 mmHg.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: respiratory rate = 15 (current) [line: "Observations now: respiratory rate 15/min."]
- patient: altered mentation present (past) [line: "Was confused for a day after surgery years ago; recovered fully."]
- patient: systolic blood pressure = 128 (current) [line: "Current systolic blood pressure 128 mmHg."]

**A3-G16-C3**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
```
Man of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: respiratory rate 15/min.
Gives a clear account of the illness.
Current systolic blood pressure 128 mmHg.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: respiratory rate = 15 (current) [line: "Observations now: respiratory rate 15/min."]
- altered mentation: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]
- patient: systolic blood pressure = 128 (current) [line: "Current systolic blood pressure 128 mmHg."]

**A3-G16-C4**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
```
Male patient of 48 years.
Suspected urinary sepsis, assessed in the emergency department.
Observations now: blood pressure 128/85 mmHg.
Gives a clear account of the illness.
Paints watercolors as a hobby.
Current respiratory rate 15/min.
```

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 128 (current) [line: "Observations now: blood pressure 128/85 mmHg."]
- altered mentation: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]
- patient: respiratory rate = 15 (current) [line: "Current respiratory rate 15/min."]


## G17

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**A3-G17-C1**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 68 (current) [line: "Current heart rate 68/min."]
- angioedema: stated as unknown [line: "Angioedema: unknown."]
- patient: white cell count = 9.8 (current) [line: "Current white cell count 9.8 x10^9/L."]
- patient: eGFR = 41 (current) [line: "eGFR now 41 mL/min/1.73 m2."]

**A3-G17-C2**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 68 (current) [line: "Current heart rate 68/min."]
- angioedema: not named; a general line implies absence (counts as absent) [line: "Free of facial or oropharyngeal edema."]
- patient: white cell count = 9.8 (current) [line: "Current white cell count 9.8 x10^9/L."]
- patient: eGFR = 41 (current) [line: "eGFR now 41 mL/min/1.73 m2."]

**A3-G17-C3**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 68 (current) [line: "Current heart rate 68/min."]
- patient: angioedema present (past) [line: "Formerly had recurrent angioedema, in remission for many years now."]
- patient: white cell count = 9.8 (current) [line: "Current white cell count 9.8 x10^9/L."]
- patient: eGFR = 41 (current) [line: "eGFR now 41 mL/min/1.73 m2."]

**A3-G17-C4**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 68 (current) [line: "Current heart rate 68/min."]
- father: angioedema present (past) [line: "His father had an attack of angioedema years ago."]
- patient: white cell count = 9.8 (current) [line: "Current white cell count 9.8 x10^9/L."]
- patient: eGFR = 41 (current) [line: "eGFR now 41 mL/min/1.73 m2."]

**A3-G17-C5**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- angioedema: not named; a general line implies absence (counts as absent) [line: "Free of facial or oropharyngeal edema."]
- patient: heart rate = 68 (current) [line: "Heart rate now 68/min on a pulse check."]
- patient: white cell count = 9.8 (current) [line: "Latest WBC is 9.8 x10^9/L."]
- patient: eGFR = 41 (current) [line: "Current eGFR 41 mL/min/1.73 m2."]


## G18

Rule: For primary prevention, start atorvastatin. If the current ALT is above 80 U/L, start ezetimibe instead.

**A3-G18-C1**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Photographs local wildlife.
Current ALT 25 U/L.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 25 (current) [line: "Current ALT 25 U/L."]

**A3-G18-C2**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Female patient of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
ALT now 25 U/L.
Photographs local wildlife.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 25 (current) [line: "ALT now 25 U/L."]

**A3-G18-C3**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Photographs local wildlife.
Current ALT 77 U/L.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 77 (current) [line: "Current ALT 77 U/L."]

**A3-G18-C4**

Claims: s = Start atorvastatin. | s' = Start ezetimibe.

Criterion claims: s = Under the rule, the condition "ALT above 80" does not hold for this patient. | s' = Under the rule, the condition "ALT above 80" holds for this patient.
```
Woman of 58 years.
Primary prevention; LDL cholesterol 182 mg/dL.
Photographs local wildlife.
Current ALT 94 U/L.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 94 (current) [line: "Current ALT 94 U/L."]


## G19

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 30 mL/min/1.73 m2 and the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time, prescribe a progestin-only pill instead.

**A3-G19-C1**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
eGFR now 17 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- father: diabetes present (past) [line: "Her father had diabetes years ago that went away after a change in diet."]
- patient: eGFR = 17 (current) [line: "eGFR now 17 mL/min/1.73 m2."]

**A3-G19-C2**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
eGFR now 30 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- father: diabetes present (past) [line: "Her father had diabetes years ago that went away after a change in diet."]
- patient: eGFR = 30 (current) [line: "eGFR now 30 mL/min/1.73 m2."]

**A3-G19-C3**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Female patient of 19 years.
Requests contraception.
Her father had diabetes years ago that went away after a change in diet.
Has two cats.
Current eGFR 89 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- father: diabetes present (past) [line: "Her father had diabetes years ago that went away after a change in diet."]
- patient: eGFR = 89 (current) [line: "Current eGFR 89 mL/min/1.73 m2."]

**A3-G19-C4**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
```

Facts (for q1, after q2 and q3):
- father: diabetes present (past) [line: "Her father had diabetes years ago that went away after a change in diet."]
- eGFR: not mentioned (unknown)

**A3-G19-C5**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
```
Woman of 19 years.
Requests contraception.
Has two cats.
Her father had diabetes years ago that went away after a change in diet.
eGFR now 89 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- father: diabetes present (past) [line: "Her father had diabetes years ago that went away after a change in diet."]
- patient: eGFR = 89 (current) [line: "eGFR now 89 mL/min/1.73 m2."]


## G20

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. Score 1 point if the patient has ever had angioedema (current or past); 1 point if the patient has new confusion; 2 points if the current temperature is above 38.0 C; 2 points if the age of the patient is 65 years or more. If the score is 5 or more, prescribe intermittent pneumatic compression instead.

**A3-G20-C1**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
An adult man.
Admitted for community-acquired pneumonia; immobile.
Current temperature 39.1 C.
Currently aged 68 years.
Prefers morning appointments.
Speech clear; follows commands.
An episode of angioedema years ago, with full recovery.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 39.1 (current) [line: "Current temperature 39.1 C."]
- patient: age = 68 (current) [line: "Currently aged 68 years."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]

**A3-G20-C2**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
An adult man.
Admitted for community-acquired pneumonia; immobile.
Current temperature 37.4 C.
Currently aged 68 years.
Prefers morning appointments.
Speech clear; follows commands.
An episode of angioedema years ago, with full recovery.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 37.4 (current) [line: "Current temperature 37.4 C."]
- patient: age = 68 (current) [line: "Currently aged 68 years."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]

**A3-G20-C3**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Man, adult.
Admitted for community-acquired pneumonia; immobile.
An episode of angioedema years ago, with full recovery.
Speech clear; follows commands.
Temperature now 37.4 C (tympanic).
Prefers morning appointments.
Current age 68 years.
```

Facts (for q1, after q2 and q3):
- patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: temperature = 37.4 (current) [line: "Temperature now 37.4 C (tympanic)."]
- patient: age = 68 (current) [line: "Current age 68 years."]

**A3-G20-C4**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
An adult man.
Admitted for community-acquired pneumonia; immobile.
Current temperature 37.8 C.
Currently aged 68 years.
Prefers morning appointments.
Speech clear; follows commands.
An episode of angioedema years ago, with full recovery.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 37.8 (current) [line: "Current temperature 37.8 C."]
- patient: age = 68 (current) [line: "Currently aged 68 years."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]


## G21

Rule: For Zentha disease, prescribe valtimide. If the patient has ever had a stroke or TIA (current or past) and the current temperature is above 38.0 C, prescribe isomarin instead.

**A3-G21-C1**

Claims: s = Prescribe valtimide. | s' = Prescribe isomarin.

Criterion claims: s = Under the rule, the condition "stroke/TIA" does not hold for this patient. | s' = Under the rule, the condition "stroke/TIA" holds for this patient.
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

Facts (for q1, after q2 and q3):
- roommate: stroke/TIA present (past) [line: "Her roommate had a TIA years ago."]
- patient: temperature = 38.4 (current) [line: "Temperature now 38.4 C (tympanic)."]

**A3-G21-C2**

Claims: s = Prescribe valtimide. | s' = Prescribe isomarin.

Criterion claims: s = Under the rule, the condition "stroke/TIA" does not hold for this patient. | s' = Under the rule, the condition "stroke/TIA" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: temperature = 38.4 (current) [line: "Temperature now 38.4 C (tympanic)."]
- stroke/TIA: not mentioned (counts as absent)

**A3-G21-C3**

Claims: s = Prescribe valtimide. | s' = Prescribe isomarin.

Criterion claims: s = Under the rule, the condition "stroke/TIA" does not hold for this patient. | s' = Under the rule, the condition "stroke/TIA" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: stroke/TIA present (past) [line: "TIA years ago, with full recovery."]
- patient: temperature = 38.4 (current) [line: "Temperature now 38.4 C (tympanic)."]

**A3-G21-C4**

Claims: s = Prescribe valtimide. | s' = Prescribe isomarin.

Criterion claims: s = Under the rule, the condition "stroke/TIA" does not hold for this patient. | s' = Under the rule, the condition "stroke/TIA" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: temperature = 38.4 (current) [line: "Current temperature 38.4 C."]
- stroke/TIA: not mentioned (counts as absent)


## G22

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**A3-G22-C1**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Abdomen soft and non-tender."]
- patient: temperature = 38.7 (current) [line: "Current temperature 38.7 C."]

**A3-G22-C2**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Abdomen soft and non-tender."]
- patient: temperature = 38.7 (current) [line: "Temperature now 38.7 C (tympanic)."]

**A3-G22-C3**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- patient: temperature = 38.7 (current) [line: "Current temperature 38.7 C."]

**A3-G22-C4**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "peptic ulcer at any time" does not hold for this patient. | s' = Under the rule, the condition "peptic ulcer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- friend: peptic ulcer present (current) [line: "His friend has peptic ulcer disease."]
- patient: temperature = 38.7 (current) [line: "Current temperature 38.7 C."]


## G23

Rule: For Pallis disease, prescribe brexadol. If the patient has had cancer at any time (active or in remission) or the current white cell count is above 12.0 x10^9/L, prescribe corlitane instead.

**A3-G23-C1**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]
- patient: white cell count = 5.7 (current) [line: "Latest WBC is 5.7 x10^9/L."]

**A3-G23-C2**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: cancer denied by name [line: "Free of cancer throughout life."]
- patient: white cell count = 5.7 (current) [line: "Latest WBC is 5.7 x10^9/L."]

**A3-G23-C3**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]
- patient: white cell count = 5.7 (current) [line: "Current white cell count 5.7 x10^9/L."]

**A3-G23-C4**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "cancer at any time" does not hold for this patient. | s' = Under the rule, the condition "cancer at any time" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: cancer present (current) [line: "Has melanoma skin cancer and is receiving treatment for it."]
- patient: white cell count = 5.7 (current) [line: "Latest WBC is 5.7 x10^9/L."]


## G24

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. If the current temperature is above 38.0 C and the patient has ever had a peptic ulcer (current or past), prescribe warfarin instead.

**A3-G24-C1**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Woman of 50 years.
Atrial fibrillation; anticoagulation indicated.
Last month, temperature was 37.2 C; the newest measurement replaces it.
Has an active duodenal ulcer.
Temperature now 37.3 C (tympanic).
Has two cats.
Teeth in good repair.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 37.2 (past) [line: "Last month, temperature was 37.2 C; the newest measurement replaces it."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: temperature = 37.3 (current) [line: "Temperature now 37.3 C (tympanic)."]

**A3-G24-C2**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Female patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Current temperature 37.3 C.
Has an active duodenal ulcer.
Last month, temperature was 39.2 C; the newest measurement replaces it.
Has two cats.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 37.3 (current) [line: "Current temperature 37.3 C."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: temperature = 39.2 (past) [line: "Last month, temperature was 39.2 C; the newest measurement replaces it."]

**A3-G24-C3**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Female patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Current temperature 39.1 C.
Has an active duodenal ulcer.
Last month, temperature was 37.2 C; the newest measurement replaces it.
Has two cats.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 39.1 (current) [line: "Current temperature 39.1 C."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: temperature = 37.2 (past) [line: "Last month, temperature was 37.2 C; the newest measurement replaces it."]

**A3-G24-C4**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "temperature above 38.0" does not hold for this patient. | s' = Under the rule, the condition "temperature above 38.0" holds for this patient.
```
Female patient of 50 years.
Atrial fibrillation; anticoagulation indicated.
Teeth in good repair.
Current temperature 37.3 C.
Has an active duodenal ulcer.
Last month, temperature was 37.2 C; the newest measurement replaces it.
Has two cats.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 37.3 (current) [line: "Current temperature 37.3 C."]
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: temperature = 37.2 (past) [line: "Last month, temperature was 37.2 C; the newest measurement replaces it."]


## G25

Rule: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

**A3-G25-C1**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: heart rate = 96 (current) [line: "Heart rate now 96/min on a pulse check."]
- patient: eGFR = 42 (current) [line: "Current eGFR 42 mL/min/1.73 m2."]

**A3-G25-C2**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: heart rate = 96 (current) [line: "Heart rate now 96/min on a pulse check."]
- patient: eGFR = 45 (current) [line: "Current eGFR 45 mL/min/1.73 m2."]

**A3-G25-C3**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: heart rate = 96 (current) [line: "Heart rate now 96/min on a pulse check."]
- patient: eGFR = 55 (current) [line: "Current eGFR 55 mL/min/1.73 m2."]

**A3-G25-C4**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: eGFR = 55 (current) [line: "eGFR now 55 mL/min/1.73 m2."]
- patient: heart rate = 96 (current) [line: "Current heart rate 96/min."]

**A3-G25-C5**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "eGFR below 45" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 45" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: heart rate = 96 (current) [line: "Heart rate now 96/min on a pulse check."]
- eGFR: not mentioned (unknown)


## G26

Rule: AIMS65 (as used here, partial): 1 point each for a current international normalized ratio (INR) above 1.5; current altered mental status (confusion or disorientation); a current systolic blood pressure of 90 mmHg or less; age 65 years or more. Other AIMS65 items are not part of this question.

**A3-G26-C1**

Claims: s = The international normalized ratio criterion contributes 0 points. | s' = The international normalized ratio criterion contributes 1 point.
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Paints watercolors as a hobby.
Current international normalized ratio 2.3.
Observations now: blood pressure 105/73 mmHg.
Current age 46 years.
```

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 2.3 (current) [line: "Current international normalized ratio 2.3."]
- patient: systolic blood pressure = 105 (current) [line: "Observations now: blood pressure 105/73 mmHg."]
- patient: age = 46 (current) [line: "Current age 46 years."]
- altered mental status: not mentioned (counts as absent)

**A3-G26-C2**

Claims: s = The international normalized ratio criterion contributes 0 points. | s' = The international normalized ratio criterion contributes 1 point.
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Paints watercolors as a hobby.
Current international normalized ratio 1.2.
Observations now: blood pressure 105/73 mmHg.
Current age 46 years.
```

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.2 (current) [line: "Current international normalized ratio 1.2."]
- patient: systolic blood pressure = 105 (current) [line: "Observations now: blood pressure 105/73 mmHg."]
- patient: age = 46 (current) [line: "Current age 46 years."]
- altered mental status: not mentioned (counts as absent)

**A3-G26-C3**

Claims: s = The international normalized ratio criterion contributes 0 points. | s' = The international normalized ratio criterion contributes 1 point.
```
Woman, adult.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Paints watercolors as a hobby.
Current international normalized ratio 1.4.
Observations now: blood pressure 105/73 mmHg.
Current age 46 years.
```

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.4 (current) [line: "Current international normalized ratio 1.4."]
- patient: systolic blood pressure = 105 (current) [line: "Observations now: blood pressure 105/73 mmHg."]
- patient: age = 46 (current) [line: "Current age 46 years."]
- altered mental status: not mentioned (counts as absent)

**A3-G26-C4**

Claims: s = The international normalized ratio criterion contributes 0 points. | s' = The international normalized ratio criterion contributes 1 point.
```
An adult woman.
Upper gastrointestinal bleeding with black stools; admitted for endoscopy.
Current systolic blood pressure 105 mmHg.
Latest international normalized ratio (INR): 1.2.
Paints watercolors as a hobby.
Currently aged 46 years.
```

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 105 (current) [line: "Current systolic blood pressure 105 mmHg."]
- patient: international normalized ratio = 1.2 (current) [line: "Latest international normalized ratio (INR): 1.2."]
- patient: age = 46 (current) [line: "Currently aged 46 years."]
- altered mental status: not mentioned (counts as absent)


## G27

Rule: CHADS2 (as used here): 2 points for a stroke or TIA at any time; 1 point each for heart failure at any time, hypertension at any time, diabetes at any time, and a current age of 75 years or more.

**A3-G27-C1**

Claims: s = The diabetes criterion contributes 0 points. | s' = The diabetes criterion contributes 1 point.
```
Woman, adult.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Prefers morning appointments.
Sleeps seven hours a night.
Currently aged 51 years.
Power and sensation normal in all limbs.
Sees a dentist yearly.
```

Facts (for q1, after q2 and q3):
- patient: age = 51 (current) [line: "Currently aged 51 years."]
- stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]
- heart failure: not mentioned (counts as absent)
- hypertension: not mentioned (counts as absent)
- diabetes: not mentioned (counts as absent)

**A3-G27-C2**

Claims: s = The diabetes criterion contributes 0 points. | s' = The diabetes criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: age = 51 (current) [line: "Current age 51 years."]
- patient: diabetes present (past) [line: "Formerly diabetic; in remission since 2019."]
- stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]
- heart failure: not mentioned (counts as absent)
- hypertension: not mentioned (counts as absent)

**A3-G27-C3**

Claims: s = The diabetes criterion contributes 0 points. | s' = The diabetes criterion contributes 1 point.
```
An adult woman.
Newly diagnosed atrial fibrillation; anticoagulant therapy under discussion.
Sleeps seven hours a night.
Current age 51 years.
Prefers morning appointments.
Power and sensation normal in all limbs.
Sees a dentist yearly.
```

Facts (for q1, after q2 and q3):
- patient: age = 51 (current) [line: "Current age 51 years."]
- stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]
- heart failure: not mentioned (counts as absent)
- hypertension: not mentioned (counts as absent)
- diabetes: not mentioned (counts as absent)

**A3-G27-C4**

Claims: s = The diabetes criterion contributes 0 points. | s' = The diabetes criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: age = 51 (current) [line: "Current age 51 years."]
- father: diabetes present (past) [line: "Her father had diabetes years ago that went away after a change in diet."]
- stroke/TIA: not named; a general line implies absence (counts as absent) [line: "Power and sensation normal in all limbs."]
- heart failure: not mentioned (counts as absent)
- hypertension: not mentioned (counts as absent)


## G28

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).

**A3-G28-C1**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 78 (current) [line: "Heart rate now 78/min on a pulse check."]
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

**A3-G28-C2**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 78 (current) [line: "Current heart rate 78/min."]
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

**A3-G28-C3**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 87 (current) [line: "Heart rate now 87/min on a pulse check."]
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

**A3-G28-C4**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 104 (current) [line: "Heart rate now 104/min on a pulse check."]
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

**A3-G28-C5**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- heart rate: not mentioned (unknown)


## G29

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the patient has ever had diabetes (current or past) and the current white cell count is above 12.0 x10^9/L, prescribe diltiazem instead.

**A3-G29-C1**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 5.4 (current) [line: "Latest WBC is 5.4 x10^9/L."]

**A3-G29-C2**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 5.4 (current) [line: "Current white cell count 5.4 x10^9/L."]

**A3-G29-C3**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 12.0 (current) [line: "Latest WBC is 12.0 x10^9/L."]

**A3-G29-C4**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- white cell count: not mentioned (unknown)

**A3-G29-C5**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 13.9 (current) [line: "Latest WBC is 13.9 x10^9/L."]


## G30

Rule: For cellulitis of the lower leg, prescribe cephalexin. If at least two of the following apply, prescribe clindamycin instead: the patient has ever had a peptic ulcer (current or past); the current ALT is above 120 U/L; the patient has ever had a venous thromboembolism (current or past).

**A3-G30-C1**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 30 years.
Spreading redness and warmth of the right shin for two days.
Current ALT 155 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
Photographs local wildlife.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 155 (current) [line: "Current ALT 155 U/L."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G30-C2**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 30 years.
Spreading redness and warmth of the right shin for two days.
Current ALT 120 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
Photographs local wildlife.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 120 (current) [line: "Current ALT 120 U/L."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G30-C3**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 30 years.
Spreading redness and warmth of the right shin for two days.
Current ALT 25 U/L.
Duodenal ulcer years ago; recovered fully with treatment.
Photographs local wildlife.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 25 (current) [line: "Current ALT 25 U/L."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G30-C4**

Claims: s = Prescribe cephalexin. | s' = Prescribe clindamycin.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Male patient of 30 years.
Spreading redness and warmth of the right shin for two days.
ALT now 25 U/L.
Photographs local wildlife.
Duodenal ulcer years ago; recovered fully with treatment.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 25 (current) [line: "ALT now 25 U/L."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- venous thromboembolism: not mentioned (counts as absent)


## G31

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.

**A3-G31-C1**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Records from 2011 list blood urea nitrogen at 29 mg/dL.
Blood urea nitrogen now: 13 mg/dL.
Active peptic ulcer disease.
```

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 29 (past) [line: "Records from 2011 list blood urea nitrogen at 29 mg/dL."]
- patient: blood urea nitrogen = 13 (current) [line: "Blood urea nitrogen now: 13 mg/dL."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]

**A3-G31-C2**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Man of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Active peptic ulcer disease.
Blood urea nitrogen 13 mg/dL on the current labs.
Sees a dentist yearly.
Back in 2011, blood urea nitrogen stood at 15 mg/dL.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- patient: blood urea nitrogen = 13 (current) [line: "Blood urea nitrogen 13 mg/dL on the current labs."]
- patient: blood urea nitrogen = 15 (past) [line: "Back in 2011, blood urea nitrogen stood at 15 mg/dL."]

**A3-G31-C3**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Records from 2011 list blood urea nitrogen at 15 mg/dL.
Blood urea nitrogen now: 30 mg/dL.
Active peptic ulcer disease.
```

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 15 (past) [line: "Records from 2011 list blood urea nitrogen at 15 mg/dL."]
- patient: blood urea nitrogen = 30 (current) [line: "Blood urea nitrogen now: 30 mg/dL."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]

**A3-G31-C4**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Records from 2011 list blood urea nitrogen at 15 mg/dL.
Blood urea nitrogen now: 13 mg/dL.
Active peptic ulcer disease.
```

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 15 (past) [line: "Records from 2011 list blood urea nitrogen at 15 mg/dL."]
- patient: blood urea nitrogen = 13 (current) [line: "Blood urea nitrogen now: 13 mg/dL."]
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]

**A3-G31-C5**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
```
Male patient of 63 years.
Newly diagnosed hypertension (blood pressure 158/94 mmHg on repeated readings).
Sees a dentist yearly.
Paints watercolors as a hobby.
Active peptic ulcer disease.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Active peptic ulcer disease."]
- blood urea nitrogen: not mentioned (unknown)


## G32

Rule: BAP-65 (as used here, partial): 1 point each for a current blood urea nitrogen of 25 mg/dL or more; current altered mental status (confusion or disorientation); a current heart rate of 109/min or more. Age is scored separately and is not part of this question.

**A3-G32-C1**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 80 (current) [line: "Current heart rate 80/min."]
- patient: altered mental status denied by name [line: "Confusion absent; answers questions appropriately."]
- patient: blood urea nitrogen = 8 (current) [line: "Blood urea nitrogen 8 mg/dL on the current labs."]

**A3-G32-C2**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 8 (current) [line: "Blood urea nitrogen now: 8 mg/dL."]
- altered mental status: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: heart rate = 80 (current) [line: "Heart rate now 80/min on a pulse check."]

**A3-G32-C3**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 80 (current) [line: "Current heart rate 80/min."]
- altered mental status: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: blood urea nitrogen = 8 (current) [line: "Blood urea nitrogen 8 mg/dL on the current labs."]

**A3-G32-C4**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 80 (current) [line: "Current heart rate 80/min."]
- patient: altered mental status present (current) [line: "Newly disoriented and unable to give a clear history."]
- patient: blood urea nitrogen = 8 (current) [line: "Blood urea nitrogen 8 mg/dL on the current labs."]


## G33

Rule: For an acute gout flare, prescribe colchicine. If the current serum creatinine is above 2.0 mg/dL and the current heart rate is above 90/min, prescribe prednisone instead.

**A3-G33-C1**

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 1.4 (current) [line: "Current serum creatinine 1.4 mg/dL."]
- patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]

**A3-G33-C2**

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 2.9 (current) [line: "Current serum creatinine 2.9 mg/dL."]
- patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]

**A3-G33-C3**

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 99 (current) [line: "Current heart rate 99/min."]
- patient: serum creatinine = 1.4 (current) [line: "Latest creatinine result: 1.4 mg/dL."]

**A3-G33-C4**

Claims: s = Prescribe colchicine. | s' = Prescribe prednisone.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 1.8 (current) [line: "Current serum creatinine 1.8 mg/dL."]
- patient: heart rate = 99 (current) [line: "Heart rate now 99/min on a pulse check."]


## G34

Rule: For primary prevention, prescribe atorvastatin. If at least two of the following apply, prescribe ezetimibe instead: the current systolic blood pressure is above 160 mmHg; the age of the patient is 75 years or more; the patient has ever had asthma (current or past).

**A3-G34-C1**

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- patient: systolic blood pressure = 153 (current) [line: "Current systolic blood pressure 153 mmHg."]
- patient: age = 78 (current) [line: "Current age 78 years."]

**A3-G34-C2**

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- patient: systolic blood pressure = 137 (current) [line: "Current systolic blood pressure 137 mmHg."]
- patient: age = 78 (current) [line: "Current age 78 years."]

**A3-G34-C3**

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- patient: age = 78 (current) [line: "Current age 78 years."]
- systolic blood pressure: not mentioned (unknown)

**A3-G34-C4**

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- patient: systolic blood pressure = 168 (current) [line: "Current systolic blood pressure 168 mmHg."]
- patient: age = 78 (current) [line: "Current age 78 years."]

**A3-G34-C5**

Claims: s = Prescribe atorvastatin. | s' = Prescribe ezetimibe.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 137 (current) [line: "Observations now: blood pressure 137/90 mmHg."]
- patient: age = 78 (current) [line: "Currently aged 78 years."]
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]


## G35

Rule: For thromboprophylaxis after hip replacement, prescribe enoxaparin. If at least two of the following apply, prescribe fondaparinux instead: the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; the patient has ever had a peptic ulcer (current or past); the current weight is 60 kg or less.

**A3-G35-C1**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 56 years.
First day after elective total hip replacement.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 68 kg; the newest measurement replaces it.
Latest weight 60 kg.
Appetite good; no indigestion.
```

Facts (for q1, after q2 and q3):
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- patient: weight = 68 (past) [line: "Last month, weight was 68 kg; the newest measurement replaces it."]
- patient: weight = 60 (current) [line: "Latest weight 60 kg."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]

**A3-G35-C2**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 56 years.
First day after elective total hip replacement.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 55 kg; the newest measurement replaces it.
Latest weight 73 kg.
Appetite good; no indigestion.
```

Facts (for q1, after q2 and q3):
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- patient: weight = 55 (past) [line: "Last month, weight was 55 kg; the newest measurement replaces it."]
- patient: weight = 73 (current) [line: "Latest weight 73 kg."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]

**A3-G35-C3**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Woman of 56 years.
First day after elective total hip replacement.
Current weight 73 kg.
Appetite good; no indigestion.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 68 kg; the newest measurement replaces it.
```

Facts (for q1, after q2 and q3):
- patient: weight = 73 (current) [line: "Current weight 73 kg."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- patient: weight = 68 (past) [line: "Last month, weight was 68 kg; the newest measurement replaces it."]

**A3-G35-C4**

Claims: s = Prescribe enoxaparin. | s' = Prescribe fondaparinux.

Criterion claims: s = Under the rule, the condition "weight at or below 60" does not hold for this patient. | s' = Under the rule, the condition "weight at or below 60" holds for this patient.
```
Female patient of 56 years.
First day after elective total hip replacement.
Has two cats.
Has an acute pulmonary embolism, diagnosed this week.
Last month, weight was 68 kg; the newest measurement replaces it.
Latest weight 73 kg.
Appetite good; no indigestion.
```

Facts (for q1, after q2 and q3):
- patient: venous thromboembolism present (current) [line: "Has an acute pulmonary embolism, diagnosed this week."]
- patient: weight = 68 (past) [line: "Last month, weight was 68 kg; the newest measurement replaces it."]
- patient: weight = 73 (current) [line: "Latest weight 73 kg."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]


## G36

Rule: Simplified Pulmonary Embolism Severity Index (as used here, partial): 1 point each for active cancer; a current heart rate of 110/min or more; a current systolic blood pressure below 100 mmHg; a current oxygen saturation below 90%; an age above 80 years. Other items of the index are not part of this question.

**A3-G36-C1**

Claims: s = The active cancer criterion contributes 0 points. | s' = The active cancer criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 92 (current) [line: "Current heart rate 92/min."]
- patient: age = 57 (current) [line: "Current age 57 years."]
- patient: oxygen saturation = 100 (current) [line: "Current oxygen saturation 100%."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]
- patient: systolic blood pressure = 118 (current) [line: "Observations now: blood pressure 118/80 mmHg."]

**A3-G36-C2**

Claims: s = The active cancer criterion contributes 0 points. | s' = The active cancer criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 92 (current) [line: "Current heart rate 92/min."]
- patient: age = 57 (current) [line: "Current age 57 years."]
- patient: oxygen saturation = 100 (current) [line: "Current oxygen saturation 100%."]
- cancer: stated as unknown [line: "Active cancer: status unclear from the records at hand."]
- patient: systolic blood pressure = 118 (current) [line: "Observations now: blood pressure 118/80 mmHg."]

**A3-G36-C3**

Claims: s = The active cancer criterion contributes 0 points. | s' = The active cancer criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 92 (current) [line: "Heart rate now 92/min on a pulse check."]
- patient: age = 57 (current) [line: "Currently aged 57 years."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]
- patient: oxygen saturation = 100 (current) [line: "Latest oxygen saturation reading: 100%."]
- patient: systolic blood pressure = 118 (current) [line: "Current systolic blood pressure 118 mmHg."]

**A3-G36-C4**

Claims: s = The active cancer criterion contributes 0 points. | s' = The active cancer criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 92 (current) [line: "Current heart rate 92/min."]
- patient: age = 57 (current) [line: "Current age 57 years."]
- patient: oxygen saturation = 100 (current) [line: "Current oxygen saturation 100%."]
- patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]
- patient: systolic blood pressure = 118 (current) [line: "Observations now: blood pressure 118/80 mmHg."]

**A3-G36-C5**

Claims: s = The active cancer criterion contributes 0 points. | s' = The active cancer criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 92 (current) [line: "Current heart rate 92/min."]
- patient: age = 57 (current) [line: "Current age 57 years."]
- patient: oxygen saturation = 100 (current) [line: "Current oxygen saturation 100%."]
- friend: cancer present (current) [line: "His friend has lung cancer that has spread to the liver."]
- patient: systolic blood pressure = 118 (current) [line: "Observations now: blood pressure 118/80 mmHg."]


## G37

Rule: For heart failure with reduced ejection fraction, prescribe spironolactone. Score 2 points if the current white cell count is above 12.0 x10^9/L; 3 points if the patient has ever had angioedema (current or past); 2 points if the current eGFR is below 45 mL/min/1.73 m2; 1 point if the current heart rate is above 90/min. If the score is 4 or more, prescribe dapagliflozin instead.

**A3-G37-C1**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 80 (current) [line: "Heart rate now 80/min on a pulse check."]
- patient: white cell count = 13.1 (current) [line: "Latest WBC is 13.1 x10^9/L."]
- patient: eGFR = 87 (current) [line: "eGFR now 87 mL/min/1.73 m2."]
- angioedema: not named; a general line implies absence (counts as absent) [line: "Free of facial or oropharyngeal edema."]

**A3-G37-C2**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 80 (current) [line: "Heart rate now 80/min on a pulse check."]
- patient: white cell count = 13.1 (current) [line: "Latest WBC is 13.1 x10^9/L."]
- patient: eGFR = 87 (current) [line: "eGFR now 87 mL/min/1.73 m2."]
- patient: angioedema present (past) [line: "An episode of angioedema years ago, with full recovery."]

**A3-G37-C3**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 80 (current) [line: "Heart rate now 80/min on a pulse check."]
- patient: white cell count = 13.1 (current) [line: "Latest WBC is 13.1 x10^9/L."]
- patient: eGFR = 87 (current) [line: "eGFR now 87 mL/min/1.73 m2."]
- sister: angioedema present (past) [line: "His sister recovered from an episode of angioedema in 2006."]

**A3-G37-C4**

Claims: s = Prescribe spironolactone. | s' = Prescribe dapagliflozin.

Criterion claims: s = Under the rule, the condition "angioedema" does not hold for this patient. | s' = Under the rule, the condition "angioedema" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: eGFR = 87 (current) [line: "Current eGFR 87 mL/min/1.73 m2."]
- patient: heart rate = 80 (current) [line: "Current heart rate 80/min."]
- angioedema: not named; a general line implies absence (counts as absent) [line: "Free of facial or oropharyngeal edema."]
- patient: white cell count = 13.1 (current) [line: "Current white cell count 13.1 x10^9/L."]


## G38

Rule: Mortality in Emergency Department Sepsis score (as used here, partial): 3 points for a current platelet count below 150 x10^9/L; 3 points for an age above 65 years; 2 points for current altered mental status (confusion or disorientation). Other items of the score are not part of this question.

**A3-G38-C1**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: age = 48 (current) [line: "Current age 48 years."]
- patient: platelet count = 195 (current) [line: "Platelet count now 195 x10^9/L."]
- patient: altered mental status denied by name [line: "Confusion absent; answers questions appropriately."]

**A3-G38-C2**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- altered mental status: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: age = 48 (current) [line: "Currently aged 48 years."]
- patient: platelet count = 195 (current) [line: "Current platelet count 195 x10^9/L."]

**A3-G38-C3**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: age = 48 (current) [line: "Current age 48 years."]
- patient: platelet count = 195 (current) [line: "Platelet count now 195 x10^9/L."]
- patient: altered mental status present (current) [line: "Disoriented to time and place, which is new for the patient."]

**A3-G38-C4**

Claims: s = The altered mental status criterion contributes 0 points. | s' = The altered mental status criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: age = 48 (current) [line: "Current age 48 years."]
- patient: platelet count = 195 (current) [line: "Platelet count now 195 x10^9/L."]
- altered mental status: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]


## G39

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 2 points if the patient has ever had a myocardial infarction or peripheral artery disease (current or past); 2 points if the patient currently has tonsillar exudate; 3 points if the current calf swelling compared with the other leg is 3.0 cm or more; 1 point if the patient has ever had a peptic ulcer (current or past). If the score is 8 or more, prescribe nitrofurantoin instead.

**A3-G39-C1**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: myocardial infarction or peripheral artery disease present (past) [line: "Heart attack years ago, with full recovery."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: calf swelling = 2.8 (current) [line: "Current calf swelling 2.8 cm compared with the other leg."]

**A3-G39-C2**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: myocardial infarction or peripheral artery disease present (past) [line: "Heart attack years ago, with full recovery."]
- patient: calf swelling = 1.4 (current) [line: "Difference in calf circumference now 1.4 cm."]

**A3-G39-C3**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: myocardial infarction or peripheral artery disease present (past) [line: "Heart attack years ago, with full recovery."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: calf swelling = 1.4 (current) [line: "Current calf swelling 1.4 cm compared with the other leg."]

**A3-G39-C4**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "calf swelling at least 3.0" does not hold for this patient. | s' = Under the rule, the condition "calf swelling at least 3.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: myocardial infarction or peripheral artery disease present (past) [line: "Heart attack years ago, with full recovery."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: calf swelling = 3.0 (current) [line: "Current calf swelling 3.0 cm compared with the other leg."]


## G40

Rule: For vaginal candidiasis, prescribe oral fluconazole. If the current heart rate is above 90/min or the current weight is 60 kg or less, prescribe clotrimazole pessaries instead.

**A3-G40-C1**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: weight = 97 (current) [line: "Latest weight 97 kg."]
- patient: heart rate = 68 (current) [line: "Heart rate now 68/min on a pulse check."]

**A3-G40-C2**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 90 (current) [line: "Current heart rate 90/min."]
- patient: weight = 97 (current) [line: "Current weight 97 kg."]

**A3-G40-C3**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 101 (current) [line: "Current heart rate 101/min."]
- patient: weight = 97 (current) [line: "Current weight 97 kg."]

**A3-G40-C4**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: weight = 97 (current) [line: "Current weight 97 kg."]
- heart rate: not mentioned (unknown)

**A3-G40-C5**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "heart rate above 90" does not hold for this patient. | s' = Under the rule, the condition "heart rate above 90" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 68 (current) [line: "Current heart rate 68/min."]
- patient: weight = 97 (current) [line: "Current weight 97 kg."]


## G41

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 50 mL/min/1.73 m2 or the patient currently has tonsillar exudate, prescribe a progestin-only pill instead.

**A3-G41-C1**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tonsillar exudate" does not hold for this patient. | s' = Under the rule, the condition "tonsillar exudate" holds for this patient.
```
Woman of 31 years.
Requests contraception.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Tonsils free of exudate.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 58 (current) [line: "eGFR now 58 mL/min/1.73 m2."]
- patient: tonsillar exudate denied by name [line: "Tonsils free of exudate."]

**A3-G41-C2**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tonsillar exudate" does not hold for this patient. | s' = Under the rule, the condition "tonsillar exudate" holds for this patient.
```
Woman of 31 years.
Requests contraception.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Tonsillar exudate visible on both sides.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 58 (current) [line: "eGFR now 58 mL/min/1.73 m2."]
- patient: tonsillar exudate present (current) [line: "Tonsillar exudate visible on both sides."]

**A3-G41-C3**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tonsillar exudate" does not hold for this patient. | s' = Under the rule, the condition "tonsillar exudate" holds for this patient.
```
Woman of 31 years.
Requests contraception.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 58 (current) [line: "eGFR now 58 mL/min/1.73 m2."]
- tonsillar exudate: not mentioned (counts as absent)

**A3-G41-C4**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "tonsillar exudate" does not hold for this patient. | s' = Under the rule, the condition "tonsillar exudate" holds for this patient.
```
Female patient of 31 years.
Requests contraception.
Has two cats.
Paints watercolors as a hobby.
Current eGFR 58 mL/min/1.73 m2.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 58 (current) [line: "Current eGFR 58 mL/min/1.73 m2."]
- tonsillar exudate: not mentioned (counts as absent)


## G42

Rule: For contraception, prescribe a combined oral contraceptive. If the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time or the patient has ever had asthma (current or past), prescribe a progestin-only pill instead.

**A3-G42-C1**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "diabetes (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "diabetes (patient or first-degree relative)" holds for this patient.
```
Woman of 36 years.
Requests contraception.
Lungs clear, without wheeze or prolonged expiration.
Has two cats.
Prefers morning appointments.
Has type 2 diabetes on metformin.
```

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- patient: diabetes present (current) [line: "Has type 2 diabetes on metformin."]

**A3-G42-C2**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "diabetes (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "diabetes (patient or first-degree relative)" holds for this patient.
```
Female patient of 36 years.
Requests contraception.
Has two cats.
Random glucose 92 mg/dL.
Prefers morning appointments.
Lungs clear, without wheeze or prolonged expiration.
```

Facts (for q1, after q2 and q3):
- diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]

**A3-G42-C3**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "diabetes (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "diabetes (patient or first-degree relative)" holds for this patient.
```
Woman of 36 years.
Requests contraception.
Lungs clear, without wheeze or prolonged expiration.
Has two cats.
Prefers morning appointments.
Random glucose 92 mg/dL.
```

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]

**A3-G42-C4**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "diabetes (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "diabetes (patient or first-degree relative)" holds for this patient.
```
Woman of 36 years.
Requests contraception.
Lungs clear, without wheeze or prolonged expiration.
Has two cats.
Prefers morning appointments.
Has never had diabetes.
```

Facts (for q1, after q2 and q3):
- asthma: not named; a general line implies absence (counts as absent) [line: "Lungs clear, without wheeze or prolonged expiration."]
- patient: diabetes denied by name [line: "Has never had diabetes."]


## G43

Rule: For acute sore throat, prescribe ibuprofen. If the patient has ever had a myocardial infarction or peripheral artery disease (current or past) and the current temperature is above 38.0 C, prescribe penicillin V instead.

**A3-G43-C1**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Female patient of 42 years.
Sore throat for two days.
Plays the piano.
Current temperature 38.3 C.
Drives a car.
Knits as a hobby.
Enjoys board games.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 38.3 (current) [line: "Current temperature 38.3 C."]
- myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

**A3-G43-C2**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- sister: myocardial infarction or peripheral artery disease present (past) [line: "Her sister had a heart attack years ago."]
- patient: temperature = 38.3 (current) [line: "Temperature now 38.3 C (tympanic)."]

**A3-G43-C3**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Woman of 42 years.
Sore throat for two days.
Plays the piano.
Drives a car.
Knits as a hobby.
Temperature now 38.3 C (tympanic).
Enjoys board games.
```

Facts (for q1, after q2 and q3):
- patient: temperature = 38.3 (current) [line: "Temperature now 38.3 C (tympanic)."]
- myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

**A3-G43-C4**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: myocardial infarction or peripheral artery disease present (past) [line: "Recovered from a heart attack in 2016."]
- patient: temperature = 38.3 (current) [line: "Temperature now 38.3 C (tympanic)."]

**A3-G43-C5**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- myocardial infarction or peripheral artery disease: stated as unknown [line: "Myocardial infarction or peripheral artery disease: status unclear from the records at hand."]
- patient: temperature = 38.3 (current) [line: "Temperature now 38.3 C (tympanic)."]


## G44

Rule: For newly diagnosed type 2 diabetes, prescribe metformin. If at least two of the following apply, prescribe sitagliptin instead: the patient has ever had a peptic ulcer (current or past); the current serum potassium is above 5.0 mmol/L; the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time.

**A3-G44-C1**

Claims: s = Prescribe metformin. | s' = Prescribe sitagliptin.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- serum potassium: not mentioned (unknown)

**A3-G44-C2**

Claims: s = Prescribe metformin. | s' = Prescribe sitagliptin.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest potassium result: 3.9 mmol/L.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- patient: serum potassium = 3.9 (current) [line: "Latest potassium result: 3.9 mmol/L."]

**A3-G44-C3**

Claims: s = Prescribe metformin. | s' = Prescribe sitagliptin.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest potassium result: 5.2 mmol/L.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- patient: serum potassium = 5.2 (current) [line: "Latest potassium result: 5.2 mmol/L."]

**A3-G44-C4**

Claims: s = Prescribe metformin. | s' = Prescribe sitagliptin.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Varicose veins: none seen.
Lives in a second-floor apartment.
Latest potassium result: 5.0 mmol/L.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- patient: serum potassium = 5.0 (current) [line: "Latest potassium result: 5.0 mmol/L."]

**A3-G44-C5**

Claims: s = Prescribe metformin. | s' = Prescribe sitagliptin.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Male patient of 39 years.
Newly diagnosed type 2 diabetes (HbA1c 7.9%).
Has an active duodenal ulcer.
Lives in a second-floor apartment.
Current serum potassium 3.9 mmol/L.
Varicose veins: none seen.
```

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (current) [line: "Has an active duodenal ulcer."]
- patient: serum potassium = 3.9 (current) [line: "Current serum potassium 3.9 mmol/L."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]


## G45

Rule: Centor score (as used here, partial): 1 point each for temperature above 38.0 C; tonsillar exudate; tender anterior cervical lymph nodes. Only current findings count.

**A3-G45-C1**

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: temperature = 38.0 (current) [line: "Temperature now 38.0 C (tympanic)."]
- tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Neck palpation unremarkable."]

**A3-G45-C2**

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: temperature = 39.0 (current) [line: "Temperature now 39.0 C (tympanic)."]
- tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Neck palpation unremarkable."]

**A3-G45-C3**

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: temperature = 37.2 (current) [line: "Current temperature 37.2 C."]
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Neck palpation unremarkable."]

**A3-G45-C4**

Claims: s = The temperature criterion contributes 0 points. | s' = The temperature criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: temperature = 37.2 (current) [line: "Temperature now 37.2 C (tympanic)."]
- tender cervical lymph nodes: not named; a general line implies absence (counts as absent) [line: "Neck palpation unremarkable."]


## G46

Rule: For stroke prevention in atrial fibrillation, prescribe apixaban. Score 3 points if the patient has ever had coronary artery disease (current or past); 3 points if the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; 2 points if the current white cell count is above 12.0 x10^9/L. If the score is 7 or more, prescribe warfarin instead.

**A3-G46-C1**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 14.0 (past) [line: "Last month, white cell count was 14.0 x10^9/L; the newest measurement replaces it."]
- patient: colorectal cancer present (current) [line: "Lives with colon cancer and attends an oncology clinic."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: white cell count = 8.8 (current) [line: "Current white cell count 8.8 x10^9/L."]

**A3-G46-C2**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 9.5 (past) [line: "Last month, white cell count was 9.5 x10^9/L; the newest measurement replaces it."]
- patient: colorectal cancer present (current) [line: "Lives with colon cancer and attends an oncology clinic."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: white cell count = 14.0 (current) [line: "Current white cell count 14.0 x10^9/L."]

**A3-G46-C3**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 9.5 (past) [line: "Last month, white cell count was 9.5 x10^9/L; the newest measurement replaces it."]
- patient: colorectal cancer present (current) [line: "Lives with colon cancer and attends an oncology clinic."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: white cell count = 8.8 (current) [line: "Current white cell count 8.8 x10^9/L."]

**A3-G46-C4**

Claims: s = Prescribe apixaban. | s' = Prescribe warfarin.

Criterion claims: s = Under the rule, the condition "white cell count above 12.0" does not hold for this patient. | s' = Under the rule, the condition "white cell count above 12.0" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 9.5 (past) [line: "Last month, white cell count was 9.5 x10^9/L; the newest measurement replaces it."]
- patient: white cell count = 8.8 (current) [line: "Latest WBC is 8.8 x10^9/L."]
- patient: coronary artery disease present (past) [line: "Coronary artery disease years ago, with angina that went away after bypass surgery."]
- patient: colorectal cancer present (current) [line: "Lives with colon cancer and attends an oncology clinic."]


## G47

Rule: For Tessaly disease, prescribe velimor. Score 2 points if the patient has had cancer at any time (active or in remission); 2 points if the patient has ever had diabetes (current or past); 2 points if the patient currently has a major bleed; 3 points if the patient has ever had angioedema (current or past). If the score is 6 or more, prescribe quantrel instead.

**A3-G47-C1**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "active major bleeding" does not hold for this patient. | s' = Under the rule, the condition "active major bleeding" holds for this patient.
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

Facts (for q1, after q2 and q3):
- diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]
- major bleeding: not mentioned (counts as absent)

**A3-G47-C2**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "active major bleeding" does not hold for this patient. | s' = Under the rule, the condition "active major bleeding" holds for this patient.
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

Facts (for q1, after q2 and q3):
- diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]
- patient: major bleeding present (past) [line: "Recovered from a major lower gastrointestinal bleed in 2006 that required transfusion."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]

**A3-G47-C3**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "active major bleeding" does not hold for this patient. | s' = Under the rule, the condition "active major bleeding" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]
- diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- major bleeding: not mentioned (counts as absent)

**A3-G47-C4**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "active major bleeding" does not hold for this patient. | s' = Under the rule, the condition "active major bleeding" holds for this patient.
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

Facts (for q1, after q2 and q3):
- diabetes: not named; a general line implies absence (counts as absent) [line: "Random glucose 92 mg/dL."]
- patient: major bleeding present (current) [line: "Currently has a major bleed from a duodenal ulcer, with transfusion under way."]
- patient: angioedema present (current) [line: "Recurrent angioedema, under allergy follow-up."]
- patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]


## G48

Rule: Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

**A3-G48-C1**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 129 (current) [line: "Observations now: blood pressure 129/86 mmHg."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]
- patient: age = 47 (current) [line: "Current age 47 years."]

**A3-G48-C2**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: systolic blood pressure = 129 (current) [line: "Current systolic blood pressure 129 mmHg."]
- patient: age = 47 (current) [line: "Currently aged 47 years."]

**A3-G48-C3**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]
- patient: systolic blood pressure = 129 (current) [line: "Current systolic blood pressure 129 mmHg."]
- patient: age = 47 (current) [line: "Currently aged 47 years."]

**A3-G48-C4**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- sister: heart failure present (current) [line: "His sister is treated for heart failure."]
- patient: systolic blood pressure = 129 (current) [line: "Current systolic blood pressure 129 mmHg."]
- patient: age = 47 (current) [line: "Currently aged 47 years."]


## G49

Rule: For heart failure with reduced ejection fraction, add spironolactone. If the current serum potassium is above 4.5 mmol/L, add dapagliflozin instead.

**A3-G49-C1**

Claims: s = Add spironolactone. | s' = Add dapagliflozin.

Criterion claims: s = Under the rule, the condition "potassium above 4.5" does not hold for this patient. | s' = Under the rule, the condition "potassium above 4.5" holds for this patient.
```
Male patient of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Paints watercolors as a hobby.
Latest potassium result: 4.2 mmol/L.
```

Facts (for q1, after q2 and q3):
- patient: potassium = 4.2 (current) [line: "Latest potassium result: 4.2 mmol/L."]

**A3-G49-C2**

Claims: s = Add spironolactone. | s' = Add dapagliflozin.

Criterion claims: s = Under the rule, the condition "potassium above 4.5" does not hold for this patient. | s' = Under the rule, the condition "potassium above 4.5" holds for this patient.
```
Man of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 4.8 mmol/L.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: potassium = 4.8 (current) [line: "Current serum potassium 4.8 mmol/L."]

**A3-G49-C3**

Claims: s = Add spironolactone. | s' = Add dapagliflozin.

Criterion claims: s = Under the rule, the condition "potassium above 4.5" does not hold for this patient. | s' = Under the rule, the condition "potassium above 4.5" holds for this patient.
```
Man of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 4.3 mmol/L.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: potassium = 4.3 (current) [line: "Current serum potassium 4.3 mmol/L."]

**A3-G49-C4**

Claims: s = Add spironolactone. | s' = Add dapagliflozin.

Criterion claims: s = Under the rule, the condition "potassium above 4.5" does not hold for this patient. | s' = Under the rule, the condition "potassium above 4.5" holds for this patient.
```
Man of 67 years.
Heart failure with reduced ejection fraction (ejection fraction 30%), still symptomatic.
Current serum potassium 4.2 mmol/L.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: potassium = 4.2 (current) [line: "Current serum potassium 4.2 mmol/L."]


## G50

Rule: For community-acquired pneumonia, prescribe oral amoxicillin. If at least two of the following apply, prescribe intravenous co-amoxiclav instead: the patient or a first-degree relative (parent, sibling or child) has had colorectal cancer at any time; the current calf swelling compared with the other leg is 3.0 cm or more; the age of the patient is above 65 years.

**A3-G50-C1**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "age above 65" does not hold for this patient. | s' = Under the rule, the condition "age above 65" holds for this patient.
```
An adult man.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Rectal exam unremarkable.
Current calf swelling 3.6 cm compared with the other leg.
Current age 49 years.
Owns a bicycle.
```

Facts (for q1, after q2 and q3):
- colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]
- patient: calf swelling = 3.6 (current) [line: "Current calf swelling 3.6 cm compared with the other leg."]
- patient: age = 49 (current) [line: "Current age 49 years."]

**A3-G50-C2**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "age above 65" does not hold for this patient. | s' = Under the rule, the condition "age above 65" holds for this patient.
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Currently aged 63 years.
```

Facts (for q1, after q2 and q3):
- colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]
- patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]
- patient: age = 63 (current) [line: "Currently aged 63 years."]

**A3-G50-C3**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "age above 65" does not hold for this patient. | s' = Under the rule, the condition "age above 65" holds for this patient.
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Currently aged 49 years.
```

Facts (for q1, after q2 and q3):
- colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]
- patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]
- patient: age = 49 (current) [line: "Currently aged 49 years."]

**A3-G50-C4**

Claims: s = Prescribe oral amoxicillin. | s' = Prescribe intravenous co-amoxiclav.

Criterion claims: s = Under the rule, the condition "age above 65" does not hold for this patient. | s' = Under the rule, the condition "age above 65" holds for this patient.
```
Man, adult.
Community-acquired pneumonia confirmed on chest radiograph.
Prefers to be addressed by first name.
Owns a bicycle.
Rectal exam unremarkable.
Difference in calf circumference now 3.6 cm.
Currently aged 67 years.
```

Facts (for q1, after q2 and q3):
- colorectal cancer: not named; a general line implies absence (counts as absent) [line: "Rectal exam unremarkable."]
- patient: calf swelling = 3.6 (current) [line: "Difference in calf circumference now 3.6 cm."]
- patient: age = 67 (current) [line: "Currently aged 67 years."]


## G51

Rule: For contraception, prescribe a combined oral contraceptive. If the current eGFR is below 50 mL/min/1.73 m2 or the patient currently has tonsillar exudate, prescribe a progestin-only pill instead.

**A3-G51-C1**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: eGFR = 62 (current) [line: "eGFR now 62 mL/min/1.73 m2."]

**A3-G51-C2**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: eGFR = 51 (current) [line: "eGFR now 51 mL/min/1.73 m2."]

**A3-G51-C3**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: eGFR = 46 (current) [line: "eGFR now 46 mL/min/1.73 m2."]

**A3-G51-C4**

Claims: s = Prescribe a combined oral contraceptive. | s' = Prescribe a progestin-only pill.

Criterion claims: s = Under the rule, the condition "eGFR below 50" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 50" holds for this patient.
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

Facts (for q1, after q2 and q3):
- tonsillar exudate: not named; a general line implies absence (counts as absent) [line: "Tonsils pink and clean on inspection."]
- patient: eGFR = 62 (current) [line: "Current eGFR 62 mL/min/1.73 m2."]


## G52

Rule: Revised Cardiac Risk Index (as used here, partial): 1 point each for coronary artery disease at any time; heart failure at any time; a stroke or TIA at any time; a current serum creatinine above 1.5 mg/dL. Other items are not part of this question.

**A3-G52-C1**

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Female patient of 62 years.
Preoperative assessment before elective colectomy.
Pupils equal and reactive to light.
Current serum creatinine 1.9 mg/dL.
Heart sounds without a gallop.
Chest pain on exertion: none reported.
```

Facts (for q1, after q2 and q3):
- patient: creatinine = 1.9 (current) [line: "Current serum creatinine 1.9 mg/dL."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- stroke/TIA: not mentioned (counts as absent)

**A3-G52-C2**

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Female patient of 62 years.
Preoperative assessment before elective colectomy.
Pupils equal and reactive to light.
Current serum creatinine 1.5 mg/dL.
Heart sounds without a gallop.
Chest pain on exertion: none reported.
```

Facts (for q1, after q2 and q3):
- patient: creatinine = 1.5 (current) [line: "Current serum creatinine 1.5 mg/dL."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- stroke/TIA: not mentioned (counts as absent)

**A3-G52-C3**

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Woman of 62 years.
Preoperative assessment before elective colectomy.
Heart sounds without a gallop.
Latest creatinine result: 1.3 mg/dL.
Pupils equal and reactive to light.
Chest pain on exertion: none reported.
```

Facts (for q1, after q2 and q3):
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- patient: creatinine = 1.3 (current) [line: "Latest creatinine result: 1.3 mg/dL."]
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- stroke/TIA: not mentioned (counts as absent)

**A3-G52-C4**

Claims: s = The creatinine criterion contributes 0 points. | s' = The creatinine criterion contributes 1 point.
```
Female patient of 62 years.
Preoperative assessment before elective colectomy.
Pupils equal and reactive to light.
Current serum creatinine 1.3 mg/dL.
Heart sounds without a gallop.
Chest pain on exertion: none reported.
```

Facts (for q1, after q2 and q3):
- patient: creatinine = 1.3 (current) [line: "Current serum creatinine 1.3 mg/dL."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- stroke/TIA: not mentioned (counts as absent)


## G53

Rule: Revised Geneva score (as used here, partial): 2 points each for active cancer and current hemoptysis (coughing up blood); 1 point for a current age above 65 years. Other Geneva items are not part of this question.

**A3-G53-C1**

Claims: s = The age criterion contributes 0 points. | s' = The age criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- hemoptysis: not named; a general line implies absence (counts as absent) [line: "Dry cough, with nothing brought up."]
- patient: age = 49 (current) [line: "Currently aged 49 years."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]

**A3-G53-C2**

Claims: s = The age criterion contributes 0 points. | s' = The age criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- hemoptysis: not named; a general line implies absence (counts as absent) [line: "Dry cough, with nothing brought up."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]
- patient: age = 49 (current) [line: "Current age 49 years."]

**A3-G53-C3**

Claims: s = The age criterion contributes 0 points. | s' = The age criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- hemoptysis: not named; a general line implies absence (counts as absent) [line: "Dry cough, with nothing brought up."]
- patient: age = 69 (current) [line: "Currently aged 69 years."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]

**A3-G53-C4**

Claims: s = The age criterion contributes 0 points. | s' = The age criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- hemoptysis: not named; a general line implies absence (counts as absent) [line: "Dry cough, with nothing brought up."]
- patient: age = 64 (current) [line: "Currently aged 64 years."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Weight steady over the past year."]


## G54

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If the current eGFR is below 30 mL/min/1.73 m2 and the current calf swelling compared with the other leg is 3.0 cm or more, prescribe diltiazem instead.

**A3-G54-C1**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: calf swelling = 3.9 (current) [line: "Difference in calf circumference now 3.9 cm."]
- patient: eGFR = 30 (current) [line: "eGFR now 30 mL/min/1.73 m2."]

**A3-G54-C2**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: calf swelling = 3.9 (current) [line: "Difference in calf circumference now 3.9 cm."]
- patient: eGFR = 73 (current) [line: "eGFR now 73 mL/min/1.73 m2."]

**A3-G54-C3**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: calf swelling = 3.9 (current) [line: "Current calf swelling 3.9 cm compared with the other leg."]
- patient: eGFR = 73 (current) [line: "Current eGFR 73 mL/min/1.73 m2."]

**A3-G54-C4**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "eGFR below 30" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 30" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: calf swelling = 3.9 (current) [line: "Difference in calf circumference now 3.9 cm."]
- patient: eGFR = 17 (current) [line: "eGFR now 17 mL/min/1.73 m2."]


## G55

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. Score 3 points if the current ALT is above 120 U/L; 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 3 points if the current systolic blood pressure is above 160 mmHg; 2 points if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time. If the score is 4 or more, prescribe nitrofurantoin instead.

**A3-G55-C1**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 148 (current) [line: "Current systolic blood pressure 148 mmHg."]
- patient: diabetes present (current) [line: "Has type 2 diabetes on metformin."]
- patient: ALT = 34 (current) [line: "ALT now 34 U/L."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G55-C2**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 153 (current) [line: "Current systolic blood pressure 153 mmHg."]
- patient: diabetes present (current) [line: "Has type 2 diabetes on metformin."]
- patient: ALT = 34 (current) [line: "ALT now 34 U/L."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G55-C3**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (current) [line: "Has type 2 diabetes on metformin."]
- patient: ALT = 34 (current) [line: "Current ALT 34 U/L."]
- patient: systolic blood pressure = 148 (current) [line: "Observations now: blood pressure 148/96 mmHg."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G55-C4**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "systolic blood pressure above 160" does not hold for this patient. | s' = Under the rule, the condition "systolic blood pressure above 160" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 184 (current) [line: "Current systolic blood pressure 184 mmHg."]
- patient: diabetes present (current) [line: "Has type 2 diabetes on metformin."]
- patient: ALT = 34 (current) [line: "ALT now 34 U/L."]
- venous thromboembolism: not mentioned (counts as absent)


## G56

Rule: Rockall score (as used here, partial, pre-endoscopy items): 1 point for age 60 years or more; 2 points for a current systolic blood pressure below 100 mmHg; 2 points for current heart failure. Other Rockall items are not part of this question.

**A3-G56-C1**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 137 (current) [line: "Observations now: blood pressure 137/90 mmHg."]
- patient: heart failure present (current) [line: "Has heart failure, treated with diuretics."]
- patient: age = 46 (current) [line: "Currently aged 46 years."]

**A3-G56-C2**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 137 (current) [line: "Current systolic blood pressure 137 mmHg."]
- patient: age = 46 (current) [line: "Current age 46 years."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]

**A3-G56-C3**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 137 (current) [line: "Observations now: blood pressure 137/90 mmHg."]
- patient: heart failure denied by name [line: "Heart failure: never diagnosed."]
- patient: age = 46 (current) [line: "Currently aged 46 years."]

**A3-G56-C4**

Claims: s = The heart failure criterion contributes 0 points. | s' = The heart failure criterion contributes 2 points.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 137 (current) [line: "Observations now: blood pressure 137/90 mmHg."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- patient: age = 46 (current) [line: "Currently aged 46 years."]


## G57

Rule: For thromboprophylaxis in a medical inpatient, prescribe compression stockings. Score 3 points for active cancer; 3 points for a venous thromboembolism of the patient, current or previous; 1 point for age 70 years or more; 1 point for current heart failure. If the score is 4 or more, prescribe enoxaparin instead.

**A3-G57-C1**

Claims: s = Prescribe compression stockings. | s' = Prescribe enoxaparin.

Criterion claims: s = Under the rule, the condition "active cancer" does not hold for this patient. | s' = Under the rule, the condition "active cancer" holds for this patient.
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

Facts (for q1, after q2 and q3):
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- patient: cancer present (current) [line: "Has metastatic lung cancer, receiving palliative treatment."]
- patient: age = 76 (current) [line: "Current age 76 years."]

**A3-G57-C2**

Claims: s = Prescribe compression stockings. | s' = Prescribe enoxaparin.

Criterion claims: s = Under the rule, the condition "active cancer" does not hold for this patient. | s' = Under the rule, the condition "active cancer" holds for this patient.
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

Facts (for q1, after q2 and q3):
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- patient: age = 76 (current) [line: "Current age 76 years."]
- cancer: not mentioned (counts as absent)

**A3-G57-C3**

Claims: s = Prescribe compression stockings. | s' = Prescribe enoxaparin.

Criterion claims: s = Under the rule, the condition "active cancer" does not hold for this patient. | s' = Under the rule, the condition "active cancer" holds for this patient.
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

Facts (for q1, after q2 and q3):
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- patient: cancer present (past) [line: "Had thyroid cancer years ago and is now cured."]
- patient: age = 76 (current) [line: "Current age 76 years."]

**A3-G57-C4**

Claims: s = Prescribe compression stockings. | s' = Prescribe enoxaparin.

Criterion claims: s = Under the rule, the condition "active cancer" does not hold for this patient. | s' = Under the rule, the condition "active cancer" holds for this patient.
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

Facts (for q1, after q2 and q3):
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- cancer: stated as unknown [line: "Active cancer: status unclear from the records at hand."]
- patient: age = 76 (current) [line: "Current age 76 years."]

**A3-G57-C5**

Claims: s = Prescribe compression stockings. | s' = Prescribe enoxaparin.

Criterion claims: s = Under the rule, the condition "active cancer" does not hold for this patient. | s' = Under the rule, the condition "active cancer" holds for this patient.
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

Facts (for q1, after q2 and q3):
- heart failure: not named; a general line implies absence (counts as absent) [line: "Heart sounds without a gallop."]
- patient: age = 76 (current) [line: "Currently aged 76 years."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Coagulation tests normal on recent bloodwork."]
- cancer: not mentioned (counts as absent)


## G58

Rule: Wells score for pulmonary embolism (as used here, partial): 1.5 points for a current heart rate above 100/min; 1 point each for current hemoptysis (coughing up blood) and active cancer. Other Wells items are not part of this question.

**A3-G58-C1**

Claims: s = The hemoptysis criterion contributes 0 points. | s' = The hemoptysis criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 67 (current) [line: "Heart rate now 67/min on a pulse check."]
- hemoptysis: not named; a general line implies absence (counts as absent) [line: "Sputum colorless on inspection."]
- cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]

**A3-G58-C2**

Claims: s = The hemoptysis criterion contributes 0 points. | s' = The hemoptysis criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]
- patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]
- hemoptysis: stated as unknown [line: "Hemoptysis: status unclear from the records at hand."]

**A3-G58-C3**

Claims: s = The hemoptysis criterion contributes 0 points. | s' = The hemoptysis criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]
- patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]
- patient: hemoptysis present (current) [line: "Currently coughing up blood with each bout of coughing."]

**A3-G58-C4**

Claims: s = The hemoptysis criterion contributes 0 points. | s' = The hemoptysis criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]
- patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]
- hemoptysis: not named; a general line implies absence (counts as absent) [line: "Sputum colorless on inspection."]

**A3-G58-C5**

Claims: s = The hemoptysis criterion contributes 0 points. | s' = The hemoptysis criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- cancer: not named; a general line implies absence (counts as absent) [line: "Oncology follow-up: none."]
- patient: heart rate = 67 (current) [line: "Current heart rate 67/min."]
- uncle: hemoptysis present (current) [line: "Her uncle is currently coughing up blood."]


## G59

Rule: For hip osteoarthritis pain, prescribe naproxen alone. If the current systolic blood pressure is above 160 mmHg or the current serum creatinine is above 2.0 mg/dL, prescribe naproxen with omeprazole instead.

**A3-G59-C1**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Current systolic blood pressure 139 mmHg.
```

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 139 (current) [line: "Current systolic blood pressure 139 mmHg."]
- serum creatinine: not mentioned (unknown)

**A3-G59-C2**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Latest creatinine result: 0.7 mg/dL.
Current systolic blood pressure 139 mmHg.
```

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 0.7 (current) [line: "Latest creatinine result: 0.7 mg/dL."]
- patient: systolic blood pressure = 139 (current) [line: "Current systolic blood pressure 139 mmHg."]

**A3-G59-C3**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
```
Male patient of 54 years.
Hip osteoarthritis with pain on walking.
Current serum creatinine 0.7 mg/dL.
Sleeps seven hours a night.
Observations now: blood pressure 139/91 mmHg.
```

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 0.7 (current) [line: "Current serum creatinine 0.7 mg/dL."]
- patient: systolic blood pressure = 139 (current) [line: "Observations now: blood pressure 139/91 mmHg."]

**A3-G59-C4**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Latest creatinine result: 2.7 mg/dL.
Current systolic blood pressure 139 mmHg.
```

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 2.7 (current) [line: "Latest creatinine result: 2.7 mg/dL."]
- patient: systolic blood pressure = 139 (current) [line: "Current systolic blood pressure 139 mmHg."]

**A3-G59-C5**

Claims: s = Prescribe naproxen alone. | s' = Prescribe naproxen with omeprazole.

Criterion claims: s = Under the rule, the condition "serum creatinine above 2.0" does not hold for this patient. | s' = Under the rule, the condition "serum creatinine above 2.0" holds for this patient.
```
Man of 54 years.
Hip osteoarthritis with pain on walking.
Sleeps seven hours a night.
Latest creatinine result: 2.0 mg/dL.
Current systolic blood pressure 139 mmHg.
```

Facts (for q1, after q2 and q3):
- patient: serum creatinine = 2.0 (current) [line: "Latest creatinine result: 2.0 mg/dL."]
- patient: systolic blood pressure = 139 (current) [line: "Current systolic blood pressure 139 mmHg."]


## G60

Rule: For Tessaly disease, prescribe velimor. If the patient is allergic to penicillin, prescribe quantrel instead.

**A3-G60-C1**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Man of 28 years.
Referred with Tessaly disease.
Sees a dentist yearly.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
```

Facts (for q1, after q2 and q3):
- penicillin allergy: not mentioned (counts as absent)

**A3-G60-C2**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Male patient of 28 years.
Referred with Tessaly disease.
His roommate has a penicillin allergy.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

Facts (for q1, after q2 and q3):
- roommate: penicillin allergy present (current) [line: "His roommate has a penicillin allergy."]

**A3-G60-C3**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Male patient of 28 years.
Referred with Tessaly disease.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

Facts (for q1, after q2 and q3):
- penicillin allergy: not mentioned (counts as absent)

**A3-G60-C4**

Claims: s = Prescribe velimor. | s' = Prescribe quantrel.

Criterion claims: s = Under the rule, the condition "penicillin allergy" does not hold for this patient. | s' = Under the rule, the condition "penicillin allergy" holds for this patient.
```
Male patient of 28 years.
Referred with Tessaly disease.
Known penicillin allergy with angioedema.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Sees a dentist yearly.
```

Facts (for q1, after q2 and q3):
- patient: penicillin allergy present (current) [line: "Known penicillin allergy with angioedema."]


## G61

Rule: For rate control in atrial fibrillation, prescribe metoprolol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had diabetes at any time; 2 points if the patient has ever had a venous thromboembolism (current or past); 3 points if the patient has ever had coronary artery disease (current or past); 1 point if the current white cell count is above 12.0 x10^9/L. If the score is 4 or more, prescribe diltiazem instead.

**A3-G61-C1**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
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

Facts (for q1, after q2 and q3):
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 12.9 (current) [line: "Current white cell count 12.9 x10^9/L."]

**A3-G61-C2**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
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

Facts (for q1, after q2 and q3):
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- patient: venous thromboembolism denied by name [line: "Venous thromboembolism has never occurred in the patient or in any parent, sibling or child."]
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 12.9 (current) [line: "Current white cell count 12.9 x10^9/L."]

**A3-G61-C3**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
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

Facts (for q1, after q2 and q3):
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- patient: venous thromboembolism present (past) [line: "Pulmonary embolism years ago, treated for six months."]
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- patient: white cell count = 12.9 (current) [line: "Current white cell count 12.9 x10^9/L."]

**A3-G61-C4**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "venous thromboembolism" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: diabetes present (past) [line: "Had diabetes years ago that went into remission on a low-calorie diet."]
- coronary artery disease: not named; a general line implies absence (counts as absent) [line: "Chest pain on exertion: none reported."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- patient: white cell count = 12.9 (current) [line: "Latest WBC is 12.9 x10^9/L."]


## G62

Rule: qSOFA (as used here): 1 point each for a respiratory rate of 22/min or more; altered mentation; systolic blood pressure of 100 mmHg or less. Only current findings count.

**A3-G62-C1**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 139 (current) [line: "Observations now: blood pressure 139/91 mmHg."]
- patient: respiratory rate = 15 (current) [line: "Current respiratory rate 15/min."]
- father: altered mentation present (current) [line: "His father is newly disoriented."]

**A3-G62-C2**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 139 (current) [line: "Observations now: blood pressure 139/91 mmHg."]
- patient: respiratory rate = 15 (current) [line: "Current respiratory rate 15/min."]
- patient: altered mentation present (current) [line: "Disoriented to time and place, which is new for the patient."]

**A3-G62-C3**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- altered mentation: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]
- patient: systolic blood pressure = 139 (current) [line: "Current systolic blood pressure 139 mmHg."]
- patient: respiratory rate = 15 (current) [line: "Observations now: respiratory rate 15/min."]

**A3-G62-C4**

Claims: s = The altered mentation criterion contributes 0 points. | s' = The altered mentation criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: systolic blood pressure = 139 (current) [line: "Observations now: blood pressure 139/91 mmHg."]
- patient: respiratory rate = 15 (current) [line: "Current respiratory rate 15/min."]
- altered mentation: not named; a general line implies absence (counts as absent) [line: "Gives a clear account of the illness."]


## G63

Rule: For Pallis disease, prescribe brexadol. Score 1 point if the patient or a first-degree relative (parent, sibling or child) has had a venous thromboembolism at any time; 2 points if the current ALT is above 120 U/L; 3 points if the current eGFR is below 30 mL/min/1.73 m2. If the score is 4 or more, prescribe corlitane instead.

**A3-G63-C1**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: eGFR = 20 (current) [line: "eGFR now 20 mL/min/1.73 m2."]
- uncle: venous thromboembolism present (past) [line: "Her uncle had a DVT years ago."]
- patient: ALT = 12 (current) [line: "Current ALT 12 U/L."]

**A3-G63-C2**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: eGFR = 20 (current) [line: "eGFR now 20 mL/min/1.73 m2."]
- father: venous thromboembolism present (past) [line: "Her father recovered from a pulmonary embolism in 2013."]
- patient: ALT = 12 (current) [line: "Current ALT 12 U/L."]

**A3-G63-C3**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: ALT = 12 (current) [line: "ALT now 12 U/L."]
- patient: eGFR = 20 (current) [line: "Current eGFR 20 mL/min/1.73 m2."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G63-C4**

Claims: s = Prescribe brexadol. | s' = Prescribe corlitane.

Criterion claims: s = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" does not hold for this patient. | s' = Under the rule, the condition "venous thromboembolism (patient or first-degree relative)" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: eGFR = 20 (current) [line: "eGFR now 20 mL/min/1.73 m2."]
- patient: ALT = 12 (current) [line: "Current ALT 12 U/L."]
- venous thromboembolism: not mentioned (counts as absent)


## G64

Rule: Child-Pugh score (as used here, partial; each finding below adds 1 point, whatever its grade): 1 point each for a current international normalized ratio (INR) of 1.7 or more; current ascites; new confusion (encephalopathy). Bilirubin, albumin and other items are not part of this question.

**A3-G64-C1**

Claims: s = The ascites criterion contributes 0 points. | s' = The ascites criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]
- patient: international normalized ratio = 1.1 (current) [line: "Current international normalized ratio 1.1."]

**A3-G64-C2**

Claims: s = The ascites criterion contributes 0 points. | s' = The ascites criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.1 (current) [line: "Latest international normalized ratio (INR): 1.1."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: ascites present (current) [line: "Mild ascites seen on the current ultrasound scan."]

**A3-G64-C3**

Claims: s = The ascites criterion contributes 0 points. | s' = The ascites criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.1 (current) [line: "Latest international normalized ratio (INR): 1.1."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]

**A3-G64-C4**

Claims: s = The ascites criterion contributes 0 points. | s' = The ascites criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.1 (current) [line: "Latest international normalized ratio (INR): 1.1."]
- new confusion: not named; a general line implies absence (counts as absent) [line: "Speech clear; follows commands."]
- patient: ascites denied by name [line: "Ultrasound negative for ascites at this visit."]


## G65

Rule: Child-Pugh score (as used here, partial; each finding below adds 1 point, whatever its grade): 1 point each for a current international normalized ratio (INR) of 1.7 or more; current ascites; new confusion (encephalopathy). Bilirubin, albumin and other items are not part of this question.

**A3-G65-C1**

Claims: s = The new confusion criterion contributes 0 points. | s' = The new confusion criterion contributes 1 point.
```
Man of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Latest international normalized ratio (INR): 1.0.
Sees a dentist yearly.
Pupils equal and reactive to light.
Abdomen soft, without distension or fluid.
Teeth in good repair.
```

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.0 (current) [line: "Latest international normalized ratio (INR): 1.0."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]
- new confusion: not mentioned (counts as absent)

**A3-G65-C2**

Claims: s = The new confusion criterion contributes 0 points. | s' = The new confusion criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.0 (current) [line: "Current international normalized ratio 1.0."]
- new confusion: stated as unknown [line: "New confusion: status unclear from the records at hand."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]

**A3-G65-C3**

Claims: s = The new confusion criterion contributes 0 points. | s' = The new confusion criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.0 (current) [line: "Current international normalized ratio 1.0."]
- patient: new confusion denied by name [line: "Confusion absent; answers questions appropriately."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]

**A3-G65-C4**

Claims: s = The new confusion criterion contributes 0 points. | s' = The new confusion criterion contributes 1 point.
```
Male patient of 41 years.
Cirrhosis due to chronic hepatitis B; reviewed by the hepatology team.
Pupils equal and reactive to light.
Teeth in good repair.
Sees a dentist yearly.
Current international normalized ratio 1.0.
Abdomen soft, without distension or fluid.
```

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.0 (current) [line: "Current international normalized ratio 1.0."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]
- new confusion: not mentioned (counts as absent)

**A3-G65-C5**

Claims: s = The new confusion criterion contributes 0 points. | s' = The new confusion criterion contributes 1 point.
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

Facts (for q1, after q2 and q3):
- patient: international normalized ratio = 1.0 (current) [line: "Current international normalized ratio 1.0."]
- patient: new confusion present (current) [line: "Disoriented to time and place, which is new for the patient."]
- ascites: not named; a general line implies absence (counts as absent) [line: "Abdomen soft, without distension or fluid."]


## G66

Rule: For rate control in atrial fibrillation, prescribe metoprolol. If at least two of the following apply, prescribe diltiazem instead: the patient currently has tender anterior cervical lymph nodes; the patient currently has a venous thromboembolism; the patient has ever had angioedema (current or past).

**A3-G66-C1**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: angioedema present (current) [line: "Lives with chronic angioedema that flares several times a year."]
- roommate: tender cervical lymph nodes present (current) [line: "His roommate currently has tender anterior cervical lymphadenopathy."]
- venous thromboembolism: not mentioned (counts as absent)

**A3-G66-C2**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: angioedema present (current) [line: "Lives with chronic angioedema that flares several times a year."]
- tender cervical lymph nodes: not mentioned (counts as absent)
- venous thromboembolism: not mentioned (counts as absent)

**A3-G66-C3**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: angioedema present (current) [line: "Lives with chronic angioedema that flares several times a year."]
- tender cervical lymph nodes: not mentioned (counts as absent)
- venous thromboembolism: not mentioned (counts as absent)

**A3-G66-C4**

Claims: s = Prescribe metoprolol. | s' = Prescribe diltiazem.

Criterion claims: s = Under the rule, the condition "tender cervical lymph nodes" does not hold for this patient. | s' = Under the rule, the condition "tender cervical lymph nodes" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: angioedema present (current) [line: "Lives with chronic angioedema that flares several times a year."]
- patient: tender cervical lymph nodes present (current) [line: "Anterior cervical lymph nodes enlarged and tender to touch."]
- venous thromboembolism: not mentioned (counts as absent)


## G67

Rule: For inpatient VTE prophylaxis, prescribe enoxaparin. If at least two of the following apply, prescribe intermittent pneumatic compression instead: the current heart rate is above 90/min; the patient has ever had heart failure (current or past); the patient has ever had a venous thromboembolism (current or past).

**A3-G67-C1**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
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

Facts (for q1, after q2 and q3):
- heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]
- patient: heart rate = 98 (current) [line: "Heart rate now 98/min on a pulse check."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]

**A3-G67-C2**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure denied by name [line: "Heart failure: never diagnosed."]
- patient: heart rate = 98 (current) [line: "Heart rate now 98/min on a pulse check."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]

**A3-G67-C3**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 98 (current) [line: "Current heart rate 98/min."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]
- heart failure: not named; a general line implies absence (counts as absent) [line: "Sleeps flat on one pillow."]

**A3-G67-C4**

Claims: s = Prescribe enoxaparin. | s' = Prescribe intermittent pneumatic compression.

Criterion claims: s = Under the rule, the condition "heart failure" does not hold for this patient. | s' = Under the rule, the condition "heart failure" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart failure present (current) [line: "Current heart failure with ankle swelling."]
- patient: heart rate = 98 (current) [line: "Heart rate now 98/min on a pulse check."]
- venous thromboembolism: not named; a general line implies absence (counts as absent) [line: "Varicose veins: none seen."]


## G68

Rule: For Graves' hyperthyroidism, prescribe methimazole. If the current ALT is above 120 U/L, prescribe radioactive iodine instead.

**A3-G68-C1**

Claims: s = Prescribe methimazole. | s' = Prescribe radioactive iodine.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Male patient of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Current ALT 119 U/L.
Plays the piano.
Lives in a second-floor apartment.
Prefers morning appointments.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 119 (current) [line: "Current ALT 119 U/L."]

**A3-G68-C2**

Claims: s = Prescribe methimazole. | s' = Prescribe radioactive iodine.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Male patient of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Current ALT 83 U/L.
Plays the piano.
Lives in a second-floor apartment.
Prefers morning appointments.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 83 (current) [line: "Current ALT 83 U/L."]

**A3-G68-C3**

Claims: s = Prescribe methimazole. | s' = Prescribe radioactive iodine.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Male patient of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Current ALT 178 U/L.
Plays the piano.
Lives in a second-floor apartment.
Prefers morning appointments.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 178 (current) [line: "Current ALT 178 U/L."]

**A3-G68-C4**

Claims: s = Prescribe methimazole. | s' = Prescribe radioactive iodine.

Criterion claims: s = Under the rule, the condition "ALT above 120" does not hold for this patient. | s' = Under the rule, the condition "ALT above 120" holds for this patient.
```
Man of 57 years.
Graves' hyperthyroidism: suppressed TSH, raised free T4 and positive TSH receptor antibodies.
Plays the piano.
ALT now 83 U/L.
Lives in a second-floor apartment.
Prefers morning appointments.
```

Facts (for q1, after q2 and q3):
- patient: ALT = 83 (current) [line: "ALT now 83 U/L."]


## G69

Rule: For uncomplicated cystitis, prescribe trimethoprim-sulfamethoxazole. If the current heart rate is above 90/min or the current serum potassium is above 4.8 mmol/L, prescribe nitrofurantoin instead.

**A3-G69-C1**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 82 (current) [line: "Current heart rate 82/min."]
- patient: serum potassium = 4.3 (current) [line: "Current serum potassium 4.3 mmol/L."]

**A3-G69-C2**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum potassium = 4.3 (current) [line: "Latest potassium result: 4.3 mmol/L."]
- patient: heart rate = 82 (current) [line: "Heart rate now 82/min on a pulse check."]

**A3-G69-C3**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum potassium = 5.1 (current) [line: "Latest potassium result: 5.1 mmol/L."]
- patient: heart rate = 82 (current) [line: "Heart rate now 82/min on a pulse check."]

**A3-G69-C4**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: heart rate = 82 (current) [line: "Heart rate now 82/min on a pulse check."]
- serum potassium: not mentioned (unknown)

**A3-G69-C5**

Claims: s = Prescribe trimethoprim-sulfamethoxazole. | s' = Prescribe nitrofurantoin.

Criterion claims: s = Under the rule, the condition "serum potassium above 4.8" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 4.8" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: serum potassium = 4.8 (current) [line: "Latest potassium result: 4.8 mmol/L."]
- patient: heart rate = 82 (current) [line: "Heart rate now 82/min on a pulse check."]


## G70

Rule: For acute sore throat, prescribe ibuprofen. If at least two of the following apply, prescribe penicillin V instead: the patient currently has tonsillar exudate; the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the current white cell count is above 12.0 x10^9/L.

**A3-G70-C1**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 12.9 (current) [line: "Latest WBC is 12.9 x10^9/L."]
- uncle: myocardial infarction or peripheral artery disease present (past) [line: "His uncle had a heart attack years ago."]
- tonsillar exudate: not mentioned (counts as absent)

**A3-G70-C2**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: white cell count = 12.9 (current) [line: "Latest WBC is 12.9 x10^9/L."]
- patient: myocardial infarction or peripheral artery disease present (past) [line: "Recovered from a heart attack in 2024."]
- tonsillar exudate: not mentioned (counts as absent)

**A3-G70-C3**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Man of 20 years.
Sore throat for two days.
Uses sunscreen in summer.
Plays the piano.
Photographs local wildlife.
Sleeps seven hours a night.
Current white cell count 12.9 x10^9/L.
```

Facts (for q1, after q2 and q3):
- patient: white cell count = 12.9 (current) [line: "Current white cell count 12.9 x10^9/L."]
- tonsillar exudate: not mentioned (counts as absent)
- myocardial infarction or peripheral artery disease: not mentioned (counts as absent)

**A3-G70-C4**

Claims: s = Prescribe ibuprofen. | s' = Prescribe penicillin V.

Criterion claims: s = Under the rule, the condition "myocardial infarction or peripheral artery disease" does not hold for this patient. | s' = Under the rule, the condition "myocardial infarction or peripheral artery disease" holds for this patient.
```
Male patient of 20 years.
Sore throat for two days.
Photographs local wildlife.
Latest WBC is 12.9 x10^9/L.
Plays the piano.
Sleeps seven hours a night.
Uses sunscreen in summer.
```

Facts (for q1, after q2 and q3):
- patient: white cell count = 12.9 (current) [line: "Latest WBC is 12.9 x10^9/L."]
- tonsillar exudate: not mentioned (counts as absent)
- myocardial infarction or peripheral artery disease: not mentioned (counts as absent)


## G71

Rule: For vaginal candidiasis, prescribe oral fluconazole. Score 1 point if the current eGFR is below 45 mL/min/1.73 m2; 3 points if the current heart rate is above 90/min; 2 points if the patient has ever had coronary artery disease (current or past). If the score is 6 or more, prescribe clotrimazole pessaries instead.

**A3-G71-C1**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Female patient of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
Prefers morning appointments.
Current eGFR 43 mL/min/1.73 m2.
Heart rate now 98/min on a pulse check.
Has two cats.
Knits as a hobby.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 43 (current) [line: "Current eGFR 43 mL/min/1.73 m2."]
- patient: heart rate = 98 (current) [line: "Heart rate now 98/min on a pulse check."]
- coronary artery disease: not mentioned (counts as absent)

**A3-G71-C2**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: eGFR = 43 (current) [line: "Current eGFR 43 mL/min/1.73 m2."]
- patient: heart rate = 98 (current) [line: "Heart rate now 98/min on a pulse check."]
- sister: coronary artery disease present (current) [line: "Her sister has angina from coronary artery disease."]

**A3-G71-C3**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
```
Woman of 59 years.
Vaginal itching and discharge; candidiasis confirmed on microscopy.
eGFR now 43 mL/min/1.73 m2.
Knits as a hobby.
Prefers morning appointments.
Has two cats.
Current heart rate 98/min.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 43 (current) [line: "eGFR now 43 mL/min/1.73 m2."]
- patient: heart rate = 98 (current) [line: "Current heart rate 98/min."]
- coronary artery disease: not mentioned (counts as absent)

**A3-G71-C4**

Claims: s = Prescribe oral fluconazole. | s' = Prescribe clotrimazole pessaries.

Criterion claims: s = Under the rule, the condition "coronary artery disease" does not hold for this patient. | s' = Under the rule, the condition "coronary artery disease" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: eGFR = 43 (current) [line: "Current eGFR 43 mL/min/1.73 m2."]
- patient: heart rate = 98 (current) [line: "Heart rate now 98/min on a pulse check."]
- patient: coronary artery disease present (current) [line: "Known coronary artery disease (two-vessel disease on angiography)."]


## G72

Rule: For knee osteoarthritis pain, prescribe naproxen. If the patient's current eGFR is below 75 mL/min/1.73 m2, prescribe acetaminophen instead.

**A3-G72-C1**

Claims: s = Prescribe naproxen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "eGFR below 75" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 75" holds for this patient.
```
Male patient of 55 years.
Knee osteoarthritis with pain on walking.
Current eGFR 100 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
Sleeps seven hours a night.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 100 (current) [line: "Current eGFR 100 mL/min/1.73 m2."]

**A3-G72-C2**

Claims: s = Prescribe naproxen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "eGFR below 75" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 75" holds for this patient.
```
Man of 55 years.
Knee osteoarthritis with pain on walking.
Sleeps seven hours a night.
eGFR now 100 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 100 (current) [line: "eGFR now 100 mL/min/1.73 m2."]

**A3-G72-C3**

Claims: s = Prescribe naproxen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "eGFR below 75" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 75" holds for this patient.
```
Male patient of 55 years.
Knee osteoarthritis with pain on walking.
Current eGFR 75 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
Sleeps seven hours a night.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 75 (current) [line: "Current eGFR 75 mL/min/1.73 m2."]

**A3-G72-C4**

Claims: s = Prescribe naproxen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "eGFR below 75" does not hold for this patient. | s' = Under the rule, the condition "eGFR below 75" holds for this patient.
```
Male patient of 55 years.
Knee osteoarthritis with pain on walking.
Current eGFR 63 mL/min/1.73 m2.
Photographs local wildlife.
Prefers morning appointments.
Sleeps seven hours a night.
```

Facts (for q1, after q2 and q3):
- patient: eGFR = 63 (current) [line: "Current eGFR 63 mL/min/1.73 m2."]


## G73

Rule: For newly diagnosed hypertension, prescribe lisinopril. If the patient has ever had a peptic ulcer (current or past) and the current blood urea nitrogen is above 19 mg/dL, prescribe amlodipine instead.

**A3-G73-C1**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 10 (past) [line: "Back in 2023, blood urea nitrogen stood at 10 mg/dL."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: blood urea nitrogen = 28 (current) [line: "Blood urea nitrogen now: 28 mg/dL."]

**A3-G73-C2**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- blood urea nitrogen: not mentioned (unknown)

**A3-G73-C3**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 23 (past) [line: "Back in 2023, blood urea nitrogen stood at 23 mg/dL."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: blood urea nitrogen = 10 (current) [line: "Blood urea nitrogen now: 10 mg/dL."]

**A3-G73-C4**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: blood urea nitrogen = 10 (past) [line: "Back in 2023, blood urea nitrogen stood at 10 mg/dL."]
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: blood urea nitrogen = 10 (current) [line: "Blood urea nitrogen now: 10 mg/dL."]

**A3-G73-C5**

Claims: s = Prescribe lisinopril. | s' = Prescribe amlodipine.

Criterion claims: s = Under the rule, the condition "blood urea nitrogen above 19" does not hold for this patient. | s' = Under the rule, the condition "blood urea nitrogen above 19" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: peptic ulcer present (past) [line: "Duodenal ulcer years ago; recovered fully with treatment."]
- patient: blood urea nitrogen = 10 (past) [line: "Records from 2023 list blood urea nitrogen at 10 mg/dL."]
- patient: blood urea nitrogen = 10 (current) [line: "Blood urea nitrogen 10 mg/dL on the current labs."]


## G74

Rule: For Delmar fever, prescribe fenrastat. If at least two of the following apply, prescribe kivolane instead: the patient has ever had a myocardial infarction or peripheral artery disease (current or past); the patient has ever had a peptic ulcer (current or past); the patient is currently taking clarithromycin.

**A3-G74-C1**

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "clarithromycin" does not hold for this patient. | s' = Under the rule, the condition "clarithromycin" holds for this patient.
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

Facts (for q1, after q2 and q3):
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]
- clarithromycin: not named; a general line implies absence (counts as absent) [line: "Has no antibiotic course under way."]
- patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

**A3-G74-C2**

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "clarithromycin" does not hold for this patient. | s' = Under the rule, the condition "clarithromycin" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: clarithromycin present (current) [line: "On clarithromycin for a chest infection, day 3 of 7."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]
- patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

**A3-G74-C3**

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "clarithromycin" does not hold for this patient. | s' = Under the rule, the condition "clarithromycin" holds for this patient.
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

Facts (for q1, after q2 and q3):
- patient: clarithromycin present (past) [line: "Formerly took clarithromycin for a chest infection in 2023."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]
- patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]

**A3-G74-C4**

Claims: s = Prescribe fenrastat. | s' = Prescribe kivolane.

Criterion claims: s = Under the rule, the condition "clarithromycin" does not hold for this patient. | s' = Under the rule, the condition "clarithromycin" holds for this patient.
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

Facts (for q1, after q2 and q3):
- clarithromycin: not named; a general line implies absence (counts as absent) [line: "Has no antibiotic course under way."]
- peptic ulcer: not named; a general line implies absence (counts as absent) [line: "Appetite good; no indigestion."]
- patient: myocardial infarction or peripheral artery disease present (current) [line: "Lives with peripheral artery disease affecting the left leg."]


## G75

Rule: For musculoskeletal pain, prescribe ibuprofen. If at least two of the following apply, prescribe acetaminophen instead: the patient currently has tonsillar exudate; the current serum potassium is above 5.0 mmol/L; the patient has ever had coronary artery disease (current or past).

**A3-G75-C1**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 48 years.
Acute low back pain after lifting.
Tonsils swollen and coated with yellow exudate.
Last month, serum potassium was 5.6 mmol/L; the newest measurement replaces it.
Latest potassium result: 4.3 mmol/L.
Plays the piano.
Prefers to be addressed by first name.
```

Facts (for q1, after q2 and q3):
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: serum potassium = 5.6 (past) [line: "Last month, serum potassium was 5.6 mmol/L; the newest measurement replaces it."]
- patient: serum potassium = 4.3 (current) [line: "Latest potassium result: 4.3 mmol/L."]
- coronary artery disease: not mentioned (counts as absent)

**A3-G75-C2**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 48 years.
Acute low back pain after lifting.
Tonsils swollen and coated with yellow exudate.
Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it.
Latest potassium result: 5.3 mmol/L.
Plays the piano.
Prefers to be addressed by first name.
```

Facts (for q1, after q2 and q3):
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: serum potassium = 4.5 (past) [line: "Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it."]
- patient: serum potassium = 5.3 (current) [line: "Latest potassium result: 5.3 mmol/L."]
- coronary artery disease: not mentioned (counts as absent)

**A3-G75-C3**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Man of 48 years.
Acute low back pain after lifting.
Tonsils swollen and coated with yellow exudate.
Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it.
Latest potassium result: 4.3 mmol/L.
Plays the piano.
Prefers to be addressed by first name.
```

Facts (for q1, after q2 and q3):
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: serum potassium = 4.5 (past) [line: "Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it."]
- patient: serum potassium = 4.3 (current) [line: "Latest potassium result: 4.3 mmol/L."]
- coronary artery disease: not mentioned (counts as absent)

**A3-G75-C4**

Claims: s = Prescribe ibuprofen. | s' = Prescribe acetaminophen.

Criterion claims: s = Under the rule, the condition "serum potassium above 5.0" does not hold for this patient. | s' = Under the rule, the condition "serum potassium above 5.0" holds for this patient.
```
Male patient of 48 years.
Acute low back pain after lifting.
Prefers to be addressed by first name.
Tonsils swollen and coated with yellow exudate.
Plays the piano.
Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it.
Current serum potassium 4.3 mmol/L.
```

Facts (for q1, after q2 and q3):
- patient: tonsillar exudate present (current) [line: "Tonsils swollen and coated with yellow exudate."]
- patient: serum potassium = 4.5 (past) [line: "Last month, serum potassium was 4.5 mmol/L; the newest measurement replaces it."]
- patient: serum potassium = 4.3 (current) [line: "Current serum potassium 4.3 mmol/L."]
- coronary artery disease: not mentioned (counts as absent)
