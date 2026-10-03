# STATE role A
Updated: Sat 3 Oct 2026, early morning. Working on FINAL_TASKS_A (P0 in order, then P1), plus the
lead's addendum of 2 Oct: `docs/PAPER_VS_CODE.md`; the paper follows the code; windows only in
the new sets.

## P0 status
1. **Audit of rule_v1: done.**
   - Outputs: `docs/DATA_AUDIT_rule_v1.md`, `docs/PAPER_VS_CODE.md`, `tables/data_stats.json`,
     `data/rule_v1/{RULE_MANIFEST,RULE_SOURCES,KNOWN_ISSUES}.json`.
   - Re-executed check: 0 violations over 16,200 groups.
   - Sources of the 103 hand-written rules were checked by model agents: 97 simplified, 6
     synthetic, 53 with a stated contradiction.
   - Reviewer disclosure: the 450 groups were read by 6 LLM sessions and no person
     (`audit/model_review/`).
   - H1 sheets: `audit/fidelity_author{1..4}.csv`.
   - Regenerate with `python scripts/audit_rule_v1.py && python scripts/render_docs.py`.
2. **xr_v1: done and frozen.**
   - 400 items: window, currency, subject, inclusivity.
   - Validation scorers all at XA 0; the program at XA 100.
   - Code: `selrm/xr.py`, `scripts/build_xr_v1.py` (`--restore` writes the records).
   - Change request filed for the new case kinds.
3. **challenge_v1 kit: done.**
   - 160 specifications in `challenge_v1/form_author{1..4}.md` with `WRITING_GUIDE.md`.
   - Assembler: `scripts/challenge_v1.py assemble`.
   - Freeze after H2.
4. **Corpora for B: done.**
   - `train_triplets_no_boundary` is new and frozen.
   - `no_subject`, `no_time` and `nm05/12/25` are registry aliases of `lo_*` and `dose_*`.
5. **ec_v1: sign-off sheet ready.**
   - Pipeline: 294 selected candidates; 108 confirmed by both skeptics; 6 rescued with the kinds the
     rejecting skeptic named; registry context checked (sub-items, sections) and duplicates removed.
   - Result: 100 criteria from 90 trials, 498 groups, shortcut validation PASS.
   - Outputs: `docs/EC_SIGNOFF.csv` for H3 (`ec_v1/SIGNOFF_GUIDE.md`), `ec_v1/EXCLUSIONS.csv`.
   - Next: run `python scripts/build_ec_v1.py freeze` once two authors have signed off.
6. **rewrite_v1: ready, blocked.**
   - `scripts/rewrite_tier.py` writes `rewrite_v1/test` plus the audit file
     `data/rewrite_v1/rejected.jsonl`.
   - Waits for `OPENROUTER_API_KEY` (compute request #1).

## P1 (after P0)
- Appendix B and C text from the audit.
- MedCalc-Bench as a separate named set, if time allows.
- Folds 2-3, diversity corpora, check code and reference graphs: already registered or done.

## Open compute requests
- #1 (2 Oct): `OPENROUTER_API_KEY` for rewrite_v1, about $2-3.

## Human tasks prepared by A
- H1: `audit/fidelity_author{1..4}.csv`.
- H2: `challenge_v1/form_author{1..4}.md`.
- H3: `docs/EC_SIGNOFF.csv` (100 rows) with `ec_v1/SIGNOFF_GUIDE.md`.

## Notes for whoever resumes
- Commit as Srivatsan Sarvesan <srivatsan6923@gmail.com>, with no assistant trailers.
- rule_v1 is frozen. Never regenerate or edit it; new sets get new names.
- Bash heredocs mangle backslashes. Edit Python files with the Edit tool.
