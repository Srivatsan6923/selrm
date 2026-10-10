"""results/A-SETS/summary.json: facts of role A's new sets from their MANIFESTs, so prose and tables can
cite them as sum/A-SETS/<set>.<field> (a number in a doc is not an input; docs/RESULT_KEYS.md).

  python scripts/export_set_summaries.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SETS = {"xr_v1": "xr_v1/test", "challenge_v1": "challenge_v1/test", "ec_v1": "ec_v1/test", "rewrite_v1": "rewrite_v1/test",
        "mcv_v1": "mcv_v1/criteria_test", "kb_v1": "kb_v1/triplets_test"}   # stage 2: one manifest per set


def main():
    reg = json.loads((ROOT / "data" / "REGISTRY.json").read_text(encoding="utf-8"))
    out = {"run_id": "A-SETS"}
    for short, name in SETS.items():
        if name in reg:
            m = json.loads((ROOT / "data" / reg[name]["manifest"]).read_text(encoding="utf-8"))
            out[short] = {k: v for k, v in m.items() if k not in ("git_commit", "python", "template_split_hash")}
            out[short]["frozen"] = int(bool(reg[name].get("frozen")))
    if "xr_v1" in out:                              # xr_v1 is reported on 400 items and on 362 without the known issues
        known = json.loads((ROOT / "data" / "xr_v1" / "KNOWN_ISSUES.json").read_text(encoding="utf-8"))
        items = sorted({i for issue in known["issues"] for i in issue["items"]})
        out["xr_v1"]["known_issue_items"] = len(items)
        out["xr_v1"]["n_items_without_known_issues"] = out["xr_v1"]["n_items"] - len(items)
        path = ROOT / "data" / reg["xr_v1/test"]["path"]
        if path.exists():                           # records are rebuilt by build_xr_v1.py --restore
            import importlib.util
            import sys
            sys.path.insert(0, str(ROOT))
            spec = importlib.util.spec_from_file_location("bx", ROOT / "scripts" / "build_xr_v1.py")
            bx = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(bx)
            from selrm import xr
            recs = [json.loads(line) for line in open(path, encoding="utf-8")]
            out["xr_v1"]["validation_without_known_issues"] = {
                k: xr.crossed_accuracy(recs, s, exclude=items) for k, s in bx.scorers(recs).items()}
    acc = ROOT / "results" / "A-MCV-ACCEPT" / "summary.json"
    if acc.exists():
        d = json.loads(acc.read_text(encoding="utf-8"))
        out["mcv_v1_accept"] = {k: d[k] for k in ("n_scores", "n_accepted", "test_rows_covered", "test_human_covered", "train_rows_covered")}
    prep = ROOT / "ec_v1" / "prepare_summary.json"
    if prep.exists():
        out["ec_v1_prepare"] = json.loads(prep.read_text(encoding="utf-8"))
    specs = ROOT / "challenge_v1" / "specs.jsonl"
    if specs.exists():
        rows = [json.loads(l) for l in open(specs, encoding="utf-8")]
        kinds = {}
        for r in rows:
            kinds[r["nm_kind"]] = kinds.get(r["nm_kind"], 0) + 1
        out["challenge_v1_kit"] = {"specs": len(rows), "by_kind": kinds,
                                   "authors": len({r["author"] for r in rows})}
    d = ROOT / "results" / "A-SETS"
    d.mkdir(parents=True, exist_ok=True)
    (d / "summary.json").write_text(json.dumps(out, indent=1, sort_keys=True), encoding="utf-8")
    (d / "DONE").write_text("", encoding="utf-8")
    print(sorted(out))


if __name__ == "__main__":
    main()
