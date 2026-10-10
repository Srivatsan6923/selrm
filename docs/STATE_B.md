# STATE role B
Updated: 2026-10-09 ~00:30 UTC. Plan: docs/STAGE2_TASKS_B.md with docs/STAGE2_SPEC.md (replace FINAL_TASKS_B and
NEXT_TASKS_B; the lead lifted the 7 Oct run freeze). Decisions: docs/DECISIONS_B.md. Analyses: docs/ANALYSIS_B.md.
Nothing is tuned on a test set: parser, linker, gate and prompts are developed on dev portions only.

## Stage-2 tasks
- B0 housekeeping: DONE except the L3-inv cells.
  - Every finished run is pulled, registered and resummarised (16 new: B-LC ledger2 triplets s0-s2, LOKO seeds 1-2
    of verdict and summary2, B-SC summary2 triplets s1, B-TR-tripclin-s0 valid rerun). Folds 2-3 are complete.
  - configs/adapters.json has the stage-2 names (`<format>_<corpus>_s<seed>`, alias_of = the B-F run);
    verdict_{blocks,triplets}_s0-4, summary2_triplets_s0, ledger2_blocks_s0, ledger2_triplets_s0-4 checked on the
    PVC (adapter_config.json and weights present).
  - Red cells: summary x blocks seed 4 (ANALYSIS_B 12, 13); premise gate (15); XA without the 38 known-issue items
    (12, column XA-); budget (7); B-TR-tripclin-s0 (7, 12, summaries); learning rate 1e-4, no lambda in the code
    (HANDOFFS 9 Oct). L3-inv cells of Table 20: DONE (B-NS-L3inv-*, HANDOFFS 9 Oct).
  - Gate eval mode (eval_local modes gate / gate_struct, runner GEN 5) checked on rule_v1/dev with the stage-1
    decision-field adapter: B-S2-rule_v1dev-decfield-gate-s0.
- B1 gate library: DONE for rule_v1/dev and rule_v2/dev (results_git/B-S2-gate-dev). TODO: cls_v1/dev (linker
  top-1, top-10, abstention; local copy via scratch/role_a_s3 `build_cls_v1.py --restore`, dev only), reg_v1/dev
  (needs the Leaf and Chia archives; struct form numeric/window as in rule_v2), mcv_v1/dev (struct form with
  inputs/levels/thresholds: from_struct returns None for it; needs its own reading), unit conversion.
- B2 training on rule_v2: QUEUED 10 Oct (configs/queues/v2/b_v2.json, 20 runs, prepped, min_gen 7, priority 6-12).
  Format ledger_g (selrm/formats.py). When runs finish: pull, register (add aliases v2_verdict_*, v2_reader_* to
  register_adapters.py), resummarize is not needed (runner summaries; no local copies of the test sets),
  report by near-miss kind in docs/ANALYSIS_B_S2.md.
- B3 Ledger-RM-G: round 1 failed the stop rule (rule_v1/dev, 0.67 below); the lead (user, 10 Oct) chose a second
  development round. Gate changed (DECISIONS_B 10 Oct: computes(), route reader_bit, classes linked by name).
  Requeued: configs/queues/v2/b_s2g.json (B-S2G-{gate,struct,bit,verdict}-s<k>-dev for every seed whose reader and
  verdict adapters exist; min_gen 9). When B-S2G-gate-s<k>-dev and -struct- are DONE: pull,
  `python scripts/assemble_rmg.py --validate <k>`. If seed 0 passes: queue the tests
  (make_queue_b.composite(adapters, tests=True) -> a queue file, push, prep), bring the test record files into the
  local data copy for the summaries, assemble, register ledger_rm_g_s<k> with variants, write docs/ANALYSIS_B_S2.md.
  If it fails again: stop for good and report.
- B4 adaptation arms: running (v2/b_mix.json). Done: B-MIX-blocks-s0 (mix_blocks_s0). The long-prompt runs use
  "big" settings on 80 GB cards (per-device 4, scoring batch 32).
- B5 handoffs: adapters line sent 9 Oct; resources per configuration after B2.
- Carry-over: Qwen3.5-4B cells (3, queued, the runners take them), 6 B-NS-xr_v1-B-AUX evals (queued); diversity
  curves (39), seeds 1-2 of non-core ablations: not queued, to be run when GPUs are idle after B2-B4 or reported to D.

## GPUs
- 10 Oct 07:15 UTC: composite validation, seed 0: B-S2G-bit-s0-dev and B-S2G-verdict-s0-dev are done and pulled;
  B-S2G-gate-s0-dev and B-S2G-struct-s0-dev are requeued on code 9cf63f3 (GEN 8, min_gen 8) after the linker fix
  (DECISIONS_B 10 Oct). Runners on the new code: one each h100-opp, l40, a40, a6000 (pending); the four running
  pods (two A100, two H100) are on older code and take only training runs. Then: pull, `python
  scripts/assemble_rmg.py --validate 0`. Also done and registered: v2_reader_blocks_s0, v2_verdict_triplets_s1.
- 10 Oct 06:30 UTC: v2_reader_s0 done and registered; composite validation runs queued and prepped
  (configs/queues/v2/b_s2g.json: B-S2G-{gate,struct,bit,verdict}-s0-dev, priority 4). reg_v1/dev and reg_v1/test are
  on the PVC (not yet in the B-V2 runs' eval sets: score them by eval-only runs).
- 10 Oct 05:15 UTC: done and registered: v2_verdict_blocks_s0, v2_verdict_triplets_s0, mix_blocks_s0-1,
  mix_triplets_s0-1. Running: A100 (B-MIX-blocks-s2), A100 (B-V2-verdict-blocks-s1), H100 (B-V2-reader-triplets-s0),
  H100 (B-V2-reader-blocks-s0); means 65-94% over the last 10 minutes, no LOWUTIL file. B3 is prepared:
  when B-V2-reader-triplets-s<k> is DONE, write configs/queues/v2/b_s2g.json from make_queue_b.composite(adapters)
  (add it to scratch/regen_revised.py), push, prep, run; pull; `python scripts/assemble_rmg.py --validate <k>`;
  only if it passes, composite(adapters, tests=True) and `assemble_rmg.py <k>` (test record files must then be in
  the local data copy for the summaries).
- 10 Oct 02:00 UTC: runners on code 45c7476 (GEN 7): two h100-opp, one each l40, a40, a6000, a100; the A100 runner
  of 9 Oct (GEN 6, MIX and DIV runs only) is still running. role A data on the PVC through `submit_b.py fetch-ref`
  and `restore-data` (code 8043eadcc3ad).
- 10 Oct 00:30 UTC: utilisation since the restart: A100 runner mean 87%, H100 pods 75-93%; no LOWUTIL file.
  H100 pods failed four times with CUDA out of memory in the mcv_v1/dev scoring at batch 48; "big" scoring batch is
  now 32, the failure marks of B-MIX-triplets-s0 and B-MIX-blocks-s1 were renamed old_FAILED_*, two h100-opp
  runners restarted. Done: B-MIX-blocks-s0 (registered as mix_blocks_s0), the four Qwen3.5-4B cells,
  B-DIV-base-16-s0. Running: B-MIX-triplets-s1 on the A100.
- 9 Oct 17:30 UTC: runners restarted with the user's approval and the 40% guard (DECISIONS_B 9 Oct: runner GEN 6
  stops a run below 40% over 10 min and marks LOWUTIL for that GPU model; "big" spec for 80 GB cards; staging
  limited to 12 min; us-west nodes only). Jobs: two h100-opp (max-runs 8, hours 10) and one each of l40, a40,
  a6000, a100 (max-runs 4, hours 16); 9B weights only. Check the pods' gpu_util.csv and runner.log
  ("LOW UTILISATION") under /pvc/selrm/logs at every visit; a LOWUTIL file in a results dir means the run needs
  a larger batch on that GPU model.
- `python scripts/submit_b.py runners all --n 2 --gpu h100-opp --max-runs 8 --hours 8 --models
  unsloth--Qwen3.5-9B,unsloth--Qwen3.5-4B` (opportunistic H100; code 506c27b, GEN 4).
- 9 Oct 00:50 UTC: no H100 free and the namespace's A100 quota (4) is used by other roles; pending Jobs: two
  h100-opp runners on all queues, one L40 runner on v2/b_l3inv.json. Queued: 5 L3-inv evals, 13 B-DIV seed-0 runs
  (b_x_s0.json, prepped, priority 80), 3 Qwen3.5-4B cells, 6 B-NS-xr_v1-B-AUX evals.
- 9 Oct 02:15 UTC: the H100 runner was preempted during B-BB-qwen3.5-4b-verdict-triplets-s0 (KILLED_1; it resumes
  from its checkpoint); B-BB-qwen3.5-4b-verdict-blocks-s0 is done. Pending Jobs on all queues: two h100-opp, one
  a6000, one a40 (A100 quota still full). Nothing from A, C or D for stage 2 on origin yet.
- 9 Oct ~03:40 UTC: main (3a544a1) merged into role-b (6ef936d). Running on all queues: two h100-opp runners and
  one l40 (the three Qwen3.5-4B cells first, then B-DIV seed 0 and the B-NS evals); pending: a6000, a40, h200-opp,
  rtx8000. The namespace's A100 quota (4) is held by another group's jobs; add an a100 runner when a slot opens.
  Drive D: dropped out for a while on 9 Oct (laptop); nothing lost.
- Sync pod selrm-b-sync created 8 Oct ~23:10 UTC (6 h limit): recreate with `kubectl -n ecepxie delete pod
  selrm-b-sync`, then `python scripts/submit_b.py sync-up`.
- Never run two data jobs at once. Laptop memory is tight: analysis and resummarize one at a time.

## Routine
Pull (`submit_b.py pull`), `register_adapters.py`, `resummarize_b.py <runs>`, analysis (temp file, then move),
commit and push; HANDOFFS lines for results C or D use. `python scratch/regen_revised.py` regenerates queue files.

## Open compute requests
- None. #2 closed 10 Oct: the user supplied a write token; it is the cluster secret `selrm-b-hf-write` (key token;
  never in the repo). Published to the private repo srivatsan6923/selrm-adapters: the four stage-1 headline
  adapters of configs/keep_adapters.json (job selrm-b-publish-11942; README.md of PEFT left out). To publish
  more: add run ids to configs/keep_adapters.json, then
  `submit_b.py publish srivatsan6923/selrm-adapters --secret selrm-b-hf-write:token`.

## Blockers
- A: rule_v2 (A5), mcv_v1 (A1), onto_v1 / cls_v1 (A4), reg_v1 (A6); the `struct` and onto_v1 file formats.
- Stage-1 S1 aux grid (NLI4CT, MedEinst dev splits from C) is not part of the stage-2 plan and is not pursued.
