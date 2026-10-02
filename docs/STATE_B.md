# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~10:05 UTC (Fri). Schedule: on time (B-C0 due today).

## Done
- First commands pass; kubectl works (context nautilus, ns ecepxie). Clone: D:\NAACL27\selrm-role-b (role-b).
- B-C0 code: selrm/formats.py, selrm/runq.py, scripts/{pretok,finetune,eval_local,train_eval_job,make_queue_b,
  submit_b,nrp_status_b,report_b,cpu_selftest_b}.py, k8s/{build_env,stage,prep}.sh. CPU end-to-end self-test
  passes for all five formats. 4-lens adversarial review (23 agents): all confirmed findings fixed
  (DECISIONS_B 2 Oct entries); resampling now follows the draft's q(.|x).
- NRP: PVC selrm-b (rook-cephfs, 200 Gi); env v1 tarball built (torch 2.11.0+cu130, unsloth 2026.9.14,
  transformers 5.5.0, trl 0.24.0, peft 0.21.2, fla 0.5.2, causal-conv1d 1.7.0 compiled); smoke_v2 rebuilt in-cluster
  with matching hashes; unsloth/Qwen3.5-9B@005429c on the PVC; b_smoke pre-tokenised (tok/unsloth--Qwen3.5-9B/...).
- First A100 measurement (16x4, verdict, smoke): 3.0 s/step, GPU 100%, 22.6 GB, 1 CPU core, RSS 2.9 GiB.

## In progress
- 3 single-A100 runner Jobs on queue b_smoke (code d66bb6fa7d53): B-C0-smoke-verdict-{blocks,triplets}-s0 and
  B-T0-{verdict,rationale,summary2,value2,ledger2}.

## Next
1. Pull results, docs/SMOKE_B_C0.md (provisional, by near-miss kind) + HANDOFFS line to the lead; docs/TIMING_B_T0.md
   (s/step, tok/s, peak mem, GPU util mean/p10/windows<40 per format); update est_hours in RUN_MATRIX_B.
2. rule_v1: role A's builder is on role-a (scripts/build_rule_v1.py; registry has per-file sha256). When A freezes
   (Sat evening): rebuild in-cluster from A's commit, verify sha256, prep + factorial seed-0 queue (20 cells, n=60k).
3. B-PRM plan once C reports MedPRMBench status; B-TR-fover converter (FoVer IDs verified in configs/datasets_b.json).

## GPUs held
- up to 3 x A100 (Jobs selrm-b-run-b-smoke-a100-*), started ~10:00 UTC; utilisation per run in results/<run>/gpu_util.csv.

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's.
  Workaround in use: code via the selrm-b-sync pod (small streams only).

## Blockers
- none.
