# STATE role D (lead; maintained by the D session)
Updated: 2026-10-03 ~11:45 UTC (Sat). Plan of record: FINAL_TASKS_D.md (repo root).

## Where D works
- Clone `D:/NAACL27/selrm-role-d` (github Srivatsan6923/selrm): D's work on `role-d`; publish with
  `git push origin role-d:main` (main = role-d + merges). Daily merges in a separate worktree
  (`git worktree add D:/NAACL27/selrm-merge main`; resolve append-only tables with `scripts/union_merge.py`,
  code conflicts in favour of the file's owner). `D:/selrm` is role A's tree: never use it.
- Verified rule_v1 records in `data/rule_v1/<eval set>/records.jsonl` (gitignored) and, all 44 sets of 2 Oct,
  in `D:/NAACL27/rule_v1_rebuild/`. LaTeX: tectonic at `D:/NAACL27/tools/tectonic.exe` (set TECTONIC).
- NRP (namespace ecepxie): PVC `selrm-d` (/pvc), B's PVC read-only (/pvcb). Launcher `scripts/submit_d.py`
  (`export MSYS_NO_PATHCONV=1` in Git Bash). Env `/pvc/env/selrm-d-env-v1.tar` (vllm 0.30.0, torch 2.13.0 cu130,
  transformers 5.18.0, peft 0.21.2). Sync pod `selrm-d-sync` (6 h max; recreate with sync-up). Merged ledger
  models `/pvc/merged/B-F-ledger2-{triplets,blocks}-s0`; Med-PRM `/pvc/models/dmis-lab--llama-3.1-medprm-reward-v1.0`.
  GPU jobs: `gpu NAME --gpu 24gb --n-gpu 2 ... --tp 2` (two 24 GB cards, tensor parallel) schedules fastest;
  48 GB cards were saturated on 3 Oct. vLLM needs VLLM_USE_FLASHINFER_SAMPLER=0 (set by the launcher).

## Done
- P0.1 merges 1-4 (main 1c11383: 85 tests; rule_v1 hashes unchanged; scored sets frozen); STATUS_BOARD; change
  requests answered/filed (open: tooling markers, A/B/C). Key-pair decision: C's one-directional sets
  (keypairs_medqa_oneway 357, keypairs_careqa_oneway 225) for every key-pair column (DECISIONS_D 3 Oct).
- P0.2 make_tables.py (keys, seeds, pooled CIs, C's paired_test/holm, MR, near-miss decisions, macro); tables/.
- P0.3 update_paper.py, build_paper.py; v13 wired (docs/PAPER_NUMBERS.md). Build fails while placeholders remain.
- P0.4 error sheets, citation checklist, development timeline (docs/TIMELINE.md, scripts/timeline.py --check).
- P0.5 length plan (docs/LENGTH_PLAN.md).
- P1: D-RES; pool/scoring/selection code; merged-adapter validation passed (D-VAL-ledger2-triplets-s0).
## In progress
- Pools (k8s/pool_pipeline_d.sh <pool> <tp>; one site per pool; scores in /pvc/scores/<pool>/<scorer>.jsonl):
  - medqa_dev: done and scored; pulled to D:/NAACL27/d_pools (checksummed); D-CAL committed (results_git/D-CAL:
    Platt scaling; Med-PRM dev AUC 0.65, ledger 0.51/0.48).
  - medqa_test: running on a west H100 (selrm-d-pipe-medqa-test-13393, since 08:50 UTC).
  - medqa_kp (714 key-pair questions; then 64 samples on 150 pairs): running on a west H100
    (selrm-d-pipe-medqa-kp-16468, since ~09:05 UTC; k8s/kp_pipeline_d.sh).
  - careqa_en: done; selection committed (results_git/D-SEL-*/summary_sel~careqa.json).
  - medeinst_test: running on a west H100 (selrm-d-pipe-medeinst-test-18983).
  Rates per 8,000 traces on H100: 343 s generation, 306 s Med-PRM, 1,051 s ledger.
- GRPO (ROLE.md: Qwen3.5-4B LoRA; rewards outcome, refgraph, stepcheck, ledger2-blocks, ledger2-triplets; group 8):
  setup check passed (results_git/D-RL-setup-outcome: 64-prompt overfit, ~26 s/step on H100; untrained policy at
  89.3% on held-out pairs). Queued on h100-opp, seed 0, 1,000 steps (k8s/grpo_d.sh; checkpoint + resume every 200):
  selrm-d-grpo-{outcome,refgraph,stepcheck}-s0-*; ledger2-{blocks,triplets} (2 GPUs each) after the pools.
  Outputs /pvc/grpo/D-RL-<reward>-s0 -> pull (without ckpt/) into results_git/.
- Sync pod selrm-d-sync recreated 09:25 UTC (expires ~15:25 UTC; `submit_d.py sync-down` then `sync-up`);
  the central sync pod is deleted (all pools run in the west).
- Lessons: cross-region CephFS reads ~5 MB/s (jobs require their PVC's region); vLLM needs
  VLLM_USE_FLASHINFER_SAMPLER=0; transformers 5 apply_chat_template(tokenize=True) returns a dict (tokenise the
  rendered text); argparse keeps '--' (the launcher strips it); a pod mounting the same PVC twice (rw + ro) hung in
  ContainerCreating (central mounts once); opportunistic H100s (priorityClassName opportunistic) are usable.
## Next
1. When a pool's scores exist: `submit_d.py pull /pvc/pools/<pool> <local>` and /pvc/scores/<pool> (central:
   --site central), run select_eval.py (D-CAL needs medqa_dev; medqa_kp gives sel/keypairs and D-SELN), then
   make_tables, update_paper, results_summary; commit results D-CAL, D-POOL-*, D-SEL-*, D-SELN.
2. If the pools are still pending around 12:00 UTC: COMPUTE REQUEST for a Colab 96 GB GPU session (STATE plan).
3. Daily merge (worktree D:/NAACL27/selrm-merge), board, results summary; Mon 5: schedule ladder incl. the GRPO
   decision (scripts/grpo_d.py ready, env v2); Wed 7 run freeze; Thu 8 RESULTS_SUMMARY; Sat 10 final audit.
4. Human decisions on the board: H7a framing (C's TrialGPT report is in), H7 gates, H6 prose incl. key pairs.
## Open compute requests
- none. If NRP stays saturated for the pools, ask for the Colab 96 GB GPU session (COMPUTE REQUEST).

## Blockers
- Table 5 MedEinst column: C's MedEinst runs are separate; D's MedEinst pool is its own 500 pairs (pending GPU).
- Closed-judge row of Table 5: needs an API key (C's COMPUTE REQUEST #1).

## Schedule
- P0 on time. Run freeze Wed 7 Oct 23:59; final audit Sat 10 Oct.
