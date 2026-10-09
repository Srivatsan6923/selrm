# ROLE D: downstream experiments, tables, paper, and team lead

## Lead duties (every day)
- Merge `role-a|b|c|d` into `main`; resolve conflicts in favour of the owner
  of the file (table in CLAUDE.md).
- Answer `docs/CHANGE_REQUESTS.md` within the same working block.
- Apply the schedule ladder on Mon 5 and Wed 7 Oct; record it in
  `docs/DECISIONS_D.md` and tell the other roles through `docs/HANDOFFS.md`.
- Keep `docs/STATUS_BOARD.md`: per paper item (docs/PAPER_CONTEXT.md
  section 4) -> not started / running / done / dropped, with run counts.
- Run freeze: Wed 7 Oct 23:59. After that only reruns of failed P0 items.

## Deliverables (docs/RUN_MATRIX_D.csv)
1. **D-L0** repo, shared Drive tree, registry files.
2. **D-POOL-*** candidate pools: frozen policy = Qwen3.5-9B, sampled chain of
   thought with numbered steps and a final line "Final answer: <option>";
   16 samples per question (MedQA test, CareQA, MedEinst questions), 64 for a
   fixed 300-question MedQA subset. A trace is eligible if it has a final
   answer; report the share that is not.
3. **D-CAL, D-SEL-***, **D-SELN** (Table 5, Figure 3 right).
4. **D-RL-*** policy training (appendix G).
5. **D-TAB** `scripts/make_tables.py`, `scripts/update_paper.py`;
   **D-SUM** `docs/RESULTS_SUMMARY.md`; **D-PAPER**; **D-AUDIT**.

## Answer selection
- Step scores: the step check scores each step with the vignette. The ledger
  score: the reader receives the vignette and the step and writes a ledger;
  the judge scores the step from the ledger alone. A trace's score is the
  minimum over its steps. Combined = minimum of the two after temperature
  scaling fitted on development data; also report the product and a logistic
  combination fitted on development data.
- Rows: single sample, self-consistency, step check, step check with the
  vignette of another question (swapped), ledger score, combined, combined
  swapped, combined with the ledger model trained on blocks (no near-misses),
  closed judge as selector (C's client), oracle selection.
- Columns: MedQA accuracy, CareQA accuracy, key-pair accuracy (both members
  right), MedEinst pair / control / trap accuracy. Paired bootstrap over
  questions; the 1-point non-inferiority margin is fixed in advance.
- Selection pressure: N in {1, 2, 4, 8, 16, 32, 64} on the 300-question
  subset.
- Adapters come from `configs/adapters.json` (B). Until then use provisional
  adapters trained on smoke data to build and test the pipeline.

## Policy training (GRPO)
Policy: Qwen3.5-4B with LoRA on rule-application prompts from train-level
rules ("decide and justify in numbered steps"). Rewards: outcome (rule
program), step check, ledger model trained on blocks, ledger model trained on
triplets, reference-graph coverage (A's `reference_graph`). 2 seeds, about
1-2k steps, group size 8 (verify the GRPO implementation you use). Before
each run check that reward terms are not collinear within groups and that a
64-prompt subset can be overfit. Evaluate the policy with the rule program on
held-out signature classes: accuracy on base, flip and near cases; log reward
against program accuracy over training (reward exploitation).

## Tables and paper
- `make_tables.py` reads only `results/*/summary_*.json` and
  `scores_*.jsonl`; writes `tables/*.tex`, `figures/*.pdf` and
  `tables/numbers.tex` (one macro per number used in running text).
  Missing input -> "not run". Seeds: mean and s.d.; CIs and paired tests from
  `selrm.metrics`; Holm over the four primary comparisons.
- `update_paper.py` replaces table bodies in `paper/latex/main.tex` and
  checks that no `\ph{` remains before switching to `\placeholdersfalse`.
- `docs/RESULTS_SUMMARY.md` (Thu 8 Oct): for each claim in the abstract and
  contribution list: estimate, CI, test, supported / not supported / not run,
  and the sentence the paper may state.
- Paper rewrite: docs/PAPER_CONTEXT.md section 8. A, B and C deliver appendix
  text for their parts on Thu 8 Oct.
- Final audit on Sat 10 Oct (Prompt 4 in PROMPTS.md). Submission is done by
  the human.

## Decision rules
- If B's step check is the released Med-PRM, say so in Table 5's caption.
- If selection gains are within the non-inferiority margin, report that; do
  not search aggregation rules on test data.
- Policy training is dropped first if the ladder is applied.
