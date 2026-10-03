"""Final audit (FINAL_TASKS_D P1, Sat 10 Oct; also run at every merge) -> docs/FINAL_AUDIT.md.

  python scripts/final_audit.py [--tests]

Run after scripts/make_tables.py and scripts/update_paper.py. Each check is 'pass' or 'open' with the items
behind it:
 1. rule_v1 frozen: every set registered at the freeze (git e40789b) has the same sha256 now.
 2. Registries: every entry of data/REGISTRY.json and data/clin_v1/REGISTRY_C.json is frozen.
 3. Scored sets: every results*/<run>/summary_<set>.json names a frozen set ('~<variant>' parts such as edit,
    swap, nocase, lenient score a frozen set); sel/<pool> are D's candidate pools (sources pinned in
    configs/datasets_d.json).
 4. Provenance: every measured table cell and paper number (tables/PROVENANCE.json) comes from files that git
    tracks and that are unchanged in the working tree; record files match their sha256.
 5. Per-example scores: next to every summary_<set>.json behind a measured number, scores_<set>.jsonl is
    tracked by git; runs of two-stage formats keep the reader output in each line.
 6. Key cells {verdict, ledger2} x {blocks, triplets}: at least 3 seeds DONE (never dropped, project spec).
 7. Primary comparisons: all p-values present, so the Holm correction is computed.
 8. Paper: placeholders left in the paper (paper/latex_v14/main.tex) (the build fails while any remain).
 9. Tooling markers in tracked files and co-author trailers in commit messages since the freeze.
10. (--tests) the test suite.
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FREEZE = "e40789b"
KEY_CELLS = [f"B-F-{f}-{d}" for f in ("verdict", "ledger2") for d in ("blocks", "triplets")]
TWO_STAGE = ("ledger2", "summary2", "value2", "conddrv", "promptledger", "promptsum")
# analyses computed from the per-example scores of their source runs (named in the summary), not scoring runs
DERIVED = ("C-DG-",)


def git(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True, encoding="utf-8").stdout


def registry():
    reg = json.load(open(os.path.join(ROOT, "data", "REGISTRY.json"), encoding="utf-8"))
    regc = json.load(open(os.path.join(ROOT, "data", "clin_v1", "REGISTRY_C.json"), encoding="utf-8"))
    return reg, regc


def summary_set(path):
    """results*/<run>/summary_<set>.json -> set name ('~' or '__' for '/'), None for summary.json."""
    m = re.match(r"summary_(.+)\.json$", os.path.basename(path))
    return m.group(1).replace("~", "/").replace("__", "/") if m else None


def checks(run_tests):
    out = []
    reg, regc = registry()
    old = json.loads(git("show", f"{FREEZE}:data/REGISTRY.json") or "{}")
    changed = [k for k, v in old.items() if (reg.get(k) or {}).get("sha256") != v.get("sha256")]
    out.append(("rule_v1 sets frozen at e40789b unchanged", not changed,
                f"{len(old)} sets at the freeze, {len(reg)} now", changed))

    unfrozen = [k for r in (reg, regc) for k, v in r.items() if not v.get("frozen")]
    out.append(("Every registry entry frozen", not unfrozen, f"{len(reg)} + {len(regc)} entries", unfrozen))

    frozen = {k for r in (reg, regc) for k, v in r.items() if v.get("frozen")}
    bad, n = [], 0
    for p in sorted(glob.glob(os.path.join(ROOT, "results*", "*", "summary_*.json"))):
        s = summary_set(p)
        if not s:
            continue
        n += 1
        if not (s.startswith(("sel/", "smoke_v2/")) or any(f"/{f}/" in f"/{s}/" for f in frozen)):
            bad.append(f"{os.path.relpath(p, ROOT)} ({s})")
    out.append(("Scored sets are frozen", not bad, f"{n} summary files", bad))

    prov = json.load(open(os.path.join(ROOT, "tables", "PROVENANCE.json"), encoding="utf-8"))
    tracked = set(git("ls-files").splitlines())
    dirty = {ln[3:].strip().strip('"') for ln in git("status", "--porcelain").splitlines()}
    files, measured = set(), 0
    for k, v in prov["keys"].items():
        if v.get("number") is None:
            continue
        measured += 1
        files |= {r["file"].replace("\\", "/") for r in v.get("runs", []) if r.get("file")}
    files |= {c["file"] for c in prov.get("comparisons", {}).values() if isinstance(c, dict) and c.get("file")}
    issues = [f"{f}: not tracked by git" for f in sorted(files) if f not in tracked]
    issues += [f"{f}: smoke data in a table" for f in sorted(files) if (summary_set(f) or "").startswith("smoke")]
    issues += [f"{f}: changed in the working tree" for f in sorted(files) if f in dirty]
    for name, r in prov.get("records", {}).items():
        p = os.path.join(ROOT, r["file"])
        if not os.path.exists(p) or hashlib.sha256(open(p, "rb").read()).hexdigest() != r["sha256"]:
            issues.append(f"{r['file']}: missing or sha256 differs from the registry")
    out.append(("Measured numbers come from tracked, unchanged files", not issues,
                f"{measured} measured keys, {len(files)} files, {len(prov.get('records', {}))} record files",
                issues + [f"make_tables warning: {w}" for w in prov.get("warnings", [])]))

    missing, n = [], 0
    for f in sorted(files):
        s = summary_set(f)
        if not s or f.split("/")[1].startswith(DERIVED):
            continue
        n += 1
        sc = f.replace("/summary_", "/scores_")[:-len(".json")] + ".jsonl"
        if sc not in tracked:
            missing.append(f"{sc}: {'local only' if os.path.exists(os.path.join(ROOT, sc)) else 'missing'}")
        elif any(t in f.split("/")[1] for t in TWO_STAGE):
            with open(os.path.join(ROOT, sc), encoding="utf-8") as fh:
                line = fh.readline()
            if line and "reader_output" not in json.loads(line):
                missing.append(f"{sc}: no reader output")
    out.append(("Per-example scores (and reader outputs) kept for every tabled summary", not missing,
                f"{n} summaries behind measured numbers", missing))

    seeds = {c: sorted(int(d.rsplit("-s", 1)[1]) for d in map(os.path.basename,
                       glob.glob(os.path.join(ROOT, "results_git", f"{c}-s[0-9]")))
                       if os.path.exists(os.path.join(ROOT, "results_git", d, "DONE"))) for c in KEY_CELLS}
    out.append(("Key cells have at least 3 seeds", all(len(v) >= 3 for v in seeds.values()),
                "; ".join(f"{c}: seeds {v}" for c, v in seeds.items()), [c for c, v in seeds.items() if len(v) < 3]))

    cmp = {k: v for k, v in prov.get("comparisons", {}).items() if re.fullmatch(r"p\d+[ab]?", k)}
    nop = [k for k, v in cmp.items() if v.get("p") is None]
    out.append(("Primary comparisons complete (Holm)", bool(cmp) and not nop, f"{len(cmp)} comparisons", nop))

    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import update_paper as U
    numbers = json.load(open(os.path.join(ROOT, "tables", "numbers.json"), encoding="utf-8"))
    n_ph, unresolved, keys = U.placeholders(open(os.path.join(U.PAPER, "main.tex"), encoding="utf-8").read(), numbers)
    out.append(("Paper without placeholders", n_ph == 0 and not unresolved,
                f"{n_ph} placeholders, {len(unresolved)} of {len(keys)} keys without a value", unresolved[:40]))

    # locations only, never the matched text; the requests and reports that name the markers are left out
    own = ("scripts/final_audit.py", "docs/FINAL_AUDIT.md", "docs/CHANGE_REQUESTS.md", "docs/STATUS_BOARD.md")
    marks = [":".join(ln.split(":")[:2]) for ln in git("grep", "-n", "-I", "-E",
                                                       r"ponytail:|maintained by [A-Z][a-z]+ [A-Z]").splitlines()
             if not ln.startswith(own)]
    trailers = [f"commit {ln.split()[0]}: co-author trailer" for ln in git(
        "log", "--format=%h %(trailers:key=Co-authored-by,valueonly)", f"{FREEZE}..HEAD").splitlines()
        if len(ln.split()) > 1]
    out.append(("No tooling markers or co-author trailers", not marks and not trailers,
                f"{len(marks)} marker lines, {len(trailers)} commits with trailers", marks + trailers))

    if run_tests:
        r = subprocess.run([sys.executable, "-m", "pytest", "-q", os.path.join(ROOT, "tests")], cwd=ROOT,
                           capture_output=True, text=True)
        last = (r.stdout.strip().splitlines() or ["no output"])[-1]
        out.append(("Test suite passes", r.returncode == 0, last, [] if r.returncode == 0 else [last]))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tests", action="store_true")
    a = ap.parse_args()
    res = checks(a.tests)
    head = git("rev-parse", "--short=12", "HEAD").strip()
    lines = ["# Final audit (generated by scripts/final_audit.py; do not edit)", "",
             f"Commit {head}{' (uncommitted changes)' if git('status', '--porcelain').strip() else ''}. "
             f"{sum(ok for _, ok, _, _ in res)} of {len(res)} checks pass.", "",
             "| # | Check | Result | Scope |", "|---|---|---|---|"]
    for i, (name, ok, scope, _) in enumerate(res, 1):
        lines.append(f"| {i} | {name} | {'pass' if ok else 'open'} | {scope} |")
    for i, (name, ok, _, items) in enumerate(res, 1):
        if items:
            lines += ["", f"## {i}. {name}: {len(items)} item(s)", ""] + [f"- {x}" for x in items[:200]]
            if len(items) > 200:
                lines.append(f"- ... and {len(items) - 200} more")
    open(os.path.join(ROOT, "docs", "FINAL_AUDIT.md"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    for i, (name, ok, scope, items) in enumerate(res, 1):
        print(f"{i:2d} {'pass' if ok else 'OPEN'}  {name}: {scope}" + (f" ({len(items)} items)" if items else ""))


if __name__ == "__main__":
    main()
