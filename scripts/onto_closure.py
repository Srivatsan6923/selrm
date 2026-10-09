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
    """Drug classes: FDA EPC classes by their direct ingredient members (amended rule of 8 Oct, see
    docs/CHANGE_REQUESTS.md). A class whose members also agree with one ATC level-4 code (Jaccard and common
    members as in the first rule) carries agreement = True, so results can be reported on that subset."""
    S = snap()
    raw = json.loads((OUT / "drug_classes_raw.json").read_text(encoding="utf-8"))
    atc = {k: {m[0]: m[1] for m in v} for k, v in raw["atc4"].items()}
    trans = {k: {m[0] for m in v["members"]} for k, v in raw["epc"].items()}          # with members of sub-classes
    epc_name = {c["classId"]: c["className"] for c in S.classes("EPC")}

    def direct(cid):
        d = S.rx("rxclass/classMembers.json", classId=cid, relaSource="DAILYMED", rela="has_EPC", ttys="IN", trans=1)
        ms = (d.get("drugMemberGroup") or {}).get("drugMember") or []
        return {m["minConcept"]["rxcui"]: m["minConcept"]["name"] for m in ms}
    with ThreadPoolExecutor(8) as ex:
        epc = {k: v for k, v in zip(sorted(epc_name), ex.map(direct, sorted(epc_name))) if v}
    owner = defaultdict(int)
    for ms in epc.values():
        for m in ms:
            owner[m] += 1
    atc_of, group = defaultdict(set), defaultdict(dict)
    for code, ms in atc.items():
        for m, n in ms.items():
            atc_of[m].add(code)
            if "/" not in n:
                group[code[:4]][m] = n
    classes = []
    for e in sorted(epc):
        ms = sorted(m for m, n in epc[e].items() if owner[m] == 1 and "/" not in n)   # one class only; no combinations
        if len(ms) < MIN_MEMBERS:
            continue
        agree = sorted(a for a, am in atc.items() if len(set(am) & set(epc[e])) >= COMMON
                       and len(set(am) & set(epc[e])) / len(set(am) | set(epc[e])) >= JACCARD)
        classes.append({"id": f"EPC:{e}", "epc": e, "name": epc_name[e], "domain": "drug", "ingredients": ms,
                        "agreement": bool(agree), "atc4": agree, "names_of": {m: epc[e][m] for m in ms}})
    ing = sorted({m for c in classes for m in c["ingredients"]})

    def brands(rxcui):
        d = S.rx(f"rxcui/{rxcui}/related.json", tty="BN")
        out = []
        for g in (d.get("relatedGroup") or {}).get("conceptGroup") or []:
            out += [p["name"] for p in g.get("conceptProperties") or []]
        return sorted(set(out))
    with ThreadPoolExecutor(8) as ex:
        bn = dict(zip(ing, ex.map(brands, ing)))
    member_of = {m: c["id"] for c in classes for m in c["ingredients"]}       # selected class of an ingredient
    chosen = []
    for c in classes:
        e = c["epc"]
        c["members"] = [{"id": f"RXCUI:{m}", "names": [c["names_of"][m]] + [b for b in bn[m] if NAME_OK.match(b)][:3]}
                        for m in c["ingredients"]]
        # Near-miss ingredients: from the members' ATC level-3 groups, with an FDA class of their own (so the
        # label does not rest on a drug the FDA lists leave unclassified), sharing no ATC level-4 code with a
        # member, and outside the class and its sub-classes.
        own4 = {code for m in epc[e] for code in atc_of[m]}
        sib = {}
        for m in c["ingredients"]:
            for code in atc_of[m]:
                for x, name in group[code[:4]].items():
                    if (x in owner and x not in epc[e] and x not in trans.get(e, ()) and not (atc_of[x] & own4)
                            and NAME_OK.match(name)):
                        sib[x] = name
        c["siblings"] = [{"id": f"RXCUI:{m}", "names": [n], "member_of": member_of.get(m)} for m, n in sorted(sib.items())]
        for k in ("ingredients", "names_of"):
            del c[k]
        if len(c["siblings"]) >= 2:
            chosen.append({"family": c["id"], "general": None, "classes": [c]})
    stats = {"epc_classes_with_direct_ingredients": len(epc), "classes_with_4_exclusive_single_ingredients": len(classes),
             "classes_with_two_near_miss_ingredients": len(chosen),
             "classes_agreeing_with_an_atc_level4_code": sum(f["classes"][0]["agreement"] for f in chosen),
             "ingredients": len(ing), "ingredients_with_brand_names": sum(bool(v) for v in bn.values())}
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
    split_of = {c["id"]: f["split"] for f in out["drug"] for c in f["classes"]}
    for f in out["drug"]:                                # a near-miss from a selected class stays inside its split
        for c in f["classes"]:
            c["siblings"] = [m for m in c["siblings"] if m["member_of"] is None or split_of.get(m["member_of"]) == f["split"]]
    out["drug"] = [f for f in out["drug"] if len(f["classes"][0]["siblings"]) >= 2]
    stats["drug"]["classes_with_two_near_miss_ingredients_in_split"] = len(out["drug"])
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
           "rules": {"drug_class": f"an FDA EPC class by its direct ingredient members (rxclass classMembers, trans=1) with >= {MIN_MEMBERS} single ingredients that belong to no other EPC class; "
                                   f"agreement = the members also match one ATC level-4 code (Jaccard >= {JACCARD}, >= {COMMON} common); names shown are EPC names; near-miss ingredients come from the "
                                   "members' ATC level-3 groups, have an FDA class of their own, share no ATC level-4 code with a member, lie outside the class and its sub-classes, and, if they are members of a selected class, that class is in the same split",
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
