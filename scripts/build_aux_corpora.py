"""rule_v1x/aux_blocks_20k and rule_v1x/aux_triplets_20k: 20,000-record subsamples of the frozen
rule_v1/train_blocks and rule_v1/train_triplets corpora (NEXT_TASKS_A item 1), for the auxiliary-supervision
grid of docs/AUX_PROTOCOL.md (S1, a secondary analysis specified on 3 Oct after the planned comparisons
(4)-(6) failed).

  python scripts/build_aux_corpora.py            # build, check, freeze and register both sets
  python scripts/build_aux_corpora.py --restore  # rewrite the records of the frozen sets and check their sha256

Both parent corpora walk the same group pool in blocks of 14 groups (selrm/datasets.py corpus()), and their
first 5,617 groups are identical and in the same order. The subsamples take whole groups of the 401
complete blocks, in one seeded block order for both corpora, until 20,000 records are reached at a group
boundary (the parents' own stopping rule). Both sets therefore hold the same groups up to the shorter one,
whole blocks keep the parents' case proportions (base/near-miss, presentation, missing input), and every
line is byte-identical to a line of its parent, so the records are verdict-ready as they are.
"""
import argparse
import datetime
import hashlib
import json
import os
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from selrm import datasets as D  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PARENTS = {"aux_blocks_20k": "rule_v1/train_blocks", "aux_triplets_20k": "rule_v1/train_triplets"}
N, BLOCK, SEED = 20000, 14, "rule_v1x.aux_20k"
PURPOSE = ("Auxiliary supervision for the secondary analysis S1 of docs/AUX_PROTOCOL.md (near-miss rule data next "
           "to in-domain medical training), specified on 3 Oct 2026 after the planned comparisons (4)-(6) failed.")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parent_groups(name, registry):
    """[(tid, n_records, start_byte, end_byte)] of a frozen parent in file order, read in one streaming pass
    that also checks its sha256 against the registry (the parents are ~120 MB; nothing is held in memory)."""
    path, h, groups, pos = DATA / registry[name]["path"], hashlib.sha256(), [], 0
    with open(path, "rb") as f:
        for line in f:
            h.update(line)
            tid = json.loads(line)["tid"]
            if not groups or groups[-1][0] != tid:
                groups.append([tid, 0, pos, pos])
            groups[-1][1] += 1
            pos += len(line)
            groups[-1][3] = pos
    if h.hexdigest() != registry[name]["sha256"]:
        sys.exit(f"{name}: records do not match the registry's sha256; rebuild the parent first")
    return [tuple(g) for g in groups]


def select(groups, order):
    """Group indices in the seeded block order, whole groups, until N records."""
    picked, n = [], 0
    for b in order:
        for g in range(b * BLOCK, min((b + 1) * BLOCK, len(groups))):
            if n >= N:
                return picked, n
            picked.append(g)
            n += groups[g][1]
    if n < N:
        sys.exit(f"pool too small: {n} < {N} records")
    return picked, n


def read_lines(name, registry, groups, picked):
    """The picked groups' lines, verbatim and in parent order."""
    with open(DATA / registry[name]["path"], "rb") as f:
        out = []
        for g in sorted(picked):
            f.seek(groups[g][2])
            out.append(f.read(groups[g][3] - groups[g][2]).decode("utf-8"))
    return "".join(out).splitlines(keepends=True)


def build(registry):
    G = {k: parent_groups(p, registry) for k, p in PARENTS.items()}
    common = min(len(g) for g in G.values())
    assert [g[0] for g in G["aux_blocks_20k"][:common]] == [g[0] for g in G["aux_triplets_20k"][:common]], \
        "the parents' groups differ"
    n_blocks = common // BLOCK
    order = list(range(n_blocks))
    random.Random(SEED).shuffle(order)
    out = {}
    for k, groups in G.items():
        picked, _ = select(groups, order)
        out[k] = (picked, read_lines(PARENTS[k], registry, groups, picked))
    shared = set(out["aux_blocks_20k"][0]) & set(out["aux_triplets_20k"][0])
    return out, shared, n_blocks


def describe(lines):
    recs = [json.loads(x) for x in lines]
    return {"n_records": len(recs), "n_groups": len({r["tid"] for r in recs}),
            "cases_by_kind": dict(Counter(r["case_kind"] for r in recs if r["claim_role"] == "s"
                                          and r["claim_type"] == "conclusion")),
            "records_by_case_kind": dict(Counter(r["case_kind"] for r in recs)),
            "records_by_claim_type": dict(Counter(r["claim_type"] for r in recs)),
            "labels": dict(Counter(r["label"] for r in recs)),
            "labels_without_missing_input": dict(Counter(r["label"] for r in recs if r["case_kind"] != "missing")),
            "by_nm_kind": dict(Counter(r["nm_kind"] for r in recs if r["case_kind"] == "flip" and r["claim_role"] == "s"
                                       and r["claim_type"] == "conclusion")),
            "rules": len({r["rid"] for r in recs})}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--restore", action="store_true")
    a = ap.parse_args()
    reg_path = DATA / "REGISTRY.json"
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    out, shared, n_blocks = build(registry)
    created = datetime.date.today().isoformat()
    for k, (picked, lines) in out.items():
        name, d = f"rule_v1x/{k}", DATA / "rule_v1x" / k
        text = "".join(lines)
        digest = sha(text)
        if registry.get(name, {}).get("frozen"):
            if not a.restore:
                sys.exit(f"refusing to rebuild: {name} is frozen (use --restore to write its records)")
            if digest != registry[name]["sha256"]:
                sys.exit(f"refusing to restore {name}: sha256 {digest[:16]} differs from the registry")
            d.mkdir(parents=True, exist_ok=True)
            (d / "records.jsonl").write_text(text, encoding="utf-8", newline="\n")
            print(f"restored {name}: sha256 matches")
            continue
        if a.restore:
            sys.exit(f"{name} is not frozen yet; run without --restore")
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text(text, encoding="utf-8", newline="\n")
        parent = PARENTS[k]
        pm = json.loads((DATA / registry[parent]["manifest"]).read_text(encoding="utf-8"))
        man = {"name": k, "set": "rule_v1x", "split": "train", "level": "L0", "templates": "train",
               "corpus": pm.get("corpus"), "created": created, "frozen": True, "sha256": digest,
               "generator": "scripts/build_aux_corpora.py", "build_command": "python scripts/build_aux_corpora.py",
               "git_commit": D.git_commit(), "purpose": PURPOSE,
               "derived_from": {"name": parent, "sha256": registry[parent]["sha256"],
                                "rule": f"whole groups of the {n_blocks} complete {BLOCK}-group blocks shared by both "
                                        f"parents, blocks in the order random.Random('{SEED}').shuffle(range({n_blocks})), "
                                        f"until {N:,} records at a group boundary; lines copied verbatim, in parent order",
                                "groups_taken": len(picked), "groups_shared_with_sibling": len(shared),
                                "template_split_hash": pm.get("template_split_hash")},
               **describe(lines),
               "shortcut_validation": {"result": "n/a", "output": "training corpus without complete triplets; the "
                                                                    "parent's validation applies (validation runs on "
                                                                    "triplet sets)"}}
        (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
        registry[name] = {"path": f"rule_v1x/{k}/records.jsonl", "split": "train", "level": "L0",
                          "n_groups": man["n_groups"], "n_records": man["n_records"],
                          "manifest": f"rule_v1x/{k}/MANIFEST.json", "frozen": True, "created": created,
                          "sha256": digest, "derived_from": parent}
        print(f"{name} frozen: {man['n_records']} records, {man['n_groups']} groups ({len(shared)} shared), "
              f"sha256 {digest[:16]}")
    if not a.restore:
        reg_path.write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")


if __name__ == "__main__":
    main()
