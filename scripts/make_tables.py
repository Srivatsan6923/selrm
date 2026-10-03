r"""Every table and every number of the paper, from result files only (FINAL_TASKS_D P0.2).

  python scripts/make_tables.py [--paper paper/latex_v13/main.tex]

Reads results/<run_id>/ and results_git/<run_id>/ (a run counts only once it has a
DONE file), the frozen records in data/ (sha256 checked against data/REGISTRY.json;
needed only for pooled intervals and paired tests) and computes every statistic
with selrm.metrics. Writes
  tables/<name>.tex        table bodies: the rows between the paper's
                           "% <tables:name>" and "% </tables:name>" markers
  tables/numbers.tex       \resdef{<key>}{<value>} for every \res{<key>} the paper uses
  tables/numbers.json      the same values (read by scripts/update_paper.py)
  tables/PROVENANCE.json   every key and table cell -> runs -> files -> commits
A missing result is written as \ph{tbd}: red in a draft build, an error once the
paper switches to \placeholdersfalse. Seeds s0..s4 of a run are pooled: a cell
shows their mean (and s.d. when there are two or more); tables/seeds.tex lists
every seed.

Keys, as used in \res{...} (fields are separated by '/'):
  run/<prefix>/<set>/<slice>/<metric>[/<stat>]
      prefix  run id without its seed suffix "-s<k>" (a run without seeds: its id)
      set     L2 dev L0 L1 L3alt L3inv hard missing dev_missing readapply f2L2 f3L2, or a
              set name written with ':' for '/', e.g. clin_v1:medeinst_test
      slice   all | nm_kind=<k> | tier=<t> | family=<f> | level=<l> | top (a top-level
              field such as MR or Reversal) | step=<claim type> | eval (the eval block)
      metric  a field of that slice: Rev Hold TA BaseAcc Tie PresHold n MR Reversal ...
      stat    mean (default) | sd | n (seeds) | min | max | s<k> | lo | hi
              (lo, hi: 95% interval, rules resampled with their triplets, seeds pooled)
  meta/<prefix>/<dotted.field>[/<stat>]   a meta.json field (mean over seeds by default)
  a15/<dotted.field>                      results/A-D15/summary.json
  sum/<run_id>/<dotted.field>            results/<run_id>/summary.json (a run without per-set summaries)
  cmp/<name>/<field>                      primary comparison: diff lo hi p padj n
  d/<key>|<key>[|<key>...]                first key minus the others
  min/<key>|<key>...  max/<key>|<key>...  smallest / largest of several keys
A key may end in @<format>: @0 @1 @2 @3 (decimals), @pct1 @pct2 (x100), @int.
"""
import argparse
import hashlib
import json
import math
import os
import re
import statistics
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from selrm import metrics as M  # noqa: E402

TOPS = ("results", "results_git")
SETS = {"L2": "rule_v1/test_L2", "dev": "rule_v1/dev", "L0": "rule_v1/test_L0", "L1": "rule_v1/test_L1",
        "L3alt": "rule_v1/test_L3alt", "L3inv": "rule_v1/test_L3inv", "hard": "rule_v1/test_hard",
        "missing": "rule_v1/missing", "dev_missing": "rule_v1/dev_missing", "readapply": "rule_v1/readapply",
        "f2L2": "rule_v1_fold2/test_L2", "f3L2": "rule_v1_fold3/test_L2"}
# Sets other roles have not published yet (names to be confirmed when they register them).
XR, CHALLENGE, REWRITE, EC = "xr_v1:test", "challenge_v1:test", "rewrite_v1:test", "ec_v1:test"
MEDEINST, KEY_MQA, KEY_CQA, NLI, TRIALGPT = ("clin_v1:medeinst_test", "clin_v1:keypairs_medqa",
                                             "clin_v1:keypairs_careqa", "clin_v1:nli4ct", "clin_v1:trialgpt_test")


def tg(prefix):
    """TrialGPT scores of a system live under C's run C-TG-<x> (HANDOFFS 3 Oct): B-F-<x> and C-TF-<x> -> C-TG-<x>."""
    for head in ("B-F-", "C-TF-"):
        if prefix.startswith(head):
            return "C-TG-" + prefix[len(head):]
    return prefix
SEL = {"mqa": "sel:medqa", "cqa": "sel:careqa", "key": "sel:keypairs", "me": "sel:medeinst"}
SEEDS = range(5)
TBD = r"\ph{tbd}"

WARN, DATA_PROV, CACHE, RUNS, _REC, _DEC, _COMMIT = [], {}, {}, {}, {}, {}, {}


def load_json(p):
    try:
        return json.load(open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return None


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def git(*a):
    try:
        return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except OSError:
        return ""


def file_commit(p):
    """Last commit that touched the file, or 'uncommitted'."""
    if p not in _COMMIT:
        _COMMIT[p] = git("log", "-1", "--format=%H", "--", rel(p)) or "uncommitted"
    return _COMMIT[p]


def set_name(abbr):
    return SETS.get(abbr, abbr.replace(":", "/"))


# ---------------------------------------------------------------- runs and files
class Run:
    def __init__(self, rid, path):
        self.id, self.path = rid, path
        self.meta = load_json(os.path.join(path, "meta.json")) or {}
        self.summaries, self.scores = {}, {}
        for f in sorted(os.listdir(path)):
            fp = os.path.join(path, f)
            if f.startswith("summary") and f.endswith(".json"):
                d = load_json(fp)
                s = d.get("set") if isinstance(d, dict) and isinstance(d.get("set"), str) else None
                s = s or f[len("summary_"):-5].replace("~", "/").replace("__", "/")
                self.summaries[s] = (fp, d)
            elif f.startswith("scores_") and f.endswith(".jsonl"):
                self.scores[f[len("scores_"):-6].replace("~", "/").replace("__", "/")] = fp


def run(rid):
    if rid not in RUNS:
        RUNS[rid] = None
        for top in TOPS:
            p = os.path.join(ROOT, top, rid)
            if os.path.exists(os.path.join(p, "DONE")):
                RUNS[rid] = Run(rid, p)
                break
    return RUNS[rid]


def seeds(prefix):
    """[(seed, Run)] for prefix-s0..s4 with DONE; [(None, Run)] for a run without seeds."""
    out = [(k, run(f"{prefix}-s{k}")) for k in SEEDS]
    out = [(k, r) for k, r in out if r]
    return out or ([(None, run(prefix))] if run(prefix) else [])


def records(set_):
    """Frozen records of a rule set (sha256 = registry), or None."""
    if set_ not in _REC:
        reg = load_json(os.path.join(ROOT, "data", "REGISTRY.json")) or {}
        e, recs = reg.get(set_), None
        p = os.path.join(ROOT, "data", e["path"]) if e else None
        if e and e.get("frozen") and os.path.exists(p) and sha256(p) == e["sha256"]:
            recs = [json.loads(line) for line in open(p, encoding="utf-8")]
            DATA_PROV[set_] = {"file": rel(p), "sha256": e["sha256"]}
        elif e:
            WARN.append(f"records of {set_} absent or not equal to the registry (rebuild with "
                        f"scripts/build_rule_v1.py): intervals and paired tests on it are tbd")
        _REC[set_] = recs
    return _REC[set_]


def triplets(r, set_):
    """selrm.metrics.decisions() of one run on one set, from its scores file; None if not possible."""
    key = (r.id, set_)
    if key not in _DEC:
        out, recs, f = None, records(set_), r.scores.get(set_)
        if recs and f:
            u = {}
            for line in open(f, encoding="utf-8"):
                j = json.loads(line)
                u[j["iid"]] = j["u"]
            if all(x["iid"] in u for x in recs):
                out = M.decisions(recs, [u[x["iid"]] for x in recs])
            else:
                WARN.append(f"{rel(f)} does not score every record of {set_}")
        _DEC[key] = out
    return _DEC[key]


def pooled(runs, set_, sl):
    """Triplet decisions of several seeds merged (tids prefixed by seed), restricted to a slice."""
    T = {}
    for k, r in runs:
        t = triplets(r, set_)
        if t is None:
            return None
        T.update({f"s{k}|{tid}": v for tid, v in t.items()})
    if sl not in ("all", "top") and "=" in sl:
        a, b = sl.split("=", 1)
        T = {k: v for k, v in T.items() if str(v.get(a)) == b}
    return T


def field(d, sl, metric):
    if not isinstance(d, dict):
        return None
    if sl == "top":
        x = d.get(metric)
    elif sl.startswith("step="):
        x = (d.get("step") or {}).get(sl[5:], {}).get(metric)
    else:
        x = (d.get(sl) or {}).get(metric) if isinstance(d.get(sl), dict) else None
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) else None


def prov_run(r, f, fld, k=None):
    return {"run_id": r.id, "seed": k, "file": rel(f), "field": fld, "file_commit": file_commit(f),
            "code_commit": r.meta.get("git_commit")}


# ---------------------------------------------------------------- key resolution
def fmt(x, spec=None, integer=False):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return TBD
    if spec in ("pct1", "pct2"):
        return f"{100 * x:.{spec[-1]}f}"
    if spec == "int" or (spec is None and integer):
        return f"{int(round(x)):,}".replace(",", "{,}")
    return f"{x:.{int(spec) if spec and spec.isdigit() else 1}f}"


def resolve(key):
    """-> (number or None, LaTeX text, provenance dict). Never raises."""
    if key not in CACHE:
        try:
            CACHE[key] = _resolve(key)
        except Exception as e:  # malformed key: tbd, and say why
            CACHE[key] = (None, TBD, {"error": f"{type(e).__name__}: {e}"})
    return CACHE[key]


def _resolve(key):
    spec = None
    if "@" in key.rsplit("/", 1)[-1]:
        key, spec = key.rsplit("@", 1)
    if key[:2] == "d/" or key[:4] in ("min/", "max/"):
        op, _, body = key.partition("/")
        parts = body.split("|")
        xs = [resolve(k)[0] for k in parts]
        if any(x is None for x in xs):
            n = None
        else:
            n = xs[0] - sum(xs[1:]) if op == "d" else (min(xs) if op == "min" else max(xs))
        return n, fmt(n, spec), {op: parts}
    head, _, rest = key.partition("/")
    if head == "run":
        return run_value(rest, spec)
    if head == "meta":
        return meta_value(rest, spec)
    if head in ("a15", "sum"):     # a field of a run's summary.json (a run without per-set summaries)
        rid, path = ("A-D15", rest) if head == "a15" else rest.split("/", 1)
        r = run(rid)
        p = os.path.join(r.path, "summary.json") if r else None
        x = load_json(p) if p else None
        for part in path.split("."):
            x = x.get(part) if isinstance(x, dict) else None
        x = x if isinstance(x, (int, float)) and not isinstance(x, bool) else None
        return x, fmt(x, spec, isinstance(x, int)), {"runs": [prov_run(r, p, path)] if r else []}
    if head == "cmp":
        name, fld = rest.split("/")
        c = comparisons().get(name)
        x = c.get(fld) if c else None
        return x, fmt(x, spec or ("3" if fld in ("p", "padj") else None), fld == "n"), {"comparison": name}
    raise KeyError(f"unknown key head {head!r}")


def scores_of(r, set_):
    f = r.scores.get(set_)
    if not f:
        return None, None
    u = {j["iid"]: j["u"] for j in map(json.loads, open(f, encoding="utf-8"))}
    recs = records(set_)
    return (recs, [u[x["iid"]] for x in recs]) if recs and all(x["iid"] in u for x in recs) else (None, None)


def derived(r, set_, sl, metric):
    """Statistics a summary file does not hold, computed by selrm.metrics from the run's scores:
    MR/FR at 5% false rejection (threshold from dev_missing), near-miss decisions (slice
    'nmt:<all|nm_kind=k>'), macro-averages (slice 'macro:<rid|family>'). -> (value, files) or (None, None)."""
    if set_ == SETS["missing"] and sl == "top" and metric in ("MR", "FR", "threshold"):
        dr, du = scores_of(r, SETS["dev_missing"])
        mr, mu = scores_of(r, set_)
        if dr is None or mr is None:
            return None, None
        out = M.missing_rejection(mr, mu, M.mr_threshold(dr, du))
        return out[metric], [r.scores[SETS["dev_missing"]], r.scores[set_]]
    if sl.startswith("nmt:") or sl.startswith("macro:"):
        T = triplets(r, set_)
        if T is None:
            return None, None
        if sl.startswith("nmt:"):
            x = M.nearmiss_table(T).get(sl[4:], {}).get(metric)
        else:
            x = M.macro(T, metric, over=sl[6:])["macro"]
        return x, [r.scores[set_]]
    return None, None


def run_value(rest, spec):
    prefix, sab, sl, metric, *st = rest.split("/")
    stat, set_ = (st[0] if st else "mean"), set_name(sab)
    runs = seeds(prefix)
    vals = []
    for k, r in runs:
        fd = r.summaries.get(set_)
        x = field(fd[1], sl, metric) if fd else None
        if x is not None:
            vals.append((k, x, fd[0], r))
        else:
            x, files = derived(r, set_, sl, metric)
            if x is not None:
                vals.append((k, x, files[-1], r))
    prov = {"runs": [prov_run(r, f, f"{sl}.{metric}", k) for k, _, f, r in vals],
            "set": set_, "stat": stat, "seeds_found": [k for k, *_ in vals]}
    xs = [x for _, x, _, _ in vals]
    integer = metric == "n" and all(float(x).is_integer() for x in xs)
    if not xs:
        return None, TBD, prov
    if stat == "n":
        return len(xs), str(len(xs)), prov
    if stat == "mean":
        n = statistics.fmean(xs)
    elif stat == "sd":
        n = statistics.stdev(xs) if len(xs) > 1 else None
    elif stat in ("min", "max"):
        n = min(xs) if stat == "min" else max(xs)
    elif re.fullmatch(r"s\d", stat):
        n = next((x for k, x, *_ in vals if k == int(stat[1:])), None)
    elif stat in ("lo", "hi"):
        n = interval(prefix, [(k, r) for k, _, _, r in vals], set_, sl, metric, prov)
        n = None if n is None else n[0 if stat == "lo" else 1]
    else:
        raise KeyError(f"unknown stat {stat!r}")
    return n, fmt(n, spec, integer), prov


def interval(prefix, runs, set_, sl, metric, prov):
    """95% interval of a slice metric: the summary's CI95 for one seed and the whole set,
    otherwise selrm.metrics.bootstrap_ci on the triplets of all seeds pooled."""
    if len(runs) == 1 and sl == "all":
        fp, d = runs[0][1].summaries[set_]
        ci = (d.get("CI95") or {}).get(metric)
        if isinstance(ci, list) and len(ci) == 2:
            prov["interval"] = "CI95 of the summary file"
            return ci
    T = pooled(runs, set_, sl)
    if not T or metric not in ("Rev", "Hold", "TA", "BaseAcc", "Tie", "PresHold"):
        return None
    for k, r in runs:
        prov.setdefault("scores", []).append(rel(r.scores[set_]))
    prov["interval"] = f"selrm.metrics.bootstrap_ci, {len(runs)} seed(s) pooled, rules resampled"
    prov["records"] = DATA_PROV.get(set_)
    return M.bootstrap_ci(T, metric)


def meta_value(rest, spec):
    prefix, path, *st = rest.split("/")
    stat = st[0] if st else "mean"
    xs, prov = [], {"runs": []}
    for k, r in seeds(prefix):
        x = r.meta
        for part in path.split("."):
            x = x.get(part) if isinstance(x, dict) else None
        if isinstance(x, (int, float)) and not isinstance(x, bool):
            xs.append(x)
            prov["runs"].append(prov_run(r, os.path.join(r.path, "meta.json"), path, k))
    if not xs:
        return None, TBD, prov
    n = {"mean": statistics.fmean, "min": min, "max": max, "sum": sum}[stat](xs) if stat != "n" else len(xs)
    return n, fmt(n, spec, all(isinstance(x, int) for x in xs)), prov


# ---------------------------------------------------------------- primary comparisons
# App. A of the paper: the primary comparisons, a minus b, one Holm family.
COMPARISONS = [
    ("p1", "B-F-verdict-balanced", "B-F-verdict-natural", "L2", "TA"),
    ("p2", "B-F-verdict-triplets", "B-F-verdict-blocks", "L2", "TA"),
    ("p3", "B-F-ledger2-triplets", "B-F-summary2-triplets", "L2", "TA"),
    ("p4", "B-F-ledger2-triplets", "C-TF-critic", MEDEINST, "Reversal"),
    ("p5", "B-F-ledger2-triplets", "B-F-summary2-triplets", MEDEINST, "Reversal"),
    ("p6a", "C-TG-ledger2-triplets", "C-TG-critic", TRIALGPT, "macroF1"),   # C writes these two with a patient
    ("p6b", "C-TG-ledger2-triplets", "C-TG-ledger2-blocks", TRIALGPT, "macroF1"),   # bootstrap (C-TG-comparisons_test.json)
]
_CMP = {}


def comparisons():
    """{name: {diff, lo, hi, p, padj, n}}; p and padj only when selrm.metrics provides
    paired_test and holm (change request to C, 2 Oct)."""
    if _CMP:
        return _CMP
    test, holm = getattr(M, "paired_test", None), getattr(M, "holm", None)
    for name, a, b, sab, metric in COMPARISONS:
        set_, out = set_name(sab), {"a": a, "b": b, "set": set_name(sab), "metric": metric}
        ra, rb = dict(seeds(a)), dict(seeds(b))
        common = sorted(set(ra) & set(rb), key=str)
        if set_.startswith("rule_v1") and common:
            Ta = pooled([(k, ra[k]) for k in common], set_, "all")
            Tb = pooled([(k, rb[k]) for k in common], set_, "all")
            if Ta and Tb:
                out["diff"], out["lo"], out["hi"] = M.paired_diff(Ta, Tb, metric)
                out["n"], out["seeds"] = len(Ta.keys() & Tb.keys()), [str(k) for k in common]
                if test:
                    out["p"] = test(Ta, Tb, metric)[-1]
        _CMP[name] = out
    ps = [c.get("p") for c in _CMP.values()]
    if holm and all(p is not None for p in ps):
        for c, q in zip(_CMP.values(), holm(ps)):
            c["padj"] = q
    _CMP["holm"] = {"n": len(COMPARISONS)}
    return _CMP


# ---------------------------------------------------------------- table helpers
CELLS = {}      # table -> [{"row", "col", "key", "value"}]


def cell(table, row, col, key, seeded=True):
    """Text of one table cell; mean (+ s.d. over seeds) of a run key; records provenance."""
    n, text, _ = resolve(key)
    if seeded and key.startswith("run/") and "@" not in key and len(key.split("/")) == 5 and n is not None:
        k_n, _, _ = resolve(key + "/n")
        if k_n and k_n > 1:
            text += r"\sd{" + resolve(key + "/sd")[1] + "}"
    CELLS.setdefault(table, []).append({"row": row, "col": col, "key": key, "value": text})
    return text, n


def rows_tex(table, rows, cols, bold="none"):
    """rows: [(label, {col: key or None})] or ("group", text); cols: [col names]. None -> '--'.
    bold: 'max' bolds the largest value of each column, 'table' the largest of the table."""
    built = []
    for r in rows:
        if r[0] == "group":
            built.append(("group", r[1]))
            continue
        label, keys = r
        built.append((label, [(cell(table, label, c, keys[c]) if keys.get(c) else ("--", None)) for c in cols]))
    if bold == "table":
        cand = [(b[1][j][1], i, j) for i, b in enumerate(built) if b[0] != "group"
                for j in range(len(cols)) if b[1][j][1] is not None]
        top = max((c[0] for c in cand), default=None)
        for x, i, j in cand:
            if x == top:
                built[i][1][j] = (r"\textbf{" + built[i][1][j][0] + "}", x)
    if bold == "max":
        for j in range(len(cols)):
            vals = [b[1][j][1] for b in built if b[0] != "group" and b[1][j][1] is not None]
            if len(vals) > 1:
                top = max(vals)
                for b in built:
                    if b[0] != "group" and b[1][j][1] == top:
                        b[1][j] = (r"\textbf{" + b[1][j][0] + "}", top)
    out = []
    for b in built:
        if b[0] == "group":
            out.append(r"\multicolumn{" + str(len(cols) + 1) + r"}{@{}l}{\emph{" + b[1] + r"}}\\")
        else:
            out.append(b[0] + " & " + " & ".join(t for t, _ in b[1]) + r"\\")
    return "\n".join(out) + "\n"


def runkey(prefix, sab, metric, sl="all"):
    return f"run/{prefix}/{sab}/{sl}/{metric}"


def label(prefix, fallback):
    """Row label of an audited model: the verified model ID from the run's meta.json, else the
    draft's placeholder name in red."""
    rs = seeds(prefix)
    m = rs[0][1].meta.get("model") if rs else None
    return m.replace("_", r"\_") if m else r"\ph{" + fallback + "}"


# ---------------------------------------------------------------- the tables of v13
CORPORA = ("natural", "balanced", "blocks", "triplets")
FORMATS = [("verdict", "Verdict only"), ("rationale", "Rationale, then verdict"),
           ("summary2", "Evidence summary (prose)"), ("value2", "Value ledger"),
           ("ledger2", "Applicability ledger")]


def t_factorial():
    rows = [("group", "One-stage (verdict produced with the case in context)")]
    for f, lab in FORMATS:
        if f == "summary2":
            rows.append(("group", "Two-stage (case-blind judge)"))
        rows.append((lab, {c: runkey(f"B-F-{f}-{c}", "L2", "TA") for c in CORPORA}))
    rows += [("group", "Two-stage, judge also sees the case"),
             ("Evidence summary", {"triplets": runkey("B-F-summary2case-triplets", "L2", "TA")})]
    return rows_tex("factorial", rows, CORPORA, bold="table")


AUDIT = [("Trained PRMs", [("C-AUD-meds3", "MedS$^3$ PRM"), ("C-AUD-medprm", "Med-PRM"),
                           ("C-AUD-fover", "FoVer PRM"), ("C-AUD-injerr", "Inj.-error PRM"),
                           ("C-AUD-thinkprm", "ThinkPRM"), ("C-AUD-genprm", "GenPRM-7B")]),
         ("Open judges", [("C-AUD-qwen35-9b", r"\bb{}"), ("C-AUD-llama70b", "Llama-3.3-70B"),
                          ("C-AUD-qwen35-27b", "Qwen3.5-27B"), ("C-AUD-kimi-k3", "Kimi K3")]),
         ("Closed judges", [("C-AUD-closed-1", "GPT-5.4"), ("C-AUD-closed-2", "Gemini 3.1 Pro"),
                            ("C-AUD-closed-3", "Claude Opus 5.5")])]
AUDIT_SET = "L2"    # FINAL_TASKS_C P1: 13 signals, closed judges on L2 triplets (v13's caption says L0)


def t_audit():
    cols = ["Rev", "Hold", "TA", "MR", "ME", "Key"]
    rows = []
    for group, members in AUDIT:
        rows.append(("group", group))
        for prefix, name in members:
            lab = label(prefix, name) if name != r"\bb{}" else name
            rows.append((lab, {"Rev": runkey(prefix, AUDIT_SET, "Rev"), "Hold": runkey(prefix, AUDIT_SET, "Hold"),
                               "TA": runkey(prefix, AUDIT_SET, "TA"), "MR": f"run/{prefix}/missing/top/MR",
                               "ME": f"run/{prefix}/{MEDEINST}/top/Reversal",
                               "Key": f"run/{prefix}/{KEY_MQA}/top/Reversal"}))
    return rows_tex("audit", rows, cols)


TRANSFER = [
    ("Training-free, \\bb", [("Critic", "C-TF-critic"), ("\\ \\ + default correction", "C-TF-defcorr"),
                              ("\\ \\ + prompted ledger", "C-TF-promptledger"),
                              ("Generated-program verifier", "C-TF-genprog")]),
    ("Trained without medical QA data (clinical columns are zero-shot)", [
        ("Verdict only, rule blocks", "B-F-verdict-blocks"), ("Verdict only, FoVer data", "B-TR-fover"),
        ("Verdict only, rule triplets", "B-F-verdict-triplets"),
        ("Evidence summary, rule triplets", "B-F-summary2-triplets"),
        ("GenPRM-style verifier, rule triplets", "B-TR-genprm"),
        ("\\method{}, rule balanced", "B-F-ledger2-balanced"), ("\\method{}, rule blocks", "B-F-ledger2-blocks"),
        ("\\textbf{\\method}, rule triplets", "B-F-ledger2-triplets")]),
    ("With medical data", [("\\method{}, rule triplets + step-error data", "B-TR-steperr"),
                           ("\\method{}, clinical pairs only", "B-TR-clinonly"),
                           ("\\method{}, rule triplets + clinical pairs", "B-TR-tripclin")]),
    ("References", [("CLOSED, zero-shot", "C-REF-closed-zero"), ("CLOSED, prompted ledger", "C-REF-closed-ledger"),
                    ("Extraction + hand-written program", "C-REF-extract-program")]),
]
NO_CLINICAL = {"C-TF-genprog", "C-REF-extract-program"}


def closed_label(text, prefix):
    return text.replace("CLOSED", label(prefix, "Claude Opus 5.5"))


def t_main():
    cols = ["L2", "L3-alt", "XA", "Hold", "MR", "Criteria", "TrialGPT", "MedEinst"]
    rows = []
    for group, members in TRANSFER:
        rows.append(("group", group))
        for lab, p in members:
            keys = {"L2": runkey(p, "L2", "TA"), "L3-alt": runkey(p, "L3alt", "TA"), "XA": f"run/{p}/{XR}/top/XA",
                    "Hold": runkey(p, "L2", "Hold"), "MR": f"run/{p}/missing/top/MR"}
            if p not in NO_CLINICAL:
                keys |= {"Criteria": runkey(p, EC, "TA"), "TrialGPT": f"run/{tg(p)}/{TRIALGPT}/top/macroF1",
                         "MedEinst": f"run/{p}/{MEDEINST}/top/Reversal"}
            rows.append((closed_label(lab, p), keys))
    return rows_tex("main", rows, cols)


def t_main_app():
    cols = ["Key", "NLI-F", "NLI-C"]
    rows = []
    for group, members in TRANSFER:
        rows.append(("group", group))
        for lab, p in members:
            keys = {} if p in NO_CLINICAL else {"Key": f"run/{p}/{KEY_MQA}/top/Reversal",
                                                "NLI-F": f"run/{p}/{NLI}/top/faithfulness",
                                                "NLI-C": f"run/{p}/{NLI}/top/consistency"}
            rows.append((closed_label(lab, p), keys))
    return rows_tex("main-app", rows, cols)


SELECTION = [("Single sample", "D-SEL-single"), ("Self-consistency", "D-SEL-selfcons"),
             ("Step check", "D-SEL-stepcheck"), ("\\ \\ \\ vignette swapped", "D-SEL-stepcheck-swap"),
             ("Ledger score", "D-SEL-ledger"), ("Combined", "D-SEL-combined"),
             ("\\ \\ \\ vignette swapped", "D-SEL-combined-swap"), ("\\ \\ \\ no near-misses", "D-SEL-no-nearmiss"),
             ("CLOSED", "D-SEL-closed")]


def t_downstream():
    cols = ["MQA", "CQA", "Key", "pair", "ctrl", "trap"]

    def keys(p):
        return {"MQA": f"run/{p}/{SEL['mqa']}/top/acc", "CQA": f"run/{p}/{SEL['cqa']}/top/acc",
                "Key": f"run/{p}/{SEL['key']}/top/pair_acc", "pair": f"run/{p}/{SEL['me']}/top/pair_acc",
                "ctrl": f"run/{p}/{SEL['me']}/top/control_acc", "trap": f"run/{p}/{SEL['me']}/top/trap_acc"}
    rows = [(closed_label(lab, p), keys(p)) for lab, p in SELECTION]
    body = rows_tex("downstream", rows, cols, bold="max")
    return body + "\\midrule\n" + rows_tex("downstream", [("Oracle selection", keys("D-SEL-oracle"))], cols)


ABLATION = [("\\method{} (facts only)", "B-F-ledger2-triplets", "all"),
            ("\\ \\ + decision field", "B-AB-decfield", "all"),
            ("\\ \\ decision field only", "B-AB-bitonly-judge", "all"),
            ("\\ \\ program on predicted bit", "B-AE-pred-bit-program", "all"),
            ("\\ \\ reader writes bit only", "B-AB-bitonly-reader", "all"),
            ("\\ \\ condition derived by the reader", "B-AB-condition", "all"),
            ("\\ \\ + verification pass", "B-AB-verify", "all"),
            ("\\ \\ program-supplied ledger", "B-AE-oracle-ledger", "all"),
            ("\\ \\ program on predicted ledger", "B-AE-pred-ledger-program", "all"),
            ("One-stage ledger", "B-F-rationale-triplets", "all"),
            ("Value ledger", "B-F-value2-triplets", "all"),
            ("Evidence summary (matched prose)", "B-F-summary2-triplets", "all"),
            ("\\ \\ judge also sees the case", "B-F-summary2case-triplets", "all"),
            ("Concept scorer", "B-AB-concept", "all"),
            ("Premise gate", "B-AE-premise-gate", "all"),
            ("$-$ near-misses", "B-F-ledger2-blocks", "all"),
            ("\\ \\ + probe re-weighting", "B-AB-probe-rw", "all"),
            ("$-$ other-person near-misses", "B-LOKO-subject-ledger2", "nm_kind=subject"),
            ("$-$ past near-misses", "B-LOKO-time-ledger2", "nm_kind=time"),
            ("$-$ threshold near-misses", "B-LOKO-boundary-ledger2", "nm_kind=boundary"),
            ("$-$ presentation edits", "B-AB-nopres", "all"),
            ("$-$ ledger resampling", "B-AB-noresamp", "all"),
            ("Verdict only, pairwise loss", "B-AB-pairwise", "all")]
NO_ME = {"B-AE-pred-bit-program", "B-AE-oracle-ledger", "B-AE-pred-ledger-program"}


def t_ablation():
    cols = ["Rev", "Hold", "TA", "MR", "ME"]
    rows = [(lab, {"Rev": runkey(p, "L2", "Rev", sl), "Hold": runkey(p, "L2", "Hold", sl),
                   "TA": runkey(p, "L2", "TA", sl), "MR": f"run/{p}/missing/top/MR",
                   "ME": None if p in NO_ME else f"run/{p}/{MEDEINST}/top/Reversal"}) for lab, p, sl in ABLATION]
    return rows_tex("ablation", rows, cols)


LADDER = [("Critic", "C-TF-critic"), ("Verdict only, blocks", "B-F-verdict-blocks"),
          ("\\method{}, rule blocks", "B-F-ledger2-blocks"), ("Verdict only, triplets", "B-F-verdict-triplets"),
          ("\\method{}, rule triplets", "B-F-ledger2-triplets"), ("Closed judge, ledger", "C-REF-closed-ledger")]
LADDER_SETS = [("Dev", "dev"), ("L0", "L0"), ("L1", "L1"), ("L2", "L2"), ("L3-inv", "L3inv"),
               ("L3-alt", "L3alt"), ("Long", "hard")]


def t_ladder():
    cols = [c for c, _ in LADDER_SETS]
    return rows_tex("ladder", [(lab, {c: runkey(p, s, "TA") for c, s in LADDER_SETS}) for lab, p in LADDER], cols)


KINDS = [("thr.", "boundary"), ("neg.", "negation"), ("num.", "numeric"), ("subj.", "subject"), ("time", "time")]


def t_kinds():
    systems = [("Verdict only, blocks", "B-F-verdict-blocks"), ("\\method{}, blocks", "B-F-ledger2-blocks"),
               ("Verdict only, triplets", "B-F-verdict-triplets"), ("\\method{}, triplets", "B-F-ledger2-triplets")]
    cols = [c for c, _ in KINDS]
    body = rows_tex("kinds", [(lab, {c: runkey(p, "L2", "TA", f"nm_kind={k}") for c, k in KINDS})
                              for lab, p in systems], cols)
    n_row = rows_tex("kinds", [("$n$ (triplets)", {c: f"run/B-F-ledger2-triplets/L2/nm_kind={k}/n@int"
                                                   for c, k in KINDS})], cols)
    # near-miss decisions of the headline system (selrm.metrics.nearmiss_table on its L2 scores)
    extra = rows_tex("kinds", [(f"\\method{{}} triplets: {lab}",
                                {c: f"run/B-F-ledger2-triplets/L2/nmt:nm_kind={k}/{m}" for c, k in KINDS})
                               for lab, m in (("same decision on base and near-miss", "SameDecision"),
                                              ("both correct", "BothCorrect"),
                                              ("near-miss correct given base correct", "NearGivenBase"))], cols)
    return body + "\\midrule\n" + n_row + extra


SHORTCUTS = [("Always default", "A-D14-always_default"), ("Claim only", "A-D14-claim_only"),
             ("Concept named ($h_k$)", "A-D14-concept_named"), ("Bag of words, case + claim", "A-D14-bag_of_words"),
             ("Attribute-blind, logistic", "A-D14-attribute_blind"),
             ("Trigger lexicon + program, training cue phrases", "A-D14-trigger_train"),
             ("\\ \\ given the test cue phrases", "A-D14-trigger_all"),
             ("General-purpose trigger tagger + program", "C-DG-trigger")]


def t_shortcuts():
    cols = ["Rev", "Hold", "TA"]
    return rows_tex("shortcuts", [(lab, {c: runkey(p, "L2", c) for c in cols}) for lab, p in SHORTCUTS], cols)


def t_rules():
    def k(path, spec="int"):
        return f"a15/{path}@{spec}"
    rows = [("Published scores, our implementation", {"Rules": k("rules_by_kind.score"), "Classes": None}),
            ("Constraint rules from public recommendations",
             {"Rules": "d/a15/rules_total|a15/rules_by_kind.score|a15/rules_by_source.grammar_sampled@int",
              "Classes": None}),
            ("Grammar-sampled rules", {"Rules": k("rules_by_source.grammar_sampled"), "Classes": None})]
    body = rows_tex("rules", rows, ["Rules", "Classes"])
    total = rows_tex("rules", [("Total (\\texttt{rule\\_v1})", {"Rules": k("rules_total"), "Classes": k("folds.1.n_classes")})],
                     ["Rules", "Classes"])
    return (body + "MedCalc-Bench calculators            & \\multicolumn{2}{r}{not included}\\\\\n\\midrule\n" + total)


def t_seeds():
    """Every seed of every seeded run prefix used in the tables: L2 triplet accuracy.
    A seed that has not been run prints '--' (the cells above pool the seeds that exist)."""
    prefixes = sorted({c["key"].split("/")[1] for cs in CELLS.values() for c in cs
                       if c["key"].startswith("run/") and c["key"].split("/")[2:5] == ["L2", "all", "TA"]})
    out = []
    for p in prefixes:
        rs = seeds(p)
        if not rs or rs[0][0] is None:
            continue
        key, have = runkey(p, "L2", "TA"), {k for k, _ in rs}
        vals = [cell("seeds", p, f"s{k}", f"{key}/s{k}", seeded=False)[0] if k in have else "--" for k in SEEDS]
        mean = cell("seeds", p, "mean", key, seeded=False)[0]
        sd = cell("seeds", p, "sd", key + "/sd", seeded=False)[0] if len(rs) > 1 else "--"
        lo, hi = (cell("seeds", p, s, f"{key}/{s}", seeded=False)[0] for s in ("lo", "hi"))
        out.append(r"\texttt{" + p.replace("_", r"\_") + "} & " + " & ".join(vals)
                   + f" & {mean} & {sd} & [{lo}, {hi}]" + r"\\")
    return "\n".join(out) + "\n"


def t_primary():
    """App. A primary comparisons: paired difference on identical items (selrm.metrics.paired_diff,
    rules resampled with their triplets, seeds paired by index), p and Holm-adjusted p."""
    names = {"p1": "(1) balanced $-$ natural, verdict only, L2 TA",
             "p2": "(2) triplets $-$ blocks, verdict only, L2 TA",
             "p3": "(3) applicability ledger $-$ evidence summary, triplets, L2 TA",
             "p4": "(4) rule-only \\method{} $-$ critic, MedEinst reversal",
             "p5": "(5) rule-only \\method{} $-$ rule-only summary, MedEinst reversal",
             "p6a": "(6a) \\method{} triplets $-$ backbone, TrialGPT macro-F1",
             "p6b": "(6b) \\method{} triplets $-$ blocks, TrialGPT macro-F1"}
    cols = ["diff", "CI", "p", "padj"]
    out = []
    for name, *_ in COMPARISONS:
        d, lo, hi, p, q = (cell("primary", name, f, f"cmp/{name}/{f}", seeded=False)[0]
                           for f in ("diff", "lo", "hi", "p", "padj"))
        out.append(names[name] + f" & {d} & [{lo}, {hi}] & {p} & {q}" + r"\\")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- figure bodies (pgfplots \addplot lines)
DIV = [("new", "blue!75!black", "mark=*", "new struct.", (16, 32, 63, 64, 128, 223)),
       ("same", "orange!85!black", "mark=triangle*", "same struct.", (16, 32, 63)),
       ("patients", "black!60", "mark=square*", "more cases", (16, 32, 63, 64, 128, 223))]


def plot(table, color, mark, name, pts, errors=False):
    """One \\addplot of (x, key) points; points without a result are left out."""
    coords, last = [], None
    for x, key in pts:
        n = cell(table, name, str(x), key, seeded=False)[1]
        if n is None:
            continue
        sd = resolve(key + "/sd")[0] if errors and key.startswith("run/") else None
        coords.append(f"({x},{n:.1f})" + (f" +- (0,{sd:.1f})" if errors and sd is not None else ""))
        last = (x, n)
    if not coords:                     # no result yet: no plot (an empty plot breaks some axes)
        return "", False
    opts = f"{color}, thick, {mark}, mark size=1pt" + (", error bars/.cd, y dir=both, y explicit" if errors else "")
    out = r"\addplot[" + opts + "] coordinates {" + " ".join(coords) + "};\n"
    if last:
        out += (r"\node[font=\tiny, text=" + color + r", anchor=south east] at (axis cs:"
                f"{last[0]},{last[1]:.1f})" + " {" + name + "};\n")
    return out, bool(coords)


def tbd_node(any_data):
    return "" if any_data else r"\node[red, font=\tiny] at (rel axis cs:0.5,0.5) {" + TBD + "};" + "\n"


def f_div():
    """Fig. 3 left: L2 triplet accuracy of the diversity runs (mean over seeds, bars: s.d.)."""
    body, anyd = "", False
    for curve, color, mark, name, xs in DIV:
        pts = [(x, runkey("B-DIV-base-16" if x == 16 else f"B-DIV-{curve}-{x}", "L2", "TA")) for x in xs]
        b, d = plot("fig-div", color, mark, name, pts, errors=True)
        body, anyd = body + b, anyd or d
    return body + tbd_node(anyd)


SELN = [("combined", "blue!75!black", "mark=*", r"\method"), ("stepcheck", "black!60", "mark=square*", "step check"),
        ("oracle", "black!45", "dashed", "oracle")]


def f_seln():
    """Fig. 3 right: key-pair accuracy of the trace selected among N samples (D-SELN)."""
    body, anyd = "", False
    for sel, color, mark, name in SELN:
        pts = [(n, f"run/D-SELN/{SEL['key']}/selector={sel}/N{n}") for n in (1, 2, 4, 8, 16, 32, 64)]
        b, d = plot("fig-seln", color, mark, name, pts)
        body, anyd = body + b, anyd or d
    return body + tbd_node(anyd)


DIAG = [("Verdict (blocks)", "B-F-verdict-blocks"), ("27B judge", "C-AUD-qwen35-27b"),
        ("9B judge", "C-AUD-qwen35-9b"), ("Inj.\\ PRM", "C-AUD-medprm")]


def f_diag_classes():
    """Fig. diagnosis left: shift classes per signal (C-DG-shift summary, set L0)."""
    body, anyd = "", False
    for cls, fill in (("crossed", "blue!55"), ("short", "orange!60"), ("unmoved", "black!25"), ("wrong", "red!45")):
        coords = []
        for i, (lab, p) in enumerate(DIAG, 1):
            n = cell("fig-diag", lab, cls, f"run/C-DG-shift/L0/signal={p}/{cls}", seeded=False)[1]
            if n is not None:
                coords.append(f"({n:.1f},{i})")
        anyd = anyd or bool(coords)
        body += r"\addplot[fill=" + fill + ", draw=black!60] coordinates {" + " ".join(coords) + "};\n"
    return body + r"\legend{crossed,short,unmoved,wrong}" + "\n" if anyd else tbd_node(False)


def f_diag_kappa():
    """Fig. diagnosis right: shift ratio kappa per signal (C-DG-shift)."""
    coords = []
    for sym, p in (("Inj", "C-AUD-medprm"), ("8B", "C-AUD-qwen35-9b"), ("32B", "C-AUD-qwen35-27b"),
                   ("Blk", "B-F-verdict-blocks")):
        n = cell("fig-diag-kappa", p, "kappa", f"run/C-DG-shift/L0/signal={p}/kappa", seeded=False)[1]
        if n is not None:
            coords.append(f"({sym},{n:.2f})")
    if not coords:
        return tbd_node(False)
    return r"\addplot[fill=black!45, draw=black!60] coordinates {" + " ".join(coords) + "};\n"


TABLES = [("factorial", t_factorial), ("audit", t_audit), ("main", t_main), ("main-app", t_main_app),
          ("downstream", t_downstream), ("ablation", t_ablation), ("ladder", t_ladder), ("kinds", t_kinds),
          ("shortcuts", t_shortcuts), ("rules", t_rules), ("primary", t_primary), ("seeds", t_seeds),
          ("fig-div", f_div), ("fig-seln", f_seln), ("fig-diag", f_diag_classes), ("fig-diag-kappa", f_diag_kappa)]


# ---------------------------------------------------------------- main
def paper_keys(path):
    if not path or not os.path.exists(path):
        return []
    text = open(path, encoding="utf-8").read()
    text = re.sub(r"(?<!\\)%.*", "", text)              # comments
    return sorted(set(re.findall(r"\\res\{([^{}]+)\}", text)))


def catalog():
    """Every finished run with its sets, slices and numeric fields (to find keys)."""
    for top in TOPS:
        for rid in sorted(os.listdir(os.path.join(ROOT, top)) if os.path.isdir(os.path.join(ROOT, top)) else []):
            r = run(rid)
            if not r:
                continue
            print(f"{rid}  ({top})")
            for s, (f, d) in sorted(r.summaries.items()):
                if not isinstance(d, dict):
                    continue
                top_fields = sorted(k for k, v in d.items() if isinstance(v, (int, float)) and not isinstance(v, bool))
                slices = sorted(k for k, v in d.items() if isinstance(v, dict) and k not in ("CI95", "step", "eval"))
                print(f"  set {s}: slices {', '.join(slices) or '-'}; top-level {', '.join(top_fields) or '-'}")


def main():
    # selrm.metrics.paired_diff iterates a set of triplet ids, whose order depends on the hash
    # seed; a fixed seed makes every interval reproducible (change request to C, 3 Oct).
    if os.environ.get("PYTHONHASHSEED") != "0":      # (os.exec* loses the output on Windows)
        sys.exit(subprocess.run([sys.executable, *sys.argv], env=os.environ | {"PYTHONHASHSEED": "0"}).returncode)
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", default=os.path.join(ROOT, "paper", "latex_v13", "main.tex"))
    ap.add_argument("--out", default=os.path.join(ROOT, "tables"))
    ap.add_argument("--key", action="append", help="print the value and provenance of a key, write nothing")
    ap.add_argument("--catalog", action="store_true", help="list finished runs, sets and fields, write nothing")
    a = ap.parse_args()
    if a.catalog:
        return catalog()
    if a.key:
        for k in a.key:
            n, text, prov = resolve(k)
            print(f"{k} = {text}")
            print("  " + json.dumps(prov, default=str)[:600])
        return
    os.makedirs(a.out, exist_ok=True)
    for name, fn in TABLES:
        body = fn()
        open(os.path.join(a.out, f"{name}.tex"), "w", encoding="utf-8", newline="\n").write(
            f"% generated by scripts/make_tables.py ({name}); do not edit\n" + body)
    keys = paper_keys(a.paper)
    for k in keys:
        resolve(k)
    head = git("rev-parse", "HEAD")
    dirty = bool(git("status", "--porcelain", "--", "results", "results_git", "scripts", "selrm"))
    lines = [f"% generated by scripts/make_tables.py at commit {head[:12]}{' (uncommitted changes)' if dirty else ''}; "
             "do not edit"]
    numbers = {}
    for k in keys:
        n, text, _ = resolve(k)
        numbers[k] = {"value": text, "number": n}
        if n is not None:
            lines.append(r"\resdef{" + k + "}{" + text + "}")
    open(os.path.join(a.out, "numbers.tex"), "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    json.dump(numbers, open(os.path.join(a.out, "numbers.json"), "w", encoding="utf-8", newline="\n"),
              indent=1, sort_keys=True)
    prov = {"generated_by": "scripts/make_tables.py", "code_commit": head, "uncommitted_changes": dirty,
            "records": DATA_PROV, "comparisons": comparisons(),
            "keys": {k: {"value": v[1], "number": v[0], **v[2]} for k, v in sorted(CACHE.items())},
            "tables": CELLS, "warnings": sorted(set(WARN))}
    json.dump(prov, open(os.path.join(a.out, "PROVENANCE.json"), "w", encoding="utf-8", newline="\n"),
              indent=1, default=str)
    n_cells = sum(len(v) for v in CELLS.values())
    n_tbd = sum(c["value"] == TBD for v in CELLS.values() for c in v)
    print(f"{len(TABLES)} tables, {n_cells} cells ({n_cells - n_tbd} measured, {n_tbd} tbd); "
          f"{len(keys)} paper keys ({sum(1 for k in keys if numbers[k]['number'] is not None)} measured)")
    for w in sorted(set(WARN)):
        print("warning:", w)


if __name__ == "__main__":
    main()
