# FINAL TASKS C (evaluation) -- 3 Oct 2026

## Paste this into your Claude Code session
> Read `FINAL_TASKS_C.md`. It replaces every earlier directive, scope file
> and run-matrix priority for role C. The frozen decisions in `CLAUDE.md`,
> `docs/INTERFACES.md` and `docs/AUTONOMY_PROTOCOL.md` still apply. Work autonomously; ask me only for
> compute or credentials. Do P0 in the order given, then P1. Rules for all
> roles: `rule_v1` is frozen and is never edited or regenerated; every new
> dataset gets a new name, a manifest and a shortcut-validation result and is
> frozen before any model is scored on it; nothing is tuned on a test set;
> every run keeps per-example scores and reader outputs; every number in a
> table comes from a results file. Seed-0 results are provisional: do not
> change the paper's design because of them. Log decisions in
> `docs/DECISIONS_C.md`, publish outputs through `docs/HANDOFFS.md`, keep
> `docs/STATE_C.md` current.

## Context (same for all roles)
The paper is v13: v10's full design (audit of 13 signals, training data x
representation table, transfer table, ablations, candidate selection, policy
training) with review corrections. Seed 0 on held-out rule structures (L2):
verdict 58.2 (blocks) -> 91.3 (triplets); one-stage rationale 61.5 -> 91.0;
two-stage prose summary 98.0 (triplets); two-stage ledger 75.3 -> 99.2.
What reviewers will ask for first, and what therefore comes first: seeds and
paired statistics; the prose summary as a central baseline; tests the
generator does not determine (rule-side edits, author-written cases); data
audits; one external evaluation on existing expert labels.

## P0 (in order)
1. **TrialGPT criterion annotations.** List the columns; separate expert
   fields from GPT-4 outputs; send A the trial IDs. Write and commit
   `docs/TRIALGPT_PROTOCOL.md` before scoring anything: inputs (patient
   summary, criterion with its type; never a GPT-4 field); targets (expert
   eligibility labels); categories kept, including "not enough information"
   and "not applicable" (no forced binary mapping); a patient-disjoint
   development portion for interface decisions and an untouched test
   portion; metrics (accuracy, macro-F1, class-wise errors, precision and
   recall of quoted sentences against expert sentences, which evaluate
   evidence selection only); bootstrap over patients, paired differences.
   Then score, zero-shot: untrained backbone, verdict x blocks, verdict x
   triplets, ledger x blocks, summary x triplets, ledger x triplets (and
   summary x blocks when B has it). Report in `docs/TRIALGPT_RESULTS.md`.
2. **Untrained backbone on L2**: direct verdict and prompted two-stage
   (summary and ledger).
3. **Metrics** in `selrm/metrics.py`: paired bootstrap with triplets kept
   together and rule, family or patient clusters; per-seed listing;
   macro-averages; crossed accuracy for `xr_v1`; for near-misses: same
   decision, both correct, near-miss correct given base correct;
   denominators per kind.
4. **Existing adapters and baselines on `xr_v1`, `challenge_v1`,
   `rewrite_v1`, `ec_v1`** as A registers them.
5. **General-purpose trigger baseline** (frozen clinical context tagger +
   rule program) for the shortcut table.

## P1 (the rest of v10's evaluation)
Audit of 13 signals (Table 2): released PRMs (3-hour timebox each), open
judges, closed judges on L2 triplets (1,000 for costly models), `xr_v1`,
MedEinst, key pairs. Training-free rows (critic, default correction,
prompted ledger, generated-program verifier) and references of the transfer
table. MedEinst for all adapters; quote what its authors report about
physician review after checking the paper. Key pairs from MedQA and CareQA.
NLI4CT-P. Clinical training pairs for B (`clin_v1/clinpairs_train`: MedEinst
reference pairs and MedQA-train key pairs with ledger targets) and the
disease-held-out split. Critic and closed judge on the ladder sets.
Composition gap and shift analysis. Sampling-noise check (log-odds against a
sampled readout on one open judge). Exploratory probe last. MedPRMBench status and input
ablations if released. CondMedQA and EHRNote-ChatQA only if accessible; never
send credentialed data to an API.
