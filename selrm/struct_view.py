"""Role A's `struct` fields and onto_v1 tables in the constraint form the gate library reads (role B, 9 Oct).

The frozen records keep their own `struct` (one dict per condition). constraints(struct) gives the same
content as a list of constraints:
  {"kind": "value", "op": "gt|ge|lt|le", "thr": number, "unit": str}
  {"kind": "time", "scope": "current|ever|window", "n": int, "unit": "day|week|month|year", "inclusive": bool}
  {"kind": "subject", "allowed": ["patient"] | ["patient", "first-degree"]}
  {"kind": "status", "allowed": ["present"]}
  {"kind": "concept", "class": <onto_v1 class id>}
terms() and closure() give onto_v1 as {"id", "label", "synonyms"} and {class id: [member ids]}.
"""
from selrm import cls as C

OP = {">": "gt", ">=": "ge", "<": "lt", "<=": "le"}
UNIT = {"days": "day", "weeks": "week", "months": "month", "years": "year"}


def constraints(struct):
    """Constraint list of one record's struct; None for the item-level struct of mcv_v1 (several inputs)."""
    kind = struct.get("kind")
    if "levels" in struct or kind not in ("window", "class", "numeric", "finding"):
        return None
    family = struct.get("subject") == "patient or first-degree relative"
    out = [{"kind": "subject", "allowed": ["patient", "first-degree"] if family else ["patient"]},
           {"kind": "status", "allowed": ["present"]}]
    if kind == "window":
        out.append({"kind": "time", "scope": "window", "n": struct["n"], "unit": UNIT[struct["unit"]], "inclusive": True})
    else:
        out.append({"kind": "time", "scope": "ever" if struct.get("time") == "ever" else "current", "n": None, "unit": None, "inclusive": True})
    if kind == "class":
        out.append({"kind": "concept", "class": struct["class_id"]})
    if kind == "numeric":
        out.append({"kind": "value", "op": OP[struct["op"]], "thr": struct["threshold"], "unit": struct.get("unit", "")})
    return out


def terms():
    """Every member and near-miss term of onto_v1: {id: {"id", "label", "synonyms"}}."""
    out = {}
    for fams in C.tables().values():
        for f in fams:
            if f.get("general"):
                out[f["general"]["id"]] = {"id": f["general"]["id"], "label": f["general"]["name"], "synonyms": []}
            for c in f["classes"]:
                for m in c["members"] + c.get("siblings", []):
                    out[m["id"]] = {"id": m["id"], "label": m["names"][0], "synonyms": list(m["names"][1:])}
    return out


def closure():
    """{class id: [member ids]} with each class's split, domain, name and agreement flag in info()."""
    return {c["id"]: [m["id"] for m in c["members"]] for fams in C.tables().values() for f in fams for c in f["classes"]}


def info():
    return {c["id"]: {"name": c["name"], "domain": c["domain"], "split": f["split"], "agreement": c.get("agreement")}
            for fams in C.tables().values() for f in fams for c in f["classes"]}
