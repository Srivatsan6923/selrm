# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~09:10 UTC (Fri). Schedule: on time (B-C0 due today).

## Done
- First commands pass (test_foundation, make_smoke smoke_v2, validate_shortcuts PASS); kubectl works (context nautilus, ns ecepxie).
- B-C0 code: selrm/formats.py (5 formats, budget split, resampling, ledger check), scripts/pretok.py,
  scripts/finetune.py (unsloth + hf backends, resume, TRAINED marker), scripts/eval_local.py (verdict,
  rationale, two-stage reader->judge, malformed rule, padding self-check), scripts/train_eval_job.py
  (queue runner, claims/heartbeat/DONE, GPU monitor + watchdog), scripts/make_queue_b.py,
  scripts/submit_b.py (NRP launcher), scripts/nrp_status_b.py (Thanos checks), k8s/*.sh.
- CPU end-to-end self-test passes for all five formats (scripts/cpu_selftest_b.py; tiny random Qwen3.5).
- NRP: PVC selrm-b (rook-cephfs, 200 Gi) created; code snapshot pushed; queue b_smoke.json pushed.
- Research logged: NRP policy/storage/monitoring, Unsloth/Qwen3.5 pins, CUDA extension facts (docs/NRP_B.md).

## In progress
- CPU Job selrm-b-build-env-v1: env tarball (torch 2.11.0+cu130, unsloth 2026.9.14, transformers 5.5.0,
  trl 0.24.0, fla 0.5.2, causal-conv1d 1.7.0 compile).
- Adversarial review workflow of the pipeline (findings to fix before GPU runs).

## Next
1. prep Job (smoke_v2 rebuild + hash check, weights download, pretok b_smoke) -> 3 A100 runner Jobs on b_smoke
   (B-C0-smoke-verdict-{blocks,triplets}-s0, B-T0-<format> x5).
2. Pull results, generate the provisional smoke report for the lead (Rev/Hold/TA by near-miss kind), B-T0 table
   (s/step, tok/s, peak mem, GPU util mean/p10/windows<40 per format), update est_hours.
3. When rule_v1 is in data/REGISTRY.json: rebuild/verify it in-cluster, factorial seed-0 queue (20 cells).

## GPUs held
- none yet (CPU Jobs only).

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's.
  Workaround in use: code via the selrm-b-sync pod (small streams only).

## Blockers
- none.
