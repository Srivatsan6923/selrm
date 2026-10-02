# STATE role A (maintained by Claude Code)
- **Done (code, tested; 43 tests pass):**
  - selrm/engine.py: canonical records, invariants, tiers, boundary kind, missing twins, reading/application pairs.
  - selrm/folds.py: signature classes and 3 folds.
  - selrm/datasets.py and scripts/build_rule_v1.py: every rule_v1 set, plus folds 2-3.
  - selrm/reference.py: check code and reference graphs (A-D13).
  - Rule batches C1-C3 and S1-S4 merged. Diversity (A-D10) and ablation (A-D12) corpora are in the builder.
- **In progress:**
  - Pre-freeze audit: 300 rendered groups (scratchpad audit/) are being read by four reviewers. Their findings get applied before the freeze.
  - Library: 354 rules (104 hand-written, including 43 scoring; 250 grammar-sampled), plus 60 invented rules for L3-inv. 53 concepts. Phrase banks are final.
- **Next:**
  1. Apply the audit fixes, then run the full tests and a dry-run build.
  2. Freeze:
     - `python scripts/build_rule_v1.py --freeze`, then the same with `--fold 2` and `--fold 3`.
     - `python scripts/dataset_stats.py`, `python scripts/shortcut_scorers.py`, and `python scripts/sample_triplets.py data/rule_v1/test_L2/records.jsonl 100 > docs/SAMPLE_TRIPLETS.md`.
     - Commit the REGISTRY, MANIFESTs, FOLDS and results summaries. Add a HANDOFFS line.
  3. A-D11 rewritten tier on the local RTX 4060 (8 GB): a small open rewriter and two extractors. Verify model IDs first.
- **Open compute requests:** none.
- **Blockers:** none.
- **Schedule:** on time (Fri 2 Oct, evening). Freeze target is Sat 3 Oct 18:00.
