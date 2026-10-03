# STATE role C (maintained by Claude Code)
Updated: 2026-10-03 ~16:55 UTC (Sat). Task list: FINAL_TASKS_C.md. Branch role-c, clone D:\NAACL27\selrm-role-c.

## Compute and how runs work
- NRP namespace ecepxie: own PVC selrm-c (/pvc/selrmc); B's PVC selrm-b read-only at /pvcb. Objects selrm-c-*.
- Sync pod selrm-c-sync recreated ~16:40 UTC; it expires after 6 h (~22:40 UTC): `python scripts/submit_c.py sync-down`,
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
- P0.1 TrialGPT: all required systems + summary x blocks, seeds verdict-blocks-s2 / verdict-triplets-s1;
  docs/TRIALGPT_RESULTS.md (seed table, threshold sensitivity). Comparison (6) not supported.
- P0.2 + P1 training-free rows (docs/RESULTS_C.md): critic 27.1, prompted summary 67.5, prompted ledger strict 0.1 /
  format-normalised 59.5, default correction 26.4, generated-program verifier 89.8 (1,000-triplet subset); MR / XA
  in summaries (score.py --write-summary). Reference C-REF-extract-program 2.1 (vocabulary, see handoff).
- P0.3 metrics; P0.5 trigger tagger (77.7).
- Audit PRMs merged: C-AUD-medprm 11.9, C-AUD-meds3 10.0, C-AUD-fover 31.8 (rule sets, xr_v1, MedEinst, key pairs).
- Clinical: MedEinst (docs/MEDEINST_RESULTS.md; comparisons (4), (5) in results_git/C-ME-comparisons.json with
  label-pair clusters: primary negative), key pairs (docs/KEYPAIRS_RESULTS.md), NLI4CT-P (docs/NLI4CT_RESULTS.md).
- Diagnostics: C-DG-shift (9B judge, verdict x blocks, Med-PRM), C-DG-noise, C-TF-critic/diagnostics.json;
  probe results_git/C-DG-probe/probe.json (activations in scratch/probe, sha256 checked).
- Clinical training pairs for B; Med-PRM per-example scores for B's premise gate (handoff 3 Oct).

## In progress (16:55 UTC)
- C-AUD-genprm--p1 (re-queued; 24gbf runner, 12 h), C-AUD-thinkprm--p2 / --p3 (l40 / a6000 runners, 12 h).
- C-ME-ledger2-blocks-s0, C-NL-ledger2-blocks-s0, C-NL-ledger2-triplets-s0 (c_long2 24 GB runners);
  C-ME-promptsum, C-ME-promptledger (+ -lenient rejudge) on the >= 30 GB c_long2 runners (32gb, l40).
- C-ME-ledger2-triplets-s0-lenient (POST HOC re-read) on the c_tf_rule 24gbf runner.

## Next
1. As runs land: pull; merge C-AUD-genprm / C-AUD-thinkprm parts; score.py --write-summary; eval_clinical medeinst /
   nli4ct; report_c.py; handoff the remaining rows.
2. API audit when COMPUTE REQUEST #1 is granted (run ids C-AUD-closed-1/2/3, C-AUD-llama70b, C-AUD-kimi-k3;
   references C-REF-closed-zero / -closed-ledger; closed extractor for C-REF-extract-program).
3. More systems when B registers them (ledger2-balanced, B-TR-*): C-TG-<x>, C-ME-<x>, C-KP-<x>, C-NL-<x>.
4. P0.4 ec_v1 / challenge_v1 / rewrite_v1 when A freezes them.

## Notes
- Runner jobs die at their --hours deadline (activeDeadlineSeconds); generative PRM parts need 12 h.
- Large files from the PVC: split -b 20000000 on the pod, copy chunks with kubectl exec sh -c cat, check sha256
  (a single kubectl exec stream breaks above ~75 MB).
- Old runners (code before generation 3) ignore min_gen: put generation-gated runs in task files only new runners read.

## Local scratch (not in git; .git/info/exclude)
scratch/rv1 (rule_v1 eval records), scratch/acode (A 59034a3), scratch/acode_xr (A 2df9308 + KNOWN_ISSUES.json from
bf51d94), scratch/bcode (B ac524e8), scratch/bres (B's dev_missing scores), scratch/topk, scratch/venv_ctx,
scratch/qwen35_tok, scratch/verify_ids.json, cache/api.

## Open compute requests
- #1 (3 Oct): OPENROUTER_API_KEY (API judges: three closed flagships, Kimi K3, Llama-3.3-70B; references).

## Blockers
- GPUs: the cluster is full (many pods pending); >= 40 GB cards scarce (ThinkPRM, prompted MedEinst).
