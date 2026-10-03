#!/bin/bash
# Role D's Python environment (vLLM for candidate pools and selection scoring), built ONCE
# in a CPU pod on local disk and stored on D's PVC as one tarball: NRP forbids pip installs
# on CephFS, so GPU pods unpack it to local NVMe (stage_d.sh). Same layout as role B's
# k8s/build_env.sh: uv-managed CPython 3.12 + venv under /opt/selrm-env.
# Pins verified 2 Oct 2026 on PyPI: vllm 0.30.0 (requires torch==2.13.0,
# transformers>=5.10.4) supports Qwen3_5ForConditionalGeneration (vllm registry.py).
# Usage (CPU Job, PVC mounted at /pvc): bash build_env_d.sh <tag>
set -euo pipefail
TAG=$1
ENVD=/opt/selrm-env
OUT=/pvc/env/selrm-d-env-$TAG.tar
mkdir -p "$ENVD" /pvc/env
[ -f "$OUT" ] && { echo "exists: $OUT"; exit 0; }
apt-get update -qq && apt-get install -y -qq --no-install-recommends curl ca-certificates > /dev/null
curl -LsSf https://github.com/astral-sh/uv/releases/download/0.12.22/uv-x86_64-unknown-linux-gnu.tar.gz \
  | tar -xz -C /usr/local/bin --strip-components=1
export UV_CACHE_DIR=/tmp/uv-cache UV_PYTHON_INSTALL_DIR=$ENVD/python UV_LINK_MODE=copy
uv python install 3.12
uv venv --python 3.12 "$ENVD/venv"
PY=$ENVD/venv/bin/python
uv pip install --python "$PY" "vllm==0.30.0" peft pandas pyarrow numpy scipy huggingface_hub
"$PY" - <<'EOF'
import importlib.metadata as m
for p in ("vllm", "torch", "transformers", "peft", "triton", "xformers", "flashinfer-python", "numpy", "pandas"):
    try:
        print(p, m.version(p))
    except m.PackageNotFoundError:
        print(p, "MISSING")
import torch
print("torch cuda build", torch.version.cuda)
EOF
uv pip freeze --python "$PY" > "/pvc/env/selrm-d-env-$TAG.freeze.txt"
du -sh "$ENVD"
tar -cf "$OUT.tmp" -C /opt selrm-env
mv "$OUT.tmp" "$OUT"
ls -la "$OUT"
echo "BUILD OK $TAG"
