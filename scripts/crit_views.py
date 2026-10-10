"""Criterion views (STAGE2_SPEC section 5): identical records with rule_text replaced and the iid suffixed @<cond>.
  python scripts/crit_views.py --set rule_v1/test_L2 --cond none|wrong [--data scratch/rv1] [--out data]
Handlers: rule_v1 (controls of the rule tier; C1), mcv_v1 (C3), kb_v1 (C4).
  none   rule text removed ('').
  wrong  the rule text of another rule of the same set, the same for every case and claim of a group: drawn with
         random.Random('<SEED>|<tid>') from the sorted texts of other rules that mention none of the group's claims
         (case-insensitive, claim text without its final full stop).
Labels are untouched: they stay the labels under the rule that generated the case, so a view measures how much
of a system's accuracy survives without (or against) the stated rule. Writes <out>/views/<set>@<cond>/records.jsonl
and MANIFEST.json, and registers the view (frozen) in <out>/clin_v1/REGISTRY_C.json."""
import argparse, collections, hashlib, json, os, random, subprocess, sys, time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEED = 20261008
NL = chr(10)


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rule_v1(recs, cond):
    """-> {tid: (text, provenance)}"""
    groups = collections.defaultdict(list)
    for r in recs:
        groups[r["tid"]].append(r)
    if cond == "none":
        return {t: ("", "rule text removed") for t in groups}
    texts = collections.defaultdict(set)            # rule text -> rids
    for r in recs:
        texts[r["rule_text"]].add(r["rid"])
    out = {}
    for tid, g in sorted(groups.items()):
        claims = {r["claim_text"].rstrip(".").lower() for r in g}
        cands = sorted(t for t, rids in texts.items() if g[0]["rid"] not in rids and not any(c in t.lower() for c in claims))
        t = random.Random(f"{SEED}|{tid}").choice(cands)
        out[tid] = (t, f"rule text of {sorted(texts[t])[0]}")
    return out


def mcv_v1(recs, cond):
    """MedCalc-V: none = no score text (the claim still names the score); wrong = the definition of another score,
    one per score: random.Random('<SEED>|<score id>') over the sorted definitions of the other scores."""
    tids = {r["tid"]: r["rid"] for r in recs}
    if cond == "none":
        return {t: ("", "score text removed") for t in tids}
    text = {}
    for r in recs:
        text.setdefault(r["rid"], r["rule_text"])
    other = {}
    for rid in sorted(text):
        c = random.Random(f"{SEED}|{rid}").choice(sorted(k for k in text if k != rid and text[k] != text[rid]))
        other[rid] = (text[c], f"score text of {c}")
    return {t: other[rid] for t, rid in tids.items()}


def kb_v1(recs, cond):
    """Derived criterion (kb_v1): none = no lists; wrong = lists exchanged: the headings of the two exclusive
    lists ('Findings listed for <diagnosis> only:') swap places, so each list stands under the other diagnosis."""
    out = {}
    for r in recs:
        if r["tid"] in out:
            continue
        if cond == "none":
            out[r["tid"]] = ("", "criterion text removed")
            continue
        L = r["rule_text"].split("\n")
        h = [i for i, x in enumerate(L) if x.startswith("Findings listed for ") and x.endswith(" only:")]
        assert len(h) == 2, r["tid"]
        L[h[0]], L[h[1]] = L[h[1]], L[h[0]]
        out[r["tid"]] = ("\n".join(L), "exclusive lists exchanged")
    return out


def _swap(text):
    L = text.split(NL)
    h = [i for i, x in enumerate(L) if x.startswith("Findings listed for ") and x.endswith(" only:")]
    assert len(h) == 2
    L[h[0]], L[h[1]] = L[h[1]], L[h[0]]
    return NL.join(L)


def clin_v1(recs, cond):
    """MedEinst test pairs (C4): derived = the criterion of the pair's two diagnoses rendered from the DDXPlus lists
    (role A's selrm/kb_criterion.render; the same text for both cases of a pair and for every pair with these two
    diagnoses); wrong = the same text with the two exclusive lists exchanged."""
    sys.path.insert(0, f"{REPO}/scratch/acode_s2")
    from selrm import kb_criterion as K
    out = {}
    for r in recs:
        if r["tid"] not in out:
            t = K.render(r["meta"]["y_gt"], r["meta"]["y_bias"])
            out[r["tid"]] = (t, "selrm.kb_criterion.render") if cond == "derived" else (_swap(t), "exclusive lists exchanged")
    return out


HANDLERS = {"rule_v1": rule_v1, "mcv_v1": mcv_v1, "kb_v1": kb_v1, "clin_v1": clin_v1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", required=True)
    ap.add_argument("--cond", required=True, choices=["none", "wrong", "derived"])
    ap.add_argument("--data", default=os.environ.get("SELRM_DATA", f"{REPO}/scratch/rv1"))
    ap.add_argument("--out", default=f"{REPO}/data")
    a = ap.parse_args()
    ap_reg = "clin_v1/REGISTRY_C.json" if a.set.startswith("clin_v1") else "REGISTRY.json"
    reg_src = json.load(open(f"{a.data}/{ap_reg}", encoding="utf-8"))
    recs = [json.loads(l) for l in open(f"{a.data}/{reg_src[a.set]['path']}", encoding="utf-8")]
    new = HANDLERS[a.set.split("/")[0]](recs, a.cond)
    name = f"{a.set}@{a.cond}"
    out = []
    for r in recs:
        text, prov = new[r["tid"]]
        out.append(r | {"iid": f"{r['iid']}@{a.cond}", "rule_text": text,
                        "crit": {"source": a.cond, "provenance": prov, "text_sha": sha(text)}, "cluster": r.get("cluster", r["rid"])})
    d = f"{a.out}/views/{name}"
    os.makedirs(d, exist_ok=True)
    with open(f"{d}/records.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in out:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    h = hashlib.sha256(open(f"{d}/records.jsonl", "rb").read()).hexdigest()
    by_tid = collections.defaultdict(set)
    for r in out:
        by_tid[r["tid"]].add(r["rule_text"])
    leak = sum(r["claim_text"].rstrip(".").lower() in r["rule_text"].lower() for r in out)
    man = {"name": name, "parent": a.set, "parent_sha256": reg_src[a.set]["sha256"], "cond": a.cond, "seed": SEED,
           "builder": "scripts/crit_views.py", "n_records": len(out), "n_groups": len(by_tid),
           "shortcut_validation": {
               "one_text_per_group": all(len(v) == 1 for v in by_tid.values()),
               "records_whose_rule_text_mentions_their_claim": leak,
               "text_equals_parent_text": sum(o["rule_text"] == r["rule_text"] for o, r in zip(out, recs)),
               "note": "labels, cases and claims are the parent's, so the parent's shortcut validation applies to the "
                       "case side; the view's text is independent of case and label (one text per group)"},
           "git_commit": subprocess.run(["git", "-C", REPO, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(),
           "sha256": h, "created": time.strftime("%Y-%m-%d"), "frozen": True}
    json.dump(man, open(f"{d}/MANIFEST.json", "w", encoding="utf-8", newline="\n"), indent=1)
    regp = f"{a.out}/clin_v1/REGISTRY_C.json"
    reg = json.load(open(regp, encoding="utf-8"))
    reg[name] = {"path": f"views/{name}/records.jsonl", "split": "test", "level": reg_src[a.set].get("level"),
                 "tier": "view", "n_groups": len(by_tid), "n_records": len(out), "manifest": f"views/{name}/MANIFEST.json",
                 "frozen": True, "created": man["created"], "sha256": h, "parent": a.set}
    json.dump(reg, open(regp, "w", encoding="utf-8", newline="\n"), indent=1, sort_keys=True)
    print(name, len(out), "records", len(by_tid), "groups", h[:12], man["shortcut_validation"])


if __name__ == "__main__":
    main()
