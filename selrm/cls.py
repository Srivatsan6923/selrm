"""Class conditions from onto_v1 for the stage-2 engine (cls_v1 and the class clause of rule_v2)."""
import hashlib
import json
from functools import lru_cache
from pathlib import Path

from selrm import engine2 as E
from selrm import rules_grammar as RG

ROOT = Path(__file__).resolve().parents[1]
MAX_NEAR_PER_SIBLING = 8


@lru_cache(maxsize=None)
def tables():
    return json.loads((ROOT / "data" / "onto_v1" / "classes.json").read_text(encoding="utf-8"))


def _clash(a, b):
    a, b = a.lower(), b.lower()
    return a in b or b in a


def conditions(split, domain):
    """[(Cond, family, class entry)] for the classes of one split and domain. Near-miss terms: members of a
    sibling class (ontologies: the other classes under the same parent; drugs: the class's near-miss
    ingredients) and, for ontologies, the parent term as the too-general term. A near-miss name that contains
    or is contained in a member name is left out, so a name alone decides membership."""
    out = []
    for fam in tables()[domain]:
        if fam["split"] != split:
            continue
        for c in fam["classes"]:
            members = tuple((m["id"], tuple(m["names"])) for m in c["members"])
            names = [n for _, ns in members for n in ns]
            if domain == "drug":
                near = [(m["id"], m["names"][0], "sibling") for m in c["siblings"]]
            else:
                near = [(m["id"], m["names"][0], "sibling") for o in fam["classes"] if o is not c
                        for m in o["members"][:MAX_NEAR_PER_SIBLING]]
                near.append((fam["general"]["id"], fam["general"]["name"], "general"))
            near = tuple(x for x in near if not any(_clash(x[1], n) for n in names))
            if len(near) >= 2:
                out.append((E.Cond("c1", "class", c["id"], domain=domain, name=c["name"], members=members, near=near), fam, c))
    return out


def scenario(cond, key):
    """A rule_v1 scenario, seeded by key, whose text names no member and no near-miss term of the class."""
    names = [n.lower() for _, ns in cond.members for n in ns] + [n.lower() for _, n, _ in cond.near]
    order = sorted(range(len(RG.SCENARIOS)), key=lambda i: hashlib.sha256(f"{key}/{i}".encode()).hexdigest())
    for i in order:
        text = " ".join(map(str, RG.SCENARIOS[i][:4])).lower()
        if not any(n in text for n in names if len(n) > 3):
            return RG.SCENARIOS[i]
    raise ValueError(f"no scenario for {cond.key}")


def rule(cond, rid, key, source=None):
    intro, default, alt, setting, sex, ages = scenario(cond, key)
    return E.Rule2(rid, "any", (cond,), intro, default, alt, setting, sex, ages, family="single|class", source=source or {})


def member_list(cond):
    """The open-book sentence: every member with every name the cases may use."""
    items = [ns[0] + (f" (also: {', '.join(ns[1:])})" if len(ns) > 1 else "") for _, ns in cond.members]
    return f"Members of the class \"{cond.name}\": " + "; ".join(items) + "."
