"""General-purpose trigger tagger + rule program (shortcut table, last row; FINAL_TASKS_C P0.5).
Role A's trigger-lexicon scorer (A-D14 trigger_train / trigger_all, scripts/shortcut_scorers.py at
59034a3) with its three cue lexicons (negation, time, persons) replaced by a frozen
general-purpose clinical context tagger: medspaCy's ConText with its default rules
(medspacy 1.3.1). Everything else is A's reader unchanged: lines after the header and setting,
a line is read if a keyword of the decisive concept occurs in it, the first number after the
keyword is the value of a measurement, a year in the line marks the past, and the rule program
decides from the state with the decisive concept's mentions replaced by the read ones.
ConText -> mention: FAMILY modifier -> subject = its trigger word (lower case, possessive
stripped; the program counts only first-degree relatives where the criterion counts family);
NEGATED_EXISTENCE or HYPOTHETICAL -> status absent; HISTORICAL -> time past.
Runs in a process whose path holds role A's code (both packages are named selrm):
  python scripts/gp_trigger.py --acode A_CODE_DIR --data DATA_DIR --set rule_v1/test_L2 --out RUN_DIR
Writes RUN_DIR/scores_<set>.jsonl ({iid, u}), RUN_DIR/reads_<set>.jsonl (what the tagger read per
group and case) and RUN_DIR/meta.json; metrics come from scripts/score.py."""
import argparse, json, os, re, sys, time

ap = argparse.ArgumentParser()
ap.add_argument("--acode", required=True)
ap.add_argument("--data", required=True)
ap.add_argument("--set", action="append", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--cues", default="context", choices=["context", "train", "all"],
                help="context = medspaCy ConText default rules; train / all = A's cue lexicons (reproduction check)")
a = ap.parse_args()
sys.path.insert(0, a.acode)

import medspacy, spacy
from medspacy.context import ConText
from selrm import datasets as D
from selrm import phrases as P
from selrm.rules import Mention
from selrm.rules_grammar import invented_rules

D.register(invented_rules())
YEAR = re.compile(r"\b(19|20)\d\d\b")
NUM = re.compile(r"\d+(?:\.\d+)?")
nlp = spacy.blank("en")
context = ConText(nlp)                       # default rules shipped with medspaCy


def crit(r):
    return D.RULES_BY_ID[r["rid"]].crit(r["cid"])


def tag(line, start, end):
    """ConText modifiers of the target span [start, end) of one line (one sentence)."""
    doc = nlp.make_doc(line)
    span = doc.char_span(start, end, label="TARGET", alignment_mode="expand")
    if span is None:
        return None
    doc.ents = [span]
    for t in doc:                            # one sentence per line
        t.is_sent_start = t.i == 0
    context(doc)
    ent = doc.ents[0]
    fam = [doc[m.modifier_span[0]:m.modifier_span[1]].text for m in ent._.modifiers if m.category == "FAMILY"]
    return {"family": fam, "negated": ent._.is_negated, "hypothetical": ent._.is_hypothetical,
            "historical": ent._.is_historical, "uncertain": ent._.is_uncertain,
            "categories": sorted({m.category for m in ent._.modifiers})}


def person(words):
    w = re.sub(r"('s|s')$", "", words[0].lower().strip()) if words else ""
    return w or "relative"


def lexicon_tag(line, low):
    """A's cue lexicons (shortcut_scorers.lexicon / read_lines), for the reproduction check."""
    splits = ("train",) if a.cues == "train" else ("train", "test")
    persons = sorted({p for s in splits for p in P.by_split(P.PERSONS, s)}, key=len, reverse=True)
    who = next((p for p in persons if re.search(rf"(?<![\w-]){re.escape(p)}(?![\w-])", low)), None)
    neg = any(re.search(rf"\b{re.escape(w)}\b", low) for s in splits for w in P.NEG_CUES[s])
    past = any(re.search(rf"\b{re.escape(w)}\b", low) for s in splits for w in P.TIME_CUES[s])
    return {"family": [who] if who else [], "negated": neg, "hypothetical": False, "historical": past,
            "uncertain": False, "categories": []}


def read_lines(r):
    c = crit(r)
    out, log = [], []
    for line in r["case_text"].split("\n")[2:]:
        low = line.lower()
        hits = sorted((low.find(k), k) for k in c.keywords if k in low)
        if not hits:
            continue
        pos, kw = hits[0]
        t = tag(line, pos, pos + len(kw)) if a.cues == "context" else lexicon_tag(line, low)
        if t is None:
            continue
        value = True
        if c.kind == "numeric":
            nums = [float(x) for x in NUM.findall(low[pos:]) if not YEAR.fullmatch(x)]
            if not nums:
                continue
            value = nums[0]
        who = person(t["family"]) if t["family"] else "patient"
        status = "absent" if t["negated"] or t["hypothetical"] else "present"
        when = "past" if t["historical"] or YEAR.search(line) else "current"
        out.append(Mention(c.concept, c.kind, value, who, status, when))
        log.append({"line": line, "keyword": kw, "subject": who, "status": status, "time": when, "context": t})
    return out, log


def program(r, mentions):
    """1 if the program finds claim s_prime correct for this case, else 0 (A's trigger())."""
    rule, c = D.RULES_BY_ID[r["rid"]], crit(r)
    state = [Mention(**m) for m in r["state"] if m["concept"] != c.concept] + mentions
    try:
        return rule.label(state, c.cid, r["meta"]["overrides"]) if r["claim_type"] == "conclusion" \
            else int(c.evaluate(state, r["meta"]["overrides"].get(c.cid)))
    except ValueError:                       # no readable current value: the default answer (as A's scorer)
        return 0


def main():
    os.makedirs(a.out, exist_ok=True)
    reg = json.load(open(f"{a.data}/REGISTRY.json", encoding="utf-8"))
    t0 = time.time()
    for s in a.set:
        recs = [json.loads(l) for l in open(f"{a.data}/{reg[s]['path']}", encoding="utf-8")]
        cache, reads = {}, {}
        name = s.replace("/", "~")
        with open(f"{a.out}/scores_{name}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for r in recs:
                key = (r["tid"], r["case_kind"])
                if key not in cache:
                    cache[key], reads[key] = read_lines(r)
                y = program(r, cache[key])            # 1 if s_prime is correct (A's trigger()); as A's as_u:
                u = y if r["claim_role"] == "s_prime" else 1 - y      # u(s') = y, u(s) = 1 - y
                f.write(json.dumps({"iid": r["iid"], "u": float(u)}) + "\n")
        with open(f"{a.out}/reads_{name}.jsonl", "w", encoding="utf-8", newline="\n") as f:
            for (tid, kind), log in reads.items():
                f.write(json.dumps({"tid": tid, "case_kind": kind, "reads": log}, ensure_ascii=False) + "\n")
        print(s, len(recs), "records", len(reads), "cases", f"{time.time() - t0:.0f} s", flush=True)
    meta = {"run_id": os.path.basename(os.path.normpath(a.out)), "role": "C",
            "model": "general-purpose trigger tagger (medspaCy ConText default rules) + rule program",
            "medspacy": medspacy.__version__, "spacy": spacy.__version__, "a_code": open(f"{a.acode}/COMMIT").read().strip()
            if os.path.exists(f"{a.acode}/COMMIT") else a.acode, "sets": a.set,
            "date": time.strftime("%Y-%m-%d"), "seconds": round(time.time() - t0, 1)}
    json.dump(meta, open(f"{a.out}/meta.json", "w", encoding="utf-8", newline="\n"), indent=1)


if __name__ == "__main__":
    main()
