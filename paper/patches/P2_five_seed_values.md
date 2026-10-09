# P2. Statements typed at four seeds or at seed 0 that the five-seed files change

Status: waits for approval. Each item is a sentence whose wording, not only its number, depends on the value.
Sources: `docs/PAPER_NUMBERS_V14.md` (rows "differ" and "ambiguous"), computed from the score files with
`selrm.metrics.paired_test` as `scripts/analysis_b.py` does.

1. Appendix H, further ablations: "on blocks the ledger is 2.7 points above prose over four seeds
   ($[-0.1,5.6]$)". Summary x blocks now has five seeds; pooled over five the difference is +5.2 [2.6, 7.9],
   which no longer includes zero. Proposed: "on blocks the ledger is 5.2 points above prose over five seeds
   ($[2.6,7.9]$)". This also touches Section 6.2's reading that typed fields add little over prose: on
   triplets the difference stays +0.8 [0.3, 1.3]; on blocks it is now established.
2. Section 6.2, "11.5\% solved" and "33.8\%" (blocks-trained verdict model on subject and time near-misses):
   both are seed-0 values in a paragraph of five-seed means; the five-seed means are 9.8 and 21.6. Proposed:
   the five-seed means, or the words "at seed 0".
3. Section 6.2, leave-one-kind-out "when trained with it" (91.0, 88.2, 93.2): seed-0 values; five-seed means
   90.9, 90.7, 93.5. Same choice.
4. Appendix B, fold 1 "58.2\%" and L3-alt "94.6" for verdict x blocks: seed-0 values; five-seed means 53.7 and
   89.8. Fold 2 "63.1": seed 0; three seeds are finished (mean 66.4).
5. Appendix C, "at least 99.2\% for every trained model" (missing-evidence rejection): the minimum over every
   trained model is 98.7 (rationale x natural); 99.2 holds for the rationale format on balanced and triplets,
   and 99.9-100.0 for verdict, summary and ledger. Proposed: "at least 98.7\%".
6. Appendix F, malformed reader outputs "1.9--4.0\% on TrialGPT" for the main model: 1.9 is the blocks model;
   the main model's seeds give 0.7-4.0. Proposed: "0.7--4.0\%".
7. Appendix D, clinical-pairs model "at two seeds ... trap accuracy above 95\%": three seeds are finished
   (pair accuracy 7.8, 43.5, 48.7; trap accuracy 97.4, 95.7, 94.8). Proposed: three seeds, "about 95\%".
8. Appendix C, "uniformly random preferences 1.5\%": no result file; analytically 1/64 = 1.56\%, which the
   draft's rounding prints as 1.6. Proposed: "1.6\% (1/64)".
9. Appendix C, "60{,}000 records" per training corpus: natural and balanced hold 60,000, blocks and triplets
   60,004 (60,000 examples are trained). Proposed: "60{,}000 training examples per run".
10. Policy training, "one seed" (Section 6.6, Limitations, Appendix H): two seeds are finished and a third is
    running; see `P1_policy_ledger_rewards.md`.
