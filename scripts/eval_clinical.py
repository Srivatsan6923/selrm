"""Clinical-set evaluation from per-example scores (owner C). No GPU.
  python scripts/eval_clinical.py trialgpt --split dev|test [--results results_git] [--data scratch/rv1]
  python scripts/eval_clinical.py medeinst [--results results_git]   (every run with MedEinst test scores)
TrialGPT (docs/TRIALGPT_PROTOCOL.md): for every system run found, the acceptance threshold
tau comes from the run's own rule_v1/dev_missing scores (selrm.metrics.mr_threshold, 5%
false rejection); per item NEI if max(u_s, u_s') < tau or u_s = u_s', else met / not met
by the larger score. Writes results_git/<run>/summary_clin_v1~trialgpt_<split>.json
(replacing the triplet summary the GPU job wrote, which is empty for these records) and,
for the test split, docs/TRIALGPT_RESULTS.md. Every number comes from scores files."""
import argparse, collections, json, os, re, statistics, sys

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
    ("verdict-blocks", "Verdict only x blocks", "verdict"),
    ("verdict-triplets", "Verdict only x triplets", "verdict"),
    ("summary2-blocks", "Prose summary x blocks", "summary2"),
    ("summary2-triplets", "Prose summary x triplets", "summary2"),
    ("ledger2-blocks", "Ledger x blocks", "ledger2"),
    ("ledger2-triplets", "Ledger x triplets", "ledger2"),
]
UNTRAINED = ("critic", "promptsum", "promptledger", "promptledger-lenient")


def run_ids(res, name, split):
    if split == "dev":
        return [f"C-TG-{name}-dev"]
    if name in UNTRAINED:
        return [f"C-TG-{name}"]
    return [f"C-TG-{name}-s{k}" for k in range(5) if os.path.isdir(f"{res}/C-TG-{name}-s{k}")] or [f"C-TG-{name}-s0"]
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

def note_sentences(note):
    """{sentence id: (start, end)} of a released note ('<k>. text' per line)."""
    out, pos = {}, 0
    for line in note.split("\n"):
        m = re.match(r"^(\d+)\.\s", line)
        if m:
            out[int(m.group(1))] = (pos, pos + len(line))
        pos += len(line) + 1
    return out


def quotes(text, fmt):
    """Quoted spans of a reader output: ledger found values; double-quoted spans of prose."""
    if fmt == "ledger2":
        out = []
        for raw in text.split("\n"):
            line = re.sub(r"^(?:[-*•+]|\d+[.)])\s+", "", raw.strip().strip("`").strip()).replace("**", "")
            m = re.match(r"^found\s*:\s*(.*)$", line, flags=re.I)
            if m:
                v = m.group(1).strip()
                if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                    v = v[1:-1].strip()
                if v and v.lower().rstrip(".") != "not mentioned":
                    out.append(v)
        return out
    if fmt == "summary2":
        return [a or b for a, b in re.findall(r'"([^"\n]+)"|“([^”\n]+)”', text)]
    return []


def sentence_ids(note, qs):
    """Numbered sentences overlapping any verbatim occurrence of a quote."""
    spans, ids = note_sentences(note), set()
    for q in qs:
        start = note.find(q)
        while start >= 0:
            end = start + len(q)
            ids |= {k for k, (a, b) in spans.items() if a < end and start < b}
            start = note.find(q, start + 1)
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
    return list(items.values())


def macro_f1(xs):
    return M.prf([x["gold"] for x in xs], [x["pred"] for x in xs], CATS)["macroF1"]


def accuracy(xs):
    return M.prf([x["gold"] for x in xs], [x["pred"] for x in xs], CATS)["acc"]


def evidence(items):
    pred = [x for x in items if x["quoted"]]
    gold = [x for x in items if x["expert"]]
    if not any(x["quoted"] is not None for x in items):
        return None
    hit_p = sum(len(x["quoted"] & x["expert"]) for x in pred)
    hit_r = sum(len((x["quoted"] or set()) & x["expert"]) for x in gold)
    return {"precision": 100.0 * hit_p / max(1, sum(len(x["quoted"]) for x in pred)), "n_items_pred": len(pred),
            "recall": 100.0 * hit_r / max(1, sum(len(x["expert"]) for x in gold)), "n_items_gold": len(gold),
            "items_without_quote": sum(not x["quoted"] for x in items)}


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
    tacc = sorted(100.0 * sum(v) / len(v) for v in trials.values() if len(v) >= 5)
    return {"run_id": run, "set": f"clin_v1/trialgpt_{split}", "protocol": "docs/TRIALGPT_PROTOCOL.md",
            "threshold": tau, "n_items": len(items), "n_scored": len(main),
            "macroF1": rep["macroF1"], "macroF1_CI95": [f1[1], f1[2]], "acc": rep["acc"], "acc_CI95": [acc[1], acc[2]],
            "per_class": rep["per_class"], "confusion": rep["confusion"],
            "pred_distribution": dict(collections.Counter(x["pred"] for x in main)),
            "macroF1_five_names": rep5["macroF1"], "per_class_five_names": rep5["per_class"],
            "by_type": {t: {"macroF1": v["macroF1"], "acc": v["acc"], "n": v["n"]} for t, v in bytype.items()},
            "not_applicable": {"n": sum(na.values()), "pred": dict(na)},
            "forced_choice_acc": 100.0 * sum(x["forced"] == x["gold"] for x in fc) / len(fc) if fc else None,
            "n_forced": len(fc), "evidence": evidence(items),
            "per_trial_acc": {"n_trials": len(tacc), "min": tacc[0] if tacc else None,
                              "median": statistics.median(tacc) if tacc else None, "max": tacc[-1] if tacc else None},
            "bootstrap": {"unit": "patient", "B": 1000, "seed": 0}}


def run_system(recs, dm, split, fmt, run_dir):
    """(items, summary) of one run, or (None, None) if it has no scores for the split yet."""
    sc = scores(f"{run_dir}/scores_clin_v1~trialgpt_{split}.jsonl")
    src = f"{run_dir}/scores_rule_v1~dev_missing.jsonl"
    if not os.path.exists(src):          # test run of a system with a dev run: same adapter, code and set
        src = re.sub(r"(-s0)?$", "-dev", run_dir, count=1) + "/scores_rule_v1~dev_missing.jsonl"
    sd = scores(src)
    if sc is None or sd is None:
        return None, None
    tau = M.mr_threshold(dm, [sd[r["iid"]]["u"] for r in dm])
    items = evaluate(recs, sc, tau, fmt)
    return items, summary(items, tau, os.path.basename(run_dir), split) | {
        "threshold_source": os.path.relpath(src, os.path.dirname(os.path.dirname(run_dir))).replace(os.sep, "/")}


def fmt_num(x, nd=1):
    return "-" if x is None else f"{x:.{nd}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["trialgpt", "medeinst", "keypairs", "nli4ct"])
    ap.add_argument("--split", default="dev", choices=["dev", "test"])
    ap.add_argument("--results", default=f"{REPO}/results_git")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--data-c", default=f"{REPO}/data", help="C's sets (clin_v1/...)")
    a = ap.parse_args()
    if a.dataset == "medeinst":
        return medeinst(a)
    if a.dataset == "keypairs":
        return keypairs(a)
    if a.dataset == "nli4ct":
        return nli4ct(a)
    recs = load_jsonl(f"{REPO}/data/clin_v1/trialgpt_{a.split}/records.jsonl")
    dm = dataset(a.data, "rule_v1/dev_missing")
    rows, items_by = [], {}
    for name, label, fmt, run in [(n, l, f, r) for n, l, f in SYSTEMS for r in run_ids(a.results, n, a.split)]:
        items, summ = run_system(recs, dm, a.split, fmt, f"{a.results}/{run}")
        seed = run.rsplit("-s", 1)[1] if run[-3:-1] == "-s" else None
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
ME_COMPARISONS = [("ledger2-triplets-s0", "critic"), ("ledger2-triplets-s0", "summary2-triplets-s0")]   # plan (4), (5)


def me_pairs(recs, sc):
    """One item per pair: d on the control (base) and on the trap (flip); flags from the records."""
    P = {}
    for r in recs:
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
            pairs = [{"tid": t, "a": bx[t], "b": by[t]} for t in sorted(bx.keys() & by.keys())]
            r = M.paired_cluster_bootstrap(pairs, "tid", lambda ps: reversal([p["a"] for p in ps]),
                                           lambda ps: reversal([p["b"] for p in ps]))
            comps.append((x, y, r))
            print(f"paired Reversal {x} - {y}: {r['diff']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}] p={r['p']:.3f}")
    if comps:
        json.dump({f"{x} - {y}": r for x, y, r in comps},
                  open(f"{a.results}/C-ME-comparisons.json", "w", encoding="utf-8", newline="\n"), indent=1)
    L = ["# MedEinst test pairs: results (role C)", "",
         "Generated by `scripts/eval_clinical.py medeinst` from `results_git/*/scores_clin_v1~medeinst_test.jsonl` "
         "(no typed numbers). Two candidate diagnoses per pair (control y_gt, trap y_bias); see "
         "`data/clin_v1/medeinst_test/MANIFEST.json` for the release, normalisation and flags.", "",
         "| run | Reversal [95% CI pairs] | CI label pairs | control acc | trap acc | bias-trap rate | ties | excl. no-diff | excl. overlap |",
         "|---|---|---|---|---|---|---|---|---|"]
    for d, s in rows:
        L.append(f"| {d} | {s['Reversal']:.1f} [{s['CI95'][0]:.1f}, {s['CI95'][1]:.1f}] | [{s['CI95_label_pairs'][0]:.1f}, "
                 f"{s['CI95_label_pairs'][1]:.1f}] | {s['control_acc']:.1f} | {s['trap_acc']:.1f} | "
                 f"{fmt_num(s['bias_trap_rate'])} | {s['tie_rate']:.1f} | {s['Reversal_excl_no_content_diff']:.1f} | "
                 f"{s['Reversal_excl_overlap_ref']:.1f} |")
    if comps:
        L += ["", "Paired differences in Reversal (same pairs, bootstrap over pairs, 1,000 resamples):", ""]
        L += [f"- {x} minus {y}: {r['diff']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}], p = {r['p']:.3f} ({r['n_items']} pairs)"
              for x, y, r in comps]
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
            out = f"{a.results}/{d}/summary_{set_name.replace('/', '~')}.json"
            old = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
            summ["eval"] = old.get("eval")
            json.dump(summ, open(out, "w", encoding="utf-8", newline="\n"), indent=1)
            L.append(f"| {d} | {m['Control_F1']:.3f} | {m['Control_macroF1']:.3f} | {m['Faithfulness']:.3f} | "
                     f"{m['Consistency']:.3f} | {m['Consistency_acc']:.3f} | {m['Contrast_F1']:.3f} | {m['Average']:.3f} |")
            print(set_name, d, {k: round(v, 3) for k, v in m.items() if isinstance(v, float)})
        L.append("")
    open(f"{REPO}/docs/NLI4CT_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/NLI4CT_RESULTS.md")


def write_report(rows, comps):
    L = ["# TrialGPT criterion annotations: results (role C)", "",
         "Generated by `scripts/eval_clinical.py trialgpt --split test` from `results_git/C-TG-*/` (no typed numbers).",
         "Protocol: `docs/TRIALGPT_PROTOCOL.md`. Test portion: 43 patients; N/A items reported separately.", "",
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
        L += ["", "Paired differences in macro-F1 (same items, patient bootstrap, 1,000 resamples; Holm across the "
                  "primary comparisons is applied by the lead):", ""]
        L += [f"- {x} minus {y}: {r['diff']:.1f} [{r['lo']:.1f}, {r['hi']:.1f}], p = {r['p']:.3f} "
              f"({r['n_items']} items, {r['n_clusters']} patients)" for x, y, r in comps]
    open(f"{REPO}/docs/TRIALGPT_RESULTS.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("wrote docs/TRIALGPT_RESULTS.md")


if __name__ == "__main__":
    main()
