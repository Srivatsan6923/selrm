# P4. Large open judges solve the triplet test

Status: waits for approval. Already in the paper without approval, as values from result files: Table
`tab:openjudges` (Appendix H), the pointers to it in Section 5 and in the caption of Table 2, and the Scope
limitation, which now says that no closed judge has been scored (it said no larger judge either).

## What the files show (role C, `results_git/C-AUD-*`; 1,000 L2 triplets, conclusion claims)

With the two-order choice prompt: gpt-oss-120b 98.5, Gemma 4 31B 99.7, Qwen3.5-27B 98.1, Llama-3.3-70B 94.6,
Nemotron 3 Super 85.5 (triplet accuracy). With a one-token log-probability readout the same models are far
lower (Qwen3.5-397B 13.7), so the readout, not only the model, decides the score. The untrained 9B backbone is
at 27.1 and the released medical PRMs at 10.0-11.9.

## Why wording is affected

1. Section 6.1 and the abstract present the failure of released medical PRMs and of the untrained backbone. The
   draft already says the test is solvable without training on our rules (ThinkPRM-14B, 87.5% of 200 triplets).
   The new rows make that much stronger: several general models solve it almost completely. A reader will ask
   why a near-miss-trained 9B verifier matters if a 31B general model scores 99.7.
2. The comparison is not like for like (model size, a generated answer in both orders against a pointwise score
   usable as a reward, cost per judgment), and that has to be said, not left to the reader.

## Proposed sentence for Section 6.1 (after the ThinkPRM sentence)

> Larger general models solve the test when asked to choose between the two claims in both orders
> (\res{run/C-AUD-nemotron-3-super-choice/L2/all/TA}--\res{run/C-AUD-gemma-4-31b-choice/L2/all/TA}\% for five open models of 27B to 120B parameters,
> Table~\ref{tab:openjudges}); the same models read out as a one-token score, the form a process reward
> takes, are far lower. The test is therefore not hard for a capable reader; the released medical reward
> models and a 9B backbone fail it.

Length: about four lines; proposed removal: the sentence on larger judges in Section 5 ("larger open judges
are in Table ..., closed ones not yet scored") moves into this one.

## Proposed addition to Limitations (Scope)

> Large general judges solve the rule triplets with a choice prompt, so the trained verifier's advantage is
> one of size and of the pointwise score, not of capability that no other model has.

## Not proposed

No change to the abstract's first result sentence ("released medical PRMs solve 10-12% of triplets"): it is
true as written. Whether the abstract should mention the large judges is the authors' decision.
