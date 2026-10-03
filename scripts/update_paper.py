r"""Put the generated tables and measured numbers into the paper (FINAL_TASKS_D P0.3).

  python scripts/update_paper.py            # apply, report, switch placeholders off when none remain
  python scripts/update_paper.py --check    # change nothing; exit 1 while any placeholder remains

Run scripts/make_tables.py first. This script
1. replaces the body between each "% <tables:name>" and "% </tables:name>" line of
   paper/latex_v13/main.tex with tables/<name>.tex;
2. copies tables/numbers.tex next to main.tex (\res{key} reads it);
3. lists every sentence whose \res numbers changed by more than one point since the last
   update (paper/latex_v13/numbers_applied.json), and every table cell that did
   (paper/latex_v13/cells_applied.json);
4. counts the placeholders left (\ph{...} in the document body, \res keys without a value)
   and switches \placeholderstrue to \placeholdersfalse only when none is left.
It edits nothing else: the text outside the marked bodies is compared before and after,
apart from the \placeholders switch, and the script stops if it differs.
"""
import argparse
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(ROOT, "paper", "latex_v13")
TABLES = os.path.join(ROOT, "tables")
MARK = re.compile(r"^% <tables:([\w-]+)>$")
NUM = re.compile(r"-?\d+(?:\.\d+)?")


def bodies(lines):
    """{name: (start index of the opening marker, index of the closing marker)}."""
    out, i = {}, 0
    while i < len(lines):
        m = MARK.match(lines[i])
        if m:
            name = m.group(1)
            j = lines.index(f"% </tables:{name}>", i + 1)
            out[name] = (i, j)
            i = j
        i += 1
    return out


def outside(text):
    """The text outside the marked bodies, with the placeholder switch normalised."""
    lines = text.split("\n")
    keep, skip = [], False
    for ln in lines:
        if MARK.match(ln):
            skip = True
            keep.append(ln)
        elif skip and ln.startswith("% </tables:"):
            skip = False
            keep.append(ln)
        elif not skip:
            keep.append(re.sub(r"\\placeholders(true|false)$", r"\\placeholdersX", ln))
    return "\n".join(keep)


def document_body(text):
    """main.tex after \begin{document}, comments removed."""
    body = text.split(r"\begin{document}", 1)[-1]
    return "\n".join(re.sub(r"(?<!\\)%.*", "", ln) for ln in body.split("\n"))


def placeholders(text, numbers):
    body = document_body(text)
    ph = [m.start() for m in re.finditer(r"\\ph\{", body)]
    keys = sorted(set(re.findall(r"\\res\{([^{}]+)\}", body)))
    unresolved = [k for k in keys if (numbers.get(k) or {}).get("number") is None]
    return len(ph), unresolved, keys


def sentences(text):
    """[(line number, sentence)] of the document body; sentences end at '. ' or a blank line."""
    body_start = text.split("\n").index(r"\begin{document}") if r"\begin{document}" in text.split("\n") else 0
    lines = text.split("\n")
    out, buf, start = [], [], None
    for n, ln in enumerate(lines[body_start:], body_start + 1):
        ln = re.sub(r"(?<!\\)%.*", "", ln)
        if not ln.strip():
            if buf:
                out.append((start, " ".join(buf)))
            buf, start = [], None
            continue
        for part in re.split(r"(?<=[.?!])\s+(?=[A-Z\\])", ln.strip()):
            if start is None:
                start = n
            buf.append(part)
            if re.search(r"[.?!]$", part):
                out.append((start, " ".join(buf)))
                buf, start = [], None
    if buf:
        out.append((start, " ".join(buf)))
    return out


def changed(old, new):
    try:
        return abs(float(old) - float(new)) > 1.0
    except (TypeError, ValueError):
        return old != new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    tex_path = os.path.join(PAPER, "main.tex")
    text = open(tex_path, encoding="utf-8").read()
    numbers = json.load(open(os.path.join(TABLES, "numbers.json"), encoding="utf-8"))

    if not a.check:
        lines = text.split("\n")
        for name, (i, j) in sorted(bodies(lines).items(), key=lambda kv: -kv[1][0]):
            src = os.path.join(TABLES, f"{name}.tex")
            if not os.path.exists(src):
                sys.exit(f"tables/{name}.tex missing: run scripts/make_tables.py")
            new = open(src, encoding="utf-8").read().rstrip("\n").split("\n")
            lines[i + 1:j] = new
        new_text = "\n".join(lines)
        if outside(new_text) != outside(text):
            sys.exit("refusing to write: text outside the marked bodies would change")
        # 3. what changed since the last update
        applied_p = os.path.join(PAPER, "numbers_applied.json")
        applied = json.load(open(applied_p, encoding="utf-8")) if os.path.exists(applied_p) else {}
        moved = {k: (applied[k], v["value"]) for k, v in numbers.items()
                 if k in applied and changed(applied[k], v["value"] if v["number"] is not None else None)}
        report = []
        for n, s in sentences(new_text):
            ks = [k for k in re.findall(r"\\res\{([^{}]+)\}", s) if k in moved]
            if ks:
                report.append(f"line {n}: {s}\n    " + "; ".join(f"{k}: {moved[k][0]} -> {moved[k][1]}" for k in ks))
        prov = json.load(open(os.path.join(TABLES, "PROVENANCE.json"), encoding="utf-8"))
        cells_p = os.path.join(PAPER, "cells_applied.json")
        old_cells = json.load(open(cells_p, encoding="utf-8")) if os.path.exists(cells_p) else {}
        new_cells = {f"{t}|{c['row']}|{c['col']}": c["value"] for t, cs in prov["tables"].items() for c in cs}
        cell_moves = [f"{k}: {old_cells[k]} -> {v}" for k, v in sorted(new_cells.items())
                      if k in old_cells and old_cells[k] != v
                      and changed(*(NUM.search(x).group() if NUM.search(x) else x for x in (old_cells[k], v)))]
        # 4. placeholder switch
        n_ph, unresolved, keys = placeholders(new_text, numbers)
        if n_ph == 0 and not unresolved:
            new_text = re.sub(r"^\\placeholderstrue$", r"\\placeholdersfalse", new_text, flags=re.M)
        open(tex_path, "w", encoding="utf-8", newline="\n").write(new_text)
        shutil.copyfile(os.path.join(TABLES, "numbers.tex"), os.path.join(PAPER, "numbers.tex"))
        json.dump({k: v["value"] for k, v in numbers.items() if v["number"] is not None},
                  open(applied_p, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)
        json.dump(new_cells, open(cells_p, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)
        print(f"{len(bodies(lines))} bodies replaced; numbers.tex copied; {len(keys)} \\res keys in the text")
        print(f"sentences whose numbers moved by more than one point since the last update: {len(report)}")
        for r in report:
            print("  " + r)
        print(f"table cells that moved by more than one point: {len(cell_moves)}")
        for r in cell_moves:
            print("  " + r)
        text = new_text

    n_ph, unresolved, keys = placeholders(text, numbers)
    state = "false" if re.search(r"^\\placeholdersfalse$", text, re.M) else "true"
    print(f"placeholders left: {n_ph} \\ph{{...}} and {len(unresolved)} \\res keys without a value "
          f"(\\placeholders{state})")
    if n_ph or unresolved:
        if a.check:
            for k in unresolved:
                print("  no value: " + k)
        sys.exit(1)


if __name__ == "__main__":
    main()
