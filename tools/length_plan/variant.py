"""Optional move O1, measured on top of trial step 19 (Figure 2 kept):
the 'With medical data' and 'References' row groups of Table 4 go to an
appendix table. Needs make_tables.py to emit the 'main' rows as two tables.

Usage: python variant.py BASE_DIR OUT_DIR
"""
import shutil
import sys
from pathlib import Path

import apply_moves as am
import floatcheck


def o1(t):
    t, rows = am.cut(t, "\\multicolumn{9}{@{}l}{\\emph{With medical data}}\\\\",
                     "Extraction + hand-written program & \\ph{tbd} & \\ph{tbd} & \\ph{tbd} & \\ph{tbd}"
                     " & \\ph{tbd} & -- & -- & --\\\\")
    t = am.insert(t, "which is medical supervision and not transfer", r" (Table~\ref{tab:main-more})")
    table = ("\\begin{table}[!ht]\n\\centering\\small\n\\setlength{\\tabcolsep}{3pt}\n"
             "\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\n"
             "System & L2 & L3-alt & XA & Hold & MR & Criteria & TrialGPT & MedEinst\\\\\n\\midrule\n"
             + rows.strip() + "\n\\bottomrule\n\\end{tabular}}\n"
             "\\caption{Rows of Table~\\ref{tab:main} trained with medical data, and references (\\%).}\n"
             "\\label{tab:main-more}\n\\end{table}\n\n")
    return am.insert(t, "\\paragraph{NLI4CT-P.}", table, where="before")


def main():
    base, out = Path(sys.argv[1]), Path(sys.argv[2])
    text = (base / "main.tex").read_text(encoding="utf-8")
    for m in am.MOVES[:19]:
        text = m(text)
    text = o1(text)
    out.mkdir(parents=True, exist_ok=True)
    for f in ("acl.sty", "acl_natbib.bst", "custom.bib", "main.bbl"):
        shutil.copy(base / f, out / f)
    (out / "main.tex").write_text(text, encoding="utf-8", newline="\n")
    rc, undef, multi = am.build(out)
    lim, lim_pos, eff, report = floatcheck.check(str(out / "main.tex"), str(out / "main.pdf"))
    late = [r[1] for r in report if r[3]]
    print(f"steps 1-19 + O1: rc={rc} Limitations p{lim[0]}{lim[1]} y={lim[2]:.1f} effective={eff:.3f}"
          f" undefined={undef} multiply={multi} main_floats_after_Limitations={late}")


if __name__ == "__main__":
    main()
