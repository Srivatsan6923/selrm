"""Probe re-weighting weights (B-AB-probe-rw, after DynaCF): from a model's scores on
rule_v1/abl_probe_blocks (blocks groups plus their near-miss and presentation cases as
probes, meta.probe), the drop in the probability of preferring the base claim when the
case is replaced by a probe, s_g = mean over probes of max(0, sig(d_base) - sig(d_probe)),
d = u(s) - u(s') on the conclusion claim. Weight w_g = max(0.1, 1 - s_g), normalised to
mean 1. Pairs whose preference shifts under edits that should not matter are
down-weighted. Writes {tid: w}.
  python scripts/probe_weights.py --root ROOT --scores_run RUN_ID --set rule_v1/abl_probe_blocks --out FILE"""
import argparse, json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm.formats import dataset_path


def weights(recs, u):
    d = {}
    for r in recs:
        if r["claim_type"] == "conclusion" and r["iid"] in u:
            d.setdefault(r["tid"], {}).setdefault(r["case_kind"], {})[r["claim_role"]] = u[r["iid"]]
    sig = lambda x: 1 / (1 + math.exp(-max(-50, min(50, x))))
    w = {}
    for tid, kinds in d.items():
        dd = {k: v["s"] - v["s_prime"] for k, v in kinds.items() if len(v) == 2}
        if "base" not in dd:
            continue
        drops = [max(0.0, sig(dd["base"]) - sig(dd[k])) for k in ("near", "pres") if k in dd]
        w[tid] = max(0.1, 1 - sum(drops) / len(drops)) if drops else 1.0
    mean = sum(w.values()) / max(1, len(w))
    return {t: v / mean for t, v in w.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--scores_run", required=True)
    ap.add_argument("--set", default="rule_v1/abl_probe_blocks")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    recs = [json.loads(l) for l in open(dataset_path(a.root, a.set), encoding="utf-8")]
    u = {}
    for line in open(f"{a.root}/results/{a.scores_run}/scores_{a.set.replace('/', '~')}.jsonl", encoding="utf-8"):
        row = json.loads(line)
        u[row["iid"]] = row["u"]
    w = weights(recs, u)
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(w, open(a.out, "w"))
    vals = sorted(w.values())
    print(json.dumps({"groups": len(w), "min": vals[0] if vals else None, "median": vals[len(vals) // 2] if vals else None,
                      "share_downweighted": round(sum(v < 1 for v in vals) / max(1, len(vals)), 3)}))


if __name__ == "__main__":
    main()
