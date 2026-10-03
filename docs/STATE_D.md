# STATE role D (lead; maintained by the D session)
Updated: 2026-10-02 late evening (Fri). Plan of record: FINAL_TASKS_D.md (repo root).

## Where D works
- Clone `D:/NAACL27/selrm-role-d` (github Srivatsan6923/selrm). Merges on `main`; D's own work on `role-d`,
  merged into main at each daily merge. `D:/selrm` is role A's working tree: do not use it.
- Verified rule_v1 records (rebuilt, sha256 = registry) are in `data/rule_v1/<eval set>/records.jsonl`
  (gitignored) and, for every set incl. folds 2-3, in `D:/NAACL27/rule_v1_rebuild/` (outside git).

## Done
- P0.1 daily merge 1 (role-a 813e921, role-b f16af67, role-c edecf51 -> main); FINAL_TASKS files and v13 sources
  in the repo; docs/STATUS_BOARD.md (+ scripts/status_board.py for run counts); rule_v1 integrity checks
  (all 44 sets rebuild byte-identically); B's change requests answered, two filed (B test, C holm/p-values).

## In progress
- P0.2 scripts/make_tables.py (tables/*.tex, tables/numbers.tex, tables/PROVENANCE.json).

## Next
1. P0.2 make_tables.py from results/ and results_git/ (seeds listed, tbd for missing, provenance).
2. P0.3 update_paper.py on paper/latex_v13/main.tex (table bodies + number macros; sentence-change report;
   build fails on placeholders).
3. P0.4 kits (error sheets from B's per-example scores, citation checklist, git timeline); P0.5 length plan.

## Open compute requests
- none yet. P1 pools and GRPO need GPUs (NRP namespace ecepxie, as B; kubectl present on this machine).

## Blockers
- Holm and paired p-values wait for C's metrics (CHANGE_REQUESTS 2 Oct); tables print tbd meanwhile.
- No LaTeX on this machine: page counts come from the v13 PDF until a TeX build is set up.

## Schedule
- On time for P0.1. Run freeze Wed 7 Oct 23:59; final audit Sat 10 Oct.
