"""Merge part runs <RUN>--p<k> (same system, code and settings; disjoint sets) into one run directory <RUN>, so
that one run id holds every set of a system (D's tables read one run per row). No GPU.
  python scripts/merge_parts.py RUN [--results results_git]
Copies scores_*, summary_* and reader audits of every DONE part; meta.json = the first part's meta with
'parts' (each part's run id, sets, seconds, GPU, node), union of sets, summed wall seconds; DONE written last.
Refuses if a set occurs in two parts or a part is not DONE."""
import argparse, glob, json, os, shutil, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("run")
    ap.add_argument("--results", default=f"{REPO}/results_git")
    a = ap.parse_args()
    parts = sorted(glob.glob(f"{a.results}/{a.run}--p*"))
    if not parts or not all(os.path.exists(f"{p}/DONE") for p in parts):
        sys.exit(f"not every part of {a.run} is DONE: {parts}")
    out, seen, metas = f"{a.results}/{a.run}", {}, []
    os.makedirs(out, exist_ok=True)
    for p in parts:
        m = json.load(open(f"{p}/meta.json", encoding="utf-8"))
        metas.append(m)
        for f in sorted(os.listdir(p)):
            if f.startswith(("scores_", "summary_")):
                if f in seen:
                    sys.exit(f"{f} in {seen[f]} and {p}")
                seen[f] = p
                shutil.copyfile(f"{p}/{f}", f"{out}/{f}")
    meta = dict(metas[0]) | {"run_id": a.run, "sets": [s for m in metas for s in m.get("sets", [])],
                             "wall_seconds": sum(m.get("wall_seconds") or 0 for m in metas),
                             "eval_seconds_by_set": {k: v for m in metas for k, v in (m.get("eval_seconds_by_set") or {}).items()},
                             "summaries": {k: v for m in metas for k, v in (m.get("summaries") or {}).items()},
                             "parts": [{"run_id": m["run_id"], "sets": m.get("sets"), "wall_seconds": m.get("wall_seconds"),
                                        "gpu": m.get("gpu"), "node": m.get("node"), "git_commit": m.get("git_commit")}
                                       for m in metas],
                             "merged": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    json.dump(meta, open(f"{out}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)
    open(f"{out}/DONE", "w").write(meta["merged"] + "\n")
    print(f"merged {len(parts)} parts into {out}: {len(seen)} files")


if __name__ == "__main__":
    main()
