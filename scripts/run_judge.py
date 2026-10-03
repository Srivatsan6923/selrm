"""Score rule-tier sets with an API judge (owner C). Laptop side; no GPU.
  python scripts/run_judge.py --model NAME --run_id RID --set rule_v1/test_L2 [--set ...] [--n 1000]
         [--data DIR] [--estimate-only] [--pilot] [--workers 16]
NAME is an entry of configs/models.json (verified id, readout, params, prices). Conclusion claims
only (TA, Rev, Hold, PresHold; MR on missing twins). --n keeps a fixed subset of groups: n/5 per
near-miss kind, drawn with random.Random(0) from the sorted group ids, the same for every model.
Before any call the cost is estimated (selrm.judges.estimate_cost) and checked against
configs/budget.json minus the spend ledger results_git/C-API/ledger.jsonl; the run stops if it would
exceed the cap (apply the budget ladder of CLAUDE.md and log it). Writes
results_git/<run_id>/{meta.json, scores_<set>.jsonl, summary_<set>.json, DONE}; every reply is cached
(cache/api/, not in git) and kept in the scores file (raw, parsed, order)."""
import argparse, collections, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from selrm import judges as J
from selrm import metrics as M
from selrm.prompts import CHOICE_SYSTEM, choice_prompt, verdict_prompt

LEDGER = f"{REPO}/results_git/C-API/ledger.jsonl"


def load_jsonl(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def records(data, name):
    reg = json.load(open(f"{data}/REGISTRY.json", encoding="utf-8"))
    return load_jsonl(f"{data}/{reg[name]['path']}")


def subset(recs, n):
    if not n:
        return recs
    group = lambda r: r["meta"]["xr"]["item"] if "xr" in r.get("meta", {}) else r["tid"]   # xr_v1: an item spans 2 tids
    by = collections.defaultdict(set)
    for r in recs:
        by[r["nm_kind"]].add(group(r))
    keep = set()
    for kind in sorted(by):
        keep |= set(random.Random(0).sample(sorted(by[kind]), min(len(by[kind]), n // len(by))))
    return [r for r in recs if group(r) in keep]


def spent():
    if not os.path.exists(LEDGER):
        return 0.0
    return sum(x.get("cost_actual") or x.get("cost_estimate") or 0.0 for x in load_jsonl(LEDGER))


def plan(recs, readout):
    """(pairs for the choice / logprob readouts, records for pointwise calls)."""
    conc = [r for r in recs if r["claim_type"] == "conclusion"]
    by = collections.defaultdict(dict)
    for r in conc:
        by[(r["tid"], r["case_kind"])][r["claim_role"]] = r
    pairs = [(v["s"], v["s_prime"]) for k, v in by.items() if len(v) == 2 and k[1] != "missing"]
    point = [r for r in conc if r["case_kind"] == "missing"]
    return pairs, point


def prompts_of(pairs, point, readout):
    if readout == "choice":
        out = [CHOICE_SYSTEM + choice_prompt(s["rule_text"], s["case_text"], s["claim_text"], sp["claim_text"])
               for s, sp in pairs for _ in (0, 1)]
    else:
        out = [verdict_prompt(r) for s, sp in pairs for r in (s, sp)]
    return out + [verdict_prompt(r) for r in point]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--run_id", required=True)
    ap.add_argument("--set", action="append", required=True)
    ap.add_argument("--n", type=int, default=0)
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--estimate-only", action="store_true")
    ap.add_argument("--pilot", action="store_true", help="also check the pilot cap")
    ap.add_argument("--workers", type=int, default=16)
    a = ap.parse_args()
    cfg = next(m for m in json.load(open(f"{REPO}/configs/models.json", encoding="utf-8"))["models"] if m["name"] == a.model)
    budget = json.load(open(f"{REPO}/configs/budget.json", encoding="utf-8"))
    sets = {s: subset(records(a.data, s), a.n) for s in a.set}
    est = 0.0
    for s, recs in sets.items():
        pairs, point = plan(recs, cfg["readout"])
        e = J.estimate_cost(cfg, prompts_of(pairs, point, cfg["readout"]), cfg.get("est_completion_tokens", 16))
        print(f"{s}: {len(pairs)} pairs, {len(point)} pointwise records, estimated ${e:.2f}")
        est += e
    left = budget["api_usd_cap_total"] - spent()
    print(f"estimate ${est:.2f}; spent so far ${spent():.2f}; left ${left:.2f} of ${budget['api_usd_cap_total']}")
    if est > left or (a.pilot and est > budget["api_usd_cap_pilot"]):
        sys.exit("over budget: apply the budget ladder (CLAUDE.md) and log it in docs/DECISIONS_C.md")
    if a.estimate_only:
        return
    from openai import OpenAI
    key = os.environ.get(cfg.get("key_env", "OPENROUTER_API_KEY"))
    client = OpenAI(base_url=cfg.get("base_url", "https://openrouter.ai/api/v1"), api_key=key, max_retries=2,
                    timeout=cfg.get("timeout", 300)) if key else None
    judge = J.Judge(cfg, client, J.Cache(f"{REPO}/cache/api"), a.workers)
    out_dir = f"{REPO}/results_git/{a.run_id}"
    os.makedirs(out_dir, exist_ok=True)
    t0, summ_all = time.time(), {}
    for s, recs in sets.items():
        pairs, point = plan(recs, cfg["readout"])
        rows = []
        if cfg["readout"] == "choice":
            for (rs, rsp), res in zip(pairs, judge.score_pairs(pairs)):
                rows.append({"iid": rs["iid"], "u": res["d"] / 2, "raw": res["raw"], "parsed": res["parsed"],
                             "order": res["order"]})
                rows.append({"iid": rsp["iid"], "u": -res["d"] / 2})
        else:
            flat = [r for p in pairs for r in p]
            for r, res in zip(flat, judge.score_logprob(flat)):
                rows.append({"iid": r["iid"], "u": res["u"], "top": res["top"], "raw": res["raw"]})
        for r, res in zip(point, judge.score_pointwise(point)):
            rows.append({"iid": r["iid"], "u": res["u"], "raw": res["raw"], "parsed": res["parsed"], "readout": "pointwise"})
        name = s.replace("/", "~")
        with open(f"{out_dir}/scores_{name}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for row in rows:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        u = {row["iid"]: row["u"] for row in rows}
        scored = [r for r in recs if r["iid"] in u]
        T = M.decisions(scored, [u[r["iid"]] for r in scored])
        summ = {"run_id": a.run_id, "set": s, "claim_type": "conclusion", "readout": cfg["readout"]} | M.summarise(T)
        if summ.get("all"):
            summ["CI95"] = {m: list(M.bootstrap_ci(T, m)) for m in ("TA", "Rev", "Hold")}
        if point:     # MR for choice / text readouts: both claims of a missing twin answered "-" (threshold 0)
            summ |= {k: v for k, v in M.missing_rejection(scored, [u[r["iid"]] for r in scored], 0.0).items()
                     if k in ("MR", "n_missing")} | {"MR_readout": "pointwise text answer, reject iff '-'"}
        json.dump(summ, open(f"{out_dir}/summary_{name}.json", "w", encoding="utf-8", newline="\n"), indent=1)
        summ_all[s] = summ.get("all")
        print(s, summ.get("all"), {k: summ.get(k) for k in ("MR", "n_missing")})
    commit = subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    meta = {"run_id": a.run_id, "role": "C", "model": cfg["id"], "name": cfg["name"], "provider": cfg.get("provider", "openrouter"),
            "access_date": time.strftime("%Y-%m-%d"), "readout": cfg["readout"], "params": cfg.get("params", {}),
            "reasoning": cfg.get("reasoning_note"), "sets": a.set, "n_groups": a.n or "all",
            "subset_rule": "n/5 groups per near-miss kind, random.Random(0) over sorted tids" if a.n else None,
            "usage": judge.usage, "cost_estimate": est, "cost_actual": judge.usage["cost"],
            "wall_seconds": round(time.time() - t0, 1), "git_commit": commit, "summaries": summ_all}
    json.dump(meta, open(f"{out_dir}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps({"run_id": a.run_id, "model": cfg["id"], "sets": a.set, "cost_estimate": est,
                            "cost_actual": judge.usage["cost"], "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}) + "\n")
    if not judge.usage["errors"]:
        open(f"{out_dir}/DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) + "\n")
    print("usage", judge.usage)


if __name__ == "__main__":
    main()
