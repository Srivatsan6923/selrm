"""Derived numbers for the plan, read from the saved logs in this folder.

lengths.txt     measure.py on the authors' PDF and the base tectonic build
calib.txt       calib.py (retained-paragraph offset of the trial)
trial_run.txt   apply_moves.py (effective main-text length per step)
variant_o1.txt  variant.py (steps 1-19 plus optional move O1)
sim.txt         sim_fill.py (placeholders filled, with and without s.d.)
"""
import re

PAGE = 104
lengths = re.findall(r"main text = ([\d.]+) pages", open("lengths.txt").read())
pdf_len, tec_len = float(lengths[0]), float(lengths[1])
base_off = tec_len - pdf_len
cal = open("calib.txt").read()
ret_off = float(re.search(r"step_20/main.pdf: retained-block offset \d+ lines = ([\d.]+) pages", cal).group(1))
steps = {int(m.group(1)): float(m.group(2)) for m in
         re.finditer(r"^\s*(\d+) \w+\s+rc=0 .*? effective=([\d.]+)", open("trial_run.txt").read(), re.M)}
o1 = float(re.search(r"effective=([\d.]+)", open("variant_o1.txt").read()).group(1))
sim = {m.group(1): float(m.group(2)) for m in
       re.finditer(r"sim\W(\w+): .*? effective=([\d.]+)", open("sim.txt").read())}
over = re.search(r"fillsd_step_20: .*?overfull: \[\('([\d.]+)'", open("sim.txt").read()).group(1)

print(f"pdflatex (authors) {pdf_len:.3f} pages; tectonic {tec_len:.3f}; offset {base_off:.3f} pages"
      f" = {base_off * PAGE:.1f} lines")
print(f"to reach 8.000: pdflatex must lose {(pdf_len - 8) * PAGE:.1f} lines, tectonic {(tec_len - 8) * PAGE:.1f}")
print(f"trial offset range: {ret_off:.3f} (retained paragraphs) to {base_off:.3f} (whole v13) pages")
for name, t in (("step 19 (moves 1-19)", steps[19]), ("step 20 (moves 1-20)", steps[20]),
                ("steps 1-19 + O1", o1)):
    lo, hi = t - base_off, t - ret_off
    print(f"{name}: tectonic {t:.3f}; predicted pdflatex {lo:.3f} to {hi:.3f};"
          f" slack to 8.000 at the long end {(8 - hi) * PAGE:+.1f} lines, at the short end {(8 - lo) * PAGE:+.1f} lines")
print(f"saved by moves 1-20: tectonic {(steps[0] - steps[20]) * PAGE:.1f} lines;"
      f" moves 1-19: {(steps[0] - steps[19]) * PAGE:.1f} lines; move 20 alone: {(steps[19] - steps[20]) * PAGE:.1f};"
      f" O1 on top of step 19: {(steps[19] - o1) * PAGE:.1f}")
for s in ("base", "step_19", "step_20"):
    ref = tec_len if s == "base" else steps[int(s[-2:])]
    print(f"{s}: placeholders filled {(sim['fill_' + s] - ref) * PAGE:+.1f} lines;"
          f" filled and s.d. added {(sim['fillsd_' + s] - ref) * PAGE:+.1f} lines")
print(f"Table 3 with s.d. suffixes is {over} pt wider than the column (overfull)")

# the same moves applied to the repository HEAD version (979e42d, generated table bodies)
head = {int(m.group(1)): float(m.group(2)) for m in
        re.finditer(r"^\s*(\d+) \w+\s+rc=0 .*? effective=([\d.]+)", open("trial_head_run.txt").read(), re.M)}
simh = {m.group(1): (int(m.group(2)), float(m.group(3))) for m in
        re.finditer(r"sim\W(\w+): replaced (\d+) tbd; .*? effective=([\d.]+)", open("sim_head.txt").read())}
print(f"HEAD: base tectonic {head[0]:.3f}; moves 1-19 {head[19]:.3f}; moves 1-20 {head[20]:.3f};"
      f" saved by moves 1-20 {(head[0] - head[20]) * PAGE:.1f} lines")
for name, t in (("HEAD moves 1-19", head[19]), ("HEAD moves 1-20", head[20])):
    lo, hi = t - base_off, t - ret_off
    print(f"{name}: predicted pdflatex {lo:.3f} to {hi:.3f}; slack at the long end {(8 - hi) * PAGE:+.1f} lines,"
          f" at the short end {(8 - lo) * PAGE:+.1f} lines")
n, v = simh["fill_head20"]
print(f"HEAD moves 1-20: {n} placeholders filled {(v - head[20]) * PAGE:+.1f} lines;"
      f" filled and s.d. added {(simh['fillsd_head20'][1] - head[20]) * PAGE:+.1f} lines")
