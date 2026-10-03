# AUX PROTOCOL: secondary analyses added on 3-4 Oct 2026

Status: specified after the planned zero-shot comparisons (4), (5), (6)
failed. These analyses are secondary. The planned comparisons stay in the
paper as failed. Role C completes the fields marked TODO and commits this
file before any model is trained or scored under it.

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
- TODO (C): exact file hashes, prompts, label mappings, dev splits.

## S2. Holding on denied evidence in clinical cases
`clin_v1/medeinst_neg`: control case plus an explicit denial of the finding
that distinguishes the trap; the control diagnosis remains correct by
construction. Metric: share of items where the control diagnosis is still
preferred. Compared across the recipes of S1 and recipe (4): in-domain plus
denied-evidence near-misses built from the reference pairs.

## S3. Judge that sees the case
Zero-shot rows for the two-stage systems whose judge receives the case and
the record, next to the case-blind rows, on TrialGPT, MedEinst, key pairs,
NLI4CT-P. Descriptive; no claim of transfer rests on it.

## S4. Policies trained against each reward
Final policies scored on held-out rule cases, xr_v1, ec_v1 and TrialGPT.
Descriptive unless two seeds agree.

## Reporting
Every table that contains S1-S4 says "secondary analysis, specified after the
planned comparisons". No prompt, mapping or epoch count changes after the
first scored run.
