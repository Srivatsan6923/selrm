# STATE role C (maintained by Claude Code)
Updated: 2026-10-03 ~06:10 UTC (Sat). Task list: FINAL_TASKS_C.md (replaces earlier directives). Branch role-c,
clone D:\NAACL27\selrm-role-c.

## Compute
- NRP namespace ecepxie: own PVC selrm-c (60 Gi, /pvc/selrmc); B's PVC selrm-b read-only at /pvcb (env tarball v1,
  base weights, rule_v1 data and pre-tokenised prompts, adapters). Objects selrm-c-*, label app=selrm-c.
- Launcher scripts/submit_c.py (sync-up/down, push-code, push, sh, runner [--gpu a100|l40|a40|a6000|32gb|24gb],
  pull). GPU driver scripts/eval_c.py with B's scoring code (snapshot ac524e8062ef on /pvcb). CPU self-test:
  `python tests/selftest_eval_c.py scratch/bcode scratch/qwen35_tok scratch/rv1`.
- Task files on the PVC (git: configs/tasks_c/): c_tf_rule.json (read by every runner; runs without new options),
  c_wave2.json (nocase / rejudge_from runs; only runners on code >= 05b0826 read it), c_tg_test.json (TrialGPT test;
  push after the dev check). Runners re-read their file before every claim. min_gb gates big generation runs.
- GPU availability (06:00 UTC): every A100/A40/A6000/L40 and the RTX 5000 Ada cards allocated; 24 GB cards
  (A10/L4/3090) available. A node without the CephFS CSI driver strands a pod in Init: delete its Job.
- Results: results_git/<run_id>/ (`python scripts/submit_c.py pull`).

## Done
- TrialGPT protocol (docs/TRIALGPT_PROTOCOL.md, amended section 10 from dev); clin_v1/trialgpt_{dev,test};
  exclusion list for A; shortcut validation in the MANIFESTs.
- Dev portion scored: critic, prompted summary, prompted ledger (strict), verdict x blocks/triplets
  (results_git/C-TG-*-dev; development numbers only).
- Metrics: selrm/metrics.py (paired_test -> (diff, lo, hi, p), holm(list), cluster bootstraps, macro, near-miss,
  step revisions, MR/FR, crossed accuracy on A's xr_v1 records, seed_table, prf); reproducible CIs (B's CR);
  scripts/score.py; tests/test_metrics_c.py.
- P0.5 general-purpose trigger tagger + program: results_git/C-SC-gptrigger (L2 TA 77.7 [75.4, 79.7]).
- API judge harness (selrm/judges.py, scripts/run_judge.py, tests/test_judges.py); waits for COMPUTE REQUEST #1.
- Reader audit (scripts/reader_audit.py): untrained readers write decisions into summaries/ledgers (16-44%).

## In progress (NRP)
- C-TG-{ledger2-blocks,ledger2-triplets,summary2-triplets}-dev; C-TG-promptledger-lenient-dev (wave 2).
- Queued: C-TF-critic (verdict, every rule_v1 dev/test set + xr_v1), C-TF-promptsum, C-TF-promptledger (>= 30 GB),
  C-TF-promptledger-lenient and C-TF-defcorr-nocase (wave 2).
- Workflow wf_7fd2fd5e-25b: verification of external ids (MedEinst, MedQA/CareQA, NLI4CT, MedPRMBench, CondMedQA,
  released PRMs, API models, local judges) -> configs/models.json, configs/datasets_c.json.

## Next
1. Dev check of the remaining TrialGPT systems (malformed rates of trained readers); then push c_tg_test.json and
   launch; then `python scripts/eval_clinical.py trialgpt --split test` -> docs/TRIALGPT_RESULTS.md.
2. Pull C-TF-*; scripts/score.py --write-summary where needed; scripts/defcorr.py; report untrained-backbone rows.
3. P1, in this order: MedEinst (primary endpoint: conversion, all systems), released PRMs and open judges (GPU),
   key pairs, NLI4CT-P, clinpairs_train for B; API judges when the key arrives.
4. P0.4 for challenge_v1, rewrite_v1, ec_v1 when A registers them (baselines; B scores its adapters).

## Local scratch (not in git; .git/info/exclude)
scratch/rv1 (rule_v1 eval records, sha256 checked), scratch/acode (A 59034a3), scratch/acode_xr (A 2df9308, xr_v1
restored), scratch/bcode (B ac524e8), scratch/venv_ctx (medspacy 1.3.1), scratch/qwen35_tok, cache/api (judge cache).

## Open compute requests
- #1 (3 Oct): OPENROUTER_API_KEY for the P1 API judges and references. Not needed for P0.

## Blockers
- none for P0 except GPU availability. P0.4 waits for A's remaining sets.
