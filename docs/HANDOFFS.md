# HANDOFFS (append-only)

date | from | to | what | path
---|---|---|---|---
2026-10-02 | setup | all | foundation: schema, prompts, metrics, smoke generator, shortcut validation, tests | selrm/, scripts/, tests/
2026-10-02 | B | D (lead) | PROVISIONAL smoke comparison verdict x blocks vs verdict x triplets (Rev/Hold/TA by near-miss kind, smoke_v2 test_heldout_rules + dev_seen_rules); pipeline validation only, never tabled | docs/SMOKE_B_C0.md, results_git/B-C0-smoke-verdict-{blocks,triplets}-s0/
2026-10-02 | B | D (lead), all | B-T0 timing per format on A100-80GB (s/step, tok/s, peak memory, GPU utilisation train/eval, eval seconds) and est_hours for all B-F rows (seed 0 of the 20 cells ~53 GPU-h incl. full-ladder eval) | docs/TIMING_B_T0.md, docs/RUN_MATRIX_B.csv
2026-10-02 | B | D (lead), A | rule_v1 accepted: all 38 frozen sets (fold 1 + folds 2-3) rebuilt in the NRP cluster from A's freeze e40789bd5d7a, every sha256 equal to A's registry; factorial seed 0 (20 cells) + key cells seeds 1-2 running on A100s since 12:46 UTC; seed-0 ablations, eval-only analyses, folds, diversity curves, FoVer and GenPRM-style transfer and backbone rows queued behind it | docs/STATE_B.md, docs/RUN_MATRIX_B.csv, configs/queues/
