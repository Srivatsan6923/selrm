# STATE role C (maintained by Claude Code)
Updated: 2026-10-03 ~08:50 UTC (Sat). Task list: FINAL_TASKS_C.md. Branch role-c, clone D:\NAACL27\selrm-role-c.

## Compute and how runs work
- NRP namespace ecepxie: own PVC selrm-c (/pvc/selrmc); B's PVC selrm-b read-only at /pvcb. Objects selrm-c-*.
- Sync pod selrm-c-sync recreated 08:37 UTC; it expires after 6 h (~14:35 UTC): `python scripts/submit_c.py sync-down`,
  wait until it is gone, then `sync-up`.
- Launcher scripts/submit_c.py: sync-up/down, push-code (git archive HEAD), push FILE DEST, sh CMD,
  runner TASKS --gpu {a100,l40,a40,a6000,32gb,24gb} --bcode ac524e8062ef [--code SHA] [--online for PRM runs]
  [--models "" to skip base staging], pull. Runners only on us-west / us-central nodes.
- GPU driver scripts/eval_c.py (B's scoring code ac524e8062ef on sys.path). GEN = 5 (runs with min_gen > GEN are
  skipped by older runners): 3 topk/subsets/budgets, 4 ThinkPRM wrapper, 5 xr_v1 subsets keep whole items.
  Latest code snapshot 098d039c0957. Self-test: python tests/selftest_eval_c.py scratch/bcode scratch/qwen35_tok scratch/rv1
- Task files (configs/tasks_c/ -> /pvc/selrmc/tasks/, re-read before every claim): c_tf_rule (main; also new
  C-TG-summary2-blocks-dev, C-TG-verdict-blocks-s2, C-TG-verdict-triplets-s1), c_wave2 (nocase, rejudge), c_tg_test,
  c_long / c_long2 (MedEinst, key pairs, NLI4CT-P, MedQA train reader; 24 GB token budgets), c_noise, c_prm.
- Part runs <RUN>--p<k> are merged with python scripts/merge_parts.py RUN after pulling.
- Results: python scripts/submit_c.py pull RUN... -> results_git/<run_id>/ (topk files are not pulled; fetch to
  scratch/topk/<run>/ by kubectl exec tar).

## Done
- P0.1 TrialGPT: protocol (sections 10 amendments, 11 corrections after test), dev check, test scored for 9 systems,
  docs/TRIALGPT_RESULTS.md regenerated after an independent verification (all primary numbers, CIs, comparisons
  reproduced; fixes: evidence quotes, undefined precision, unrounded case-blind values, per-seed listing, tau source
  for later seeds, threshold-source sensitivity table). Comparison (6) not supported on test.
- P0.3 metrics (selrm/metrics.py): crossed_accuracy now as A's selrm.xr (raises on incomplete items; exclude=).
- P0.5 general-purpose trigger tagger: results_git/C-SC-gptrigger (L2 TA 77.7).
- PRM wrappers: scripts/prms/{medprm,meds3prm,foverprm,thinkprm,genprm}.py, each reviewed against the official
  code; tests/test_prm_*.py pass; weights load straight onto the GPU (12 GiB pods).
- Noise check (App. F): results from scratch/topk/C-DG-noise (rerun with --logodds results_git/C-TF-critic, copy
  noise_check.json into results_git/C-DG-noise/).
- Pulled: C-TF-promptsum--p1, C-TF-defcorr-nocase, C-DG-noise (C-ME-critic DONE on the PVC, not pulled yet).
- External ids verified; clinical sets built (MedEinst, key pairs, NLI4CT-P, clinical training pairs).
- Not run (logged): CondMedQA, EHRNote-ChatQA, MedPRMBench ablation, injected-error PRM, pilot.

## In progress (08:45 UTC)
- C-TF-critic: 10 of 11 sets done (readapply, xr_v1 left). Then: pull, report_c.py, defcorr.py, noise_check --logodds.
- C-TF-promptledger--p1/--p2, C-TF-genprog, C-CP-medqa-train-reader, C-AUD-medprm--p1, C-AUD-meds3--p1 running.
- Queued: C-TG-summary2-blocks-dev (then its test run C-TG-summary2-blocks-s0, after the dev check), seeds
  C-TG-verdict-blocks-s2 / -triplets-s1, C-TF-prompt{sum,ledger}--p2/p3, lenient rejudges, C-ME-*, C-KP-*, C-NL-*,
  C-AUD-* (ThinkPRM on the a6000 / l40 runners, pending).

## Next
1. C-TF-critic DONE -> pull; report_c.py (docs/RESULTS_C.md); defcorr.py; noise_check.py with --logodds; reader audits.
2. C-TG-summary2-blocks-dev DONE -> dev check (every record scored, malformed rate, gen_not_stopped) -> add
   C-TG-summary2-blocks-s0 (test, max_new 768) to c_tg_test.json; seeds -> eval_clinical trialgpt --split test.
3. Merge prompted parts when all DONE; lenient rejudges; P0.2 report and handoff.
4. C-ME-* -> eval_clinical medeinst (comparisons (4), (5)); C-KP-*, C-NL-*; clinpairs_prep.py after the MedQA reader.
5. PRM audit: merge parts, summaries; send B the Med-PRM per-example scores (rule_v1/dev, test_L2, all claim types).
6. API audit when COMPUTE REQUEST #1 is granted (run_judge.py --estimate-only first; budget ladder if needed).
7. P0.4 ec_v1 / challenge_v1 / rewrite_v1 when A freezes them (not in A's registry yet).

## Local scratch (not in git; .git/info/exclude)
scratch/rv1 (rule_v1 eval records), scratch/acode (A 59034a3), scratch/acode_xr (A 2df9308 + KNOWN_ISSUES.json from
bf51d94), scratch/bcode (B ac524e8), scratch/bres (B's dev_missing scores), scratch/topk, scratch/venv_ctx,
scratch/qwen35_tok, scratch/verify_ids.json, cache/api.

## Open compute requests
- #1 (3 Oct): OPENROUTER_API_KEY (API judges: three closed flagships, Kimi K3, Llama-3.3-70B; references).

## Blockers
- GPUs: the cluster is full (many pods pending); >= 40 GB cards scarce (ThinkPRM, prompted MedEinst).
