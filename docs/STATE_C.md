# STATE role C (maintained by Claude Code)
Updated: 2026-10-03 ~06:50 UTC (Sat). Task list: FINAL_TASKS_C.md. Branch role-c, clone D:\NAACL27\selrm-role-c.

## Compute and how runs work
- NRP namespace ecepxie: own PVC selrm-c (/pvc/selrmc); B's PVC selrm-b read-only at /pvcb. Objects selrm-c-*.
- Launcher scripts/submit_c.py: sync-up/down, push-code, push FILE DEST, sh CMD, runner TASKS --gpu
  {a100,l40,a40,a6000,32gb,24gb} [--online for PRM runs] [--models '' to skip base staging], pull.
  Runners only on us-west / us-central nodes (us-east staging took > 40 min; one node lacked the CephFS driver).
  The launcher pushes a missing code snapshot itself; it refuses while the tree is dirty (then pass --code <pushed sha>).
- GPU driver scripts/eval_c.py with B's scoring code (ac524e8062ef): standard runs, nocase (default correction),
  rejudge_from (format-normalised prompted ledger), prm (released PRMs via scripts/prms/<module>.py). Self-test:
  python tests/selftest_eval_c.py scratch/bcode scratch/qwen35_tok scratch/rv1
- Task files (configs/tasks_c/ -> /pvc/selrmc/tasks/): c_tf_rule.json (main queue, all runners), c_wave2.json
  (nocase / rejudge; code >= 05b0826), c_tg_test.json (TrialGPT test). Runners re-read before every claim.
- Part runs <RUN>--p<k> are merged with python scripts/merge_parts.py RUN after pulling (prompted rule-tier rows).
- Results: python scripts/submit_c.py pull -> results_git/<run_id>/; then evaluation scripts below.
- C's PVC registry: /pvc/selrmc/data/REGISTRY.json = data/clin_v1/REGISTRY_C.json + A's xr_v1/test entry
  (regenerate scratch/pvc_registry.json and push after adding a set).

## Done
- P0.1 TrialGPT: protocol (+ amendments, section 10), sets, dev check of all 8 systems (development numbers in
  results_git/C-TG-*-dev). Test runs in flight (C-TG-*); report: python scripts/eval_clinical.py trialgpt --split test.
- P0.3 metrics (selrm/metrics.py; D's and B's change requests done); scripts/score.py; tests/test_metrics_c.py.
- P0.5 general-purpose trigger tagger: results_git/C-SC-gptrigger (L2 TA 77.7).
- External ids verified (configs/models.json, configs/datasets_c.json; workflow wf_7fd2fd5e-25b record in scratch).
- Clinical sets: MedEinst test/ref_dev/ref_train; key pairs (v13 definition tiny: 13/3; one-way variant 357/225;
  lead decides); NLI4CT-P test/dev; clinical training pairs for B (MedEinst part) + disease-held-out split.
- Not run (logged): CondMedQA (no general answers), EHRNote-ChatQA, MedPRMBench ablation, injected-error PRM, pilot.
- Harness for API judges (selrm/judges.py, scripts/run_judge.py); diagnostics (scripts/diagnostics.py: P/K/G, shift).

## In progress
- NRP queue (c_tf_rule.json): C-TF-critic (every rule_v1 set + xr_v1), C-TF-prompt{ledger,sum}--p1..3, C-ME-*
  (MedEinst), C-KP-* (key pairs), C-NL-* (NLI4CT-P), C-CP-medqa-train-reader; c_wave2: C-TF-defcorr-nocase,
  C-TF-promptledger-lenient--p1..3, C-TG-promptledger-lenient-dev, C-ME-promptledger-lenient; c_tg_test: C-TG-*.
- Workflow wf_d5b8ee00-423: wrappers for the released PRMs (scripts/prms/{medprm,meds3prm,foverprm,thinkprm,genprm}.py
  + tests); then PRM audit runs (prm field, --online runners).

## Next
1. When C-TG-* test runs are DONE: pull, eval_clinical trialgpt --split test, reader audits, docs/TRIALGPT_RESULTS.md,
   HANDOFFS to D (the lead's framing decision H7a waits for it).
2. Pull C-TF-*, merge parts, defcorr.py, score.py; report the untrained-backbone rows (P0.2) incl. xr_v1 (P0.4).
3. Integrate PRM wrappers; queue C-AUD-{medprm,meds3,fover,thinkprm,genprm} on L2 (+ missing, xr_v1, MedEinst, keys).
4. Pull C-ME/C-KP/C-NL; eval_clinical medeinst / keypairs / nli4ct; clinpairs_prep.py after C-CP-medqa-train-reader.
5. API audit when COMPUTE REQUEST #1 is granted (run_judge.py --estimate-only first; budget ladder if needed).

## Local scratch (not in git; .git/info/exclude)
scratch/rv1 (rule_v1 eval records incl. readapply, test_L0), scratch/acode (A 59034a3), scratch/acode_xr (A 2df9308),
scratch/bcode (B ac524e8), scratch/venv_ctx (medspacy), scratch/qwen35_tok, scratch/verify_ids.json, cache/api.

## Open compute requests
- #1 (3 Oct): OPENROUTER_API_KEY (API judges: three closed flagships, Kimi K3, Llama-3.3-70B; references).

## Blockers
- GPUs: >= 30 GB cards scarce (prompted MedEinst runs wait for them). API judges wait for #1.
