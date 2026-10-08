# Tasks only the authors can do (stage 2)

No clinician is involved and the paper says so. These tasks are the evidence
that people read the data and decided the claims.

## Blocking (the roles wait for these)
| ID | Task | Who | Output |
|---|---|---|---|
| H-S2-1 | Read `STAGE2_ANALYSIS_PLAN.md`. Change it now if you disagree; after the commit it is only appended to. Tell role D "commit". | lead | `docs/ANALYSIS_PLAN_STAGE2.md` on `main` |
| H-S2-2 | Credentials still open from 3 Oct: OpenRouter key (rewritten cases, API judges, closed-judge row), the read-only GitHub secret and the Hugging Face token for role B. Without the key the paper keeps "not scored" for the large judges. | lead | secrets set; never in the repository |
| H-S2-5 | After gate G4: read role D's patch set for the outcome that occurred (abstract, contribution 3, Section 6.5, conclusion, limitations). Approve or rewrite. Role D applies nothing that changes a claim without this. | lead | approval in `docs/DECISIONS_D.md` |

## Not blocking, needed before submission
| ID | Task | Who | Output |
|---|---|---|---|
| H-S2-3 | Read the stage-2 sample sheets: 100 edited MedCalc notes (is the edit the only change, does the note now state the edited fact, is the label right under the score text); 50 compiled registered criteria (does the program do what the sentence says); 20 rendered DDXPlus criteria. | two authors each | `audit/s2/*.csv` |
| H-S2-4 | Open every `VERIFY` entry of `custom.bib` at its source. Fifteen were added in v14 from memory: saeidi2018sharc, holzenberger2020sara, clark2020ruletaker, dhuliawala2024cove, she2023scone, ravichander2022condaqa, he2023ontolama, he2024hit, kury2020chia, dobbins2022lct, gargano2024hpo, vasilevsky2022mondo, nelson2011rxnorm, gao2023scaling, winston1970. Delete what cannot be confirmed. | split | `docs/CITATIONS_CHECKED.csv` |
| H1 | Carry-over: each author reads 75 rendered groups of `rule_v1`. | all four | `audit/h1/answers_authorN.csv` |
| H2 | Carry-over: 40 author-written challenge cases each. Optional now; without it the paper keeps "not used in this draft". | all four | `challenge_v1/notes_authorN.md` |
| H3 | Carry-over, optional: sign off the 95 `ec_v1` criteria. `reg_v1` (structure from published annotation) replaces it in the paper if this is not done. | two authors | `docs/ec_signoff/` |
| H4 | Carry-over: code 50 failures each from role D's sheets; add the stage-2 sheet when it exists. | all four | `audit/errors_<name>.csv` |
| H6 | The development history (Appendix J) from your own records; the introduction and discussion in your own words once the stage-2 outcome is known. | lead + one | `paper/latex_v14/main.tex` |
| H8 | Read the venue's policy on AI assistance and complete the disclosure. | lead | checklist |
| H9 | Decide the submission cycle and submit. | lead | -- |

## Decisions the roles will ask for
- G1: MedCalc-V is small after the acceptance test (fewer than 8 scores or
  150 human-written notes). Continue with the stated power, or stop the tier.
- G2: the executor decides fewer than half of the MedEinst pairs. The plan
  already says: drop comparison (11). You only confirm.
- A "not run" sentence for an item that will not be run (diversity curves,
  large judges, rewritten cases). Role D proposes the sentence.
