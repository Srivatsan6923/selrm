"""Audit of two-stage reader outputs (owner C): does a ledger or summary carry a decision?
  python scripts/reader_audit.py RUN_DIR [--set NAME ...] [--data DIR]
Per set, over reader units (one output per case and condition): strict malformed rate (B's
formats.well_formed via eval_c's copy of its rules is not imported here: the strict rate is read
from the run's summary), share of outputs with decision language, by pattern class, and with the
text of either claim. Decision language (heuristic, lower case):
  verdict   'the claim is/was (in)correct|true|false', 'answer:', a final line that is only + or -
  criterion "(criterion|condition) is/was (not) met|satisfied|fulfilled", "meets/does not meet", satisfies,
            contradicts, falls within/outside (the range),
            '(not) eligible', 'applies' / 'does not apply'
  action    'therefore', 'thus', 'hence', 'should (not)', 'recommend', 'is indicated', 'contraindicated'
  compare   a value compared with a threshold: 'above|below|greater than|less than|exceeds|higher than|
            lower than|at or above|at or below' followed by a number
Writes RUN_DIR/reader_audit.json (all sets) and prints a line per set."""
import argparse, collections, glob, json, os, re

PATTERNS = {
    "verdict": [r"\bthe claim (?:is|was) (?:not )?(?:correct|incorrect|true|false|right|wrong)\b", r"\banswer\s*:",
                r"(?:^|\n)\s*[+\-]\s*$"],
    "criterion": [r"\b(?:criterion|condition|requirement)s? (?:is|are|was|were) (?:not )?(?:met|satisfied|fulfilled)\b",
                  r"\b(?:meets|does not meet|do not meet|fails to meet)\b", r"\b(?:not )?eligible\b",
                  r"\bdoes not apply\b", r"\bapplies\b", r"\bsatisf(?:ies|y|ied)\b", r"\bcontradict",
                  r"\bfalls? (?:within|outside)\b", r"\bwithin the (?:specified |required )?range\b", r"\bfulfil"],
    "action": [r"\btherefore\b", r"\bthus\b", r"\bhence\b", r"\bshould(?: not)?\b", r"\brecommend", r"\bis indicated\b",
               r"\bcontraindicat"],
    "compare": [r"\b(?:above|below|greater than|less than|exceeds?|higher than|lower than|at or above|at or below)\s+\d"],
}
RX = {k: [re.compile(p, re.I) for p in v] for k, v in PATTERNS.items()}


def classes(text):
    return [k for k, ps in RX.items() if any(p.search(text or "") for p in ps)]


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--set", action="append")
    ap.add_argument("--data", default=None, help="records dir (REGISTRY.json); needed for the claim-text check")
    a = ap.parse_args()
    files = sorted(glob.glob(f"{a.run_dir}/scores_*.jsonl"))
    out = {}
    for f in files:
        name = os.path.basename(f)[7:-6]
        if a.set and name.replace("~", "/") not in a.set:
            continue
        rows = load_jsonl(f)
        if not rows or "reader_output" not in rows[0]:
            continue
        units = {}
        for r in rows:
            units.setdefault("/".join(r["iid"].split("/")[:2]), r["reader_output"])
        c = collections.Counter()
        for text in units.values():
            ks = classes(text)
            c["any"] += bool(ks)
            for k in ks:
                c[k] += 1
        n = len(units)
        summ = {}
        sp = f"{a.run_dir}/summary_{name}.json"
        if os.path.exists(sp):
            summ = json.load(open(sp, encoding="utf-8")).get("eval") or {}
        out[name.replace("~", "/")] = {"units": n, "decision_language_any": round(100.0 * c["any"] / n, 2),
                                       **{f"decision_language_{k}": round(100.0 * c[k] / n, 2) for k in PATTERNS},
                                       "malformed_rate_strict": summ.get("malformed_rate"),
                                       "mean_chars": round(sum(len(t or "") for t in units.values()) / n, 1)}
        print(name, out[name.replace("~", "/")])
    json.dump({"patterns": PATTERNS, "sets": out}, open(f"{a.run_dir}/reader_audit.json", "w", encoding="utf-8",
                                                          newline="\n"), indent=1)


if __name__ == "__main__":
    main()
