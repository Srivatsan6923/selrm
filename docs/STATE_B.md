# STATE role B (maintained by Claude Code)
Updated: 2026-10-02 ~16:45 UTC (Fri). Working to the lead's revised plan (2 Oct evening). Run freeze: Wed 7 Oct 23:59.

## Report for the lead (revised plan, "report first")
Full tables, generated from results and queue files: docs/PROJECTION_B.md (scripts/report_b.py timesplit, projection).
1. Time split, finished rule_v1 runs (all on A100-SXM4-80GB; full 10-set evaluation):
   - verdict x {blocks, natural, triplets}: 1.51-1.56 GPU-h training, 0.65-0.68 GPU-h evaluation, total 2.18-2.25.
   - ledger2 x blocks: 1.76 GPU-h training, 1.03 GPU-h evaluation, total 2.80.
   - Training dominates. Per-set evaluation seconds (verdict / ledger2): test_L2 526-551 / 822, readapply 272-283 /
     526, test_L0 249-260 / 386, test_hard 354-369 / 438, dev 94-98 / 149, missing 134-139 / 209, dev_missing 41 / 64.
   - Per-set seconds were already in summary_<set>.json; new runs also write meta.json eval_seconds_by_set.
2. Projection (A100-80GB rates measured above; formats not yet finished on rule_v1 scaled by their B-T0 ratios):
   revised queue incl. not-yet-queued P2 rows = 372.6 GPU-h for 203 runs. Capacity to the run freeze = 127.4 h x
   4.12 GPUs (mean held by B over the last 6 h) = 525 GPU-h. It fits at A100-80GB speed; slower cards (A100-40GB
   PCIe, L40, A40) stretch it, so the cut order stays: B-DIV seeds 1-2, then the other P2 rows, then B-DIV seed 0.

## Revised plan, applied 16:30-16:45 UTC
- Evaluation scope: the four key cells keep every frozen dev/test set (every seed); every other run evaluates on dev,
  test_L2, dev_missing, missing (B-TR rows + test_L3alt; LOKO dev/L2/L0; dose, folds, diversity dev/L2). Runs
  already claimed or running keep their scope (rationale x 4, verdict x balanced, ledger2 x triplets, B-BB 4B).
- Run order (scripts/make_queue_b.py priority()): ledger2 x triplets (running) and summary2 x triplets -> C-TF-critic
  -> rest of seed 0 -> seeds 1-2 of the key cells and summary2 x triplets -> LOKO (subject first) -> dose -> extras
  by matrix priority (ablations, transfer, backbones, folds) -> seeds 1-2 of the other cells -> B-DIV last.
- Cut: seeds 3-4 of the 16 non-key cells (32 rows dropped). New: 12 rows (B-LOKO x 6, B-DOSE x 6); their corpora
  (A 3e0c832) rebuilt in the cluster, sha256 equal to A's registry; pre-tokenising.
- C-TF-critic queued (zero-shot base, verdict prompt, every frozen dev/test set; results_git/C-TF-critic).
- configs/adapters.json: PVC paths for verdict_triplets, verdict_blocks, ledger2_blocks (DONE); ledger2_triplets
  when its run is DONE.

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
- rule_v1 seed 0 DONE: verdict x blocks / natural / triplets, ledger2 x blocks (docs/FACTORIAL_B_S0.md, provisional).
- Code review workflow (5 reviewers + 2 skeptics each): field-edit numeric conditions and runner capability check
  fixed before use.

## Next
1. B-F-ledger2-triplets-s0 DONE: malformed rate, L2 TA by near-miss kind, MR; regenerate the report; adapters.json.
2. Watch B-C0-val-gpu-ckpt (on-GPU checkpointing: VRAM, host shmem) on the first new runner.
3. Probe re-weighting step 2 after B-AB-probe-rw-s0-scores is DONE: `submit_b.py prep v2/b_probe_rw_s0.json`.
4. When C publishes clin_v1/medeinst_test + scripts/eval_clinical.py: eval-only specs for the kept adapters.
5. Regenerate docs/PROJECTION_B.md as runs finish (rates for rationale, summary2, value2 replace the B-T0 ratios).

## GPUs held
- Running: 5 x A100 (old code, draining) + 1 x L40 (backbone runner, old code). Pending on the latest code: 3 x A100,
  2 x A40, 1 x L40, 1 x A6000 (backbones). Finished runs: 94-95% mean GPU util; namespace 1 h mean 87%.

## Open compute requests
- #1 (2 Oct): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the user's (needed to
  publish kept adapters to a private HF repo). The user will answer. Until then kept adapters stay on the PVC.

## Blockers
- none. Clinical columns wait for C (clin_v1, eval_clinical.py).
