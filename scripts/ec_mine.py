"""ec_v1 step 1: candidate eligibility criteria from ClinicalTrials.gov (API v2), public domain.

  python scripts/ec_mine.py            # writes ec_v1/candidates.jsonl and ec_v1/mining.json

Excludes every trial and criterion text of the TrialGPT annotations (configs/trialgpt_exclusions.json,
from role C). Keeps single criterion lines (one bullet) that name exactly one concept the generator
can render. Formalisation, exclusion reasons and sign-off follow (ec_v1/README.md).
"""
import datetime
import json
import re
import time
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ec_v1"
API = "https://clinicaltrials.gov/api/v2/studies"
QUERIES = ["atrial fibrillation", "venous thromboembolism", "deep vein thrombosis", "pulmonary embolism",
           "community-acquired pneumonia", "heart failure", "type 2 diabetes", "hypertension",
           "chronic kidney disease", "osteoarthritis", "migraine", "asthma", "COPD exacerbation", "acute stroke",
           "sepsis", "gout", "urinary tract infection", "cellulitis", "acute coronary syndrome", "anticoagulation",
           "pharyngitis", "contraception", "peptic ulcer", "cancer associated thrombosis", "anemia",
           "thrombocytopenia", "hyperkalemia", "obesity", "hip fracture", "influenza"]
CONCEPTS = {   # concept -> pattern in a criterion line
    "platelets": r"platelet", "creatinine": r"creatinine(?! clearance)", "egfr": r"\begfr\b|glomerular filtration",
    "hemoglobin": r"h(a)?emoglobin|\bhgb\b|\bhb\b", "alt_enzyme": r"\balt\b|alanine aminotransferase|\bsgpt\b",
    "potassium": r"potassium", "inr": r"\binr\b|international normali[sz]ed ratio",
    "neutrophils": r"neutrophil|\banc\b", "wbc": r"white (blood )?cell count|\bwbc\b|leukocyte count",
    "bmi": r"\bbmi\b|body mass index", "weight": r"\bweigh", "age": r"\bage\b|years of age|years old",
    "sbp": r"systolic", "heart_rate": r"heart rate", "temperature": r"temperature",
    "spo2": r"oxygen saturation|\bspo2\b|\bsao2\b", "rr": r"respiratory rate", "bun": r"urea",
    "pregnancy": r"pregnan", "stroke": r"stroke|\btia\b|transient ischa?emic", "vte": r"venous thrombo|\bdvt\b|deep vein thrombosis|pulmonary embol",
    "bleeding": r"bleed|ha?emorrhag", "vascular": r"myocardial infarction|heart attack|peripheral arter",
    "cad": r"coronary artery disease", "chf": r"heart failure", "diabetes": r"diabet", "asthma": r"asthma",
    "cancer": r"cancer|malignan|carcinoma|lymphoma|leuka?emia|myeloma", "peptic_ulcer": r"peptic ulcer|gastric ulcer|duodenal ulcer",
    "pen_allergy": r"penicillin", "sulfa_allergy": r"sulfonamide|sulfa ", "hit": r"heparin.induced",
    "mech_valve": r"mechanical (heart )?valve|prosthetic (heart )?valve", "warfarin": r"warfarin|vitamin k antagonist",
    "aspirin": r"aspirin", "angioedema": r"angioedema", "hypertension": r"hypertension", "fall": r"\bfalls?\b",
    "contrast_allergy": r"contrast", "methotrexate": r"methotrexate", "lithium": r"lithium",
    "clarithromycin": r"clarithromycin"}
PAT = {k: re.compile(v, re.I) for k, v in CONCEPTS.items()}


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def fetch(cond, n=100):
    q = urllib.parse.urlencode({"query.cond": cond, "filter.advanced": "AREA[StudyType]INTERVENTIONAL",
                                "fields": "NCTId,BriefTitle,EligibilityCriteria,OverallStatus", "pageSize": n,
                                "format": "json"})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": "selrm-research/1.0"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)["studies"]
        except OSError:
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"ClinicalTrials.gov query failed: {cond}")


def lines(text):
    """(type, line) for the bullet lines of an eligibility text, by section."""
    kind = None
    for raw in text.replace("\\>", ">").replace("\\<", "<").replace("\\=", "=").splitlines():
        s = raw.strip()
        low = s.lower()
        if re.match(r"^(key )?inclusion criteria", low):
            kind = "inclusion"
            continue
        if re.match(r"^(key )?exclusion criteria", low):
            kind = "exclusion"
            continue
        m = re.match(r"^(?:[*\-•]|\d{1,2}[.)])\s+(.*)$", s)
        if kind and m:
            yield kind, m.group(1).strip()


def main():
    ex = json.loads((ROOT / "configs" / "trialgpt_exclusions.json").read_text(encoding="utf-8"))
    bad_trials, bad_texts = set(ex["trial_ids"]), {norm(t) for t in ex["criterion_texts"]}
    stats, seen, out = Counter(), set(), []
    for cond in QUERIES:
        for s in fetch(cond):
            ps = s["protocolSection"]
            nct = ps["identificationModule"]["nctId"]
            if nct in seen:
                continue
            seen.add(nct)
            stats["trials"] += 1
            if nct in bad_trials:
                stats["trials_excluded_trialgpt"] += 1
                continue
            for kind, line in lines(ps.get("eligibilityModule", {}).get("eligibilityCriteria", "")):
                stats["lines"] += 1
                if norm(line) in bad_texts:
                    stats["lines_excluded_trialgpt_text"] += 1
                    continue
                hits = [c for c, p in PAT.items() if p.search(line)]
                if len(hits) != 1 or not 10 <= len(line) <= 220:
                    continue
                out.append({"nct_id": nct, "title": ps["identificationModule"]["briefTitle"],
                            "status": ps.get("statusModule", {}).get("overallStatus"), "type": kind, "text": line,
                            "concept": hits[0], "query": cond})
        time.sleep(1)
    OUT.mkdir(exist_ok=True)
    out.sort(key=lambda r: (r["concept"], r["nct_id"], r["text"]))
    with open(OUT / "candidates.jsonl", "w", encoding="utf-8", newline="\n") as f:
        f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in out)
    stats["candidates"] = len(out)
    info = {"source": "ClinicalTrials.gov API v2 (public domain)", "endpoint": API,
            "fetched_on": datetime.date.today().isoformat(), "queries": QUERIES, "study_type": "INTERVENTIONAL",
            "pages": "first 100 studies per query", "trialgpt_exclusions": ex["source"], **stats,
            "by_concept": dict(Counter(r["concept"] for r in out)), "by_type": dict(Counter(r["type"] for r in out))}
    (OUT / "mining.json").write_text(json.dumps(info, indent=1), encoding="utf-8")
    print(json.dumps(info, indent=1))


NUMERIC = {"platelets", "creatinine", "egfr", "hemoglobin", "alt_enzyme", "potassium", "inr", "neutrophils", "wbc",
           "bmi", "weight", "age", "sbp", "heart_rate", "temperature", "spo2", "rr", "bun"}
VAGUE = re.compile(r"(?i)\b(uln|upper limit|lower limit|lln|times|investigator|opinion|judg|clinically|significant|"
                   r"severe|moderate|mild|uncontrolled|unstable|suspected|plan|intend|willing|able to|consent|"
                   r"requir|unless|except|such as|e\.g|i\.e|etc|including|other than|due to|secondary|related|"
                   r"associated|according|defined|calculated|formula|score|scale|grade|class|stage|nyha|nihss|"
                   r"test|screening|randomi[sz]|enrol|baseline|dose|mg/kg|recent|acute|chronic|risk|index|"
                   r"criteria|protocol|study|trial|procedure|surgery|operation)\b|%|\bx\s*\d|\d\s*x\b")
COMPARATOR = re.compile(r"(?i)(≤|≥|<=|>=|=<|=>|<|>|less than|greater than|more than|below|above|at least|"
                        r"or more|or less|or older|or younger|exceed|under|over)")
RANGE = re.compile(r"(?i)\d\s*(-|–|to|and)\s*[<>≤≥]?\s*\d|between|\bfrom\b|\band\b.*\d.*[<>≤≥]")


def select(per_concept=8, seed=2030):
    """Candidates with explicit semantics: a measurement with one comparator and no range, or a short
    finding line; then at most per_concept per concept, from distinct trials."""
    import random
    rows = [json.loads(l) for l in open(OUT / "candidates.jsonl", encoding="utf-8")]
    keep = []
    for r in rows:
        t = r["text"]
        if len(t) > 140 or VAGUE.search(t):
            continue
        if r["concept"] in NUMERIC:
            if len(COMPARATOR.findall(t)) != 1 or RANGE.search(t) or not re.search(r"\d", t):
                continue
        elif len(t.split()) > 14 or re.search(r"\d", t) and not re.search(r"(?i)within|past|last|prior|previous", t):
            continue
        keep.append(r)
    rng, by = random.Random(seed), {}
    for r in keep:
        by.setdefault(r["concept"], []).append(r)
    out = []
    for c in sorted(by):
        rng.shuffle(by[c])
        trials = set()
        for r in by[c]:
            if r["nct_id"] not in trials and len([x for x in out if x["concept"] == c]) < per_concept:
                trials.add(r["nct_id"])
                out.append(r)
    for i, r in enumerate(out):
        r["cand"] = f"k{i + 1:03d}"
    with open(OUT / "selected.jsonl", "w", encoding="utf-8", newline="\n") as f:
        f.writelines(json.dumps(r, ensure_ascii=False) + "\n" for r in out)
    print(len(keep), "explicit;", len(out), "selected;", dict(Counter(r["concept"] for r in out)))


if __name__ == "__main__":
    import sys
    select() if sys.argv[1:] == ["select"] else main()
