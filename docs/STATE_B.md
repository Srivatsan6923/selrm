# STATE role B (maintained by Claude Code)
Updated: 2026-10-03 ~06:30 UTC (Sat). Plan: docs/FINAL_TASKS_B.md (3 Oct; replaces every earlier directive).
Run freeze: Wed 7 Oct 23:59 (UTC assumed). Decisions: docs/DECISIONS_B.md. Analyses: docs/ANALYSIS_B.md.

## P0 status
1. Analyses on existing predictions (docs/ANALYSIS_B.md, `python scripts/analysis_b.py > docs/ANALYSIS_B.md`): done
   (sections 1-9; B-AE-oracle-ledger, B-AE-field-edit, B-AE-field-swap DONE 05:53-06:00 UTC on H100s). Field
   edits that should change the verdict are followed in 47.8% (handoff 3 Oct). Left: the blocks half of the
   paired ledger-summary comparison after summary2 x blocks.
2. B-F-summary2-blocks-s0: training on an H100 runner since 06:00 UTC.
3. Core seeds 1-2 ({verdict, summary2, ledger2} x {blocks, triplets}): 12 runs queued (priority 20).
4. B-SC-summary2-triplets-s0 (format summary2_case: judge sees rule, case, prose, claim): queued (30), prep done.
5. LOKO {verdict, summary2, ledger2} x {subject, time, boundary}: waiting for A's
   rule_v1/train_triplets_no_{kind} (not in origin/role-a REGISTRY at 05:10 UTC). When registered: fetch role-a,
   build-data with A's commit (`--only` the new sets, sha256 check), `make_queue_b.py newexp`, push, prep.
6. New sets xr_v1, challenge_v1, rewrite_v1, ec_v1: waiting for A. Then eval-only B-NS specs for every kept
   adapter. configs/adapters.json lists 6 kept adapters on the PVC (ledger2, verdict x blocks/triplets;
   summary2, rationale x triplets).

## Queue (configs/queues, pushed to /pvc/selrm/queues; priority from make_queue_b.py)
0 B-AE-* P0.1 -> 1 B-F-rationale-balanced-s0 (orphan claim, resumes) -> 10 summary2 x blocks -> 20 core seeds 1-2
-> 30 B-SC -> 40-42 LOKO -> 50 remaining seed 0 -> 55 core seeds 3-4 -> 60-70 ablations -> 72 FoVer -> 73 GenPRM
-> 76-77 folds -> 80-81 diversity -> 85 second backbone (granite-4.1-8b) -> 92-99 unlisted rows.

## GPUs held
- 10 runner Jobs (code 625e935: every queued format except conddrv) on 6 x A100, 2 x A40, 1 x L40, 1 x A6000,
  all Pending since 04:56 UTC: the cluster has no free card of these types (scheduler: Insufficient
  nvidia.com/a100). Namespace A100 quota 7/9 (C shares it; B uses at most 6). 24 GB cards are not used: training
  peaks at 21-27 GB.
- 6 runner Jobs on H100 at priority class opportunistic (outside the A100 quota): 2 from 05:40 UTC (code 072d46d,
  max 3 runs), 4 from 06:15 UTC (code 3b62811, max 6 runs, 16 h; 1 running, 3 pending). Preemptible: the run resumes
  from its last 20-min checkpoint when another runner claims it. One A100 runner started 06:00 UTC.
- B-AB-conddrv-s0 needs a runner on code >= bc9d2bc (the H100 runners, or any runner submitted later).
- Sync pod selrm-b-sync created ~03:00 UTC (6 h deadline): recreate before ~09:00 UTC (delete the Completed pod
  first, then sync-up).

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

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). Until then kept adapters stay on the PVC.

## Blockers
- A: train_triplets_no_*, xr_v1, challenge_v1, rewrite_v1, ec_v1 (A's last commit 813e921: paused).
- Cluster: no free GPUs of B's types.
