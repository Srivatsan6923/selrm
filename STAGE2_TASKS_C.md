# STAGE-2 TASKS C (evaluation) -- 8 Oct 2026

## Paste this into your Claude Code session
> Read `README.md`, `STAGE2_ANALYSIS_PLAN.md`, `STAGE2_SPEC.md` and
> `STAGE2_TASKS_C.md`, then Sections 6.4-6.5 and Appendices A, D, E and G of
> `paper/latex_v14/main.tex`. These files replace `FINAL_TASKS_C.md`. The
> frozen decisions in `CLAUDE.md`, `docs/INTERFACES.md` and
> `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute, credentials, or a decision listed in `HUMAN_TASKS_STAGE2.md`. Do
> the tasks in the order given. Start by reconciling `docs/STATE_C.md` with
> this file. A test set is scored once per system and condition, after it is
> frozen; reruns only after a crash, logged. Interface decisions are made on
> the development portions of the spec. Log decisions in
> `docs/DECISIONS_C.md`, publish outputs through `docs/HANDOFFS.md`, keep
> `docs/STATE_C.md` current.

## Context
You produce the numbers that decide the paper's main open claim. The primary
comparisons and their decision rules are in the analysis plan; apply them as
written. Four of the six comparisons need no new model: (7), (8), (9) and
(11) use the stage-1 verdict adapters, five seeds each, and the critic.

Expect either outcome. On rule-tier criterion claims the triplet-trained
verifiers are at 97.7 or more, the backbone at 83.9 and the blocks-trained
verdict model at 53.5-66.5. Whether that pattern appears on clinical notes
is not known.

## C1. Rule-tier controls  (now; no dependency)
Views `rule_v1/test_L2@none` (rule text removed) and `@wrong` (the rule of
another group, chosen by a seeded rule so that its text does not mention
the claims) via `scripts/crit_views.py` (write the `rule_v1` handler if A
has not). Systems: critic,
`verdict_blocks_s{0..4}`, `verdict_triplets_s{0..4}`, `summary2_triplets_s0`,
`ledger2_triplets_s{0..4}`. Report TA, Rev, Hold with the rule, without it
and with the wrong rule; split by rule source (hand-written, sampled,
invented names), because a claim of a hand-written rule can be guessed from
medical priors. Then `xp_v1` when A registers it: rate of changed verdict
signs under program-preserving paraphrase, next to the rate under
presentation edits of the case and a rerun. Output: `docs/STAGE2_RESULTS.md`
section 1; the two rule-tier values and the paraphrase value of Appendix E.

## C2. MedEinst: executor audit  (after A2 posts the renderer; before any
model sees a derived criterion)
1. Sentence table. MedEinst narratives are bullet lists in a fixed wording.
   Check on the reference (train) split whether `case_id` links a control
   case to its DDXPlus patient (age, sex, pathology and findings agree). If
   it does, induce the table sentence -> evidence code from linked reference
   cases; if not, build it from the question texts and report how.
   Trap sentences that match no table entry go to a lexical matcher whose
   threshold is fixed on the reference split; report the shares matched
   exactly, by the matcher, and unmatched. No model in the executor.
2. Executor: narrative -> evidence codes -> the stated procedure -> A, B or
   undecided. Report on all 5,383 test pairs: control, trap and pair
   accuracy, share of pairs decided, by label pair. Also a string-match
   baseline that counts hits in the two exclusive lists.
3. Hand D the two numbers. D records the gate: fewer than half of the pairs
   decided means comparison (11) is dropped.
The research notes saw 9 test pairs: 8 trap cases still contained findings
listed for the control diagnosis only and 1 contained a finding listed for
the trap diagnosis only. A low executor accuracy is a likely result and is
reported as the bound on what a rule-follower can gain.

## C3. MedCalc-V  (after A1)  -> comparisons (7), (8), (9)
1. Views `none`, `stated`, `self`, `wrong` of `criteria_test` and
   `edits_test`. The self-written definitions are generated once from the
   score name, hashed and frozen first; prompt chosen on `mcv_v1/dev`.
2. Score critic and the ten verdict adapters under `none` and `stated`.
   Compute (7), (8), (9) with notes as clusters; (7) and (8) use balanced
   accuracy, and accuracy on items that score points and on items that
   score none is always printed next to it. Write them to
   `results_git/C-S2-comparisons.json` and post the decision input to D.
3. Then the secondary cells: `self` and `wrong`; note type; stratum;
   `natural_band_test`; `ruleside_test` (crossed accuracy, and the rate at
   which a system follows the altered threshold); stage-1 two-stage systems
   under `stated` for reference; B's adaptation arms on held-out and seen
   scores; Ledger-RM-G when B registers it.
4. Report malformed-record rates and prompt lengths per system.

## C4. Derived criterion  (after C2 and A2)
- If the executor gate passes: MedEinst test pairs under `none`, `derived`,
  `self`, `wrong` (lists exchanged) for critic, `verdict_blocks`,
  `verdict_triplets` (five seeds), Ledger-RM-G; controls: criterion of an
  unrelated pair, neutral diagnosis labels, lists without the procedure.
  Comparison (11) with the 134 label pairs as clusters. Also report the
  pairs the executor decides, marked post hoc.
- In either case: `kb_v1/triplets_test` for the same systems and conditions
  (TA, Rev, Hold; the tagged items where a family or past finding counts).

## C5. Class triplets  (after A4 and B2-B3)  -> comparison (10)
Learned verdict (`v2_verdict_triplets`), learned verdict with the member
list, gate; closed book and open book kept apart; by domain, class size and
name type (ingredient, brand, synonym). Linking accuracy and abstention
separately from verifier accuracy.

## C6. Registered criteria, windows, TrialGPT  (after A6 and B3)
- `reg_v1/test`: stage-1 systems, `v2` systems, Ledger-RM-G with
  `reader_bit`, `gate`, `gate_struct`; windows with and without the date
  check; `wrong` = another criterion of the same trial and type.
- `xr_v1` (frozen): Ledger-RM-G with the three variants; the window column
  is the one to watch (stage 1: ledger 68, bit reader 91).
- TrialGPT test portion: Ledger-RM-G under `stated` and `wrong`; critic under
  `wrong`. Same protocol file as stage 1; interface decisions on the
  10-patient development portion only. Also fill the evidence-sentence
  precision and recall for the ledger trained on triplets.

## C7. Key pairs  -> comparison (12)
`keypairs_medqa` and `keypairs_careqa`: Ledger-RM-G as deployed (no
criterion; record its routes), under `self` and under `wrong` (the
self-written text of another pair). Self-written texts are generated from
the option set without the vignette, hashed and frozen first; prompt chosen
on MedQA-train key pairs. Comparison (12): non-inferiority to
`verdict_triplets` at a margin of two points.

## C8. Family, report, handoff
`results_git/C-S2-comparisons.json`: estimate, interval, p, Holm-adjusted p
for (7)-(12), with the family reduced to five if (11) is dropped.
`docs/STAGE2_RESULTS.md`: one section per tier with the ladder cells of
Table 14, the secondary analyses of the plan in its order, and for every
number the result file. A sentence per decision rule: which branch applies.

## C9. Stage-1 cells still red that are yours  (interleave; list in
`RED_CELLS.md`)
- Audit table: ThinkPRM parts 2-3 and the merge of part 1 (it is local-only
  and not on origin; push it), GenPRM part 1 and the crossed-accuracy
  summary of part 2, Rev and Hold and criterion-claim TA for default
  correction, criterion-claim TA for the generated-program verifier,
  MedEinst for prompted summary and prompted ledger, key pairs for prompted
  ledger and default correction.
- Transfer table: clinical columns for the FoVer-data, rationale, natural,
  balanced, clinical-pairs and triplets-plus-clinical-pairs rows as B
  registers them; MedEinst for ledger x blocks; NLI4CT-P for both ledger
  systems and the prompted rows; key pairs for summary x blocks.
- Diagnostics: shift classes for the remaining signals; denominators per
  near-miss kind and near-miss correctness given a correct base judgment.
- NLI4CT-P eligibility-section slice from stored scores (no new runs).
- Larger open and closed judges when an API key or an 80 GB GPU exists. If
  neither arrives, tell D; the paper then says "not scored".
- Confirm for D: the TrialGPT label mapping against the evaluation script,
  the item set of the "choice" column, the one-directional key-pair rule in
  one sentence, the denominator pairs of the shift ratio.

## Stop rules
- A set is not frozen, or its manifest lacks the shortcut validation: do not
  score it.
- A system fails on format (more than 20% malformed records on a tier):
  report the rate; do not re-parse leniently for the primary row. A lenient
  row may be added, marked post hoc.
- A comparison comes out against the expectation: report it and apply the
  decision rule. Do not add analyses to rescue it.
