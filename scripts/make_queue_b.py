"""Write a queue file for B's runners (train_eval_job.py) from docs/RUN_MATRIX_B.csv.
  python scripts/make_queue_b.py smoke   OUT.json        # B-C0 smoke comparison + B-T0 timing
  python scripts/make_queue_b.py factorial OUT.json --seeds 0 [--registry data/REGISTRY.json]
Factorial rows read their training set as <version>/train_<corpus> and are
evaluated on every frozen dev/test set of that version in the registry."""
import argparse, csv, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FMTS = ("verdict", "rationale", "summary2", "value2", "ledger2")
PRIO = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


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


def factorial(seeds, registry, version):
    reg = json.load(open(registry))
    evals = sorted(n for n, v in reg.items() if n.startswith(version + "/") and v.get("frozen")
                   and v.get("split") in ("dev", "test"))
    keep, runs = keep_list(), []
    for r in csv.DictReader(open(f"{ROOT}/docs/RUN_MATRIX_B.csv", encoding="utf-8")):
        m = re.fullmatch(r"B-F-(\w+)-(\w+)-s(\d)", r["run_id"])
        if not m or int(m[3]) not in seeds or r["status"] in ("done", "dropped"):
            continue
        corpus = f"{version}/train_{m[2]}"
        if corpus not in reg or not reg[corpus].get("frozen"):
            sys.exit(f"{corpus} not frozen in {registry}")
        runs.append({"run_id": r["run_id"], "format": m[1], "corpus": corpus, "seed": int(m[3]),
                     "n_examples": 60000, "priority": PRIO[r["priority"]],
                     "keep_adapter": r["run_id"] in keep, "eval_sets": evals})
    return runs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["smoke", "factorial"])
    ap.add_argument("out")
    ap.add_argument("--seeds", default="0")
    ap.add_argument("--registry", default=f"{ROOT}/data/REGISTRY.json")
    ap.add_argument("--version", default="rule_v1")
    a = ap.parse_args()
    runs = smoke() if a.kind == "smoke" else factorial({int(s) for s in a.seeds.split(",")}, a.registry, a.version)
    json.dump({"runs": runs}, open(a.out, "w"), indent=1)
    print(f"{len(runs)} runs -> {a.out}")


if __name__ == "__main__":
    main()
