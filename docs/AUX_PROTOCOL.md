# AUX PROTOCOL: secondary analyses added on 3-4 Oct 2026

Status: specified after the planned zero-shot comparisons (4), (5), (6)
failed. These analyses are secondary. The planned comparisons stay in the
paper as failed. Role C completed the fields that were marked TODO
(sections "S1 details" and "S2 details") on 3 Oct 2026, after building and
freezing the sets named below and before any model was trained or scored
under this protocol.

## S1. Near-miss rule data as auxiliary supervision
Question: when a verifier is trained on a medical dataset, does adding rule
triplets with near-misses improve it over adding flip pairs, and over
in-domain data alone?
- Backbone and settings: as in the main grid; verdict format.
- Recipes: (1) in-domain only; (1b) in-domain only, same optimiser steps as
  (2)/(3); (2) in-domain + aux_blocks_20k; (3) in-domain + aux_triplets_20k.
  Three seeds. Epochs for the in-domain part chosen on the dataset's dev
  split with recipe (1) and then fixed for all recipes.
- Datasets, metrics, clusters:
  | Dataset | Train | Test | Primary metric | Cluster |
  |---|---|---|---|---|
  | NLI4CT | released train | NLI4CT-P test | mean of faithfulness and consistency | trial report |
  | MedEinst | 7,807 reference pairs | 5,383 test pairs | pair reversal | diagnosis pair |
  | TrialGPT | 5 folds by patient | held-out fold | macro-F1 | patient |
- Primary contrast per dataset: (3) minus (2). Secondary: (3) minus (1b).
  Paired on identical items, Holm over the three datasets.

### S1 details (role C, 3 Oct 2026)
Files (registry `data/clin_v1/REGISTRY_C.json` on role-c; records on C's PVC
at /pvc/selrmc/data/clin_v1/<set>/records.jsonl; every set frozen, sha256 of
records.jsonl):

| Role in S1 | Set | Items | sha256 |
|---|---|---|---|
| NLI4CT train | clin_v1/nli4ct_train (released train.json, 1,700 statements, 850 entailed) | 1,700 | a6865c75ca0a9c27e570a5197421f684ea3ae28b9483cea29f6b8a441716cdb4 |
| NLI4CT dev | clin_v1/nli4ct_dev (the 200 dev originals + their contrast statements) | 2,142 | 62935e59f9b12ffaf0d87979d06bc061a5c0cfbc37c3635b2b1d22b9c73a564c |
| NLI4CT test | clin_v1/nli4ct_test (NLI4CT-P: 500 originals + 5,000 interventions, meta.intervention) | 5,500 | e8102c29f2dacc921fb929a52cba132e93fd4aaf333a6d7325af2687701ecf64 |
| MedEinst train | clin_v1/medeinst_train (alias of clin_v1/clinpairs_medeinst: 7,807 reference pairs) | 7,807 pairs | 5b0e7e9a3fdd2c958d020a34eab2b8636c11a012e176125207c222fda28ee37a |
| MedEinst dev | clin_v1/medeinst_ref_dev (500 reference pairs, disjoint from the training pairs) | 500 pairs | 7ba6648aefdb16333a4bdf0f2f47a7a770a611fea4d721bf192ed8d2c66585a4 |
| MedEinst test | clin_v1/medeinst_test | 5,383 pairs | e8f373d223583dc6c14dd8a4c70324bb2ea06659be9cb9f1cd28baa96893c284 |
| TrialGPT train/test | clin_v1/trialgpt_cv (the 43 test-portion patients, meta.fold 0-4 by patient) | 801 items | 89f2229e731f5be56fe7e91554566f63f4777cb081dbc26ab4d6fb731b194c81 |
| TrialGPT dev | clin_v1/trialgpt_dev (10 patients, never in a fold) | 213 items | 62d7cf315a8d8867ec791b51b89ec8b23be43a54e4a40698abdd360347079e4c |
| Auxiliary | rule_v1x/aux_blocks_20k, rule_v1x/aux_triplets_20k (role A) | 20,000 records each | as A registers them |

Known overlaps: no NLI4CT statement occurs in two splits; 100 trial reports
appear in both train and test (task design; the bootstrap clusters by trial
report). MedEinst reference pairs that share a narrative with a test pair
were removed when the reference sets were built.

Prompt: the frozen verdict prompt (`selrm.prompts.verdict_prompt`:
rule, case, claim -> '+' or '-'), trained and scored as in the main grid
(target '+' iff label 1; u = logit('+') - logit('-')). Per dataset:
- NLI4CT: rule_text ''; case_text = the statement's section of the trial
  report ('<Section> section of clinical trial <NCT id>:' + the section
  lines; both trials, each headed, for Comparison statements); claim_text =
  the statement. Label 1 = Entailment, 0 = Contradiction.
- MedEinst: rule_text ''; case_text = the whitespace-normalised narrative;
  claims s = 'The most likely diagnosis is <y_gt>.', s_prime = the same with
  <y_bias>. Labels: control case s 1, s_prime 0; trap case s 0, s_prime 1.
- TrialGPT: rule_text = '<Inclusion|Exclusion> criterion: <criterion text>';
  case_text = the patient note as released; claims s = 'The patient meets
  this criterion.', s_prime = 'The patient does not meet this criterion.'.
  Labels: met (1, 0); not met (0, 1); NEI (0, 0). N/A items are not used for
  training and are not scored.

Prediction rules (fixed now, the same for every recipe and seed):
- NLI4CT: Entailment iff u > 0.
- MedEinst: control correct iff d(control) = u(s) - u(s_prime) > 0, trap
  correct iff d(trap) < 0; ties fail.
- TrialGPT: per item NEI iff max(u_s, u_s') < 0 or u_s = u_s', else met if
  u_s > u_s', not met otherwise (threshold 0: these models are trained to
  give NEI items two negative claims; the zero-shot rows keep their own
  rule).

Metrics (computed by `scripts/eval_clinical.py`, the functions already used
for the zero-shot rows):
- NLI4CT: the task scorer's faithfulness (altering interventions) and
  consistency (preserving interventions) on the NLI4CT-P test; primary = their
  mean; also Control F1 (binary Entailment on the originals). Cluster = trial
  report of the statement (Primary_id).
- MedEinst: pair reversal (control and trap both correct) on the 5,383 test
  pairs; also control and trap accuracy. Cluster = (y_gt, y_bias) label pair.
- TrialGPT: macro-F1 over {met, not met, NEI} on the non-N/A items, pooled
  over the five held-out folds (every item predicted by the model that did
  not train on its patient). Cluster = patient.

Development split and epochs: recipe (1), seed 0, one run of five epochs,
evaluated after each epoch on the dev split with the primary metric; the
smallest epoch count with the best dev value is fixed for every recipe and
seed of that dataset. TrialGPT: the epoch run trains on folds 1-4 (fold 0's
training portion) and is evaluated on clin_v1/trialgpt_dev. (1b) repeats the
in-domain examples so that its optimiser steps equal those of (2)/(3); (2)
and (3) see every in-domain example the chosen number of times and every
auxiliary record once (B fixes the mixing order before the first run and
records it in its decision log).

Comparisons: per dataset, (3) - (2) (primary) and (3) - (1b) (secondary);
(3) - (1) descriptive. Paired cluster bootstrap on identical test items
(1,000 resamples, seed 0): in each resample the clusters are drawn once,
every seed's metric of both recipes is recomputed on that draw and averaged
over the three seeds, and the contrast is the difference of the averages;
percentile CI, two-sided bootstrap p. Holm over the three datasets' primary
contrasts; the secondary contrasts get their own Holm family. Seeds are
listed individually with mean and s.d.

## S2. Holding on denied evidence in clinical cases
`clin_v1/medeinst_neg`: control case plus an explicit denial of the finding
that distinguishes the trap; the control diagnosis remains correct by
construction. Metric: share of items where the control diagnosis is still
preferred. Compared across the recipes of S1 and recipe (4): in-domain plus
denied-evidence near-misses built from the reference pairs.

### S2 details (role C, 3 Oct 2026)
- Construction (`scripts/medeinst_neg.py`): MedEinst has no structured
  findings; the distinguishing finding is the trap narrative's single added
  top-level line. Pairs with no such line (1,368 test pairs) or with more
  than one (78) are left out: 3,937 test items. The denial is one line,
  '- <template>' with the finding line verbatim in the template's slot,
  appended to the control's section (Symptoms or Antecedents) that holds the
  line in the trap. Templates: role A's negation phrase bank, test-split
  phrases for clin_v1/medeinst_neg, train-split phrases for
  clin_v1/medeinst_neg_train (the same construction on the reference pairs:
  7,523 items). Both sets are frozen, and their sha256 added here, when A's
  bank is in; until then they exist only as unregistered builds.
- 46 test items deny a past-history line that names a diagnosis
  (meta.diagnosis_named); hold is reported with and without them.
- Shortcut validation (MANIFEST): the denied finding is named in every case,
  so a scorer that prefers the trap diagnosis whenever its finding is named
  holds on no item.
- Metric: hold = share of items with d = u(s) - u(s_prime) > 0 (ties fail);
  joined with the same system's MedEinst control and trap scores through
  meta.source_tid for the share of pairs that are right on control, trap and
  denial together. Cluster = diagnosis pair. Contrasts (4) - (1) and
  (3) - (2) with the S1 bootstrap; not part of a Holm family (descriptive).

## S3. Judge that sees the case
Zero-shot rows for the two-stage systems whose judge receives the case and
the record, next to the case-blind rows, on TrialGPT, MedEinst, key pairs,
NLI4CT-P. Descriptive; no claim of transfer rests on it. Scored under the
zero-shot protocols of the case-blind rows (TrialGPT: docs/TRIALGPT_PROTOCOL.md
with tau from rule_v1/dev_missing; MedEinst and key pairs: reversal; NLI4CT-P:
Entailment iff u > 0), plus hold on clin_v1/medeinst_neg once frozen.

## S4. Policies trained against each reward
Final policies scored on held-out rule cases, xr_v1, ec_v1 and TrialGPT.
Descriptive unless two seeds agree.

## Reporting
Every table that contains S1-S4 says "secondary analysis, specified after the
planned comparisons". No prompt, mapping or epoch count changes after the
first scored run.
