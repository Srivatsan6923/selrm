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
    (HANDOFFS 9 Oct). OPEN: L3-inv of FoVer data, ledger natural, ledger balanced, clinical pairs only and
    triplets + clinical pairs: eval-only runs B-NS-L3inv-<run> (configs/queues/v2/b_l3inv.json, prepped), two
    H100 runners started 00:20 UTC. After they finish: pull, resummarize_b.py, analysis, HANDOFFS line to D.
- B1 gate library: DONE for rule_v1/dev. selrm/crit_parse.py, selrm/link.py, selrm/gate.py, tests/test_gate.py
  (boundary day in both conventions), scripts/gate_dev.py (results_git/B-S2-gate-dev/summary_<set>.json; rule_v1/dev:
  parser coverage and agreement with the program on every unit). TODO when A registers them: rule_v2/dev, reg_v1/dev,
  mcv_v1/dev (parser; precision against `struct` needs A's struct format, asked in HANDOFFS), cls_v1/dev (linker
  top-1, top-10 recall, abstention; choose and verify the encoder then), unit conversion in gate.value_check.
- B2 training on rule_v2: blocked on A5 (rule_v2 not registered). Needs a stage-2 record format in selrm/formats.py
  (date in `time`, `concept`, `applies`; judge prompts record-only and record+case, half each) and queue rows.
- B3 Ledger-RM-G: after B1 and B2. Validation stop rule (0.5 TA on rule_v2/dev and rule_v1/dev).
- B4 adaptation arms: blocked on A1 (mcv_v1/adapt_blocks, adapt_triplets).
- B5 handoffs: adapters line sent 9 Oct; resources per configuration after B2.
- Carry-over: Qwen3.5-4B cells (3, queued, the runners take them), 6 B-NS-xr_v1-B-AUX evals (queued); diversity
  curves (39), seeds 1-2 of non-core ablations: not queued, to be run when GPUs are idle after B2-B4 or reported to D.

## GPUs
- `python scripts/submit_b.py runners all --n 2 --gpu h100-opp --max-runs 8 --hours 8 --models
  unsloth--Qwen3.5-9B,unsloth--Qwen3.5-4B` (opportunistic H100; code 506c27b, GEN 4).
- 9 Oct 00:50 UTC: no H100 free and the namespace's A100 quota (4) is used by other roles; pending Jobs: two
  h100-opp runners on all queues, one L40 runner on v2/b_l3inv.json. Queued: 5 L3-inv evals, 13 B-DIV seed-0 runs
  (b_x_s0.json, prepped, priority 80), 3 Qwen3.5-4B cells, 6 B-NS-xr_v1-B-AUX evals.
- Sync pod selrm-b-sync created 8 Oct ~23:10 UTC (6 h limit): recreate with `kubectl -n ecepxie delete pod
  selrm-b-sync`, then `python scripts/submit_b.py sync-up`.
- Never run two data jobs at once. Laptop memory is tight: analysis and resummarize one at a time.

## Routine
Pull (`submit_b.py pull`), `register_adapters.py`, `resummarize_b.py <runs>`, analysis (temp file, then move),
commit and push; HANDOFFS lines for results C or D use. `python scratch/regen_revised.py` regenerates queue files.

## Open compute requests
- #1 (2 Oct, also H-S2-2): read-only GitHub token secret `selrm-github-ro`; confirm `hf-token-srivatsan` is the
  user's. Until then kept adapters stay on the PVC (C mounts selrm-b read-only).

## Blockers
- A: rule_v2 (A5), mcv_v1 (A1), onto_v1 / cls_v1 (A4), reg_v1 (A6); the `struct` and onto_v1 file formats.
- Stage-1 S1 aux grid (NLI4CT, MedEinst dev splits from C) is not part of the stage-2 plan and is not pursued.
