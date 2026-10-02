# INTERFACES (frozen 2 Oct; changes only through docs/CHANGE_REQUESTS.md and the lead)

Four sessions work in parallel. These contracts are what keeps their code
compatible. If you need something different, file a change request and work
around it; do not edit a contract locally.

## 1. Canonical instance record (`selrm/schema.py`)
One JSON object per (case, claim), one per line. See `docs/SAMPLE_RECORDS.md`.

| Key | Meaning |
|---|---|
| `iid` | `<tid>/<case_kind>/<claim_type>/<claim_role>` |
| `tid` | group id: base, flip, near, pres (and missing, read, apply) of one context |
| `set`, `split` | dataset version (`rule_v1`), `train` / `dev` / `test` |
| `level` | `L0` seen rules, `L1` unseen rules of seen class, `L2` held-out classes, `L3-inv` invented, `L3-alt` altered thresholds |
| `tier` | `easy`, `long`, `superseded`, `delabelled`, `alt`, `rewritten` |
| `rid`, `cid`, `family` | rule, target criterion, structural family (signature class) |
| `nm_kind` | `numeric`, `boundary`, `subject`, `negation`, `time` |
| `case_kind` | `base`, `flip`, `near`, `pres`, `missing`, `read`, `apply` |
| `rule_text`, `case_text`, `condition` | what prompts are built from |
| `claim_type` | `conclusion` (used for TA), `criterion`, `applicability` |
| `claim_role` | `s` (correct on base/near/pres) or `s_prime` (correct on flip) |
| `claim_text`, `label` | label 1 = claim correct for this case |
| `state` | mentions as dicts (program input) |
| `ledger` | program-generated entries: `need, found, subject, status, time` |
| `prose` | the same evidence as plain sentences (matched two-stage baseline) |
| `meta` | template ids, seeds, keywords for rules not in `rules.py` |

Rules: every case carries both claims of every emitted claim type; `label`
comes from the program; `ledger` and `prose` never contain a decision.
Missing twins: `case_kind = missing`, both claims have `label = 0`.

## 2. Prompts (`selrm/prompts.py`)
`verdict_prompt`, `rationale_prompt` (one-stage), `reader_prompt(rec,
prose=False|True)`, `judge_prompt(rec, record_text)`, `choice_prompt` (API),
`ledger_to_text`, `answer`. Targets: verdict/judge -> `"+"` or `"-"`;
reader -> `ledger_to_text(rec["ledger"])` or `rec["prose"]`; rationale ->
ledger text, newline, answer. Chat template applied by the caller with
thinking disabled.

## 3. Scoring conventions
- Local: one forward pass per record; `u = logit("+") - logit("-")` at the
  answer position (assert both are single tokens). Two-stage: greedy-generate
  the reader output once per (case, condition), reuse it for both claims.
  Malformed ledger (unparsable, or a quoted `found` that is not a substring
  of the case) -> `u = -20` for both claims (tie -> failure).
- API: log-probabilities if available (same u); else `choice_prompt` in both
  orders, d in {+1, 0, -1}. Missing-evidence rejection for choice-format
  models: pointwise accept/reject calls on the missing twins.
- Preference `d = u(s) - u(s_prime)` per (tid, case_kind, claim_type).
- `selrm.metrics.decisions(records, scores)` then `summarise`, `bootstrap_ci`,
  `paired_diff`. Add metrics there (owner C); never re-implement elsewhere.

## 4. Results layout (see `docs/RESULTS_SCHEMA.md`)
`results/<run_id>/{meta.json, scores_<set>.jsonl, summary_<set>.json, DONE}`.
`scores_*.jsonl`: `{iid, u}` (plus `reader_output` for two-stage runs).
`summary_*.json`: output of `summarise` plus CIs.

## 5. Dataset registry (owner A)
`data/REGISTRY.json`: `{name: {path, split, level, tier, n_groups,
n_records, manifest, frozen: true|false, created}}`. Datasets are immutable
once `frozen`. New content = new version name. Every dataset has
`MANIFEST.json` (seed, git commit, counts by rule/kind/tier/level, template
split hash, shortcut-validation result).
Names A will publish: `rule_v1/test_L2`, `rule_v1/dev`,
`rule_v1/train_{natural,balanced,blocks,triplets}`, `rule_v1/test_{L0,L1,
L3inv,L3alt}`, `rule_v1/test_hard`, `rule_v1/missing`, `rule_v1/readapply`,
`rule_v1_fold{2,3}/...`, `rule_v1/div_*`, `rule_v1/rewritten`,
`rule_v1/abl_*`. Clinical sets by C: `clin_v1/{medeinst_test, keypairs_medqa,
keypairs_careqa, nli4ct, clinpairs_train, condmedqa}` in the same record
schema where it applies (`rule_text` = "" when no rule is stated).

## 6. Adapter registry (owner B)
`configs/keep_adapters.json` (which runs keep their adapter) and
`configs/adapters.json`: `{system_name: {run_id, path, base_model, format}}`.
Systems C and D rely on: `ledger2_triplets`, `ledger2_blocks`,
`verdict_triplets`, `stepcheck`.

## 7. Run claims and heartbeats
Before starting a run: create `results/<run_id>/CLAIMED_<role>`; touch
`results/<run_id>/HEARTBEAT` at least hourly; write `DONE` at the end.
Update your `docs/RUN_MATRIX_<role>.csv` rows (`status`, `measured_hours`).

## 8. Git
One repo. Branch `role-<a|b|c|d>`. Commit small and often. The lead merges to
`main` daily. Shared files you may edit on your branch: only those you own
(table in CLAUDE.md). For anything else: `docs/CHANGE_REQUESTS.md`.
