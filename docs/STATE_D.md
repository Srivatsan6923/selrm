# STATE role D (lead)
Updated: 2026-10-08 (stage 2). Plan of record: STAGE2_TASKS_D.md, STAGE2_SPEC.md (= docs/INTERFACES.md section 9),
docs/ANALYSIS_PLAN_STAGE2.md (commit 733ad25), HUMAN_TASKS_STAGE2.md. FINAL_TASKS and NEXT_TASKS are replaced.
The run freeze of 7 Oct and the dates of 11-12 Oct are lifted (DECISIONS_D 8 Oct).

## Where D works
- Clone `D:/NAACL27/selrm-role-d` (github Srivatsan6923/selrm): D's work on `role-d`; publish with
  `git push origin role-d` and `git push origin role-d:main`. Merges of role-a/b/c in the worktree
  `D:/NAACL27/selrm-merge` (branch main; append-only tables with `scripts/union_merge.py`; code conflicts in
  favour of the file's owner), push main, then `git merge origin/main` in the clone. `D:/selrm` is role A's
  tree: never use it.
- LaTeX: tectonic at `D:/NAACL27/tools/tectonic.exe` (TECTONIC). No pdflatex on this machine. Page check:
  `python tools/length_plan/measure.py <pdf>`; the shipped v14 PDF (pdflatex) measures 7.999 pages and the same
  source under tectonic 8.128, so a local build is within the limit when it measures 8.128 or less.
- NRP (namespace ecepxie): PVC `selrm-d` (/pvc), B's PVC read-only (/pvcb). Launcher `scripts/submit_d.py`
  (`export MSYS_NO_PATHCONV=1` in Git Bash). Sync pod `selrm-d-sync` lives 6 h (`submit_d.py sync-down`, then
  `sync-up`). Objects `selrm-d-*`, label app=selrm-d; never touch `selrm-b-*`.
- Local pools and scores: `D:/NAACL27/d_pools/{pools,scores,grpo}`.

## Done in stage 2 (8 Oct)
- D0: plan on main (733ad25), hash in App. A, spec merged, role files in the root, decisions, board.
- README.md and docs/TEAM_TASKS.md (people, tasks, due Sun 11 Oct), docs/PAPER_QUERIES.md.
- D2: `scripts/red_cells.py` (count on the board, history in docs/RED_COUNT.csv): 215 tbd, 33 notes.
- D4: patches prepared in paper/patches/ (G4_holds, G4_fails, P1 policy rewards); nothing applied.
- D5: collected D-RL-ledger2-triplets-s1 (pairs 89.3 -> 43.3), D-RL-summary2-triplets-s0 (-> 52.0), rule-side and
  TrialGPT answers of outcome-s1 and stepcheck-s1; `scripts/policy_analysis.py` -> results_git/D-RL-analysis,
  audit/policy_outputs_D-RL-stepcheck-s*.md.
- D6: swapped rows explained from the files (results_git/D-SEL-combined-swap/summary_sel~*.json: with a swapped
  vignette the ledger's calibrated probability is the minimum in 0.03-0.4% of traces on MedQA, key pairs and
  MedEinst, so the combined selector picks the step check's answer on every question; on CareQA 33 answers
  differ, 14 right on each side). Not an implementation fault.
- D8: citation checklist regenerated from v14 (94 keys, 28 with a VERIFY comment).

## Running
- GRPO jobs queued 8 Oct on h100-opp: refgraph-s1, and seed 2 of outcome, stepcheck, refgraph, ledger2-blocks,
  ledger2-triplets (`k8s/grpo_d.sh <reward> D-RL-<reward>-s<k> --seed k --steps 1000 --eval-every 200
  --eval-triplets 150`); evaluation-only jobs for xr/tg of ledger2-triplets-s1 and summary2-triplets-s0.
  When DONE: `submit_d.py pull /pvc/grpo/<run> D:/NAACL27/d_pools/grpo --exclude ckpt`, copy everything except
  vllm_server.log into results_git/<run>, `python scripts/policy_analysis.py`, commit.
- D1: check of every black number of v14 against the result files (parts in the session scratchpad, to be
  assembled into docs/PAPER_NUMBERS_V14.md), then typed numbers become result keys.

## Next
1. D1.2: result keys inline in v14 (`\res{key}` reads numbers.tex; a missing result prints a red tbd); numbers
   corrected to the files; mismatches listed in HANDOFFS for the human lead.
2. D3: table shells for comparisons (7)-(12), MedCalc-V, gate, Table 14 (appendix until results exist).
3. D7: merge at least daily; docs/CLAIMS_AUDIT_V14.md after each results merge; final audit.
4. D5: after seed 2, three-seed table and the reward triplet profiles next to the policy outcome.
5. D8: stage-2 sample sheets when A's sets exist; stage-2 failure sheets after C3.
6. Gates G1-G4 as their inputs arrive (board).

## Waiting on the human lead
- H-S2-2 credentials (OpenRouter key; GitHub read secret and Hugging Face token for B).
- Approval of paper/patches/P1_policy_ledger_rewards.md.
- "Not run" sentences for items that will not be run (the lead proposes them when the owners report).
