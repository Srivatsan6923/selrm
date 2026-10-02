# ROLE A: rule library, engine and every rule-tier dataset

You are on the critical path. B, C and D can only produce reportable numbers
after you publish `rule_v1`. **Core freeze: Saturday 3 Oct, evening.**

## Deliverables, in order (IDs in docs/RUN_MATRIX_A.csv)
1. **A-D0 `selrm/engine.py`** replacing `mini_engine.py`, emitting canonical
   records (same fields as `selrm/smoke.py`, which you may reuse).
2. **A-D1..D3 rule library** in `selrm/rules.py` + `selrm/rules_*.py`.
3. **A-D4 freeze `rule_v1` core**: `test_L2` (2,000 triplets, fold 1), `dev`
   (300, train-level rules, test templates), `train_{natural, balanced,
   blocks, triplets}` (60k records each). `data/REGISTRY.json`, MANIFESTs,
   shortcut validation PASS, one line in `docs/HANDOFFS.md`.
4. A-D5..D8: ladder sets, hard tiers, missing twins, reading/application pairs.
5. A-D9..D13: folds 2-3, diversity corpora, rewritten-note tier, ablation
   corpora, check-code renderer and reference graphs.
6. A-D14..D15: shortcut-scorer table, statistics, overlap table,
   `docs/SAMPLE_TRIPLETS.md` (100 random triplets), appendix B and C text.

## Engine specification
- **Templates.** Every mention form (present, named absence, other person,
  past/resolved, family first-degree, numeric now, numeric past) has at least
  6 templates per concept group; indices 0-3 train, 4-5 test. Headers, cue
  words for negation and time, and relative names are split the same way.
  A test asserts zero overlap of template ids, cue words and relatives.
- **Cases per group.** base, flip, near, pres (same state, other templates
  and order); optional missing, read, apply.
- **Flip forms.** If the criterion counts past or family findings, flips use
  those forms part of the time (a past stroke is a flip for CHA2DS2-VASc).
- **Near-miss kinds.** numeric (strictly inside `near_delta`, default side);
  `boundary` (value exactly at the threshold) is its own kind; subject
  (a person the criterion does not count); negation (named absence); time
  (past or resolved; numeric: an old value on the flip side with a year while
  today's value stays on the default side). Only kinds valid for the
  criterion (`Criterion.nm_kinds()`).
- **Invariants** (reject, resample, log rates per rule and kind):
  labels base = near = pres = 0, flip = 1 from `Rule.label`; exactly one
  criterion changes between base and flip; for findings the concept keywords
  are absent from the base text and present in flip and near; for numerics
  present in all three; no filler line contains any keyword of any rule in
  the case; `ledger` quotes are substrings of `case_text`.
- **Tiers.** easy (at most 4 lines); long (15+ filler lines, including other
  people's unrelated conditions and old values of unrelated labs);
  superseded; delabelled (allergy label removed after testing); alt (rule
  text uses `alt_threshold`; keep cases where the original threshold gives
  the other answer); rewritten (A-D11).
- **Step claims.** conclusion (always); criterion (constraint rules);
  applicability (optional).
- **Missing twins.** Remove the decisive input; for findings that are not
  closed-world add an explicit "not recorded" line; both claims label 0.
  Verify by enumeration that both outcomes are reachable. Add an equal number
  of ordinary supported claims so C can measure false rejection.
- **Reading / application pairs.** read: claims quote the decisive finding
  correctly vs incorrectly; apply: a one-line case with only that finding.

## Rule library targets (report what is built; v10's counts were placeholders)
| Source | Minimum | Stretch | Notes |
|---|---|---|---|
| Constraint rules | 60 | 120 | recommendation -> decision tree -> program; families: allergy switch, lab threshold (renal, hepatic, haematologic), state switch, drug interaction, history switch, family switch, age limit, any-of / all-of two conditions |
| Scoring rules | 40 | 138 | additive and banded scores from published definitions and MedCalc-Bench scoring calculators (verify dataset ID and licence; use its worked examples as unit tests) |
| Grammar-sampled rules | 200 | 300 | grammar over operators (threshold, any-of, all-of, k-of-n, banded, default-with-exception), input types and applicability predicates; neutral invented names for L3-inv |

Extend `Rule` with a `logic` field for multi-criterion rules. Each rule gets
a structural **signature** (kind, operators, depth, input types,
applicability types); signature classes define L1 vs L2. Three folds, each
holding out at least 4 classes. Every rule needs boundary tests.

## Corpora (all 60k records, 15% presentation and 15% missing-input cases)
natural: states sampled with flip-side conditions at 15% prevalence, cases
independent; balanced: outcomes 50/50, cases independent; blocks: base+flip
pairs; triplets: blocks where near-misses replace half of the base cases
(all kinds equally). Train-level rules and train templates only.

## Other tasks
- **A-D11 rewritten tier.** Rewrite test cases with an open LLM (verify ID)
  into note-like text; accept a group only if two different extractor models
  recover the full state (concept, value, subject, status, time) of all its
  cases. Report the acceptance rate.
- **A-D13.** `render_check_code(rec)` (Python that reads the stated values
  and prints the verdict) for B's GenPRM-style verifier; `reference_graph(
  rec)` (decisive findings and criteria as nodes) for D's graph reward.
- **A-D14 shortcut scorers** on `test_L2`: always default, claim only,
  concept named, attribute-blind logistic (concept-value features without
  subject/status/time), bag of words, trigger lexicon + program (ConText
  style, built from training cue phrases; also with test cues given).

## Decision rules
- Freeze late? At 18:00 on 3 Oct freeze what passes validation (constraint +
  scoring rules) as `rule_v1`; grammar rules and folds go into `rule_v1_fold*`
  and L3-inv later. Never delay the freeze for completeness.
- NO-GO pilot (from C): raise hard-tier share to 60%, add combined tiers
  (long + superseded, long + alt), publish `rule_v2` within 12 hours.
- After the freeze your GPU serves the pooled queue (INTERFACES section 7).
