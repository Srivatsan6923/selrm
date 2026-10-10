# Data audit: reg_v1 (registered eligibility criteria)

Written from `data/reg_v1/MANIFEST.json` (created 2026-10-09); rebuild with `python scripts/build_reg_v1.py --restore`.

## Sources
- Chia, figshare doi 10.6084/m9.figshare.11855817.v2, CC BY 4.0; sha256 `b51ec05ba42a3805...` (`chia_with_scope.zip`)
- Leaf Clinical Trials corpus, figshare doi 10.6084/m9.figshare.17209610.v2, CC BY 4.0; sha256 `fa875243c14295ad...` (`lct_corpus.tar.gz`)

## Selection
A criterion is one annotated line. It is kept only if its annotation is a single condition: an observation or the age with one comparison, or a condition, procedure or drug with one time window in the past. Lines with a relation to another entity, a second value, a severity, a negation, an assertion or any annotator flag are not compiled.

| step | Leaf (LCT) | Chia |
|---|---|---|
| annotated lines | 7872 | 12350 |
| compiled as a single condition | 250 | 469 |
| a number, unit or operator of the structure is not in the criterion text | 37 | 3 |
| duplicate criterion text | 15 | 34 |
| threshold not positive, text over 200 characters or name under 2 characters | 2 | 1 |
| trial or criterion text of the TrialGPT annotations | 2 | 43 |
| unit or name carries a second number, comparator or conjunction (a range or a second condition) | 4 | 57 |
| candidates | 190 | 331 |
| of which numeric / window | 170 / 20 | 288 / 43 |

Lines not compiled, by reason (Leaf): comparison without one operator and one value, or with a second value, a recency or a period other than the past: 538; entity with further arguments (severity, stability, location, ...): 67; linked by a relation (or, and, example, cause, ...): 4208; not an observation or age with a value, nor a condition, procedure or drug with a time window: 318; not one entity with one comparison: 2413; operator not one of >, >=, <, <=, or value not a number: 74; temporal comparison that is not 'within N days, weeks, months or years': 4.

Lines not compiled, by reason (Chia): entity and value not linked by exactly one relation: 618; flagged by the annotators (Competing_trial): 94; flagged by the annotators (Competing_trial, Non-query-able): 1; flagged by the annotators (Context_Error): 46; flagged by the annotators (Context_Error, Grammar_Error): 3; flagged by the annotators (Context_Error, Grammar_Error, Parsing_Error): 2; flagged by the annotators (Context_Error, Grammar_Error, Undefined_semantics): 1; flagged by the annotators (Context_Error, Non-query-able): 23; flagged by the annotators (Context_Error, Non-query-able, Parsing_Error): 9; flagged by the annotators (Context_Error, Non-query-able, Parsing_Error, Post-eligibility): 1; flagged by the annotators (Context_Error, Non-query-able, Post-eligibility): 4; flagged by the annotators (Context_Error, Non-query-able, Post-eligibility, Undefined_semantics): 1.

## Model check
Two model sessions (google/gemma-4-31b-it, openai/gpt-oss-120b) read each of the 521 candidates with the compiled reading in words and answer whether it is the same condition; a criterion is kept only if both say yes: 404 kept. these are model checks, not human checks; the authors' sheet is audit/s2/reg_criteria_sheet.csv.

## Portions
| portion | criteria | trials | groups | records | numeric | window | Leaf groups | Chia groups | sha256 |
|---|---|---|---|---|---|---|---|---|---|
| dev | 27 | 23 | 81 | 486 | 66 | 15 | 15 | 66 | 3a57292501576867 |
| test | 374 | 283 | 1122 | 6732 | 978 | 144 | 306 | 816 | 6396ce64dbb4159e |

Groups by near-miss kind (test): boundary 224, negation 48, numeric 754, subject 48, window 48. Criteria for which no valid case could be drawn (test): 3.

## Conventions stated in the rule text
- numeric: Conventions: the value meant is the patient's current value as stated in the case.
- window: Conventions: time is counted back from the visit date stated in the case; an event on the day exactly {n} {unit} before the visit still counts; only events of the patient count.

## Shortcut validation
dev: always_default TA 0.0 (Rev 0.0, Hold 100.0); concept_named TA 0.0 (Rev 18.52, Hold 0.0); program TA 100.0 (Rev 100.0, Hold 100.0).
test: always_default TA 0.0 (Rev 0.0, Hold 100.0); concept_named TA 0.0 (Rev 12.83, Hold 0.0); program TA 100.0 (Rev 100.0, Hold 100.0).

## Limits
- The rule text is the registered criterion followed by the stated conventions. Case values are drawn around the threshold (within half the threshold on each side, at least five steps; age within 12 years) and are not checked for clinical plausibility. No clinician read the criteria.
- Events named by a criterion are arbitrary phrases; a case states them in a dated log line (for example `Dated 14 May 2026: <event>.`).
- The patient's sex and age in the case header are not matched to the criterion (a criterion on giving birth can meet a male header).
- Time windows are few (the annotation of most temporal criteria carries a reference point other than the visit).
