"""List block starts (headings, floats, paragraphs) of the v13 main text with line numbers."""
import re
import sys

lines = open(sys.argv[1], encoding="utf-8").read().split("\n")
pat = re.compile(r"^(\\section|\\subsection|\\paragraph|\\begin\{(table|figure|abstract|proposition|equation|align)"
                 r"|\\end\{(table|figure|abstract|proposition|equation|align)|\\emph\{[A-Z]|\\noindent|\\maketitle|\\smallskip)")
prev_blank = True
for i, l in enumerate(lines, 1):
    if i > int(sys.argv[2]):
        break
    if i >= 68 and (pat.match(l) or (prev_blank and l.strip() and not l.startswith("%"))):
        print(i, l[:90])
    prev_blank = l.strip() == ""
