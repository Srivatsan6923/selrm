# STATE role B (maintained by Claude Code)
Updated: 2026-10-03 ~07:05 UTC (Sat). Plan: docs/FINAL_TASKS_B.md (3 Oct; replaces every earlier directive).
Run freeze: Wed 7 Oct 23:59 (UTC assumed). Decisions: docs/DECISIONS_B.md. Analyses: docs/ANALYSIS_B.md.

## P0 status
1. Analyses on existing predictions (docs/ANALYSIS_B.md, `python scripts/analysis_b.py > docs/ANALYSIS_B.md`): done
   (sections 1-9; B-AE-oracle-ledger, B-AE-field-edit, B-AE-field-swap DONE 05:53-06:00 UTC on H100s). Field
   edits that should change the verdict are followed in 47.8% (handoff 3 Oct). Left: the blocks half of the
   paired ledger-summary comparison after summary2 x blocks.
2. B-F-summary2-blocks-s0: training on an H100 runner since 06:00 UTC.
3. Core seeds 1-2 ({verdict, summary2, ledger2} x {blocks, triplets}): 12 runs; verdict x {blocks, triplets} s1-s2
   running since 06:08-06:38 UTC (A100, 2 x H100, L40); the rest queued (priority 20).
4. B-SC-summary2-triplets-s0 (format summary2_case: judge sees rule, case, prose, claim): queued (30), prep done.
5. LOKO {verdict, summary2, ledger2} x {subject, time, boundary}: 9 runs queued (40-42) on A's
   rule_v1/train_triplets_no_{kind} (aliases of train_triplets_lo_{kind}; lo_boundary built in the cluster 06:45 UTC,
   sha256 = A's); eval dev, test_L2, test_L0 (+ xr_v1/test).
6. New sets: xr_v1/test registered by A (efe0128) and restored on the PVC (sha256 = A's). Every not-started training
   run (except folds and diversity curves) now evaluates on it and keeps its adapter; kept adapters of finished runs
   get eval-only runs B-NS-xr_v1-<run> (configs/queues/v2/b_ns.json, priority 45). Summaries carry crossed accuracy
   (meta.xr.item). Runs claimed before 06:45 UTC (summary2 x blocks s0, verdict core seeds 1-2) need B-NS after
   they finish: `python scripts/submit_b.py pull` first, then `python scratch/regen_revised.py` (ns_eval reads
   results_git meta.json), push v2/b_ns.json, prep. challenge_v1, rewrite_v1, ec_v1: not registered yet.
   configs/adapters.json lists 6 kept adapters for C and D.

## Queue (configs/queues, pushed to /pvc/selrm/queues; priority from make_queue_b.py)
0 B-AE-* P0.1 -> 1 B-F-rationale-balanced-s0 (orphan claim, resumes) -> 10 summary2 x blocks -> 20 core seeds 1-2
-> 30 B-SC -> 40-42 LOKO -> 50 remaining seed 0 -> 55 core seeds 3-4 -> 60-70 ablations -> 72 FoVer -> 73 GenPRM
-> 76-77 folds -> 80-81 diversity -> 85 second backbone (Qwen3.5-4B; seeds 1-2 at 95) -> 92-99 unlisted rows.
45: B-NS eval-only runs on A's new sets. B-AB-conddrv-s0 (63) has min_gen 3 (runner code >= f179ade).

## GPUs held (07:05 UTC)
- Running: 4 x H100 (opportunistic; runner Jobs from 05:40 and 06:15 UTC, max 3 / 6 runs), 1 x A100, 1 x L40.
  Pending: 5 x A100, 2 x A40, 1 x A6000 (runner code 625e935), 3 x H100 (code 3b62811). A100 quota shared with C
  (B at most 6). 24 GB cards are not used: training peaks at 21-27 GB. H100 runs resume from their last 20-min
  checkpoint if preempted.
- Sync pod selrm-b-sync created ~03:00 UTC (6 h deadline): recreate before ~09:00 UTC (delete the Completed pod
  first, then sync-up).
- Never run two data jobs (build-data, restore-data) at once: each rewrites the PVC registry.

## Done (rule_v1 seed 0, provisional; docs/FACTORIAL_B_S0.md)
verdict x {natural, balanced, blocks, triplets}; rationale x {natural, blocks, triplets}; summary2 x triplets;
ledger2 x {blocks, triplets}; B-BB-qwen3.5-4b verdict x blocks; all B-C0 validation runs; B-T0 timing.

## P1 work without GPUs
- B-AB-conddrv-s0 (condition derived by the reader): format conddrv implemented, CPU self-test passes, queued
  (priority 63), prep OK.
- New sets from A (P0.6): check that their records carry gold ledgers before the reader formats are run on them
  (pretok check_gold requires one per (case, condition)); C's xr_v1 convention: selrm.metrics.crossed_accuracy.
- Premise gate: needs the step check (C/D). Probe re-weighting step 2 after its scores run.
- Medical-data rows, B-DIS: need C's clinical pairs.

## Before the tables
- Summaries written by runners on code before e86e9f7 carry CIs from the old bootstrap (process-dependent order;
  ~0.1 point): recompute every summary from its scores file with the final selrm/metrics.py before make_tables.
- Regenerate docs/PROJECTION_B.md once an H100 training run has finished (H100 speed is unmeasured until then).

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Until then kept adapters stay on the PVC.

## Blockers
- A: train_triplets_no_*, xr_v1, challenge_v1, rewrite_v1, ec_v1 (A's last commit 813e921: paused).
- Cluster: no free GPUs of B's types.
