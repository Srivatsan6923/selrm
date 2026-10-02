# rule_v1 data (role A)

## Getting the data
- Rebuild: `python scripts/build_rule_v1.py`. It takes about a minute and writes `data/rule_v1/<set>/{records.jsonl, MANIFEST.json}`, `data/rule_v1/FOLDS.json` and `data/REGISTRY.json`.
- The build is deterministic: every group is seeded by its id. Compare each set's `sha256` with the committed `data/REGISTRY.json`. A mismatch means the code version (`git_commit`) or the Python version (`python`) differs from the one recorded in the MANIFEST.
- The record files are not in git. They are also copied to the Shared Drive under `selrm/data/rule_v1/` with the same layout.

## Sets (fold 1)
| set | rules | templates | content |
|---|---|---|---|
| test_L2 | held-out signature classes | test | 2,000 groups: base, flip, near, pres |
| test_hard | held-out classes | test | 1,000 groups, tiers long, superseded and delabelled only |
| missing | held-out classes | test | missing twins of the first 1,000 test_L2 groups (same tids), each with one ordinary case (base or flip, alternating) |
| test_L0 | training rules | test | 1,000 groups (new patients) |
| test_L1 | L1 rules (unseen rules of seen classes) | test | 1,000 groups |
| test_L3alt | training rules, altered thresholds in the rule text | test | 1,000 groups; each flip value lies between the original and the altered threshold |
| test_L3inv | 60 invented rules (`rules_grammar.INVENTED`; never in training) | test | 1,000 groups |
| dev | training rules | test | 300 groups, `split = dev` |
| dev_missing | training rules | test | missing twins of the dev groups plus one ordinary case each: the threshold set for MR at 5% false rejection |
| readapply | training rules whose one-line cases decide the conclusion | test | 1,000 triplets with reading and application pairs |
| train_{natural, balanced, blocks, triplets} | training rules | train | 60,000 records each (plus at most 16), from one group pool |
| div_{base,new,same,patients}_{x} | training rules | train | A-D10 diversity curves: triplets corpora over x training rules (records proportional to x, 60k at 256): rules of new classes, of the two starting classes, or more patients for the same 16 rules. Sizes the library cannot fill are not built (see each MANIFEST `diversity`) |
| abl_nopres_triplets, abl_conclusion_triplets, abl_probe_blocks | training rules | train | A-D12 ablations: triplets without presentation edits (missing kept near 15%); triplets with conclusion claims only (60k records); train_blocks plus its groups' near and pres cases with `meta.probe = true` (never trained on; inputs for re-weighting). Decision-field / bit-only targets: `meta.criterion_holds`; ledger resampling: the ledgers of the other cases of a group |

Corpora, by case share:
- **natural.** One case per group, in blocks of 200 groups: 30 pres, 30 missing, 21 flip and 119 base.
- **balanced.** One case per group, in blocks of 20: 3 pres, 3 missing, 7 flip and 7 base.
- **blocks.** Base and flip from every group. In each block of 14 groups, 6 groups also give pres and 6 give missing.
- **triplets.** As blocks, but 7 of each 14 groups give near in place of base.

Near-miss kinds have equal shares in every set. Tiers are drawn with weights easy 2 : long 1 : superseded 1 : delabelled 1 among the tiers valid for the cell. The alt tier appears only in test_L3alt.

## Record conventions beyond docs/INTERFACES.md
- **Presentation edit** (`case_kind = pres`): the same facts as base. The line order and header frame change, and numeric values (current, or past with the same year) are reworded with the same value. Finding lines, superseded values and fillers keep their exact lines, so nothing but presentation changes.
- **Missing twin** (`case_kind = missing`). The base case with the decisive input unknown:
  - A measured value is omitted. A finding gets a "not recorded" line; there are 6 templates, 4 for train and 2 for test.
  - Both claims have label 0 (undetermined). The ledger status is `unknown`.
  - It is kept only if the base and flip completions reach both outcomes.
- **Reading and application pairs.**
  - Group ids are `<tid>.base` and `<tid>.flip`; case kinds are `read` and `apply`. `meta.source_tid` and `meta.origin` link them to the triplet `<tid>` in the same file.
  - `read` cases are the full base or flip case. The claims quote the decisive line: s quotes the base line, s' the flip line.
  - `apply` cases contain only the decisive line, after the header and setting, with the original claims.
  - The claim type is `conclusion`, so `metrics.decisions()` returns d.
  - The composition-gap events are:
    - P: d(read at `.base`) > 0 and d(read at `.flip`) < 0.
    - K: the same condition on apply.
    - U: d(base) > 0 and d(flip) < 0 at `<tid>`.
- **dev records** have `split = dev` and use test templates (`meta.tpl_split = test`).
- **Criterion claims** (`claim_type = criterion`) are emitted for constraint rules. TA uses `conclusion` only, so a scorer may skip criterion claims.
- **Folds 2 and 3:** `python scripts/build_rule_v1.py --fold 2` (and 3) writes `rule_v1_fold2/3` with test_L2, dev, train_blocks and train_triplets. It uses the fold assignment frozen in `data/rule_v1/FOLDS.json`.
- **Not built yet:** the rewritten tier (A-D11), and the diversity and ablation corpora (A-D10, A-D12).

## Scripts
- `scripts/sample_triplets.py <records.jsonl> 100`: readable triplets (docs/SAMPLE_TRIPLETS.md).
- `scripts/shortcut_scorers.py`: the Table 7 scorers on test_L2, written to `results/A-D14-<scorer>/`.
- `scripts/dataset_stats.py`: library, fold, overlap and dataset statistics, written to `results/A-D15/summary.json`.
- `selrm/reference.py`: `render_check_code(rec)` for B's GenPRM-style verifier and `reference_graph(rec)` for D's graph reward.

## Folds
`data/rule_v1/FOLDS.json` holds the signature classes (operator | input types | applicability: `cur`, or `ext` for past or family). For each fold it lists `l2_classes`, `l2_rules`, `l1_rules` and `train_rules`.
