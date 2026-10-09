# Stage-2 tasks (8 Oct 2026)

One file per role; each starts with the prompt to paste. These files replace
the FINAL_TASKS files of 3 Oct. Unfinished items of those files are carried
over inside each role file under "Carry-over".

The paper is v14: `paper/learning_when_to_change_naacl2027_draft_v14.pdf`,
sources in `paper/latex_v14/`. Nothing of v10/v13 is cut.

## Read in this order
1. `STAGE2_ANALYSIS_PLAN.md`  what is tested and how each outcome is read.
   The lead commits it to `docs/ANALYSIS_PLAN_STAGE2.md` before any stage-2
   test set is built.
2. `STAGE2_SPEC.md`           shared names, record fields, system names, the
   gate, the criterion conditions. It extends `docs/INTERFACES.md`.
3. `STAGE2_TASKS_<A|B|C|D>.md` your tasks, in order, with acceptance checks.
4. `RED_CELLS.md`             every unmeasured value of v14 and who owns it.
5. `HUMAN_TASKS_STAGE2.md`    what only the authors can do.

## What stage 2 is for
Stage 1 showed: near-miss supervision teaches a verifier when evidence
applies (53.7 -> 91.8 on held-out rule structures; 98.5-99.2 with a separate
reading pass), the trained verifiers follow edits to the rule (85-94% on
rule-side items against 39% untrained), and none of this transfers to
benchmarks that state no criterion (MedEinst 24.2 -> 22.8 / 15.7; key pairs
79.8 -> 78.2 / 30.5). The zero-shot medical claim is withdrawn.

Stage 2 asks one question: is that boundary the absence of a criterion? It
tests it where a criterion has a source we did not write, on clinical text:

| Tier | Criterion comes from | Labels come from | New training needed |
|---|---|---|---|
| MedCalc-V | score definition shipped with each instance | released entity values + rule code | no |
| MedEinst with derived criterion | DDXPlus condition lists, by script | benchmark labels | no |
| Knowledge-base triplets | same lists | exclusion procedure | no |
| Registered criteria | Chia / Leaf annotation of registry text | compiled program | no (windows: yes for the gate) |
| Class triplets | RxClass, HPO, Mondo | class closure | yes |
| Key pairs | none (self-written, diagnostic) | answer keys | no |

The first three answer the main question with the adapters that already
exist. That is why role A builds MedCalc-V first and role C scores it first.

## Order by dependency (dates are lifted)
The lead lifted the run freeze of 7 Oct and the dates of 11-12 Oct on 8 Oct.
Work is ordered by dependency:

```
D0  commit analysis plan ............................ blocks every stage-2 test set
C1  rule-tier controls on existing adapters ......... no dependency, start now
A1  MedCalc-V  ->  C3  comparisons (7) (8) (9) ...... first answer to the main question
A2  KB criterion ->  C2 executor audit -> C4 (11) ... gate: executor decides >= 50% of pairs
A3  rule paraphrases -> C1
A4  ontology snapshot + class triplets  \
A5  rule_v2 (windows, classes, record)   >  B2 training on rule_v2 -> B3 composite -> C5-C7 (10) (12), ladders
A6  registered criteria                 /
B1  gate library (parser, linker, checks) ........... no dependency, start now
D   tables, red-cell closure, policy training, decision rules, paper patches, audits (continuous)
```

## Rules for all roles (unchanged, plus four)
- `rule_v1`, `xr_v1` and every frozen set stay frozen. New content gets a new
  name, a manifest, a shortcut-validation result, and is frozen with a hash
  before any system is scored on it.
- Nothing is tuned on a test set. Prompts, thresholds, the criterion parser
  and the linker are developed on the development portions named in the spec.
- Every run keeps per-example scores and reader outputs. Every number in a
  table comes from a results file.
- No fabricated, estimated or copied numbers. A result that contradicts the
  expectation is reported as found, and the decision rule is applied as
  written.
- New: no stage-2 test set is built before `docs/ANALYSIS_PLAN_STAGE2.md` is
  on `main`. Loaders, rule code and tests may be written before that.
- New: external data are pinned (tag, commit or DOI, plus sha256) and their
  licence is recorded in the manifest. Code from dataset repositories is not
  imported or executed; we implement from the stated text.
- New: a criterion text never depends on the case or its label. Both members
  of a pair, and all cases of a triplet, receive the identical text.
- New: credentialed data never goes to an external API. MedCalc-Bench,
  DDXPlus, MedEinst, Chia, Leaf, HPO, Mondo and RxNav are public.

## Ask the lead only for
GPU access, credentials, and the decisions listed in `HUMAN_TASKS_STAGE2.md`.
If an input from another role is missing, work on the next unblocked task and
mark dependent runs `provisional`.
