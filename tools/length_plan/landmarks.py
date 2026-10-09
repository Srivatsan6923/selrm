"""List section headings and float captions (page, column, y, flow position)."""
import re
import sys
import fitz

COL_TOP, COL_H, MID_X = 73.5, 52 * 13.55, 297.6


def landmarks(path, last_page=None):
    d = fitz.open(path)
    out = []
    for pno, page in enumerate(d):
        if last_page and pno + 1 > last_page:
            break
        for b in page.get_text("dict")["blocks"]:
            if b["type"] != 0:
                continue
            for l in b["lines"]:
                t = "".join(s["text"] for s in l["spans"]).strip()
                sz = max(s["size"] for s in l["spans"])
                x0, y0 = l["bbox"][0], l["bbox"][1]
                if x0 < 60 or y0 < 60 or y0 > 790:
                    continue
                head = (sz > 11.5 and re.match(r"^[0-9A-Z]", t) and len(t) < 60) or \
                       (re.match(r"^\d\.\d$", t) and sz > 10.5)
                cap = re.match(r"^(Table|Figure) \d+:", t)
                if head or cap:
                    col = "R" if x0 > MID_X else "L"
                    pos = pno + (0.5 if col == "R" else 0) + 0.5 * (y0 - COL_TOP) / COL_H
                    out.append((pno + 1, col, round(y0, 1), round(pos, 3), t[:50]))
    return out


if __name__ == "__main__":
    for row in landmarks(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else None):
        print(*row, sep="\t")
