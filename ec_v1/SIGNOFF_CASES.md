# ec_v1: every rendered case, by criterion (H3)

Answers are the program's: base, near-miss and presentation cases do not meet the criterion, the flip meets it. Sign off a criterion's cases only if every case below is unambiguous under its rule text.

Conventions the answers follow (as in ec_v1/SIGNOFF_GUIDE.md): a condition the case does not mention is absent; a general line ("No allergies.") means absence; a finding counts only now unless the rule text counts the past; a measurement counts only as its current value; 'above'/'below' are strict and 'or more'/'or less' inclusive; ages are in completed years.

<a id="k001"></a>
## k001 (NCT02204488)

Inclusion criterion: 40 years of age or more.

Program: met iff the patient's current age >= 40 years

### near-miss kind: numeric

**base** (does not meet)
```
Woman, adult.
Screening visit for a clinical trial.
Photographs local wildlife.
Drives a car.
Uses sunscreen in summer.
Currently aged 30 years.
```

**flip** (meets)
```
Woman, adult.
Screening visit for a clinical trial.
Photographs local wildlife.
Drives a car.
Uses sunscreen in summer.
Currently aged 40 years.
```

**near** (does not meet)
```
Woman, adult.
Screening visit for a clinical trial.
Photographs local wildlife.
Drives a car.
Uses sunscreen in summer.
Currently aged 38 years.
```

**pres** (does not meet)
```
An adult woman.
Screening visit for a clinical trial.
Current age 30 years.
Drives a car.
Uses sunscreen in summer.
Photographs local wildlife.
```

<a id="k005"></a>
## k005 (NCT00743639)

Inclusion criterion: Age below 70 years

Program: met iff the patient's current age < 70 years

### near-miss kind: boundary

**base** (does not meet)
```
An adult woman.
Screening visit for a clinical trial.
Currently aged 79 years.
Photographs local wildlife.
```

**flip** (meets)
```
An adult woman.
Screening visit for a clinical trial.
Currently aged 66 years.
Photographs local wildlife.
```

**near** (does not meet)
```
An adult woman.
Screening visit for a clinical trial.
Currently aged 70 years.
Photographs local wildlife.
```

**pres** (does not meet)
```
Woman, adult.
Screening visit for a clinical trial.
Photographs local wildlife.
Current age 79 years.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman, adult.
Screening visit for a clinical trial.
Has two cats.
Plays the piano.
Currently aged 77 years.
```

**flip** (meets)
```
Woman, adult.
Screening visit for a clinical trial.
Has two cats.
Plays the piano.
Currently aged 60 years.
```

**near** (does not meet)
```
Woman, adult.
Screening visit for a clinical trial.
Has two cats.
Plays the piano.
Currently aged 72 years.
```

**pres** (does not meet)
```
An adult woman.
Screening visit for a clinical trial.
Plays the piano.
Current age 77 years.
Has two cats.
```

<a id="k007"></a>
## k007 (NCT03234322)

Inclusion criterion: age > 35 years

Program: met iff the patient's current age > 35 years

### near-miss kind: numeric

**base** (does not meet)
```
Man, adult.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Enjoys board games.
Currently aged 22 years.
Prefers morning appointments.
```

**flip** (meets)
```
Man, adult.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Enjoys board games.
Currently aged 38 years.
Prefers morning appointments.
```

**near** (does not meet)
```
Man, adult.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Enjoys board games.
Currently aged 33 years.
Prefers morning appointments.
```

**pres** (does not meet)
```
An adult man.
Screening visit for a clinical trial.
Enjoys board games.
Prefers morning appointments.
Paints watercolors as a hobby.
Current age 22 years.
```

<a id="k017"></a>
## k017 (NCT02924727)

Exclusion criterion: Patients with a known history of angioedema

Program: met iff the patient has angioedema at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Has two cats.
Face and neck without swelling on examination.
```

**flip** (meets)
```
Woman of 36 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Has two cats.
An episode of angioedema years ago, with full recovery.
```

**near** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Has two cats.
Never diagnosed with angioedema.
```

**pres** (does not meet)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Has two cats.
Face and neck without swelling on examination.
Prefers to be addressed by first name.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 32 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Free of facial or oropharyngeal edema.
Knits as a hobby.
Sleeps seven hours a night.
```

**flip** (meets)
```
Woman of 32 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Lives with chronic angioedema that flares several times a year.
Knits as a hobby.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Woman of 32 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Her father is being treated for angioedema.
Knits as a hobby.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Female patient of 32 years.
Screening visit for a clinical trial.
Plays the piano.
Knits as a hobby.
Free of facial or oropharyngeal edema.
Sleeps seven hours a night.
Paints watercolors as a hobby.
```

<a id="k031"></a>
## k031 (NCT00916773)

Exclusion criterion: Clinical asthma

Program: met iff the patient has asthma now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Lungs clear, without wheeze or prolonged expiration.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
```

**flip** (meets)
```
Man of 50 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Asthma, on a daily inhaled steroid.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
```

**near** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Asthma ruled out on lung function testing.
Plays the piano.
Owns a bicycle.
Teeth in good repair.
```

**pres** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Teeth in good repair.
Owns a bicycle.
Plays the piano.
Lungs clear, without wheeze or prolonged expiration.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 41 years.
Screening visit for a clinical trial.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Man of 41 years.
Screening visit for a clinical trial.
Owns a bicycle.
Persistent asthma, using a rescue inhaler most weeks.
Pupils equal and reactive to light.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Man of 41 years.
Screening visit for a clinical trial.
Owns a bicycle.
His roommate uses an inhaler for asthma.
Pupils equal and reactive to light.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Male patient of 41 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
```

<a id="k045"></a>
## k045 (NCT03664167)

Inclusion criterion: BMI >30kg/m2

Program: met iff the patient's current body mass index > 30 kg/m2

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Has two cats.
Current body mass index 24.6 kg/m2.
Owns a bicycle.
```

**flip** (meets)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Has two cats.
Current body mass index 32.6 kg/m2.
Owns a bicycle.
```

**near** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Has two cats.
Current body mass index 30.0 kg/m2.
Owns a bicycle.
```

**pres** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Owns a bicycle.
Paints watercolors as a hobby.
Latest BMI is 24.6 kg/m2.
Has two cats.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 40 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Latest BMI is 27.3 kg/m2.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Woman of 40 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Latest BMI is 30.2 kg/m2.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Woman of 40 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Latest BMI is 28.7 kg/m2.
Lives in a second-floor apartment.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Female patient of 40 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Pupils equal and reactive to light.
Lives in a second-floor apartment.
Sees a dentist yearly.
Current body mass index 27.3 kg/m2.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 46 years.
Screening visit for a clinical trial.
Knits as a hobby.
Back in 2019, body mass index stood at 27.9 kg/m2.
Current body mass index 18.2 kg/m2.
Photographs local wildlife.
```

**flip** (meets)
```
Man of 46 years.
Screening visit for a clinical trial.
Knits as a hobby.
Back in 2019, body mass index stood at 27.9 kg/m2.
Current body mass index 33.7 kg/m2.
Photographs local wildlife.
```

**near** (does not meet)
```
Man of 46 years.
Screening visit for a clinical trial.
Knits as a hobby.
Back in 2019, body mass index stood at 32.2 kg/m2.
Current body mass index 18.2 kg/m2.
Photographs local wildlife.
```

**pres** (does not meet)
```
Male patient of 46 years.
Screening visit for a clinical trial.
Latest BMI is 18.2 kg/m2.
Records from 2019 list body mass index at 27.9 kg/m2.
Knits as a hobby.
Photographs local wildlife.
```

<a id="k046"></a>
## k046 (NCT03368599)

Exclusion criterion: Obesity (BMI ≥ 35 kg/m2)

Program: met iff the patient's current body mass index >= 35 kg/m2

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Current body mass index 27.9 kg/m2.
Lives in a second-floor apartment.
Drives a car.
```

**flip** (meets)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Current body mass index 36.2 kg/m2.
Lives in a second-floor apartment.
Drives a car.
```

**near** (does not meet)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Current body mass index 34.2 kg/m2.
Lives in a second-floor apartment.
Drives a car.
```

**pres** (does not meet)
```
Woman of 57 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Drives a car.
Latest BMI is 27.9 kg/m2.
Knits as a hobby.
Lives in a second-floor apartment.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 39 years.
Screening visit for a clinical trial.
Has two cats.
Current body mass index 32.8 kg/m2.
Knits as a hobby.
Records from 2012 list body mass index at 28.2 kg/m2.
```

**flip** (meets)
```
Man of 39 years.
Screening visit for a clinical trial.
Has two cats.
Current body mass index 37.9 kg/m2.
Knits as a hobby.
Records from 2012 list body mass index at 28.2 kg/m2.
```

**near** (does not meet)
```
Man of 39 years.
Screening visit for a clinical trial.
Has two cats.
Current body mass index 32.8 kg/m2.
Knits as a hobby.
Records from 2012 list body mass index at 35.4 kg/m2.
```

**pres** (does not meet)
```
Male patient of 39 years.
Screening visit for a clinical trial.
Knits as a hobby.
Has two cats.
Latest BMI is 32.8 kg/m2.
Back in 2012, body mass index stood at 28.2 kg/m2.
```

<a id="k047"></a>
## k047 (NCT02056678)

Inclusion criterion: Obesity (BMI greater than or equal to 30 kg/m2)

Program: met iff the patient's current body mass index >= 30 kg/m2

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Latest BMI is 20.8 kg/m2.
Teeth in good repair.
```

**flip** (meets)
```
Woman of 36 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Latest BMI is 33.9 kg/m2.
Teeth in good repair.
```

**near** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Latest BMI is 28.7 kg/m2.
Teeth in good repair.
```

**pres** (does not meet)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Teeth in good repair.
Current body mass index 20.8 kg/m2.
Knits as a hobby.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 49 years.
Screening visit for a clinical trial.
Owns a bicycle.
Back in 2013, body mass index stood at 21.6 kg/m2.
Current body mass index 19.6 kg/m2.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

**flip** (meets)
```
Man of 49 years.
Screening visit for a clinical trial.
Owns a bicycle.
Back in 2013, body mass index stood at 21.6 kg/m2.
Current body mass index 30.0 kg/m2.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Man of 49 years.
Screening visit for a clinical trial.
Owns a bicycle.
Back in 2013, body mass index stood at 30.7 kg/m2.
Current body mass index 19.6 kg/m2.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Male patient of 49 years.
Screening visit for a clinical trial.
Latest BMI is 19.6 kg/m2.
Records from 2013 list body mass index at 21.6 kg/m2.
Owns a bicycle.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

<a id="k049"></a>
## k049 (NCT07538726)

Exclusion criterion: Morbid obesity (BMI > 40 kg/m2)

Program: met iff the patient's current body mass index > 40 kg/m2

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 53 years.
Screening visit for a clinical trial.
Latest BMI is 29.0 kg/m2.
Sleeps seven hours a night.
Prefers morning appointments.
```

**flip** (meets)
```
Female patient of 53 years.
Screening visit for a clinical trial.
Latest BMI is 40.1 kg/m2.
Sleeps seven hours a night.
Prefers morning appointments.
```

**near** (does not meet)
```
Female patient of 53 years.
Screening visit for a clinical trial.
Latest BMI is 39.0 kg/m2.
Sleeps seven hours a night.
Prefers morning appointments.
```

**pres** (does not meet)
```
Woman of 53 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current body mass index 29.0 kg/m2.
Sleeps seven hours a night.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 54 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Has two cats.
Back in 2016, body mass index stood at 32.3 kg/m2.
Latest BMI is 28.8 kg/m2.
Enjoys board games.
```

**flip** (meets)
```
Woman of 54 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Has two cats.
Back in 2016, body mass index stood at 32.3 kg/m2.
Latest BMI is 43.6 kg/m2.
Enjoys board games.
```

**near** (does not meet)
```
Woman of 54 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Has two cats.
Back in 2016, body mass index stood at 41.1 kg/m2.
Latest BMI is 28.8 kg/m2.
Enjoys board games.
```

**pres** (does not meet)
```
Female patient of 54 years.
Screening visit for a clinical trial.
Enjoys board games.
Current body mass index 28.8 kg/m2.
Records from 2016 list body mass index at 32.3 kg/m2.
Has two cats.
Paints watercolors as a hobby.
```

<a id="k050"></a>
## k050 (NCT02682563)

Inclusion criterion: BMI: >25 kg/m2

Program: met iff the patient's current body mass index > 25 kg/m2

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Current body mass index 17.7 kg/m2.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Drives a car.
```

**flip** (meets)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Current body mass index 26.0 kg/m2.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Drives a car.
```

**near** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Current body mass index 25.0 kg/m2.
Uses sunscreen in summer.
Paints watercolors as a hobby.
Drives a car.
```

**pres** (does not meet)
```
Man of 47 years.
Screening visit for a clinical trial.
Latest BMI is 17.7 kg/m2.
Paints watercolors as a hobby.
Drives a car.
Uses sunscreen in summer.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Latest BMI is 23.0 kg/m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Latest BMI is 26.3 kg/m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Latest BMI is 24.8 kg/m2.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Man of 71 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Current body mass index 23.0 kg/m2.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Current body mass index 17.8 kg/m2.
Records from 2017 list body mass index at 21.2 kg/m2.
Sees a dentist yearly.
Photographs local wildlife.
Owns a bicycle.
```

**flip** (meets)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Current body mass index 25.7 kg/m2.
Records from 2017 list body mass index at 21.2 kg/m2.
Sees a dentist yearly.
Photographs local wildlife.
Owns a bicycle.
```

**near** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Current body mass index 17.8 kg/m2.
Records from 2017 list body mass index at 28.8 kg/m2.
Sees a dentist yearly.
Photographs local wildlife.
Owns a bicycle.
```

**pres** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Photographs local wildlife.
Back in 2017, body mass index stood at 21.2 kg/m2.
Owns a bicycle.
Latest BMI is 17.8 kg/m2.
```

<a id="k051"></a>
## k051 (NCT03804697)

Inclusion criterion: BMI <40Kg / M ^ 2

Program: met iff the patient's current body mass index < 40 kg/m2

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 56 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Photographs local wildlife.
Knits as a hobby.
Owns a bicycle.
Latest BMI is 47.2 kg/m2.
```

**flip** (meets)
```
Female patient of 56 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Photographs local wildlife.
Knits as a hobby.
Owns a bicycle.
Latest BMI is 39.7 kg/m2.
```

**near** (does not meet)
```
Female patient of 56 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Photographs local wildlife.
Knits as a hobby.
Owns a bicycle.
Latest BMI is 40.0 kg/m2.
```

**pres** (does not meet)
```
Woman of 56 years.
Screening visit for a clinical trial.
Owns a bicycle.
Photographs local wildlife.
Pupils equal and reactive to light.
Knits as a hobby.
Current body mass index 47.2 kg/m2.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 45 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Current body mass index 48.2 kg/m2.
Has two cats.
Plays the piano.
```

**flip** (meets)
```
Male patient of 45 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Current body mass index 36.7 kg/m2.
Has two cats.
Plays the piano.
```

**near** (does not meet)
```
Male patient of 45 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Current body mass index 41.0 kg/m2.
Has two cats.
Plays the piano.
```

**pres** (does not meet)
```
Man of 45 years.
Screening visit for a clinical trial.
Plays the piano.
Has two cats.
Lives in a second-floor apartment.
Latest BMI is 48.2 kg/m2.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 83 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Records from 2012 list body mass index at 45.1 kg/m2.
Sleeps seven hours a night.
Latest BMI is 43.3 kg/m2.
```

**flip** (meets)
```
Male patient of 83 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Records from 2012 list body mass index at 45.1 kg/m2.
Sleeps seven hours a night.
Latest BMI is 35.6 kg/m2.
```

**near** (does not meet)
```
Male patient of 83 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Records from 2012 list body mass index at 37.1 kg/m2.
Sleeps seven hours a night.
Latest BMI is 43.3 kg/m2.
```

**pres** (does not meet)
```
Man of 83 years.
Screening visit for a clinical trial.
Teeth in good repair.
Back in 2012, body mass index stood at 45.1 kg/m2.
Lives in a second-floor apartment.
Sleeps seven hours a night.
Current body mass index 43.3 kg/m2.
```

<a id="k052"></a>
## k052 (NCT04422405)

Inclusion criterion: BMI> 35 kg/m2

Program: met iff the patient's current body mass index > 35 kg/m2

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Latest BMI is 33.6 kg/m2.
Owns a bicycle.
Photographs local wildlife.
```

**flip** (meets)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Latest BMI is 36.0 kg/m2.
Owns a bicycle.
Photographs local wildlife.
```

**near** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Latest BMI is 35.0 kg/m2.
Owns a bicycle.
Photographs local wildlife.
```

**pres** (does not meet)
```
Man of 47 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Owns a bicycle.
Photographs local wildlife.
Current body mass index 33.6 kg/m2.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Current body mass index 32.2 kg/m2.
Owns a bicycle.
Paints watercolors as a hobby.
Sees a dentist yearly.
Teeth in good repair.
```

**flip** (meets)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Current body mass index 38.4 kg/m2.
Owns a bicycle.
Paints watercolors as a hobby.
Sees a dentist yearly.
Teeth in good repair.
```

**near** (does not meet)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Current body mass index 34.2 kg/m2.
Owns a bicycle.
Paints watercolors as a hobby.
Sees a dentist yearly.
Teeth in good repair.
```

**pres** (does not meet)
```
Man of 51 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Latest BMI is 32.2 kg/m2.
Teeth in good repair.
Owns a bicycle.
Paints watercolors as a hobby.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Back in 2006, body mass index stood at 33.5 kg/m2.
Latest BMI is 27.8 kg/m2.
```

**flip** (meets)
```
Woman of 48 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Back in 2006, body mass index stood at 33.5 kg/m2.
Latest BMI is 38.8 kg/m2.
```

**near** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Back in 2006, body mass index stood at 35.5 kg/m2.
Latest BMI is 27.8 kg/m2.
```

**pres** (does not meet)
```
Female patient of 48 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Current body mass index 27.8 kg/m2.
Records from 2006 list body mass index at 33.5 kg/m2.
```

<a id="k053"></a>
## k053 (NCT01545349)

Exclusion criterion: Blood urea nitrogen (BUN) > 27 mg/dL

Program: met iff the patient's current blood urea nitrogen > 27 mg/dL

### near-miss kind: boundary

**base** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Knits as a hobby.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Blood urea nitrogen 10 mg/dL on the current labs.
```

**flip** (meets)
```
Man of 67 years.
Screening visit for a clinical trial.
Knits as a hobby.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Blood urea nitrogen 35 mg/dL on the current labs.
```

**near** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Knits as a hobby.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
Blood urea nitrogen 27 mg/dL on the current labs.
```

**pres** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Knits as a hobby.
Blood urea nitrogen now: 10 mg/dL.
Lives in a second-floor apartment.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 77 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Blood urea nitrogen 7 mg/dL on the current labs.
Pupils equal and reactive to light.
Plays the piano.
```

**flip** (meets)
```
Male patient of 77 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Blood urea nitrogen 35 mg/dL on the current labs.
Pupils equal and reactive to light.
Plays the piano.
```

**near** (does not meet)
```
Male patient of 77 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Blood urea nitrogen 26 mg/dL on the current labs.
Pupils equal and reactive to light.
Plays the piano.
```

**pres** (does not meet)
```
Man of 77 years.
Screening visit for a clinical trial.
Plays the piano.
Sleeps seven hours a night.
Blood urea nitrogen now: 7 mg/dL.
Pupils equal and reactive to light.
Knits as a hobby.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 65 years.
Screening visit for a clinical trial.
Blood urea nitrogen 6 mg/dL on the current labs.
Enjoys board games.
Prefers morning appointments.
Pupils equal and reactive to light.
Owns a bicycle.
Back in 2006, blood urea nitrogen stood at 18 mg/dL.
```

**flip** (meets)
```
Man of 65 years.
Screening visit for a clinical trial.
Blood urea nitrogen 29 mg/dL on the current labs.
Enjoys board games.
Prefers morning appointments.
Pupils equal and reactive to light.
Owns a bicycle.
Back in 2006, blood urea nitrogen stood at 18 mg/dL.
```

**near** (does not meet)
```
Man of 65 years.
Screening visit for a clinical trial.
Blood urea nitrogen 6 mg/dL on the current labs.
Enjoys board games.
Prefers morning appointments.
Pupils equal and reactive to light.
Owns a bicycle.
Back in 2006, blood urea nitrogen stood at 31 mg/dL.
```

**pres** (does not meet)
```
Male patient of 65 years.
Screening visit for a clinical trial.
Owns a bicycle.
Pupils equal and reactive to light.
Blood urea nitrogen now: 6 mg/dL.
Records from 2006 list blood urea nitrogen at 18 mg/dL.
Prefers morning appointments.
Enjoys board games.
```

<a id="k058"></a>
## k058 (NCT01219959)

Exclusion criterion: Blood Urea Nitrogen (BUN) > 95 mg/dL

Program: met iff the patient's current blood urea nitrogen > 95 mg/dL

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 48 years.
Screening visit for a clinical trial.
Blood urea nitrogen now: 79 mg/dL.
Has two cats.
```

**flip** (meets)
```
Male patient of 48 years.
Screening visit for a clinical trial.
Blood urea nitrogen now: 97 mg/dL.
Has two cats.
```

**near** (does not meet)
```
Male patient of 48 years.
Screening visit for a clinical trial.
Blood urea nitrogen now: 95 mg/dL.
Has two cats.
```

**pres** (does not meet)
```
Man of 48 years.
Screening visit for a clinical trial.
Has two cats.
Blood urea nitrogen 79 mg/dL on the current labs.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 68 years.
Screening visit for a clinical trial.
Blood urea nitrogen 64 mg/dL on the current labs.
Enjoys board games.
Prefers morning appointments.
```

**flip** (meets)
```
Man of 68 years.
Screening visit for a clinical trial.
Blood urea nitrogen 97 mg/dL on the current labs.
Enjoys board games.
Prefers morning appointments.
```

**near** (does not meet)
```
Man of 68 years.
Screening visit for a clinical trial.
Blood urea nitrogen 93 mg/dL on the current labs.
Enjoys board games.
Prefers morning appointments.
```

**pres** (does not meet)
```
Male patient of 68 years.
Screening visit for a clinical trial.
Blood urea nitrogen now: 64 mg/dL.
Prefers morning appointments.
Enjoys board games.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Drives a car.
Blood urea nitrogen now: 73 mg/dL.
Prefers to be addressed by first name.
Records from 2007 list blood urea nitrogen at 83 mg/dL.
```

**flip** (meets)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Drives a car.
Blood urea nitrogen now: 99 mg/dL.
Prefers to be addressed by first name.
Records from 2007 list blood urea nitrogen at 83 mg/dL.
```

**near** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Drives a car.
Blood urea nitrogen now: 73 mg/dL.
Prefers to be addressed by first name.
Records from 2007 list blood urea nitrogen at 97 mg/dL.
```

**pres** (does not meet)
```
Man of 47 years.
Screening visit for a clinical trial.
Blood urea nitrogen 73 mg/dL on the current labs.
Back in 2007, blood urea nitrogen stood at 83 mg/dL.
Prefers to be addressed by first name.
Drives a car.
```

<a id="k062"></a>
## k062 (NCT03674021)

Exclusion criterion: Have known coronary artery disease

Program: met iff the patient has coronary artery disease now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Cardiac stress test unremarkable last year.
Prefers morning appointments.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Woman of 31 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Has coronary artery disease, managed medically.
Prefers morning appointments.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Never diagnosed with coronary artery disease.
Prefers morning appointments.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Lives in a second-floor apartment.
Cardiac stress test unremarkable last year.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Drives a car.
Plays the piano.
Cardiac stress test unremarkable last year.
Sees a dentist yearly.
```

**flip** (meets)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Drives a car.
Plays the piano.
Has coronary artery disease, managed medically.
Sees a dentist yearly.
```

**near** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Drives a car.
Plays the piano.
His wife has angina from coronary artery disease.
Sees a dentist yearly.
```

**pres** (does not meet)
```
Man of 63 years.
Screening visit for a clinical trial.
Cardiac stress test unremarkable last year.
Drives a car.
Sees a dentist yearly.
Plays the piano.
```

<a id="k065"></a>
## k065 (NCT04609605)

Exclusion criterion: coronary artery disease

Program: met iff the patient has coronary artery disease now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Enjoys board games.
Cardiac stress test unremarkable last year.
Sees a dentist yearly.
```

**flip** (meets)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Enjoys board games.
Known coronary artery disease (two-vessel disease on angiography).
Sees a dentist yearly.
```

**near** (does not meet)
```
Male patient of 47 years.
Screening visit for a clinical trial.
Enjoys board games.
Never diagnosed with coronary artery disease.
Sees a dentist yearly.
```

**pres** (does not meet)
```
Man of 47 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Cardiac stress test unremarkable last year.
Enjoys board games.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 60 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Owns a bicycle.
Cardiac stress test unremarkable last year.
Sees a dentist yearly.
```

**flip** (meets)
```
Female patient of 60 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Owns a bicycle.
Known coronary artery disease (two-vessel disease on angiography).
Sees a dentist yearly.
```

**near** (does not meet)
```
Female patient of 60 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Owns a bicycle.
Her father has known coronary artery disease.
Sees a dentist yearly.
```

**pres** (does not meet)
```
Woman of 60 years.
Screening visit for a clinical trial.
Owns a bicycle.
Sees a dentist yearly.
Prefers to be addressed by first name.
Cardiac stress test unremarkable last year.
```

<a id="k067"></a>
## k067 (NCT04508439)

Exclusion criterion: History of active or inactive cancer

Program: met iff the patient has cancer at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Drives a car.
Teeth in good repair.
Paints watercolors as a hobby.
Plays the piano.
```

**flip** (meets)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Had thyroid cancer years ago and is now cured.
Drives a car.
Teeth in good repair.
Paints watercolors as a hobby.
Plays the piano.
```

**near** (does not meet)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Has never had cancer.
Drives a car.
Teeth in good repair.
Paints watercolors as a hobby.
Plays the piano.
```

**pres** (does not meet)
```
Woman of 33 years.
Screening visit for a clinical trial.
Plays the piano.
Drives a car.
Teeth in good repair.
Paints watercolors as a hobby.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 55 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Weight steady over the past year.
```

**flip** (meets)
```
Female patient of 55 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Formerly had kidney cancer, cured by surgery in 2013.
```

**near** (does not meet)
```
Female patient of 55 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Her father was formerly treated for myeloma.
```

**pres** (does not meet)
```
Woman of 55 years.
Screening visit for a clinical trial.
Weight steady over the past year.
Uses sunscreen in summer.
```

<a id="k075"></a>
## k075 (NCT02653209)

Exclusion criterion: History of heart failure

Program: met iff the patient has heart failure at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 78 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Enjoys board games.
Plays the piano.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Male patient of 78 years.
Screening visit for a clinical trial.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2010 and off all heart medicines since.
Uses sunscreen in summer.
Enjoys board games.
Plays the piano.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Male patient of 78 years.
Screening visit for a clinical trial.
Has never had heart failure.
Uses sunscreen in summer.
Enjoys board games.
Plays the piano.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Man of 78 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Uses sunscreen in summer.
Enjoys board games.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 65 years.
Screening visit for a clinical trial.
Enjoys board games.
Heart sounds without a gallop.
Has two cats.
```

**flip** (meets)
```
Male patient of 65 years.
Screening visit for a clinical trial.
Enjoys board games.
Formerly had heart failure from stress cardiomyopathy; recovered fully in 2023 and off all heart medicines since.
Has two cats.
```

**near** (does not meet)
```
Male patient of 65 years.
Screening visit for a clinical trial.
Enjoys board games.
His sister had heart failure long ago and made a full recovery.
Has two cats.
```

**pres** (does not meet)
```
Man of 65 years.
Screening visit for a clinical trial.
Has two cats.
Heart sounds without a gallop.
Enjoys board games.
```

<a id="k089"></a>
## k089 (NCT04067505)

Exclusion criterion: Allergic to iodine contrast agents in the past

Program: met iff the patient has an allergy to iodinated contrast at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Plays the piano.
Uses sunscreen in summer.
```

**flip** (meets)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Formerly allergic to iodinated contrast; has since had several contrast scans uneventfully.
Plays the piano.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Has never been allergic to iodinated contrast.
Plays the piano.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Man of 53 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Sees a dentist yearly.
Plays the piano.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 44 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Reports no allergies of any kind.
Has two cats.
```

**flip** (meets)
```
Man of 44 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
An iodinated contrast allergy recorded years ago has been outgrown; recent contrast scans were uneventful.
Has two cats.
```

**near** (does not meet)
```
Man of 44 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
His sister needs premedication before iodinated contrast because of an allergy.
Has two cats.
```

**pres** (does not meet)
```
Male patient of 44 years.
Screening visit for a clinical trial.
Has two cats.
Reports no allergies of any kind.
Lives in a second-floor apartment.
```

<a id="k095"></a>
## k095 (NCT01736514)

Exclusion criterion: Subject who has serum creatinine >= 1.5mg/dL

Program: met iff the patient's current serum creatinine >= 1.5 mg/dL

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 58 years.
Screening visit for a clinical trial.
Current serum creatinine 0.9 mg/dL.
Sleeps seven hours a night.
```

**flip** (meets)
```
Woman of 58 years.
Screening visit for a clinical trial.
Current serum creatinine 1.5 mg/dL.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Woman of 58 years.
Screening visit for a clinical trial.
Current serum creatinine 1.4 mg/dL.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Female patient of 58 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest creatinine result: 0.9 mg/dL.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 57 years.
Screening visit for a clinical trial.
Drives a car.
Latest creatinine result: 1.1 mg/dL.
Back in 2005, serum creatinine stood at 1.3 mg/dL.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Woman of 57 years.
Screening visit for a clinical trial.
Drives a car.
Latest creatinine result: 1.7 mg/dL.
Back in 2005, serum creatinine stood at 1.3 mg/dL.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Woman of 57 years.
Screening visit for a clinical trial.
Drives a car.
Latest creatinine result: 1.1 mg/dL.
Back in 2005, serum creatinine stood at 1.9 mg/dL.
Prefers to be addressed by first name.
Teeth in good repair.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Drives a car.
Lives in a second-floor apartment.
Teeth in good repair.
Prefers to be addressed by first name.
Current serum creatinine 1.1 mg/dL.
Records from 2005 list serum creatinine at 1.3 mg/dL.
```

<a id="k096"></a>
## k096 (NCT01545349)

Exclusion criterion: Creatinine > 1.8 mg/dL

Program: met iff the patient's current serum creatinine > 1.8 mg/dL

### near-miss kind: boundary

**base** (does not meet)
```
Man of 75 years.
Screening visit for a clinical trial.
Current serum creatinine 1.4 mg/dL.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
```

**flip** (meets)
```
Man of 75 years.
Screening visit for a clinical trial.
Current serum creatinine 2.0 mg/dL.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
```

**near** (does not meet)
```
Man of 75 years.
Screening visit for a clinical trial.
Current serum creatinine 1.8 mg/dL.
Uses sunscreen in summer.
Plays the piano.
Enjoys board games.
```

**pres** (does not meet)
```
Male patient of 75 years.
Screening visit for a clinical trial.
Plays the piano.
Uses sunscreen in summer.
Enjoys board games.
Latest creatinine result: 1.4 mg/dL.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 76 years.
Screening visit for a clinical trial.
Teeth in good repair.
Has two cats.
Latest creatinine result: 0.5 mg/dL.
```

**flip** (meets)
```
Female patient of 76 years.
Screening visit for a clinical trial.
Teeth in good repair.
Has two cats.
Latest creatinine result: 2.2 mg/dL.
```

**near** (does not meet)
```
Female patient of 76 years.
Screening visit for a clinical trial.
Teeth in good repair.
Has two cats.
Latest creatinine result: 1.7 mg/dL.
```

**pres** (does not meet)
```
Woman of 76 years.
Screening visit for a clinical trial.
Has two cats.
Teeth in good repair.
Current serum creatinine 0.5 mg/dL.
```

<a id="k098"></a>
## k098 (NCT01964053)

Exclusion criterion: Have renal failure (serum creatinine greater than 2.0mg/dl)

Program: met iff the patient's current serum creatinine > 2 mg/dL

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 71 years.
Screening visit for a clinical trial.
Latest creatinine result: 0.9 mg/dL.
Teeth in good repair.
Knits as a hobby.
```

**flip** (meets)
```
Female patient of 71 years.
Screening visit for a clinical trial.
Latest creatinine result: 2.4 mg/dL.
Teeth in good repair.
Knits as a hobby.
```

**near** (does not meet)
```
Female patient of 71 years.
Screening visit for a clinical trial.
Latest creatinine result: 2.0 mg/dL.
Teeth in good repair.
Knits as a hobby.
```

**pres** (does not meet)
```
Woman of 71 years.
Screening visit for a clinical trial.
Knits as a hobby.
Current serum creatinine 0.9 mg/dL.
Teeth in good repair.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 69 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Latest creatinine result: 0.9 mg/dL.
```

**flip** (meets)
```
Man of 69 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Latest creatinine result: 2.3 mg/dL.
```

**near** (does not meet)
```
Man of 69 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Has two cats.
Pupils equal and reactive to light.
Latest creatinine result: 1.9 mg/dL.
```

**pres** (does not meet)
```
Male patient of 69 years.
Screening visit for a clinical trial.
Current serum creatinine 0.9 mg/dL.
Pupils equal and reactive to light.
Has two cats.
Prefers to be addressed by first name.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Records from 2007 list serum creatinine at 1.2 mg/dL.
Owns a bicycle.
Teeth in good repair.
Latest creatinine result: 1.7 mg/dL.
```

**flip** (meets)
```
Woman of 48 years.
Screening visit for a clinical trial.
Records from 2007 list serum creatinine at 1.2 mg/dL.
Owns a bicycle.
Teeth in good repair.
Latest creatinine result: 2.6 mg/dL.
```

**near** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Records from 2007 list serum creatinine at 2.5 mg/dL.
Owns a bicycle.
Teeth in good repair.
Latest creatinine result: 1.7 mg/dL.
```

**pres** (does not meet)
```
Female patient of 48 years.
Screening visit for a clinical trial.
Back in 2007, serum creatinine stood at 1.2 mg/dL.
Teeth in good repair.
Current serum creatinine 1.7 mg/dL.
Owns a bicycle.
```

<a id="k099"></a>
## k099 (NCT00174967)

Inclusion criterion: Must have adequate renal function (serum creatinine <1.5 mg/dL).

Program: met iff the patient's current serum creatinine < 1.5 mg/dL

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 37 years.
Screening visit for a clinical trial.
Plays the piano.
Current serum creatinine 2.4 mg/dL.
```

**flip** (meets)
```
Male patient of 37 years.
Screening visit for a clinical trial.
Plays the piano.
Current serum creatinine 1.0 mg/dL.
```

**near** (does not meet)
```
Male patient of 37 years.
Screening visit for a clinical trial.
Plays the piano.
Current serum creatinine 1.5 mg/dL.
```

**pres** (does not meet)
```
Man of 37 years.
Screening visit for a clinical trial.
Latest creatinine result: 2.4 mg/dL.
Plays the piano.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 45 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Uses sunscreen in summer.
Latest creatinine result: 2.8 mg/dL.
Drives a car.
```

**flip** (meets)
```
Woman of 45 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Uses sunscreen in summer.
Latest creatinine result: 1.0 mg/dL.
Drives a car.
```

**near** (does not meet)
```
Woman of 45 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Uses sunscreen in summer.
Latest creatinine result: 1.6 mg/dL.
Drives a car.
```

**pres** (does not meet)
```
Female patient of 45 years.
Screening visit for a clinical trial.
Current serum creatinine 2.8 mg/dL.
Drives a car.
Uses sunscreen in summer.
Sleeps seven hours a night.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 66 years.
Screening visit for a clinical trial.
Current serum creatinine 2.0 mg/dL.
Records from 2005 list serum creatinine at 2.7 mg/dL.
Plays the piano.
Has two cats.
```

**flip** (meets)
```
Female patient of 66 years.
Screening visit for a clinical trial.
Current serum creatinine 1.4 mg/dL.
Records from 2005 list serum creatinine at 2.7 mg/dL.
Plays the piano.
Has two cats.
```

**near** (does not meet)
```
Female patient of 66 years.
Screening visit for a clinical trial.
Current serum creatinine 2.0 mg/dL.
Records from 2005 list serum creatinine at 1.3 mg/dL.
Plays the piano.
Has two cats.
```

**pres** (does not meet)
```
Woman of 66 years.
Screening visit for a clinical trial.
Plays the piano.
Latest creatinine result: 2.0 mg/dL.
Has two cats.
Back in 2005, serum creatinine stood at 2.7 mg/dL.
```

<a id="k103"></a>
## k103 (NCT02582177)

Exclusion criterion: Participants diagnosed with Diabetes Mellitus

Program: met iff the patient has diabetes now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Plays the piano.
Paints watercolors as a hobby.
Uses sunscreen in summer.
HbA1c 5.3% at a routine check.
```

**flip** (meets)
```
Woman of 37 years.
Screening visit for a clinical trial.
Plays the piano.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Insulin-treated diabetes.
```

**near** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Plays the piano.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Never diagnosed with diabetes.
```

**pres** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
HbA1c 5.3% at a routine check.
Paints watercolors as a hobby.
Uses sunscreen in summer.
Plays the piano.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Random glucose 92 mg/dL.
Drives a car.
```

**flip** (meets)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Has type 2 diabetes on metformin.
Drives a car.
```

**near** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
His father is diabetic.
Drives a car.
```

**pres** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Drives a car.
Random glucose 92 mg/dL.
```

<a id="k106"></a>
## k106 (NCT04433338)

Exclusion criterion: Diabetes Mellitus

Program: met iff the patient has diabetes now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Woman of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Prefers to be addressed by first name.
Drives a car.
Sleeps seven hours a night.
HbA1c 5.3% at a routine check.
```

**flip** (meets)
```
Woman of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Prefers to be addressed by first name.
Drives a car.
Sleeps seven hours a night.
Has type 2 diabetes on metformin.
```

**near** (does not meet)
```
Woman of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Prefers to be addressed by first name.
Drives a car.
Sleeps seven hours a night.
Has never had diabetes.
```

**pres** (does not meet)
```
Female patient of 52 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
HbA1c 5.3% at a routine check.
Enjoys board games.
Drives a car.
Prefers to be addressed by first name.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Random glucose 92 mg/dL.
```

**flip** (meets)
```
Man of 50 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Insulin-treated diabetes.
```

**near** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
His father lives with type 1 diabetes.
```

**pres** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Random glucose 92 mg/dL.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

<a id="k113"></a>
## k113 (NCT03372200)

Exclusion criterion: eGFR: < 30 mL/min/1.73 m2

Program: met iff the patient's current eGFR < 30 mL/min/1.73 m2

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 63 years.
Screening visit for a clinical trial.
Current eGFR 45 mL/min/1.73 m2.
Drives a car.
Teeth in good repair.
```

**flip** (meets)
```
Female patient of 63 years.
Screening visit for a clinical trial.
Current eGFR 20 mL/min/1.73 m2.
Drives a car.
Teeth in good repair.
```

**near** (does not meet)
```
Female patient of 63 years.
Screening visit for a clinical trial.
Current eGFR 30 mL/min/1.73 m2.
Drives a car.
Teeth in good repair.
```

**pres** (does not meet)
```
Woman of 63 years.
Screening visit for a clinical trial.
eGFR now 45 mL/min/1.73 m2.
Teeth in good repair.
Drives a car.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 45 years.
Screening visit for a clinical trial.
Current eGFR 70 mL/min/1.73 m2.
Prefers morning appointments.
```

**flip** (meets)
```
Male patient of 45 years.
Screening visit for a clinical trial.
Current eGFR 24 mL/min/1.73 m2.
Prefers morning appointments.
```

**near** (does not meet)
```
Male patient of 45 years.
Screening visit for a clinical trial.
Current eGFR 33 mL/min/1.73 m2.
Prefers morning appointments.
```

**pres** (does not meet)
```
Man of 45 years.
Screening visit for a clinical trial.
Prefers morning appointments.
eGFR now 70 mL/min/1.73 m2.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 82 years.
Screening visit for a clinical trial.
Has two cats.
Current eGFR 57 mL/min/1.73 m2.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Back in 2005, eGFR stood at 58 mL/min/1.73 m2.
```

**flip** (meets)
```
Woman of 82 years.
Screening visit for a clinical trial.
Has two cats.
Current eGFR 28 mL/min/1.73 m2.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Back in 2005, eGFR stood at 58 mL/min/1.73 m2.
```

**near** (does not meet)
```
Woman of 82 years.
Screening visit for a clinical trial.
Has two cats.
Current eGFR 57 mL/min/1.73 m2.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Back in 2005, eGFR stood at 16 mL/min/1.73 m2.
```

**pres** (does not meet)
```
Female patient of 82 years.
Screening visit for a clinical trial.
Has two cats.
Records from 2005 list eGFR at 58 mL/min/1.73 m2.
Paints watercolors as a hobby.
eGFR now 57 mL/min/1.73 m2.
Prefers to be addressed by first name.
```

<a id="k117"></a>
## k117 (NCT02653209)

Exclusion criterion: eGFR <60mls/min/1.73m²

Program: met iff the patient's current eGFR < 60 mL/min/1.73 m2

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 38 years.
Screening visit for a clinical trial.
Plays the piano.
Sees a dentist yearly.
Current eGFR 64 mL/min/1.73 m2.
```

**flip** (meets)
```
Woman of 38 years.
Screening visit for a clinical trial.
Plays the piano.
Sees a dentist yearly.
Current eGFR 54 mL/min/1.73 m2.
```

**near** (does not meet)
```
Woman of 38 years.
Screening visit for a clinical trial.
Plays the piano.
Sees a dentist yearly.
Current eGFR 60 mL/min/1.73 m2.
```

**pres** (does not meet)
```
Female patient of 38 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
eGFR now 64 mL/min/1.73 m2.
Plays the piano.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Owns a bicycle.
Lives in a second-floor apartment.
Has two cats.
eGFR now 98 mL/min/1.73 m2.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Man of 40 years.
Screening visit for a clinical trial.
Owns a bicycle.
Lives in a second-floor apartment.
Has two cats.
eGFR now 58 mL/min/1.73 m2.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Owns a bicycle.
Lives in a second-floor apartment.
Has two cats.
eGFR now 61 mL/min/1.73 m2.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Male patient of 40 years.
Screening visit for a clinical trial.
Owns a bicycle.
Lives in a second-floor apartment.
Has two cats.
Paints watercolors as a hobby.
Current eGFR 98 mL/min/1.73 m2.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 63 years.
Screening visit for a clinical trial.
Current eGFR 79 mL/min/1.73 m2.
Photographs local wildlife.
Records from 2009 list eGFR at 82 mL/min/1.73 m2.
```

**flip** (meets)
```
Man of 63 years.
Screening visit for a clinical trial.
Current eGFR 54 mL/min/1.73 m2.
Photographs local wildlife.
Records from 2009 list eGFR at 82 mL/min/1.73 m2.
```

**near** (does not meet)
```
Man of 63 years.
Screening visit for a clinical trial.
Current eGFR 79 mL/min/1.73 m2.
Photographs local wildlife.
Records from 2009 list eGFR at 52 mL/min/1.73 m2.
```

**pres** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Back in 2009, eGFR stood at 82 mL/min/1.73 m2.
eGFR now 79 mL/min/1.73 m2.
Photographs local wildlife.
```

<a id="k123"></a>
## k123 (NCT03637400)

Exclusion criterion: Heart rate less than 45 beats per minute (BPM)

Program: met iff the patient's current heart rate < 45 /min

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 49 years.
Screening visit for a clinical trial.
Current heart rate 83/min.
Drives a car.
```

**flip** (meets)
```
Female patient of 49 years.
Screening visit for a clinical trial.
Current heart rate 40/min.
Drives a car.
```

**near** (does not meet)
```
Female patient of 49 years.
Screening visit for a clinical trial.
Current heart rate 45/min.
Drives a car.
```

**pres** (does not meet)
```
Woman of 49 years.
Screening visit for a clinical trial.
Drives a car.
Heart rate now 83/min on a pulse check.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 72 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Heart rate now 55/min on a pulse check.
Uses sunscreen in summer.
Plays the piano.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 72 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Heart rate now 43/min on a pulse check.
Uses sunscreen in summer.
Plays the piano.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 72 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Heart rate now 49/min on a pulse check.
Uses sunscreen in summer.
Plays the piano.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 72 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Knits as a hobby.
Current heart rate 55/min.
Plays the piano.
Pupils equal and reactive to light.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Back in 2021, heart rate stood at 77/min.
Paints watercolors as a hobby.
Heart rate now 50/min on a pulse check.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 48 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Back in 2021, heart rate stood at 77/min.
Paints watercolors as a hobby.
Heart rate now 41/min on a pulse check.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Back in 2021, heart rate stood at 42/min.
Paints watercolors as a hobby.
Heart rate now 50/min on a pulse check.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 48 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Current heart rate 50/min.
Photographs local wildlife.
Records from 2021 list heart rate at 77/min.
Knits as a hobby.
```

<a id="k125"></a>
## k125 (NCT06472921)

Exclusion criterion: Presence of bradycardia (heart rate below 60 beats per minute) or sick sinus syndrome

Program: met iff the patient's current heart rate < 60 /min

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 58 years.
Screening visit for a clinical trial.
Owns a bicycle.
Heart rate now 63/min on a pulse check.
```

**flip** (meets)
```
Woman of 58 years.
Screening visit for a clinical trial.
Owns a bicycle.
Heart rate now 45/min on a pulse check.
```

**near** (does not meet)
```
Woman of 58 years.
Screening visit for a clinical trial.
Owns a bicycle.
Heart rate now 60/min on a pulse check.
```

**pres** (does not meet)
```
Female patient of 58 years.
Screening visit for a clinical trial.
Current heart rate 63/min.
Owns a bicycle.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 36 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current heart rate 95/min.
```

**flip** (meets)
```
Man of 36 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current heart rate 47/min.
```

**near** (does not meet)
```
Man of 36 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current heart rate 63/min.
```

**pres** (does not meet)
```
Male patient of 36 years.
Screening visit for a clinical trial.
Heart rate now 95/min on a pulse check.
Sees a dentist yearly.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Current heart rate 81/min.
Sees a dentist yearly.
Back in 2009, heart rate stood at 91/min.
Photographs local wildlife.
```

**flip** (meets)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Current heart rate 53/min.
Sees a dentist yearly.
Back in 2009, heart rate stood at 91/min.
Photographs local wildlife.
```

**near** (does not meet)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Current heart rate 81/min.
Sees a dentist yearly.
Back in 2009, heart rate stood at 59/min.
Photographs local wildlife.
```

**pres** (does not meet)
```
Man of 71 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Records from 2009 list heart rate at 91/min.
Photographs local wildlife.
Sees a dentist yearly.
Heart rate now 81/min on a pulse check.
```

<a id="k127"></a>
## k127 (NCT05285878)

Exclusion criterion: Heart rate <60 beats per minute

Program: met iff the patient's current heart rate < 60 /min

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 43 years.
Screening visit for a clinical trial.
Enjoys board games.
Current heart rate 83/min.
Lives in a second-floor apartment.
Plays the piano.
```

**flip** (meets)
```
Woman of 43 years.
Screening visit for a clinical trial.
Enjoys board games.
Current heart rate 52/min.
Lives in a second-floor apartment.
Plays the piano.
```

**near** (does not meet)
```
Woman of 43 years.
Screening visit for a clinical trial.
Enjoys board games.
Current heart rate 60/min.
Lives in a second-floor apartment.
Plays the piano.
```

**pres** (does not meet)
```
Female patient of 43 years.
Screening visit for a clinical trial.
Enjoys board games.
Plays the piano.
Lives in a second-floor apartment.
Heart rate now 83/min on a pulse check.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Pupils equal and reactive to light.
Current heart rate 88/min.
Has two cats.
```

**flip** (meets)
```
Female patient of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Pupils equal and reactive to light.
Current heart rate 57/min.
Has two cats.
```

**near** (does not meet)
```
Female patient of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Pupils equal and reactive to light.
Current heart rate 63/min.
Has two cats.
```

**pres** (does not meet)
```
Woman of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Has two cats.
Heart rate now 88/min on a pulse check.
Pupils equal and reactive to light.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 47 years.
Screening visit for a clinical trial.
Records from 2015 list heart rate at 97/min.
Current heart rate 74/min.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Woman of 47 years.
Screening visit for a clinical trial.
Records from 2015 list heart rate at 97/min.
Current heart rate 52/min.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Woman of 47 years.
Screening visit for a clinical trial.
Records from 2015 list heart rate at 54/min.
Current heart rate 74/min.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Female patient of 47 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Heart rate now 74/min on a pulse check.
Back in 2015, heart rate stood at 97/min.
```

<a id="k129"></a>
## k129 (NCT01485315)

Inclusion criterion: Have haemoglobin of 9.0 g/dl or less

Program: met iff the patient's current hemoglobin <= 9 g/dL

### near-miss kind: numeric

**base** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Has two cats.
Current Hgb 9.7 g/dL.
Drives a car.
```

**flip** (meets)
```
Man of 30 years.
Screening visit for a clinical trial.
Has two cats.
Current Hgb 9.0 g/dL.
Drives a car.
```

**near** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Has two cats.
Current Hgb 9.4 g/dL.
Drives a car.
```

**pres** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Latest Hgb result: 9.7 g/dL.
Drives a car.
Has two cats.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Current Hgb 10.6 g/dL.
Back in 2006, Hgb stood at 12.7 g/dL.
```

**flip** (meets)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Current Hgb 9.0 g/dL.
Back in 2006, Hgb stood at 12.7 g/dL.
```

**near** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Current Hgb 10.6 g/dL.
Back in 2006, Hgb stood at 8.3 g/dL.
```

**pres** (does not meet)
```
Man of 76 years.
Screening visit for a clinical trial.
Records from 2006 list Hgb at 12.7 g/dL.
Latest Hgb result: 10.6 g/dL.
Sleeps seven hours a night.
```

<a id="k130"></a>
## k130 (NCT04933942)

Inclusion criterion: Hemoglobin ≥ 8 g/dl

Program: met iff the patient's current hemoglobin >= 8 g/dL

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 64 years.
Screening visit for a clinical trial.
Knits as a hobby.
Teeth in good repair.
Prefers to be addressed by first name.
Latest Hgb result: 7.5 g/dL.
Owns a bicycle.
```

**flip** (meets)
```
Female patient of 64 years.
Screening visit for a clinical trial.
Knits as a hobby.
Teeth in good repair.
Prefers to be addressed by first name.
Latest Hgb result: 8.7 g/dL.
Owns a bicycle.
```

**near** (does not meet)
```
Female patient of 64 years.
Screening visit for a clinical trial.
Knits as a hobby.
Teeth in good repair.
Prefers to be addressed by first name.
Latest Hgb result: 7.8 g/dL.
Owns a bicycle.
```

**pres** (does not meet)
```
Woman of 64 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Teeth in good repair.
Current Hgb 7.5 g/dL.
Knits as a hobby.
Owns a bicycle.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 46 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Latest Hgb result: 7.3 g/dL.
Records from 2017 list Hgb at 6.9 g/dL.
```

**flip** (meets)
```
Female patient of 46 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Latest Hgb result: 8.9 g/dL.
Records from 2017 list Hgb at 6.9 g/dL.
```

**near** (does not meet)
```
Female patient of 46 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Latest Hgb result: 7.3 g/dL.
Records from 2017 list Hgb at 8.5 g/dL.
```

**pres** (does not meet)
```
Woman of 46 years.
Screening visit for a clinical trial.
Back in 2017, Hgb stood at 6.9 g/dL.
Paints watercolors as a hobby.
Current Hgb 7.3 g/dL.
```

<a id="k132"></a>
## k132 (NCT03692065)

Exclusion criterion: Hemoglobin < 8g /dl

Program: met iff the patient's current hemoglobin < 8 g/dL

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 84 years.
Screening visit for a clinical trial.
Latest Hgb result: 9.8 g/dL.
Sees a dentist yearly.
Teeth in good repair.
Pupils equal and reactive to light.
Uses sunscreen in summer.
```

**flip** (meets)
```
Woman of 84 years.
Screening visit for a clinical trial.
Latest Hgb result: 7.5 g/dL.
Sees a dentist yearly.
Teeth in good repair.
Pupils equal and reactive to light.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Woman of 84 years.
Screening visit for a clinical trial.
Latest Hgb result: 8.0 g/dL.
Sees a dentist yearly.
Teeth in good repair.
Pupils equal and reactive to light.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Female patient of 84 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Uses sunscreen in summer.
Teeth in good repair.
Current Hgb 9.8 g/dL.
Pupils equal and reactive to light.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 43 years.
Screening visit for a clinical trial.
Current Hgb 9.2 g/dL.
Uses sunscreen in summer.
Sleeps seven hours a night.
```

**flip** (meets)
```
Man of 43 years.
Screening visit for a clinical trial.
Current Hgb 7.6 g/dL.
Uses sunscreen in summer.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Man of 43 years.
Screening visit for a clinical trial.
Current Hgb 8.1 g/dL.
Uses sunscreen in summer.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Male patient of 43 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest Hgb result: 9.2 g/dL.
Uses sunscreen in summer.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Current Hgb 11.4 g/dL.
Owns a bicycle.
Back in 2015, Hgb stood at 11.3 g/dL.
```

**flip** (meets)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Current Hgb 6.9 g/dL.
Owns a bicycle.
Back in 2015, Hgb stood at 11.3 g/dL.
```

**near** (does not meet)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Current Hgb 11.4 g/dL.
Owns a bicycle.
Back in 2015, Hgb stood at 7.5 g/dL.
```

**pres** (does not meet)
```
Man of 53 years.
Screening visit for a clinical trial.
Owns a bicycle.
Records from 2015 list Hgb at 11.3 g/dL.
Latest Hgb result: 11.4 g/dL.
```

<a id="k134"></a>
## k134 (NCT05535920)

Exclusion criterion: Patients with a Haemoglobin < 9 g/dl.

Program: met iff the patient's current hemoglobin < 9 g/dL

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Latest Hgb result: 10.4 g/dL.
Drives a car.
```

**flip** (meets)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Latest Hgb result: 8.7 g/dL.
Drives a car.
```

**near** (does not meet)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Latest Hgb result: 9.0 g/dL.
Drives a car.
```

**pres** (does not meet)
```
Man of 66 years.
Screening visit for a clinical trial.
Drives a car.
Current Hgb 10.4 g/dL.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 61 years.
Screening visit for a clinical trial.
Owns a bicycle.
Current Hgb 12.2 g/dL.
Uses sunscreen in summer.
```

**flip** (meets)
```
Woman of 61 years.
Screening visit for a clinical trial.
Owns a bicycle.
Current Hgb 7.8 g/dL.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Woman of 61 years.
Screening visit for a clinical trial.
Owns a bicycle.
Current Hgb 9.4 g/dL.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Female patient of 61 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Owns a bicycle.
Latest Hgb result: 12.2 g/dL.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Latest Hgb result: 11.9 g/dL.
Teeth in good repair.
Back in 2022, Hgb stood at 10.6 g/dL.
```

**flip** (meets)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Latest Hgb result: 8.7 g/dL.
Teeth in good repair.
Back in 2022, Hgb stood at 10.6 g/dL.
```

**near** (does not meet)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Latest Hgb result: 11.9 g/dL.
Teeth in good repair.
Back in 2022, Hgb stood at 7.6 g/dL.
```

**pres** (does not meet)
```
Man of 58 years.
Screening visit for a clinical trial.
Records from 2022 list Hgb at 10.6 g/dL.
Teeth in good repair.
Current Hgb 11.9 g/dL.
```

<a id="k135"></a>
## k135 (NCT01114204)

Exclusion criterion: Hemoglobin ≤7.0 g/dL

Program: met iff the patient's current hemoglobin <= 7 g/dL

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 55 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Current Hgb 10.0 g/dL.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 55 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Current Hgb 7.0 g/dL.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 55 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Current Hgb 7.3 g/dL.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 55 years.
Screening visit for a clinical trial.
Latest Hgb result: 10.0 g/dL.
Knits as a hobby.
Photographs local wildlife.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Latest Hgb result: 9.0 g/dL.
Plays the piano.
Uses sunscreen in summer.
Records from 2016 list Hgb at 10.8 g/dL.
```

**flip** (meets)
```
Man of 67 years.
Screening visit for a clinical trial.
Latest Hgb result: 7.0 g/dL.
Plays the piano.
Uses sunscreen in summer.
Records from 2016 list Hgb at 10.8 g/dL.
```

**near** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Latest Hgb result: 9.0 g/dL.
Plays the piano.
Uses sunscreen in summer.
Records from 2016 list Hgb at 6.3 g/dL.
```

**pres** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Current Hgb 9.0 g/dL.
Plays the piano.
Back in 2016, Hgb stood at 10.8 g/dL.
Uses sunscreen in summer.
```

<a id="k136"></a>
## k136 (NCT04345848)

Exclusion criterion: personal history of heparin-induced thrombocytopenia

Program: met iff the patient has heparin-induced thrombocytopenia at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 38 years.
Screening visit for a clinical trial.
Heparin exposure within the past 100 days: none.
Prefers morning appointments.
Plays the piano.
Sleeps seven hours a night.
```

**flip** (meets)
```
Male patient of 38 years.
Screening visit for a clinical trial.
Heparin-induced thrombocytopenia, with heparin antibodies still positive.
Prefers morning appointments.
Plays the piano.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Male patient of 38 years.
Screening visit for a clinical trial.
Has never had heparin-induced thrombocytopenia.
Prefers morning appointments.
Plays the piano.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Man of 38 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Plays the piano.
Heparin exposure within the past 100 days: none.
Sleeps seven hours a night.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 47 years.
Screening visit for a clinical trial.
Has two cats.
Knits as a hobby.
Uses sunscreen in summer.
Heparin exposure within the past 100 days: none.
```

**flip** (meets)
```
Woman of 47 years.
Screening visit for a clinical trial.
Has two cats.
Knits as a hobby.
Uses sunscreen in summer.
Being treated for heparin-induced thrombocytopenia by the hematology team.
```

**near** (does not meet)
```
Woman of 47 years.
Screening visit for a clinical trial.
Has two cats.
Knits as a hobby.
Uses sunscreen in summer.
Her friend has developed heparin-induced thrombocytopenia after surgery.
```

**pres** (does not meet)
```
Female patient of 47 years.
Screening visit for a clinical trial.
Has two cats.
Heparin exposure within the past 100 days: none.
Knits as a hobby.
Uses sunscreen in summer.
```

<a id="k137"></a>
## k137 (NCT00786474)

Exclusion criterion: Allergy to heparin or history of heparin-induced thrombocytopenia

Program: met iff the patient has heparin-induced thrombocytopenia at any time (current or past); also listed in the text but never mentioned in cases: allergy to heparin

### near-miss kind: negation

**base** (does not meet)
```
Woman of 84 years.
Screening visit for a clinical trial.
Last received heparin more than a year ago.
Owns a bicycle.
```

**flip** (meets)
```
Woman of 84 years.
Screening visit for a clinical trial.
Being treated for heparin-induced thrombocytopenia by the hematology team.
Owns a bicycle.
```

**near** (does not meet)
```
Woman of 84 years.
Screening visit for a clinical trial.
Has never had heparin-induced thrombocytopenia.
Owns a bicycle.
```

**pres** (does not meet)
```
Female patient of 84 years.
Screening visit for a clinical trial.
Owns a bicycle.
Last received heparin more than a year ago.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Last received heparin more than a year ago.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Being treated for heparin-induced thrombocytopenia by the hematology team.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
His sister has developed heparin-induced thrombocytopenia after surgery.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Last received heparin more than a year ago.
```

<a id="k138"></a>
## k138 (NCT00061373)

Exclusion criterion: History of heparin induced thrombocytopenia.

Program: met iff the patient has heparin-induced thrombocytopenia at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 57 years.
Screening visit for a clinical trial.
Last received heparin more than a year ago.
Drives a car.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Male patient of 57 years.
Screening visit for a clinical trial.
Being treated for heparin-induced thrombocytopenia by the hematology team.
Drives a car.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Male patient of 57 years.
Screening visit for a clinical trial.
Never diagnosed with heparin-induced thrombocytopenia.
Drives a car.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Man of 57 years.
Screening visit for a clinical trial.
Drives a car.
Last received heparin more than a year ago.
Paints watercolors as a hobby.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Owns a bicycle.
Knits as a hobby.
```

**flip** (meets)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Owns a bicycle.
Knits as a hobby.
Formerly had heparin-induced thrombocytopenia during a hospital stay in 2020; blood counts recovered afterward.
```

**near** (does not meet)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Owns a bicycle.
Knits as a hobby.
Her roommate developed heparin-induced thrombocytopenia years ago.
```

**pres** (does not meet)
```
Woman of 34 years.
Screening visit for a clinical trial.
Knits as a hobby.
Owns a bicycle.
```

<a id="k139"></a>
## k139 (NCT04066764)

Exclusion criterion: With previous heparin-induced thrombocytopenia

Program: met iff the patient has heparin-induced thrombocytopenia at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 47 years.
Screening visit for a clinical trial.
Enjoys board games.
Heparin exposure within the past 100 days: none.
Drives a car.
```

**flip** (meets)
```
Female patient of 47 years.
Screening visit for a clinical trial.
Enjoys board games.
Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully.
Drives a car.
```

**near** (does not meet)
```
Female patient of 47 years.
Screening visit for a clinical trial.
Enjoys board games.
Has never had heparin-induced thrombocytopenia.
Drives a car.
```

**pres** (does not meet)
```
Woman of 47 years.
Screening visit for a clinical trial.
Heparin exposure within the past 100 days: none.
Enjoys board games.
Drives a car.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Plays the piano.
Uses sunscreen in summer.
```

**flip** (meets)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully.
Plays the piano.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Her roommate developed heparin-induced thrombocytopenia years ago.
Plays the piano.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Woman of 70 years.
Screening visit for a clinical trial.
Owns a bicycle.
Plays the piano.
Lives in a second-floor apartment.
Uses sunscreen in summer.
```

<a id="k140"></a>
## k140 (NCT04317703)

Exclusion criterion: History of sensitivity to heparin or heparin-induced thrombocytopenia

Program: met iff the patient has heparin-induced thrombocytopenia at any time (current or past); also listed in the text but never mentioned in cases: history of sensitivity to heparin

### near-miss kind: negation

**base** (does not meet)
```
Man of 38 years.
Screening visit for a clinical trial.
Teeth in good repair.
Plays the piano.
Pupils equal and reactive to light.
Prefers morning appointments.
```

**flip** (meets)
```
Man of 38 years.
Screening visit for a clinical trial.
Teeth in good repair.
Plays the piano.
Pupils equal and reactive to light.
Prefers morning appointments.
Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully.
```

**near** (does not meet)
```
Man of 38 years.
Screening visit for a clinical trial.
Teeth in good repair.
Plays the piano.
Pupils equal and reactive to light.
Prefers morning appointments.
Never diagnosed with heparin-induced thrombocytopenia.
```

**pres** (does not meet)
```
Male patient of 38 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Plays the piano.
Prefers morning appointments.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Drives a car.
Teeth in good repair.
Plays the piano.
Heparin exposure within the past 100 days: none.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Drives a car.
Teeth in good repair.
Plays the piano.
Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Drives a car.
Teeth in good repair.
Plays the piano.
Her uncle developed heparin-induced thrombocytopenia years ago.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Woman of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Pupils equal and reactive to light.
Plays the piano.
Heparin exposure within the past 100 days: none.
Drives a car.
```

<a id="k141"></a>
## k141 (NCT01181544)

Exclusion criterion: Diagnosis of Heparin-Induced Thrombocytopenia (HIT)

Program: met iff the patient has heparin-induced thrombocytopenia now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Man of 55 years.
Screening visit for a clinical trial.
Teeth in good repair.
Sees a dentist yearly.
```

**flip** (meets)
```
Man of 55 years.
Screening visit for a clinical trial.
Teeth in good repair.
Sees a dentist yearly.
Being treated for heparin-induced thrombocytopenia by the hematology team.
```

**near** (does not meet)
```
Man of 55 years.
Screening visit for a clinical trial.
Teeth in good repair.
Sees a dentist yearly.
Has never had heparin-induced thrombocytopenia.
```

**pres** (does not meet)
```
Male patient of 55 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Teeth in good repair.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Last received heparin more than a year ago.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Heparin-induced thrombocytopenia, with heparin antibodies still positive.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Her sister has developed heparin-induced thrombocytopenia after surgery.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Woman of 75 years.
Screening visit for a clinical trial.
Last received heparin more than a year ago.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
```

<a id="k152"></a>
## k152 (NCT03291249)

Exclusion criterion: International Normalized Ratio (INR) >1.5

Program: met iff the patient's current INR > 1.5

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 77 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 0.8.
Teeth in good repair.
Prefers to be addressed by first name.
```

**flip** (meets)
```
Female patient of 77 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 1.8.
Teeth in good repair.
Prefers to be addressed by first name.
```

**near** (does not meet)
```
Female patient of 77 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 1.5.
Teeth in good repair.
Prefers to be addressed by first name.
```

**pres** (does not meet)
```
Woman of 77 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current international normalized ratio 0.8.
Prefers to be addressed by first name.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Knits as a hobby.
Current international normalized ratio 0.9.
Enjoys board games.
Teeth in good repair.
```

**flip** (meets)
```
Woman of 37 years.
Screening visit for a clinical trial.
Knits as a hobby.
Current international normalized ratio 1.9.
Enjoys board games.
Teeth in good repair.
```

**near** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Knits as a hobby.
Current international normalized ratio 1.4.
Enjoys board games.
Teeth in good repair.
```

**pres** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Knits as a hobby.
Teeth in good repair.
Latest international normalized ratio (INR): 0.9.
Enjoys board games.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Enjoys board games.
Prefers morning appointments.
Teeth in good repair.
Back in 2015, international normalized ratio stood at 0.9.
Current international normalized ratio 1.1.
```

**flip** (meets)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Enjoys board games.
Prefers morning appointments.
Teeth in good repair.
Back in 2015, international normalized ratio stood at 0.9.
Current international normalized ratio 2.0.
```

**near** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Enjoys board games.
Prefers morning appointments.
Teeth in good repair.
Back in 2015, international normalized ratio stood at 1.8.
Current international normalized ratio 1.1.
```

**pres** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Records from 2015 list international normalized ratio at 0.9.
Enjoys board games.
Prefers morning appointments.
Teeth in good repair.
Latest international normalized ratio (INR): 1.1.
```

<a id="k154"></a>
## k154 (NCT02586233)

Exclusion criterion: Has International Normalized Ratio greater than 1.7

Program: met iff the patient's current INR > 1.7

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Current international normalized ratio 1.2.
```

**flip** (meets)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Current international normalized ratio 2.2.
```

**near** (does not meet)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Current international normalized ratio 1.7.
```

**pres** (does not meet)
```
Woman of 34 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 1.2.
Uses sunscreen in summer.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Drives a car.
Owns a bicycle.
Current international normalized ratio 1.4.
```

**flip** (meets)
```
Woman of 36 years.
Screening visit for a clinical trial.
Drives a car.
Owns a bicycle.
Current international normalized ratio 2.2.
```

**near** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Drives a car.
Owns a bicycle.
Current international normalized ratio 1.6.
```

**pres** (does not meet)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Owns a bicycle.
Latest international normalized ratio (INR): 1.4.
Drives a car.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 78 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Latest international normalized ratio (INR): 1.1.
Records from 2014 list international normalized ratio at 0.9.
```

**flip** (meets)
```
Female patient of 78 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Latest international normalized ratio (INR): 2.0.
Records from 2014 list international normalized ratio at 0.9.
```

**near** (does not meet)
```
Female patient of 78 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Latest international normalized ratio (INR): 1.1.
Records from 2014 list international normalized ratio at 2.2.
```

**pres** (does not meet)
```
Woman of 78 years.
Screening visit for a clinical trial.
Back in 2014, international normalized ratio stood at 0.9.
Current international normalized ratio 1.1.
Prefers to be addressed by first name.
```

<a id="k155"></a>
## k155 (NCT05907564)

Exclusion criterion: International normalized ratio (INR) > 3

Program: met iff the patient's current INR > 3

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 35 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Photographs local wildlife.
Uses sunscreen in summer.
Current international normalized ratio 1.5.
```

**flip** (meets)
```
Male patient of 35 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Photographs local wildlife.
Uses sunscreen in summer.
Current international normalized ratio 3.5.
```

**near** (does not meet)
```
Male patient of 35 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Photographs local wildlife.
Uses sunscreen in summer.
Current international normalized ratio 3.0.
```

**pres** (does not meet)
```
Man of 35 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Latest international normalized ratio (INR): 1.5.
Pupils equal and reactive to light.
Uses sunscreen in summer.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 70 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Latest international normalized ratio (INR): 2.5.
```

**flip** (meets)
```
Man of 70 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Latest international normalized ratio (INR): 3.2.
```

**near** (does not meet)
```
Man of 70 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Latest international normalized ratio (INR): 2.9.
```

**pres** (does not meet)
```
Male patient of 70 years.
Screening visit for a clinical trial.
Current international normalized ratio 2.5.
Owns a bicycle.
Lives in a second-floor apartment.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 53 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 1.7.
Enjoys board games.
Paints watercolors as a hobby.
Back in 2018, international normalized ratio stood at 2.6.
```

**flip** (meets)
```
Man of 53 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 3.1.
Enjoys board games.
Paints watercolors as a hobby.
Back in 2018, international normalized ratio stood at 2.6.
```

**near** (does not meet)
```
Man of 53 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 1.7.
Enjoys board games.
Paints watercolors as a hobby.
Back in 2018, international normalized ratio stood at 3.4.
```

**pres** (does not meet)
```
Male patient of 53 years.
Screening visit for a clinical trial.
Records from 2018 list international normalized ratio at 2.6.
Enjoys board games.
Current international normalized ratio 1.7.
Paints watercolors as a hobby.
```

<a id="k159"></a>
## k159 (NCT04645550)

Exclusion criterion: Base line INR >2

Program: met iff the patient's current INR > 2

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 43 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Current international normalized ratio 1.7.
Teeth in good repair.
```

**flip** (meets)
```
Female patient of 43 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Current international normalized ratio 2.5.
Teeth in good repair.
```

**near** (does not meet)
```
Female patient of 43 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Current international normalized ratio 2.0.
Teeth in good repair.
```

**pres** (does not meet)
```
Woman of 43 years.
Screening visit for a clinical trial.
Latest international normalized ratio (INR): 1.7.
Prefers to be addressed by first name.
Teeth in good repair.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 42 years.
Screening visit for a clinical trial.
Current international normalized ratio 1.2.
Prefers morning appointments.
```

**flip** (meets)
```
Female patient of 42 years.
Screening visit for a clinical trial.
Current international normalized ratio 2.4.
Prefers morning appointments.
```

**near** (does not meet)
```
Female patient of 42 years.
Screening visit for a clinical trial.
Current international normalized ratio 1.9.
Prefers morning appointments.
```

**pres** (does not meet)
```
Woman of 42 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Latest international normalized ratio (INR): 1.2.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 71 years.
Screening visit for a clinical trial.
Teeth in good repair.
Drives a car.
Back in 2015, international normalized ratio stood at 1.8.
Latest international normalized ratio (INR): 1.5.
Plays the piano.
Owns a bicycle.
```

**flip** (meets)
```
Man of 71 years.
Screening visit for a clinical trial.
Teeth in good repair.
Drives a car.
Back in 2015, international normalized ratio stood at 1.8.
Latest international normalized ratio (INR): 2.4.
Plays the piano.
Owns a bicycle.
```

**near** (does not meet)
```
Man of 71 years.
Screening visit for a clinical trial.
Teeth in good repair.
Drives a car.
Back in 2015, international normalized ratio stood at 2.4.
Latest international normalized ratio (INR): 1.5.
Plays the piano.
Owns a bicycle.
```

**pres** (does not meet)
```
Male patient of 71 years.
Screening visit for a clinical trial.
Plays the piano.
Drives a car.
Teeth in good repair.
Owns a bicycle.
Current international normalized ratio 1.5.
Records from 2015 list international normalized ratio at 1.8.
```

<a id="k161"></a>
## k161 (NCT00555217)

Exclusion criterion: Current use of Lithium

Program: met iff the patient has lithium treatment now (current)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 45 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Photographs local wildlife.
Uses no psychotropic drugs.
```

**flip** (meets)
```
Female patient of 45 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Photographs local wildlife.
Lithium for bipolar disorder, with stable levels.
```

**near** (does not meet)
```
Female patient of 45 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Photographs local wildlife.
Has never taken lithium.
```

**pres** (does not meet)
```
Woman of 45 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Lives in a second-floor apartment.
Uses no psychotropic drugs.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 80 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Plays the piano.
Has two cats.
```

**flip** (meets)
```
Man of 80 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Plays the piano.
Has two cats.
Lithium for bipolar disorder, with stable levels.
```

**near** (does not meet)
```
Man of 80 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Plays the piano.
Has two cats.
His friend uses lithium to prevent mood swings.
```

**pres** (does not meet)
```
Male patient of 80 years.
Screening visit for a clinical trial.
Plays the piano.
Pupils equal and reactive to light.
Has two cats.
Teeth in good repair.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Takes no medicines for mental health.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Lithium for bipolar disorder, with stable levels.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Female patient of 57 years.
Screening visit for a clinical trial.
Last took lithium in 2021; it was discontinued for good.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Woman of 57 years.
Screening visit for a clinical trial.
Takes no medicines for mental health.
Paints watercolors as a hobby.
Photographs local wildlife.
```

<a id="k163"></a>
## k163 (NCT02585713)

Exclusion criterion: Mechanical heart valve

Program: met iff the patient has a mechanical heart valve now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Woman of 67 years.
Screening visit for a clinical trial.
Teeth in good repair.
Drives a car.
Owns a bicycle.
```

**flip** (meets)
```
Woman of 67 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives with a mechanical aortic valve prosthesis.
Drives a car.
Owns a bicycle.
```

**near** (does not meet)
```
Woman of 67 years.
Screening visit for a clinical trial.
Teeth in good repair.
Never received a mechanical heart valve.
Drives a car.
Owns a bicycle.
```

**pres** (does not meet)
```
Female patient of 67 years.
Screening visit for a clinical trial.
Owns a bicycle.
Drives a car.
Teeth in good repair.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 41 years.
Screening visit for a clinical trial.
Drives a car.
Heart sounds free of clicks.
```

**flip** (meets)
```
Male patient of 41 years.
Screening visit for a clinical trial.
Drives a car.
Lives with a mechanical aortic valve prosthesis.
```

**near** (does not meet)
```
Male patient of 41 years.
Screening visit for a clinical trial.
Drives a car.
His father attends a valve clinic for a mechanical mitral valve.
```

**pres** (does not meet)
```
Man of 41 years.
Screening visit for a clinical trial.
Heart sounds free of clicks.
Drives a car.
```

<a id="k165"></a>
## k165 (NCT07084142)

Exclusion criterion: History of mechanical valve replacement

Program: met iff the patient has a mechanical heart valve at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Man of 66 years.
Screening visit for a clinical trial.
Teeth in good repair.
Photographs local wildlife.
Owns a bicycle.
Heart sounds free of clicks.
```

**flip** (meets)
```
Man of 66 years.
Screening visit for a clinical trial.
Teeth in good repair.
Photographs local wildlife.
Owns a bicycle.
Formerly had a mechanical mitral valve, exchanged for a bioprosthetic valve in 2008.
```

**near** (does not meet)
```
Man of 66 years.
Screening visit for a clinical trial.
Teeth in good repair.
Photographs local wildlife.
Owns a bicycle.
Never received a mechanical heart valve.
```

**pres** (does not meet)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Teeth in good repair.
Heart sounds free of clicks.
Owns a bicycle.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 74 years.
Screening visit for a clinical trial.
Teeth in good repair.
Heart sounds without a metallic click.
```

**flip** (meets)
```
Man of 74 years.
Screening visit for a clinical trial.
Teeth in good repair.
Formerly had a mechanical mitral valve, exchanged for a bioprosthetic valve in 2015.
```

**near** (does not meet)
```
Man of 74 years.
Screening visit for a clinical trial.
Teeth in good repair.
His friend has an implanted mechanical aortic valve.
```

**pres** (does not meet)
```
Male patient of 74 years.
Screening visit for a clinical trial.
Heart sounds without a metallic click.
Teeth in good repair.
```

<a id="k166"></a>
## k166 (NCT00786474)

Exclusion criterion: Any mechanical prosthetic heart valve

Program: met iff the patient has a mechanical heart valve now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Knits as a hobby.
Heart sounds free of clicks.
Prefers to be addressed by first name.
```

**flip** (meets)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Knits as a hobby.
Mechanical mitral valve in place; metallic closing clicks audible.
Prefers to be addressed by first name.
```

**near** (does not meet)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Knits as a hobby.
Never received a mechanical heart valve.
Prefers to be addressed by first name.
```

**pres** (does not meet)
```
Woman of 70 years.
Screening visit for a clinical trial.
Knits as a hobby.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Heart sounds free of clicks.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 44 years.
Screening visit for a clinical trial.
Drives a car.
Paints watercolors as a hobby.
Heart sounds without a metallic click.
```

**flip** (meets)
```
Woman of 44 years.
Screening visit for a clinical trial.
Drives a car.
Paints watercolors as a hobby.
Mechanical mitral valve in place; metallic closing clicks audible.
```

**near** (does not meet)
```
Woman of 44 years.
Screening visit for a clinical trial.
Drives a car.
Paints watercolors as a hobby.
Her roommate attends a valve clinic for a mechanical mitral valve.
```

**pres** (does not meet)
```
Female patient of 44 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Heart sounds without a metallic click.
Drives a car.
```

<a id="k169"></a>
## k169 (NCT05554822)

Exclusion criterion: Mechanical heart prosthetic valve

Program: met iff the patient has a mechanical heart valve now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Knits as a hobby.
```

**flip** (meets)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Lives with a mechanical aortic valve prosthesis.
Knits as a hobby.
```

**near** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Never received a mechanical heart valve.
Knits as a hobby.
```

**pres** (does not meet)
```
Man of 63 years.
Screening visit for a clinical trial.
Knits as a hobby.
Sees a dentist yearly.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 73 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Heart sounds free of clicks.
```

**flip** (meets)
```
Man of 73 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Lives with a mechanical aortic valve prosthesis.
```

**near** (does not meet)
```
Man of 73 years.
Screening visit for a clinical trial.
Photographs local wildlife.
His friend has an implanted mechanical aortic valve.
```

**pres** (does not meet)
```
Male patient of 73 years.
Screening visit for a clinical trial.
Heart sounds free of clicks.
Photographs local wildlife.
```

<a id="k174"></a>
## k174 (NCT04256525)

Exclusion criterion: patients taking methotrexate

Program: met iff the patient has methotrexate treatment now (current)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 41 years.
Screening visit for a clinical trial.
Enjoys board games.
Takes no long-term prescription drugs.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Female patient of 41 years.
Screening visit for a clinical trial.
Enjoys board games.
Methotrexate 10 mg weekly, prescribed by a rheumatologist.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Female patient of 41 years.
Screening visit for a clinical trial.
Enjoys board games.
Methotrexate is absent from the pharmacy record.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Woman of 41 years.
Screening visit for a clinical trial.
Enjoys board games.
Pupils equal and reactive to light.
Takes no long-term prescription drugs.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 24 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Immunosuppressant therapy: none.
Has two cats.
```

**flip** (meets)
```
Woman of 24 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Uses methotrexate injections once a week for rheumatoid arthritis.
Has two cats.
```

**near** (does not meet)
```
Woman of 24 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Her roommate has rheumatoid arthritis treated with methotrexate.
Has two cats.
```

**pres** (does not meet)
```
Female patient of 24 years.
Screening visit for a clinical trial.
Immunosuppressant therapy: none.
Has two cats.
Pupils equal and reactive to light.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 33 years.
Screening visit for a clinical trial.
Immunosuppressant therapy: none.
Prefers to be addressed by first name.
Teeth in good repair.
```

**flip** (meets)
```
Woman of 33 years.
Screening visit for a clinical trial.
Uses methotrexate injections once a week for rheumatoid arthritis.
Prefers to be addressed by first name.
Teeth in good repair.
```

**near** (does not meet)
```
Woman of 33 years.
Screening visit for a clinical trial.
Came off methotrexate in 2023 and has taken none since.
Prefers to be addressed by first name.
Teeth in good repair.
```

**pres** (does not meet)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Immunosuppressant therapy: none.
Teeth in good repair.
```

<a id="k176"></a>
## k176 (NCT01545349)

Exclusion criterion: Neutrophil < 0.5 x10^9/L

Program: met iff the patient's current neutrophil count < 0.5 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Man of 79 years.
Screening visit for a clinical trial.
Latest neutrophil count: 0.7 x10^9/L.
Drives a car.
Sees a dentist yearly.
```

**flip** (meets)
```
Man of 79 years.
Screening visit for a clinical trial.
Latest neutrophil count: 0.3 x10^9/L.
Drives a car.
Sees a dentist yearly.
```

**near** (does not meet)
```
Man of 79 years.
Screening visit for a clinical trial.
Latest neutrophil count: 0.5 x10^9/L.
Drives a car.
Sees a dentist yearly.
```

**pres** (does not meet)
```
Male patient of 79 years.
Screening visit for a clinical trial.
Drives a car.
Sees a dentist yearly.
Current neutrophil count 0.7 x10^9/L.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 68 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest neutrophil count: 1.7 x10^9/L.
Owns a bicycle.
```

**flip** (meets)
```
Man of 68 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest neutrophil count: 0.4 x10^9/L.
Owns a bicycle.
```

**near** (does not meet)
```
Man of 68 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest neutrophil count: 0.6 x10^9/L.
Owns a bicycle.
```

**pres** (does not meet)
```
Male patient of 68 years.
Screening visit for a clinical trial.
Current neutrophil count 1.7 x10^9/L.
Owns a bicycle.
Sleeps seven hours a night.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 72 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Plays the piano.
Knits as a hobby.
Lives in a second-floor apartment.
Current neutrophil count 1.2 x10^9/L.
Records from 2005 list neutrophil count at 1.1 x10^9/L.
```

**flip** (meets)
```
Man of 72 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Plays the piano.
Knits as a hobby.
Lives in a second-floor apartment.
Current neutrophil count 0.3 x10^9/L.
Records from 2005 list neutrophil count at 1.1 x10^9/L.
```

**near** (does not meet)
```
Man of 72 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Plays the piano.
Knits as a hobby.
Lives in a second-floor apartment.
Current neutrophil count 1.2 x10^9/L.
Records from 2005 list neutrophil count at 0.4 x10^9/L.
```

**pres** (does not meet)
```
Male patient of 72 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Latest neutrophil count: 1.2 x10^9/L.
Back in 2005, neutrophil count stood at 1.1 x10^9/L.
Knits as a hobby.
Plays the piano.
Prefers to be addressed by first name.
```

<a id="k179"></a>
## k179 (NCT06968429)

Exclusion criterion: Neutrophil count ≤ 1.0 x10^9/L

Program: met iff the patient's current neutrophil count <= 1 x10^9/L

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 68 years.
Screening visit for a clinical trial.
Latest neutrophil count: 2.3 x10^9/L.
Photographs local wildlife.
```

**flip** (meets)
```
Female patient of 68 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.0 x10^9/L.
Photographs local wildlife.
```

**near** (does not meet)
```
Female patient of 68 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.1 x10^9/L.
Photographs local wildlife.
```

**pres** (does not meet)
```
Woman of 68 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Current neutrophil count 2.3 x10^9/L.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.5 x10^9/L.
Sleeps seven hours a night.
Back in 2012, neutrophil count stood at 1.5 x10^9/L.
Lives in a second-floor apartment.
Photographs local wildlife.
```

**flip** (meets)
```
Woman of 37 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.0 x10^9/L.
Sleeps seven hours a night.
Back in 2012, neutrophil count stood at 1.5 x10^9/L.
Lives in a second-floor apartment.
Photographs local wildlife.
```

**near** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.5 x10^9/L.
Sleeps seven hours a night.
Back in 2012, neutrophil count stood at 0.8 x10^9/L.
Lives in a second-floor apartment.
Photographs local wildlife.
```

**pres** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Records from 2012 list neutrophil count at 1.5 x10^9/L.
Current neutrophil count 1.5 x10^9/L.
```

<a id="k180"></a>
## k180 (NCT07495722)

Exclusion criterion: Absolute neutrophil count <1.5 x10^9/L

Program: met iff the patient's current neutrophil count < 1.5 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 65 years.
Screening visit for a clinical trial.
Latest neutrophil count: 2.4 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
Enjoys board games.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Female patient of 65 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.4 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
Enjoys board games.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Female patient of 65 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.5 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
Enjoys board games.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Woman of 65 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Enjoys board games.
Teeth in good repair.
Current neutrophil count 2.4 x10^9/L.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 78 years.
Screening visit for a clinical trial.
Latest neutrophil count: 3.0 x10^9/L.
Photographs local wildlife.
Sleeps seven hours a night.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 78 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.3 x10^9/L.
Photographs local wildlife.
Sleeps seven hours a night.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 78 years.
Screening visit for a clinical trial.
Latest neutrophil count: 1.6 x10^9/L.
Photographs local wildlife.
Sleeps seven hours a night.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 78 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Current neutrophil count 3.0 x10^9/L.
Photographs local wildlife.
Knits as a hobby.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 48 years.
Screening visit for a clinical trial.
Latest neutrophil count: 3.0 x10^9/L.
Sees a dentist yearly.
Records from 2009 list neutrophil count at 2.2 x10^9/L.
```

**flip** (meets)
```
Female patient of 48 years.
Screening visit for a clinical trial.
Latest neutrophil count: 0.9 x10^9/L.
Sees a dentist yearly.
Records from 2009 list neutrophil count at 2.2 x10^9/L.
```

**near** (does not meet)
```
Female patient of 48 years.
Screening visit for a clinical trial.
Latest neutrophil count: 3.0 x10^9/L.
Sees a dentist yearly.
Records from 2009 list neutrophil count at 1.0 x10^9/L.
```

**pres** (does not meet)
```
Woman of 48 years.
Screening visit for a clinical trial.
Back in 2009, neutrophil count stood at 2.2 x10^9/L.
Current neutrophil count 3.0 x10^9/L.
Sees a dentist yearly.
```

<a id="k181"></a>
## k181 (NCT06202521)

Exclusion criterion: Absolute neutrophil count (ANC) <1.0 x10^9/L

Program: met iff the patient's current neutrophil count < 1 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Drives a car.
Enjoys board games.
Latest neutrophil count: 1.7 x10^9/L.
```

**flip** (meets)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Drives a car.
Enjoys board games.
Latest neutrophil count: 0.6 x10^9/L.
```

**near** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Drives a car.
Enjoys board games.
Latest neutrophil count: 1.0 x10^9/L.
```

**pres** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Current neutrophil count 1.7 x10^9/L.
Enjoys board games.
Drives a car.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Plays the piano.
Current neutrophil count 2.6 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
```

**flip** (meets)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Plays the piano.
Current neutrophil count 0.4 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Plays the piano.
Current neutrophil count 1.1 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Man of 76 years.
Screening visit for a clinical trial.
Latest neutrophil count: 2.6 x10^9/L.
Teeth in good repair.
Uses sunscreen in summer.
Plays the piano.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Records from 2012 list neutrophil count at 2.4 x10^9/L.
Enjoys board games.
Teeth in good repair.
Lives in a second-floor apartment.
Current neutrophil count 2.0 x10^9/L.
```

**flip** (meets)
```
Man of 40 years.
Screening visit for a clinical trial.
Records from 2012 list neutrophil count at 2.4 x10^9/L.
Enjoys board games.
Teeth in good repair.
Lives in a second-floor apartment.
Current neutrophil count 0.6 x10^9/L.
```

**near** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Records from 2012 list neutrophil count at 0.4 x10^9/L.
Enjoys board games.
Teeth in good repair.
Lives in a second-floor apartment.
Current neutrophil count 2.0 x10^9/L.
```

**pres** (does not meet)
```
Male patient of 40 years.
Screening visit for a clinical trial.
Teeth in good repair.
Latest neutrophil count: 2.0 x10^9/L.
Lives in a second-floor apartment.
Enjoys board games.
Back in 2012, neutrophil count stood at 2.4 x10^9/L.
```

<a id="k182"></a>
## k182 (NCT01431339)

Exclusion criterion: Absolute neutrophil count < 0.5 x10^9/L

Program: met iff the patient's current neutrophil count < 0.5 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Man of 58 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest neutrophil count: 1.3 x10^9/L.
```

**flip** (meets)
```
Man of 58 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest neutrophil count: 0.4 x10^9/L.
```

**near** (does not meet)
```
Man of 58 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Latest neutrophil count: 0.5 x10^9/L.
```

**pres** (does not meet)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Current neutrophil count 1.3 x10^9/L.
Sleeps seven hours a night.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 45 years.
Screening visit for a clinical trial.
Current neutrophil count 1.1 x10^9/L.
Enjoys board games.
Pupils equal and reactive to light.
Photographs local wildlife.
Owns a bicycle.
```

**flip** (meets)
```
Woman of 45 years.
Screening visit for a clinical trial.
Current neutrophil count 0.2 x10^9/L.
Enjoys board games.
Pupils equal and reactive to light.
Photographs local wildlife.
Owns a bicycle.
```

**near** (does not meet)
```
Woman of 45 years.
Screening visit for a clinical trial.
Current neutrophil count 0.6 x10^9/L.
Enjoys board games.
Pupils equal and reactive to light.
Photographs local wildlife.
Owns a bicycle.
```

**pres** (does not meet)
```
Female patient of 45 years.
Screening visit for a clinical trial.
Owns a bicycle.
Pupils equal and reactive to light.
Photographs local wildlife.
Enjoys board games.
Latest neutrophil count: 1.1 x10^9/L.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 39 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Knits as a hobby.
Current neutrophil count 1.3 x10^9/L.
Records from 2014 list neutrophil count at 1.3 x10^9/L.
```

**flip** (meets)
```
Male patient of 39 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Knits as a hobby.
Current neutrophil count 0.2 x10^9/L.
Records from 2014 list neutrophil count at 1.3 x10^9/L.
```

**near** (does not meet)
```
Male patient of 39 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Knits as a hobby.
Current neutrophil count 1.3 x10^9/L.
Records from 2014 list neutrophil count at 0.4 x10^9/L.
```

**pres** (does not meet)
```
Man of 39 years.
Screening visit for a clinical trial.
Knits as a hobby.
Latest neutrophil count: 1.3 x10^9/L.
Paints watercolors as a hobby.
Back in 2014, neutrophil count stood at 1.3 x10^9/L.
```

<a id="k192"></a>
## k192 (NCT04025983)

Inclusion criterion: Diagnosed with gastritis, duodenitis, or peptic ulcer

Program: met iff the patient has a peptic ulcer now (the criterion does not say whether a past occurrence counts; no case states one); also listed in the text but never mentioned in cases: gastritis, duodenitis

### near-miss kind: negation

**base** (does not meet)
```
Man of 74 years.
Screening visit for a clinical trial.
Owns a bicycle.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Man of 74 years.
Screening visit for a clinical trial.
Owns a bicycle.
Active peptic ulcer disease.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Man of 74 years.
Screening visit for a clinical trial.
Owns a bicycle.
Has never had a peptic ulcer.
Photographs local wildlife.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Male patient of 74 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Paints watercolors as a hobby.
Owns a bicycle.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 56 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Appetite good; no indigestion.
Has two cats.
Plays the piano.
```

**flip** (meets)
```
Woman of 56 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Has an active duodenal ulcer.
Has two cats.
Plays the piano.
```

**near** (does not meet)
```
Woman of 56 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Her uncle is being treated for a duodenal ulcer.
Has two cats.
Plays the piano.
```

**pres** (does not meet)
```
Female patient of 56 years.
Screening visit for a clinical trial.
Appetite good; no indigestion.
Has two cats.
Sleeps seven hours a night.
Plays the piano.
```

<a id="k193"></a>
## k193 (NCT03988842)

Exclusion criterion: Active gastric or duodenal ulcers

Program: met iff the patient has a peptic ulcer now (current)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 75 years.
Screening visit for a clinical trial.
Knits as a hobby.
Enjoys board games.
Abdomen soft and non-tender.
```

**flip** (meets)
```
Male patient of 75 years.
Screening visit for a clinical trial.
Knits as a hobby.
Enjoys board games.
Has an active duodenal ulcer.
```

**near** (does not meet)
```
Male patient of 75 years.
Screening visit for a clinical trial.
Knits as a hobby.
Enjoys board games.
Medical record negative for peptic ulcer, current or past.
```

**pres** (does not meet)
```
Man of 75 years.
Screening visit for a clinical trial.
Enjoys board games.
Knits as a hobby.
Abdomen soft and non-tender.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 66 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Woman of 66 years.
Screening visit for a clinical trial.
Active peptic ulcer disease.
Prefers morning appointments.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Woman of 66 years.
Screening visit for a clinical trial.
Her sister has peptic ulcer disease.
Prefers morning appointments.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Female patient of 66 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Prefers morning appointments.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Abdomen soft and non-tender.
Pupils equal and reactive to light.
Prefers morning appointments.
Photographs local wildlife.
```

**flip** (meets)
```
Woman of 37 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Active peptic ulcer disease.
Pupils equal and reactive to light.
Prefers morning appointments.
Photographs local wildlife.
```

**near** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Duodenal ulcer years ago; recovered fully with treatment.
Pupils equal and reactive to light.
Prefers morning appointments.
Photographs local wildlife.
```

**pres** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Abdomen soft and non-tender.
Sleeps seven hours a night.
Pupils equal and reactive to light.
Photographs local wildlife.
Prefers morning appointments.
```

<a id="k194"></a>
## k194 (NCT04375696)

Exclusion criterion: Active peptic ulcer, ulcerative colitis, Crohn disease, celiac disease, inflammatory bowel disease

Program: met iff the patient has a peptic ulcer now (current); also listed in the text but never mentioned in cases: ulcerative colitis, Crohn disease, celiac disease, inflammatory bowel disease

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Abdomen soft and non-tender.
Knits as a hobby.
```

**flip** (meets)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Has an active duodenal ulcer.
Knits as a hobby.
```

**near** (does not meet)
```
Male patient of 58 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Medical record negative for peptic ulcer, current or past.
Knits as a hobby.
```

**pres** (does not meet)
```
Man of 58 years.
Screening visit for a clinical trial.
Abdomen soft and non-tender.
Knits as a hobby.
Uses sunscreen in summer.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Drives a car.
Appetite good; no indigestion.
```

**flip** (meets)
```
Female patient of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Drives a car.
Active peptic ulcer disease.
```

**near** (does not meet)
```
Female patient of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Drives a car.
Her wife is being treated for a duodenal ulcer.
```

**pres** (does not meet)
```
Woman of 52 years.
Screening visit for a clinical trial.
Enjoys board games.
Appetite good; no indigestion.
Drives a car.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 39 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Appetite good; no indigestion.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 39 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Active peptic ulcer disease.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 39 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Formerly treated for a peptic ulcer; endoscopy in 2020 showed it had gone.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 39 years.
Screening visit for a clinical trial.
Appetite good; no indigestion.
Photographs local wildlife.
Knits as a hobby.
```

<a id="k196"></a>
## k196 (NCT00430248)

Exclusion criterion: Active liver or peptic ulcer disease

Program: met iff the patient has a peptic ulcer now (current); also listed in the text but never mentioned in cases: active liver disease

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 61 years.
Screening visit for a clinical trial.
Plays the piano.
Abdomen soft and non-tender.
Prefers morning appointments.
Teeth in good repair.
Uses sunscreen in summer.
```

**flip** (meets)
```
Female patient of 61 years.
Screening visit for a clinical trial.
Plays the piano.
Active peptic ulcer disease.
Prefers morning appointments.
Teeth in good repair.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Female patient of 61 years.
Screening visit for a clinical trial.
Plays the piano.
Medical record negative for peptic ulcer, current or past.
Prefers morning appointments.
Teeth in good repair.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Woman of 61 years.
Screening visit for a clinical trial.
Teeth in good repair.
Abdomen soft and non-tender.
Uses sunscreen in summer.
Prefers morning appointments.
Plays the piano.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 60 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Abdomen soft and non-tender.
Sees a dentist yearly.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

**flip** (meets)
```
Man of 60 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Active peptic ulcer disease.
Sees a dentist yearly.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Man of 60 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
His roommate has peptic ulcer disease.
Sees a dentist yearly.
Prefers to be addressed by first name.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Male patient of 60 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Sees a dentist yearly.
Abdomen soft and non-tender.
Sleeps seven hours a night.
Paints watercolors as a hobby.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Appetite good; no indigestion.
```

**flip** (meets)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Active peptic ulcer disease.
```

**near** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Duodenal ulcer years ago; recovered fully with treatment.
```

**pres** (does not meet)
```
Man of 76 years.
Screening visit for a clinical trial.
Appetite good; no indigestion.
Paints watercolors as a hobby.
```

<a id="k197"></a>
## k197 (NCT00247130)

Inclusion criterion: Patients with identified gastric or duodenal ulcer

Program: met iff the patient has a peptic ulcer now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Abdomen soft and non-tender.
Prefers to be addressed by first name.
Enjoys board games.
Plays the piano.
```

**flip** (meets)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Has an active duodenal ulcer.
Prefers to be addressed by first name.
Enjoys board games.
Plays the piano.
```

**near** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Has never had a peptic ulcer.
Prefers to be addressed by first name.
Enjoys board games.
Plays the piano.
```

**pres** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Prefers to be addressed by first name.
Enjoys board games.
Abdomen soft and non-tender.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 40 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Appetite good; no indigestion.
Uses sunscreen in summer.
```

**flip** (meets)
```
Male patient of 40 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Active peptic ulcer disease.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Male patient of 40 years.
Screening visit for a clinical trial.
Photographs local wildlife.
His roommate is being treated for a duodenal ulcer.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Uses sunscreen in summer.
Appetite good; no indigestion.
```

<a id="k199"></a>
## k199 (NCT01545349)

Exclusion criterion: Platelets < 125 x10^9/L

Program: met iff the patient's current platelet count < 125 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 79 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Platelet count now 141 x10^9/L.
```

**flip** (meets)
```
Woman of 79 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Platelet count now 110 x10^9/L.
```

**near** (does not meet)
```
Woman of 79 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Platelet count now 125 x10^9/L.
```

**pres** (does not meet)
```
Female patient of 79 years.
Screening visit for a clinical trial.
Current platelet count 141 x10^9/L.
Sees a dentist yearly.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 74 years.
Screening visit for a clinical trial.
Platelet count now 156 x10^9/L.
Has two cats.
Prefers morning appointments.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Female patient of 74 years.
Screening visit for a clinical trial.
Platelet count now 107 x10^9/L.
Has two cats.
Prefers morning appointments.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Female patient of 74 years.
Screening visit for a clinical trial.
Platelet count now 127 x10^9/L.
Has two cats.
Prefers morning appointments.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Woman of 74 years.
Screening visit for a clinical trial.
Current platelet count 156 x10^9/L.
Paints watercolors as a hobby.
Has two cats.
Prefers morning appointments.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Platelet count now 183 x10^9/L.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Records from 2012 list platelet count at 174 x10^9/L.
```

**flip** (meets)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Platelet count now 120 x10^9/L.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Records from 2012 list platelet count at 174 x10^9/L.
```

**near** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Platelet count now 183 x10^9/L.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Records from 2012 list platelet count at 115 x10^9/L.
```

**pres** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Current platelet count 183 x10^9/L.
Paints watercolors as a hobby.
Sleeps seven hours a night.
Lives in a second-floor apartment.
Back in 2012, platelet count stood at 174 x10^9/L.
```

<a id="k202"></a>
## k202 (NCT05554822)

Exclusion criterion: Platelet count <50 x10^9/L

Program: met iff the patient's current platelet count < 50 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Man of 57 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Plays the piano.
Current platelet count 106 x10^9/L.
```

**flip** (meets)
```
Man of 57 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Plays the piano.
Current platelet count 34 x10^9/L.
```

**near** (does not meet)
```
Man of 57 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Plays the piano.
Current platelet count 50 x10^9/L.
```

**pres** (does not meet)
```
Male patient of 57 years.
Screening visit for a clinical trial.
Teeth in good repair.
Platelet count now 106 x10^9/L.
Plays the piano.
Lives in a second-floor apartment.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Enjoys board games.
Sleeps seven hours a night.
Current platelet count 89 x10^9/L.
```

**flip** (meets)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Enjoys board games.
Sleeps seven hours a night.
Current platelet count 39 x10^9/L.
```

**near** (does not meet)
```
Male patient of 63 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Enjoys board games.
Sleeps seven hours a night.
Current platelet count 57 x10^9/L.
```

**pres** (does not meet)
```
Man of 63 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Plays the piano.
Sleeps seven hours a night.
Platelet count now 89 x10^9/L.
Enjoys board games.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Has two cats.
Back in 2008, platelet count stood at 74 x10^9/L.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current platelet count 86 x10^9/L.
```

**flip** (meets)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Has two cats.
Back in 2008, platelet count stood at 74 x10^9/L.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current platelet count 48 x10^9/L.
```

**near** (does not meet)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Has two cats.
Back in 2008, platelet count stood at 28 x10^9/L.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current platelet count 86 x10^9/L.
```

**pres** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Records from 2008 list platelet count at 74 x10^9/L.
Paints watercolors as a hobby.
Has two cats.
Platelet count now 86 x10^9/L.
Prefers to be addressed by first name.
```

<a id="k203"></a>
## k203 (NCT07270263)

Exclusion criterion: Thrombocytopenia with platelet count <30 × 10⁹/L

Program: met iff the patient's current platelet count < 30 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 44 years.
Screening visit for a clinical trial.
Has two cats.
Paints watercolors as a hobby.
Current platelet count 35 x10^9/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
```

**flip** (meets)
```
Woman of 44 years.
Screening visit for a clinical trial.
Has two cats.
Paints watercolors as a hobby.
Current platelet count 26 x10^9/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
```

**near** (does not meet)
```
Woman of 44 years.
Screening visit for a clinical trial.
Has two cats.
Paints watercolors as a hobby.
Current platelet count 30 x10^9/L.
Lives in a second-floor apartment.
Prefers to be addressed by first name.
```

**pres** (does not meet)
```
Female patient of 44 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
Has two cats.
Platelet count now 35 x10^9/L.
```

### near-miss kind: numeric

**base** (does not meet)
```
Man of 78 years.
Screening visit for a clinical trial.
Has two cats.
Current platelet count 54 x10^9/L.
Sees a dentist yearly.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Man of 78 years.
Screening visit for a clinical trial.
Has two cats.
Current platelet count 28 x10^9/L.
Sees a dentist yearly.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Man of 78 years.
Screening visit for a clinical trial.
Has two cats.
Current platelet count 33 x10^9/L.
Sees a dentist yearly.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Male patient of 78 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Platelet count now 54 x10^9/L.
Sees a dentist yearly.
Has two cats.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Owns a bicycle.
Records from 2022 list platelet count at 61 x10^9/L.
Sleeps seven hours a night.
Photographs local wildlife.
Platelet count now 65 x10^9/L.
```

**flip** (meets)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Owns a bicycle.
Records from 2022 list platelet count at 61 x10^9/L.
Sleeps seven hours a night.
Photographs local wildlife.
Platelet count now 21 x10^9/L.
```

**near** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Owns a bicycle.
Records from 2022 list platelet count at 22 x10^9/L.
Sleeps seven hours a night.
Photographs local wildlife.
Platelet count now 65 x10^9/L.
```

**pres** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Owns a bicycle.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Photographs local wildlife.
Current platelet count 65 x10^9/L.
Back in 2022, platelet count stood at 61 x10^9/L.
```

<a id="k205"></a>
## k205 (NCT04276155)

Exclusion criterion: Platelet count < 90 x10^9/L at the selection visit

Program: met iff the patient's current platelet count < 90 x10^9/L

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 33 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Platelet count now 96 x10^9/L.
```

**flip** (meets)
```
Male patient of 33 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Platelet count now 68 x10^9/L.
```

**near** (does not meet)
```
Male patient of 33 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Platelet count now 90 x10^9/L.
```

**pres** (does not meet)
```
Man of 33 years.
Screening visit for a clinical trial.
Current platelet count 96 x10^9/L.
Pupils equal and reactive to light.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Enjoys board games.
Platelet count now 103 x10^9/L.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Photographs local wildlife.
```

**flip** (meets)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Enjoys board games.
Platelet count now 86 x10^9/L.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Photographs local wildlife.
```

**near** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Enjoys board games.
Platelet count now 96 x10^9/L.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
Photographs local wildlife.
```

**pres** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Enjoys board games.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Current platelet count 103 x10^9/L.
Photographs local wildlife.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Current platelet count 102 x10^9/L.
Has two cats.
Records from 2009 list platelet count at 137 x10^9/L.
```

**flip** (meets)
```
Man of 50 years.
Screening visit for a clinical trial.
Current platelet count 87 x10^9/L.
Has two cats.
Records from 2009 list platelet count at 137 x10^9/L.
```

**near** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Current platelet count 102 x10^9/L.
Has two cats.
Records from 2009 list platelet count at 75 x10^9/L.
```

**pres** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Has two cats.
Platelet count now 102 x10^9/L.
Back in 2009, platelet count stood at 137 x10^9/L.
```

<a id="k207"></a>
## k207 (NCT04853758)

Exclusion criterion: Patients with serum potassium > 5.2 mmol/L

Program: met iff the patient's current serum potassium > 5.2 mmol/L

### near-miss kind: boundary

**base** (does not meet)
```
Female patient of 54 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Drives a car.
Prefers to be addressed by first name.
Sees a dentist yearly.
Current serum potassium 4.7 mmol/L.
```

**flip** (meets)
```
Female patient of 54 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Drives a car.
Prefers to be addressed by first name.
Sees a dentist yearly.
Current serum potassium 5.3 mmol/L.
```

**near** (does not meet)
```
Female patient of 54 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Drives a car.
Prefers to be addressed by first name.
Sees a dentist yearly.
Current serum potassium 5.2 mmol/L.
```

**pres** (does not meet)
```
Woman of 54 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Latest potassium result: 4.7 mmol/L.
Drives a car.
Pupils equal and reactive to light.
Sees a dentist yearly.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Latest potassium result: 4.5 mmol/L.
Prefers morning appointments.
```

**flip** (meets)
```
Woman of 30 years.
Screening visit for a clinical trial.
Latest potassium result: 5.5 mmol/L.
Prefers morning appointments.
```

**near** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Latest potassium result: 5.1 mmol/L.
Prefers morning appointments.
```

**pres** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current serum potassium 4.5 mmol/L.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Back in 2018, serum potassium stood at 4.7 mmol/L.
Pupils equal and reactive to light.
Owns a bicycle.
Sleeps seven hours a night.
Latest potassium result: 4.0 mmol/L.
Teeth in good repair.
```

**flip** (meets)
```
Woman of 31 years.
Screening visit for a clinical trial.
Back in 2018, serum potassium stood at 4.7 mmol/L.
Pupils equal and reactive to light.
Owns a bicycle.
Sleeps seven hours a night.
Latest potassium result: 5.5 mmol/L.
Teeth in good repair.
```

**near** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Back in 2018, serum potassium stood at 5.4 mmol/L.
Pupils equal and reactive to light.
Owns a bicycle.
Sleeps seven hours a night.
Latest potassium result: 4.0 mmol/L.
Teeth in good repair.
```

**pres** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Current serum potassium 4.0 mmol/L.
Teeth in good repair.
Owns a bicycle.
Pupils equal and reactive to light.
Sleeps seven hours a night.
Records from 2018 list serum potassium at 4.7 mmol/L.
```

<a id="k208"></a>
## k208 (NCT01944774)

Exclusion criterion: Potassium is < 3.5 mmol/L

Program: met iff the patient's current serum potassium < 3.5 mmol/L

### near-miss kind: boundary

**base** (does not meet)
```
Man of 51 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Teeth in good repair.
Prefers to be addressed by first name.
Latest potassium result: 5.0 mmol/L.
```

**flip** (meets)
```
Man of 51 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Teeth in good repair.
Prefers to be addressed by first name.
Latest potassium result: 3.3 mmol/L.
```

**near** (does not meet)
```
Man of 51 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Teeth in good repair.
Prefers to be addressed by first name.
Latest potassium result: 3.5 mmol/L.
```

**pres** (does not meet)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Teeth in good repair.
Current serum potassium 5.0 mmol/L.
Prefers morning appointments.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Uses sunscreen in summer.
Latest potassium result: 4.4 mmol/L.
Sees a dentist yearly.
```

**flip** (meets)
```
Woman of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Uses sunscreen in summer.
Latest potassium result: 3.4 mmol/L.
Sees a dentist yearly.
```

**near** (does not meet)
```
Woman of 59 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Uses sunscreen in summer.
Latest potassium result: 3.6 mmol/L.
Sees a dentist yearly.
```

**pres** (does not meet)
```
Female patient of 59 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Prefers morning appointments.
Current serum potassium 4.4 mmol/L.
Uses sunscreen in summer.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Current serum potassium 3.7 mmol/L.
Owns a bicycle.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Records from 2019 list serum potassium at 3.7 mmol/L.
```

**flip** (meets)
```
Man of 54 years.
Screening visit for a clinical trial.
Current serum potassium 3.3 mmol/L.
Owns a bicycle.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Records from 2019 list serum potassium at 3.7 mmol/L.
```

**near** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Current serum potassium 3.7 mmol/L.
Owns a bicycle.
Prefers to be addressed by first name.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Records from 2019 list serum potassium at 3.4 mmol/L.
```

**pres** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Back in 2019, serum potassium stood at 3.7 mmol/L.
Sleeps seven hours a night.
Latest potassium result: 3.7 mmol/L.
Owns a bicycle.
Paints watercolors as a hobby.
```

<a id="k209"></a>
## k209 (NCT07307729)

Inclusion criterion: serum potassium ≥5.5 mmol/L

Program: met iff the patient's current serum potassium >= 5.5 mmol/L

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 82 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Latest potassium result: 4.4 mmol/L.
Enjoys board games.
Plays the piano.
```

**flip** (meets)
```
Woman of 82 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Latest potassium result: 6.1 mmol/L.
Enjoys board games.
Plays the piano.
```

**near** (does not meet)
```
Woman of 82 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Latest potassium result: 5.4 mmol/L.
Enjoys board games.
Plays the piano.
```

**pres** (does not meet)
```
Female patient of 82 years.
Screening visit for a clinical trial.
Plays the piano.
Enjoys board games.
Current serum potassium 4.4 mmol/L.
Pupils equal and reactive to light.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Current serum potassium 4.7 mmol/L.
Back in 2023, serum potassium stood at 4.8 mmol/L.
Sleeps seven hours a night.
Owns a bicycle.
```

**flip** (meets)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Current serum potassium 5.5 mmol/L.
Back in 2023, serum potassium stood at 4.8 mmol/L.
Sleeps seven hours a night.
Owns a bicycle.
```

**near** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Current serum potassium 4.7 mmol/L.
Back in 2023, serum potassium stood at 5.6 mmol/L.
Sleeps seven hours a night.
Owns a bicycle.
```

**pres** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Records from 2023 list serum potassium at 4.8 mmol/L.
Latest potassium result: 4.7 mmol/L.
Owns a bicycle.
```

<a id="k211"></a>
## k211 (NCT00555217)

Exclusion criterion: Serum potassium level >5.5 mmol/L

Program: met iff the patient's current serum potassium > 5.5 mmol/L

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Latest potassium result: 4.0 mmol/L.
```

**flip** (meets)
```
Male patient of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Latest potassium result: 5.9 mmol/L.
```

**near** (does not meet)
```
Male patient of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Latest potassium result: 5.5 mmol/L.
```

**pres** (does not meet)
```
Man of 33 years.
Screening visit for a clinical trial.
Current serum potassium 4.0 mmol/L.
Teeth in good repair.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Owns a bicycle.
Current serum potassium 4.0 mmol/L.
```

**flip** (meets)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Owns a bicycle.
Current serum potassium 5.7 mmol/L.
```

**near** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Owns a bicycle.
Current serum potassium 5.4 mmol/L.
```

**pres** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Latest potassium result: 4.0 mmol/L.
Owns a bicycle.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current serum potassium 5.1 mmol/L.
Back in 2024, serum potassium stood at 4.2 mmol/L.
```

**flip** (meets)
```
Woman of 30 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current serum potassium 5.6 mmol/L.
Back in 2024, serum potassium stood at 4.2 mmol/L.
```

**near** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current serum potassium 5.1 mmol/L.
Back in 2024, serum potassium stood at 6.0 mmol/L.
```

**pres** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Latest potassium result: 5.1 mmol/L.
Sees a dentist yearly.
Records from 2024 list serum potassium at 4.2 mmol/L.
```

<a id="k213"></a>
## k213 (NCT04433338)

Exclusion criterion: Hypokalaemia: serum potassium level <3.4 mmol/l

Program: met iff the patient's current serum potassium < 3.4 mmol/L

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current serum potassium 4.3 mmol/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current serum potassium 3.3 mmol/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current serum potassium 3.4 mmol/L.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Man of 61 years.
Screening visit for a clinical trial.
Latest potassium result: 4.3 mmol/L.
Prefers morning appointments.
Sees a dentist yearly.
Paints watercolors as a hobby.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Knits as a hobby.
Latest potassium result: 4.9 mmol/L.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
```

**flip** (meets)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Knits as a hobby.
Latest potassium result: 2.9 mmol/L.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
```

**near** (does not meet)
```
Male patient of 51 years.
Screening visit for a clinical trial.
Knits as a hobby.
Latest potassium result: 3.5 mmol/L.
Paints watercolors as a hobby.
Prefers to be addressed by first name.
```

**pres** (does not meet)
```
Man of 51 years.
Screening visit for a clinical trial.
Knits as a hobby.
Prefers to be addressed by first name.
Paints watercolors as a hobby.
Current serum potassium 4.9 mmol/L.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 34 years.
Screening visit for a clinical trial.
Records from 2020 list serum potassium at 4.0 mmol/L.
Current serum potassium 4.3 mmol/L.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Man of 34 years.
Screening visit for a clinical trial.
Records from 2020 list serum potassium at 4.0 mmol/L.
Current serum potassium 3.1 mmol/L.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Man of 34 years.
Screening visit for a clinical trial.
Records from 2020 list serum potassium at 3.1 mmol/L.
Current serum potassium 4.3 mmol/L.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Male patient of 34 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Latest potassium result: 4.3 mmol/L.
Back in 2020, serum potassium stood at 4.0 mmol/L.
```

<a id="k214"></a>
## k214 (NCT03574363)

Exclusion criterion: Serum potassium > 4.8 mmol/L

Program: met iff the patient's current serum potassium > 4.8 mmol/L

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 65 years.
Screening visit for a clinical trial.
Current serum potassium 3.6 mmol/L.
Enjoys board games.
Plays the piano.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Woman of 65 years.
Screening visit for a clinical trial.
Current serum potassium 5.2 mmol/L.
Enjoys board games.
Plays the piano.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Woman of 65 years.
Screening visit for a clinical trial.
Current serum potassium 4.8 mmol/L.
Enjoys board games.
Plays the piano.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Female patient of 65 years.
Screening visit for a clinical trial.
Latest potassium result: 3.6 mmol/L.
Plays the piano.
Enjoys board games.
Pupils equal and reactive to light.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 70 years.
Screening visit for a clinical trial.
Current serum potassium 3.2 mmol/L.
Drives a car.
Enjoys board games.
```

**flip** (meets)
```
Woman of 70 years.
Screening visit for a clinical trial.
Current serum potassium 5.0 mmol/L.
Drives a car.
Enjoys board games.
```

**near** (does not meet)
```
Woman of 70 years.
Screening visit for a clinical trial.
Current serum potassium 4.7 mmol/L.
Drives a car.
Enjoys board games.
```

**pres** (does not meet)
```
Female patient of 70 years.
Screening visit for a clinical trial.
Enjoys board games.
Latest potassium result: 3.2 mmol/L.
Drives a car.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Back in 2009, serum potassium stood at 4.4 mmol/L.
Latest potassium result: 3.6 mmol/L.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Man of 54 years.
Screening visit for a clinical trial.
Back in 2009, serum potassium stood at 4.4 mmol/L.
Latest potassium result: 5.2 mmol/L.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Man of 54 years.
Screening visit for a clinical trial.
Back in 2009, serum potassium stood at 5.4 mmol/L.
Latest potassium result: 3.6 mmol/L.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Male patient of 54 years.
Screening visit for a clinical trial.
Current serum potassium 3.6 mmol/L.
Records from 2009 list serum potassium at 4.4 mmol/L.
Paints watercolors as a hobby.
```

<a id="k216"></a>
## k216 (NCT05818137)

Exclusion criterion: Pregnant or breastfeeding women

Program: met iff the patient has pregnancy now (current); also listed in the text but never mentioned in cases: breastfeeding

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 42 years.
Screening visit for a clinical trial.
Enjoys board games.
Photographs local wildlife.
```

**flip** (meets)
```
Female patient of 42 years.
Screening visit for a clinical trial.
Enjoys board games.
She is pregnant (18 weeks).
Photographs local wildlife.
```

**near** (does not meet)
```
Female patient of 42 years.
Screening visit for a clinical trial.
Enjoys board games.
Pregnancy ruled out by a blood test at this visit.
Photographs local wildlife.
```

**pres** (does not meet)
```
Woman of 42 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Enjoys board games.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Owns a bicycle.
Menstrual cycles every 28 days.
```

**flip** (meets)
```
Woman of 31 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Owns a bicycle.
She is pregnant (18 weeks).
```

**near** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Owns a bicycle.
Her friend is currently pregnant with twins.
```

**pres** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Menstrual cycles every 28 days.
Sleeps seven hours a night.
Paints watercolors as a hobby.
Owns a bicycle.
```

<a id="k218"></a>
## k218 (NCT06204640)

Exclusion criterion: Pregnant or nursing women

Program: met iff the patient has pregnancy now (current); also listed in the text but never mentioned in cases: nursing

### near-miss kind: negation

**base** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Sees a dentist yearly.
Prefers morning appointments.
```

**flip** (meets)
```
Woman of 30 years.
Screening visit for a clinical trial.
Plays the piano.
She is pregnant (18 weeks).
Sees a dentist yearly.
Prefers morning appointments.
```

**near** (does not meet)
```
Woman of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Pregnancy test negative at this visit.
Sees a dentist yearly.
Prefers morning appointments.
```

**pres** (does not meet)
```
Female patient of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Prefers morning appointments.
Sees a dentist yearly.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 32 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Menstrual cycles every 28 days.
```

**flip** (meets)
```
Female patient of 32 years.
Screening visit for a clinical trial.
Photographs local wildlife.
She is pregnant (18 weeks).
```

**near** (does not meet)
```
Female patient of 32 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Her roommate is currently pregnant with twins.
```

**pres** (does not meet)
```
Woman of 32 years.
Screening visit for a clinical trial.
Menstrual cycles every 28 days.
Photographs local wildlife.
```

<a id="k219"></a>
## k219 (NCT07606872)

Exclusion criterion: Currently pregnant or breastfeeding

Program: met iff the patient has pregnancy now (current); also listed in the text but never mentioned in cases: breastfeeding

### near-miss kind: negation

**base** (does not meet)
```
Woman of 40 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Last menstrual period began eight days before this visit.
```

**flip** (meets)
```
Woman of 40 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Pregnant, confirmed by ultrasound at 9 weeks.
```

**near** (does not meet)
```
Woman of 40 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Teeth in good repair.
Paints watercolors as a hobby.
Pregnancy ruled out by a blood test at this visit.
```

**pres** (does not meet)
```
Female patient of 40 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
Teeth in good repair.
Last menstrual period began eight days before this visit.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 41 years.
Screening visit for a clinical trial.
Menstrual cycles every 28 days.
Plays the piano.
Prefers to be addressed by first name.
Enjoys board games.
```

**flip** (meets)
```
Woman of 41 years.
Screening visit for a clinical trial.
She is pregnant (18 weeks).
Plays the piano.
Prefers to be addressed by first name.
Enjoys board games.
```

**near** (does not meet)
```
Woman of 41 years.
Screening visit for a clinical trial.
Her wife is currently pregnant with twins.
Plays the piano.
Prefers to be addressed by first name.
Enjoys board games.
```

**pres** (does not meet)
```
Female patient of 41 years.
Screening visit for a clinical trial.
Menstrual cycles every 28 days.
Enjoys board games.
Prefers to be addressed by first name.
Plays the piano.
```

<a id="k221"></a>
## k221 (NCT01431339)

Exclusion criterion: Pregnant or nursing females

Program: met iff the patient has pregnancy now (current); also listed in the text but never mentioned in cases: nursing

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 25 years.
Screening visit for a clinical trial.
Drives a car.
Lives in a second-floor apartment.
Has two cats.
```

**flip** (meets)
```
Female patient of 25 years.
Screening visit for a clinical trial.
Drives a car.
Lives in a second-floor apartment.
She is pregnant (18 weeks).
Has two cats.
```

**near** (does not meet)
```
Female patient of 25 years.
Screening visit for a clinical trial.
Drives a car.
Lives in a second-floor apartment.
Pregnancy ruled out by a blood test at this visit.
Has two cats.
```

**pres** (does not meet)
```
Woman of 25 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Drives a car.
Has two cats.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Has two cats.
Last menstrual period began eight days before this visit.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 37 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Has two cats.
Pregnant, confirmed by ultrasound at 9 weeks.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Uses sunscreen in summer.
Has two cats.
Her wife is pregnant and due next month.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Last menstrual period began eight days before this visit.
Uses sunscreen in summer.
Pupils equal and reactive to light.
Knits as a hobby.
Has two cats.
```

<a id="k225"></a>
## k225 (NCT03208361)

Exclusion criterion: Respiratory rate> 30 breaths / minute

Program: met iff the patient's current respiratory rate > 30 /min

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 71 years.
Screening visit for a clinical trial.
Observations now: respiratory rate 11/min.
Knits as a hobby.
```

**flip** (meets)
```
Woman of 71 years.
Screening visit for a clinical trial.
Observations now: respiratory rate 38/min.
Knits as a hobby.
```

**near** (does not meet)
```
Woman of 71 years.
Screening visit for a clinical trial.
Observations now: respiratory rate 30/min.
Knits as a hobby.
```

**pres** (does not meet)
```
Female patient of 71 years.
Screening visit for a clinical trial.
Knits as a hobby.
Current respiratory rate 11/min.
```

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Enjoys board games.
Observations now: respiratory rate 19/min.
Knits as a hobby.
Has two cats.
```

**flip** (meets)
```
Woman of 36 years.
Screening visit for a clinical trial.
Enjoys board games.
Observations now: respiratory rate 32/min.
Knits as a hobby.
Has two cats.
```

**near** (does not meet)
```
Woman of 36 years.
Screening visit for a clinical trial.
Enjoys board games.
Observations now: respiratory rate 28/min.
Knits as a hobby.
Has two cats.
```

**pres** (does not meet)
```
Female patient of 36 years.
Screening visit for a clinical trial.
Current respiratory rate 19/min.
Has two cats.
Knits as a hobby.
Enjoys board games.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Observations now: respiratory rate 27/min.
Lives in a second-floor apartment.
Records from 2015 list respiratory rate at 18/min.
```

**flip** (meets)
```
Man of 67 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Observations now: respiratory rate 37/min.
Lives in a second-floor apartment.
Records from 2015 list respiratory rate at 18/min.
```

**near** (does not meet)
```
Man of 67 years.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Observations now: respiratory rate 27/min.
Lives in a second-floor apartment.
Records from 2015 list respiratory rate at 35/min.
```

**pres** (does not meet)
```
Male patient of 67 years.
Screening visit for a clinical trial.
Back in 2015, respiratory rate stood at 18/min.
Lives in a second-floor apartment.
Current respiratory rate 27/min.
Pupils equal and reactive to light.
```

<a id="k230"></a>
## k230 (NCT06160687)

Exclusion criterion: Hypotension (systolic blood pressure <90 mmHg).

Program: met iff the patient's current systolic blood pressure < 90 mmHg

### near-miss kind: boundary

**base** (does not meet)
```
Man of 65 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Photographs local wildlife.
Current systolic blood pressure 133 mmHg.
```

**flip** (meets)
```
Man of 65 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Photographs local wildlife.
Current systolic blood pressure 82 mmHg.
```

**near** (does not meet)
```
Man of 65 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Photographs local wildlife.
Current systolic blood pressure 90 mmHg.
```

**pres** (does not meet)
```
Male patient of 65 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Observations now: blood pressure 133/88 mmHg.
Paints watercolors as a hobby.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 72 years.
Screening visit for a clinical trial.
Enjoys board games.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Observations now: blood pressure 148/96 mmHg.
```

**flip** (meets)
```
Female patient of 72 years.
Screening visit for a clinical trial.
Enjoys board games.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Observations now: blood pressure 82/60 mmHg.
```

**near** (does not meet)
```
Female patient of 72 years.
Screening visit for a clinical trial.
Enjoys board games.
Lives in a second-floor apartment.
Uses sunscreen in summer.
Observations now: blood pressure 94/67 mmHg.
```

**pres** (does not meet)
```
Woman of 72 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Enjoys board games.
Lives in a second-floor apartment.
Current systolic blood pressure 148 mmHg.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 59 years.
Screening visit for a clinical trial.
Knits as a hobby.
Back in 2017, systolic blood pressure stood at 153 mmHg.
Observations now: blood pressure 141/93 mmHg.
```

**flip** (meets)
```
Male patient of 59 years.
Screening visit for a clinical trial.
Knits as a hobby.
Back in 2017, systolic blood pressure stood at 153 mmHg.
Observations now: blood pressure 82/60 mmHg.
```

**near** (does not meet)
```
Male patient of 59 years.
Screening visit for a clinical trial.
Knits as a hobby.
Back in 2017, systolic blood pressure stood at 88 mmHg.
Observations now: blood pressure 141/93 mmHg.
```

**pres** (does not meet)
```
Man of 59 years.
Screening visit for a clinical trial.
Current systolic blood pressure 141 mmHg.
Knits as a hobby.
Records from 2017 list systolic blood pressure at 153 mmHg.
```

<a id="k231"></a>
## k231 (NCT07804654)

Exclusion criterion: Cardiogenic shock or systolic blood pressure below 100 mmHg

Program: met iff the patient's current systolic blood pressure < 100 mmHg

### near-miss kind: boundary

**base** (does not meet)
```
Man of 61 years.
Screening visit for a clinical trial.
Plays the piano.
Observations now: blood pressure 159/102 mmHg.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Man of 61 years.
Screening visit for a clinical trial.
Plays the piano.
Observations now: blood pressure 83/61 mmHg.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Man of 61 years.
Screening visit for a clinical trial.
Plays the piano.
Observations now: blood pressure 100/70 mmHg.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Plays the piano.
Current systolic blood pressure 159 mmHg.
```

### near-miss kind: numeric

**base** (does not meet)
```
Male patient of 52 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Observations now: blood pressure 132/88 mmHg.
```

**flip** (meets)
```
Male patient of 52 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Observations now: blood pressure 85/62 mmHg.
```

**near** (does not meet)
```
Male patient of 52 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Observations now: blood pressure 102/71 mmHg.
```

**pres** (does not meet)
```
Man of 52 years.
Screening visit for a clinical trial.
Current systolic blood pressure 132 mmHg.
Uses sunscreen in summer.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 46 years.
Screening visit for a clinical trial.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Back in 2023, systolic blood pressure stood at 125 mmHg.
Owns a bicycle.
Observations now: blood pressure 129/86 mmHg.
```

**flip** (meets)
```
Male patient of 46 years.
Screening visit for a clinical trial.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Back in 2023, systolic blood pressure stood at 125 mmHg.
Owns a bicycle.
Observations now: blood pressure 84/61 mmHg.
```

**near** (does not meet)
```
Male patient of 46 years.
Screening visit for a clinical trial.
Enjoys board games.
Teeth in good repair.
Sees a dentist yearly.
Back in 2023, systolic blood pressure stood at 98 mmHg.
Owns a bicycle.
Observations now: blood pressure 129/86 mmHg.
```

**pres** (does not meet)
```
Man of 46 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current systolic blood pressure 129 mmHg.
Enjoys board games.
Owns a bicycle.
Records from 2023 list systolic blood pressure at 125 mmHg.
Sees a dentist yearly.
```

<a id="k233"></a>
## k233 (NCT04755686)

Inclusion criterion: systolic blood pressure: >90 mmHg

Program: met iff the patient's current systolic blood pressure > 90 mmHg

### near-miss kind: boundary

**base** (does not meet)
```
Male patient of 73 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current systolic blood pressure 84 mmHg.
```

**flip** (meets)
```
Male patient of 73 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current systolic blood pressure 107 mmHg.
```

**near** (does not meet)
```
Male patient of 73 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current systolic blood pressure 90 mmHg.
```

**pres** (does not meet)
```
Man of 73 years.
Screening visit for a clinical trial.
Observations now: blood pressure 84/61 mmHg.
Teeth in good repair.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 69 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current systolic blood pressure 83 mmHg.
Plays the piano.
```

**flip** (meets)
```
Female patient of 69 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current systolic blood pressure 102 mmHg.
Plays the piano.
```

**near** (does not meet)
```
Female patient of 69 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Current systolic blood pressure 87 mmHg.
Plays the piano.
```

**pres** (does not meet)
```
Woman of 69 years.
Screening visit for a clinical trial.
Observations now: blood pressure 83/61 mmHg.
Plays the piano.
Prefers morning appointments.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 79 years.
Screening visit for a clinical trial.
Back in 2009, systolic blood pressure stood at 82 mmHg.
Current systolic blood pressure 82 mmHg.
Has two cats.
```

**flip** (meets)
```
Female patient of 79 years.
Screening visit for a clinical trial.
Back in 2009, systolic blood pressure stood at 82 mmHg.
Current systolic blood pressure 98 mmHg.
Has two cats.
```

**near** (does not meet)
```
Female patient of 79 years.
Screening visit for a clinical trial.
Back in 2009, systolic blood pressure stood at 100 mmHg.
Current systolic blood pressure 82 mmHg.
Has two cats.
```

**pres** (does not meet)
```
Woman of 79 years.
Screening visit for a clinical trial.
Has two cats.
Records from 2009 list systolic blood pressure at 82 mmHg.
Observations now: blood pressure 82/60 mmHg.
```

<a id="k235"></a>
## k235 (NCT00124137)

Exclusion criterion: Systolic blood pressure less than or equal to 90 mmHg

Program: met iff the patient's current systolic blood pressure <= 90 mmHg

### near-miss kind: numeric

**base** (does not meet)
```
Woman of 62 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Observations now: blood pressure 125/84 mmHg.
Owns a bicycle.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Woman of 62 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Observations now: blood pressure 81/60 mmHg.
Owns a bicycle.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Woman of 62 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Observations now: blood pressure 94/67 mmHg.
Owns a bicycle.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Female patient of 62 years.
Screening visit for a clinical trial.
Current systolic blood pressure 125 mmHg.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Photographs local wildlife.
Owns a bicycle.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 37 years.
Screening visit for a clinical trial.
Records from 2013 list systolic blood pressure at 145 mmHg.
Current systolic blood pressure 152 mmHg.
Drives a car.
Sleeps seven hours a night.
```

**flip** (meets)
```
Man of 37 years.
Screening visit for a clinical trial.
Records from 2013 list systolic blood pressure at 145 mmHg.
Current systolic blood pressure 88 mmHg.
Drives a car.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Man of 37 years.
Screening visit for a clinical trial.
Records from 2013 list systolic blood pressure at 85 mmHg.
Current systolic blood pressure 152 mmHg.
Drives a car.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Male patient of 37 years.
Screening visit for a clinical trial.
Back in 2013, systolic blood pressure stood at 145 mmHg.
Sleeps seven hours a night.
Observations now: blood pressure 152/99 mmHg.
Drives a car.
```

<a id="k245"></a>
## k245 (NCT02293395)

Exclusion criterion: Participant with a prior stroke of any etiology or transient ischemic attack (TIA)

Program: met iff the patient has a stroke or TIA at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Man of 39 years.
Screening visit for a clinical trial.
Owns a bicycle.
Has two cats.
```

**flip** (meets)
```
Man of 39 years.
Screening visit for a clinical trial.
Owns a bicycle.
Transient ischemic attack this week; carotid imaging is pending.
Has two cats.
```

**near** (does not meet)
```
Man of 39 years.
Screening visit for a clinical trial.
Owns a bicycle.
Has never had a stroke or TIA.
Has two cats.
```

**pres** (does not meet)
```
Male patient of 39 years.
Screening visit for a clinical trial.
Has two cats.
Owns a bicycle.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Gait normal; no focal weakness.
Owns a bicycle.
Knits as a hobby.
```

**flip** (meets)
```
Male patient of 76 years.
Screening visit for a clinical trial.
Has weakness of the left arm from a stroke this month.
Owns a bicycle.
Knits as a hobby.
```

**near** (does not meet)
```
Male patient of 76 years.
Screening visit for a clinical trial.
His roommate is in the hospital with a TIA.
Owns a bicycle.
Knits as a hobby.
```

**pres** (does not meet)
```
Man of 76 years.
Screening visit for a clinical trial.
Knits as a hobby.
Gait normal; no focal weakness.
Owns a bicycle.
```

<a id="k247"></a>
## k247 (NCT00973765)

Exclusion criterion: Patients with sulfa allergy will be excluded.

Program: met iff the patient has a sulfonamide allergy now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Man of 38 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Medication allergies: none at present.
Has two cats.
```

**flip** (meets)
```
Man of 38 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Sulfonamide antibiotic allergy: generalized rash.
Has two cats.
```

**near** (does not meet)
```
Man of 38 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Has never been allergic to sulfonamide antibiotics.
Has two cats.
```

**pres** (does not meet)
```
Male patient of 38 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Has two cats.
Medication allergies: none at present.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Owns a bicycle.
Current drug allergies: none.
```

**flip** (meets)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Owns a bicycle.
Sulfonamide antibiotic allergy: generalized rash.
```

**near** (does not meet)
```
Male patient of 50 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Owns a bicycle.
His sister has a documented sulfa allergy.
```

**pres** (does not meet)
```
Man of 50 years.
Screening visit for a clinical trial.
Current drug allergies: none.
Owns a bicycle.
Sleeps seven hours a night.
```

<a id="k248"></a>
## k248 (NCT00676130)

Exclusion criterion: Allergy to sulfa drugs

Program: met iff the patient has a sulfonamide allergy now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Man of 69 years.
Screening visit for a clinical trial.
Medication allergies: none at present.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Man of 69 years.
Screening visit for a clinical trial.
Sulfonamide antibiotic allergy: generalized rash.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Man of 69 years.
Screening visit for a clinical trial.
Allergy history negative for sulfa drugs.
Enjoys board games.
Drives a car.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Male patient of 69 years.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Medication allergies: none at present.
Drives a car.
Enjoys board games.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 63 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Medication allergies: none at present.
Has two cats.
```

**flip** (meets)
```
Woman of 63 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Develops hives whenever given sulfonamide antibiotics.
Has two cats.
```

**near** (does not meet)
```
Woman of 63 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Her wife has a documented sulfa allergy.
Has two cats.
```

**pres** (does not meet)
```
Female patient of 63 years.
Screening visit for a clinical trial.
Medication allergies: none at present.
Lives in a second-floor apartment.
Has two cats.
```

<a id="k249"></a>
## k249 (NCT04682366)

Exclusion criterion: Patient with known allergy to Tamsulosin or sulfa drugs

Program: met iff the patient has a sulfonamide allergy now (the criterion does not say whether a past occurrence counts; no case states one); also listed in the text but never mentioned in cases: known allergy to tamsulosin

### near-miss kind: negation

**base** (does not meet)
```
Woman of 73 years.
Screening visit for a clinical trial.
Enjoys board games.
Current drug allergies: none.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Woman of 73 years.
Screening visit for a clinical trial.
Enjoys board games.
Develops hives whenever given sulfonamide antibiotics.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Woman of 73 years.
Screening visit for a clinical trial.
Enjoys board games.
Allergy history negative for sulfa drugs.
Photographs local wildlife.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Female patient of 73 years.
Screening visit for a clinical trial.
Enjoys board games.
Lives in a second-floor apartment.
Current drug allergies: none.
Photographs local wildlife.
```

### near-miss kind: subject

**base** (does not meet)
```
Woman of 34 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Current drug allergies: none.
Uses sunscreen in summer.
```

**flip** (meets)
```
Woman of 34 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Sulfonamide antibiotic allergy: generalized rash.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Woman of 34 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Her uncle has a documented sulfa allergy.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Female patient of 34 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Photographs local wildlife.
Current drug allergies: none.
```

<a id="k250"></a>
## k250 (NCT00143611)

Exclusion criterion: Has known hypersensitivity to sulfonamides.

Program: met iff the patient has a sulfonamide allergy now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Man of 78 years.
Screening visit for a clinical trial.
Medication allergies: none at present.
Drives a car.
Prefers morning appointments.
Knits as a hobby.
```

**flip** (meets)
```
Man of 78 years.
Screening visit for a clinical trial.
Develops hives whenever given sulfonamide antibiotics.
Drives a car.
Prefers morning appointments.
Knits as a hobby.
```

**near** (does not meet)
```
Man of 78 years.
Screening visit for a clinical trial.
Has never been allergic to sulfonamide antibiotics.
Drives a car.
Prefers morning appointments.
Knits as a hobby.
```

**pres** (does not meet)
```
Male patient of 78 years.
Screening visit for a clinical trial.
Drives a car.
Prefers morning appointments.
Medication allergies: none at present.
Knits as a hobby.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Medication allergies: none at present.
Drives a car.
Prefers to be addressed by first name.
```

**flip** (meets)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Sulfonamide antibiotic allergy: generalized rash.
Drives a car.
Prefers to be addressed by first name.
```

**near** (does not meet)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Her sister has a sulfonamide antibiotic allergy.
Drives a car.
Prefers to be addressed by first name.
```

**pres** (does not meet)
```
Woman of 75 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Drives a car.
Medication allergies: none at present.
```

<a id="k260"></a>
## k260 (NCT02137187)

Exclusion criterion: myocardial infarction within the previous 3 months (the day exactly 3 months before the visit counts)

Program: met iff the patient has a myocardial infarction (heart attack) within the 3 months before the visit date (boundary day counts)

### near-miss kind: negation

**base** (does not meet)
```
Woman of 63 years.
Visit date: 28 August 2025.
Screening visit for a clinical trial.
Sees a dentist yearly.
```

**flip** (meets)
```
Woman of 63 years.
Visit date: 28 August 2025.
Screening visit for a clinical trial.
Sees a dentist yearly.
Was admitted with a myocardial infarction in July 2025.
```

**near** (does not meet)
```
Woman of 63 years.
Visit date: 28 August 2025.
Screening visit for a clinical trial.
Sees a dentist yearly.
Has never had a heart attack.
```

**pres** (does not meet)
```
Female patient of 63 years.
Visit date: 28 August 2025.
Screening visit for a clinical trial.
Sees a dentist yearly.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 60 years.
Visit date: 14 August 2024.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Enjoys board games.
```

**flip** (meets)
```
Female patient of 60 years.
Visit date: 14 August 2024.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Had a myocardial infarction in July 2024; free of chest pain since.
Enjoys board games.
```

**near** (does not meet)
```
Female patient of 60 years.
Visit date: 14 August 2024.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Her sister had a heart attack in July 2024.
Enjoys board games.
```

**pres** (does not meet)
```
Woman of 60 years.
Visit date: 14 August 2024.
Screening visit for a clinical trial.
Enjoys board games.
Prefers to be addressed by first name.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 77 years.
Visit date: 24 February 2024.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Male patient of 77 years.
Visit date: 24 February 2024.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Had a myocardial infarction 1 month ago; free of chest pain since.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Male patient of 77 years.
Visit date: 24 February 2024.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Had a myocardial infarction 16 months ago; free of chest pain since.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Man of 77 years.
Visit date: 24 February 2024.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Uses sunscreen in summer.
```

<a id="k261"></a>
## k261 (NCT04433338)

Exclusion criterion: A heart attack (myocardial infarct) in the past twelve months (the day exactly twelve months before the visit counts)

Program: met iff the patient has a myocardial infarction (heart attack) within the 12 months before the visit date (boundary day counts)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 31 years.
Visit date: 4 April 2024.
Screening visit for a clinical trial.
Owns a bicycle.
Enjoys board games.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Female patient of 31 years.
Visit date: 4 April 2024.
Screening visit for a clinical trial.
Had a heart attack in March 2024, treated with a stent.
Owns a bicycle.
Enjoys board games.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Female patient of 31 years.
Visit date: 4 April 2024.
Screening visit for a clinical trial.
Has never had a heart attack.
Owns a bicycle.
Enjoys board games.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Woman of 31 years.
Visit date: 4 April 2024.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Owns a bicycle.
Enjoys board games.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 45 years.
Visit date: 7 June 2025.
Screening visit for a clinical trial.
Enjoys board games.
Has two cats.
```

**flip** (meets)
```
Male patient of 45 years.
Visit date: 7 June 2025.
Screening visit for a clinical trial.
Enjoys board games.
Was admitted with a myocardial infarction in December 2024.
Has two cats.
```

**near** (does not meet)
```
Male patient of 45 years.
Visit date: 7 June 2025.
Screening visit for a clinical trial.
Enjoys board games.
His roommate had a heart attack in January 2025.
Has two cats.
```

**pres** (does not meet)
```
Man of 45 years.
Visit date: 7 June 2025.
Screening visit for a clinical trial.
Has two cats.
Enjoys board games.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 43 years.
Visit date: 20 August 2024.
Screening visit for a clinical trial.
Knits as a hobby.
Prefers morning appointments.
```

**flip** (meets)
```
Male patient of 43 years.
Visit date: 20 August 2024.
Screening visit for a clinical trial.
Knits as a hobby.
Had a myocardial infarction 2 months ago; free of chest pain since.
Prefers morning appointments.
```

**near** (does not meet)
```
Male patient of 43 years.
Visit date: 20 August 2024.
Screening visit for a clinical trial.
Knits as a hobby.
Had a heart attack 14 months ago, treated with a stent.
Prefers morning appointments.
```

**pres** (does not meet)
```
Man of 43 years.
Visit date: 20 August 2024.
Screening visit for a clinical trial.
Prefers morning appointments.
Knits as a hobby.
```

<a id="k266"></a>
## k266 (NCT04248894)

Exclusion criterion: Myocardial infarction within three months (the day exactly three months before the visit counts)

Program: met iff the patient has a myocardial infarction (heart attack) within the 3 months before the visit date (boundary day counts)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 50 years.
Visit date: 15 May 2024.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Male patient of 50 years.
Visit date: 15 May 2024.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Had a myocardial infarction 1 month ago; free of chest pain since.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Male patient of 50 years.
Visit date: 15 May 2024.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Has never had a heart attack.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Man of 50 years.
Visit date: 15 May 2024.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 33 years.
Visit date: 4 November 2025.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
```

**flip** (meets)
```
Man of 33 years.
Visit date: 4 November 2025.
Screening visit for a clinical trial.
Had a myocardial infarction 1 month ago; free of chest pain since.
Prefers to be addressed by first name.
```

**near** (does not meet)
```
Man of 33 years.
Visit date: 4 November 2025.
Screening visit for a clinical trial.
His wife had a heart attack 1 month ago.
Prefers to be addressed by first name.
```

**pres** (does not meet)
```
Male patient of 33 years.
Visit date: 4 November 2025.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 39 years.
Visit date: 2 April 2025.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
```

**flip** (meets)
```
Male patient of 39 years.
Visit date: 2 April 2025.
Screening visit for a clinical trial.
Had a myocardial infarction in March 2025; free of chest pain since.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
```

**near** (does not meet)
```
Male patient of 39 years.
Visit date: 2 April 2025.
Screening visit for a clinical trial.
Had a myocardial infarction in February 2023; free of chest pain since.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
```

**pres** (does not meet)
```
Man of 39 years.
Visit date: 2 April 2025.
Screening visit for a clinical trial.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
```

<a id="k269"></a>
## k269 (NCT04257500)

Exclusion criterion: Current or past deep vein thrombosis or pulmonary embolism

Program: met iff the patient has a venous thromboembolism at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Enjoys board games.
Varicose veins: none seen.
```

**flip** (meets)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Enjoys board games.
Pulmonary embolism years ago, treated for six months.
```

**near** (does not meet)
```
Female patient of 37 years.
Screening visit for a clinical trial.
Prefers morning appointments.
Sees a dentist yearly.
Enjoys board games.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
```

**pres** (does not meet)
```
Woman of 37 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Varicose veins: none seen.
Prefers morning appointments.
Enjoys board games.
```

### near-miss kind: subject

**base** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Sleeps seven hours a night.
Coagulation tests normal on recent bloodwork.
Enjoys board games.
```

**flip** (meets)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Sleeps seven hours a night.
Has an acute pulmonary embolism, diagnosed this week.
Enjoys board games.
```

**near** (does not meet)
```
Female patient of 31 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Sleeps seven hours a night.
Her friend is on anticoagulation for venous thrombosis.
Enjoys board games.
```

**pres** (does not meet)
```
Woman of 31 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Enjoys board games.
Coagulation tests normal on recent bloodwork.
Sleeps seven hours a night.
```

<a id="k271"></a>
## k271 (NCT00937911)

Exclusion criterion: Subject has history of deep vein thrombosis and/or pulmonary embolism

Program: met iff the patient has a venous thromboembolism at any time (current or past)

### near-miss kind: negation

**base** (does not meet)
```
Male patient of 44 years.
Screening visit for a clinical trial.
Coagulation tests normal on recent bloodwork.
Uses sunscreen in summer.
Plays the piano.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Male patient of 44 years.
Screening visit for a clinical trial.
Recovered from a pulmonary embolism in 2019.
Uses sunscreen in summer.
Plays the piano.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Male patient of 44 years.
Screening visit for a clinical trial.
Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.
Uses sunscreen in summer.
Plays the piano.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Man of 44 years.
Screening visit for a clinical trial.
Uses sunscreen in summer.
Lives in a second-floor apartment.
Coagulation tests normal on recent bloodwork.
Plays the piano.
```

### near-miss kind: subject

**base** (does not meet)
```
Man of 66 years.
Screening visit for a clinical trial.
Knits as a hobby.
Coagulation tests normal on recent bloodwork.
Drives a car.
```

**flip** (meets)
```
Man of 66 years.
Screening visit for a clinical trial.
Knits as a hobby.
Ongoing treatment for a deep vein thrombosis of the left arm.
Drives a car.
```

**near** (does not meet)
```
Man of 66 years.
Screening visit for a clinical trial.
Knits as a hobby.
His wife is being treated for a pulmonary embolism.
Drives a car.
```

**pres** (does not meet)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Coagulation tests normal on recent bloodwork.
Knits as a hobby.
Drives a car.
```

<a id="k272"></a>
## k272 (NCT00774748)

Exclusion criterion: Venous thromboembolism within the last 4 weeks (the day exactly 4 weeks before the visit counts)

Program: met iff the patient has a venous thromboembolism within the 4 weeks before the visit date (boundary day counts)

### near-miss kind: negation

**base** (does not meet)
```
Man of 73 years.
Visit date: 20 February 2025.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
```

**flip** (meets)
```
Man of 73 years.
Visit date: 20 February 2025.
Screening visit for a clinical trial.
Had a pulmonary embolism 3 weeks ago, treated with anticoagulation.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
```

**near** (does not meet)
```
Man of 73 years.
Visit date: 20 February 2025.
Screening visit for a clinical trial.
Has never had a DVT or pulmonary embolism.
Lives in a second-floor apartment.
Sees a dentist yearly.
Owns a bicycle.
```

**pres** (does not meet)
```
Male patient of 73 years.
Visit date: 20 February 2025.
Screening visit for a clinical trial.
Sees a dentist yearly.
Owns a bicycle.
Lives in a second-floor apartment.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 79 years.
Visit date: 19 November 2025.
Screening visit for a clinical trial.
Prefers morning appointments.
Paints watercolors as a hobby.
Uses sunscreen in summer.
```

**flip** (meets)
```
Male patient of 79 years.
Visit date: 19 November 2025.
Screening visit for a clinical trial.
Prefers morning appointments.
Had a pulmonary embolism on 1 November 2025, treated with anticoagulation.
Paints watercolors as a hobby.
Uses sunscreen in summer.
```

**near** (does not meet)
```
Male patient of 79 years.
Visit date: 19 November 2025.
Screening visit for a clinical trial.
Prefers morning appointments.
His roommate was treated for a DVT on 29 October 2025.
Paints watercolors as a hobby.
Uses sunscreen in summer.
```

**pres** (does not meet)
```
Man of 79 years.
Visit date: 19 November 2025.
Screening visit for a clinical trial.
Paints watercolors as a hobby.
Prefers morning appointments.
Uses sunscreen in summer.
```

### near-miss kind: time

**base** (does not meet)
```
Male patient of 31 years.
Visit date: 2 July 2024.
Screening visit for a clinical trial.
Prefers morning appointments.
Sleeps seven hours a night.
```

**flip** (meets)
```
Male patient of 31 years.
Visit date: 2 July 2024.
Screening visit for a clinical trial.
Prefers morning appointments.
Had a pulmonary embolism 8 days ago, treated with anticoagulation.
Sleeps seven hours a night.
```

**near** (does not meet)
```
Male patient of 31 years.
Visit date: 2 July 2024.
Screening visit for a clinical trial.
Prefers morning appointments.
Had a pulmonary embolism 9 weeks ago, treated with anticoagulation.
Sleeps seven hours a night.
```

**pres** (does not meet)
```
Man of 31 years.
Visit date: 2 July 2024.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Prefers morning appointments.
```

<a id="k273"></a>
## k273 (NCT05491109)

Exclusion criterion: Known pulmonary embolism (PE) or deep vein thrombosis (DVT)

Program: met iff the patient has a venous thromboembolism now (the criterion does not say whether a past occurrence counts; no case states one)

### near-miss kind: negation

**base** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Varicose veins: none seen.
Teeth in good repair.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
```

**flip** (meets)
```
Man of 40 years.
Screening visit for a clinical trial.
Has an acute pulmonary embolism, diagnosed this week.
Teeth in good repair.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
```

**near** (does not meet)
```
Man of 40 years.
Screening visit for a clinical trial.
Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child.
Teeth in good repair.
Paints watercolors as a hobby.
Lives in a second-floor apartment.
```

**pres** (does not meet)
```
Male patient of 40 years.
Screening visit for a clinical trial.
Teeth in good repair.
Lives in a second-floor apartment.
Paints watercolors as a hobby.
Varicose veins: none seen.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Knits as a hobby.
Drives a car.
Coagulation tests normal on recent bloodwork.
```

**flip** (meets)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Knits as a hobby.
Drives a car.
Ongoing treatment for a deep vein thrombosis of the left arm.
```

**near** (does not meet)
```
Male patient of 66 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Knits as a hobby.
Drives a car.
His friend is being treated for a pulmonary embolism.
```

**pres** (does not meet)
```
Man of 66 years.
Screening visit for a clinical trial.
Coagulation tests normal on recent bloodwork.
Lives in a second-floor apartment.
Drives a car.
Knits as a hobby.
```

<a id="k281"></a>
## k281 (NCT00839657)

Exclusion criterion: Currently taking warfarin

Program: met iff the patient has warfarin treatment now (current)

### near-miss kind: negation

**base** (does not meet)
```
Female patient of 82 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current anticoagulants: none.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**flip** (meets)
```
Female patient of 82 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Currently on warfarin, prescribed by the cardiology clinic.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**near** (does not meet)
```
Female patient of 82 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Has never been prescribed warfarin.
Pupils equal and reactive to light.
Paints watercolors as a hobby.
```

**pres** (does not meet)
```
Woman of 82 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Current anticoagulants: none.
Paints watercolors as a hobby.
Pupils equal and reactive to light.
```

### near-miss kind: subject

**base** (does not meet)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Anticoagulant therapy: none at present.
Lives in a second-floor apartment.
Sees a dentist yearly.
```

**flip** (meets)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
Currently on warfarin, prescribed by the cardiology clinic.
Lives in a second-floor apartment.
Sees a dentist yearly.
```

**near** (does not meet)
```
Male patient of 61 years.
Screening visit for a clinical trial.
Sleeps seven hours a night.
Knits as a hobby.
His friend is on warfarin with monthly INR checks.
Lives in a second-floor apartment.
Sees a dentist yearly.
```

**pres** (does not meet)
```
Man of 61 years.
Screening visit for a clinical trial.
Lives in a second-floor apartment.
Knits as a hobby.
Sees a dentist yearly.
Anticoagulant therapy: none at present.
Sleeps seven hours a night.
```

### near-miss kind: time

**base** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Current anticoagulants: none.
Sleeps seven hours a night.
Has two cats.
```

**flip** (meets)
```
Man of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Currently on warfarin, prescribed by the cardiology clinic.
Sleeps seven hours a night.
Has two cats.
```

**near** (does not meet)
```
Man of 30 years.
Screening visit for a clinical trial.
Plays the piano.
Finished a warfarin course in 2021 and is now off warfarin.
Sleeps seven hours a night.
Has two cats.
```

**pres** (does not meet)
```
Male patient of 30 years.
Screening visit for a clinical trial.
Has two cats.
Sleeps seven hours a night.
Current anticoagulants: none.
Plays the piano.
```

<a id="k287"></a>
## k287 (NCT02408185)

Inclusion criterion: More than 60 Kg of weigh

Program: met iff the patient's current weight > 60 kg

### near-miss kind: boundary

**base** (does not meet)
```
Woman of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current weight 48 kg.
Uses sunscreen in summer.
Photographs local wildlife.
```

**flip** (meets)
```
Woman of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current weight 64 kg.
Uses sunscreen in summer.
Photographs local wildlife.
```

**near** (does not meet)
```
Woman of 33 years.
Screening visit for a clinical trial.
Teeth in good repair.
Current weight 60 kg.
Uses sunscreen in summer.
Photographs local wildlife.
```

**pres** (does not meet)
```
Female patient of 33 years.
Screening visit for a clinical trial.
Photographs local wildlife.
Uses sunscreen in summer.
Teeth in good repair.
Latest weight 48 kg.
```

### near-miss kind: numeric

**base** (does not meet)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Latest weight 52 kg.
Plays the piano.
Prefers morning appointments.
```

**flip** (meets)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Latest weight 63 kg.
Plays the piano.
Prefers morning appointments.
```

**near** (does not meet)
```
Female patient of 75 years.
Screening visit for a clinical trial.
Latest weight 57 kg.
Plays the piano.
Prefers morning appointments.
```

**pres** (does not meet)
```
Woman of 75 years.
Screening visit for a clinical trial.
Current weight 52 kg.
Prefers morning appointments.
Plays the piano.
```

### near-miss kind: time

**base** (does not meet)
```
Woman of 78 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Back in 2015, weight stood at 50 kg.
Owns a bicycle.
Latest weight 51 kg.
```

**flip** (meets)
```
Woman of 78 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Back in 2015, weight stood at 50 kg.
Owns a bicycle.
Latest weight 63 kg.
```

**near** (does not meet)
```
Woman of 78 years.
Screening visit for a clinical trial.
Prefers to be addressed by first name.
Pupils equal and reactive to light.
Back in 2015, weight stood at 61 kg.
Owns a bicycle.
Latest weight 51 kg.
```

**pres** (does not meet)
```
Female patient of 78 years.
Screening visit for a clinical trial.
Owns a bicycle.
Records from 2015 list weight at 50 kg.
Pupils equal and reactive to light.
Prefers to be addressed by first name.
Current weight 51 kg.
```

<a id="k291"></a>
## k291 (NCT05515432)

Inclusion criterion: Body weight equal or above 55 kg

Program: met iff the patient's current weight >= 55 kg

### near-miss kind: numeric

**base** (does not meet)
```
Man of 48 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Enjoys board games.
Uses sunscreen in summer.
Knits as a hobby.
Current weight 48 kg.
```

**flip** (meets)
```
Man of 48 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Enjoys board games.
Uses sunscreen in summer.
Knits as a hobby.
Current weight 55 kg.
```

**near** (does not meet)
```
Man of 48 years.
Screening visit for a clinical trial.
Sees a dentist yearly.
Enjoys board games.
Uses sunscreen in summer.
Knits as a hobby.
Current weight 52 kg.
```

**pres** (does not meet)
```
Male patient of 48 years.
Screening visit for a clinical trial.
Latest weight 48 kg.
Enjoys board games.
Knits as a hobby.
Sees a dentist yearly.
Uses sunscreen in summer.
```

### near-miss kind: time

**base** (does not meet)
```
Female patient of 69 years.
Screening visit for a clinical trial.
Back in 2023, weight stood at 46 kg.
Latest weight 46 kg.
Enjoys board games.
Pupils equal and reactive to light.
Plays the piano.
```

**flip** (meets)
```
Female patient of 69 years.
Screening visit for a clinical trial.
Back in 2023, weight stood at 46 kg.
Latest weight 55 kg.
Enjoys board games.
Pupils equal and reactive to light.
Plays the piano.
```

**near** (does not meet)
```
Female patient of 69 years.
Screening visit for a clinical trial.
Back in 2023, weight stood at 67 kg.
Latest weight 46 kg.
Enjoys board games.
Pupils equal and reactive to light.
Plays the piano.
```

**pres** (does not meet)
```
Woman of 69 years.
Screening visit for a clinical trial.
Current weight 46 kg.
Pupils equal and reactive to light.
Plays the piano.
Enjoys board games.
Records from 2023 list weight at 46 kg.
```
