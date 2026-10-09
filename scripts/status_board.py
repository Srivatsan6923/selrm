"""Rewrite the generated block of docs/STATUS_BOARD.md: run counts per paper item.

  python scripts/status_board.py

Counts come from docs/RUN_MATRIX_<role>.csv (each role's own rows) and the run
directories in results/ and results_git/: DONE file = done, CLAIMED_* without
DONE = claimed, else the matrix status. Everything outside the markers is
hand-written and left alone.
"""
import csv
import glob
import os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(ROOT, "docs", "STATUS_BOARD.md")
BEGIN, END = "<!-- BEGIN GENERATED: scripts/status_board.py -->", "<!-- END GENERATED -->"


def run_state(run_id):
    for top in ("results", "results_git"):
        d = os.path.join(ROOT, top, run_id)
        if os.path.exists(os.path.join(d, "DONE")):
            return "done"
    for top in ("results", "results_git"):
        if glob.glob(os.path.join(ROOT, top, run_id, "CLAIMED_*")):
            return "claimed"
    return None


def main():
    rows = {}
    for role in "ABCD":
        p = os.path.join(ROOT, "docs", f"RUN_MATRIX_{role}.csv")
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8")):
                rows[r["run_id"]] = r
    by_item = defaultdict(Counter)
    for rid, r in rows.items():
        st = run_state(rid) or (r.get("status") or "todo").strip() or "todo"
        by_item[(r["paper_item"], r["owner"])][st] += 1
    states = ["done", "claimed", "running", "requested", "todo", "failed", "dropped"]
    seen = sorted({s for c in by_item.values() for s in c} - set(states))
    cols = states + seen
    out = [BEGIN, "", "| paper item | owner | " + " | ".join(cols) + " | total |",
           "|---|---|" + "---|" * (len(cols) + 1)]
    for (item, owner), c in sorted(by_item.items()):
        out.append(f"| {item} | {owner} | " + " | ".join(str(c.get(s, 0)) for s in cols)
                   + f" | {sum(c.values())} |")
    tot = Counter()
    for c in by_item.values():
        tot.update(c)
    out.append("| **all** | | " + " | ".join(str(tot.get(s, 0)) for s in cols) + f" | {sum(tot.values())} |")
    out += ["", END]
    text = open(BOARD, encoding="utf-8").read()
    a, b = text.index(BEGIN), text.index(END) + len(END)
    open(BOARD, "w", encoding="utf-8", newline="\n").write(text[:a] + "\n".join(out) + text[b:])
    print(f"{len(rows)} matrix rows, {sum(tot.values())} counted")


if __name__ == "__main__":
    main()
