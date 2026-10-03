"""Per-paragraph calibration between the authors' pdflatex build and tectonic.

For every main-text block (matched by its first words) the line-count
difference tectonic - pdflatex is measured on the two v13 builds. For a trial
PDF built with tectonic, the predicted pdflatex length is the trial length
minus the summed differences of the blocks that are still in its main text.

Usage: python calib.py AUTHORS.pdf BASE_TECTONIC.pdf TRIAL.pdf [TRIAL.pdf ...]
"""
import re
import sys
from collections import defaultdict

import inventory

PITCH, PAGE_LINES = 13.55, 104


def key(text):
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff")
    words = re.sub(r"[^A-Za-z0-9 ]", " ", text).split()
    return " ".join(words[:6]).lower()


def blocks(pdf):
    flow, floats = inventory.analyse(pdf)
    return [(key(b["text"]), b["nlines"]) for b in inventory.blocks(flow) if b["text"] != "<<STOP>>"]


def main():
    auth, tect = blocks(sys.argv[1]), blocks(sys.argv[2])
    a, t = defaultdict(list), defaultdict(list)
    for k, n in auth:
        a[k].append(n)
    for k, n in tect:
        t[k].append(n)
    diff = {}
    for k in t:
        if k in a and len(a[k]) == len(t[k]):
            diff[k] = sum(t[k]) - sum(a[k])
    total = sum(diff.values())
    unmatched = [k for k in t if k not in diff]
    print(f"matched blocks {len(diff)}; tectonic - pdflatex = {total} lines over matched blocks;"
          f" unmatched tectonic blocks: {unmatched}")
    for k, v in sorted(diff.items(), key=lambda kv: -kv[1]):
        if v:
            print(f"   {v:+d}  {k}")
    for trial in sys.argv[3:]:
        tb = blocks(trial)
        kept = {k for k, _ in tb}
        off = sum(v for k, v in diff.items() if k in kept)
        new = [k for k in kept if k not in diff]
        print(f"{trial}: retained-block offset {off} lines = {off / PAGE_LINES:.3f} pages;"
              f" blocks not in base (pointers, edited paragraphs): {len(new)}")


if __name__ == "__main__":
    main()
