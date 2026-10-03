# STATE role C (maintained by Claude Code)
Updated: 2026-10-03 ~09:10 UTC (Sat). Task list: FINAL_TASKS_C.md. Branch role-c, clone D:\NAACL27\selrm-role-c.

## Compute and how runs work
- NRP namespace ecepxie: own PVC selrm-c (/pvc/selrmc); B's PVC selrm-b read-only at /pvcb. Objects selrm-c-*.
- Sync pod selrm-c-sync recreated ~08:23 UTC; it expires after 6 h (~14:20 UTC): `python scripts/submit_c.py sync-down`,
  wait until it is gone, then `sync-up`.
- Launcher scripts/submit_c.py: sync-up/down, push-code (git archive HEAD), push FILE DEST, sh CMD,
  runner TASKS --gpu {a100,l40,a40,a6000,32gb,24gb} --bcode ac524e8062ef [--code SHA] [--online for PRM runs]
  [--models "" to skip base staging], pull. Runners only on us-west / us-central nodes.
- GPU driver scripts/eval_c.py (B's scoring code ac524e8062ef on sys.path). GEN = 7 (runs with min_gen > GEN are
  skipped by older runners): 3 topk/subsets/budgets, 4 ThinkPRM wrapper, 5 xr_v1 subsets keep whole items,
  6 MedS3 loader fix, 7 hidden states.
  Latest code snapshot 00d227d4a525 (GEN 7). Self-test: python tests/selftest_eval_c.py scratch/bcode scratch/qwen35_tok scratch/rv1
- Task files (configs/tasks_c/ -> /pvc/selrmc/tasks/, re-read before every claim): c_tf_rule (main; also new
  C-TG-summary2-blocks-dev, C-TG-verdict-blocks-s2, C-TG-verdict-triplets-s1), c_wave2 (nocase, rejudge), c_tg_test,
  c_long / c_long2 (MedEinst, key pairs, NLI4CT-P, MedQA train reader; 24 GB token budgets), c_noise, c_prm.
- Part runs <RUN>--p<k> are merged with python scripts/merge_parts.py RUN after pulling.
- Results: python scripts/submit_c.py pull RUN... -> results_git/<run_id>/ (topk files are not pulled; fetch to
  scratch/topk/<run>/ by kubectl exec tar).

## Done
- P0.1 TrialGPT: protocol (sections 10 amendments, 11 corrections after test), dev check of all 9 systems (incl.
  summary2-blocks), test scored for 9 systems + verdict-blocks seed 2; report regenerated after an independent
  verification (docs/TRIALGPT_RESULTS.md: seed table, threshold-source sensitivity). Comparison (6) not supported.
- P0.2 critic: results_git/C-TF-critic (every rule_v1 set + xr_v1; MR, XA in summaries); default correction
  results_git/C-TF-defcorr (alpha -> inf on dev, extended grid) + C-ME-defcorr; docs/RESULTS_C.md (rows + ladder).
- P0.3 metrics (selrm/metrics.py; crossed_accuracy as A's selrm.xr: raises on incomplete items, exclude=).
- P0.5 general-purpose trigger tagger: results_git/C-SC-gptrigger (L2 TA 77.7).
- Diagnostics: C-TF-critic/diagnostics.json (G, L0 columns); results_git/C-DG-shift (slices signal=C-AUD-qwen35-9b
  from C-TF-critic, signal=B-F-verdict-blocks from B-F-verdict-blocks-s0); sampling noise results_git/C-DG-noise
  (noise_check.json T 0.7 / top-p 0.95; noise_check_T1.json T 1.0).
- Clinical pairs for B complete (clinpairs_train 7,929 = MedEinst 7,807 + MedQA 122); shortcut validation in every
  pair-set MANIFEST incl. medeinst_dis_test.
- PRM wrappers reviewed; GPU loading fixed (straight to device; MedS3 without second warm-up, runner generation 6).
- Scripts ready, waiting for inputs: scripts/ref_extract_program.py (C-REF-extract-program from the merged
  C-TF-promptledger-lenient), scripts/probe.py (C-DG-probe hidden states, generation 7), scripts/dg_shift.py (add
  C-AUD-medprm when merged).
- External ids verified; clinical sets built; not run (logged): CondMedQA, EHRNote-ChatQA, MedPRMBench ablation,
  injected-error PRM, pilot.

## In progress (09:10 UTC)
- c_tf_rule: C-TF-promptledger--p2 (L2), lenient rejudges --p1..3 (also on c_wave2), C-TF-promptsum--p2/--p3,
  C-TF-promptledger--p3, C-TG-summary2-blocks-s0, C-TG-verdict-triplets-s1, C-DG-probe (generation 7 only).
- c_wave2: C-TF-genprog (32 GB runner). c_long2: C-ME-* (verdict-blocks-s0, verdict-triplets-s0, ledger2-triplets-s0
  running), then C-KP-*, C-NL-*. c_prm: C-AUD-medprm--p1/--p2, C-AUD-fover--p1, C-AUD-meds3--p1 running; ThinkPRM on
  a6000 / l40 runners (pending).
- Background watcher: scratchpad/watch_done.sh (exits when a run gains DONE).

## Next
1. As parts finish: pull; merge_parts.py C-TF-promptsum / C-TF-promptledger / C-TF-promptledger-lenient /
   C-AUD-<prm>; score.py --write-summary on merged runs; reader_audit.py; report_c.py; ref_extract_program.py;
   dg_shift.py C-AUD-medprm=results_git/C-AUD-medprm; handoff P0.2 rows to D.
2. TrialGPT: when C-TG-summary2-blocks-s0 / -verdict-triplets-s1 land, eval_clinical trialgpt --split test.
3. MedEinst / key pairs / NLI4CT-P: eval_clinical medeinst | keypairs | nli4ct as C-ME / C-KP / C-NL runs land;
   comparisons (4), (5) in results_git/C-ME-comparisons.json.
4. Probe: when C-DG-probe is DONE, fetch hidden_*.npz to scratch (not git), python scripts/probe.py <dir>.
5. API audit when COMPUTE REQUEST #1 is granted: run ids C-AUD-closed-1 (GPT), -closed-2 (Gemini), -closed-3
   (Claude), C-AUD-llama70b, C-AUD-kimi-k3 (lead's make_tables names); L2 estimate: GPT $265 (1,000 triplets),
   Claude $106, Gemini $63, Kimi $12, Llama $3; references C-REF-closed-zero / -closed-ledger.
6. More systems when B registers them (ledger2-balanced, B-TR-*): C-TG-<x>, C-ME-<x>.
7. P0.4 ec_v1 / challenge_v1 / rewrite_v1 when A freezes them.

## Local scratch (not in git; .git/info/exclude)
scratch/rv1 (rule_v1 eval records), scratch/acode (A 59034a3), scratch/acode_xr (A 2df9308 + KNOWN_ISSUES.json from
bf51d94), scratch/bcode (B ac524e8), scratch/bres (B's dev_missing scores), scratch/topk, scratch/venv_ctx,
scratch/qwen35_tok, scratch/verify_ids.json, cache/api.

## Open compute requests
- #1 (3 Oct): OPENROUTER_API_KEY (API judges: three closed flagships, Kimi K3, Llama-3.3-70B; references).

## Blockers
- GPUs: the cluster is full (many pods pending); >= 40 GB cards scarce (ThinkPRM, prompted MedEinst).
