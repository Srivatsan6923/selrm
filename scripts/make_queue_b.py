"""Write a queue file for B's runners (train_eval_job.py) from docs/RUN_MATRIX_B.csv.
  python scripts/make_queue_b.py smoke   OUT.json        # B-C0 smoke comparison + B-T0 timing
  python scripts/make_queue_b.py factorial OUT.json --seeds 0 [--registry data/REGISTRY.json] [--key_only]
  python scripts/make_queue_b.py transfer|extras|backbones|newexp OUT.json --seeds 0
  python scripts/make_queue_b.py critic OUT.json          # C-TF-critic (owner C, run by B's runners)
Revised plan (lead, 2 Oct evening): only the four key cells are evaluated on every frozen dev/test set
(every seed); every other run on dev, test_L2, dev_missing and missing (B-TR rows add test_L3alt; the new
experiments and folds use the sets the plan names; diversity curves the reduced sets). priority() encodes the
run order."""
import argparse, csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMTS = ("verdict", "rationale", "summary2", "value2", "ledger2")
PRIO = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
KEY_CELLS = {("verdict", "blocks"), ("verdict", "triplets"), ("ledger2", "blocks"), ("ledger2", "triplets")}
EVAL = {"bs_score": 128, "bs_gen": 256, "max_new": 384}    # B-T0b: 1.7x faster rationale eval than 64/64; capped at 128 below 60 GB
REDUCED = ("dev", "test_L2")          # FINAL_TASKS_B: non-core runs on dev and L2 (+ A's new sets, separate runs)
TRANSFER = ("dev", "test_L2", "test_L3alt", "dev_missing", "missing")   # Table 4 rows (B-TR): its L3-alt and MR columns
A_CODE = "e40789bd5d7a"     # role A's rule_v1 freeze: check-code renderer for genprm (snapshot under ROOT/code)
# adapters kept on the PVC for the clinical columns (C's eval_clinical.py, not yet available): Table 4 rows and
# the MedEinst column of Table 9; only configs/keep_adapters.json runs are published for C and D
CLINICAL_CELLS = {("verdict", "triplets"), ("summary2", "triplets"), ("rationale", "triplets"), ("value2", "triplets"),
                  ("ledger2", "balanced"), ("ledger2", "blocks"), ("ledger2", "triplets")}


CORE_CELLS = {(f, c) for f in ("verdict", "summary2", "ledger2") for c in ("blocks", "triplets")}
ABL_ORDER = ("decfield", "bitonly-judge", "bitonly-reader", "conddrv", "verify", "concept", "premise-gate", "probe-rw",
             "nopres", "noresamp", "pairwise")       # FINAL_TASKS_B P1 order


def priority(rid, seed, mprio="P1"):
    """Run order of FINAL_TASKS_B (3 Oct; lower first, equal values in queue-file order). P0: eval-only runs of the
    analyses (program-supplied ledger, field interventions), summary x blocks s0, seeds 1-2 of the six core cells,
    the summary pipeline whose judge also sees the case, leave one near-miss kind out (subject, time, boundary),
    evaluations on A's new sets. P1: remaining seed-0 cells, seeds 3-4 of the core cells, ablations in the listed
    order, FoVer and GenPRM rows, medical-data rows, folds 2-3, diversity curves, second backbone. Rows the file does
    not list (dose curve, seeds 1-2 of non-core cells, P2 seeds of ablations) come after everything."""
    m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", rid)
    cell = (m[1], m[2]) if m else None
    if rid in ("B-AE-oracle-ledger", "B-AE-field-edit", "B-AE-field-swap"):
        return 0
    if rid == "B-F-summary2-blocks-s0":
        return 10
    if m and cell in CORE_CELLS and seed in (1, 2):
        return 20
    if rid.startswith("B-SC-"):
        return 30
    if rid.startswith("B-LOKO-"):
        return 40 + {"subject": 0, "time": 1, "boundary": 2}.get(rid.split("-")[2], 3)
    if rid.startswith("B-NS-"):
        return 45
    if m and seed == 0:
        return 50
    if m and cell in CORE_CELLS and seed in (3, 4):
        return 55
    a = re.fullmatch(r"B-AB-([\w-]+?)(-scores)?-s(\d)(-scores)?", rid)
    if a and int(a[3]) == 0 and a[1] in ABL_ORDER:
        return 60 + ABL_ORDER.index(a[1])
    if rid == "B-AE-pred-bit-program":
        return 60
    if rid.startswith("B-TR-fover"):
        return 72 + (seed > 0) * 20
    if rid.startswith("B-TR-genprm"):
        return 73 + (seed > 0) * 20
    if rid.startswith(("B-TR-", "B-DIS-")):
        return 74
    if rid.startswith("B-FOLD"):
        return 76 + (seed > 0)
    if rid.startswith("B-DIV-"):
        return 80 + (seed > 0)
    if rid.startswith("B-BB-"):
        return 85 + (seed > 0) * 10
    return 99


def keep_list():
    return set(json.load(open(f"{ROOT}/configs/keep_adapters.json"))["keep"])


def matrix():
    return list(csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")))


def frozen_evals(registry, version):
    reg = json.load(open(registry))
    return reg, sorted(n for n, v in reg.items() if n.startswith(version + "/") and v.get("frozen")
                       and v.get("split") in ("dev", "test"))


def smoke():
    runs = [{"run_id": f"B-C0-smoke-verdict-{c}-s0", "format": "verdict", "corpus": f"smoke_v2/train_{c}",
             "seed": 0, "priority": 0, "provisional": True,
             "eval_sets": ["smoke_v2/dev_seen_rules", "smoke_v2/test_heldout_rules"]}
            for c in ("blocks", "triplets")]
    runs += [{"run_id": f"B-T0-{f}", "format": f, "corpus": "smoke_v2/train_triplets", "seed": 0,
              "priority": 1, "provisional": True, "timing": True, "max_steps": 200,
              "eval_sets": ["smoke_v2/test_heldout_rules"]} for f in FMTS]
    return runs


def factorial(seeds, registry, version, key_only=False):
    reg, evals = frozen_evals(registry, version)
    keep, runs = keep_list(), []
    for r in matrix():
        m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", r["run_id"])
        if not m or int(m[3]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        if key_only and (m[1], m[2]) not in CORE_CELLS:
            continue
        corpus = f"{version}/train_{m[2]}"
        if corpus not in reg or not reg[corpus].get("frozen"):
            sys.exit(f"{corpus} not frozen in {registry}")
        full = (m[1], m[2]) in CORE_CELLS      # every frozen dev/test set: the six core cells, every seed
        runs.append({"run_id": r["run_id"], "format": m[1], "corpus": corpus, "seed": int(m[3]),
                     "n_examples": 60000, "priority": priority(r["run_id"], int(m[3]), r["priority"]),
                     "keep_adapter": r["run_id"] in keep or (m[1], m[2]) in CLINICAL_CELLS | CORE_CELLS, "eval": dict(EVAL),
                     "eval_sets": evals if full else [f"{version}/{s}" for s in REDUCED]})
    return runs


def transfer(seeds, registry, version):
    """B-TR rows that need no other role's data: fover (verdict on FoVer formal steps) and genprm
    (GenPRM-style verifier on rule triplets). Table 4 rows: reduced sets + test_L3alt."""
    runs = []
    for r in matrix():
        m = re.fullmatch(r"B-TR-(fover|genprm)-s(\d)", r["run_id"])
        if not m or int(m[2]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        seed = int(m[2])
        spec = ({"format": "verdict", "corpus": "fover_v1/train"} if m[1] == "fover" else
                {"format": "genprm", "corpus": f"{version}/train_triplets", "a_code": A_CODE, "min_gen": 2})
        runs.append({"run_id": r["run_id"], "seed": seed, "n_examples": 60000,
                     "priority": priority(r["run_id"], seed, r["priority"]),
                     "keep_adapter": True,   # Table 4 rows (clinical columns)
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in TRANSFER], **spec})
    return runs


BACKBONES = {"qwen3.5-4b": "unsloth/Qwen3.5-4B", "non-qwen-4to9b": "unsloth/granite-4.1-8b"}   # configs/models_b.json


def backbones(seeds, registry, version):
    """B-BB rows: the key cells on other base models (claimable only by runners that staged them,
    submit_b.py runners ... --models)."""
    runs = []
    for r in matrix():
        m = re.fullmatch(r"B-BB-(.+)-(verdict|ledger2)-(blocks|triplets)-s(\d)", r["run_id"])
        if not m or int(m[4]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        runs.append({"run_id": r["run_id"], "format": m[2], "corpus": f"{version}/train_{m[3]}", "seed": int(m[4]),
                     "n_examples": 60000, "base_model": BACKBONES[m[1]],
                     "priority": priority(r["run_id"], int(m[4]), r["priority"]), "keep_adapter": False,
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]})
    return runs


# Table 9 ablations: changes against ledger2 x triplets (corpus names inside <version>/)
ABLATIONS = {"decfield": {"format": "ledger2_dec"}, "bitonly-judge": {"format": "dec_judge"},
             "bitonly-reader": {"format": "bit_reader"}, "verify": {"format": "ledger2_verify", "mode": "verify"},
             "concept": {"kind": "concept"}, "nopres": {"corpus": "abl_nopres_triplets"},
             "noresamp": {"resample_p": 0}, "pairwise": {"format": "verdict_bt"},
             "concl-only": {"corpus": "abl_conclusion_triplets"}}
# Table 9 / Sec. 7.4 evaluation-only rows: adapter run, format, eval mode, sets
EVAL_ONLY = {"oracle-ledger": ("B-F-ledger2-triplets-s0", "ledger2", "oracle_ledger", ("dev", "test_L2")),
             "pred-bit-program": ("B-AB-decfield-s0", "ledger2_dec", "program_bit", ("dev", "test_L2")),
             "field-swap": ("B-F-ledger2-triplets-s0", "ledger2", "ledger_swap", ("dev", "test_L2")),
             "field-edit": ("B-F-ledger2-triplets-s0", "ledger2", "ledger_edit", ("test_L2",))}   # newer runners (v2/)


def extras(seeds, registry, version):
    """B-AB ablations, B-AE evaluation-only rows, B-FOLD fold replications and B-DIV diversity curves
    whose inputs exist (change loss and the premise gate are queued by hand; probe re-weighting step 1 here,
    the weighted run in probe_rw())."""
    reg = json.load(open(registry))
    ok = lambda name: name in reg and reg[name].get("frozen")
    runs = []
    for r in matrix():
        rid, seed = r["run_id"], int(r["seed"]) if r["seed"].isdigit() else 0
        if seed not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        base = {"run_id": rid, "seed": seed, "priority": priority(rid, seed, r["priority"]), "eval": dict(EVAL)}
        if rid == "B-AB-probe-rw-s0":    # step 1 of 3 (then scripts/probe_weights.py, then the weighted run)
            runs.append({**base, "run_id": rid + "-scores", "format": "ledger2", "train": False,
                         "adapter": "adapters/B-F-ledger2-blocks-s0", "eval_sets": [f"{version}/abl_probe_blocks"]})
            continue
        m = re.fullmatch(r"B-AB-([\w-]+)-s\d", rid)
        if m and m[1] in ABLATIONS:
            ch = dict(ABLATIONS[m[1]])
            spec = {**base, "format": "ledger2", "corpus": f"{version}/train_triplets", "n_examples": 60000,
                    "keep_adapter": seed == 0, "eval_sets": [f"{version}/{s}" for s in REDUCED]}
            if "mode" in ch:
                spec["eval"]["mode"] = ch.pop("mode")
            if "corpus" in ch:
                ch["corpus"] = f"{version}/{ch['corpus']}"
            runs.append({**spec, **ch})
            continue
        m = re.fullmatch(r"B-AE-([\w-]+)", rid)
        if m and m[1] in EVAL_ONLY:
            src, fmt, mode, sets = EVAL_ONLY[m[1]]
            runs.append({**base, "format": fmt, "train": False, "adapter": f"adapters/{src}", "a_code": A_CODE,
                         "eval": {**EVAL, "mode": mode}, "eval_sets": [f"{version}/{s}" for s in sets]}
                        | ({"min_gen": 2} if mode == "ledger_edit" else {}))
            continue
        m = re.fullmatch(r"B-FOLD(\d)-(\w+)-(\w+)-s\d", rid)
        if m and ok(f"{version}_fold{m[1]}/train_{m[3]}"):
            v = f"{version}_fold{m[1]}"
            runs.append({**base, "format": m[2], "corpus": f"{v}/train_{m[3]}", "n_examples": 60000,
                         "keep_adapter": False, "eval_sets": [f"{v}/dev", f"{v}/test_L2"]})
            continue
        m = re.fullmatch(r"B-DIV-(\w+)-(\d+)-s\d", rid)
        if m and ok(f"{version}/div_{m[1]}_{m[2]}"):
            runs.append({**base, "format": "ledger2", "corpus": f"{version}/div_{m[1]}_{m[2]}", "n_examples": None,
                         "keep_adapter": False, "eval_sets": [f"{version}/{s}" for s in REDUCED]})
    order = ("B-AB", "B-AE", "B-FOLD", "B-DIV")     # within a priority: Table 9 first, then folds, then curves
    return sorted(runs, key=lambda r: next(i for i, f in enumerate(order) if r["run_id"].startswith(f)))


def probe_rw(version):
    """Probe re-weighting step 3: ledger2 on abl_probe_blocks (probes are never trained on), judge pairs drawn
    by the weights that pretok derives from B-AB-probe-rw-s0-scores (step 2 runs inside prep)."""
    return [{"run_id": "B-AB-probe-rw-s0", "seed": 0, "priority": priority("B-AB-probe-rw-s0", 0), "format": "ledger2",
             "corpus": f"{version}/abl_probe_blocks", "n_examples": 60000,
             "pair_weights": "derived/probe_rw/B-F-ledger2-blocks-s0.json",
             "probe_scores": "B-AB-probe-rw-s0-scores", "probe_set": f"{version}/abl_probe_blocks",
             "keep_adapter": True, "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]}]


def critic(registry, version):
    """C-TF-critic (owner C, executed by B's runners): zero-shot base model, frozen verdict prompt, pointwise u,
    every frozen dev/test set."""
    _, evals = frozen_evals(registry, version)
    return [{"run_id": "C-TF-critic", "seed": 0, "priority": priority("C-TF-critic", 0), "format": "verdict",
             "train": False, "keep_adapter": False, "eval": dict(EVAL), "eval_sets": evals}]


def newexp(seeds, registry, version):
    """Leave one near-miss kind out (FINAL_TASKS_B P0.5): B-LOKO-<kind>-<format>-s0, format verdict, summary2 or
    ledger2, kind subject, time or boundary, on A's train_triplets_no_<kind> (queued once A registers it; dev,
    test_L2, test_L0, scored on the held-out kind). Near-miss dose (not in FINAL_TASKS_B; last): B-DOSE-<pct>-<format>-s0
    on train_dose_<pct> (dev, test_L2)."""
    reg = json.load(open(registry))
    frozen = {n for n, v in reg.items() if v.get("frozen")}
    runs = []
    for r in matrix():
        rid = r["run_id"]
        m = re.fullmatch(r"B-(LOKO|DOSE)-(\w+)-(verdict|summary2|ledger2)-s(\d)", rid)
        if not m or int(m[4]) not in seeds or r["status"] in ("done", "dropped", "deferred"):
            continue
        if m[1] == "LOKO":
            hits = sorted(n for n in frozen if n.endswith(f"/train_triplets_no_{m[2]}"))
            if not hits:
                continue                                  # A has not registered the corpus yet
            corpus, sets = hits[0], ("dev", "test_L2", "test_L0")
        else:
            corpus, sets = f"{version}/train_dose_{m[2]}", ("dev", "test_L2")
            if corpus not in frozen:
                continue
        runs.append({"run_id": rid, "format": m[3], "corpus": corpus, "seed": int(m[4]), "n_examples": 60000,
                     "priority": priority(rid, int(m[4]), r["priority"]), "keep_adapter": m[1] == "LOKO",
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in sets]})
    return sorted(runs, key=lambda r: r["priority"])


def summary_case(registry, version):
    """FINAL_TASKS_B P0.4: the summary pipeline whose judge also sees the case, on triplets (B-SC-summary2-triplets-s0)."""
    return [{"run_id": "B-SC-summary2-triplets-s0", "seed": 0, "priority": priority("B-SC-summary2-triplets-s0", 0),
             "format": "summary2_case", "corpus": f"{version}/train_triplets", "n_examples": 60000, "keep_adapter": True,
             "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in REDUCED]}]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["smoke", "factorial", "transfer", "extras", "backbones", "probe_rw", "critic",
                                     "newexp", "summary_case"])
    ap.add_argument("out")
    ap.add_argument("--seeds", default="0")
    ap.add_argument("--registry", default=f"{ROOT}/data/REGISTRY.json")
    ap.add_argument("--version", default="rule_v1")
    ap.add_argument("--key_only", action="store_true", help="factorial: the four key cells only")
    ap.add_argument("--runs", default="", help="keep run_ids matching this regex")
    a = ap.parse_args()
    seeds = {int(s) for s in a.seeds.split(",")}
    gen = {"smoke": lambda: smoke(),
           "factorial": lambda: factorial(seeds, a.registry, a.version, a.key_only),
           "transfer": lambda: transfer(seeds, a.registry, a.version),
           "backbones": lambda: backbones(seeds, a.registry, a.version),
           "extras": lambda: extras(seeds, a.registry, a.version),
           "probe_rw": lambda: probe_rw(a.version),
           "critic": lambda: critic(a.registry, a.version),
           "newexp": lambda: newexp(seeds, a.registry, a.version),
           "summary_case": lambda: summary_case(a.registry, a.version)}
    runs = [r for r in gen[a.kind]() if re.search(a.runs, r["run_id"])]
    newer = [r["run_id"] for r in runs if r.get("min_gen", 0) >= 2]   # runners staged before 2 Oct 13:00 read the top level
    if newer and "v2" not in os.path.normpath(os.path.abspath(a.out)).split(os.sep):
        sys.exit(f"{newer} need runner code from 2 Oct 13:00 UTC on: write them under configs/queues/v2/ (docs/NRP_B.md)")
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump({"runs": runs}, open(a.out, "w", newline="\n"), indent=1)
    print(f"{len(runs)} runs -> {a.out}")


if __name__ == "__main__":
    main()
