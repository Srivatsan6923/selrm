#!/bin/sh
# Init container of every role-B GPU pod (runs before the GPU is used): unpack the
# prebuilt env, copy the code snapshot and the base weights to local NVMe, so the
# GPU container never installs, downloads or reads small files over CephFS.
# Usage: sh stage.sh <env_tag> <code_sha> <model_dir_name> [<model_dir_name> ...]
set -eu
ENVTAG=$1; CODE=$2; shift 2
ROOT=/pvc/selrm
t0=$(date +%s)
tar -xf "$ROOT/env/selrm-env-$ENVTAG.tar" -C /opt
cp -r "$ROOT/code/$CODE" /work/code
mkdir -p /work/models
for m in "$@"; do
  cp -r "$ROOT/models/$m" /work/models/
done
echo "staged env $ENVTAG, code $CODE, models $* in $(( $(date +%s) - t0 )) s"
