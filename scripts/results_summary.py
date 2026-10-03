"""docs/RESULTS_SUMMARY.md (D-SUM): every claim of the abstract and the contribution list
with its estimate, interval, test, status and the sentence the paper may state, computed
through the same keys as the tables (scripts/make_tables.py). Re-run after every new result.

  python scripts/results_summary.py

Status rules (App. A of the paper, fixed before the results): a primary comparison is
'supported' when the paired difference has the predicted sign and its Holm-adjusted p is
below 0.05; 'not supported' otherwise; 'pending' while any p of the Holm family is missing
(the unadjusted p is shown); 'not run' while the comparison has no estimate.
"""
import importlib.util
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("make_tables", os.path.join(ROOT, "scripts", "make_tables.py"))
MT = importlib.util.module_from_spec(spec)
spec.loader.exec_module(MT)

# (id, claim as the paper states it, comparison or None, predicted sign, keys to show, decision rule if it fails)
CLAIMS = [
    ("A1", "Across the audited reward signals, few triplets are solved: trained medical PRMs seldom reverse and "
           "general judges reverse on near-misses (abstract; contribution 1).", None, None,
     ["min/" + "|".join(f"run/{p}/L2/all/TA" for g in MT.AUDIT for p, _ in g[1]),
      "max/" + "|".join(f"run/{p}/L2/all/TA" for g in MT.AUDIT for p, _ in g[1])],
     "Report the audit as found (CLAUDE.md pilot rule)."),
    ("P1", "Balanced outcomes teach reversal: balanced above natural, verdict only, L2 TA (App. A (1)).", "p1", +1,
     ["run/B-F-verdict-balanced/L2/all/TA", "run/B-F-verdict-natural/L2/all/TA",
      "run/B-F-verdict-balanced/L2/all/Rev", "run/B-F-verdict-natural/L2/all/Rev"],
     "Report that balance does not teach reversal in this setup."),
    ("P2", "Flip pairs alone leave over-triggering unresolved and near-misses in the same budget remove most of it: "
           "triplets above blocks, verdict only, L2 TA (abstract; contribution 2; App. A (2)).", "p2", +1,
     ["run/B-F-verdict-triplets/L2/all/TA", "run/B-F-verdict-blocks/L2/all/TA",
      "run/B-F-verdict-triplets/L2/all/Hold", "run/B-F-verdict-blocks/L2/all/Hold"],
     "If (2) fails, near-misses are reported as an evaluation device only."),
    ("P3", "The typed applicability ledger is above the matched prose summary under the same case-blind judge, "
           "trained on triplets, L2 TA (abstract; contribution 2; App. A (3)).", "p3", +1,
     ["run/B-F-ledger2-triplets/L2/all/TA", "run/B-F-summary2-triplets/L2/all/TA"],
     "If (3) fails, the paper is a data-design result and the typed ledger is reported as equal to prose."),
    ("P4", "Trained on rules alone, Ledger-RM raises agreement with MedEinst pair labels over the untrained critic, "
           "zero-shot (abstract; contribution 3; App. A (4)).", "p4", +1,
     ["run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal", "run/C-TF-critic/clin_v1:medeinst_test/top/Reversal"],
     "If (4) and (6) fail, the answer outside rules is negative and the medical claim is withdrawn; if the gain "
     "appears only with step-error data, it is a gain from medical supervision."),
    ("P5", "Rule-only Ledger-RM above the rule-only evidence summary on MedEinst (App. A (5)).", "p5", +1,
     ["run/B-F-ledger2-triplets/clin_v1:medeinst_test/top/Reversal",
      "run/B-F-summary2-triplets/clin_v1:medeinst_test/top/Reversal"], "Report as found."),
    ("P6a", "Trained on rules alone, Ledger-RM raises macro-F1 against physician eligibility judgments over the "
            "untrained backbone (abstract; contribution 3; App. A (6)).", "p6a", +1,
     ["run/C-TG-ledger2-triplets/clin_v1:trialgpt_test/top/macroF1",
      "run/C-TG-critic/clin_v1:trialgpt_test/top/macroF1"],
     "If (4) and (6) fail, the medical claim is withdrawn."),
    ("P6b", "Triplets above blocks for Ledger-RM on the TrialGPT annotations (App. A (6)).", "p6b", +1,
     ["run/C-TG-ledger2-triplets/clin_v1:trialgpt_test/top/macroF1",
      "run/C-TG-ledger2-blocks/clin_v1:trialgpt_test/top/macroF1"], "Report as found."),
    ("C2b", "A separately written record is what helps: the same ledger written in one pass with the verdict "
            "(rationale) gives no gain over verdict only, triplets, L2 TA (contribution 2; descriptive).", None, None,
     ["run/B-F-rationale-triplets/L2/all/TA", "run/B-F-verdict-triplets/L2/all/TA",
      "d/run/B-F-rationale-triplets/L2/all/TA|run/B-F-verdict-triplets/L2/all/TA"],
     "Descriptive; not a primary comparison."),
    ("C3", "A model trained on rule triplets only reaches the reported accuracy on rules of held-out structure "
           "(contribution 3).", None, None,
     ["run/B-F-ledger2-triplets/L2/all/TA", "run/B-F-ledger2-triplets/L2/all/TA/lo", "run/B-F-ledger2-triplets/L2/all/TA/hi",
      "run/B-F-ledger2-triplets/L2/all/TA/n"], "Descriptive."),
    ("T5", "As a process reward, the combined reward is non-inferior to the step check on MedQA (1-point margin) and "
           "better on key pairs and MedEinst pairs; swapping the vignette removes the gain (Sec. 7.5).", None, None,
     ["run/D-SEL-combined/sel:medqa/top/acc", "run/D-SEL-stepcheck/sel:medqa/top/acc",
      "run/D-SEL-combined-swap/sel:medqa/top/acc", "run/D-SEL-combined/sel:keypairs/top/pair_acc",
      "run/D-SEL-stepcheck/sel:keypairs/top/pair_acc"],
     "If the gains are within the non-inferiority margin, say so; no aggregation rule is searched on test data "
     "(ROLE.md)."),
]


def status(cmp_name, sign):
    c = MT.comparisons().get(cmp_name) or {}
    if c.get("diff") is None:
        return "not run", c
    if c.get("padj") is None:
        return "pending (Holm family incomplete)", c
    ok = (c["diff"] > 0) == (sign > 0) and c["padj"] < 0.05
    return ("supported" if ok else "not supported"), c


def main():
    head = subprocess.run(["git", "-C", ROOT, "rev-parse", "--short=12", "HEAD"], capture_output=True, text=True).stdout.strip()
    out = ["# Results summary (D-SUM)", "",
           f"Generated by `python scripts/results_summary.py` at commit {head} from the result files, through the keys",
           "of `scripts/make_tables.py`. Every value is provisional until its runs are complete; the number of seeds",
           "behind a value is shown where it applies. Status rules: docstring of the script (App. A of the paper).", "",
           "| id | claim | estimate | test | status |", "|---|---|---|---|---|"]
    detail = []
    for cid, claim, cmp_name, sign, keys, rule in CLAIMS:
        vals = "; ".join(f"`{k if len(k) < 70 else k[:67] + '...'}` = {MT.resolve(k)[1]}" for k in keys)
        if cmp_name:
            st, c = status(cmp_name, sign)
            test = (f"{c.get('diff', 0):+.1f} [{c.get('lo', 0):+.1f}, {c.get('hi', 0):+.1f}], p {MT.resolve(f'cmp/{cmp_name}/p')[1]}, "
                    f"Holm {MT.resolve(f'cmp/{cmp_name}/padj')[1]}, n {c.get('n')}, seeds {','.join(c.get('seeds', [])) or '-'}"
                    if c.get("diff") is not None else "-")
        else:
            st = "descriptive" if any(MT.resolve(k)[0] is not None for k in keys) else "not run"
            test = "-"
        out.append(f"| {cid} | {claim} | see below | {test} | {st} |")
        detail += ["", f"## {cid}", "", claim, "", f"- values: {vals}", f"- if it fails: {rule}"]
    text = "\n".join(out + detail).replace(r"\ph{tbd}", "tbd").replace("$<$", "<") + "\n"
    open(os.path.join(ROOT, "docs", "RESULTS_SUMMARY.md"), "w", encoding="utf-8", newline="\n").write(text)
    print(text[:3000])


if __name__ == "__main__":
    if os.environ.get("PYTHONHASHSEED") != "0":
        sys.exit(subprocess.run([sys.executable, *sys.argv], env=os.environ | {"PYTHONHASHSEED": "0"}).returncode)
    main()
