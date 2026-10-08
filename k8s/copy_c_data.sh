#!/bin/bash
# Copy role C's frozen clin_v1 sets from C's PVC (selrm-c, mounted read-only at /c; C's tree is /c/selrmc) to B's
# PVC, verifying the sha256 in C's registry (data/clin_v1/REGISTRY_C.json in C's code snapshot on B's PVC, made by
# submit_b.py push-ref origin/role-c), with each set's MANIFEST.json; then add the registry entries to B's.
# Usage (CPU Job): bash copy_c_data.sh <env_tag> <code_sha_of_C> <set name> [...]
#   e.g. bash copy_c_data.sh v1 a1377b9c1d2e clin_v1/clinpairs_medeinst_dis clin_v1/medeinst_dis_test
set -euo pipefail
ENVTAG=$1; CCODE=$2; shift 2
ROOT=/pvc/selrm
tar -xf "$ROOT/env/selrm-env-$ENVTAG.tar" -C /opt
/opt/selrm-env/venv/bin/python - "$ROOT/code/$CCODE" "$@" <<'EOF'
import hashlib, json, os, shutil, sys
code, names, root = sys.argv[1], sys.argv[2:], "/pvc/selrm/data"
reg_c = json.load(open(f"{code}/data/clin_v1/REGISTRY_C.json"))
reg = json.load(open(f"{root}/REGISTRY.json"))
print("C's PVC clin_v1:", sorted(os.listdir("/c/selrmc/data/clin_v1")) if os.path.isdir("/c/selrmc/data/clin_v1") else "none")
for name in names:
    e = reg_c[name]
    src = next((p for p in (f"/c/selrmc/data/{e['path']}", f"{code}/data/{e['path']}") if os.path.exists(p)), None)
    if src is None:                          # neither on C's PVC nor in C's git: reported, the others still copied
        print("MISSING", name, e["path"])
        continue
    h = hashlib.sha256(open(src, "rb").read()).hexdigest()
    if h != e["sha256"] or not e.get("frozen"):
        raise SystemExit(f"MISMATCH or not frozen {name}: {h[:12]} vs {e['sha256'][:12]}")
    d = f"{root}/{os.path.dirname(e['path'])}"
    if os.path.exists(d):                 # an existing copy must be the registered version, never assumed to be
        hd = hashlib.sha256(open(f"{root}/{e['path']}", "rb").read()).hexdigest()
        if hd != e["sha256"]:
            raise SystemExit(f"EXISTING COPY DIFFERS {name}: {hd[:12]} on B's PVC vs {e['sha256'][:12]} registered")
    if not os.path.exists(d):
        os.makedirs(d + ".tmp", exist_ok=True)
        shutil.copyfile(src, f"{d}.tmp/{os.path.basename(e['path'])}")
        man = f"{code}/data/{os.path.dirname(e['path'])}/MANIFEST.json"
        if os.path.exists(man):
            shutil.copyfile(man, f"{d}.tmp/MANIFEST.json")
        os.replace(d + ".tmp", d)
    reg[name] = e
    print("copied", name, h[:12], e.get("n_records"))
reg = json.load(open(f"{root}/REGISTRY.json")) | {n: reg[n] for n in names if n in reg}   # re-read: keep concurrent writes
json.dump(reg, open(f"{root}/REGISTRY.json.tmp", "w"), indent=1, sort_keys=True)
os.replace(f"{root}/REGISTRY.json.tmp", f"{root}/REGISTRY.json")
EOF
echo "COPY C DATA OK"
