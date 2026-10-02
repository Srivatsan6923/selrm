# SelRM: project spec (common to all four packages)

Paper: "Learning When to Change: Symbolic Supervision for Selective Evidence
Sensitivity in Medical Reward Models" (draft v10 in `paper/`; every number in
it is a placeholder). NAACL/COLING 2027 via ARR, deadline 12 Oct 2026;
manuscript frozen Sun 11 Oct. Today is Fri 2 Oct.

Goal: execute the **full v10 paper** (all three contributions, every table,
figure and appendix item) with four people working in parallel, one GPU each.

**Your role is defined in `ROLE.md`. Read it right after this file.**
Precedence when files disagree: `docs/INTERFACES.md` > `ROLE.md` >
`CLAUDE.md` > `docs/PAPER_CONTEXT.md` > the draft in `paper/`.

## Operating mode: autonomous
Work without waiting for approval. Ask the human only for **compute access
and credentials** (COMPUTE REQUEST format, `docs/AUTONOMY_PROTOCOL.md`).
Decide everything else by the rules in this file and in `ROLE.md`; log each
decision in `docs/DECISIONS_<role>.md`. Keep `docs/STATE_<role>.md` current
so a new session can resume from it. Never block on another role: use the
stated fallback (usually smoke data or a stub) and continue.

## Frozen decisions
- Labels = executed rule program on a structured state, relative to the rule
  text shown in the prompt. No LLM-written labels in any test set. Stated
  rules are test specifications, not clinical guidance.
- Record format, prompts and scoring conventions: `docs/INTERFACES.md`,
  implemented in `selrm/schema.py`, `selrm/prompts.py`, `selrm/metrics.py`.
- Local models: pointwise score u = logit("+") - logit("-") at the answer
  position; preference d = u(s) - u(s'). API models: log-probabilities when
  the provider returns them, otherwise the two-order choice prompt
  (same choice in both orders = decision; split or unparsable = tie).
- Triplet solved iff d(base) > 0, d(flip) < 0, d(near) > 0 on the conclusion
  claim. Ties are failures. Metrics: Rev, Hold, TA (primary), PresHold, MR at
  5% false rejection (threshold from dev), TieRate; by near-miss kind, tier,
  level (L0..L3-alt), family. 95% CIs: bootstrap over rules (1,000 reps),
  triplets kept together; paired bootstrap for comparisons; Holm over the
  primary comparisons.
- Dev for every choice (prompts, lambda, alpha, temperatures, checkpoints).
  Test once per system after the choice is frozen and logged.
- Never hand-type, estimate or invent a number. Every table cell comes from
  `results/<run_id>/summary.json` through `scripts/make_tables.py`. A missing
  result prints "not run".
- Verify every external identifier (models, datasets, library calls) against
  its live source; record ID, source and date in `configs/`. If it cannot be
  verified, skip the item and log it. Model names in the draft are
  placeholders; use what exists today.
- Backbone: `unsloth/Qwen3.5-9B` (verified 2 Oct), 16-bit LoRA r=64, 1 epoch,
  60k examples per run. Measured: about 0.44 steps/s at batch 64.

## Scope: what "the full v10 paper" contains
Run IDs are in `docs/RUN_MATRIX.csv` (312 rows; your rows in
`docs/RUN_MATRIX_<role>.csv`). Table-by-table mapping: `docs/PAPER_CONTEXT.md`
section 4.
- Rule tier (A): rule library (constraint, scoring, grammar-sampled rules;
  signature classes; folds), triplets with four near-miss kinds, presentation
  edits, missing twins, ladder L0 / L1 / L2 / L3-inv / L3-alt, hard tiers,
  rewritten-note tier, four training corpora, shortcut scorers.
- Table 2 audit (C): released PRMs, open judges, closed judges on rule
  triplets, MedEinst and key pairs.
- Table 3 factorial (B): 5 representations x 4 corpora x 5 seeds on L2.
- Table 4 transfer (B trains, C evaluates baselines and references): rule
  ladder, Hold, MR, MedEinst, key pairs, NLI4CT-P.
- Section 7.4 and Table 9 (B): decision bit, reader bottleneck, one-stage
  variant, field interventions, ablations, diversity curves, other backbones.
- Table 5 and Figure 3 (D): answer selection on MedQA and CareQA with the
  swapped-vignette control, step check, combined reward, selection pressure.
- Appendix (C, D): composition gap, shift analysis, sampling noise, input
  ablations, CondMedQA, policy training (GRPO), resources.
- Conditional on access: MedPRMBench (step-check training; fallback: released
  Med-PRM as step check), EHRNote-ChatQA (credentialed; never to APIs;
  default: not run), CondMedQA (only if released with general answers).

## Shared foundation (already written and tested; extend, do not fork)
| File | Status | Owner |
|---|---|---|
| `selrm/rules.py` | 11 pilot rules, applicability predicates | A |
| `selrm/mini_engine.py` | teammate's generator, 3 templates per form | A (to be replaced by `engine.py`) |
| `selrm/schema.py` | canonical record + `validate()` | A |
| `selrm/prompts.py` | frozen prompt builders | A |
| `selrm/smoke.py`, `scripts/make_smoke.py` | smoke data in the canonical schema, with held-out rules and templates | A |
| `selrm/metrics.py` | Rev/Hold/TA, bootstrap, paired difference | C |
| `scripts/validate_shortcuts.py` | passes on smoke data | A |
| `tests/test_foundation.py` | passes | all |
First command in every package: `python tests/test_foundation.py` and
`python scripts/make_smoke.py data/smoke_v2`. B, C and D develop against
`data/smoke_v2` until A publishes `rule_v1` in `data/REGISTRY.json`.

## Storage, adapters, GPU pool
- Shared Drive tree `selrm/{data,results,ckpt,cache,logs,adapters}`; write
  only your own run_ids. Adapters are about 230 MB each: a training job
  trains, evaluates on every registered test set, writes results, then
  deletes its adapter unless the run is listed in `configs/keep_adapters.json`
  (headline systems needed by C and D).
- Pooled GPU queue: runs with `pool=yes` may be executed by any role whose
  own queue is empty, highest priority first. Claim a run by creating
  `results/<run_id>/CLAIMED_<role>` before starting; skip runs that already
  have CLAIMED or DONE. Stale claims (no heartbeat file update for 3 hours)
  may be re-claimed.

## Autonomous decision rules (shared)
- Pilot (C, 4 Oct): 300 test triplets x 5 models. GO if the best model's TA
  on hard tiers is below 85% and at least 3 models are below 85% on Rev or
  Hold. NO-GO: A raises the hard-tier share to 60% and adds combined tiers,
  re-freeze as `rule_v2`, re-pilot once; then continue regardless and report
  the audit as found.
- Timeboxes: 3 hours per released checkpoint, 2 hours per failing API model,
  4 hours per blocked dependency; then drop, log, move on.
- API budget: `configs/budget.json`. If a run would exceed it: 1,000 triplets
  instead of 2,000 -> fewer API models -> drop the in-context extension.
- Schedule ladder (lead applies; everyone obeys): drop P3, then P2, then P1
  rows. Never drop: held-out test sets with passing shortcut validation; the
  four key cells {verdict, ledger2} x {blocks, triplets} with at least 3
  seeds; the audit with at least 8 signals; MedEinst zero-shot; MedQA
  selection with the swapped-vignette control.
- Results that contradict the hypotheses are reported; the claim changes,
  not the number.
