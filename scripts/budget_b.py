"""Training budget per configuration (Appendix H of the paper) as a result file: for every finished training run,
from its meta.json: corpus records, examples, reader and judge targets, prompt and completion tokens, optimiser
steps, learning rate, batch, rank, max length. One entry per run and one per configuration (the run id without
its seed, e.g. B-F-ledger2-triplets; the values of seed 0, with a flag if another seed differs).
  python scripts/budget_b.py      ->  results_git/B-BUDGET/summary.json"""
import ast, glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RG = f"{ROOT}/results_git"


def lit(x):
    return ast.literal_eval(x) if isinstance(x, str) else (x or {})


def main():
    runs, conf = {}, {}
    for mp in sorted(glob.glob(f"{RG}/B-*/meta.json")):
        d = os.path.dirname(mp)
        m = json.load(open(mp, encoding="utf-8"))
        ps, tr = lit(m.get("pretok_stats")), lit(m.get("train"))
        if not os.path.exists(f"{d}/DONE") or not ps or tr.get("eval_only") or not tr.get("steps") or m.get("provisional"):
            continue
        parts = ps.get("parts") or ps.get("corpus") or {}
        hp = (tr.get("key") or {}).get("hp") or tr.get("hp") or {}
        row = {"format": m["format"], "corpus": m.get("corpus"), "seed": m.get("seed"), "examples": ps.get("examples", ps.get("n")),
               "reader_targets": parts.get("reader"), "judge_targets": parts.get("judge"), "tokens": ps.get("tokens"),
               "completion_tokens": ps.get("completion_tokens"), "steps": tr.get("steps"), "lr": hp.get("lr"),
               "batch": hp.get("batch"), "lora_r": hp.get("lora_r"), "max_len": hp.get("max_len"), "epochs": hp.get("epochs")}
        runs[m["run_id"]] = row
        key = re.sub(r"-s\d+$", "", m["run_id"])        # the run family: several families share a format and corpus
        same = {k: v for k, v in row.items() if k != "seed"}
        if key not in conf or m.get("seed") == 0:
            conf[key] = same | {"differs_across_seeds": conf.get(key, same) != same and key in conf}
        elif {k: v for k, v in conf[key].items() if k != "differs_across_seeds"} != same:
            conf[key]["differs_across_seeds"] = True
    os.makedirs(f"{RG}/B-BUDGET", exist_ok=True)
    json.dump({"run_id": "B-BUDGET", "configurations": conf, "runs": runs},
              open(f"{RG}/B-BUDGET/summary.json", "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{RG}/B-BUDGET/DONE", "w", newline="\n").write("from meta.json of the finished runs\n")
    print(len(runs), "runs,", len(conf), "configurations")


if __name__ == "__main__":
    main()
