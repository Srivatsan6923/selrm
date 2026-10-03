"""Check that the trial loses no content of the v13 main text.

1. Every sentence of the v13 main text (abstract to Conclusion) must occur
   verbatim (whitespace-normalised) somewhere in the trial document; the
   sentences that do not are printed (expected: pointers rewritten in place,
   self-references adjusted, duplicates of appendix text).
2. The multiset of numbers and \\ph{} values in the whole v13 document must be
   contained in the trial document.
3. Every \\label of v13 must still exist.

Usage: python check_nothing_lost.py base/main.tex trial/step_20/main.tex
"""
import re
import sys
from collections import Counter


def body(path):
    t = open(path, encoding="utf-8").read()
    return " ".join(t.split("\\begin{document}", 1)[1].split())


base, trial = body(sys.argv[1]), body(sys.argv[2])
main = base.split("\\section*{Limitations}")[0]
# break at environments, headings, labels and captions so that no "sentence" spans a float or heading
main = re.sub(r"\\(?:begin|end)\{[^}]*\}(?:\[[^\]]*\])?|\\(?:sub)?section\*?\{[^}]*\}|\\paragraph\{[^}]*\}"
              r"|\\label\{[^}]*\}|\\caption\{|\\noindent", "\n", main)
sentences = [s.strip().rstrip("}").strip() for part in main.split("\n")
             for s in re.split(r"(?<=[.;:])\s+(?=[A-Z\\(])", part)]
sentences = [s for s in sentences if len(s) > 25 and "&" not in s]   # table rows are checked as numbers
missing = [s for s in sentences if s not in trial]
print(f"main-text sentences: {len(sentences)}; found verbatim in the trial: {len(sentences) - len(missing)};"
      f" not found verbatim: {len(missing)}")
for s in missing:
    print("  -", s[:160])

num = re.compile(r"\\ph\{[^{}]*\}|\d+(?:\.\d+)?")
cb, ct = Counter(num.findall(base)), Counter(num.findall(trial))
lost = {k: cb[k] - ct[k] for k in cb if cb[k] > ct[k]}
print(f"numbers/placeholders in v13: {sum(cb.values())}; in trial: {sum(ct.values())}; lost: {lost}")

lb = set(re.findall(r"\\label\{([^}]*)\}", base))
lt = set(re.findall(r"\\label\{([^}]*)\}", trial))
print(f"labels in v13 missing from the trial: {sorted(lb - lt)}; new labels: {sorted(lt - lb)}")
