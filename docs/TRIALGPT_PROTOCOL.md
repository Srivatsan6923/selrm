# TrialGPT criterion annotations: evaluation protocol (role C)

Fixed on 3 Oct 2026 (UTC), before any system was scored on these data. Changes after
that point are logged in `docs/DECISIONS_C.md` with the reason and are applied only from
the development portion (section 7). Results: `docs/TRIALGPT_RESULTS.md`.

## 1. Source
- `ncbi/TrialGPT-Criterion-Annotations` on Hugging Face, revision
  `1cfcafde94a1560a33b4addc1638664fe28fc059` (verified 3 Oct 2026 through the Hub API),
  file `data/train-00000-of-00001.parquet` (sha256 in each MANIFEST). Licence: public
  domain (NCBI notice in the release's LICENSE). Paper: Jin et al., "Matching Patients to
  Clinical Trials with Large Language Models" (TrialGPT).
- 1,015 patient-criterion annotations, 53 patient summaries (SIGIR cohort, synthetic
  summaries), 103 trials, 1,001 distinct criterion texts.
- Built by `scripts/trialgpt_prep.py` (deterministic) into `clin_v1/trialgpt_dev` and
  `clin_v1/trialgpt_test` (`data/clin_v1/`, registry `data/clin_v1/REGISTRY_C.json`).

## 2. Columns and what we use

| Column | Kind | Use |
|---|---|---|
| `annotation_id` | identifier | item id (`tid = trialgpt_<id>`) |
| `patient_id` | identifier | split unit and bootstrap unit |
| `note` | patient summary (input) | case text, exactly as released (numbered sentences) |
| `trial_id` | identifier | trial (exclusion list for role A; per-trial variation) |
| `trial_title` | trial metadata | not used |
| `criterion_type` | criterion (input) | `inclusion` / `exclusion`, stated in the rule text |
| `criterion_text` | criterion (input) | the rule text and the condition under test |
| `expert_eligibility` | **expert label (target)** | included, not included, excluded, not excluded, not enough information, not applicable |
| `expert_sentences` | **expert evidence (target)** | ids of note sentences the expert marked as relevant; evaluates evidence selection only |
| `gpt4_explanation` | GPT-4 output | never used |
| `gpt4_sentences` | GPT-4 output | never used |
| `gpt4_eligibility` | GPT-4 output | never used |
| `explanation_correctness` | expert rating of the GPT-4 explanation | never used (it is about a GPT-4 output) |
| `training` | release flag | not used (not patient-disjoint: its 134 False rows share all 44 patients with True rows) |

The GPT-4 columns are dropped when the records are built; the build asserts that no
record contains them.

## 3. Items, categories and labels
- Dropped: annotation 883 (patient sigir-201519, NCT02213809): the release has no
  criterion text (the trial lists no exclusion criteria). Recorded in the dev MANIFEST.
- Category of an item, from `expert_eligibility` and the criterion type:
  met = included (inclusion) or excluded (exclusion); not met = not included or not
  excluded; NEI = not enough information; N/A = not applicable.
- Claims (fixed): `s` = "The patient meets this criterion.", `s_prime` = "The patient does
  not meet this criterion." Labels: met -> (1, 0); not met -> (0, 1); NEI and N/A -> (0, 0).
- No forced binary mapping: NEI is a predicted category (section 5); N/A items are kept
  and reported separately.

## 4. Inputs and systems
- Prompts are the frozen builders in `selrm/prompts.py` with the chat template and
  thinking disabled; scoring code is role B's `eval_local.py` at commit `ac524e8`
  (pointwise u = logit("+") - logit("-") at the answer position; two-stage readers
  generate once per item; a malformed ledger gives u = -20 for both claims).
- `rule_text` = "Inclusion criterion: <criterion_text>" or "Exclusion criterion:
  <criterion_text>"; `case_text` = the note as released; `condition` (shown to readers)
  = the criterion text. No GPT-4 field, no trial title, no other trial text.
- Systems, all zero-shot on these data (nothing is trained or tuned on TrialGPT):
  untrained backbone `unsloth/Qwen3.5-9B@005429c` with the verdict prompt (critic);
  the same backbone with the prompted two-stage pipelines (prose summary; ledger);
  B's adapters verdict x blocks, verdict x triplets, ledger2 x blocks, summary2 x
  triplets, ledger2 x triplets (seed 0 as registered in `configs/adapters.json`); summary2
  x blocks and further seeds when B registers them, under this protocol unchanged.
- Reader generation: max 384 new tokens for trained readers (B's setting), 768 for the
  untrained prompted readers (the same setting as their rule-tier runs).

## 5. Prediction rule
For each system, tau = its acceptance threshold from the rule-tier development set,
computed as for MR: the sorted scores u of the supported (label 1) conclusion claims of
the ordinary (non-missing) cases of `rule_v1/dev_missing`; tau = sorted[int(0.05 n)]
(rejects 5% of supported claims). Per item, with u_s and u_s':
- NEI if max(u_s, u_s') < tau, or if u_s = u_s' (no preference);
- otherwise met if u_s > u_s', not met if u_s' > u_s.
Malformed reader output therefore yields NEI (both scores -20). A secondary forced-choice
readout ignores tau (met iff u_s > u_s', ties count as wrong) and is reported on met and
not-met items only.

## 6. Metrics
Primary: macro-F1 over {met, not met, NEI} on the non-N/A items of the test portion.
Secondary: three-class accuracy; per-class precision, recall and F1 and the confusion
matrix (class-wise errors); results by criterion type (macro-F1 over the dataset's five
category names as a variant); prediction distribution on N/A items; forced-choice accuracy.
Evidence selection (systems whose reader quotes the note): a quote is the `found` value of
a ledger entry, or a double-quoted span of a prose summary, that occurs verbatim in the
note; it maps to the numbered note sentences that contain it. Precision = matched
predicted sentences / predicted sentences (items with at least one predicted sentence);
recall = matched expert sentences / expert sentences (items with at least one expert
sentence); both micro-averaged over items, on all test items including N/A. These evaluate
evidence selection only; the expert sentences do not validate subject, status or time.

## 7. Development and test portions
- Patient-disjoint split, fixed by `random.Random(20261003).sample(sorted patient ids, 10)`:
  dev = 10 patients (213 items, 20 trials), test = 43 patients (801 items, 83 trials). No
  trial occurs in both portions; 2 criterion texts do.
- Every system is scored on dev first. Dev is used only for interface checks: every record
  scored; malformed-reader rate; prompt and generation lengths. Allowed fixes are
  formatting fixes (generation length, truncation); thresholds, claims, rule text, labels
  and the prediction rule are not changed on the basis of dev scores. Any fix is logged in
  `docs/DECISIONS_C.md` before test is scored.
- Test is scored once per system. Dev numbers may appear as development results only.

## 8. Uncertainty and comparisons
- 95% CIs: percentile bootstrap over patients (1,000 resamples, seed 0); each resample
  recomputes the metric on all items of the drawn patients.
- Paired comparisons on identical items with the same resampled patients; two-sided
  bootstrap p-value. Comparison (6) of the analysis plan (fixed before any external result):
  ledger2 x triplets against the untrained backbone and against ledger2 x blocks, macro-F1;
  Holm correction is applied by the lead across the primary comparisons.
- Variation across trials: per-trial accuracy for trials with at least 5 test items
  (descriptive).
- Seeds: each seed is scored and listed separately; the summary gives mean and s.d.

## 9. What a result can show
An external, expert-annotated evaluation on synthetic patient summaries: agreement with
physician criterion-level judgments, not clinical validation, not trial screening and not
diagnosis. The patient summaries were written for retrieval research and are not
clinical records.

## 10. Amendments (each made on development data, before any test scoring)
- 3 Oct 2026: the untrained backbone's prompted ledger is read in two ways, each its own row:
  (a) the frozen malformed check (INTERFACES 3), as fixed above; (b) a format-normalised readout
  (run C-TG-promptledger-lenient), because the untrained reader writes its ledger as a markdown table or
  with markdown key-value lines, which the frozen check rejects (rule_v1/dev_missing: 586 of 600 reader
  outputs were still rejected by a line-based normalisation that did not read tables). (b) reads tables
  and markdown key-value lines (scripts/eval_c.py lenient_ledger, version 2) and keeps the verbatim-quote
  rule; it re-judges the saved reader outputs and generates nothing. Trained readers are read with the
  frozen check only.
- 3 Oct 2026: two-stage readers on the test portion generate up to 768 new tokens (development portion: 2 of 213
  ledger x triplets outputs stopped at the 384-token cap and were malformed). A cap only; no other change.
