# FINAL TASKS A (data) -- 3 Oct 2026

## Paste this into your Claude Code session
> Read `FINAL_TASKS_A.md`. It replaces every earlier directive, scope file
> and run-matrix priority for role A. The frozen decisions in `CLAUDE.md`,
> `docs/INTERFACES.md` and `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute or credentials. Do P0 in the order given, then P1. Rules for all
> roles: `rule_v1` is frozen and is never edited or regenerated; every new
> dataset gets a new name, a manifest and a shortcut-validation result and is
> frozen before any model is scored on it; nothing is tuned on a test set;
> every run keeps per-example scores and reader outputs; every number in a
> table comes from a results file. Seed-0 results are provisional: do not
> change the paper's design because of them. Log decisions in
> `docs/DECISIONS_A.md`, publish outputs through `docs/HANDOFFS.md`, keep
> `docs/STATE_A.md` current.

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
1. **Audit of `rule_v1`** -> `docs/DATA_AUDIT_rule_v1.md`, `tables/data_stats.json`.
   - Manifest per rule: source or specification, displayed text, program,
     applicability semantics, tests, version; verbatim source / simplified
     source / synthetic.
   - Target-claim check on every test group, including composite rules and
     missing inputs. Violations go to `data/rule_v1/KNOWN_ISSUES.json`.
   - Structure statistics (distinct normalised structures, conditions per
     judgment, depth, mentions, competing mentions, temporal / numeric /
     exception operations, per family in train and L2).
   - Overlap between train and each test set: program, normalised structure,
     subexpression, template, cue phrase, relative name, base state.
   - Composition of L3-alt; requirements table that replaces the "hard" label.
   - Who reviewed the 450 groups (people or model agents) and what they
     checked. Sample sheet of 300 groups for the authors' reading.
   - The semantics actually implemented: several mentions, conflicting
     values, units, threshold inclusivity, reference date, window boundaries,
     omitted information.
2. **`xr_v1` rule-side items.** Case fixed; only the applicability clause of
   the rule changes: time window, currency, subject, boundary inclusivity.
   Both directions, both labels, several phrasings. One item = two rules x
   three cases; solved only if all six are right. Validation: a scorer that
   ignores the rule text, one that never counts the contested form and one
   that always counts it solve 0 items. Modified registered criteria are
   labelled as synthetic interventions.
3. **`challenge_v1` kit** for author-written cases (160 groups, 32 per
   near-miss kind): state specifications, writing form, assembler, labels
   from the program, second-author check field.
4. **Corpora for B:** `train_triplets_no_{subject,time,boundary}`,
   `train_triplets_nm{05,12,25}`.
5. **`ec_v1` registered eligibility criteria** (evaluation set only): source
   trial ID, original wording, every simplification, program, boundary and
   time tests, reasons for exclusions; only criteria with unambiguous
   executable semantics; exclude trials and criterion texts in the TrialGPT
   annotations (IDs from C); sign-off sheet for the authors; rendered cases
   checked as well as programs.
6. **`rewrite_v1`:** model rewrites of L2 triplets; only groups whose state
   two extractors recover are scored; rejected groups are an audit file.

## P1 (v10 items that remain yours)
Folds 2-3 and diversity corpora stay registered for B. Check-code renderer
for the GenPRM-style verifier and reference graphs for the graph reward.
MedCalc-Bench calculators as a separate named set if time allows. Appendix B
and C text from the audit.
