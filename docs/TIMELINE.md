# Development timeline (from git history and the files on disk)

Input for the appendix "Development History and Error Analysis" (`app:history` in
`paper/latex_v13/main.tex`), which the authors write themselves. Every entry below points to a
commit, a file line or a script output. Nothing here is an estimate.

**Sources.**
- `Symbolic_PRM_NAACL`: the old public repository in `D:/NAACL27` (github
  Srivatsan6923/Symbolic_PRM_NAACL; branches `main`, `selrm-dataset`; 2 commits). Its untracked and
  git-ignored files and the zip bundles in `D:/NAACL27` are not git history; they are cited as
  "file on disk" with their modification time.
- `selrm`: the private repository (github Srivatsan6923/selrm), read in the clone
  `D:/NAACL27/selrm-role-d` at the refs it held during the run of the script with `--disk` (started
  2026-10-03 00:52:00 -0700; section "Commits"): `main` at `201e360` (2026-10-02 23:37:02 -0700);
  `origin/main` at `129e5b4` (2026-10-03 00:31:27 -0700); `role-d` and `origin/role-d` at `a6bd390`
  (00:42:26); `origin/role-a` at `82d20a4`, `origin/role-b` at `25a659d` and `origin/role-c` at
  `ae5ad31` (2026-10-02 23:36:46 to 23:38:49 -0700). Present-tense statements about `selrm` refer
  to `selrm@129e5b4` (constant `NOW` of the script). The clone `D:/selrm` (role A) was read with
  `git log` only; the commits it has and this clone lacks (4 during that run, the oldest `dc758b3`
  of 2026-10-02 23:39:30 -0700) are not used. The other clones in `D:/NAACL27`
  (`selrm-role-b`, `selrm-role-c`, `selrm-merge`) were searched as files only (section "Pilot
  result on past/family rules").

**Conventions.**
- Git times are printed as `git log --date=iso` prints them, with the commit's offset (-0700 for
  every commit in the table; `selrm@c80a9a4`, cited in section "Pilot result on past/family
  rules", is -0500); file times use -0700.
- Zip entry times carry no timezone. For every bundle, the file's modification time converted to
  UTC is 1 to 60 minutes later than its newest entry (section "Bundles" of the script).
- Run logs use UTC (`Z`).
- `repo@hash` is a commit; `repo@hash:path` line N is a line of that file at that commit. A path
  with a line number next to a `selrm@` commit is read at that commit.
- "Project spec" is the specification file at the root of a bundle, a working tree or a commit,
  known by its line 1. In `selrm_handoff.zip` it is the only Markdown member (line 1 "# SelRM:
  selective evidence sensitivity in medical reward models"). In `selrm_autonomous_pack.zip` it is
  the member under `selrm_auto/` whose line 1 is "# SelRM: project spec (source of truth)"; the
  root file of the `D:/NAACL27` working tree with that line 1 has the same LF-normalised SHA-256
  (script section "Bundles"). In `selrm` it is the root file whose line 1 is "# SelRM: project spec
  (common to all four packages)".
- Counts that are not quoted from a file are printed by `python scripts/timeline.py`
  (read-only), in the section named in the evidence. `--disk` adds the search of the working
  trees. The script prints its own run time: "run took 89 s" for a run without `--disk` (started
  2026-10-03 01:03:22 -0700) and "run took 653 s" for the run with it (started 00:52:00).
  `python scripts/timeline.py --check` compares the first column of the table with git and with
  the file times and checks the order of the rows.

## Table

| Date and time | Event | Evidence |
|---|---|---|
| 2026-10-01 22:06:54 -0700 | Draft v10 saved as PDF; every experimental number in it is a placeholder. | file on disk `D:/NAACL27/learning_when_to_change_naacl2027_draft_v10.pdf`, modified 2026-10-01 22:06:54 -0700; `Symbolic_PRM_NAACL@c965184:paper/latex/README.md` lines 1, 18-20 |
| 2026-10-01 22:32:53 -0700 | Old public repository created with one file, `README`. | `Symbolic_PRM_NAACL@47c12e6` |
| 2026-10-01 22:49:58 -0700 | Handoff bundle saved. It holds the 11-rule library `selrm/rules.py`, with the same LF-normalised SHA-256 as the file later committed in `selrm@a6db79d` (earliest record of the 11 rules), and a project spec. The spec calls them "11 pilot rules" (lines 30-31), lists the engine as "TODO" (line 35), and specifies flips in which a first-degree relative's or a past finding counts where the criterion counts it (lines 54-55), a presentation case (line 63), and templates, relative names and cue words split train/test by index parity (lines 32-34). | file on disk `D:/NAACL27/selrm_handoff.zip`, modified 2026-10-01 22:49:58 -0700; members `selrm/selrm/rules.py` and the project spec; script section "Bundles" |
| 2026-10-01 22:50:11 -0700 | v10 LaTeX bundle saved. The draft says that some criteria count past or family findings and that such mentions are flips; its README lists held-out test templates and cue phrases in step 1 of its order of experiments. It also holds `SYMRM_INTEGRATION.md` on the earlier SymRM pilot. | file on disk `D:/NAACL27/learning_when_to_change_naacl2027_latex_v10.zip`, modified 2026-10-01 22:50:11 -0700; members `main.tex` lines 312-313 and 1051-1052, `README.md` lines 27-29 (same files in `Symbolic_PRM_NAACL@c965184:paper/latex/`) |
| 2026-10-01 23:02:49 -0700 | Old repository set up in `D:/NAACL27`: `origin` fetched and branch `main` created from `origin/main` (the reflog has no clone entry). | reflog of `D:/NAACL27` at 23:02:49: "fetch -q origin: storing head", "branch: Created from origin/main" (script section "Commits"); `Symbolic_PRM_NAACL@c965184:docs/DECISIONS.md` line 5 |
| 2026-10-01 23:22:04 -0700 | Project pack saved: project spec, docs (among them `REVIEW_HISTORY.md` and `PAPER_CONTEXT.md`), v10 sources and the same `selrm/rules.py`. Its project spec states "flip: counting mention (use family/past forms when the criterion counts them)" (lines 61-62) and "Presentation edits = 15% of label-0 cases (except the no-presentation ablation)" (lines 130-131). | file on disk `D:/NAACL27/selrm_autonomous_pack.zip`, modified 2026-10-01 23:22:04 -0700; script section "Bundles" |
| 2026-10-01 23:38:46 -0700 | Pack files written into the old repository's working tree. `docs/REVIEW_HISTORY.md` and `docs/RUN_MATRIX.csv` were committed later in `c965184`, with `notebooks/00_setup.ipynb`, `requirements-colab.txt` and `paper/latex/*`; the other pack files, among them `docs/STATE.md` and `docs/PAPER_CONTEXT.md`, are untracked. `docs/STATE.md` line 3: "Done: selrm/rules.py (11 pilot rules, applicability predicates)". | file on disk `D:/NAACL27/docs/STATE.md`, modified 2026-10-01 23:38:46 -0700; script section "Files on disk"; `Symbolic_PRM_NAACL@c965184:docs/SALVAGE.md` lines 62-64 |
| 2026-10-01 (date in file) | First dataset build (old repository) logs its decisions: 41 rules = 11 pilot rules and 30 new ones, among them 12 grammar-composed rules in 4 held-out structural families; train/test split of cue words; dev on train-split phrases. Rows 8-10 cite `selrm/engine.py` as evidence. | `Symbolic_PRM_NAACL@c965184:docs/DECISIONS.md` lines 5-14 (rows dated 2026-10-01) |
| 2026-10-02 00:33:34 -0700 | First build's shortcut validation written: "generated 8820 triplets (441 cells x 2 splits x 10)" ... "CHECKPOINT PASSED". Test, dev and training-corpus logs follow until 00:34:26. | file on disk `D:/NAACL27/results/D0/validate_shortcuts.txt`, modified 2026-10-02 00:33:34 -0700, lines 1 and 54; `D:/NAACL27/results/D3/make_train.txt` modified 2026-10-02 00:34:26 -0700; both also in `Symbolic_PRM_NAACL@c965184` |
| 2026-10-02 00:33:41 -0700 | First build's test and dev sets written to `D:/NAACL27/data/` (git-ignored); the five training corpora and their manifest follow from 00:34:21 to 00:34:26. Rebuilt from `c965184`, all eight files are byte-identical. In 135 of the 2,000 test flips the target finding counts only through past or relatives' mentions, 44 of them on migraine_cad, contra_vte or chadsvasc; in each training corpus, 2,929 of the 30,000 flip examples. | file on disk `D:/NAACL27/data/test.jsonl`, modified 2026-10-02 00:33:41 -0700; script section "First dataset build" |
| 2026-10-02 00:46:14 -0700 | Role packages A to D saved (00:46:14 to 00:46:17). Each holds the pilot generator `selrm/mini_engine.py`, `selrm/smoke.py`, `scripts/make_smoke.py` and `docs/MEASURED_FACTS.md`. None of these files is in an earlier bundle or anywhere in the old repository. | file on disk `D:/NAACL27/selrm_pkg_D_downstream_lead.zip`, modified 2026-10-02 00:46:14 -0700 (entries of these files 2026-10-02 07:12:34 to 07:17:00, no timezone); script section "Bundles" |
| 2026-10-02 00:46:19 -0700 | First dataset build committed on branch `selrm-dataset` of the old repository. Its engine draws each finding flip from the patient now, the past or a first-degree relative, the last two only where the criterion counts them, and renders a presentation case from the base state. | `Symbolic_PRM_NAACL@c965184`; `selrm/engine.py` lines 210-217 and 265; `tests/test_engine.py` lines 186-194 |
| 2026-10-02 00:57:25 -0700 | First commit of the private repository ("Package D: shared foundation and lead role"): the 11 pilot rules, the pilot generator (project spec line 78: "teammate's generator, 3 templates per form"), the smoke-data generator (3 held-out rules, 1 held-out template), `docs/MEASURED_FACTS.md`, the v10 sources. | `selrm@a6db79d` |
| 2026-10-02 00:57:49 -0700 | First dataset build copied into `salvage/` ("Salvage: first dataset build, kept for porting"); its `engine.py`, `rules.py` and `tests/test_engine.py` are the same blobs as in `c965184`. | `selrm@a725ffc`; `salvage/README.md` lines 3-6; script section "Bundles" |
| 2026-10-02 00:57:59 -0700 | Role A's specification committed: `engine.py` replacing `mini_engine.py`; at least 6 templates per mention form (indices 0-3 train, 4-5 test), with headers, cue words and relative names split the same way; flips in past or family form where the criterion counts them; `boundary` as its own near-miss kind; signature classes and three folds; "Core freeze: Saturday 3 Oct, evening." | `selrm@249f969`; `ROLE.md` lines 4, 7, 21-25, 28-31, 63-66 |
| 2026-10-02 02:27:36 -0700 | Role A's engine, phrase banks, folds and rule_v1 builder committed, with decisions on templates, signature classes and folds, missing twins, near-misses that mirror the flip, and invented rules for L3-inv. The flip form is drawn from patient, past and family where the criterion counts them. | `selrm@38277ca`; `docs/DECISIONS_A.md` lines 5-8, 16, 19; `selrm/engine.py` line 219 |
| 2026-10-02 02:36:33 -0700 | Final phrase banks; constraint batches C1-C3 and scoring batches S1-S2 merged. | `selrm@113f176` |
| 2026-10-02 02:48:11 -0700 | Scoring batch S4, value-neutral time forms, boundary tests. | `selrm@7adc5d6` |
| 2026-10-02 09:49 (UTC, as written in the file) | Round 1 of the pre-freeze review starts: four review sessions of 75 rendered groups each. | `selrm@6966837:docs/DATA_AUDIT_rule_v1.md` lines 373-378 |
| 2026-10-02 02:52:28 -0700 | Scoring batch S3 merged; age-consistent relatives. | `selrm@20e06cc` |
| 2026-10-02 02:56:25 -0700 | Diversity-curve and ablation corpora. | `selrm@2b8eff9` |
| 2026-10-02T10:13:37Z | First logged training step of role B's smoke runs on data from the pilot generator (verdict x blocks; verdict x triplets at 10:17:52Z), backbone Qwen3.5-9B. | `results_git/B-C0-smoke-verdict-blocks-s0/run.log` line 1 and `results_git/B-C0-smoke-verdict-triplets-s0/run.log` line 1, added in `selrm@465befc`; script section "First logged training steps" |
| 2026-10-02 10:14 (UTC, as written in the file) | Round 2 of the pre-freeze review starts: two sessions of 75 new groups each. | `selrm@6966837:docs/DATA_AUDIT_rule_v1.md` lines 379-380 |
| 2026-10-02 03:15:10 -0700 | Pre-freeze audit 1 and its fixes logged: "four independent readers checked 300 rendered groups"; "No base, flip, near or pres label was wrong under a literal reading." | `selrm@cbd80b9`; `docs/DECISIONS_A.md` line 24 |
| 2026-10-02 03:35:24 -0700 | Audit round 2, reader B (75 groups): "no label errors"; fixes applied. | `selrm@33506cb`; `docs/DECISIONS_A.md` line 25 |
| 2026-10-02 03:39:01 -0700 | Smoke comparison committed, titled "(PROVISIONAL, never reported)": TA on the three held-out pilot rules 99.7 (blocks) and 100.0 (triplets); on training rules with the held-out template 87.3 and 97.3. | `selrm@465befc`; `docs/SMOKE_B_C0.md` lines 1, 8, 12-13, 34, 38-39 |
| 2026-10-02 03:44:09 -0700 | Audit round 2, reader A (75 groups): "no label errors"; fixes applied. | `selrm@b2f7463`; `docs/DECISIONS_A.md` line 26 |
| 2026-10-02 03:46:53 -0700 | Code version from which all 38 frozen sets were built (`git_commit` of every MANIFEST at the freeze). | `selrm@59034a3`; script section "Freeze" |
| 2026-10-02 03:50:32 -0700 | Freeze: "Freeze rule_v1 (fold 1) and rule_v1_fold2/3". `data/REGISTRY.json` lists 38 sets, each with its sha256 and `"frozen": true`; MANIFESTs and FOLDS committed; shortcut validation PASS on 12 sets: the 11 test and dev triplet sets and `readapply`, which holds 1,000 triplets and reading and application pairs (its MANIFEST `note`). | `selrm@e40789b`; script section "Freeze" |
| 2026-10-02 05:22:39 -0700 | Role B queues the seed-0 factorial: 20 runs on rule_v1. | `selrm@0661a00` |
| 2026-10-02 05:32:18 -0700 | Role B logs that rule_v1, rebuilt in the cluster and on a laptop, matches the registry sha256 for all 30 fold-1 sets. | `selrm@452a6e9`; `docs/DECISIONS_B.md` line 40 |
| 2026-10-02T12:50:08Z | First logged training step on a frozen rule_v1 corpus (verdict x triplets; verdict x blocks at 12:50:12Z). The freeze commit is 10:50:32Z; none of the 11 rule_v1 runs with a step log logged a step before it. | `results_git/B-F-verdict-triplets-s0/run.log` line 1, added in `selrm@a8d4111`; script section "First logged training steps" |
| 2026-10-02 06:06:25 -0700 | Role B logs the concept scorer's check on the held-out smoke rules: "TA 0.2 (always the default)". | `selrm@f260922`; `docs/DECISIONS_B.md` line 45 |
| 2026-10-02 07:59:00 -0700 | First rule_v1 results, seed 0: TA on test_L2 58.2 (verdict x blocks) and 91.3 (verdict x triplets). | `selrm@a8d4111`; `results_git/B-F-verdict-blocks-s0/summary_rule_v1~test_L2.json` line 8, `results_git/B-F-verdict-triplets-s0/summary_rule_v1~test_L2.json` line 8 |
| 2026-10-02 08:43:42 -0700 | ledger2 x blocks, seed 0: TA on test_L2 75.3. | `selrm@09fd29c`; `results_git/B-F-ledger2-blocks-s0/summary_rule_v1~test_L2.json` line 8 |
| 2026-10-02 09:25:05 -0700 | New corpora under new names (leave one near-miss kind out; near-miss dose), built with `--only`; the new code reproduces four frozen sets byte-identically. | `selrm@a8add2d`; `docs/DECISIONS_A.md` line 27 (added in `selrm@3e0c832`) |
| 2026-10-02 09:26:57 -0700 | The 6 new sets frozen; the registry has 44 entries and none of the 38 sha256 values of the freeze changed. | `selrm@3e0c832`; script section "Freeze" |
| 2026-10-02 09:47:58 -0700 | ledger2 x triplets, seed 0: TA on test_L2 99.2. | `selrm@c3bdac6`; `results_git/B-F-ledger2-triplets-s0/summary_rule_v1~test_L2.json` line 8 |
| 2026-10-02 21:43:52 -0700 | Lead merges role-a into main; role-b at 21:49:18 (`selrm@b47dd33`) and role-c at 21:49:23 (`selrm@d6429e1`). | `selrm@13b09b0` |
| 2026-10-02 21:44:41 -0700 | Final-task bundle saved: FINAL_TASKS_A to D, HUMAN_TASKS and the v13 sources, which add the appendix "Development History and Error Analysis" (v10's `main.tex` has no such section). | file on disk `D:/NAACL27/selrm_final_tasks (1).zip`, modified 2026-10-02 21:44:41 -0700 (entries 2026-10-03 04:42:56, no timezone) |
| 2026-10-02 21:53:58 -0700 | Lead's local rebuild of rule_v1 fold 1 finished (folds 2 and 3 at 21:55:29 and 21:56:02); all 44 sets match the registry sha256. | file on disk `D:/NAACL27/rule_v1_rebuild/build_f1.log`, modified 2026-10-02 21:53:58 -0700; `selrm@1a670f0:docs/DECISIONS_D.md` line 9 |
| 2026-10-02 21:57:23 -0700 | v13 sources committed; the appendix paragraph on the pilot carries the placeholder `\ph{59.7}`. | `selrm@1a670f0`; `paper/latex_v13/main.tex` lines 1955-1973 (placeholder line 1963) |
| 2026-10-02 21:58:45 -0700 | Branch `selrm-dataset` of the old repository (first dataset build, `c965184`) pushed to its public origin. | reflog of `D:/NAACL27`: `refs/remotes/origin/selrm-dataset@{2026-10-02 21:58:45 -0700}: update by push` |
| 2026-10-02 22:00:00 -0700 | Role C registers the TrialGPT sets `clin_v1/trialgpt_dev` and `clin_v1/trialgpt_test`, frozen, in a registry of their own. | `selrm@d91a6a1`; `data/clin_v1/REGISTRY_C.json` |
| 2026-10-02 22:18:57 -0700 | Role A's audit of rule_v1 committed on `role-a`, with a section on who reviewed the 450 pre-freeze groups. | `selrm@6966837`; `docs/DATA_AUDIT_rule_v1.md` lines 362-414 |
| 2026-10-02 22:31:16 -0700 | Rule-side items `xr_v1` built and frozen on `role-a` as a separate set: 400 items, 100 each for window, currency, subject and inclusivity; registry entry `xr_v1/test`. | `selrm@2df9308`; `docs/DECISIONS_A.md` line 30; `docs/HANDOFFS.md` line 8 |
| 2026-10-02 22:38:03 -0700 | On `role-a`: a leave-boundary-out corpus frozen and further names registered as aliases of frozen corpora (registry: 52 entries, the last change to `data/REGISTRY.json` on any ref); no sha256 of the 38 sets frozen at the freeze changed on any branch. | `selrm@11f77f7`; script section "Freeze" (registry per branch) |
| 2026-10-02 22:46:41 -0700 | Lead merges role-a into main (the audit, `xr_v1`, the `challenge_v1` kit, the new corpora); role-b at 22:46:51 (`selrm@255f72b`) and role-c at 22:48:59 (`selrm@ec31d81`). | `selrm@6f6db69` |
| 2026-10-02 23:08:07 -0700 | Role C registers the MedEinst sets in `data/clin_v1/REGISTRY_C.json`; key pairs (23:23:24, `selrm@602f552`), NLI4CT-P sets (23:28:09, `selrm@e7b92b6`) and clinical training pairs (23:33:06, `selrm@1e751fe`) follow, merged into main at 23:37:02 (`selrm@201e360`). That registry then has 16 entries, all frozen. | `selrm@ac8eb3b`; script section "Freeze" |

## Pilot

The records use "pilot" for three different things.

1. **The SymRM pilot**, an earlier study used as a source for draft v5.
   `paper/latex/SYMRM_INTEGRATION.md` (in the v10 bundle and in `Symbolic_PRM_NAACL@c965184`)
   line 9: "(10 rules, 300 scenarios, 3 far-OOD rules"; line 55: "The pilot ran on an 8 GB laptop
   GPU with Qwen2.5-1.5B and Qwen3-4B (4-bit)." Line 3 names its sources ("the SymRM Gate 2a
   dashboard, the Phase 3 report and the dataset audit page"); none of them is in these
   repositories or bundles. It is not the 11-rule generator.
2. **The 11 pilot rules and the pilot generator**, which the v13 appendix describes.
3. **The audit pilot C-P0** (300 test triplets x 5 models). Planned for "Sun 4 Oct"
   (`selrm@a6db79d:docs/TEAM_PLAN.md` lines 21-22: "B seed-0 grid and C pilot (Sun 4 Oct)"; project
   spec of the same commit, line 102: "Pilot (C, 4 Oct)"). Status "todo" in
   `selrm@1a670f0:docs/RUN_MATRIX_C.csv` line 4, and still "todo" on `origin/role-c` and at
   `selrm@129e5b4`.

**What the pilot generator was** (files at `selrm@a6db79d`):
- Rules: `selrm/rules.py`, list `RULES` at lines 140-232 under the comment of line 137 ("# Pilot
  library. ..."). The script lists 11 rules: strep_amox, t2d_metformin, htn_pregnancy,
  vte_platelets, pain_ulcer, statin_alt, gout_clarith, migraine_cad, contra_vte, curb65,
  chadsvasc. Criteria that count past findings occur in migraine_cad, contra_vte and chadsvasc;
  only contra_vte counts first-degree relatives (lines 188-202, 219-231; script section "Pilot
  generator").
- Generator: `selrm/mini_engine.py` line 1: "Minimal triplet generator for a first training run
  (stand-in for engine.py)." Its rendering part has 14 form keys with 3 templates each and 3
  header frames (lines 124-146; script). Every set draws the template index the same way
  (`rng.randrange(60)`, line 203), so sets made with different seeds share the same 3 templates.
- Flips are always a current mention of the patient (`flip = bg + [Mention(c.concept,
  "finding")]`, line 34; numerics line 44), also for criteria that count past or family findings.
  Past and other-person mentions appear only as near-misses. Each triplet has base, flip and near
  cases only (line 207).
- Smoke data built on it (`selrm/smoke.py`, same commit), lines 5-7: "It already holds out
  rendering templates and whole rules, so the first flips-vs-triplets comparison can be run on it.
  It is NOT the paper's dataset: 11 rules, short notes, no hard tiers, no ladder, no missing
  twins." Line 18: `HELDOUT_RULES = ("migraine_cad", "contra_vte", "vte_platelets")`; line 19:
  `TRAIN_TPL, TEST_TPL = (0, 1), (2,)`; presentation cases for a share of groups (`pres_share=0.15`,
  line 116).
- Who and when. The 11-rule file is first recorded in `selrm_handoff.zip` (file modified
  2026-10-01 22:49:58 -0700), whose project spec already calls them "11 pilot rules" (lines
  30-31). `mini_engine.py`, `smoke.py` and `MEASURED_FACTS.md` are first recorded in the role
  packages (files modified 2026-10-02 00:46:14 to 00:46:17 -0700; zip entry of `mini_engine.py`
  2026-10-02 07:12:34, no timezone) and first committed in `selrm@a6db79d` (2026-10-02 00:57:25
  -0700). The project spec of that commit calls `selrm/mini_engine.py` the "teammate's generator, 3
  templates per form" (line 78), and `docs/MEASURED_FACTS.md` line 1 dates the notebook
  measurements: "# Measured facts (2 Oct, teammate's Colab notebook)". Which teammate wrote the
  generator, and when, is not recorded. The first dataset build (section "Redesign") is a
  different generator.
- Train/dev template sharing: `docs/MEASURED_FACTS.md` lines 21-22: "Neither number is reportable:
  dev shared 176 of 178 line templates with training."

**Training results on smoke data (before the freeze).**
- The notebook run: `docs/MEASURED_FACTS.md` lines 19-22: "Zero-shot Qwen3.5-9B on an
  in-distribution smoke dev set (278 triplets): Rev 82.0, Hold 85.3, TA 70.9; numeric near-miss
  Hold 63.2. After training on triplets: 100/100/100 on the same in-distribution dev." The file
  does not name the generator the run used; it is first recorded together with `mini_engine.py`
  (same packages, same commit `selrm@a6db79d`). The notebook, its prompt format and its outputs
  are not in any repository or bundle.
- Role B's smoke runs on smoke_v2 (Qwen3.5-9B, format verdict; `results_git/B-C0-smoke-*/meta.json`):
  `docs/SMOKE_B_C0.md` (`selrm@465befc`) line 3: "these numbers never enter a table". TA on
  `smoke_v2/test_heldout_rules` (held-out rules and template, n = 600): 99.7 (blocks) and 100.0
  (triplets), lines 12-13; on `smoke_v2/dev_seen_rules` (training rules, held-out template, n =
  300): 87.3 (blocks) and 97.3 (triplets), lines 38-39. The later pipeline checks on the same
  held-out set (other formats and backbones) report TA between 93.5 and 100.0, except the concept
  scorer at 0.2 (script section "Pilot generator", list of runs).

## Pilot result on past/family rules

- No file records the value 59.7 as a result of the pilot, and no file records a run in which a
  model trained on pilot-generator data was tested on cases where a past or family finding counts.
- Search (script section "Search", run with `--disk` started 2026-10-03 00:52:00 -0700). A hit is
  a number that rounds to 59.7 (59.65 to below 59.75, or a share from 0.5965 to below 0.5975) or
  that contains the characters 59.7. Searched: every file version committed on any ref of both
  repositories (1,561 blobs in `selrm`, 39 in `Symbolic_PRM_NAACL`); every member of the 9
  bundles, including the v10 zip nested in the project pack; and, with `--disk`, 12,727 files
  under `D:/NAACL27` (every clone in it) and `D:/selrm`. PDFs are read as text page by page, zip
  and tar archives member by member, gzip, bz2 and xz files unpacked. Not searched: files with a
  NUL byte that are none of these (model weights, arrays, pickles, parquet files, executables;
  the script lists them by extension) and 10 test files of the joblib package in role C's
  virtual environment that do not open as gzip. Two kinds of hits are counted, not listed:
  per-item score margins (`"u": 0.597...` in score files; 13 in 9 files of git history, 112 in 50
  files of the working trees) and training progress (`epoch=0.5973` in run logs; 11 in git
  history, 45 in the working trees). The other hits are of three kinds.
  - The placeholder and copies of it. `paper/latex_v13/main.tex` line 1963 at `selrm@1a670f0`
    (line 2052 at `selrm@129e5b4`); the v13 sources are on `main` and `role-d` only, and on disk
    in the clones `selrm-role-d` and `selrm-merge`; the final-task bundle's copy (line 1968). The
    v13 PDF, page 22, "it solved 59.7%": `selrm@1a670f0:paper/learning_when_to_change_naacl2027_draft_v13.pdf`,
    the same PDF in the final-task bundle, at `D:/NAACL27/learning_when_to_change_naacl2027_draft_v13.pdf`
    and in `paper/` of `selrm-role-d` and `selrm-merge`. Builds: `D:/NAACL27/tools/v13build/main.tex`
    line 1963 and `main.pdf` page 22; the git-ignored `paper/build/main.tex` line 2052 and
    `main.pdf` page 23 in `selrm-role-d`. `docs/PAPER_NUMBERS.md` line 273 (`selrm@fdcf5a7`), the
    lead's list of the paper's numbers, which says of it "No run in RUN_MATRIX_* reproduces it and
    no results/ run holds it."; `docs/STATUS_BOARD.md` line 16 (`selrm@2d030db`): "v13 App. H says
    the pilot model solved 59.7% on held-out rules where a past or family finding counts; no file
    records that test"; this file and `scripts/timeline.py`.
  - Other quantities in result files of `selrm`, all written after the freeze. Role B's
    Qwen3.5-4B verdict x blocks run: `results_git/B-BB-qwen3.5-4b-verdict-blocks-s0/run.log` line
    98, "rule_v1/dev: TA 59.0 Rev 99.3 Hold 59.7 n=300", the same Hold as `59.666666666666664` in
    `summary_rule_v1~dev.json` lines 7 (all) and 34 (level L0) and `meta.json` line 152 of that
    run (`selrm@f16af67`). `results_git/B-F-rationale-blocks-s0/summary_rule_v1~test_hard.json`
    line 160, lower end of the TA interval, `59.747817652764304` (`selrm@f16af67`). Both values
    are copied into `docs/assets/data.js` line 2 (`selrm@c80a9a4`), the data file of the status
    pages. `results_git/B-F-verdict-natural-s0/summary_rule_v1~test_L3inv.json` line 25 (Hold,
    tier easy, `59.77742448330684`) and line 80 (TA, tier long, `59.701492537313435`)
    (`selrm@3834b8f`), where test_L3inv holds the 60 invented rules
    (`selrm@38277ca:docs/DECISIONS_A.md` line 19). Role C's TrialGPT runs:
    `results_git/C-TG-critic-dev/summary_clin_v1~trialgpt_dev.json` line 95, `"acc":
    59.701492537313435` (`selrm@4c6b46c`), and `results_git/C-TG-ledger2-blocks-dev/meta.json`
    line 53, `"wall_seconds": 1059.7` (`selrm@cfe37bb`). The same files are in the working trees
    of the clones.
  - Only in working trees, not in any ref of this clone. Role B's clone:
    `D:/NAACL27/selrm-role-b/results_git/B-F-verdict-blocks-s2/summary_rule_v1~test_L3inv.json`
    line 52, `"Hold": 59.683794466403164`. Role C's clone: `scratch/bres/vb.json` line 198,
    `"macro": 59.78388589724916`; `scratch/noise_fake/topk_rule_v1~dev.jsonl` lines 1137 and 1220
    (`top_logits` values `0.5968952703395868` and `0.5971213665131236`); a clinical-trial record in
    its download of the NLI4CT release, `data/clin_v1/nli4ct_raw/training_data.zip`, member
    `CT json/NCT03346161.json` line 37 ("percentage of answers correct  59.7"); a test file of numpy
    in `scratch/venv_ctx` (`numpy/lib/tests/test_function_base.py` line 2594, `0.5969`); and
    copies of committed result files in `scratch/bcode/`.
- The held-out-rule test that exists for pilot-generator data is `smoke_v2/test_heldout_rules`.
  Two of its three rules state that past findings count, migraine_cad ("If the patient has ever
  had coronary artery disease (current or past)", `selrm@a6db79d:selrm/rules.py` lines 189-190)
  and contra_vte ("If the patient or a first-degree relative (parent, sibling or child) has had a
  venous thromboembolism at any time", lines 195-197). They supply 1,616 of its 2,400 cases.
- In smoke_v2 rebuilt from `selrm@a6db79d` (same item ids as role B's score file), no case in any
  file has a past or family mention that makes the criterion hold: 0 of 6,467 cases in each
  training corpus, 0 of 1,200 in dev, 0 of 2,400 in the held-out test. In the triplets corpus 859
  cases contain a past or other-person mention of the target concept, and none of these mentions
  makes the criterion hold (script section "Pilot generator"). None of the 600 triplets behind the
  TA of 100.0 (`docs/SMOKE_B_C0.md` line 13) has a past or family mention that counts.
- Part of the appendix sentence is supported: in pilot-generator data, past and family mentions
  never count (the counts above; `selrm/mini_engine.py` line 34). This holds for the pilot
  generator only: the first dataset build made such mentions count in its flips (section
  "Redesign").

## Redesign

**Statements in the records that bear on the reasons.**
- `docs/MEASURED_FACTS.md` (`selrm@a6db79d`) lines 21-22, template overlap (quoted above); lines
  23-24: "Numeric near-misses in that run included values exactly at the threshold; report those
  as the separate kind `boundary`."
- The generator is a stand-in: `selrm/mini_engine.py` line 1; `selrm/smoke.py` lines 6-7 (quoted
  above); role A's `ROLE.md` (`selrm@249f969`) line 7 lists deliverable A-D0, `selrm/engine.py`
  "replacing `mini_engine.py`".
- Design statements older in the records than the pilot generator (v10 bundle, file modified
  2026-10-01 22:50:11 -0700): `main.tex` lines 312-313: "In \ph{23}\% of criteria a past or family
  finding counts, so no global heuristic about time or subject is correct."; lines 1051-1052: "For
  criteria whose predicate counts past or family findings, such mentions are flips."; `README.md`
  lines 27-29: "test templates and cue phrases held out from training".
- Review history (`docs/REVIEW_HISTORY.md`, in the project pack and in `selrm@a6db79d`; the passes
  carry no dates). Line 17 (review of v5, change in v6): "Applicability is a per-criterion predicate
  A_j; in a stated share of criteria past or family findings count and are flips". Line 135 (review
  of v8, change in v9): "Templates shared between training and test allow shortcuts | Valid: v8
  reported 100% shared templates | Test templates and cue phrases (relatives, negation, time) are
  now held out".
- No file gives a measured failure on rules where past or family findings count as a reason for
  the redesign.

**Generator designs in the records before rule_v1**, in the order of their first record.
1. The handoff spec (`selrm_handoff.zip`, file modified 2026-10-01 22:49:58 -0700) specifies an
   engine that is not yet written (line 35 lists `selrm/engine.py` as "TODO"). Lines 54-55:
   "flip: finding -> patient/present/current (if counts_family: sometimes a first-degree relative;
   if counts_past: sometimes past form)"; line 63: "pres: base state re-rendered with other
   templates and order"; lines 33-34: "templates split train/test by index parity; relative names
   and cue words split too." The project pack's spec (file modified 2026-10-01 23:22:04 -0700)
   repeats the flip rule (lines 61-62) and sets presentation edits at 15% of label-0 cases (lines
   130-131).
2. The first dataset build (`Symbolic_PRM_NAACL@c965184`): decision rows dated 2026-10-01 that
   cite `selrm/engine.py` (`docs/DECISIONS.md` lines 8-10), sets written 2026-10-02 00:33:41 to
   00:34:26 -0700, committed 00:46:19.
   - Flips in which a past or a first-degree relative's finding counts. `selrm/engine.py` lines
     210-217, `counting()`: "A finding mention that the criterion counts: the patient now, or the
     past or a first-degree relative where the predicate counts those.", drawn by `way =
     rng.choice(["patient"] + ["past"] * c.counts_past + ["family"] * c.counts_family)` (line
     213; line 213 of `salvage/selrm/engine.py` at `selrm@a725ffc`, the same blob).
     `tests/test_engine.py` lines 186-194 (`test_flips_cover_patient_past_and_family_ways`, rule
     contra_vte) requires all three ways. `docs/DECISIONS.md` line 15 (dated 2026-10-02) mentions
     "family flips".
   - Counts (sets rebuilt from `c965184`, byte-identical to the files in `D:/NAACL27/data/`;
     script section "First dataset build"): in `test.jsonl`, the target finding of 135 of the
     2,000 flips counts only through past or relatives' mentions (131 of them past only), 44 of
     them on the pilot rules migraine_cad, contra_vte and chadsvasc; in `dev.jsonl`, 18 of 300 (6
     on those rules). In each of the five training corpora, 2,929 of the 30,000 flip examples
     have counting ledger entries that are all past or relatives' (1,066 of them on the 11 pilot
     rules).
   - Presentation edits: `selrm/engine.py` line 265 ("# 3. Presentation edit: the base state with
     other templates, header and order."); `pres_share_of_label0` in `data/train/manifest.json`:
     0.1497 (balanced, flips), 0.1501 (triplets, conclusion_only), 0.0 (no_pres).
   - Held-out phrasing and structures: `docs/SALVAGE.md` line 36: "30 new rules: 10 constraint
     rules in seen families, 8 partial MedCalc-style scores, 12 grammar-composed rules in 4 held-out
     structural families"; line 37: "Phrase banks for 38 concepts (702 templates) ... Train/test
     split by index parity for templates, fillers, header frames and person names."
   - No missing-input cases: every triplet of `test.jsonl` and `dev.jsonl` has the cases base,
     flip, near and pres only, and the training corpora have no other case kinds (script).
   - It was copied into the private repository as `salvage/` (`selrm@a725ffc`). `salvage/README.md`
     lines 3-5: "The first dataset build (1-2 Oct), kept for reference. Role A ports what fits
     (rules, phrase banks, engine pieces) to the record format in `docs/INTERFACES.md` and
     `selrm/schema.py`".
3. The pilot generator (`selrm/mini_engine.py`; first recorded in the role packages of 2026-10-02
   00:46:14 to 00:46:17 -0700, committed in `selrm@a6db79d`): flips always a current mention of
   the patient (section "Pilot").

When the pilot generator was written is not recorded, so the records do not show which of the two
generators was written first. By date of record, the specification of past and family flips (1)
and the first build's decision rows (2) are older than any record of the pilot generator. A
statement of the same age concerns some generator with shared templates: `docs/REVIEW_HISTORY.md`
line 135 (in the project pack, file modified 2026-10-01 23:22:04 -0700) says that draft v8
"reported 100% shared templates". It does not name the generator, and no file of draft v8 is in
these repositories or bundles.

**When rule_v1 was made.** Specified in role A's `ROLE.md` (`selrm@249f969`, 2026-10-02 00:57:59
-0700), implemented from `selrm@38277ca` (02:27:36) to `selrm@59034a3` (03:46:53), frozen in
`selrm@e40789b` (03:50:32).

**What rule_v1 contains**, item by item against the appendix paragraph "What changed", with what
the earlier versions had:
- Held-out signature classes. `docs/DECISIONS_A.md` line 7 (`selrm@38277ca`): "Signature class =
  operator (single, any, all, k-of-n, score) x input types (numeric, finding, mixed) x
  applicability (current only, or past/family)." `data/rule_v1/FOLDS.json` at the freeze: 21
  classes; fold 1 holds out 5 classes (103 L2 rules) and keeps 223 training rules and 27 L1 rules
  (script section "Freeze"). Earlier: the first build held out 4 structural families of 3 rules
  each (`Symbolic_PRM_NAACL@c965184:docs/DECISIONS.md` line 6); the smoke data built on the pilot
  generator holds out 3 whole rules, not structures (`selrm/smoke.py` line 18).
- Held-out templates and cue phrases. `docs/DECISIONS_A.md` line 6: "Phrase banks use 6 templates
  per concept and form (0-3 train, 4-5 test). Headers, fillers, people and cue lexicons for
  negation, time and current use the same split." `results/A-D15/summary.json` lines 49-54 (at
  `selrm@e40789b`): `"templates_train": 1032`, `"templates_test": 516`, `"templates_shared": 0`,
  `"cue_words_train": 14`, `"cue_words_test": 19`, `"cue_words_shared": 0`. Earlier: the first
  build split templates, fillers, header frames, person names and cue lexicons by index parity
  (`docs/SALVAGE.md` line 37, `docs/DECISIONS.md` line 11); the pilot generator's sets share its 3
  templates per form, of which the smoke data holds out one (`selrm/smoke.py` line 19).
- Rules under which past or family findings count. FOLDS `class_def`: "operator|inputs|applicability
  (cur, ext = past or family)"; 9 of the 21 classes and 181 of the 353 rules are `ext`; in fold 1,
  93 of the 223 training rules and 76 of the 103 L2 rules (script). `selrm/engine.py` draws the
  flip from patient, past and family where the criterion counts them (line 219 at `selrm@38277ca`,
  line 253 at `selrm@59034a3`). Flip cases whose decisive finding counts only through past or
  relatives' mentions: 513 of 5,623 in `train_triplets` (467 of them with every counting mention
  in the past) and 273 of 2,000 in `test_L2` (script; records rebuilt and checked against the
  registry sha256). `docs/PAPER_VS_CODE.md` (`selrm@6966837`) lines 82-84, on the share of
  criteria that count past or family findings: "30.5% of the 791 criteria of the library. Among
  the 459 finding criteria alone it is 52.5%." Earlier: three of the 11 pilot rules already state
  that past or family findings count (section "Pilot"), and the first build made such flips (item 2
  above); the pilot generator never did.
- Presentation edits and missing inputs. `record_share` in the MANIFESTs of the four main training
  corpora at the freeze (script): `pres` 0.15 (natural), 0.1509 (balanced), 0.1502 (blocks),
  0.1498 (triplets); `missing` 0.1488, 0.1501, 0.1501, 0.1497. Of the 24 training, ablation and
  diversity corpora at the freeze (`train_*`, `abl_*`, `div_*`; 31 at `selrm@129e5b4`), every one
  has missing-input cases and every one except `abl_nopres_triplets` has presentation cases; that
  corpus, the no-presentation ablation, has `record_share` base 0.2119, flip 0.4242, missing
  0.1516, near 0.2123 (script). Earlier: presentation edits were in the first build (0.1497 to
  0.1501 of label-0 cases, none in its `no_pres` corpus) and in the smoke data
  (`selrm/smoke.py` line 116); neither had missing-input cases (`selrm/smoke.py` line 7; script
  section "First dataset build").
- `boundary` as a near-miss kind of its own: role A's `ROLE.md` lines 30-31 (`selrm@249f969`).

## Freeze

**Audits before the freeze.**
- `docs/DECISIONS_A.md` line 24 (`selrm@cbd80b9`, 03:15:10): "Pre-freeze audit 1: four independent
  readers checked 300 rendered groups (train and test templates, every kind and tier, with missing
  twins). No base, flip, near or pres label was wrong under a literal reading." The same line lists
  ten classes of fixes.
- Line 25 (`selrm@33506cb`, 03:35:24): "Audit round 2 (reader B, 75 fresh groups): no label errors".
  Line 26 (`selrm@b2f7463`, 03:44:09): "Audit round 2 (reader A, 75 fresh groups): no label errors."
- `docs/SUMMARY_A.md` line 51 (`selrm@969d3d0`): "Two audit rounds (6 readers, 450 rendered groups)
  found no label errors."
- Who the readers were, written after the freeze in `docs/DATA_AUDIT_rule_v1.md` (`selrm@6966837`,
  in main since `selrm@6f6db69`); this is what the v13 placeholder at lines 1288-1289 of
  `selrm@1a670f0:paper/latex_v13/main.tex` asks for ("\ph{[state who reviewed them and what they
  were asked]}"). Line 364 "**People: 0.**". Lines 369-371: each session "read only its own
  sample, and edited no file", and the six sessions "are not independent of" the generator (the
  reason is stated in those lines); `docs/DECISIONS_A.md` line 24 calls the round-1 readers "four
  independent readers". Lines 373-380 list the six sessions (round 1: four sessions started
  2026-10-02 09:49 UTC; round 2: two sessions started 10:14 UTC; 75 groups each; the reviewer
  column ends in "no human"); lines 382-387 list what each session checked; line 390: "The
  instructions, the full reports and the rendered samples are in `audit/model_review/`."; lines
  412-413: "The reviewed groups were rendered by pre-freeze versions of the generator. No group of
  the frozen sets has been read by a person."
- Shortcut checks. `docs/DECISIONS_A.md` line 16: before near-misses mirrored the flip, "an
  attribute-blind logistic model scored TA 69% (subject 72%, time 75%) using mention counts. After
  it: 40%, all on numeric and boundary kinds; subject, negation and time 0 (dry-run build)". TA of
  the shortcut scorers on test_L2, committed with the freeze
  (`results/A-D14-<scorer>/summary_rule_v1__test_L2.json` line 5 at `selrm@e40789b`):
  always_default 0.0, claim_only 0.0, concept_named 0.0, bag_of_words 7.05, attribute_blind 40.0,
  trigger_train 53.95, trigger_all 99.5.

**The freeze.**
- `selrm@e40789b`, 2026-10-02 03:50:32 -0700 (10:50:32Z), "Freeze rule_v1 (fold 1) and
  rule_v1_fold2/3".
- `data/REGISTRY.json`: 38 sets, all `"frozen": true` and `"created": "2026-10-02"`; folds 2 and 3
  hold dev, test_L2, train_blocks and train_triplets each (script).
- Every MANIFEST at the freeze: `git_commit` 59034a3dc24319fe2f1c596f7ad89336617da76f, `python`
  3.12.7, the same `template_split_hash` (1020bdc7bdae5d60...). Shortcut validation `PASS` on 12
  sets: rule_v1 dev, test_L0, test_L1, test_L2, test_L3alt, test_L3inv and test_hard, dev and
  test_L2 of folds 2 and 3 (11 triplet sets), and rule_v1 `readapply` (MANIFEST `note`: "triplets
  (tid) + reading and application pairs"); `n/a` on the 24 training, ablation and diversity
  corpora and the 2 missing-input sets (script).
- sha256 of `records.jsonl` (registry): test_L2
  `e0b81644a7278070de3ac253426acb1bfbe5da8958cf9e68c00fb5b85b8ddbdd` (`n_groups` 2000,
  `n_records` 29248); dev `4a9c6dc4fb247e8ffdc30fe85b925588ab181b9f637273b9ea6afddc6d1749ff`
  (`n_groups` 300); train_blocks `e07e99627f8d6df88a10288985e795379176b3b9ebe87e9f147754a4bd6a1f1d`;
  train_triplets `9474d523138b2b7fd06d267fc4ff93963e19a7dd0541b90f3cea2825b5ff72bf`. The other 34
  are in `data/REGISTRY.json`.
- Planned date: role A's `ROLE.md` line 4 (`selrm@249f969`) "Core freeze: Saturday 3 Oct,
  evening."; `docs/TEAM_PLAN.md` line 21 (`selrm@a6db79d`) "A's freeze of `rule_v1` (Sat 3 Oct
  evening)". The freeze commit is dated 2026-10-02 03:50:32 -0700.
- Hash checks after the freeze: `docs/DECISIONS_B.md` line 40 (`selrm@452a6e9`): "all 30 fold-1
  sets match A's registry sha256"; `docs/DECISIONS_D.md` line 9 (`selrm@1a670f0`): a local rebuild
  of all 44 sets "matches the registry sha256 byte for byte"; on every branch that has a registry,
  none of the 38 sha256 values of the freeze changed (script).

## After the freeze

- New sets under new names. `selrm@a8add2d` (09:25:05) built `train_triplets_lo_{subject,negation,time}`
  and `train_dose_{05,12,25}`; `selrm@3e0c832` (09:26:57) froze them. `docs/DECISIONS_A.md` line
  27: "Added to rule_v1 as new frozen names with `build_rule_v1.py --only` (frozen folds read,
  never rewritten); the new code reproduces the frozen sets byte-identically (test_L2, dev,
  train_blocks, train_triplets sha256 equal)." On `role-a`, `selrm@2df9308` (22:31:16) froze the
  rule-side set `xr_v1/test` and `selrm@11f77f7` (22:38:03) a leave-boundary-out corpus and alias
  names; `selrm@3387e03` (22:36:07) added the kit for author-written cases (`challenge_v1`). All
  three are in main since `selrm@6f6db69` (22:46:41). The registry has 52 entries from
  `selrm@11f77f7` on (script). Role C froze `clin_v1/trialgpt_dev` and `clin_v1/trialgpt_test`
  (`selrm@d91a6a1`, 22:00:00) and 14 further clinical sets from 23:08:07 to 23:33:06 (MedEinst,
  key pairs, NLI4CT-P, clinical training pairs; `data/clin_v1/REGISTRY_C.json`, 16 entries, all
  frozen; script).
- `xr_v1` (`docs/DECISIONS_A.md` line 30 at `selrm@2df9308`): items of two rules that differ only
  in the applicability clause, over the same three cases; the dimensions include "currency (current
  or past vs current)" and "subject (patient or first-degree relative vs patient)". `docs/HANDOFFS.md`
  line 8: "Validation: program XA 100; always-default, concept-named, two rule-blind scorers,
  never-count and always-count all XA 0 (MANIFEST)."
- First trained runs. Role B queued 20 seed-0 runs on rule_v1 (`selrm@0661a00`, 05:22:39). The
  first logged training step on a rule_v1 corpus is 2026-10-02T12:50:08Z
  (`results_git/B-F-verdict-triplets-s0/run.log` line 1); none of the 11 rule_v1 runs with a step
  log logged a step before the freeze commit (10:50:32Z). The runs before the freeze trained on
  smoke_v2 (`B-C0-*`, `B-T0-*`; script section "First logged training steps").
- First results on test_L2 (seed 0), TA from line 8 of `results_git/<run>/summary_rule_v1~test_L2.json`:
  verdict x blocks 58.2 and verdict x triplets 91.3 (`selrm@a8d4111`, 07:59:00); ledger2 x blocks
  75.3 (`selrm@09fd29c`, 08:43:42); verdict x natural 58.0 (`selrm@3834b8f`, 08:55:48); ledger2 x
  triplets 99.2 (`selrm@c3bdac6`, 09:47:58).
- Not run at the refs read: the audit pilot C-P0 (status "todo" in `docs/RUN_MATRIX_C.csv` line 4
  at `selrm@1a670f0`, on `origin/role-c` and at `selrm@129e5b4`) and the rewritten-note tier
  (pipeline in `selrm@8a61abd`; `docs/SUMMARY_A.md` line 58, unchanged from `selrm@1a670f0` to
  `selrm@129e5b4` and on `origin/role-a`: "As soon as `OPENROUTER_API_KEY` exists (COMPUTE REQUEST
  #1), run").

## Not in the records

Items 1-7 are statements of the v13 draft that no file supports as written; items 8-9 are facts
the records lack. Line numbers refer to `selrm@1a670f0:paper/latex_v13/main.tex`; the paragraphs
are unchanged at `selrm@129e5b4` (heading at line 2047, "What changed" at lines 2057-2062,
Limitations "Development" at lines 1171-1174). The authors need their own records for these.

1. "it solved \ph{59.7}\%" (line 1963) and the test it reports, a model trained on pilot triplets
   and scored "On rules held out from training in which a past or a family finding counts" (lines
   1962-1963). No file records the value as a pilot result or records such a test, and the
   pilot-generator data contain no case in which a past or family mention counts (section "Pilot
   result on past/family rules").
2. "A verdict-only model" (line 1961): `docs/MEASURED_FACTS.md` records "100/100/100 on the same
   in-distribution dev" (line 21), which supports "solved every development triplet", but not the
   output format of that model or the generator of its data. Role B's verdict model trained on pilot
   triplets (`B-C0-smoke-verdict-triplets-s0`) has TA 97.3 on its dev set with the held-out
   template (`docs/SMOKE_B_C0.md` line 39).
3. "``past or family means ignore'' was a sufficient strategy" (lines 1964-1965): the records show
   that such mentions never count in pilot-generator data; no file records a test of the strategy.
4. "This result is from the pilot setup and motivates the rule-side test" (lines 1965-1966) and
   "Rule-side items test the same failure directly" (line 1972): no file links the rule-side items
   to a pilot result. The final-task files list "tests the generator does not determine
   (rule-side edits, author-written cases)" among what reviewers will ask for first
   (`FINAL_TASKS_D.md` lines 23-26). That rule-side items "were built after the freeze as a separate
   set" (lines 1972-1973) is in the records: `xr_v1`, frozen in `selrm@2df9308` (section "After the
   freeze").
5. Heading "The first generator and the shortcut it allowed" (line 1958). No file shows that the
   pilot generator was the first generator. Older in the records than any record of it are the
   handoff spec of 2026-10-01 22:49:58 -0700, which specifies flips in which past or relatives'
   findings count, and the first dataset build, whose decision rows are dated 2026-10-01 and
   whose sets contain such flips (135 of 2,000 test flips; 2,929 of 30,000 flip examples per
   training corpus; section "Redesign"). The review of v8 mentions "100% shared templates"
   without naming a generator (`docs/REVIEW_HISTORY.md` line 135). The appendix as drafted does
   not mention the first build.
6. "What changed" (lines 1969-1971) presents these as changes in `rule_v1`; measured against the
   records:
   - "contains rules under which past or family findings count": three of the 11 pilot rules
     already state that past or family findings count, and the first build already made flips in
     which they count, 44 of its 135 such test flips on those three pilot rules. What the records
     show as new relative to the pilot generator is that such mentions count in the data; relative
     to the first build, it is not new.
   - "adds presentation edits": presentation cases were already in the smoke data built on the
     pilot generator (`selrm/smoke.py` line 116) and in the first build (`pres_share_of_label0`
     0.1497 to 0.1501). Missing inputs are new in `rule_v1`.
   - "to every corpus": the frozen corpus `rule_v1/abl_nopres_triplets` has no presentation cases
     (section "Redesign"); every training, ablation and diversity corpus has missing inputs.
   - "holds out ... templates and cue phrases": the first build already did (by index parity), and
     the smoke data held out one of the pilot generator's 3 templates per form; signature classes
     and folds are new in `rule_v1`.
7. Limitations, "Development" (lines 1156-1159): "the frozen version followed an earlier one whose
   failure we describe": the records hold two earlier versions (the pilot generator; the first
   dataset build, `Symbolic_PRM_NAACL@c965184`) and a measured failure of neither on past or
   family findings. The recorded problems are the template overlap (`docs/MEASURED_FACTS.md`
   lines 21-22) and the gaps in `Symbolic_PRM_NAACL@c965184:docs/SALVAGE.md` lines 66-77.
8. Which teammate wrote the pilot generator and when: the records say only "teammate's generator"
   (project spec of `selrm@a6db79d`, line 78) and "2 Oct, teammate's Colab notebook"
   (`docs/MEASURED_FACTS.md` line 1). The notebook and its outputs are not in the records either.
9. The SymRM pilot (10 rules) has no dates or result files in these repositories, only the summary
   in `paper/latex/SYMRM_INTEGRATION.md`. The appendix does not mention it; it is listed so that
   the two pilots are not confused.
