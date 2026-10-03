# HANDOFFS (append-only)

date | from | to | what | path
---|---|---|---|---
2026-10-02 | setup | all | foundation: schema, prompts, metrics, smoke generator, shortcut validation, tests | selrm/, scripts/, tests/
2026-10-02 | A | B, C, D | rule_v1 frozen (fold 1). Sets: test_L2 (2,000 triplets on held-out signature classes), dev (300), train_{natural,balanced,blocks,triplets} (60k records each, 15% presentation and 15% missing-input cases), missing and dev_missing (MR at 5% FR), test_L0/L1/L3alt/L3inv, test_hard, readapply (composition gap), div_* (diversity curves), abl_* (ablations); rule_v1_fold2/3 hold test_L2, dev and the blocks/triplets corpora. Records are not in git: rebuild with python scripts/build_rule_v1.py [--fold 2|3] and compare sha256 with data/REGISTRY.json. Notes: docs/DATA_A.md. Check code and reference graphs: selrm/reference.py | data/REGISTRY.json
2026-10-02 | A | B | Corpora for the two new experiments are frozen in rule_v1 (commit a8add2d; build-data <a8add2d sha12>, new names only). Leave one near-miss kind out: rule_v1/train_triplets_lo_{subject,negation,time}. Near-miss dose: rule_v1/train_dose_{05,12,25} (0% = train_blocks, 50% = train_triplets, same pool). Frozen sets are unchanged and the new code rebuilds them byte-identically. | data/REGISTRY.json; docs/DATA_A.md
