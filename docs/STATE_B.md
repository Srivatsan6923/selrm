# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~13:05 UTC (Fri). Schedule: ahead (rule_v1 frozen by A on Fri, not Sat; factorial running).

## Done
- B-C0 (code + NRP pipeline): selrm/{formats,runq}.py; scripts/{pretok,finetune,eval_local,train_eval_job,make_queue_b,
  submit_b,nrp_status_b,report_b,publish_adapters_b,cpu_selftest_b,render_checks,field_edits}.py;
  k8s/{build_env,stage,prep,build_data}.sh. CPU self-test passes (all formats incl. genprm, eval-only, all eval modes
  incl. verify / ledger_edit, concept, queue directory with a newer-format spec skipped).
- Smoke comparison (PROVISIONAL, never tabled) -> lead: docs/SMOKE_B_C0.md. B-T0 timing: docs/TIMING_B_T0.md.
- GPU validation of every ablation code path on smoke_v2 (60 steps, provisional): verdict_bt, ledger2_dec, program_bit,
  ledger2_verify, verify pass, concept scorer (TA ~0 by construction, DECISIONS_B), oracle ledger, ledger swap.
- rule_v1 (A's freeze e40789bd5d7a): all 38 sets (fold 1: 30, folds 2-3: 4 each) rebuilt in the cluster, sha256 equal
  to A's registry, published on the PVC; fold-1 also rebuilt on the laptop (30/30 match).

## In progress (NRP)
- Factorial seed 0 (20 runs, queue b_f_s0) + key cells seeds 1-2 (8 runs, b_f_key_s12): running on A100s since
  12:46 UTC (verdict x blocks, verdict x triplets, ledger2 x blocks first; ~1.2 h training per verdict run).
- Seed-0 extras queued behind the factorial (b_x_s0: 9 ablations, probe-rw step 1, 3 eval-only, 8 fold runs,
  13 diversity runs; b_tr_s0: FoVer transfer). Newer-code queues in queue/v2/: b_genprm_s0 (GenPRM-style verifier),
  b_x2_s0 (field edits).
- Runners: 8 A100 Jobs (4 running, 4 pending; the 4 pending are replaced with current code so v2 queues get a reader).

## Next
1. Commit + push the GenPRM / field-edit / queue-dir code; push v2 queues; prep; replace pending runners.
2. If A100 runners stay pending > 1 h (since 12:35): add 48 GB runners (rtxa6000 / l40 / a40), `runners all`.
3. First key-cell results (~14:30 UTC): pull, sanity-check dev/test_L2, then queue seeds 1-2 of the other cells.
4. Probe re-weighting step 2 after B-AB-probe-rw-s0-scores is DONE: scripts/probe_weights.py on CPU ->
   derived weights -> queue B-AB-probe-rw-s0 (pair_weights).
5. Publish kept adapters (HF secret, COMPUTE REQUEST #1), configs/adapters.json, HANDOFFS.
6. Clinical evaluation of PVC-kept adapters once C's eval_clinical.py and clin_v1 exist.

## GPUs held
- 4 x A100 (Missouri x2, SDSC, Great Plains) running; 4 A100 Jobs pending. Utilisation per run in meta.json;
  validation runs today 66-100%, no 5-min window < 40%.

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Workaround: code via the selrm-b-sync pod (small streams only).

## Blockers
- none. A100 contention (all A100 nodes full at 12:30) may slow the factorial; 48 GB overflow ready.
