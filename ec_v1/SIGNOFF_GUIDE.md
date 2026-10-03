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
| `simplifications` | the formaliser's deliberate simplifications, with its reasons |
| `text_edits` | every word-level difference between `original_text` and the shown text, computed (so it can list edits that `simplifications` calls "none") |
| `never_mentioned_disjuncts` | parts of the criterion that cases never mention, so they count as absent (e.g. "or breastfeeding") |
| `program` | when the program says "meets"; it also says when the text leaves a time scope open, in which case no case states it |
| `executed_tests` | the program run on boundary inputs: values one step below, at and above a threshold (for age with a strict threshold, no case states the age at the threshold, since ages are in completed years); a window's boundary day; each kind of finding mention |
| `near_miss_kinds` | the edits whose cases must NOT meet the criterion; kinds the formalisation allowed but the generator does not render are listed with the reason |
| `groups` | the number of rendered groups: one per near-miss kind |
| `cases` | where to read **every** case of this criterion: each group has base, flip, near-miss and presentation cases, in `ec_v1/SIGNOFF_CASES.md` |
| `fingerprint` | identifies exactly the cases, the rule text and the program you read (do not edit) |

## Your file

Each reviewer works in their own file, so neither sees the other's answers:
1. Copy `docs/ec_signoff/TEMPLATE.csv` to `docs/ec_signoff/<authorN>.csv`, with your assigned id
   (author1 to author4) and not your name.
2. Fill in the rows you review. Leave the decision cells of the other rows empty.
3. Do not open another reviewer's file.

Every criterion needs exactly two reviewers. Agree among yourselves who takes which rows. If you
use Excel, save as "CSV UTF-8 (comma delimited)".

## Your two decisions

1. **`program_ok`: yes / no.** Does the program do exactly what the sentence in `rule_text_shown`
   says? Check:
   - thresholds and units, inclusive or strict;
   - the time window, and whether the boundary day counts;
   - whose finding counts (patient only, or relatives too), current or past;
   - inclusion versus exclusion.
   Say no if the original is vague, or if a simplification changes what the trial meant.
2. **`cases_ok`: yes / no.** Read every case of the criterion in `SIGNOFF_CASES.md`.
   - Each case must be unambiguous to a careful reader of the rule text: base not met, flip met,
     near-miss not met, presentation not met.
   - Each must be plausible for a screening visit.
   - Say no if any case could reasonably be read the other way.
   - If your `program_ok` is no, you may leave `cases_ok` empty: the row is rejected either way.

Give a reason in `comment` for every no. Keep the `crit_id` and `fingerprint` cells as they are.

## Freezing

```
python scripts/build_ec_v1.py freeze
```

The freeze refuses to run until:
- every criterion on the sheet has exactly two reviews;
- every review has the current fingerprint;
- every review has yes or no decisions, and a comment for every no.

A criterion enters ec_v1 only if both reviewers answer yes twice. The decisions are merged into
`docs/ec_signoff/MERGED.csv`. Criteria not approved are listed in the manifest as rejected at
sign-off.

If the sheet is regenerated (`prepare --force`), any criterion whose fingerprint changed must be
reviewed again; `prepare` refuses to run while review files exist unless forced. Criteria excluded
automatically, with their reasons, are in `ec_v1/EXCLUSIONS.csv`. If you think one was excluded
wrongly, tell role A; exclusions are not reversed by hand.
