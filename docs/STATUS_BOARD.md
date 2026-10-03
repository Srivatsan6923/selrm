# STATUS BOARD (lead; updated at every merge)

Plan: `FINAL_TASKS_{A,B,C,D}.md` and `HUMAN_TASKS.md` (repo root) replace every
earlier directive. Statuses: not started / running / done / blocked (reason) /
dropped. Updated 2026-10-02 after merging role-a 813e921, role-b f16af67,
role-c edecf51 into main.

## Integrity checks (lead, at every merge)
| Check | Result | Evidence |
|---|---|---|
| rule_v1 sha256 unchanged since the freeze (e40789b) | pass: 38 frozen sets unchanged; 6 sets added later under new names (train_triplets_lo_*, train_dose_*), all frozen | `git show e40789b:data/REGISTRY.json` vs HEAD |
| No registry entry unfrozen | pass (44 of 44 frozen) | `data/REGISTRY.json` |
| Runs scored only on frozen sets | pass: B's runs list only frozen rule_v1 sets (plus smoke_v2 pipeline checks, never tabled); A's A-D14 scorers ran on rule_v1/test_L2 | `results_git/*/meta.json` eval_sets; `results/A-D14-*/meta.json` |
| Independent local rebuild of rule_v1 fold 1 matches the registry | see DECISIONS_D.md (rebuild 2 Oct) | `D:\NAACL27\rule_v1_rebuild` (outside git) |
| Test suite on main | 51 pass, 1 fails: tests/test_role_b.py::test_budget_and_balance (fails on role-b alone too; reported to B) | CHANGE_REQUESTS.md |

## Tasks
| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| A-P0.1 | Audit of rule_v1: manifest per rule, target-claim check, structure stats, overlap, L3-alt composition, requirements table, reviewers of the 450 groups, 300-group sample sheet, implemented semantics | A | not started (inputs exist: results/A-D15, docs/SAMPLE_TRIPLETS.md) | docs/DATA_AUDIT_rule_v1.md, tables/data_stats.json, data/rule_v1/KNOWN_ISSUES.json |
| A-P0.2 | xr_v1 rule-side items (2 rules x 3 cases; validation scorers solve 0) | A | not started | data/xr_v1/ + manifest + shortcut validation |
| A-P0.3 | challenge_v1 kit (160 groups, 32 per kind): specs, form, assembler, program labels, second-author field | A | not started | challenge_v1/ |
| A-P0.4 | Corpora for B: train_triplets_no_{subject,time,boundary}, train_triplets_nm{05,12,25} | A | partly exists under other names (rule_v1/train_triplets_lo_{subject,negation,time}, train_dose_{05,12,25}); boundary-held-out corpus not built | data/REGISTRY.json |
| A-P0.5 | ec_v1 registered eligibility criteria (test only), TrialGPT trials excluded, sign-off sheet | A | not started (needs C's TrialGPT IDs) | data/ec_v1/, docs/EC_SIGNOFF.csv (template) |
| A-P0.6 | rewrite_v1: model rewrites of L2 triplets, two-extractor acceptance, rejected = audit file | A | blocked (A's COMPUTE REQUEST #1: OPENROUTER_API_KEY); pipeline scripts/rewrite_tier.py ready | data/rewrite_v1/ |
| A-P1 | folds 2-3 + diversity corpora (done, frozen); check code + reference graphs (done: selrm/reference.py); MedCalc-Bench set (not run, A's decision); App. B, C text (not started) | A | partly done | selrm/reference.py, data/REGISTRY.json |
| B-P0.1 | Analyses on existing predictions (ledger-minus-summary paired diff, verdict check on records, program-supplied ledger 2x2, program on predicted ledger, macro-averages, natural/balanced Rev and near-miss, budget table, resampling flag, field interventions) | B | not started | docs/ANALYSIS_B.md |
| B-P0.2 | summary x blocks, seed 0 | B | not started (B paused 17:20 UTC) | results_git/B-F-summary2-blocks-s0 |
| B-P0.3 | Seeds 1-2: verdict, summary, ledger x {blocks, triplets} | B | queued before the pause (claims in results_git), not running | results_git/B-F-*-s{1,2} |
| B-P0.4 | Summary pipeline, judge also sees the case, x triplets | B | not started | results_git/ |
| B-P0.5 | Leave one near-miss kind out: {verdict, summary, ledger} x {subject, time, boundary} | B | partly queued (verdict, ledger2 x {subject, negation, time} claimed); summary and boundary not queued | results_git/B-LOKO-* |
| B-P0.6 | Evaluate kept and new adapters on xr_v1, challenge_v1, rewrite_v1, ec_v1; register adapters for C, D | B | waiting for A's sets; 4 key adapters of seed 0 registered | configs/adapters.json |
| B-P1 | Remaining factorial cells, seeds 3-4 of core cells, ablations, FoVer row, GenPRM-style verifier, medical-data rows, folds 2-3, diversity curves, second backbone, step check for D | B | partly claimed/queued before the pause; 14 rule_v1 runs done | docs/RUN_MATRIX_B.csv |
| C-P0.1 | TrialGPT criterion annotations: protocol first (docs/TRIALGPT_PROTOCOL.md), IDs to A, zero-shot scoring of 6-7 systems | C | not started | docs/TRIALGPT_PROTOCOL.md, docs/TRIALGPT_RESULTS.md |
| C-P0.2 | Untrained backbone on L2: direct verdict, prompted summary and ledger | C | verdict readout queued on B's runners as C-TF-critic (claimed, not run) | results_git/C-TF-critic |
| C-P0.3 | Metrics in selrm/metrics.py: clustered paired bootstrap, per-seed listing, macro-averages, crossed accuracy, near-miss decision metrics | C | not started | selrm/metrics.py |
| C-P0.4 | Adapters and baselines on xr_v1, challenge_v1, rewrite_v1, ec_v1 | C | waiting for A's sets | results/C-* |
| C-P0.5 | General-purpose trigger baseline (frozen tagger + program) | C | not started | results/C-DG-trigger* |
| C-P1 | Audit of 13 signals, training-free rows, MedEinst, key pairs, NLI4CT-P, clinical pairs for B, diagnostics | C | not started | docs/RUN_MATRIX_C.csv |
| D-P0.1 | Integration: daily merges, final-task files in root, this board, freeze/hash checks, framing decision after C's TrialGPT report | D | running (first merge done 2 Oct) | main, docs/STATUS_BOARD.md |
| D-P0.2 | Tables with provenance: make_tables.py, numbers.tex, PROVENANCE.json, seeds listed, paired tests + Holm from selrm.metrics | D | not started | scripts/make_tables.py, tables/ |
| D-P0.3 | Paper: v13 in paper/latex_v13, update_paper.py (table bodies + number macros only), build fails on placeholders | D | v13 sources added; script not started | paper/latex_v13/, scripts/update_paper.py |
| D-P0.4 | Author kits: error-analysis sheets (200 failures), citation checklist, development timeline | D | not started | audit/, docs/CITATIONS_TODO.csv, docs/TIMELINE.md |
| D-P0.5 | Length plan: about 10.5 pages to 8, no experiment removed | D | not started | docs/LENGTH_PLAN.md |
| D-P1 | Candidate pools, Table 5 selection, selection-pressure curve, GRPO policy training, resources table, final audit Sat 10 Oct | D | not started | docs/RUN_MATRIX_D.csv |
| H1 | Read 75 rendered groups each (300) from A's sample sheet | authors (all four) | not started (needs A-P0.1 sheet) | audit/fidelity_<name>.csv |
| H2 | Write 40 challenge cases each from A's specifications; second author checks | authors (all four) | not started (needs A-P0.3 kit) | challenge_v1/notes_<name>.jsonl |
| H3 | Sign off each registered criterion's program | two authors | not started (needs A-P0.5) | docs/EC_SIGNOFF.csv |
| H4 | Code 50 failures each (200) from D's sheet | authors (all four) | not started (needs D-P0.4 sheet) | audit/errors_<name>.csv |
| H5 | Open every cited paper; confirm title, authors, venue and attributed sentence | authors (split) | not started (needs D-P0.4 checklist) | docs/CITATIONS_CHECKED.csv |
| H6 | Write introduction, discussion, error analysis, development history | lead + one author | not started (Fri 9 - Sat 10) | paper/latex_v13/main.tex |
| H7 | Decide gates G1-G3 from the agents' numbers (definitions are the authors'; not written in the repo) | lead (human) | open (Sun 4, Wed 7) | docs/DECISIONS_D.md |
| H7a | Framing decision after C's TrialGPT report | lead (human) | waiting for C-P0.1 | docs/DECISIONS_D.md |
| H8 | Venue policy on AI assistance; complete the disclosure | lead (human) | not started (by Sat 10) | checklist |

## Runs by paper item (matrix rows; done = DONE file, claimed = CLAIMED_* without DONE)
<!-- BEGIN GENERATED: scripts/status_board.py -->

| paper item | owner | done | claimed | running | requested | todo | failed | dropped | in progress | queued | total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| - | B | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| - | D | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| AppB | A | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| AppC text tiers | A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| AppF | C | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 5 |
| AppG | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppG | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| AppG policy training | D | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 10 |
| AppG resources | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Fig3 left | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Fig3 left | B | 0 | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| Fig3 right | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Sec3 | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
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
| Tab3,Tab4 | B | 10 | 58 | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 100 |
| Tab4 | B | 0 | 6 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 15 |
| Tab4 | C | 0 | 1 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 7 |
| Tab4,AppG | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab5 | D | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 13 |
| Tab7 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab8 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab9 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab9,Sec7.4 | B | 0 | 14 | 0 | 0 | 2 | 0 | 0 | 0 | 4 | 20 |
| all tables | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| extension | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| new: leave one near-miss kind out | B | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| new: near-miss dose | B | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| paper | D | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 |
| pilot | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| **all** | | 30 | 177 | 1 | 0 | 84 | 0 | 32 | 1 | 4 | 329 |

<!-- END GENERATED -->
