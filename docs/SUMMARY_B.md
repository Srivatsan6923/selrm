# Role B summary (paused)

Fri 2 Oct 2026, 17:25 UTC. On the user's instruction no new runs start: the queue files on the NRP volume are empty
(full copies in /pvc/selrm/queues_paused/ and in git under configs/queues/), and the runner Jobs that had not
started were deleted. Each running runner finishes its current run and then exits ("no claimable run left").

## What exists
- **Pipeline (tested).** Every training format (verdict, rationale, summary2, value2, ledger2, the decision-bit and
  verification ablations, pairwise BT, GenPRM-style), every eval mode (oracle ledger, program on the bit, ledger
  swap and field edits, verification pass), the concept scorer, NRP queue runners with claims, heartbeats and a GPU
  watchdog. The CPU self-test passes; every path ran on GPU with smoke data, incl. Qwen3.5-4B and granite-4.1-8b.
- **Data on the NRP volume.** All 44 frozen rule_v1 sets (folds 2-3, LOKO and dose corpora included), each rebuilt
  in the cluster with sha256 equal to A's registry.
- **Results (rule_v1, seed 0, one seed: provisional).** Triplet accuracy on test_L2 (docs/FACTORIAL_B_S0.md):

| format | natural | balanced | blocks | triplets |
|---|---|---|---|---|
| verdict | 58.0 [54.1, 61.9] | 49.1 [45.6, 53.1] | 58.2 [54.2, 62.5] | 91.3 [87.3, 95.0] |
| rationale | not run | not run | not run | not run |
| summary2 | not run | not run | not run | not run |
| value2 | not run | not run | not run | not run |
| ledger2 | not run | not run | 75.3 [72.0, 78.5] | 99.2 [98.6, 99.7] |

  Malformed ledgers stay at or below 0.17% on every set. MR is about 100 for every trained model, so per the lead
  it is not presented as a result.
- **Adapters.** The four key systems (verdict and ledger2 x blocks and triplets, seed 0) on PVC selrm-b at
  selrm/adapters/<run_id>, listed in configs/adapters.json for C and D. Step check = the released Med-PRM
  (MedPRMBench has no data release).
- **Plan.** The lead's revised plan is fully queued (now paused): 201 runs, 370.9 A100-80GB
  hours projected against 521 A100-80GB hours (540 GPU-h) deliverable to Wed 7 Oct 23:59 UTC
  (docs/PROJECTION_B.md). Matrix, decisions and handoffs are current (docs/RUN_MATRIX_B.csv, DECISIONS_B.md,
  HANDOFFS.md).

## What is running (finishes, then stops)
| run | state |
|---|---|
| B-F-rationale-natural-s0 | evaluation (10 sets) |
| B-F-rationale-blocks-s0, B-F-rationale-triplets-s0 | training on old-code runners (host-RAM offload; if one is OOM-killed it resumes from its checkpoint only when queues are restored) |
| B-F-rationale-balanced-s0 | training, resumed from checkpoint after the 16:03 OOM kill |
| B-F-summary2-triplets-s0 | training (plan step 2) |
| B-BB-qwen3.5-4b-verdict-blocks-s0 | backbone run on an L40 |
| B-C0-val-gpu-ckpt | 40-step smoke check of the on-GPU checkpointing fix |

## What I would do next
1. Read B-C0-val-gpu-ckpt (VRAM peak, host shared memory) to confirm the memory fix.
2. Pull each finished run, regenerate docs/FACTORIAL_B_S0.md and docs/PROJECTION_B.md (measured rationale and
   summary2 rates replace the B-T0 ratios), add finished key systems to configs/adapters.json.
3. When allowed to resume: `cp -r /pvc/selrm/queues_paused/. /pvc/selrm/queues/` on the sync pod, then relaunch
   runners on the current code (A100 up to quota 9, 48 GB overflow, one backbone runner). Order: C-TF-critic, rest of
   seed 0, seeds 1-2 of the key cells, summary2 x triplets and verdict x natural, LOKO, dose, ablations, transfer,
   backbones, folds, seeds 1-2 of the other cells, P2 rows, diversity last.
4. Waiting on others: the HF secret (COMPUTE REQUEST #1) to publish adapters; C's clin_v1 and eval_clinical.py
   for the clinical columns of the kept adapters; C's step-check wrapper for the premise gate.
5. Risks: A100 availability (48 GB cards measured slower); summary2 and value2 evaluation not yet measured on rule_v1.
