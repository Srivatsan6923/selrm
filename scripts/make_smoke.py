"""Build smoke_v2 in the canonical schema: held-out rules AND held-out templates.
Usage: python scripts/make_smoke.py [out_dir] [n_train_groups]"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import smoke as S
from selrm.schema import validate

out = sys.argv[1] if len(sys.argv) > 1 else "data/smoke_v2"
n_train = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
os.makedirs(out, exist_ok=True)
seen, held = S.split_rules()
train = S.generate(n_train, 1, seen, "smoke_v2", "train", S.TRAIN_TPL)
files = {
    "train_blocks": S.corpus(train, "blocks"),
    "train_triplets": S.corpus(train, "triplets"),
    "dev_seen_rules": [r for t in S.generate(300, 2, seen, "smoke_v2", "dev", S.TEST_TPL) for r in t],
    "test_heldout_rules": [r for t in S.generate(600, 3, held, "smoke_v2", "test", S.TEST_TPL) for r in t],
}
manifest = {"set": "smoke_v2", "heldout_rules": list(S.HELDOUT_RULES),
            "train_templates": S.TRAIN_TPL, "test_templates": S.TEST_TPL, "files": {}}
for name, recs in files.items():
    for r in recs:
        validate(r)
    with open(f"{out}/{name}.jsonl", "w") as f:
        for r in recs:
            f.write(json.dumps(r) + "\n")
    manifest["files"][name] = {"records": len(recs), "groups": len({r["tid"] for r in recs})}
json.dump(manifest, open(f"{out}/MANIFEST.json", "w"), indent=2)
print(json.dumps(manifest, indent=2))
