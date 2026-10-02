# Role A summary (Fri 2 Oct 2026, late evening)

## What exists
Branch `role-a` is pushed; the lead has not merged it into main yet.

**Code**
- `selrm/engine.py` builds base, flip, near-miss and presentation cases from executable rules.
  - Labels come from the program. Every group must pass its invariants before it is kept.
  - Near-miss kinds: numeric, boundary, subject, negation, time.
  - Tiers: easy, long, superseded, delabelled, alt.
  - Optional cases: missing twins (both claims 0) and reading/application pairs.
- **Rule library:** 353 rules.
  - 104 hand-written: 61 constraint and 43 scoring rules (partial published scores).
  - 250 sampled from a typed grammar. The sampler avoids setting conflicts, coupled concepts, and contraindicated alternatives.
  - 60 invented rules, test only, for L3-inv.
  - `selrm/folds.py`: 21 signature classes and 3 folds, each holding out 5 classes for L2.
- **Phrase banks:** 53 concepts and 1,428 templates (4 train and 2 test per form).
  - Cue words for negation, time and current values are split the same way.
  - Sources are in `tools/phrase_kit`.
- **Tools for other roles:**
  - `selrm/reference.py`: check code and reference graphs.
  - `scripts/build_rule_v1.py`: every set, deterministic; `--fold`, `--only`.
  - `scripts/shortcut_scorers.py`, `scripts/dataset_stats.py`, `scripts/sample_triplets.py`.
  - `scripts/rewrite_tier.py`: the A-D11 pipeline, ready.

**Data: frozen 2 Oct.** `data/REGISTRY.json` and the MANIFESTs are in git. Records are rebuilt by script and checked by sha256; B's cluster rebuild matched.
- **rule_v1 (fold 1)** has 36 sets:
  - test_L2: 2,000 triplets;
  - dev: 300;
  - test_L0, L1, L3alt, L3inv and hard;
  - missing and dev_missing;
  - readapply;
  - 4 training corpora of 60k records each;
  - 13 diversity corpora and 3 ablation corpora;
  - 3 leave-one-near-miss-kind-out corpora and 3 near-miss dose corpora.
- **rule_v1_fold2/3** each hold test_L2, dev, train_blocks and train_triplets.

**Results** (`results/A-D14-*`, TA on test_L2)

| Scorer | TA |
|---|---|
| Always default, claim only, concept named | 0 |
| Bag of words | 7.0 |
| Attribute-blind | 40.0 |
| Trigger lexicon, training cues | 54.0 |
| Trigger lexicon, test cues | 99.5 |

- **Statistics** (`results/A-D15`): between training and L2 rules, 0% of programs, rule texts, templates and cue words are shared. Criterion subexpressions are 72–85% shared (L2 means new structure over familiar criteria).
- **Quality:**
  - 45 tests pass, and shortcut validation passes on every triplet set.
  - Two audit rounds (6 readers, 450 rendered groups) found no label errors. Every consistency finding was fixed before the freeze.
  - The reject rate is about 1%, all from presentation edits that needed re-rendering.

## What is running
Nothing for role A. Role B's training jobs on NRP belong to role B.

## What I would do next
1. **A-D11 rewritten-note tier.** As soon as `OPENROUTER_API_KEY` exists (COMPUTE REQUEST #1), run `python scripts/rewrite_tier.py --n 1000 --freeze`.
   - Rewriter: Gemma 4 31B. Extractors: DeepSeek V4 Pro and gpt-oss-120b. Cost is about $2–3.
   - Report the acceptance rate and publish `rule_v1/rewritten`.
   - This matters now because the rule tier is lexically solvable: the trigger lexicon given the test cues scores 99.5.
2. **C's pilot (Sun 4 Oct).** On NO-GO, build rule_v2 under new names: 60% hard tiers, plus long + superseded and long + alt combinations.
3. **Appendix B and C text** (library, splits, overlap, construction, audits, reject rates, shortcut table), from `results/A-D15`, `results/A-D14-*` and `docs/DECISIONS_A.md`.
4. **Missing-input design, for the lead.** MR is 100 for trained models because the "unknown" wording is learnable. If the paper needs MR for trained models, the fix is a harder missing variant (for example, a value omitted with no marker). Otherwise MR stays a zero-shot audit column, as planned.
5. **Leave alone:**
   - MedCalc-Bench stays "not run".
   - The prompt files for B, C and D, and the old package files in `D:\NAACL27`, stay out of git, because that folder is the old public repository.
