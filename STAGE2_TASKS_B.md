# STAGE-2 TASKS B (training) -- 8 Oct 2026

## Paste this into your Claude Code session
> Read `README.md`, `STAGE2_ANALYSIS_PLAN.md`, `STAGE2_SPEC.md` and
> `STAGE2_TASKS_B.md`, then Section 4 and Appendices A, E, F and H of
> `paper/latex_v14/main.tex`. These files replace `FINAL_TASKS_B.md`. The
> frozen decisions in `CLAUDE.md`, `docs/INTERFACES.md` and
> `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute, credentials, or a decision listed in `HUMAN_TASKS_STAGE2.md`. Do
> the tasks in the order given. Start by reconciling `docs/STATE_B.md` with
> this file. Nothing is tuned on a test set: the parser, the linker, the gate
> and every prompt are developed on the development portions of the spec.
> Log decisions in `docs/DECISIONS_B.md`, publish outputs through
> `docs/HANDOFFS.md`, keep `docs/STATE_B.md` current.

## Context
Stage 1 gave three facts that define your work.
1. What the pipeline learns is one decision: does this finding count under
   the rule in view. A reader that writes only that bit solves 99.95% of L2
   triplets and 97.8% of rule-side items.
2. The learned judge is not a faithful function of the record: it follows
   47.8% of single-field edits that should flip the verdict. A rule program
   on the predicted record matches it (99.4 against 99.2).
3. Two-stage systems lose where the record has nothing to say: 35.9% of
   reader outputs malformed on MedEinst; key pairs 30.5-35.9 against 78-80.
Hence Ledger-RM-G (spec section 7): execute the parts of applicability that
are computable, keep the learned bit elsewhere, let the judge see the case
when the gate cannot decide, and fall back to a verdict-only score when
there is no criterion or no usable record.

The primary comparisons (7), (8), (9) and (11) use your existing stage-1
adapters. Keeping those ten verdict adapters loadable for C comes first.

## B0. Housekeeping and availability  (now)
1. Pull the runs that finished on the cluster and are not in git (summary x
   blocks seed 4, MedEinst held-out seed 2, the fold runs); if the laptop
   still runs out of memory, make `scripts/analysis_b.py` load one set at a
   time. Run `scripts/resummarize_b.py --all`. Sync `RUN_MATRIX_B.csv`.
2. Confirm that `verdict_blocks_s{0..4}`, `verdict_triplets_s{0..4}`,
   `summary2_triplets_s0`, `ledger2_blocks_s0` and `ledger2_triplets_s{0..4}`
   are in `configs/adapters.json` and loadable by C (cluster volume, or the
   private Hugging Face repository once the token is confirmed).
3. Supply the stage-1 cells still red in the paper that are yours (see
   `RED_CELLS.md`): seed 4 of summary x blocks (TA and XA), premise gate
   (CPU), L3-inv for the natural, balanced, FoVer-data and clinical-pairs
   rows, `B-TR-tripclin-s0`, XA on the 362 items without known issues for
   the nine systems of Table 19, the budget table (unique cases, reader and
   judge targets, tokens, optimiser steps per configuration), learning rate
   and lambda as used.

## B1. Gate library  (start now; needs no new data)
`selrm/crit_parse.py`, `selrm/link.py`, `selrm/gate.py`, with tests.
- Parser: deterministic, no model. Develop on `rule_v1/dev` rule texts, then
  on `rule_v2/dev`, `reg_v1/dev`, `mcv_v1/dev` as A registers them. Never on
  `xr_v1` or any test portion.
- Linker: retrieval over `onto_v1` labels and synonyms (exact, normalised,
  then an encoder that runs without a licence), top 10; the reader chooses
  or abstains. Report top-1, top-10 recall and abstention on `cls_v1/dev`.
- Gate: checks and `applies` exactly as in spec section 7.
- Acceptance: on gold records of each development set, the gate with
  `struct` equals the rule program's applicability on every record. Parser
  coverage and precision against `struct` are reported per development set.
  The date check passes boundary-day tests in both conventions.

## B2. Training on `rule_v2`  (after A5)
Same backbone, LoRA rank, budget and schedule as stage 1.
| Run | Corpus | Seeds |
|---|---|---|
| `v2_verdict_blocks` | `rule_v2/train_blocks` | 0-4 |
| `v2_verdict_triplets` | `rule_v2/train_triplets` | 0-4 |
| `v2_reader` (stage-2 record with `applies`; judge prompts in the same adapter: record only, and record plus case, half each) | `rule_v2/train_triplets` | 0-4 |
| `v2_reader` on blocks | `rule_v2/train_blocks` | 0 |
| leave-one-kind-out: `v2_verdict` and `v2_reader` | `train_triplets_lo_window`, `train_triplets_lo_class` | 0 |
Donor-record resampling as in stage 1 (p = 0.3), always with the verdict the
shown record implies. Evaluate every run on `rule_v2/dev` and `test_L2`,
`rule_v1/test_L2` (regression check against the stage-1 cells), `xr_v1`,
`cls_v1`, `reg_v1`. Report by near-miss kind.
Rough cost from stage-1 timings (2.2-2.8 GPU-hours per run): about 26 runs,
60-75 GPU-hours, plus evaluation.

## B3. Ledger-RM-G  (after B1 and B2)
1. Assemble the composite exactly as in spec section 7. Every score stores
   its `route` and the gate checks.
2. Validation before C scores anything, criteria fixed here: on
   `rule_v2/dev` the composite is not below `v2_reader` with its own bit by
   more than 0.5 points TA; on `rule_v1/dev` it is not below
   `ledger2_triplets` by more than 0.5 points. If either fails, report and
   stop; do not adjust on a test set.
3. Register `ledger_rm_g_s{0..4}` with the three variants C must report:
   `reader_bit`, `gate` (parsed criterion), `gate_struct`.
4. `docs/ANALYSIS_B_S2.md`: TA by route and by near-miss kind; gate coverage;
   where the gate overrides the bit, the 2 x 2 table (rescued, broken,
   unchanged); leave-one-kind-out for `window` and `class`: verdict-only
   against the composite (does a symbolic check remove the need to cover the
   condition in training); field-edit test repeated on the composite.

## B4. Adaptation arms  (after A1)
Verdict-only, from the backbone, 60,000 records, seeds 0-2:
- `mix_blocks`: 48,000 records of `rule_v1/train_triplets` (one fixed
  subsample, the same in both arms) + `mcv_v1/adapt_blocks`.
- `mix_triplets`: the same 48,000 + `mcv_v1/adapt_triplets`.
The arms differ only in whether the clinical-note items contain near-miss
edits. C evaluates on `mcv_v1/edits_test`, held-out scores and seen scores
separately. Reference arm: `verdict_triplets` without adaptation.

## B5. Handoffs to C and D
One line per registered system; `configs/adapters.json` entries with base
model, format and run id; for D the resources per configuration.

## Carry-over (stage-1 P1, after B0-B4 or when GPUs are idle)
GenPRM-style verifier; folds 2-3; second backbone (three remaining cells);
diversity curves (39 runs; the appendix sentence on training-rule count
depends on them); seeds 1-2 of non-core ablations. If a row will not be run,
tell D so the paper says "not run" instead of carrying a red cell.

## Stop rules
- A validation in B3.2 fails: stop the composite, report, continue with
  carry-over.
- Parser coverage on a development set below 80% of criteria with a numeric
  or temporal constraint: report it; the gate is then evaluated with its
  measured coverage, not improved on test data.
- Any need to look at test items to fix a component: do not; file the issue
  in `docs/DECISIONS_B.md`.
