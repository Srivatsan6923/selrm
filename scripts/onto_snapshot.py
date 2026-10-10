"""onto_v1, step 1: snapshot of the open ontologies and of RxNav class membership (STAGE2_TASKS_A, A4.1).

  python scripts/onto_snapshot.py          # download what is missing, cache every RxNav response, write the manifest

Files under data/_ext/onto/ (git-ignored): hp.obo, phenotype.hpoa, mondo.obo, doid.obo, rxnav/<hash>.json.
The manifest data/onto_v1/SNAPSHOT.json records release identifiers, sha256 and terms of use. ATC class names
are not redistributed: only ATC codes are stored in derived files; class names shown are FDA EPC names.
"""
import hashlib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXT = ROOT / "data" / "_ext" / "onto"
RX = "https://rxnav.nlm.nih.gov/REST"
FILES = {
    "hp.obo": ("https://purl.obolibrary.org/obo/hp.obo", "HPO: free to use with attribution, no alteration of the ontology (hpo.jax.org/license)"),
    "phenotype.hpoa": ("https://purl.obolibrary.org/obo/hp/hpoa/phenotype.hpoa", "HPO annotations: same terms as HPO"),
    "mondo.obo": ("https://purl.obolibrary.org/obo/mondo.obo", "Mondo: CC BY 4.0"),
    "doid.obo": ("https://purl.obolibrary.org/obo/doid.obo", "Disease Ontology: CC0 1.0"),
}


def rx(path, **params):
    """A cached RxNav GET; every response is stored under data/_ext/onto/rxnav/."""
    url = f"{RX}/{path}?" + urllib.parse.urlencode(sorted(params.items()))
    f = EXT / "rxnav" / (hashlib.sha256(url.encode()).hexdigest()[:24] + ".json")
    if f.exists():
        return json.loads(f.read_text(encoding="utf-8"))["response"]
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as r:
                resp = json.loads(r.read())
            break
        except Exception:
            if attempt == 4:
                raise
            time.sleep(1 + attempt)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps({"url": url, "response": resp}), encoding="utf-8")
    return resp


def classes(class_type):
    return rx("rxclass/allClasses.json", classTypes=class_type)["rxclassMinConceptList"]["rxclassMinConcept"]


def members(class_id, rela_source, rela=None):
    """Ingredient members (TTY IN) of a class: [(rxcui, name)]."""
    p = {"classId": class_id, "relaSource": rela_source, "ttys": "IN"}
    if rela:
        p["rela"] = rela
    d = rx("rxclass/classMembers.json", **p)
    ms = (d.get("drugMemberGroup") or {}).get("drugMember") or []
    return sorted({(m["minConcept"]["rxcui"], m["minConcept"]["name"]) for m in ms})


def main():
    EXT.mkdir(parents=True, exist_ok=True)
    man = {"created": time.strftime("%Y-%m-%d"), "files": {}, "rxnav": {}}
    for name, (url, terms) in FILES.items():
        f = EXT / name
        if not f.exists() or f.stat().st_size == 0:
            urllib.request.urlretrieve(url, f)
        raw = f.read_bytes()
        head = raw[:4000].decode("utf-8", "replace")
        ver = re.search(r"^(?:data-version: |#version: )(.+)$", head, re.M)
        man["files"][name] = {"url": url, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw),
                              "release": ver.group(1).strip() if ver else None, "terms": terms}
    man["rxnav"]["version"] = rx("version.json")
    atc4 = [c for c in classes("ATC1-4") if len(c["classId"]) == 5]
    epc = classes("EPC")
    with ThreadPoolExecutor(8) as ex:
        a = list(ex.map(lambda c: members(c["classId"], "ATC"), atc4))
        e = list(ex.map(lambda c: members(c["classId"], "DAILYMED", "has_EPC"), epc))
    out = ROOT / "data" / "onto_v1"
    out.mkdir(parents=True, exist_ok=True)
    (out / "drug_classes_raw.json").write_text(json.dumps({
        "atc4": {c["classId"]: m for c, m in zip(atc4, a) if m},                       # codes only, no ATC names
        "epc": {c["classId"]: {"name": c["className"], "members": m} for c, m in zip(epc, e) if m}}, indent=0), encoding="utf-8")
    man["rxnav"].update({"atc_level4_classes": len(atc4), "atc_level4_with_ingredients": sum(bool(m) for m in a),
                         "epc_classes": len(epc), "epc_with_ingredients": sum(bool(m) for m in e),
                         "responses_cached": len(list((EXT / "rxnav").glob("*.json"))),
                         "terms": "RxNorm and RxClass via the RxNav API need no licence; ATC class names are not redistributed (codes only); class names shown are FDA EPC names",
                         "queries": "rxclass/allClasses (ATC1-4, EPC); rxclass/classMembers (relaSource ATC; relaSource DAILYMED, rela has_EPC; ttys IN)"})
    (out / "SNAPSHOT.json").write_text(json.dumps(man, indent=1, sort_keys=True), encoding="utf-8")
    print(json.dumps({k: v.get("release") for k, v in man["files"].items()}), man["rxnav"])


if __name__ == "__main__":
    sys.exit(main())
