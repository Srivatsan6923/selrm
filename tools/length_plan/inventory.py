"""Inventory of main-text blocks of an ACL two-column PDF with measured heights.

Every column (52 lines x 13.55 pt) is split into float space (from the column
top to the first body line, attributed to the captions found there) and body
flow. Body lines are merged per visual line and grouped into blocks: a new
block starts at a section heading, a bold run-in heading, an indented first
line, or the line after a heading. A block's height is the flow distance from
its first line to the next block's first line, with the extra space above each
block (parskip, heading skip) attributed to the block it precedes. Heights are
reported in pt and in body lines (13.55 pt); a page is 104 lines. The title
box (both columns) and the floats are listed separately; everything sums to
the main-text length.

Usage: python inventory.py file.pdf
"""
import re
import sys
import fitz

COL_TOP, PITCH, NLINES = 73.5, 13.55, 52
COL_BOT = COL_TOP + NLINES * PITCH          # where the line after the last would start
TITLE_END = 219.0                           # bottom of the title box on page 1
CAP_RE = re.compile(r"^(Table|Figure) (\d+):")


def is_bold(font):
    return "Medi" in font or "Bold" in font


def visual_lines(page):
    """Merge PyMuPDF lines that share a baseline within a column."""
    raw = []
    for b in page.get_text("dict")["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            spans = [s for s in l["spans"] if s["text"].strip()]
            if not spans:
                continue
            x0, y0, x1, y1 = l["bbox"]
            if x1 < 72 or x0 > 523 or y1 < 62 or y0 > 785:
                continue                                 # line numbers, banner, page no.
            col = "R" if x0 > 297.6 else "L"
            raw.append(dict(col=col, x0=x0, x1=x1, y0=y0, y1=y1, spans=spans,
                            ks=round(max(s["size"] for s in spans))))
    raw.sort(key=lambda r: (r["col"], r["y0"], r["x0"]))
    merged = []
    for r in raw:
        m = merged[-1] if merged else None
        if m and m["col"] == r["col"] and abs(m["y0"] - r["y0"]) < 3.5 and m["ks"] == r["ks"]:
            m["spans"] += r["spans"]
            m["x0"], m["x1"] = min(m["x0"], r["x0"]), max(m["x1"], r["x1"])
            m["y0"], m["y1"] = min(m["y0"], r["y0"]), max(m["y1"], r["y1"])
            continue
        merged.append(r)
    for m in merged:
        m["spans"].sort(key=lambda s: s["bbox"][0])
        m["text"] = " ".join(s["text"].strip() for s in m["spans"])
        sizes = [round(s["size"], 1) for s in m["spans"]]
        m["size"] = max(sizes, key=sizes.count)
        m["maxsize"] = max(sizes)
        m["bold0"] = is_bold(m["spans"][0]["font"])
    return merged


def caption_bottom(lines, cap):
    cb = cap["y1"]
    for v in lines:
        if v["y0"] > cap["y0"] and v["y0"] - cb < 4 and v["size"] < 10.6:
            cb = v["y1"]
    return cb


def analyse(path, stop_title="Limitations"):
    doc = fitz.open(path)
    flow, floats = [], []
    in_abstract = False
    for pno, page in enumerate(doc):
        vl = visual_lines(page)
        start = TITLE_END if pno == 0 else COL_TOP
        cols = {c: [v for v in vl if v["col"] == c and v["y0"] >= start - 1] for c in "LR"}
        body = {}
        for c in "LR":
            out = []
            for v in cols[c]:
                heading = v["maxsize"] > 11.5 and len(v["text"]) < 70
                if heading and v["text"] == "Abstract":
                    in_abstract = True
                elif heading:
                    in_abstract = False
                if heading or 10.6 < v["size"] < 11.3 or (in_abstract and v["size"] > 9.5):
                    v["abstract"] = in_abstract and not heading
                    out.append(v)
            body[c] = out
        # top floats: captions above the first body line of their column
        caps = {c: [v for v in cols[c] if CAP_RE.match(v["text"])] for c in "LR"}
        full = [v for c in "LR" for v in caps[c] if v["x0"] < 75 and v["x1"] > 400]
        firsty = {}
        for c in "LR":
            colcaps = [v for v in caps[c] if v not in full]
            cb = max([caption_bottom(cols[c], v) for v in caps[c]], default=0)
            body[c] = [b for b in body[c] if b["y0"] > cb] if cb and all(
                not any(b["y0"] < v["y0"] for b in body[c]) for v in caps[c]) else body[c]
            firsty[c] = body[c][0]["y0"] if body[c] else COL_BOT
        full_end = start
        if full:
            fb = max(caption_bottom(cols[full[0]["col"]], v) for v in full)
            clean = [c for c in "LR" if not [v for v in caps[c] if v not in full]]
            full_end = min(firsty[c] for c in clean) if clean else fb + 20
            floats.append(dict(page=pno + 1, col="LR", cap=full[0]["text"][:60],
                               space=2 * (full_end - start)))
        for c in "LR":
            colcaps = sorted([v for v in caps[c] if v not in full and
                              not any(b["y0"] < v["y0"] for b in body[c])], key=lambda v: v["y0"])
            prev = full_end
            for i, v in enumerate(colcaps):
                end = (caption_bottom(cols[c], v) + 12.0) if i < len(colcaps) - 1 else firsty[c]
                floats.append(dict(page=pno + 1, col=c, cap=v["text"][:60], space=end - prev))
                prev = end
        for c in "LR":
            for b in body[c]:
                if b["maxsize"] > 11.5 and b["text"].strip() == stop_title:
                    flow.append(dict(page=pno + 1, col=c, y0=b["y0"], text="<<STOP>>", v=b))
                    return flow, floats
                flow.append(dict(page=pno + 1, col=c, y0=b["y0"], text=b["text"], v=b))
    return flow, floats


def blocks(flow):
    firsts = {}
    for i, f in enumerate(flow):
        firsts.setdefault((f["page"], f["col"]), i)
    acc, base = 0.0, {}
    for k in sorted(firsts):
        y = flow[firsts[k]]["y0"]
        base[k] = acc - y
        acc += COL_BOT - y
    for f in flow:
        f["pos"] = base[(f["page"], f["col"])] + f["y0"]
    out, prev_heading = [], False
    for i, f in enumerate(flow):
        v, t = f["v"], f["text"]
        colx = 70.9 if f["col"] == "L" else 306.1
        heading = v["maxsize"] > 11.5 or (re.match(r"^\d\.\d\s", t) is not None and v["bold0"])
        if v.get("abstract"):
            start = not (out and out[-1].get("abstract"))
        else:
            start = heading or prev_heading or v["bold0"] or v["x0"] - colx > 8 or t == "<<STOP>>" or not out
            if out and out[-1].get("abstract"):
                start = True
        if start:
            out.append(dict(i=i, page=f["page"], col=f["col"], y0=f["y0"], text=t,
                            heading=heading, abstract=v.get("abstract", False), nlines=0))
        out[-1]["nlines"] += 1
        prev_heading = heading
    for b in out:
        i = b["i"]
        same = i > 0 and (flow[i - 1]["page"], flow[i - 1]["col"]) == (flow[i]["page"], flow[i]["col"])
        b["extra"] = flow[i]["y0"] - flow[i - 1]["y0"] - PITCH if same else 0.0
    for j, b in enumerate(out[:-1]):
        nxt = out[j + 1]
        b["height"] = flow[nxt["i"]]["pos"] - flow[b["i"]]["pos"] - nxt["extra"] + b["extra"]
    out[-1]["height"] = 0.0
    return out


def main(path):
    flow, floats = analyse(path)
    bl = blocks(flow)
    stop = flow[-1]
    print(f"# {path}: Limitations at page {stop['page']} col {stop['col']} y={stop['y0']:.1f}")
    title = 2 * (TITLE_END - COL_TOP)
    rows = [("T", "p1LR", 0, 0, title, "title box (both columns)")]
    for b in bl:
        rows.append(("B", f"p{b['page']}{b['col']}", round(b["y0"]), b["nlines"], b["height"], b["text"][:72]))
    for f in floats:
        rows.append(("F", f"p{f['page']}{f['col']}", 0, 0, f["space"], f["cap"]))
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]:.1f}\t{r[4] / PITCH:.1f}\t{r[5]}")
    tot = sum(r[4] for r in rows)
    body = sum(r[4] for r in rows if r[0] == "B")
    fl = sum(r[4] for r in rows if r[0] == "F")
    print(f"# title {title / PITCH:.1f} + body {body / PITCH:.1f} + floats {fl / PITCH:.1f}"
          f" = {tot / PITCH:.1f} lines = {tot / PITCH / (2 * NLINES):.3f} pages")


if __name__ == "__main__":
    main(sys.argv[1])
