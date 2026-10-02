# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~12:35 UTC (Fri). Schedule: ahead (rule_v1 frozen by A on Fri, not Sat; seed 0 queued).

## Done
- B-C0 (code + NRP pipeline): selrm/{formats,runq}.py; scripts/{pretok,finetune,eval_local,train_eval_job,make_queue_b,
  submit_b,nrp_status_b,report_b,publish_adapters_b,cpu_selftest_b}.py; k8s/{build_env,stage,prep,build_data}.sh.
  CPU self-test passes (5 formats + eval-only). 4-lens adversarial review: all confirmed findings fixed (DECISIONS_B).
- Smoke comparison (PROVISIONAL, never tabled) -> lead: docs/SMOKE_B_C0.md. Held-out rules at ceiling for both
  corpora (TA 99.7 blocks vs 100 triplets); dev (seen rules, held-out template): triplets - blocks TA +10.0
  [+1.9, +20.4], all of it Hold on numeric near-misses (45.1 vs 100).
- B-T0 timing (A100-80GB, 16x4): docs/TIMING_B_T0.md. All formats 82-91% mean GPU util, no 5-min window < 40%.
  Eval batches score 128 / generate 256. est_hours of all B-F rows in RUN_MATRIX_B from measurements.
- GPU validation of the ablation code paths on smoke_v2 (60 steps, provisional): verdict_bt (BT pairwise loss),
  ledger2_dec (decision field), program_bit (eval-only on a kept adapter) all ran end to end on A100, 66-83% util.
- rule_v1 (A's freeze e40789bd5d7a): rebuilt in the cluster and on the laptop, all 30 fold-1 sets match A's sha256,
  published on the PVC (/pvc/selrm/data, registry merged).

## In progress
- Factorial seed 0 (20 runs, b_f_s0) + key cells seeds 1-2 (8 runs, b_f_key_s12): queued, claims pushed
  (results_git/*/CLAIMED_B), pre-tokenisation Jobs running (claim order), 4 A100 runner Jobs submitted 12:30 UTC
  (max 4 runs each, 20 h deadline); scheduler: all A100 nodes full at submission -> pending.
- Validation queue 2 (b_val2: ledger2_verify, verify pass, concept scorer, oracle ledger, ledger swap) on 1 A100.
- Fold 2 rebuild (CPU Job); fold 3 after it (each updates the PVC registry, so one at a time).

## Next
1. Launch 4 more A100 runners once the key ledger2 cells are pre-tokenised (quota 9); if runners wait > 1 h for
   A100s, add 48 GB runners (rtxa6000 / l40 / a40) on the same queues (DECISIONS_B GPU-type policy).
2. Review the first key-cell results (dev, test_L2) for sanity; then queue seeds 1-2 of the other 16 cells and
   seeds 3-4 of the key cells (primary sets), ablations (P1) after.
3. Publish kept adapters (needs the HF secret confirmed, COMPUTE REQUEST #1), configs/adapters.json, HANDOFFS.
4. Delete validation adapters (B-C0-val-ledger2_dec, B-C0-val-ledger2_verify) once b_val2 is done.

## GPUs held
- 1 x A100 (SDSC node-1-3) for b_val2; 4 runner Jobs pending for A100. Today's runs so far: 82-91% mean util
  (B-T0), 66-83% (validation), no 5-min window < 40%.

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Workaround: code via the selrm-b-sync pod (small streams only).

## Blockers
- none. A100 contention may slow seed 0 (overflow to 48 GB cards ready).
