# G4, outcome "fails": one block per decision rule of the plan

Prepared before any stage-2 result exists. Applied only after approval (H-S2-5). Each block quotes the decision
rule of `docs/ANALYSIS_PLAN_STAGE2.md` (commit 733ad25) word for word and gives the passages it changes. Blocks
combine: the base text is `G4_holds.md`, and every fired rule replaces the sentences it names. Results are
reported with their estimates and intervals whatever the outcome; nothing is dropped.

## A. "(7) and (9) both fail: near-miss supervision is a result about generated text. The abstract and the first sentence of the conclusion say so."

Abstract, replacing the sentence on sourced criteria ("We therefore make the criterion ... (not yet run).")
> On clinical notes with a published score definition this advantage does not reappear
> (\res{cmp/p7/diff} points on criterion claims, \res{cmp/p9/diff} on edited notes; neither established):
> near-miss supervision is, so far, a result about generated text.

Contribution (3), last sentence
> On real clinical notes with stated score definitions the advantage of near-miss supervision is not
> established (Section 6.5).

Section 6.5, first paragraph
> On \mcv{} the ordering of the rule tier does not reappear. On criterion claims over human-written notes
> the verifier trained on triplets differs from the one trained on blocks by \res{cmp/p7/diff} points
> [\res{cmp/p7/lo}, \res{cmp/p7/hi}], and on edited notes by \res{cmp/p9/diff} [\res{cmp/p9/lo},
> \res{cmp/p9/hi}] (Table~\ref{tab:mcv}). Near-miss supervision is a result about generated text.

Conclusion, first sentence becomes
> On generated cases from executable rules, medical reward models fail in two directions, and supervision on
> decisive evidence alone cures the first failure and produces the second; on clinical notes we could not
> establish the same.

and the last sentence is removed. Limitations, "Transfer", last two sentences become
> The experiments on clinical text with stated criteria do not establish the advantage of near-miss
> supervision. What remains is a controlled study of supervision for rule-conditioned verification on
> generated cases.

If only one of (7), (9) fails, rule A does not fire: the "holds" text is used and the failed comparison is
reported in Section 6.5 with its estimate and interval and the words "not established".

## B. "(8) shows no interaction: the trained verifier's advantage on clinical notes does not come from reading the criterion. Reported in those words."

Section 6.5, paragraph "The criterion is read" becomes
> **The criterion.** Stating the score definition changes the trained verifier by \res{cmp/p8/diff} points
> relative to the backbone [\res{cmp/p8/lo}, \res{cmp/p8/hi}]: the trained verifier's advantage on clinical
> notes does not come from reading the criterion.

Abstract (holds version): the clause "and its advantage over the untrained backbone depends on the criterion
being stated" is removed. Contribution (3): "and removing or exchanging the criterion lowers the trained
verifier more than the backbone" is removed. Conclusion: "and it depends on the criterion being stated" is
removed; the sentence "selectivity is relative to a criterion, which has to be an input with a source" is
limited to the rule tier ("On the rule tier, selectivity is relative to the stated rule").

## C. "The symbolic executor of the derived criterion decides fewer than half of the MedEinst pairs: (11) is dropped from the family (Holm over five), and MedEinst is reported only as the contrast without a criterion."

Section 6.5, paragraph "Derived criterion" becomes
> **Derived criterion.** The symbolic executor of the criterion derived from the DDXPlus lists decides
> \res{sum/C-S2-executor/test.both_decided} of the MedEinst pairs, fewer than half. By the rule fixed in
> advance, the comparison on MedEinst is dropped from the family, and MedEinst is reported only as the
> contrast without a criterion (Section 6.4).

Appendix A: "Holm-corrected as one family" of six becomes five, with the sentence above. Table 14: the
MedEinst rows under "derived" stay as secondary values, marked post hoc where they concern the pairs the
executor decides.

## D. "(10) fails: class conditions are left to the learned judge; the gate keeps quotation, value, time, subject and status."

Section 6.5, paragraph "Executable parts", first sentence becomes
> On classes held out from training the gate is not above the learned verdict (\res{cmp/p10/diff} points
> [\res{cmp/p10/lo}, \res{cmp/p10/hi}]). Class conditions are left to the learned judge; the gate keeps
> quotation, value, time, subject and status.

Section 4 (method), the sentence that lists the gate's checks, and Figure 2(c) ("gate: quotation, class,
number, date") drop the class check; Appendix F states the reason and the measured linking accuracy.

## E. "(12) fails: the composite is reported as harmful where no criterion is stated, and the verdict-only verifier is the recommended system there."

Section 6.5, paragraph "Executable parts", last sentence becomes
> Where no criterion is stated the composite is harmful: on key pairs it is \res{cmp/p12/diff} points below
> the verdict-only verifier [\res{cmp/p12/lo}, \res{cmp/p12/hi}], outside the margin of two points. The
> verdict-only verifier is the recommended system there.

Limitations, "The reader", adds the same sentence.

## F. All of the plan's "What would count against the thesis" hold

(the pattern of the rule tier does not reappear on MedCalc-V criterion claims; removing or exchanging the
criterion moves the trained verifier no more than the backbone; a derived criterion does not help where it
decides the label)

Title and abstract framing, as the plan states: "the paper is a controlled study of supervision for
rule-conditioned verification on generated cases, and says so." Blocks A and B apply; in addition the abstract
sentence "Selectivity is relative to a criterion." and contribution (3)'s heading "A boundary, and a design
that follows from it" become "A boundary" with the design described as tested and not supported. A change of
the title is the authors' decision and is not proposed here.
