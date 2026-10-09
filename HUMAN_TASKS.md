# Tasks only the authors can do (about 6-8 hours each, 3-10 Oct)

| ID | Task | Who | When | Output |
|---|---|---|---|---|
| H1 | Read 75 rendered groups each (300 total) from A's sample sheet. For each case: does the text state exactly the facts in the state? Is the correct claim unambiguous under the rule text? | all four | by Mon 5 | `audit/fidelity_<name>.csv` |
| H2 | Write 40 challenge cases each from A's state specifications, in your own words, without looking at generated notes. A second author checks each note against its specification | all four | by Mon 5 | `challenge_v1/notes_<name>.jsonl` |
| H3 | For each eligibility criterion A formalised: does the program do what the sentence says (thresholds, inclusive or exclusive, time window, whose finding)? Reject anything vague | two authors | by Mon 5 | `docs/EC_SIGNOFF.csv` |
| H4 | Code 50 failures each (200 total) from D's sheet: extraction error, applicability error, unseen wording, rule misread, other | all four | by Tue 6 | `audit/errors_<name>.csv` |
| H5 | Open every cited paper. Confirm title, authors, venue, and the sentence we attribute to it. Delete what cannot be confirmed | split | by Thu 8 | `docs/CITATIONS_CHECKED.csv` |
| H6 | Write the introduction, the discussion of results, the error analysis and the development history in your own words. v13 is a scaffold | lead + one | Fri 9 - Sat 10 | `paper/latex_v13/main.tex` |
| H7 | Decide gates G1-G3 from the agents' numbers | lead | Sun 4, Wed 7 | `docs/DECISIONS_D.md` |
| H8 | Read the venue's policy on AI assistance and complete the disclosure | lead | by Sat 10 | checklist |

Why these matter: they are the evidence that people read the data, checked
the logic, and understood the failures. No agent output can substitute.
If A's "six independent reviewers" were model agents, H1 is the only human
check of text fidelity the paper has.
