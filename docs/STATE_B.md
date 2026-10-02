# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~15:05 UTC (Fri). Schedule: ahead (rule_v1 frozen by A on Fri; factorial running since 12:46).

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
- Factorial seed 0 (20 runs) + key cells seeds 1-2 (8): 2 DONE (verdict x blocks, verdict x triplets; provisional
  report docs/FACTORIAL_B_S0.md: L2 TA 58.2 vs 91.3, MR 100 both, shortcut scorers <= 54); running: ledger2 x blocks,
  ledger2 x triplets, verdict x natural, verdict x balanced, rationale x natural.
- Queued behind it: seed-0 extras (b_x_s0, b_tr_s0, v2/: genprm, field edits, backbones, probe re-weighting), then
  seeds 1-2 of the other 16 cells (b_f_s12) and of the fold runs (b_x_s12). Everything pre-tokenised.
- Runners: 5 x A100 running; 3 A100, 2 A40, 3 A6000, 3 L40 Jobs pending (all GPU types full); 2 of the 48 GB Jobs stage
  the backbone bases (Qwen3.5-4B, granite-4.1-8b) and take B-C0-val-{qwen4b,granite} first.
- Code review (5 reviewers + 2 skeptics per finding): 2 confirmed defects fixed before any run used them (field edits
  dropped verdict-changing numeric edits; runner capability check format-only), generator guard added.

## Next
1. ledger2 x blocks (~15:40) and ledger2 x triplets (~17:00): check malformed rate, L2, MR; regenerate the report.
2. Probe re-weighting step 2: after B-AB-probe-rw-s0-scores is DONE, `submit_b.py prep v2/b_probe_rw_s0.json`.
3. Publish kept adapters (HF secret, COMPUTE REQUEST #1), fill paths in configs/adapters.json, HANDOFFS.
4. Seeds 3-4 (P2) once seeds 1-2 are claimed; clinical evaluation of PVC-kept adapters when C's eval_clinical exists.
5. sync pod expires ~18:00 UTC: `submit_b.py sync-up` before pulls.

## GPUs held
- 5 x A100 (Missouri x2, Great Plains, SDSC x2). Finished runs: 94-95% mean GPU util (meta.json); Thanos 1 h means
  62-75% per pod incl. staging; the Great Plains pod idled ~25 min on a slow local disk before training (rising).

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Workaround: code via the selrm-b-sync pod (small streams only).

## Blockers
- none. A100 contention (all A100 nodes full at 12:30) may slow the factorial; 48 GB overflow ready.
