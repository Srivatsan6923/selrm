# ec_v1 sign-off (H3): two authors per criterion

`docs/EC_SIGNOFF.csv` has one row per eligibility criterion that passed the automatic pipeline. Each
row comes from a registered trial on ClinicalTrials.gov, after two steps:
- a model formalised it and two model reviewers confirmed it;
- the generator rendered it.

No person has checked any row yet. Your sign-off decides what enters the set. Reject anything you
would hesitate to defend.

## What each row shows

| Column | Meaning |
|---|---|
| `original_text` | the criterion as registered (trial `nct_id`, `criterion_type`) |
| `rule_text_shown` | what models see as the rule |
| `simplifications` | every change from the original |
| `never_mentioned_disjuncts` | parts of the criterion that cases never mention, so they count as absent; for example "or breastfeeding" |
| `program` | when the program says "meets" |
| `executed_tests` | the program run on boundary inputs: values one step below, at and above a threshold; a window's boundary day; each kind of finding mention |
| `near_miss_kinds` | the edits the cases use that must NOT meet the criterion |
| `example_base`, `example_flip`, `example_near` | one rendered group. The answer is: base not met, flip met, near-miss not met |

## Your two decisions (fill your own columns)

1. **`program_ok_N`: yes / no.** Does the program do exactly what the sentence in
   `rule_text_shown` says? Check each of these:
   - thresholds and units;
   - inclusive or strict;
   - the time window and whether the boundary day counts;
   - whose finding counts (patient only, or relatives too);
   - current only, or past too;
   - inclusion versus exclusion.

   Say no if the original is vague, or if a simplification changes what the trial meant.
2. **`cases_ok_N`: yes / no.** Read the three example cases. Is each answer unambiguous to a careful
   reader of the rule text? Say no if any case could reasonably be read the other way: a hedged time
   phrase, a relative who might count, a value whose unit differs.

Put your name in `reviewer_N` and a reason in `comment_N` for every "no". The first author fills
the `_1` columns and the second author the `_2` columns, without looking at each other's answers.

A criterion enters ec_v1 only with four yeses from two different reviewers:
```
python scripts/build_ec_v1.py freeze
```
This refuses to run while any row lacks a sign-off. It renders the approved criteria afresh and
freezes the set.

Rejected criteria and the reasons for every automatic exclusion are in `ec_v1/EXCLUSIONS.csv`.
Read it if you think something was excluded wrongly. Exclusions are not reversed by hand; tell
role A.
