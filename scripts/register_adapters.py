"""Add every finished run whose adapter is kept on the PVC to configs/adapters.json (for C and D).
A run counts when results_git/<run>/ has DONE and its meta.json says keep_adapter; existing systems keep their
names, new ones are named by run_id. Idempotent.
  python scripts/register_adapters.py"""
import glob, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    p = f"{ROOT}/configs/adapters.json"
    reg = json.load(open(p, encoding="utf-8"))
    known = {v.get("run_id") for v in reg["systems"].values()}
    added = []
    for meta in sorted(glob.glob(f"{ROOT}/results_git/B-*/meta.json")):
        d = os.path.dirname(meta)
        m = json.load(open(meta, encoding="utf-8"))
        rid = m["run_id"]
        trained = isinstance(m.get("train"), dict) and m["train"].get("steps") and not m["train"].get("eval_only")
        if (rid in known or rid.startswith(("B-C0", "B-T0")) or not m.get("keep_adapter") or not trained
                or not str(m.get("adapter_path") or "").endswith(f"/adapters/{rid}") or m.get("kind") == "concept"
                or not os.path.exists(f"{d}/DONE")):
            continue                    # only trained runs whose own adapter directory was kept
        reg["systems"][rid] = {"run_id": rid, "path": None, "status": f"DONE (seed {m['seed']}); on the PVC",
                               "base_model": f"{m['model']}@{m['model_revision']}", "format": m["format"],
                               "corpus": m["corpus"], "pvc": "selrm-b", "pvc_path": f"selrm/adapters/{rid}"}
        added.append(rid)
    for v in list(reg["systems"].values()):     # stage-2 names (STAGE2_SPEC section 6): <format>_<corpus>_s<seed>
        parts = str(v.get("run_id")).split("-")
        if parts[:2] == ["B", "F"] and len(parts) == 5 and "alias_of" not in v:
            reg["systems"].setdefault(f"{parts[2]}_{parts[3]}_{parts[4]}", v | {"alias_of": v["run_id"]})
        if parts[:2] == ["B", "MIX"] and len(parts) == 4 and "alias_of" not in v:     # mix_blocks_s0
            reg["systems"].setdefault(f"mix_{parts[2]}_{parts[3]}", v | {"alias_of": v["run_id"]})
    open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(reg, indent=1, ensure_ascii=False) + "\n")
    print(f"{len(added)} added: {', '.join(added)}")


if __name__ == "__main__":
    main()
