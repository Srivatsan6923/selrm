# P1. Policy training: the runs with the ledger rewards are finished

Status: waits for approval (H-S2-5 procedure). Values are from `results_git/D-RL-*/summary_rule_v1~test_L2.json`
(`start_pair`, `acc_pair`), per-example outputs in `eval_step*.jsonl`.

## What the runs show (seeds finished on 8 Oct)

Pair accuracy on 150 held-out L2 pairs, untrained policy to step 1,000:

| Reward | seed 0 | seed 1 |
|---|---|---|
| Outcome | 88.7 -> 96.7 | 89.3 -> 98.0 |
| Reference graph | 88.7 -> 98.0 | running |
| Med-PRM (step check) | 88.0 -> 38.7 | 89.3 -> 54.7 |
| Ledger-RM trained on blocks | 89.3 -> 36.0 | 89.3 -> 34.0 |
| Ledger-RM trained on triplets | 89.3 -> 52.7 | 89.3 -> 43.3 |
| Summary pipeline trained on triplets | 89.3 -> 52.0 | not planned |

Seed 2 of the five rewards and seed 1 of the reference graph are queued.

## Already filled without approval (red values; no claim changes)

- Section 6.6, "Runs with the two ledger rewards are not finished." becomes one sentence with the two measured
  values of seed 0.
- Appendix H, "The two ledger rewards are tbd." becomes the measured pair and triplet accuracies.

## Needs approval

### (a) Limitations, "Verifier, process reward, training reward"

Now:
> The policy experiment has one seed and one policy, and its runs with our own rewards are unfinished; we make
> no claim that a policy trained against our verifier is safer.

Proposed (the result contradicts "unfinished" and decides the open question against us):
> The policy experiment has one policy and at most three seeds per reward. Our own process rewards are
> exploited as well: with the ledger score as the only reward, pair accuracy falls from
> \res{run/D-RL-ledger2-triplets/L2/top/start_pair} to \res{run/D-RL-ledger2-triplets/L2/top/acc_pair}
> (trained on triplets) and to \res{run/D-RL-ledger2-blocks/L2/top/acc_pair} (trained on blocks). A verifier
> that passes the triplet test is therefore not a safe training reward by itself.

### (b) Section 6.6, last two sentences of "Policy training"

Now the paragraph links exploitation to a reward that fails the triplet test ("A reward that fails the triplet
test can be optimised without solving the task"). The ledger trained on triplets passes the test (99.2) and is
exploited too, so the link as written is not supported by the finished runs. Proposed first sentence:
> A process reward can be optimised without solving the task, whether or not it passes the triplet test.

and, replacing "as its reversal rate of 19.4\% would suggest":
> The two ledger rewards, which score written steps and never the final answer, are exploited as well
> (to \res{run/D-RL-ledger2-blocks/L2/top/acc_pair} and \res{run/D-RL-ledger2-triplets/L2/top/acc_pair}): the
> policy learns to write one step that restates a fact of the case and often gives no final answer.

The second half of that sentence rests on the analysis of what the collapsed policies write (STAGE2_TASKS_D
D5.3; fixed-seed sample of 50 outputs per reward), which is not finished. Until then only the first half is
proposed.

### (c) Abstract, last sentence, and contribution (4)

No change proposed: both speak of the released medical PRM only, and that result stands at two seeds
(88.0 -> 38.7 and 89.3 -> 54.7). If (b) is approved, contribution (4) could add "our own process rewards are
exploited too" at the cost of one line elsewhere.

Length: (a) is outside the page limit (Limitations). (b) adds about two lines to Section 6.6; proposed removal:
the sentence "Such exploitation is known ...; we add an exactly labelled held-out evaluation and the exploited
reward's triplet profile." moves to Appendix I, where the same citations already appear.
