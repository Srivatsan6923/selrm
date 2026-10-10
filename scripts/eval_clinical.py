"""Clinical-set evaluation from per-example scores (owner C). No GPU.
  python scripts/eval_clinical.py trialgpt --split dev|test [--results results_git] [--data scratch/rv1]
  python scripts/eval_clinical.py medeinst [--results results_git]   (every run with MedEinst test scores)
TrialGPT (docs/TRIALGPT_PROTOCOL.md): for every system run found, the acceptance threshold
tau comes from the run's own rule_v1/dev_missing scores (selrm.metrics.mr_threshold, 5%
false rejection); per item NEI if max(u_s, u_s') < tau or u_s = u_s', else met / not met
by the larger score. Writes results_git/<run>/summary_clin_v1~trialgpt_<split>.json
(replacing the triplet summary the GPU job wrote, which is empty for these records) and,
for the test split, docs/TRIALGPT_RESULTS.md. Every number comes from scores files."""
import argparse, collections, json, os, re, statistics, subprocess, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import metrics as M

CATS = ("met", "not_met", "nei")
NAME5 = {("inclusion", "met"): "included", ("inclusion", "not_met"): "not included",
         ("exclusion", "met"): "excluded", ("exclusion", "not_met"): "not excluded"}
SYSTEMS = [  # (name in run ids, row label, format). Test runs: C-TG-<name> for the untrained backbone
    # (mirrors C-TF-<name>), C-TG-<name>-s<k> for B's adapters (mirrors B-F-<name>-s<k>); dev: C-TG-<name>-dev
    ("critic", "Untrained backbone, verdict (critic)", "verdict"),
    ("promptsum", "Untrained backbone, prompted summary", "summary2"),
    ("promptledger", "Untrained backbone, prompted ledger (frozen malformed check)", "ledger2"),
    ("promptledger-lenient", "Untrained backbone, prompted ledger (format-normalised readout)", "ledger2"),
    ("defcorr", "Untrained backbone, default correction", "verdict"),
    ("verdict-blocks", "Verdict only x blocks", "verdict"),
    ("verdict-triplets", "Verdict only x triplets", "verdict"),
    ("summary2-blocks", "Prose summary x blocks", "summary2"),
    ("summary2-triplets", "Prose summary x triplets", "summary2"),
    ("ledger2-blocks", "Ledger x blocks", "ledger2"),
    ("ledger2-triplets", "Ledger x triplets", "ledger2"),
    ("ledger2-balanced", "Ledger x balanced", "ledger2"),
    ("TR-fover", "Verdict only, FoVer data (B-TR-fover)", "verdict"),
    ("TR-clinonly", "Ledger, clinical pairs only (B-TR-clinonly)", "ledger2"),
    ("rationale-triplets", "One-stage rationale x triplets", "rationale"),
    ("ledger2-natural", "Ledger x natural", "ledger2"),
    ("sc-summary2-triplets", "Summary x triplets, judge sees the case (secondary analysis S3)", "summary2"),
]
UNTRAINED = ("critic", "promptsum", "promptledger", "promptledger-lenient", "defcorr")
MALFORMED_U = -20.0     # INTERFACES 3: a malformed ledger scores -20 on both claims
# threshold-source sensitivity: rule_v1/dev_missing scores of the same model from an independent run
ALT_TAU = {"critic": "C-TF-critic", "promptsum": "C-TF-promptsum--p1", "promptledger": "C-TF-promptledger--p1",
           "promptledger-lenient": "C-TF-promptledger-lenient--p1"}   # adapters: B's run B-F-<name>-s<k> (origin/role-b)


def planned_runs():
    out = set()
    for f in os.listdir(f"{REPO}/configs/tasks_c"):
        out |= {r["run_id"] for r in json.load(open(f"{REPO}/configs/tasks_c/{f}", encoding="utf-8"))["runs"]}
    return out


def run_ids(res, name, split, planned=frozenset()):
    """Run ids of a system: every seed that is scored or listed in a task file (so a queued seed prints 'not run')."""
    if split == "dev":
        return [f"C-TG-{name}-dev"]
    if name in UNTRAINED:
        return [f"C-TG-{name}"]
    return [r for r in (f"C-TG-{name}-s{k}" for k in range(5)) if os.path.isdir(f"{res}/{r}") or r in planned] \
        or [f"C-TG-{name}-s0"]
COMPARISONS = [("ledger2-triplets", "critic"), ("ledger2-triplets", "ledger2-blocks")]   # analysis plan (6)


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def scores(path):
    return {r["iid"]: r for r in load_jsonl(path)} if os.path.exists(path) else None


def dataset(data, name):
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    return load_jsonl(f"{data}/{reg[name]['path']}")


# ---------------------------------------------------------------- evidence quotes

def quotes(text, fmt):
    """Quoted spans of a reader output: ledger found values (each line of a multi-line value is its own
    quote, since the note has one sentence per line); double-quoted spans of prose."""
    if fmt == "ledger2":
        out, key = [], None
        for raw in text.split("\n"):
            line = re.sub(r"^(?:[-*•+]|\d+[.)])\s+", "", raw.strip().strip("`").strip()).replace("**", "")
            m = re.match(r"^(need|found|subject|status|time)\s*:\s*(.*)$", line, flags=re.I)
            if m:
                key, v = m.group(1).lower(), m.group(2).strip()
            elif not line:
                key = None
                continue
            else:
                v = line
            if key != "found":
                continue
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1].strip()
            if v and v.lower().rstrip(".") != "not mentioned":
                out.append(v)
        return out
    if fmt == "summary2":
        return [a or b for a, b in re.findall(r'"([^"\n]+)"|“([^”\n]+)”', text)]
    return []


def sentence_ids(note, qs):
    """Numbered note sentences ('<k>. text' per line) holding a verbatim occurrence of a quote that reaches
    past the '<k>. ' label (a quote such as '5' does not match the label of sentence 5)."""
    ids = set()
    for line in note.split("\n"):
        m = re.match(r"^(\d+)\.\s", line)
        for q in qs if m else ():
            start = line.find(q)
            while start >= 0 and start + len(q) <= m.end():
                start = line.find(q, start + 1)
            if start >= 0:
                ids.add(int(m.group(1)))
    return ids


# ---------------------------------------------------------------- one system

def predict(us, usp, tau):
    if max(us, usp) < tau or us == usp:
        return "nei"
    return "met" if us > usp else "not_met"


def evaluate(recs, sc, tau, fmt):
    """-> list of items with gold, prediction and evidence sets."""
    items = {}
    for r in recs:
        it = items.setdefault(r["tid"], {"tid": r["tid"], "patient": r["meta"]["patient_id"], "trial": r["rid"],
                                         "type": r["family"], "gold": r["meta"]["category"], "u": {},
                                         "expert": set(r["meta"]["expert_sentences"]), "note": r["case_text"]})
        s = sc[r["iid"]]
        it["u"][r["claim_role"]] = s["u"]
        if "reader_output" in s:      # a re-judged run's quotes come from the ledger its judge read
            it["reader"] = s.get("ledger_lenient") or s["reader_output"]
    for it in items.values():
        it["pred"] = predict(it["u"]["s"], it["u"]["s_prime"], tau)
        d = it["u"]["s"] - it["u"]["s_prime"]
        it["forced"] = "met" if d > 0 else ("not_met" if d < 0 else "tie")
        it["quoted"] = sentence_ids(it["note"], quotes(it.get("reader", ""), fmt)) if "reader" in it else None
        it["malformed"] = fmt == "ledger2" and it["u"]["s"] == it["u"]["s_prime"] == MALFORMED_U
    return list(items.values())


def macro_f1(xs):
    return M.prf([x["gold"] for x in xs], [x["pred"] for x in xs], CATS)["macroF1"]


def accuracy(xs):
    return M.prf([x["gold"] for x in xs], [x["pred"] for x in xs], CATS)["acc"]


def evidence(items, drop_malformed=False):
    """Micro P/R of quoted vs expert sentences (protocol section 6); None where a denominator is empty.
    drop_malformed: ledgers rejected by the frozen check carry no quotes (sensitivity reading)."""
    if not any(x["quoted"] is not None for x in items):
        return None
    q = lambda x: set() if drop_malformed and x["malformed"] else (x["quoted"] or set())
    pred = [x for x in items if q(x)]
    gold = [x for x in items if x["expert"]]
    n_p, n_g = sum(len(q(x)) for x in pred), sum(len(x["expert"]) for x in gold)
    return {"precision": 100.0 * sum(len(q(x) & x["expert"]) for x in pred) / n_p if n_p else None,
            "n_items_pred": len(pred),
            "recall": 100.0 * sum(len(q(x) & x["expert"]) for x in gold) / n_g if n_g else None,
            "n_items_gold": len(gold), "items_without_quote": sum(not q(x) for x in items)}


def summary(items, tau, run, split):
    main = [x for x in items if x["gold"] != "na"]
    rep = M.prf([x["gold"] for x in main], [x["pred"] for x in main], CATS)
    f1 = M.cluster_bootstrap(main, "patient", macro_f1)
    acc = M.cluster_bootstrap(main, "patient", accuracy)
    five = [x for x in main]
    name5 = lambda x, k: NAME5.get((x["type"], x[k]), "not enough information")
    rep5 = M.prf([name5(x, "gold") for x in five], [name5(x, "pred") for x in five],
                 ["included", "not included", "excluded", "not excluded", "not enough information"])
    bytype = {t: M.prf([x["gold"] for x in main if x["type"] == t], [x["pred"] for x in main if x["type"] == t], CATS)
              for t in ("inclusion", "exclusion")}
    na = collections.Counter(x["pred"] for x in items if x["gold"] == "na")
    fc = [x for x in main if x["gold"] in ("met", "not_met")]
    trials = collections.defaultdict(list)
    for x in main:
        trials[x["trial"]].append(x["gold"] == x["pred"])
    tacc = sorted(100.0 * sum(v) / len(v) for v in trials.values() if len(v) >= 5)   # >= 5 non-N/A items
    return {"run_id": run, "set": f"clin_v1/trialgpt_{split}", "protocol": "docs/TRIALGPT_PROTOCOL.md",
            "threshold": tau, "n_items": len(items), "n_scored": len(main), "n_patients": len({x["patient"] for x in main}),
            "macroF1": rep["macroF1"], "macroF1_CI95": [f1[1], f1[2]], "acc": rep["acc"], "acc_CI95": [acc[1], acc[2]],
            "per_class": rep["per_class"], "confusion": rep["confusion"],
            "pred_distribution": dict(collections.Counter(x["pred"] for x in main)),
            "macroF1_five_names": rep5["macroF1"], "per_class_five_names": rep5["per_class"],
            "by_type": {t: {"macroF1": v["macroF1"], "acc": v["acc"], "n": v["n"]} for t, v in bytype.items()},
            "not_applicable": {"n": sum(na.values()), "pred": dict(na)},
            "forced_choice_acc": 100.0 * sum(x["forced"] == x["gold"] for x in fc) / len(fc) if fc else None,
            "n_forced": len(fc), "evidence": evidence(items),
            "evidence_malformed_without_quotes": evidence(items, True) if any(x["malformed"] for x in items) else None,
            "per_trial_acc": {"n_trials": len(tacc), "min_items": 5, "min": tacc[0] if tacc else None,
                              "median": statistics.median(tacc) if tacc else None, "max": tacc[-1] if tacc else None},
            "bootstrap": {"unit": "patient", "B": 1000, "seed": 0}}


def alt_tau_scores(res, name, seed):
    """(source, dev_missing scores) of the same model from an independent run, or (None, None)."""
    if name in ALT_TAU:
        p = f"{res}/{ALT_TAU[name]}/scores_rule_v1~dev_missing.jsonl"
        return (f"results_git/{ALT_TAU[name]}", scores(p)) if os.path.exists(p) else (None, None)
    src = f"origin/role-b:results_git/B-F-{name}-s{seed or 0}/scores_rule_v1~dev_missing.jsonl"
    p = subprocess.run(["git", "-C", REPO, "show", src], capture_output=True, encoding="utf-8")
    if p.returncode:
        return None, None
    return src, {r["iid"]: r for r in (json.loads(l) for l in p.stdout.splitlines() if l.strip())}


def run_system(recs, dm, split, fmt, run_dir, name=None, seed=None):
    """(items, summary) of one run, or (None, None) if it has no scores for the split yet."""
    sc = scores(f"{run_dir}/scores_clin_v1~trialgpt_{split}.jsonl")
    src = f"{run_dir}/scores_rule_v1~dev_missing.jsonl"
    if not os.path.exists(src) and not re.search(r"-s[1-9]$", run_dir):
        # seed-0 and untrained test runs: tau from the system's dev run (same model, adapter, set and B's scoring
        # code; other runner commit and GPU). Later seeds score rule_v1/dev_missing in their own run.
        src = re.sub(r"-s0$", "", run_dir) + "-dev/scores_rule_v1~dev_missing.jsonl"
    sd = scores(src)
    if sc is not None and sd is None:
        print(f"WARNING {os.path.basename(run_dir)}: test scores but no rule_v1/dev_missing scores for tau ({src})")
    if sc is None or sd is None:
        return None, None
    tau = M.mr_threshold(dm, [sd[r["iid"]]["u"] for r in dm])
    items = evaluate(recs, sc, tau, fmt)
    out = summary(items, tau, os.path.basename(run_dir), split) | {
        "threshold_source": os.path.relpath(src, os.path.dirname(os.path.dirname(run_dir))).replace(os.sep, "/")}
    if split == "test" and name:
        asrc, alt = alt_tau_scores(os.path.dirname(run_dir), name, seed)
        if alt and all(r["iid"] in alt for r in dm):
            atau = M.mr_threshold(dm, [alt[r["iid"]]["u"] for r in dm])
            main = [x | {"pred": predict(x["u"]["s"], x["u"]["s_prime"], atau)} for x in items if x["gold"] != "na"]
            out["threshold_alt"] = {"source": asrc, "tau": atau, "macroF1": macro_f1(main), "acc": accuracy(main)}
    return items, out


def fmt_num(x, nd=1):
    return "-" if x is None else f"{x:.{nd}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["trialgpt", "medeinst", "keypairs", "nli4ct", "medeinst_neg"])
    ap.add_argument("--split", default="dev", choices=["dev", "test"])
    ap.add_argument("--results", default=f"{REPO}/results_git")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--data-c", default=f"{REPO}/data", help="C's sets (clin_v1/...)")
    a = ap.parse_args()
    if a.dataset == "medeinst":
        return medeinst(a)
    if a.dataset == "keypairs":
        return keypairs(a)
    if a.dataset == "medeinst_neg":
        return medeinst_neg(a)
    if a.dataset == "nli4ct":
        return nli4ct(a)
    recs = load_jsonl(f"{REPO}/data/clin_v1/trialgpt_{a.split}/records.jsonl")
    dm = dataset(a.data, "rule_v1/dev_missing")
    rows, items_by, planned = [], {}, planned_runs()
    for name, label, fmt, run in [(n, l, f, r) for n, l, f in SYSTEMS for r in run_ids(a.results, n, a.split, planned)]:
        seed = run.rsplit("-s", 1)[1] if run[-3:-1] == "-s" else None
        items, summ = run_system(recs, dm, a.split, fmt, f"{a.results}/{run}", name, seed)
        key = name + (f"@s{seed}" if seed not in (None, "0") else "")
        rows.append((key, label + (f", seed {seed}" if seed else ""), run, summ))
        if summ is None:
            continue
        items_by[key] = items
        out = f"{a.results}/{run}/summary_clin_v1~trialgpt_{a.split}.json"
        old = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
        summ["eval"] = old.get("eval")
        json.dump(summ, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
        print(f"{key:24s} macroF1 {summ['macroF1']:.1f} [{summ['macroF1_CI95'][0]:.1f}, {summ['macroF1_CI95'][1]:.1f}]"
              f" acc {summ['acc']:.1f} tau {summ['threshold']:.3f} pred {summ['pred_distribution']}")
    comps = []
    for x, y in COMPARISONS:
        if x in items_by and y in items_by:
            bx = {i["tid"]: i for i in items_by[x] if i["gold"] != "na"}
            by = {i["tid"]: i for i in items_by[y] if i["gold"] != "na"}
            pairs = [{"patient": bx[t]["patient"], "a": bx[t], "b": by[t]} for t in sorted(bx.keys() & by.keys())]
            res = M.paired_cluster_bootstrap(pairs, "patient", lambda ps: macro_f1([p["a"] for p in ps]),
                                             lambda ps: macro_f1([p["b"] for p in ps]))
            comps.append((x, y, res))
            print(f"paired macroF1 {x} - {y}: {res['diff']:.1f} [{res['lo']:.1f}, {res['hi']:.1f}] p={res['p']:.3f}")
    if comps:
        json.dump({f"{x} - {y}": r for x, y, r in comps},
                  open(f"{a.results}/C-TG-comparisons_{a.split}.json", "w", encoding="utf-8", newline="\n"), indent=1)
    if a.split == "test":
        write_report(rows, comps)


# ---------------------------------------------------------------- MedEinst

ME_SET = "clin_v1/medeinst_test"
ME_POST_HOC = {"C-ME-ledger2-triplets-s0-lenient"}   # decided after the primary result (DECISIONS_C 3 Oct)
ME_COMPARISONS = [("ledger2-triplets-s0", "critic"), ("ledger2-triplets-s0", "summary2-triplets-s0")]   # plan (4), (5)


def me_pairs(recs, sc):
    """One item per pair: d on the control (base) and on the trap (flip); flags from the records. Pairs a run did
    not score (fixed subsets of the generative PRMs) are left out; a partly scored pair raises."""
    P = {}
    for r in recs:
        if r["iid"] not in sc:
            continue
        p = P.setdefault(r["tid"], {"tid": r["tid"], "labels": r["rid"], "u": {}, "flags": r["meta"]})
        p["u"][(r["case_kind"], r["claim_role"])] = sc[r["iid"]]["u"]
    out = []
    for p in P.values():
        u = p["u"]
        dc, dt = u[("base", "s")] - u[("base", "s_prime")], u[("flip", "s")] - u[("flip", "s_prime")]
        out.append({"tid": p["tid"], "labels": p["labels"], "control": dc > 0, "trap": dt < 0, "tie": dc == 0 or dt == 0,
                    "trapped": dc > 0 and dt > 0, "no_diff": p["flags"].get("no_content_diff", False),
                    "overlap": p["flags"].get("overlap_ref", False), "meta": p["flags"]})
    return out


KP_SETS = ("clin_v1/keypairs_medqa", "clin_v1/keypairs_careqa", "clin_v1/keypairs_medqa_oneway",
           "clin_v1/keypairs_careqa_oneway")


def keypairs(a):
    """Key pairs: reversal = each question preferred with its own key (ties fail); by stem-similarity tercile
    and by category of the first question; bootstrap over pairs."""
    L = ["# Key pairs: results (role C)", "",
         "Generated by `scripts/eval_clinical.py keypairs` from `results_git/*/scores_clin_v1~keypairs_*.jsonl` (no typed "
         "numbers). Definitions and yields: `data/clin_v1/keypairs_*/MANIFEST.json`; the v13 definition gives very few "
         "pairs (see docs/DECISIONS_C.md).", ""]
    for set_name in KP_SETS:
        recs = load_jsonl(f"{a.data_c}/{set_name}/records.jsonl")
        L += [f"## {set_name}", "", "| run | Reversal [95% CI] | n | q1 correct | q2 correct | ties | by tercile 1/2/3 |",
              "|---|---|---|---|---|---|---|"]
        for d in sorted(os.listdir(a.results)):
            f = f"{a.results}/{d}/scores_{set_name.replace('/', '~')}.jsonl"
            if not os.path.exists(f) or not os.path.exists(f"{a.results}/{d}/DONE"):
                continue
            items = me_pairs(recs, scores(f))
            rv = M.cluster_bootstrap(items, "tid", reversal)
            terc = {t: reversal(v) for t in (1, 2, 3) if (v := [x for x in items if x["meta"]["tercile"] == t])}
            cats = collections.defaultdict(list)
            for x in items:
                cats[str(x["meta"]["category"][0])].append(x)
            summ = {"run_id": d, "set": set_name, "Reversal": rv[0], "CI95": [rv[1], rv[2]], "n_pairs": len(items),
                    "q1_acc": pct(items, "control"), "q2_acc": pct(items, "trap"), "tie_rate": pct(items, "tie"),
                    "Reversal_by_tercile": terc, "Reversal_by_category": {k: reversal(v) for k, v in sorted(cats.items())},
                    "n_by_category": {k: len(v) for k, v in sorted(cats.items())},
                    "bootstrap": {"unit": "pair", "B": 1000, "seed": 0}}
            out = f"{a.results}/{d}/summary_{set_name.replace('/', '~')}.json"
            old = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
            summ["eval"] = old.get("eval")
            json.dump(summ, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
            L.append(f"| {d} | {rv[0]:.1f} [{rv[1]:.1f}, {rv[2]:.1f}] | {len(items)} | {summ['q1_acc']:.1f} | "
                     f"{summ['q2_acc']:.1f} | {summ['tie_rate']:.1f} | " + " / ".join(f"{terc.get(t, float('nan')):.1f}" for t in (1, 2, 3)) + " |")
            print(set_name, d, f"Reversal {rv[0]:.1f} [{rv[1]:.1f}, {rv[2]:.1f}] n={len(items)}")
        L.append("")
    open(f"{REPO}/docs/KEYPAIRS_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/KEYPAIRS_RESULTS.md")


def pct(xs, key):
    return 100.0 * sum(x[key] for x in xs) / len(xs)


def reversal(xs):
    return 100.0 * sum(x["control"] and x["trap"] for x in xs) / len(xs)


def me_summary(items, run):
    ctrl = [x for x in items if x["control"]]
    rv = M.cluster_bootstrap(items, "tid", reversal)
    rv_lab = M.cluster_bootstrap(items, "labels", reversal)
    sub = lambda f: [x for x in items if f(x)]
    return {"run_id": run, "set": ME_SET, "Reversal": rv[0], "CI95": [rv[1], rv[2]], "CI95_label_pairs": [rv_lab[1], rv_lab[2]],
            "n_pairs": len(items), "control_acc": pct(items, "control"), "trap_acc": pct(items, "trap"),
            "bias_trap_rate": 100.0 * sum(x["trapped"] for x in ctrl) / len(ctrl) if ctrl else None,
            "n_control_correct": len(ctrl), "tie_rate": pct(items, "tie"),
            "Reversal_excl_no_content_diff": reversal(sub(lambda x: not x["no_diff"])),
            "Reversal_excl_overlap_ref": reversal(sub(lambda x: not x["overlap"])),
            "n_no_content_diff": sum(x["no_diff"] for x in items), "n_overlap_ref": sum(x["overlap"] for x in items),
            "definitions": "control correct: d(control) > 0; trap correct: d(trap) < 0; Reversal = both (ties fail); "
                           "bias_trap_rate = share of control-correct pairs with d(trap) > 0 (MedEinst's R_bias on two candidates)",
            "bootstrap": {"unit": "pair (CI95) and (y_gt, y_bias) label pair (CI95_label_pairs)", "B": 1000, "seed": 0}}


def medeinst(a):
    recs = load_jsonl(f"{a.data_c}/clin_v1/medeinst_test/records.jsonl")
    rows, items_by = [], {}
    for d in sorted(os.listdir(a.results)):
        f = f"{a.results}/{d}/scores_{ME_SET.replace('/', '~')}.jsonl"
        if not os.path.exists(f) or not os.path.exists(f"{a.results}/{d}/DONE"):
            continue
        items = me_pairs(recs, scores(f))
        s = me_summary(items, d)
        out = f"{a.results}/{d}/summary_{ME_SET.replace('/', '~')}.json"
        old = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
        s["eval"] = old.get("eval")
        json.dump(s, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
        items_by[d.replace("C-ME-", "")] = items
        rows.append((d, s))
        print(f"{d:28s} Reversal {s['Reversal']:.1f} [{s['CI95'][0]:.1f}, {s['CI95'][1]:.1f}] control {s['control_acc']:.1f} "
              f"trap {s['trap_acc']:.1f} bias-trap {s['bias_trap_rate'] or float('nan'):.1f} ties {s['tie_rate']:.1f}")
    comps = []
    for x, y in ME_COMPARISONS:
        if x in items_by and y in items_by:
            bx, by = {i["tid"]: i for i in items_by[x]}, {i["tid"]: i for i in items_by[y]}
            pairs = [{"tid": t, "labels": bx[t]["labels"], "a": bx[t], "b": by[t]} for t in sorted(bx.keys() & by.keys())]
            stats = (lambda ps: reversal([p["a"] for p in ps]), lambda ps: reversal([p["b"] for p in ps]))
            r = M.paired_cluster_bootstrap(pairs, "tid", *stats)
            # pairs sharing (y_gt, y_bias) are correlated: the same comparison with label pairs as clusters
            r["label_pairs"] = {k: v for k, v in M.paired_cluster_bootstrap(pairs, "labels", *stats).items()
                                if k in ("lo", "hi", "p", "n_clusters", "B")}
            comps.append((x, y, r))
            print(f"paired Reversal {x} - {y}: {r['diff']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}] p={r['p']:.3f}; label pairs "
                  f"[{r['label_pairs']['lo']:.1f}, {r['label_pairs']['hi']:.1f}] p={r['label_pairs']['p']:.3f}")
    if comps:
        json.dump({f"{x} - {y}": r for x, y, r in comps},
                  open(f"{a.results}/C-ME-comparisons.json", "w", encoding="utf-8", newline="\n"), indent=1)
    L = ["# MedEinst test pairs: results (role C)", "",
         "Generated by `scripts/eval_clinical.py medeinst` from `results_git/*/scores_clin_v1~medeinst_test.jsonl` "
         "(no typed numbers). Two candidate diagnoses per pair (control y_gt, trap y_bias); see "
         "`data/clin_v1/medeinst_test/MANIFEST.json` for the release, normalisation and flags. Pairs that share their "
         "two diagnoses are correlated, so the CI over (y_gt, y_bias) label pairs is the conservative one.",
         "", "Validation of the release as its authors report it (MedEinst paper, Sec. 3.4, checked 3 Oct 2026; their "
         "numbers, not ours): four physicians reviewed a stratified sample of 1,500 pairs, 96.1% were judged valid, "
         "Fleiss' kappa 0.79.", "",
         "| run | Reversal [95% CI pairs] | CI label pairs | control acc | trap acc | bias-trap rate | ties | excl. no-diff | excl. overlap |",
         "|---|---|---|---|---|---|---|---|---|"]
    for d, s in rows:
        tag = " (POST HOC re-read with the format-normalised readout; not a primary row)" if d in ME_POST_HOC else \
              " (secondary analysis S3: judge sees the case)" if d.startswith("C-ME-sc-") else ""
        L.append(f"| {d}{tag} | {s['Reversal']:.1f} [{s['CI95'][0]:.1f}, {s['CI95'][1]:.1f}] | [{s['CI95_label_pairs'][0]:.1f}, "
                 f"{s['CI95_label_pairs'][1]:.1f}] | {s['control_acc']:.1f} | {s['trap_acc']:.1f} | "
                 f"{fmt_num(s['bias_trap_rate'])} | {s['tie_rate']:.1f} | {s['Reversal_excl_no_content_diff']:.1f} | "
                 f"{s['Reversal_excl_overlap_ref']:.1f} |")
    if comps:
        L += ["", "Planned comparisons (4), (5): paired differences in Reversal on the same pairs, 1,000 resamples; "
                  "clusters = pairs, and = (y_gt, y_bias) label pairs (the interval for inference):", ""]
        L += [f"- {x} minus {y}: {r['diff']:.1f}; pairs [{r['lo']:.1f}, {r['hi']:.1f}], p = {r['p']:.3f}; label pairs "
              f"[{r['label_pairs']['lo']:.1f}, {r['label_pairs']['hi']:.1f}], p = {r['label_pairs']['p']:.3f} "
              f"({r['n_items']} pairs, {r['label_pairs']['n_clusters']} label pairs)" for x, y, r in comps]
    open(f"{REPO}/docs/MEDEINST_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/MEDEINST_RESULTS.md")


# ---------------------------------------------------------------- NLI4CT-P

NLI_SETS = ("clin_v1/nli4ct_test", "clin_v1/nli4ct_dev")


def nli_metrics(recs, pred):
    """The SemEval-2024 Task 2 scorer's definitions (ai-systems/Task-2-SemEval-2024, evaluate.py; data 267230cc,
    scorer HEAD 7f32fa6c whose consistency follows paper Eq. 2 and the 2025 erratum; HEAD's call sites crash, so
    the formulas are reproduced here). pred: {uuid: 'Entailment'|'Contradiction'}. F1 = binary F1 of the
    Entailment class (the scorer's sklearn default), macro-F1 alongside.
    Faithfulness: altering items, Prediction(x) != gold Label(original). Consistency: preserving items,
    Prediction(x) == Prediction(original) (HEAD, Eq. 2); consistency_acc: Prediction(x) == gold Label(x) (267230cc)."""
    gold = {r["meta"]["uuid"]: r["meta"]["label_name"] for r in recs}
    meta = {r["meta"]["uuid"]: r["meta"] for r in recs}
    def f1(ids, positive="Entailment"):
        g = [gold[i] == positive for i in ids]
        p = [pred[i] == positive for i in ids]
        tp = sum(a and b for a, b in zip(g, p))
        prec = tp / sum(p) if sum(p) else 0.0
        rec = tp / sum(g) if sum(g) else 0.0
        return 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    ctrl = [u for u, m in meta.items() if m["causal_type"] is None]
    contrast = [u for u, m in meta.items() if m["causal_type"] is not None]
    alter = [u for u in contrast if meta[u]["causal_type"] == "Altering"]
    keep = [u for u in contrast if meta[u]["causal_type"] == "Preserving"]
    out = {"Control_F1": f1(ctrl), "Control_macroF1": (f1(ctrl) + f1(ctrl, "Contradiction")) / 2,
           "Contrast_F1": f1(contrast),
           "Faithfulness": sum(pred[u] != gold[meta[u]["original_uuid"]] for u in alter) / len(alter) if alter else None,
           "Consistency": sum(pred[u] == pred[meta[u]["original_uuid"]] for u in keep) / len(keep) if keep else None,
           "Consistency_acc": sum(pred[u] == gold[u] for u in keep) / len(keep) if keep else None,
           "n_control": len(ctrl), "n_altering": len(alter), "n_preserving": len(keep)}
    for iv in sorted({meta[u]["intervention"] for u in contrast}):
        ids = [u for u in contrast if meta[u]["intervention"] == iv]
        out[f"acc_{iv}"] = sum(pred[u] == gold[u] for u in ids) / len(ids)
    out["Average"] = (out["Control_F1"] + (out["Faithfulness"] or 0) + (out["Consistency"] or 0)) / 3
    return out


def medeinst_neg(a):
    """Hold on denied evidence (docs/AUX_PROTOCOL.md S2, S3; secondary): d = u(s) - u(s') > 0 on clin_v1/medeinst_neg,
    with and without items whose denied line names a diagnosis; CI over (y_gt, y_bias) label pairs. Joined with the
    same system's MedEinst scores (run C-MN-<x> -> C-ME-<x>, or the same run) for pairs right on all three cases."""
    recs = load_jsonl(f"{a.data_c}/clin_v1/medeinst_neg/records.jsonl")
    me_recs = load_jsonl(f"{a.data_c}/clin_v1/medeinst_test/records.jsonl")
    L = ["# MedEinst with denied evidence (secondary analysis, specified after the planned comparisons)", "",
         "Generated by `scripts/eval_clinical.py medeinst_neg` (no typed numbers). Set clin_v1/medeinst_neg "
         "(docs/AUX_PROTOCOL.md S2): the control case plus one line denying the trap's distinguishing finding; hold = "
         "control diagnosis still preferred (ties fail). CI: bootstrap over (y_gt, y_bias) label pairs (1,000).", "",
         "| run | hold [95% CI] | hold, no diagnosis named | n | control, trap and denial all right | n pairs |",
         "|---|---|---|---|---|---|"]
    for d in sorted(os.listdir(a.results)):
        f = f"{a.results}/{d}/scores_clin_v1~medeinst_neg.jsonl"
        if not os.path.exists(f) or not os.path.exists(f"{a.results}/{d}/DONE"):
            continue
        sc = scores(f)
        items = {}
        for r in recs:
            if r["iid"] in sc:
                it = items.setdefault(r["tid"], {"cl": (r["meta"]["y_gt"], r["meta"]["y_bias"]), "src": r["meta"]["source_tid"],
                                                 "named": r["meta"]["diagnosis_named"], "u": {}})
                it["u"][r["claim_role"]] = sc[r["iid"]]["u"]
        xs = [{"cl": x["cl"], "src": x["src"], "named": x["named"], "ok": x["u"]["s"] - x["u"]["s_prime"] > 0} for x in items.values()]
        hold = lambda v: 100.0 * sum(x["ok"] for x in v) / len(v)
        h = M.cluster_bootstrap(xs, "cl", hold)
        un = [x for x in xs if not x["named"]]
        me_run = d.replace("C-MN-", "C-ME-", 1)
        mf = f"{a.results}/{me_run}/scores_{ME_SET.replace('/', '~')}.jsonl"
        joint = None
        if os.path.exists(mf):
            pairs = {p["tid"]: p for p in me_pairs(me_recs, scores(mf))}
            j = [x["ok"] and pairs[x["src"]]["control"] and pairs[x["src"]]["trap"] for x in xs if x["src"] in pairs]
            joint = (100.0 * sum(j) / len(j), len(j)) if j else None
        summ = {"run_id": d, "set": "clin_v1/medeinst_neg", "analysis": "secondary (docs/AUX_PROTOCOL.md S2/S3)",
                "hold": h[0], "CI95": [h[1], h[2]], "n": len(xs), "hold_without_diagnosis_named": hold(un) if un else None,
                "n_without_diagnosis_named": len(un), "all_three_right": joint[0] if joint else None,
                "all_three_right_n": joint[1] if joint else None, "medeinst_run": me_run if joint else None,
                "bootstrap": {"unit": "(y_gt, y_bias) label pair", "B": 1000, "seed": 0}}
        out = f"{a.results}/{d}/summary_clin_v1~medeinst_neg.json"
        old = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
        summ["eval"] = old.get("eval")
        json.dump(summ, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
        tag = " (S3: judge sees the case)" if "-sc-" in d else ""
        L.append(f"| {d}{tag} | {fmt_num(h[0])} [{fmt_num(h[1])}, {fmt_num(h[2])}] | {fmt_num(summ['hold_without_diagnosis_named'])} | "
                 f"{len(xs)} | {fmt_num(joint[0]) if joint else '-'} | {joint[1] if joint else '-'} |")
        print(d, f"hold {h[0]:.1f} [{h[1]:.1f}, {h[2]:.1f}] n={len(xs)}", "all three" if joint else "", f"{joint[0]:.1f}" if joint else "")
    open(f"{REPO}/docs/MEDEINST_NEG_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/MEDEINST_NEG_RESULTS.md")


def nli4ct(a):
    L = ["# NLI4CT-P: results (role C)", "",
         "Generated by `scripts/eval_clinical.py nli4ct` (no typed numbers). Entailment iff u > 0 (fixed before scoring). "
         "Definitions: the task scorer's (binary Entailment F1; faithfulness on altering, consistency on preserving "
         "items; Average = mean of F1, faithfulness, consistency). Fractions, as the task reports them.", ""]
    for set_name in NLI_SETS:
        p = f"{a.data_c}/{set_name}/records.jsonl"
        if not os.path.exists(p):
            continue
        recs = load_jsonl(p)
        elig = [r for r in recs if r["meta"]["section"] == "Eligibility"]
        E = ["", f"### {set_name}: statements about the Eligibility section", "",
             "| run | Control F1 | Faithfulness | Consistency | Average | n control / altering / preserving |", "|---|---|---|---|---|---|"]
        L += [f"## {set_name}", "", "| run | Control F1 | macro-F1 | Faithfulness | Consistency | Consistency (acc.) | Contrast F1 | Average |",
              "|---|---|---|---|---|---|---|---|"]
        for d in sorted(os.listdir(a.results)):
            f = f"{a.results}/{d}/scores_{set_name.replace('/', '~')}.jsonl"
            if not os.path.exists(f) or not os.path.exists(f"{a.results}/{d}/DONE"):
                continue
            sc = scores(f)
            pred = {r["meta"]["uuid"]: "Entailment" if sc[r["iid"]]["u"] > 0 else "Contradiction" for r in recs}
            m = nli_metrics(recs, pred)
            summ = {"run_id": d, "set": set_name, "prediction_rule": "Entailment iff u > 0", "macroF1": m["Control_macroF1"],
                    "faithfulness": m["Faithfulness"], "consistency": m["Consistency"]} | m
            me = nli_metrics(elig, pred)          # eligibility-section slice (plan, secondary 12)
            summ["section=Eligibility"] = {k: me[k] for k in ("Control_F1", "Faithfulness", "Consistency", "Average",
                                                              "n_control", "n_altering", "n_preserving")}
            E.append(f"| {d} | {me['Control_F1']:.3f} | {me['Faithfulness']:.3f} | {me['Consistency']:.3f} | {me['Average']:.3f} | "
                     f"{me['n_control']} / {me['n_altering']} / {me['n_preserving']} |")
            out = f"{a.results}/{d}/summary_{set_name.replace('/', '~')}.json"
            old = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
            summ["eval"] = old.get("eval")
            json.dump(summ, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
            L.append(f"| {d} | {m['Control_F1']:.3f} | {m['Control_macroF1']:.3f} | {m['Faithfulness']:.3f} | "
                     f"{m['Consistency']:.3f} | {m['Consistency_acc']:.3f} | {m['Contrast_F1']:.3f} | {m['Average']:.3f} |")
            print(set_name, d, {k: round(v, 3) for k, v in m.items() if isinstance(v, float)})
        L += E + [""]
    open(f"{REPO}/docs/NLI4CT_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/NLI4CT_RESULTS.md")


def write_report(rows, comps):
    done = [s for _, _, _, s in rows if s]
    npat = sorted({s["n_patients"] for s in done})
    L = ["# TrialGPT criterion annotations: results (role C)", "",
         "Generated by `scripts/eval_clinical.py trialgpt --split test` from `results_git/C-TG-*/` (no typed numbers).",
         f"Protocol: `docs/TRIALGPT_PROTOCOL.md`. Test portion: {'/'.join(map(str, npat))} patients; N/A items "
         "reported separately. Evidence P / R: protocol section 6; a multi-line `found` value gives one quote per "
         "line; a quote must reach past a sentence's number label.", "",
         "| System | run | macro-F1 [95% CI] | accuracy [95% CI] | F1 met | F1 not met | F1 NEI | NEI predicted | forced choice | evidence P / R | tau |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for key, label, run, s in rows:
        if s is None:
            L.append(f"| {label} | {run} | not run | | | | | | | | |")
            continue
        pc, ev = s["per_class"], s["evidence"]
        L.append(f"| {label} | {run} | {fmt_num(s['macroF1'])} [{fmt_num(s['macroF1_CI95'][0])}, {fmt_num(s['macroF1_CI95'][1])}]"
                 f" | {fmt_num(s['acc'])} [{fmt_num(s['acc_CI95'][0])}, {fmt_num(s['acc_CI95'][1])}]"
                 f" | {fmt_num(pc['met']['F1'])} | {fmt_num(pc['not_met']['F1'])} | {fmt_num(pc['nei']['F1'])}"
                 f" | {s['pred_distribution'].get('nei', 0)} of {s['n_scored']} | {fmt_num(s['forced_choice_acc'])}"
                 f" | {(fmt_num(ev['precision']) + ' / ' + fmt_num(ev['recall'])) if ev else '-'} | {fmt_num(s['threshold'], 2)} |")
    if comps:
        L += ["", f"Paired differences in macro-F1 (same items, patient bootstrap, {comps[0][2]['B']:,} resamples; comparison (6) of the "
                  "analysis plan; Holm across the primary comparisons is applied by the lead):", ""]
        L += [f"- {x} minus {y}: {r['diff']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}], p = {r['p']:.3f} "
              f"({r['n_items']} items, {r['n_clusters']} patients)" for x, y, r in comps]
    seeds = collections.defaultdict(dict)
    for key, _, run, s in rows:
        if s and key.split("@")[0] not in UNTRAINED:
            seeds[key.split("@")[0]][run.rsplit("-s", 1)[1]] = s
    multi = {k: v for k, v in seeds.items() if len(v) > 1}
    if multi:
        L += ["", "Seeds (protocol section 8): macro-F1 per seed, mean and s.d. (n - 1):", "",
              "| System | macro-F1 by seed | mean | s.d. | accuracy mean | accuracy s.d. |", "|---|---|---|---|---|---|"]
        for k, v in multi.items():
            f1, ac = M.seed_table({sd: s["macroF1"] for sd, s in v.items()}), M.seed_table({sd: s["acc"] for sd, s in v.items()})
            L.append(f"| {k} | {', '.join(f's{sd} {fmt_num(x)}' for sd, x in f1['seeds'].items())} | {fmt_num(f1['mean'])} | "
                     f"{fmt_num(f1['sd'])} | {fmt_num(ac['mean'])} | {fmt_num(ac['sd'])} |")
    L += ["", "Threshold-source sensitivity: tau and macro-F1 with tau computed from the same model's rule_v1/dev_missing "
              "scores in an independent run (adapters: B's evaluation run of the adapter; untrained backbone: role C's "
              "rule-tier run), against the reported tau (from the system's TrialGPT development run; seeds 1+ from "
              "their own run). Evidence P / R with malformed ledgers carrying no quotes (frozen check; ledger rows):", "",
          "| System | run | tau reported | tau alternative | macro-F1 reported | macro-F1 at alternative tau | accuracy at alternative tau | alternative source | evidence P / R, malformed without quotes |",
          "|---|---|---|---|---|---|---|---|---|"]
    for key, label, run, s in rows:
        if s is None:
            continue
        t, em = s.get("threshold_alt") or {}, s.get("evidence_malformed_without_quotes")
        L.append(f"| {label} | {run} | {fmt_num(s['threshold'], 3)} | {fmt_num(t.get('tau'), 3)} | {fmt_num(s['macroF1'])} | "
                 f"{fmt_num(t.get('macroF1'))} | {fmt_num(t.get('acc'))} | {t.get('source', 'not available').split('/scores_')[0]} | "
                 f"{(fmt_num(em['precision']) + ' / ' + fmt_num(em['recall'])) if em else '-'} |")
    L += ["", "By criterion type, the dataset's five category names, predictions on not-applicable items, per-trial "
              "accuracy (trials with at least 5 non-N/A items) and decision language in reader outputs "
              "(scripts/reader_audit.py):", "",
          "| System | macro-F1 inclusion (n) | macro-F1 exclusion (n) | macro-F1, five names | N/A items: predicted | per-trial acc. min / median / max | decision language |",
          "|---|---|---|---|---|---|---|"]
    for key, label, run, s in rows:
        if s is None:
            continue
        bt, pt = s["by_type"], s["per_trial_acc"]
        aud = f"{REPO}/results_git/{run}/reader_audit.json"
        dl = json.load(open(aud, encoding="utf-8"))["sets"].get(s["set"], {}).get("decision_language_any") if os.path.exists(aud) else None
        L.append(f"| {label} | {fmt_num(bt['inclusion']['macroF1'])} ({bt['inclusion']['n']}) | "
                 f"{fmt_num(bt['exclusion']['macroF1'])} ({bt['exclusion']['n']}) | {fmt_num(s['macroF1_five_names'])} | "
                 f"{', '.join(f'{k} {v}' for k, v in sorted(s['not_applicable']['pred'].items()))} | "
                 f"{fmt_num(pt['min'])} / {fmt_num(pt['median'])} / {fmt_num(pt['max'])} | {fmt_num(dl)} |")
    man = json.load(open(f"{REPO}/data/clin_v1/trialgpt_test/MANIFEST.json", encoding="utf-8"))
    dev = {r["meta"]["patient_id"] for r in load_jsonl(f"{REPO}/data/clin_v1/trialgpt_dev/records.jsonl")}
    L += ["", "Case-blind predictors on the same items (shortcut validation in the set's MANIFEST): " +
          "; ".join(f"{k}: macro-F1 {v['macroF1']:.1f}, accuracy {v['acc']:.1f}" for k, v in man["shortcut_validation"]["predictors"].items()) + ".",
          "", f"Development-portion numbers ({len(dev)} patients) are in results_git/C-TG-*-dev and are not test results."]
    open(f"{REPO}/docs/TRIALGPT_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/TRIALGPT_RESULTS.md")


if __name__ == "__main__":
    main()
