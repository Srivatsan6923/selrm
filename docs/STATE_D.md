# STATE role D (lead; maintained by the D session)
Updated: 2026-10-03 ~07:35 UTC (Sat). Plan of record: FINAL_TASKS_D.md (repo root).

## Where D works
- Clone `D:/NAACL27/selrm-role-d` (github Srivatsan6923/selrm): D's work on `role-d`; publish with
  `git push origin role-d:main` (main = role-d + merges). Daily merges in a separate worktree
  (`git worktree add D:/NAACL27/selrm-merge main`; resolve append-only tables with `scripts/union_merge.py`,
  code conflicts in favour of the file's owner). `D:/selrm` is role A's tree: never use it.
- Verified rule_v1 records in `data/rule_v1/<eval set>/records.jsonl` (gitignored) and, all 44 sets of 2 Oct,
  in `D:/NAACL27/rule_v1_rebuild/`. LaTeX: tectonic at `D:/NAACL27/tools/tectonic.exe` (set TECTONIC).
- NRP (namespace ecepxie): PVC `selrm-d` (/pvc), B's PVC read-only (/pvcb). Launcher `scripts/submit_d.py`
  (`export MSYS_NO_PATHCONV=1` in Git Bash). Env `/pvc/env/selrm-d-env-v1.tar` (vllm 0.30.0, torch 2.13.0 cu130,
  transformers 5.18.0, peft 0.21.2). Sync pod `selrm-d-sync` (6 h max; recreate with sync-up). Merged ledger
  models `/pvc/merged/B-F-ledger2-{triplets,blocks}-s0`; Med-PRM `/pvc/models/dmis-lab--llama-3.1-medprm-reward-v1.0`.
  GPU jobs: `gpu NAME --gpu 24gb --n-gpu 2 ... --tp 2` (two 24 GB cards, tensor parallel) schedules fastest;
  48 GB cards were saturated on 3 Oct. vLLM needs VLLM_USE_FLASHINFER_SAMPLER=0 (set by the launcher).

## Done
- P0.1 merges 1-2 (main ec31d81 + lead commits); STATUS_BOARD; integrity checks (no rule_v1 hash change; all
  52 registry sets frozen; scored sets frozen); change requests answered/filed.
- P0.2 make_tables.py (keys, seeds, pooled CIs, C's paired_test/holm, MR, near-miss decisions, macro); tables/.
- P0.3 update_paper.py, build_paper.py; v13 wired: 185 numbers are keys (two reviewers per section); report of the
  4 rejected mappings and 317 numbers without a key: docs/PAPER_NUMBERS.md. Build fails while placeholders remain.
- P0.4 error sheets (audit/error_sheet*.csv, ERROR_CODING.md) and citation checklist (docs/CITATIONS_TODO.csv).
- P1: D-RES (results/D-RES); pool/scoring/selection code; tests/test_role_d.py.

## In progress
- Workflow wf_e31e6623-e81: verification of docs/TIMELINE.md (untracked until its verdict).
- NRP west: validation of the merged ledger model against B's test_L2 scores running on an opportunistic H100
  (selrm-d-validate-l2t-h100-11263) and staging on 2 x 24 GB (selrm-d-validate-l2t-24gb-9709): keep the first that
  finishes; acceptance criteria DECISIONS_D 3 Oct. Pool smoke tests pending (selrm-d-pool-smoke-24gb-9712, -l40-9972).
- NRP central (second site, us-central): PVC selrm-d-central, sync pod selrm-d-sync-c, mirror job
  selrm-d-mirror-central-12448 (env, code, adapters, validation records from the west; pinned base model and Med-PRM
  from Hugging Face; merges the two adapters there). Jobs there: `--site central`, paths /pvc/selrm/... instead of
  /pvcb/selrm/..., and the central merged copies are validated like the west ones before use.
- Lessons: cross-region CephFS reads ~5 MB/s (jobs require their PVC's region); vLLM needs
  VLLM_USE_FLASHINFER_SAMPLER=0; transformers 5 apply_chat_template(tokenize=True) returns a dict (tokenise the
  rendered text); argparse keeps '--' (the launcher strips it); a pod mounting the same PVC twice (rw + ro) hung in
  ContainerCreating (central mounts once); opportunistic H100s (priorityClassName opportunistic) are usable.

## Next
1. Validation passes -> pipelines (k8s/pool_pipeline_d.sh <pool> <tp>): medqa_dev (calibration; scorers medprm
   ledger2-triplets ledger2-blocks), medqa_test, careqa_en, medeinst_test (all five scorers); pull /pvc/pools and
   /pvc/scores (submit_d.py pull), run select_eval.py (--keypairs once C publishes them), make_tables, update_paper.
   Validation fails -> score with B's HF+PEFT code path (scripts/eval_local.Scorer) on smaller pools; log it.
2. When C publishes the MedQA key pairs: write /pvc/pools/medqa_test.extend.json (their qids) and run the pipeline
   with --ext (samples 16-63, scored as <scorer>.ext.jsonl) for Fig. 3 right.
3. Daily merge (worktree D:/NAACL27/selrm-merge), board, results summary; Mon 5: schedule ladder incl. the GRPO
   decision (scripts/grpo_d.py ready, env v2).

## Open compute requests
- none. If NRP stays saturated for the pools, ask for the Colab 96 GB GPU session (COMPUTE REQUEST).

## Blockers
- Table 5 key-pair and MedEinst columns: C's clin_v1 key pairs (asked to use configs/datasets_d.json MedQA rows)
  and MedEinst sets.

## Schedule
- P0 on time. Run freeze Wed 7 Oct 23:59; final audit Sat 10 Oct.
