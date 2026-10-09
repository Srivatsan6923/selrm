# NEXT TASKS A (data) -- 3 Oct 2026, after the status board

## Paste this into your Claude Code session
> Read `NEXT_TASKS_A.md` and `docs/AUX_PROTOCOL.md`. They reprioritise
> `FINAL_TASKS_A.md` from the results on the status board of 3 Oct. Work
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
1. **`rule_v1x/aux_blocks_20k` and `aux_triplets_20k`** (today): 20,000-record
   subsamples of the frozen blocks and triplets corpora, same groups where
   possible, verdict-ready, frozen and registered. B mixes them with
   in-domain data.
2. **Negation phrase bank for C**: test-split and train-split templates for
   an explicitly denied finding ("denies X", "no X"), for C's MedEinst
   negated-evidence set.
3. **`rewrite_v1`** as soon as the API key exists: 1,000 L2 groups, accepted
   groups only, acceptance rate reported, rejected groups to the audit file.
4. **Training-side rewrites** `rule_v1x/train_triplets_rw` and
   `train_blocks_rw`: replace the text of 25% of the groups in the two
   corpora by rewrites that pass the same two-extractor check (states and
   labels unchanged; test templates and test groups never used). Freeze.
5. After the authors finish: assemble and freeze `challenge_v1` (H2), freeze
   `ec_v1` with the approved criteria only (H3), aggregate H1.
6. Report `xr_v1` in two versions everywhere (400 items; 362 without the 38
   known issues).
7. Appendix B and C text from result keys only, including: 0 people among
   the pre-freeze readers; 97 of 103 hand-written rules simplified from
   sources and 53 deviating from them (call them stated rules, never
   guideline rules); the known semantic limits.

## Do not
Start MedCalc-Bench, new rule families or `rule_v2`.
