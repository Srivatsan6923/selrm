# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~17:20 UTC (Fri). Working to the lead's revised plan (2 Oct evening). Run freeze: Wed 7 Oct 23:59.

## Report for the lead (revised plan, "report first"; corrected 17:15 UTC after a verification pass)
Full tables, generated from results, PVC run logs and queue files: docs/PROJECTION_B.md (report_b.py timesplit,
projection).
1. Time split, the six finished rule_v1 runs (full 10-set evaluation):
   - verdict x {balanced, blocks, natural, triplets} (A100-SXM4-80GB): 1.48-1.56 GPU-h training, 0.65-0.68 GPU-h
     evaluation, total 2.15-2.25.
   - ledger2 x blocks (A100-SXM4-80GB): 1.76 + 1.03 = 2.80 GPU-h; ledger2 x triplets (A100-PCIE-40GB): 2.29 + 1.41
     = 3.73 GPU-h.
   - Training dominates. Seconds per set are in the table (test_L2 the largest: 526-551 verdict, 822 ledger2 on
     A100-80GB). New runs also write meta.json eval_seconds_by_set.
2. Projection, in A100-SXM4-80GB hours (training and evaluation rates measured on rule_v1 runs, finished or
   running; summary2 / value2 evaluation still scaled by B-T0 until their first runs finish): the revised queue incl.
   P2 rows and blocked rows = 370.9 h for 201 runs. Capacity to Wed 7 Oct 23:59 UTC = 126.7 h x GPUs held over the
   last 6 h per model (A100-SXM4-80GB 3.25, A100-PCIE-40GB 0.69 at measured speed 0.78, L40 0.32 at 1.00 until
   measured) = 540 GPU-h = 521 A100-80GB hours. It fits; cut order if it slips (plan): B-DIV seeds 1-2, then seed 0.

## Revised plan, applied 16:30-16:45 UTC
- Evaluation scope: the four key cells keep every frozen dev/test set (every seed); every other run evaluates on dev,
  test_L2, dev_missing, missing (B-TR rows + test_L3alt; LOKO dev/L2/L0; dose and folds dev/L2). Runs
  already claimed or running keep their scope (rationale x 4, verdict x balanced, ledger2 x triplets, B-BB 4B).
- Run order (scripts/make_queue_b.py priority()): ledger2 x triplets (running) and summary2 x triplets -> C-TF-critic
  -> rest of seed 0 -> seeds 1-2 of the key cells and summary2 x triplets -> LOKO (subject first) -> dose -> extras
  by matrix priority (ablations, transfer, backbones, folds) -> seeds 1-2 of the other cells -> B-DIV last.
- Cut: seeds 3-4 of the 16 non-key cells (32 rows dropped). New: 12 rows (B-LOKO x 6, B-DOSE x 6); their corpora
  (A 3e0c832) rebuilt in the cluster, sha256 equal to A's registry; pre-tokenising.
- C-TF-critic queued (zero-shot base, verdict prompt, every frozen dev/test set; results_git/C-TF-critic).
- configs/adapters.json: PVC paths of all four key systems (seed 0 DONE).
- After the verification pass: verdict x natural seeds 1-2 run with the key-cell seeds (the lead's natural vs
  blocks claim); diversity runs on dev, test_L2, dev_missing, missing; P2 rows and diversity seeds 1-2 queued at the
  end (the projection fits).

## Host-memory incident (16:03) and fix
- A 12 Gi runner was OOM-killed: Unsloth's offloaded gradient checkpointing pins 7.3-8.5 GB of host RAM at rule_v1
  lengths and keeps it across runs. Fix: on-GPU checkpointing for every run started after 16:30 (same maths).
- Runners with the old code drain: queues moved to /pvc/selrm/queues (old root holds empty stubs), so each finishes
  its current run and exits. Pending Jobs relaunched on the latest code; the first takes B-C0-val-gpu-ckpt first.

## Done
- B-C0 pipeline + CPU self-test (all formats incl. genprm, all eval modes, queue directory with a newer spec).
- Smoke comparison docs/SMOKE_B_C0.md; B-T0 timing docs/TIMING_B_T0.md (both provisional).
- GPU validation of every ablation path; backbones (Qwen3.5-4B, granite-4.1-8b) validated on smoke.
- rule_v1: all 38 + 6 new frozen sets rebuilt in the cluster with A's sha256.
- rule_v1 seed 0 DONE: verdict x {natural, balanced, blocks, triplets}, ledger2 x {blocks, triplets} (headline: L2 TA
  99.2; docs/FACTORIAL_B_S0.md, provisional).
- Code review workflow (5 reviewers + 2 skeptics each): field-edit numeric conditions and runner capability check
  fixed before use.

## Next
1. Watch B-C0-val-gpu-ckpt (on-GPU checkpointing: VRAM, host shmem) on the first new runner.
3. Probe re-weighting step 2 after B-AB-probe-rw-s0-scores is DONE: `submit_b.py prep v2/b_probe_rw_s0.json`.
4. When C publishes clin_v1/medeinst_test + scripts/eval_clinical.py: eval-only specs for the kept adapters.
5. Regenerate docs/PROJECTION_B.md as runs finish (rates for rationale, summary2, value2 replace the B-T0 ratios).

## GPUs held
- Running: 3 x A100 (old code, draining) + 1 x L40 (backbone runner, old code) + 3 x A100 on the latest code;
  pending: 2 x A100, 2 x A40, 1 x L40, 1 x A6000 (backbones). Finished runs: 93.3-96.7% mean GPU util on
  A100-SXM4-80GB, 90.0% for ledger2 x triplets on A100-PCIE-40GB (meta.json gpu_util_mean).

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). The user will answer. Until then kept adapters stay on the PVC.

## Blockers
- none. Clinical columns wait for C (clin_v1, eval_clinical.py).
