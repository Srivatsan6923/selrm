# SelRM: Learning When to Change

Code, data builders and results for the paper *Learning When to Change: Symbolic Supervision for
Selective Evidence Sensitivity in Medical Reward Models* (target: NAACL 2027 via ARR).

Current draft: [`paper/learning_when_to_change_naacl2027_draft_v14.pdf`](paper/learning_when_to_change_naacl2027_draft_v14.pdf),
sources in [`paper/latex_v14/`](paper/latex_v14/).

**New to the project? Read this page, then your section of [`docs/TEAM_TASKS.md`](docs/TEAM_TASKS.md).**

## What we are doing

A reward model (verifier) for clinical reasoning should change its verdict when decisive evidence
changes, and keep it when a similar-looking but inapplicable mention appears (a relative's history,
a negated finding, a past value, a number just short of a threshold). We test both in one item, the
**rule triplet**: a base case, a *flip* (decisive edit) and a *near-miss* (same concept, does not
count under the rule). A triplet is solved only if the verifier is right on all three. Labels come
from an executed rule program, never from a model.

We then ask what training data makes a verifier pass this test, and where the result stops holding.

## What is done (stage 1, measured)

- Released medical reward models fail the test (Med-PRM solves about 12% of triplets, MedS3 10%,
  FoVer 32%).
- Training on decisive edits alone gives reversal without holding (53.7% of triplets on held-out
  rule structures). Putting near-misses into the same budget gives 91.8%; with a separate
  evidence-reading pass 98.5-99.2%.
- The trained verifiers follow edits to the rule itself (85-94% on rule-side items, 39% untrained).
- None of this transfers to benchmarks that state no criterion (MedEinst, MedQA/CareQA key pairs,
  answer selection). **The zero-shot medical-transfer claim is withdrawn** and reported as a
  negative result.
- As a training reward for a policy (GRPO): an outcome reward improves the policy; Med-PRM and the
  process-only ledger rewards are exploited and accuracy collapses.

Every number is in a results file and traced in [`docs/RESULTS_SUMMARY.md`](docs/RESULTS_SUMMARY.md).
Nothing in the paper is typed by hand: tables come from `scripts/make_tables.py`.

## What is pending (stage 2, opened 8 Oct)

One question: is the boundary above simply the absence of a criterion? We test it on clinical text
where the criterion has a source we did not write (MedCalc-Bench score definitions, DDXPlus
condition lists, registered trial criteria, drug and disease ontologies). The plan was committed
before any stage-2 data were built: [`docs/ANALYSIS_PLAN_STAGE2.md`](docs/ANALYSIS_PLAN_STAGE2.md)
(commit `733ad25`), six primary comparisons (7)-(12) with decision rules fixed in advance.

The draft has 215 unmeasured values and 33 open notes, all printed in red. Each has an owner in
[`docs/RED_CELLS.md`](docs/RED_CELLS.md); live status is on [`docs/STATUS_BOARD.md`](docs/STATUS_BOARD.md).

| Pending | Where it is tracked |
|---|---|
| Stage-2 data sets, training, scoring, tables | `STAGE2_TASKS_{A,B,C,D}.md` (compute side, run by Srivatsan on NRP) |
| Reading the data, checking citations, coding failures, writing | [`docs/TEAM_TASKS.md`](docs/TEAM_TASKS.md) (everyone, due Sun 11 Oct) |
| API-model rows of the audit and selection tables | [`docs/TEAM_TASKS.md`](docs/TEAM_TASKS.md), Basil |

## Who does what

| Person | Role | Tasks |
|---|---|---|
| Srivatsan | Lead. All GPU training and scoring (NRP), integration, tables, decisions | [`docs/TEAM_TASKS.md#srivatsan`](docs/TEAM_TASKS.md#srivatsan) |
| Basil | API-model runs and small training jobs; data reading | [`docs/TEAM_TASKS.md#basil`](docs/TEAM_TASKS.md#basil) |
| Charansai | Writing (Sections 1-4), data reading, citations | [`docs/TEAM_TASKS.md#charansai`](docs/TEAM_TASKS.md#charansai) |
| Hemashruthi | Writing (Sections 5-7, appendix J), stage-2 sample sheets, citations | [`docs/TEAM_TASKS.md#hemashruthi`](docs/TEAM_TASKS.md#hemashruthi) |
| Undergraduate assistant | Citation checks, proofreading, consistency checks | [`docs/TEAM_TASKS.md#undergraduate-assistant`](docs/TEAM_TASKS.md#undergraduate-assistant) |

## Repository map

| Path | Content |
|---|---|
| `selrm/` | Rule library, case engine, prompts, metrics |
| `scripts/` | Set builders, training, scoring, `make_tables.py`, `update_paper.py`, `build_paper.py` |
| `data/` | Frozen sets with manifests and hashes (`data/REGISTRY.json`); never edited after freezing |
| `results_git/<run_id>/` | Summary and per-example scores of every run behind a number |
| `tables/` | Generated LaTeX tables and `PROVENANCE.json` (which file each number comes from) |
| `paper/` | Drafts; `paper/patches/` holds prepared wording changes awaiting approval |
| `audit/`, `challenge_v1/`, `docs/ec_signoff/` | Sheets for the authors' reading tasks |
| `docs/` | Decisions, handoffs, status board, protocols, analysis plans |

## Ground rules

1. No number is typed, estimated or copied by hand. If a result does not exist the paper says so.
2. Frozen data are never edited. New data get a new name and are frozen before anything is scored.
3. Nothing is tuned on a test set.
4. A result that contradicts the paper changes the paper, not the result.
5. No API keys in the repository. Credentialed data never go to an external API.

## Quick start

```bash
git clone https://github.com/Srivatsan6923/selrm.git && cd selrm
pip install -r requirements-colab.txt        # only needed to run code
python tests/test_foundation.py              # sanity check
python scripts/make_tables.py                # regenerate tables from results
python scripts/build_paper.py                # build the PDF (needs tectonic or pdflatex)
```

Reading and writing tasks need no installation: a spreadsheet program, a text editor and git.
