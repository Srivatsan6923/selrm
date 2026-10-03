#!/bin/bash
# Rebuild role A's frozen datasets inside the cluster (Drive is not reachable from NRP) and
# publish them on the PVC only if every records.jsonl matches the sha256 in A's registry.
# Usage (CPU Job): bash build_data.sh <env_tag> <code_sha_of_A> <build args...>
#   e.g. bash build_data.sh v1 113f176c825c --fold 2   (one at a time: each updates the PVC registry)
# Expects data/REGISTRY.json (A's frozen registry, committed by A) inside the code snapshot.
set -euo pipefail
ENVTAG=$1; CODE=$2; shift 2
ROOT=/pvc/selrm
tar -xf "$ROOT/env/selrm-env-$ENVTAG.tar" -C /opt
PY=/opt/selrm-env/venv/bin/python
cp -r "$ROOT/code/$CODE" /tmp/code
cd /tmp/code
test -f data/REGISTRY.json || { echo "no data/REGISTRY.json in code $CODE"; exit 2; }
# folds 2-3 read the fold assignment frozen with rule_v1 from <out>/rule_v1/FOLDS.json (as in A's build)
if [ -f data/rule_v1/FOLDS.json ]; then mkdir -p /tmp/data/rule_v1 && cp data/rule_v1/FOLDS.json /tmp/data/rule_v1/; fi
"$PY" scripts/build_rule_v1.py --out /tmp/data "$@"
"$PY" - <<'EOF'
import hashlib, json, os, shutil, sys
exp = json.load(open("data/REGISTRY.json"))
built = json.load(open("/tmp/data/REGISTRY.json"))
ok, bad = [], []
for name, e in built.items():
    if name not in exp:
        bad.append(f"{name}: built but not in A's registry"); continue
    h = hashlib.sha256(open(f"/tmp/data/{e['path']}", "rb").read()).hexdigest()
    (ok if h == exp[name]["sha256"] else bad).append(f"{name}: {h[:12]} vs {exp[name]['sha256'][:12]}")
print("match:", len(ok)); [print("  ", x) for x in ok]
if bad:
    print("MISMATCH:"); [print("  ", x) for x in bad]; sys.exit(1)
root = "/pvc/selrm/data"
for name, e in built.items():           # publish set by set (tmp dir + rename), registry last
    src, dst = f"/tmp/data/{os.path.dirname(e['path'])}", f"{root}/{os.path.dirname(e['path'])}"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(dst):
        continue                       # frozen sets are immutable; an existing copy was verified before
    shutil.copytree(src, dst + ".tmp")
    os.replace(dst + ".tmp", dst)
reg = json.load(open(f"{root}/REGISTRY.json")) if os.path.exists(f"{root}/REGISTRY.json") else {}
reg.update({k: exp[k] for k in built})
reg.update({k: v for k, v in exp.items() if v.get("alias_of") in reg})   # A's alias names of published sets
json.dump(reg, open(f"{root}/REGISTRY.json.tmp", "w"), indent=1, sort_keys=True)
os.replace(f"{root}/REGISTRY.json.tmp", f"{root}/REGISTRY.json")
print("published", len(built), "sets to", root)
EOF
echo "BUILD DATA OK"
