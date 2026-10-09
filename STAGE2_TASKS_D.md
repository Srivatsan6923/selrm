# STAGE-2 TASKS D (lead: integration, tables, paper, policy training) -- 8 Oct 2026

## Paste this into your Claude Code session
> Read `README.md`, `STAGE2_ANALYSIS_PLAN.md`, `STAGE2_SPEC.md`,
> `STAGE2_TASKS_D.md`, `RED_CELLS.md` and `HUMAN_TASKS_STAGE2.md`, then the
> whole of `paper/latex_v14/main.tex`. These files replace
> `FINAL_TASKS_D.md`. The frozen decisions in `CLAUDE.md`,
> `docs/INTERFACES.md` and `docs/AUTONOMY_PROTOCOL.md` still apply. Work
> autonomously; ask me only for compute, credentials, or a decision listed in
> `HUMAN_TASKS_STAGE2.md`. Start by reconciling `docs/STATE_D.md` with this
> file. You update numbers and tables in the paper from result files. You
> never change a claim on your own: a change of wording that alters what the
> paper claims is prepared as a patch and applied after I approve it. Log
> decisions in `docs/DECISIONS_D.md`, keep `docs/STATE_D.md` and the status
> board current.

## Context
v14 reports stage 1 as measured, withdraws the zero-shot medical claim, and
specifies stage 2. It has 215 unmeasured values and 34 red notes.
"Finished" means: every one of them is a measured value from a result file,
or a plain sentence that the item was not run, approved by the lead; the
build with placeholders switched off passes; Sections 1-7 fit in 8 pages;
the final audit passes.

## D0. Open stage 2  (first; blocks every stage-2 test set)
1. When the lead says go (H-S2-1): commit `STAGE2_ANALYSIS_PLAN.md` unchanged
   as `docs/ANALYSIS_PLAN_STAGE2.md` on `main`. Put its commit hash into the
   stage-2 paragraph of Appendix A and remove the red note there and in
   Section 5.
2. Merge `STAGE2_SPEC.md` as one change request to `docs/INTERFACES.md`. Put
   the role files in the repository root. Tell A, B, C.
3. Record in `docs/DECISIONS_D.md`: the run freeze of 7 Oct and the dates of
   11-12 Oct are lifted (lead, 8 Oct); work is ordered by dependency.
4. Status board: one row per task of the four role files and per human task,
   with owner, status, output path; a row per gate (below).

## D1. v14 in the repository, numbers under control
1. `paper/latex_v14/` from this pack. The black numbers of v14 were typed
   from the status board of 3 Oct. Check every one against the result files:
   `docs/PAPER_NUMBERS_V14.md` with value, result key, file, commit, match.
   The paper is corrected to the files, never the reverse. List every
   mismatch in the handoff to the lead.
2. Port `scripts/make_tables.py` and `scripts/update_paper.py` to v14 (25
   tables). Replace typed numbers by result keys; `\tbd` cells become keys
   that print "tbd" until a result exists. `tables/PROVENANCE.json` as
   before. Rounding: one decimal, as printed in v14.
3. The rounding of v14 follows Python `round(x, 1)` on the stored values
   (11.95 -> 11.9, 99.35 -> 99.3). Keep one rule and state it in the
   reproducibility appendix.

## D2. Red-cell closure
`docs/RED_CELLS.md` starts as the file of this pack. After each merge:
regenerate the count from the LaTeX (`\tbd` and `\ph{`), update the owner
and status of each item, and print the remaining count on the board. An item
leaves the list only through a result file or a lead-approved "not run"
sentence.

## D3. Table shells for stage 2
Add to the paper, filled by `make_tables.py`:
- primary comparisons (7)-(12): estimate, interval, p, Holm-adjusted p,
  outcome (like Table 5);
- MedCalc-V: critic, verdict x blocks, verdict x triplets by condition
  (none, stated), note type and stratum; edits by edit type;
- gate: tier by variant (`reader_bit`, `gate`, `gate_struct`), with gate
  coverage, parser coverage and linking accuracy;
- Table 14 (criterion ladder) and the values in the text of Appendix E.
Keep them in the appendix until results exist; one of them replaces the
"not yet run" paragraph of Section 6.5 afterwards.

## D4. Gates and decision rules
| Gate | Input | You record |
|---|---|---|
| G1 | A1: scores accepted, human-written notes remaining | set size; a power note if fewer than 8 scores or 150 notes |
| G2 | C2: share of MedEinst pairs the executor decides | (11) kept or dropped |
| G3 | B3.2: composite validation | composite released to C, or stopped |
| G4 | C8: comparisons (7)-(12) | the branch of each decision rule, word for word from the plan |
Before G4, prepare both versions of each affected passage as patches in
`paper/patches/` (abstract, contribution 3, Section 6.5, conclusion,
limitations): one for "holds", one for "fails". After G4, send the matching
set to the lead for approval (H-S2-5) and apply it when approved.

## D5. Policy training (Section 6.6)
1. Collect the two ledger-reward runs; fill the two red values.
2. Seeds 1 and 2 for the five rewards (outcome, Med-PRM, reference graph,
   ledger x triplets, ledger x blocks), same setup, 150 held-out pairs.
3. Analysis of the policy trained against Med-PRM: what the collapsed policy
   writes, and whether its errors are failures to reverse (rule program on
   its outputs; 50 outputs sampled with a fixed seed for the appendix).
4. For each reward: its triplet profile (Rev, Hold, TA on L2) next to the
   policy outcome. This is the link the paper draws; keep it descriptive
   unless three seeds agree.
5. Optional, after B3: Ledger-RM-G as the reward, same setup.

## D6. Selection (Table 25)
The two swapped-vignette rows are identical in every column. Find out why
(the swap may not reach the step check's input) and fix or explain; rerun
those rows. Rerun the ledger rows with `B-TR-tripclin-s0` when it exists.
Confirm the policy model named in the caption. Closed-judge row when a key
exists. Optional: Ledger-RM-G as a selector; expectation is no gain where no
criterion is stated.

## D7. Integration and audits (continuous)
- Merge `role-a`, `role-b`, `role-c` into `main` at least daily. At each
  merge: tests pass; frozen sets unchanged (hashes); no run scored on an
  unfrozen set; every stage-2 set postdates the plan commit.
- `docs/CLAIMS_AUDIT_V14.md` after each results merge: every statement of
  v14 against the result files (consistent, contradicted, waiting).
  Contradictions go to the lead as patches, not into the text.
- Page check on every build: Sections 1-7 within 8 pages. v14 fits exactly,
  so any added line in the main text needs a line removed. Propose which.
- Sync Appendix A with the committed plan if they differ.
- Final audit: the nine checks of `scripts/final_audit.py`, plus: placeholders
  off builds; no number without provenance; licences table (CC BY-SA items
  from MedCalc-Bench carry share-alike; ATC names are not redistributed);
  the reproducibility appendix compiles in.

## D8. Kits for the authors
Sheets for H-S2-3 from A's files (100 edited MedCalc notes; 50 compiled
registered criteria; 20 rendered DDXPlus criteria); the citation checklist
extended with the `VERIFY` keys of v14; the failure sheets for stage-2
errors (100 failures of the best system on MedCalc-V edits, stratified by
edit type).

## Carry-over
Resources table (API rows when C has API runs); `docs/RESULTS_SUMMARY.md`
regenerated for v14; the development-history appendix stays the authors'
text (H6): give them the timeline, do not write it.

## Stop rules
- A result contradicts a sentence of the paper: do not soften or drop the
  result; write the patch and wait for approval.
- A role scored on an unfrozen set or before the plan commit: mark the run
  invalid on the board, ask the role to rerun after the freeze.
- The count of red items rises between two merges: find out why before
  anything else.
