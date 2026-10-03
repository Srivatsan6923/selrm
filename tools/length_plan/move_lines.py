"""Report the v13 source line range of every span each move cuts.

Usage: python move_lines.py base/main.tex
"""
import sys

import apply_moves as am

base = open(sys.argv[1], encoding="utf-8").read()
spans = []
_cut, _cut_env = am.cut, am.cut_env


def rec(moved):
    i = base.find(moved)
    if i < 0:
        spans.append("(text not found verbatim in v13)")
        return
    a = base.count("\n", 0, i) + 1
    b = base.count("\n", 0, i + len(moved)) + 1
    spans.append(f"{a}-{b}")


def cut(text, start, end, pointer=""):
    t, mv = _cut(text, start, end, pointer)
    rec(mv)
    return t, mv


def cut_env(text, label):
    t, env = _cut_env(text, label)
    rec(env.replace("[!ht]", "[t]", 1))
    return t, env


am.cut, am.cut_env = cut, cut_env
text = base
for m in am.MOVES:
    spans.clear()
    text = m(text)
    print(f"{m.__name__}\t{', '.join(spans)}\t{m.__doc__.strip().splitlines()[0]}")
