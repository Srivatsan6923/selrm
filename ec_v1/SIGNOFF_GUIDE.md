# ec_v1 sign-off (H3): two authors per criterion

`docs/EC_SIGNOFF.csv` has one row per eligibility criterion that passed the automatic pipeline. The
pipeline was:
1. The criterion was taken from a registered trial on ClinicalTrials.gov.
2. A model formalised it, and two model verifiers checked the formalisation. The `verification`
   column says whether both verifiers confirmed it, or whether it was rescued by restricting its
   near-miss kinds as a rejecting verifier specified (the verifier is quoted).
3. The generator rendered it.

No person has checked any row yet. Your sign-off decides what enters the set. Reject anything you
would hesitate to defend.

## What each row shows

| Column | Meaning |
|---|---|
| `original_text` | the criterion as registered (trial `nct_id`, `criterion_type`) |
| `registry_context` | the parent line when the criterion is one item of a list in the registry |
| `rule_text_shown` | what models see as the rule |
| `simplifications` | every change from the original |
| `never_mentioned_disjuncts` | parts of the criterion that cases never mention, so they count as absent (e.g. "or breastfeeding") |
| `program` | when the program says "meets"; it also says when the text leaves a time scope open, in which case no case states it |
| `executed_tests` | the program run on boundary inputs: values one step below, at and above a threshold; a window's boundary day; each kind of finding mention |
| `near_miss_kinds` | the edits whose cases must NOT meet the criterion |
| `cases` | where to read **every** case of this criterion: one group per near-miss kind, each with base, flip, near-miss and presentation cases, in `ec_v1/SIGNOFF_CASES.md` |
| `records_sha256` | fingerprint of exactly those cases (do not edit) |

## Your two decisions (fill your own columns)

1. **`program_ok_N`: yes / no.** Does the program do exactly what the sentence in
   `rule_text_shown` says? Check thresholds and units, inclusive or strict, the time window and
   whether the boundary day counts, whose finding counts (patient only, or relatives too), current
   or past, and inclusion versus exclusion. Say no if the original is vague, or if a simplification
   changes what the trial meant.
2. **`cases_ok_N`: yes / no.** Read every case of the criterion in `SIGNOFF_CASES.md`. Each must be
   unambiguous to a careful reader of the rule text: base not met, flip met, near-miss not met,
   presentation not met. Each must also be plausible for a screening visit. Say no if any case could
   reasonably be read the other way.

Put your name in `reviewer_N` and a reason in `comment_N` for every "no". The first author fills
the `_1` columns and the second the `_2` columns, without looking at each other's answers.

## Freezing

```
python scripts/build_ec_v1.py freeze
```

This refuses to run until every row has two different reviewers, four yes/no decisions and a
comment for every no. A criterion enters ec_v1 only with four yeses. The freeze renders the approved
criteria again and refuses if their cases differ from the ones you read (`records_sha256`).
Criteria excluded automatically, with their reasons, are in `ec_v1/EXCLUSIONS.csv`. If you think
one was excluded wrongly, tell role A; exclusions are not reversed by hand.
