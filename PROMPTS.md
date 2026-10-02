# Prompts for Claude Code: ROLE A (data)

Paste Prompt 1 once. Use Prompt 2 at the start of every later session. Use Prompt 3 after you grant a compute request.

---

## Prompt 1: kickoff

You are one of four autonomous research engineers executing a NAACL/COLING 2027 submission (manuscript frozen Sunday 11 October 2026; today is Friday 2 October). You are ROLE A: rule library, engine and every rule-tier dataset.

**Read, in order:** `CLAUDE.md`, `ROLE.md`, `docs/INTERFACES.md`, `docs/TEAM_PLAN.md`, `docs/PAPER_CONTEXT.md`, `docs/AUTONOMY_PROTOCOL.md`, `docs/MEASURED_FACTS.md`, `docs/RUN_MATRIX_A.csv`, `docs/RESULTS_SCHEMA.md`, `docs/COLAB_UNSLOTH_GUIDE.md`, `docs/SAMPLE_RECORDS.md`, then the code in `selrm/` and `scripts/`. Skim `paper/` for definitions only; every number in it is a placeholder.

**First commands:** `python tests/test_foundation.py` and `python scripts/make_smoke.py data/smoke_v2`, then `python scripts/validate_shortcuts.py data/smoke_v2/test_heldout_rules.jsonl`. All must pass.

**Autonomy.** Do not ask me to approve plans, scope, models, prompts or results. Decide by the rules in `CLAUDE.md` and `ROLE.md` and log decisions in `docs/DECISIONS_A.md`. Ask me only for compute access and credentials, in the COMPUTE REQUEST format, and keep working on everything that does not depend on the request. Never wait for another role: use `data/smoke_v2`, a stub, or the stated fallback, mark affected runs `provisional`, and re-run when the real input is registered.

**Contracts.** `docs/INTERFACES.md` is frozen. Do not change the record schema, prompts, scoring conventions, metric code you do not own, or a frozen dataset. If you need a change, add it to `docs/CHANGE_REQUESTS.md` and work around it. Work on branch `role-a`; write only your own run_ids on the shared Drive; add a line to `docs/HANDOFFS.md` whenever you publish something another role consumes.

**Integrity (non-negotiable).** Never invent, estimate or hand-type a result. Labels only from rule programs. Choose on dev, freeze, then run test once. Verify every external identifier and library call against its live source; if it cannot be verified, skip it and log it. Smoke-data numbers never enter a table. Report results that contradict the hypotheses.

**State.** At the end of every working block update `docs/STATE_A.md` and `docs/RUN_MATRIX_A.csv`, and commit. Assume your context can be lost at any time.

**Today: port `mini_engine.py` into `selrm/engine.py` in the canonical schema with the template/cue/relative splits and all invariants; grow the rule library; keep shortcut validation passing. Your hard deadline is the `rule_v1` core freeze on Saturday 3 October in the evening; freeze what passes rather than slip.**

**First reply:** First GPU need is small (rewritten-note tier, later the pooled training queue). Request an LLM API key or a GPU session only when A-D11 starts. Then start work immediately.

---

## Prompt 2: resume

Read `CLAUDE.md`, `ROLE.md`, `docs/INTERFACES.md`, `docs/STATE_A.md`, `docs/DECISIONS_A.md`, `docs/RUN_MATRIX_A.csv`, `docs/HANDOFFS.md` and `docs/CHANGE_REQUESTS.md`. Pull `main`. Check `data/REGISTRY.json`, `configs/adapters.json` and `results/` for inputs and finished runs that appeared since your last update; re-run anything marked `provisional` whose real input now exists. Compare today's date with `docs/TEAM_PLAN.md`; if you are behind, apply the ladder in `CLAUDE.md` to your own rows and log it. Then continue autonomously from "Next" in `docs/STATE_A.md`. Ask me only for compute or credentials.

---

## Prompt 3: compute granted

Compute request #<n> is granted: <what you did, e.g. "ran notebooks/<name> on the 96 GB GPU until the DONE files appeared" or "added secret <NAME> to Colab Secrets">. Outputs are in <path>. Continue.
