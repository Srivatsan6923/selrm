# STATE role B (maintained by Claude Code)
Updated: 2026-10-03 ~10:45 UTC (Sat). Plan: docs/FINAL_TASKS_B.md (3 Oct; replaces every earlier directive).
Run freeze: Wed 7 Oct 23:59 (UTC assumed). Decisions: docs/DECISIONS_B.md. Analyses: docs/ANALYSIS_B.md.

## P0 status
1. Analyses on existing predictions (docs/ANALYSIS_B.md, `python scripts/analysis_b.py > docs/ANALYSIS_B.md`): done
   (sections 1-9; B-AE-oracle-ledger, B-AE-field-edit, B-AE-field-swap DONE 05:53-06:00 UTC on H100s). Field
   edits that should change the verdict are followed in 47.8% (handoff 3 Oct). Left: the blocks half of the
   paired ledger-summary comparison after summary2 x blocks.
2. B-F-summary2-blocks-s0: DONE (L2 TA 67.3); paired ledger-summary on blocks in ANALYSIS_B section 1.
3. Core seeds 1-2: DONE verdict x blocks s1-s2, verdict x triplets s1, summary2 x blocks s2, summary2 x triplets
   s1-s2, ledger2 x blocks s1; running (09:10 UTC) verdict x triplets s2 (L40), summary2 x blocks s1 (A6000), ledger2 x
   blocks s2 (A100), ledger2 x triplets s1-s2 (H100). Blocks cells vary a lot across seeds (handoff 3 Oct).
4. B-SC-summary2-triplets-s0: DONE (L2 TA 98.8 vs 98.0 blind; ANALYSIS_B section 11).
5. LOKO {verdict, summary2, ledger2} x {subject, time, boundary}: subject x 3 and time x verdict DONE
   (ANALYSIS_B section 10); the rest queued or running (40-42).
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
- Sync pod selrm-b-sync started 08:10 UTC (6 h deadline): recreate before ~14:00 UTC (`kubectl -n ecepxie delete pod
  selrm-b-sync`, then `python scripts/submit_b.py sync-up`).
- Never run two data jobs (build-data, restore-data) at once: each rewrites the PVC registry.

## Done (rule_v1 seed 0, provisional; docs/FACTORIAL_B_S0.md)
verdict x {natural, balanced, blocks, triplets}; rationale x {natural, blocks, triplets}; summary2 x triplets;
ledger2 x {blocks, triplets}; B-BB-qwen3.5-4b verdict x blocks; all B-C0 validation runs; B-T0 timing.

## P1 status
- B-DIS-s0..s2 queued (74): ledger2 on C's clin_v1/clinpairs_medeinst_dis (copied from PVC selrm-c, sha256 = C's),
  eval clin_v1/medeinst_dis_test (pair reversal) + rule dev/L2 + xr_v1. B-TR-steperr dropped (MedPRMBench unreleased).
- B-TR-clinonly-s0 and B-TR-tripclin-s0 queued (74) on C's final clin_v1/clinpairs_train (sha 548d26d0); seeds
  1-2 at 94. Clinical train dirs rebuilt by one prep job after a two-pod temp-file collision (fixed: uuid names).
- Premise gate: C publishes Med-PRM per-example scores (results_git/C-AUD-medprm on role-c, dev and test_L2).

## P1 work without GPUs
- B-AB-conddrv-s0 (condition derived by the reader): format conddrv implemented, CPU self-test passes, queued
  (priority 63), prep OK.
- New sets from A (P0.6): check that their records carry gold ledgers before the reader formats are run on them
  (pretok check_gold requires one per (case, condition)); C's xr_v1 convention: selrm.metrics.crossed_accuracy.
- Premise gate: needs the step check (C/D). Probe re-weighting step 2 after its scores run.
- Medical-data rows, B-DIS: need C's clinical pairs.

## Before the tables
- Summaries written by runners on code before e86e9f7 carry CIs from the old bootstrap (process-dependent order;
  ~0.1 point): recompute every summary from its scores file with the final selrm/metrics.py before make_tables:
  `python scripts/resummarize_b.py --all` (also adds xr crossed accuracy / clinical pair reversal to summaries
  written by older runner code; run it on every pulled run that evaluated xr_v1 or a clinical pair set).
- Regenerate docs/PROJECTION_B.md once an H100 training run has finished (H100 speed is unmeasured until then).

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Until then kept adapters stay on the PVC.

## Blockers
- A: train_triplets_no_*, xr_v1, challenge_v1, rewrite_v1, ec_v1 (A's last commit 813e921: paused).
- Cluster: no free GPUs of B's types.
