# Sample canonical records (one triplet, claim s, conclusion)

## base  (label of claim s = 1; nm_kind = time; rule = vte_platelets)

```
Female, 30 years. Admitted for community-acquired pneumonia; immobile.
Latex allergy (contact dermatitis).
Drinks alcohol socially.
Platelet count measured this morning: 361
```

claim: Prescribe enoxaparin.

ledger:
```
need: platelet count below 50
found: 361
subject: patient
status: present
time: current
```

prose: For platelet count below 50, the note states "361"; this concerns the patient, is recorded as present, at present.

## flip  (label of claim s = 0; nm_kind = time; rule = vte_platelets)

```
Female, 30 years. Admitted for community-acquired pneumonia; immobile.
Latex allergy (contact dermatitis).
Drinks alcohol socially.
Platelet count measured this morning: 30
```

claim: Prescribe enoxaparin.

ledger:
```
need: platelet count below 50
found: 30
subject: patient
status: present
time: current
```

prose: For platelet count below 50, the note states "30"; this concerns the patient, is recorded as present, at present.

## near  (label of claim s = 1; nm_kind = time; rule = vte_platelets)

```
Female, 30 years. Admitted for community-acquired pneumonia; immobile.
Latex allergy (contact dermatitis).
Drinks alcohol socially.
Platelet count measured this morning: 361
Prior platelet count (2019): 33
```

claim: Prescribe enoxaparin.

ledger:
```
need: platelet count below 50
found: 361
subject: patient
status: present
time: current

need: platelet count below 50
found: 33
subject: patient
status: present
time: past (2019)
```

prose: For platelet count below 50, the note states "361"; this concerns the patient, is recorded as present, at present. For platelet count below 50, the note states "33"; this concerns the patient, is recorded as present, in the past (2019).

## pres  (label of claim s = 1; nm_kind = time; rule = vte_platelets)

```
Female, 30 years. Admitted for community-acquired pneumonia; immobile.
Platelet count measured this morning: 361
Latex allergy (contact dermatitis).
Drinks alcohol socially.
```

claim: Prescribe enoxaparin.

ledger:
```
need: platelet count below 50
found: 361
subject: patient
status: present
time: current
```

prose: For platelet count below 50, the note states "361"; this concerns the patient, is recorded as present, at present.


## One full record (JSON)
```json
{
 "tid": "test3_000000",
 "set": "smoke_v2",
 "split": "test",
 "tier": "easy",
 "level": "smoke",
 "rid": "vte_platelets",
 "cid": "plt",
 "family": "lab_threshold",
 "nm_kind": "time",
 "case_kind": "near",
 "rule_text": "For inpatient VTE prophylaxis, give enoxaparin. If the current platelet count is below 50 x10^9/L, use intermittent pneumatic compression instead.",
 "case_text": "Female, 30 years. Admitted for community-acquired pneumonia; immobile.\nLatex allergy (contact dermatitis).\nDrinks alcohol socially.\nPlatelet count measured this morning: 361\nPrior platelet count (2019): 33",
 "condition": "platelet count below 50",
 "state": [
  {
   "concept": "platelets",
   "kind": "numeric",
   "value": 361.0,
   "subject": "patient",
   "status": "present",
   "time": "current",
   "form": "present",
   "year": null
  },
  {
   "concept": "platelets",
   "kind": "numeric",
   "value": 33.0,
   "subject": "patient",
   "status": "present",
   "time": "past",
   "form": "present",
   "year": 2019
  }
 ],
 "ledger": [
  {
   "need": "platelet count below 50",
   "found": "361",
   "subject": "patient",
   "status": "present",
   "time": "current"
  },
  {
   "need": "platelet count below 50",
   "found": "33",
   "subject": "patient",
   "status": "present",
   "time": "past (2019)"
  }
 ],
 "prose": "For platelet count below 50, the note states \"361\"; this concerns the patient, is recorded as present, at present. For platelet count below 50, the note states \"33\"; this concerns the patient, is recorded as present, in the past (2019).",
 "meta": {
  "tpl": 2,
  "hdr": 2
 },
 "iid": "test3_000000/near/conclusion/s",
 "claim_type": "conclusion",
 "claim_role": "s",
 "claim_text": "Prescribe enoxaparin.",
 "label": 1
}
```
