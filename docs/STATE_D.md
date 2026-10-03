# STATE role D (lead; maintained by the D session)
Updated: 2026-10-03 ~06:20 UTC (Sat). Plan of record: FINAL_TASKS_D.md (repo root).

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
- Workflow wf_e31e6623-e81: timeline (docs/TIMELINE.md) build, length plan (docs/LENGTH_PLAN.md) verification.
- NRP: pool smoke test (24 GB x2) running; validation of the merged ledger model against B's test_L2 scores
  pending (24gb, l40, a6000, a40: keep the first that finishes, delete the rest).

## Next
1. When validation passes (sign agreement with B's preferences, TA equal within noise): launch
   `k8s/pool_pipeline_d.sh` for medqa_dev, medqa_test, careqa_en (24 GB x2, tp 2); then select_eval.py; wire
   Table 5 / Fig. 3 right / App. G selection numbers (D-SEL-combined-product, -logistic exist as runs).
2. Daily merge 3; board; framing decision is the human lead's after C's TrialGPT report.
3. GRPO (P1, decide Mon 5 with the ladder; dropped first): env v2 + trl 1.14.1 (supports vllm <= 0.30.0);
   policy Qwen3.5-4B LoRA (ROLE.md; v13 text says 9B: change the text if run); prompts from train-rule triplets;
   rewards outcome / step check / ledger2-blocks / ledger2-triplets / reference graph (selrm/reference.py);
   evaluation by the rule program on test_L2 base/flip/near.

## Open compute requests
- none. If NRP stays saturated for the pools, ask for the Colab 96 GB GPU session (COMPUTE REQUEST).

## Blockers
- Table 5 key-pair and MedEinst columns: C's clin_v1 key pairs (asked to use configs/datasets_d.json MedQA rows)
  and MedEinst sets.

## Schedule
- P0 on time. Run freeze Wed 7 Oct 23:59; final audit Sat 10 Oct.
