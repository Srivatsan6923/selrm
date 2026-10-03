# STATUS BOARD (lead; updated at every merge)

Plan: `FINAL_TASKS_{A,B,C,D}.md` and `HUMAN_TASKS.md` (repo root) replace every earlier directive.
Statuses: not started / running / done / blocked (reason) / dropped.
Updated 2026-10-03 ~17:10 UTC after merge 5 (main 3202740: 123 tests pass; rule_v1 hashes unchanged; scored sets frozen; key cells at 5 seeds).

## Integrity checks (lead, at every merge)
| Check | Result | Evidence |
|---|---|---|
| rule_v1 sha256 unchanged since the freeze (e40789b) | pass at merge 5: 38 frozen sets unchanged; 14 sets added later under new names, all frozen | docs/FINAL_AUDIT.md check 1 |
| No registry entry unfrozen | pass (52 of 52 in data/REGISTRY.json; 16 of 16 in data/clin_v1/REGISTRY_C.json) | registries |
| Runs scored only on frozen sets | pass at merge 4: every set named in results*/*/summary_*.json is frozen; variant files (field edits and swaps, no-case, lenient readout) score frozen sets | DECISIONS_D 3 Oct |
| Independent rebuild of rule_v1 matches the registry | pass (2 Oct): all 44 sets of that day byte-identical | DECISIONS_D 2 Oct |
| Test suite on main | merge 5: 123 passed | pytest -q tests |
| Interface mismatch | resolved: B's analysis_b.py unpacks C's paired_test tuple | scripts/analysis_b.py:48 |
| Paper claim without a record | v13 App. H says the pilot model solved 59.7% on held-out rules where a past or family finding counts; no file records that test or value, and the pilot-generator data contain no case in which such a mention counts. The first dataset build (old repo c965184) already had such flips (135 of 2,000 test flips) and presentation edits, so App. H's "What changed" also needs the authors' records. The authors produce the record or remove the claims (H6) | docs/TIMELINE.md, 'Not in the records' 1-7 |
| Tooling markers in committed files | open: 'ponytail:' comment tags in selrm/rules_constraint.py:127 (A), scripts/eval_local.py:66 (B), scripts/eval_c.py:49 and scripts/prms/genprm.py:62,118,216 (C); a tooling note in the first line of docs/STATE_B.md and docs/STATE_C.md; commit c80a9a4 (status site, a teammate's) carries a co-author trailer: rewriting published history is the human lead's decision (H8) | CHANGE_REQUESTS 3 Oct; docs/FINAL_AUDIT.md check 9 |
| Hand-typed number differing from its result | bag-of-words TA: v13 7.1, results/A-D14-bag_of_words 7.0 (now read from the result) | docs/PAPER_NUMBERS.md |

## Tasks
| ID | Task | Owner | Status | Output |
|---|---|---|---|---|
| A-P0.1 | Audit of rule_v1 (manifest, target-claim check, structure, overlap, L3-alt, requirements, reviewers, 300-group sheet, semantics) | A | done (6966837: 0 target-claim violations) | docs/DATA_AUDIT_rule_v1.md, tables/data_stats.json, data/rule_v1/KNOWN_ISSUES.json |
| A-P0.2 | xr_v1 rule-side items | A | done: 400 items frozen, validation scorers XA 0, program XA 100 | data/xr_v1/ |
| A-P0.3 | challenge_v1 kit (160 groups) | A | done (kit); set frozen after the authors' notes (H2) | challenge_v1/ |
| A-P0.4 | Corpora train_triplets_no_{subject,time,boundary}, _nm{05,12,25} | A | done (no_boundary new; others registry aliases of identical frozen corpora) | data/REGISTRY.json |
| A-P0.5 | ec_v1 registered eligibility criteria | A | sign-off kit ready: 95 criteria from 85 trials, 235 groups (one per near-miss kind); frozen after two authors sign off (H3) | ec_v1/SIGNOFF_CASES.md, docs/EC_SIGNOFF.csv, docs/ec_signoff/ |
| A-P0.6 | rewrite_v1 | A | blocked: A's COMPUTE REQUEST #1 (OPENROUTER_API_KEY) | data/rewrite_v1/ |
| A-P1 | folds, diversity corpora, check code, reference graphs (done); App. B, C draft with result keys (done, 73 keys); MedCalc-Bench deferred (its code has no licence) | A | partly done | docs/drafts/appendix_BC_A.tex |
| B-P0.1 | Analyses on existing predictions | B | done (sections 1-15 incl. oracle ledger, field edits, seed-pooled ledger-summary on blocks and triplets) | docs/ANALYSIS_B.md |
| B-P0.2 | summary x blocks, seed 0 | B | done (L2 TA 67.3) | results_git/B-F-summary2-blocks-s0 |
| B-P0.3 | Seeds 1-2: {verdict, summary, ledger} x {blocks, triplets} | B | done; the four key cells now have seeds 0-4 | results_git/B-F-*-s{1..4} |
| B-P0.4 | Summary pipeline, judge sees the case, x triplets | B | done (L2 TA 98.8 vs 98.0 case-blind) | results_git/B-SC-summary2-triplets-s0 |
| B-P0.5 | Leave one near-miss kind out, 3 formats x {subject, time, boundary} | B | done (9 runs; ANALYSIS_B section 10) | results_git/B-LOKO-* |
| B-P0.6 | Kept and new adapters on xr_v1, challenge_v1, rewrite_v1, ec_v1 | B | xr_v1 done for 23 runs (XA: triplets-trained 88.5-92.8, blocks-trained 47.2-80.2); the other sets wait for A | results_git/B-NS-* |
| B-P1 | rest of v10's training | B | running: Table 9 rows, value ledger, FoVer, GenPRM, clinical-pairs runs (B-TR-clinonly, B-TR-tripclin, B-DIS); folds, diversity, second backbone queued | docs/RUN_MATRIX_B.csv |
| C-P0.1 | TrialGPT: protocol, sets, zero-shot scoring | C | done: test portion of nine systems scored once, report independently recomputed; comparison (6) not supported | docs/TRIALGPT_RESULTS.md, results_git/C-TG-* |
| C-P0.2 | Untrained backbone on L2 (verdict, prompted summary, prompted ledger) | C | critic done (L2 TA 27.1 [21.5, 33.6]); default correction done; prompted ledger and summary running in parts | results_git/C-TF-*, docs/RESULTS_C.md |
| C-P0.3 | Metrics in selrm/metrics.py | C | done (paired_test, holm, MR, near-miss decisions, macro, XA, seed table, prf) | selrm/metrics.py |
| C-P0.4 | Baselines on xr_v1, challenge_v1, rewrite_v1, ec_v1 | C | xr_v1: critic XA 39.0 (42.5 without A's known issues); other sets wait for A | results_git/C-* |
| C-P0.5 | General-purpose trigger tagger + program | C | done: L2 TA 77.7 | results_git/C-SC-gptrigger |
| C-P1 | audit of 13 signals, clinical sets, diagnostics | C | running: released-PRM audit (Med-PRM, FoVer, MedS3; ThinkPRM pending), MedEinst / key pairs / NLI4CT-P runs; diagnostics (shift, sampling noise) done; API judges wait for C #1 | docs/RUN_MATRIX_C.csv, results_git/C-* |
| D-P0.1 | Integration (daily merges, board, freeze/hash checks, framing decision) | D | running: merges 1-5 done (main 3202740, 123 tests); key-pair decision | main, docs/DECISIONS_D.md |
| D-P0.2 | make_tables.py with provenance, seeds, paired tests + Holm | D | done; specs follow the other roles' run ids (docs/RESULT_KEYS.md) | scripts/make_tables.py, tables/ |
| D-P0.3 | update_paper.py, build that fails on placeholders, v13 sources | D | done: 185 numbers wired to keys; report docs/PAPER_NUMBERS.md | scripts/update_paper.py, scripts/build_paper.py |
| D-P0.4 | Kits: error sheets, citation checklist, development timeline | D | done: timeline has 49 rows checked against git and file times, and the draft statements the records do not support | audit/, docs/CITATIONS_TODO.csv, docs/TIMELINE.md |
| D-P0.5 | Length plan to 8 pages | D | done (proposal): 20 moves take the main text from 10.9 to 7.9 pages in a trial build, no experiment removed; the authors apply it (H6) | docs/LENGTH_PLAN.md, tools/length_plan/ |
| D-P1 | Pools, Table 5, selection pressure, GRPO, resources, final audit | D | running: Table 5 and Fig. 3 right measured with the rule-only ledger (T5 not supported, docs/RESULTS_SUMMARY.md); switch to the clinical-pairs ledger ready for when B-TR-tripclin-s0 ends; GRPO: step-check reward exploited (held-out pairs 89.3 -> 37.3), outcome 97.3, ledger rewards wait for 2-GPU slots; final audit script | results_git/D-*, docs/FINAL_AUDIT.md |
| H1 | Read 75 rendered groups each (300) | authors | kit ready (A): audit/fidelity_author{1..4}.csv | audit/fidelity_<name>.csv |
| H2 | Write 40 challenge cases each; second author checks | authors | kit ready (A): challenge_v1/form_author{1..4}.md | challenge_v1/notes_<name>.jsonl |
| H3 | Sign off each registered criterion's program | two authors | waits for A-P0.5 | docs/EC_SIGNOFF.csv |
| H4 | Code 50 failures each (200) | authors | kit ready (D): audit/error_sheet_part{1..4}.csv, audit/ERROR_CODING.md | audit/errors_<name>.csv |
| H5 | Open every cited paper; confirm the attributed sentence | authors | kit ready (D): docs/CITATIONS_TODO.csv (63 keys, 13 flagged) | docs/CITATIONS_CHECKED.csv |
| H6 | Introduction, discussion, error analysis, development history; statements the results contradict (docs/CLAIMS_AUDIT.md: 98 contradicted, 50 partly, 34 placeholders with no result planned) | lead + one author | Fri 9 - Sat 10 | paper/latex_v13/main.tex, docs/CLAIMS_AUDIT.md |
| H7 | Gates: decided by the human lead's NEXT_TASKS bundle (DECISIONS_D 3 Oct: transfer claim withdrawn; typed-ledger headline gate not met; near-miss generalisation reported as found); the lead confirms | lead (human) | confirm | docs/DECISIONS_D.md |
| H7a | Framing decision | lead (human) | done: NEXT_TASKS_D contributions (test and audit; near-miss supervision; separate evidence reading with the judge seeing the case; behaviour as a training reward); transfer and selection reported as negative | NEXT_TASKS_D.md, docs/DECISIONS_D.md |
| H8 | Venue policy on AI assistance; disclosure; whether to rewrite commit c80a9a4's co-author trailer | lead (human) | by Sat 10 | checklist, docs/FINAL_AUDIT.md |

## Runs by paper item (matrix rows; done = DONE file, claimed = CLAIMED_* without DONE)
<!-- BEGIN GENERATED: scripts/status_board.py -->

| paper item | owner | done | claimed | running | requested | todo | failed | dropped | blocked | deferred | in progress | kit done | queued | sign-off sheet ready | total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| - | B | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| - | D | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| AppB | A | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| AppB,AppC,Sec3.1 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppC | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppC text tiers | A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| AppF | C | 3 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| AppF Tab shortcuts | C | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppG | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppG | D | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| AppG policy training | D | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| AppG resources | D | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Fig3 left | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Fig3 left | B | 0 | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| Fig3 right | D | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec3 | C | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec3,AppC | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec3.1,AppC | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| Sec3.2,AppD | A | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Sec3.2,AppD | C | 5 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Sec5 | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec5 | D | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec6 | C | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sec7.3, AppD | B | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Sec7.4 | A | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Sec7.4 backbones | B | 1 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 24 |
| Tab10 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab2 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab2 | C | 1 | 0 | 3 | 0 | 7 | 0 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 15 |
| Tab2,Tab4 (MR) | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab2,Tab5 | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab3 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab3 | B | 0 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 24 |
| Tab3,Tab4 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab3,Tab4 | B | 43 | 29 | 0 | 0 | 0 | 0 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 100 |
| Tab3,Tab4 (new sets) | B | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Tab3,Tab9 | B | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab4 | B | 0 | 12 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| Tab4 | C | 2 | 0 | 3 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 8 |
| Tab4,AppE | C | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Tab4,AppG | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab5 | D | 9 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 |
| Tab7 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab8 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab9 | A | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Tab9, P0.5 | B | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Tab9,Sec7.4 | B | 14 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 22 |
| all tables | D | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| extension | C | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| new: leave one near-miss kind out | B | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| new: near-miss dose | B | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| paper | D | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| pilot | C | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **all** | | 126 | 132 | 11 | 0 | 28 | 0 | 36 | 3 | 12 | 1 | 1 | 2 | 1 | 353 |

<!-- END GENERATED -->
