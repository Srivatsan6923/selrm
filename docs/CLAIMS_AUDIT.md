# Claims audit of the v13 draft against the measured results

Commit 2f8cbbbb9113 (3 Oct, after merge 5). Every empirical statement of paper/latex_v13/main.tex (abstract, sections 1-8,
limitations, appendices A-G) was compared with the result files, the tables generated from them
(tables/numbers.json) and the roles' analysis documents; every statement found contradicted was then checked a
second time, independently, from the files. Related work, ethics, the development history (see docs/TIMELINE.md)
and the reproducibility section were not audited. Statements are quoted from the LaTeX source: values in
\res{...} are the current measured values, values in \ph{...} are draft placeholders. Line numbers refer to this
commit.

872 statements: 522 consistent with the results, 98 contradicted (confirmed by the second
check), 50 partly contradicted, 9 first flagged but found to hold,
159 waiting for a result, 34 placeholders for which no run or result exists
or is planned. The prose is the authors' (H6): this report lists facts only; each note says what the results show,
not how to write it.

| Section | consistent | flagged | pending | no result planned |
|---|---|---|---|---|
| Abstract and introduction | 32 | 6 | 10 | 0 |
| Rule triplets, external tiers, diagnostics, method | 64 | 21 | 10 | 0 |
| Experimental setup; audit of reward signals | 54 | 21 | 14 | 1 |
| Training distribution and representation | 46 | 4 | 2 | 2 |
| Transfer within and beyond rules | 38 | 6 | 29 | 5 |
| What the judge uses | 31 | 7 | 10 | 0 |
| Candidate selection, conclusion, limitations | 36 | 12 | 8 | 0 |
| App. A-C (analysis plan, rule library, triplet construction) | 64 | 35 | 38 | 3 |
| App. D-E (external tiers, ledger format) | 46 | 13 | 15 | 16 |
| App. F (diagnostics) | 40 | 19 | 13 | 4 |
| App. G (additional results) | 71 | 13 | 10 | 3 |

'flagged' = found contradicted on the first check; sections 1, 2 and 5 give the outcome of the second.

## 1. Contradicted by the results (98)


### Abstract and introduction

- **line 95** `Across \ph{13} reward signals,`
  - results: Context (paper/latex_v13/main.tex l.95-96): "Across \ph{13} reward signals, \res{min/...}--\res{max/...}\% of triplets are solved". The min and max keys each list 13 runs, including run/C-AUD-injerr/L2/all/TA. The Systems paragraph (l.669-675) names 13 audited signals, one of them "a PRM trained on the MedPRMBench training split (injected-error PRM)".  Keys: in tables/numbers.json, both 13-key TA entries (min/...@...
  - note: Confirmed. The sentence gives results across 13 reward signals, but one of the 13, the injected-error PRM (C-AUD-injerr), is recorded as dropped: MedPRMBench has no public release. At most 12 signals can be measured: 5 released PRMs, 4 open judges and 3 closed judges. So the stated count is a procedure fact the repository shows is no longer true.  The 13 is a \ph placeholder and the TA range is pending (both keys ...
- **line 105** `and macro-F1 against physician-annotated eligibility judgments from`
  - results: Context (main.tex 103-106): "Trained on rules alone, with no medical QA data, the model raises agreement with MedEinst pair labels from ... and macro-F1 against physician-annotated eligibility judgments from [critic] to [Ledger-RM]."  Keys in tables/numbers.json: run/C-TG-critic/clin_v1:trialgpt_test/top/macroF1 = 65.7; run/C-TG-ledger2-triplets/clin_v1:trialgpt_test/top/macroF1 = 69.1 (seed 0 only). The two print...
  - note: Scope: what is contradicted is the claim of a gain ("raises") in the TrialGPT clause, on significance. The values 65.7 and 69.1 are right, as the first check said.  - **MedEinst half of the same sentence:** pending, not contradicted. run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal@0 = tbd; the critic's value is 24. - **RESULTS_SUMMARY P6a status:** it still reads "pending (Holm family incomplete)". Thi...
- **line 171** `in which the decisive concept appears without counting under the rule: in a relative`
  - results: Context, main.tex lines 169-172: "a \emph{near-miss} in which the decisive concept appears without counting under the rule: in a relative, negated, at a time the rule does not count, or as a value that approaches a threshold without crossing it." There are no \res keys in lines 160-182, so numbers.json is not involved; this is a data fact.  I recounted it myself. For each of the 400 nm_kind=subject triplets in dat...
  - note: The contradiction covers only the subject item, "in a relative": 40% of subject near-misses in every test set are in a roommate or friend. The other three items in the sentence (negated, at a time the rule does not count, a value at or near a threshold) match the construction. the first check counts are exact, and its suggested wording "in another person" fixes the line. That wording also matches what the draft al...
- **line 192** `\ph{13} reward signals`
  - results: Line 192 says "Across \ph{13} reward signals \res{min/...}--\res{max/...}\% of triplets are solved". The \ph{13} is a typed placeholder, and its \res list names 13 runs, including run/C-AUD-injerr. The repository says that 13th signal is dropped and nothing replaces it: - docs/DECISIONS_C.md line 20 (3 Oct): "injected-error PRM not run (MedPRMBench unreleased, re-verified today)". The signals that row lists are Me...
  - note: the first check is right: at most 12 signals can be audited, so "13 reward signals" is a statement about procedure that the repository shows is no longer true. Only the count is contradicted. The TA range in the same sentence is pending, because both keys are null. That range also cannot fill as written. scripts/make_tables.py lines 261-262 return None when any part of a min/max key is missing, and the key still i...
- **line 206** `and with physician eligibility judgments from`
  - results: Context (main.tex 203-207): "A model trained on rule triplets only ... without medical QA data, raises agreement with MedEinst labels from ... and with physician eligibility judgments from \res{C-TG-critic...macroF1} to \res{C-TG-ledger2-triplets...macroF1}". In tables/numbers.json, run/C-TG-critic/clin_v1:trialgpt_test/top/macroF1 = 65.7 (65.70) and run/C-TG-ledger2-triplets/clin_v1:trialgpt_test/top/macroF1 = 69...
  - note: Status: contradicted on significance, not on direction or values. 65.7 and 69.1 are printed correctly and the point estimate does go up. But "raises" states the effect that the registered comparison (6a) tests, and that test fails: +3.4, CI [-2.6, 9.2], p 0.244.  RESULTS_SUMMARY still marks P6a as "pending (Holm family incomplete)". The outcome is already settled, because a Holm-adjusted p can only be at least the...

### Rule triplets, external tiers, diagnostics, method

- **line 369** `a value exactly at the threshold is reported as its own kind`
  - results: Lines 367-370 of paper/latex_v13/main.tex define a numeric near-miss: "a counted value moves toward the threshold without crossing; a value exactly at the threshold is reported as its own kind". The clause has no \res keys and does not say whether the threshold is strict or inclusive. In the repository the at-threshold kind exists only at strict thresholds. At inclusive thresholds the value exactly at the threshol...
  - note: the first check numbers and reading are correct. Read on its own, the clause says that any value at the threshold is a separate near-miss kind. That is false for inclusive thresholds, where 411 of 1,198 numeric flips (test and dev) sit exactly on the threshold, by design (DECISIONS_A row 24, fix 8).  One could argue the clause applies only inside the near-miss definition. Under that reading it would be technically...
- **line 494** `10,689 reference pairs)`
  - results: Line 494 of paper/latex_v13/main.tex, read in context (lines 492-494): "\emph{MedEinst} \citep{chen2026medeinst} pairs a control case with a trap case ... (5,383 test pairs; 10,689 reference pairs)". The count is typed as plain text. It is not a \res key or a \ph, and there are no \res keys in lines 484-504, so nothing on this line resolves through tables/numbers.json. Line 1497 of the same draft says the paper us...
  - note: Confirmed for the quoted fragment. 10,689 is the benchmark paper's figure, but the release the paper says it uses (v13 line 1497) has 10,609 reference pairs, 80 fewer. Dropping the 63 pairs that overlap test leaves 10,546 actually used (ref_dev 500 + ref_train 10,046). docs/DECISIONS_C.md line 19 requires reporting the release, and v13 has not done so. The rest of the sentence holds: "5,383 test pairs" matches the...
- **line 494** `\emph{Key pairs} are two exam questions whose keyed answers each occur among the other's options.`
  - results: Line 494 of paper/latex_v13/main.tex gives the two-way definition, "keyed answers each occur among the other's options". There are no \res keys in this sentence or within 5 lines of it (lines 489-499). The repository no longer uses that definition: (1) docs/DECISIONS_D.md line 30 (2026-10-03): "every key-pair column (Tables 2, 4/App. key pairs, 5; Fig. 3 right) uses C's one-directional sets clin_v1/keypairs_medqa_...
  - note: The sentence states a fact about the data that the repository shows is no longer true. Every key-pair test set and every measured key-pair value comes from the one-directional sets, which need only one key to occur among the other question's options. The two-way definition is kept only as a yield (13 MedQA-test pairs, 3 CareQA pairs). The neighbouring sentences still match the manifests: the exclusions for negativ...
- **line 509** `For each base--flip pair we build a \emph{reading} pair, whose claims quote the decisive finding, and an \emph{application} pair`
  - results: The sentence is at paper/latex_v13/main.tex lines 509-511. Lines 504-514 contain no \res keys. The sentence says pairs are built "For each base--flip pair", and nothing in the draft limits that scope. I searched the draft for 'reading', 'application pair', 'one-line', 'any-of', 'all-of', 'k-of-n' and 'eligible'. The only other matches are lines 775-776, the tab:pk caption at 1720-1722 (which says only "L0 (%)") an...
  - note: The contradiction is the scope only. The words "For each base--flip pair" claim every pair, but pairs exist for just 1,000 L0 triplets (training rules) from single and any-of constraint rules and score rules whose decisive line alone decides the conclusion. Composite all-of and k-of-n rules are left out, which matters for a "composition gap" diagnostic.  The description of what each pair contains is correct.  Sugg...
- **line 576** `A deterministic parser maps ledger text to a state for $y_\rho$; incomplete or inconsistent ledgers have no state and yield no judge example.`
  - results: paper/latex_v13/main.tex lines 573-578 have no \res keys. The text sits under "In implementation" and says: "A deterministic parser maps ledger text to a state for $y_\rho$; incomplete or inconsistent ledgers have no state and yield no judge example."  What the code does: (1) selrm/formats.py build_examples, lines 274-287: after donor resampling, which swaps the pair key for another case from N(x), each judge exam...
  - note: This is a contradiction about procedure, and it covers both clauses of the sentence. The training pipeline has no parser from ledger text to state: the judge target is the program label already stored on the donor record. It also has no rule that drops judge examples: a malformed gold ledger stops the whole corpus build, and every run keeps all 30,000 judge examples. No measured number is affected. Donor ledgers a...
- **line 599** `after temperature scaling on development data.`
  - results: paper/latex_v13/main.tex lines 598-599 read: "For candidate selection we rank by the minimum of the two scores after temperature scaling on development data." Lines 594-604 contain no \res keys, so there is nothing to look up in tables/numbers.json; the claim is about procedure.  (1) docs/DECISIONS_D.md, row dated 2026-10-03 (file line 34): "Calibration (D-CAL) is Platt scaling, sigmoid(a s + b) per scorer, fitted...
  - note: The contradiction is real but narrow: only the method name is wrong. The rest of the sentence holds. Ranking by the minimum of the two calibrated scores matches select_eval.py (comb mode "min"). Fitting on development data also holds: the medqa_dev pool, with the 141 key-pair questions left out. The caveat on lines 601-602 that each score is scaled separately also still holds under Platt scaling. Fix: replace "tem...

### Experimental setup; audit of reward signals

- **line 614** `constraint rules over renal function, pregnancy, allergy, age and interacting drugs`
  - results: Lines 613-617 of paper/latex_v13/main.tex say: "\res{d/...} constraint rules over renal function, pregnancy, allergy, age and interacting drugs, compiled from public recommendations". In tables/numbers.json, key "d/a15/rules_total|a15/rules_by_kind.score|a15/rules_by_source.grammar_sampled@int" = 60 (353 - 43 - 250). So the sentence describes all 60 hand-written constraint rules.  data/rule_v1/RULE_MANIFEST.json h...
  - note: the first check is right. Without "such as", the five-domain list reads as a description of the whole set, and the data contradict it.  The borderline rules do not change this. Even if angioedema and HIT are counted as allergy and potassium as renal, 24 of the 60 rules (40%) are still outside the named domains.  The wording comes from the older plan in paper/latex/main.tex line 509 ("\ph{120} constraint rules over...
- **line 615** `compiled from public recommendations by the tree-then-program procedure of`
  - results: Context (main.tex 613-617): "The frozen library has \res{a15/rules_total}=353 rules: \res{..score}=43 scoring rules ..., \res{d/...}=60 constraint rules ... compiled from public recommendations by the tree-then-program procedure of \citet{shen2026medguidex}, and \res{..grammar_sampled}=250 rules sampled from a typed grammar." I looked up all four keys in tables/numbers.json: a15/rules_total@int=353, a15/rules_by_k...
  - note: Confirmed. The numbers in the sentence are right (353 = 43 + 60 + 250, as numbers.json gives them). What is wrong is the method. No tree-then-program (MedGuideX) step was used for any rule: all 60 constraint rules were written by hand as Python programs together with their rule text (PAPER_VS_CODE B-4, the manifest specification field, DECISIONS_A C1-C3, no tree code in the repository). In addition, 6 of the 60 ar...
- **line 632** `all cases derived from one base state stay in one split`
  - results: The sentence (main.tex lines 630-632, no \res keys): "In all test sets the rendering templates and cue phrases ... do not occur in training, and all cases derived from one base state stay in one split." The repository defines a base state as "the rule plus the multiset of (concept, value, subject, status, time)" (docs/DATA_AUDIT_rule_v1.md section 5, line 242). scripts/audit_rule_v1.py does the same: base_state_ke...
  - note: the first check is right. Using the repository's own meaning of "base state", the sentence is false for two of the test sets it covers: L0 (480 of 862 base states also occur in training) and L3-alt (196 of 797). It is also false for dev (162 of 280). The sentence holds only per group (DATA_AUDIT line 272). It also holds for L1, L2, L3-inv and hard, but only because their rules never occur in training (0 shared). O...
- **line 639** `All trained models use \bb{} with LoRA \citep{hu2022lora} of rank 64 for one epoch on 60{,}000 records.`
  - results: Line 639 says "All trained models use \bb{} with LoRA \citep{hu2022lora} of rank 64 for one epoch on 60{,}000 records." In main.tex line 74, \bb is defined as Qwen3.5-9B. The configuration holds for every B-F factorial seed, the B-LOKO, B-SC, B-AB-bitonly-judge and B-AB-conddrv runs. In their results_git/*/meta.json files the model is unsloth/Qwen3.5-9B, with lora_r 64, epochs 1 and 60,000 examples. This matches s...
  - note: Confirmed. The backbone claim is contradicted by a measured run the paper prints itself: the Qwen3.5-4B model at 49.9 (lines 1055-1057). The 70,000-example verification run also contradicts the record count if "records" means training examples, as in the per-configuration budget table; its corpus has 60,004 records, so that point depends on reading. Rank 64, one epoch and roughly 60,000 records are correct for eve...
- **line 671** `a PRM trained on the MedPRMBench training split (injected-error PRM)`
  - results: Line 670-675 of paper/latex_v13/main.tex (no \res keys; it is a list of systems) names "a PRM trained on the MedPRMBench training split (injected-error PRM)" among the "Audited signals". The repository says this signal was dropped and has no result: - docs/DECISIONS_C.md, 2026-10-03 audit row: "injected-error PRM not run (MedPRMBench unreleased, re-verified today)". - configs/models.json notes: "injected-error PRM...
  - note: Confirmed. The sentence describes the audit procedure, and the repository shows this part is no longer true: the audit does not include a PRM trained on MedPRMBench, because MedPRMBench has no data release (re-checked 3 Oct). The rest of the list is a separate matter: the other 12 signals are planned, though none has results yet (no C-AUD-* folders), and four of them are \ph names. the first check count is right: ...
- **line 675** `\ph{GPT-5.4}`
  - results: paper/latex_v13/main.tex:675 reads "\ph{Kimi K3}; \ph{GPT-5.4}, \ph{Gemini 3.1 Pro} and \ph{Claude Opus 5.5}." It lists GPT-5.4 as the audited closed OpenAI judge. Lines 670-680 contain no \res keys, so nothing in tables/numbers.json applies. The repository fixes a different model: - configs/models.json (top-level "verified": "2026-10-03") has an entry with name "gpt", table "Closed judge (current OpenAI flagship)...
  - note: Confirmed as a contradiction of which model was used, not of a measured number. No closed-judge result exists yet: there is no results_git/C-AUD-closed-1 or results/C-AUD-closed-1, and STATE_C.md says the API audit is waiting for COMPUTE REQUEST #1 (OPENROUTER_API_KEY). Even so, the repository has fixed the OpenAI judge as openai/gpt-6-astra, so "GPT-5.4" is no longer true. Because a run is planned, the status is ...
- **line 690** `\ph{1{,}240} key pairs from MedQA test`
  - results: Context, main.tex lines 689-691: "MedEinst test pairs, \ph{1{,}240} key pairs from MedQA test and \ph{960} from CareQA, and NLI4CT-P; versions are pinned". The line has no \res keys. The 1,240 is a typed placeholder, but registered results exist for it, and they disagree: (1) data/clin_v1/keypairs_medqa_oneway/MANIFEST.json: n_pairs 357, mode "oneway", source_file is the test + validation parquet files, questions ...
  - note: Both parts of the quoted claim are contradicted. The count is wrong: 357 pairs in the set actually used, and 13 under the v13 definition, against 1,240. The source is also wrong: the set used pools MedQA test and validation, not test alone. the first check evidence and note match the files. The suggested fix ("357 pairs from test and validation") is what the lead asked for in HANDOFFS line 45, which also adds "one...
- **line 691** `\ph{960} from CareQA`
  - results: main.tex lines 690-691: "MedEinst test pairs, \ph{1{,}240} key pairs from MedQA test and \ph{960} from CareQA, and NLI4CT-P". The line has no \res key, and tables/numbers.json has no key for the CareQA key-pair count (the only key-pair keys are D-SEL/D-SELN sel:keypairs accuracies). The frozen data contradicts 960: (1) data/clin_v1/keypairs_careqa/MANIFEST.json (v13 definition, case_description_required true): "n_...
  - note: I confirm the contradiction. The CareQA key-pair set the repository uses has 225 pairs, and the v13 definition yields only 3. Neither matches 960, and the adopted set also drops the case-description requirement that the v13 definition has. No CareQA key-pair scores exist yet: there is no summary_*keypairs_careqa* file in results_git/ or results/. The contradiction is about the size and definition of the data, not ...
- **line 693** `verdict frequencies over \ph{32} samples otherwise`
  - results: Context, main.tex lines 692-694: "Scores are verdict log-odds where token log-probabilities are available and verdict frequencies over \ph{32} samples otherwise." There is no \res key. \ph{32} is a placeholder.  The repository fixes a different readout for models without log-probabilities: - configs/models.json (verified 2026-10-03): gpt ("openai/gpt-6-astra"), gemini ("google/gemini-3.1-pro-preview") and claude (...
  - note: the first check is right about the part it quoted. Models without log-probabilities are scored by asking the two-order choice prompt once per order, giving a decision of +1, -1 or 0 (tie). The 32-sample frequency is not the registered or implemented readout. The closed-judge audit runs C-AUD-closed-1/2/3 have not run yet (todo; numbers.json values \ph{tbd}), so this is a contradicted procedure fact, not a contradi...
- **line 694** `values printed in black in this draft are from seed 0`
  - results: Context, paper/latex_v13/main.tex lines 693-695: "We train \ph{5} seeds; values printed in black in this draft are from seed 0." Several black \res values in the same draft are means over seeds 0-4, not seed 0. Checked against tables/numbers.json, the per-seed raw summaries and tables/seeds.tex: (1) run/B-F-verdict-blocks/L2/all/TA prints "53.7" (number 53.66). It is printed in black at lines 806, 815, 834, 856 an...
  - note: The sentence claims every black value comes from seed 0. That is false for the key cells (B-F-{verdict,ledger2}-{blocks,triplets}), which now print the mean of 5 seeds, and for summary2-triplets/blocks, which also print a mean over several seeds. The values differ by more than 1 point for verdict x blocks (53.7 vs 58.2 at seed 0) and ledger2 x blocks (71.0 vs 75.3). Single-seed runs (natural/balanced cells, ration...
- **line 733** `\ph{Inj.-error PRM} & \ph{tbd}`
  - results: Context: paper/latex_v13/main.tex lines 727-745 hold the generated Table 2 body ('% generated by scripts/make_tables.py (audit); do not edit'). Line 733 is a row under 'Trained PRMs': '\ph{Inj.-error PRM} & \ph{tbd}' repeated for all six columns. The line has no \res keys. tables/numbers.json (159 keys) has no run/C-AUD-injerr/* key. C-AUD-injerr appears only inside 8 composite min/max keys, and all of them have n...
  - note: the first check is right. What is contradicted is a fact about models and procedure, not a measured number. The row presents a trained injected-error PRM (Systems paragraph, line 672: 'a PRM trained on the MedPRMBench training split') as an audited signal whose results are still to come. The repository shows no such PRM exists and its audit run is dropped. Taken one by one, the six \ph{tbd} cells would be 'placeho...
- **line 749** `Rule triplets, L0: reversal, hold, triplet accuracy`
  - results: Context: lines 748-751 are the Table 2 (audit) caption: "Rule triplets, L0: reversal, hold, triplet accuracy, missing-evidence rejection at \ph{5}\% false rejection." In the draft, L0 is a different test set from L2. Line 626 defines L0 as "new generated cases of trained rules (L0)", while L2 is the held-out rule structures.  The repository puts the audit on L2: (1) docs/DECISIONS_D.md, row of 2026-10-03: "audit s...
  - note: Only the level "L0" is wrong. The audit set is L2 (DECISIONS_D and DECISIONS_C, rows of 3 Oct; make_tables.py AUDIT_SET="L2"), and the lead has already logged the caption for the authors to correct. The rest of the quoted text is right: reversal, hold and triplet accuracy match the table's Rev, Hold and TA columns. This is a procedure contradiction, not a numeric one, because no audit value has been measured yet (...
- **line 755** `Trained PRMs seldom reverse`
  - results: Paper (paper/latex_v13/main.tex:755-757): "Trained PRMs seldom reverse (\res{min/...Rev}--\res{max/...Rev}\%) and therefore hold; they solve \res{min/...TA}--\res{max/...TA}\% of triplets." The min/max keys pool run/C-AUD-{meds3,medprm,fover,injerr,thinkprm,genprm}/L2/all/Rev (and /TA), the six "Trained PRMs" rows of Table 2. In role-d tables/numbers.json every one of these keys has number null (prints \ph{tbd}). ...
  - note: the first check values are all correct. "Seldom reverse" holds only for Med-PRM (19.45) and MedS3 (22.6). FoVer reverses on half the flips (49.9, CI 43.7-56.5, committed). ThinkPRM, on its finished but unmerged 200-triplet subset, reverses almost always (96.5). Once the results are merged, the printed range would read about 19.4--96.5%, which contradicts "seldom" in the same sentence. the first check missed one mo...
- **line 756** `and therefore hold; they solve`
  - results: Lines 755-757 of paper/latex_v13/main.tex say: "Trained PRMs seldom reverse (\res{min/...Rev}--\res{max/...Rev}\%) and therefore hold; they solve \res{min/...TA}--\res{max/...TA}\% of triplets". The ranges cover C-AUD-{meds3,medprm,fover,injerr,thinkprm,genprm}. In the role-d tables/numbers.json every one of these keys has number null and prints \ph{tbd}, so the draft has no numbers here yet.  Line 437 defines Hol...
  - note: the first check is right. MedS3 seldom reverses (22.6%) but is right on only 16.35% of near-misses. It reverses rarely because it already prefers the wrong claim s' on the base case (BaseAcc 25.4), so "therefore hold" fails for it.  The other PRMs: - FoVer is middling: Rev 49.9, Hold 61.9. - Med-PRM is the only one that fits both halves: Rev 19.45, Hold 85.95. - ThinkPRM holds (90.0) but reverses on 96.5% of its s...
- **line 759** `Reversal is lower on MedEinst for every signal`
  - results: Line 759-760: "Reversal is lower on MedEinst for every signal and higher on key pairs, which are not minimal." The sentence has no \res keys. It compares the Table 2 ME column with its rule-triplet Rev column. scripts/make_tables.py:546 sets AUDIT_SET = "L2" ("v13's caption says L0"). Line 558 fills ME from clin_v1:medeinst_test/Reversal, and line 559 fills Key from keypairs_medqa_oneway/Reversal. The two metrics ...
  - note: the first check is right: "lower on MedEinst for every signal" fails for MedS3 PRM, with MedEinst 25.1 against L2 Rev 22.6, the opposite direction. The contradiction covers only the MedEinst clause. "Higher on key pairs" holds for all 4 signals measured so far. The MedS3 gap is small and not significant: the L2 rule-bootstrap CI [17.6, 28.4] contains 25.1. The sentence states a direction for every signal, so it is...
- **line 776** `fails the full pair in \ph{11}--\ph{80}\% of the cases in which it solves both`
  - results: Paper, main.tex lines 775-777: "Every signal reverses correctly on at least \ph{84.9}\% of reading and of application pairs and fails the full pair in \ph{11}--\ph{80}\% of the cases in which it solves both (Appendix~\ref{app:diag})". Both values are \ph placeholders, and the sentence uses no \res keys. tables/numbers.json has no composition-gap, P, K or G key; its only readapply keys are B's readapply TA.  Measur...
  - note: The quoted range is contradicted. The sentence says every signal fails the full pair in 11-80% of the cases where it solves both reading and application. The only measured signal, the untrained Qwen3.5-9B backbone (C-TF-critic), fails in 7.9% of 944 cases. That is 3.1 points below the stated lower bound of 11. The rest of the same sentence holds for this signal: P 97.7 and K 96.0 are both at least 84.9. The other ...

### Training distribution and representation

- **line 820** `The statement is limited to these three formats: the`
  - results: Context, main.tex lines 819-821: "...the applicability ledger from \res{...ledger2-blocks...}\% to \res{...ledger2-triplets...}\%. The statement is limited to these three formats: the matched prose pipeline has no blocks run yet (\res{run/B-F-summary2-blocks/L2/all/TA})."  1. The key in that parenthesis is no longer empty. In tables/numbers.json, "run/B-F-summary2-blocks/L2/all/TA" has number 64.9125 and value "64...
  - note: the first check read the evidence correctly. Every number they cited reproduces from the raw summaries.  **Rewrite.** Drop the three-format restriction and the clause saying the prose blocks run is missing. Add the remaining two formats: - **Prose:** 64.9 to 98.5 (+33.6). Blocks averages seeds 0-3 and triplets seeds 0-4. Seed 4 of prose blocks is only CLAIMED, so the key will change slightly when it finishes. - **...
- **line 821** `matched prose pipeline has no blocks run yet (\res{run/B-F-summary2-blocks/L2/all/TA})`
  - results: main.tex lines 820-821: "The statement is limited to these three formats: the matched prose pipeline has no blocks run yet (\res{run/B-F-summary2-blocks/L2/all/TA})". tables/numbers.json: run/B-F-summary2-blocks/L2/all/TA = {"number": 64.9125, "value": "64.9"}, so the sentence prints "(64.9)" right after saying no run exists. Raw results: results_git/B-F-summary2-blocks-s0..s3 each have DONE (s0 DONE timestamp 202...
  - note: I confirmed the first check reading. The clause "no blocks run yet" is false: summary2 x blocks has four finished seeds (0-3), and the key the sentence cites prints the measured 64.9, so the sentence contradicts itself. The lead-in "The statement is limited to these three formats" rests on that clause, so it no longer holds either. The matched prose pipeline now shows the same pattern as the other formats: 64.9 on...
- **line 834** `and blocks are level with it (\res{run/B-F-verdict-blocks/L2/all/TA}\%)`
  - results: The context is paper/latex_v13/main.tex lines 833-834: "At seed 0 the balanced corpus is below the natural one (\res{...balanced...TA}\% against \res{...natural...TA}\%) and blocks are level with it (\res{run/B-F-verdict-blocks/L2/all/TA}\%)".  Values from tables/numbers.json (paper/latex_v13/numbers.tex prints the same): - run/B-F-verdict-blocks/L2/all/TA = 53.7 (number 53.66), lo 49.7, hi 57.3. - run/B-F-verdict...
  - note: the first check figures all check out. The quoted clause ("blocks are level with it", printing 53.7) is contradicted, because the key now averages seeds 0-4 while the sentence still says "At seed 0". There is also a mismatch: a 5-seed blocks mean is compared with single-seed natural and balanced cells, whose seeds 1-2 are only CLAIMED and not finished.  There is no paired blocks-vs-natural comparison in docs/RESUL...

### Transfer within and beyond rules

- **line 904** `Criteria: triplet accuracy on verbatim eligibility criteria`
  - results: Context: line 904 is in the Table 4 (tab:main) caption. Lines 899-909 contain no \res keys. Every cell of the Criteria column is \ph{tbd}, and tables/numbers.json has run/B-F-ledger2-triplets/ec_v1:test/all/TA and run/B-F-verdict-triplets/ec_v1:test/all/TA = {"number": null, "value": "\ph{tbd}"}. So no accuracy value exists yet. The contradicted part is the data claim "verbatim".  1. docs/EC_SIGNOFF.csv has 95 row...
  - note: Only the word "verbatim" is contradicted. The rest of the clause (triplet accuracy on registered eligibility criteria) matches the design: the ec_v1 keys measure TA. Those values are pending, because ec_v1 is "still not frozen and not to be scored" (docs/HANDOFFS.md line 60).  the first check 37% counts punctuation-only edits. A stricter count of real wording changes is 20 of 95 (21%), and that is still clearly no...
- **line 907** `Black: measured, seed 0;`
  - results: Context: paper/latex_v13/main.tex lines 902-915 are the caption of Table tab:main (Transfer). The table body between the "% <tables:main>" markers is exactly tables/main.tex, which make_tables.py writes. The cell() function in make_tables.py adds \sd{} (defined at main.tex:61 as "±x") whenever a run key has n>1 seeds.  What the table prints now, from tables/main.tex: - Verdict only, rule blocks: 53.7\sd{5.4}, 89.8...
  - note: Confirmed. The "measured" half holds: every black cell traces to a results file. The "seed 0" half is wrong for most cells of the trained rows.  Cells that are seed means: - Five seeds (0-4): every rule-tier cell (L2, L3-alt, Hold, MR) of verdict-blocks, verdict-triplets, evidence-summary-triplets, Ledger-RM-blocks and Ledger-RM-triplets. - Two seeds: the verdict-blocks TrialGPT cell (seeds 0 and 2) and the verdic...
- **line 908** `external columns keep earlier placeholder values for MedEinst.`
  - results: This clause sits in the caption of Table tab:main (paper/latex_v13/main.tex lines 902-914). Lines 903-913 contain no \res keys, so there is nothing to look up in numbers.json. The table body at v13 lines 875-899 is generated and matches tables/main.tex line for line.  MedEinst column, row by row: - Critic: 24.2. Measured: results_git/C-ME-critic/summary_clin_v1~medeinst_test.json gives Reversal 24.187 over n_pairs...
  - note: I agree with the first check: the clause should be deleted, or replaced with "unmeasured external cells are marked" to match the rule-tier wording.  Two small corrections to the evidence: 1. The PAPER_NUMBERS.md note says "every external cell is now \ph{tbd}". That is itself out of date: it matches the older paper/build/main.tex snapshot, where all external cells were tbd. In v13, two MedEinst cells and seven Tria...
- **line 932** `on verbatim eligibility criteria`
  - results: Line 932-933 of paper/latex_v13/main.tex reads: "on verbatim eligibility criteria \res{run/B-F-ledger2-triplets/ec_v1:test/all/TA} and \res{run/B-F-verdict-triplets/ec_v1:test/all/TA}". In tables/numbers.json both keys have number null and value '\ph{tbd}', so the two scores are pending. Only the word "verbatim" is in question.  1. What the models see: ec_v1/SIGNOFF_GUIDE.md says 'rule_text_shown' is "what models ...
  - note: Confirmed. The descriptor "verbatim" in line 932 is false for the ec_v1 criteria as the models see them: 35 of 95 differ from the registered text, and 18 of those change content (unit conversions, added units, a dropped mM equivalent, added clauses about whether the boundary day counts). The rest of the sentence is not contradicted: both ec_v1 TA keys are pending (null, tbd).  The same wording appears elsewhere: "...
- **line 941** `A gain there shows better criterion judgments on that benchmark`
  - results: Context (paper/latex_v13/main.tex 936-944): the sentence comes right after the macro-F1 numbers. Those keys resolve in tables/numbers.json to: run/C-TG-ledger2-triplets/.../macroF1 = 69.1, C-TG-critic = 65.7, C-TG-ledger2-blocks = 70.9, evidence P/R = 55.6/67.9. So the sentence presents the 69.1 vs 65.7 difference as showing better criterion judgments.  Contradicting evidence, checked against the source files: (1)...
  - note: the first check evidence is all correct. In context, the clause presents the TrialGPT macro-F1 gain over the untrained backbone as showing better criterion judgments. The measured gain is only a nominal +3.4, with a 95% CI that includes 0 (p 0.244). This is the "other significance" case, and the registered comparison (6) is recorded as not supported.  Breaking the gain down by class weakens the claim further: - Th...
- **line 947** `Adding MedPRMBench step-error data to the adapter adds \res{d/run/B-TR-steperr/clin_v1:medeinst_test/top/Reversal|run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal} points`
  - results: Context (main.tex lines 945-948): this sentence comes right after the MedEinst rule-only result. It says: "Adding MedPRMBench step-error data to the adapter adds \res{d/run/B-TR-steperr/...|run/B-F-ledger2-triplets/...} points, which is medical supervision and not transfer."  Key lookup: - tables/numbers.json line 94: the key "d/run/B-TR-steperr/clin_v1:medeinst_test/top/Reversal|run/B-F-ledger2-triplets/clin_v1:m...
  - note: the first check read the evidence correctly. The sentence says the adapter was trained with MedPRMBench step-error data. The repository shows that data was never released and the run was dropped (DECISIONS_B.md, 3 Oct row; HANDOFFS.md, C, 3 Oct). This is the rubric's "stated fact about data/procedure that is no longer true" case.  The contradiction is in the premise, not in a measured number. The \res value is nul...

### What the judge uses

- **line 993** `\node[font=\tiny, text=blue!75!black, anchor=south east] at (axis cs:64,76.0) {\method};`
  - results: Line 993 has no \res key. It is the generated label of the blue curve at line 992, coordinates (1,67.3) (2,71.3) (4,72.0) (8,78.0) (16,78.0) (32,78.0) (64,76.0). Those values are exactly selector=combined in results_git/D-SELN/summary_sel~keypairs.json (n_pairs 150). The mapping comes from scripts/make_tables.py line 808: SELN = [("combined", "blue!75!black", "mark=*", r"\method"), ...]. \method expands to "Ledger...
  - note: Only the name is wrong. The anchor (64, 76.0) does sit at the end of the plotted combined curve, so the node is placed correctly but names the wrong system.  There is one possible defence: line 598 says "For candidate selection we rank by the minimum of the two scores", which could be read as the method's selection rule. But Table 5 and App. line 2070 consistently call that selector "Combined" / "the combined rewa...

### Candidate selection, conclusion, limitations

- **line 1094** `Step check: injected-error PRM.`
  - results: The sentence has no \res keys. It states which model the step check is, and the repository shows a different model. The chain from Table 5 to the model, as I read it in the files: (1) scripts/make_tables.py line 616 builds Table 5's "Step check" row from run D-SEL-stepcheck (results_git/D-SEL-stepcheck/summary_sel~medqa.json acc 86.17; the table shows 86.2). (2) scripts/select_eval.py lines 233-234: out["stepcheck...
  - note: The whole quoted sentence is contradicted. No injected-error PRM exists in this repository, and every Table 5 step-check number comes from the released Med-PRM (dmis-lab/llama-3.1-medprm-reward-v1.0@6948b9e), run with the model card's prompt and readout and no retrieved documents. the first check rewrite is right, for example: "Step check: released Med-PRM, run without retrieved documents." Related lines carry the...
- **line 1094** `Ledger score: \method{} trained on rule triplets and clinical pairs.`
  - results: Context: the quoted sentence is the Table 5 (tab:downstream) caption, lines 1094-1095: "Ledger score: \method{} trained on rule triplets and clinical pairs." It has no \res keys. The "Ledger score" row comes from tables/downstream.tex and reads 83.8 / 88.4 / 71.1 / 26.2 / 73.2 / 49.8. Those values match results_git/D-SEL-ledger/summary_sel~*.json: medqa acc 83.82, careqa 88.4, keypairs pair_acc 71.15, medeinst pai...
  - note: Confirmed. The caption says the Ledger score row (and so Combined) comes from the model trained on rule triplets plus clinical pairs. Every measured number in those rows actually comes from the rule-only model B-F-ledger2-triplets-s0, with -blocks-s0 used for the no-near-misses row. The clinical-pairs model has not been trained: B-TR-tripclin-s0 is only queued. The table makes this worse: the sub-row labelled "rul...
- **line 1105** `non-inferior at a margin of one point).`
  - results: Lines 1103-1105 of paper/latex_v13/main.tex: "difference \res{d/...D-SEL-combined...|...D-SEL-stepcheck...} [\res{cmp/sel-mqa-comb-step/lo}, \res{cmp/sel-mqa-comb-step/hi}] on MedQA, non-inferior at a margin of one point)." The sentence claims the combined reward is non-inferior to the step check, with a margin of 1 point.  Values from tables/numbers.json: the difference key = -0.9 (-0.864), cmp/sel-mqa-comb-step/...
  - note: the first check was right. The whole quoted clause is contradicted. For a 1-point margin the lower bound of the combined-minus-step-check difference would have to be above -1. It is -2.1 on MedQA, and -1.5 on CareQA, which the sentence does not mention. This holds whether you use the 95% two-sided interval or a one-sided 95% interval. On a one-sided 95% interval the bounds are -1.9 and -1.2, which I recomputed wit...
- **line 1107** `Swapping in the vignette of another question removes the gain of the combined reward`
  - results: Context (paper/latex_v13/main.tex 1107-1110, no \res keys in this sentence): "Swapping in the vignette of another question removes the gain of the combined reward and leaves the step check almost unchanged: the ledger score depends on the supplied case." The Table 5 rows (lines 1077-1084, same as tables/downstream.tex) come from raw summaries I read in results_git/D-SEL-*/summary_sel~*.json: - MedQA acc: single 82...
  - note: The quoted clause is contradicted under both readings of "gain": over the single sample, the gain stays; over the step check, there is none.  Same sentence, other clauses: - "Leaves the step check almost unchanged" holds: 86.2 to 85.6, sel-mqa-step-swap 0.55 [-1.10, 2.44], p 0.554. - The contrast the sentence draws does not exist: both rewards are flat under the swap. So this control does not support "the ledger s...
- **line 1110** `That the dependence is correct is what the pair columns show.`
  - results: Context (main.tex 1104-1110): the sentences compare the combined reward with the step check on both pair columns, then say the vignette swap shows "the ledger score depends on the supplied case. That the dependence is correct is what the pair columns show." I looked up the \res keys in tables/numbers.json, and they match the raw summaries. Key pairs: combined 76.8 (D-SEL-combined/summary_sel~keypairs.json pair_acc...
  - note: the first check is right. The pair columns do not show that the case-dependence is correct. The combined reward is no better than the step check on either pair column, and it does as well or better with a swapped vignette (76.8 against 76.8; 22.6 against 23.0). Only one cell leans the claim's way: ledger alone on MedEinst pairs, 26.2. No registered comparison tests it, its unregistered CI against the step check in...
- **line 1112** `As $N$ grows, pair accuracy under the step check stays flat`
  - results: Context (main.tex lines 1111-1114): "As $N$ grows, pair accuracy under the step check stays flat while the oracle rises (Figure~\ref{fig:diversity}, right)." The sentence has no \res keys.  Evidence I read myself: - results_git/D-SELN/summary_sel~keypairs.json (n_pairs 150). Step check: N1 67.3, N2 70.7, N4 72.7, N8 78.0, N16 79.3, N32 79.3, N64 78.0. Oracle: 67.3, 80.0, 87.3, 91.3, 94.0, 95.3, 96.7. Combined: 67....
  - note: the first check is right about the clause it quoted. The rest of the sentence holds: the oracle rises from 67.3 to 96.7. So does the widening gap: regret is 0 at N=1, 13.3 at N=8 and 18.7 at N=64.  Suggested rewrite from measured values: "pair accuracy under the step check rises from 67.3% to 78.0% by N=8 and then levels off near 78-79%, while the oracle keeps rising to 96.7% (regret 18.7 points at N=64; combined ...
- **line 1145** `most judgments concern one condition of one rule`
  - results: Context, main.tex l.1142-1148 (Limitations, "The rule language"): "...there are few such classes, and most judgments concern one condition of one rule: the task is local applicability verification, not clinical reasoning." There are no \res keys in l.1140-1150. The appendix repeats the claim at l.1365, "Most judgments concern one condition of one rule; where that is so we call the task local applicability verifica...
  - note: Confirmed for the clause "most judgments concern one condition of one rule": 2.51 conditions per judgment on L2, and 17.2% of L2 judgments need one condition (41.9% in train, 36.4% across all test sets). The rest of the same sentence holds. "Few such classes": test_L2 has 5 signature classes (data_stats.json) out of 21 in the library (DATA_AUDIT section 1). "Reuse primitives": 76.3% of L2 criterion subexpressions ...
- **line 1153** `by expert-reviewed distractors in real discharge summaries that attribute a correct fact to the wrong admission \citep{kim2026ehrnotechatqa}`
  - results: Sentence context (main.tex 1150-1156): "Beyond rules, holding is tested on author-written cases and registered criteria ... and on the claim side: by NLI4CT-P consistency under statement edits and by expert-reviewed distractors in real discharge summaries..." It contains no \res keys, so the claim is about procedure: it says the test was run. The repository shows it was not run and cannot be: - docs/RUN_MATRIX_C.c...
  - note: Confirmed for the quoted clause. The description of the dataset is accurate (docs/REVIEW_HISTORY.md line 157: expert-reviewed distractors, including a "correct fact attributed to the wrong admission" pattern). What is wrong is the claim that holding "is tested" on it: DECISIONS_C (3 Oct) records it as not run because the data is not released.  The NLI4CT-P clause in the same sentence is a different matter. Its con...
- **line 1188** `Measured values in this draft come from one seed and one backbone.`
  - results: Line 1188 of paper/latex_v13/main.tex, under "Interpretation and scope", says "Measured values in this draft come from one seed and one backbone." The sentence has no \res keys. The draft itself contradicts both halves.  (1) "One seed" is contradicted. tables/numbers.json gives run/B-F-verdict-blocks/L2/all/TA = 53.66 ('53.7'). That is the mean of the s0-s4 values in results_git/B-F-verdict-blocks-s{0..4}/summary_...
  - note: The verdict holds but one detail of the first check evidence is wrong. It said B-BB-qwen3.5-4b-* has results for seeds 0-2. Only results_git/B-BB-qwen3.5-4b-verdict-blocks-s0 is DONE. The other 11 B-BB directories hold only CLAIMED_B: verdict-blocks s1-s2, and s0-s2 for verdict-triplets, ledger2-blocks and ledger2-triplets.  Even so, the draft prints one 4B value (49.9, line 1056), so "one backbone" is false. "One...

### App. A-C (analysis plan, rule library, triplet construction)

- **line 1210** `Values printed in black in the factorial, transfer, ablation, ladder and shortcut tables are measured on \texttt{rule\_v1} with seed 0.`
  - results: Line 1210 is a draft-status note inside \ifplaceholders. It contains no \res keys of its own. Both of its claims are now false.  (1) "with seed 0". docs/HANDOFFS.md line 79 (3 Oct, D, merge 5) says: "the key cells now have seeds 0-4, so every \res key of them prints the mean over the available seeds". docs/DECISIONS_D.md line 12 (3 Oct) says make_tables.py pools seeds s0..s4. The make_tables.py docstring says the ...
  - note: the first check evidence is correct. The banner is out of date in both halves. "Seed 0" is wrong for every cell that now pools several seeds, in the factorial, transfer, ablation and ladder tables. "rule_v1" is wrong for the transfer table's XA, TrialGPT and MedEinst cells. Parts of the sentence still hold: - The shortcut table: A-D14 scorers on L2, which have no training seed. - The cells measured at one seed onl...
- **line 1238** `If the gain in (4) appears only with step-error data, it is reported as a gain from medical supervision.`
  - results: The line is in context: App. A "Decision rules", main.tex lines 1234-1239, rule (4) = "rule-only \method{} against the untrained critic" on MedEinst. The sentence has no \res keys. Its condition needs a Ledger-RM adapter trained with step-error data. The same draft plans that adapter as the Table 4 row "\method{}, rule triplets + step-error data" (line 892) and as the key d/run/B-TR-steperr/... (line 947).  The re...
  - note: the first check read the evidence correctly. This is a contradiction about procedure, not a measured number that disagrees. The rule depends on a step-error-data variant (B-TR-steperr) that DECISIONS_B (3 Oct) and RUN_MATRIX_B record as dropped, so its condition can never be checked and the analysis plan no longer describes what will be done. The repository shows no sign the variant will return: the 2 Oct B-PRM ro...
- **line 1243** `awaits the paired test.`
  - results: Context (main.tex 1241-1243, 'Status at seed 0'): "(3) is \res{d/run/B-F-ledger2-triplets/L2/all/TA/s0|run/B-F-summary2-triplets/L2/all/TA/s0} points near the ceiling and awaits the paired test." The \res key resolves in tables/numbers.json to 1.2 (PROVENANCE: d of run/B-F-ledger2-triplets/L2/all/TA/s0 = 99.2 and the seed-0 summary2 value; ANALYSIS_B sec. 1: 99.2 vs 98.0). The paired test exists. (a) tables/primar...
  - note: The quoted claim that (3) still awaits the paired test is no longer true. The paired test has been run at seed 0 (+1.2 [+0.2, +2.2], p 0.016) and over seeds 0-4 (+0.8 [0.3, 1.3], p 0.004); only the Holm adjustment is pending. The rest of the sentence holds: '1.2 points near the ceiling' matches the seed-0 key value (1.2). The pooled five-seed estimate is 0.8, so the 'Status at seed 0' wording is out of date. Sugge...
- **line 1314** `specification review by a second author`
  - results: main.tex l.1314 (App. "Rule Library and Splits", Table tab:validity) gives "specification review by a second author" as evidence that the program implements the stated rule. The line has no \res keys. The repository says no author has done this review. - data/rule_v1/RULE_SOURCES.json: for all 103 hand-written rules, checked_by = "a reviewer that is not a person + a reviewer that is not a person (adversarial verif...
  - note: Only the review phrase is contradicted, and it is the whole of the first check quote. The review that was actually done was by a reviewer that is not a person and a reviewer that is not a person, not a second author, and no author review is recorded or scheduled for rule_v1. So this is a wrong statement about procedure, not a pending result. The tests half of the cell ("boundary, unit and dependency tests") was no...
- **line 1328** `Formalisations of source-derived rules are checked against the source sentence by an author who did not write them`
  - results: paper/latex_v13/main.tex l.1324-1333 ("Manifest and provenance", about the rule library) has no \res keys. Its only values are \ph{tbd}: the verbatim, simplified and synthetic counts, and "\ph{tbd} of \ph{tbd} were corrected or dropped".  Four sources say no author has done this check: (1) docs/DATA_AUDIT_rule_v1.md l.49-50 (last regenerated a6cc31a, 2026-10-03 09:43, after A checked PAPER_VS_CODE against v13): "T...
  - note: the first check is right. The sentence says an author who did not write the formalisations checks them against the source. The repository says the check was done by a reviewer that is not a person (a reviewer that is not a person plus a reviewer that is not a person trying to refute each finding), and no author has checked any of the 103 hand-written rules.  A check against the source text does exist (supporting_t...
- **line 1340** `none was found in base, flip, near-miss or presentation cases`
  - results: paper/latex_v13/main.tex 1339-1342: "reviewed for label errors \ph{...}; none was found in base, flip, near-miss or presentation cases, and missing-input lines that could be read as ''absent'' were reworded". Lines 1335-1345 contain no \res keys; "450" is plain typed text.  1. audit/model_review/reviews.json, round 1, session 1. The reviewer writes "No case is plainly mislabelled under the program's semantics", bu...
  - note: Confirmed for the quoted clause. The rest of the sentence holds: 450 groups were reviewed before the freeze (300 in round 1, 150 in round 2), and the "unknown" wording for missing inputs is among the listed fixes.  The clause is true only if "label error" means "the stored label disagrees with the program". That is true for every case kind, including the missing twins. But then the sentence could not single out th...
- **line 1344** `near-misses that differed from the flip in more than one attribute were found and removed`
  - results: Context (main.tex lines 1338-1348, Rendering audit paragraph): "Presentation edits that changed a fact, sampled alternatives ruled out by the condition, and near-misses that differed from the flip in more than one attribute were found and removed." There are no \res keys on this line, only nearby \ph{tbd} and \ph{[state who reviewed them...]}, so there is nothing to look up in numbers.json.  (1) tables/data_stats....
  - note: the first check evidence is accurate and I re-read every source myself. The sentence implies that no near-miss in the released sets differs from its flip in more than one attribute. In fact 670 of 2,180 negation near-misses in the test and dev sets (30.7%) differ in status and also in time or subject; in test_L2 it is 136 of 400. This happens on criteria that count past or family mentions: the flip may be a past o...
- **line 1352** `It is derived from a public drug-label or guideline recommendation in three steps taken from \citet{shen2026medguidex}`
  - results: Context, main.tex lines 1350-1358: the sentence goes on to say "a model extracts the recommendation, writes it as a decision tree, and compiles the tree to a program", and that we "show the verbalised tree in the prompt". Lines 1347-1357 contain no \res keys to resolve.  1) The three-step MedGuideX procedure was never used. - docs/PAPER_VS_CODE.md B-4, which checks the v13 text, says: "The MedGuideX extract–tree–c...
  - note: Confirmed. The main assertion, that rules were derived through MedGuideX's extract, decision-tree, compile steps, is false for every rule: the library was written by hand as programs with rule text, plus grammar sampling.  The source-derivation half holds only in part: - It is true for 54 of the 60 hand-written constraint rules (simplified_source, with simplifications listed). - It is false for 6 synthetic hand-wr...
- **line 1360** `Every case reports the same fields with raw values, so the presence of a field carries no label information.`
  - results: The sentence is at main.tex lines 1360-1361 and contains no \res keys. It is the last sentence of the "Constraint rules and claims" paragraph and makes a claim about every case.  1) tables/data_stats.json, semantics/all_test_and_dev (audit commit 412a4d2, code_modified_since_commit False), covering 47,600 labelled test and dev cases: - finding_bases = 5156 and finding_bases_naming_concept = 0, so the decisive find...
  - note: Both halves of the sentence fail for findings and hold for measured inputs. Every measured input appears in every labelled case (56,592 of 56,592). For findings, the cases do not all report the same fields, and whether the finding is named carries label information: it separates base from flip. By design it does not separate flip from near-miss, which is why it solves no triplet (Proposition 1). I rate this confir...
- **line 1365** `Most judgments concern one condition of one rule`
  - results: Line 1365 has no \res keys. In context it introduces Table tab:structure, whose own row is "Conditions needed per judgment (mean; max)" (cells are \ph{tbd}). That row is measured in tables/data_stats.json, structure: train_triplets conditions_mean 1.79, test_L2 conditions_mean 2.51, conditions_max 4 for both. scripts/audit_rule_v1.py judgment_rows (line 329) defines the count as one row per conclusion claim with '...
  - note: The main claim, "most judgments concern one condition", is contradicted by the measure in the table the sentence introduces. Two parts still hold. "Of one rule" is true: every rule_v1 group sits under one stated rule, and two-rule items exist only in xr_v1. "Where that is so we call..." only names the task, so it is not a factual claim. the first check other reading, that each flip edits exactly one target criteri...
- **line 1399** `All cases derived from one base state are in one split.`
  - results: Line 1399-1400 of paper/latex_v13/main.tex has no \res key. It sits in the general "Splits and overlap" paragraph, and its main-text twin at line 632 says the same for "all test sets". Line 341 of the draft defines a state by its content: "A generated state z is a set of mentions".  The repository uses the same content definition. scripts/audit_rule_v1.py, base_state_key = (rid, sorted (concept, value, subject, st...
  - note: As worded, the sentence is false for L0, dev and L3-alt. The draft defines a state by its content, and identical base states have cases in both training and those sets (480/862, 162/280, 196/797). It holds only in the sense that each generated group (base, flip, near-miss, presentation) stays in one split, and for L1, L2, L3-inv and hard, where rule-keyed overlap is 0. Use the first check rewording, "All cases of ...
- **line 1404** `which is why models that fail on other kinds do well on it.`
  - results: Context, main.tex 1402-1405: "L3-alt moves one or two thresholds and keeps only cases whose outcome differs ...; its near-miss kinds are \ph{tbd}, which is why models that fail on other kinds do well on it." The quote has no \res key, so it rests only on that placeholder.  What L3-alt contains (tables/data_stats.json /l3alt/near_miss_kinds; docs/DATA_AUDIT_rule_v1.md section 6): boundary 333, time 333, numeric 334...
  - note: the first check is right. The part that holds is the observation: models that fail on subject and negation on L2 do well on L3-alt (critic subject 18.8 and negation 24.2, yet 83.9 on L3-alt; verdict x blocks subject 9.8, yet 89.8). The part that is contradicted is "which is why", the claim that the near-miss kinds explain it. The same models also fail on L2 the kinds L3-alt does contain, and solve those same kinds...
- **line 1421** `Of the proposed flips, \ph{7.9}\% are discarded because a second criterion changes or the claim does not`
  - results: The sentence is paper/latex_v13/main.tex lines 1421-1422 (App. C "Invariants"): "Of the proposed flips, \ph{7.9}\% are discarded because a second criterion changes or the claim does not". It has no \res key. 7.9 is a \ph value that was typed in and never measured, and tables/numbers.json has no key for reject or discard rates.  What the repository measured: (1) The generation logs of every registered set (data/rul...
  - note: the first check is right: the measured rate is 0%, more than 1 point from the stated 7.9%. The sentence also describes the procedure wrongly, because flips are decisive by construction (engine.pivots). Outside the quoted clause, the rest of the same sentence ("of the proposed missing twins, \ph{18.6}\% because the remaining inputs determine the claim") is also contradicted. When the twins were regenerated from the...
- **line 1423** `of the proposed missing twins, \ph{18.6}\% because the remaining inputs determine the claim`
  - results: paper/latex_v13/main.tex l.1421-1424 (App. C "Invariants"): "Of the proposed flips, \ph{7.9}\% are discarded ...; of the proposed missing twins, \ph{18.6}\% because the remaining inputs determine the claim." The line has no \res key; 18.6 is a typed placeholder. tables/numbers.json has no key for the missing-twin rejection share (docs/PAPER_NUMBERS.md row 1416 says the same).  Measured result in tables/data_stats....
  - note: the first check is right. The sentence's figure, 18.6% of missing-twin proposals discarded because the remaining inputs determine the claim, is contradicted by the measured rate of 0%: 0/1000 on missing and 0/306 on dev_missing for that reason. That is off by far more than 1 point. The check itself is real (_check_missing executes the base and flip completions), so the procedure the sentence implies is accurate; i...
- **line 1424** `Near-misses are checked by executing the program on the state recovered from the rendered case`
  - results: The sentence has no \res keys, so there is nothing to look up in numbers.json. docs/PAPER_VS_CODE.md C-4 checks this exact v13 text and says: "*Does not match.* The program executes on the generator's state; no parser recovers a state from text." The audit ran at commit 412a4d29, and the doc records that the code has not changed since. I checked the code directly. In selrm/engine.py, case() sets the state to the g...
  - note: The quoted clause is wrong. Near-misses are checked by running the program on the generator's state, which is what the text is rendered from, not on a state recovered from the rendered case. This holds even in the rewritten tier, where the extracted states are only compared with the generator's state. The second half of the same sentence ("the equalities h_k ... are checked on the rendered text of every triplet") ...
- **line 1433** `for a measurement the most recent value dated at or before the reference date`
  - results: The sentence (main.tex lines 1432-1434, Appendix C "Semantics") contains no \res or \ph keys, so it was checked against the code and the data audit.  1. Code: selrm/rules.py Criterion.evaluate (lines 61-63) does not pick the latest value. It builds 'vals = [m.value for m in app if m.status == "present"]' and then runs 'if len(vals) != 1: raise ValueError(...)'. Criterion.applies (lines 52-53) drops every past ment...
  - note: The quoted measurement clause is contradicted as a statement of procedure. No program picks the most recent of several values, and no rule_v1 case states a reference date (0 of 47,600). The criterion counts exactly one current value, and two counted values raise an error.  In every generated case the current value is also the newest one, because older values are past mentions dated with a year or marked as replace...
- **line 1439** `values exactly at a threshold form their own near-miss kind`
  - results: Context, main.tex lines 1438-1440: "Thresholds are inclusive or exclusive as the rule text says, and values exactly at a threshold form their own near-miss kind." The line has no \res keys, so numbers.json is not involved.  1. selrm/engine.py lines 42-47: nm_kinds() adds "boundary" only when c.op in ("<", ">"). Its docstring says "a value exactly at a strict threshold". 2. selrm/engine.py line 212: "flip_v = thr  ...
  - note: The quoted clause is a general statement and the current data contradict it. At an inclusive threshold (>=, <=) a value exactly at the threshold is not a near-miss. It is a flip, because the label changes. This is deliberate (DECISIONS_A item 8): 411 of 1,198 inclusive numeric flips in test and dev sit exactly on the threshold, 98 of 254 in test_L2. The clause is true only for strict thresholds: the "boundary" kin...
- **line 1440** `Every case has a reference date`
  - results: Line 1440 (appendix "Semantics" paragraph) reads: "\emph{Time.} Every case has a reference date; ''within $W$ months'' includes the boundary day." The sentence has no \res keys, so tables/numbers.json does not apply. (1) tables/data_stats.json, semantics.all_test_and_dev: cases_stating_a_reference_date = 0, and semantics.test_L2: cases_stating_a_reference_date = 0. The same file has generator_reference_year = 2026...
  - note: The quoted claim is false as a universal statement. None of the rule_v1 cases (L2 test, dev, all training corpora) states a reference date. The generator keeps only an unshown internal year, 2026, and role A's audit says outright that the cases have no reference date. Only the xr_v1 and ec_v1 cases state a visit date. The second clause of the same sentence ("within W months includes the boundary day") does hold wh...
- **line 1444** `\ph{tbd}\% of base cases state the required absence explicitly`
  - results: Context, paper/latex_v13/main.tex lines 1443-1446: "This is a stipulation of the generator, not a general reading of clinical notes; \ph{tbd}\% of base cases state the required absence explicitly, and results on that subset are \ph{tbd}." Lines 1439-1449 contain no \res keys. tables/numbers.json has 159 keys and none of them is this share.  Raw result, results/A-AUDIT/summary.json (same values in tables/data_stats...
  - note: the first check is right. By construction the share is 0 (0 of 5,156 finding bases in test and dev; 0 of 932 in L2). So the explicit-absence subset that the sentence reports results on is empty, and no such slice exists or is planned.  - **Clause 1:** read literally, filling the share with "0%" would make it true. But the sentence goes on to report "results on that subset", which only makes sense if some bases sta...
- **line 1487** `notes rewritten by \ph{Gemma-3-27B}`
  - results: paper/latex_v13/main.tex:1487-1488: "notes rewritten by \ph{Gemma-3-27B} are accepted if two extractors recover the intended state (\ph{8.7}\% rejected)". The model name is a typed placeholder. The repository fixes a different rewriter: - docs/DECISIONS_A.md line 33 (2026-10-02, rewrite_v1 row): "rewriter google/gemma-4-31b-it; extractors deepseek/deepseek-v4-pro and openai/gpt-oss-120b; acceptance only when both ...
  - note: The claim is confirmed only for the model name. Under the task's STATUS rule, a stated fact about models that a DECISIONS row shows is no longer true counts as contradicted. Here the conflict is with the configured procedure (DECISIONS_A, 2 Oct, and scripts/rewrite_tier.py:39), not with any run output, because A-D11 has not run.  The rest of the sentence: - The two-extractor acceptance rule agrees with DECISIONS_A...

### App. D-E (external tiers, ledger format)

- **line 1511** `Rule-side variants of a criterion are labelled as`
  - results: Context (main.tex 1500-1513, App. D "Registered eligibility criteria"): "The set is used for testing only; ... Rule-side variants of a criterion are labelled as synthetic interventions on the original text." The sentence has no \res keys. Here "a criterion" means a registered criterion, and "the original text" means its registered wording.  What the repository shows: (1) ec_v1/prepare_summary.json: by_kind = {nume...
  - note: the first check three citations check out. ec_v1 has no rule-side variants, and DECISIONS_A records that no registered criterion is modified. The sentence describes a labelling step from the P0.2 plan, and that step was never carried out. Read strictly as a conditional convention, the sentence is empty rather than false: no data carry a different label. But in a description of what the set contains, it tells the r...
- **line 1541** `evidence where released and from a token diff otherwise; the two agree on`
  - results: Context (main.tex 1538-1546, MedEinst paragraph): 'the found targets are the findings in which the two cases differ, taken from the structured evidence where released and from a token diff otherwise; the two agree on \ph{96.2}\% of a sample of \ph{500} pairs'. The line has no \res keys, only \ph values.  What the repository shows: (1) docs/DECISIONS_C.md, 3 Oct: 'MedEinst ledger targets from the line diff of the t...
  - note: the first check is right about everything in the quoted fragment. - No target comes from structured evidence, because the release has none. - Every target comes from a line diff, not a token diff. - So there are not two sources whose agreement could be measured. The \ph{96.2}% of \ph{500} pairs has no run and cannot be computed, and the same holds for the \ph{97}-of-\ph{100} author inspection: no result exists or ...
- **line 1545** `(\ph{12} of 49)`
  - results: main.tex lines 1544-1546: "a pair is in the test set only if both of its diagnoses are test diseases (\ph{12} of 49), and in the training set only if both are training diseases." These lines have no \res keys. tables/numbers.json (159 keys) has no key for the disease split. (1) data/clin_v1/medeinst_dis_test/MANIFEST.json and data/clin_v1/clinpairs_medeinst_dis/MANIFEST.json both have split_rule "held-out diseases...
  - note: Only the denominator is wrong. The placeholder 12 matches the measured split (12 held-out diseases, per both MANIFESTs). The pair-membership rule (both diagnoses test means test, both training means training) matches scripts/clinpairs_prep.py. The split was drawn from the 46 diagnoses that occur in the MedEinst release (3 of DDXPlus's 49 labels are absent), not from 49. Writing 49 implies 37 training diseases; the...
- **line 1552** `For training rows, ledgers are sampled once from the frozen`
  - results: paper/latex_v13/main.tex 1552-1555: "For training rows, ledgers are sampled once from the frozen rule-trained reader and kept if their quotations occur in the case and the frozen rule-trained judge returns the keyed verdict on all four cells (\ph{38.5}\% kept)". This sentence has no \res keys, so nothing needed resolving in tables/numbers.json.  Evidence that decoding was greedy: (1) docs/DECISIONS_C.md, 2026-10-0...
  - note: Only one word is wrong: "sampled" should read "decoded greedily" (or "generated once by greedy decoding").  The rest of the procedure in the sentence checks out: - The reader is the frozen rule-trained B-F-ledger2-triplets-s0 (meta.json adapter_run). - The quote check is real: selrm/formats.py:176 well_formed requires every found to be "a verbatim substring of the case". - Keyed verdict on all four cells matches D...
- **line 1555** `(\ph{38.5}\% kept)`
  - results: Context (main.tex lines 1552-1555), Key pairs paragraph: "For training rows, ledgers are sampled once from the frozen rule-trained reader and kept if their quotations occur in the case and the frozen rule-trained judge returns the keyed verdict on all four cells (\ph{38.5}\% kept)". The value is a \ph placeholder. It has no \res key, and nothing in tables/numbers.json (159 keys) covers a clinpairs keep rate.  Meas...
  - note: the first check is right: \ph{38.5} should be 33.9 (122 of 360 pairs, data/clin_v1/clinpairs_medqa/MANIFEST.json kept_share 0.3389; I recomputed it from the raw reader scores).  The rest of the sentence is consistent with the measurements: - The keep filter (verbatim quotes in the case, keyed verdict in all four cells) matches selrm/formats.py well_formed() and scripts/clinpairs_prep.py. - "The kept set is fixed a...
- **line 1559** `\ph{4}\% of pairs.`
  - results: Line 1559 of paper/latex_v13/main.tex, in context (1557-1559): "CareQA covers six subject areas; results by area are in the repository, and the biology and chemistry areas contribute \ph{4}\% of pairs." There is no \res key. tables/numbers.json has 159 keys and none of them mentions careqa, area, biology, chemistry or category. docs/PAPER_NUMBERS.md:249 says this \ph is "a C-CL-keypairs data statistic; no summary ...
  - note: the first check is right. On the 225 one-way CareQA pairs used for every key-pair column, biology and chemistry account for 39.6% of the questions in pairs, 28.4% of pairs where both questions are from these areas, and 50.7% of pairs that contain at least one such question. Every reading is about an order of magnitude above 4%. the first check 39.6% is a share of questions, not of pairs. Whichever unit the authors...
- **line 1653** `Temperature scaling for the combined`
  - results: Context, main.tex 1653-1654: "Temperature scaling for the combined reward is fitted on development data separately for the two scores." The sentence has no \res keys and no \ph values. The \ph{tbd} values just before it belong to the previous sentence, about decision-word leaks.  (1) docs/DECISIONS_D.md row 34 (2026-10-03): "Calibration (D-CAL) is Platt scaling, sigmoid(a s + b) per scorer, fitted on medqa_dev wit...
  - note: the first check point holds. Only the method name is wrong. The rest of the sentence checks out: there is one fit per scorer, made on the dev pool medqa_dev with the 141 key-pair questions left out. the first check fix is enough, e.g. "Platt scaling (slope and intercept per score) for the combined reward is fitted on development data separately for the two scores." Line 599 (Sec. method, "Step check and combined r...

### App. F (diagnostics)

- **line 1714** `Inj.-error PRM`
  - results: Line 1714 is the first row of Table tab:pk (the L0 composition-gap table in App. F): "Inj.-error PRM & \ph{93.5} & \ph{0.0} & \ph{8.1} (\ph{4{,}769}) & \ph{92.8} & \ph{89.5} & \ph{71.4}". It has no \res keys, so there is nothing to look up in tables/numbers.json, and every cell is a typed placeholder. The row label says the study contains an injected-error PRM signal. The repository shows it does not: (1) docs/DEC...
  - note: the first check is right: the row names a model that was never trained or run, so the label states a fact about the models that is no longer true. The six values are placeholders with no planned result, because C-AUD-injerr was dropped. Relabelling the row as "Med-PRM" fixes the name but still leaves it without numbers: no Med-PRM P/K/G/L0 diagnostics exist yet. C-DG-pkg delivered only the backbone row. One more p...
- **line 1714** `(\ph{4{,}769})`
  - results: Context: main.tex line 1714 is the "Inj.-error PRM" row of Table tab:pk. Its caption (lines 1720-1722) reads "L0 (%). Base accuracy; tied preferences; unnecessary reversal among triplets with a correct base preference, with its denominator". The quoted (\ph{4{,}769}) is a placeholder, not a \res key, and it is that denominator. How the denominator is defined: scripts/diagnostics.py (pk) takes L0_UR_n from nm["n_ba...
  - note: I agree with the first check. On the frozen rule_v1/test_L0 (1,000 triplets) the denominator cannot be above 1,000 for any signal, so 4,769 is impossible. The "686" the first check cites belongs to the 9B (\bb{}) row, not this one. That does not weaken the finding, because the 1,000 bound applies to every row. The draft's other denominators (4,090, 4,508, 4,896) cannot occur either. Fixing the number alone is not ...
- **line 1715** `& \ph{80.2} &`
  - results: Context: paper/latex_v13/main.tex l.1715 is the \bb{} row of Table tab:pk (App. F, caption "L0 (%). Base accuracy; tied preferences; ..."). The quoted cell is the Base column: "\bb{}           & \ph{80.2} & \ph{0.0} & \ph{24.6} (\ph{4{,}090}) ...". l.74 has \newcommand{\bb}{Qwen3.5-9B}. The cell has no \res key. It is a typed \ph placeholder and occurs only once in the file. docs/PAPER_NUMBERS.md l.320 identifies ...
  - note: the first check reading is right. The base accuracy of the untrained Qwen3.5-9B on L0 is 68.6, not 80.2 (results_git/C-TF-critic/diagnostics.json pk.L0_BaseAcc, which matches summary_rule_v1~test_L0.json all.BaseAcc, n = 1000). The planned run C-DG-pkg was replaced by C-TF-critic/diagnostics.json (DECISIONS_C l.24; HANDOFFS l.55 and l.78), so a measured value exists for this cell.  Outside the quoted cell, the oth...
- **line 1715** `& \ph{24.6} (`
  - results: Line 1715 of paper/latex_v13/main.tex is the \bb{} row of Table tab:pk. Line 74 defines \newcommand{\bb}{Qwen3.5-9B}. The row reads "\bb{} & \ph{80.2} & \ph{0.0} & \ph{24.6} (\ph{4{,}090}) & \ph{95.3} & \ph{91.2} & \ph{56.8}". The caption defines the column as "unnecessary reversal among triplets with a correct base preference, with its denominator". The row contains only \ph values, so there are no \res keys to r...
  - note: Confirmed: the UR cell for Qwen3.5-9B should read 34.0 (686), not 24.6 (4,090). The \ph row was carried over unchanged from the original draft (paper/latex/main.tex line 1192, then labelled "Qwen3-8B"). It matching the critic's test_hard TA of 24.6 is a coincidence. The other cells on line 1715 also disagree with C-TF-critic/diagnostics.json: - Base: 80.2 in the draft, 68.6 measured (also all/BaseAcc in summary_ru...
- **line 1715** `(\ph{4{,}090})`
  - results: Line 1715 of paper/latex_v13/main.tex is the \bb{} row of Table tab:pk (caption: "L0 (%). ... unnecessary reversal among triplets with a correct base preference, with its denominator"). Line 74 defines \bb as "Qwen3.5-9B". The row is "\bb{} & \ph{80.2} & \ph{0.0} & \ph{24.6} (\ph{4{,}090}) & \ph{95.3} & \ph{91.2} & \ph{56.8}". It has no \res keys, and tables/numbers.json has no key for Table pk; its only C-TF-crit...
  - note: Confirmed. the first check read the evidence correctly. The UR denominator for the Qwen3.5-9B row is 686, not 4,090. That is 68.6% base accuracy on 1,000 L0 triplets, and I reproduced it from per-example scores.  The placeholders in every row of this table (4,769; 4,090; 4,508; 4,896) seem to assume an L0 set of about 5,100 triplets. The real test_L0 has 1,000 triplets, so all four denominators are impossible.  Th...
- **line 1715** `& \ph{95.3} &`
  - results: Context: paper/latex_v13/main.tex line 1715 is the '\bb{}' row of Table tab:pk, captioned "L0 (%). Base accuracy; tied preferences; unnecessary reversal ...; reading and application reversal; composition gap." The full line is "\bb{} & \ph{80.2} & \ph{0.0} & \ph{24.6} (\ph{4{,}090}) & \ph{95.3} & \ph{91.2} & \ph{56.8}". Line 74 defines '\newcommand{\bb}{Qwen3.5-9B}', so '\ph{95.3}' is the P column (reading reversa...
  - note: the first check is right: the P cell '\ph{95.3}' for Qwen3.5-9B in tab:pk is contradicted. The measured reading reversal is 97.7% on 1,000 readapply triplets, from the untrained-backbone run C-TF-critic. I got the same value recomputing it from the raw scores with a read-only script locally ((a local copy) so this is not a misreading.  Most other placeholders in the same row also disagree with the same file: - Bas...
- **line 1715** `& \ph{91.2} &`
  - results: The quoted cell is on line 1715, '\bb{} & \ph{80.2} & \ph{0.0} & \ph{24.6} (\ph{4{,}090}) & \ph{95.3} & \ph{91.2} & \ph{56.8}\\', in Table tab:pk (caption: "L0 (%) ... reading and application reversal; composition gap"). The K column is application reversal, defined at lines 509-513. Line 74 sets '\newcommand{\bb}{Qwen3.5-9B}', so this row is the untrained backbone. The cell is a \ph value and the line has no \res...
  - note: The claim is contradicted. The paper's K cell (application reversal) for the untrained Qwen3.5-9B row reads 91.2, but the measured value is 96.0 on 1,000 L0 readapply triplets. That is 4.8 points off, above the 1-point tolerance. the first check read this correctly.  The other cells on this row, which are not part of the quote, also disagree with the same diagnostics.json: - Base: 80.2 in the paper, 68.6 measured....
- **line 1715** `& \ph{56.8}`
  - results: The quoted cell is on paper/latex_v13/main.tex line 1715: "\bb{}           & \ph{80.2} & \ph{0.0} & \ph{24.6} (\ph{4{,}090}) & \ph{95.3} & \ph{91.2} & \ph{56.8}\\". It is the G (composition gap) column of Table tab:pk, whose header is "Signal & Base & Ties & UR ($n$) & $P$ & $K$ & $G$" and whose caption begins "L0 (%)". Line 74 defines \newcommand{\bb}{Qwen3.5-9B}. The paper (lines 509-514) defines G as 1 - Pr[U |...
  - note: the first check is right. For the untrained Qwen3.5-9B (run C-TF-critic), the measured composition gap is 7.9 (n_P_and_K = 944 of 1,000), not 56.8. It was measured with the paper's own definition on the readapply set, which is registered at level L0, so it is a small gap, not a large one.  The rest of the same row (line 1715) is also contradicted by the same diagnostics.json, though it is outside the quoted cell: ...
- **line 1716** `(\ph{4{,}508})`
  - results: The line is paper/latex_v13/main.tex:1716 in Table tab:pk: "Qwen3.5-27B & \ph{88.4} & \ph{0.0} & \ph{26.0} (\ph{4{,}508})". The caption (lines 1720-1722) reads "L0 (%) ... unnecessary reversal among triplets with a correct base preference, with its denominator". The line has no \res keys, and tables/numbers.json has no pk or L0_UR key for any signal, so 4,508 is a typed placeholder.  The current L0 set has 1,000 t...
  - note: the first check is right: (\ph{4{,}508}) is a count from an earlier, larger L0 set and is impossible on rule_v1/test_L0, which has 1,000 triplets, so any denominator is at most 1,000.  The row's other values (88.4, 0.0, 26.0, 97.6, 95.4, 33.4) are pending, not contradicted. Qwen3.5-27B has not been run on L0: there is no results_git/*27b* directory, and DECISIONS_C (3 Oct) says "the 27B judge needs an 80 GB card o...
- **line 1717** `(\ph{4{,}896})`
  - results: Line 1717 (tab:pk, caption 'L0 (%) ... unnecessary reversal among triplets with a correct base preference, with its denominator') is all \ph: '\ph{12.9} (\ph{4{,}896})'. It has no \res key, so there is nothing to look up in tables/numbers.json. The denominator cannot be larger than 1,000: (1) The L0 set has 1,000 triplets. docs/DATA_AUDIT_rule_v1.md section 8 gives test_L0 groups = 1000, and section 7 also gives G...
  - note: the first check is right: 4,896 cannot occur as a UR denominator on rule_v1/test_L0, which has 1,000 triplets, so for any system the denominator is at most 1,000. The cell is a typed placeholder copied from the v10 draft (paper/latex/main.tex:1194). No closed-judge composition-gap result exists. C-DG-pkg (RUN_MATRIX_C, marked done) has measured only C-TF-critic. docs/PAPER_NUMBERS.md:339 says 'C-DG-pkg has no docu...
- **line 1782** `where the denominator runs over matched pairs of a correct step $s^{+}$ and its injected-error version $s^{-}$ on the same case in the MedPRMBench development split`
  - results: Context, paper/latex_v13/main.tex 1777-1785: Eq. kappa = med{y*delta(x): y*d0<0} / med{u(s+,x)-u(s-,x)}, "where the denominator runs over matched pairs of a correct step $s^{+}$ and its injected-error version $s^{-}$ on the same case in the MedPRMBench development split". The \res keys nearby (run/C-DG-shift/L0/signal=C-AUD-medprm/{crossed,short,unmoved,wrong,kappa@2}) are all number null ('tbd') in tables/numbers...
  - note: the first check is right. The sentence says the denominator comes from MedPRMBench development-split pairs of a step and its injected-error version. No such data exists in the repository, and the code instead uses the correct claim versus the opposite (incorrect) claim on the ordinary rule_v1/missing case. Only the generic shape survives: a correct and an incorrect claim on the same case, in log-odds. Rewording ne...
- **line 1786** `For the injected-error PRM,`
  - results: Line 1786 credits the shift classes and kappa to "the injected-error PRM". The draft defines that model at lines 670-672 as "a PRM trained on the MedPRMBench training split (injected-error PRM)" and lists it apart from Med-PRM \citep{yun2025medprm}. All five \res keys on lines 1786-1788 use signal=C-AUD-medprm, which is the released Med-PRM.  Sources: - scripts/make_tables.py:822-823 maps the label to Med-PRM: DIA...
  - note: Confirmed: the sentence names the wrong model. The project never trained or ran an injected-error PRM, and the keys on this line belong to the released Med-PRM, so "For the injected-error PRM" should say "For the released Med-PRM". The percentages and kappa in the sentence have no results yet (all tbd), so they are pending, not contradicted.  The same wrong label appears in two other places: - The figure's y-tick ...
- **line 1796** `Inj.\ PRM`
  - results: Context: line 1796 is the y-tick list of the left panel of Fig. diagnosis (App. F): "yticklabels={Verdict (blocks),27B judge,9B judge,Inj.\ PRM}". The paper defines the injected-error PRM at line 672 as "a PRM trained on the MedPRMBench training split (injected-error PRM)". The text at line 1786 says "For the injected-error PRM, \res{run/C-DG-shift/L0/signal=C-AUD-medprm/crossed}...", so it uses Med-PRM keys under...
  - note: Confirmed. The tick label claims the fourth row is an injected-error PRM, which the paper defines as one trained on MedPRMBench. No such model exists in the study: C-AUD-injerr was dropped because MedPRMBench is unreleased. make_tables.py fills that row from the released Med-PRM (C-AUD-medprm), so once Med-PRM is merged its numbers will appear under the wrong name. The label should read 'Med-PRM'.  The row's value...
- **line 1816** `symbolic x coords={Inj,8B,32B,Blk}`
  - results: paper/latex_v13/main.tex line 1816 is an axis option of the right panel of Fig. diagnosis: 'symbolic x coords={Inj,8B,32B,Blk}, xtick=data'. No xticklabels are set, so these symbol names are what prints as the tick labels. The line has no \res keys. The nearby keys run/C-DG-shift/L0/signal=C-AUD-medprm/{crossed,short,unmoved,wrong,kappa@2} are all number null in tables/numbers.json ('\ph{tbd}').  1. scripts/make_t...
  - note: I confirmed the first check finding against make_tables.py, the C-DG-shift summary and configs/models.json. The labels 8B and 32B are wrong model sizes for Qwen3.5-9B and Qwen3.5-27B. They also disagree with the left panel's '9B judge' and '27B judge'.  The 8B mislabel is already visible: it sits under the plotted kappa of 0.50, which is the 9B model's value. The 32B label will only print once the 27B kappa exists...
- **line 1835** `API judges without log-probabilities the verdict frequency over \ph{32} samples at temperature \ph{1.0}`
  - results: The quote has no \res keys. Its only values are \ph{32} and \ph{1.0}, which are typed placeholders, not measurements. The sentence describes how API judges without log-probabilities are read out, and the repository fixes a different procedure. (1) configs/models.json, verified 2026-10-03: openai/gpt-6-astra, google/gemini-3.1-pro-preview and the third closed judge of DECISIONS_C all have "readout": "choice" and "l...
  - note: the first check is right. The sentence says API judges without log-probabilities are scored by verdict frequency over 32 samples at T=1.0. The frozen protocol in INTERFACES 3, models.json and DECISIONS_C instead uses the two-order choice prompt with one call per order, the result in {+1, 0, -1}, and reasoning effort low. No closed-judge audit has run yet (no results_git/C-AUD-* directories), but the procedure itse...

### App. G (additional results)

- **line 1934** `Long: longer notes with superseded values (requirements in Table~\ref{tab:hard})`
  - results: Context: line 1934 sits in the caption of tab:ladder, the rule-ladder table. The quoted clause has no \res keys. The \res keys on lines 1936-1937 resolve in tables/numbers.json to readapply TA 71.9, 73.5 and 99.6. They are not part of the claim.  Which set the "Long" column shows: scripts/make_tables.py lines 673-674 define LADDER_SETS ("Long", "hard"). Line 53 maps "hard" to "rule_v1/test_hard", and line 127 reso...
  - note: The caption says the Long column is "longer notes with superseded values". The column is really a mix of tiers. 917 of 1,000 triplets are long notes with no superseded value. 80 are short notes (6-11 lines) that do contain one. 3 are short notes with a delabelled allergy. No triplet is both long and superseded: that combination was only planned for rule_v2, which was never built.  The "longer notes" part is accura...
- **line 2015** `peak GPU memory in the configuration with on-GPU checkpointing was 21.9~GB, which we report for that configuration only.`
  - results: The sentence at main.tex lines 2015-2017 has no \res key. "21.9~GB" was typed by hand, and the Training paragraph it sits in describes the paper's 60,000-record runs.  1) The 21.9 figure matches only results_git/B-C0-val-gpu-ckpt/meta.json: train.peak_mem_gb = 21.87, steps = 40, corpus smoke_v2/train_triplets, len_max 315, provisional = true. Its run.log says "trained 40 steps in 5.4 min ... peak 21.87 GB". This i...
  - note: Contradicted: for the paper's runs with on-GPU checkpointing, the measured peak is 23.1-35.8 GB, not 21.9 GB. The 21.9 comes from a 40-step validation run on smoke_v2, whose sequences are shorter (len_max 315 against 465-575 on rule_v1). A small correction to the first check: the switch arrived in commit 27886a1; 3633b71 is only the first run commit that has it. the first check figures (23.66, 23.17, 35.82) are co...
- **line 2039** `and \ph{1} generated token`
  - results: Context (main.tex 2039-2040): "Per scored claim: verdict only, \ph{1} pass and \ph{1} generated token; \method{}, \ph{2} passes and \res{sum/D-RES/systems.ledger2.generated_tokens_per_claim@0} tokens". The token figure is a \ph placeholder, not a measured value. In tables/numbers.json, the Ledger-RM key sum/D-RES/systems.ledger2.generated_tokens_per_claim@0 = {value "10", number 10.011}.  The measured result disag...
  - note: Only the token count is contradicted. "\ph{1} generated token" should read 0 generated tokens (one forward pass, score read at the answer position). The other half of the clause, "\ph{1} pass", matches D-RES passes_per_claim 1. The 1-point tolerance does not apply here: the gap between 0 and 1 is not rounding. It is a fact about procedure, since the verdict interface generates nothing, and that fact is defined by ...
- **line 2048** `GRPO from one \bb{} initialisation on rule triplets`
  - results: paper/latex_v13/main.tex l.74 defines '\newcommand{\bb}{Qwen3.5-9B}', and no later \renewcommand or \def changes it. So l.2048-2049 prints "GRPO from one Qwen3.5-9B initialisation on rule triplets". Lines 2046-2059 contain no \res keys, only \ph values.  The repository shows the GRPO policy is Qwen3.5-4B: - results_git/D-RL-setup-outcome/meta.json: "policy": "/pvcb/selrm/models/unsloth--Qwen3.5-4B" (seed 0, group_...
  - note: Only the model name is wrong. "On rule triplets" and "one initialisation" are correct. \bb itself is fine: Qwen3.5-9B is the reward-model backbone and the D-POOL policy (ROLE.md l.15), so redefining it would break other parts of the paper. The fix is to replace \bb{} on l.2049 alone with Qwen3.5-4B.  Outside the quote, the \ph values on the same line also differ from the logged runs. DECISIONS_D (3 Oct) gives 1,00...
- **line 2049** `\ph{3} runs`
  - results: main.tex lines 2048-2050 say: "GRPO from one \bb{} initialisation on rule triplets, \ph{3} runs, \ph{8} rollouts per prompt, \ph{2000} steps". There is no \res key in this sentence, and numbers.json has no D-RL key, so "3" is an unmeasured placeholder. The repository fixes the run count at a different value: (1) docs/DECISIONS_D.md, 2026-10-03 GRPO row: "Runs: the five rewards, seed 0, 1,000 steps ... seed 1 if GP...
  - note: the first check read the evidence correctly. "\ph{3} runs" is a stated fact about procedure, and DECISIONS_D 3 Oct contradicts it: one seed-0 run per reward, with seed 1 only if GPUs allow. It is not "placeholder-no-result-planned", because the runs exist and their count is decided.  Reading "3 runs" as a total does not save it either. This paragraph reports results for four rewards (outcome, injected-error PRM, L...
- **line 2050** `\ph{2000} steps`
  - results: The sentence at paper/latex_v13/main.tex line 2050 ("GRPO from one \bb{} initialisation on rule triplets, \ph{3} runs, \ph{8} rollouts per prompt, \ph{2000} steps") describes how the policy-training runs were set up. "2000" is a typed-in \ph placeholder; there is no \res key to look up in tables/numbers.json.  Three sources show 1,000 steps instead: (1) docs/DECISIONS_D.md, row dated 2026-10-03 (GRPO setup check):...
  - note: the first check evidence holds. The value should read 1,000 steps (ROLE.md allowed 1-2k; D chose 1,000 because 2,000 would take about 14 h per reward). This is a stated procedural fact that the repository shows is no longer true, so it counts as a contradiction even though the 2000 is a placeholder rather than a measured result. Outside this claim, nearby placeholders in the same sentence may also be stale: '\ph{3...
- **line 2052** `Accuracy on base--flip pairs of held-out structures, judged by the rule program, moves from \ph{38.6}\%`
  - results: Context: paper/latex_v13/main.tex lines 2046-2059, App. G "Policy training". Line 2052 reads "Accuracy on base--flip pairs of held-out structures, judged by the rule program, moves from \ph{38.6}\% to \ph{52.3}\% with an outcome reward". The line has no \res key, and tables/numbers.json has no D-RL key; grepping it for RL/grpo/policy finds only a15/folds L2-overlap keys. So 38.6 is a typed placeholder that was nev...
  - note: Confirmed. The starting accuracy the sentence states (38.6%) is a \ph placeholder. The measured starting accuracy of the untrained policy, on the same metric and set (150 rule_v1/test_L2 triplets, base and flip both right, judged by the rule program), is 89.3%. The value is recorded in the repo's results_git/D-RL-setup-outcome and repeated in D-RL-stepcheck-s0.  Points outside the checked quote: - The rest of the ...
- **line 2054** `\ph{52.3}\% with an outcome reward`
  - results: paper/latex_v13/main.tex lines 2052-2054: "Accuracy on base--flip pairs of held-out structures, judged by the rule program, moves from \ph{38.6}\% to \ph{52.3}\% with an outcome reward". Both numbers are \ph placeholders, and the sentence has no \res key. tables/numbers.json has no D-RL key at all (0 matches), and docs/RESULTS_SUMMARY.md G1 lists run/D-RL-outcome/L2/top/acc_pair = tbd.  Measured evidence, which I ...
  - note: the first check reading is correct, and a measured result contradicts the 52.3%. The run's final value at step 1,000 is not written yet: the runs are planned for 1,000 steps (DECISIONS_D, STATE_D line 35), and the outcome curve stops at step 800 with no summary file. So the exact final number is still pending.  Still, every measured value of this quantity under the outcome reward is between 97.3 and 98.7, which is...
- **line 2054** `\ph{33.9}\% with the injected-error PRM`
  - results: Context, main.tex lines 2052-2055: "Accuracy on base--flip pairs of held-out structures, judged by the rule program, moves from \ph{38.6}\% to \ph{52.3}\% with an outcome reward, \ph{33.9}\% with the injected-error PRM and \ph{63.5}\% with \method{}." The clause uses only \ph values and no \res keys. tables/numbers.json has no D-RL key at all. docs/RESULTS_SUMMARY.md G1 still lists run/D-RL-stepcheck/L2/top/acc_pa...
  - note: Confirmed on two counts: 1. The value: the measured final pair accuracy for this reward is 37.3, not 33.9, so it is off by more than 1 point. 2. The procedure: the reward is the released Med-PRM (dmis-lab/llama-3.1-medprm-reward-v1.0), not an injected-error PRM. No injected-error PRM exists because MedPRMBench has no release.  Only the direction holds: accuracy ends below the start, which is consistent with reward...
- **line 2057** `gives \ph{58.0}\%`
  - results: Context (paper/latex_v13/main.tex 2052-2058): "Accuracy on base--flip pairs of held-out structures, judged by the rule program, moves from \ph{38.6}\% to ..." and then "A reference-graph reward after \citet{medceg2025} ... gives \ph{58.0}\%". The passage has no \res keys, only \ph values. tables/numbers.json has no D-RL key, and docs/RESULTS_SUMMARY.md (G1) lists run/D-RL-refgraph/L2/top/acc_pair = tbd.  Measured ...
  - note: The contradiction is real but rests on interim checkpoints (steps 200 and 400 of 1,000); the end-of-training value is still pending. To end at 58.0, the policy would have to drop about 40 points, to well below its untrained 89.3%. Nothing in the curve points that way: half of the refgraph reward is the outcome term, and train_outcome is 0.97-0.99. The \ph{58.0} was never measured and has no registered key.  The re...

## 2. Partly contradicted (50)


### Abstract and introduction

- **line 255** `(d) Controlled tests (blue) and external labels (grey).`
  - results: The caption's colour key is right for five of the six boxes in panel (d). The one it gets wrong is the "registered eligibility criteria" box (main.tex line 246, fill=black!6), which the key calls "external labels".  Blue boxes (lines 243-245), which are program-labelled controlled tests: - held-out structures - rule-side edits and altered rules - independently written cases  Grey boxes at lines 247-248 that do hol...
  - note: the first check is right in substance about the one box. The caption sentence is not wrong in itself; what is wrong is the grey fill on "registered eligibility criteria" at line 246. With that fill, the legend calls a program-labelled triplet set an external-label source, against the repository and against the draft's own Table 1 caption. Fix: change line 246 to fill=blue!4 (or move the box into the blue group). T...

### Rule triplets, external tiers, diagnostics, method

- **line 347** `In \ph{23}\% of criteria a past or family finding counts, so no global heuristic about time or subject is correct.`
  - results: paper/latex_v13/main.tex lines 343-348 read: "In \ph{23}\% of criteria a past or family finding counts, so no global heuristic about time or subject is correct." The value is a bare placeholder. No \res key exists for it: a search of tables/numbers.json for past/family finds nothing.  Measured values are in tables/data_stats.json, library_semantics, from commit 412a4d2 with code_modified_since_commit false: - crit...
  - note: Only the number is contradicted. The inference clause holds. The \ph{23} should be replaced by a measured share: - 30.5% of all 791 criteria, if "criteria" is kept as the denominator; - 52.5% of the 459 finding criteria, if the sentence is reworded to refer to finding criteria (the reading PAPER_VS_CODE 3.1-5 recommends).  There is no \res key for this statistic, so the value has to come from tables/data_stats.jso...
- **line 350** `a criterion uses the mentions its predicate counts: the most recent current value of a measurement`
  - results: Context: paper/latex_v13/main.tex lines 348-351 say: "When a concept is mentioned more than once, a criterion uses the mentions its predicate counts: the most recent current value of a measurement, any counted mention of a finding with status present." The sentence has no \res or \ph keys, so the evidence is the code and the role-A audit.  What is contradicted: the recency rule. In selrm/rules.py lines 61-63, Crit...
  - note: Only the words "most recent" are contradicted, and they are wrong about the procedure, not about the labels. The program counts exactly one current value and has no recency rule. With two current values it raises an error instead of choosing one. No label is affected, because every case has one current value and every older value is past (dated 2005-2024 or marked superseded), so the counted value is always the ne...
- **line 352** `the reference date and window boundaries are fixed per rule and stated in its text`
  - results: Sentence (paper/latex_v13/main.tex 351-353, no \res keys): "Units, threshold inclusivity, the reference date and window boundaries are fixed per rule and stated in its text". The paragraph describes rule_v1, whose state model records time only as current or past (line 343).  What is contradicted: (1) Reference date. rule_v1 has none. - tables/data_stats.json semantics.all_test_and_dev: cases 47600, cases_stating_a...
  - note: Only part of the sentence is contradicted.  Contradicted: - The reference-date clause. rule_v1 has no reference date in any case or rule text. In xr_v1 and ec_v1 the visit date is given in each case, and the rule text only names it as the anchor ("before the visit date"). - The window-boundary clause, for rule_v1. The one rule text that names a window (s3_jhfrat) states no boundary, and its program does not run th...
- **line 363** `A \emph{flip} (decisive edit) changes a mention that $A_j$ counts so that $c_j$ changes`
  - results: There are no \res keys in lines 358-368 of main.tex, so nothing needed resolving. I read three sources for this check.  (1) tables/data_stats.json, semantics.all_test_and_dev: finding_bases = 5156, finding_bases_no_line = 1584, finding_bases_generic_absence_line = 3572. For test_L2 alone: 932 / 286 / 646. scripts/audit_rule_v1.py:559 counts no_line as 'not tg', meaning the base state has no mention of the target c...
  - note: the first check evidence is accurate, but only part of the sentence is contradicted. The wrong part is the verb "changes a mention that A_j counts": in 30.7% of finding triplets in test and dev (1,584 of 5,156; 286 of 932 in test_L2) the base has no line about the concept, so the flip adds a counted mention instead. The clause "so that c_j changes" holds, as do the rest of the sentence's invariants, all numeric fl...
- **line 371** `the concept and value of the flip are reported in a mention that $A_j$ does not count: another subject, absent status, or a time outside $A_j$`
  - results: Context (main.tex 366-376) has no \res or \ph keys, so nothing needs resolving in tables/numbers.json. What I read myself: (1) selrm/rules.py lines 47-54: Criterion.applies (A_j) checks only the concept, the subject (the patient, or a first-degree relative if counts_family) and the time (past only if counts_past). It never reads status. evaluate (line 60) then requires 'any(m.status == "present" for m in app)' amo...
  - note: Only the "absent status" item is contradicted. Line 372-373 lists absent status as one way a mention falls outside A_j, but in the code A_j does count the patient's current denial. The negation near-miss leaves the criterion unchanged only because evaluate needs a counted mention with status present. The other two items hold: the subject near-miss uses a person A_j excludes, and the time near-miss is a past mentio...
- **line 373** `A \emph{presentation} edit re-renders the same state with another unit, order or template, matched in size to the flips`
  - results: Lines 361-387 of main.tex are the "Edits and invariants" paragraph. The sentence has no \res keys, so there was nothing to look up in numbers.json. At lines 264-266 the paper explains the same citation as "meaning-preserving edits of the same size; our near-miss and presentation edits are such baselines", so "matched in size" means the size of the edit.  (1) UNIT is contradicted. - selrm/engine.py lines 329-349: a...
  - note: Only two parts of the sentence are contradicted.  1. "another unit": no unit ever changes. Every measured input has one unit, and the code has no conversion. 2. "matched in size to the flips": a flip changes one line. A presentation edit always replaces the header, reorders the lines (median 7, minimum 3 lines differ by line diff) and rewords measured values, so it is much larger than a flip.  "Re-renders the same...
- **line 472** `Only the first two contain controlled edits; the others are external labels.`
  - results: There are no \res keys in lines 467-477. NLI4CT keys in tables/numbers.json are all null ('tbd'), but the sentence is about how the data were built, not about a measured value.  The first clause ("Only the first two contain controlled edits") is contradicted. data/clin_v1/nli4ct_test/MANIFEST.json, "by_intervention", gives Original 500, Paraphrase 1500, Contradiction 1500, Text_appended 1500, Numerical_contradicti...
  - note: Partly. The claim that only the first two sources contain controlled edits is wrong for NLI4CT-P: the repository data and the table's own row say its test set is controlled interventions. MedEinst traps are also edits of control cases, made by the benchmark. The second clause, "the others are external labels", is correct, and the claim is right for TrialGPT and key pairs.  The fix is wording only, along the lines ...
- **line 479** `\emph{Registered criteria} are unambiguous registered clinical-trial eligibility criteria quoted as written`
  - results: Context, main.tex lines 479-482: "\emph{Registered criteria} are unambiguous registered clinical-trial eligibility criteria quoted as written, with programs checked by an author; a selected subset, from which nothing follows about trial eligibility in general." These lines have no \res keys. The ec_v1 keys in tables/numbers.json (run/B-F-{ledger2,verdict}-triplets/ec_v1:test/all/TA) have number null and print \ph{...
  - note: the first check is right about "quoted as written": the texts are not verbatim. Of the 35/95 edited rows, 18 only trim punctuation, escapes or list words. The other 17 change content: unit restatements, added units, removed equivalents, and added boundary-day clauses. "Unambiguous" is overstated for 20 criteria: 16 do not settle whether a past occurrence counts, and in 4 the boundary day had to be written into the...
- **line 527** `of up to \ph{3} entries.`
  - results: Context (main.tex 522-539, Method section): the reader takes "the criterion, or the set of candidate answers", and the claims "are judged from one ledger $e=R_\phi(x,\rho,\omega)$ of up to \ph{3} entries." The sentence has no \res key. tables/numbers.json has no key about ledger entries. docs/PAPER_NUMBERS.md (row 527) lists \ph{3} under "Placeholders that no planned run produces" and notes "selrm/formats.py sets ...
  - note: Only part holds. The bound is true for what the sentence names, rule-tier triplets: every gold ledger and every ledger from the headline reader in seeds 0-4 has 1-2 entries, and 2 is within "up to 3". So the first check numbers show 3 is not the real maximum, not that it is exceeded. The part that is contradicted is "up to 3" as a property of the ledger format and the reader R_phi, which is how a Method sentence r...
- **line 532** `Keys and categorical fields are fixed by a grammar`
  - results: Context, paper/latex_v13/main.tex lines 527-537: the reader's ledger has the fields need, found, subject, status (present, absent, unknown) and time (current or past), followed by "Keys and categorical fields are fixed by a grammar, and a quotation that does not occur in the case makes the ledger malformed." There are no \res keys in this window. The only macro is \ph{3} on line 527 ("up to 3 entries"), which is n...
  - note: Partly contradicted.  Holds: the clause "a quotation that does not occur in the case makes the ledger malformed" is exactly what the code does. "Keys ... are fixed" also holds, but the keys are enforced by a check after generation, not by a decoding grammar.  Contradicted: "categorical fields are fixed by a grammar". Neither generation nor the check restricts the values of subject, status or time: - Prompted reade...
- **line 555** `(log-odds are unbounded, so no finite floor is used)`
  - results: Sentence (main.tex 553-555, no \res or \ph keys, so nothing to look up in numbers.json): "A malformed ledger is an explicit invalid outcome: both claims are rejected and the pair is a tie, which counts as a failure (log-odds are unbounded, so no finite floor is used)."  The code gives a malformed ledger a finite score: - docs/INTERFACES.md lines 45-46 set the frozen rule: a malformed ledger gets "u = -20 for both ...
  - note: Only the parenthesis is contradicted, specifically "no finite floor is used". The repository uses a finite floor of u = -20 everywhere (INTERFACES 3, formats.py MALFORMED_U). - In selection the floor counts: it goes into the minimum over steps and into the Platt fit, on about 43-45% of dev traces (D-CAL). - On rule-tier pairs it has no effect on d, because both claims share the ledger.  "Log-odds are unbounded" is...
- **line 575** `with $|e^\ast|$ the number of target tokens, and one judge example per claim; $\lambda$ is their ratio in the corpus.`
  - results: Context: paper/latex_v13/main.tex lines 566-576 give the objective with -(1/|e*|) log p(e*) for the reader and λ times the judge log-likelihood. Line 576 says "λ is their ratio in the corpus", and App. line 2012 says λ=\ph{1.0}. The quote has no \res keys.  1) Training code. scripts/finetune.py:252 uses the stock 'Trainer(... data_collator=Collate(...))'. Collate (lines 87-102) sets labels to -100 on the prompt an...
  - note: Two parts are contradicted: (a) the per-example 1/|e*| normalisation, and (b) "λ is their ratio in the corpus". The implemented loss averages over all response tokens in the batch. That makes the effective λ about 1/34 of the 1:1 example ratio, so judge targets carry about 6% of the loss.  What still holds: separate supervised examples in one corpus, one reader unit per (case, condition) shared by both claims, and...
- **line 586** `A missing or misattributed entry cannot be repaired by the judge.`
  - results: Line 586-587 ("A missing or misattributed entry cannot be repaired by the judge.") contains no \res key. The related key run/B-AE-field-edit/L2/top/agreement is null in tables/numbers.json, so it prints \ph{tbd}. The raw result does exist.  1) Contradicts the "misattributed" half. Source: results_git/B-AE-field-edit/summary_rule_v1~test_L2~edit.json. - Edits that change the verdict (changed=1): agreement 47.84, n=...
  - note: The contradiction holds only for the "misattributed" part, and only in its absolute form ("cannot"). In the B-AE-field-edit runs, a subject, status or time field was edited so that it contradicts the entry's own verbatim quotation. The judge often ignored the edit and returned the verdict the quotation supports, which is the correct one for the case.  The rest is consistent with the sentence: - When the whole ledg...
- **line 597** `Errors internal to a step are scored by a separate adapter, the injected-error PRM, which sees the case.`
  - results: Sentence (paper/latex_v13/main.tex 597-598, under "Step check and combined reward"): "Errors internal to a step are scored by a separate adapter, the injected-error PRM, which sees the case." It has no \res keys, so nothing to look up in tables/numbers.json.  Evidence that the step scorer is not an injected-error PRM and not an adapter: - configs/adapters.json systems.stepcheck: path "hf://dmis-lab/llama-3.1-medpr...
  - note: Contradicted part: the identity of the scorer, "a separate adapter, the injected-error PRM". No injected-error PRM was trained, because MedPRMBench has no release (re-checked 3 Oct). The step-error run was dropped (DECISIONS_B row 80). Every measured step-check result comes from the released Med-PRM, a whole Llama-3.1-8B-Instruct-based model, not an adapter. That covers the Table 5 "Step check" row (86.2 / 89.0 / ...

### Experimental setup; audit of reward signals

- **line 626** `new rule identities and constants within seen signatures (L1)`
  - results: Context (paper/latex_v13/main.tex 625-630): "The test levels separate four kinds of novelty: new generated cases of trained rules (L0); new rule identities and constants within seen signatures (L1); held-out signature classes". There are no \res keys on lines 626-627.  What holds: (1) New rule identities. tables/data_stats.json overlap."rule_v1/test_L1" has rules 27 and rule_text_pct 0.0. DOCS/DATA_AUDIT_rule_v1.m...
  - note: the first check read the evidence correctly, but only one part of the phrase fails. "New rule identities ... within seen signatures" holds. "New ... constants" is false for 37% of L1 rules (10 of 27): their program, thresholds and cutoff included, is a training rule's program. Also, 89.5% of L1 criteria, with their thresholds, appear in training.  structure_pct 77.8 does not contradict "within seen signatures". Th...
- **line 630** `In all test sets the rendering templates and cue phrases for relatives, negation and time do not occur in training`
  - results: The sentence at main.tex 630-632 has no \res or \ph keys. I checked tables/data_stats.json "overlap" for every set.  Parts that hold: - Templates: templates_shared = 0 in every set (L2 0 of 358, L0 0 of 373, L3alt 0 of 74, and the rest). - Relatives: cases_with_train_relative_pct = 0.0 in every set. On the training side, cases_with_test_relative_pct = 0.0. - Evidence lines: flip_lines_with_train_cue_pct and near_l...
  - note: Partly contradicted. The claims about templates and relatives hold. The claim about negation and time cue phrases holds only for the evidence lines (flip and near-miss) and the cue lists. It does not hold for the full case text. Test-split generic-absence lines use the training negation cue "no" and current-time cue "today". This affects 3.8% of L2 cases and 13.0% of L3-alt cases, and every test set has some (4.5-...
- **line 694** `We train \ph{5} seeds`
  - results: Context: main.tex 694-695 (in "External data and protocol") reads "We train \ph{5} seeds; values printed in black in this draft are from seed 0." The 5 is a placeholder. No numbers.json key holds a seed count.  The 5-seed claim holds for the core cells: - tables/seeds.tex has s0-s4 for B-F-verdict-blocks (58.2/53.5/60.0/47.6/49.0, mean 53.7), verdict-triplets (mean 91.8), ledger2-blocks (mean 71.0), ledger2-triple...
  - note: I confirmed the first check evidence. The sentence is right for the six core cells. Five of them have seeds 0-4 measured, and summary2 x blocks has seeds 0-3, with seed 4 claimed but no results yet. The sentence is wrong for every other trained configuration: the non-core factorial cells, ablations, LOKO, transfer and B-SC rows. Each of these has only seed 0, and at most seeds 0-2 are planned for the non-core fact...
- **line 742** `\ph{GPT-5.4} & \ph{tbd}`
  - results: Line 742 is the closed-judge row of the generated Table 2. It is identical to tables/audit.tex line 15. There are two parts to judge.  (1) Row label \ph{GPT-5.4]: contradicted. configs/models.json (verified 2026-10-03) lists the only OpenAI closed judge as "id": "openai/gpt-6-astra", with table "Closed judge (current OpenAI flagship)" and revision "openai/gpt-6-astra-20260903". docs/DECISIONS_C.md has a 2026-10-03...
  - note: Only the model name in the row label is contradicted. The six value cells print 'tbd' because the closed-judge run C-AUD-closed-1 has not happened yet, so nothing measured disagrees with them.  The label is a placeholder fallback. scripts/make_tables.py line 544 hard-codes ("C-AUD-closed-1", "GPT-5.4"). The function label() (lines 513-518) prints "the verified model ID from the run's meta.json, else the draft's pl...

### Training distribution and representation

- **line 805** `(seed 0); intervals over rules: verdict`
  - results: Context: main.tex 804-805, the Table 3 caption: "Values in black are measured (seed 0); intervals over rules: verdict \res{...}". The table body just above it (lines 792-797, the same as tables/factorial.tex) prints six cells with \sd, so it contradicts the caption on the same page: 53.7\sd{5.4}, 91.8\sd{0.4}, 64.9\sd{6.2}, 98.5\sd{0.7}, 71.0\sd{10.7} and 99.2\sd{0.3}.  Seed values. tables/seeds.tex and the raw re...
  - note: Only the "(seed 0)" part of the caption is contradicted. It is wrong for six of the 20 cells: verdict, summary2 and ledger2, each on blocks and triplets. These print means over seeds 0-4 (seeds 0-3 for summary2 x blocks). Three of them differ from their seed-0 value by more than 1 point: 53.7 vs 58.2, 71.0 vs 75.3 and 64.9 vs 67.3. The other three differ by at most 0.5.  What holds: - "Values in black are measured...

### What the judge uses

- **line 1001** `\caption{Not yet measured; curves show the layout only. Left: L2 triplet`
  - results: Line 1001 opens the Fig. 3 caption: "\caption{Not yet measured; curves show the layout only. Left: L2 triplet". The caption has no \res keys (only \ph{16}), so it covers both panels.  RIGHT PANEL: measured, so the caption is contradicted here. - In main.tex lines 990-998, the right axis now holds the generated body "% generated by scripts/make_tables.py (fig-seln); do not edit". Its coordinates are combined (\meth...
  - note: The contradiction covers only the right panel. The opening "Not yet measured; curves show the layout only" is wrong for Fig. 3 right, which is measured (D-SELN, 150 MedQA key pairs, N = 1..64) and plotted from generated data. It is still true for Fig. 3 left: the B-DIV runs are only claimed, their keys are null, and the panel shows a red tbd. The new left panel has no curves at all, so "layout only" no longer desc...

### Candidate selection, conclusion, limitations

- **line 1109** `the ledger score depends on the supplied case.`
  - results: Context (main.tex 1107-1110): "Swapping in the vignette of another question removes the gain of the combined reward and leaves the step check almost unchanged: the ledger score depends on the supplied case." The quoted clause has no \res keys. The swap rows come from tables/downstream.tex. numbers.json has no key for a ledger-only swap, and no D-SEL-ledger-swap run exists: scripts/select_eval.py defines only stepc...
  - note: the first check is right that the sentence's stated basis fails, but wrong that the quoted clause is false.  Contradicted: the premise on line 1108, "removes the gain of the combined reward". The combined reward has no gain to remove (combined minus step check -0.9, p 0.126), and the swap does not lower it (combined minus swapped -0.3 [-2.2, 1.6], p 0.822). So the colon's inference that the swap shows case depende...
- **line 1174** `Rules come from our implementations of published scores, constraints compiled from public recommendations and a grammar;`
  - results: Context: main.tex 1174-1176 is the "Rule population" limitation. The sentence has no \res keys. The group it refers to is defined in Sec. 4, lines 613-617, which use these keys from tables/numbers.json: a15/rules_total@int = 353; a15/rules_by_kind.score@int = 43; d/a15/rules_total|a15/rules_by_kind.score|a15/rules_by_source.grammar_sampled@int = 60 (constraint rules "compiled from public recommendations"); a15/rul...
  - note: Only the clause "constraints compiled from public recommendations" is contradicted, and only for 6 of the 60 hand-written constraint rules (6 of the 353 library rules). The score clause, the grammar clause and "No clinician reviewed the rules" hold.  Caveat: the 5 grammar_curated rules have their text composed by G() in rules_grammar.py, so a reader could count them under "a grammar". But the paper counts them amo...

### App. A-C (analysis plan, rule library, triplet construction)

- **line 1213** `Every value printed in red is a placeholder: a number is a target value used to lay out an experiment that has not been run`
  - results: Context (main.tex 1210-1217) is the red "Draft status" note in the appendix. Its first clause holds by construction. The preamble defines \ph{x} as \textcolor{red}{x}, and \res{KEY} with no value prints \ph{tbd}, so every red value is a \ph placeholder.  The second clause says each red number is "a target value used to lay out an experiment that has not been run". That is now false for several red numbers whose qu...
  - note: The verdict is partly. The convention "red = placeholder" is still accurate. The explanation "target value ... experiment that has not been run" is contradicted for red numbers whose measurement now exists. Three of them differ from the measured value: 7.9 -> 0, 18.6 -> 0 and 38.6 -> 89.3. Others agree with the measurement but are still red: 40/20/20/20, 3 folds, 5 classes, 6/4/2 templates, 0% shared templates and...
- **line 1225** `rules as clusters`
  - results: Context, main.tex lines 1224-1228: "Primary comparisons (paired on identical items, triplets kept together, rules as clusters, Holm-corrected): on L2, (1)...(3); on MedEinst, (4)...(5). Added before any external result was seen: (6) on the TrialGPT annotations". There are no \res keys within 5 lines of line 1225.  What holds: for (1)-(3) the clusters really are rules. scripts/make_tables.py comparisons() calls sel...
  - note: the first check is right in substance, but only part of the sentence is wrong. Rules are the clusters for the L2 comparisons (1)-(3). For TrialGPT (6a/6b), the measured comparisons use patients (43 clusters, 759 items). For MedEinst (4)/(5), DECISIONS_C fixes pairs and (y_gt, y_bias) label pairs as clusters, with the label-pair interval used for inference. (4)/(5) are still pending, so for them the conflict is wit...
- **line 1243** `(4)--(6) are not run.`
  - results: The sentence is paper/latex_v13/main.tex line 1243: "(4)--(6) are not run." It sits in the "Status at seed 0." paragraph (lines 1241-1243). Line 1243 has no \res key. The key on line 1242, d/run/B-F-ledger2-triplets/L2/all/TA/s0|run/B-F-summary2-triplets/L2/all/TA/s0, is 1.2 in tables/numbers.json and is not at issue here.  What is wrong: (6), the TrialGPT comparison, has been run. - results_git/C-TG-comparisons_t...
  - note: Only the (6) part of the sentence is contradicted. the first check numbers are correct. (6) was run on the TrialGPT test portion (43 patients, 759 items) and is not supported: - 6a: Ledger-RM on triplets minus the untrained backbone is +3.4, and its CI [-2.6, 9.2] includes 0. - 6b: triplets minus blocks is -1.8 [-4.8, 1.1], the wrong direction, with a CI that also includes 0.  Holm-adjusted p values are still \ph{...
- **line 1273** `development splits only: development triplets from training-fold signature classes and a held-out part of the MedEinst reference set.`
  - results: Context, main.tex 1271-1275: "Hyperparameters, thresholds, the calibration of the combined reward and the choice of headline system use development splits only: development triplets from training-fold signature classes and a held-out part of the MedEinst reference set." The line has no \res keys to resolve.  Contradicted part: the calibration of the combined reward was fitted on neither listed split. - results_git...
  - note: Only the list of splits after the colon is contradicted, and only for the combined-reward calibration. That calibration (Platt scaling plus the logistic combination, D-CAL) was fitted on the MedQA dev pool: the first 500 validation questions minus the 141 key-pair questions, leaving 359 questions and 5,578 traces. Neither listed split was used. The "development splits only" claim and the description of the dev tri...
- **line 1274** `Test sets are generated or opened after these choices are frozen and are evaluated once.`
  - results: Line 1274-1275 (App. A, "Selection and freezing") has no \res keys: "Test sets are generated or opened after these choices are frozen and are evaluated once."  Evidence that "evaluated once" is not true: (1) B's own test scoring: results_git/B-F-ledger2-triplets-s0/summary_rule_v1~test_L2.json, all.TA = 99.2 (Rev 99.25, Hold 99.95, n 2000). (2) A second scoring of the same adapter on the same test set: results/D-V...
  - note: the first check read the evidence correctly. Only the clause "are evaluated once" is contradicted: - rule_v1/test_L2 was scored twice with B-F-ledger2-triplets-s0 (B's run, TA 99.2; D's vLLM reproduction D-VAL, TA 99.05). - The second scoring's result decided which scoring path answer selection uses. - DECISIONS_D row 33 plans a third test_L2 scoring for B-TR-tripclin-s0.  The other two claims are not contradicted...
- **line 1291** `Constraint rules from public recommendations & 60 & --`
  - results: main.tex:1291 is a generated row of tab:rules: "Constraint rules from public recommendations & 60 & --". The count is CONSISTENT: the cell key d/a15/rules_total|a15/rules_by_kind.score|a15/rules_by_source.grammar_sampled@int = 60 in tables/numbers.json (353-43-250), and tables/data_stats.json rules.hand_written_by_kind.constraint = 60. The provenance label is CONTRADICTED for 6 of the 60: data_stats.json rules.han...
  - note: Partly contradicted: the number 60 is right; the row label 'from public recommendations' is false for the 6 synthetic hand-written constraint rules (54/60 hold). the first check second point (53 of 103 hand-written rules contradict their source, sources_with_contradictions = 53) concerns how faithfully the rules follow their sources. It does not contradict 'from public recommendations' for the 54 simplified_source...
- **line 1315** `rendering audit by the authors (below)`
  - results: Line 1315 (Table "validity", row "Does the text express the intended state?") reads "rendering audit by the authors (below); extraction check on rewrites". It has no \res keys, and tables/numbers.json has no H1 or rendering key. "(below)" points to the paragraph "Rendering audit." at lines 1338-1348, which has two parts:  (1) "Before the freeze, 450 rendered groups were reviewed for label errors \ph{[state who rev...
  - note: Contradicted part: the cell credits the authors with the rendering audit described below. The audit that was actually done, the 450 pre-freeze groups, was read by a reviewer that is not a person and no person ("People: 0"). The paragraph still has a \ph placeholder for who did that review, so this table cell is the only place the draft names a reviewer, and the name is wrong.  Not contradicted: the authors' own re...
- **line 1355** `We keep a rule if the tree is complete, the program passes the boundary tests and agrees with the tree on sampled inputs, and show the verbalised tree in the prompt.`
  - results: The sentence is at paper/latex_v13/main.tex lines 1355-1357 and has no \res keys. It sets four conditions, and three of them are contradicted.  Contradicted: "the tree is complete", "agrees with the tree on sampled inputs" and "show the verbalised tree in the prompt". (1) docs/PAPER_VS_CODE.md, item B-4 (lines 402-405), which audits this same v13 text: "The MedGuideX extract–tree–compile pipeline. *Does not match....
  - note: I rate this partly, not confirmed, because the boundary-test clause holds. the first check own evidence says so too. Three parts are contradicted by docs/PAPER_VS_CODE.md B-4, docs/HANDOFFS.md line 35 and the code: the tree-completeness check, the agreement check against a tree on sampled inputs, and showing a verbalised tree in the prompt. No tree exists and the prompt shows the rule text. The boundary tests only...
- **line 1392** `L0 the generated cases only`
  - results: The sentence is at paper/latex_v13/main.tex line 1392: "The levels change different things: L0 the generated cases only; L1 rule identities and constants; L2 logical compositions; all test sets the wording." It has no \res keys. The only nearby key is on line 1391: a15/folds.1.n_classes@int = 21 (tables/numbers.json).  What holds: - At L0 nothing on the rule side changes. tables/data_stats.json overlap/rule_v1/tes...
  - note: Only part of the sentence is contradicted. The word "only" holds: L0 shares every program, structure, subexpression and rule text with training. The clause "all test sets the wording" also holds (0 of 373 templates shared).  What fails is the claim that L0 changes the generated cases. For 480 of 862 distinct L0 base states (55.7%), the same rule and state already occur in training. For those, only the wording diff...
- **line 1392** `L1 rule identities and constants`
  - results: Context, paper/latex_v13/main.tex lines 1392-1393: "The levels change different things: L0 the generated cases only; L1 rule identities and constants; L2 logical compositions; all test sets the wording." These lines have no \res keys. The neighbouring key a15/folds.1.n_classes@int is 21, and numbers.json has overlap keys for L2 only. Line 627 says the same thing: "new rule identities and constants within seen sign...
  - note: Partly contradicted.  What holds: the "rule identities" part. Every L1 rule is new: 0% of rule texts and 0 of 629 base states are shared with training.  What is contradicted: the "constants" part, which is stated for all of L1. For 10 of 27 L1 rules (37%), training contains a rule with the identical program: same concepts, operators, thresholds, points, logic and cutoff. For those rules L1 changes only the setting...
- **line 1399** `the words that mark relatives, negation and time are split in the same way`
  - results: Context (main.tex 1397-1400): "each input type has \ph{6} templates, \ph{4} for training and \ph{2} for test, and the words that mark relatives, negation and time are split in the same way." The sentence has no \res keys, and 6/4/2 are \ph placeholders. I read the evidence myself: (1) tables/data_stats.json "lexicons": negation_cues train 3 / test 6 / shared 0; time_cues 8/8/0; current_cues 3/5/0; persons 12/6/0. ...
  - note: Only "negation and time ... split in the same way" is contradicted, and only if "in the same way" means the templates' 4:2 per-6 index split. If it just means held-out training and test lists, it holds, because all lexicons share 0 words. the first check goes too far by including relatives: PERSONS is split exactly like the templates (12/6). the first check rewording ("split into disjoint training and test lists",...
- **line 1402** `L3-alt moves one or two thresholds`
  - results: main.tex l.1402-1403: "L3-alt moves one or two thresholds and keeps only cases whose outcome differs between the original and the altered rule". tables/data_stats.json l3alt: groups 1000, rules 17, criteria 18, threshold_moved {higher 575, lower 425}, thresholds_moved_per_group {"1": 1000}, flips_between_thresholds_pct 100.0. The same figures appear in docs/DATA_AUDIT_rule_v1.md sec. 6, rows "Thresholds moved per ...
  - note: Only "or two" is contradicted. No L3-alt group moves two thresholds, and the generator cannot produce one. "Moves one threshold" holds for all 1,000 groups. The rest of the sentence also holds: only cases whose outcome differs between the original and altered rule are kept (flip lies between the two thresholds in 100% of groups). "Its near-miss kinds are \ph{tbd}" is a placeholder that is not covered by this check...
- **line 1464** `Rule-dependent time scope & the same past event counts under ''ever'', not under ''within six months'' & \ph{tbd}`
  - results: Context: main.tex lines 1454-1455 say "Table~\ref{tab:hard} lists the requirements and how many test triplets have each." The row at line 1464 has no \res key, and its n is \ph{tbd}.  (1) The requirement exists and has counts. In tables/data_stats.json, "requirements" → rule_dependent_time_scope is: test_L2 54, test_hard 25, test_L0 40, test_L1 20, test_L3inv 33, dev 8, and absent (0) in test_L3alt. tables/numbers...
  - note: Two parts of the row hold. The requirement exists in the test triplets, and the "same past event counts under 'ever'" half is right: some other library rule counts the finding in the past. The n cell is \ph{tbd}. Counts exist in tables/data_stats.json (test_L2 54, test_hard 25) but are not bound in numbers.json, so that cell is pending.  The contradicted part is the "not under 'within six months'" half. Every targ...
- **line 1465** `Competing mentions & a relative has the finding; the patient explicitly does not & \ph{tbd}`
  - results: Context: main.tex l.1454-1455 says the table "lists the requirements and how many test triplets have each". Row l.1465 has no \res key, and its n cell is \ph{tbd}.  The example is contradicted: - results/A-AUDIT/summary.json, identical to tables/data_stats.json: semantics.all_test_and_dev.finding_inputs_two_or_more_mentions = 0 of finding_inputs = 56,740 (47,600 test and dev cases). For test_L2 it is 0 of 12,548. ...
  - note: The contradicted part is the Example column. The case "a relative has the finding; the patient explicitly does not" is never generated: 0 of 56,740 finding inputs have two mentions, and every case keeps one mention per finding, by design (DECISIONS_A).  The row label "Competing mentions" is not contradicted on its own. Under the rule_v1 definition it has measured counts: test_L2 268 and test_hard 138. But those ar...
- **line 1478** `Each item has three cases (the contested form, an uncontested positive, an absent finding)`
  - results: Line 1478-1479 has no \res keys. The preceding sentence lists four clause dimensions, including "boundary inclusivity". (1) Generator: selrm/xr.py line 327, used for every inclusivity item, sets vals = {"contested": thr, "positive": round(thr + sign * 2 * nd, dec), "negative": round(thr - sign * 2 * nd, dec)}. So the third case is a current numeric value on the other side of the threshold, not an absent finding. F...
  - note: Only part of the sentence is wrong. Every one of the 400 items does have three cases: a contested form, an uncontested positive (for inclusivity items, a value 2*near_delta on the counting side), and a negative. Each item is solved only if all six judgments are right (crossed_accuracy in xr.py checks len == 6). The wrong part is "an absent finding". That holds for the 300 window, currency and subject items, but no...

### App. D-E (external tiers, ledger format)

- **line 1498** `MedPRMBench and CareQA at pinned revisions listed in the repository.`
  - results: Line 1498 (inside \paragraph{Releases.}, App. External Tiers, lines 1496-1498) contains no \res keys, so there is nothing to look up in tables/numbers.json. The sentence says two datasets are used at pinned revisions.  (1) MedPRMBench: contradicted. - configs/datasets_c.json, lines 92-98: "id": "arXiv:2604.17282 (no HF / GitHub / ModelScope data or model repo exists)", "use": "status check", "exists": false. Its o...
  - note: Only the MedPRMBench part is contradicted. MedPRMBench released no data or model (verified 2 and 3 Oct), so no revision can be pinned, and none of our runs uses its data. The only entry for it in the repository is a status check with exists=false, and that entry's "revision" is arXiv v1 of the paper. The CareQA part holds: it is pinned at revision 1d976cc in configs/datasets_c.json and configs/datasets_d.json, and...
- **line 1543** `Other ledger fields are not`
  - results: paper/latex_v13/main.tex 1539-1544, the MedEinst training-row paragraph, has no \res keys. It says found holds the differing findings, then: "Other ledger fields are not supervised there."  1. docs/DECISIONS_B.md, row 2026-10-03 (clinical pairs). Its rule-applied column cites this same v13 sentence. The row says the reader targets keep C's literal 'unknown' for subject, status and time, "so no field value is train...
  - note: What holds: no value taken from the case is a training target for subject, status or time on MedEinst rows. They are placeholders, the data flags them as unsupervised, and B logged this sentence as the rule it applied. So the first check read the evidence correctly, but no case-derived field value has changed.  What is contradicted: the sentence describes the training procedure as 'not supervised'. In fact these f...
- **line 1549** `Pairs are mined within a split and reduced to a one-to-one matching, so that`
  - results: The sentence (main.tex lines 1549-1550, appendix paragraph "Key pairs.") reads in full: "Pairs are mined within a split and reduced to a one-to-one matching, so that no question occurs in two pairs." It has no \res or \ph keys.  Contradicted clause, "mined within a split": - docs/DECISIONS_D.md, 3 Oct key-pair row: "every key-pair column (Tables 2, 4/App. key pairs, 5; Fig. 3 right) uses C's one-directional sets c...
  - note: Partly confirmed. the first check numbers are right, but they contradict only the "mined within a split" clause, and only for the MedQA evaluation key pairs. The lead's decision row explicitly asks for this paragraph to be rewritten to say test + validation. The one-to-one matching clause and "no question occurs in two pairs" are consistent (714 distinct questions in 357 pairs). The MedQA-train and CareQA sets rea...
- **line 1550** `Excluded: negatively phrased lead-ins,`
  - results: Context (main.tex lines 1548-1559, "Key pairs" paragraph, which also covers CareQA): "Excluded: negatively phrased lead-ins, options that refer to other options, and questions without a case description." These lines have no \res keys, only \ph values. DECISIONS_D.md (line 30, 3 Oct) says every key-pair column uses the one-way sets keypairs_medqa_oneway (357 pairs) and keypairs_careqa_oneway (225 pairs). STATE_D.m...
  - note: Only the last clause is contradicted, and only for CareQA. The quoted part holds: negatively phrased lead-ins are excluded in both sets (MedQA 13, CareQA 914), and so are options that refer to other options (3 and 30). Questions without a case description are excluded for MedQA (131) but kept for CareQA, so 'questions without a case description' is wrong for the 225 CareQA pairs. The list also leaves out the short...
- **line 1563** `condition, each with the answer given the condition and the general answer`
  - results: Context: D:/NAACL27/selrm-role-d/paper/latex_v13/main.tex lines 1561-1571 (App. CondMedQA paragraph). Lines 1562-1565 say: "CondMedQA \citep{parekh2026cgr} has 100 questions that contain a patient condition, each with the answer given the condition and the general answer that would hold without it". The paragraph has no \res keys (0 matches). Its numbers are all \ph: 41.0, 56.0, [46, 66] and 80.0. tables/numbers.j...
  - note: Only the clause "and the general answer that would hold without it" is contradicted, and only as a statement about the data that can be used. The cited paper did make a general answer for each question while building the benchmark, so the clause correctly describes how the benchmark was built. But the release has only the condition-appropriate answer (DECISIONS_C 3 Oct; live CSV columns id, wiki1, wiki2, q, a). Th...
- **line 1582** `The data are under credentialed access and may not be sent to external`
  - results: The context is lines 1573-1583 of paper/latex_v13/main.tex. It has no \res keys. The sentence before it gives the critic, rule-only and clinical-pairs results as \ph{58.0}, \ph{69.5} and \ph{77.0}. tables/numbers.json has no EHRNote key, and there is no C-CL-ehrnote directory in results/ or results_git/.  Evidence that contradicts the sentence: (1) configs/datasets_c.json (verified 2026-10-03), EHRNote-ChatQA entr...
  - note: Two parts of the sentence are contradicted.  1. "The data are under credentialed access" is wrong as a statement about the present. The data are not published. Credentialed access through PhysioNet is only planned, and the licence or data use agreement is not visible yet.  2. The sentence gives the access rule as the reason closed judges are excluded. Together with the sentence before it, this implies the open sys...

### App. F (diagnostics)

- **line 1682** `Bag of words, case + claim`
  - results: Line 1682 (table rows 1679-1686, Table shortcuts): "Bag of words, case + claim & 13.2 & 61.7 & 7.0\\". The row has no \res key because the table body is generated. The label is hard-coded in scripts/make_tables.py line 703: ("Bag of words, case + claim", "A-D14-bag_of_words").  The numbers hold. results/A-D14-bag_of_words/summary_rule_v1__test_L2.json, field "all", gives TA 7.05, Rev 13.25 and Hold 61.7, with CI95...
  - note: Only "+ claim" in the row label is contradicted. The scorer is a bag of words over the case text alone, and the claim selects only p or 1-p. "Bag of words, case" and the three printed values (Rev 13.2, Hold 61.7, TA 7.0 vs 13.25 / 61.7 / 7.05 in the result file) are consistent.  It is a minor procedural mislabel, and no number changes. The fix belongs in the generator, not main.tex: relabel in scripts/make_tables....
- **line 1756** `other person, past finding`
  - results: paper/latex_v13/main.tex lines 1755-1757 are the caption of Table tab:kinds. It glosses the five columns (thr., neg., num., subj., time) as follows: "Triplet accuracy on L2 by near-miss kind (\%, seed 0): value at the threshold, negated finding, value near the threshold, other person, past finding." The caption has no \res keys. The table body comes from tables/kinds.tex, where n = 400 for each kind (run/B-F-ledge...
  - note: Only the "past finding" gloss of the time column is wrong. It fits 132 of the 400 L2 time triplets (33%). The other 268 (67%) are older measured values: 201 dated past values and 67 superseded values. The paper's own Appendix C Semantics separates measurements from findings ("for a measurement ... for a finding ..."), and Section 3.1 defines this kind as "a time outside A_j". The "other person" gloss for the subj....
- **line 1837** `Scoring Qwen3.5-27B by the same sampling protocol lowers its triplet accuracy from \res{run/C-AUD-qwen35-27b/L2/all/TA}\% to \ph{42.0}\%, with \ph{4.1}\% ties.`
  - results: Line context (main.tex 1833-1839, the "Readouts and sampling noise" paragraph): the previous sentence sets out the sampled readout as \ph{32} samples at temperature \ph{1.0}. Our sentence then gives the 27B result.  (1) The \res key is pending. In tables/numbers.json, "run/C-AUD-qwen35-27b/L2/all/TA" has number null and value "\ph{tbd}". In docs/RUN_MATRIX_C.csv, C-AUD-qwen35-27b is "blocked, no 80 GB card free; A...
  - note: Every number and file the first check cited matches what I read. I label this 'partly' rather than 'confirmed' only because part of the sentence holds.  **Contradicted:** - **Model.** The sentence says Qwen3.5-27B. The only sampling check, C-DG-noise, ran on Qwen3.5-9B (the untrained model before training). No 27B sampling run exists or is registered. - **Placeholder values.** At the stated setting (32 samples, te...

### App. G (additional results)

- **line 1985** `Triplet accuracy on L2 (\%) for every seed of every trained configuration in the tables; -- marks a seed that was not run.`
  - results: Caption (main.tex 1985): "Triplet accuracy on L2 (\%) for every seed of every trained configuration in the tables; -- marks a seed that was not run."  Clause 1, coverage: contradicted. tab:ablation (main.tex 1886-1888) has three rows from separately trained runs: "$-$ other-person near-misses & 93.8 & 67.5 & 62.5", "$-$ past near-misses ... 86.2" and "$-$ threshold near-misses ... 87.0". They come from scripts/mak...
  - note: the first check contradiction holds for the coverage clause. Three trained, finished seed-0 LOKO ledger2 configurations are shown in tab:ablation but have no row in tab:seeds. The "--" legend, and the mean/s.d. and pooled-interval wording, are correct.  Two other row groups, for context: - The B-AE-* rows in tab:ablation are not separately trained. Their meta.json has eval_only true and reuses the adapters B-F-led...
- **line 2051** `Before each run we check that reward terms are not collinear within groups`
  - results: Sentence (main.tex 2051-2052): "Before each run we check that reward terms are not collinear within groups and that the setup fits a \ph{64}-prompt subset." It has no \res keys, and none of the 159 keys in tables/numbers.json is an RL, setup or collinearity key.  (1) Only one setup check exists, run once before all runs. - docs/DECISIONS_D.md line 35 (2026-10-03): "GRPO setup check (ROLE.md: a 64-prompt subset mus...
  - note: Contradicted: - "Before each run". The fit check was run once, with the outcome reward only, before all runs. - The pre-run check that reward terms are not collinear. No such check runs before a run. The reward's correlation with the rule program's outcome is only logged during each run. The one pre-run log shows 1.0, collinear by construction because that reward is the outcome itself.  Consistent: the setup does ...
- **line 2056** `which scores a rollout by its coverage of the decisive findings and of the chain from finding to criterion to conclusion`
  - results: Context, main.tex lines 2055-2059: "A reference-graph reward after \citet{medceg2025}, which scores a rollout by its coverage of the decisive findings and of the chain from finding to criterion to conclusion, gives \ph{58.0}\%". The sentence has no \res keys. tables/numbers.json has no RL-refgraph key, and docs/RESULTS_SUMMARY.md G1 lists run/D-RL-refgraph/L2/top/acc_pair = tbd.  The reward is defined in D:/NAACL2...
  - note: Part contradicted: "and of the chain from finding to criterion to conclusion". No reward term scores the chain or the criterion step. The second half of the reward (0.5) is final-answer correctness only.  Parts that hold: "coverage of the decisive findings" roughly matches the 0.5 term. It is binary and needs only any one decisive mention at 60% word overlap, so "coverage" overstates it. "Uses the answer for each ...

## 3. Placeholders with no run or result planned (34)


### Experimental setup; audit of reward signals

- **line 761** `a classifier that sees only the step reaches a macro-F1 of \ph{81.7} on the MedPRMBench test split, against \ph{41.2} for the majority class`
  - evidence: DECISIONS_C 3 Oct 'Not run: ... MedPRMBench input ablation (no released data)'; configs/datasets_c.json arXiv:2604.17282 'no HF / GitHub / ModelScope data or model repo exists'. There is no key in tables/numbers.json or docs/RESULT_KEYS.md and no row in RUN_MATRIX
  - note: Remove the clause. The rule-triplet claim-only scorer (A-D14-claim_only) can carry the point instead.

### Training distribution and representation

- **line 852** `the ledger is right and the prose record wrong on`
  - evidence: The value is \ph{tbd} on line 853 and has no key: cmp keys expose only diff/lo/hi/p/padj/n. PAPER_NUMBERS line 208 lists it under 'Placeholders that no planned run produces'. docs/ANALYSIS_B.md section 1 has seed-0 counts only: ledger-only 38 (negation 11, subject 26, time 1). No pooled-seed counts exist.
  - note: Either reword to seed 0 and use 38, or extend comparisons() to the 5-seed pairs.
- **line 853** `and the reverse on \ph{tbd}`
  - evidence: No key (PAPER_NUMBERS line 209). The seed-0 summary-only count is 14 (negation 6, subject 8) in ANALYSIS_B section 1. No pooled-seed count exists.

### Transfer within and beyond rules

- **line 879** `& 3.6 & \ph{tbd} & \ph{tbd} & 24.7`
  - evidence: The TrialGPT cell reads run/C-TG-defcorr/clin_v1:trialgpt_test (tables/PROVENANCE.json). No C-TG-defcorr exists in results_git, docs/RUN_MATRIX_C.csv or configs/tasks_c/*.json. The C-TF-defcorr row of RUN_MATRIX_C lists only C-ME-defcorr for clinical data.
  - note: Queue C-TG-defcorr or print '--'. The Criteria cell is covered by the Criteria-column finding.
- **line 888** `& 49.4 & \ph{tbd} & \ph{tbd} & 51.6 & \ph{tbd}`
  - evidence: B-F-ledger2-balanced-s0 scored only dev, test_L2 and xr_v1. docs/FINAL_TASKS_B.md P1: 'Non-core runs are evaluated on dev, L2 and the new sets only'. DECISIONS_B (3 Oct) keeps L3alt and missing only for core cells and B-TR rows.
  - note: The L3-alt and MR cells of this row are not planned; print '--'. Its XA exists (54.5, s0, xr.conclusion.XA) but is not wired. Its TrialGPT and MedEinst cells are planned by C (STATE_C Next 6), so those are pending.
- **line 892** `\method{}, rule triplets + step-error data & \ph{tbd}`
  - evidence: docs/DECISIONS_B.md (3 Oct, B-DIS row): 'B-TR-steperr dropped: MedPRMBench has no public data'. docs/HANDOFFS.md (C, 3 Oct): MedPRMBench 'no public data or model release'. docs/STATE_B.md: 'B-TR-steperr dropped'. No results_git/B-TR-steperr-*.
  - note: Remove the row or mark it not run.
- **line 898** `Extraction + hand-written program & \ph{tbd} & \ph{tbd} & \ph{tbd}`
  - evidence: docs/DECISIONS_C.md (3 Oct): C-REF-extract-program has 'no xr_v1: the freeze has no xr_v1 programs'.
  - note: This refers to the XA cell (third numeric column); print '--' there.
- **line 961** `in \ph{81}\% of its near-miss errors a relative's or a past finding is passed to the code as the patient's`
  - evidence: docs/PAPER_NUMBERS.md (line-961 entry): this needs an error analysis of B-TR-genprm's check code, and 'No task or summary field plans it'. No such analysis appears in docs/RUN_MATRIX*.csv or docs/FINAL_TASKS_B.md.
  - note: The preceding claim ('Executed code settles how a rule is applied and not how the case is read') rests on this number. Plan the analysis or drop both.

### App. A-C (analysis plan, rule library, triplet construction)

- **line 1331** `\ph{tbd} of \ph{tbd} were corrected or dropped`
  - evidence: No author pass done or scheduled (HUMAN_TASKS.md H1-H8 have none for rule_v1; PAPER_NUMBERS.md line 178 'No run or summary field records it'). a reviewer that is not a person check found 53 of 103 hand-written rules contradicting their source in at least one respect; they were kept as test specifications, not corrected or dropped (DATA_AUDIT sec. 1).
- **line 1401** `With training templates and cues on the same L2 rules, triplet accuracy of \method{} is \ph{tbd}`
  - evidence: No registered set renders L2 rules with training templates (data/REGISTRY.json) and no run in RUN_MATRIX_A-D or FINAL_TASKS evaluates it (PAPER_NUMBERS.md line 231).
- **line 1445** `results on that subset are \ph{tbd}`
  - evidence: The subset is empty by construction; no slice selects it (slices are nm_kind, tier, family, level, step; PAPER_NUMBERS.md line 236).

### App. D-E (external tiers, ledger format)

- **line 1542** `\ph{96.2}\% of a sample of \ph{500} pairs`
  - evidence: Traps have no structured evidence (DECISIONS_C 3 Oct), so agreement between two target sources cannot be computed. No run or field exists (docs/PAPER_NUMBERS.md: 'RESULT_KEYS.md defines no summary field for it'). Searched results_git and docs.
  - note: Drop this clause together with the structured-evidence wording.
- **line 1542** `in \ph{97} of \ph{100} pairs`
  - evidence: HUMAN_TASKS.md H1-H8 include no inspection of MedEinst pairs, and no file in audit/ or docs records one.
  - note: Schedule an author check of 100 pairs or remove the clause.
- **line 1567** `\ph{41.0}\% for the critic,`
  - evidence: DECISIONS_C 3 Oct: 'Not run: CondMedQA (... general answers ... are not released ...)'. HANDOFFS 3 Oct (C): 'App. CondMedQA paragraph: mark not run or remove'. No CondMedQA run exists in results_git.
  - note: Remove the paragraph or mark it not run.
- **line 1568** `\ph{56.0}\% for rule-only \method{} [\ph{46}, \ph{66}]`
  - evidence: CondMedQA was not run (DECISIONS_C 3 Oct), so there is no run or key for the value or its interval.
  - note: -
- **line 1568** `\ph{80.0}\% for the`
  - evidence: CondMedQA was not run (DECISIONS_C 3 Oct). Closed-judge reference runs are also blocked on the API key (RUN_MATRIX_C C-REF-closed-zero).
  - note: -
- **line 1580** `preferred to such a distractor in \ph{58.0}\% of cases by the critic, in`
  - evidence: configs/datasets_c.json, EHRNote-ChatQA: exists false; 'Data: not yet published, planned PhysioNet credentialed access'. DECISIONS_C 3 Oct: 'Not run: ... EHRNote-ChatQA (data not on PhysioNet ...)'.
  - note: Remove the paragraph or mark it not run.
- **line 1581** `\ph{69.5}\% by rule-only \method{}`
  - evidence: The EHRNote-ChatQA data are unreleased and the dataset was not run (configs/datasets_c.json; DECISIONS_C 3 Oct).
  - note: -
- **line 1581** `\ph{77.0}\% with clinical pairs.`
  - evidence: The EHRNote-ChatQA data are unreleased and the dataset was not run (DECISIONS_C 3 Oct). The clinical-pairs adapters (B-TR-clinonly, B-TR-tripclin) have not run either.
  - note: -
- **line 1610** `\method{}, rule triplets + step-error data & \ph{tbd} & \ph{tbd} & \ph{tbd}\\`
  - evidence: docs/RUN_MATRIX_B.csv, B-TR-steperr-s0..s2: 'dropped, 3 Oct: MedPRMBench has no public data release ... not run'. STATE_B.md: 'B-TR-steperr dropped'.
  - note: No step-error data exist, so remove this row.
- **line 1657** `\ph{41}\% of wrong entries`
  - evidence: The results_git/B-AB-verify-s0 summaries record totals only: test_L2 has 9,071 entries, 69 rejected, 70 regenerated, 14 replaced; dev 1,325 / 16; xr_v1 2,525 / 0. The scores files keep no per-entry verdict, so no split by entry correctness exists or is planned (docs/PAPER_NUMBERS.md).
  - note: -
- **line 1657** `\ph{3.2}\% of correct ones.`
  - evidence: B-AB-verify-s0 records no split by entry correctness. Overall rejection on test_L2 is 69 of 9,071 entries (0.76%); on dev it is 16 of 1,325 (1.2%).
  - note: If this means generated entries, it is implausible: rejecting 3.2% of correct entries with only 69 rejections in total would require at least 76% of entries to be wrong, while this adapter's L2 TA is 99.8.
- **line 1660** `ledgers are identical in \ph{98.7}\% of cases.`
  - evidence: The D-SEL-* summaries hold only acc, pair_acc, control_acc, trap_acc and n (results_git/D-SEL-ledger). score_pool.py meta counts unique reader units only. docs/PAPER_NUMBERS.md: no field.
  - note: For context, 42.5% (triplets) and 44.7% (blocks) of dev-pool traces contain a malformed step (results_git/D-CAL/summary.json, share_traces_with_malformed_step).
- **line 1660** `On L2 the reader is right on \ph{96.9}\%`
  - evidence: Neither docs/ANALYSIS_B.md nor any summary reports per-field reader accuracy (docs/PAPER_NUMBERS.md: 'No planned run or documented field'). The closest result is ANALYSIS_B section 4 (B-F-ledger2-triplets-s0, test_L2): 15,343 entries matched to case mentions, 29 unmatched; the program applied to the predicted ledger reaches TA 99.4.
  - note: Field accuracies near 94-97% would be hard to reconcile with TA 99.4 for the program on predicted ledgers.
- **line 1660** `\ph{95.4}\%`
  - evidence: There is no per-field (subject) reader accuracy in any run or doc (docs/PAPER_NUMBERS.md).
  - note: -
- **line 1660** `\ph{94.1}\% of`
  - evidence: There is no per-field (time) reader accuracy in any run or doc (docs/PAPER_NUMBERS.md).
  - note: -
- **line 1661** `In \ph{2.1}\% of`
  - evidence: No run or field measures quotes that occur in the case but are not the decisive finding (docs/PAPER_NUMBERS.md: 'No planned run or field'). ANALYSIS_B section 4 counts only matched vs unmatched entries (15,343 / 29).
  - note: -

### App. F (diagnostics)

- **line 1714** `& \ph{93.5} & \ph{0.0} & \ph{8.1} (\ph{4{,}769})  & \ph{92.8} & \ph{89.5} & \ph{71.4}`
  - evidence: C-AUD-injerr dropped (RUN_MATRIX_C). Composition-gap output exists only in results_git/C-TF-critic/diagnostics.json (C-DG-pkg marked done with that run). The Med-PRM substitute's tasks (configs/tasks_c/c_prm.json, C-AUD-medprm--p1..p3) score dev, test_L2, dev_missing, missing, xr_v1 and clinical sets but not test_L0 or readapply. make_tables has no tab:pk keys
  - note: Searched results_git, results, numbers.json, RUN_MATRIX_C, c_prm.json, DECISIONS_C.
- **line 1842** `Replacing the question stem by ''No case description is available'' lowers PRMScore on MedPRMBench by \ph{1.2}--\ph{2.9} points for trained PRMs.`
  - evidence: docs/RUN_MATRIX_C.csv C-DG-inputabl 'dropped, MedPRMBench data not released'; DECISIONS_C:25 'Not run: ... MedPRMBench input ablation (no released data)'; no key in numbers.json
  - note: Remove the paragraph or mark it not run.
- **line 1846** `On the error types that the benchmark defines relative to the case the loss is \ph{4.0}--\ph{9.5} points`
  - evidence: C-DG-inputabl dropped (RUN_MATRIX_C); DECISIONS_C:25
- **line 1847** `\ph{6.2}--\ph{13.0} when numbers and quoted spans of the stem are also masked in the chain.`
  - evidence: C-DG-inputabl dropped (RUN_MATRIX_C); DECISIONS_C:25

### App. G (additional results)

- **line 1870** `\ \ + decision field & 99.7 & 99.8 & 99.5 & \ph{tbd}`
  - evidence: The MR cells of the rows at lines 1870-1876, 1879, 1881-1882 and 1886-1891 are \ph{tbd}. Their runs (B-AB-*, B-AE-pred-bit-program, B-AE-oracle-ledger, B-F-value2-triplets-s0, B-SC-summary2-triplets-s0, B-LOKO-*-ledger2-s0) list only dev and test_L2 (+ xr_v1, test_L0) in meta.json eval_sets, with no rule_v1/missing or dev_missing. FINAL_TASKS_B P1: 'Non-core runs are evaluated on dev, L2 and the new sets only.'
  - note: Most of these adapters are still on B's PVC (configs/adapters.json), so MR could be added with an extra evaluation. None is queued.
- **line 2066** `With a paraphrased vignette the combined reward gives \ph{78.0}\% on MedQA.`
  - evidence: No paraphrased-vignette run, code or key exists in results_git, scripts, RUN_MATRIX_D or FINAL_TASKS_D. The planned control swaps in another question's vignette: D-SEL-combined-swap gives 85.6 on MedQA.
  - note: docs/PAPER_NUMBERS.md also says no run is planned. Drop the sentence or replace it with the swapped-vignette result.
- **line 2071** `On the open-ended version of CareQA, graded against reference answers by a fixed model grader, the share graded correct moves from \ph{48.2}\% to \ph{51.0}\%`
  - evidence: No D-OPEN results, script or key exist. RUN_MATRIX_D lists D-OPEN as todo P3 (API grader), but neither FINAL_TASKS_D P1 (the plan of record) nor docs/STATE_D.md includes it.
  - note: The sentence also does not name which two selectors are compared.

## 4. Waiting for a result (159)


### Abstract and introduction

- **line 96** `run/C-AUD-closed-3/L2/all/TA@0}\% of triplets are solved: trained medical PRMs seldom`
  - evidence: tables/numbers.json: the min and max keys over the 13 C-AUD runs have number null (tbd). There is no C-AUD-* directory in results_git/ or results/. RESULTS_SUMMARY A1: 'not run'. The only audited signal measured so far sits under another id: C-TF-critic (backbone) L2 TA 27.15 (results_git/C-TF-critic/summary_rule_v1~test_L2.json). HANDOFFS C 3 Oct asks make_tables to read C-TF-critic for C-AUD-qwen35-9b.
  - note: The range does not exist yet. The key includes C-AUD-injerr, which will never run, and C-AUD-qwen35-9b, which is not yet mapped to C-TF-critic.
- **line 96** `trained medical PRMs seldom reverse, and general judges reverse on near-misses`
  - evidence: RESULTS_SUMMARY A1: 'not run'. tables/audit.tex: every cell is tbd, and no PRM run (C-AUD-medprm/meds3/fover/thinkprm/genprm) has results. Only one general judge is measured, the untrained Qwen3.5-9B critic (C-TF-critic, L2): Rev 38.55, Hold 32.2, BaseAcc 39.55, TA 27.15.
  - note: No PRM result exists. The one general judge measured fails on base cases about as often as on near-misses (BaseAcc 39.6 vs Hold 32.2), so its errors are not specifically reversals on near-misses.
- **line 104** `raises agreement with MedEinst pair labels from \res{run/C-TF-critic/clin_v1:medeinst_test/top/Reversal@0}\% to \res{run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal@0}\%`
  - evidence: tables/numbers.json: run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal@0 is null. docs/MEDEINST_RESULTS.md has only C-ME-critic, 24.2 [23.0, 25.4] (label-pair CI [14.4, 35.6]), and C-ME-defcorr. tables/primary.tex (4): tbd. RESULTS_SUMMARY P4: 'not run'.
  - note: The baseline, 24% (C-ME-critic, 24.19), is measured and correct. The trained value and the comparison do not exist yet. DECISIONS_C: the label-pair CI is the one to use for inference.
- **line 185** `and policy training (Appendix~\ref{app:more}) the third`
  - evidence: RESULTS_SUMMARY G1: 'not run'; all D-RL keys are tbd. the interim GRPO files (now results_git/D-RL-*): untrained start pair 89.3 / triplet 84.7. The step-check run finished 1,000 steps (reward 0.9997, pair 37.3). The outcome run is at step 800 (pair 97.3) and the refgraph run at step 400 (pair 98.0), both still running. The ledger-reward runs have not started.
  - note: The policy-training experiment is incomplete. The ledger-reward arm does not exist yet.
- **line 187** `we make no claim about preventing reward exploitation beyond what the policy-training experiment measures`
  - evidence: the interim GRPO files (now results_git/D-RL-*)/D-RL-stepcheck-s0.curve.jsonl: reward rises to 0.9997 while held-out pair accuracy falls 89.3 -> 37.3. STATUS_BOARD D-P1: 'step-check reward exploited'. Ledger-reward runs have not started.
  - note: Exploitation by the step-check reward is measured. Whether the ledger reward prevents it is not measured yet.
- **line 192** `run/C-AUD-closed-2/L2/all/TA|run/C-AUD-closed-3/L2/all/TA}\% of triplets are solved`
  - evidence: tables/numbers.json: the min and max keys over the 13 C-AUD runs are null. No C-AUD-* results exist. RESULTS_SUMMARY A1: 'not run'.
  - note: Same keys as the abstract. They include C-AUD-injerr, which will never have a value.
- **line 205** `raises agreement with MedEinst labels from \res{run/C-TF-critic/clin_v1:medeinst_test/top/Reversal}\% to \res{run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal}\%`
  - evidence: tables/numbers.json: the trained key is null. MEDEINST_RESULTS.md: C-ME-critic 24.2 [23.0, 25.4] is the only relevant value. tables/primary.tex (4): tbd. RESULTS_SUMMARY P4: 'not run'.
  - note: The baseline of 24.2 matches. The trained result does not exist yet.
- **line 245** `independently written cases`
  - evidence: STATUS_BOARD A-P0.3/H2: challenge_v1 exists only as a kit and is frozen after the authors' notes. A-P0.6: rewrite_v1 is blocked on the API key. numbers.json: the challenge_v1 and rewrite_v1 keys are tbd.
  - note: There is no set or result yet.
- **line 246** `registered eligibility criteria`
  - evidence: HANDOFFS A 3 Oct: ec_v1 is not frozen and not to be scored (95 criteria, 85 trials, 235 groups awaiting the two-author sign-off H3). numbers.json: the ec_v1 keys are tbd.
  - note: Not frozen or scored yet.
- **line 248** `MedEinst, key pairs, NLI4CT-P`
  - evidence: MEDEINST_RESULTS.md has only critic and defcorr results; the trained two-stage runs were re-queued (DECISIONS_C, runner operations). results_git has no C-KP-* or C-NL-* runs. numbers.json: the NLI4CT keys are tbd. DECISIONS_D: the key pairs are the one-directional sets (357 MedQA, 225 CareQA).
  - note: Trained-system results do not exist yet for any of the three.

### Rule triplets, external tiers, diagnostics, method

- **line 395** `\emph{Author-written cases} are written from a state specification without access to generated text.`
  - evidence: challenge_v1 is a kit only: 160 state specifications in form_author1-4.md (DECISIONS_A row 31). There are no notes files in challenge_v1/. docs/STATUS_BOARD.md H2 reads 'kit ready'; the set is frozen only after H2
  - note: The design matches; no accepted cases or results exist yet.
- **line 396** `\emph{Rewritten cases} are model rewrites kept only when two extractors recover the state; rejected rewrites are an audit set and are not scored`
  - evidence: DECISIONS_A rows 28, 33: rewriter google/gemma-4-31b-it; extractors deepseek/deepseek-v4-pro and openai/gpt-oss-120b; a group is accepted only if both recover the full state; rejects go to data/rewrite_v1/rejected.jsonl and are never scored. docs/STATE_A.md and STATUS_BOARD A-P0.6: blocked on OPENROUTER_API_KEY. No results/A-D11
  - note: The design matches; the tier has not been built.
- **line 432** `so sampled readouts are reported with tie rates and intervals.`
  - evidence: The sampled two-order-choice readouts (closed judges, DECISIONS_C row 20) have no results: tables/audit.tex is all tbd, and Table 2 has no tie column. Only results_git/C-DG-noise/noise_check.json reports a sampled readout (untrained backbone, 32 draws x 10 seeds: TA 24.8 with s.d. 0.4; ties 5.15%)
- **line 443** `and gives base accuracy, ties and denominators per near-miss kind.`
  - evidence: Denominators are given (n = 400 per kind, tables/kinds.tex). Per-kind BaseAcc and Tie exist only in run summaries (e.g. results_git/B-F-ledger2-triplets-s0/summary_rule_v1~test_L2.json: BaseAcc 99.0-100.0, Tie 0.0 per kind). No generated table shows them: tab:kinds lacks them, and the tab:pk Base and Ties cells are \ph and given per signal on L0
- **line 465** `Registered criteria & program of a registered trial eligibility criterion, checked by an author`
  - evidence: ec_v1 is not frozen and is not to be scored (HANDOFFS rows 46, 59, 60). docs/ec_signoff holds only TEMPLATE.csv. The freeze requires two author reviews per criterion and rejects on any 'no' (DECISIONS_A rows 37-39). docs/EC_SIGNOFF.csv verification so far: 90 'confirmed by both model verifiers', 5 rescued
  - note: If signed off as designed, the text should say 'checked by two authors'.
- **line 480** `with programs checked by an author`
  - evidence: The programs were formalised by an LLM workflow (one formalizer, two skeptics; DECISIONS_A row 35). Author sign-off H3 is not done: docs/ec_signoff has only TEMPLATE.csv (STATUS_BOARD H3). The freeze needs two reviewers per criterion (DECISIONS_A rows 37-39)
- **line 502** `edits expert-written statements about trial reports; we report its faithfulness and consistency with base F1.`
  - evidence: clin_v1/nli4ct_test is registered (5,500 records). C-NL-* runs are queued (docs/STATE_C.md), but none is in results_git. Every NLI4CT key in tables/numbers.json (faithfulness, consistency, macroF1) has number null (tbd)
- **line 512** `the composition gap is $G=1-\Pr[U\mid P\wedge K]$`
  - evidence: No G result exists in results_git or tables/numbers.json, and the appendix table tab:pk (P, K, G columns) is all \ph. scripts/diagnostics.py pk exists (DECISIONS_C row 24). Only readapply TA exists: verdict x blocks 71.9, ledger2 x blocks 73.5, verdict x triplets 99.6
- **line 552** `paraphrase controls test this`
  - evidence: No paraphrase-control run in docs/RUN_MATRIX*.csv, results_git or numbers.json. docs/PAPER_NUMBERS.md line 272 notes that no paraphrase run is planned (for the vignette control)
  - note: No such run exists or is planned.
- **line 604** `and reliability gating \citep{evpv2026}`
  - evidence: scripts/select_eval.py has no gating selector, and docs/RUN_MATRIX_D.csv has no gating row. The only gate in the plans is B-AE-premise-gate (Table 9, rule tier, status todo in RUN_MATRIX_B)
  - note: No selection run is planned.

### Experimental setup; audit of reward signals

- **line 633** `Rule-side items, author-written cases, rewritten cases and registered criteria (\S\ref{sec:twins}) are separate, separately frozen sets.`
  - evidence: xr_v1 was frozen on 2 Oct (docs/TIMELINE.md; HANDOFFS A 2 Oct). challenge_v1 is an author kit waiting for H2 (DECISIONS_A P0.3 and review rows). rewrite_v1 has not run and waits for OPENROUTER_API_KEY (DECISIONS_A P0.6; PAPER_VS_CODE 3.1-24). ec_v1 is not frozen and waits for two-author sign-off: 95 criteria, 85 trials, 235 groups (DECISIONS_A third review; HANDOFFS A 3 Oct)
  - note: Only xr_v1 exists as a frozen set.
- **line 651** `Appendix~\ref{app:more} gives, per configuration, unique cases, claims, reader and judge targets, tokens, optimiser steps and runtime.`
  - evidence: tables/ has no generated budget table. docs/ANALYSIS_B.md s7 lists, per finished run, corpus records, examples, reader and judge targets, tokens, completion tokens, steps (938) and train/eval hours, but not unique cases or claims
  - note: Most of the data exists; the table and two of its columns do not.
- **line 684** `\emph{References}: the best closed judge with the prompted ledger`
  - evidence: No C-AUD-closed-* or C-REF-closed-* run in results_git or results; RUN_MATRIX C-REF-closed-ledger is todo; role C's handoff says the API key has not been granted yet
- **line 689** `Registered eligibility criteria`
  - evidence: ec_v1 is not frozen: HANDOFFS A 3 Oct says it is 'ready for sign-off, not frozen and not to be scored'; DECISIONS_A third review: 95 criteria, 85 trials, 235 groups
- **line 698** `report macro-averages over rules and signature classes`
  - evidence: docs/ANALYSIS_B.md s5 has seed-0 macro-averages over 103 rules and 7 structural families (e.g. ledger2 x triplets 99.1 / 98.7); selrm/metrics.py macro(over='rid'|'family'); paper/latex_v13/main.tex uses no macro key
  - note: The second grouping is the 7 'family' slices, not the 5 L2 signature classes.
- **line 730** `\ph{MedS$^3$ PRM} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}\\`
  - evidence: role-d has no results_git/C-AUD-* run; tables/audit.tex is all tbd; the numbers.json C-AUD min/max keys are null
  - note: Unmerged role-c results (D:/NAACL27/selrm-role-c/results_git/C-AUD-*/summary_*.json), as L2 Rev/Hold/TA/MR/ME/Key(MedQA one-way): MedS3 22.6/16.4/10.0/0.6/25.1/39.5; Med-PRM 19.5/86.0/12.0/0.0/16.2/57.7; FoVer 49.9/61.9/31.8/14.8/21.0/67.2; ThinkPRM (200 L2 triplets) 96.5/90.0/87.5; GenPRM ME 22.0 (200 pairs).
- **line 737** `\bb{} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}\\`
  - evidence: Measured but not wired: results_git/C-TF-critic L2 Rev 38.55, Hold 32.2, TA 27.15 [21.5, 33.6]; summary_rule_v1~missing.json MR 7.7; results_git/C-ME-critic Reversal 24.2. make_tables reads C-AUD-qwen35-9b, which does not exist (HANDOFFS C 3 Oct: read C-TF-critic there)
  - note: Key-pair values exist only in unmerged role-c C-KP-critic (MedQA one-way 79.8, CareQA 84.4). Fixing the key mapping fills this row.
- **line 755** `The two failures separate the signals (Table~\ref{tab:audit}).`
  - evidence: The audit is incomplete: only the backbone is in role-d (C-TF-critic L2 Rev 38.55, Hold 32.2). Unmerged role-c: MedS3 22.6/16.35, Med-PRM 19.45/85.95, FoVer 49.9/61.9, ThinkPRM 96.5/90.0
  - note: So far there is no clean split: the backbone and MedS3 fail both checks, and ThinkPRM fails neither.
- **line 757** `\res{min/run/C-AUD-meds3/L2/all/TA|run/C-AUD-medprm/L2/all/TA|run/C-AUD-fover/L2/all/TA|run/C-AUD-injerr/L2/all/TA|`
  - evidence: numbers.json min/max PRM TA keys are null (no C-AUD run in role-d). Unmerged role-c TA: MedS3 10.0, Med-PRM 11.95, FoVer 31.8, ThinkPRM 87.5 (200-triplet subset). GenPRM L2 is not finished; the injected-error PRM is not run
  - note: The range so far is 10.0-87.5. The key list includes C-AUD-injerr, which will never exist.
- **line 757** `Open judges reverse more often and hold on`
  - evidence: Only the backbone is measured (results_git/C-TF-critic L2 Rev 38.55); Llama-3.3-70B, Qwen3.5-27B and Kimi K3 are not run
  - note: The backbone reverses more often than Med-PRM (19.45) and MedS3 (22.6), but less often than FoVer (49.9) and ThinkPRM (96.5) (unmerged role-c).
- **line 758** `hold on only \res{min/run/C-AUD-qwen35-9b/L2/all/Hold|run/C-AUD-llama70b/L2/all/Hold|run/C-AUD-qwen35-27b/L2/all/Hold|run/C-AUD-kimi-k3/L2/all/Hold@0}`
  - evidence: Backbone Hold 32.2 (results_git/C-TF-critic); the key names C-AUD-qwen35-9b, which does not exist; the other open judges are not run
- **line 758** `Closed judges solve`
  - evidence: No C-AUD-closed-* run in results_git or results; numbers.json keys are null; no API key yet (role C's handoff)
- **line 760** `higher on key pairs, which are not minimal`
  - evidence: Role-d has no key-pair result (no C-KP run). Unmerged role-c, MedQA one-way key-pair Reversal vs L2 Rev: backbone 79.8 vs 38.55, MedS3 39.5 vs 22.6, Med-PRM 57.7 vs 19.45, FoVer 67.2 vs 49.9
  - note: Holds for the 4 signals measured so far; 8 signals are missing.
- **line 775** `Every signal reverses correctly on at least \ph{84.9}\% of reading and of application pairs`
  - evidence: Only the backbone has reading and application scores: results_git/C-TF-critic/diagnostics.json pk P 97.7, K 96.0 (n 1,000). Role C's PRM runs did not score rule_v1/readapply
  - note: Consistent so far for the one signal measured.

### Training distribution and representation

- **line 830** `of DynaCF to case edits, gives \ph{tbd} (Table~\ref{tab:ablation}).`
  - evidence: B-AB-probe-rw-s0 is 'queued' in RUN_MATRIX_B. results_git/B-AB-probe-rw-s0 has only CLAIMED_B. Step 1 (B-AB-probe-rw-s0-scores) is DONE. The '+ probe re-weighting' row in tables/ablation.tex is all \ph{tbd}.
  - note: PAPER_NUMBERS line 21: the sentence names no metric. Once the run is done, the key is run/B-AB-probe-rw/L2/all/TA (or Hold).
- **line 835** `and the reversal rates of these two corpora (\res{run/B-F-verdict-balanced/L2/all/Rev}, \res{run/B-F-verdict-natural/L2/all/Rev}) decide`
  - evidence: B-F-verdict-{balanced,natural}-s1/s2 are 'todo' in RUN_MATRIX_B (CLAIMED_B 'queued ... b_f_s12.json', no DONE). Seeds 3-4 were dropped (DECISIONS_B row 57). The reversal rates are measured: balanced 93.7 against natural 92.0 (seed 0; ANALYSIS_B section 6).
  - note: Covers 'the remaining seeds' on line 834. On reversal, balanced is only 1.6 points higher. P1 (TA) already goes the opposite way with p<0.001 at seed 0.

### Transfer within and beyond rules

- **line 880** `\ \ + prompted ledger & \ph{tbd} & \ph{tbd}`
  - evidence: docs/STATE_C.md (09:10 UTC): C-TF-promptledger parts --p2/--p3 and the lenient rejudges are still running. docs/RESULTS_C.md: C-TF-promptledger 'not run'. C-ME-promptledger is queued in configs/tasks_c/c_long2.json.
  - note: The rule-tier, Criteria and MedEinst cells of this row have no result yet.
- **line 881** `Generated-program verifier & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & -- & -- & --`
  - evidence: C-TF-genprog is queued in configs/tasks_c/c_wave2.json and listed in progress (32 GB runner) in docs/STATE_C.md. docs/RESULTS_C.md: 'not run'.
- **line 883** `100.0\sd{0.0} & \ph{tbd} & 66.7\sd{2.7}`
  - evidence: Every Criteria cell reads ec_v1:test. docs/HANDOFFS.md (A, 3 Oct): ec_v1 is 'still not frozen and not to be scored'. data/REGISTRY.json has no ec_v1 entry. docs/EC_SIGNOFF.csv: 95 criteria await two reviews.
  - note: The whole Criteria column of Table main prints tbd.
- **line 884** `Verdict only, FoVer data & \ph{tbd}`
  - evidence: results_git/B-TR-fover-s0..s2 contain only CLAIMED_B (no DONE). Data: ryokamoi/FoVer-FormalLogic-FormalProof-Qwen-2.5-7B-LastStepBalanced-40k (DECISIONS_B 2 Oct). Eval sets: dev, L2, L3alt, dev_missing, missing, xr_v1 (configs/queues/b_tr_s0.json).
  - note: No clinical set or ec_v1 is in its eval list, and make_tables aliases clinical keys only for B-F-/C-TF- prefixes. The TrialGPT and MedEinst cells of B-TR rows therefore need a C run plus a key alias. STATE_C (Next 6) plans C-TG/C-ME runs for B-TR-*.
- **line 887** `GenPRM-style verifier, rule triplets & \ph{tbd}`
  - evidence: results_git/B-TR-genprm-s0..s2 contain only CLAIMED_B. configs/queues/v2/b_genprm_s0.json eval sets: dev, L2, L3alt, dev_missing, missing, xr_v1.
  - note: Its clinical columns have the same wiring gap as the FoVer row.
- **line 890** `& 100.0\sd{0.0} & \ph{tbd} & 99.9\sd{0.1}`
  - evidence: The XA cells of all trained rows print tbd, but the results exist. B's summaries store XA as xr.conclusion.XA (e.g. results_git/B-F-ledger2-triplets-s1/summary_xr_v1~test.json 88.75), while make_tables reads top/XA. The s0 values sit in B-NS-xr_v1-B-F-<x>-s0. Seed means (docs/ANALYSIS_B.md s12): ledger2-triplets 89.8, verdict-triplets 88.85, summary2-triplets 90.45, ledger2-blocks 62.3 (s.d. 19.9), verdict-blocks ...
  - note: These cells are measured but shown as tbd, so the caption's 'rule-tier cells not yet measured are marked' is wrong for XA. Wire the key, and also give the 362-item variant without A's known issues.
- **line 890** `& 69.1 & \ph{tbd}`
  - evidence: The MedEinst column of the trained rows: results_git holds only C-ME-critic and C-ME-defcorr. C-ME-{verdict-blocks,verdict-triplets,ledger2-triplets,ledger2-blocks,summary2-triplets}-s0 are queued or running (configs/tasks_c/c_long2.json; docs/STATE_C.md). docs/RESULTS_SUMMARY.md: P4 and P5 'not run'.
- **line 893** `\method{}, clinical pairs only & \ph{tbd}`
  - evidence: results_git/B-TR-clinonly-s0..s2 contain only CLAIMED_B. Corpus clin_v1/clinpairs_train = 7,807 MedEinst reference pairs + 122 MedQA-train key pairs (DECISIONS_B 3 Oct). Its eval list has no medeinst_test or trialgpt_test (configs/queues/b_tr_s0.json).
  - note: The MedEinst and TrialGPT cells also need a C-ME/C-TG run and a key alias for B-TR prefixes.
- **line 894** `\method{}, rule triplets + clinical pairs & \ph{tbd}`
  - evidence: results_git/B-TR-tripclin-s0..s2 contain only CLAIMED_B (30k rule triplets + 30k clinical pairs; DECISIONS_B 3 Oct). Its eval list has the same gap (configs/queues/b_tr_s0.json).
  - note: Per DECISIONS_D (3 Oct), Table 5 switches to this model if it is DONE by the run freeze.
- **line 896** `\ph{Claude Opus 5.5}, zero-shot & \ph{tbd}`
  - evidence: C-REF-closed-zero and C-REF-closed-ledger (docs/RUN_MATRIX.csv, todo) wait for OPENROUTER_API_KEY, which is open COMPUTE REQUEST #1 (docs/STATE_C.md). No C-REF-* run exists in results_git.
  - note: Covers rows 896-897. The model name is a placeholder until the audit picks the best closed judge; DECISIONS_C lists the third closed judge of DECISIONS_C among three closed flagships.
- **line 898** `Extraction + hand-written program & \ph{tbd}`
  - evidence: docs/DECISIONS_C.md (3 Oct) C-REF-extract-program: the extractor is the untrained backbone's format-normalised prompted ledger, and the program is A's rule_v1 program run through B's program_ledger.py, on dev_missing, missing, test_L2 and test_L3alt. The script is ready and waits for the merged C-TF-promptledger-lenient (docs/STATE_C.md).
  - note: The extractor is the untrained 9B backbone, not a strong or closed model (RUN_MATRIX said 'extraction by a strong model').
- **line 930** `the three tests the renderer does not determine`
  - evidence: xr_v1 is frozen and scored (data/REGISTRY.json). challenge_v1 has author kits only (challenge_v1/form_author*.md) and no registry entry. ec_v1 is not frozen and 'not to be scored' (docs/HANDOFFS.md, A, 3 Oct).
  - note: Two of the three tests do not exist yet. xr_v1 itself is built with the generator's test templates (MANIFEST 'templates': 'test'), but role A's docs/PAPER_VS_CODE.md (3.1-22) accepts it under this heading.
- **line 931** `rule-side items is \res{run/B-F-ledger2-triplets/xr_v1:test/top/XA} for \method{} and \res{run/B-F-verdict-triplets/xr_v1:test/top/XA} for the verdict-only model`
  - evidence: tables/numbers.json: both keys are null (tbd). Raw results exist (field xr.conclusion.XA): Ledger-RM 89.75/88.75/91.5/94.0/85.0, mean 89.8; verdict-only 90.25/91.25/90.0/87.25/85.5, mean 88.85 (docs/ANALYSIS_B.md s12; B-NS-xr_v1-*-s0 and B-F-*-s1..s4 summaries).
  - note: The key reads top/XA, but B writes xr.conclusion.XA, and the s0 values live in B-NS-xr_v1-B-F-<x>-s0. At seed 0 the verdict-only model is higher (90.2 vs 89.8). The bit-only systems reach 97.8 (HANDOFFS, B, 3 Oct), so xr_v1 shows no advantage from the ledger fields.
- **line 932** `on author-written cases triplet accuracy is \res{run/B-F-ledger2-triplets/challenge_v1:test/all/TA} and \res{run/B-F-verdict-triplets/challenge_v1:test/all/TA}`
  - evidence: tables/numbers.json: null. challenge_v1 has not been assembled or frozen (author kit H2, docs/HANDOFFS.md, A, 3 Oct) and has no entry in data/REGISTRY.json.
- **line 933** `eligibility criteria \res{run/B-F-ledger2-triplets/ec_v1:test/all/TA} and \res{run/B-F-verdict-triplets/ec_v1:test/all/TA}`
  - evidence: tables/numbers.json: null. ec_v1 is 'still not frozen and not to be scored' (docs/HANDOFFS.md, A, 3 Oct).
- **line 933** `Training on FoVer's formal data gives \res{run/B-TR-fover/L2/all/TA} on L2`
  - evidence: tables/numbers.json: null. results_git/B-TR-fover-s0..s2 contain only CLAIMED_B.
  - note: 'Formal data' matches the design: FoVer FormalLogic/FormalProof, 60k verdict records (DECISIONS_B 2 Oct).
- **line 945** `to \res{run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal}\%`
  - evidence: tables/numbers.json: null. docs/RESULTS_SUMMARY.md P4: 'not run'. C-ME-ledger2-triplets-s0 is running (configs/tasks_c/c_long2.json; docs/STATE_C.md).
  - note: The claimed rise cannot be checked yet.
- **line 946** `[\res{run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal/lo}, \res{run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal/hi}]`
  - evidence: tables/numbers.json: both null.
  - note: DECISIONS_C (3 Oct): pairs that share both diagnoses are correlated, so the label-pair CI is the one to use for inference (critic: [14.4, 35.6] vs [23.0, 25.4] over pairs). Make sure lo/hi use it.
- **line 946** `against \res{run/B-F-summary2-triplets/clin_v1:medeinst_test/top/Reversal}\% for the free-form summary`
  - evidence: tables/numbers.json: null. docs/RESULTS_SUMMARY.md P5: 'not run'. C-ME-summary2-triplets-s0 is queued (configs/tasks_c/c_long2.json).
- **line 948** `at a small price in reversal`
  - evidence: MedEinst and NLI4CT-P have not been run for the blocks and triplets models (C-ME- and C-NL-ledger2-{blocks,triplets}-s0 are queued in c_long2.json). On L2 there is no price at all: Rev 99.3 vs 99.3 (ledger) and 92.6 vs 92.6 (verdict) (docs/ANALYSIS_B.md s13).
  - note: If the claim is meant generally, the rule tier does not support it.
- **line 949** `the triplets model loses \res{d/run/B-F-ledger2-blocks/clin_v1:medeinst_test/top/Reversal|run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal} points on MedEinst`
  - evidence: tables/numbers.json: null. C-ME-ledger2-blocks-s0 and C-ME-ledger2-triplets-s0 are queued or running (configs/tasks_c/c_long2.json).
- **line 950** `\res{d/run/B-F-ledger2-blocks/clin_v1:nli4ct_test/top/faithfulness|run/B-F-ledger2-triplets/clin_v1:nli4ct_test/top/faithfulness} of NLI4CT-P faithfulness`
  - evidence: tables/numbers.json: null. results_git has no C-NL-* run. C-NL-ledger2-{triplets,blocks}-s0 are queued (configs/tasks_c/c_long2.json).
- **line 950** `and gains \res{d/run/B-F-ledger2-triplets/clin_v1:nli4ct_test/top/consistency|run/B-F-ledger2-blocks/clin_v1:nli4ct_test/top/consistency} of consistency`
  - evidence: tables/numbers.json: null. C-NL-* runs are queued but have not run.
- **line 951** `Trained on clinical pairs, the model reaches \ph{66.8}\% on MedEinst`
  - evidence: B-TR-clinonly-s0..s2 and B-TR-tripclin-s0..s2 contain only CLAIMED_B. Neither eval list includes clin_v1/medeinst_test (configs/queues/b_tr_s0.json). docs/PAPER_NUMBERS.md rejected the mapping: 66.8 was v10's tripclin placeholder, but the prose names clinonly.
  - note: Name the row, queue its MedEinst scoring (C-ME run) and alias the key.
- **line 952** `with diseases held out it is \ph{58.9}\%`
  - evidence: B-DIS-s0..s2 contain only CLAIMED_B. They train on clin_v1/clinpairs_medeinst_dis (3,145 pairs, training diseases) and evaluate on clin_v1/medeinst_dis_test (115 pairs, 12 held-out diagnoses) (configs/queues/b_tr_s0.json; DECISIONS_B 3 Oct).
  - note: B-DIS uses MedEinst pairs only (no MedQA key pairs), so it matches clinonly rather than tripclin.
- **line 957** `It reaches \res{run/B-TR-genprm/L2/all/TA}\% on L2 and \res{run/B-TR-genprm/L3alt/all/TA}\% on altered rules`
  - evidence: tables/numbers.json: null. results_git/B-TR-genprm-s0..s2 contain only CLAIMED_B.
- **line 957** `at \ph{11} times the generated tokens`
  - evidence: B-TR-genprm records the tokens it generates (DECISIONS_B 2 Oct) but is not DONE. docs/PAPER_NUMBERS.md (line-957 entry): the key grammar has no ratio, and eval_generated_tokens covers different set lists per run.
  - note: Once the run is done, this needs a defined key computed on the same sets for both systems.
- **line 959** `on MedEinst, where there is nothing to execute, it is at \res{run/B-TR-genprm/clin_v1:medeinst_test/top/Reversal}\%`
  - evidence: tables/numbers.json: null. The B-TR-genprm eval list has no clin_v1/medeinst_test (configs/queues/v2/b_genprm_s0.json), and no C-ME genprm run is queued (configs/tasks_c/c_long2.json).
  - note: 'Nothing to execute' fits, because MedEinst records have an empty rule_text (DECISIONS_C). Without a queued run this value stays tbd.
- **line 962** `The closed judge with a ledger prompt leads on L2, key pairs and NLI4CT-P.`
  - evidence: C-REF-closed-ledger has not run: the API judges wait for OPENROUTER_API_KEY (COMPUTE REQUEST #1, docs/STATE_C.md). results_git has no C-REF-*, C-KP-* or C-NL-* run, and the main-app table is all tbd.
  - note: To lead on L2, the closed judge would have to beat Ledger-RM's 99.2.

### What the judge uses

- **line 980** `\node[red, font=\tiny] at (rel axis cs:0.5,0.5) {\ph{tbd}};`
  - evidence: This is the generated fig-div body (tables/fig-div.tex; make_tables.py f_div reads run/B-DIV-*/L2/all/TA). All 39 results_git/B-DIV-{base,new,same,patients}-*-s{0,1,2} directories hold only CLAIMED_B: no DONE file and no summary. The numbers.json keys run/B-DIV-base-16, -new-223, -same-63 and -patients-223 (L2/all/TA) are all null.
  - note: The runs are registered (DECISIONS_B 2 Oct diversity row; seed 0 at priority 80, seeds 1-2 at 90). HANDOFFS B 2 Oct names them as the first cut if the schedule slips.
- **line 1014** `test of the fields: \res{run/B-AB-bitonly-judge/clin_v1:medeinst_test/top/Reversal}\%`
  - evidence: numbers.json key is null. results_git/B-AB-bitonly-judge-s0 holds only dev, test_L2 and xr_v1 summaries. The only MedEinst results so far are C-ME-critic (24.2) and C-ME-defcorr (24.7) (docs/MEDEINST_RESULTS.md). C will score B's kept adapters as C-ME-* runs (HANDOFFS C 3 Oct), and DECISIONS_B 2 Oct keeps the B-AB seed-0 adapters for this.
  - note: On xr_v1, the other transfer test that exists, the bit-only judge has XA 97.8 against 85.0-94.0 for ledger2 x triplets seeds 0-4 (ANALYSIS_B sec. 12). B's correction in HANDOFFS 3 Oct: 'xr_v1 does not show a transfer benefit of the fields'.
- **line 1014** `against \res{run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal}\% on MedEinst zero-shot`
  - evidence: numbers.json key is null, and no results_git/B-F-ledger2-triplets-s* directory has a summary_clin_v1~medeinst_test.json. RESULTS_SUMMARY lists P4 and P5 as 'not run'. The ME column of Table ablation is all tbd.
  - note: Planned: C-ME-* runs on B's registered adapters.
- **line 1016** `and a reader trained to write the bit without fields reaches \ph{tbd}\%.`
  - evidence: I read this as the MedEinst value, because the clause sits in the transfer sentence and the 'reader writes bit only' row of Table ablation has ME tbd. results_git/B-AB-bitonly-reader-s0 holds only dev, test_L2 and xr_v1 summaries (s1 and s2 are CLAIMED_B only), so no MedEinst result exists. The L2 result does exist: TA 99.95 (printed 100.0), Rev 99.95, Hold 100.0; +0.8 [+0.3, +1.4], p < 0.001 over the fact-only le...
  - note: If the authors meant L2 (v10 had \ph{63.0} here as the L2 TA), the value is 100.0. That is above the fact-only ledger, the opposite of what v10 claimed; HANDOFFS B 3 Oct: 'against the draft's 63.0 placeholder'.
- **line 1033** `On MedEinst zero-shot it is \res{d/run/B-F-rationale-triplets/clin_v1:medeinst_test/top/Reversal|run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal} points better than`
  - evidence: The difference key in numbers.json is null. Neither results_git/B-F-rationale-triplets-s0 nor any B-F-ledger2-triplets-s* has a clin_v1/medeinst_test summary. The rationale x triplets s0 adapter is registered for C (HANDOFFS B 3 Oct) and kept for the Table 9 MedEinst column (DECISIONS_B 2 Oct).
  - note: The direction 'better' has not been measured yet.
- **line 1034** `where a few typed fields cannot carry the evidence, the bottleneck costs accuracy.`
  - evidence: This depends on the MedEinst comparison above, which has no result (key null).
  - note: On rule triplets the opposite holds: one-stage 91.0 against two-stage 99.2.
- **line 1054** `classes raise L2 accuracy from \res{run/B-DIV-base-16/L2/all/TA}\%`
  - evidence: numbers.json run/B-DIV-base-16/L2/all/TA is null, and results_git/B-DIV-base-16-s0..s2 hold CLAIMED_B only.
  - note: The run is registered (DECISIONS_B 2 Oct).
- **line 1054** `to \res{run/B-DIV-new-223/L2/all/TA}\%, rules of seen classes to`
  - evidence: numbers.json run/B-DIV-new-223/L2/all/TA is null, and results_git/B-DIV-new-223-s0..s2 hold CLAIMED_B only.
  - note: The direction 'raise' has not been measured.
- **line 1055** `\res{run/B-DIV-same-63/L2/all/TA}\%, more cases to`
  - evidence: numbers.json is null, and results_git/B-DIV-same-63-s0..s2 hold CLAIMED_B only.
  - note: The seen-classes arm stops at 63 rules because the library cannot fill more (DATA_A.md). The text therefore compares it with the new-classes arm at 223 rules.
- **line 1055** `more cases to \res{run/B-DIV-patients-223/L2/all/TA}\%.`
  - evidence: numbers.json is null, and results_git/B-DIV-patients-223-s0..s2 hold CLAIMED_B only.
  - note: The run is registered (DECISIONS_B 2 Oct).

### Candidate selection, conclusion, limitations

- **line 1082** `\ \ \ rule triplets only & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}`
  - evidence: In scripts/make_tables.py SELECTION, these rows (lines 1082 and 1085) map to D-SEL-ledger-rule and D-SEL-combined-rule. select_eval.py creates them only when Ledger/Combined use B-TR-tripclin-s0, and results_git/B-TR-tripclin-s0 holds only CLAIMED_B. DECISIONS_D 3 Oct: if that run is not DONE by the 7 Oct freeze, Table 5 uses the rule-only models.
  - note: If B-TR-tripclin-s0 misses the freeze, both rows are dropped, as the make_tables comment says.
- **line 1087** `\ph{Claude Opus 5.5} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}`
  - evidence: docs/RUN_MATRIX_D.csv lists D-SEL-closed (closed judge as selector, P1, todo), and results_git has no D-SEL-closed. docs/STATE_D.md Blockers: 'Closed-judge row of Table 5: needs an API key (C's COMPUTE REQUEST #1)'.
  - note: The model name is itself a placeholder. DECISIONS_C 3 Oct lists the third closed judge of DECISIONS_C among the audit's closed models.
- **line 1118** `On executable rules, reward models fail in two directions.`
  - evidence: RESULTS_SUMMARY A1 (audit) is 'not run'. tables/audit.tex is all \ph{tbd}, and results_git has no C-AUD-* runs.
  - note: Partial evidence: the untrained Qwen3.5-9B critic on L2 has Rev 38.5, Hold 32.2, TA 27.1 (docs/RESULTS_C.md, C-TF-critic). Verdict x blocks has Rev 92.6 and Hold 57.9 (5 seeds). The audit of released PRMs and judges is missing.
- **line 1121** `and, \ph{in part}, to existing clinical labels.`
  - evidence: P4 (MedEinst, Ledger-RM vs critic) is not run: B-F-ledger2-triplets MedEinst Reversal is tbd, and only C-ME-critic (24.2) and C-ME-defcorr exist. P6a (TrialGPT macro-F1) is 69.1 vs 65.7: +3.4 [-2.6, +9.2], p 0.244 (docs/TRIALGPT_RESULTS.md). HANDOFFS 3 Oct (C): 'Comparison (6) ... does not hold on test'.
  - note: On the only measured clinical-label comparison the gain is not significant. \ph{in part} depends on P4.
- **line 1151** `Beyond rules, holding is tested on author-written cases and registered criteria, which still use our programs`
  - evidence: The author-written cases (challenge_v1, kit H2) are still with the authors and are frozen only when all 160 groups pass (HANDOFFS 3 Oct, A). ec_v1 (95 criteria awaiting sign-off) is 'still not frozen and not to be scored' (HANDOFFS 3 Oct, A). results_git has no results for either.
- **line 1153** `by NLI4CT-P consistency under statement edits`
  - evidence: The data are built (RUN_MATRIX_C C-CL-nli4ct done; clin_v1/nli4ct_test frozen), but no C-NL-* run is in results_git. numbers.json NLI4CT keys print tbd, e.g. run/B-F-ledger2-triplets/clin_v1:nli4ct_test/top/macroF1.
- **line 1162** `the one-stage variant is better on MedEinst.`
  - evidence: tables/numbers.json key d/run/B-F-rationale-triplets/clin_v1:medeinst_test/top/Reversal|run/B-F-ledger2-triplets/... is tbd. The ablation table's ME column is tbd. results_git has only C-ME-critic and C-ME-defcorr.
  - note: 'One-stage variant' here means the rationale model (main.tex line 1029).
- **line 1170** `We do not show that a policy trained against it is safer, and we make no claim about preventing reward exploitation beyond the policy-training experiment.`
  - evidence: The ledger-reward GRPO runs have not started (DECISIONS_D 3 Oct; RESULTS_SUMMARY G1 'not run'). Seed 0, Qwen3.5-4B, held-out L2 pairs: the step-check (Med-PRM) reward takes pair accuracy from 89.3 at the start to 37.3 at step 1,000 while reward rises to 0.9997 (results_git/ (GRPO files; interim copies at audit time) D-RL-stepcheck-s0.curve.jsonl). The outcome reward is at 97.3 at step 800 and the reference graph a...
  - note: The experiment the sentence refers to has no ledger-reward result yet.

### App. A-C (analysis plan, rule library, triplet construction)

- **line 1221** `reversal on MedEinst test pairs for the model trained on rule triplets only.`
  - evidence: First endpoint exists: run/B-F-ledger2-triplets/L2/all/TA = 99.2 (seeds 0-4, CI [98.9, 99.6]; numbers.json). Second does not: RESULTS_SUMMARY P4/P5 'run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal = tbd'; results_git holds only C-ME-critic (24.2 [23.0, 25.4]) and C-ME-defcorr (24.7) (docs/MEDEINST_RESULTS.md).
  - note: L2 TA endpoint measured; MedEinst reversal of the rule-triplet model not yet run.
- **line 1225** `Holm-corrected`
  - evidence: tables/primary.tex prints p_Holm \ph{tbd} in every row; make_tables.py computes padj only when all 7 p-values exist and (4), (5) have none; RESULTS_SUMMARY P1-P6b status 'pending (Holm family incomplete)'.
  - note: Family of 7 is defined (cmp/holm/n = 7); adjusted p-values await the MedEinst comparisons.
- **line 1237** `If (4) and (6) fail, the answer outside rules is negative and the medical claim is withdrawn.`
  - evidence: (6) has failed: 6a +3.4 [-2.6, 9.2], p 0.244; 6b -1.8 [-4.8, 1.1], p 0.214 (results_git/C-TG-comparisons_test.json; DECISIONS_C 3 Oct 'TrialGPT ... (6) not supported'; HANDOFFS 3 Oct C 'Comparison (6) ... does not hold on test'). (4) not run (RESULTS_SUMMARY P4: ledger reversal tbd; critic 24.2).
  - note: The outcome of this rule now depends only on (4).
- **line 1251** `$p_{\mathrm{Holm}}$`
  - evidence: All seven p_Holm cells print \ph{tbd} (tables/primary.tex); padj is computed only once (4) and (5) have p-values (make_tables.py comparisons()).
  - note: Planned; waits for the MedEinst comparisons (C-ME-comparisons.json not yet written).
- **line 1258** `(4) rule-only \method{} $-$ critic, MedEinst reversal & \ph{tbd} & [\ph{tbd}, \ph{tbd}] & \ph{tbd}`
  - evidence: PROVENANCE p4 has no diff/p; results_git/C-ME-comparisons.json absent; only the critic side exists (C-ME-critic reversal 24.2 [23.0, 25.4]).
  - note: Waits for C-ME runs of B-F-ledger2-triplets.
- **line 1259** `(5) rule-only \method{} $-$ rule-only summary, MedEinst reversal & \ph{tbd}`
  - evidence: PROVENANCE p5 empty; neither ledger nor summary MedEinst run in results_git (RESULTS_SUMMARY P5 'not run').
  - note: Waits for C-ME runs.
- **line 1315** `extraction check on rewrites`
  - evidence: rewrite_v1 not built: DECISIONS_A 2 Oct (rewriter and two extractors configured; 'Still waits for OPENROUTER_API_KEY'); no rewrite_v1 entry in data/REGISTRY.json; no results/A-D11.
- **line 1316** `author-written cases`
  - evidence: challenge_v1 is a kit only (form_author1-4.md, specs.jsonl; no notes; not in data/REGISTRY.json); PAPER_VS_CODE 3.1-23 'the set exists after H2'.
- **line 1317** `registered criteria`
  - evidence: ec_v1 awaits author sign-off (H3) and is 'not frozen and not to be scored' (HANDOFFS 3 Oct A; DECISIONS_A 3 Oct: 95 criteria, 85 trials, 235 groups prepared); not in data/REGISTRY.json.
- **line 1317** `MedEinst`
  - evidence: Only the untrained critic (24.2 [23.0, 25.4]) and default correction (24.7) are scored on MedEinst (docs/MEDEINST_RESULTS.md); no trained system yet (RESULTS_SUMMARY P4/P5).
- **line 1327** `Each rule is marked as a \emph{verbatim source rule} (\ph{tbd}), a \emph{simplified source rule} (\ph{tbd}) or \emph{synthetic} (\ph{tbd}).`
  - evidence: Value available, not keyed: data_stats.json rules.provenance verbatim 0, simplified_source 97, synthetic 256 (library of 353); hand-written: 97 simplified, 6 synthetic (DATA_AUDIT sec. 1; PAPER_VS_CODE B-2; results/A-AUDIT/summary.json 'rules').
  - note: Fill 0 / 97 / 256; no rule restates a source verbatim.
- **line 1340** `\ph{[state who reviewed them and what they were asked]}`
  - evidence: Value available: DATA_AUDIT sec. 10 'People: 0'; the review sessions recorded there are not independent of the generator (DATA_AUDIT_rule_v1.md lines 369-371) and checked label, consistency, rendering, give-aways and missing twins; instructions and reports in audit/model_review/.
  - note: Fill from the audit; it also means Table validity's 'by the authors' is wrong.
- **line 1345** `The authors separately read \ph{tbd} groups for dropped negation, wrong subject, ambiguous time expressions, conflicting measurements and omitted exceptions, and found \ph{tbd}`
  - evidence: H1 planned: 300 fold-1 test groups (L2 150, hard 50, L3-inv 30, L3-alt 30, L0 20, L1 20; 1,276 rows) in audit/h1/; no answers_*.csv and no results/A-H1 (HANDOFFS 3 Oct A).
  - note: H1 problem types are dropped negation, wrong subject, ambiguous time, conflicting lines, wording, other (audit/h1/README.md); 'omitted exceptions' is not one.
- **line 1359** `Options are plain orders of one form that differ by at most \ph{2} tokens and contain no word that gives a reason.`
  - evidence: Measured in whitespace words, not tokens: constraint_claim_word_diff_max = 2 over 310 constraint rules (data_stats library_semantics; PAPER_VS_CODE 3.1-9, B-5); claims read '<Verb> <default>.' vs '<Verb> <alternative>.'. No token count exists or is planned (PAPER_NUMBERS.md line 219).
  - note: Write 'words' (then consistent at 2) or measure tokens.
- **line 1375** `Distinct program structures (names, constants removed) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: data_stats structure.train_triplets.distinct_structures = 74, structure.test_L2 = 56 (also results/A-AUDIT/summary.json 'structure').
  - note: Fill 74 / 56.
- **line 1376** `Signature classes & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: signature_classes 16 (train_triplets) / 5 (test_L2).
  - note: Fill 16 / 5.
- **line 1377** `Conditions needed per judgment (mean; max) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: conditions_mean 1.79, max 4 (train) / 2.51, max 4 (L2).
- **line 1378** `Dependency depth (mean; max) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: depth_mean 1.58, max 2 (train) / 1.83, max 2 (L2).
- **line 1379** `Evidence mentions required (mean) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: evidence_mentions_mean 1.75 (train) / 2.49 (L2), mean over base, flip and near-miss.
- **line 1380** `Cases with competing mentions of the concept (\%) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: competing_mentions_pct 9.0 (train) / 13.4 (L2).
  - note: In rule_v1 these are only an older value beside the current value (DATA_AUDIT sec. 7).
- **line 1381** `Judgments with a temporal operation (\%) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: temporal_pct 24.3 (train) / 49.1 (L2).
- **line 1382** `Judgments with a numeric comparison (\%) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: numeric_pct 64.1 (train) / 83.0 (L2).
- **line 1383** `Judgments with an exception (\%) & \ph{tbd} & \ph{tbd}`
  - evidence: Value available: exception_pct 86.9 (train) / 82.8 (L2).
- **line 1394** `source documents (\ph{tbd})`
  - evidence: Value available: data_stats overlap.rule_v1/test_L2.source_shared_with_train_pct = 5.0 (of the 20 L2 rules with a source record; DATA_AUDIT sec. 5; PAPER_VS_CODE B-9).
  - note: Fill 5%.
- **line 1395** `parameter-normalised structures (\ph{tbd})`
  - evidence: Value available: data_stats overlap.rule_v1/test_L2.structure_pct = 0.0 (PAPER_VS_CODE B-9 'normalised structures 0%').
  - note: Fill 0%.
- **line 1397** `underlying states (\ph{tbd})`
  - evidence: Value available: rule-keyed base states shared 0 of 1,775 (by construction); patient states without the rule 51 of 1,745 (data_stats overlap.rule_v1/test_L2; DATA_AUDIT sec. 5).
- **line 1404** `its near-miss kinds are \ph{tbd}`
  - evidence: Value available: test_L3alt kinds boundary 333, time 333, numeric 334; no subject or negation, since L3-alt has only measured criteria (17 rules, 18 criteria; DATA_AUDIT sec. 6).
  - note: Fill 'numeric, boundary and time only'.
- **line 1409** `Rule-side items, author-written cases, rewritten cases and registered criteria are separate named sets, each frozen before any system was scored on it.`
  - evidence: challenge_v1 (kit; H2 not done), rewrite_v1 (not run; needs OPENROUTER_API_KEY) and ec_v1 (sign-off H3 pending, 'not to be scored') are not in data/REGISTRY.json.
  - note: Author-written, rewritten and registered-criteria sets do not exist yet.
- **line 1411** `Defects found after the freeze are listed with the affected items, and results are given with and without them (\ph{tbd} items).`
  - evidence: xr_v1: 38 known-issue items (23 age, 15 diabetes; data/xr_v1/KNOWN_ISSUES.json), XA reported both ways (e.g. critic 39.0 on 400 / 42.5 on 362; docs/RESULTS_C.md). rule_v1: KNOWN_ISSUES.json has 0 violations and lists semantic limits (23 s3_jhfrat window groups; 7 cases in 4 angioedema groups); no results without them exist or are planned (PAPER_NUMBERS.md line 232).
  - note: Count available per set; rule_v1 with/without results not planned.
- **line 1449** `(of which at the threshold \ph{tbd})`
  - evidence: Value available: boundary kind = 400 of the 800 numeric near-misses in L2 (half; 20% of all) (DATA_AUDIT sec. 8; PAPER_NUMBERS.md line 112).
  - note: Strict thresholds only.
- **line 1466** `Temporal selection & an older value crosses the threshold; the latest does not & \ph{tbd}`
  - evidence: Value available: test_L2 268, test_hard 138 (DATA_AUDIT sec. 7).
  - note: Same count as competing mentions in rule_v1; the table does not say which test set.
- **line 1467** `Composition & two conditions with an explicit exception & \ph{tbd}`
  - evidence: Value available: test_L2 1,656 (1,526 with another condition met in the base), test_hard 815 (DATA_AUDIT sec. 7).
- **line 1468** `Numerical semantics & values at inclusive and exclusive boundaries; unit given in the rule & \ph{tbd}`
  - evidence: Value available: value at a strict threshold or flip at an inclusive one, test_L2 498, test_hard 241 (DATA_AUDIT sec. 7).
  - note: No rule needs a unit conversion.
- **line 1469** `Long note & 15 or more unrelated lines & \ph{tbd}`
  - evidence: Value available: test_L2 603, test_hard 917 (DATA_AUDIT sec. 7; a15 tier.long).
- **line 1482** `(\ph{tbd} items; \ph{tbd} phrasings per clause)`
  - evidence: Value available: 400 items; 3 phrasings per clause (items per phrasing index 134/133/133) (PAPER_VS_CODE 3.1-22, C-18).
- **line 1485** `\emph{Author-written cases}: \ph{tbd} groups written by the authors from state specifications, each checked by a second author.`
  - evidence: challenge_v1: 160 state specifications planned (32 per near-miss kind, 40 per author; the assembler requires a second-author check; DECISIONS_A 2-3 Oct); no notes written, set not frozen (absent from data/REGISTRY.json).
- **line 1488** `(\ph{8.7}\% rejected)`
  - evidence: rewrite_v1 not run: waits for OPENROUTER_API_KEY (DECISIONS_A 2 Oct; TIMELINE 'Not run at the refs read'); no results/A-D11.
- **line 1489** `(\method{}: \res{run/B-F-ledger2-triplets/rewrite_v1:test/all/TA})`
  - evidence: numbers.json: key value \ph{tbd}, number null; rewrite_v1 not built.

### App. D-E (external tiers, ledger format)

- **line 1501** `Criteria are taken as written from registered trials (\ph{tbd} criteria from \ph{tbd}`
  - evidence: ec_v1/prepare_summary.json: kept 95, trials 85, groups 235 (17 inclusion, 78 exclusion). HANDOFFS 3 Oct (A): 'ec_v1 has 95 criteria (85 trials, 235 groups) ... still not frozen and not to be scored'. docs/ec_signoff/ holds only TEMPLATE.csv.
  - note: The current count is 95 criteria from 85 trials. It changed at each review (100/90, then 99, 96/86, 95/85) and is final only after the two-author sign-off and freeze.
- **line 1508** `who did not write the program checks it against the sentence; this is a`
  - evidence: HUMAN_TASKS.md H3 (two authors, due Mon 5). docs/ec_signoff/ contains only TEMPLATE.csv. HANDOFFS 3 Oct (A): 'ec_v1 is still not frozen'. EC_SIGNOFF.csv verification column: 90 'confirmed by both model verifiers', 5 rescued.
  - note: So far only a reviewer that is not a person have formalised and checked the programs. The author check has not been done.
- **line 1556** `tercile of vignette similarity, reversal of the critic is \ph{55.7}\%,`
  - evidence: No C-KP-* run exists in results_git or results. Key-pair records carry stem similarity and its tercile in meta (keypairs_*_oneway MANIFEST rule). C-KP-critic is the planned run (HANDOFFS 3 Oct, C).
  - note: The C-KP summary needs a tercile slice; at present it defines only a top-level Reversal.
- **line 1557** `\ph{44.1}\% and \ph{33.8}\%.`
  - evidence: Same as line 1556: there is no C-KP-critic result yet, and the tercile is in the record meta.
  - note: -
- **line 1558** `are in the repository`
  - evidence: There is no C-KP-* result yet. DECISIONS_C 3 Oct plans to report the CareQA one-directional pairs 'by area'.
  - note: -
- **line 1596** `Critic & \ph{tbd} & \ph{tbd} & \ph{tbd}\\`
  - evidence: The generated tables/main-app.tex has \ph{tbd} in every cell. No C-KP-* or C-NL-* run exists in results_git. numbers.json nli4ct keys have number null.
  - note: Applies to every cell of tab:main-app (lines 1596-1615): no system has been scored yet on key pairs or NLI4CT-P.
- **line 1611** `\method{}, clinical pairs only & \ph{tbd} & \ph{tbd} & \ph{tbd}\\`
  - evidence: results_git/B-TR-clinonly-s0..s2 and B-TR-tripclin-s0..s2 contain only CLAIMED_B. Their training set clin_v1/clinpairs_train is frozen (HANDOFFS 3 Oct, C).
  - note: Also applies to the 'rule triplets + clinical pairs' row (line 1612).
- **line 1614** `\ph{Claude Opus 5.5}, zero-shot & \ph{tbd} & \ph{tbd} & \ph{tbd}\\`
  - evidence: docs/RUN_MATRIX_C.csv: C-REF-closed-zero and C-REF-closed-ledger are 'blocked, API key (COMPUTE REQUEST #1)'. configs/models.json: id the third closed judge of DECISIONS_C, verified.
  - note: The row label can be typed as the verified model name; the cells wait on the API key. Also applies to line 1615.
- **line 1626** `Base macro-F1 is \res{run/C-TF-critic/clin_v1:nli4ct_test/top/macroF1} for the critic`
  - evidence: tables/numbers.json: number null (prints \ph{tbd}). No C-NL-* run exists in results_git. clin_v1/nli4ct_test is frozen with 5,500 records.
  - note: -
- **line 1626** `\res{run/B-F-ledger2-triplets/clin_v1:nli4ct_test/top/macroF1} for rule-only`
  - evidence: tables/numbers.json: number null. No NLI4CT run of B-F-ledger2-triplets exists (C-NL-*).
  - note: -
- **line 1628** `interventions is \ph{38.5}\% and \ph{47.9}\%.`
  - evidence: No C-NL run exists yet. scripts/eval_clinical.py nli_metrics computes Control F1/macro-F1, faithfulness, consistency and per-intervention accuracy, but not joint correctness over an original and all its interventions (docs/PAPER_NUMBERS.md: 'C would need to add a field').
  - note: The NLI4CT summary needs a new field once the C-NL runs exist.
- **line 1629** `that share an original statement are resampled together.`
  - evidence: scripts/eval_clinical.py nli4ct computes point estimates only, with no bootstrap or interval. No NLI4CT result exists.
  - note: Resampling clustered by original statement still has to be implemented.
- **line 1632** `By normalised question text, CareQA shares no question with MedQA.`
  - evidence: No CareQA-MedQA overlap check exists in scripts/ (grep 'overlap' finds only MedEinst and rule-tier audits) or in any doc or result file.
  - note: A check is needed before this can be stated.
- **line 1633** `portion of ReMedQA \citep{cocchieri2026remedqa} lies within the MedQA test`
  - evidence: configs/datasets_c.json lists disi-unibo-nlp/ReMedQA@3abb4b47 for an 'overlap note' but records only licence facts. No overlap result is recorded anywhere.
  - note: -
- **line 1650** `and \ph{2.4}\% of MedEinst instances; a malformed ledger is recorded as an`
  - evidence: results_git has only C-ME-critic and C-ME-defcorr, both verdict-only with no ledger. The MedEinst two-stage runs were stopped and re-queued (DECISIONS_C 3 Oct, runner row).
  - note: The value must come from eval.malformed_rate of the C-ME ledger runs. For comparison, other clinical sets give 4.0% (TrialGPT) and 16.7% (MedQA-train key pairs).

### App. F (diagnostics)

- **line 1716** `& \ph{88.4} & \ph{0.0} & \ph{26.0} (\ph{4{,}508}) & \ph{97.6} & \ph{95.4} & \ph{33.4}`
  - evidence: No Qwen3.5-27B scores: numbers.json run/C-AUD-qwen35-27b/L2/all/TA = null; RUN_MATRIX_C C-AUD-qwen35-27b 'blocked, no 80 GB card free; API key pending'; no task file lists it; C-DG-pkg diagnostics exist only for C-TF-critic
  - note: Whether a 27B run would score test_L0 and readapply is not registered anywhere yet.
- **line 1717** `\ph{Claude Opus 5.5} & \ph{96.0} & \ph{3.8} & \ph{12.9} (\ph{4{,}896}) & \ph{99.2} & \ph{98.1} & \ph{11.3}`
  - evidence: C-AUD-closed-3 (the third closed judge of DECISIONS_C, verified in configs/models.json 2026-10-03, readout 'choice') is todo and waiting on COMPUTE REQUEST #1 (STATE_C). FINAL_TASKS_C P1 plans the closed judge on the ladder sets and the composition gap
  - note: DECISIONS_C:20 limits costly models to 1,000 L2 triplets and no readapply scoring is registered for API judges, so P/K/G for this row may never exist.
- **line 1784** `$\kappa$ is reported with a bootstrap interval when the denominator is positive.`
  - evidence: results_git/C-DG-shift/summary_rule_v1~test_L0.json holds only point kappa (0.502 for the 9B judge, 1.008 for verdict blocks, both with positive denominators); scripts/diagnostics.py computes no interval; the text and figure print points only
  - note: No interval exists yet. Add one or drop the clause.
- **line 1786** `\res{run/C-DG-shift/L0/signal=C-AUD-medprm/crossed}\% of baseline-conflicting cases cross`
  - evidence: numbers.json value null; C-DG-shift summary has only signal=C-AUD-qwen35-9b and signal=B-F-verdict-blocks; DECISIONS_C: 'Med-PRM is added when C-AUD-medprm is merged' (C-AUD-medprm running per RUN_MATRIX_C/STATE_C)
- **line 1787** `\res{run/C-DG-shift/L0/signal=C-AUD-medprm/short}\% move the right way and fall short`
  - evidence: numbers.json null; no signal=C-AUD-medprm slice in results_git/C-DG-shift
- **line 1787** `\res{run/C-DG-shift/L0/signal=C-AUD-medprm/unmoved}\% do not move`
  - evidence: numbers.json null; no signal=C-AUD-medprm slice in results_git/C-DG-shift
- **line 1788** `\res{run/C-DG-shift/L0/signal=C-AUD-medprm/wrong}\% move the wrong way`
  - evidence: numbers.json null; no signal=C-AUD-medprm slice in results_git/C-DG-shift
- **line 1788** `$\kappa=\res{run/C-DG-shift/L0/signal=C-AUD-medprm/kappa@2}$`
  - evidence: numbers.json null; no signal=C-AUD-medprm slice in results_git/C-DG-shift
  - note: Measured kappa exists only for the 9B judge (0.50) and verdict blocks (1.01).
- **line 1796** `27B judge`
  - evidence: No signal=C-AUD-qwen35-27b in results_git/C-DG-shift; RUN_MATRIX_C C-DG-shift: '27B needs 80 GB card or API'; C-AUD-qwen35-27b blocked
  - note: Bar is empty.
- **line 1838** `lowers its triplet accuracy from \res{run/C-AUD-qwen35-27b/L2/all/TA}\%`
  - evidence: tables/numbers.json run/C-AUD-qwen35-27b/L2/all/TA: number null ('tbd'); RUN_MATRIX_C C-AUD-qwen35-27b blocked (no 80 GB card; API key pending)
  - note: If the sentence moves to the 9B (see next finding), the log-odds reference is C-TF-critic TA 27.15.
- **line 1844** `many injected errors are detectable within the step, and chains restate patient facts.`
  - evidence: There is no MedPRMBench data in the repository (unreleased: DECISIONS_B:51, DECISIONS_C:20/25), and no run looks at its errors or chains
  - note: Cannot be checked, and no run will ever provide evidence. Goes with the dropped paragraph.
- **line 1851** `A probe on the residual stream of the critic predicts the criterion outcome on held-out signature classes with \ph{90.8}\% accuracy`
  - evidence: C-DG-probe is in progress (STATE_C 'In progress'; RUN_MATRIX_C P3 todo; configs/tasks_c/c_gen7.json); no results_git/C-DG-probe and no probe.json. scripts/probe.py matches the design: critic hidden states, trained on test_L0 rules, tested once on test_L2 held-out signature classes
- **line 1853** `(control task \citep{hewitt2019control}: \ph{49.6}\%)`
  - evidence: Same C-DG-probe run; scripts/probe.py has the control task (random label per condition via sha256). No result yet

### App. G (additional results)

- **line 1883** `Premise gate & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}`
  - evidence: B-AE-premise-gate has no results directory. RUN_MATRIX_B lists it as todo P1 ('needs step-check scores'). HANDOFFS, 3 Oct: B asked C for the C-AUD-medprm per-example scores on dev/test_L2 and C accepted; C-AUD-medprm is not in results_git.
  - note: Planned in FINAL_TASKS_B P1. The caption's definition (gate on a ledger extracted once per case) cannot be checked until it runs.
- **line 1885** `\ \ + probe re-weighting & \ph{tbd} & \ph{tbd} & \ph{tbd}`
  - evidence: results_git/B-AB-probe-rw-s0 holds only CLAIMED_B (no DONE). Step 1, B-AB-probe-rw-s0-scores, is DONE. RUN_MATRIX_B: queued. The 3-step procedure is in DECISIONS_B, 2 Oct.
- **line 1895** `Ablations on L2 and MedEinst zero-shot (\%)`
  - evidence: Every ME cell is \ph{tbd}. make_tables reads these from C-ME-<x> runs, and only C-ME-critic (24.2) and C-ME-defcorr exist (docs/MEDEINST_RESULTS.md). RESULTS_SUMMARY P4/P5: MedEinst not run for B-F-ledger2-triplets or summary2-triplets. Still planned: FINAL_TASKS_C P1 'MedEinst for all adapters'; DECISIONS_B, 2 Oct, keeps the B-AB adapters for the Table 9 MedEinst column.
  - note: The ME column has no measured value in any row.
- **line 1929** `Closed judge, ledger & \ph{tbd} & \ph{tbd}`
  - evidence: C-REF-closed-ledger is not in results_git. RUN_MATRIX_C: 'blocked, API key (COMPUTE REQUEST #1)'.
- **line 1937** `Macro-averages over rules and over signature classes, per-seed values and the lowest held-out class are \ph{tbd}.`
  - evidence: No make_tables key produces these. docs/ANALYSIS_B.md s.5 has macro-averages over 103 rules and 7 families for seed 0 on test_L2 only (e.g. ledger2-triplets 99.1/98.7, verdict-blocks 59.8/65.6). No macro over signature classes or lowest held-out class was found. Per-seed L2 values are in tab:seeds, and per-seed ladder values exist in the B-F-*-s<k> summaries.
  - note: Partly available but not wired.
- **line 2026** `Verdict only           & \ph{tbd} & -- & \ph{tbd}`
  - evidence: tab:budget (lines 2026-2029) has no make_tables markers. The values exist in docs/ANALYSIS_B.md s.7 and meta.json. Examples: verdict-triplets-s0 13,094,434 tokens, 938 steps; ledger2-triplets-s0 30,000 reader + 30,000 judge targets, 13,162,612 tokens; summary2-triplets-s0 12,007,777 tokens; rationale-triplets-s0 16,138,949 tokens.
  - note: Data available but not wired; the rows do not name a corpus. Unique cases are only partly recorded (pretok_stats reader_units, unique_judge_pairs).
- **line 2040** `generated-program verifier, \ph{1} pass, \ph{540} tokens and one execution`
  - evidence: C-TF-genprog: RUN_MATRIX_C says 'running', docs/RESULTS_C.md says 'not run', and it is not in results_git. D-RES has no genprog entry.
- **line 2041** `GenPRM-style verifier, \ph{1} pass, \ph{500} tokens and one execution`
  - evidence: B-TR-genprm-s0..s2 hold only CLAIMED_B (no DONE). D-RES has no entry.
- **line 2042** `closed judge with ledger prompt, \ph{1} API call and \ph{210} tokens, about \ph{60} times the list price of the backbone per claim`
  - evidence: C-REF-closed-ledger is blocked on an API key (RUN_MATRIX_C, COMPUTE REQUEST #1). RUN_MATRIX_D D-RES: 'API rows wait for C'.
  - note: The prompted-ledger pipeline makes a reader call and a judge call (DECISIONS_C, 3 Oct), so '1 API call' needs checking once it runs.
- **line 2055** `and \ph{63.5}\% with \method{}.`
  - evidence: D-RL-ledger2-triplets-s0 and -blocks-s0 have not started (DECISIONS_D, 3 Oct; STATE_D). RESULTS_SUMMARY G1: 'not run'.
  - note: The outcome and reference-graph rewards already reach 97-98%, so the implied 'Ledger-RM highest' (G1) needs more than that.

## 5. First flagged, found to hold on the second check (9)


### Rule triplets, external tiers, diagnostics, method

- **line 390** `\emph{Rule-side edits} keep the case and change only the applicability clause of the rule`
  - results: The sentence at paper/latex_v13/main.tex lines 390-395 contains no \res keys. the first check read the counts correctly: data/xr_v1/test/MANIFEST.json gives by_dimension currency 100, inclusivity 100, subject 100, window 100. Its conclusion that inclusivity items do not edit the applicability clause goes against the repository's own definitions: (1) selrm/xr.py, docstring lines 1-9: "Rule-side items (xr_v1): the c...
  - note: No measured result or repository fact contradicts the sentence. The code, the DECISIONS_A row and the paper's own appendix all call the inclusivity edit a change to the applicability clause. The objection is about terminology, and it rests on one tension inside the paper: line 343 defines the applicability predicate as "which mentions it counts", and lines 351-353 list threshold inclusivity as a separate fixed pro...

### Experimental setup; audit of reward signals

- **line 706** `Primary endpoints are triplet accuracy on L2 and MedEinst reversal of the rule-only model`
  - results: The sentence makes two claims, and the repository supports both.  (1) The endpoints. paper/latex_v13/main.tex lines 1220-1222 (App. A) say: "Primary endpoints. Triplet accuracy on L2 (rendered text, rule stated) and reversal on MedEinst test pairs for the model trained on rule triplets only." Lines 1229-1232 then add comparison (6) on TrialGPT as an extra primary comparison, "Added before any external result was s...
  - note: No measured result or repository fact contradicts the sentence. It names App. A's two primary endpoints and the Holm count, which prints 7 and matches the 7 rows of tables/primary.tex. the first check read "two of the seven comparisons use TrialGPT macro-F1" as "the endpoint list is wrong". The sentence never says all seven comparisons are on those two endpoints, and App. A deliberately lists (6) as an added compa...

### What the judge uses

- **line 1019** `On the same items, \ph{tbd} errors of the full`
  - results: Context, main.tex lines 1018-1022: "With program-supplied ledgers the judge solves \res{run/B-AE-oracle-ledger/L2/all/TA}% of L2 triplets. On the same items, \ph{tbd} errors of the full model are rescued by the program-supplied ledger, \ph{tbd} correct judgments are broken and \ph{tbd} errors are unchanged. The first number bounds what better extraction could recover; it does not assign every error to the reader."...
  - note: the first check number is right: 12 rescued, and I recomputed it myself. But this is not a contradiction. The sentence gives no value, only \ph{tbd}, so there is no direction, significance or number for the result to disagree with. the first check own note says the sentence is supported.  The measured result fits the sentence's framing. The 12 rescued triplets are what perfect extraction would recover. The 4 tripl...
- **line 1020** `model are rescued by the program-supplied ledger, \ph{tbd} correct judgments are`
  - results: The sentence, paper/latex_v13/main.tex lines 1019-1021: "On the same items, \ph{tbd} errors of the full model are rescued by the program-supplied ledger, \ph{tbd} correct judgments are broken and \ph{tbd} errors are unchanged." All three slots are literally \ph{tbd}, so the sentence states no count that a result could contradict.  Keys in tables/numbers.json: - run/B-AE-oracle-ledger/L2/all/TA = 99.8 - run/B-F-led...
  - note: Refuted as a contradiction. The draft only says "tbd", so the measured 0 fits the sentence ("0 correct judgments are broken") rather than disagreeing with it. the first check point is really that the placeholder can now be filled. The right status is consistent, or "fillable", not contradicted.  The values to fill, from ANALYSIS_B section 3 (seed 0, test_L2, triplets): 12 rescued, 0 broken, 4 unchanged, out of 200...
- **line 1021** `broken and \ph{tbd} errors are unchanged.`
  - results: Context, main.tex lines 1018-1022: "With program-supplied ledgers the judge solves \res{run/B-AE-oracle-ledger/L2/all/TA}% of L2 triplets. On the same items, \ph{tbd} errors of the full model are rescued by the program-supplied ledger, \ph{tbd} correct judgments are broken and \ph{tbd} errors are unchanged." The quoted placeholder is the third one, the count of triplets unsolved with either ledger.  Key in the par...
  - note: This is not a contradiction. It is an unfilled placeholder whose result now exists. the first check evidence is right (neither = 4; I recomputed it from the raw scores), but \ph{tbd} asserts no value. The fix is a fill-in: rescued 12, broken 0, unchanged 4 (seed 0, test_L2, B-AE-oracle-ledger against B-F-ledger2-triplets-s0).  Under the house rules (never type a number), the counts first need a summary field and \...
- **line 1040** `\texttt{subject}, \texttt{status} or \texttt{time} in a correct ledger changes the verdict as the program prescribes in \res{run/B-AE-field-edit/L2/top/agreement}\% of cases`
  - results: paper/latex_v13/main.tex 1038-1042, verbatim: "Changing \texttt{subject}, \texttt{status} or \texttt{time} in a correct ledger changes the verdict as the program prescribes in \res{run/B-AE-field-edit/L2/top/agreement}\% of cases". tables/numbers.json line 210: that key has number null and value "\ph{tbd}". The swap key on line 214 is also null. So the sentence prints "tbd%" for both measurements.  What the run me...
  - note: the first check read the evidence correctly, but the sentence does not assert anything the evidence contradicts. In v13 both values print tbd. The sentence states no number, direction or significance, and it does not say that edits are followed. Its description of the procedure matches ANALYSIS_B sec. 9: one subject, status or time field is edited in a correct ledger, and the judge's verdict is compared with the p...
- **line 1042** `ledger of another case the judge returns the verdict that ledger implies in \res{run/B-AE-field-swap/L2/top/agreement}\%`
  - results: Context (main.tex 1038-1043): "...given the ledger of another case the judge returns the verdict that ledger implies in \res{run/B-AE-field-swap/L2/top/agreement}\% (Appendix~\ref{app:ledger})." In tables/numbers.json (line 214) this key is {"number": null, "value": "\ph{tbd}"}, so the draft prints "tbd%" and states no number. The measured result exists. results_git/B-AE-field-swap/summary_rule_v1~test_L2~swap.jso...
  - note: No measured result disagrees with the sentence. It gives no value of its own (it prints tbd), and the measured 99.88% (99.9% once rounded) supports what it says: the judge follows the swapped-in ledger. the first check own evidence and note say the same thing. The problem is a broken key, not a contradiction, so the status of this sentence should be 'consistent' (99.88%, n 29,136) once make_tables maps the ~swap s...

### Candidate selection, conclusion, limitations

- **line 1179** `the frozen version followed an earlier one whose failure we describe in Appendix~\ref{app:history}.`
  - results: The sentence (main.tex lines 1178-1181) has no \res keys. It makes two claims, and both hold as written.  1. "The frozen version followed an earlier one." This is consistent with the records. rule_v1 was frozen at selrm@e40789b, "Fri Oct 2 03:50:32 2026 -0700 Freeze rule_v1 ...". Two generators came before it: the pilot generator at selrm@a6db79d (00:57:25, selrm/mini_engine.py line 1: "Minimal triplet generator f...
  - note: The right status for this sentence is 'pending' or placeholder-dependent, not 'contradicted'. The failure it points to rests on two placeholders: the appendix's \ph{59.7} (line 2083) and the author note "\ph{[Authors: write this from your own records.]}" (line 2079). No file holds either result and no run is planned for them; the only planned work is the timeline.  Two wording caveats for the authors, neither a me...

### App. F (diagnostics)

- **line 1728** `we also report, per system, the share of base and near-miss pairs with the same decision, the share with both decisions correct, and near-miss correctness given a correct base`
  - results: The sentence (paper/latex_v13/main.tex, lines 1727-1731) has no \res keys, and tables/numbers.json has no near-miss-decision (nmt) keys, 0 matches.  What exists now: - tables/kinds.tex, lines 8-10, which is the same as main.tex lines 1749-1751, gives the three quantities for one system only, '\method{} triplets', by kind (thr./neg./num./subj./time):   - SameDecision: 100.0 / 99.1 / 100.0 / 98.4 / 99.8   - BothCorr...
  - note: Not a contradiction. The sentence says these quantities are reported per system. Measured values exist and are printed for the headline system (Ledger-RM triplets). For the other three systems in tab:kinds they have not been generated yet, and the caption marks them 'to be reported per system'. The right status for the per-system part is 'pending': fixing it means extending t_kinds to all four systems. The data ex...

