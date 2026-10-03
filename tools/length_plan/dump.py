"""Dump text lines and drawing boxes of a PDF page range, per column."""
import sys
import fitz

pdf, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
d = fitz.open(pdf)
for pno in range(first - 1, last):
    p = d[pno]
    print(f"===== page {pno + 1} =====")
    items = []
    for b in p.get_text("dict")["blocks"]:
        if b["type"] != 0:
            items.append((b["bbox"], "[image]"))
            continue
        for l in b["lines"]:
            t = "".join(s["text"] for s in l["spans"]).strip()
            x0, y0, x1, y1 = l["bbox"]
            # skip review line numbers and the draft banner
            if x1 < 72 or x0 > 523 or y1 < 60:
                continue
            items.append((l["bbox"], t))
    for dr in p.get_drawings():
        r = dr["rect"]
        if r.y1 < 60 or r.x1 < 72 or r.x0 > 523:
            continue
        items.append(((r.x0, r.y0, r.x1, r.y1), "[draw]"))
    items.sort(key=lambda it: (0 if it[0][0] < 290 else 1, it[0][1]))
    for bb, t in items:
        col = "L" if bb[0] < 290 else "R"
        if bb[2] - bb[0] > 300:
            col = "W"
        print(f"{col} y={bb[1]:6.1f}-{bb[3]:6.1f} x={bb[0]:5.1f}-{bb[2]:5.1f} {t[:70]}")
