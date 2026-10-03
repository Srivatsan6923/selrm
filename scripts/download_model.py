"""Download a pinned Hugging Face model snapshot (CPU job on NRP).

  python scripts/download_model.py REPO_ID REVISION OUT_DIR
"""
import os
import sys

from huggingface_hub import snapshot_download

repo, rev, out = sys.argv[1:4]
if os.path.exists(os.path.join(out, "REVISION")):
    print("exists:", out)
    sys.exit(0)
snapshot_download(repo_id=repo, revision=rev, local_dir=out)
open(os.path.join(out, "REVISION"), "w").write(rev + "\n")
print("downloaded", repo, rev, "->", out)
