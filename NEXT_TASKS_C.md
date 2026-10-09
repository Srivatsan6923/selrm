# NEXT TASKS C (evaluation and external data) -- 3 Oct 2026, after the status board

## Paste this into your Claude Code session
> Read `NEXT_TASKS_C.md` and `docs/AUX_PROTOCOL.md`. They reprioritise
> `FINAL_TASKS_C.md` from the results on the status board of 3 Oct. Work
> autonomously to the end of your list; ask me only for compute or
> credentials. All integrity rules stand: frozen data are never edited, new
> sets get new names and are frozen before scoring, nothing is tuned on a
> test set, every number comes from a results file. The planned comparisons
> that failed stay reported as failed. Everything in `docs/AUX_PROTOCOL.md`
> is a secondary analysis specified after those failures and must be
> labelled so in every table and summary. Run freeze: Wed 7 Oct 23:59 UTC.

## Where the project stands (3 Oct, five seeds on the core cells)
- Near-miss supervision works: held-out rules, verdict 53.7 -> 91.8, prose
  summary 64.9 -> 98.5, ledger 71.0 -> 99.2; rule-side test 85-94 for
  triplet-trained against 36-82 for flip-pair-trained systems.
- Released medical PRMs solve 10-12% of triplets; optimising a policy
  against Med-PRM dropped held-out accuracy from 88.0 to 38.7.
- The typed ledger is not the driver: +0.8 over prose; a decision bit does
  as well; the judge follows an edited field 47.8% of the time.
- Zero-shot medical transfer failed: TrialGPT +3.4 (n.s.), MedEinst -8.5,
  key pairs collapse for two-stage systems because the judge cannot see the
  case. Only positive sign: NLI4CT-P average 0.809 -> 0.855 for verdict
  models.
- Direction from here: (1) a judge that sees the case and the record;
  (2) near-miss rule data as auxiliary supervision next to in-domain medical
  training; (3) external metrics that measure reversing and holding;
  (4) the policy-training result; (5) tests the renderer does not determine.

## Do, in this order
1. **`docs/AUX_PROTOCOL.md`**: complete the template and commit it before B
   trains anything on in-domain data. Fix splits, prompts, label mappings,
   metrics and the comparisons there.
2. **In-domain sets in the canonical verdict format** (frozen, with
   manifests): `clin_v1/nli4ct_train|dev` and the NLI4CT-P test with its
   intervention types; `clin_v1/medeinst_train` (the 7,807 reference pairs)
   and test pairs; `clin_v1/trialgpt_cv` (5 folds by patient, the 10
   development patients kept out).
3. **`clin_v1/medeinst_neg`**: for each MedEinst test pair, the control case
   plus one line that explicitly denies the finding distinguishing the trap
   (A's test-split phrases; the finding from the structured difference of the
   pair). The control diagnosis stays correct by construction, since the
   finding was already absent. Also the same construction on reference pairs
   for training (train-split phrases). Shortcut validation: a scorer that
   prefers the trap diagnosis whenever the finding is named gets 0.
4. **Zero-shot scoring of B's case-visible systems** on TrialGPT, MedEinst,
   `medeinst_neg`, key pairs and NLI4CT-P, next to the case-blind rows.
5. **Evaluate the auxiliary grid** (or hand B the scripts): NLI4CT-P F1,
   faithfulness, consistency; MedEinst pair reversal, control and trap
   accuracy, hold on `medeinst_neg`; TrialGPT macro-F1. Paired contrasts
   (3) vs (2) and (3) vs (1), clusters = trial report, diagnosis pair,
   patient; Holm over the three datasets.
6. **API audit** when the key arrives: three closed flagships, Kimi K3,
   Llama-3.3-70B (GLM-5.3 and Nemotron optional) on 1,000 L2 triplets,
   `xr_v1`, 1,000 MedEinst pairs, key pairs, TrialGPT; the same models with
   the prompted two-stage summary on L2; closed-judge reference rows and a
   closed extractor for the extraction + program row. Lowest reasoning
   setting; cost estimate checked against the budget before each run.
7. **Finish**: ThinkPRM and GenPRM audit parts, NLI4CT-P ledger rows,
   27B judge; score A's new sets for baselines; with D, score the trained
   policies on TrialGPT and `ec_v1`.
8. **If time remains**: trial-level eligibility on the public TREC/SIGIR
   cohorts (verify availability and licence; 1,000 patient-trial pairs,
   eligible against excluded), protocol first.

## Do not
Tune prompts or mappings on any test portion; send credentialed data to an
API; report a re-read of malformed MedEinst ledgers in place of the primary
row.
