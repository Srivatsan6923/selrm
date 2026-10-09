# STATE role C (maintained by Claude Code)
Updated: 2026-10-08 ~23:30 UTC. Task file: STAGE2_TASKS_C.md (8 Oct; copy with README, spec, analysis plan and
red cells in scratch/stage2/selrm_stage2_tasks/). It replaces FINAL_TASKS_C / NEXT_TASKS_C. Dates are lifted; work
is ordered by dependency. Branch role-c, clone D:\NAACL27\selrm-role-c.

## Compute and how runs work
- NRP namespace ecepxie: own PVC selrm-c (/pvc/selrmc); B's PVC selrm-b read-only at /pvcb. Objects selrm-c-*.
- Sync pod selrm-c-sync: 6 h lifetime; `python scripts/submit_c.py sync-up` (sync-down first if it still exists).
- Launcher scripts/submit_c.py: runner TASKS --gpu {24gbf,24gb,32gb,l40,a6000,a40,a100} --hours H --bcode SHA
  [--code SHA] [--online --models "" for PRM runs]; pull; push FILE DEST; push-code. --hours is a hard deadline.
  B code: ac524e8062ef for stage-1 formats (comparable with earlier rows); 10e1882945ce for summary2_case.
- Runner scripts/eval_c.py, GEN 7. Views (set names with '@') are read from C's volume.
- Large files to the pod: gzip -c f | kubectl exec -i selrm-c-sync -- sh -c 'gunzip > dest' and check sha256; from
  the pod: split -b 20000000 and copy chunks. The laptop is short of memory: no background watchers; poll by hand.
- Task files in configs/tasks_c/ -> /pvc/selrmc/tasks/. Part runs merged with scripts/merge_parts.py.

## Stage 2 status
- D0 (analysis plan on main): NOT yet on origin/main (8 Oct 23:00). No stage-2 test set of A exists yet.
- C1 rule-tier controls: scripts/crit_views.py (rule_v1 handler); views rule_v1/test_L2@{none,wrong} and
  rule_v1/test_L3inv@{none,wrong} frozen (L3inv carries the invented-name rules; L2 = 20 hand-written + 83 sampled
  rules); runs C-S2-ctrl-<system> (17 systems, c_s2_ctrl.json) launched 8 Oct. Then: pull, report TA/Rev/Hold
  with rule (stage-1 runs), without, wrong; by rule source; docs/STAGE2_RESULTS.md section 1. xp_v1 when A registers.
- C2 executor audit: waits for A2's renderer; the DDXPlus linkage check on the MedEinst reference split can start.
- C3-C7: wait for A1 (mcv_v1), A2 (kb_v1), A4-A6, B2-B3.
- C9 carry-over, done 8 Oct: ThinkPRM (L2 87.5, XA 100 on its subsets) and GenPRM merged and pushed; TrialGPT
  seeds 0-4 of the six core cells + ledger2-balanced, TR-fover, TR-clinonly; S3 case-visible summary system
  (MedEinst 28.7, key pairs 66.9, NLI4CT-P; TrialGPT test queued); denial hold docs/MEDEINST_NEG_RESULTS.md;
  prompted MedEinst rows. Open: criterion-claim TA columns, default-correction Rev/Hold, key pairs for prompted
  ledger / default correction / summary x blocks, NLI4CT-P prompted rows and eligibility slice, shift classes for
  other signals, Table 17 denominators, the four confirmations for D, clinical columns for rationale / natural /
  tripclin rows, larger judges (API key or 80 GB GPU; else "not scored").

## Reports and evaluators
docs/RESULTS_C.md (report_c.py), TRIALGPT_RESULTS.md, MEDEINST_RESULTS.md, MEDEINST_NEG_RESULTS.md,
KEYPAIRS_RESULTS.md, NLI4CT_RESULTS.md (eval_clinical.py <trialgpt|medeinst|medeinst_neg|keypairs|nli4ct>),
AUX_PROTOCOL.md + scripts/eval_aux.py (S1/S2; B's B-AUX runs), scripts/score.py --write-summary (MR, XA).

## Open requests
- COMPUTE REQUEST #1: OPENROUTER_API_KEY (large judges, closed rows, references).

## Local scratch (not in git)
scratch/rv1 (rule_v1 records), scratch/acode_xr (xr_v1 + KNOWN_ISSUES), scratch/afreeze (A's rule freeze),
scratch/bcode (B ac524e8), scratch/bcode2 (B 10e1882), scratch/anegbank, scratch/probe, scratch/stage2.

## Update 9 Oct (resume here)
- Cluster: runners for c_s2_mcv.json (MedCalc-V, 22 runs; code 329a633d028a, B code ac524e8062ef) and c_s2_kb.json (kb_v1 x 11 verdict systems x {stated, none, wrong}; xp_v1 x 17 systems) launched 9 Oct ~06:00-06:50 UTC, 20 h deadline. Next: `submit_c.py pull`, `python scripts/s2_compare.py` -> comparisons (7),(8),(9) -> decision input to D; then secondary MedCalc-V cells (C-S2-mcv2-*), kb_v1 and xp_v1 tables (not written yet: extend scripts/stage2_report.py).
- C2 done: scripts/medeinst_executor.py, results_git/C-S2-executor, docs/MEDEINST_EXECUTOR.md (handoff 8 Oct). C4 on MedEinst pairs (derived criterion) waits for D's gate record.
- C1: two-stage controls in docs/STAGE2_RESULTS.md; ledger2-triplets-s4 still running; paraphrase tier queued (C-S2-xp-*).
- API judges: see HANDOFFS 9 Oct. BLOCKED on OpenRouter credits (402). When credits are back: `sh scratch/api_logs/run_one.sh MODEL RUN_ID` for kimi-k3 / C-AUD-kimi-k3, kimi-k3-choice / C-AUD-kimi-k3-choice (smoke with --n 10 first), nemotron-3-super-choice, qwen35-397b-choice, gemma-4-31b-choice and qwen35-27b (missing twins only; cached otherwise). run_judge.py refuses to write a set with more than 2% failed calls.
- Volume registry: scratch/pvc_registry.json is the source for /pvc/selrmc/data/REGISTRY.json (rebuilt 9 Oct; fetch it with `kubectl exec ... -- sh -c 'cat /pvc/...'`, never with a bare absolute path from Git Bash).
- Not started: C5-C7 (need B's v2 / Ledger-RM-G systems), C8 family report, MedCalc-V `self` views.
