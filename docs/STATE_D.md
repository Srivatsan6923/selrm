# STATE role D (lead; maintained by the D session)
Updated: 2026-10-03 ~19:10 UTC (Sat). Plan of record: FINAL_TASKS_D.md (repo root).

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
- Pools: all five done and pulled (D:/NAACL27/d_pools, checksummed); selection committed: D-CAL, D-POOL-*,
  D-SEL-* (sel/medqa, careqa, medeinst, keypairs), D-SEL-comparisons.json, D-SELN (curve). Re-run (deterministic):
  python scripts/select_eval.py --pools D:/NAACL27/d_pools/pools --scores D:/NAACL27/d_pools/scores --out results_git
- Clinical-pairs ledger (Table 5 caption): when B-TR-tripclin-s0 is DONE with its adapter on B's PVC, run
  `submit_d.py gpu tripclin --gpu h100-opp --models "" --gpu-mem 64Gi --hours 10 -- k8s/tripclin_d.sh 1`
  (merge, validation with the fixed criteria, then every pool + swaps + key-pair extension), pull the scores, then
  `select_eval.py ... --ledger tripclin` (rows -rule keep the rule-only model; DECISIONS_D 3 Oct).
- GRPO (D-RL-*, seed 0, 1,000 steps, Qwen3.5-4B LoRA, group 8; k8s/grpo_d.sh): committed outcome (pairs 88.7 ->
  96.7) and stepcheck (88.0 -> 38.7, exploited); refgraph running (step 800); ledger2-triplets and ledger2-blocks
  running since ~18:40 UTC on one H100 each (ledger server on the same GPU: server 32%, rollouts 22%,
  --max-num-seqs 256), about 20 s/step. Finished runs started before per-example outputs need
  `k8s/grpo_d.sh <reward> <run> --eval-from base /pvc/grpo/<run>/ckpt/checkpoint-1000` (24 GB GPU), then pull with
  `submit_d.py pull /pvc/grpo/<run> D:/NAACL27/d_pools/grpo --exclude ckpt` and copy summary, curve, groups, meta,
  eval_step*.jsonl, DONE into results_git/<run>. Ledger runs write eval_step*.jsonl themselves.
- Claims audit of v13: docs/CLAIMS_AUDIT.md (872 statements; 98 contradicted, 50 partly; read main.tex at c43e751).
- Sync pod selrm-d-sync recreated 16:45 UTC (expires ~22:45 UTC; `submit_d.py sync-down` then `sync-up`).
- Lessons: cross-region CephFS reads ~5 MB/s (jobs require their PVC's region); vLLM needs
  VLLM_USE_FLASHINFER_SAMPLER=0; transformers 5 apply_chat_template(tokenize=True) returns a dict (tokenise the
  rendered text); argparse keeps '--' (the launcher strips it); a pod mounting the same PVC twice (rw + ro) hung in
  ContainerCreating; opportunistic H100s are usable; a ~30 MB raw tar through kubectl exec was cut short (pull now
  packs, checksums and retries); Qwen3.5 LoRA checkpoints from TRL need the image-text class to load (the text-only
  class silently ignores the adapter); in Git Bash export MSYS_NO_PATHCONV=1 before kubectl exec with /pvc paths.
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
