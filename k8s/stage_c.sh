#!/bin/sh
# Init container of every role-C GPU pod: unpack B's prebuilt env (read-only volume /pvcb),
# copy B's code snapshot (scoring code), C's code snapshot and the base weights to local NVMe.
# Usage: sh stage_c.sh <env_tag> <b_code_sha> <c_code_sha> <model_dir_name> [...]
set -eu
ENVTAG=$1; BCODE=$2; CODE=$3; shift 3
t0=$(date +%s)
tar -xf "/pvcb/selrm/env/selrm-env-$ENVTAG.tar" -C /opt
cp -r "/pvcb/selrm/code/$BCODE" /work/bcode
cp -r "/pvc/selrmc/code/$CODE" /work/code
mkdir -p /work/models
for m in "$@"; do
  cp -r "/pvcb/selrm/models/$m" /work/models/
done
echo "staged env $ENVTAG, B code $BCODE, C code $CODE, models $* in $(( $(date +%s) - t0 )) s"
