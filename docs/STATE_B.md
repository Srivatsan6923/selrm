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
- B1 gate library: DONE for rule_v1/dev. selrm/crit_parse.py, selrm/link.py, selrm/gate.py, tests/test_gate.py
  (boundary day in both conventions), scripts/gate_dev.py (results_git/B-S2-gate-dev/summary_<set>.json; rule_v1/dev:
  parser coverage and agreement with the program on every unit). TODO when A registers them: rule_v2/dev, reg_v1/dev,
  mcv_v1/dev (parser; precision against `struct` needs A's struct format, asked in HANDOFFS), cls_v1/dev (linker
  top-1, top-10 recall, abstention; choose and verify the encoder then), unit conversion in gate.value_check.
- B2 training on rule_v2: blocked on A5 (rule_v2 not registered). Needs a stage-2 record format in selrm/formats.py
  (date in `time`, `concept`, `applies`; judge prompts record-only and record+case, half each) and queue rows.
- B3 Ledger-RM-G: after B1 and B2. Validation stop rule (0.5 TA on rule_v2/dev and rule_v1/dev).
- B4 adaptation arms: QUEUED 9 Oct (configs/queues/v2/b_mix.json, prepped; B-MIX-{blocks,triplets}-s0..2, priority
  12-14, max_len 3072). mcv_v1/adapt_blocks, adapt_triplets and dev are on the PVC (registry copy:
  scratch/registry_rule_v1.json; local records under scratch/role_a_s2/data/mcv_v1). When done: pull,
  register as mix_blocks_s*/mix_triplets_s* (add the alias rule to register_adapters.py), HANDOFFS to C.
  New data from A: `submit_b.py fetch-ref origin/role-a [path=url=sha256 ...]`, then `restore-data <sha12>
  <set,set,...> <builder>`.
- Next unblocked step: parser on mcv_v1/dev (gate_dev.py reads meta.criterion_holds; mcv records have struct
  and meta.points instead, so it needs a small adapter), precision against struct.
- B5 handoffs: adapters line sent 9 Oct; resources per configuration after B2.
- Carry-over: Qwen3.5-4B cells (3, queued, the runners take them), 6 B-NS-xr_v1-B-AUX evals (queued); diversity
  curves (39), seeds 1-2 of non-core ablations: not queued, to be run when GPUs are idle after B2-B4 or reported to D.

## GPUs
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
- #1 CLOSED 9 Oct (lead's handoff and the user): `selrm-github-ro` (key token) exists; `hf-token-srivatsan` (key
  token) is the user's and B may use it. Publishing kept adapters to a private HF repo
  (`submit_b.py publish <owner>/selrm-adapters --secret hf-token-srivatsan:token`) needs the HF account name;
  asked 9 Oct. Not blocking: C mounts PVC selrm-b read-only.

## Blockers
- A: rule_v2 (A5), mcv_v1 (A1), onto_v1 / cls_v1 (A4), reg_v1 (A6); the `struct` and onto_v1 file formats.
- Stage-1 S1 aux grid (NLI4CT, MedEinst dev splits from C) is not part of the stage-2 plan and is not pursued.
