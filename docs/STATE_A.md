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
- **In progress:** none.
- **Next:**
  1. A-D11 rewritten tier: verify an open rewriter and two extractor models, run them on the local RTX 4060, and report the acceptance rate.
  2. Copy data/rule_v1* to the Shared Drive (selrm/data/).
  3. After the C pilot (4 Oct): if NO-GO, build rule_v2 with a 60% hard-tier share and combined tiers.
- **Open compute requests:** none.
- **Blockers:** none.
- **Schedule:** on time (Fri 2 Oct, evening). Freeze target is Sat 3 Oct 18:00.
