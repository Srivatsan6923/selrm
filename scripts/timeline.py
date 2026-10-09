"""Facts behind docs/TIMELINE.md, recomputed from git, the files on disk and the bundles.

    python scripts/timeline.py           # print every computed fact the timeline cites
    python scripts/timeline.py --check   # only check docs/TIMELINE.md: the date of every commit and
                                         # disk file the table cites first, and chronological order
                                         # (after a self-test of the number search)
    python scripts/timeline.py --disk    # also search the working trees (slow) for the value of the
                                         # appendix placeholder, as git history and bundles are

Read-only: nothing is written into either repository. Code of old commits is unpacked into a
temporary directory with `git archive`, and the sets it rebuilds are written there. The old public
repository and the bundles are expected in D:/NAACL27 (the private repository is the parent of
this script's folder).
"""
import argparse
import bz2
import datetime
import filecmp
import glob
import gzip
import hashlib
import io
import json
import lzma
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import zipfile
from collections import Counter

import fitz  # PyMuPDF: text of PDF pages

NEW = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # github Srivatsan6923/selrm
OLD = "D:/NAACL27"                                                   # github Srivatsan6923/Symbolic_PRM_NAACL
REPOS = {"selrm": NEW, "Symbolic_PRM_NAACL": OLD}
PILOT, FIRST, FREEZE, FREEZE_CODE = "a6db79d", "c965184", "e40789b", "59034a3"
NOW = "129e5b4"  # role-d when the timeline was last read; its present-tense statements refer to this commit
CORPORA = ("balanced", "flips", "triplets", "no_pres", "conclusion_only")   # first build, data/train/


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, check=True).stdout


def gdate(repo, rev):
    return git(repo, "log", "-1", "--date=iso", "--format=%ad", rev).decode().strip()


def mtime(path):
    t = datetime.datetime.fromtimestamp(os.path.getmtime(path)).astimezone()
    return t.strftime("%Y-%m-%d %H:%M:%S %z")


def sha(data):  # LF-normalised, so a CRLF checkout and a git blob compare equal
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()[:16]


def archive(rev, tmp, repo=NEW):
    out = os.path.join(tmp, rev)
    tarfile.open(fileobj=io.BytesIO(git(repo, "archive", rev, "selrm", "scripts"))).extractall(out, filter="data")
    return out


def py(code, cwd, *args):
    """Run code with an old commit's `selrm` package first on the path."""
    sys.stdout.flush()
    subprocess.run([sys.executable, "-c", code, *args], cwd=cwd, check=True,
                   env=dict(os.environ, PYTHONPATH=cwd))


def commits():
    print("== Commits, oldest first (git log --all --date=iso)")
    for name, repo in REPOS.items():
        rows = git(repo, "log", "--all", "--date=iso", "--format=%h  %ad  %s").decode().splitlines()
        print(f"{name} ({repo}): {len(rows)} commits")
        for r in reversed(rows):
            print("   ", r[:160])
    print(f"selrm refs in {NEW} (author date of the commit each points to):")
    for r in git(NEW, "for-each-ref", "--format=%(refname:short) %(objectname:short) %(authordate:iso)",
                 "refs/heads", "refs/remotes").decode().splitlines():
        print("   ", r)
    print(f"Reflog of {OLD} (local; records the fetch, the branches and the push):")
    for r in git(OLD, "reflog", "--all", "--date=iso").decode().splitlines():
        print("   ", r)
    if os.path.isdir("D:/selrm/.git"):  # another clone of selrm; git log only
        other = git("D:/selrm", "rev-list", "--all").decode().split()
        mine = set(git(NEW, "rev-list", "--all").decode().split())
        print(f"D:/selrm: {len(other)} commits, {len(set(other) - mine)} of them not in {NEW}")


def bundles():
    print("\n== Bundles in D:/NAACL27 (zip entry times carry no timezone)")
    keys = ("rules.py", "mini_engine.py", "smoke.py", "MEASURED_FACTS.md", "ROLE.md", "FINAL_TASKS_D.md",
            "HUMAN_TASKS.md", "main.tex", "SYMRM_INTEGRATION.md", "README.md")
    for z in sorted(glob.glob(OLD + "/*.zip")):
        infos = zipfile.ZipFile(z).infolist()
        newest = max(datetime.datetime(*i.date_time) for i in infos)
        utc = datetime.datetime.fromtimestamp(os.path.getmtime(z), datetime.timezone.utc).replace(tzinfo=None)
        print(f"{os.path.basename(z)}: file modified {mtime(z)}, {len(infos)} entries, newest entry "
              f"{newest}; file time in UTC minus newest entry = {utc - newest}")
        for i in infos:
            if i.filename.endswith(keys):
                data = zipfile.ZipFile(z).read(i)
                print(f"    {datetime.datetime(*i.date_time)}  {i.file_size:7d}  sha {sha(data)}  {i.filename}")
    for rev, path in ((PILOT, "selrm/rules.py"), (PILOT, "selrm/mini_engine.py"), (PILOT, "selrm/smoke.py"),
                      (PILOT, "docs/MEASURED_FACTS.md")):
        print(f"    git selrm@{rev}:{path}  sha {sha(git(NEW, 'show', f'{rev}:{path}'))}")
    print(f"    git Symbolic_PRM_NAACL@{FIRST}:selrm/rules.py  sha {sha(git(OLD, 'show', f'{FIRST}:selrm/rules.py'))}")
    for path in ("selrm/engine.py", "selrm/rules.py", "tests/test_engine.py"):
        same = git(OLD, "rev-parse", f"{FIRST}:{path}") == git(NEW, "rev-parse", f"a725ffc:salvage/{path}")
        print(f"    Symbolic_PRM_NAACL@{FIRST}:{path} {'is' if same else 'is NOT'} the same blob as selrm@a725ffc:salvage/{path}")
    print("Root Markdown files of the project pack and of the D:/NAACL27 working tree:")
    z = zipfile.ZipFile(OLD + "/selrm_autonomous_pack.zip")
    for n in z.namelist():
        if n.count("/") == 1 and n.endswith(".md"):
            print(f"    pack {n}  sha {sha(z.read(n))}")
    for p in sorted(glob.glob(OLD + "/*.md")):
        print(f"    disk {os.path.basename(p)}  sha {sha(open(p, 'rb').read())}  modified {mtime(p)}")


def disk():
    print("\n== Files on disk that are not git history (modification times)")
    names = ["learning_when_to_change_naacl2027_draft_v10.pdf", "docs/STATE.md", "results/D0/validate_shortcuts.txt",
             "results/D3/make_train.txt", "rule_v1_rebuild/build_f1.log", "rule_v1_rebuild/build_f2.log",
             "rule_v1_rebuild/build_f3.log", "selrm-role-c/scratch/bres/vb.json"]
    for n in names:
        p = os.path.join(OLD, n)
        print(f"    {mtime(p) if os.path.exists(p) else 'missing':26s} {p}")
    tracked = set(git(OLD, "ls-files").decode().split())
    print("    old repository working tree, files not in git (git status --porcelain):")
    for r in git(OLD, "--no-optional-locks", "status", "--porcelain", "--untracked-files=all", "--", "docs",
                 "configs").decode().splitlines():
        p = r[3:]
        print(f"      {mtime(os.path.join(OLD, p))}  {r[:2]} {p}")
    print(f"    files of the pack that are tracked in {FIRST}: "
          f"{sorted(p for p in ('docs/REVIEW_HISTORY.md', 'docs/RUN_MATRIX.csv', 'docs/STATE.md') if p in tracked)}")


PILOT_FACTS = r'''
from selrm import rules, mini_engine as E, smoke as S
R = rules.RULES
print("rules:", len(R), [r.rid for r in R])
print("rules with a criterion that counts past findings:", [r.rid for r in R if any(c.counts_past for c in r.criteria)])
print("rules with a criterion that counts first-degree relatives:", [r.rid for r in R if any(c.counts_family for c in r.criteria)])
print("mini_engine TEMPLATES per form key:", {k: len(v) for k, v in E.TEMPLATES.items()}, "HEADERS:", len(E.HEADERS))
print("smoke.py HELDOUT_RULES:", S.HELDOUT_RULES, "TRAIN_TPL:", S.TRAIN_TPL, "TEST_TPL:", S.TEST_TPL)
'''

SMOKE_COUNTS = r'''
import json, sys
from collections import Counter
from selrm.rules import RULES_BY_ID, Mention
D, scores = sys.argv[1], sys.argv[2]
for name in ("train_blocks", "train_triplets", "dev_seen_rules", "test_heldout_rules"):
    seen, n = set(), Counter()
    for line in open(f"{D}/{name}.jsonl"):
        r = json.loads(line)
        if (r["tid"], r["case_kind"]) in seen:
            continue
        seen.add((r["tid"], r["case_kind"]))
        c = RULES_BY_ID[r["rid"]].crit(r["cid"])
        other = [m for m in (Mention(**x) for x in r["state"])
                 if m.concept == c.concept and (m.time == "past" or m.subject != "patient")]
        n["cases"] += 1
        n["with a past or other-person mention of the target concept"] += bool(other)
        n["where such a mention makes the criterion hold"] += any(c.applies(m) and m.status == "present" for m in other)
        n["from migraine_cad or contra_vte"] += r["rid"] in ("migraine_cad", "contra_vte")
    print(f"    {name}: {dict(n)}")
iids = lambda p: {json.loads(l)["iid"] for l in open(p)}
print("    rebuilt test_heldout_rules has exactly the iids of the B-C0 score file:",
      iids(f"{D}/test_heldout_rules.jsonl") == iids(scores))
'''


def pilot(tmp):
    print(f"\n== Pilot generator and smoke data at selrm@{PILOT}")
    code = archive(PILOT, tmp)
    py(PILOT_FACTS, code)
    out = os.path.join(tmp, "smoke_v2")
    subprocess.run([sys.executable, "scripts/make_smoke.py", out], cwd=code, check=True, capture_output=True)
    print("smoke_v2 rebuilt from that commit; cases (unique tid x case kind) per file:")
    scores = os.path.join(NEW, "results_git/B-C0-smoke-verdict-triplets-s0/scores_smoke_v2~test_heldout_rules.jsonl")
    py(SMOKE_COUNTS, code, out, scores)
    print("Runs trained or scored on smoke_v2 (results_git/*/meta.json), TA by set:")
    for m in sorted(glob.glob(os.path.join(NEW, "results_git/*/meta.json"))):
        d = json.load(open(m))
        s = {k: v for k, v in (d.get("summaries") or {}).items() if v}
        if any(k.startswith("smoke_v2") for k in s):
            print(f"    {d['run_id']}: format {d.get('format')}, corpus {d.get('corpus')}, "
                  + ", ".join(f"{k} TA {v['TA']:.1f} (n={v['n']})" for k, v in s.items()))


FIRST_COUNTS = r'''
import json, sys
from collections import Counter
from selrm.rules import RULES, RULES_BY_ID, Mention
D = sys.argv[1]
pilot = [r.rid for r in RULES[:11]]
ext = [r.rid for r in RULES[:11] if any(c.counts_past or c.counts_family for c in r.criteria)]
print("    first 11 rules of RULES:", pilot)
print("    of these, rules with a criterion that counts past or family findings:", ext)
def counting(c, ms):
    return [m for m in ms if c.applies(m) and m.status == "present"]
def only_ext(c, ms):
    """A finding criterion that holds in the flip only through past or relatives' mentions."""
    app = counting(c, ms)
    return c.kind == "finding" and bool(app) and all(m.time == "past" or m.subject != "patient" for m in app)
for name in ("test", "dev"):
    n = Counter()
    for line in open(f"{D}/{name}.jsonl", encoding="utf-8"):
        t = json.loads(line)
        c = RULES_BY_ID[t["rule"]].crit(t["criterion"])
        ms = [Mention(**x) for x in t["cases"]["flip"]["state"]]
        n["triplets"] += 1
        n["case kinds " + "/".join(t["cases"])] += 1
        if only_ext(c, ms):
            n["flip holds only through past or relatives' mentions"] += 1
            n["  of these, every counting mention past"] += all(m.time == "past" for m in counting(c, ms))
            n["  of these, on one of the first 11 rules"] += t["rule"] in pilot
            n["  of these, on " + "/".join(ext)] += t["rule"] in ext
    print(f"    {name}.jsonl: {dict(n)}")
for name in sys.argv[2:]:
    n = Counter()
    for line in open(f"{D}/train/{name}.jsonl", encoding="utf-8"):
        r = json.loads(line)
        n["case " + r["case"]] += 1
        if r["case"] == "flip":
            c = RULES_BY_ID[r["rule"]].crit(r["criterion"])
            ms = [Mention(c.concept, c.kind, True, e["subject"], e["status"], e["time"]) for e in r["ledger"]]
            if only_ext(c, ms):
                n["flip examples whose counting ledger entries are all past or relatives'"] += 1
                n["  of these, on one of the first 11 rules"] += r["rule"] in pilot
    print(f"    train/{name}.jsonl: {dict(n)}")
'''


def first_build(tmp):
    print(f"\n== First dataset build (Symbolic_PRM_NAACL@{FIRST}), sets rebuilt from that commit")
    code, out = archive(FIRST, tmp, OLD), os.path.join(tmp, "first")
    for script, *args in (("make_set.py", "--set", "test", "--out", f"{out}/test.jsonl"),
                          ("make_set.py", "--set", "dev", "--out", f"{out}/dev.jsonl"),
                          ("make_train.py", "--out", f"{out}/train")):
        subprocess.run([sys.executable, f"scripts/{script}", *args], cwd=code, check=True, capture_output=True)
    for rel in ("test.jsonl", "dev.jsonl", "train/manifest.json", *(f"train/{c}.jsonl" for c in CORPORA)):
        p = os.path.join(OLD, "data", rel)
        same = os.path.exists(p) and filecmp.cmp(os.path.join(out, rel), p, shallow=False)
        print(f"    rebuilt {rel} {'is identical to' if same else 'is NOT identical to'} {p}"
              + (f" (modified {mtime(p)})" if os.path.exists(p) else " (missing)"))
    man = json.load(open(os.path.join(out, "train", "manifest.json")))
    for c in CORPORA:
        print(f"    train/{c}: n {man[c]['n']}, cases {man[c]['cases']}, pres_share_of_label0 {man[c]['pres_share_of_label0']}")
    py(FIRST_COUNTS, code, out, *CORPORA)


V1_COUNTS = r'''
import json, sys
from collections import Counter
from selrm.library import LIBRARY_BY_ID
from selrm.rules import Mention
F = set(Mention.__dataclass_fields__)
for path in sys.argv[1:]:
    seen, n = set(), Counter()
    for line in open(path, encoding="utf-8"):
        r = json.loads(line)
        if r["case_kind"] != "flip" or r["tid"] in seen:
            continue
        seen.add(r["tid"])
        c = LIBRARY_BY_ID[r["rid"]].crit(r["cid"])
        app = [m for m in (Mention(**{k: v for k, v in x.items() if k in F}) for x in r["state"])
               if c.applies(m) and m.status == "present"]
        n["flip cases"] += 1
        if c.kind == "finding" and app and all(m.time == "past" or m.subject != "patient" for m in app):
            n["decisive finding counts only through past or relatives' mentions"] += 1
            n["  of these, all counting mentions past"] += all(m.time == "past" for m in app)
    print(f"    {path}: {dict(n)}")
'''


def manifests(rev):
    return {p.split("/")[1] + "/" + p.split("/")[2]: json.loads(git(NEW, "show", f"{rev}:{p}"))
            for p in git(NEW, "ls-tree", "-r", "--name-only", rev, "data").decode().split()
            if p.startswith("data/rule_v1") and p.endswith("/MANIFEST.json")}


def frozen(tmp):
    print(f"\n== Freeze (selrm@{FREEZE}) and later registry")
    reg = lambda rev: json.loads(git(NEW, "show", f"{rev}:data/REGISTRY.json"))
    a, b = reg(FREEZE), reg(NOW)
    print("commits that change data/REGISTRY.json (any ref):",
          git(NEW, "log", "--all", "--date=iso", "--format=%h %ad", "--", "data/REGISTRY.json").decode().split("\n")[:-1])
    for rev in (FREEZE, "3e0c832", "11f77f7", NOW):
        r = reg(rev)
        print(f"registry at {rev}: {len(r)} entries, {sum(v['frozen'] for v in r.values())} frozen, "
              f"{sum(r.get(k, {}).get('sha256') != v['sha256'] for k, v in a.items())} of the {len(a)} frozen at "
              f"{FREEZE} changed or missing")
    for v in sorted({k.split("/")[0] for k in a}):
        print(f"    at the freeze, {v}: {sorted(k.split('/')[1] for k in a if k.startswith(v + '/'))}")
    print("added after the freeze:", sorted(set(b) - set(a)))
    print("removed:", sorted(set(a) - set(b)), "sha256 changed:", [k for k in a if k in b and a[k]["sha256"] != b[k]["sha256"]])
    for ref in git(NEW, "for-each-ref", "--format=%(refname:short)", "refs/heads", "refs/remotes").decode().split():
        r = subprocess.run(["git", "-C", NEW, "show", f"{ref}:data/REGISTRY.json"], capture_output=True).stdout
        if not r:
            print(f"    {ref}: no data/REGISTRY.json")
            continue
        r = json.loads(r)
        print(f"    {ref}: {len(r)} entries, versions {sorted({k.split('/')[0] for k in r})}, entries frozen at "
              f"{FREEZE} with a changed or missing sha256: {sum(r.get(k, {}).get('sha256') != v['sha256'] for k, v in a.items())}")
    for k in ("rule_v1/test_L2", "rule_v1/dev", "rule_v1/train_blocks", "rule_v1/train_triplets"):
        print(f"    {k}: sha256 {a[k]['sha256']}, groups {a[k]['n_groups']}, records {a[k]['n_records']}")
    c = json.loads(git(NEW, "show", f"{NOW}:data/clin_v1/REGISTRY_C.json"))
    print(f"data/clin_v1/REGISTRY_C.json at {NOW}: {len(c)} entries, {sum(bool(v.get('frozen')) for v in c.values())} "
          f"frozen: {sorted(c)}")
    mans = manifests(FREEZE)
    print(f"MANIFESTs at {FREEZE}: {len(mans)}; git_commit:", Counter(m["git_commit"][:7] for m in mans.values()),
          "python:", Counter(m["python"] for m in mans.values()))
    print("shortcut validation:", Counter(m["shortcut_validation"]["result"] for m in mans.values()),
          "PASS sets:", [k for k, m in mans.items() if m["shortcut_validation"]["result"] == "PASS"])
    print("    rule_v1/readapply: cases_by_kind", mans["rule_v1/readapply"]["cases_by_kind"],
          "note:", mans["rule_v1/readapply"]["note"])
    print("template_split_hash:", Counter(m["template_split_hash"][:16] for m in mans.values()))
    for rev in (FREEZE, NOW):
        ms = mans if rev == FREEZE else manifests(rev)
        corp = {k: m["record_share"] for k, m in ms.items() if k.split("/")[1].startswith(("train_", "abl_", "div_"))}
        print(f"corpora (train_*, abl_*, div_*) at {rev}: {len(corp)}; without pres cases: "
              f"{[k for k, s in corp.items() if 'pres' not in s]}; without missing cases: "
              f"{[k for k, s in corp.items() if 'missing' not in s]}")
    print("    record_share of rule_v1/abl_nopres_triplets at the freeze:", mans["rule_v1/abl_nopres_triplets"]["record_share"])
    F = json.loads(git(NEW, "show", f"{FREEZE}:data/rule_v1/FOLDS.json"))
    ext = {r for k, v in F["classes"].items() if k.endswith("|ext") for r in v}
    print(f"FOLDS.json: class_def '{F['class_def']}'; {len(F['classes'])} classes, "
          f"{sum(k.endswith('|ext') for k in F['classes'])} with applicability ext; "
          f"{sum(map(len, F['classes'].values()))} rules, {len(ext)} in ext classes")
    for name, f in F["folds"].items():
        print(f"    fold {name}: L2 classes {f['l2_classes']}; " + "; ".join(
            f"{k} {len(f[k])} ({len(set(f[k]) & ext)} in ext classes)" for k in ("train_rules", "l1_rules", "l2_rules")))
    for s in ("train_natural", "train_balanced", "train_blocks", "train_triplets"):
        print(f"    {s}: record_share {mans['rule_v1/' + s]['record_share']}")
    d = json.loads(git(NEW, "show", f"{FREEZE}:results/A-D15/summary.json"))
    print("results/A-D15 templates:", d["templates"])
    print("Flip cases of frozen sets whose decisive finding counts only through a past or a relative's mention")
    print(f"(library code of selrm@{FREEZE_CODE}; records found locally and checked against the registry sha256):")
    found = []
    for s in ("train_triplets", "test_L2"):
        for root in (os.path.join(NEW, "data"), os.path.join(OLD, "rule_v1_rebuild", "f1")):
            p = os.path.join(root, "rule_v1", s, "records.jsonl")
            if os.path.exists(p) and hashlib.sha256(open(p, "rb").read()).hexdigest() == a[f"rule_v1/{s}"]["sha256"]:
                found.append(p)
                break
        else:
            print(f"    {s}: records not found (rebuild with scripts/build_rule_v1.py --out <dir>)")
    if found:
        py(V1_COUNTS, archive(FREEZE_CODE, tmp), *found)


def runs():
    print("\n== First logged training steps (results_git/*/run.log, UTC)")
    freeze = datetime.datetime.strptime(gdate(NEW, FREEZE), "%Y-%m-%d %H:%M:%S %z").astimezone(datetime.timezone.utc)
    print(f"freeze commit {FREEZE} in UTC: {freeze:%Y-%m-%dT%H:%M:%SZ}")
    rows = []
    for m in glob.glob(os.path.join(NEW, "results_git/*/meta.json")):
        d, log = json.load(open(m)), os.path.join(os.path.dirname(m), "run.log")
        hit = re.search(r"^(\S+Z) step ", open(log, encoding="utf-8", errors="replace").read(), re.M) if os.path.exists(log) else None
        if hit:
            rows.append((hit.group(1), d["run_id"], str(d.get("corpus"))))
    rows.sort()
    for r in rows[:4] + [r for r in rows if r[2].startswith("rule_v1")][:3]:
        print("    first step at", *r)
    v1 = [r for r in rows if r[2].startswith("rule_v1")]
    print(f"runs trained on rule_v1 with a step log: {len(v1)}; logged before the freeze: "
          f"{sum(r[0] < f'{freeze:%Y-%m-%dT%H:%M:%SZ}' for r in v1)}")


CAND = re.compile(rb"59\.[67]|0\.59[67]")


def hits(data):
    """(line, number, kind, line text) for every number that rounds to 59.7 (59.65 to below 59.75, or
    a share from 0.5965 to below 0.5975) or contains the characters 59.7. kind is 'u' for a per-item
    score margin ("u": ...), 'epoch' for training progress (epoch=...), '' otherwise."""
    out, line, last, end = [], 1, 0, -1
    for m in CAND.finditer(data):
        if m.start() < end:  # same number as the previous candidate
            continue
        s, e = m.start(), m.end()
        while s and data[s - 1] in b"0123456789.":
            s -= 1
        while e < len(data) and data[e] in b"0123456789":
            e += 1
        end, tok = e, data[s:e].decode()
        try:
            v = float(tok)
        except ValueError:
            v = None
        if "59.7" not in tok and not (v is not None and (59.65 <= v < 59.75 or 0.5965 <= v < 0.5975)):
            continue
        line, last = line + data.count(b"\n", last, s), s
        a, b = data.rfind(b"\n", 0, s) + 1, data.find(b"\n", e)
        pre = data[a:s].rstrip(b"-")
        kind = "u" if pre.endswith(b'"u": ') else "epoch" if pre.endswith(b"epoch=") else ""
        out.append((line, tok, kind, data[a:b if b >= 0 else len(data)].decode(errors="replace").strip()[:160]))
    return out


UNPACK = {".gz": gzip.decompress, ".gzip": gzip.decompress, ".bz2": bz2.decompress, ".xz": lzma.decompress,
          ".lzma": lzma.decompress}


def scan(name, data, found):
    """Add (name, place, number, kind, text) to found for every hit. Zip and tar archives are read
    member by member (nested ones too), gzip/bz2/xz files unpacked, PDFs read page by page as text;
    other files with a NUL byte are skipped (False)."""
    low = name.lower()
    if low.endswith((".zip", ".whl")):
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for i in z.infolist():
                if not i.is_dir():
                    scan(f"{name}!{i.filename}", z.read(i), found)
    elif low.endswith((".tgz", ".tar.gz", ".tar")):
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            for m in t.getmembers():
                if m.isfile():
                    scan(f"{name}!{m.name}", t.extractfile(m).read(), found)
    elif os.path.splitext(low)[1] in UNPACK:
        return scan(f"{name}!", UNPACK[os.path.splitext(low)[1]](data), found)
    elif low.endswith(".pdf"):
        for p, page in enumerate(fitz.open(stream=data, filetype="pdf"), 1):
            found += [(name, f"p.{p}", *h[1:]) for h in hits(page.get_text().encode())]
    elif b"\0" in data[:8000]:
        return False
    else:
        found += [(name, f"line {h[0]}", *h[1:]) for h in hits(data)]
    return True


def git_blobs(repo):
    """Yield ('commit:path', data) for every blob a commit on any ref added or changed (merges diffed
    against each parent), oldest first; commit and path are where the blob first appears."""
    first, commit = {}, None
    log = git(repo, "log", "--all", "--reverse", "-m", "--raw", "--no-abbrev", "--no-renames", "--format=C %h")
    for l in log.decode(errors="replace").splitlines():
        if l.startswith("C "):
            commit = l[2:9]  # --no-abbrev also lengthens %h
        elif l.startswith(":"):
            meta, path = l.split("\t", 1)
            mode, new = meta.split()[1], meta.split()[3]
            if mode != "160000" and new.strip("0"):
                first.setdefault(new, f"{commit}:{path}")
    p = subprocess.Popen(["git", "-C", repo, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for blob, where in first.items():
        p.stdin.write(blob.encode() + b"\n")
        p.stdin.flush()
        head = p.stdout.readline().split()
        if head[1] == b"missing":
            continue
        data = p.stdout.read(int(head[2]))
        p.stdout.read(1)
        yield where, data
    p.stdin.close()
    p.wait()


def show(title, found, git_names=False):
    counted, listed = Counter(), {}
    for name, place, tok, kind, text in found:
        path = name.split(":", 1)[1] if git_names else name
        if kind:
            counted[kind, path] += 1
        else:
            listed.setdefault((path, place, text), f"{name} {place}: {tok}  | {text}")
    print(title)
    for row in listed.values():
        print("   ", row)
    for kind, what in (("u", 'per-item score margins ("u")'), ("epoch", "training progress (epoch=)")):
        files = [f for k, f in counted if k == kind]
        print(f"    counted, not listed: {sum(v for (k, f), v in counted.items() if k == kind)} hits in {what} "
              f"in {len(files)} files")


def search(walk):
    print("\n== Search for the value of the appendix placeholder")
    print("A hit is a number that rounds to 59.7 (59.65 to below 59.75, or a share from 0.5965 to below 0.5975)")
    print("or that contains the characters 59.7. Text of PDFs is searched page by page, zips member by member.")
    for name, repo in REPOS.items():
        found, n = [], 0
        for where, data in git_blobs(repo):
            n += 1
            scan(where, data, found)
        show(f"{name}: {n} blobs (every version of every file committed on any ref; first commit:path shown)",
             found, git_names=True)
    found = []
    for z in sorted(glob.glob(OLD + "/*.zip")):
        scan(os.path.basename(z), open(z, "rb").read(), found)
    show("Bundles in D:/NAACL27 (every member, nested zips included):", found)
    if not walk:
        print("(working trees not searched; use --disk)")
        return
    found, n, skipped = [], 0, Counter()
    for root in (OLD, "D:/selrm"):
        for d, dirs, files in os.walk(root):
            dirs[:] = [x for x in dirs if x not in (".git", "__pycache__")]
            for f in files:
                p = os.path.join(d, f).replace("\\", "/")
                if os.path.dirname(p) == OLD and f.endswith(".zip"):
                    continue  # the bundles, searched above
                try:
                    n += 1
                    if not scan(p, open(p, "rb").read(), found):
                        skipped[os.path.splitext(f)[1].lower() or "(none)"] += 1
                except Exception as e:  # unreadable file or broken archive (test data of installed packages)
                    skipped[f"error {type(e).__name__}"] += 1
                    print(f"    not searched ({type(e).__name__}): {p}")
    show(f"Working trees under {OLD} (every clone in it) and D:/selrm: {n} files opened; files not searched "
         f"(binary, by extension, or failed): {dict(skipped.most_common())}", found)


def utc(date):
    """Table date as UTC: '... -0700' rows, '...Z' run-log rows, '... (UTC, ...)' rows; None if no time."""
    m = re.match(r"(\d{4}-\d\d-\d\d)[ T](\d\d:\d\d(?::\d\d)?)(?: ([+-]\d{4}))?", date)
    if not m:
        return None
    t, z = datetime.datetime.fromisoformat(f"{m.group(1)}T{m.group(2)}"), m.group(3)
    return t - datetime.timedelta(hours=int(z[:3]), minutes=int(z[0] + z[3:])) if z else t


def selftest():
    h = lambda s: [(tok, kind) for _, tok, kind, _ in hits(s.encode())]
    assert h("Hold 59.7 n=300") == [("59.7", "")]
    assert h('"u": -0.5966304540634155}') == [("0.5966304540634155", "u")]
    assert h("epoch=0.5973 x") == [("0.5973", "epoch")]
    assert h("1059.7 59.65 59.649 159.68 0.5975 10.5973") == [("1059.7", ""), ("59.65", "")]


def check(path):
    selftest()
    bad, last, rows, checked = 0, None, 0, 0
    for line in open(path, encoding="utf-8"):
        if not line.startswith("| 20"):
            continue
        rows += 1
        date, _, ev = [c.strip() for c in line.strip().strip("|").split("|")][:3]
        t = utc(date)
        if t and last and t < last:
            bad += 1
            print("BAD order:", date)
        last = t or last
        c = re.match(r"`?(Symbolic_PRM_NAACL|selrm)@([0-9a-f]{7,40})", ev)
        f = re.match(r"file on disk `([^`]+)`", ev)
        d = re.match(r"\d{4}-\d\d-\d\d \d\d:\d\d:\d\d [+-]\d{4}", date)
        if not d or not (c or f):
            continue
        checked += 1
        real = gdate(REPOS[c.group(1)], c.group(2)) if c else mtime(f.group(1))
        bad += real != d.group(0)
        print("ok " if real == d.group(0) else "BAD", d.group(0), (c or f).group(0), "" if real == d.group(0) else f"(actual {real})")
    print(f"table rows: {rows}; rows whose date was compared with git or the file time: {checked}; "
          f"problems (wrong date or order): {bad}")
    return bad


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--disk", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # PDF text has ligatures; output may be a file
    if a.check:
        sys.exit(1 if check(os.path.join(NEW, "docs", "TIMELINE.md")) else 0)
    t0 = datetime.datetime.now().astimezone()
    print(f"run started {t0:%Y-%m-%d %H:%M:%S %z}")
    commits()
    bundles()
    disk()
    with tempfile.TemporaryDirectory() as tmp:
        pilot(tmp)
        first_build(tmp)
        frozen(tmp)
    runs()
    search(a.disk)
    print(f"\nrun took {(datetime.datetime.now().astimezone() - t0).total_seconds():.0f} s")
