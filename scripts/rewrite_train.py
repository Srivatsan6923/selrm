"""rule_v1x/train_triplets_rw and rule_v1x/train_blocks_rw (NEXT_TASKS_A item 4): the frozen training corpora
with the text of 25% of their groups replaced by clinical-note rewrites that pass rewrite_v1's two-extractor
check (scripts/rewrite_tier.py: same rewriter, extractors, prompts and acceptance rule).

  python scripts/rewrite_train.py                # API calls (OPENROUTER_API_KEY), cached; builds both corpora
  python scripts/rewrite_train.py --freeze       # also freeze and register them
  python scripts/rewrite_train.py --dry-run      # whole path without API: identity rewrite, gold extraction

Groups: the two parents share their first 5,617 groups (same tids, same order). Candidates are those shared
groups in a seeded order; each candidate's cases (every case kind either corpus uses: base, flip, near,
presentation, missing input) are rewritten once, and the group is accepted only if both extractors recover
every case's state. The first accepted groups in candidate order, up to 25% of the larger corpus, replace
their text in both corpora, so the two corpora carry the same rewrites. States, labels and claims are
unchanged; ledger quotes are re-anchored in the rewritten text. Only training groups and training-template
text are ever rewritten (the prompts hold no examples). Every API response is cached under
data/rule_v1x/rw_cache/, so the corpora rebuild without calls.
"""
import argparse
import concurrent.futures as cf
import datetime
import hashlib
import json
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rewrite_tier as RT  # noqa: E402
from selrm import datasets as D  # noqa: E402
from selrm import phrases as P  # noqa: E402
from selrm.schema import validate  # noqa: E402
from selrm.smoke import ledger_to_prose  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PARENTS = {"train_triplets_rw": "rule_v1/train_triplets", "train_blocks_rw": "rule_v1/train_blocks"}
SHARE, SEED = 0.25, "rule_v1x.rw"
CACHE = DATA / "rule_v1x" / "rw_cache"
TEST_CUES = re.compile(r"(?i)\b(" + "|".join(map(re.escape, P.NEG_CUES["test"] + P.TIME_CUES["test"]
                                                    + P.CURRENT_CUES["test"])) + r")\b")


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parent_groups(name, registry):
    """{tid: [(record, raw line)]} of a frozen parent and its tids in file order (sha256 checked); unchanged
    records are written back as their raw lines, byte for byte."""
    path, h = DATA / registry[name]["path"], hashlib.sha256()
    G, order = defaultdict(list), []
    with open(path, "rb") as f:
        for line in f:
            h.update(line)
            r = json.loads(line)
            if r["tid"] not in G:
                order.append(r["tid"])
            G[r["tid"]].append((r, line.decode("utf-8")))
    if h.hexdigest() != registry[name]["sha256"]:
        sys.exit(f"{name}: records do not match the registry's sha256; rebuild the parent first")
    return G, order


def gold_extraction(r, crit):
    """What a perfect extractor returns for record r: its named mentions, plus each ledger quote of the
    target concept (a general absence line included) as a mention with that quote."""
    ms = [{"concept": m["concept"], "value": m["value"] if m["kind"] == "numeric" else None,
           "subject": m["subject"], "status": m["status"], "time": m["time"], "quote": None}
          for m in r["state"] if m["form"] != "generic"]
    for e in r["ledger"]:
        if e["found"] != "not mentioned" and crit.kind != "numeric":
            subj = "patient" if e["subject"] == "patient" else e["subject"][len("other ("):-1]
            ms.append({"concept": crit.concept, "value": None, "subject": subj, "status": e["status"],
                       "time": "current" if e["time"] == "current" else "past", "quote": e["found"]})
    return ms


def rewrite_group(tid, recs, rp, ep, dry):
    """Rewrite every case of a group, check it with both extractors, and build its rewritten records;
    (ok, why, {iid: rewritten record})."""
    rule = D.RULES_BY_ID[recs[0]["rid"]]
    crit = rule.crit(recs[0]["cid"])
    decimals = {c.concept: c.decimals for c in rule.criteria}
    case = {}
    for r in recs:
        if r["claim_role"] == "s" and (r["case_kind"] not in case or r["claim_type"] == "conclusion"):
            case[r["case_kind"]] = r
    notes, first = {}, {}
    for k, r in sorted(case.items()):
        if dry:                                    # identity rewrite and gold extraction: tests the path
            notes[k], first[k] = r["case_text"], gold_extraction(r, crit)
            named = [m for m in first[k] if m["quote"] is None]
            if not RT.accepts(r, named, decimals):
                return False, f"{k}: gold state rejected", {}
            continue
        notes[k] = RT.call(RT.REWRITER, RT.REWRITE.format(case=r["case_text"]), rp, cache=CACHE).strip()
        for x in RT.EXTRACTORS:
            raw = RT.call(x, RT.EXTRACT.format(concepts=RT.concepts_text(rule), note=notes[k]), ep, cache=CACHE)
            try:
                ms = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])["mentions"]
            except (ValueError, KeyError, TypeError):
                return False, f"{k}: {x} unparsable", {}
            if x == RT.EXTRACTORS[0]:
                first[k] = ms
            if not RT.accepts(r, ms, decimals):
                return False, f"{k}: {x} state differs", {}
    new = {}
    for r in recs:                                 # both corpora's records of the group, rewritten once
        if r["iid"] in new:
            continue
        rec = rewritten(r, notes[r["case_kind"]], first[r["case_kind"]], crit)
        if rec is None:
            return False, f"{r['case_kind']}: ledger quote not in note", {}
        new[r["iid"]] = rec
    return True, "", new


def rewritten(r, note, mentions, crit):
    """Record r with its case text replaced, ledger re-anchored and prose re-rendered (None if a quote is
    missing from the note)."""
    rule = D.RULES_BY_ID[r["rid"]]
    led = RT.anchored_ledger(r, note, mentions, {"kind": crit.kind, "concept": crit.concept},
                             {c.concept: c.decimals for c in rule.criteria})
    if led is None:
        return None
    meta = dict(r["meta"], rewritten={"rewriter": RT.REWRITER, "extractors": list(RT.EXTRACTORS),
                                      "source_tid": r["tid"], "original_tpl": r["meta"].get("tpl", [])}, tpl=[])
    return dict(r, case_text=note, ledger=led, prose=ledger_to_prose(led), meta=meta)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--freeze", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", default=str(DATA))
    a = ap.parse_args()
    out_root = Path(a.out)
    registry = json.loads((DATA / "REGISTRY.json").read_text(encoding="utf-8"))
    G = {k: parent_groups(p, registry) for k, p in PARENTS.items()}
    trip, blocks = G["train_triplets_rw"], G["train_blocks_rw"]
    shared = [t for t in blocks[1] if t in trip[0]]
    target = math.ceil(SHARE * max(len(trip[1]), len(blocks[1])))
    cand = list(shared)
    random.Random(SEED).shuffle(cand)
    rp = {"temperature": 0.7, "seed": 2026, "max_tokens": 900}
    ep = {"temperature": 0, "seed": 2026, "max_tokens": 2000, "response_format": {"type": "json_object"}}
    results, accepted, i = {}, [], 0
    with cf.ThreadPoolExecutor(a.workers) as pool:
        while len(accepted) < target and i < len(cand):
            chunk = cand[i:i + max(50, 2 * (target - len(accepted)))]
            i += len(chunk)
            union = {t: [r for r, _ in trip[0][t] + blocks[0][t]] for t in chunk}
            for t, res in zip(chunk, pool.map(lambda t: rewrite_group(t, union[t], rp, ep, a.dry_run), chunk)):
                results[t] = res
            accepted = [t for t in cand[:i] if results[t][0]][:target]
    if len(accepted) < target:
        sys.exit(f"only {len(accepted)} of {target} groups accepted from {len(cand)} candidates")
    tried = cand[:cand.index(accepted[-1]) + 1]
    acc = set(accepted)
    stats, created = {}, datetime.date.today().isoformat()
    for k, (g, order) in G.items():
        lines, n_rw, cue_hits = [], 0, 0
        for t in order:
            for r, raw in g[t]:
                if t not in acc:
                    lines.append(raw)                  # unchanged record: the frozen line itself
                    continue
                new = results[t][2][r["iid"]]
                validate(new)
                n_rw += 1
                cue_hits += bool(TEST_CUES.search(new["case_text"]))
                lines.append(json.dumps(new, sort_keys=True) + "\n")
        stats[k] = {"lines": lines, "records_rewritten": n_rw, "records_with_test_cue_words": cue_hits}
    summary = {"run_id": "A-D11-train", "groups_tried": len(tried), "groups_accepted": len(accepted),
               "acceptance_rate": 100.0 * len(accepted) / len(tried), "target_share": SHARE,
               "reasons": dict(Counter(results[t][1].split(":")[-1].strip() for t in tried if not results[t][0])),
               "rewriter": RT.REWRITER, "extractors": list(RT.EXTRACTORS), "routes": RT.ROUTES,
               "rewrite_params": rp, "extract_params": ep,
               "dry_run": a.dry_run, "date": created}
    for k, s in stats.items():
        name, d = f"rule_v1x/{k}", out_root / "rule_v1x" / k
        text = "".join(s["lines"])
        d.mkdir(parents=True, exist_ok=True)
        (d / "records.jsonl").write_text(text, encoding="utf-8", newline="\n")
        parent = PARENTS[k]
        man = {"name": k, "set": "rule_v1x", "split": "train", "level": "L0", "templates": "train + rewritten",
               "created": created, "frozen": a.freeze and not a.dry_run, "sha256": sha(text),
               "generator": "scripts/rewrite_train.py", "build_command": "python scripts/rewrite_train.py --freeze",
               "git_commit": D.git_commit(), "derived_from": {"name": parent, "sha256": registry[parent]["sha256"]},
               "n_records": len(s["lines"]), "n_groups": len(G[k][1]), "groups_rewritten": len(accepted),
               "records_rewritten": s["records_rewritten"],
               "records_rewritten_with_test_cue_words": s["records_with_test_cue_words"],
               "rewriting": {x: summary[x] for x in ("groups_tried", "groups_accepted", "acceptance_rate", "reasons",
                                                     "rewriter", "extractors", "routes", "rewrite_params", "extract_params")},
               "shortcut_validation": {"result": "n/a", "output": "training corpus without complete triplets"}}
        (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
        if man["frozen"]:
            if registry.get(name, {}).get("frozen"):
                sys.exit(f"refusing to rebuild: {name} is frozen")
            registry[name] = {"path": f"rule_v1x/{k}/records.jsonl", "split": "train", "level": "L0",
                              "n_groups": man["n_groups"], "n_records": man["n_records"],
                              "manifest": f"rule_v1x/{k}/MANIFEST.json", "frozen": True, "created": created,
                              "sha256": man["sha256"], "derived_from": parent}
        print(f"{name}: {man['n_records']} records, {len(accepted)} groups rewritten "
              f"({s['records_rewritten']} records), sha256 {man['sha256'][:16]}")
    if not a.dry_run:
        res = ROOT / "results" / "A-D11-train"
        res.mkdir(parents=True, exist_ok=True)
        (res / "summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
        (res / "DONE").write_text("")
        if a.freeze:
            (DATA / "REGISTRY.json").write_text(json.dumps(registry, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("groups_tried", "groups_accepted", "acceptance_rate", "reasons")}))


if __name__ == "__main__":
    main()
