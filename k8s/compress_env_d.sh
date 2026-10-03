#!/bin/sh
# Gzip copies of D's env tarballs (half the bytes to read from CephFS when a GPU pod stages the env
# outside us-west). Usage (CPU Job): sh k8s/compress_env_d.sh v1 v2
set -eu
for t in "$@"; do
  f=/pvc/env/selrm-d-env-$t.tar
  [ -f "$f.gz" ] && { echo "exists: $f.gz"; continue; }
  gzip -1 -c "$f" > "$f.gz.tmp" && mv "$f.gz.tmp" "$f.gz"
  ls -la "$f" "$f.gz"
done
echo "COMPRESS OK"
