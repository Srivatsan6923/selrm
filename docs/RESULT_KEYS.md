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
| Key pairs | system run id | `summary_clin_v1~keypairs_medqa.json` (and `_careqa`) top-level `Reversal` |
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
