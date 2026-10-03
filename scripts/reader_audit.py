"""Audit of two-stage reader outputs (owner C): does a ledger or summary carry a decision?
  python scripts/reader_audit.py RUN_DIR [--set NAME ...] [--data DIR] [--data-c DIR]
Per set, over reader units (one output per case and condition): the strict malformed rate (read from
the run's summary) and the share of outputs with decision language, by pattern class. The condition
under test is removed from the text first (every occurrence), and so are ledger 'need:' lines: they
restate the rule by design and are not a decision. Records are read from DIR (A's layout:
REGISTRY.json, rule_v1 sets) or DIR_C (C's sets, registry clin_v1/REGISTRY_C.json).
Decision language (heuristic, case-insensitive):
  verdict   'the claim is/was (in)correct|true|false', 'answer:', a final line that is only + or -
  criterion '(criterion|condition) is/was (not) met|satisfied|fulfilled', 'meets / does not meet',
            '(not) eligible', 'applies' / 'does not apply', 'satisfies', 'contradicts',
            'falls within / outside (the range)', 'fulfil'
  action    'therefore', 'thus', 'hence', 'should (not)', 'recommend', 'is indicated', 'contraindicated'
  compare   a value compared with a threshold: 'above|below|greater than|less than|exceeds|higher than|
            lower than|at or above|at or below' followed by a number
Writes RUN_DIR/reader_audit.json (all sets) and prints a line per set."""
import argparse, collections, glob, json, os, re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


def strip_condition(text, condition):
    text = "\n".join(l for l in (text or "").split("\n") if not re.match(r"^\W*need\W*:", l.strip(), re.I))
    return text.replace(condition, " ") if condition else text


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def conditions(name, data, data_c):
    """{tid/case_kind: condition} of a set, or None if its records are not available locally."""
    for reg_path, root in ((f"{data}/REGISTRY.json", data), (f"{data_c}/clin_v1/REGISTRY_C.json", data_c)):
        if os.path.exists(reg_path):
            entry = json.load(open(reg_path, encoding="utf-8")).get(name)
            if entry and os.path.exists(f"{root}/{entry['path']}"):
                return {"/".join(r["iid"].split("/")[:2]): r["condition"] for r in load_jsonl(f"{root}/{entry['path']}")}
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run_dir")
    ap.add_argument("--set", action="append")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--data-c", default=f"{REPO}/data")
    a = ap.parse_args()
    out = {}
    for f in sorted(glob.glob(f"{a.run_dir}/scores_*.jsonl")):
        name = os.path.basename(f)[7:-6].replace("~", "/")
        if a.set and name not in a.set:
            continue
        rows = load_jsonl(f)
        if not rows or "reader_output" not in rows[0]:
            continue
        cond = conditions(name, a.data, a.data_c) or {}
        units = {}
        for r in rows:
            units.setdefault("/".join(r["iid"].split("/")[:2]), r["reader_output"])
        c = collections.Counter()
        for k, text in units.items():
            ks = classes(strip_condition(text, cond.get(k, "")))
            c["any"] += bool(ks)
            for kk in ks:
                c[kk] += 1
        n = len(units)
        sp = f"{a.run_dir}/summary_{name.replace('/', '~')}.json"
        ev = (json.load(open(sp, encoding="utf-8")).get("eval") or {}) if os.path.exists(sp) else {}
        out[name] = {"units": n, "condition_removed": bool(cond), "decision_language_any": round(100.0 * c["any"] / n, 2),
                     **{f"decision_language_{k}": round(100.0 * c[k] / n, 2) for k in PATTERNS},
                     "malformed_rate_strict": ev.get("malformed_rate"),
                     "mean_chars": round(sum(len(t or "") for t in units.values()) / n, 1)}
        print(name, out[name])
    json.dump({"patterns": PATTERNS, "sets": out}, open(f"{a.run_dir}/reader_audit.json", "w", encoding="utf-8",
                                                          newline="\n"), indent=1)


if __name__ == "__main__":
    main()
