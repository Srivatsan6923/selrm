# NEXT TASKS D (lead: integration, policy training, tables, paper) -- 3 Oct 2026, after the status board

## Paste this into your Claude Code session
> Read `NEXT_TASKS_D.md` and `docs/AUX_PROTOCOL.md`. They reprioritise
> `FINAL_TASKS_D.md` from the results on the status board of 3 Oct. Work
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
1. **Record decisions in `docs/DECISIONS_D.md`** (the human lead confirms):
   the zero-shot medical-transfer claim is withdrawn as the analysis plan
   requires; the secondary analyses of `docs/AUX_PROTOCOL.md` are added and
   dated; gate definitions (typed ledger a headline only if it beats prose
   on L2 and on one external or independent set: not met; near-miss
   generalisation across kinds: report as found). Answer B: the second
   backbone is Qwen3.5-4B; the condition-finding reader receives the rule
   and the claim.
2. **Merge** role-a, role-b, role-c daily; regenerate the board; keep the
   integrity checks green.
3. **Policy training (now a headline result)**: finish seed 0 for the two
   ledger rewards and the reference-graph reward; add a summary-pipeline
   reward trained on triplets; run seed 1 for outcome, step check, ledger x
   blocks, ledger x triplets. For every final policy report, from saved
   per-example outputs: accuracy on held-out base/flip/near-miss cases,
   `xr_v1`, `ec_v1`, TrialGPT (with C), and reward against program accuracy
   over training. No statement about reward exploitation beyond these runs.
4. **Tables**: add the auxiliary-supervision table, the case-visible rows,
   leave-one-kind-out, crossed accuracy, and the policy-training table to
   `make_tables.py`; secondary analyses are marked as such; Table 5 stays as
   measured and moves to the appendix; do not wait for the clinical-pairs
   ledger.
5. **Paper scaffold v14** from result keys: contributions = (1) the test and
   the audit of medical PRMs; (2) near-miss supervision; (3) separate
   evidence reading, with the judge seeing the case; (4) behaviour as a
   training reward. Zero-shot transfer and selection are reported as
   negative. Apply the 20 moves of the length plan; cut every statement the
   claims audit marks contradicted; cut the development-history claims that
   have no record. Prose is the authors' job (H6).
6. **Kits and audits**: keep H1-H5 paths current; rerun the claims audit
   after each table update; final audit on Sat 10 Oct.
