"""Clinical-set evaluation from per-example scores (owner C). No GPU.
  python scripts/eval_clinical.py trialgpt --split dev|test [--results results_git] [--data scratch/rv1]
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
        if "reader_output" in s:
            it["reader"] = s["reader_output"]
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
    sd = scores(f"{run_dir}/scores_rule_v1~dev_missing.jsonl")
    if sc is None or sd is None:
        return None, None
    tau = M.mr_threshold(dm, [sd[r["iid"]]["u"] for r in dm])
    items = evaluate(recs, sc, tau, fmt)
    return items, summary(items, tau, os.path.basename(run_dir), split)


def fmt_num(x, nd=1):
    return "-" if x is None else f"{x:.{nd}f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["trialgpt"])
    ap.add_argument("--split", default="dev", choices=["dev", "test"])
    ap.add_argument("--results", default=f"{REPO}/results_git")
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    a = ap.parse_args()
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
