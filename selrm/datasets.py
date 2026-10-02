"""Dataset builders (A-D4, A-D7): group sampling, triplet sets, missing-input
sets, training corpora and manifests (docs/INTERFACES.md section 5).

Group specs: near-miss kind first (equal shares over the kinds the rules
support), then a rule supporting it, a criterion, and a tier by TIER_W
(the alt tier only in L3-alt sets). Group i of a spec list has seed i.

Corpora (train rules, train templates; same group pool, same record count):
  natural   one case per group: 15% pres, 15% missing, the rest flips at 15%
  balanced  one case per group: 15% pres, 15% missing, the rest flips at 50%
  blocks    base + flip per group; pres and missing added to 6 of every 14 groups
  triplets  flip + base (7 of 14 groups) or near (the other 7), same extras
so that presentation and missing cases are 15% of cases each in every corpus.
"""
from __future__ import annotations

import hashlib
import json
import random
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from selrm import engine as E
from selrm import folds as FD
from selrm import phrases as P
from selrm.library import LIBRARY_BY_ID

RULES_BY_ID = dict(LIBRARY_BY_ID)   # plus test-only rules (L3-inv) added by register()
KINDS = ("numeric", "boundary", "subject", "negation", "time")
TIER_W = {"easy": 2, "long": 1, "superseded": 1, "delabelled": 1}
ROOT = Path(__file__).resolve().parents[1]


def _independent(n, counts):
    """One case per group; a block of n groups holds exactly these case counts."""
    return n, lambda rng: [{k} for k in rng.sample([k for k, c in counts.items() for _ in range(c)], n)]


def _paired(core, n_pres=6, n_miss=6):
    """Core cases per group from core(rng); pres and missing each in 6 of 14 groups."""
    def pick(rng):
        cores = core(rng)
        pres, miss = set(rng.sample(range(14), n_pres)), set(rng.sample(range(14), n_miss))
        return [cores[i] | ({"pres"} if i in pres else set()) | ({"missing"} if i in miss else set())
                for i in range(14)]
    return 14, pick


def _triplet_core(rng):
    """Flip in every group; base in 7 of 14, near in the other 7."""
    return [{"flip", k} for k in rng.sample(["base"] * 7 + ["near"] * 7, 14)]


# corpus -> (block size in groups, block -> case kinds per group)
CORPORA = {
    "natural": _independent(200, {"pres": 30, "missing": 30, "flip": 21, "base": 119}),
    "balanced": _independent(20, {"pres": 3, "missing": 3, "flip": 7, "base": 7}),
    "blocks": _paired(lambda rng: [{"base", "flip"}] * 14),
    "triplets": _paired(_triplet_core),
}
# A-D12 ablation: triplets without presentation edits (missing kept near 15%: 5 of 33 cases)
ABLATIONS = {"triplets_nopres": _paired(_triplet_core, 0, 5)}


def register(rules):
    """Makes test-only rules (outside LIBRARY) available to the builders."""
    RULES_BY_ID.update({r.rid: r for r in rules})
    return rules


def options(rules, tier_w=TIER_W):
    """nm_kind -> {rid: [cid, ...]} over criteria that can decide their rule and
    have a tier of tier_w for that kind."""
    out = defaultdict(lambda: defaultdict(list))
    for r in rules:
        for c in r.criteria:
            if E.pivots(r, c):
                for k in E.nm_kinds(c):
                    if any(E._tier_ok(c, k, t) for t in tier_w):
                        out[k][r.rid].append(c.cid)
    return out


def sample_specs(rules, n, seed, tier_w=TIER_W):
    """n group specs (rid, cid, nm_kind, tier) with near-miss kinds in equal shares."""
    rng, opts = random.Random(f"specs.{seed}"), options(rules, tier_w)
    kinds = [k for k in KINDS if opts[k]]
    order = (kinds * (n // len(kinds) + 1))[:n]
    rng.shuffle(order)
    specs = []
    for k in order:
        rid = rng.choice(sorted(opts[k]))
        cid = rng.choice(opts[k][rid])
        c = RULES_BY_ID[rid].crit(cid)
        tiers = [t for t in tier_w if E._tier_ok(c, k, t)]
        specs.append((rid, cid, k, rng.choices(tiers, [tier_w[t] for t in tiers])[0]))
    return specs


def readapply_set(specs, n, set_name, level):
    """Triplets (base, flip, near) of the first n groups that admit reading and
    application pairs, with those pairs (engine.readapply_records)."""
    k = 0
    for i, spec in enumerate(specs):
        recs = E.make_group(RULES_BY_ID[spec[0]], *spec[1:], "test", i, set_name, level,
                            readapply=True)
        if any(r["case_kind"] == "read" for r in recs):
            yield from (r for r in recs if r["case_kind"] != "pres")
            k += 1
            if k == n:
                return
    raise ValueError(f"only {k} of {n} groups admit reading and application pairs")


def groups(specs, split, set_name, level, stats=None, tpl_split=None, missing=False):
    """Yields the records of group i (seed i) for every spec."""
    for i, spec in enumerate(specs):
        yield E.make_group(RULES_BY_ID[spec[0]], *spec[1:], split, i, set_name, level, stats,
                           tpl_split, missing)


def corpus(kind, specs, n_records, set_name="rule_v1", stats=None, claim_types=None, probes=False):
    """Yields the records of one training corpus: walks the group pool block by
    block, keeping the case kinds of its pattern, until n_records are out.
    claim_types: keep only these claim types (A-D12 conclusion-only labels);
    probes: also yield the group's other near and pres cases with meta.probe =
    True, outside the record count (A-D12 probe re-weighting inputs)."""
    size, pattern = {**CORPORA, **ABLATIONS}[kind]
    n, gen = 0, groups(specs, "train", set_name, "L0", stats, missing=True)
    for b in range(len(specs) // size):
        for want in pattern(random.Random(f"{kind}.{b}")):
            for r in next(gen):
                if claim_types and r["claim_type"] not in claim_types:
                    continue
                if r["case_kind"] in want:
                    yield r
                    n += 1
                elif probes and r["case_kind"] in ("near", "pres"):
                    yield dict(r, meta=dict(r["meta"], probe=True))
            if n >= n_records:
                return
    raise ValueError(f"group pool too small for {kind}: {n} < {n_records} records")


def missing_set(test_groups):
    """Missing twins, each with one ordinary case of its group (base or flip,
    alternating) whose supported claim measures false rejection."""
    for i, recs in enumerate(test_groups):
        yield from (r for r in recs if r["case_kind"] in ("missing", ("base", "flip")[i % 2]))


# ---------------------------------------------------------------- manifests
def template_split_hash():
    lists = {"banks": P.BANKS, "fillers": [P.FILLERS, P.FILLERS_OTHER, P.FILLERS_LAB],
             "headers": [P.HEADER, P.HEADER_NO_AGE], "persons": P.PERSONS, "missing": P.MISSING,
             "cues": [P.NEG_CUES, P.TIME_CUES, P.CURRENT_CUES]}
    return hashlib.sha256(json.dumps(lists, sort_keys=True).encode()).hexdigest()


def git_commit():
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
                              text=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def validate_shortcuts(path):
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_shortcuts.py"), str(path)],
                         capture_output=True, text=True)
    return {"result": "PASS" if out.returncode == 0 else "FAIL", "output": out.stdout.strip()}


def describe(rows):
    """rows: (tid, case_kind, rid, nm_kind, tier, level, family, label) per record."""
    first, cases = {}, set()
    for row in rows:
        first.setdefault(row[0], row)
        cases.add(row[:2])
    keys = ("rid", "nm_kind", "tier", "level", "family")
    by = {k: dict(sorted(Counter(g[i + 2] for g in first.values()).items())) for i, k in enumerate(keys)}
    by["class"] = dict(sorted(Counter(FD.sig_class(RULES_BY_ID[g[2]]) for g in first.values()).items()))
    kinds = Counter(row[1] for row in rows)
    return {"n_groups": len(first), "n_cases": len(cases), "n_records": len(rows),
            "cases_by_kind": dict(sorted(Counter(k for _, k in cases).items())),
            "record_share": {k: round(v / len(rows), 4) for k, v in sorted(kinds.items())},
            "labels": {str(k): v for k, v in sorted(Counter(row[7] for row in rows).items())},
            "groups_by": by}


def write(out_dir, name, recs, info, validate=False):
    """Streams records to <out_dir>/<name>/records.jsonl and writes MANIFEST.json."""
    d = Path(out_dir) / name
    d.mkdir(parents=True, exist_ok=True)
    h, rows = hashlib.sha256(), []
    with open(d / "records.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in recs:
            line = json.dumps(r, sort_keys=True) + "\n"
            f.write(line)
            h.update(line.encode("utf-8"))
            rows.append(tuple(r[k] for k in ("tid", "case_kind", "rid", "nm_kind", "tier", "level",
                                             "family", "label")))
    man = dict(info, name=name, **describe(rows), git_commit=git_commit(),
               python=sys.version.split()[0], template_split_hash=template_split_hash(),
               sha256=h.hexdigest())
    man["shortcut_validation"] = validate_shortcuts(d / "records.jsonl") if validate else \
        {"result": "n/a", "output": "no complete triplets (validation runs on triplet sets)"}
    (d / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    return man
