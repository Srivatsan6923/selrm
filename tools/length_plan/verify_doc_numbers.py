"""List every number in LENGTH_PLAN.md that does not occur in the saved logs/scripts.

Usage: python verify_doc_numbers.py ../path/LENGTH_PLAN.md
"""
import re
import sys
from pathlib import Path

doc = Path(sys.argv[1]).read_text(encoding="utf-8")
sources = ["lengths.txt", "calib.txt", "trial_run.txt", "summary.txt", "sim.txt", "nothing_lost.txt",
           "numbering.txt", "lm_auth.txt", "lm_tect.txt", "plan_tables.md", "variant_o1.txt",
           "unmatched_trial_blocks.txt", "floatcheck_step11.txt", "move_lines.tsv", "dump_auth.txt",
           "base/main.log", "measure.py", "inventory.py", "trial_head_run.txt", "sim_head.txt", "provenance.txt"]
pool = " ".join(Path(s).read_text(encoding="utf-8", errors="replace") for s in sources)
pool_nums = set(re.findall(r"\d+(?:\.\d+)?", pool.replace(",", "")))
pool_nums |= {n.rstrip("0").rstrip(".") for n in pool_nums if "." in n}
# drop LaTeX/code spans: numbers inside backticks are quoted source, not results
text = re.sub(r"`[^`]*`", " ", doc)
missing = []
for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
    n = m.group(0).replace(",", "")
    alt = n.rstrip("0").rstrip(".") if "." in n else n
    if n not in pool_nums and alt not in pool_nums:
        ctx = text[max(0, m.start() - 40):m.end() + 20].replace("\n", " ")
        missing.append((n, ctx))
for n, ctx in missing:
    print(f"{n:>8}  ...{ctx}...")
print(f"{len(missing)} numbers not found in the logs")
