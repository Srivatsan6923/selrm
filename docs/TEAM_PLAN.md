# TEAM PLAN: full v10 paper, 4 people, 1 GPU each (2-11 Oct 2026)

## Roles
| Role | Person owns | Package |
|---|---|---|
| A | Rule library, engine, every rule-tier dataset, shortcut scorers | selrm_pkg_A_data |
| B | All training: factorial, transfer rows, ablations, curves, backbones, step check | selrm_pkg_B_training |
| C | Metrics, judge harness, audit, training-free rows, references, clinical data, diagnostics, API budget | selrm_pkg_C_evaluation |
| D (lead) | Candidate pools, answer selection, policy training, tables, paper; merges, decisions | selrm_pkg_D_downstream_lead |

## Load and capacity
- Plan: 312 rows, about 300 GPU-hours (B 186, D 73, C 44); P0 alone is about
  65 GPU-hours. Four GPUs from 4 to 8 Oct give roughly 290 GPU-hours at 60%
  utilisation. P0 and P1 fit; P2 depends on utilisation. Estimates will be
  replaced by B's timing test.
- B's queue is the largest. Runs marked `pool=yes` are executed by any idle
  GPU (A's GPU is mostly free after the 3 Oct freeze). Claim protocol:
  docs/INTERFACES.md section 7.

## Critical path
A's freeze of `rule_v1` (Sat 3 Oct evening) -> B seed-0 grid and C pilot
(Sun 4 Oct) -> everything else. Nobody waits for it: B, C and D build and
test on `data/smoke_v2`, which already has held-out rules and templates.

## Day by day
| Day | A | B | C | D (lead) |
|---|---|---|---|---|
| Fri 2 | engine.py from mini_engine; rule library growth; tests | finetune + eval on smoke_v2 for all five formats; first smoke comparison blocks vs triplets | metrics extensions; judges harness; verify model IDs; download clinical data | repo + shared Drive; MedQA pool generation; merge plan |
| Sat 3 | grammar rules, classes, folds; **freeze rule_v1 core by evening** | timing test; train-then-eval job; step-check plan | local scoring + API harness tested; MedEinst blocks; MedPRMBench check | CareQA + MedEinst pools; calibration + selection code on smoke adapters |
| Sun 4 | ladder, hard tiers, missing twins | seed 0 of all 20 factorial cells (pooled) | **pilot + GO rule**; start audit | selection harness; table script skeleton |
| Mon 5 | folds 2-3, diversity sets, ablation corpora | key cells seeds 1-2; transfer rows; keep headline adapters | audit: released PRMs + API judges | calibration; selection with real adapters; GRPO environment |
| Tue 6 | rewritten-note tier; shortcut table; check-code + reference graphs | ablations; remaining seeds | training-free rows; references; key pairs, NLI4CT-P | GRPO runs; selection pressure |
| Wed 7 | statistics, 100-sample read, appendix text | diversity curves, backbones, folds | diagnostics; clinical evals of kept adapters | tables from finished runs. **Run freeze 23:59** |
| Thu 8 | appendix B, C text | appendix G training text | appendix D, F text | final tables; RESULTS_SUMMARY.md; claim decisions |
| Fri 9 - Sat 10 | review | review | review | paper rewrite; clean build |
| Sun 11 | | | | final audit; human read; submit |

## Coordination
- Daily 15-minute sync. Only numbers from `summary_*.json`.
- `docs/HANDOFFS.md` (append-only): date | from | to | what | path.
- `docs/CHANGE_REQUESTS.md`: anything touching a frozen interface.
- The lead applies the schedule ladder (CLAUDE.md) on Mon 5 and Wed 7.

## What can still stop a paper item (known today)
| Item | Risk | Fallback |
|---|---|---|
| Step-check PRM | MedPRMBench release not verified | released Med-PRM as step check |
| MedS3 PRM, ThinkPRM, GenPRM checkpoints | may not load | 3-hour timebox each; drop and say so |
| EHRNote-ChatQA | credentialed access | not run; wording restored to "untested" |
| CondMedQA | release not verified | not run |
| Rule-library size (v10 says 558) | implementation time | report what is built (minimum about 300 incl. grammar rules) |
| Audit headroom | frontier models may solve easy cases | hard tiers; GO rule |
