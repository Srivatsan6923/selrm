#!/bin/bash
# Build the Python environment for role-B GPU pods ONCE, in a CPU-only pod, on the
# pod's local disk, and store it on the PVC as a single tarball. NRP forbids pip/conda
# installs on CephFS, so GPU pods unpack the tarball to local NVMe (k8s/stage.sh).
# Self-contained: uv-managed CPython 3.12 + venv under /opt/selrm-env (same path in
# every pod). CUDA extension causal-conv1d is compiled here with nvcc 13.0 for
# A100 (8.0), A40/A6000 (8.6), L40/L40S (8.9), H100 (9.0).
# Usage (CPU Job): bash build_env.sh <env_tag>
set -euo pipefail
TAG=$1
ROOT=/pvc/selrm
ENVD=/opt/selrm-env
OUT=$ROOT/env/selrm-env-$TAG.tar
mkdir -p "$ENVD" "$ROOT/env"
[ -f "$OUT" ] && { echo "exists: $OUT"; exit 0; }

apt-get update -qq && apt-get install -y -qq --no-install-recommends curl ca-certificates > /dev/null
curl -LsSf https://github.com/astral-sh/uv/releases/download/0.12.22/uv-x86_64-unknown-linux-gnu.tar.gz \
  | tar -xz -C /usr/local/bin --strip-components=1
export UV_CACHE_DIR=/tmp/uv-cache UV_PYTHON_INSTALL_DIR=$ENVD/python UV_LINK_MODE=copy
uv python install 3.12
uv venv --python 3.12 "$ENVD/venv"
PY=$ENVD/venv/bin/python

# Pins: newest set allowed by unsloth 2026.9.14 (transformers<=5.5.0, trl<=0.24.0,
# datasets<4.4, torch<2.13); torch 2.11.0+cu130 is the stack measured on Colab.
uv pip install --python "$PY" --index-url https://pypi.org/simple \
  --extra-index-url https://download.pytorch.org/whl/cu130 --index-strategy unsafe-best-match \
  "torch==2.11.0+cu130" "torchvision==0.26.0+cu130" \
  "unsloth==2026.9.14" "unsloth_zoo==2026.9.9" "transformers==5.5.0" "trl==0.24.0" \
  "datasets==4.3.0" "flash-linear-attention==0.5.2" "fla-core==0.5.2" \
  numpy ninja packaging setuptools wheel huggingface_hub

export CUDA_HOME=/usr/local/cuda TORCH_CUDA_ARCH_LIST="8.0;8.6;8.9;9.0" MAX_JOBS=${MAX_JOBS:-6} \
       CAUSAL_CONV1D_FORCE_BUILD=TRUE
uv pip install --python "$PY" --no-build-isolation "causal-conv1d==1.7.0"

"$PY" - <<'EOF'
import importlib.metadata as m
for p in ("torch", "torchvision", "triton", "transformers", "trl", "peft", "accelerate", "datasets",
          "unsloth", "unsloth_zoo", "flash-linear-attention", "fla-core", "causal-conv1d", "xformers",
          "bitsandbytes", "numpy", "huggingface_hub"):
    try:
        print(p, m.version(p))
    except m.PackageNotFoundError:
        print(p, "MISSING")
import torch, transformers, trl, peft, fla           # unsloth needs a GPU to import; checked in B-T0
print("torch cuda build", torch.version.cuda)
try:
    import causal_conv1d
    print("causal_conv1d import ok")
except Exception as e:                             # may need libcuda (GPU node); checked in B-T0
    print("causal_conv1d import deferred:", type(e).__name__, e)
EOF
uv pip freeze --python "$PY" > "$ROOT/env/selrm-env-$TAG.freeze.txt"
du -sh "$ENVD"
tar -cf "$OUT.tmp" -C /opt selrm-env
mv "$OUT.tmp" "$OUT"
ls -la "$OUT"
echo "BUILD OK $TAG"
