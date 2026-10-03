"""docs/AUX_PROTOCOL.md S1 epoch selection (secondary analysis): for each dataset whose five epoch adapters have been
scored on its dev split (B-AUX-<ds>-ep5-s0-e<k>, recipe 1, seed 0), the primary metric after each epoch; the
smallest epoch count with the best value is fixed in configs/aux_epochs.json ("chosen") for every recipe and seed
of that dataset. A dataset already fixed is never changed (the protocol: no epoch count changes after the first
scored run). Metrics as fixed by C: NLI4CT mean of faithfulness and consistency (C's scripts/eval_clinical.py
nli_metrics, read from --c_ref), MedEinst pair reversal, TrialGPT macro-F1 over met / not met / NEI on the non-N/A
items with the trained-model rule (NEI iff max(u_s, u_s') < 0 or u_s = u_s'). Dev records come from the local data
copy (report_b.DATA).
  python scripts/aux_epochs.py [--c_ref origin/role-c]"""
import argparse, collections, json, os, subprocess, sys, types
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from eval_local import pair_reversal
from make_queue_b import AUX_DS, AUX_EPOCHS
from report_b import DATA, RG
from selrm.metrics import prf


def scores(rid, set_name):
    p = f"{RG}/{rid}/scores_{set_name.replace('/', '~')}.jsonl"
    return {r["iid"]: r["u"] for r in map(json.loads, open(p, encoding="utf-8"))} if os.path.exists(p) else None


def trialgpt_f1(recs, u):
    items = collections.defaultdict(dict)
    for r in recs:
        items[r["tid"]][r["claim_role"]] = u[r["iid"]]
        items[r["tid"]]["gold"] = r["meta"]["category"]
    gold, pred = [], []
    for it in items.values():
        if it["gold"] == "na":
            continue
        us, usp = it["s"], it["s_prime"]
        gold.append(it["gold"])
        pred.append("nei" if max(us, usp) < 0 or us == usp else "met" if us > usp else "not_met")
    return prf(gold, pred, ("met", "not_met", "nei"))["macroF1"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--c_ref", default="origin/role-c")
    a = ap.parse_args()
    reg = json.load(open(f"{DATA}/REGISTRY.json"))
    out = json.load(open(AUX_EPOCHS)) if os.path.exists(AUX_EPOCHS) else {"chosen": {}, "dev": {}}
    nli = None
    for ds, c in AUX_DS.items():
        ep = f"B-AUX-{ds}-ep5-s0"
        if ds in out["chosen"] or not all(os.path.exists(f"{RG}/{ep}-e{k}/DONE") for k in range(1, 6)):
            continue
        recs = [json.loads(l) for l in open(f"{DATA}/{reg[c['dev']]['path']}", encoding="utf-8")]
        dev = {}
        for k in range(1, 6):
            u = scores(f"{ep}-e{k}", c["dev"])
            R = [r for r in recs if r["iid"] in u]
            if ds == "trialgpt":
                dev[k] = trialgpt_f1(R, u)
            elif ds == "medeinst":
                dev[k] = pair_reversal(R, [u[r["iid"]] for r in R])["Reversal"]
            else:
                if nli is None:                  # C's scorer, unchanged (it imports only the stdlib and selrm.metrics)
                    src = subprocess.run(["git", "-C", ROOT, "show", f"{a.c_ref}:scripts/eval_clinical.py"],
                                         capture_output=True, text=True, encoding="utf-8", check=True).stdout
                    nli = types.ModuleType("eval_clinical_c")
                    nli.__file__ = os.path.join(ROOT, "scripts", "eval_clinical_c.py")
                    exec(compile(src, "eval_clinical.py", "exec"), nli.__dict__)
                pred = {r["meta"]["uuid"]: "Entailment" if u[r["iid"]] > 0 else "Contradiction" for r in R}
                m = nli.nli_metrics(R, pred)
                dev[k] = (m["Faithfulness"] + m["Consistency"]) / 2
        best = max(dev.values())
        out["chosen"][ds] = min(k for k, v in dev.items() if v == best)
        out["dev"][ds] = {"metric": {"trialgpt": "macro-F1", "medeinst": "pair reversal",
                                     "nli4ct": "mean of faithfulness and consistency"}[ds],
                          "set": c["dev"], "by_epoch": dev, "runs": [f"{ep}-e{k}" for k in range(1, 6)]}
        print(ds, "dev by epoch", {k: round(v, 4) for k, v in dev.items()}, "-> epochs", out["chosen"][ds])
    json.dump(out, open(AUX_EPOCHS, "w", encoding="utf-8", newline="\n"), indent=1)


if __name__ == "__main__":
    main()
