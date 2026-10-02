# STATE role A (maintained by Claude Code)
- **Done (code, tested; 38 tests pass):**
  - selrm/engine.py: canonical records, invariants, tiers, boundary kind, missing twins, reading/application pairs.
  - selrm/folds.py: signature classes and 3 folds.
  - selrm/datasets.py and scripts/build_rule_v1.py: every rule_v1 set, plus folds 2-3.
  - selrm/reference.py: check code and reference graphs (A-D13).
  - Rule library: 41 hand-written rules, 250 grammar-sampled, 60 invented (L3-inv, test only).
- **In progress:** scoring batch S3 (10 rules) in review. Phrase banks are final (phrase_kit2 banks G1-G6, F, N -> phrases.py).
- **Next:**
  1. Merge the rules and banks; run the full tests.
  2. Run `python scripts/build_rule_v1.py --freeze`; commit REGISTRY, MANIFESTs and FOLDS; add a HANDOFFS line.
  3. A-D15: statistics and docs/SAMPLE_TRIPLETS.md.
  4. A-D14: shortcut scorers.
  5. A-D10 and A-D12: diversity and ablation corpora.
  6. A-D11: rewritten tier.
- **Open compute requests:** none.
- **Blockers:** none.
- **Schedule:** on time (Fri 2 Oct, evening). Freeze target is Sat 3 Oct 18:00.
