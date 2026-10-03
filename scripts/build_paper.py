r"""Build the paper; the build fails while any placeholder remains (FINAL_TASKS_D P0.3).

  python scripts/build_paper.py            # make_tables + update_paper + LaTeX; draft PDF
  python scripts/build_paper.py --final    # the same with \placeholdersfalse forced

Output: paper/build/main.pdf (and main.log). The exit status is 1 while any \ph{...} or
\res key without a value remains (the draft PDF is still written, with placeholders in
red); with --final LaTeX itself stops at the first placeholder. LaTeX: latexmk or
pdflatex + bibtex if installed, else tectonic (TECTONIC environment variable or PATH).
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.join(ROOT, "paper", "latex_v13")
BUILD = os.path.join(ROOT, "paper", "build")


def sh(cmd, cwd=ROOT):
    print("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd).returncode


def latex(final):
    shutil.rmtree(BUILD, ignore_errors=True)
    shutil.copytree(PAPER, BUILD, ignore=shutil.ignore_patterns("*.json", "*.pdf"))
    if final:
        p = os.path.join(BUILD, "main.tex")
        t = open(p, encoding="utf-8").read()
        open(p, "w", encoding="utf-8", newline="\n").write(
            re.sub(r"^\\placeholderstrue$", r"\\placeholdersfalse", t, flags=re.M))
    if shutil.which("latexmk"):
        return sh(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], BUILD)
    if shutil.which("pdflatex") and shutil.which("bibtex"):
        rc = 0
        for cmd in (["pdflatex"], ["bibtex"], ["pdflatex"], ["pdflatex"]):
            arg = ["main"] if cmd == ["bibtex"] else ["-interaction=nonstopmode", "-halt-on-error", "main.tex"]
            rc = sh(cmd + arg, BUILD) if cmd != ["bibtex"] else (sh(cmd + arg, BUILD), 0)[1]
            if rc:
                return rc
        return rc
    tec = os.environ.get("TECTONIC") or shutil.which("tectonic")
    if not tec:
        print("no LaTeX found: install TeX Live or set TECTONIC to a tectonic binary")
        return 2
    return sh([tec, "-X", "compile", "main.tex", "--keep-logs"], BUILD)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--final", action="store_true")
    a = ap.parse_args()
    py = sys.executable
    if sh([py, os.path.join("scripts", "make_tables.py")]):
        sys.exit("make_tables.py failed")
    sh([py, os.path.join("scripts", "update_paper.py")])
    rc_latex = latex(a.final)
    rc_check = sh([py, os.path.join("scripts", "update_paper.py"), "--check"])
    pdf = os.path.join(BUILD, "main.pdf")
    print(f"LaTeX exit {rc_latex}; PDF {'written: ' + pdf if os.path.exists(pdf) else 'not written'}")
    if rc_latex or rc_check:
        sys.exit(1)


if __name__ == "__main__":
    main()
