# ROLE C: metrics, judges, audit, baselines, clinical tier, diagnostics

## Deliverables, in order (docs/RUN_MATRIX_C.csv)
1. **C-M0** extend `selrm/metrics.py` (you own it): MR/FR on missing twins,
   step-level metrics (correct / unnecessary revision), level and tier
   breakdowns, clinical metrics. `scripts/score.py`, `scripts/eval_rule.py`,
   `scripts/eval_clinical.py` (B and D call these; publish early via
   HANDOFFS).
2. **C-J0** `selrm/judges.py`, `scripts/run_judge.py`, `configs/models.json`.
3. **C-CL-*** clinical data in the canonical schema (`clin_v1/...`).
4. **C-P0 pilot** on Sun 4 Oct; apply the GO rule yourself; log it.
5. **C-AUD-*** audit (Table 2), **C-TF-*** training-free rows, **C-REF-***
   references (Table 4).
6. **C-DG-*** diagnostics (appendix F); appendix D and F text.

## Judge harness
- Local open judges: Unsloth or transformers, pointwise u (INTERFACES 3).
- Released PRMs/RMs (Med-PRM, MedS3 PRM, FoVer PRM, ThinkPRM, GenPRM-7B):
  use each as released (its own prompt format and scoring head); wrap as
  `score(records) -> u` where the claim is the step to be scored after the
  rule and case. 3-hour timebox each; record what "as released" meant.
- API judges: one OpenAI-compatible client; log-probabilities if the provider
  returns them, else the two-order choice prompt. Disk cache keyed by
  hash(model, messages, params); retries; thread pool; cost estimate printed
  and checked against `configs/budget.json` before each run. Fix reasoning
  effort per model. Verify every model ID on the provider page and record ID,
  provider, date in `configs/models.json`: current GPT, Gemini and Claude
  flagships; Kimi K3; GLM-5.3; Nemotron 3 (Ultra or Super via API, Nano
  locally); Qwen3.5-27B and Llama-3.3-70B locally (quantised if needed).

## Audit columns (Table 2)
Rule triplets: Rev, Hold, TA, MR (2,000 triplets; 1,000 for costly reasoning
models). MedEinst: reversal over test pairs. Key pairs: reversal.
Report the readout type per model (log-odds or choice).

## Training-free rows and references (Table 4)
critic (backbone zero-shot); default correction u(s,x) + a[u(s,x) -
u(s, no case)] with a from dev; prompted ledger (two prompts, judge sees no
case); generated-program verifier (the model writes a program for the stated
rule, executed in a sandbox). References: best closed judge zero-shot and
with the prompted ledger; extraction by a strong model followed by our rule
program (rule tier only).

## Clinical tier (appendix D of the draft gives the definitions)
- **MedEinst**: verify the repository and licence; test pairs -> blocks (two
  cases x two diagnoses); keep reference pairs separate for B; control and
  trap accuracy; disease-held-out split for B-DIS.
- **Key pairs** (MedQA, CareQA): two questions with the same option set and
  different keys; one-to-one matching by closest stem; exclude negated stems,
  "all of the above" options and one-token stems; report the yield.
- **NLI4CT-P** (SemEval-2024 Task 2): statements as claims, trial section as
  case; the task's scorer for macro-F1, faithfulness, consistency.
- **clinpairs_train** for B: MedEinst reference pairs + MedQA-train key
  pairs, with ledger targets from the released structured evidence or the
  sentence-level difference of the two vignettes.
- **MedPRMBench**: check today whether the data are released; tell B and D
  (HANDOFFS) which step check to use.
- **CondMedQA**: only if released with general answers. **EHRNote-ChatQA**:
  blocked until credentialed access exists; never send to an API.

## Diagnostics (appendix F)
composition gap P/K/G on A's reading/application pairs; shift classes and
kappa using missing twins; sampling-noise check (log-odds vs sampled
readout on one open judge); MedPRMBench input ablation (conditional);
linear probe with a control task (P3).

## Decision rules
- GO rule and budget ladder: CLAUDE.md. You apply both without asking.
- A model that cannot be verified or run inside its timebox is dropped and
  listed in the appendix as attempted.
- Until `rule_v1` exists, build and test everything on `data/smoke_v2`.
