"""Training-side rewrites under the rule of rewrite_v2: rule_v1x/train_triplets_rw2 and train_blocks_rw2.

  python scripts/rewrite_train_v2.py [--workers 64]      # builds, registers and freezes both corpora

scripts/rewrite_train.py with the prompts and the ledger anchoring of scripts/rewrite_v2.py (fixed on
rule_v1/dev). Same parents, same share (25% of the groups), same seeded order of candidate groups as the
first corpora (rule_v1x/train_*_rw), which stay frozen. The first script builds into a scratch folder under
its own names; this script files the result under the new names.
"""
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))
import rewrite_train as T  # noqa: E402

spec = importlib.util.spec_from_file_location("rewrite_v2", ROOT / "scripts" / "rewrite_v2.py")
V = importlib.util.module_from_spec(spec)
spec.loader.exec_module(V)
RT = T.RT
EP = {"temperature": 0, "seed": 2026, "max_tokens": 2000, "response_format": {"type": "json_object"}}
SCRATCH = ROOT / "data" / "rule_v1x" / "_rw2_build"
NAMES = {"train_triplets_rw": "train_triplets_rw2", "train_blocks_rw": "train_blocks_rw2"}


def anchored(rec, note, mentions, crit, decimals):
    """rewrite_v2's anchoring: either extractor's quote (the second extraction is read from the cache)."""
    rule = T.D.RULES_BY_ID[rec["rid"]]
    raw = RT.call(RT.EXTRACTORS[1], RT.EXTRACT.format(concepts=RT.concepts_text(rule), note=note), EP, cache=T.CACHE)
    try:
        second = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])["mentions"]
    except (ValueError, KeyError, TypeError):
        second = []
    return V.anchored(rec, note, [mentions, second], crit)


def main():
    reg_path = ROOT / "data" / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    if any(registry.get(f"rule_v1x/{n}", {}).get("frozen") for n in NAMES.values()):
        sys.exit("refusing to rebuild: the rw2 corpora are frozen")
    RT.REWRITE, RT.EXTRACT = V.REWRITE, V.EXTRACT
    RT.anchored_ledger = anchored
    first = ROOT / "results" / "A-D11-train" / "summary.json"
    keep = first.read_text(encoding="utf-8")                 # T.main() writes its summary to this path
    workers = sys.argv[sys.argv.index("--workers") + 1] if "--workers" in sys.argv else "64"
    sys.argv = [sys.argv[0], "--workers", workers, "--out", str(SCRATCH)]
    try:
        T.main()
        s = json.loads(first.read_text(encoding="utf-8"))
    finally:
        first.write_text(keep, encoding="utf-8")
    s["run_id"] = "A-D11-train-v2"
    s["rule"] = "prompts and ledger anchoring of scripts/rewrite_v2.py (fixed on rule_v1/dev)"
    out = ROOT / "results" / "A-D11-train-v2"
    out.mkdir(parents=True, exist_ok=True)
    (out / "summary.json").write_text(json.dumps(s, indent=1), encoding="utf-8")
    (out / "DONE").write_text("")
    for old, new in NAMES.items():
        src = SCRATCH / "rule_v1x" / old
        text = (src / "records.jsonl").read_text(encoding="utf-8")
        m = json.loads((src / "MANIFEST.json").read_text(encoding="utf-8"))
        assert T.sha(text) == m["sha256"]
        m.update(name=new, frozen=True, generator="scripts/rewrite_train_v2.py", build_command="python scripts/rewrite_train_v2.py")
        m["rewriting"]["rule"] = s["rule"]
        d = ROOT / "data" / "rule_v1x" / new
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text(text, encoding="utf-8", newline="\n")
        (d / "MANIFEST.json").write_text(json.dumps(m, indent=1, sort_keys=True), encoding="utf-8")
        registry[f"rule_v1x/{new}"] = {"path": f"rule_v1x/{new}/records.jsonl", "split": "train", "level": "L0", "n_groups": m["n_groups"],
                                      "n_records": m["n_records"], "manifest": f"rule_v1x/{new}/MANIFEST.json", "frozen": True,
                                      "created": m["created"], "sha256": m["sha256"], "derived_from": T.PARENTS[old]}
    reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps({k: s[k] for k in ("groups_tried", "groups_accepted", "acceptance_rate", "reasons")}))


if __name__ == "__main__":
    main()
