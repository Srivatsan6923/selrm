# Prepared wording changes (lead; applied only after the human lead approves)

Numbers and tables are filled from result files without approval. A change of wording that alters what the
paper claims is written here first, with the passage it replaces, and applied to `paper/latex_v14/main.tex`
after the approval is recorded in `docs/DECISIONS_D.md` (H-S2-5).

| File | Passage | Trigger | Status |
|---|---|---|---|
| `P1_policy_ledger_rewards.md` | Limitations, "Verifier, process reward, training reward"; scope sentence of Section 6.6 | the two ledger-reward runs finished (seeds 0 and 1) | waits for approval; final numbers after seed 2 |
| `P2_five_seed_values.md` | ten sentences typed at four seeds or seed 0 whose wording depends on the value | merge of 8 Oct (five-seed files) | waits for approval |
| `P3_drug_classes.md` | Appendix E class membership, Limitations (sources of criteria), Appendix A, table of sources | plan amendment of 9 Oct (drug classes from one source) | decision taken; wording waits for approval |
| `G4_holds.md` | abstract, contribution 3, Section 6.5, conclusion, limitations ("Transfer") | gate G4, comparisons (7)-(12) meet their expectations | prepared; values are result keys |
| `G4_fails.md` | same passages | gate G4, one or more decision rules of the plan fire | prepared; one block per decision rule, wording of the plan |

Conventions: `\res{cmp/p7/diff}` etc. are result keys (`docs/RESULT_KEYS.md`); they print the measured value
once C's comparison files exist and a red "tbd" before. No number is typed. Each patch names what it removes
so that Sections 1-7 stay within 8 pages.

After G4 the lead sends the matching set; where the outcome is mixed (for example (7) holds and (10) fails),
the "holds" text is the base and the block of each fired decision rule from `G4_fails.md` replaces the
sentence it names.
