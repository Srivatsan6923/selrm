# How a number reaches the paper (lead; read by every role)

`results/<run_id>/` or `results_git/<run_id>/` (with `DONE`) -> `scripts/make_tables.py` ->
`tables/<name>.tex`, `tables/numbers.tex`, `tables/PROVENANCE.json` -> `scripts/update_paper.py` ->
`paper/latex_v13/main.tex`. Nothing else enters the paper. A number that is only in a doc
(`docs/*.md`) is not an input: write it into a summary JSON of a run.

## Keys
Prose uses `\res{<key>}`; tables use the same keys internally (PROVENANCE.json maps every cell
to its key, runs, files and commits). `python scripts/make_tables.py --key "<key>"` prints a
key's value and provenance; `--catalog` lists finished runs, their sets and fields.

| Key | Meaning |
|---|---|
| `run/<prefix>/<set>/<slice>/<metric>[/<stat>]` | a field of `summary_<set>.json`; `<prefix>` = run id without `-s<k>` (seeds s0..s4 pooled); `<stat>` = mean (default), sd, n (seeds), min, max, s<k>, lo, hi (95% CI: rules resampled with their triplets, seeds pooled) |
| `meta/<prefix>/<dotted.field>[/<stat>]` | a `meta.json` field, mean over seeds |
| `a15/<dotted.field>`, `sum/<run_id>/<dotted.field>` | a field of `results/<run_id>/summary.json` (runs without per-set summaries; a15 = A-D15) |
| `cmp/<name>/<field>` | primary comparison p1..p6b: diff, lo, hi, p, padj, n |
| `d/<k1>\|<k2>[\|...]`, `min/<k1>\|<k2>...`, `max/...` | difference (k1 minus the rest), smallest, largest |

Sets: `L2 dev L0 L1 L3alt L3inv hard missing dev_missing readapply f2L2 f3L2` = `rule_v1/...`
(fold 2-3: `rule_v1_fold{2,3}/test_L2`); any other set is written with `:` for `/`
(`clin_v1:medeinst_test`). Slices: `all`, `nm_kind=<k>`, `tier=<t>`, `family=<f>`,
`level=<l>`, `step=<claim type>`, `eval`, `top` (top-level field). A key may end in
`@0 @1 @2 @3 @pct1 @pct2 @int` (format). Percentages are stored as percentages.

## What each role must write so its numbers are read
| Result | Run id(s) | Summary file and fields |
|---|---|---|
| Rule-tier sets (rule_v1, xr_v1, challenge_v1, rewrite_v1, ec_v1) | any | `summary_<set>.json`: `"set"`, `"all"` {Rev, Hold, TA, BaseAcc, Tie, PresHold, n}, slices `nm_kind=`, `tier=`, `family=`, `level=`, `"CI95"`; scores `scores_<set>.jsonl` {iid, u, reader_output} |
| MR at 5% FR | any | `summary_rule_v1~missing.json` top-level `MR`, `FR`, `threshold` (selrm.metrics, owner C) |
| Crossed accuracy (xr_v1) | any | `summary_xr_v1~test.json` top-level `XA`, `n_items` |
| Registered criteria | any | `summary_ec_v1~test.json` (rule-tier format) |
| MedEinst | the system's own run id | `summary_clin_v1~medeinst_test.json` top-level `Reversal`, `control_acc`, `trap_acc`, `n_pairs`, `CI95` |
| Key pairs | C-KP-<x>[-s<k>] (B-F-<x> and C-TF-<x> map there; C-AUD-* hold their own) | `summary_clin_v1~keypairs_medqa_oneway.json` (and `_careqa_oneway`; the tables use these, DECISIONS_D 3 Oct) top-level `Reversal` |
| NLI4CT-P | C-NL-<x>[-s<k>] (B-F-<x> and C-TF-<x> map there) | `summary_clin_v1~nli4ct_test.json` top-level `macroF1`, `faithfulness`, `consistency` |
| NLI4CT-P | system run id | `summary_clin_v1~nli4ct.json` top-level `macroF1`, `faithfulness`, `consistency` |
| TrialGPT | C-TG-<x> (C scores system B-F-<x> / C-TF-<x>) | `summary_clin_v1~trialgpt_test.json` top-level `macroF1`, `acc`, `macroF1_CI95`, `per_class`; nested `evidence` {`precision`, `recall`} (key slice `evidence`); a variant file `summary_clin_v1~trialgpt_test~lenient.json` is read as set `clin_v1/trialgpt_test/lenient` |
| Selection (D) | D-SEL-* | `summary_sel~{medqa,careqa,keypairs,medeinst}.json` top-level `acc`, `pair_acc`, `control_acc`, `trap_acc`, `n` |
| Selection pressure (D) | D-SELN | `summary_sel~keypairs.json` slices `selector=<combined/stepcheck/oracle>` with fields `N1`..`N64` |
| Shift classes, kappa (C) | C-DG-shift | `summary_rule_v1~test_L0.json` slices `signal=<run prefix>` with `crossed short unmoved wrong kappa` |

Clinical evaluations of B's adapters: write them under the adapter's run id (e.g.
`results_git/B-F-ledger2-triplets-s0/summary_clin_v1~medeinst_test.json`) or under an
eval-only run id `<adapter run id>-eval` that the lead maps; say which in HANDOFFS.

## Run ids for rows the run matrices do not name
`B-SC-summary2-triplets-s<k>` (summary pipeline, judge also sees the case), `B-LOKO-<subject|time|boundary>-<verdict|summary2|ledger2>-s0`, `B-AB-conddrv-s0` (condition derived by the reader), `B-AE-program-ledger` (rule program on the predicted ledger), `C-SC-gptrigger` (general-purpose trigger tagger + program), `C-TG-<x>` (TrialGPT scores of system `B-F-<x>` or `C-TF-<x>`, set clin_v1/trialgpt_test). Other ids: `docs/RUN_MATRIX_{A,B,C,D}.csv`.

## Stage 2 (added 8 Oct): what C and B write so that the paper's stage-2 cells fill

Run ids follow C's first stage-2 runs (`C-S2-ctrl-verdict-triplets-s0`): `C-S2-<tier>-<system>[-s<k>]`, one run
holding every view it scores, one summary per view: `summary_<set>~<portion>@<cond>.json` (`"set":
"<set>/<portion>@<cond>"`). Seeds `-s0..-s4` are pooled as in stage 1. The paper's key is
`run/C-S2-<tier>-<system>/<set>:<portion>@<cond>/<slice>/<metric>`.

| Tier | `<tier>` | Views (`<set>:<portion>@<cond>`) | Fields |
|---|---|---|---|
| Rule-tier controls | `ctrl` | `rule_v1:test_L2@{none,wrong}`, `rule_v1:test_L3inv@{none,wrong}` | `all` {TA, Rev, Hold} |
| MedCalc-V criteria | `mcv` | `mcv_v1:criteria_test@{none,stated,self,wrong}` | `all`, `note_type={human,model}`, `stratum={stated,denied,default}`: {BalAcc, Acc, n} |
| MedCalc-V edits | `mcv` | `mcv_v1:edits_test@{none,stated,self,wrong}` | `all`, `note_type=human`, `edit_type={value,sentence}`: {TA, Rev, Hold, n} |
| Registered criteria | `reg` | `reg_v1:test@{stated,wrong}` | `all` {TA, Rev, Hold} |
| TrialGPT | `tg` | `clin_v1:trialgpt_test@{stated,wrong}` | top-level `macroF1` |
| Class triplets | `cls` | `cls_v1:test@{none,stated,wrong}` (none = closed book, stated = member list or gate) | `all` {TA, Rev, Hold} |
| Knowledge-base triplets | `kb` | `kb_v1:triplets_test@{none,derived,self,wrong}` | `all` {TA} |
| MedEinst | `me` | `clin_v1:medeinst_test@{none,derived,self,wrong}` | top-level `Reversal` (pair accuracy), `control_acc`, `trap_acc` |
| Key pairs | `kp` | `clin_v1:keypairs_medqa_oneway@{none,self,wrong}` | top-level `Reversal` |
| Stage-2 rule library | `rule2` | `rule_v2:test_L2@stated` | `all` {TA, Rev, Hold} |

Systems (`<system>`): `critic`, `verdict-blocks`, `verdict-triplets` (stage-1 adapters, seeds 0-4),
`v2-verdict-triplets`, `ledger-rm-g` (the composite as deployed), and its reference variants `reader-bit`,
`gate`, `gate-struct`. A `gate` run's summary also carries the top-level fields `gate_coverage`,
`parser_coverage`, `linking_acc`, `fallback_rate`, `malformed_rate` (percentages).

Comparisons (7)-(12): `results_git/C-S2-comparisons.json` = `{"p7": {"diff", "lo", "hi", "p", "n_clusters"},
..., "p12": {...}}`; a comparison dropped by its gate is written as `{"dropped": true, "reason": ...}`.
make_tables.py applies Holm over the members that are not dropped, once all six entries exist; keys
`cmp/p7/diff` ... `cmp/p12/padj`. The MedEinst executor audit: `results_git/C-S2-executor/summary.json`
(`test.both_decided`, `test.pair`; key `sum/C-S2-executor/<dotted field>`; the run needs its `DONE` file).

If your code already writes something else, say so in HANDOFFS and the lead changes the keys, not your files.
