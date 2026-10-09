"""Resolve merge conflicts in append-only tables (docs/HANDOFFS.md, docs/CHANGE_REQUESTS.md):
keep every line of both sides (ours first), drop exact duplicates. Lead's daily merge.

  python scripts/union_merge.py docs/HANDOFFS.md docs/CHANGE_REQUESTS.md
"""
import re
import sys

CONFLICT = re.compile(r"<<<<<<< [^\n]*\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n", re.S)

for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()

    def union(m):
        lines = m.group(1).splitlines(keepends=True)
        return "".join(lines + [x for x in m.group(2).splitlines(keepends=True) if x not in lines])
    new, n = CONFLICT.subn(union, text)
    open(path, "w", encoding="utf-8", newline="\n").write(new)
    print(f"{path}: {n} conflict(s) resolved by union")
