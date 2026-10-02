# ROLE B: all training

You own every trained model in the paper and the largest GPU queue
(docs/RUN_MATRIX_B.csv, 225 rows; `pool=yes` rows are shared with idle GPUs).

## Deliverables, in order
1. **B-C0** `scripts/finetune.py`, `scripts/eval_local.py`,
   `scripts/train_eval_job.py` (train -> evaluate on every registered test
   set -> write results -> delete adapter unless kept), all resumable, with
   claims and heartbeats. Works on `data/smoke_v2` today.
2. **Today, on smoke data:** verdict x blocks vs verdict x triplets, tested on
   `smoke_v2/test_heldout_rules` (held-out rules and templates). Report
   Rev/Hold/TA by near-miss kind to the lead. Provisional, not for the paper.
3. **B-T0** timing test per format; update `est_hours`.
4. **B-F-*** factorial (Table 3): seed 0 of all 20 cells first; then seeds
   1-2 of the four key cells {verdict, ledger2} x {blocks, triplets}; then
   everything else by priority.
5. **B-PRM** step check; **B-REG** `configs/adapters.json` for kept adapters.
6. **B-TR-*** transfer rows; **B-AB-*, B-AE-*** ablations; **B-FOLD***,
   **B-DIV-***, **B-BB-***, **B-DIS-***.

## Formats (build examples from canonical records with `selrm/prompts.py`)
| Format | Training examples | Scoring |
|---|---|---|
| verdict | `verdict_prompt` -> answer | one pass |
| rationale (one-stage) | `rationale_prompt` -> ledger text, newline, answer | generate the ledger, then read the answer logits |
| summary2 | reader `reader_prompt(prose=True)` -> `prose`; judge `judge_prompt(rec, prose)` -> answer | reader generates, judge scores |
| value2 | as ledger2 with ledger entries cut to need and found | same |
| ledger2 | reader `reader_prompt` -> `ledger_to_text(ledger)`; judge `judge_prompt(rec, ledger text)` -> answer | same |

- **Equal budget:** every run trains on 60k examples for 1 epoch. Two-stage
  formats: 30k reader examples (one per case and condition) and 30k judge
  examples. Same optimiser, batch 64, lr 1e-4 cosine, max length 1024 (2048
  for long-tier evaluation), LoRA r=64, loss on the response only.
- **Ledger resampling** (judge examples): with p = 0.3 use another case of
  the same group (same rule and condition) with its own ledger and label, so
  the judge sees one claim under different ledgers. Ablation: p = 0.
- **Seeds** set data order and LoRA initialisation.
- **Evaluation of every adapter:** `rule_v1/dev`, `test_L2`, ladder sets,
  `test_hard`, `missing` (MR at 5% FR, threshold from dev), and the clinical
  sets through C's `scripts/eval_clinical.py` (fallback until it exists:
  rule-tier sets only; re-evaluate kept adapters later). INTERFACES section 3
  defines scoring and the malformed-ledger rule.

## Transfer rows (Table 4)
- fover: verdict only on FoVer formal-verification data (verify the dataset
  ID; convert to the verdict format; same example budget).
- genprm: target = short analysis + Python check (from A's
  `render_check_code`) + its output + answer. At test time generate, execute
  in a subprocess with a timeout and no network, feed the output back, read
  the answer. Record generated tokens.
- steperr: ledger2 on triplets + step-error data (only if C confirms
  MedPRMBench is released). clinonly / tripclin: need C's
  `clin_v1/clinpairs_train`.

## Ablations (Table 9, Section 7.4)
decision field; judge sees bit only; reader writes bit only; verification
pass; concept scorer (linear heads on frozen features for the ledger fields
and a linear verdict); no near-misses + probe re-weighting (down-weight
base-flip pairs whose preference shifts under near-miss and presentation
probes); no presentation edits; no resampling; verdict with a pairwise
Bradley-Terry loss; (optional P2) change loss, conclusion-only labels.
Evaluation-only items on the headline adapter: program-supplied ledger
(reader error share), program on the predicted bit, field interventions
(edit subject / status / time in a correct ledger; swap in another case's
ledger), premise gate on the step check.

## Step check (B-PRM)
If MedPRMBench is available: verdict-format PRM trained on its injected-error
steps, with the case. Otherwise register the released Med-PRM as `stepcheck`
(C provides the scoring wrapper) and log the substitution.

## Decision rules
- No hyperparameter search beyond: resampling p in {0, 0.3}, change-loss
  lambda in {0.3, 1, 3}, all on dev with seed 0.
- A run that fails twice is marked `failed` with the log path; move on.
- If `rule_v1` is late, run seed 0 of the key cells on `smoke_v2` as
  `provisional` to validate the pipeline, then re-run.
- Install flash-linear-attention and causal-conv1d before loading the model;
  record tokens/s in every `meta.json`.
