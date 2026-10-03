"""Resources per scored claim (D-RES; App. G "Resources"), from the runs' own meta.json files.

  python scripts/resources.py            # -> results/D-RES/summary.json (+ DONE)

For each system: forward passes per claim (by its interface: verdict 1; rationale = one
generation + the scoring pass; two-stage = reader generation, shared by the claims of a case
and condition, + judge pass), generated tokens per claim and per reader unit (meta
eval_generated_tokens over the records and reader units of the sets it evaluated; record
counts from data/REGISTRY.json, reader units from the summaries), evaluation GPU-seconds per
1,000 claims and the GPU. Runs not finished are left out. Keys: sum/D-RES/<system>.<field>.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSTEMS = {"verdict": ("B-F-verdict-triplets-s0", 1), "rationale": ("B-F-rationale-triplets-s0", 2),
           "summary2": ("B-F-summary2-triplets-s0", 2), "ledger2": ("B-F-ledger2-triplets-s0", 2),
           "genprm": ("B-TR-genprm-s0", 2)}


def run_dir(rid):
    for top in ("results", "results_git"):
        d = os.path.join(ROOT, top, rid)
        if os.path.exists(os.path.join(d, "DONE")):
            return d
    return None


def main():
    reg = json.load(open(os.path.join(ROOT, "data", "REGISTRY.json"), encoding="utf-8"))
    out = {"run_id": "D-RES", "note": __doc__.strip().split("\n")[0], "systems": {}}
    for name, (rid, passes) in SYSTEMS.items():
        d = run_dir(rid)
        if not d:
            continue
        m = json.load(open(os.path.join(d, "meta.json"), encoding="utf-8"))
        sets = m.get("eval_sets") or []
        claims = sum(reg[s]["n_records"] for s in sets if s in reg)
        units = 0
        for s in sets:
            p = os.path.join(d, f"summary_{s.replace('/', '~')}.json")
            if os.path.exists(p):
                units += (json.load(open(p, encoding="utf-8")).get("eval") or {}).get("reader_units") or 0
        gen = m.get("eval_generated_tokens") or 0
        out["systems"][name] = {
            "run_id": rid, "passes_per_claim": passes, "claims": claims, "reader_units": units or None,
            "generated_tokens": gen, "generated_tokens_per_claim": gen / claims if claims else None,
            "generated_tokens_per_reader_unit": gen / units if units else None,
            "eval_gpu_seconds": m.get("eval_seconds"),
            "eval_gpu_seconds_per_1000_claims": 1000 * m["eval_seconds"] / claims if claims and m.get("eval_seconds") else None,
            "gpu": (m.get("gpu") or "").split(",")[0], "eval_sets": sets}
    os.makedirs(os.path.join(ROOT, "results", "D-RES"), exist_ok=True)
    json.dump(out, open(os.path.join(ROOT, "results", "D-RES", "summary.json"), "w", encoding="utf-8", newline="\n"),
              indent=1)
    open(os.path.join(ROOT, "results", "D-RES", "DONE"), "w").close()
    for k, v in out["systems"].items():
        print(k, {f: (round(x, 2) if isinstance(x, float) else x) for f, x in v.items() if f != "eval_sets"})


if __name__ == "__main__":
    main()
