# v14: what changed, what the research found, what to run next

8 Oct 2026. Companion to `learning_when_to_change_naacl2027_draft_v14.pdf` and `learning_when_to_change_naacl2027_latex_v14.zip`.

- Draft: 28 pages; Sections 1–7 fit in 8 pages; compiles standalone (pdflatex, bibtex, pdflatex ×2).
- Black = measured, taken from the status board of 3 Oct 2026. Red = not run or to confirm: 215 `tbd` cells, 34 red notes.
- No target, example or invented values anywhere in the draft.

---

## 1. What v14 keeps, and what it changes

**Kept from v10/v13:** the title; the triplet test; the training-distribution × representation factorial; every audit, ablation, diagnostic, transfer tier, the selection experiment and the GRPO experiment. Nothing was removed. To fit 8 pages, the full transfer table, the selection table, the objective, the systems list and the long related work moved to appendices.

**Changed:**

1. **Thesis: selectivity is relative to a criterion.** Applicability is a conjunction of five typed conditions (concept, subject, status, time, value; Eq. 1). A near-miss makes exactly one of them false.
2. **Measured results are in, and the claims follow them.**
   - Stands:
     - Released medical PRMs fail the triplet test: Med-PRM 11.9% (reverses 19.4%, holds 86.0%, base accuracy 91.2%), MedS3 10.0%, FoVer 31.8%. Untrained backbone 27.1% on conclusion claims, 83.9% on criterion claims.
     - Decisive edits alone give reversal without holding: 53.7 ± 5.4. Near-misses in the same budget: 91.8 ± 0.4 (+38.2 [34.9, 41.2]). The blocks-trained model ends below the untrained backbone on criterion claims (53.5–66.5 against 83.9).
     - Separate reading pass: 98.5 ± 0.7 (prose), 99.2 ± 0.3 (ledger).
     - One applicability bit carries the result: bit-only reader 99.95, decision-field-only judge 99.3; both 97.8 on rule-side items.
     - The verifiers read the rule: crossed accuracy on rule-side items 85.0–94.0 (ledger) and 85.5–91.2 (verdict only), against 39.0 untrained and 13.5 for Med-PRM.
     - Reward exploitation: with Med-PRM as the GRPO reward, reward reaches 0.9997 while accuracy falls 88.0 → 38.7; outcome reward 88.7 → 96.7.
   - Withdrawn or corrected:
     - Zero-shot medical transfer is withdrawn, by the decision rule fixed in advance. MedEinst pairs: backbone 24.2, verdict/triplets 22.8, Ledger-RM 15.7. Key pairs: 79.8, 78.2–78.7, 30.5–35.9. TrialGPT: +3.4 [−2.6, 9.2], not established.
     - "Balanced data helps": not supported (−8.8 [−11.9, −5.8]).
     - Typed fields over prose: +0.8 [0.3, 1.3] only. Reported as that.
     - Ledger score added to a step check for selection: −0.9 [−2.1, 0.2] on MedQA; trace AUC 0.51.
     - The judge is not a faithful function of the fields: it follows 47.8% of single-field edits that should flip the verdict.
   - New, stated plainly: ThinkPRM-14B solves 87.5% of a 200-triplet subset. The test is solvable without training on our rules; the released medical PRMs do not solve it.
3. **Criterion grounding (new; specified, not run).** Where no rule is stated, a grounding function maps the task identity to a criterion text with a provenance tag (stated, derived, self-written). Results are reported as a ladder: no criterion, stated or derived, self-written, wrong.
4. **Symbolic gate, giving Ledger-RM-G (new; not run).** Executes the computable parts of applicability: quotation string match, threshold comparison with unit conversion, date arithmetic against a reference date, class membership by ontology closure, subject and status set membership. If every applicable check is computable, the conjunction replaces the reader's bit. Otherwise the bit stands and the judge also sees the case. With no criterion, the system abstains and falls back to the verdict-only score.
5. **Open-ontology layer, no SNOMED CT or UMLS licence.** HPO, Mondo (DOID fallback), RxNorm ingredients, RxClass (ATC level 4 ∩ FDA class), MED-RT relations, openFDA/DailyMed.
6. **New tiers whose criterion has a source we did not write.** MedCalc-V, registered criteria (Chia, Leaf), DDXPlus knowledge-base triplets, class triplets, MedEinst with a derived criterion, key pairs with self-written criteria (diagnostic only).
7. **Two-stage analysis plan.** Stage 1 outcome table (comparisons 1–6b). Stage 2 comparisons 7–12 with decision rules. The stage-2 text exists in Appendix A and is not yet committed to the repository; the sentence that says it was registered is red until it is.
8. **Corrections made today on re-checking:**
   - MedCalc-Bench: the pinned tag postdates both audits; the second audit examined the Verified release itself (the earlier wording had both auditing the original).
   - Open-book figure: one model, 51.9% → 81.5% (the earlier "52% to 81–85%" merged two models and a subsample).
   - Agreement of the two corrected label sets, recomputed from the two files: 62 shared rule-based test rows; the other set gives no answer for 10 and a different answer for 9 of the other 52.
   - Section 6.5: the prediction for MedCalc-V now follows the rule tier's result on criterion claims (triplets above the backbone, blocks below it); the earlier wording gave the conclusion-claim ordering.
   - Table 14: the "no criterion" cells for TrialGPT and registered criteria are marked not defined (the claim is the criterion), which removes four cells.
   - Appendix A now matches the analysis plan in the task pack (existing adapters for comparisons 7, 8, 9, 11; a rule for comparison 12).

---

## 2. Answers to the questions asked

### Can rules be created for MedEinst, TrialGPT, MedQA and other open datasets, with backing?

| Dataset | Source of the criterion | Label basis | Verdict |
|---|---|---|---|
| MedCalc-Bench Verified, rule-based subset (19 scores; 380 test notes, 230 human-written) | Score definition shipped inside each instance | Released criterion values + rule code | Best new tier: real clinical text, stated rule, released labels. Build first. |
| Trial criteria via Chia and Leaf corpora | Registry text; structure from published human annotation | Program compiled from the annotation | Yes. Adds time windows and thresholds with independent backing. Execution conventions (boundary day, reference date) stay ours and are printed in the prompt. |
| TrialGPT annotations | Already stated (trial criterion text) | Physician labels | Keep, but it cannot carry the claim: only 33 of 1,015 labels are decisive negatives; 610 pairs have no relevant sentence. |
| MedEinst | Derived by script from the DDXPlus lists (49 conditions, 223 findings, 888 links; no probabilities released) | Benchmark labels | Conditional. Trap labels were accepted as plausible, not entailed, so a symbolic executor is run on every pair first; its accuracy bounds what a rule-follower can gain. |
| DDXPlus knowledge-base triplets | Same lists, same script | Exclusion procedure on the lists | Yes; exact relative to the lists. Tests the same source without the MedEinst label gap. |
| MedQA / CareQA key pairs | None that is not the answer itself | Answer keys | No. Declared the boundary. Self-written criteria only as a diagnostic, with a mismatched-criterion control. |

Not in the paper, optional later: n2c2 2018 Track 1 (13 stated criteria with per-criterion expert labels on real longitudinal notes, including 6-month and 1-year windows; needs a signed data use agreement) and the NegEx/ConText test kit (2,376 de-identified sentence–concept pairs; 491 negated, 257 historical, 6 non-patient).

### Ontology or knowledge graph without SNOMED CT?

- Everything needed is open today: HPO (free with attribution, no alteration), Mondo (CC BY 4.0), Disease Ontology (CC0), RxNorm prescribable subset and RxNav/RxClass (no licence; ATC names not redistributable), openFDA/DailyMed.
- What the literature shows about how to use it:
  - As a lookup or constraint at inference it helps: retrieve-then-select normalisation to HPO reaches F1 0.80–0.89 against 0.12 for direct ID generation; type-gated retrieval in OntGQA is worth 4.9 and 16.7 Hit@1 points.
  - Injected into weights it does little: OntoTune moves the zero-shot medical-QA average 56.9 → 58.7 and MedQA 51.7 → 51.5.
- So v14 uses the ontology in two places only: as an exact label source for class-level near-misses (a class member flips, a relative outside the closure holds), and as the closure check inside the gate. Linking is retrieval followed by a choice among candidates, never free generation of identifiers.
- Known failure modes, handled in the protocol: drug-class sources disagree (keep a membership only where ATC level 4 and the FDA class agree); a missing contraindication assertion is not evidence of safety; labels are exact only relative to a named release.
- Knowledge-graph retrieval pipelines were not adopted: their knowledge is associative, there are no exact labels, and measured retrieval gains on MedQA for capable readers are small or negative.

### A structured workflow that strengthens the method?

- NS-PRM (attached): a deterministic verifier decides what is executable and a PRM is trained on negatives that pass it. Its gain comes from the verifier (ProcessBench average F1 74.2 full, 68.8 without it, 73.5 for the strongest prior PRM). All its perturbations change the label. v14 takes "execute what is executable" (the gate) and adds the label-preserving side.
- Solver pipelines for eligibility and guidelines (SMT, ASP; VERDICT, VeriDx): nothing is trained, criteria are given, and the dominant errors are fact extraction, negation and missing information. That is the part our near-miss-trained reader addresses.
- Sadhu et al. (2026): deleting or replacing the rule left every audited compliance detector unchanged. Our rule-side items already answer this (85–94% against 39%); stage 2 adds rule-removed, rule-swapped and rule-paraphrase controls.
- Augmented Policy Training (ACL 2026): label-changing perturbations alone give precision 0.50 at recall 1.00; adding label-preserving ones gives 0.90 and 0.78. Same pattern as blocks against triplets, in another domain.

### Novelty status after the sweep

| Claim | Status | What remains ours |
|---|---|---|
| Test (triplets + rule-side items on medical PRMs) | Partly shown elsewhere (MedPIC-Bench: answer-changing pairs; MedDistractQA: irrelevant distractors) | Decisive edit and same-concept inapplicable mention in one item; applicability-clause edits with the case fixed; applied to released medical PRMs |
| Decisive-only supervision gives reversal without holding | Principle known (Joshi & He 2022; ScoNe; APT) | Budget-matched substitution, outcome-balance control, leave-one-kind-out, for a rule-conditioned verifier |
| Separate evidence pass | Mostly known in general form (Chain-of-Verification) | Same-record same-pass against separate-pass contrast; typed-against-prose null; sufficiency of one bit |
| Reward exploitation | Known as a phenomenon (math PRMs; rubric rewards) | Collapse from a high baseline against a released medical PRM, with an outcome-reward control and the reward's triplet profile |
| Criterion grounding + gate + near-miss-trained verifier | Not found in about 50 papers read | The conjunction and its controlled measurement (stage 2) |

Limits of the sweep: papers were read through a fetch tool, full main text where stated; the search budget ran out before two planned queries, so coverage of June–October 2026 is incomplete.

---

## 3. Stage 2: run order

Nothing below has been run. Each set is frozen with a hash before any system is scored on it. `rule_v1` is not modified. The detailed version of this section, one file per role, is `selrm_stage2_tasks.zip`.

| # | Role | Task | Acceptance / output | Feeds |
|---|---|---|---|---|
| 0 | D | Commit the stage-2 plan (Appendix A text: comparisons 7–12, decision rules, selection and freezing). Record the hash in the paper. | Commit precedes the first stage-2 set. | all |
| 1 | C | Controls on the frozen rule tier, no new data: rule removed from the prompt; rule exchanged for another group's. Systems: critic, verdict/blocks, verdict/triplets, Ledger-RM. | The two red rule-tier values in Appendix E. Trained verifiers should fall more than the backbone. | (8) logic |
| 2 | A, C | Rule-paraphrase invariance arm: rewrite rule text without changing its program (clause order, exception placement, synonyms); certify by executing both programs. | Excess rate of changed verdicts over a rerun baseline. | App. E |
| 3 | A | MedCalc-V (`mcv_v1`), from MedCalc-Bench Verified tag v1.0.8. Implement each of the 19 scores from its stated text. Items: (A) criterion claims on untouched notes in three strata (stated / denied / settled by default); (B) values naturally near a threshold; (C) single-value edits where the value string occurs exactly once and feeds no other criterion; (D) one-sentence insertions (relative, negated, past only for current-state criteria; affirmed for the patient = flip). | A score enters only if our code reproduces the released answer on every row. Report how many of 19 pass. Human-written (230) and model-written (150) notes reported separately. History-type criteria: a past mention is a flip. | (7) (8) (9) |
| 4 | A | DDXPlus criterion renderer: for a pair, findings listed for A only, B only, both, plus the exclusion procedure; canonical name order; identical text for both members. | Script and hashes of the two release files committed before any model run. | (11) |
| 5 | C | Symbolic executor on every MedEinst pair, before any model sees the derived criterion. Plus string-match baseline. | Pair accuracy and share of pairs decided. If it decides fewer than half, comparison (11) is dropped. | (11) |
| 6 | A | Knowledge-base triplets from DDXPlus test patients (flip: remove A-only findings, add B-only; near-miss: B-only finding in a form the criterion does not count). | Labels by the procedure. | ladder |
| 7 | A | Class triplets: RxNorm ingredient → member iff ATC level 4 and FDA class both contain it; HPO and Mondo by is-a closure. Negatives pass the disjointness test; combination products and multi-class ingredients excluded. Classes held out from training. | Release identifiers stored with every item. Open-book and closed-book regimes kept apart. | (10) |
| 8 | A | Registered criteria from Chia and Leaf: single-condition criteria with a threshold or a window, none of the corpora's unrepresentable/subjective flags; compile annotation to program; trials in the TrialGPT annotations excluded. Cases generated with dates and a reference date. | Recount the usable criteria (first count about 450 in Leaf). Becomes `rule_v2` together with windows and class conditions. | ladder, windows |
| 9 | B | Training on `rule_v2`: verdict-only blocks and triplets; reader with the stage-2 record (date expression, normalised concept, applies bit); case-visible judge for the fallback. MedCalc adaptation on training notes with and without near-miss edits at equal budget, a fixed set of scores held out. | Five seeds for the cells in comparisons (7) and (9). Held-out scores chosen by a seeded rule written into the plan. | (7) (9) (12) |
| 10 | B, C | Gate: five checks, each returning 1, 0 or not-computable; override rule; abstention. | On gold records the gate equals the rule program. Linking accuracy reported separately. | (10), windows |
| 11 | C | Criterion ladders per tier (none / stated or derived / self-written / wrong) for the critic, verdict-only and Ledger-RM-G. Holm correction over (7)–(12). | Table 14 (criterion ladder); controls for MedEinst: unrelated pair's criterion, lists exchanged, neutral diagnosis labels, lists without the procedure. | all |
| 12 | C | Finish the audit: ThinkPRM parts 2–3, GenPRM part 1 and the crossed-accuracy summary for part 2, default-correction cells, prompted cells on MedEinst, larger open and closed judges. | Table 2 red cells. | §6.1 |
| 13 | D | Finish the two ledger-reward GRPO runs; add seeds (now one seed, 150 pairs). Recompute the Holm correction for the stage-1 family. | §6.6 and the caption of Table 5. | §6.6 |

Comparisons, for reference: (7) MedCalc-V criteria on human-written notes, triplets against blocks; (8) criterion × system interaction on the same items; (9) MedCalc-V edits, triplets against blocks; (10) class triplets, gate against learned verdict; (11) MedEinst, derived criterion against none, trained against critic; (12) key pairs, case-visible composite non-inferior to verdict-only at two points.

---

## 4. Things only a person can do

1. Commit the stage-2 plan before any stage-2 data exist (task 0).
2. Push role C's partial ThinkPRM run. The 87.5% in Table 2 comes from `C-AUD-thinkprm--p1`, which the board lists as local-only and not on origin.
3. Open every `VERIFY` entry in `custom.bib` at its source. Fifteen of the v14 additions were typed from memory: saeidi2018sharc, holzenberger2020sara, clark2020ruletaker, dhuliawala2024cove, she2023scone, ravichander2022condaqa, he2023ontolama, he2024hit, kury2020chia, dobbins2022lct, gargano2024hpo, vasilevsky2022mondo, nelson2011rxnorm, gao2023scaling, winston1970. Older `VERIFY` entries remain as well.
4. Confirm the red facts: the count of usable Leaf criteria; licence wording of each ontology at release time; the held-out score set; the list of larger judges to score.
5. Appendix J (development history) has to be confirmed from your own records; it carries a red note saying so. The coding of the 200 collected failures (extraction, applicability, unseen wording, rule misread, other) is pending.

## 5. What would count against the thesis

- The ordering of the rule tier on criterion claims does not reappear on MedCalc-V (triplets above the backbone, blocks below it).
- The trained verifier is as indifferent to removing or exchanging the criterion as the backbone.
- The executor decides few MedEinst pairs: then MedEinst stays only as the contrast without a criterion.
- If these fail, what remains is a controlled study of supervision for rule-conditioned verification, and the draft says so.

---

## Sources

Datasets and resources
- [MedCalc-Bench Verified (repository, tag v1.0.8)](https://github.com/nikhilk7153/MedCalc-Bench-Verified)
- [Ye et al., audit of MedCalc-Bench labels, arXiv 2512.19691](https://arxiv.org/abs/2512.19691) and [corrected labels](https://github.com/junzeye/validate-medcalc-labels)
- [Krohn-Grimberghe, MedCalc-Bench audit and open-book evaluation, arXiv 2603.02222](https://arxiv.org/abs/2603.02222)
- [Chia corpus, Scientific Data 2020](https://www.nature.com/articles/s41597-020-00620-0) and [data record](https://doi.org/10.6084/m9.figshare.11855817)
- [Leaf Clinical Trials corpus, Scientific Data 2022](https://www.nature.com/articles/s41597-022-01521-0) and [repository](https://github.com/uw-bionlp/clinical-trials-gov-data)
- [TrialGPT, Nature Communications 2024](https://www.nature.com/articles/s41467-024-53081-z) and [criterion annotations](https://huggingface.co/datasets/ncbi/TrialGPT-Criterion-Annotations)
- [MedEinst, ACL 2026](https://aclanthology.org/2026.acl-long.1847/) and [dataset](https://huggingface.co/datasets/zhui711/MedEinst)
- [DDXPlus](https://github.com/mila-iqia/ddxplus/blob/main/README.md); knowledge-base files: [conditions](https://github.com/mila-iqia/Casande-RL/blob/master/Baselines/BED/dataset/ddxplus/release_conditions.json), [evidences](https://github.com/mila-iqia/Casande-RL/blob/master/Baselines/BED/dataset/ddxplus/release_evidences.json)
- [RxClass API](https://lhncbc.nlm.nih.gov/RxNav/APIs/RxClassAPIs.html) and [RxNav terms of service](https://lhncbc.nlm.nih.gov/RxNav/TermsofService.html)
- [HPO licence](https://hpo.jax.org/app/license); [Mondo](https://mondo.monarchinitiative.org/); [Disease Ontology](https://obofoundry.org/ontology/doid.html)

Papers that shaped the design
- [NS-PRM, arXiv 2608.26329](https://arxiv.org/abs/2608.26329)
- [OntoTune, arXiv 2502.05478](https://arxiv.org/abs/2502.05478v1) and [repository](https://github.com/zjukg/OntoTune)
- [OntGQA, ACL 2026](https://aclanthology.org/2026.acl-long.489/)
- [Sadhu et al., compliance detectors, arXiv 2608.16852](https://arxiv.org/abs/2608.16852)
- [Augmented Policy Training, ACL 2026](https://aclanthology.org/2026.acl-long.748.pdf)
- [VERDICT, arXiv 2609.03366](https://arxiv.org/abs/2609.03366)
- [MedPIC-Bench, arXiv 2608.03028](https://arxiv.org/html/2608.03028v1)
- [MedGuideX, arXiv 2605.26567](https://arxiv.org/pdf/2605.26567)
- [Reward Under Attack, arXiv 2603.06621](https://arxiv.org/abs/2603.06621)
