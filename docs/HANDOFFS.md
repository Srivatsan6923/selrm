# HANDOFFS (append-only)

date | from | to | what | path
---|---|---|---|---
2026-10-02 | setup | all | foundation: schema, prompts, metrics, smoke generator, shortcut validation, tests | selrm/, scripts/, tests/
2026-10-02 | A | B, C, D | rule_v1 frozen (fold 1). Sets: test_L2 (2,000 triplets on held-out signature classes), dev (300), train_{natural,balanced,blocks,triplets} (60k records each, 15% presentation and 15% missing-input cases), missing and dev_missing (MR at 5% FR), test_L0/L1/L3alt/L3inv, test_hard, readapply (composition gap), div_* (diversity curves), abl_* (ablations); rule_v1_fold2/3 hold test_L2, dev and the blocks/triplets corpora. Records are not in git: rebuild with python scripts/build_rule_v1.py [--fold 2|3] and compare sha256 with data/REGISTRY.json. Notes: docs/DATA_A.md. Check code and reference graphs: selrm/reference.py | data/REGISTRY.json
