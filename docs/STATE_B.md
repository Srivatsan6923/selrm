# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~11:50 UTC (Fri). Schedule: on time (B-C0 and B-T0 done on day 1).

## Done
- B-C0 (code + NRP pipeline): selrm/{formats,runq}.py; scripts/{pretok,finetune,eval_local,train_eval_job,make_queue_b,
  submit_b,nrp_status_b,report_b,publish_adapters_b,cpu_selftest_b}.py; k8s/{build_env,stage,prep,build_data}.sh.
  CPU self-test passes (5 formats + eval-only). 4-lens adversarial review: all confirmed findings fixed (DECISIONS_B).
- Smoke comparison (PROVISIONAL, never tabled) -> lead: docs/SMOKE_B_C0.md. Held-out rules at ceiling for both
  corpora (TA 99.7 blocks vs 100 triplets); dev (seen rules, held-out template): triplets - blocks TA +10.0
  [+1.9, +20.4], all of it Hold on numeric near-misses (45.1 vs 100).
- B-T0 timing (A100-80GB, 16x4): docs/TIMING_B_T0.md. All formats 82-91% mean GPU util, no 5-min window < 40%.
  Eval batches score 128 / generate 256 (rationale eval 431 s vs 717 s at 64/64). est_hours of all B-F rows in
  RUN_MATRIX_B from measurements (seed 0 of 20 cells ~53 GPU-h with full-ladder eval).
- Verified on role A's real rule_v1 format (1% build of role-a): registry paths, gold-ledger checks, all 20 cells
  pre-tokenise; queue runner trains+evaluates all 10 eval sets (missing sets: no CI, scores kept for C's MR).
- NRP: PVC selrm-b; env v1 tarball; weights unsloth/Qwen3.5-9B@005429c; runner = 2 CPU / 12 Gi / A100.

## In progress
- nothing on GPUs (all runner Jobs exited by themselves when their queues were empty).

## Next
1. When A freezes rule_v1 (target Sat 3 Oct 18:00, A's registry carries sha256): `submit_b.py push-ref <A commit>`,
   `build-data <sha12>` (CPU rebuild + sha256 check + publish), `make_queue_b.py factorial b_f_s0.json --seeds 0`,
   push-queue (marks CLAIMED_B in results_git; commit+push), prep, runners (n = min(20, free A100s, quota 9)).
2. Then key cells seeds 1-2 (8 runs, full ladder), publish kept adapters (after the HF secret is confirmed), B-REG.
3. P1 code while waiting: B-TR-fover converter (IDs in configs/datasets_b.json), GenPRM-style check code (A-D13
   selrm/reference.py on role-a), ablation variants (decision field, bit-only, pairwise BT loss, change loss,
   conclusion-only, concept scorer, probe re-weighting), eval-only analyses (oracle ledger, field interventions).

## GPUs held
- none (last runner exited 11:33 UTC). Peak today: 3 x A100 (Missouri, Great Plains, SDSC) 10:00-11:33 UTC,
  GPU util 82-91% per run (meta.json), RSS 0.24 of request, CPU 0.5 of request.

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Workaround: code via the selrm-b-sync pod (small streams only).

## Blockers
- none (rule_v1 expected Sat 18:00; smoke fallback not needed yet).
