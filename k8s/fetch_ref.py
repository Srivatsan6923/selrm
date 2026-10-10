"""Snapshot of a commit of the project repository -> /pvc/selrm/code/<sha12>, fetched inside the pod with the
read-only token (GH_TOKEN from the secret selrm-github-ro; never printed), for refs too large to upload from the
laptop. Optional pinned external files are downloaded into the snapshot and must match their sha256.
  python fetch_ref.py <full sha> [<path in snapshot>=<url>=<sha256> ...]"""
import hashlib, io, os, shutil, sys, tarfile, urllib.request

REPO = "Srivatsan6923/selrm"


def main():
    full, extra = sys.argv[1], sys.argv[2:]
    dest = f"/pvc/selrm/code/{full[:12]}"
    if not os.path.exists(dest):
        req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/tarball/{full}",
                                     headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"]})
        data = urllib.request.urlopen(req, timeout=600).read()
        tmp = dest + ".tmp"
        shutil.rmtree(tmp, ignore_errors=True)
        with tarfile.open(fileobj=io.BytesIO(data)) as t:
            top = t.getnames()[0].split("/")[0]
            t.extractall(tmp, filter="data")
        open(f"{tmp}/{top}/COMMIT", "w").write(full + "\n")
        os.rename(f"{tmp}/{top}", dest)
        shutil.rmtree(tmp, ignore_errors=True)
    for item in extra:
        path, url, sha = item.split("=")
        out = f"{dest}/{path}"
        if not (os.path.exists(out) and hashlib.sha256(open(out, "rb").read()).hexdigest() == sha):
            data = urllib.request.urlopen(url, timeout=600).read()
            if hashlib.sha256(data).hexdigest() != sha:
                raise SystemExit(f"MISMATCH {path}")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "wb").write(data)
        print("ok", path)
    print("FETCH REF OK", dest)


if __name__ == "__main__":
    main()
