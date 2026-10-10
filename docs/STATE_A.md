# STATE role A
Updated: Thu 8 Oct 2026. Plan of record: STAGE2_TASKS_A (8 Oct), with STAGE2_SPEC and STAGE2_ANALYSIS_PLAN
(bundle selrm_stage2_tasks.zip from the lead). It replaces FINAL_TASKS_A and NEXT_TASKS_A; the run freeze of
7 Oct is lifted. docs/ANALYSIS_PLAN_STAGE2.md is on main since b438812 (8 Oct); role-a carries the file but has not merged main (the merge is slow on this disk; let the lead merge).
API: OPENROUTER key works only with a lower-case 'sk-'; new-account limit of 20 requests a minute on DeepSeek V4 Pro (the rewrite jobs use it as an extractor).

## Stage 2 (do in this order)
| # | Item | Status |
|---|---|---|
| A1 | mcv_v1 (MedCalc-V) | **frozen 8 Oct** (3c0abf2): 19 of 19 scores; criteria_test 3,440 pairs, natural_band_test 394, edits_test 1,636 triplets after the fidelity filter (1,787 before), ruleside_test 295 crossed items, dev, adapt_blocks/adapt_triplets 12,000 records each. `python scripts/build_mcv_v1.py --restore`. Audit: docs/DATA_AUDIT_mcv_v1.md; author sheet audit/s2/mcv_edits_sheet.csv; keys in results/A-SETS |
| A2 | kb_v1 (DDXPlus criterion) | **frozen 8 Oct** (9236dd7): renderer, support check (data/kb_v1/SUPPORT.json), triplets_dev 5,138 and triplets_test 5,143 groups. `python scripts/build_kb_v1.py --restore`. Audit: docs/DATA_AUDIT_kb_v1.md; author sheet audit/s2/kb_criteria_sheet.csv |
| A3 | xp_v1 (program-preserving paraphrases) | **frozen 8 Oct**: 300 groups of test_L2, 0 program violations. `python scripts/build_xp_v1.py --restore` |
| A4 | onto_v1, cls_v1 | **frozen 9 Oct**: onto_v1 class tables (drug 47/12/21, phenotype 131/32/56, disease 141/37/54; drug-class change request approved by the user 9 Oct, plan line to be appended by D); cls_v1/dev (300 groups) and cls_v1/test (1,200 groups, 400 per domain). `python scripts/build_cls_v1.py --restore` |
| A5 | rule_v2 | **frozen 9 Oct**: engine selrm/engine2.py; train_blocks, train_triplets, lo_window, lo_class (60k records each), dev 300, test_L2 2,000; audit docs/DATA_AUDIT_rule_v2.md. `python scripts/build_rule_v2.py --restore --only <set>` |
| A6 | reg_v1 | not started |
| A7 | paper inputs from existing data | done 8 Oct: keys handed to D in docs/HANDOFFS.md (Table 8, harder set, Table 16, lines 1206 and 1499, Appendix E rule code); line 1512 waits for A6 |
| carry-over | rewrite_v1 and the _rw corpora (API key); challenge_v1 (H2); H1 aggregation | blocked as before |

External data live under data/_ext/ (git-ignored): medcalc/{test,train}_data.csv, medcalc/medcalc_v1_corrected.csv,
ddxplus/release_*.json and the patient zips. Pins and sha256 are in selrm/mcv/__init__.py and selrm/kb_criterion.py.

## Stage 1 (measured; sets stay frozen)

## Plan of record: NEXT_TASKS_A (3 Oct) and docs/AUX_PROTOCOL.md
NEXT_TASKS_A reprioritises FINAL_TASKS_A. Everything for AUX_PROTOCOL is a secondary analysis, labelled as
specified after the planned comparisons (4)-(6) failed. Run freeze: Wed 7 Oct 23:59 UTC. Not to start:
MedCalc-Bench, new rule families, rule_v2.

| # | Item | Status |
|---|---|---|
| 1 | rule_v1x/aux_blocks_20k, aux_triplets_20k | done, frozen (20,002 / 20,006 records, 1,881 shared groups; scripts/build_aux_corpora.py) |
| 2 | Negation phrase bank for C's medeinst_neg | done (selrm/negation_bank.py; handed to C) |
| 3 | rewrite_v1 (1,000 L2 groups) | ready, blocked on OPENROUTER_API_KEY (compute request #1) |
| 4 | rule_v1x/train_triplets_rw, train_blocks_rw (25% rewritten) | ready (scripts/rewrite_train.py, dry run passes), blocked on the same key |
| 5 | challenge_v1 (H2), ec_v1 (H3), H1 | waiting for the authors (package in Downloads/SelRM_author_tasks) |
| 6 | xr_v1 in two versions (400; 362 without the 38 known issues) | done in results/A-SETS and the appendix draft |
| 7 | Appendix B and C text from result keys | done: docs/drafts/appendix_BC_A.tex (82 keys, all resolve) |

When the key arrives: `python scripts/rewrite_tier.py --n 1000 --freeze`, then
`python scripts/rewrite_train.py --freeze`; report both acceptance rates and hand the sets to B and C.

## P0 status
1. **Audit of rule_v1: done.**
   - Outputs:
     - `docs/DATA_AUDIT_rule_v1.md`;
     - `docs/PAPER_VS_CODE.md`, checked against the lead's updated v13 (red items resolved; two
       non-red sentences corrected);
     - `tables/data_stats.json`, run at a clean commit (412a4d2);
     - `results/A-AUDIT`;
     - `data/rule_v1/{RULE_MANIFEST,RULE_SOURCES,KNOWN_ISSUES}.json`.
   - Re-executed check: 0 violations, coverage stated per check.
   - Regenerate with `python scripts/audit_rule_v1.py && python scripts/render_docs.py`.
2. **xr_v1: done and frozen.**
   - 400 items.
   - Known issues (38 items, to be reported with and without) and design notes:
     `data/xr_v1/KNOWN_ISSUES.json`.
   - `scripts/build_xr_v1.py --restore` writes the records.
3. **challenge_v1 kit: done.**
   - Forms: `challenge_v1/form_author{1..4}.md`; guide: `WRITING_GUIDE.md`.
   - The assembler checks each line; the second author approves the exact text by fingerprint.
   - Freeze after H2.
4. **Corpora for B: done.** `no_boundary` is new; the other five requested names are registry
   aliases.
5. **ec_v1: sign-off kit ready.**
   - 95 criteria from 85 trials, one group per near-miss kind: 235 groups, all shown in
     `ec_v1/SIGNOFF_CASES.md` (`ec_v1/prepare_summary.json`).
   - Sheet: `docs/EC_SIGNOFF.csv`. Each reviewer copies `docs/ec_signoff/TEMPLATE.csv` to
     `docs/ec_signoff/<authorN>.csv`; guide: `ec_v1/SIGNOFF_GUIDE.md`.
   - `python scripts/build_ec_v1.py freeze` needs at least two reviews per criterion, each of the
     current fingerprint; any no rejects. `restore` rewrites the frozen records in another clone.
6. **rewrite_v1: ready, blocked** on `OPENROUTER_API_KEY`. Rejected groups go to
   `data/rewrite_v1/rejected.jsonl`.

## P1
- Appendix B and C draft with result keys only: `docs/drafts/appendix_BC_A.tex` (73 keys, all
  resolve; includes the two new known issues).
- MedCalc-Bench: deferred. IDs are in `configs/medcalc_bench.json`; the code has no licence.
- Folds 2-3, diversity corpora, check code and reference graphs: done earlier.

## Open compute requests
- #1 (2 Oct): `OPENROUTER_API_KEY` for rewrite_v1, about $2-3.

## Human tasks prepared by A (order: H2 before H1 and H3, so writers do not see generated cases)
- **H2:** `challenge_v1/form_author{1..4}.md`.
  - Save as `challenge_v1/notes_<authorN>.md`, then run `python scripts/challenge_v1.py assemble`.
  - The second author writes `check_ok: yes <fingerprint>` (or `no <fingerprint>`) in the writer's
    file, from `challenge_v1/ASSEMBLY_REPORT.md`.
- **H1:** `audit/h1/sheet_author{1..4}.csv`, with the conventions in `audit/h1/README.md`.
  - Save a copy as `audit/h1/answers_<authorN>.csv` before typing; answer only there.
  - `python scripts/h1_aggregate.py` writes `results/A-H1`.
- **H3:** `docs/EC_SIGNOFF.csv` and every case in `ec_v1/SIGNOFF_CASES.md`; one review file per
  reviewer in `docs/ec_signoff/`.

## Notes for whoever resumes
- Commit as Srivatsan Sarvesan <srivatsan6923@gmail.com>, with no assistant trailers.
- rule_v1 and xr_v1 are frozen. Never regenerate or edit them; new sets get new names.
- Bash heredocs mangle backslashes. Edit Python files with the Edit tool, or build backslashes
  with `chr(92)`.
- Run the audit only at a clean tree. It records the commit and a modified-code flag.
- Do not re-run `build_ec_v1.py prepare` once review files exist in `docs/ec_signoff/`; it refuses
  unless forced, and a forced run voids every review whose fingerprint changes.
- Re-running `challenge_v1.py kit` keeps the group ids; any change to a group's written lines voids
  its approval.
