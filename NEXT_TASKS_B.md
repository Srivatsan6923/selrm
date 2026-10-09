# NEXT TASKS B (training and analysis) -- 3 Oct 2026, after the status board

## Paste this into your Claude Code session
> Read `NEXT_TASKS_B.md` and `docs/AUX_PROTOCOL.md`. They reprioritise
> `FINAL_TASKS_B.md` from the results on the status board of 3 Oct. Work
> autonomously to the end of your list; ask me only for compute or
> credentials. All integrity rules stand: frozen data are never edited, new
> sets get new names and are frozen before scoring, nothing is tuned on a
> test set, every number comes from a results file. The planned comparisons
> that failed stay reported as failed. Everything in `docs/AUX_PROTOCOL.md`
> is a secondary analysis specified after those failures and must be
> labelled so in every table and summary. Run freeze: Wed 7 Oct 23:59 UTC.

## Where the project stands (3 Oct, five seeds on the core cells)
- Near-miss supervision works: held-out rules, verdict 53.7 -> 91.8, prose
  summary 64.9 -> 98.5, ledger 71.0 -> 99.2; rule-side test 85-94 for
  triplet-trained against 36-82 for flip-pair-trained systems.
- Released medical PRMs solve 10-12% of triplets; optimising a policy
  against Med-PRM dropped held-out accuracy from 88.0 to 38.7.
- The typed ledger is not the driver: +0.8 over prose; a decision bit does
  as well; the judge follows an edited field 47.8% of the time.
- Zero-shot medical transfer failed: TrialGPT +3.4 (n.s.), MedEinst -8.5,
  key pairs collapse for two-stage systems because the judge cannot see the
  case. Only positive sign: NLI4CT-P average 0.809 -> 0.855 for verdict
  models.
- Direction from here: (1) a judge that sees the case and the record;
  (2) near-miss rule data as auxiliary supervision next to in-domain medical
  training; (3) external metrics that measure reversing and holding;
  (4) the policy-training result; (5) tests the renderer does not determine.

## Do, in this order
1. **Resume pulls with a slimmed `analysis_b.py`** (one set at a time), run
   `resummarize_b.py --all`, refresh ANALYSIS_B (five-seed ledger minus
   summary on blocks, probe re-weighting row, new xr rows), remove the two
   flagged markers.
2. **Case-visible judge** (the fix for the knowledge loss): ledger pipeline
   with a judge that sees case and record, x triplets and x blocks, seed 0;
   summary pipeline with case-visible judge x blocks seed 0; then seeds 1-2
   of the two triplets variants. Register all for C.
3. **Auxiliary-supervision grid** (`docs/AUX_PROTOCOL.md`), verdict format,
   3 seeds, in-domain sets from C:
   - recipes: (1) in-domain only; (2) in-domain + `aux_blocks_20k`;
     (3) in-domain + `aux_triplets_20k`; same in-domain examples and epochs
     in all three; (1b) in-domain only with the optimiser steps of (2)/(3);
   - datasets: NLI4CT (train -> NLI4CT-P test), MedEinst (reference pairs ->
     test pairs and the negated-evidence set), TrialGPT (5-fold by patient);
   - MedEinst extra recipe (4): in-domain + its own negated-evidence
     near-misses.
   Repeat recipes (1) and (3) with the case-visible summary pipeline for
   MedEinst and NLI4CT if GPUs allow.
4. **Leave-one-near-miss-kind-out**: seeds 1-2 for verdict and summary
   (12 runs) and a decision-bit reader with each kind left out (3 runs).
5. **Training with rewritten notes**: verdict and summary x
   `train_triplets_rw`, seed 0 (then seeds 1-2 for the better one); score on
   L2, `rewrite_v1`, `challenge_v1`, `ec_v1`, `xr_v1`.
6. **Score every kept adapter** on `challenge_v1`, `rewrite_v1`, `ec_v1` as
   A registers them.
7. **Remaining v10 rows, one seed each**: three Qwen3.5-4B cells; ledger on
   triplets + clinical pairs; GenPRM-style verifier; fold-2 and fold-3 runs
   already started; premise gate (CPU).

## Cut (do not run)
The 39 diversity-curve runs, the dose curve, seeds 1-2 of non-core cells,
extra ablation seeds, the change-loss variant. Non-core runs are evaluated
on dev, L2, `xr_v1` and the new sets only.
