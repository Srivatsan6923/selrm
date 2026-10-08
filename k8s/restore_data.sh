#!/bin/bash
# Publish one of role A's frozen sets that has its own builder with a --restore mode (e.g.
# scripts/build_xr_v1.py: rebuilds the records and writes them only if they match the sha256 in A's
# registry). The sha256 is checked again here before the set and its registry entry reach the PVC.
# Usage (CPU Job): bash restore_data.sh <env_tag> <code_sha_of_A> <set name> <builder script> [args...]
#   e.g. bash restore_data.sh v1 efe0128c1a2b xr_v1/test scripts/build_xr_v1.py
set -euo pipefail
ENVTAG=$1; CODE=$2; NAME=$3; shift 3
ROOT=/pvc/selrm
tar -xf "$ROOT/env/selrm-env-$ENVTAG.tar" -C /opt
PY=/opt/selrm-env/venv/bin/python
cp -r "$ROOT/code/$CODE" /tmp/code
cd /tmp/code
# builders that derive a set from frozen parents (e.g. scripts/build_aux_corpora.py) read the parents' records,
# which are not in git: COPY every verified record file on the PVC into the snapshot's data/ (a symlink would let
# a builder that rewrites its outputs write through to a frozen set on the PVC)
( cd "$ROOT/data" && find . -name records.jsonl ) | while read -r f; do
  [ -e "data/$f" ] || { mkdir -p "data/$(dirname "$f")"; cp "$ROOT/data/$f" "data/$f"; }
done
"$PY" "$@" --restore
NAME="$NAME" "$PY" - <<'EOF'
import hashlib, json, os, shutil
name, root = os.environ["NAME"], "/pvc/selrm/data"
e = json.load(open("data/REGISTRY.json"))[name]
src = os.path.dirname(f"data/{e['path']}")
h = hashlib.sha256(open(f"data/{e['path']}", "rb").read()).hexdigest()
if h != e["sha256"]:
    raise SystemExit(f"MISMATCH {name}: {h[:12]} vs {e['sha256'][:12]}")
dst = f"{root}/{os.path.dirname(e['path'])}"
if not os.path.exists(dst):            # frozen sets are immutable; an existing copy was verified before
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copytree(src, dst + ".tmp")
    os.replace(dst + ".tmp", dst)
reg = json.load(open(f"{root}/REGISTRY.json"))
reg[name] = e
json.dump(reg, open(f"{root}/REGISTRY.json.tmp", "w"), indent=1, sort_keys=True)
os.replace(f"{root}/REGISTRY.json.tmp", f"{root}/REGISTRY.json")
print("published", name, h[:12])
EOF
echo "RESTORE DATA OK"
