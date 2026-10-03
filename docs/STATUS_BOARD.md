# STATUS BOARD (lead; updated at every merge)

Plan: `FINAL_TASKS_{A,B,C,D}.md` and `HUMAN_TASKS.md` (repo root) replace every earlier directive.
Statuses: not started / running / done / blocked (reason) / dropped.
Updated 2026-10-03 ~06:30 UTC after daily merge 2 (role-a 11f77f7, role-b 072d46d, role-c c7b5a09 -> main ec31d81).

## Integrity checks (lead, at every merge)
| Check | Result | Evidence |
|---|---|---|
| rule_v1 sha256 unchanged since the freeze (e40789b) | pass at merge 2: 38 frozen sets unchanged; 14 sets added later under new names (train_triplets_lo_*, _no_*, _nm*, train_dose_*, xr_v1/test), all frozen | `git show e40789b:data/REGISTRY.json` vs HEAD |
| No registry entry unfrozen | pass (52 of 52 in data/REGISTRY.json; clin_v1/trialgpt_{dev,test} frozen in data/clin_v1/REGISTRY_C.json with manifests and shortcut validation) | registries |
| Runs scored only on frozen sets | pass: every set named in results*/*/meta.json and summary_*.json is frozen (smoke_v2 runs are pipeline checks, never tabled) | DECISIONS_D 3 Oct |
| Independent rebuild of rule_v1 matches the registry | pass (2 Oct): all 44 sets of that day byte-identical | DECISIONS_D 2 Oct |
| Test suite on main | merge 2: 66 passed | pytest -q tests |
| Interface mismatch | B's scripts/analysis_b.py reads paired_test as a dict; C's returns a tuple | CHANGE_REQUESTS 3 Oct (owner B) |

## Tasks
| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| A-P0.1 | Audit of rule_v1 (manifest, target-claim check, structure, overlap, L3-alt, requirements, reviewers, 300-group sheet, semantics) | A | done (6966837: 0 target-claim violations) | docs/DATA_AUDIT_rule_v1.md, tables/data_stats.json, data/rule_v1/KNOWN_ISSUES.json |
| A-P0.2 | xr_v1 rule-side items | A | done: 400 items frozen, validation scorers XA 0, program XA 100 | data/xr_v1/ |
| A-P0.3 | challenge_v1 kit (160 groups) | A | done (kit); set frozen after the authors' notes (H2) | challenge_v1/ |
| A-P0.4 | Corpora train_triplets_no_{subject,time,boundary}, _nm{05,12,25} | A | done (no_boundary new; others registry aliases of identical frozen corpora) | data/REGISTRY.json |
| A-P0.5 | ec_v1 registered eligibility criteria | A | not started (C's TrialGPT exclusions now in configs/trialgpt_exclusions.json) | data/ec_v1/, docs/EC_SIGNOFF.csv |
| A-P0.6 | rewrite_v1 | A | blocked: A's COMPUTE REQUEST #1 (OPENROUTER_API_KEY) | data/rewrite_v1/ |
| A-P1 | folds, diversity corpora, check code, reference graphs (done); MedCalc-Bench (not run); App. B, C text | A | partly done | |
| B-P0.1 | Analyses on existing predictions | B | partly done (paired ledger-summary on triplets, verdict leakage, program on predicted ledger 99.4, macro, natural/balanced, budget, resampling); oracle-ledger, field edits wait for GPUs | docs/ANALYSIS_B.md |
| B-P0.2 | summary x blocks, seed 0 | B | queued (no free GPU) | results_git/B-F-summary2-blocks-s0 |
| B-P0.3 | Seeds 1-2: {verdict, summary, ledger} x {blocks, triplets} | B | queued (12 runs) | results_git/B-F-*-s{1,2} |
| B-P0.4 | Summary pipeline, judge sees the case, x triplets | B | queued (B-SC-summary2-triplets-s0) | results_git/ |
| B-P0.5 | Leave one near-miss kind out, 3 formats x {subject, time, boundary} | B | corpora now registered (A); queue to be built | results_git/B-LOKO-* |
| B-P0.6 | Kept and new adapters on xr_v1, challenge_v1, rewrite_v1, ec_v1 | B | xr_v1 available now; others wait for A | results_git/B-NS-* |
| B-P1 | rest of v10's training | B | queued after P0; conddrv reader implemented | docs/RUN_MATRIX_B.csv |
| C-P0.1 | TrialGPT: protocol, sets, zero-shot scoring | C | protocol and frozen sets done; dev scoring running (C-TG-*-dev) | docs/TRIALGPT_PROTOCOL.md, docs/TRIALGPT_RESULTS.md |
| C-P0.2 | Untrained backbone on L2 (verdict, prompted summary, prompted ledger) | C | running (C-TF-*) | results_git/C-TF-* |
| C-P0.3 | Metrics in selrm/metrics.py | C | done (paired_test, holm, MR, near-miss decisions, macro, XA, seed table, prf) | selrm/metrics.py |
| C-P0.4 | Baselines on xr_v1, challenge_v1, rewrite_v1, ec_v1 | C | xr_v1 available now | results_git/C-* |
| C-P0.5 | General-purpose trigger tagger + program | C | done: L2 TA 77.7 | results_git/C-SC-gptrigger |
| C-P1 | audit of 13 signals, clinical sets, diagnostics | C | not started; API key requested (C #1) | docs/RUN_MATRIX_C.csv |
| D-P0.1 | Integration (daily merges, board, freeze/hash checks, framing decision) | D | running: merges 1-2 done | main |
| D-P0.2 | make_tables.py with provenance, seeds, paired tests + Holm | D | done; specs follow the other roles' run ids (docs/RESULT_KEYS.md) | scripts/make_tables.py, tables/ |
| D-P0.3 | update_paper.py, build that fails on placeholders, v13 sources | D | done: 185 numbers wired to keys; report docs/PAPER_NUMBERS.md | scripts/update_paper.py, scripts/build_paper.py |
| D-P0.4 | Kits: error sheets, citation checklist, development timeline | D | error sheets and citation checklist done; timeline running | audit/, docs/CITATIONS_TODO.csv, docs/TIMELINE.md |
| D-P0.5 | Length plan to 8 pages | D | running | docs/LENGTH_PLAN.md |
| D-P1 | Pools, Table 5, selection pressure, GRPO, resources, final audit | D | code ready; NRP env built; merged ledger models being validated against B's scores; pool jobs wait for GPUs | scripts/make_pool.py, score_pool.py, select_eval.py |
| H1 | Read 75 rendered groups each (300) | authors | kit ready (A): audit/fidelity_author{1..4}.csv | audit/fidelity_<name>.csv |
| H2 | Write 40 challenge cases each; second author checks | authors | kit ready (A): challenge_v1/form_author{1..4}.md | challenge_v1/notes_<name>.jsonl |
| H3 | Sign off each registered criterion's program | two authors | waits for A-P0.5 | docs/EC_SIGNOFF.csv |
| H4 | Code 50 failures each (200) | authors | kit ready (D): audit/error_sheet_part{1..4}.csv, audit/ERROR_CODING.md | audit/errors_<name>.csv |
| H5 | Open every cited paper; confirm the attributed sentence | authors | kit ready (D): docs/CITATIONS_TODO.csv (63 keys, 13 flagged) | docs/CITATIONS_CHECKED.csv |
| H6 | Introduction, discussion, error analysis, development history | lead + one author | Fri 9 - Sat 10 | paper/latex_v13/main.tex |
| H7 | Decide gates G1-G3 (definitions are the authors'; not in the repo) | lead (human) | open (Sun 4, Wed 7) | docs/DECISIONS_D.md |
| H7a | Framing decision after C's TrialGPT report | lead (human) | waits for C-P0.1 test results | docs/DECISIONS_D.md |
| H8 | Venue policy on AI assistance; disclosure | lead (human) | by Sat 10 | checklist |

## Runs by paper item (matrix rows; done = DONE file, claimed = CLAIMED_* without DONE)
<!-- BEGIN GENERATED: scripts/status_board.py -->

| paper item | owner | done | claimed | running | requested | todo | failed | dropped | in progress | queued | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| - | B | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| - | D | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| AppB | A | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| AppC text tiers | A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| AppF | C | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 5 |
| AppF Tab shortcuts | C | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppG | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppG | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| AppG policy training | D | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 10 |
| AppG resources | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Fig3 left | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Fig3 left | B | 0 | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| Fig3 right | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Sec3 | C | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec3,AppC | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec3.2,AppD | C | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 8 |
| Sec5 | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec5 | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Sec6 | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Sec7.3, AppD | B | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 3 |
| Sec7.4 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec7.4 backbones | B | 1 | 23 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 24 |
| Tab10 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab2 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab2 | C | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 15 |
| Tab2,Tab4 (MR) | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab2,Tab5 | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab3 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab3 | B | 0 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 24 |
| Tab3,Tab4 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab3,Tab4 | B | 10 | 62 | 0 | 0 | 0 | 0 | 28 | 0 | 0 | 100 |
| Tab3,Tab9 | B | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab4 | B | 0 | 6 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 15 |
| Tab4 | C | 0 | 0 | 3 | 0 | 5 | 0 | 0 | 0 | 0 | 8 |
| Tab4,AppE | C | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| Tab4,AppG | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab5 | D | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 13 |
| Tab7 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab8 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab9 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab9, P0.5 | B | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 5 |
| Tab9,Sec7.4 | B | 1 | 15 | 0 | 0 | 2 | 0 | 0 | 0 | 4 | 22 |
| all tables | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| extension | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| new: leave one near-miss kind out | B | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| new: near-miss dose | B | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| paper | D | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| pilot | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| **all** | | 32 | 182 | 6 | 0 | 88 | 0 | 28 | 1 | 4 | 341 |

<!-- END GENERATED -->
