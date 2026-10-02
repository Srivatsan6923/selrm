# STATE role A (maintained by Claude Code)
- **Done (code, tested; 45 tests pass):**
  - selrm/engine.py: canonical records, invariants, tiers, boundary kind, missing twins, reading/application pairs.
  - selrm/folds.py: signature classes and 3 folds.
  - selrm/datasets.py and scripts/build_rule_v1.py: every rule_v1 set, plus folds 2-3.
  - selrm/reference.py: check code and reference graphs (A-D13).
  - Rule batches C1-C3 and S1-S4 merged. Diversity (A-D10) and ablation (A-D12) corpora are in the builder.
- **rule_v1 frozen** on 2 Oct (fold 1), with rule_v1_fold2 and rule_v1_fold3:
  - data/REGISTRY.json and MANIFESTs are committed. Records are rebuilt with scripts/build_rule_v1.py and checked against the sha256 values.
  - Shortcut-scorer results are in results/A-D14-*; statistics in results/A-D15; samples in docs/SAMPLE_TRIPLETS.md.
  - Two audit rounds read 450 rendered groups and found no label errors; consistency fixes were applied before the freeze.
- **New corpora (2 Oct, evening).** Six corpora for the two new experiments are frozen in rule_v1, built from a8add2d:
  - train_triplets_lo_{subject,negation,time};
  - train_dose_{05,12,25}.
  The new code reproduces the frozen sets byte-identically.
- **In progress:** A-D11, the rewritten-note tier, using API models.
- **Next:**
  1. A-D11:
     - verify the rewriter and extractor model IDs;
     - rewrite the test_L2 cases;
     - keep a group only if two extractors recover the full state of all its cases;
     - report the acceptance rate;
     - publish rule_v1/rewritten.
  2. If C's pilot (Sun 4 Oct) is NO-GO, build rule_v2 with a 60% hard-tier share.
  3. Appendix B and C text.
- **Open compute requests:** #1 (2 Oct): an API key for the rewritten tier (see the request in the session).
- **Blockers:** none.
- **Schedule:** on time (Fri 2 Oct, evening). Freeze target is Sat 3 Oct 18:00.
