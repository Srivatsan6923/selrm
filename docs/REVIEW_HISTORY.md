# Three reviews of v5: validation and changes in v6

R1 = long technical review; R2 = structured positive review; R3 = "killer
deficiency" review. Verified means I checked it against the draft or a source.

## Adopted (valid)

| # | Point (reviewer) | Check | Change in v6 |
|---|---|---|---|
| 1 | "Rule-only" transfer was confounded: the ledger adapter also saw MedPRMBench step-error data (R1) | Verified in v5 Sec. 5 and App. G | Separate adapters. Ledger adapter is trained on rule data only unless a row says otherwise; all tables except reranking use the ledger score alone. Table 4 has rule-only rows (zero-shot on clinical columns), a "+ step-error data" row and "clinical pairs" rows |
| 2 | Proposition 1, concept-presence part, is false as written (R1) | Verified: a constant scorer is a counterexample | Restated with a feature map h: if h(flip) = h(near-miss) then d(flip) = d(near-miss). Near-misses are built to collide under the attribute-blind map h0. Three-step proof (also R3) |
| 3 | MedCalc-Eval rules are not available (R1) | Verified: the repository holds only a LICENSE file | Dependence removed. Library = MedCalc-Bench calculators + scores implemented by us from published definitions + stated constraint rules + grammar rules; correctness is relative to the rule text in the prompt |
| 4 | The `check` field carries the answer (R1) | Valid by inspection | Reader now records facts only; the judge decides applicability. Ablations: + decision field, decision field only, program on predicted bit (Sec. 7.4, Table 9) |
| 5 | Free-form baseline was one-stage, ledgers two-stage (R1) | Verified | Two-stage evidence summary with the same case-blind judge and budget; one-stage vs two-stage reported separately (Table 3) |
| 6 | Corpus contrasts changed two ingredients at once (R1) | Verified | All corpora share the same share of missing-input and presentation instances; levels differ in one ingredient |
| 7 | Missingness semantics conflict (R1) | Verified against v5 App. C | Explicit absence vs unknown; omission conventions by input type; completion-set condition; "-" covers refuted and undetermined, reported separately |
| 8 | Applicability stated globally (R1) | Valid: some scores count past or family findings | Applicability is a per-criterion predicate A_j; in a stated share of criteria past or family findings count and are flips |
| 9 | UR conditions on each model's own base accuracy (R1) | Valid | Tables report unconditional Hold; base accuracy, ties, conditional UR with denominators in App. F |
| 10 | Small loss under vignette withholding does not show a PRM ignores the patient (R1) | Valid: chains restate facts; many errors are step-internal | Removed from the audit table and abstract; reported as an input ablation in App. F, with the case-dependent error types separately |
| 11 | Vignette swap shows dependence, not correct dependence (R1) | Valid | Text says so; pair columns carry the correctness claim; paraphrase control added |
| 12 | Eq. for the margin needs y*d0 < 0 and the d0 = 0 case; kappa undefined (R1, R3) | Valid | Condition stated; d0 = 0 counted separately; kappa defined (Eq. 2) |
| 13 | u, q and y notation (R1, R3) | Valid | u(s,x) = J(R(x,rho,s),rho,s); q defined on N(x); y_rho(e,s) |
| 14 | "No path from case to verdict" is wrong; string check is symbolic at inference (R1) | Valid | "No direct case input to judge"; caption states the string check |
| 15 | min of two scores bypasses the bottleneck and needs a common scale (R1) | Valid | Step check is a separate adapter; calibrated before min; ledger-alone, step-check-alone and combined rows in Table 5 |
| 16 | Malformed-ledger scoring (R1) | Valid | Floor score -L; two malformed ledgers tie; ties fail |
| 17 | Model selection on test endpoints (R1) | Valid | Selection, thresholds and calibration on development splits; frozen before test |
| 18 | Key pairs: question graph, option semantics, not counterfactual (R1) | Valid | One-to-one matching, exclusions, renamed "paired answer discrimination" |
| 19 | MedEinst disease split must hold out both diagnoses (R1) | Valid | Defined in App. D |
| 20 | L3-alt should use cases where the rules disagree; structural overlap (R1) | Valid | Both done (Sec. 6, App. B) |
| 21 | Majority-class macro-F1 of 53.4 is impossible (R1) | Verified: bound is pi/(1+pi) <= 0.5 | Placeholder corrected |
| 22 | Shortcut table inconsistent with the near-miss mix (R1) | Verified | Table rebuilt from the proposition |
| 23 | "Hand-written program" below 100% (R1) | Valid | Renamed "extraction + hand-written program"; gap is extraction error |
| 24 | Eight sampled verdicts are noisy (R1) | Verified: s.e. up to 0.177 | 32 samples, tie rates, same protocol applied to an open model |
| 25 | Equivalence claim from a point estimate (R1) | Valid | Non-inferiority interval |
| 26 | MR needs a common operating point (R1) | Valid | MR at 5% false rejection; achieved FR reported |
| 27 | Best-of-N reward rise is mechanical (R1) | Valid | Selection regret reported instead |
| 28 | Rule triplets trade reversal for holding in the clinical columns (R1) | Valid | Stated in Sec. 7.3 |
| 29 | FoVer already shows formal-to-informal transfer; matched comparison (R1) | Valid | Novelty statement narrowed; model trained on FoVer data with our backbone added |
| 30 | A released generative PRM in the audit (R1) | Reasonable | ThinkPRM added |
| 31 | Does over-triggering hurt downstream? (R3) | Valid question | "No near-misses" row in Table 5 |
| 32 | Soft-ledger comparison belongs in the main text (R3) | Partly valid | One-stage variant discussed in Sec. 7.4 with both tiers |
| 33 | Intro overclaims "has not used the evidence" (R1) | Valid | Behavioural wording |
| 34 | "No clinician reviewed any data" misdescribes reused benchmarks (R1) | Valid | "We commissioned no new clinical annotation" |
| 35 | Uncertainty in main tables; formal headers (R1, R3) | Reasonable | Seed s.d. on primary columns, error bars in Fig. 4, declarative headers |
| 36 | Noise of diff-derived targets (R3) | Valid | Agreement with structured evidence reported; authors' inspection of rendered triplets (R2) |

## Not adopted, or adopted differently

| Point (reviewer) | Verdict |
|---|---|
| "Training on MedEinst reference pairs is data leakage; the 48.6% is invalid" (R3) | Misread. That row had no MedEinst training. Training on a benchmark's reference split is ordinary supervised evaluation. What was wrong was the step-error confound (item 1). Rows are now labelled zero-shot or in-distribution |
| "No baseline trained on the triplets without the ledger" (R3) | Already present (verdict-only on triplets). A pairwise-loss variant is added to the ablations |
| "Soft ledger scoring lower proves the judge exploits a sterilised ledger" (R3) | Not a valid inference, and the numbers are placeholders. A lower score with the case visible would mean direct access reopens the shortcut. The fair version of the concern, that a few fields cannot carry real evidence, is tested by comparing both variants on the clinical tier |
| "Prove attention dilution" (R3) | Mechanism claim; out of scope |
| Introduction should discuss "PRM scaling laws" (R3) | Not adopted |
| MedCEG reward, full VCS reimplementation, GenPRM adaptation (R1); VPRM, DynaCF, CSR, FINCARDS, DeepEra (R2) | Not run. VCS and MedCEG are positioned in the text and claims limited accordingly; the extraction + program row is the verifier-as-reward comparison. The R2 list could not be verified |
| Demands for measured results (all) | Stands until experiments are run |

## Still open

* Author lists for MedCEG and EVPV remain placeholders in custom.bib.
* MedCEG's reward and a GenPRM adaptation are the two comparisons a reviewer
  is most likely to ask for again.
* MedPRMBench's per-type split into case-dependent and step-internal errors
  must be checked against its taxonomy.

---

# Second pass (v7): audit of v6 against the same three reviews

The reviews received again are identical to those answered above. This pass
checks whether v6 really implemented each accepted point.

## Errors found in v6 and fixed

| Issue | Why it was wrong | Fix in v7 |
|---|---|---|
| Proposition 1 remark claimed the attribute-blind map of all concept-value pairs gives h(flip) = h(near-miss) | It does not: in the Figure 1 example the near-miss still contains the patient's "allergies: none" line. This is the "assumed, not constructed" collision R1 warned about | The colliding feature is now defined exactly: h_k(x) = 1 if the decisive concept k is named anywhere. The engine renders base cases without naming k and checks the equalities on every triplet. Richer attribute-blind features are an empirical baseline, not covered by the proposition |
| Shortcut table and audit sentence said the attribute-blind logistic scorer solves no applicability triplet "by the proposition" | Follows from the same wrong claim | Table has a "concept named" row (TA = 0 by the proposition) and a separate learned baseline with placeholders |
| Reader was conditioned on the candidate claim | A claim-conditioned reader can encode its own verdict in what it writes, which reopens the "answer-bearing field" objection | In triplet and pair tests the reader receives the condition under test, not a candidate's outcome, and one ledger serves both claims. For single-step selection the dependence is measured (App. E) |
| Resampled ledgers were drawn from any case of the rule | A ledger about another criterion implies no verdict for the claim | N(x) restricted to the same rule and condition |

## Accepted points that v6 had left open, now closed

| Point (reviewer) | v7 |
|---|---|
| Bibliography authors for MedCEG and EVPV (R1) | MedCEG: verified (Mu, Gu, Huang, Zhu, Zhang, Zhang; arXiv 2512.13510). EVPV: title and arXiv id verified (2603.16253); first author Junxin Wang, ten authors, full list still to enter |
| MedCEG absent from the audit (R1) | Stated reason: its reward compares a generated graph with a reference graph built per training case, which our cases do not have |
| Generative-verifier comparison at matched budget (R1) | The one-stage rationale row is identified as that design; ThinkPRM is in the audit |
| Premise-gating alternative (R1) | "Premise gate" row in the ablation table, after EVPV |
| Withholding test with restated facts removed from the chain (R1) | Added to the input-ablation paragraph |
| NLI4CT-P joint correctness (R1) | Added beside base F1 |
| Judge fed the wrong ledger; quotes that exist but are the wrong evidence (R2) | Both reported (Sec. 7.4, App. E) |
| Wording and length of the two claims (R2) | Default-swap and paraphrase check (App. B) |
| Noise of diff-derived targets on an inspected sample (R3) | Added (App. D) |
| Rejection trade-off beyond one operating point (R1) | Curves referenced with the ladder table |
| Tables inside the reference list (R1) | Checked: none in v7 |

## Still not done

* GenPRM adaptation and a full reimplementation of the verified
  counterfactual corpus of Chi and Wang; claims are limited instead.
* EVPV full author list.
* Everything that needs measurements.

---

# Third pass (v8): the seven papers, read in full

| Paper | What it is (from the PDF) | Effect on the paper |
|---|---|---|
| DynaCF (Liu et al., 2606.09043) | Reward models from pairwise preferences; rewrites the chosen response without changing content; margin shift and flips under the current model down-weight the pair in the Bradley-Terry loss. Qwen3-4B/8B. Training on the rewrites as labels did worse than using them as probes | Closest prior on reward models; now stated in related work with the difference (response-side, should-not-change only, probes). New ablation row "probe re-weighting": near-misses used only as probes, which answers the reviewer's question directly |
| CSR (Shihab et al., 2509.01544) | Trains a solver so its answer changes when an operator in its own trace is swapped; sensitivity (COS) and paraphrase invariance (SIS) | Cited. Flip-only training is its labelled counterpart, so no separate run; the text says so |
| GenPRM (Zhao et al., 2504.00891) | Generative PRM: analysis plus Python check, executed, then verdict; released 1.5B/7B/32B checkpoints trained on MATH; test-time majority over sampled verifications | Released GenPRM-7B added to the audit (13 signals). A GenPRM-style verifier trained on the same triplets added to the transfer table. Bibliography completed |
| EVPV (Wang et al., 2603.16253v2) | Extracts visual facts once per problem, independently of the solution; matches the solution's stated premises; attenuates rewards of visually dependent steps toward neutral when reliability is low | Full author list entered. Described accurately; the "premise gate" row follows this design; our min-combination is called its hard counterpart |
| MedCEG (Mu et al., 2512.13510) | Policy reward: an LLM turns the rollout into a graph that is compared with a reference graph built for each training question (node coverage, structure, chain completeness) | Cannot score a claim without a reference, so it is not in the audit, and the paper now says why. A reference-graph reward of this kind is added to the policy-training appendix, where the rule program supplies the graph |
| FinCARDS (Zhou et al., 2601.06992) | Typed "cards" (entity, metric, period, scope) for reranking chunks of financial filings; free-text summaries do worse | One citation as the retrieval analogue of a typed record. Not a baseline |
| DeepEra (Chen et al., 2601.16478) | Reranker and dataset for passages that are semantically similar but logically irrelevant | One citation as the retrieval analogue of near-misses. Not a baseline |

Corrections to my earlier notes: the four papers named by the structured
review exist and are relevant in the way described above; "could not verify"
no longer applies. The sources table moved to Appendix D to keep the main text
at eight pages.

---

# Fourth pass (v9): review of v8 (weaknesses list)

| Point | Verdict | Change in v9 |
|---|---|---|
| Reader is a bottleneck; a quote check does not show the quoted span is the right finding | Valid, already a stated limitation, but not quantified | Error attribution with program-supplied ledgers (the judge alone, then the share of errors from the reader); a second pass that re-reads each entry against the case and regenerates rejected ones, after VeNRA's two-step grounding (Sec. 7.4, Table 9, App. E) |
| Judge may hinge on a decision bit; benefit of typed fields overstated | Valid | Stated in the contribution list, not only in Sec. 7.4. New ablation: a reader trained to write only the bit, which tests the fields as reader supervision |
| min of two scores has no justification | Partly valid | Justification added (both checks must pass; the joint probability is bounded by the smaller one). Product and a fitted combination compared in App. G |
| Selectivity on real clinical text untested | Valid; cannot be closed without credentialed data | Limitations now name the nearest existing resources (i2b2 2010 assertions; EHRNote-ChatQA) and say they are not used |
| Templates shared between training and test allow shortcuts | Valid: v8 reported 100% shared templates | Test templates and cue phrases (relatives, negation, time) are now held out; the shared-template result is reported beside it; a trigger-lexicon reader in the style of ConText shows what held-out cues prevent (App. B, App. F) |
| "No experiments run" conflicts with numbers in the body | True of the draft; nothing to change until results exist | None. The red banner and the build guard stay |
| Rendering artefacts in figures | Minor | Labels in the selection plot no longer clip; the shift figure moved to App. F with its definitions |
| MedGuideX not discussed | Valid and important. Verified: Shen et al., arXiv 2605.26567 | Cited and positioned: executable guideline logic, factual and counterfactual questions, used to post-train a policy. GuideSkill (2607.26160) cited for execution at inference |
| CondMedQA / CGR | Verified: Parekh et al., arXiv 2602.17911; 100 curated conditional questions | Cited. Added as a small external check in App. D (confirm that the release includes the general answer for each question) |
| VeNRA Universal Fact Ledger | Verified: Agand, arXiv 2603.04663 | Cited for typed fact records and for the verification pass |
| EHRNote-ChatQA | Verified: Kim et al., arXiv 2606.15735; MIMIC-IV, credentialed access | Cited in Limitations as the nearest resource. Whether its distractors are near-misses in our sense was not checked |
| SURE-RAG, GSAR, CHR | Not verified | Not cited |
| Clinical NLP lineage of the ledger fields (not raised by the reviewer) | Missing in v8 | NegEx, ConText and the i2b2 2010 assertion task are now cited as the origin of subject, status and time |

The main text also changed in one structural way: the shift analysis left
Section 4 for Appendix F, which made room for the additions and brought the
sources table back into Section 3.

---

# Fifth pass (v10): the seven papers uploaded after the fourth pass, read from the PDFs

| Upload | What it is | What I had wrong or thin | Change in v10 |
|---|---|---|---|
| MedGuideX (2605.26567) | 2,793 executable functions compiled from public guideline recommendations (recommendation, decision tree, Python function, each step checked by a model); 4,963 factual and 5,028 counterfactual questions; SFT then GRPO on a policy; MedQA, MedCaseReasoning, MIMIC-CDM-FI, ER-Reason | I had only the abstract. The paper keeps only interventions that change the outcome and discards the 788 that do not; no release of the functions is mentioned | Related work states this. Section 7.2 names it as a source of flip-only data. Constraint rules are now derived by its tree-then-program steps, with the caveat that no clinician checks the tree |
| CondMedQA / CGR (2602.17911v3) | 100 questions with a patient condition; each has the answer given the condition and the general answer; model-generated, author-verified, 30 reviewed by annotators with medical expertise | My appendix test assumed a version of each question without the condition. The benchmark has none | Test rewritten: preference for the condition-specific answer over the general one, for the question as posed. Described as resisting the default, not as a reversal pair |
| EHRNote-ChatQA (2606.15735v2) | 967 patients, 8,036 content questions over MIMIC-IV discharge summaries, each with one correct and four incorrect answers following six expert-defined distractor patterns, all reviewed by 11 medical experts; credentialed access | I said its distractors were unchecked. Two patterns are claim-side near-misses: a correct fact attributed to the wrong admission, and entity or attribute substitution from elsewhere in the notes | New appendix test on real notes (claim-side applicability). Limitations and the last sentence of the abstract reworded: selectivity outside rules is tested only indirectly |
| SURE-RAG (2605.03534v2) | Verifier that decides supported, refuted or insufficient for an answer given retrieved evidence; selective answering; shortcut baselines and evidence swaps | Not read before | Cited where the verdict semantics are defined |
| GSAR (2604.23366) | Claims typed as grounded, ungrounded, contradicted or complementary, with a contradiction penalty and tiered recovery | Not read before | Cited at the same place |
| 2508.10226 | LLMs predicting psychiatric rating-scale scores for patients at clinical high risk (CHR) of schizophrenia | The reviewer's "contrastive retrieval via CHR" does not match this paper | Not relevant; not cited |
| ITM Web of Conferences 90, 05009 | Architecture sketch for hallucination detection in trading | Not the typed-ledger paper (that is VeNRA, arXiv 2603.04663, not among the uploads) | Not relevant; not cited |

Still cited from arXiv listings only, not from the PDF: VeNRA (2603.04663) and
GuideSkill (2607.26160).
