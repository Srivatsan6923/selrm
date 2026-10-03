# STATE role D (lead; maintained by the D session)
Updated: 2026-10-03 ~06:00 UTC (Fri 2 Oct, 23:00 PDT). Plan of record: FINAL_TASKS_D.md (repo root).

## Where D works
- Clone `D:/NAACL27/selrm-role-d` (github Srivatsan6923/selrm). Merges on `main`; D's work on `role-d`.
  `D:/selrm` is role A's working tree: never use it.
- Verified rule_v1 records (sha256 = registry) in `data/rule_v1/<eval set>/records.jsonl` (gitignored) and, all
  44 sets, in `D:/NAACL27/rule_v1_rebuild/` (outside git). LaTeX: tectonic at `D:/NAACL27/tools/tectonic.exe`.
- NRP (namespace ecepxie): PVC `selrm-d` (D, RW, mounted /pvc), B's PVC `selrm-b` read-only at /pvcb. Launcher
  `scripts/submit_d.py` (needs `export MSYS_NO_PATHCONV=1` in Git Bash). Env tarball `/pvc/env/selrm-d-env-v1.tar`
  (vllm 0.30.0, torch 2.13.0 cu130, transformers 5.18.0, peft 0.21.2). Sync pod `selrm-d-sync` (6 h max).

## Done
- P0.1 merge 1 (role-a 813e921, role-b f16af67, role-c edecf51 -> main 1a670f0); FINAL_TASKS + v13 in repo;
  docs/STATUS_BOARD.md (+ scripts/status_board.py); rule_v1 integrity (all 44 sets rebuild byte-identically).
- P0.2 scripts/make_tables.py: every v13 table + figure bodies + primary comparisons + per-seed table from
  results/ and results_git/; tables/numbers.tex, numbers.json, PROVENANCE.json; docs/RESULT_KEYS.md (key grammar,
  summary fields each role must write). Holm/p-values wait for C (CHANGE_REQUESTS).
- P0.3 scripts/update_paper.py (bodies + number macros only; prose check; sentence-change report; placeholder
  switch), scripts/build_paper.py (fails while placeholders remain; draft PDF in paper/build/). v13 wired with
  markers; new tables tab:primary and tab:seeds.
- P1 groundwork: configs/datasets_d.json (MedQA test/dev bigbio@484a6c0, CareQA_en HPAI-BSC@1d976cc, policy);
  scripts/make_pool.py, score_pool.py, merge_adapter.py, select_eval.py, download_model.py; tests/test_role_d.py.
  Merged ledger2-triplets and ledger2-blocks (B's s0 adapters) at /pvc/merged/<run_id>.

## In progress
- Workflow wf_1c25e335-14b: wiring v13 prose numbers to \res keys (proposals + 2 verifiers per chunk; apply after).
- Workflow wf_e31e6623-e81: error sheets (audit/), citation checklist (docs/CITATIONS_TODO.csv), timeline
  (docs/TIMELINE.md), length plan (docs/LENGTH_PLAN.md).
- NRP jobs (all pending for GPUs on a saturated cluster): pool smoke tests (a40, l40, a6000, 24gb x2),
  validation of the merged ledger model against B's test_L2 scores (l40, a6000, 24gb x2), Med-PRM download (CPU).

## Next
1. Apply the wiring proposals that both verifiers accept; rebuild; report hand-typed numbers that differ from
   results (e.g. bag-of-words TA is 7.0 in the result file, v13 says 7.1).
2. Review and commit the kits; publish via HANDOFFS; update the board.
3. When validation passes: pools medqa_dev, medqa_test, careqa_en; then score (medprm, medprm-swap,
   ledger2-triplets, ledger2-triplets-swap, ledger2-blocks) and run select_eval.py.

## Open compute requests
- none (NRP access works with the existing kubeconfig). GPU scarcity: 48 GB cards fully used tonight.

## Blockers
- Holm, paired p-values, MR and selection CIs wait for C's metrics (CHANGE_REQUESTS 2-3 Oct).
- Key-pair and MedEinst columns of Table 5 wait for C's clin_v1 sets (pairs must use configs/datasets_d.json MedQA).

## Schedule
- On time for P0. Run freeze Wed 7 Oct 23:59; final audit Sat 10 Oct.
