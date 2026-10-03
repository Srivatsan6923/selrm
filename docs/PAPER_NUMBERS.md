# Numbers in the paper: what is wired to results and what is not

Generated on 2026-10-03 when the v13 prose and captions were wired to result keys
(`\res{key}`, docs/RESULT_KEYS.md). Line numbers refer to `paper/latex_v13/main.tex` at the commit
that adds this file. Each mapping was proposed per section and checked by two independent reviewers
(one for meaning, one for values); a mapping was applied only if neither rejected it.

## Summary

- Numbers replaced by keys: 185 (83 typed measured values, 102 red placeholders).
- Of the 58 distinct keys behind typed measured values, the value printed in v13 differs from the result file in one case: the bag-of-words scorer's triplet accuracy (v13 7.1, results/A-D14-bag_of_words 7.0). Three more differ in form only ('eight' is now 8; the range '92--93' is now two keys).
- Mappings rejected by a reviewer (left as placeholders): 4.
- Numbers left as typed or as placeholders, by kind: 317 (below).

Whenever `scripts/update_paper.py` runs, it lists every sentence whose keyed numbers moved by more than one
point since the last update; such sentences must be re-read, because the prose around a number is not
regenerated (e.g. 'at seed 0', 'close to', 'level with').

## Rejected mappings (authors: make the sentence say what it measures)

- line 830 `\ph{tbd}`: rejected: The run is right: B-AB-probe-rw is Table 9 '\ \ + probe re-weighting' under '- near-misses', i.e. the ledger on blocks with probe weights. But the sentence names no metric. Table 9 reports Rev/Hold/TA/MR/ME, and this paragraph's topic (over-triggering) could just as well mean Hold. As proposed it would also print a bare number with no \%. Leave the \ph{tbd} until the authors write the metric. For 'a triplet accuracy of \ph{tbd}\%' the exact key is run/B-AB-probe-rw/L2/all/TA.
- line 951 `\ph{66.8}`: rejected: The system is ambiguous, so do not map yet. The v10 placeholder 66.8 is the 'rule triplets + clinical pairs' row (clinical pairs only was 62.4). But the sentence says 'Trained on clinical pairs', which is the row name of B-TR-clinonly; line 1088 writes 'trained on rule triplets and clinical pairs' when it means tripclin. The held-out counterpart in the same sentence (line 953) is B-DIS, which RUN_MATRIX_B describes as 'ledger2 on clinical pairs' with data C-CL-clinpairs only, i.e. clinonly-style. Mapping to tripclin would set a tripclin in-distribution number against a clinonly-style held-out one. The authors should name the row in the prose, then use run/B-TR-clinonly/clin_v1:medeinst_test/top/Reversal or run/B-TR-tripclin/clin_v1:medeinst_test/top/Reversal, with B-DIS trained the same way.
- line 1011 `\ph{tbd}`: rejected: The set is ambiguous and the value would likely be misread. In v13 this clause sits inside 'Transfer is the other test of the fields: 38.2% against 44.8% on MedEinst zero-shot ..., and a reader trained to write the bit without fields reaches X%', so a reader will take X as MedEinst reversal. v10 (a separate sentence, 'They also matter as supervision', where 63.0 is that row's TA) and REVIEW_HISTORY ('tests the fields as reader supervision') point to L2 TA instead. Mapping L2 TA here would print a rule-tier number in a MedEinst sentence. The authors should either add 'on L2' (then run/B-AB-bitonly-reader/L2/all/TA) or mean transfer (then run/B-AB-bitonly-reader/clin_v1:medeinst_test/top/Reversal; the seed-0 adapter is kept).
- line 1475 `\ph{tbd} items`: rejected: The sentence gives the size of the xr_v1 item set. That is a construction count of A's dataset, parallel to 'L2 has 2,000 triplets' (1421), the challenge_v1 group count (1478) and the ec_v1 criteria/trial counts (1494), all of which are in the leave list. Rule 4 covers dataset sizes, so this should be left too. The key measures something else: how many items B-F-ledger2-triplets was scored on, averaged over that run's seeds. It equals the set size only if every seed scored every item. The run is also an arbitrary choice: the sentence is about the three shortcut scorers, not Ledger-RM. The grammar has no data-side key for xr_v1 (a15 covers only rule_v1 sets). Move this placeholder to leave as a dataset size.

## Missed by the proposers (found by a reviewer)

- line 924 (Sec. 7.3 transfer, 7.4 what the judge uses (incl. Figure 3)): "both triplet-trained models solve all of them" -> 'All of them' is a number written as words (100%). It rests on run/B-F-ledger2-triplets/L3alt/all/TA and run/B-F-verdict-triplets/L3alt/all/TA, both 100.0 at seed 0. Seeds 1-4 are running and could pull either below 100. Either check min/run/B-F-ledger2-triplets/L3alt/all/TA|run/B-F-verdict-triplets/L3alt/all/TA = 100.0 at freeze, or have the authors reword to 'solve \res{run/B-F-ledger2-triplets/L3alt/all/TA}\% and \res{run/B-F-verdict-triplets/L3alt/all/TA}\%'.

## Quoted from other papers or datasets (stay as typed; checked in the citation kit) (24)

| line | text | note |
|---|---|---|
| 156 | `85.6\%` | Quoted from hou2026medpic (clinical LLMs mention a changed patient fact). |
| 157 | `69.8\%` | Quoted from hou2026medpic (original medication choice kept). |
| 295 | `14 error types` | Fact about cited work MedPRMBench (wu2026medprmbench), its number of injected error types; no result file of ours produces it. |
| 296 | `seven QA sources` | Fact about cited work MedPRMBench (wu2026medprmbench), its number of source QA datasets, written as a word; external. |
| 307 | `once per problem` | Describes how often the cited EVPV method (evpv2026) extracts visual facts; a property of cited work, not a result. |
| 484 | `1{,}015 patient--criterion pairs` | Size of the TrialGPT criterion-level annotation set (cited dataset, jin2024trialgpt). The authors should check it against the released file that C inspects in FINAL_TASKS_C P0.1. |
| 484 | `from 53 patient summaries` | Number of patients in the TrialGPT annotations (cited dataset). This is not a result. |
| 493 | `(5,383 test` | Size of the MedEinst test split, quoted from the benchmark (chen2026medeinst; PAPER_CONTEXT section 6). A run's n_pairs in summary_clin_v1~medeinst_test.json is the number of pairs scored, which is a different quantity. |
| 494 | `pairs; 10,689 reference pairs)` | Size of the MedEinst reference split, quoted from the benchmark. |
| 1131 | `\ph{1{,}500}` | The number of generated pairs that the MedEinst authors report as physician-reviewed. It is quoted from the cited benchmark paper and no run produces it. The authors check it against that paper and write it as plain text. |
| 1345 | `in three steps` | Construction steps taken from MedGuideX (Shen et al., cited on line 1346). This describes the method, not a result. |
| 1490 | `SemEval-2024` | Name of the external shared task. |
| 1491 | `Task~2` | Name of the external shared task. |
| 1509 | `1{,}015 patient--criterion annotations over 53 patient` | Sizes of the released TrialGPT annotation file (cited dataset). |
| 1510 | `\ph{103} trials` | Trial count in the released TrialGPT file. Check it against the release (C lists the columns under FINAL_TASKS_C P0.1) and type it; no result field. |
| 1511 | `GPT-4 outputs` | Model name in the external dataset. |
| 1513 | `GPT-4 field` | Model name in the external dataset. |
| 1538 | `of 49)` | Disease count of DDXPlus/MedEinst. |
| 1550 | `six subject areas` | Fact about the CareQA dataset. |
| 1555 | `100 questions` | CondMedQA size (cited work). |
| 1558 | `30 were reviewed` | Review count reported by the CondMedQA authors. |
| 1568 | `one correct and four incorrect answers` | Structure of the EHRNote-ChatQA dataset. |
| 1569 | `Two patterns` | Distractor patterns of the external dataset. |
| 1689 | `harkema2009context` | Citation key carrying the cited work's year, as do hewitt2019control and elazar2021amnesic on lines 1842-1843. Not results. |

## Settings and design constants (stay as typed; must match configs and run manifests) (94)

| line | text | note |
|---|---|---|
| 137 | `$>0$` | Fig. 1: required sign of d, part of the test definition (also $<0$ on line 138 and $>0$ on line 139). |
| 143 | `four generated cases` | Fig. 1 caption: base, decisive edit, near-miss and missing case. Fixed by the design. |
| 175 | `all six instances` | 3 cases x 2 claims, fixed by the design. |
| 319 | `under one budget` | Design statement: all supervision and representation conditions are compared at the same training budget. Not a measured quantity. |
| 391 | `within the last six months` | Example applicability clause quoted from a rule text. This is not a result. |
| 394 | `two rules with three cases and is solved only if all six judgments are right` | Item design of xr_v1 (FINAL_TASKS_A P0.2: two rules x three cases, solved only if all six are right). |
| 397 | `two extractors recover the state` | Acceptance criterion of rewrite_v1 (FINAL_TASKS_A P0.6). |
| 445 | `\ph{5}\% false rejection of supported claims on development data` | This is the fixed operating point of the MR metric (frozen decision: 'MR at 5% false rejection (threshold from dev)'; RESULT_KEYS row 'MR at 5% FR'). It is not a measured value. Each system's measured FR (top-level FR in summary_rule_v1~missing.json) is a different quantity, and C-M0 has not compute |
| 494 | `\emph{Key pairs} are two exam questions whose` | Definition of a key pair (two questions). |
| 496 | `so the four labels follow from the keys` | Two questions x two candidate answers, by construction. |
| 498 | `keep each question in at most one pair. Two exam questions are` | Mining constraint and definition for key pairs. |
| 625 | `four kinds of novelty; L0 (626), L1 (627), \textbf{L2} (628), \textbf{L3-alt} (630), L2 (7` | Test-level names and their number are part of the design, not results. |
| 639 | `rank 64 for one epoch` | LoRA rank and epoch count are training settings, recorded in each run's meta.json train.hp. |
| 640 | `60{,}000 records` | Corpus size is a design setting. |
| 640 | `Four corpora (640); half of the groups (649)` | Design counts written as words. |
| 641 | `15\% each` | The share of missing-input and presentation records is a generator parameter. A-D15 datasets.<set>.record_share holds the realised shares if a measured value is ever wanted. |
| 656 | `Two one-stage formats (656); Three two-stage formats (658); A sixth variant (664); the fiv` | Counts of representations in the design, written as words. |
| 693 | `\ph{32}` | A readout setting, and an outdated one. Under CLAUDE.md and PAPER_CONTEXT section 8, API models without log-probabilities are scored with the two-order choice prompt, not 32 sampled verdicts. The clause needs rewriting; no run produces a sample count. |
| 750 | `\ph{5}` | Operating point of MR: 5% false rejection, threshold set on dev_missing (CLAUDE.md frozen decision). Not a result: drop the \ph wrapper and print 5. The realised FR on the test set (run/<prefix>/missing/top/FR) is a different quantity. |
| 804 | `60k records, one epoch` | Training settings: 60,000 records per corpus, one epoch. |
| 816 | `in half of the` | Corpus design: in the triplets corpus, near-misses replace half of the base cases (DATA_A.md: 7 of each 14 groups). A number word, not a result. |
| 867 | `\setlength{\tabcolsep}{4.2pt}` | Table layout setting, not a result. |
| 913 | `its gap to 100` | The 100% ceiling; not a result. |
| 971 | `width=0.56\linewidth, height=3.7cm` | Figure layout. Lines 983-984 (xshift=9mm, width, height) are the same kind of setting. |
| 972 | `xtick={16,32,64,128,256} / xticklabels={16,32,64,128,256}` | Axis ticks. fig-div plots x values 16, 32, 63, 64, 128 and 223, so the 256 tick lies beyond the data. |
| 975 | `ymin=36, ymax=90` | Axis range set for the v10 placeholder curves (maximum 78.6). Measured ledger runs reach about 99 on L2 (Table main: 99.2), so a measured curve would be clipped at 90. Set the range from the data (for example ymax=100) once B-DIV lands. |
| 985 | `xtick={1,4,16,64}, xticklabels={1,4,16,64}` | N grid; matches the D-SELN fields N1..N64. |
| 987 | `ymin=48, ymax=88` | Axis range from the v10 placeholder curves. Reset it from the D-SELN data. |
| 998 | `\ph{16} fixed rules` | Number of fixed base rules in the diversity design (A-D10). A-D15 confirms that div_base_16 and every div_patients_* corpus have n_rules = 16. Either remove the \ph by hand or use the key \res{a15/datasets.rule_v1/div_base_16.n_rules@int}, which already resolves to 16. |
| 1050 | `the 4B model` | Backbone size: unsloth/Qwen3.5-4B (B-BB rows). |
| 1052 | `9B model; the other cells are not run` | Backbone size: Qwen3.5-9B. The phrase 'the other cells are not run' will be wrong once B-BB-qwen3.5-4b-{verdict-triplets, ledger2-blocks, ledger2-triplets}-s0 (queued, P1) finish. |
| 1054 | `15\% of such records` | Share of missing-input records in each corpus (A-D15 record_share.missing = 0.15). The claim around it, that MR is at the ceiling (also in the line 909 caption), has no keyed number yet. run/<p>/missing/top/MR is tbd in every row because summary_rule_v1~missing.json has no MR field until C's MR metr |
| 1086 | `\ph{16}` | Samples per question in the selection pools, a setting of D-POOL-medqa/careqa (RUN_MATRIX_D: 16 samples/question; FINAL_TASKS_D P1). It is not a result, and no summary_sel field records it. The authors write it as plain 16 once the pools are generated with that setting. |
| 1098 | `margin of one point` | Non-inferiority margin, a threshold of the analysis (review item 25) and not a result. |
| 1205 | `seed 0` | Seed index in the draft-status paragraph, which sits inside \ifplaceholders and is removed in the final build. It names runs; it is not a value. |
| 1234 | `Status at seed 0.` | Seed index; not a value. |
| 1244 | `95\% CI` | Interval level in the column header of tab:primary. The header is outside the generated table body. |
| 1297 | `one of four questions` | Number of validity questions, i.e. the rows of tab:validity. This is the authors' framing, not a result. |
| 1313 | `Four validity questions` | Caption count of the rows of tab:validity; not a result. |
| 1384 | `\ph{3} folds` | Number of folds, a split design setting (data/rule_v1/FOLDS.json; A-D15 has folds 1-3). No numeric key exists. Remove the \ph wrapper once confirmed, or the final build fails. |
| 1384 | `\ph{5} of` | Signature classes held out per fold, a split design setting (each fold's l2_classes in A-D15 lists 5). It is stored as a list, so there is no numeric key. Remove the \ph wrapper once confirmed. |
| 1391 | `\ph{6} templates, \ph{4} for training and \ph{2} for test` | Generator setting: templates come in blocks of 6, with indices 0-3 for training and 4-5 for test (selrm/phrases.py). A-D15 has only totals (templates_train 1032, templates_test 516, shared 0). Remove the \ph wrappers once confirmed. |
| 1395 | `one or two thresholds` | How L3-alt is constructed; not a result. |
| 1418 | `$h_k(x)=0$` | Part of the definition of the concept-named feature (0/1 values); not a result. |
| 1419 | `$h_k(\xf)=h_k(\xn)=1$ (or $h_k\equiv 1$` | Part of the definition of the concept-named feature; not a result. |
| 1420 | `60{,}000` | Corpus-size setting, listed as a design constant in the task. The built corpora have 60,000-60,012 records (a15/datasets.rule_v1/train_*.n_records). |
| 1421 | `2{,}000 triplets` | L2 size, fixed by design. It matches a15/datasets.rule_v1/test_L2.n_groups@int = 2{,}000 (checked with --key), if the lead prefers to bind it. |
| 1421 | `development set 300` | Dev size, fixed by design. It matches a15/datasets.rule_v1/dev.n_groups@int = 300 (checked with --key). |
| 1442 | `Numeric \ph{40}\%` | This is the generator's near-miss mixture: five kinds drawn equally. L2 has 400 each of numeric, boundary, subject, negation and time (a15/datasets.rule_v1/test_L2.nm_kind.*), so numeric including threshold values = 40%. The key grammar has no ratio, so type it as a design value. |
| 1442 | `(of which at the threshold \ph{tbd})` | Values at the threshold are the boundary kind, half of the numeric near-misses: 400 of 800 in L2, or 20% of all. Design value; no ratio key. |
| 1442 | `other subject \ph{20}\%` | Subject kind: 400 of 2,000 in L2. Design share. |
| 1443 | `absent status \ph{20}\%` | Negation kind: 400 of 2,000 in L2. Design share. |
| 1443 | `time outside the predicate \ph{20}\%` | Time kind: 400 of 2,000 in L2. Design share. |
| 1457 | ```within six months''` | Example rule wording, not a result. |
| 1462 | `15 or more unrelated lines` | Definition of the long tier (15 or more filler lines). |
| 1470 | `two rules` | Item construction (xr_v1). |
| 1471 | `three cases` | Item construction (xr_v1). |
| 1473 | `all six judgments` | Solving criterion for an item (2 rules x 3 cases). |
| 1475 | `\ph{tbd} phrasings per clause` | Number of phrasings per applicability clause in A's xr_v1 generator (FINAL_TASKS_A P0.2, 'several phrasings'). It comes from A's xr_v1 manifest; no result field. |
| 1480 | `two extractors` | Acceptance rule of the rewritten tier (EXTRACTORS in scripts/rewrite_tier.py). |
| 1519 | `(\ph{tbd} patients)` | Size of the patient-disjoint development portion, fixed in C's docs/TRIALGPT_PROTOCOL.md before scoring; no result field. |
| 1535 | `\ph{500} pairs` | Audit sample size. |
| 1535 | `of \ph{100} pairs` | Size of the authors' inspection sample. |
| 1538 | `(\ph{12} of` | Number of test diseases in the disease-held-out MedEinst split, part of the split definition for B-DIS and C-CL-clinpairs; no result field. |
| 1547 | `all four cells` | 2 questions x 2 claims. |
| 1664 | `\setlength{\tabcolsep}{4pt}` | Table layout setting; likewise 3.2pt on line 1701 and 3pt on line 1728. Not results. |
| 1755 | `y\in\{+1,-1\}` | Constants in the definitions of the shift analysis (also d_0<0 and d_0=0 on lines 1756-1771). Not results. |
| 1787 | `width=0.60\columnwidth, height=3.5cm` | pgfplots layout of the left axis on lines 1787-1796 (xmin 0, xmax 100, bar width, ytick 1-4, ymin 0.4, ymax 4.6, legend position and columns, column sep, legend image size, grid shade). Not results. |
| 1802 | `xshift=9mm` | Layout of the right axis on lines 1802-1808 (width 0.42, height 3.5cm, bar width, ymin 0, ymax 1.3, ytick 0/0.5/1, yshift, enlarge x limits 0.2). Not results. |
| 1825 | `\ph{32}` | Sample count of v10's sampled readout for API judges: a setting, not a result. The frozen protocol is now log-probabilities or the two-order choice (CLAUDE.md), so this sentence must be rewritten (PAPER_CONTEXT.md section 8). C-DG-noise's own sample count goes in from C's config. |
| 1825 | `\ph{1.0}` | Sampling temperature of the same readout: a setting, not a result. Same rewrite applies. |
| 1826 | `\ph{0.09}` | Standard-error bound implied by the sample count (sqrt(0.25/32) = 0.088), not a measured result. Rewrite it with the protocol. |
| 1884 | `seed 0` | Status label in the ablation caption ('black: measured, seed 0'), not a result. Generated cells pool seeds, so update the label once seeds 1+ exist. |
| 1922 | `seed 0` | Same status label in the ladder caption. The readapply numbers in this caption are now keyed with the seed mean, so revise 'seed 0' when more seeds land. |
| 1937 | `95\% CI` | Interval level in the seeds-table header; a bootstrap design setting. |
| 1937 | `s0 & s1 & s2 & s3 & s4` | Seed indices used as column labels, not results. |
| 1980 | `LoRA rank 64` | Setting. meta.json train.hp.lora_r = 64 in every B-F run. |
| 1980 | `batch size 64` | Setting. meta.json train.hp.batch = 64. |
| 1980 | `one epoch` | Setting. meta.json train.hp.epochs = 1. |
| 1980 | `60{,}000 records` | Corpus size. meta.json pretok_stats.n = 60000. |
| 1981 | `\ph{1e-4}` | Learning-rate setting. meta.json train.hp.lr = 0.0001 in every B-F run, so 1e-4 is confirmed; the authors can remove the \ph by hand (no key needed). |
| 1981 | `$\lambda=\ph{1.0}$` | Ratio of judge to reader examples in the corpus (method section). meta.json pretok_stats.parts is reader 30000 / judge 30000 in B-F-ledger2-{blocks,triplets}-s0 and B-F-summary2-triplets-s0, so the ratio is 1.0. A setting, not a result. |
| 1981 | `$p=\ph{0.3}$` | Ledger resampling probability. scripts/pretok.py defaults resample_p to 0.3 for two-stage formats, and the train_key of the B-F ledger2 and summary2 runs contains '__p0.3__'. A setting. |
| 1983 | `\ph{1}:\ph{1}` | Mixing ratio of rule triplets to clinical pairs (B-TR-tripclin: 'rule triplets + clinical pairs 1:1'). A setting. |
| 2008 | `\ph{1} pass and \ph{1} generated token` | Properties of the verdict-only scoring interface (one forward pass, log-odds at the answer position). The authors confirm and remove the \ph. |
| 2009 | `\ph{2} passes` | Reader generation plus judge scoring; a property of the interface. |
| 2010 | `\ph{1} pass` | Generated-program verifier: one generation pass (a property of the interface). |
| 2011 | `\ph{1} pass` | GenPRM-style verifier: one generation pass. |
| 2012 | `\ph{1} API call` | Interface fact for the authors to confirm. The prompted ledger has a reader call and a judge call, and C's protocol asks both orders when no log-probabilities are returned, so the true count may be more than 1. Check C-REF-closed-ledger's meta. |
| 2018 | `\ph{8}` | Rollouts per prompt (GRPO group size); a D-RL setting not yet recorded in configs. |
| 2019 | `\ph{2000} steps` | GRPO steps; a D-RL setting. |
| 2021 | `\ph{64}-prompt subset` | Size of the overfit-check subset; a setting. |
| 2038 | `$N=64$` | Pool size of the selection-pressure experiment (D-SELN). |
| 2065 | `\ph{tbd} sampled failures` | Sample size of the error analysis. scripts/error_sheet.py draws 200 failures (8 per system x near-miss kind: 5 systems x 5 kinds). The authors write it in. |

## Counts and facts the authors write (dataset sizes, numbers of rules, seeds, reviewers) (35)

| line | text | note |
|---|---|---|
| 95 | `\ph{13}` | Number of audited reward signals (rows of Table 2). The authors write this count; no key exists. Keep it equal to the number of TA keys in the min/max range on line 96. |
| 192 | `\ph{13}` | Same count of audited signals as line 95. The authors write it. |
| 694 | `\ph{5} seeds` | The authors write the seed count. Plan: seeds 0-2 for the core cells (FINAL_TASKS_B P0.3) and seeds 3-4 in P1, so 5 holds only for the core cells. Per-cell counts are available as run/<prefix>/L2/all/TA/n. |
| 805 | `(seed 0)` | Seed index, not a value. The caption's mapped keys are seed means with seed-pooled intervals, equal to seed 0 today. When seeds 1-2 land, the authors must reword the caption (or move point values to /s0). |
| 813 | `At seed 0` | Seed index. The mapped keys are seed means, equal to seed 0 today. Reword when seeds are pooled. |
| 833 | `At seed 0` | Seed index. The mapped keys are seed means, equal to seed 0 today. Reword when seeds are pooled. |
| 849 | `At seed 0` | Seed index. The mapped keys are seed means, equal to seed 0 today. Reword when seeds are pooled. |
| 907 | `seed 0` | States which seed the black cells come from. Once seeds 1-2 land, cells show the mean ± s.d. over seeds, so the authors must rewrite this sentence. Also out of date: 'external columns keep earlier placeholder values for MedEinst', since every external cell is now \ph{tbd}. |
| 911 | `The two verifier rows` | Counts table rows (generated-program verifier, GenPRM-style verifier); not a result. |
| 930 | `the three tests the renderer does not determine` | Counts the tests: xr_v1, challenge_v1, ec_v1. Update by hand if A does not build one of them. |
| 1111 | `two directions` | A conceptual count (under-reaction and over-triggering), not a measured quantity. |
| 1111 | `The remedy has two` | 'two parts': the structure of the method (near-miss training plus the ledger), not a measured quantity. |
| 1138 | `one condition of one rule` | Describes the design of the generated test, not an experimental result. |
| 1162 | `process reward for one` | 'one policy': the selection design uses one frozen Qwen3.5-9B policy (D-POOL-*). A count the authors write. |
| 1181 | `one seed` | Number of seeds behind the draft's values: a count the authors write. It becomes false once the multi-seed runs land (B factorial plans 5 seeds; key cells need at least 3). One system's seed count is run/<prefix>/<set>/all/TA/n, but this sentence covers the whole draft, so no single key fits. The au |
| 1181 | `and one` | 'one backbone' (continues on l.1182): a count the authors write. Other backbones are planned (B-BB-*, Sec. 7.4), so the authors must revise it once those rows exist. |
| 1324 | `\ph{tbd} of \ph{tbd} were corrected or dropped` | Outcome of the second-author check of source-derived formalisations. No run or summary field records it, so the authors write the count. |
| 1332 | `450 rendered groups` | Black number with no key. It is the size of A's two pre-freeze audit rounds (RUN_MATRIX_A A-D15 notes, docs/STATE_A.md). results/A-D15/summary.json has no field for it. It is a process count the authors state. |
| 1333 | `\ph{[state who reviewed them and what they were asked]}` | Text placeholder, not a number. A's audit (FINAL_TASKS_A P0.1) records who reviewed the 450 groups (people or model agents) and what they checked. |
| 1338 | `read \ph{tbd} groups` | Number of groups the authors read (H1 in HUMAN_TASKS.md: 75 each, 300 planned). It is recorded in audit/fidelity_<name>.csv, which is not a key source. |
| 1340 | `found \ph{tbd}` | Errors found in the authors' H1 read. audit/fidelity_<name>.csv is not read by make_tables.py, and no run summarises it. |
| 1397 | `near-miss kinds are \ph{tbd}` | A list of near-miss kind names, not a number. A-D15 datasets.rule_v1/test_L3alt.nm_kind = boundary 333, numeric 334, time 333 (no negation or subject). FINAL_TASKS_A P0.1 also plans a write-up of L3-alt composition. |
| 1478 | `\ph{tbd} groups written by the authors` | Authors' writing task H2: 4 x 40 = 160 groups, 32 per near-miss kind (FINAL_TASKS_A P0.3). If the lead prefers the scored count, use run/B-F-ledger2-triplets/challenge_v1:test/all/n@int. It equals the written count only if the second-author check drops no group. |
| 1535 | `\ph{97} of` | Result of the authors' manual inspection; no result file. |
| 1748 | `seed 0` | The caption names seed 0, but the generated kinds body averages every finished seed (mean, with s.d.). The authors must update the caption when seeds 1-2 of these four systems land. |
| 1981 | `\ph{[confirm against the run manifest that ledger resampling was used]}` | Author note, not a number. The manifests confirm resampling was used: train_key '...__p0.3__...' and pretok_stats.resample_groups = 795 in B-F-ledger2-blocks-s0, B-F-ledger2-triplets-s0 and B-F-summary2-triplets-s0. The bracket can be deleted. |
| 2018 | `\ph{3} runs` | Number of GRPO runs per reward. RUN_MATRIX_D plans two per reward (D-RL-<reward>-s0 at P1, -s1 at P2), so 3 does not match the plan. Also, RUN_MATRIX_D trains a Qwen3.5-4B policy, while the text says one \bb{} (Qwen3.5-9B) initialisation. |
| 2048 | `\ph{[Authors: write this from your own records.]}` | Author text (HUMAN_TASKS H6: the authors write the development history in their own words). |
| 2048 | `11` | Rule count of the pilot generator (selrm/rules.py has 11 pilot rules). A fact for the authors, not a result. |
| 2049 | `three templates per mention form` | Pilot generator design (selrm/mini_engine.py: 3 templates per form). |
| 2066 | `extraction errors \ph{tbd}` | Count coded by the authors (HUMAN_TASKS H4, audit/errors_<name>.csv); no results/ file. |
| 2066 | `applicability errors \ph{tbd}` | Count coded by the authors (H4); the \ph{tbd} is at the start of line 2067. No results/ file. |
| 2067 | `wording not seen in training \ph{tbd}` | Count coded by the authors (H4); no results/ file. |
| 2067 | `rule misread \ph{tbd}` | Count coded by the authors (H4); no results/ file. |
| 2068 | `other \ph{tbd}` | Count coded by the authors (H4); no results/ file. |

## Placeholders that no planned run produces (remove the sentence, or name the run that will produce it) (72)

| line | text | note |
|---|---|---|
| 347 | `In \ph{23}\% of criteria a past or family finding counts` | Rule-library statistic: the share of criteria whose applicability predicate counts past or family mentions. No result file holds it. results/A-D15/summary.json has only per-rule signature-class counts (cur/ext), not a per-criterion share, and the key grammar has no ratio operator. FINAL_TASKS_A P0.1 |
| 527 | `\ph{3}` | Maximum number of ledger entries per condition. This is a property of the ledger format and the generated data, not a result field. No run-matrix row, FINAL_TASKS item or RESULT_KEYS field records it, and selrm/formats.py sets no cap. To get it, either add a field to the A-D15 summary (max entries i |
| 690 | `\ph{1{,}240}` | Number of MedQA-test key pairs, built by C-CL-keypairs. RESULT_KEYS.md and RESULTS_SCHEMA.md list only Reversal for key-pair summaries; n_pairs is listed only for MedEinst, so no key yields this count. If C writes n_pairs to summary_clin_v1~keypairs_medqa.json, it becomes run/<system prefix>/clin_v1 |
| 691 | `\ph{960}` | Number of CareQA key pairs (C-CL-keypairs). As with MedQA, no documented summary field holds it. If C writes n_pairs to summary_clin_v1~keypairs_careqa.json, it becomes run/<system prefix>/clin_v1:keypairs_careqa/top/n_pairs@int. |
| 762 | `\ph{81.7}` | Macro-F1 of a step-only classifier on the MedPRMBench test split. No run in RUN_MATRIX_{B,C,D} or the FINAL_TASKS files trains or scores such a classifier. MedPRMBench has no public data release (DECISIONS_B, 2 Oct). C-DG-inputabl (P2, conditional on release) is an input ablation of PRM scoring and  |
| 763 | `\ph{41.2}` | Majority-class macro-F1 on the MedPRMBench test split: a property of unreleased data. No planned run and no key (see line 762). |
| 853 | `\ph{tbd} triplets` | Discordant count for p3 (ledger right, prose record wrong). There is no key: cmp/<name> exposes only diff, lo, hi, p, padj and n. B's disagreement table (FINAL_TASKS_B P0.1) goes to docs/ANALYSIS_B.md, which is not an input (RESULT_KEYS.md). To fill it, add both discordant counts to comparisons() in |
| 853 | `the reverse on \ph{tbd}` | The reverse discordant count (prose right, ledger wrong). Same status as the previous entry. |
| 957 | `\ph{11} times the generated tokens` | Ratio of generated tokens, GenPRM-style verifier to Ledger-RM. The key grammar has no ratio. meta.json's eval_generated_tokens covers different eval-set lists per run (B-TR runs: dev, L2, dev_missing, missing, L3alt; key cells: every set). D-RES (tokens per claim per system) defines no fields yet. D |
| 961 | `\ph{81}\% of its near-miss errors` | Needs an error analysis of B-TR-genprm's generated check code (reader_output and check_output in its scores file). No task or summary field plans it. Either plan the analysis with a summary field or drop the sentence. |
| 1014 | `\ph{tbd} errors of the full model are rescued` | The 2x2 transition counts (B-P0.1) go only into docs/ANALYSIS_B.md. Per RESULT_KEYS a doc is not an input, and no summary field exists. B would need to write top-level rescued/broken/unchanged counts into B-AE-oracle-ledger's summary_rule_v1~test_L2.json, keyed as run/B-AE-oracle-ledger/L2/top/rescu |
| 1015 | `\ph{tbd} correct judgments are broken` | Same as line 1014; the field would be 'broken'. |
| 1016 | `\ph{tbd} errors are unchanged` | Same as line 1014; the field would be 'unchanged'. |
| 1097 | `\ph{$-$0.2}` | Lower end of the paired 95% interval of combined minus step check on MedQA. No planned source. COMPARISONS in make_tables.py defines only p1-p6b, and comparisons() handles only rule_v1 sets. summary_sel~*.json specifies only acc, pair_acc, control_acc, trap_acc, n, with no CI95. Producing it needs p |
| 1097 | `\ph{1.6}` | Upper end of the same paired interval (combined minus step check, MedQA). No planned source, for the same reason as the lower end; it would become cmp/<name>/hi. |
| 1320 | `\emph{verbatim source rule} (\ph{tbd})` | Count of rules by provenance class. A's manifest audit (FINAL_TASKS_A P0.1) will classify each rule as verbatim source, simplified source or synthetic. Its outputs (docs/DATA_AUDIT_rule_v1.md, tables/data_stats.json) are not key sources, and no run id is given for them. results/A-D15/summary.json ha |
| 1321 | `\emph{simplified source rule} (\ph{tbd}) or \emph{synthetic} (\ph{tbd})` | Same as line 1320: A's planned provenance classification goes to tables/data_stats.json, which make_tables.py does not read. A-D15's rules_by_source is a different partition (for example, grammar_sampled 250 is not the same as 'synthetic'). |
| 1352 | `at most \ph{2} tokens` | Maximum token difference between a constraint rule's option texts. No script enforces or measures it: there is no rule-validator check and no A-D15 field, and no planned run reports it. A or the authors must verify it. If it is a construction constraint, it becomes a typed design constant; otherwise |
| 1368 | `Distinct program structures (names, constants removed) & \ph{tbd} & \ph{tbd}` | Unmarked table tab:structure (not generated). A plans per-split structure statistics in FINAL_TASKS_A P0.1 (normalised structures, conditions per judgment, depth, mentions, competing mentions, temporal/numeric/exception operations, train and L2). They go to tables/data_stats.json, which make_tables. |
| 1370 | `Conditions needed per judgment (mean; max) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1371 | `Dependency depth (mean; max) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1372 | `Evidence mentions required (mean) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1373 | `Cases with competing mentions of the concept (\%) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1374 | `Judgments with a temporal operation (\%) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1375 | `Judgments with a numeric comparison (\%) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1376 | `Judgments with an exception (\%) & \ph{tbd} & \ph{tbd}` | Same as line 1368: planned only for tables/data_stats.json (A P0.1); there is no run summary field. |
| 1387 | `source documents (\ph{tbd})` | No script computes overlap of source documents. It is also missing from A's planned overlap list (FINAL_TASKS_A P0.1: program, normalised structure, subexpression, template, cue phrase, relative name, base state). |
| 1388 | `parameter-normalised structures (\ph{tbd})` | A plans normalised-structure overlap (FINAL_TASKS_A P0.1), but only for tables/data_stats.json, which is not a key source. A-D15 has only canonical programs, criterion subexpressions and rule texts. |
| 1390 | `underlying states (\ph{tbd})` | A plans base-state overlap (FINAL_TASKS_A P0.1), but only for tables/data_stats.json, which make_tables.py does not read. There is no run summary field. |
| 1394 | `\method{} is \ph{tbd}` | This would be Ledger-RM's TA on L2 rules rendered with training templates and cues. No registered set renders L2 rules with training templates (data/REGISTRY.json), and no run in RUN_MATRIX_A/B/C/D or the FINAL_TASKS files evaluates it. |
| 1406 | `(\ph{tbd} items)` | Number of items affected by defects found after the freeze. A's target-claim check writes violations to data/rule_v1/KNOWN_ISSUES.json (FINAL_TASKS_A P0.1), which is not a key source. No planned run reports results with and without those items. |
| 1414 | `\ph{7.9}\%` | There is no key for the share of proposed flips discarded because a second criterion changed or the claim did not. A-D15 records only one reject rate per set: a15/datasets.<set>.reject_rate, in % of proposed groups (train_triplets 1.14, test_L2 0.0). Every recorded reject is a presentation-edit resa |
| 1416 | `\ph{18.6}\%` | There is no key for the missing-twin rejection share. The rule_v1/missing MANIFEST has no rejects (a15/datasets.rule_v1/missing.reject_rate = null), and DECISIONS_A (2 Oct) says no twin was rejected under the current construction. The sentence needs rewriting. |
| 1437 | `\ph{tbd}\%` | Share of base cases that state the required absence explicitly: no field exists in A-D15 or in any planned summary. A's P0.1 semantics audit writes to docs/DATA_AUDIT_rule_v1.md and tables/data_stats.json, and make_tables.py reads neither. Also, finding base cases never name the concept by construct |
| 1439 | `subset are \ph{tbd}` | No existing or planned slice selects an explicit-absence subset (the slices are nm_kind, tier, family, level and step). |
| 1457 | `& \ph{tbd}` | Count of test triplets with rule-dependent time scope: no field. A's P0.1 requirements table goes to docs/DATA_AUDIT_rule_v1.md and tables/data_stats.json, which make_tables.py does not read. To bind it, A must add the counts to results/A-D15/summary.json. The table also does not say whether it coun |
| 1458 | `& \ph{tbd}` | Competing-mentions count: no field (same reason as line 1457). |
| 1459 | `& \ph{tbd}` | Temporal-selection count: no field. tier=superseded (L2 67, hard 80) covers only part of it: numeric time near-misses, where an older value crosses the threshold and the current one does not, also qualify. So the tier count is a different quantity. |
| 1460 | `& \ph{tbd}` | Count of compositions with an explicit exception: no field. |
| 1461 | `& \ph{tbd}` | Numerical-semantics count: no field. nm_kind=boundary (400 in L2) covers values at a threshold but not units given in the rule. |
| 1494 | `(\ph{tbd} criteria` | Number of registered criteria in ec_v1. It is a dataset count from A's ec_v1 manifest (FINAL_TASKS_A P0.5). The ec_v1 summary uses rule-tier format, where all/n counts triplets, not criteria, so no field gives it. |
| 1494 | `from \ph{tbd}` | Number of trials behind ec_v1: from A's manifest; no result field. |
| 1535 | `\ph{96.2}\%` | Agreement of the found targets, structured evidence vs token diff, on a sample. It belongs to the C-CL-clinpairs data audit, and RESULT_KEYS.md defines no summary field for it. |
| 1548 | `(\ph{38.5}\% kept)` | Keep rate of sampled training ledgers for key pairs (C-CL-clinpairs); no summary field is defined. |
| 1549 | `\ph{55.7}\%` | Critic key-pair reversal by tercile of vignette similarity. Key-pair summaries define only a top-level Reversal (RESULT_KEYS.md); terciles would need slices from C. |
| 1550 | `\ph{44.1}\%` | Same as line 1549: no tercile slices. |
| 1550 | `\ph{33.8}\%` | Same as line 1549: no tercile slices. |
| 1552 | `\ph{4}\% of pairs` | Share of CareQA key pairs from biology and chemistry, a C-CL-keypairs data statistic; no summary field. |
| 1560 | `\ph{41.0}\%` | CondMedQA: C-CL-condmedqa is only a P2 data check. No evaluation run, set name or summary field appears in RESULT_KEYS.md or the run matrices. Per PAPER_CONTEXT section 8, drop the paragraph if no result file exists. |
| 1561 | `\ph{56.0}\%` | CondMedQA, rule-only Ledger-RM: no planned run or field (see line 1560). |
| 1561 | `[\ph{46}, \ph{66}]` | CondMedQA interval: no planned run or field (see line 1560). |
| 1561 | `\ph{80.0}\%` | CondMedQA, closed judge: no planned run or field (see line 1560). |
| 1573 | `\ph{58.0}\%` | EHRNote-ChatQA: C-CL-ehrnote is P3 and blocked on credentialed access, and no evaluation run or summary field is defined. Per PAPER_CONTEXT section 8, drop the paragraph if it is not run. |
| 1574 | `\ph{69.5}\%` | EHRNote-ChatQA, rule-only Ledger-RM: no planned run or field (see line 1573). |
| 1574 | `\ph{77.0}\%` | EHRNote-ChatQA with clinical pairs: no planned run or field (see line 1573). |
| 1621 | `\ph{38.5}\%` | Joint correctness over an original statement and all its interventions. summary_clin_v1~nli4ct.json defines only macroF1, faithfulness and consistency (RESULT_KEYS.md), so C would need to add a field. |
| 1621 | `\ph{47.9}\%` | Joint correctness for rule-only Ledger-RM: no field (see the previous entry). |
| 1646 | `\ph{tbd}\% of prose records` | Share of prose records with a decision word or claim text. B's verdict check (FINAL_TASKS_B P0.1) reports only in docs/ANALYSIS_B.md, and RESULT_KEYS.md says a number that exists only in a doc is not an input. No run id or summary field holds it. |
| 1646 | `\ph{tbd}\% of ledgers` | Same check on ledgers. It also goes only to docs/ANALYSIS_B.md, and no summary field is planned. |
| 1650 | `\ph{41}` | Verification-pass rejection rate on wrong entries. B-AB-verify-s0 is planned, but its eval block (eval_local.py verification_pass) records only verify_entries, verify_rejected_entries, verify_regenerated and verify_replaced. Rejections are not split by whether the entry was correct, so no key gives  |
| 1650 | `\ph{3.2}` | Rejection rate on correct entries. As above: B-AB-verify-s0 records no split by entry correctness. |
| 1653 | `\ph{98.7}` | Share of identical ledgers for two candidate steps about the same criterion in selection. The D-SEL-* summaries define only acc, pair_acc, control_acc, trap_acc and n (RESULT_KEYS.md). |
| 1653 | `\ph{96.9}` | Reader accuracy on the found field (L2). No planned run or documented field reports per-field reader accuracy; B-AE-oracle-ledger and B-AE-pred-ledger-program give TA only. |
| 1653 | `\ph{95.4}` | Reader accuracy on the subject field (L2). No planned run or field (see 96.9). |
| 1653 | `\ph{94.1}` | Reader accuracy on the time field (L2). No planned run or field (see 96.9). |
| 1654 | `\ph{2.1}` | Share of L2 cases whose quoted span occurs in the case but is not the decisive finding. No planned run or field. |
| 2032 | `\ph{78.0}\% on` | Product of the calibrated scores, MedQA. FINAL_TASKS_D P1 asks for the product and a fitted combination alongside the minimum, but neither RUN_MATRIX_D nor RESULT_KEYS.md has a run id for them (D-CAL compares them on dev only). Once run ids are added, the keys are run/<id>/sel:medqa/top/acc and run/ |
| 2033 | `\ph{66.1}\%` | Product combination, key pairs. No run id (as for the 78.0 entry above). |
| 2034 | `\ph{78.5}\%` | Logistic combination fitted on dev, MedQA. No run id (as above). |
| 2034 | `\ph{67.0}\%` | Logistic combination, key pairs. No run id (as above). |
| 2036 | `\ph{78.0}\% on MedQA` | Paraphrased-vignette control: no run is planned for it. The planned controls swap in another question's vignette (D-SEL-stepcheck-swap, D-SEL-combined-swap), which is a different test. Add a run or drop the sentence. |
| 2052 | `\ph{59.7}\%` | Pilot result from the generator that came before rule_v1. No run in RUN_MATRIX_* reproduces it and no results/ run holds it. B-C0-smoke-verdict-triplets-s0 is a different setup (smoke_v2 with held-out templates; TA 100 on family_switch and history_switch). FINAL_TASKS_D P0.4 plans only a timeline do |

## Results typed by hand with no result file (write the number into a results file, or remove it) (2)

| line | text | note |
|---|---|---|
| 1369 | `Signature classes & \ph{tbd} & \ph{tbd}` | A-D15 stores the classes only as lists (folds.1.l2_classes, 5 classes) plus the total folds.1.n_classes = 21. There is no numeric count per split, so neither the Train cell nor the L2 cell can be keyed. A count field is needed in results/A-D15/summary.json. |
| 1390 | `templates and cue phrases (\ph{0}\%)` | A-D15 gives counts, not a percentage: templates.templates_shared = 0 of templates_test = 516, and templates.cue_words_shared = 0 of cue_words_test = 19. A count key followed by \% would be wrong as soon as the count is nonzero. Either rephrase with counts (a15/templates.templates_shared@int, a15/tem |

## Other (90)

| line | text | note |
|---|---|---|
| 121 | `ten years ago` | Illustrative example of a rule condition in the introduction, not a measurement. |
| 123 | `the last six months` | Illustrative example of a rule condition, not a measurement. |
| 127 | `0.97\linewidth` | Fig. 1 layout lengths (also [3pt] on line 131 and tabcolsep 3pt on line 132); not quantities. |
| 190 | `(1)` | Contribution enumerators: (1) line 190, (2) line 195, (3) line 203. |
| 212 | `TikZ node coordinates and lengths` | Layout of the overview figure, lines 212-248. It contains no result or quantity. |
| 432 | `probability $1/8$` | Follows from the math: three independent fair signs give (1/2)^3. This is not a measured result. |
| 564 | `$1-p$ (564), \tfrac{1}{\|e^\ast\|} (567)` | Mathematical constants inside the training objective, not quantities. |
| 613 | `\texttt{rule\_v1}` | Dataset version name (also on line 704), not a quantity. |
| 670 | `MedS$^3$ (670); GenPRM-7B (673); Qwen3.5-27B, Llama-3.3-70B (674)` | Model identifiers, not quantities. C verifies the IDs in configs/models.json. |
| 675 | `\ph{Kimi K3}` | Placeholder for a model name, not a number, so no \res key can supply it. Replace it with the verified ID C records for C-AUD-kimi-k3 in configs/models.json, or drop it if the run is not made. |
| 675 | `\ph{GPT-5.4}` | Placeholder for a model name, not a number. Replace it with the verified current GPT flagship ID from C-AUD-closed-1 (configs/models.json), or drop it if not run. |
| 675 | `\ph{Gemini 3.1 Pro}` | Placeholder for a model name, not a number. Replace it with the verified Gemini flagship ID from C-AUD-closed-2 (configs/models.json), or drop it if not run. |
| 675 | `\ph{Claude Opus 5.5}` | Placeholder for a model name, not a number. Replace it with the verified Claude flagship ID from C-AUD-closed-3 (configs/models.json), or drop it if not run. |
| 695 | `seed 0` | Seed index inside a draft-status clause ('values printed in black ... are from seed 0'). Remove the clause once multi-seed values are in. |
| 749 | `Rule triplets, L0` | Set label, not a number, but it disagrees with the generated Table 2: make_tables.py uses AUDIT_SET = 'L2' (FINAL_TASKS_C P1: closed judges on L2 triplets). The caption should say L2. The prose ranges on lines 756-759 are mapped to L2 keys to match the table cells. |
| 763 | `solves no triplet` | Result stated in words for the step-only classifier. It follows from Proposition prop:blind, and the measured claim-only scorer agrees: run/A-D14-claim_only/L2/all/TA = 0.0. There is no numeral to replace. |
| 764 | `solves no triplet` | Concept-named scorer on L2, stated in words. It matches run/A-D14-concept_named/L2/all/TA = 0.0 (Table 7). There is no numeral to replace. |
| 775 | `\ph{84.9}` | Minimum over signals of reading (P) and application (K) reversal, from the composition gap in App. F (tab:pk, L0). The planned run is C-DG-pkg (RUN_MATRIX_C, P1, 'composition gap P/K/G for 4 signals'). RESULT_KEYS.md defines no summary file or fields for it (only C-DG-shift has signal=<prefix> slice |
| 776 | `\ph{11}--\ph{80}` | Range of the composition gap G over the same signals. Same status as line 775: C-DG-pkg is planned but has no key format. Map to min/...--max/... over the G keys once it exists. |
| 953 | `\ph{58.9}` | Planned run: B-DIS-s0..s2 (MedEinst with diseases held out). The evaluation set has no registered name. App. D defines it as test pairs whose two diagnoses are both test diseases (12 of 49), so it may not be the full medeinst_test. If C writes it as summary_clin_v1~medeinst_test.json under B-DIS-s<k |
| 1105 | `nothing on MedEinst` | A result claim in words (a loss of 0 points on MedEinst pairs without near-misses), so there is no number to replace. Once the runs exist, the authors should check it against d/run/D-SEL-combined/sel:medeinst/top/pair_acc\|run/D-SEL-no-nearmiss/sel:medeinst/top/pair_acc and reword if needed. The cla |
| 1114 | `\ph{in part}` | A placeholder in words (how far transfer to existing clinical labels holds), not a number; no key can produce words. The authors write it from the zero-shot clinical columns of Table 4 (MedEinst, TrialGPT, criteria) and cmp/p4, cmp/p6a once those runs exist. |
| 1219 | `(1) balanced against natural` | Enumeration labels (1)-(6) of the primary comparisons. The same labels recur on lines 1220-1223, 1227-1231 and 1234-1236. They are labels, not values. |
| 1462 | `& \ph{tbd}` | Long note = tier 'long'. Counts exist, but the table does not name the test set: a15/datasets.rule_v1/test_L2.tier.long@int = 603 for L2, a15/datasets.rule_v1/test_hard.tier.long@int = 917 for the hard set. Bind it once the lead decides which set the table counts. |
| 1480 | `\ph{Gemma-3-27B}` | Model-name placeholder, not a number. scripts/rewrite_tier.py (A-D11) sets REWRITER = google/gemma-4-31b-it (verified 2 Oct), and results/A-D11/summary.json will record it as 'rewriter'. Write the model actually used. |
| 1481 | `(\ph{8.7}\% rejected)` | A planned source exists, but the key grammar cannot express this quantity. A-D11 (scripts/rewrite_tier.py) writes results/A-D11/summary.json with acceptance_rate (%), groups_tried and groups_accepted. The rejected share is 100 - acceptance_rate, and the grammar has no constants or ratios. Either rew |
| 1643 | `\ph{2.4}` | Malformed-ledger rate on MedEinst. MedEinst runs of the ledger adapters are planned (FINAL_TASKS_C P1), but RESULT_KEYS.md documents only Reversal, control_acc, trap_acc, n_pairs and CI95 for summary_clin_v1~medeinst_test.json, so no key exists. If the clinical eval writes eval_local.py's eval block |
| 1707 | `\ph{93.5}` | Table pk (L0; not a generated table): Base, Inj.-error PRM row. Planned run C-DG-pkg (RUN_MATRIX_C P1, composition gap for 4 signals, A-D8 readapply pairs) will produce it. RESULT_KEYS.md defines no summary file or fields for C-DG-pkg, so no key can be written yet. The lead must document them (e.g.  |
| 1707 | `\ph{0.0}` | Table pk: Ties, Inj.-error PRM row. C-DG-pkg is planned but has no documented key fields (see Base on line 1707). |
| 1707 | `\ph{8.1}` | Table pk: UR (unnecessary reversal given a correct base), Inj.-error PRM row. C-DG-pkg has no documented key fields. |
| 1707 | `\ph{4{,}769}` | Table pk: UR denominator (count), Inj.-error PRM row. C-DG-pkg has no documented key fields. |
| 1707 | `\ph{92.8}` | Table pk: P (reading reversal), Inj.-error PRM row. C-DG-pkg has no documented key fields. |
| 1707 | `\ph{89.5}` | Table pk: K (application reversal), Inj.-error PRM row. C-DG-pkg has no documented key fields. |
| 1707 | `\ph{71.4}` | Table pk: G (composition gap), Inj.-error PRM row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{80.2}` | Table pk: Base, Qwen3.5-9B (\bb{}) row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{0.0}` | Table pk: Ties, Qwen3.5-9B row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{24.6}` | Table pk: UR, Qwen3.5-9B row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{4{,}090}` | Table pk: UR denominator, Qwen3.5-9B row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{95.3}` | Table pk: P, Qwen3.5-9B row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{91.2}` | Table pk: K, Qwen3.5-9B row. C-DG-pkg has no documented key fields. |
| 1708 | `\ph{56.8}` | Table pk: G, Qwen3.5-9B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{88.4}` | Table pk: Base, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{0.0}` | Table pk: Ties, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{26.0}` | Table pk: UR, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{4{,}508}` | Table pk: UR denominator, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{97.6}` | Table pk: P, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{95.4}` | Table pk: K, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `\ph{33.4}` | Table pk: G, Qwen3.5-27B row. C-DG-pkg has no documented key fields. |
| 1709 | `Qwen3.5-27B` | Model name in the row label (also in the prose on line 1826), not a result. Check it against the model ID in C-AUD-qwen35-27b's meta.json. |
| 1710 | `\ph{Claude Opus 5.5}` | Row-label placeholder for a model name, not a number. Replace with the verified model ID of C-AUD-closed-3 (meta.json 'model'; make_tables label() does this for generated tables). |
| 1710 | `\ph{96.0}` | Table pk: Base, closed-judge row. C-DG-pkg has no documented key fields. |
| 1710 | `\ph{3.8}` | Table pk: Ties, closed-judge row. C-DG-pkg has no documented key fields. |
| 1710 | `\ph{12.9}` | Table pk: UR, closed-judge row. C-DG-pkg has no documented key fields. |
| 1710 | `\ph{4{,}896}` | Table pk: UR denominator, closed-judge row. C-DG-pkg has no documented key fields. |
| 1710 | `\ph{99.2}` | Table pk: P, closed-judge row. C-DG-pkg has no documented key fields. |
| 1710 | `\ph{98.1}` | Table pk: K, closed-judge row. C-DG-pkg has no documented key fields. |
| 1710 | `\ph{11.3}` | Table pk: G, closed-judge row. C-DG-pkg has no documented key fields. |
| 1789 | `27B judge,9B judge` | Tick labels naming the 27B and 9B judges (model sizes), not results. They match make_tables DIAG order. |
| 1805 | `symbolic x coords={Inj,8B,32B,Blk}` | Symbols used by the generated fig-diag-kappa body (make_tables f_diag_kappa: Inj = C-AUD-medprm, 8B = C-AUD-qwen35-9b, 32B = C-AUD-qwen35-27b, Blk = B-F-verdict-blocks). They print as tick labels, and 8B/32B are outdated sizes for the 9B and 27B judges. Rename in make_tables and here together. Not r |
| 1828 | `\ph{42.0}` | Qwen3.5-27B triplet accuracy under the sampled readout. C-DG-noise (RUN_MATRIX_C P2; sampling-noise check in FINAL_TASKS_C P1) is planned, but RESULT_KEYS.md defines no summary fields for it, so no key exists yet. |
| 1828 | `\ph{4.1}` | Tie rate under the sampled readout. Same C-DG-noise situation: planned, no documented fields. |
| 1832 | `\ph{1.2}` | MedPRMBench input ablation: low end of the PRMScore loss for trained PRMs. C-DG-inputabl (RUN_MATRIX_C P2) runs only if MedPRMBench is released (no data release as of 2 Oct, B-PRM note), and RESULT_KEYS.md defines no fields. If it is not run, remove the paragraph (PAPER_CONTEXT.md section 8). |
| 1832 | `\ph{2.9}` | High end of the same range. Same C-DG-inputabl situation. |
| 1836 | `\ph{4.0}` | Loss on case-relative error types, low end. Same C-DG-inputabl situation. |
| 1836 | `\ph{9.5}` | Loss on case-relative error types, high end. Same C-DG-inputabl situation. |
| 1836 | `\ph{6.2}` | Loss with stem numbers and spans also masked, low end. Same C-DG-inputabl situation. |
| 1836 | `\ph{13.0}` | Loss with masking, high end. Same C-DG-inputabl situation. |
| 1841 | `\ph{90.8}` | Probe accuracy on held-out signature classes. C-DG-probe (RUN_MATRIX_C P3, exploratory) is planned, but RESULT_KEYS.md defines no fields for it. |
| 1842 | `\ph{49.6}` | Control-task accuracy of the same probe. Same C-DG-probe situation. |
| 1927 | `\ph{tbd}` | This placeholder covers several results (macro-averages over rules and over signature classes, per-seed values, the lowest held-out class), not one number. Per-seed values are already in tab:seeds. RESULT_KEYS.md has no macro-average stat or field (FINAL_TASKS_B P0.1 puts macro-averages in docs/ANAL |
| 1983 | `about 2.2` | Black, hand-typed, and generic ('a verdict-only run'), so no single key states it. Per-run meta gpu_hours, evaluation included: B-F-verdict-natural 2.246, -balanced 2.146, -blocks 2.182, -triplets 2.179 (meta/B-F-verdict-<corpus>/gpu_hours). To key it, reword as a range \res{min/meta/...gpu_hours\|. |
| 1984 | `about 2.8` | Black, hand-typed. Only meta/B-F-ledger2-blocks/gpu_hours matches (2.799, A100-SXM4-80GB). The other two-stage runs differ: B-F-ledger2-triplets-s0 3.732 (A100-PCIE-40GB) and B-F-summary2-triplets-s0 1.964. So 'a two-stage run about 2.8' is not one quantity. Reword (a range over the two-stage prefix |
| 1985 | `21.9~GB` | Black, hand-typed. It equals meta/B-C0-val-gpu-ckpt/train.peak_mem_gb (21.87), which comes from a 40-step smoke check of the on-GPU checkpointing fix (ledger2 on smoke_v2), not a paper run. The only full rule_v1 run in that configuration so far, B-F-summary2-triplets-s0 (code c3bdac6, use_gradient_c |
| 1995 | `Verdict only           & \ph{tbd} & -- & \ph{tbd} & \ph{tbd} & \ph{tbd}\\` | tab:budget has no tables markers, so make_tables.py does not generate it, and its rows do not name a corpus; no per-cell key matches a cell exactly. meta.json has the sources: pretok_stats.tokens (tokens), train.steps (938 for every 60k run), pretok_stats.parts (reader/judge targets; verdict: parts. |
| 1996 | `Rationale              & \ph{tbd} & -- & \ph{tbd} & \ph{tbd} & \ph{tbd}\\` | Same as the Verdict only row (meta: parts.rationale = 60000, pretok_stats.tokens, train.steps); the corpus is not named. |
| 1997 | `Evidence summary       & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}\\` | Same as the Verdict only row (B-F-summary2-<corpus>: parts reader/judge 30000/30000, reader_units, tokens, steps); the corpus is not named. |
| 1998 | `Applicability ledger   & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd} & \ph{tbd}\\` | Same as the Verdict only row (B-F-ledger2-<corpus>); the corpus is not named. |
| 2009 | `\ph{45} tokens` | Mean generated tokens per claim for Ledger-RM. D-RES is planned (RUN_MATRIX_D) but its kind is 'doc', and RESULT_KEYS.md defines no summary JSON or field for it. meta.json eval_generated_tokens is per run, not per claim. Define D-RES output first (e.g. results/D-RES/summary.json, key sum/D-RES/<syst |
| 2010 | `\ph{540} tokens` | Per-claim generated tokens of the generated-program verifier (C-TF-genprog). Belongs to D-RES, which has no key format yet. |
| 2011 | `\ph{500} tokens` | Per-claim generated tokens of the GenPRM-style verifier (B-TR-genprm). Belongs to D-RES, which has no key format yet. |
| 2012 | `\ph{210} tokens` | Per-claim tokens of the closed judge with ledger prompt (C-REF-closed-ledger). Belongs to D-RES, which has no key format yet. |
| 2012 | `\ph{60} times the list price` | API cost per claim relative to the backbone (D-RES: 'API cost per claim'). It depends on external list prices, and no key format is defined. |
| 2022 | `\ph{38.6}\%` | Accuracy of the initial policy on base-flip pairs of held-out structures, judged by the rule program. The D-RL-* runs (RUN_MATRIX_D) will log it, but RESULT_KEYS.md defines no summary file or field for RL runs (which set; start vs final accuracy). Define the D-RL output first (e.g. top-level acc_sta |
| 2023 | `\ph{52.3}\%` | Final accuracy with the outcome reward. D-RL-outcome-s0/s1 is planned, but there is no RL key format yet (see the 38.6 entry). |
| 2023 | `\ph{33.9}\%` | Final accuracy with the injected-error PRM reward. D-RL-stepcheck-s0/s1 is planned; no RL key format yet. |
| 2024 | `\ph{63.5}\%` | Final accuracy with the Ledger-RM reward. D-RL-ledger2-triplets-s0/s1 is planned; no RL key format yet. |
| 2027 | `\ph{58.0}\%` | Final accuracy with the reference-graph reward. D-RL-refgraph-s0/s1 is planned (P2); no RL key format yet. |
| 2031 | `\ph{6.1}\%` | Share of traces with no final answer. The D-POOL-* pools will produce it, but RESULT_KEYS.md defines no pool summary or field, and the sentence does not say which pool. |
| 2042 | `\ph{48.2}\%` | Share of open-ended CareQA answers graded correct. D-OPEN is planned (P3), but RESULT_KEYS.md defines no summary file or field for it, and the sentence does not name the two selectors being compared. |
| 2042 | `\ph{51.0}\%` | Same as the 48.2 entry (D-OPEN). |
