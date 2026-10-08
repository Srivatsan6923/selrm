"""Count the red items of the paper and print them on the status board (STAGE2_TASKS_D D2).

  python scripts/red_cells.py

Red items of paper/latex_v14/main.tex: every use of the tbd macro (an unmeasured value) and every red note
(ph{...} other than the macro's own definition). Writes the count between the RED markers of
docs/STATUS_BOARD.md and appends one line to docs/RED_COUNT.csv (date, commit, tbd, notes), so a rise between
two merges is visible.
"""
import datetime
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(ROOT, "paper", os.environ.get("SELRM_PAPER", "latex_v14"), "main.tex")
BOARD = os.path.join(ROOT, "docs", "STATUS_BOARD.md")
LOG = os.path.join(ROOT, "docs", "RED_COUNT.csv")
B, E = "<!-- BEGIN RED -->", "<!-- END RED -->"


def count(tex):
    """(tbd cells, red notes with their line numbers) outside comments and macro definitions."""
    tbd, notes = 0, []
    for n, line in enumerate(tex.splitlines(), 1):
        line = re.sub(r"(?<!\\)%.*", "", line)
        if "\\newcommand" in line:
            continue
        tbd += len(re.findall(r"\\tbd(?![A-Za-z])", line))
        notes += [n] * len(re.findall(r"\\ph\{", line))
    return tbd, notes


def main():
    tbd, notes = count(open(PAPER, encoding="utf-8").read())
    head = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    prev = open(LOG, encoding="utf-8").read().strip().splitlines()[-1].split(",") if os.path.exists(LOG) else None
    if not prev:
        open(LOG, "w", encoding="utf-8", newline="\n").write("date,commit,tbd,notes\n")
    line = f"{tbd} unmeasured values (tbd) and {len(notes)} red notes"
    if prev and prev[0] != "date":
        d_t, d_n = tbd - int(prev[2]), len(notes) - int(prev[3])
        line += f"; since the last count ({prev[0]}, {prev[1]}): {d_t:+d} values, {d_n:+d} notes"
        if d_t > 0 or d_n > 0:
            line += " -- THE COUNT ROSE: find out why before anything else"
    if not prev or prev[2:] != [str(tbd), str(len(notes))]:
        open(LOG, "a", encoding="utf-8", newline="\n").write(
            f"{datetime.date.today().isoformat()},{head},{tbd},{len(notes)}\n")
    text = open(BOARD, encoding="utf-8").read()
    a, b = text.index(B) + len(B), text.index(E)
    body = f"\n{line}.\nRed notes at lines: {', '.join(map(str, notes))}.\n"
    open(BOARD, "w", encoding="utf-8", newline="\n").write(text[:a] + body + text[b:])
    print(line)


if __name__ == "__main__":
    main()
