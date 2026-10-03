"""Collect the project's live state into docs/assets/data.js for the status site.

  python scripts/build_site.py

Reads only files already in the repo: run matrices, results/ and results_git/
run directories (DONE / CLAIMED_* / meta.json / summary_*.json), the data
registry, the status board, role STATE / DECISIONS files, handoffs and git log.
No number is typed here; every metric shown on the site comes from a summary file.
The output is a plain JS file (window.SELRM = {...}) so the pages open from disk.
"""
import ast
import csv
import datetime as dt
import glob
import json
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "docs", "assets", "data.js")
ROLES = "ABCD"
RESULT_TOPS = ("results", "results_git")

# Dates from CLAUDE.md / docs/TEAM_PLAN.md
MILESTONES = [
    ("2026-10-02T00:00:00Z", "Kick-off", "Foundation, engine, smoke data"),
    ("2026-10-03T23:59:00Z", "rule_v1 freeze", "Rule library and test sets frozen"),
    ("2026-10-04T12:00:00Z", "Pilot + GO rule", "300 triplets x 5 models"),
    ("2026-10-07T23:59:00Z", "Run freeze", "Last training/eval run starts"),
    ("2026-10-10T23:59:00Z", "Final audit", "Tables, provenance, human read"),
    ("2026-10-11T23:59:00Z", "Manuscript frozen", "Submit via ARR"),
    ("2026-10-12T23:59:00Z", "ARR deadline", "NAACL/COLING 2027"),
]


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_json(path):
    try:
        return json.loads(read(path))
    except (OSError, ValueError):
        return None


def git(*args):
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8").strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


# ---------------------------------------------------------------- runs

def matrix_rows():
    """Role matrices are authoritative for their rows; the master fills the rest."""
    rows = {}
    master = os.path.join(ROOT, "docs", "RUN_MATRIX.csv")
    for r in csv.DictReader(open(master, encoding="utf-8")):
        rows[r["run_id"]] = r
    for role in ROLES:
        p = os.path.join(ROOT, "docs", f"RUN_MATRIX_{role}.csv")
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding="utf-8")):
                rows[r["run_id"]] = r
    return rows


def run_dirs():
    found = {}
    for top in RESULT_TOPS:
        for d in sorted(glob.glob(os.path.join(ROOT, top, "*"))):
            if os.path.isdir(d):
                found.setdefault(os.path.basename(d), []).append(d)
    return found


def compact_summary(s):
    """Keep the headline block, CIs, near-miss kinds and missing-twin numbers."""
    if not isinstance(s, dict):
        return None
    out = {}
    if isinstance(s.get("all"), dict):
        out["all"] = {k: s["all"].get(k) for k in ("TA", "Rev", "Hold", "PresHold", "BaseAcc", "Tie", "n")}
    if isinstance(s.get("CI95"), dict):
        out["ci"] = s["CI95"]
    kinds = {k.split("=", 1)[1]: v.get("TA") for k, v in s.items()
             if k.startswith("nm_kind=") and isinstance(v, dict)}
    if kinds:
        out["kinds"] = kinds
    for k in ("MR", "FR", "threshold"):
        if isinstance(s.get(k), (int, float)):
            out[k] = s[k]
    return out or None


def set_name(fname):
    base = os.path.basename(fname)[len("summary_"):-len(".json")]
    return base.replace("~", "/").replace("__", "/")


def collect_run(run_id, dirs):
    info = {"dirs": [os.path.relpath(d, ROOT).replace("\\", "/") for d in dirs],
            "done": False, "claims": [], "summaries": {}}
    for d in dirs:
        if os.path.exists(os.path.join(d, "DONE")):
            info["done"] = True
        for c in glob.glob(os.path.join(d, "CLAIMED_*")):
            note = read(c).strip().splitlines()
            info["claims"].append({"role": os.path.basename(c)[len("CLAIMED_"):],
                                   "note": note[0][:160] if note else ""})
        if os.path.exists(os.path.join(d, "HEARTBEAT")):
            info["heartbeat"] = dt.datetime.utcfromtimestamp(
                os.path.getmtime(os.path.join(d, "HEARTBEAT"))).isoformat() + "Z"
        meta = load_json(os.path.join(d, "meta.json")) or {}
        for k in ("model", "format", "corpus", "seed", "provisional", "timing_only", "gpu",
                  "gpu_hours", "wall_seconds", "access_date", "date", "git_commit"):
            if k in meta and k not in info:
                v = meta[k]
                info[k] = v.split(",")[0] if k == "gpu" and isinstance(v, str) else v
        for f in glob.glob(os.path.join(d, "summary_*.json")):
            cs = compact_summary(load_json(f))
            if cs:
                info["summaries"][set_name(f)] = cs
    return info


def build_runs():
    rows, dirs = matrix_rows(), run_dirs()
    runs = []
    for rid in sorted(set(rows) | set(dirs)):
        r = rows.get(rid, {})
        res = collect_run(rid, dirs.get(rid, []))
        planned = (r.get("status") or "").strip() or "todo"
        if res["done"]:
            state = "done"
        elif res["claims"]:
            state = "claimed"
        elif rid in rows:
            state = planned
        else:
            state = "untracked"
        owner = r.get("owner") or rid.split("-", 1)[0]
        smoke = bool(re.search(r"-(C0|T0b?)-", rid)) or "smoke" in rid
        runs.append({
            "id": rid, "owner": owner, "state": state, "in_matrix": rid in rows,
            "pool": r.get("pool", ""), "item": r.get("paper_item", ""), "kind": r.get("kind", ""),
            "what": r.get("what", ""), "data": r.get("data", ""), "seed": r.get("seed", ""),
            "runtime": r.get("runtime", ""), "est_hours": r.get("est_hours", ""),
            "priority": r.get("priority", ""), "depends": r.get("depends_on", ""),
            "notes": r.get("notes", ""), "smoke": smoke, **res,
        })
    return runs


# ---------------------------------------------------------------- data + docs

def build_registry():
    reg = load_json(os.path.join(ROOT, "data", "REGISTRY.json")) or {}
    return [{"name": k, "split": v.get("split"), "level": v.get("level"), "tier": v.get("tier"),
             "groups": v.get("n_groups"), "records": v.get("n_records"),
             "frozen": v.get("frozen"), "created": v.get("created")}
            for k, v in sorted(reg.items())]


def build_library():
    s = load_json(os.path.join(ROOT, "results", "A-D15", "summary.json")) or {}
    return {k: s.get(k) for k in ("rules_total", "rules_by_source", "rules_by_kind",
                                  "invented_rules_L3inv")} | {"classes": len(s.get("classes") or {})}


def md_table(text, header_start):
    """Rows of the first markdown table whose header line starts with header_start."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith(header_start):
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            out = []
            for row in lines[i + 2:]:
                if not row.strip().startswith("|") and "|" not in row:
                    break
                cells = [c.strip() for c in row.strip().strip("|").split("|")]
                if len(cells) >= len(head):
                    out.append(dict(zip(head, cells[:len(head) - 1] + [" | ".join(cells[len(head) - 1:])])))
            return out
    return []


def task_status(s):
    s = s.lower()
    for key in ("blocked", "running", "done", "partly", "waiting", "queued", "open", "dropped"):
        if s.startswith(key) or (key == "partly" and "partly" in s):
            return key
    return "not started" if "not started" in s else "other"


def build_tasks():
    board = read(os.path.join(ROOT, "docs", "STATUS_BOARD.md"))
    tasks = [{"id": t["ID"], "task": t["Task"], "owner": t["Owner"], "status": t["Status"],
              "kind": task_status(t["Status"]), "output": t["Output"]}
             for t in md_table(board, "| ID |")]
    checks = [{"check": c["Check"], "result": c["Result"]} for c in md_table(board, "| Check |")]
    return tasks, checks


def section_bullets(text, title):
    m = re.search(r"^##\s+" + re.escape(title) + r".*?$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    if not m:
        return []
    items = [re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", l).strip() for l in m.group(1).splitlines()
             if re.match(r"^(?:[-*]|\d+\.)\s+", l)]
    return [re.sub(r"\*\*|`", "", i)[:220] for i in items]


def build_roles():
    names = {"A": "Data & rules", "B": "Training", "C": "Evaluation", "D": "Downstream & lead"}
    roles = []
    for r in ROLES:
        state_p = os.path.join(ROOT, "docs", f"STATE_{r}.md")
        st = read(state_p) if os.path.exists(state_p) else ""
        upd = re.search(r"^Updated:\s*(.+)$", st, re.M)
        dec_p = os.path.join(ROOT, "docs", f"DECISIONS_{r}.md")
        decisions = []
        if os.path.exists(dec_p):
            for line in read(dec_p).splitlines():
                if re.match(r"^\d{4}-\d{2}-\d{2}\s*\|", line):
                    parts = [p.strip() for p in line.split("|")]
                    decisions.append({"date": parts[0], "text": re.sub(r"`", "", parts[1])[:200]})
        roles.append({
            "id": r, "name": names[r], "updated": upd.group(1).strip() if upd else "",
            "paused": "PAUSED" in st or "Paused" in st,
            "done": section_bullets(st, "Done")[:6],
            "next": section_bullets(st, "Next")[:5],
            "blockers": [b for b in section_bullets(st, "Blockers") if b.lower() not in ("none", "none.")],
            "requests": [b for b in section_bullets(st, "Open compute requests")
                         if not b.lower().startswith("none")],
            "decisions": decisions[-6:][::-1], "n_decisions": len(decisions),
        })
    return roles


def build_handoffs():
    p = os.path.join(ROOT, "docs", "HANDOFFS.md")
    out = []
    for line in read(p).splitlines():
        if re.match(r"^\d{4}-\d{2}-\d{2}\s*\|", line):
            parts = [x.strip() for x in line.split("|")]
            if len(parts) >= 4:
                out.append({"date": parts[0], "from": parts[1], "to": parts[2],
                            "what": re.sub(r"`", "", parts[3])[:240]})
    return out[::-1][:14]


def build_modules():
    mods = []
    for folder in ("selrm", "scripts"):
        for f in sorted(glob.glob(os.path.join(ROOT, folder, "*.py"))):
            if os.path.basename(f) == "__init__.py":
                continue
            src = read(f)
            try:
                doc = ast.get_docstring(ast.parse(src)) or ""
            except SyntaxError:
                doc = ""
            first = next((l.strip() for l in doc.splitlines() if l.strip()), "")
            mods.append({"path": f"{folder}/{os.path.basename(f)}", "folder": folder,
                         "loc": src.count("\n"), "doc": first[:140]})
    return mods


def build_commits():
    log = git("log", "-12", "--date=short", "--pretty=format:%h|%ad|%an|%s")
    return [dict(zip(("hash", "date", "author", "msg"), l.split("|", 3))) for l in log.splitlines() if l]


def main():
    runs = build_runs()
    tasks, checks = build_tasks()
    data = {
        "generated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "commit": git("rev-parse", "--short", "HEAD"), "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
        "milestones": [{"at": a, "title": t, "note": n} for a, t, n in MILESTONES],
        "runs": runs, "registry": build_registry(), "library": build_library(),
        "tasks": tasks, "checks": checks, "roles": build_roles(), "handoffs": build_handoffs(),
        "modules": build_modules(), "commits": build_commits(),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("// Generated by scripts/build_site.py. Do not edit by hand.\n")
        f.write("window.SELRM = " + json.dumps(data, separators=(",", ":"), default=str) + ";\n")
    n = {s: sum(r["state"] == s for r in runs) for s in sorted({r["state"] for r in runs})}
    print(f"{len(runs)} runs {n}; {len(data['registry'])} sets; {len(tasks)} tasks -> "
          f"{os.path.relpath(OUT, ROOT)} ({os.path.getsize(OUT) // 1024} KB)")


if __name__ == "__main__":
    main()
