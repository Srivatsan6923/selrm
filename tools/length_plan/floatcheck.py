"""Effective main-text length: the later of the Limitations heading and the
bottom of every float defined before \\section*{Limitations} in the source.

Usage: python floatcheck.py main.tex main.pdf
"""
import re
import sys
import fitz

COL_TOP, COL_H, MID_X = 73.5, 52 * 13.55, 297.6


def detex(s):
    s = s.replace("\\%", "%").replace("\\bb{}", "Qwen3.5-9B").replace("\\method{}", "Ledger-RM")
    for _ in range(3):
        s = re.sub(r"\\[a-zA-Z]+\*?\{([^{}]*)\}", r"\1", s)
    s = re.sub(r"\\[a-zA-Z]+", "", s).replace("{", "").replace("}", "").replace("~", " ")
    return " ".join(s.split())


def main_floats(tex):
    """(kind, caption prefix, full width) for floats before the Limitations heading."""
    main = tex.split("\\section*{Limitations}")[0]
    out = []
    for m in re.finditer(r"\\begin\{(table|figure)(\*?)\}(.*?)\\end\{\1\2\}", main, re.S):
        cap = re.search(r"\\caption\{(.*)", m.group(3), re.S)
        words = detex(cap.group(1)).split()[:3]
        out.append((m.group(1).capitalize(), " ".join(words), m.group(2) == "*"))
    return out


def pos(page, col, y):
    return page - 1 + (0.5 if col == "R" else 0.0) + 0.5 * (y - COL_TOP) / COL_H


def check(tex_path, pdf_path):
    tex = open(tex_path, encoding="utf-8").read()
    floats = main_floats(tex)
    d = fitz.open(pdf_path)
    lim = None
    caps = []
    for pno, page in enumerate(d):
        lines = []
        for b in page.get_text("dict")["blocks"]:
            if b["type"] == 0:
                lines += b["lines"]
        for i, l in enumerate(lines):
            t = "".join(s["text"] for s in l["spans"]).strip()
            size = max(s["size"] for s in l["spans"])
            col = "R" if l["bbox"][0] > MID_X else "L"
            if t == "Limitations" and abs(size - 12) < 0.6 and lim is None:
                lim = (pno + 1, col, l["bbox"][1])
            m = re.match(r"^(Table|Figure) (\d+): (.*)", t)
            if m:
                # caption bottom: follow caption lines (10 pt) below it in the same block
                bottom = l["bbox"][3]
                for l2 in lines[i + 1:]:
                    if abs(l2["bbox"][0] - l["bbox"][0]) < 3 and 0 < l2["bbox"][1] - bottom < 4:
                        bottom = l2["bbox"][3]
                caps.append((m.group(1), m.group(3), pno + 1, col, bottom))
    lim_pos = pos(*lim)
    report, end = [], lim_pos
    for kind, prefix, full in floats:
        hit = [c for c in caps if c[0] == kind and " ".join(c[1].split()[:3]) == prefix]
        if not hit:
            report.append((kind, prefix, None, None))
            continue
        _, _, p, col, bottom = hit[0]
        fp = (p - 1 + 0.5 * (bottom - COL_TOP) / COL_H) if full else pos(p, col, bottom)
        after = (p, col == "R", bottom) > (lim[0], lim[1] == "R", lim[2]) if not full else p > lim[0]
        report.append((kind, prefix, (p, col, round(bottom)), after))
        if after:
            end = max(end, fp if not full else p - 1 + 0.5 + 0.5 * (bottom - COL_TOP) / COL_H)
    return lim, lim_pos, end, report


if __name__ == "__main__":
    lim, lim_pos, end, report = check(sys.argv[1], sys.argv[2])
    print(f"Limitations p{lim[0]}{lim[1]} y={lim[2]:.1f} -> {lim_pos:.3f}; effective main text {end:.3f} pages")
    for r in report:
        print("  ", r)
