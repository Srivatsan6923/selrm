"""Layout risk check: what happens to the main-text length when tbd cells are filled.

Copies a trial folder, then in the main text only (before the Limitations
heading):
  --fill  every \\ph{tbd} becomes the dummy "00.0" (four characters, like a
          measured percentage); other placeholders keep their printed width;
  --sd    cells of seeded rows (Table 'tab:factorial', trained rows of
          'tab:main') also get the generator's suffix \\sd{0.0} (mean +- s.d.).
The dummy values are layout fillers for this measurement only.

Usage: python sim_fill.py TRIAL_DIR OUT_DIR [--sd]
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import floatcheck  # noqa: E402

SD_DEF = "\\providecommand{\\sd}[1]{\\,{\\scriptsize$\\pm$#1}}\n"


def env_span(text, label):
    i = text.index("\\label{" + label + "}")
    b = max(text.rfind("\\begin{table", 0, i), text.rfind("\\begin{figure", 0, i))
    e = re.compile(r"\\end\{(table|figure)\*?\}").search(text, i).end()
    return b, e


def add_sd(table, rows_from=None, rows_to=None):
    out, on = [], rows_from is None
    for line in table.split("\n"):
        if rows_from and rows_from in line:
            on = True
        if rows_to and rows_to in line:
            on = False
        if on and "&" in line and line.rstrip().endswith("\\\\") and "multicolumn" not in line:
            cells = line.rstrip()[:-2].split("&")
            new = [cells[0]] + [re.sub(r"(00\.0|\d+\.\d|100\.0)", r"\1\\sd{0.0}", c, count=1)
                                if re.search(r"\d", c) and "approx" not in c else c for c in cells[1:]]
            line = "&".join(new) + "\\\\"
        out.append(line)
    return "\n".join(out)


def main():
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    sd = "--sd" in sys.argv
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(src, out)
    tex = (out / "main.tex").read_text(encoding="utf-8")
    head, tail = tex.split("\\section*{Limitations}", 1)
    pre, body = head.split("\\begin{document}", 1)
    n = body.count("\\ph{tbd}")
    body = body.replace("\\ph{tbd}", "00.0")
    if sd:
        pre += SD_DEF
        doc = body
        b, e = env_span(doc, "tab:factorial")
        doc = doc[:b] + add_sd(doc[b:e]) + doc[e:]
        b, e = env_span(doc, "tab:main")
        doc = doc[:b] + add_sd(doc[b:e], "Trained without medical QA data", "References") + doc[e:]
        body = doc
    (out / "main.tex").write_text(pre + "\\begin{document}" + body + "\\section*{Limitations}" + tail,
                                  encoding="utf-8", newline="\n")
    subprocess.run(["D:/NAACL27/tools/tectonic.exe", "-X", "compile", "main.tex", "--keep-logs"],
                   cwd=out, capture_output=True, text=True)
    lim, lim_pos, eff, report = floatcheck.check(str(out / "main.tex"), str(out / "main.pdf"))
    log = (out / "main.log").read_text(errors="replace")
    over = re.findall(r"Overfull \\hbox \(([\d.]+)pt too wide\) in (?:paragraph|alignment) at lines (\d+)--", log)
    print(f"{out}: replaced {n} tbd; sd={sd}; Limitations p{lim[0]}{lim[1]} y={lim[2]:.1f}"
          f" heading={lim_pos:.3f} effective={eff:.3f}; overfull: {over}")


if __name__ == "__main__":
    main()
