# Claims audit of v14 against the result files (lead; after the merge of 8 Oct, main 5761cac)

Scope of this version: every numeric statement of v14 (text and tables), and the wording that depends on a
number that changed. Statements without a number (interpretations, design descriptions) have not been audited
one by one against the files in this version; that pass follows the next results merge.

| Status | Count | Where |
|---|---|---|
| Consistent with the result files | 1,420 | docs/PAPER_NUMBERS_V14.csv (`match` = yes) |
| Contradicted (the typed value differs from the file) | 20 | docs/PAPER_NUMBERS_V14.md, "Differ"; corrected to the files where the number is a result key |
| No result file | 7 | docs/PAPER_NUMBERS_V14.md, "No result file" |
| Ambiguous (which seeds, which systems) | 12 | docs/PAPER_NUMBERS_V14.md, "Ambiguous" |
| Waiting for a result (red) | 298 values, 29 notes | docs/STATUS_BOARD.md, docs/RED_CELLS.md |

## Statements whose wording the results contradict (patches, not applied)

| Statement | What the files show | Patch |
|---|---|---|
| Limitations: the policy runs "with our own rewards are unfinished; we make no claim that a policy trained against our verifier is safer" | Both ledger rewards are exploited (pairs 89.3 -> 36.0 and 52.7 at seed 0; 34.0 and 43.3 at seed 1) | paper/patches/P1_policy_ledger_rewards.md (a) |
| Section 6.6: "A reward that fails the triplet test can be optimised without solving the task" as the explanation | The ledger trained on triplets passes the test and is exploited as well | P1 (b) |
| Appendix H: "on blocks the ledger is 2.7 points above prose over four seeds [-0.1, 5.6]" | Five seeds: +5.2 [2.6, 7.9] | P2 item 1 |
| Appendix C: missing-evidence rejection "at least 99.2% for every trained model" | Minimum 98.7 | P2 item 5 |
| Appendix F: malformed outputs "1.9-4.0% on TrialGPT" for the main model | 0.7-4.0 | P2 item 6 |
| Appendix D: clinical-pairs model "at two seeds", trap accuracy "above 95%" | Three seeds; 94.8 at the third | P2 item 7 |
| "one seed" for policy training (Section 6.6, Limitations, Appendix H) | Two seeds finished, a third queued | P1, P2 item 10 |

## Corrected in the text from the files (numbers and one factual caption)

Summary x blocks at five seeds (65.8 +- 5.7); range ends 93.3 and 64.8; Table 5 caption: with the Holm
correction comparisons (1) to (5) remain below 0.05 and (6a), (6b) are at 0.428 (typed: only (1) to (3)).
