# STATE role C (maintained by Claude Code)
Updated: 2026-10-03 ~05:45 UTC. Task list: FINAL_TASKS_C.md (replaces earlier directives). Branch role-c, clone
D:\NAACL27\selrm-role-c.

## Compute
- NRP namespace ecepxie: own PVC selrm-c (60 Gi, /pvc/selrmc), B's PVC selrm-b mounted read-only at /pvcb (env tarball
  v1, base weights, rule_v1 data + pre-tokenised prompts, adapters). Objects selrm-c-*, label app=selrm-c.
- Launcher scripts/submit_c.py (sync-up/down, push-code, push, sh, runner, pull). GPU driver scripts/eval_c.py uses B's
  scoring code (snapshot ac524e8062ef on /pvcb) so C's rows share B's code path. CPU self-test: tests/selftest_eval_c.py.
- Task list on the PVC: /pvc/selrmc/tasks/c_tf_rule.json (git: configs/tasks_c/c_tf_rule.json); runners re-read it
  before every claim, so adding runs there reaches running pods. Runs with min_gb 40 wait for >= 40 GB cards.
- Results: results_git/<run_id>/ (pull with `python scripts/submit_c.py pull`).

## Done
- TrialGPT: protocol committed before scoring (docs/TRIALGPT_PROTOCOL.md); clin_v1/trialgpt_{dev,test} (patient- and
  trial-disjoint, GPT-4 fields dropped, shortcut validation in MANIFEST: case-blind type prior macro-F1 46.0 on test);
  exclusion list for A (configs/trialgpt_exclusions.json).
- Metrics (P0.3): selrm/metrics.py extended; scripts/score.py; tests/test_metrics_c.py.
- P0.5: general-purpose trigger tagger + program: results_git/C-SC-gptrigger (L2 TA 77.7).

## In progress (NRP)
- C-TG-<system>-dev (8 systems, TrialGPT dev + rule_v1/dev_missing), then C-TF-critic, C-TF-promptledger,
  C-TF-promptsum.

## Next
1. Pull C-TG-*-dev, run `python scripts/eval_clinical.py trialgpt --split dev` (data in scratch/rv1), dev check per
   protocol section 7, log; then queue C-TG-<system> on clin_v1/trialgpt_test (+ rule_v1/dev_missing) and report
   docs/TRIALGPT_RESULTS.md.
2. Pull C-TF-*; score.py summaries; report the untrained-backbone rows (verdict, prompted summary, prompted ledger).
3. P0.4 when A registers xr_v1 / challenge_v1 / rewrite_v1 / ec_v1: baselines (critic, prompted pipelines, trigger
   tagger) and any adapter B does not cover; crossed accuracy via selrm.metrics.crossed_accuracy.
Then P1 (FINAL_TASKS_C).

## Local scratch (not in git; listed in .git/info/exclude)
scratch/rv1 (rule_v1 eval records copied from the PVC, sha256 checked), scratch/bcode (B's code ac524e8),
scratch/acode (A's code 59034a3), scratch/venv_ctx (medspacy 1.3.1), scratch/qwen35_tok (tokenizer).

## Open compute requests
- #1 (3 Oct): OpenRouter API key (OPENROUTER_API_KEY) for the P1 audit (closed and open API judges). Not needed for P0.

## Blockers
- none for P0. P0.4 waits for A's sets.
