"""Render random triplets of a record file as Markdown for reading (A-D15).

  python scripts/sample_triplets.py data/rule_v1/test_L2/records.jsonl 100 > docs/SAMPLE_TRIPLETS.md

Sampling is stratified by near-miss kind and seeded. For each triplet: rule,
condition, the base case, and the line edits of flip, near-miss and
presentation case relative to base, with the executed answer of each case.
"""
import difflib
import json
import random
import sys
from collections import defaultdict


def main(path, n, seed=0):
    groups = defaultdict(dict)
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if r["claim_type"] == "conclusion" and r["case_kind"] in ("base", "flip", "near", "pres", "missing"):
            groups[r["tid"]].setdefault(r["case_kind"], {})[r["claim_role"]] = r
    by_kind = defaultdict(list)
    for tid, g in sorted(groups.items()):
        if {"base", "flip", "near"} <= set(g):
            by_kind[g["base"]["s"]["nm_kind"]].append(tid)
    rng, kinds = random.Random(seed), sorted(by_kind)
    pick = []
    for i in range(n):
        pool = by_kind[kinds[i % len(kinds)]]
        pick.append(pool.pop(rng.randrange(len(pool))))
    out = [f"# Sample triplets\n\n{n} triplets from `{path}`, stratified by near-miss kind "
           f"(seed {seed}). Lines starting with `-` are removed from the base case and lines "
           "starting with `+` are added to it. **Answer** is the claim the program marks correct.\n"]
    for k, tid in enumerate(pick, 1):
        g = groups[tid]
        b = g["base"]["s"]
        out.append(f"\n## {k}. `{tid}`\n\n- **Rule** ({b['rid']}, {b['family']}): {b['rule_text']}\n"
                   f"- **Condition**: {b['condition']} | near-miss: {b['nm_kind']} | tier: {b['tier']}\n"
                   f"- **Claims**: s = \"{b['claim_text']}\" | s' = \"{g['base']['s_prime']['claim_text']}\"\n")
        base_lines = b["case_text"].split("\n")
        out.append("```\n" + b["case_text"] + "\n```\n")
        for kind in ("flip", "near", "pres", "missing"):
            if kind not in g:
                continue
            r = g[kind]
            ans = "neither" if kind == "missing" else ("s'" if r["s_prime"]["label"] else "s")
            new = r["s"]["case_text"].split("\n")
            diff = [d for d in difflib.unified_diff(base_lines, new, lineterm="", n=0)
                    if d[:1] in "+-" and not d.startswith(("+++", "---"))]
            if kind == "pres":
                diff = [f"(re-rendered: {len(new)} lines, same state)"]
            out.append(f"**{kind}** (answer: {ans})\n```\n" + "\n".join(diff) + "\n```\n")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 100)
