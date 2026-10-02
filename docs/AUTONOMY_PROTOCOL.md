# Autonomy protocol (all roles)

## You decide yourself
All engineering choices and everything covered by the decision rules in
CLAUDE.md and ROLE.md. Log non-trivial decisions in
`docs/DECISIONS_<role>.md`: `date | decision | rule applied | evidence (path)
| effect on paper`.

## You ask the human only for
1. GPU access (a Colab session to run a notebook, or an SSH host).
2. Credentials (API keys, Hugging Face token, dataset licence acceptance).

### COMPUTE REQUEST format
```
COMPUTE REQUEST #<n> (role <X>)
Need: <GPU type> for ~<hours> h  |  or: <secret name>
For: <run_ids>
Do this: <notebook to open and "Run all", or exact command>
Outputs appear in: <paths>
I will detect completion by: <DONE files>
Meanwhile I am working on: <task>
```
Batch requests (a queue of runs per session). Jobs must be resumable so a
dropped session can be re-run blindly.

## State you maintain (commit at the end of every working block)
- `docs/STATE_<role>.md`: done, in progress, next 3 tasks, open compute
  requests, blockers, date vs schedule.
- `docs/RUN_MATRIX_<role>.csv`: status todo | requested | running | done |
  failed | dropped; measured hours.
- `docs/HANDOFFS.md`: one line whenever you publish something another role
  consumes (dataset, adapter, script, table).
- `docs/CHANGE_REQUESTS.md`: when you need a frozen interface changed.

## Not blocked, ever
If an input from another role is missing: use `data/smoke_v2`, a stub or the
stated fallback, mark the affected runs `provisional`, and re-run them when
the real input appears in `data/REGISTRY.json` or `configs/adapters.json`.

## Integrity (overrides everything)
- No fabricated, estimated or copied numbers. No test-set tuning.
- Results that contradict the hypotheses are reported as found.
- Credentialed data never goes to an external API. No keys in the repo.
- Smoke-data numbers never enter a table.
