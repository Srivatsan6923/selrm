# ec_v1 concept inventory (what the case generator can state)

Cases are short notes. A criterion can be accepted only if it maps exactly onto one concept below, with the meaning shown by its sample lines (test-split templates; these are the only wordings cases will use).

## Measurements (one current value per case; an older dated value may also appear)

| concept | unit used in cases | sample line |
|---|---|---|
| age | years | Currently aged <v> years. |
| alt_enzyme | U/L | Current ALT <v> U/L. |
| bmi | kg/m2 | Current body mass index <v> kg/m2. |
| bun | mg/dL (blood urea nitrogen) | Blood urea nitrogen now: <v> mg/dL. |
| creatinine | mg/dL | Current serum creatinine <v> mg/dL. |
| egfr | mL/min/1.73 m2 | Current eGFR <v> mL/min/1.73 m2. |
| heart_rate | /min | Current heart rate <v>/min. |
| hemoglobin | g/dL | Current Hgb <v> g/dL. |
| inr | (no unit) | Current international normalized ratio <v>. |
| neutrophils | x10^9/L | Current neutrophil count <v> x10^9/L. |
| platelets | x10^9/L | Current platelet count <v> x10^9/L. |
| potassium | mmol/L | Current serum potassium <v> mmol/L. |
| rr | /min | Current respiratory rate <v>/min. |
| sbp | mmHg | Current systolic blood pressure <v> mmHg. |
| spo2 | % | Current oxygen saturation <v>%. |
| temperature | C | Current temperature <v> C. |
| wbc | x10^9/L | Current white cell count <v> x10^9/L. |
| weight | kg | Current weight <v> kg. |

## Findings

Forms: present (now), past (resolved / dated year), absent (explicit denial), rel (a relative has it now), rel_past (a relative had it). Window criteria ("within N days/weeks/months") are possible ONLY for the concepts marked dated-event, whose cases say when the event happened relative to a stated visit date.

### angioedema
- present: Recurrent angioedema, under allergy follow-up. / Lives with chronic angioedema that flares several times a year.
- past: An episode of angioedema years ago, with full recovery. / Formerly had recurrent angioedema, in remission for many years now.
- absent: Has never had angioedema. / Never diagnosed with angioedema.
- rel: {Poss} {rel} is being treated for angioedema. / {Poss} {rel} has active angioedema of the face.
- rel_past: {Poss} {rel} had an attack of angioedema years ago. / {Poss} {rel} recovered from an episode of angioedema in {year}.

### ascites
- present: Mild ascites seen on the current ultrasound scan. / Has mild ascites, managed with a low-salt diet and diuretics.
- past: Had ascites years ago that cleared with antiviral therapy; recovered fully. / Formerly had ascites, last seen on an ultrasound in {year}.
- absent: Ascites absent on the current ultrasound. / Ultrasound negative for ascites at this visit.
- rel: {Poss} {rel} currently has ascites. / {Poss} {rel} has ascites and takes diuretics for it.

### aspirin
- present: Currently on low-dose aspirin each day. / Swallows one low-dose aspirin each night.
- past: Formerly took a daily aspirin, discontinued years ago. / Quit low-dose aspirin in {year} and has stayed off it since.
- absent: Has never taken aspirin. / Medication history negative for aspirin.
- rel: {Poss} {rel} is on low-dose aspirin. / {Poss} {rel} uses a daily aspirin for heart protection.

### asthma
- present: Asthma, on a daily inhaled steroid. / Persistent asthma, using a rescue inhaler most weeks.
- past: Asthma in the early school years, outgrown long ago. / Formerly had asthma in elementary school; well for many years without inhalers.
- absent: Has never had asthma. / Asthma ruled out on lung function testing.
- rel: {Poss} {rel} uses an inhaler for asthma. / {Poss} {rel} is asthmatic.
- rel_past: {Poss} {rel} had asthma years ago. / {Poss} {rel} formerly had asthma and recovered fully.

### bleeding  (dated-event: window criteria possible)
- present: Currently has a major bleed from a duodenal ulcer, with transfusion under way. / Major bleed from the stomach at present, with hemoglobin falling.
- past: Major intracranial bleed after a fall years ago, with full recovery. / Recovered from a major lower gastrointestinal bleed in {year} that required transfusion.
- absent: Has never had a major bleed. / Medical records negative for major bleeding at any time.
- rel: {Poss} {rel} is currently being transfused for a major bleed. / {Poss} {rel} has major bleeding from the bowel at present.
- rel_past: {Poss} {rel} needed a blood transfusion for a major bleed years ago. / {Poss} {rel} recovered from a major intracranial bleed in {year}.
- dated event: Had a major gastrointestinal bleed <N months ago | in Month Year> that needed a transfusion. / Was admitted with a major bleed from a duodenal ulcer <N months ago | in Month Year>. / Needed a blood transfusion for a major bleed <N months ago | in Month Year>.

### cad
- present: Has coronary artery disease, managed medically. / Known coronary artery disease (two-vessel disease on angiography).
- past: Coronary artery disease years ago, with angina that went away after bypass surgery. / Had coronary artery disease, treated with bypass surgery in {year}; recovered well.
- absent: Has never had coronary artery disease. / Never diagnosed with coronary artery disease.
- rel: {Poss} {rel} has angina from coronary artery disease. / {Poss} {rel} has known coronary artery disease.
- rel_past: {Poss} {rel} had bypass surgery for coronary artery disease years ago. / {Poss} {rel} was formerly under the care of a cardiologist for coronary artery disease.

### cancer
- present: Has metastatic lung cancer, receiving palliative treatment. / Has melanoma skin cancer and is receiving treatment for it.
- past: Had thyroid cancer years ago and is now cured. / Formerly had kidney cancer, cured by surgery in {year}.
- absent: Has never had cancer. / Free of cancer throughout life.
- rel: {Poss} {rel} is being treated for leukemia. / {Poss} {rel} has lung cancer that has spread to the liver.
- rel_past: {Poss} {rel} had thyroid cancer years ago and recovered fully. / {Poss} {rel} was formerly treated for myeloma.

### chf
- present: Has heart failure, treated with diuretics. / Current heart failure with ankle swelling.
- past: Had heart failure years ago from severe anemia; it recovered fully once the anemia was corrected. / Formerly had heart failure from stress cardiomyopathy; recovered fully in {year} and off all heart medicines since.
- absent: Has never had heart failure. / Heart failure: never diagnosed.
- rel: {Poss} {rel} is treated for heart failure. / {Poss} {rel} has advanced heart failure.
- rel_past: {Poss} {rel} recovered from heart failure in {year}. / {Poss} {rel} had heart failure long ago and made a full recovery.

### clarithromycin
- present: On clarithromycin for a chest infection, day 3 of 7. / Currently taking clarithromycin for an ear infection.
- past: Took clarithromycin for pneumonia years ago. / Formerly took clarithromycin for a chest infection in {year}.
- absent: Has never taken clarithromycin. / Clarithromycin absent from the pharmacy dispensing record.
- rel: {Poss} {rel} is on a course of clarithromycin. / {Poss} {rel} currently uses clarithromycin.

### confusion
- present: Disoriented to time and place, which is new for the patient. / Newly disoriented and unable to give a clear history.
- past: Was confused for a day after surgery years ago; recovered fully. / Formerly had an episode of confusion with dehydration in {year}.
- absent: Confusion absent; answers questions appropriately. / Without any confusion on assessment.
- rel: {Poss} {rel} has become disoriented this week. / {Poss} {rel} is newly disoriented.

### contrast_allergy
- present: Carries an alert card for a severe iodinated contrast allergy. / Severe allergy to iodinated contrast, with anaphylaxis during a CT scan.
- past: Formerly allergic to iodinated contrast; has since had several contrast scans uneventfully. / An iodinated contrast allergy recorded years ago has been outgrown; recent contrast scans were uneventful.
- absent: Has never been allergic to iodinated contrast. / Tolerates iodinated contrast without any allergic reaction.
- rel: {Poss} {rel} is severely allergic to iodinated contrast. / {Poss} {rel} needs premedication before iodinated contrast because of an allergy.

### crc
- present: Colorectal cancer under active treatment. / Lives with colon cancer and attends an oncology clinic.
- past: Bowel cancer cured by surgery years ago, without recurrence. / Formerly had colon cancer; recovered fully after an operation in {year}.
- absent: Has never had bowel cancer. / Never diagnosed with colorectal cancer.
- rel: {Poss} {rel} is undergoing surgery for bowel cancer. / {Poss} {rel} has advanced colorectal cancer.
- rel_past: {Poss} {rel} was treated for bowel cancer years ago. / {Poss} {rel} recovered from colon cancer after an operation in {year}.

### diabetes
- present: Has type 2 diabetes on metformin. / Insulin-treated diabetes.
- past: Had diabetes years ago that went into remission on a low-calorie diet. / Formerly diabetic; in remission since {year}.
- absent: Has never had diabetes. / Never diagnosed with diabetes.
- rel: {Poss} {rel} is diabetic. / {Poss} {rel} lives with type 1 diabetes.
- rel_past: {Poss} {rel} had diabetes years ago that went away after a change in diet. / {Poss} {rel} was diabetic until bariatric surgery several years ago.

### exudate
- present: Tonsils swollen and coated with yellow exudate. / Tonsillar exudate visible on both sides.
- past: Had exudate on the tonsils with strep throat years ago, which cleared within days. / Recovered fully from tonsillitis with exudate in {year}.
- absent: Tonsils free of exudate. / Tonsillar exudate absent on examination.
- rel: {Poss} {rel} has a sore throat with tonsillar exudate. / {Poss} {rel} currently has a throat infection with tonsillar exudate.

### fall  (dated-event: window criteria possible)
- present: Has fallen once at home this month, shortly before this illness began. / Has fallen once in the past month, on the stairs at home.
- past: Had fallen on a wet floor years ago and recovered fully. / Formerly had fallen during a hiking trip in {year}, with full recovery.
- absent: Has never fallen. / Screening for having fallen this year was negative.
- rel: {Poss} {rel} has fallen at home and currently uses crutches. / {Poss} {rel} has fallen in the garden this week.
- dated event: Fell at home <N months ago | in Month Year> and bruised a hip. / Had a fall on the stairs <N months ago | in Month Year>. / Tripped and fell in the garden <N months ago | in Month Year>.

### hemoptysis
- present: Currently coughing up blood with each bout of coughing. / Coughing up blood now, mixed with the sputum.
- past: Coughed up blood during influenza years ago, and recovered within days. / Formerly coughed up blood from bronchiectasis, which settled after surgery in {year}.
- absent: Has never coughed up blood. / Coughing up blood: absent.
- rel: {Poss} {rel} is currently coughing up blood. / {Poss} {rel} coughs up blood and is awaiting a chest scan.

### hit
- present: Heparin-induced thrombocytopenia, with heparin antibodies still positive. / Being treated for heparin-induced thrombocytopenia by the hematology team.
- past: Heparin-induced thrombocytopenia after heart surgery years ago; recovered fully. / Formerly had heparin-induced thrombocytopenia during a hospital stay in {year}; blood counts recovered afterward.
- absent: Has never had heparin-induced thrombocytopenia. / Never diagnosed with heparin-induced thrombocytopenia.
- rel: {Poss} {rel} is in the hospital with heparin-induced thrombocytopenia. / {Poss} {rel} has developed heparin-induced thrombocytopenia after surgery.
- rel_past: {Poss} {rel} developed heparin-induced thrombocytopenia years ago. / {Poss} {rel} recovered from heparin-induced thrombocytopenia in {year}.

### hypertension
- present: Currently treated for hypertension with losartan. / Hypertensive, with candesartan as current treatment.
- past: Had hypertension during a thyroid illness years ago; it settled once the thyroid recovered. / Formerly treated for hypertension, which went away after an adrenal operation in {year}.
- absent: Has never had hypertension. / Never diagnosed with hypertension.
- rel: {Poss} {rel} currently takes medicine for hypertension. / {Poss} {rel} is hypertensive.
- rel_past: {Poss} {rel} had hypertension years ago. / {Poss} {rel} was formerly treated for hypertension.

### lithium
- present: Lithium for bipolar disorder, with stable levels. / Uses lithium tablets prescribed by a psychiatrist.
- past: Formerly took lithium, which was tapered off years ago. / Last took lithium in {year}; it was discontinued for good.
- absent: Has never taken lithium. / Lithium is absent from the medication history.
- rel: {Poss} {rel} uses lithium to prevent mood swings. / {Poss} {rel} has bipolar disorder treated with lithium.

### mech_valve
- present: Mechanical mitral valve in place; metallic closing clicks audible. / Lives with a mechanical aortic valve prosthesis.
- past: Formerly had a mechanical mitral valve, exchanged for a bioprosthetic valve in {year}. / Mechanical aortic valve explanted years ago for valve thrombosis; a bioprosthesis now sits in its place.
- absent: Has never had a mechanical heart valve. / Never received a mechanical heart valve.
- rel: {Poss} {rel} has an implanted mechanical aortic valve. / {Poss} {rel} attends a valve clinic for a mechanical mitral valve.

### methotrexate
- present: Uses methotrexate injections once a week for rheumatoid arthritis. / Methotrexate 10 mg weekly, prescribed by a rheumatologist.
- past: Formerly took weekly methotrexate, which was discontinued years ago. / Came off methotrexate in {year} and has taken none since.
- absent: Has never taken methotrexate. / Methotrexate is absent from the pharmacy record.
- rel: {Poss} {rel} uses methotrexate tablets every week. / {Poss} {rel} has rheumatoid arthritis treated with methotrexate.

### neck_nodes
- present: Anterior cervical lymph nodes enlarged and tender to touch. / Tender, swollen lymph nodes in the front of the neck.
- past: Tender anterior cervical lymph nodes with a throat infection years ago, which went down within two weeks. / Formerly had tender anterior cervical lymphadenopathy in {year}, with full recovery.
- absent: Neck supple, without tender lymph nodes. / Palpation of the neck negative for tender lymph nodes.
- rel: {Poss} {rel} has a throat infection with tender anterior cervical lymph nodes. / {Poss} {rel} currently has tender anterior cervical lymphadenopathy.

### pen_allergy
- present: Penicillin allergy: anaphylaxis. / Known penicillin allergy with angioedema.
- past: Outgrew a penicillin allergy by {year}. / Had a penicillin allergy as a child that was outgrown years ago.
- absent: Tolerates penicillin without any reaction. / Has never been allergic to penicillin.
- rel: {Poss} {rel} has a penicillin allergy. / {Poss} {rel} cannot take penicillin because of an allergy.

### peptic_ulcer
- present: Has an active duodenal ulcer. / Active peptic ulcer disease.
- past: Duodenal ulcer years ago; recovered fully with treatment. / Formerly treated for a peptic ulcer; endoscopy in {year} showed it had gone.
- absent: Has never had a peptic ulcer. / Medical record negative for peptic ulcer, current or past.
- rel: {Poss} {rel} is being treated for a duodenal ulcer. / {Poss} {rel} has peptic ulcer disease.
- rel_past: {Poss} {rel} recovered from a stomach ulcer years ago. / {Poss} {rel} formerly had peptic ulcer disease.

### pregnancy
- present: Pregnant, confirmed by ultrasound at 9 weeks. / She is pregnant (18 weeks).
- past: Her only pregnancy ended in a live birth two years ago. / Last pregnancy was in {year}; recovered well after the birth.
- absent: Pregnancy test negative at this visit. / Pregnancy ruled out by a blood test at this visit.
- rel: {Poss} {rel} is currently pregnant with twins. / {Poss} {rel} is pregnant and due next month.

### rlq_tenderness
- present: Focal tenderness in the right iliac fossa at this visit. / Exquisitely tender in the right lower quadrant.
- past: Right iliac fossa tenderness years ago from mesenteric adenitis; recovered fully. / Formerly tender in the right lower quadrant during a kidney infection in {year}, with full recovery.
- absent: Right lower quadrant without tenderness at this visit. / Tenderness absent from the right iliac fossa.
- rel: {Poss} {rel} currently has right iliac fossa tenderness. / {Poss} {rel} has tenderness in the right lower quadrant and is being seen by surgeons.

### stroke  (dated-event: window criteria possible)
- present: Has weakness of the left arm from a stroke this month. / Transient ischemic attack this week; carotid imaging is pending.
- past: TIA years ago, with full recovery. / Recovered from a stroke in {year}.
- absent: Has never had a stroke or TIA. / Never diagnosed with a stroke or TIA.
- rel: {Poss} {rel} was admitted with a stroke this week. / {Poss} {rel} is in the hospital with a TIA.
- rel_past: {Poss} {rel} had a TIA years ago. / {Poss} {rel} recovered fully from a stroke years ago.
- dated event: Had a transient ischemic attack <N months ago | in Month Year>, with full recovery. / Was admitted with a minor stroke <N months ago | in Month Year> and has recovered. / Had a stroke <N months ago | in Month Year>; no weakness remains.

### sulfa_allergy
- present: Sulfonamide antibiotic allergy: generalized rash. / Develops hives whenever given sulfonamide antibiotics.
- past: Outgrew a sulfonamide antibiotic allergy by {year}. / Had a sulfa antibiotic allergy as an infant that was outgrown long ago.
- absent: Has never been allergic to sulfonamide antibiotics. / Allergy history negative for sulfa drugs.
- rel: {Poss} {rel} has a sulfonamide antibiotic allergy. / {Poss} {rel} has a documented sulfa allergy.

### supp_oxygen
- present: Currently needs supplemental oxygen to keep comfortable. / Supplemental oxygen now running through a Venturi mask.
- past: Formerly needed supplemental oxygen during a chest infection, years ago. / Had supplemental oxygen during an admission in {year} and recovered fully.
- absent: Managing without supplemental oxygen at this visit. / Has never needed supplemental oxygen.
- rel: {Poss} {rel} is currently on supplemental oxygen. / {Poss} {rel} now uses supplemental oxygen at night.

### vascular  (dated-event: window criteria possible)
- present: Lives with peripheral artery disease affecting the left leg. / Has symptomatic peripheral artery disease of both legs.
- past: Heart attack years ago, with full recovery. / Recovered from a heart attack in {year}.
- absent: Has never had a heart attack or peripheral artery disease. / Never diagnosed with a myocardial infarction or peripheral artery disease.
- rel: {Poss} {rel} is in the hospital with a heart attack. / {Poss} {rel} has peripheral artery disease with leg pain.
- rel_past: {Poss} {rel} had a heart attack years ago. / {Poss} {rel} recovered from a heart attack earlier in life.
- dated event: Had a heart attack <N months ago | in Month Year>, treated with a stent. / Was admitted with a myocardial infarction <N months ago | in Month Year>. / Had a myocardial infarction <N months ago | in Month Year>; free of chest pain since.

### vte  (dated-event: window criteria possible)
- present: Has an acute pulmonary embolism, diagnosed this week. / Ongoing treatment for a deep vein thrombosis of the left arm.
- past: Pulmonary embolism years ago, treated for six months. / Recovered from a pulmonary embolism in {year}.
- absent: Has never had a DVT or pulmonary embolism, nor has any parent, sibling or child. / Venous thromboembolism has never occurred in the patient or in any parent, sibling or child.
- rel: {Poss} {rel} is being treated for a pulmonary embolism. / {Poss} {rel} is on anticoagulation for venous thrombosis.
- rel_past: {Poss} {rel} had a DVT years ago. / {Poss} {rel} recovered from a pulmonary embolism in {year}.
- dated event: Was treated for a deep vein thrombosis of the right leg <N months ago | in Month Year>. / Had a pulmonary embolism <N months ago | in Month Year>, treated with anticoagulation. / Was diagnosed with a DVT <N months ago | in Month Year> and completed treatment.

### warfarin
- present: Currently on warfarin, prescribed by the cardiology clinic. / Anticoagulated with warfarin; INR checked monthly at the clinic.
- past: Came off warfarin years ago after a heart rhythm problem settled. / Finished a warfarin course in {year} and is now off warfarin.
- absent: Has never been prescribed warfarin. / Warfarin is absent from the current medication list.
- rel: {Poss} {rel} is on warfarin with monthly INR checks. / {Poss} {rel} is anticoagulated with warfarin.
