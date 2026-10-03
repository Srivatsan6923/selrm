"""Main-text length of an ACL two-column PDF: where the Limitations heading starts.

Length = full pages before the Limitations page + fraction of that page, where
a page is two columns of 52 body lines (13.55 pt pitch, first line top at
~73.5 pt). Left column counts as the first half of the page.
"""
import sys
import fitz

COL_TOP = 73.5        # top of the first body line's bbox
COL_H = 52 * 13.55    # 52 lines per column
MID_X = 297.6         # page centre between the two columns


def find_heading(doc, title, size=12.0):
    for pno, page in enumerate(doc):
        for b in page.get_text("dict")["blocks"]:
            if b["type"] != 0:
                continue
            for l in b["lines"]:
                t = "".join(s["text"] for s in l["spans"]).strip()
                sz = max(s["size"] for s in l["spans"])
                if t == title and abs(sz - size) < 0.6:
                    return pno + 1, l["bbox"]
    return None, None


def length(doc, title="Limitations"):
    pno, bb = find_heading(doc, title)
    if pno is None:
        return None
    right = bb[0] > MID_X
    frac_col = (bb[1] - COL_TOP) / COL_H
    frac = (0.5 if right else 0.0) + 0.5 * frac_col
    return pno, "right" if right else "left", bb[1], (pno - 1) + frac


if __name__ == "__main__":
    for path in sys.argv[1:]:
        d = fitz.open(path)
        r = length(d)
        c = length(d, "Conclusion")
        print(f"{path}\n  pages={len(d)} Limitations: page {r[0]} {r[1]} column y={r[2]:.1f}"
              f" -> main text = {r[3]:.3f} pages; Conclusion heading: page {c[0]} {c[1]} y={c[2]:.1f}")
