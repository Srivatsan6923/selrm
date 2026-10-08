# Team tasks, 8-11 Oct 2026

Everything below is due **Sunday 11 Oct, 23:59 IST** unless a row says otherwise. Background:
[`README.md`](../README.md). Full list of author tasks: [`HUMAN_TASKS_STAGE2.md`](../HUMAN_TASKS_STAGE2.md).

## How to work (everyone)

1. `git clone https://github.com/Srivatsan6923/selrm.git`, then `git checkout -b author-<yourname>`.
2. Put each output at the path named in your table. Commit small, push your branch
   (`git push origin author-<yourname>`), and post in the group chat. Srivatsan merges to `main`.
3. Reading sheets carry an id, not a name:

   | id | person |
   |---|---|
   | author1 | Srivatsan |
   | author2 | Basil |
   | author3 | Charansai |
   | author4 | Hemashruthi |

4. Paper edits: one file, `paper/latex_v14/main.tex`. Edit **only your sections** (table below) so
   branches merge cleanly. Do not change any number, table, `\tbd` or red `\ph{...}` note: numbers
   are filled by script from result files. If you think a number or claim is wrong, write it in
   `docs/PAPER_QUERIES.md` (line, what, why) instead of editing it.
5. Sections 1-7 must stay within 8 pages. If you add a line, remove one.
6. Stuck for more than 30 minutes: ask Srivatsan.

## Order that matters

Do **H2 before H1** if you do H2 at all (H1 shows generated cases; H2 must be written without having
seen them). H2 is optional; if nobody does it, the paper keeps "not used in this draft".

## Schedule

| Day | Reading and checking | Writing |
|---|---|---|
| Thu 8 - Fri 9 | H1 (75 groups each), citations first half | Read v14 end to end; mark unclear passages |
| Sat 10 | H4 (50 failures each), citations second half, stage-2 sheets as they appear | First pass of your sections pushed |
| Sun 11 | Everything pushed; second-reader checks | Second pass after cross-reading; page check |

---

## Srivatsan

Lead; the only one with large-scale compute (NRP).

| Task | Output |
|---|---|
| Stage-2 compute: data sets, training, scoring, tables, merges (`STAGE2_TASKS_{A,B,C,D}.md`) | `results_git/`, `tables/`, [`STATUS_BOARD.md`](STATUS_BOARD.md) |
| Credentials (H-S2-2): OpenRouter key, GitHub read secret and Hugging Face token for the training jobs | set as secrets, never committed |
| Decisions: gates G1-G2, "not run" sentences, approval of the claim patches after the stage-2 results (H-S2-5) | [`DECISIONS_D.md`](DECISIONS_D.md), `paper/patches/` |
| H1 as author1: 75 rendered groups | `audit/h1/answers_author1.csv` |
| H4 part 1: code 50 failures | `audit/errors_author1.csv` |
| H6: development history (Appendix J) from own records, with [`TIMELINE.md`](TIMELINE.md) | `paper/latex_v14/main.tex`, Appendix J |
| H8, H9: venue policy on assistance tools and the disclosure; submission cycle | checklist |

## Basil

Has API access (Gemini, Anthropic, hosted open models through Ollama) and can run small training
jobs. These close red cells that need no large GPU.

| Task | How | Output |
|---|---|---|
| **API judges on the rule triplets** (Table 2 "larger judges", red notes at lines 552, 595, 1916-1917) | `python scripts/run_judge.py --model NAME --run_id C-AUD-NAME --set rule_v1/test_L2 --n 1000 --estimate-only`, then without `--estimate-only`. NAME is an entry of `configs/models.json`: copy an existing entry and set `id`, `base_url`, `key_env` (the environment variable holding your key), prices and today's date after checking the id against the provider's model list; a model whose id cannot be checked is skipped. The records come from `python scripts/build_rule_v1.py` (hash must match `data/REGISTRY.json`) or from Srivatsan. Suggested: one Gemini, one Claude, gpt-oss-120b, one large Qwen, one Gemma, one Llama | `results_git/C-AUD-<name>/` with `scores_*.jsonl`, `summary_*.json`, `DONE` |
| **Same judges on the rule-side items** | add `--set xr_v1/test` to the same command | same run directories |
| **Closed-judge row of the selection table** (Table 25) | ask Srivatsan for the candidate pools (`D-POOL-*`) and the scoring call; one API judge | `results_git/D-SEL-*` (Srivatsan integrates) |
| **Rewritten cases** (`rewrite_v1`; red note at 1255-1256) | `python scripts/rewrite_tier.py --selftest`, then `--n 1000` (docstring of the script; one model rewrites, two models of other families must recover every fact, the rule program keeps the labels). Do not pass `--freeze`: Srivatsan freezes the set | `data/rewrite_v1/` |
| Small training (optional, after the rows above): second-backbone run on a 4B model | coordinate with Srivatsan first so that run ids and data hashes match | `results_git/B-*` |
| H1 as author2: 75 rendered groups | [`audit/h1/README.md`](../audit/h1/README.md) | `audit/h1/answers_author2.csv` |
| H4 part 2: code 50 failures | [`audit/ERROR_CODING.md`](../audit/ERROR_CODING.md), `audit/error_sheet_part2.csv` | `audit/errors_author2.csv` |

Rules for API runs: keep per-example outputs; print the cost estimate before each run and tell
Srivatsan the total; a test set is scored once per model; prompts are the frozen ones in
`selrm/prompts.py`, unchanged; no keys in the repository (use environment variables); only the
public sets named above go to an API.

## Charansai

| Task | How | Output |
|---|---|---|
| **Writing, Sections 1-4** (Introduction, Related Work, Rule Triplets, Method; lines 102-517) plus the abstract's wording | Rewrite in your own words: plain, direct sentences; cut filler and generic phrasing; keep every claim and number exactly as it is. The claims themselves change only after the stage-2 results, by Srivatsan's patches | `paper/latex_v14/main.tex` on your branch |
| Extended Related Work (Appendix I, lines 2229-2343) | same | same |
| **Citations, first half** (H-S2-4): keys A-L of [`CITATIONS_TODO.csv`](CITATIONS_TODO.csv), and every `VERIFY` entry among them | Open each paper at its source. Confirm title, authors, venue, year, and that the sentence we attribute to it is really there. Fill the `*_ok`, `checked_by`, `action` columns. What cannot be confirmed is deleted from the paper | `docs/CITATIONS_CHECKED.csv` |
| H1 as author3: 75 rendered groups | [`audit/h1/README.md`](../audit/h1/README.md) | `audit/h1/answers_author3.csv` |
| H4 part 3: code 50 failures | [`audit/ERROR_CODING.md`](../audit/ERROR_CODING.md), `audit/error_sheet_part3.csv` | `audit/errors_author3.csv` |
| Cross-read Hemashruthi's sections on Sun 11 | comments in `docs/PAPER_QUERIES.md` | |

## Hemashruthi

| Task | How | Output |
|---|---|---|
| **Writing, Sections 5-7** (Setup, Results, Conclusion; lines 518-860) and the limitations paragraph | As for Charansai. Section 6.5, the conclusion and the limitations have two prepared versions ("holds" / "fails") in `paper/patches/`; polish both, do not choose between them | `paper/latex_v14/main.tex` on your branch |
| Error analysis text (Appendix J, second half), once the 200 failures are coded | from `audit/errors_author*.csv`; counts come from `python scripts/error_sheet.py`, not by hand | same |
| **Stage-2 sample sheets** (H-S2-3), first reader: 100 edited MedCalc notes, 50 compiled trial criteria, 20 rendered DDXPlus criteria | Sheets appear in `audit/s2/` when the data sets are built (announced in the chat). For each row: is the edit the only change, does the note state the edited fact, is the label right under the score text | `audit/s2/<sheet>_author4.csv` |
| **Citations, second half** (H-S2-4): keys M-Z of [`CITATIONS_TODO.csv`](CITATIONS_TODO.csv) | as for Charansai | `docs/CITATIONS_CHECKED.csv` |
| H1 as author4: 75 rendered groups | [`audit/h1/README.md`](../audit/h1/README.md) | `audit/h1/answers_author4.csv` |
| H4 part 4: code 50 failures | [`audit/ERROR_CODING.md`](../audit/ERROR_CODING.md), `audit/error_sheet_part4.csv` | `audit/errors_author4.csv` |
| Cross-read Charansai's sections on Sun 11 | comments in `docs/PAPER_QUERIES.md` | |

## Undergraduate assistant

No knowledge of the code needed.

| Task | How | Output |
|---|---|---|
| **The 15 references added in v14 from memory** (listed in `HUMAN_TASKS_STAGE2.md`, H-S2-4) | Find each paper at its publisher or arXiv page; correct the BibTeX entry in `paper/latex_v14/custom.bib` (title, authors, venue, year, pages, DOI) and change its note from `VERIFY` to `checked <date>`. If a paper cannot be found, list it; do not guess | `paper/latex_v14/custom.bib`, list in `docs/PAPER_QUERIES.md` |
| **Stage-2 sample sheets, second reader** (H-S2-3) | same sheets as Hemashruthi, filled independently, without looking at her answers | `audit/s2/<sheet>_reader2.csv` |
| **Proofreading of the whole PDF** | Typos, broken references ("??"), a table or figure never mentioned in the text, an abbreviation used before it is defined, inconsistent names for the same thing | `docs/PAPER_QUERIES.md` |
| **Consistency check** | Every number that appears in both the text and a table: do they agree? List disagreements; do not fix them | `docs/PAPER_QUERIES.md` |
| Appendix style pass (Appendices B-H), after the proofreading | plain wording only, no change of content | `paper/latex_v14/main.tex` on own branch |

## Optional, if time remains

| Task | Who | Output |
|---|---|---|
| H2: 40 author-written challenge cases each ([`challenge_v1/WRITING_GUIDE.md`](../challenge_v1/WRITING_GUIDE.md)); **before H1** | any author | `challenge_v1/notes_authorN.md` |
| H3: sign off the 95 registered-criterion programs ([`ec_signoff/`](ec_signoff/), `ec_v1/SIGNOFF_CASES.md`) | two authors | `docs/ec_signoff/` |
