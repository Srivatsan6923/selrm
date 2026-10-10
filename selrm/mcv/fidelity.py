"""Fidelity filter for mcv_v1 edits (STAGE2_TASKS_A, A1.4): two extractors from different model families,
neither the paper's backbone, read each edited note. A value edit is kept only if both return the edited
value; a sentence edit only if both find the inserted finding with its subject, status and time, and both
find nothing about it in the untouched note. Prompts were fixed on the dev portion before the test portion
was read. Responses are cached on disk; the verdicts are written to data/mcv_v1/FIDELITY.jsonl.
"""
import importlib.util
import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "data" / "mcv_v1" / "cache"
PARAMS = {"temperature": 0, "max_tokens": 400}
# Google and OpenAI open-weight families; the backbone is Qwen. (DeepSeek V4 Pro, first tried on dev, is limited
# to 20 requests a minute on a new OpenRouter account.)
EXTRACTORS = ("google/gemma-4-31b-it", "openai/gpt-oss-120b")

VALUE_PROMPT = """Read the patient note and report one value exactly as the note states it.

Note:
{note}

Question: what is the patient's {name}? If the note gives several, report the one from the first presentation or admission.
Reply with JSON only: {{"value": <number or null>, "unit": "<unit as written, or empty>"}}"""

FINDING_PROMPT = """Read the patient note and answer about one finding.

Note:
{note}

Finding: {np}
Does the note say anything about this finding, for the patient or for anyone else? If it does, report whom the statement is about, whether the finding is stated as present or absent for that person, and whether it is current or in the past.
Reply with JSON only: {{"mentioned": true or false, "subject": "patient" or "relative" or "none", "status": "present" or "absent" or "none", "time": "current" or "past" or "none"}}"""


def _api():
    spec = importlib.util.spec_from_file_location("rewrite_tier", ROOT / "scripts" / "rewrite_tier.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def parse(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    try:
        return json.loads(m.group(0)) if m else None
    except ValueError:
        return None


def value_ok(ans, expected, decimals):
    try:
        return ans is not None and ans.get("value") is not None and round(float(ans["value"]), decimals) == round(float(expected), decimals)
    except (TypeError, ValueError):
        return False


EXPECT = {   # what the inserted sentence must be read as: (subject, status set, time set)
    "affirm": ("patient", {"present"}, {"current", "past", "none"}),
    "affirm_past": ("patient", {"present", "absent"}, {"past"}),      # 'ever' items: a cleared past occurrence
    "negation": ("patient", {"absent"}, {"current", "past", "none"}),
    "subject": ("relative", {"present"}, {"current", "past", "none"}),
    "time": ("patient", {"present", "absent"}, {"past"}),
}


def finding_ok(ans, form):
    if form == "silent":
        return ans is not None and ans.get("mentioned") is False
    subject, status, time = EXPECT[form]
    return (ans is not None and ans.get("mentioned") is True and ans.get("subject") == subject
            and ans.get("status") in status and ans.get("time") in time)


def checks(records, lexicon):
    """The reads the filter needs: [(tid, case_kind, kind, prompt, expected)] for the edited cases of a
    portion, plus the untouched note of every sentence triplet."""
    out, seen = [], set()
    for r in records:
        if r["claim_role"] != "s" or "edit_type" not in r or (r["tid"], r["case_kind"]) in seen:
            continue
        seen.add((r["tid"], r["case_kind"]))
        m = r["meta"]
        if r["edit_type"] == "value" and r["case_kind"] in ("flip", "near"):
            name = re.sub(r"\s*\(.*?\)", "", m["input"]).strip().lower()
            out.append((r["tid"], r["case_kind"], "value", VALUE_PROMPT.format(note=r["case_text"], name=name),
                        m["value"][r["case_kind"]]))
        if r["edit_type"] == "sentence":
            np_ = lexicon[m["calculator_id"]][r["condition"]]["np"]
            if r["case_kind"] == "base":
                form = "silent"
            elif r["case_kind"] == "flip":
                form = "affirm_past" if m["flip_form"] == "past" else "affirm"
            else:
                form = r["nm_kind"]
            out.append((r["tid"], r["case_kind"], "finding", FINDING_PROMPT.format(note=r["case_text"], np=np_), form))
    return out


def run(records, lexicon, workers=32):
    """{tid: {"keep": bool, "reads": [...]}}; one API call per (model, prompt), cached."""
    api = _api()
    todo = checks(records, lexicon)

    def one(args):
        tid, ck, kind, prompt, expected = args
        row = {"tid": tid, "case_kind": ck, "kind": kind, "expected": expected, "answers": {}, "ok": True}
        for model in EXTRACTORS:
            try:
                ans = parse(api.call(model, prompt, PARAMS, cache=CACHE))
            except Exception as e:                       # a failed call rejects the edit, it does not stop the run
                ans = {"error": type(e).__name__}
            row["answers"][model] = ans
            good = value_ok(ans, expected, 3) if kind == "value" else finding_ok(ans, expected)
            row["ok"] = row["ok"] and good
        return row

    with ThreadPoolExecutor(workers) as ex:
        reads = list(ex.map(one, todo))
    out = {}
    for row in reads:
        t = out.setdefault(row["tid"], {"keep": True, "reads": []})
        t["reads"].append(row)
        t["keep"] = t["keep"] and row["ok"]
    return out
