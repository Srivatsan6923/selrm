"""onto_v1, steps 2-4: class closure tables, disjointness and the class split (STAGE2_TASKS_A, A4.2-4).

  python scripts/onto_closure.py           # writes data/onto_v1/classes.json and data/onto_v1/MANIFEST.json

Domains: drug (RxNorm ingredients; class = an ATC level-4 code and an FDA EPC class whose ingredient sets agree),
phenotype (HPO), disease (Mondo). A class comes with its sibling classes (same parent), so the unit of the
60/15/25 split is the sibling family: near-misses of a class never come from another split.
"""
import hashlib
import importlib.util
import json
import re
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "data" / "_ext" / "onto"
OUT = ROOT / "data" / "onto_v1"
SEED = 20261008
MIN_DESC, MAX_DESC = 8, 200
JACCARD, COMMON = 0.5, 4
MIN_MEMBERS = 4                      # usable member names a class needs
FAMILIES = {"phenotype": 90, "disease": 90}   # sibling families drawn per ontology domain (all drug families are kept)
ROOTS = {"phenotype": ("hp.obo", "HP:0000118"), "disease": ("mondo.obo", "MONDO:0700096")}   # phenotypic abnormality; human disease
NAME_OK = re.compile(r"^[A-Za-z][A-Za-z0-9 '\-/]{2,58}$")


def h(*x):
    return hashlib.sha256("/".join(map(str, x)).encode()).hexdigest()


def snap():
    spec = importlib.util.spec_from_file_location("onto_snapshot", ROOT / "scripts" / "onto_snapshot.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def obo(path):
    """{id: {name, parents, synonyms (EXACT)}} of the non-obsolete terms."""
    terms, cur = {}, None
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if ln.startswith("["):
            cur = {"parents": [], "synonyms": []} if ln == "[Term]" else None
            continue
        if cur is None or not ln:
            continue
        k, _, v = ln.partition(": ")
        if k == "id":
            cur["id"] = v
            terms[v] = cur
        elif k == "name":
            cur["name"] = v
        elif k == "is_a":
            cur["parents"].append(v.split(" ! ")[0].split(" {")[0].strip())
        elif k == "synonym":
            m = re.match(r'"(.*)" EXACT', v)
            if m:
                cur["synonyms"].append(m.group(1))
        elif k == "is_obsolete" and v == "true":
            cur["obsolete"] = True
    return {i: t for i, t in terms.items() if not t.get("obsolete") and "name" in t}


def descendants(terms):
    kids = defaultdict(set)
    for i, t in terms.items():
        for p in t["parents"]:
            if p in terms:
                kids[p].add(i)
    memo = {}

    def desc(i):
        if i not in memo:
            memo[i] = set()
            out = set()
            for k in kids[i]:
                out |= {k} | desc(k)
            memo[i] = out
        return memo[i]
    return kids, desc


def names(t):
    """Usable names of a term: label and exact synonyms that read as plain note wording."""
    out = []
    for n in [t["name"]] + t["synonyms"]:
        if NAME_OK.match(n) and not re.search(r"\b(obsolete|abnormality of|abnormal)\b", n, re.I) and n.lower() not in [x.lower() for x in out]:
            out.append(n)
    return out


def ontology_domain(domain):
    fname, root = ROOTS[domain]
    terms = obo(EXT / fname)
    kids, desc = descendants(terms)
    scope = desc(root) | {root}
    cand = {i for i in scope if MIN_DESC <= len(desc(i)) <= MAX_DESC and NAME_OK.match(terms[i]["name"])}
    fams = []
    for p in sorted(scope, key=lambda i: h(SEED, domain, i)):                 # seeded order of parents
        if not names(terms[p]):
            continue
        ch = sorted((c for c in kids[p] if c in cand), key=lambda i: h(SEED, i))
        keep = []
        for c in ch:                                                          # mutually disjoint siblings
            if all(not ((desc(c) | {c}) & (desc(k) | {k})) for k in keep):
                keep.append(c)
        if len(keep) >= 2:
            fams.append((p, keep))
    chosen, used = [], set()
    for p, keep in fams:                                                      # globally disjoint classes
        keep = [c for c in keep if not ((desc(c) | {c}) & used)]
        if len(keep) < 2:
            continue
        classes = []
        for c in keep[:4]:
            ms = [{"id": d, "names": names(terms[d])} for d in sorted(desc(c)) if names(terms[d])]
            if len(ms) >= MIN_MEMBERS:
                classes.append({"id": c, "name": terms[c]["name"], "domain": domain, "members": ms, "n_descendants": len(desc(c))})
        if len(classes) < 2:
            continue
        for c in classes:
            used |= desc(c["id"]) | {c["id"]}
        chosen.append({"family": p, "general": {"id": p, "name": names(terms[p])[0]}, "classes": classes})
        if len(chosen) == FAMILIES[domain]:
            break
    stats = {"terms": len(terms), "in_scope": len(scope), "candidates_8_200_descendants": len(cand),
             "families_with_two_disjoint_siblings": len(fams), "families_kept": len(chosen)}
    return chosen, stats


def drug_domain():
    S = snap()
    raw = json.loads((OUT / "drug_classes_raw.json").read_text(encoding="utf-8"))
    atc = {k: {m[0]: m[1] for m in v} for k, v in raw["atc4"].items()}
    epc = {k: {"name": v["name"], "m": {m[0]: m[1] for m in v["members"]}} for k, v in raw["epc"].items()}
    pairs = []
    for a, am in atc.items():
        for e, ev in epc.items():
            common = set(am) & set(ev["m"])
            if len(common) >= COMMON and len(common) / len(set(am) | set(ev["m"])) >= JACCARD:
                pairs.append((a, e, common))
    best = {}
    for a, e, common in sorted(pairs, key=lambda x: (-len(x[2]), x[0], x[1])):   # one pair per ATC code and per EPC class
        if a not in {x[0] for x in best.values()} and e not in best:
            best[e] = (a, common)
    count = defaultdict(int)
    for e, (a, common) in best.items():
        for m in common:
            count[m] += 1
    classes = []
    for e, (a, common) in sorted(best.items()):
        ms = sorted(m for m in common if count[m] == 1 and "/" not in atc[a][m])     # one class only; no combinations
        if len(ms) >= MIN_MEMBERS:
            classes.append({"id": f"{a}|{e}", "atc4": a, "epc": e, "name": epc[e]["name"], "domain": "drug", "ingredients": ms,
                            "excluded_one_set_only": sorted((set(atc[a]) ^ set(epc[e]["m"]))),
                            "names_of": {m: atc[a][m] for m in ms}})
    ing = sorted({m for c in classes for m in c["ingredients"]})

    def brands(rxcui):
        d = S.rx(f"rxcui/{rxcui}/related.json", tty="BN")
        out = []
        for g in (d.get("relatedGroup") or {}).get("conceptGroup") or []:
            out += [p["name"] for p in g.get("conceptProperties") or []]
        return sorted(set(out))

    def medrt(rxcui):
        d = S.rx("rxclass/class/byRxcui.json", rxcui=rxcui, relaSource="MEDRT")
        rel = (d.get("rxclassDrugInfoList") or {}).get("rxclassDrugInfo") or []
        return sorted({(r["rela"], r["rxclassMinConceptItem"]["classId"]) for r in rel})
    with ThreadPoolExecutor(8) as ex:
        bn = dict(zip(ing, ex.map(brands, ing)))
        mr = dict(zip(ing, ex.map(medrt, ing)))
    selected = set(ing)
    chosen = []
    for c in classes:
        c["members"] = [{"id": f"RXCUI:{m}", "names": [c["names_of"][m]] + [b for b in bn[m] if NAME_OK.match(b)][:3],
                         "medrt": len(mr[m])} for m in c["ingredients"]]
        a, e = c["atc4"], c["epc"]
        sib = {}                                # ingredients of the other level-4 codes under the same level-3 group
        for code, ms in atc.items():
            if code != a and code[:4] == a[:4]:
                for m, name in ms.items():
                    if m not in atc[a] and m not in epc[e]["m"] and m not in selected and "/" not in name and NAME_OK.match(name):
                        sib[m] = name
        c["siblings"] = [{"id": f"RXCUI:{m}", "names": [n]} for m, n in sorted(sib.items())]
        for k in ("ingredients", "names_of"):
            del c[k]
        if len(c["siblings"]) >= 2:
            chosen.append({"family": f"ATC:{a}", "general": None, "classes": [c]})
    stats = {"atc4_with_ingredients": len(atc), "epc_with_ingredients": len(epc), "pairs_meeting_jaccard_and_common": len(pairs),
             "classes_after_one_to_one_and_exclusions": len(classes), "classes_with_two_sibling_ingredients": len(chosen),
             "ingredients": len(ing), "ingredients_with_brand_names": sum(bool(v) for v in bn.values()),
             "medrt_relations": sum(len(v) for v in mr.values())}
    return chosen, stats


def split(fams, domain):
    """60 / 15 / 25 of the sibling families, seeded."""
    order = sorted(fams, key=lambda f: h(SEED, "split", domain, f["family"]))
    n = len(order)
    a, b = round(0.60 * n), round(0.75 * n)
    for i, f in enumerate(order):
        f["split"] = "train" if i < a else "dev" if i < b else "test"
    return order


def main():
    out, stats = {}, {}
    for domain in ("drug", "phenotype", "disease"):
        fams, st = drug_domain() if domain == "drug" else ontology_domain(domain)
        out[domain], stats[domain] = fams, st
    # a name used by more than one selected member (or sibling ingredient) is ambiguous and is dropped
    owner = defaultdict(set)
    for fams in out.values():
        for f in fams:
            for c in f["classes"]:
                for m in c["members"] + c.get("siblings", []):
                    for n in m["names"]:
                        owner[n.lower()].add(m["id"])
    dropped = 0
    for domain, fams in out.items():
        for f in fams:
            for c in f["classes"]:
                for key in ("members", "siblings"):
                    for m in c.get(key, []):
                        keep = [n for n in m["names"] if len(owner[n.lower()]) == 1]
                        dropped += len(m["names"]) - len(keep)
                        m["names"] = keep
                    if key in c:
                        c[key] = [m for m in c[key] if m["names"]]
            f["classes"] = [c for c in f["classes"] if len(c["members"]) >= MIN_MEMBERS]
        out[domain] = [f for f in fams if len(f["classes"]) >= (1 if domain == "drug" else 2)]
        stats[domain]["families_after_dropping_ambiguous_names"] = len(out[domain])
    stats["ambiguous_names_dropped"] = dropped
    for domain in out:
        out[domain] = split(out[domain], domain)
    # disjointness and leakage checks over everything that was selected
    errs = []
    member_names = {"train": set(), "dev": set(), "test": set()}
    seen_ids = {}
    for domain, fams in out.items():
        for f in fams:
            for c in f["classes"]:
                for m in c["members"]:
                    if m["id"] in seen_ids:
                        errs.append(f"{m['id']} in {seen_ids[m['id']]} and {c['id']}")
                    seen_ids[m["id"]] = c["id"]
                    member_names[f["split"]] |= {n.lower() for n in m["names"]}
    for s in ("dev", "test"):
        both = member_names[s] & member_names["train"]
        if both:
            errs.append(f"{len(both)} {s} member names also occur as training members, e.g. {sorted(both)[:5]}")
    for s_ in ("dev", "test"):                           # near-miss ingredients of dev and test are no training members
        for f in out["drug"]:
            if f["split"] == s_:
                for c in f["classes"]:
                    c["siblings"] = [m for m in c["siblings"] if not {n.lower() for n in m["names"]} & member_names["train"]]
    for domain, fams in out.items():
        st = stats[domain]
        for s in ("train", "dev", "test"):
            cs = [c for f in fams if f["split"] == s for c in f["classes"]]
            st[f"{s}_families"], st[f"{s}_classes"] = sum(f["split"] == s for f in fams), len(cs)
            st[f"{s}_members"] = sum(len(c["members"]) for c in cs)
    OUT.mkdir(parents=True, exist_ok=True)
    text = json.dumps(out, indent=0, sort_keys=True)
    (OUT / "classes.json").write_text(text, encoding="utf-8", newline="\n")
    snapshot = json.loads((OUT / "SNAPSHOT.json").read_text(encoding="utf-8"))
    man = {"set": "onto_v1", "seed": SEED, "snapshot": snapshot, "classes_sha256": hashlib.sha256(text.encode()).hexdigest(),
           "rules": {"drug_class": f"an ATC level-4 code and an FDA EPC class with Jaccard >= {JACCARD} and >= {COMMON} common ingredients; members = the intersection; "
                                   "ingredients in one set only, combinations and ingredients of several selected classes are excluded; names shown are EPC names; near-miss ingredients come from the other level-4 codes of the same ATC level-3 group and are members of no selected class",
                     "ontology_class": f"a term with {MIN_DESC}-{MAX_DESC} descendants under the domain root; members = descendants with a usable label or exact synonym; "
                                       "siblings share a parent and are disjoint; selected classes are pairwise disjoint (no subsumption, no common descendant); the parent is the too-general term",
                     "usable_name": NAME_OK.pattern + " and no 'abnormality of' / 'abnormal'",
                     "split": "60 / 15 / 25 of the sibling families per domain, seeded; a class and its siblings share a split"},
           "stats": stats, "violations": errs}
    (OUT / "MANIFEST.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps(stats, indent=1))
    print("violations:", errs[:5] if errs else 0)
    stats_keys = [k for k in stats if isinstance(stats[k], dict)]
    for domain in stats_keys:
        fams = out[domain]
        f = fams[0]
        print(domain, "|", f["family"], "| general:", f["general"], "|", [(c["name"], [m["names"][:2] for m in c["members"][:3]]) for c in f["classes"][:2]])


if __name__ == "__main__":
    sys.exit(main())
