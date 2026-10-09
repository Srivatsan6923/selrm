# FINAL TASKS B (training) -- 3 Oct 2026

## Paste this into your Claude Code session
> Read `FINAL_TASKS_B.md`. It replaces every earlier directive, scope file
> and run-matrix priority for role B. The frozen decisions in `CLAUDE.md`,
> `docs/INTERFACES.md` and `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute or credentials. Do P0 in the order given, then P1. Rules for all
> roles: `rule_v1` is frozen and is never edited or regenerated; every new
> dataset gets a new name, a manifest and a shortcut-validation result and is
> frozen before any model is scored on it; nothing is tuned on a test set;
> every run keeps per-example scores and reader outputs; every number in a
> table comes from a results file. Seed-0 results are provisional: do not
> change the paper's design because of them. Log decisions in
> `docs/DECISIONS_B.md`, publish outputs through `docs/HANDOFFS.md`, keep
> `docs/STATE_B.md` current.

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
1. **Analyses on existing predictions** -> `docs/ANALYSIS_B.md`:
   paired ledger-minus-summary difference (triplets kept together, rules as
   clusters) and the disagreement table by near-miss kind; check that no
   generated summary or ledger contains a verdict; program-supplied ledger as
   a 2x2 transition table (rescued, broken, unchanged); rule program applied
   to the predicted ledger; macro-averages over rules and families; reversal
   and near-miss correctness for the natural and balanced runs; budget table
   (cases, reader and judge targets, tokens, steps, wall time); whether
   donor-ledger resampling was active; field interventions on the ledger x
   triplets adapter (edit subject, status or time in a correct ledger; swap in
   the ledger of another case) and the share of verdicts that follow.
2. **Summary x blocks**, seed 0 (the missing cell of the central baseline).
3. **Seeds 1-2** for verdict, summary, ledger x {blocks, triplets}.
4. **Summary pipeline whose judge also sees the case**, x triplets.
5. **Leave one near-miss kind out:** {verdict, summary, ledger} x
   {subject, time, boundary}, evaluated on that kind.
6. Evaluate every kept and new adapter on `xr_v1`, `challenge_v1`,
   `rewrite_v1`, `ec_v1` as A registers them. Register adapters for C and D.

## P1 (the rest of v10's training, in this order)
Remaining cells of the training data x representation table at seed 0
(value ledger row, summary row, natural and balanced cells), then seeds 3-4
of the core cells. Ablations: decision field; bit-only judge; bit-only
reader; condition derived by the reader; verification pass; concept scorer;
premise gate; probe re-weighting (an adaptation of DynaCF, say so); no
presentation edits; no resampling; pairwise loss. FoVer-data row.
GenPRM-style verifier. The "with medical data" rows of the transfer table:
ledger on triplets + step-error data (only if C confirms MedPRMBench is
released), on clinical pairs only, and on triplets + clinical pairs (training
data from C); MedEinst with held-out diseases (3 runs). Folds 2-3. Diversity curves. Second backbone on the
four verdict/ledger cells. Step check for D. Non-core runs are evaluated on
dev, L2 and the new sets only.
