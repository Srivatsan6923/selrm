"""mcv_v1 sentence edits and rule-side items (STAGE2_TASKS_A, A1.3). Value edits are in selrm/mcv/items.py."""
import copy
import hashlib
import json
import re
from pathlib import Path

from selrm.mcv.items import _raw, _records, _safe, _unit, _with, change_point, decimals, finite

# New templates, disjoint from every rule_v1 training cue phrase (tests/test_mcv_items.py checks it).
TEMPLATES = {
    "affirm": "On review, the patient has {np}.",
    "affirm_ever": "On review, the patient has a history of {np}.",
    "negation": "On review, the patient is free of {np}.",
    "subject": "The patient's {rel} has {np}.",
    "time": "The patient had {np} some years ago, and it has since cleared.",
}
RELATIVES = ("sister", "father")           # first-degree relatives on the test side of rule_v1's person split
HISTORY = re.compile(r"\b(history|PMH|past medical|comorbidit|known case of|background of)\b", re.I)


def load_lexicon():
    """{cid: {item name: {np, lexicon, relative_ok, past_ok}}} from selrm/mcv/lexicon/c<cid>.json."""
    out = {}
    for p in sorted((Path(__file__).parent / "lexicon").glob("c*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        out[int(d["cid"])] = d["items"]
    return out


def sentences(text):
    """(start, end) spans of sentences: a full stop, question or exclamation mark followed by white space."""
    spans, start = [], 0
    for m in re.finditer(r"(?<=[.!?])\s+(?=[A-Z0-9(])", text):
        spans.append((start, m.start()))
        start = m.end()
    spans.append((start, len(text)))
    return spans


def insert_sentence(note, sentence):
    """The one insertion rule: after the first sentence of the first paragraph that speaks of the history,
    else at the end of the first paragraph."""
    first = note.split("\n")[0]
    for a, b in sentences(first):
        if HISTORY.search(first[a:b]):
            return note[:b] + " " + sentence + note[b:]
    end = len(first.rstrip())
    return note[:end] + (" " if end else "") + sentence + note[end:]


def silent(note, entry):
    return not any(re.search(p, note, re.I) for p in entry["lexicon"])


def _with_flag(ent, key, value):
    e = copy.copy(ent)
    e[key] = value
    return e


def sentence_edits(rows, specs, defs, lexicon, split="test"):
    """Triplets (base, flip, near) for finding items that are not met and that the note does not mention.

    Near-miss kinds: negation; subject (the finding in a relative); time (the finding in the past) for items
    with time scope 'current'. For scope 'ever' a past mention is a flip (meta.flip_form = 'past'); no time
    edits for 'unstated'. Labels come from the rule code on the edited dictionary.
    """
    out, skips = [], {}

    def skip(why):
        skips[why] = skips.get(why, 0) + 1

    for r in rows:
        s = specs[r["cid"]]
        for i, it in enumerate(s.items):
            entry = lexicon.get(s.cid, {}).get(it.name)
            if entry is None:
                continue
            if it.points(r["ent"]) != 0 or any(r["ent"].get(k) not in (None, False) for k in it.inputs):
                skip("item met or an input released as present")
                continue
            if not silent(r["Patient Note"], entry):
                skip("note mentions the concept")
                continue
            np_ = entry["np"]
            affirm = TEMPLATES["affirm_ever" if it.time == "ever" else "affirm"].format(np=np_)
            met, unmet = _with_flag(r["ent"], it.inputs[0], True), _with_flag(r["ent"], it.inputs[0], False)
            k = it.points(met)
            assert k != 0 and it.points(unmet) == 0, (s.cid, it.name)
            negated = TEMPLATES["negation"].format(np=np_)
            plans = [("negation", affirm, negated, unmet, "affirmed")]
            if entry.get("relative_ok"):
                h = int(hashlib.sha256(f"{r['Row Number']}/{i}".encode()).hexdigest(), 16)
                plans.append(("subject", affirm, TEMPLATES["subject"].format(rel=RELATIVES[h % len(RELATIVES)], np=np_),
                              r["ent"], "affirmed"))
            if entry.get("past_ok") and it.time == "current":
                plans.append(("time", affirm, TEMPLATES["time"].format(np=np_), r["ent"], "affirmed"))
            if entry.get("past_ok") and it.time == "ever":
                plans.append(("negation", TEMPLATES["time"].format(np=np_), negated, unmet, "past"))
            for kind, flip_s, near_s, near_e, form in plans:
                tid = f"mcv_{split}_{int(r['Row Number']):05d}_{i:02d}_s_{kind}{'_past' if form == 'past' else ''}"
                cases = {"base": (r["Patient Note"], r["ent"]), "flip": (insert_sentence(r["Patient Note"], flip_s), met),
                         "near": (insert_sentence(r["Patient Note"], near_s), near_e)}
                for ck, (text, ent) in cases.items():
                    out += _records(s, it, i, r, defs[r["cid"]], tid, ck, text, ent, 0, k,
                                    {"split": split, "edit_type": "sentence", "nm_kind": kind,
                                     "meta": {"input": it.inputs[0], "flip_form": form,
                                              "inserted": {"flip": flip_s, "near": near_s}}})
    return out, skips


def _num_str(x):
    return str(int(x)) if float(x).is_integer() else repr(float(x))


def ruleside(rows, specs, defs, ranges, split="test"):
    """Crossed items: the note is fixed and one threshold of the score text is moved past the note's value.

    Only for two-level, single-input numeric items whose cut is the only number in the item's heading of the
    score text (so no band and no second form of the cut is left inconsistent). The label
    under the altered text is the rule code's value with the threshold moved, computed as the code's points
    at the value shifted by the same amount the other way.
    """
    out, skips = [], {}

    def skip(why):
        skips[why] = skips.get(why, 0) + 1

    for r in rows:
        s = specs[r["cid"]]
        lines = defs[r["cid"]].split("\n")
        for i, it in enumerate(s.items):
            if not finite(it) or len(it.inputs) != 1 or not it.thresholds:
                continue
            key = it.inputs[0]
            v = _raw(r["ent"], key)
            if v is None:
                continue
            if (r["cid"], key, _unit(r["ent"], key)) not in ranges:
                skip("input and unit not seen in the training rows")
                continue
            lo, hi = ranges[(r["cid"], key, _unit(r["ent"], key))]
            cands = [c + (d,) for d in (1, -1) if (c := change_point(it, r["ent"], key, d, lo - abs(lo), hi + abs(hi)))]
            if not cands:
                skip("no threshold reachable")
                continue
            first, last, pts, d = min(cands, key=lambda c: abs(c[0] - v))
            cuts = [t for t in it.thresholds[key][1] if min(first, last) <= t <= max(first, last)]
            if len(cuts) != 1:
                skip("released unit differs from the score text, or the cut is not listed")
                continue
            t = cuts[0]
            line_no = [n for n, ln in enumerate(lines) if re.match(rf"\s*{i + 1}\.\s", ln)]
            if len(line_no) != 1:
                skip("item line not found")
                continue
            line = lines[line_no[0]]
            pat = re.compile(rf"(?<![\d.]){re.escape(_num_str(t))}(?![\d]|\.\d)")
            heading = re.sub(r"^\s*\d+\.\s", "", line).split(":")[0]
            numbers = re.findall(r"\d+(?:[.,]\d+)?", heading)
            if len(it.levels) != 2 or len(numbers) != 1 or len(pat.findall(heading)) != 1:
                skip("not a two-level item with the cut as the only number of its heading")
                continue
            nd = max(decimals(t), decimals(v))
            step = 10 ** -nd
            margin = max(step, round(0.05 * abs(t) / step) * step)
            new_t = round(v - d * margin, nd)
            if new_t <= 0 or any(min(t, new_t) <= c <= max(t, new_t) for c in it.thresholds[key][1] if c != t):
                skip("moved cut would pass another cut")
                continue
            shifted = _with(r["ent"], key, round(v + (t - new_t), 6))
            alt_k, base_k = _safe(it, shifted), it.points(r["ent"])
            if alt_k != pts or alt_k == base_k:
                skip("shifted value does not give the level across the cut")
                continue
            alt_lines = list(lines)
            alt_lines[line_no[0]] = pat.sub(_num_str(new_t), line)
            item_id = f"mcv_{split}_{int(r['Row Number']):05d}_{i:02d}_r"
            for variant, text, ent in (("orig", defs[r["cid"]], r["ent"]), ("alt", "\n".join(alt_lines), shifted)):
                recs = _records(s, it, i, r, text, f"{item_id}@{variant}", "contested", r["Patient Note"], ent, base_k, alt_k,
                                {"split": split, "nm_kind": "numeric",
                                 "meta": {"xr": {"item": item_id, "variant": variant}, "input": key,
                                          "cut": {"orig": t, "alt": new_t}, "value": v}})
                if variant == "alt":
                    for rec in recs:
                        rec["crit"]["provenance"] += "; one threshold altered by script"
                out += recs
    return out, skips
