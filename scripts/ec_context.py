"""ec_v1: registry context of each formalised criterion (section and nesting), from the live record.

  python scripts/ec_context.py      # reads ec_v1/formalized.json, writes ec_v1/registry_context.json

The miner split eligibility text into bullet lines. This re-reads every trial record and reports, per
candidate line: the section it sits in by the nearest header that names inclusion or exclusion (any
wording, e.g. "MAIN EXCLUSION CRITERIA:"), whether the bullet is indented under another bullet, and
whether the previous item introduces a list ("... the following:"). A criterion whose section differs
from the mined type, or that is a sub-item of a compound criterion, is excluded downstream.
"""
import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KIT = ROOT / "ec_v1"
BULLET = re.compile(r"^(\s*)(?:[*\-•]|\d{1,2}[.)])\s+(.*)$")


def fetch(nct, module=False):
    """The eligibility text of a trial (or, with module=True, its whole eligibility module: sex,
    minimumAge, maximumAge, ...)."""
    fields = "EligibilityModule" if module else "EligibilityCriteria"
    url = f"https://clinicaltrials.gov/api/v2/studies/{nct}?fields={fields}&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "selrm-research/1.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                el = json.load(r)["protocolSection"]["eligibilityModule"]
                return el if module else el["eligibilityCriteria"]
        except OSError:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(nct)


def years(age):
    """'18 Years', '12 Months', '6 Weeks' -> years (None if not given)."""
    m = re.match(r"(\d+(?:\.\d+)?)\s*(year|month|week|day)", (age or "").lower())
    if not m:
        return None
    return round(float(m.group(1)) / {"year": 1, "month": 12, "week": 52, "day": 365}[m.group(2)], 2)


def population(ncts):
    """Registered sex and age range of each trial (ec_v1/registry_population.json)."""
    out = {}
    for nct in sorted(ncts):
        el = fetch(nct, module=True)
        out[nct] = {"sex": el.get("sex", "ALL"), "min_age": years(el.get("minimumAge")),
                    "max_age": years(el.get("maximumAge")), "healthy_volunteers": el.get("healthyVolunteers")}
        time.sleep(0.3)
    (KIT / "registry_population.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    return out


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def context(text, line):
    """Section, nesting and list intro of a criterion line. A bullet is a sub-item when it is indented
    under another bullet, when it follows a top-level bullet that ends with ':', or when it follows a
    non-bullet line that ends with ':' and says more than a section name (e.g. 'Patients presenting
    with any of the following:', 'Inclusion Criteria: All patients with ischemic stroke who:')."""
    raw = text.replace("\\>", ">").replace("\\<", "<").replace("\\=", "=").splitlines()
    section, intro, parent, out = None, None, None, None
    for r in raw:
        s = r.strip()
        m = BULLET.match(r)
        if not m:
            if not s:
                continue
            low = s.lower()
            if "exclusion" in low and len(s) < 120:
                section = "exclusion"
            elif "inclusion" in low and len(s) < 120:
                section = "inclusion"
            rest = re.sub(r"(?i)^\W*(key |main |additional )?(inclusion|exclusion)( criteria)?\W*", "", s)
            intro = s if s.endswith(":") and rest.strip(" :") else None
            parent = None
            continue
        indent, body = len(m.group(1)), m.group(2).strip()
        if indent < 2:
            sub = intro is not None
            under = intro
            if norm(body) == norm(line) and out is None:
                out = {"section": section, "indented": False, "under_intro": sub, "parent": under}
            parent = body if body.endswith(":") else None
        else:
            if norm(body) == norm(line) and out is None:
                out = {"section": section, "indented": True, "under_intro": True, "parent": parent or intro}
    return out


def main():
    items = json.loads((KIT / "formalized.json").read_text(encoding="utf-8"))["items"]
    sel = {json.loads(l)["cand"]: json.loads(l) for l in open(KIT / "selected.jsonl", encoding="utf-8")}
    texts, out = {}, {}
    for it in items:
        if it["decision"] != "accept":
            continue
        s = sel[it["cand"]]
        if s["nct_id"] not in texts:
            texts[s["nct_id"]] = fetch(s["nct_id"])
            time.sleep(0.3)
        c = context(texts[s["nct_id"]], s["text"]) or {"section": None, "indented": None, "after_list_intro": None,
                                                        "previous_item": None, "not_found": True}
        c["mined_type"] = s["type"]
        c["type_mismatch"] = c["section"] is not None and c["section"] != s["type"]
        out[it["cand"]] = c
    (KIT / "registry_texts.json").write_text(json.dumps(texts, indent=1, ensure_ascii=False), encoding="utf-8")
    pop = population(texts)
    print("trials with a registered age or sex limit:",
          sum(1 for p in pop.values() if p["sex"] != "ALL" or (p["max_age"] or 99) < 90 or (p["min_age"] or 0) > 18))
    (KIT / "registry_context.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    flagged = {k: v for k, v in out.items() if v.get("type_mismatch") or v.get("under_intro") or v.get("not_found")}
    print(len(out), "checked;", len(flagged), "flagged")
    for k, v in sorted(flagged.items()):
        print(k, {x: v.get(x) for x in ("section", "mined_type", "indented", "under_intro", "not_found")},
              "|", (v.get("parent") or "")[:90])


if __name__ == "__main__":
    main()
