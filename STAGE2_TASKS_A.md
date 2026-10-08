# STAGE-2 TASKS A (data) -- 8 Oct 2026

## Paste this into your Claude Code session
> Read `README.md`, `STAGE2_ANALYSIS_PLAN.md`, `STAGE2_SPEC.md` and
> `STAGE2_TASKS_A.md`, then Appendices A, B, C and E of
> `paper/latex_v14/main.tex`. These files replace `FINAL_TASKS_A.md`. The
> frozen decisions in `CLAUDE.md`, `docs/INTERFACES.md` and
> `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute, credentials, or a decision listed in `HUMAN_TASKS_STAGE2.md`. Do
> the tasks in the order given. Start by reconciling `docs/STATE_A.md` with
> this file: mark what is already done, then continue. No stage-2 test set is
> frozen before `docs/ANALYSIS_PLAN_STAGE2.md` is on `main`; write loaders,
> rule code and tests until then. Log decisions in `docs/DECISIONS_A.md`,
> publish outputs through `docs/HANDOFFS.md`, keep `docs/STATE_A.md` current.

## Context
Stage 1 is measured. Its sets stay frozen. You now build the sets on which
the paper's main open question is tested: does the verifier's selectivity
appear on clinical text when a criterion with an outside source is stated?
`mcv_v1` comes first because roles C and B can answer comparisons (7), (8)
and (9) with existing adapters as soon as it is frozen.

Every set you build has: a manifest (pins, sha256, licence, seeds, counts,
drop reasons), a shortcut-validation result, an audit file
`docs/DATA_AUDIT_<set>.md`, registry entries, and a one-line handoff.

## A1. `mcv_v1`: MedCalc-V  (first)
Source: MedCalc-Bench Verified, pinned in the spec. Rule-based subset =
categories risk, severity, diagnosis: 19 calculators, 380 test rows (230
Extracted = human-written, 150 Synthetic = model-written), 2,426 training
rows (1,669 Extracted; treat as silver).

1. **Score specifications** in `selrm/mcv/scores/<calculator_id>.py`, written
   from the score text in the instance's explanation, not from the
   repository's code. Per item: name (heading without comparators or
   numbers), point levels, predicate over the released entities, unit, and
   typed scope: subject (patient), time (`current`, `ever`, or `unstated`),
   each with the phrase of the score text that supports it.
2. **Acceptance.** The sum of item points from the released entity dictionary
   equals `Ground Truth Answer` on every test and training row of the score.
   Conventions for an absent key are taken only from the instance text (for
   example: an unmentioned finding is absent; Centor and FeverPAIN count an
   unmentioned cough as absent, which adds a point; unmentioned Glasgow Coma
   components score full). A score with any unexplained mismatch is excluded,
   with the rows listed. No row-level special cases. Report: scores accepted
   of 19, rows covered, per-score table. If fewer than 8 scores or fewer than
   150 human-written test notes remain, report it at once and continue.
   Reproduce as a check: on the 62 rule-based test rows whose note also
   occurs unchanged in the Stanford corrected labels
   (github.com/junzeye/validate-medcalc-labels,
   `data/medcalc_v1_corrected.csv`; match on calculator and identical note
   text), that set has no answer for 10 and a different answer for 9 of the
   other 52.
3. **Items.**
   - `criteria_test`: one record pair per item of every accepted score on
     every test note, with `stratum` and `note_type`.
   - `natural_band_test`: the subset of numeric items whose value lies within
     a band of the threshold fixed per input in the manifest (age 3 years,
     rates and pressures about 5-10% of the threshold), no edit.
   - `edits_test`, type `value`: numeric items whose value string occurs
     exactly once in the note and feeds no other item. Flip: a value across
     the threshold. Near-miss: a value on the same side and strictly nearer
     to it. Both inside a plausible range per input; unit kept. Skip a note
     if it restates the value in words for that input (lexicon per input:
     tachycardic, febrile, hypotensive, elderly, and so on) or gives the
     value in a second form. For interval items do not cross the other bound.
   - `edits_test`, type `sentence`: items that are not met and about which
     the note is silent (key absent or False, and no sentence matches the
     item's concept lexicon). Near-misses: the finding in a relative; the
     finding negated; the finding in the past, only for items with time scope
     `current`. Flip: the finding affirmed for the patient. For items with
     scope `ever`, a past mention is a flip. No time edits for `unstated`.
     Sentence templates are new: disjoint from every `rule_v1` training cue
     phrase (script check). One fixed insertion rule (after the history
     sentence, else end of the first paragraph).
   - `ruleside_test`: for numeric `stated` items, the score text with that
     item's threshold moved so that the note's value falls on the other
     side; label from the rule code with the altered threshold; original and
     altered text form a crossed item as in `xr_v1`.
   Labels of every edited case are recomputed by the rule code from the
   edited dictionary.
4. **Fidelity filter for edits.** Two extractors from different model
   families, neither the paper's backbone, read each edited note and must
   return the edited value, or the inserted finding with its subject, status
   and time. Keep an edit only if both agree. Report the retention rate and
   keep the rejects as an audit file. Prepare a 100-item sheet for the
   authors (kit for H-S2-3).
5. **Development and adaptation portions** from the training notes only:
   `dev` (20% of training notes, by note id), `adapt_blocks` and
   `adapt_triplets` (12,000 records each, identical notes and base cases; the
   triplets corpus replaces the base case by a near-miss in half of the
   groups). Held-out scores: seeded shuffle of the accepted scores, seed
   20261008, first 6 held out of both adaptation corpora. Deduplicate
   training against test by note id and by text hash.
6. **Validation.** Always-default, claim-only, concept-named and
   attribute-blind scorers on `edits_test` (expected TA 0 or near it; report
   what you find) and on `criteria_test` (balanced accuracy; always-default
   is 50 by construction); rule code on edited dictionaries 100. Report counts by
   score, item, stratum, note type and edit type.
7. Freeze, register, hand off to B and C. Give D the numbers for Appendix E
   as result keys.

## A2. `kb_v1`: criterion from the DDXPlus lists
1. Download the English release; check the counts in the spec; record sha256.
2. `selrm/kb_criterion.py: render(A, B)`: canonical order of the two names;
   three lists (A only, B only, both) with `question_en` verbatim;
   categorical and multi-choice findings by question only; then the fixed
   procedure sentence of Appendix E. The same text for (A, B) and (B, A).
   Commit the script and the file hashes and post the handoff **before** any
   model sees the output. Role C needs it for the executor audit.
3. Support check on validation patients: share of patients showing a finding
   outside their pathology's list; for each of the 134 MedEinst label pairs,
   share of unedited patients of A that the procedure decides for A.
4. `triplets_dev` and `triplets_test` (validation and test patients; up to 20
   patients per label pair; patient must show at least one A-only finding).
   Case text: sex, age, then one line per finding as question and answer.
   Base: the patient. Flip: A-only findings removed, one or two B-only
   findings added. Near-miss: a B-only finding answered "no", or attributed
   to a family member (only if the question is not itself about family).
   Where a B-only question is itself about family or the past, affirming it
   is a flip; tag these items. Labels by the procedure.
5. Shortcut validation (always-A, concept-named, claim-only: expected 0;
   procedure: 100). The manifest states that labels are relative to the
   lists and that flip cases are not real patients.

## A3. `xp_v1`: program-preserving paraphrases  (small)
For 300 `rule_v1/test_L2` groups: reorder commutative clauses, move the
exception clause, exchange synonyms from a list disjoint from training cue
phrases; re-render; executing the original and the transformed program on
every state of the group must give identical outputs. Cases unchanged.

## A4. `onto_v1` and `cls_v1`
1. Snapshot: HPO (ontology and `phenotype.hpoa`), Mondo, Disease Ontology;
   from RxNav: ingredients and brand names, ATC level-4 members, FDA
   established pharmacologic class members, MED-RT relations. Cache every
   API response; manifest with release identifiers and terms of use.
2. Closure tables. Drug class = a pair (ATC level 4, FDA class) whose
   ingredient sets overlap with Jaccard at least 0.5 and at least 4 common
   members. Members = intersection. Ingredients in only one of the two sets
   are excluded from all items. Combination products and ingredients with
   several class memberships are excluded. Class names shown = FDA names.
   HPO and Mondo classes: terms with 8-200 descendants; members =
   descendants with labels and exact synonyms.
3. Negatives pass the disjointness test: no subsumption either way, no
   common descendant. Near-miss = a member of a sibling class (same parent),
   or a term too general to establish membership.
4. Split classes 60 / 15 / 25 into training (used inside `rule_v2`), `dev`,
   `test`, stratified by domain; no test member name appears as a member in
   training.
5. `cls_v1/dev`, `cls_v1/test` (about 1,200 triplets, 400 per domain):
   constraint rules from the existing grammar with a class-level concept.
   Base: no member. Flip: a member under ingredient, brand or synonym name.
   Near-miss: sibling or too-general term. Views per spec section 5.
6. Validation: shortcut scorers; a scorer that matches the class word in the
   case; the program with the closure (100).

## A5. `rule_v2`: training library for stage 2
Extends the grammar; `rule_v1` is untouched.
- New clause kinds: `window` (an event within N days, months or years before
  a reference date that the case states; boundary day as the rule text
  says) and `class` (concept condition over an `onto_v1` class from the
  training classes).
- Record targets in the stage-2 format: date in `time`, `concept` id for
  class conditions, `applies` bit. `struct` on every record.
- Templates and cue phrases disjoint from every frozen test (`rule_v1`
  tests, `xr_v1`, `reg_v1`, `cls_v1/test`, `mcv_v1`); script check.
- Same protocol as `rule_v1`: signature classes, held-out classes for
  `test_L2` (2,000 triplets, all seven near-miss kinds), `dev` 300, corpora
  `train_blocks` and `train_triplets` of 60,000 records that differ only in
  near-misses, 15% missing-input and 15% presentation records.
- Also `train_triplets_lo_window` and `train_triplets_lo_class` for B.
- Audit as for `rule_v1`: target-claim check on every group (0 violations
  required), overlap statistics, shortcut validation.

## A6. `reg_v1`: registered criteria (evaluation only)
- From Chia and Leaf: single-condition criteria with a numeric threshold or
  a time window and none of the corpora's flags for unrepresentable,
  subjective or non-queryable criteria. Recount the candidates (first count
  about 450 in Leaf).
- Compile the annotation to `struct` and a program by script. Conventions
  the annotation does not fix (boundary day, reference date) are stated in
  the rule text.
- Checks: every number, unit and operator of `struct` occurs in the
  criterion text; two model sessions read criterion and program and any
  mismatch drops the criterion (state in the audit that these are model
  checks); 50-criterion sheet for the authors (kit for H-S2-3).
- Exclude trials and criterion texts of the TrialGPT annotations.
- Cases from the `rule_v2` engine with dates; three groups per criterion;
  near-misses: value toward the threshold, event outside the window,
  relative, negated. `dev` = 10% of criteria, by trial.
- `ec_v1` (95 criteria formalised by us) stays separate and unscored unless
  the authors sign it off.

## A7. Paper inputs from data you already have
Table 8 (structure statistics, train and L2) from `tables/data_stats.json`;
counts per requirement of the harder set; Rev and Hold of the four shortcut
scorers of Table 16 from the stored per-example scores; the sentence on
several mentions of a measurement (confirm against the code).

## Carry-over (when unblocked)
`challenge_v1` assemble and freeze after H2; `rewrite_v1` when an API key
exists; H1 aggregation after the authors' reading. If still blocked when the
paper is frozen, tell D, who keeps the "not used in this draft" sentence.
