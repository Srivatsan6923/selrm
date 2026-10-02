# SALVAGE: dataset build, state on 2 Oct 2026

Every file added or changed in the dataset build, what it does, its test status and
its known gaps. Work stopped here; nothing below is in progress.

**Test status.** `python -m pytest -q` runs 47 tests (about 10 s); all 47 passed on the
last full run. After that run only docstrings, comments and docs changed. `test_sets.py`
and `test_validate_shortcuts.py` run the scripts in a subprocess on small sizes.

**Checkpoint (Oct 2, shortcut validation): PASS.** `results/D0/validate_shortcuts.txt`:
8,820 generated triplets (441 cells x 2 splits x 10), 0 invariant violations, 11 of
8,831 proposals redrawn. It also passes on the built sets (`results/D1/validate_test.txt`,
`results/D2/validate_dev.txt`).

**Built locally, not in git** (deterministic from the seeds in the scripts, about 317 MB):
`data/test.jsonl` 2,000 triplets (500 from held-out families; tiers easy 1,200, long 250,
superseded 250, delabelled 150, alt 150; all 41 rules), `data/dev.jsonl` 300 (seen
families, 29 rules), `data/train/{balanced,flips,triplets,no_pres,conclusion_only}.jsonl`
60,000 examples each plus `manifest.json`. Logs in `results/D1`-`D3`.

## Rebuild

```
python -m pytest -q
python scripts/validate_shortcuts.py                 # shortcut validation
python scripts/make_set.py --set test                # data/test.jsonl
python scripts/make_set.py --set dev                 # data/dev.jsonl
python scripts/make_train.py                         # data/train/ (5 x 60,000)
python scripts/sample_triplets.py data/test.jsonl --out docs/SAMPLE_TRIPLETS.md
```

## Library: `selrm/`

| File | What it does | Tests | Known gaps |
|---|---|---|---|
| `rules.py` (changed) | Data model and the 11 pilot rules kept as they were. Added `Rule.cutoff` (constraint switches iff the points of met criteria reach it) and `Rule.verb`; 30 new rules: 10 constraint rules in seen families, 8 partial MedCalc-style scores, 12 grammar-composed rules in 4 held-out structural families (`G()`, `HELDOUT_FAMILIES`: any_of, all_of, two_of_three, score_cutoff) | `test_rules.py` (5): library shape, every criterion can decide its rule, stated threshold wording matches each operator, numeric ranges on the right side, cutoff execution. Pass | Stated rules are test specifications, not clinically validated. Scores are partial. The 12 grammar rules are curated compositions, not sampled from a grammar. 3 rules per held-out family gives wide CIs. Altered thresholds exist for 7 criteria |
| `phrases.py` (new) | Phrase banks for 38 concepts (702 templates) by form (generic, present, past, absent, rel, rel_past, delabelled, current, superseded). Train/test split by index parity for templates, fillers, header frames and person names. Cue lexicons `NEG_CUES`, `TIME_CUES`, `CURRENT_CUES`. Age-aware `persons()`. `NOUN`, `UNITS` for claims | `test_phrases.py` (9): required forms, slots, keyword discipline within each rule, value after keyword, cue split, person names, parity split, keyword-free fillers/settings/headers. Pass | Cue split covers the lexicon words only; years and words such as "since" occur in both splits. Generic absences are class-level ("No known drug allergies"). Weight and calf "superseded" lines are framed as recording errors, because a real change of that size in a day is impossible. Banks for the 20 new concepts had one semantic review; no clinician review |
| `engine.py` (new) | Triplet generation: `cells`, `pivots` (other criteria held met in cutoff families), `claims` (applicability, criterion, conclusion), executed `labels`, program `ledger`, `ledger_text`, `prose`, `make_triplet`, `check` (labels, single-criterion flip, keyword pattern, fillers, one-line edits, ledger quotes, presentation state) | `test_engine.py` (16): every cell in both splits passes `check`, fields and claims, corruption is caught, cutoff pivots, one-attribute near-misses, flip ways, ledgers and prose length, alt tier, tier sizes, header age, split-only phrases. Pass | Labels coincide across the three claim types by construction. Labels are executed on the state that produced the text; no independent text-to-state recovery check. Prose is template-rendered from the ledger. The presentation case always changes the header frame. Test-set near-miss kinds are time-heavy (837 of 2,000), since the superseded and delabelled tiers are time near-misses |
| `shortcuts.py` (new) | Shortcut scorers: always-default, concept-named, oracle (re-executes the program per claim type), naive number parser; `score()` | `test_shortcuts.py` (5). Pass | Trigger-lexicon and bag-of-words baselines from the paper's shortcut table are not implemented |
| `metrics.py` (new) | Rev, Hold, TA, PresHold, TieRate, BaseAcc, unnecessary revision; 95% CI by bootstrap over rules (default 1,000); `breakdown`; `paired` bootstrap difference | `test_metrics.py` (7). Pass | No Holm correction. No helper that turns two-order judge choices into d (belongs in `score.py`, not built). Correct revision equals Rev in this design and is not a separate statistic |

## Scripts: `scripts/`

| File | What it does | Tests | Known gaps |
|---|---|---|---|
| `validate_shortcuts.py` (new) | Shortcut validation on generated cells or a JSONL set; exit status 1 on any failure | `test_validate_shortcuts.py` (2): passes on generated triplets; reads a set and fails on a corrupted one. Pass | None known |
| `make_set.py` (new) | Test (2,000; test phrasing; 25% held-out families; 60/40 easy/hard) and dev (300; train phrasing; seen families) sets, stratified by family group and tier, round-robin over near-miss kinds and rules, duplicates redrawn | `test_sets.py` (2 of 3). Pass | Delabelled tier comes from 2 rules only. Dev deliberately excludes held-out phrasing and families |
| `make_train.py` (new) | Five corpora cut from one shared pool and shared draws: balanced, flips, triplets, no_pres, conclusion_only; 50/50 labels; adjacent pairs; manifest | `test_sets.py::test_training_corpora`. Pass | Examples keep text, claims, label and ledger, not the state (regenerable from `tid`). No prompt formatting yet (`finetune.py` not built). Tiers easy and long only, by design |
| `sample_triplets.py` (new) | Renders triplets from a set as Markdown | None | `docs/SAMPLE_TRIPLETS.md` was not generated |

## Tests, config, docs, results

| File | What it does |
|---|---|
| `tests/test_rules.py`, `test_phrases.py`, `test_engine.py`, `test_shortcuts.py`, `test_metrics.py`, `test_sets.py`, `test_validate_shortcuts.py` (new) | The 47 tests above |
| `pyproject.toml` (new) | pytest configuration (`pythonpath`, `testpaths`) |
| `.gitignore` (new) | Caches, paper binaries, generated data |
| `docs/DECISIONS.md` (filled) | Decision log for the build |
| `docs/SALVAGE.md` (new) | This file |
| `results/D0/validate_shortcuts.txt`, `results/D1/make_set_test.txt`, `results/D1/validate_test.txt`, `results/D2/make_set_dev.txt`, `results/D2/validate_dev.txt`, `results/D3/make_train.txt` (new) | Outputs of the runs above. Wall times: D1 1.0 s, D2 0.2 s, D3 35.7 s; D0 not logged |

Copied unchanged from the project pack: `docs/REVIEW_HISTORY.md`, `docs/RUN_MATRIX.csv`,
`notebooks/00_setup.ipynb`, `requirements-colab.txt`, `paper/latex/*`. Some planning
documents from the pack are kept locally and are not in version control.

## Known gaps, project level

1. A review pass over the built sets was stopped before it produced findings; nothing
   from it was applied.
2. `docs/SAMPLE_TRIPLETS.md` was not generated, and the 100-triplet read by hand for the
   Oct 3 checkpoint is still to do. A spot check of 20 random test triplets found no label
   or rendering defect.
3. `docs/RUN_MATRIX.csv` still lists D0-D3 as todo.
4. Not built: `judges.py`, `run_judge.py`, `score.py`, `configs/models.json`,
   `finetune.py`, `eval_local.py`, `medeinst_prep.py`, `rerank_medqa.py`,
   `make_tables.py`, `update_paper.py`. No API or GPU runs.
5. The remote `origin` is public; keep the built test set out of it.
