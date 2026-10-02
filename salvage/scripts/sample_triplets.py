"""Render triplets from a set as Markdown for reading by hand.

  python scripts/sample_triplets.py data/test.jsonl [--n 100] [--out docs/SAMPLE_TRIPLETS.md]

One triplet per rule first, then a random fill (fixed seed). Lines that a
case adds relative to the base case are marked with ">>".
"""
import argparse
import json
import random
import sys
from pathlib import Path


def render(t):
    out = [f"### {t['tid']}",
           f"rule `{t['rule']}` ({t['family']}), criterion `{t['criterion']}`, near-miss "
           f"`{t['nm_kind']}`, tier `{t['tier']}`, split `{t['split']}`", "",
           f"**Rule.** {t['rule_text']}", ""]
    for kind, (s, s1) in t["claims"].items():
        out.append(f"- {kind}: s = \"{s}\" | s' = \"{s1}\"")
    base = set(t["cases"]["base"]["text"].split("\n"))
    for k, case in t["cases"].items():
        lines = case["text"].split("\n")
        mark = [("   " if k in ("base", "pres") or s in base else ">> ") + s for s in lines]
        label = ", ".join(f"{c} {v}" for c, v in case["labels"].items())
        out += ["", f"**{k}** (labels: {label})", "```", *mark, "```"]
    out += ["", "near-miss ledger: " + " / ".join(
        f"{e['found']} [{e['subject']}, {e['status']}, {e['time']}]" for e in t["cases"]["near"]["ledger"]),
        ""]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Render sample triplets as Markdown.")
    ap.add_argument("set", type=Path)
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", type=Path)
    a = ap.parse_args(argv)
    ts = [json.loads(s) for s in a.set.read_text(encoding="utf-8").splitlines() if s.strip()]
    rng = random.Random(a.seed)
    rng.shuffle(ts)
    first = list({t["rule"]: t for t in reversed(ts)}.values())[:a.n]
    rest = [t for t in ts if t not in first]
    pick = first + rest[:a.n - len(first)]
    doc = (f"# Sample triplets\n\n{len(pick)} triplets from `{a.set.as_posix()}` (seed {a.seed}): one "
           f"per rule, then random. `>>` marks lines a case adds relative to the base case.\n\n"
           + "\n".join(render(t) for t in pick))
    if a.out:
        a.out.write_text(doc, encoding="utf-8")
        print(f"wrote {len(pick)} triplets to {a.out}")
    else:
        sys.stdout.write(doc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
