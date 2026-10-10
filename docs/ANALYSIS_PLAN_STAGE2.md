# Analysis plan, stage 2

Written 8 Oct 2026, after the outcome of stage 1 and before any stage-2 set
was built. To be committed unchanged as `docs/ANALYSIS_PLAN_STAGE2.md`; the
commit hash goes into Appendix A of the paper. Changes after the commit are
appended below a dated line and never replace text.

## Question
Is the boundary found in stage 1 (no transfer where no criterion is stated)
the absence of a criterion?

## Primary comparisons (one Holm family of six)
All are paired on identical items with a cluster bootstrap from
`selrm.metrics` (10,000 resamples, two-sided p). Ties are failures.
"Verdict x triplets" and "verdict x blocks" are the existing verdict-only
adapters trained on `rule_v1`, seeds 0-4, pooled per item as in stage-1
comparison (2). "Critic" is the untrained backbone with the verdict prompt.
No model in (7), (8), (9) or (11) is trained on stage-2 data.

| # | Set and items | Contrast | Metric | Cluster |
|---|---|---|---|---|
| 7 | `mcv_v1/criteria_test`, human-written notes, items whose input is in the released dictionary; criterion stated | verdict x triplets minus verdict x blocks | balanced accuracy of the preferred claim | note |
| 8 | same items | [triplets: stated minus none] minus [critic: stated minus none] | balanced accuracy | note |
| 9 | `mcv_v1/edits_test`, human-written notes; criterion stated | verdict x triplets minus verdict x blocks | triplet accuracy | note |
| 10 | `cls_v1/test` (classes held out from training), class named, no member list | gate (parsed criterion, linker, closure) minus learned verdict (verdict-only trained on `rule_v2` triplets) | triplet accuracy | class |
| 11 | `clin_v1/medeinst_test`, all 5,383 pairs | [triplets: derived minus none] minus [critic: derived minus none] | pair accuracy | label pair (134) |
| 12 | `clin_v1/keypairs_medqa` (357 pairs), no criterion | Ledger-RM-G as deployed minus verdict x triplets | pair accuracy; non-inferiority, margin 2 points | question pair |

Balanced accuracy is the mean of the accuracy on items that score points
and on items that score none, so that a system that always prefers "no
points" is at 50%.

Expectations: (7) > 0, (8) > 0, (9) > 0, (10) > 0, (11) > 0, (12) lower
bound of the 95% interval above -2.

In (12) the composite has no criterion to read, abstains and falls back to
its verdict-only score. The comparison checks that the system as designed no
longer loses what the two-stage systems of stage 1 lost (30.5-35.9 against
78.2-79.8).

## Decision rules
- (7) and (9) both fail: near-miss supervision is a result about generated
  text. The abstract and the first sentence of the conclusion say so.
- (8) shows no interaction: the trained verifier's advantage on clinical
  notes does not come from reading the criterion. Reported in those words.
- The symbolic executor of the derived criterion decides fewer than half of
  the MedEinst pairs: (11) is dropped from the family (Holm over five), and
  MedEinst is reported only as the contrast without a criterion.
- (10) fails: class conditions are left to the learned judge; the gate keeps
  quotation, value, time, subject and status.
- (12) fails: the composite is reported as harmful where no criterion is
  stated, and the verdict-only verifier is the recommended system there.

## Secondary analyses (reported, no decision rule)
1. Criterion ladder per tier: none, stated or derived, self-written, wrong;
   for the critic, verdict x blocks, verdict x triplets and Ledger-RM-G.
2. MedCalc-V by note type (230 human-written, 150 model-written), by stratum
   (stated, denied, settled by default), and values naturally near a
   threshold.
3. MedCalc-V rule-side items: the threshold of one item is altered in the
   score text so that the note's value falls on the other side.
4. Adaptation: rule triplets plus MedCalc training items with and without
   near-miss edits, equal budget, on scores held out from adaptation.
5. Rule tier: rule text removed; rule text exchanged for another group's.
6. Rule paraphrases that preserve the program: rate of changed verdicts.
7. MedEinst: executor pair accuracy and share decided; string-match
   baseline; controls (unrelated pair's criterion, lists exchanged, neutral
   diagnosis labels, lists without the procedure); results on the pairs the
   executor decides, marked post hoc.
8. Knowledge-base triplets from DDXPlus test patients.
9. Registered criteria: triplet accuracy; time windows with and without the
   date check; `xr_v1` window items with the date check.
10. Class triplets: learned verdict, learned verdict with the member list,
    gate; by class size and name type; linking accuracy reported separately.
11. Gate with the parsed criterion against the gate with the structure taken
    from the program or the annotation; parser coverage and precision.
12. Eligibility-section slice of NLI4CT-P.
13. Leave-one-kind-out for `window` and `class` near-misses on `rule_v2`:
    verdict-only against the composite.

## Selection and freezing
| Decision | Made on |
|---|---|
| MedCalc-V prompts, claim wording, edit templates, extractor thresholds | training notes of MedCalc-Bench Verified (`mcv_v1/dev`) |
| Criterion renderer for DDXPlus pairs, executor's sentence table | DDXPlus validation patients; MedEinst reference (train) split |
| Self-written criterion prompt | MedQA-train key pairs; MedEinst reference split |
| Criterion parser, linker, gate thresholds | `rule_v2/dev`, `cls_v1/dev` (classes disjoint from test), `mcv_v1/dev` |
| Held-out scores for adaptation | seeded shuffle of the accepted scores, seed 20261008, first 6 held out |

Each stage-2 set is frozen with a sha256 before any system is scored on it.
A set is scored once per system and condition; reruns only after a crash,
logged in the role's decision file. `rule_v1` is not modified.

## What would count against the thesis
- On MedCalc-V criterion claims the pattern of the rule tier does not
  reappear (rule tier: triplets 97.7 or more, backbone 83.9, blocks
  53.5-66.5).
- Removing or exchanging the criterion moves the trained verifier no more
  than the backbone.
- A derived criterion does not help where it decides the label.
If these fail, the paper is a controlled study of supervision for
rule-conditioned verification on generated cases, and says so.

---
Appended 9 Oct 2026 (the text above is unchanged)

Drug classes of `onto_v1` / `cls_v1` (comparison 10 and secondary analysis 10). Requested by role A
(docs/CHANGE_REQUESTS.md, 8 Oct) and accepted by the lead on the human lead's word, before `cls_v1` exists and
before any model has seen a class. The rule first written (a class is an ATC level-4 code and an FDA
established pharmacologic class that agree) gives 28 usable drug classes, 7 of them held out for test,
against 56 phenotype and 54 disease test classes. Amended rule: a drug class is an FDA established
pharmacologic class by its direct ingredient members, with at least 4 single ingredients that belong to no
other such class and at least 2 near-miss ingredients under role A's near-miss rule of 8 Oct
(docs/DECISIONS_A.md); 80 classes, 47 / 12 / 21 train / dev / test. Every class carries
`agreement = true|false` (its members also match one ATC level-4 code under the first rule).
Consequences, fixed now: comparison (10) is computed on all held-out test classes under the amended rule;
its metric, contrast, cluster and decision rule are unchanged. The same contrast on the classes with
`agreement = true` (the definition first written) is reported next to it as a secondary analysis, and the
paper states both definitions and that the amendment preceded the data. No new source or licence; ATC names
are still not redistributed.

---
Appended 10 Oct 2026 (the text above is unchanged)

Note on comparison (11), recorded before any model has been scored on MedEinst with the derived criterion.
The symbolic executor decides both cases of 70.1% of the 5,383 test pairs, so by the rule above (11) stays in
the family. Its pair accuracy is 0.7% (control 98.0%, trap 0.9%): on 69.5% of pairs it gives the trap case the
control diagnosis, because the trap edit removes one finding listed for the control diagnosis only and the
others stay in the case. The derived criterion therefore does not entail the benchmark's trap labels, and a
system that follows it is expected to lose on trap cases. The expectation (11) > 0 is left as written; this
note states that its failure was foreseeable from the executor alone (results_git/C-S2-executor/summary.json).
No rule, metric or set is changed.

