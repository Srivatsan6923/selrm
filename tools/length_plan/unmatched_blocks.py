"""Trial blocks without a block matched in both v13 builds (no measured calibration).

Usage: python unmatched_blocks.py AUTHORS.pdf BASE_TECTONIC.pdf TRIAL.pdf
"""
import sys
from collections import Counter

import calib

a = Counter(k for k, _ in calib.blocks(sys.argv[1]))
t = Counter(k for k, _ in calib.blocks(sys.argv[2]))
matched = {k for k in t if k in a and a[k] == t[k]}
rows = [(k, n) for k, n in calib.blocks(sys.argv[3]) if k not in matched]
kinds = Counter("heading" if n == 1 and k[:1].isdigit() else ("in v13, unmatched there" if k in t else "new or rewritten")
                for k, n in rows)
for k, n in rows:
    print(f"{n:3d} lines  {k!r}")
print(f"total {len(rows)}: " + ", ".join(f"{v} {kk}" for kk, v in kinds.items()))
