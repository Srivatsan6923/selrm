# STATE role A
Updated: Sat 3 Oct 2026, evening. Working on FINAL_TASKS_A (P0 in order, then P1), plus the lead's
addendum of 2 Oct: `docs/PAPER_VS_CODE.md`; the paper follows the code; windows only in the new sets.
Three adversarial reviews ran on 3 Oct: one of every A deliverable (49 confirmed findings, 37 low) and
two of the three author kits (21 confirmed and 17 low; then 22 medium or high and 20 low). All are
addressed (`docs/DECISIONS_A.md`).

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
