"""Write a queue file for B's runners (train_eval_job.py) from docs/RUN_MATRIX_B.csv.
  python scripts/make_queue_b.py smoke   OUT.json        # B-C0 smoke comparison + B-T0 timing
  python scripts/make_queue_b.py factorial OUT.json --seeds 0 [--registry data/REGISTRY.json] [--key_only]
  python scripts/make_queue_b.py transfer|extras OUT.json --seeds 0   # B-TR-fover | B-AB, B-AE, B-FOLD, B-DIV
Factorial rows read their training set as <version>/train_<corpus> and are
evaluated on every frozen dev/test set of that version in the registry."""
import argparse, csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMTS = ("verdict", "rationale", "summary2", "value2", "ledger2")
PRIO = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
KEY_CELLS = {("verdict", "blocks"), ("verdict", "triplets"), ("ledger2", "blocks"), ("ledger2", "triplets")}
EVAL = {"bs_score": 128, "bs_gen": 256, "max_new": 384}    # B-T0b: 1.7x faster rationale eval than 64/64; capped at 128 below 60 GB
PRIMARY = ("dev", "test_L2", "test_L3alt", "dev_missing", "missing")   # Tables 3-4; seeds >= 1 of non-key cells
A_CODE = "e40789bd5d7a"     # role A's rule_v1 freeze: check-code renderer for genprm (snapshot under ROOT/code)
# adapters kept on the PVC for the clinical columns (C's eval_clinical.py, not yet available): Table 4 rows and
# the MedEinst column of Table 9; only configs/keep_adapters.json runs are published for C and D
CLINICAL_CELLS = {("verdict", "triplets"), ("summary2", "triplets"), ("rationale", "triplets"), ("value2", "triplets"),
                  ("ledger2", "balanced"), ("ledger2", "blocks"), ("ledger2", "triplets")}


def keep_list():
    return set(json.load(open(f"{ROOT}/configs/keep_adapters.json"))["keep"])


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
    reg = json.load(open(registry))
    evals = sorted(n for n, v in reg.items() if n.startswith(version + "/") and v.get("frozen")
                   and v.get("split") in ("dev", "test"))
    keep, runs = keep_list(), []
    for r in csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")):
        m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", r["run_id"])
        if not m or int(m[3]) not in seeds or r["status"] in ("done", "dropped"):
            continue
        if key_only and (m[1], m[2]) not in KEY_CELLS:
            continue
        corpus = f"{version}/train_{m[2]}"
        if corpus not in reg or not reg[corpus].get("frozen"):
            sys.exit(f"{corpus} not frozen in {registry}")
        # inside a priority class: seed 0 before other seeds (one seed of every cell first), key cells
        # first within each (C and D need their adapters earliest)
        full = int(m[3]) == 0 or (m[1], m[2]) in KEY_CELLS      # full ladder: seed 0 and the key cells
        runs.append({"run_id": r["run_id"], "format": m[1], "corpus": corpus, "seed": int(m[3]),
                     "n_examples": 60000,
                     "priority": 10 * PRIO[r["priority"]] + 2 * (int(m[3]) > 0) + ((m[1], m[2]) not in KEY_CELLS),
                     "keep_adapter": r["run_id"] in keep or (m[1], m[2]) in CLINICAL_CELLS, "eval": dict(EVAL),
                     "eval_sets": evals if full else [e for e in evals if e.split("/", 1)[1] in PRIMARY]})
    return runs


def transfer(seeds, registry, version):
    """B-TR rows that need no other role's data: fover (verdict on FoVer formal steps) and genprm
    (GenPRM-style verifier on rule triplets; generation per record, so primary sets only)."""
    reg = json.load(open(registry))
    evals = sorted(n for n, v in reg.items() if n.startswith(version + "/") and v.get("frozen")
                   and v.get("split") in ("dev", "test"))
    primary = [e for e in evals if e.split("/", 1)[1] in PRIMARY]
    runs = []
    for r in csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")):
        m = re.fullmatch(r"B-TR-(fover|genprm)-s(\d)", r["run_id"])
        if not m or int(m[2]) not in seeds or r["status"] in ("done", "dropped"):
            continue
        seed = int(m[2])
        spec = ({"format": "verdict", "corpus": "fover_v1/train", "eval_sets": evals if seed == 0 else primary}
                if m[1] == "fover" else
                {"format": "genprm", "corpus": f"{version}/train_triplets", "a_code": A_CODE, "eval_sets": primary})
        runs.append({"run_id": r["run_id"], "seed": seed, "n_examples": 60000,
                     "priority": 10 * PRIO[r["priority"]] + 2 * (seed > 0),
                     "keep_adapter": True,   # Table 4 rows (clinical columns)
                     "eval": dict(EVAL), **spec})
    return runs


BACKBONES = {"qwen3.5-4b": "unsloth/Qwen3.5-4B", "non-qwen-4to9b": "unsloth/granite-4.1-8b"}   # configs/models_b.json


def backbones(seeds, registry, version):
    """B-BB rows: the key cells on other base models (claimable only by runners that staged them,
    submit_b.py runners ... --models)."""
    runs = []
    for r in csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")):
        m = re.fullmatch(r"B-BB-(.+)-(verdict|ledger2)-(blocks|triplets)-s(\d)", r["run_id"])
        if not m or int(m[4]) not in seeds or r["status"] in ("done", "dropped"):
            continue
        runs.append({"run_id": r["run_id"], "format": m[2], "corpus": f"{version}/train_{m[3]}", "seed": int(m[4]),
                     "n_examples": 60000, "base_model": BACKBONES[m[1]],
                     "priority": 10 * PRIO[r["priority"]] + 2 * (int(m[4]) > 0), "keep_adapter": False,
                     "eval": dict(EVAL), "eval_sets": [f"{version}/{s}" for s in PRIMARY]})
    return runs


# Table 9 ablations: changes against ledger2 x triplets (corpus names inside <version>/)
ABLATIONS = {"decfield": {"format": "ledger2_dec"}, "bitonly-judge": {"format": "dec_judge"},
             "bitonly-reader": {"format": "bit_reader"}, "verify": {"format": "ledger2_verify", "mode": "verify"},
             "concept": {"kind": "concept"}, "nopres": {"corpus": "abl_nopres_triplets"},
             "noresamp": {"resample_p": 0}, "pairwise": {"format": "verdict_bt"},
             "concl-only": {"corpus": "abl_conclusion_triplets"}}
# Table 9 / Sec. 7.4 evaluation-only rows: adapter run, format, eval mode, sets
EVAL_ONLY = {"oracle-ledger": ("B-F-ledger2-triplets-s0", "ledger2", "oracle_ledger", PRIMARY),
             "pred-bit-program": ("B-AB-decfield-s0", "ledger2_dec", "program_bit", PRIMARY),
             "field-swap": ("B-F-ledger2-triplets-s0", "ledger2", "ledger_swap", ("dev", "test_L2")),
             "field-edit": ("B-F-ledger2-triplets-s0", "ledger2", "ledger_edit", ("test_L2",))}   # newer runners (v2/)


def extras(seeds, registry, version):
    """B-AB ablations, B-AE evaluation-only rows, B-FOLD fold replications and B-DIV diversity curves
    whose inputs exist (probe re-weighting, change loss, field edits and the premise gate are queued by hand)."""
    reg = json.load(open(registry))
    ok = lambda name: name in reg and reg[name].get("frozen")
    runs = []
    for r in csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")):
        rid, seed = r["run_id"], int(r["seed"]) if r["seed"].isdigit() else 0
        if seed not in seeds or r["status"] in ("done", "dropped"):
            continue
        base = {"run_id": rid, "seed": seed, "priority": 10 * PRIO[r["priority"]] + 2 * (seed > 0), "eval": dict(EVAL)}
        if rid == "B-AB-probe-rw-s0":    # step 1 of 3 (then scripts/probe_weights.py, then the weighted run)
            runs.append({**base, "run_id": rid + "-scores", "format": "ledger2", "train": False,
                         "adapter": "adapters/B-F-ledger2-blocks-s0", "eval_sets": [f"{version}/abl_probe_blocks"]})
            continue
        m = re.fullmatch(r"B-AB-([\w-]+)-s\d", rid)
        if m and m[1] in ABLATIONS:
            ch = dict(ABLATIONS[m[1]])
            spec = {**base, "format": "ledger2", "corpus": f"{version}/train_triplets", "n_examples": 60000,
                    "keep_adapter": seed == 0, "eval_sets": [f"{version}/{s}" for s in PRIMARY]}
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
                         "eval": {**EVAL, "mode": mode}, "eval_sets": [f"{version}/{s}" for s in sets]})
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
                         "keep_adapter": False, "eval_sets": [f"{version}/dev", f"{version}/test_L2"]})
    order = ("B-AB", "B-AE", "B-FOLD", "B-DIV")     # within a priority: Table 9 first, then folds, then curves
    return sorted(runs, key=lambda r: next(i for i, f in enumerate(order) if r["run_id"].startswith(f)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["smoke", "factorial", "transfer", "extras", "backbones"])
    ap.add_argument("out")
    ap.add_argument("--seeds", default="0")
    ap.add_argument("--registry", default=f"{ROOT}/data/REGISTRY.json")
    ap.add_argument("--version", default="rule_v1")
    ap.add_argument("--key_only", action="store_true", help="factorial: the four key cells only")
    ap.add_argument("--runs", default="", help="keep run_ids matching this regex")
    a = ap.parse_args()
    seeds = {int(s) for s in a.seeds.split(",")}
    runs = (smoke() if a.kind == "smoke" else factorial(seeds, a.registry, a.version, a.key_only) if a.kind == "factorial"
            else transfer(seeds, a.registry, a.version) if a.kind == "transfer"
            else backbones(seeds, a.registry, a.version) if a.kind == "backbones" else extras(seeds, a.registry, a.version))
    runs = [r for r in runs if re.search(a.runs, r["run_id"])]
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    json.dump({"runs": runs}, open(a.out, "w", newline="\n"), indent=1)
    print(f"{len(runs)} runs -> {a.out}")


if __name__ == "__main__":
    main()
