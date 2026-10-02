#!/bin/bash
# CPU-only preparation for role-B GPU queues (single writer, run as a CPU Job):
# rebuild smoke_v2 in the cluster and check its hashes against the laptop build,
# download the pinned base weights once, pre-tokenise every run of a queue.
# Usage: bash prep.sh <env_tag> <code_sha> <queue_file_name>
set -euo pipefail
ENVTAG=$1; CODE=$2; QUEUE=$3
ROOT=/pvc/selrm
tar -xf "$ROOT/env/selrm-env-$ENVTAG.tar" -C /opt
PY=/opt/selrm-env/venv/bin/python
cp -r "$ROOT/code/$CODE" /tmp/code
cd /tmp/code

if [ ! -f "$ROOT/data/smoke_v2/HASHES_OK" ]; then
  "$PY" scripts/make_smoke.py /tmp/smoke_v2 > /dev/null
  "$PY" - <<'EOF'
import hashlib, json, sys
exp = json.load(open("configs/smoke_v2_sha256.json"))["sha256_lf"]
bad = [f for f, h in exp.items() if hashlib.sha256(open(f"/tmp/smoke_v2/{f}", "rb").read()).hexdigest() != h]
print("smoke_v2 hash mismatch:", bad) if bad else print("smoke_v2 hashes match the laptop build")
sys.exit(1 if bad else 0)
EOF
  mkdir -p "$ROOT/data"
  rm -rf "$ROOT/data/smoke_v2.tmp" && cp -r /tmp/smoke_v2 "$ROOT/data/smoke_v2.tmp"
  rm -rf "$ROOT/data/smoke_v2" && mv "$ROOT/data/smoke_v2.tmp" "$ROOT/data/smoke_v2"
  date -u +%FT%TZ > "$ROOT/data/smoke_v2/HASHES_OK"
fi

HF_HUB_DISABLE_XET=1 "$PY" - <<'EOF'
import json, os
from huggingface_hub import snapshot_download
root = "/pvc/selrm/models"
for m in [m for m in json.load(open("configs/models_b.json"))["models"] if m.get("prefetch")]:
    d = f"{root}/{m['id'].replace('/', '--')}"
    if os.path.exists(f"{d}/REVISION") and open(f"{d}/REVISION").read().strip() == m["revision"]:
        print("present", m["id"], m["revision"]); continue
    snapshot_download(m["id"], revision=m["revision"], local_dir=d + ".tmp",
                      allow_patterns=m.get("allow_patterns"), max_workers=2)   # bounded memory (pod OOM at 8 Gi with defaults)
    open(f"{d}.tmp/REVISION", "w").write(m["revision"] + "\n")     # written before the rename
    if os.path.exists(d):
        os.replace(d, d + ".old")
    os.replace(d + ".tmp", d)
    if os.path.exists(d + ".old"):
        import shutil
        shutil.rmtree(d + ".old")
    print("downloaded", m["id"], m["revision"])
EOF

"$PY" scripts/pretok.py --root "$ROOT" --queue "$ROOT/queue/$QUEUE"
echo "PREP OK $QUEUE"
