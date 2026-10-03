# STATE role A (maintained by Claude Code)
Updated: Fri 2 Oct 2026, late evening. Paused on the user's instruction: no new runs. Nothing of role A is running.

## Done
46 tests pass, and shortcut validation passes on every triplet set.
- **Engine (`selrm/engine.py`):**
  - canonical records, invariants and tiers;
  - near-miss kinds numeric, boundary, subject, negation and time;
  - missing twins and reading/application pairs;
  - meaning-preserving presentation edits.
- **Rule library: 353 rules.**
  - 104 hand-written, including 43 scoring rules (batches C1–C3 and S1–S4 merged);
  - 250 grammar-sampled;
  - 60 invented rules for L3-inv, test only.
  - Signature classes and 3 folds are in `selrm/folds.py`.
- **Phrase banks: 53 concepts, 1,428 templates.** Sources are in `tools/phrase_kit`. The generators there regenerate `selrm/phrases.py` byte-identically.
- **rule_v1 frozen on 2 Oct.**
  - Fold 1 has 36 sets, including the 6 corpora for the two new experiments: `train_triplets_lo_{subject,negation,time}` and `train_dose_{05,12,25}`.
  - `rule_v1_fold2` and `rule_v1_fold3` have 4 sets each.
  - `data/REGISTRY.json`, the MANIFESTs and FOLDS are committed.
  - Records are rebuilt with `scripts/build_rule_v1.py` and checked against the sha256 values. B's cluster rebuild matched.
- **Results:** `results/A-D14-*` (shortcut scorers), `results/A-D15` (statistics), `docs/SAMPLE_TRIPLETS.md`.
- **Audits:** two rounds read 450 rendered groups and found no label errors. Every fix was applied before the freeze.
- **Tools for other roles:**
  - `selrm/reference.py`: check code and reference graphs (A-D13);
  - `scripts/rewrite_tier.py`: the A-D11 pipeline. Its self-test passes; it waits for an API key.

## Running
None.

## Next
1. **A-D11:** once `OPENROUTER_API_KEY` exists, run `python scripts/rewrite_tier.py --n 1000 --freeze`. Then report the acceptance rate and add a HANDOFFS line.
2. **If C's pilot (Sun 4 Oct) is NO-GO:** build rule_v2 under new names, with a 60% hard-tier share and the combined tiers.
3. **Appendix B and C text**, from `results/A-D15`, `results/A-D14-*` and `docs/DECISIONS_A.md`.

## Open compute requests
- #1 (2 Oct): an OpenRouter API key, as environment variable `OPENROUTER_API_KEY`, for A-D11. Cost is about $2–3.

## Blockers
- A-D11 waits for request #1.

## Schedule
Ahead. rule_v1 was frozen on Fri 2 Oct; the target was Sat 3 Oct 18:00.

The one-page summary is in `docs/SUMMARY_A.md`.
