# FINAL TASKS D (lead) -- 3 Oct 2026

## Paste this into your Claude Code session
> Read `FINAL_TASKS_D.md`. It replaces every earlier directive, scope file
> and run-matrix priority for role D. The frozen decisions in `CLAUDE.md`,
> `docs/INTERFACES.md` and `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute or credentials. Do P0 in the order given, then P1. Rules for all
> roles: `rule_v1` is frozen and is never edited or regenerated; every new
> dataset gets a new name, a manifest and a shortcut-validation result and is
> frozen before any model is scored on it; nothing is tuned on a test set;
> every run keeps per-example scores and reader outputs; every number in a
> table comes from a results file. Seed-0 results are provisional: do not
> change the paper's design because of them. Log decisions in
> `docs/DECISIONS_D.md`, publish outputs through `docs/HANDOFFS.md`, keep
> `docs/STATE_D.md` current.

## Context (same for all roles)
The paper is v13: v10's full design (audit of 13 signals, training data x
representation table, transfer table, ablations, candidate selection, policy
training) with review corrections. Seed 0 on held-out rule structures (L2):
verdict 58.2 (blocks) -> 91.3 (triplets); one-stage rationale 61.5 -> 91.0;
two-stage prose summary 98.0 (triplets); two-stage ledger 75.3 -> 99.2.
What reviewers will ask for first, and what therefore comes first: seeds and
paired statistics; the prose summary as a central baseline; tests the
generator does not determine (rule-side edits, author-written cases); data
audits; one external evaluation on existing expert labels.

## P0 (in order)
1. **Integration.** Merge `role-a`, `role-b`, `role-c` into `main` daily.
   Put the four FINAL_TASKS files in the repo root. `docs/STATUS_BOARD.md`:
   one line per task above with owner, status and output path. Include the authors' tasks from
   `HUMAN_TASKS.md` on the board. Check that nobody scores on an unfrozen
   dataset and that `rule_v1` hashes match. Record the framing decision after
   C's TrialGPT report (the lead decides, not an agent).
2. **Tables with provenance.** `scripts/make_tables.py` writes every table of
   v13 from `results/` only, lists each seed, prints "tbd" where no result
   exists, and writes `tables/numbers.tex` and `tables/PROVENANCE.json`
   (cell -> run -> file -> commit). Paired tests and Holm correction from
   `selrm.metrics`.
3. **Paper.** v13 sources in `paper/latex_v13/`. `scripts/update_paper.py`
   replaces table bodies and number macros only; it never edits prose and it
   lists sentences whose numbers changed by more than a point. The build
   must fail while any placeholder remains.
4. **Kits for the authors:** error-analysis sheets (200 failures, stratified
   by system and near-miss kind); citation checklist for every cited entry;
   a factual development timeline from git history (pilot generator, the
   past/family result of the pilot, the redesign, the freeze).
5. **Length.** The main text is about ten and a half pages; propose which
   paragraphs and tables move to the appendix to reach eight, without
   removing any experiment.

## P1 (v10's downstream experiments)
Candidate pools (MedQA, CareQA, MedEinst questions; 16 samples, 64 on a
300-question subset). Table 5: single sample, self-consistency, step check,
ledger score, combined (minimum, described as a heuristic; product and a
fitted combination alongside), swapped vignette, no near-misses, closed
judge, oracle; selection-pressure curve. Policy training (GRPO) with the
five rewards, evaluated by the rule program on held-out structures; this is
the only basis for statements about reward exploitation. Resources table.
Final audit on Sat 10 Oct.
