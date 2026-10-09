# Red items of v14 and their owners

v14 has 215 `tbd` cells and 34 red notes. Each row below is closed by a
result file, or by a "not run" sentence the lead approves. Role D keeps this
file current (`docs/RED_CELLS.md`). Line numbers refer to
`paper/latex_v14/main.tex` of this pack.

## A. Stage 1: values that existing or queued runs supply (159 cells)

| Where | Cells | What is missing | Owner | Depends on |
|---|---|---|---|---|
| Table 2 (audit), ThinkPRM-14B | 4 | criterion-claim TA, XA, MedEinst, key pairs; merge of part 1 (local-only) | C | 12-hour GPU runs |
| Table 2, GenPRM-7B | 6 | Rev, Hold, TA, criterion-claim TA, XA (scores exist, summary not computed), key pairs | C | GPU |
| Table 2, default correction | 4 | Rev, Hold, criterion-claim TA, key pairs | C | stored scores |
| Table 2, prompted summary / ledger | 3 | MedEinst (both), key pairs (ledger) | C | 40 GB GPU |
| Table 2, generated program | 1 | criterion-claim TA | C | stored scores |
| Table 4 and Table 20 (transfer) | 94 | see the six rows below (84 in Table 20; 10 of them repeated in Table 4) | B, C | |
| -- prompted rows, default correction | 19 | L3-inv, TrialGPT, MedEinst, key pairs, NLI4CT-P | C | GPU |
| -- generated-program verifier | 1 | L3-inv | C | |
| -- FoVer data, rationale, natural, balanced, clinical pairs only | 44 | L3-inv (B) and every clinical column (C) | B, C | adapters registered |
| -- rule triplets + clinical pairs | 12 | whole row | B then C | `B-TR-tripclin-s0` |
| -- summary x blocks | 3 | key pairs, NLI4CT-P | C | |
| -- Ledger-RM blocks and triplets | 5 | MedEinst (blocks), NLI4CT-P (both) | C | running on 3 Oct |
| Table 8 (structure) | 12 | six statistics, train and L2 | A | `tables/data_stats.json` |
| Appendix C, harder set | 1 | counts per requirement | A | |
| Appendix D, TrialGPT | 1 | evidence-sentence precision and recall, ledger x triplets | C | stored outputs |
| Table 11 (NLI4CT-P) | 4 | Ledger-RM on triplets | C | running on 3 Oct |
| Table 16 (shortcuts) | 8 | Rev and Hold of four scorers | A | stored scores |
| Appendix G, shift classes | 1 | other signals | C | stored scores |
| Table 17 (kinds), caption | 1 | denominators; near-miss correct given base correct | C | stored scores |
| Table 19 (rule-side) | 9 | XA without the 38 known-issue items | B | stored scores |
| Table 21, premise gate | 4 | whole row | B | CPU |
| Table 23 (seeds) | 2 | summary x blocks seed 4, TA and XA | B | pull from cluster |
| Appendix H, budget | 1 | cases, targets, tokens, steps per configuration | B | |
| Appendix H, policy | 2 | analysis of the collapsed policy; two ledger rewards | D | runs of 3 Oct |
| Appendix H, diversity | 1 | curve over number of training rules | B | 39 queued runs |

## B. Stage 2: values from experiments not yet run (56 cells)

| Where | Cells | What | Owner | Task |
|---|---|---|---|---|
| Appendix E, rule code | 2 | scores accepted of 19; rows | A | A1 |
| Appendix E, text | 5 | MedCalc-V edits: backbone, blocks, triplets; adaptation with and without near-misses | C (B trains) | C3, B4 |
| Appendix E, text | 2 | windows without and with the date check | C | C6 |
| Appendix E, text | 2 | rule tier: rule removed; rule exchanged | C | C1 |
| Appendix E, text | 4 | class triplets: learned verdict, with member list, gate; linking accuracy | C | C5 |
| Appendix E, text | 2 | MedEinst executor: pair accuracy; share decided | C | C2 |
| Appendix E, text | 1 | key pairs: composite | C | C7 |
| Appendix E, text | 1 | rule paraphrase: excess rate of changed verdicts | C | C1 |
| Table 14 (ladder), MedCalc-V criteria and edits | 12 | critic none / stated; Ledger-RM-G none / stated / self / wrong | C | C3 |
| Table 14, registered criteria | 3 | critic stated; Ledger-RM-G stated / wrong | C | C6 |
| Table 14, TrialGPT | 2 | Ledger-RM-G stated / wrong | C | C6 |
| Table 14, class triplets | 5 | | C | C5 |
| Table 14, knowledge-base triplets | 6 | | C | C4 |
| Table 14, MedEinst | 5 | critic derived; Ledger-RM-G four conditions | C | C4, if G2 passes |
| Table 14, key pairs | 3 | Ledger-RM-G none / self / wrong | C | C7 |
| Appendix D, NLI4CT-P | 1 | eligibility-section slice | C | C9 |
| Not yet in the paper | -- | comparisons (7)-(12) table; MedCalc-V table; gate table | D (shells), C (values) | D3 |

Sections A and B sum to 215. Table 4 repeats 10 cells of Table 20 (prompted
summary 5, Ledger-RM 5); they are counted in both.

## C. Red notes (34)

| Line | Note | Closed by | Owner |
|---|---|---|---|
| 97, 200, 800, 854 | "not yet run" (abstract, contribution 3, Section 6.5, conclusion) | stage-2 results and the approved patches | D after G4 |
| 552, 595, 1915-1916 | larger open and closed judges not scored; the list of models | API key or 80 GB GPU; else "not scored" | C, lead |
| 556, 1001 | stage-2 plan registered; commit hash | plan commit | D0 |
| 841 | ledger-reward policy runs not finished | D5 | D |
| 986 | Holm correction over the stage-1 family | table script | D |
| 1070, 1100 | authors' reading of 300 groups pending | H1 | authors, A |
| 1072 | stage-2 tiers pending | stage-2 results | D |
| 1151 | fold-2 and fold-3 runs not collected | pull | B |
| 1206 | which value a measurement criterion uses | check against code | A |
| 1254-1255 | author-written cases; rewritten cases | H2; API key; else stays "not used" | authors, A |
| 1272, 1308 | TrialGPT label mapping; item set of the choice column | check against the evaluation script | C |
| 1369 | share of reader outputs with a long entry, not reproducible | recompute from stored outputs or delete | C |
| 1383 | the one-directional key-pair rule, in one sentence | from `docs/KEYPAIRS_RESULTS.md` | C |
| 1499 | held-out scores for adaptation | seeded rule of the plan | A |
| 1512 | count of usable Leaf criteria | A6 | A |
| 1590 | licence wording of each ontology | re-read at release | A, lead |
| 1861 | denominator pairs of the shift ratio | state them or drop the ratio | C |
| 2146 | learning rate and lambda | from the configuration | B |
| 2195 | policy model in the caption of Table 25 | confirm | D |
| 2200 | swapped rows identical | D6 | D |
| 2346 | development history from the authors' records | H6 | authors |
| 2377 | coding of 200 failures | H4 | authors |

## D. Closed (lead; each by a result file)

| Date | Item | Closed by |
|---|---|---|
| 8 Oct | Section 5 and Appendix A: stage-2 plan registered, commit hash (2 notes) | docs/ANALYSIS_PLAN_STAGE2.md, commit 733ad25 |
| 8 Oct | Section 6.6: ledger-reward policy runs (1 note) | results_git/D-RL-ledger2-{blocks,triplets}-s0 |
| 8 Oct | Appendix H, policy: analysis of the collapsed policy; two ledger rewards (2 cells) | results_git/D-RL-analysis, results_git/D-RL-ledger2-* |
| 8 Oct | Table 5 caption: Holm correction (1 note) | tables/PROVENANCE.json comparisons p1-p6b (padj) |
| 8 Oct | Table 23: summary x blocks seed 4, TA and XA (2 cells) | results_git/B-F-summary2-blocks-s4 |
| 8 Oct | Table 25 caption: policy model (1 note) | results_git/D-POOL-medqa_test/summary.json (policy.model) |
| 8 Oct | Table 25 caption: swapped rows identical (1 note) | results_git/D-SEL-combined-swap/summary_sel~*.json |

Result files that exist for cells still red (owners: add a HANDOFFS line with run id and cell, or the lead
wires them at the next pass): Table 8 structure (tables/data_stats.json, `structure`); TrialGPT evidence
precision and recall for ledger x triplets (55.6 / 67.9 in C's files); NLI4CT-P row of Ledger-RM on triplets
(C-NL-*); Table 21 premise gate (B-AE-premise-gate); Table 19 XA without the 38 known-issue items (computed by
make_tables, key `run/<prefix>/xr_v1:test/xa/XA362`); the share of long reader entries, now reproducible
(C: malformed_reasons_clin_v1~medeinst_test.json).
