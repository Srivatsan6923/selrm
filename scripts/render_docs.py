"""Render docs/templates/*.md.tmpl into docs/*.md with every number taken from tables/data_stats.json.

  python scripts/render_docs.py

{{a.b.c}} is replaced by the value at that path (lists joined with ", "); {{table:name}} by a
generated table. A path that does not exist stops the render: no number is typed by hand.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
S = json.loads((ROOT / "tables" / "data_stats.json").read_text(encoding="utf-8"))
_RV = ROOT / "audit" / "model_review" / "summary.json"
if _RV.exists():                 # the model reviewers' own counts, quoted in that file
    _rv = json.loads(_RV.read_text(encoding="utf-8"))["sessions"]
    S["review_summary"] = {f"label_disputed_round{k}": [x["label_disputed"] for x in _rv if x["round"] == k]
                           for k in (1, 2)}
    S["review_summary"]["outside_missing_items"] = [i for x in _rv for i in x["outside_missing"]]
SETS = ["rule_v1/test_L0", "rule_v1/test_L1", "rule_v1/test_L2", "rule_v1/test_L3alt", "rule_v1/test_L3inv",
        "rule_v1/test_hard", "rule_v1/dev"]


def get(path):
    x = S
    for k in path.split("."):
        if isinstance(x, dict) and k in x:
            x = x[k]
        elif isinstance(x, list) and k.isdigit():
            x = x[int(k)]
        else:
            raise KeyError(path)
    return x


def fmt(x):
    if x is None:
        return "n/a"
    if isinstance(x, list):
        return ", ".join(map(fmt, x)) if x else "none"
    if isinstance(x, dict):
        return "; ".join(f"{k}: {fmt(v)}" for k, v in x.items()) if x else "none"
    if isinstance(x, float):
        return f"{x:,.1f}" if abs(x) >= 1000 else f"{x:g}"
    if isinstance(x, int) and not isinstance(x, bool):
        return f"{x:,}"
    return str(x)


def short(name):
    return name.split("/")[-1]


def md_table(head, rows):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
                     + ["| " + " | ".join(map(fmt, r)) + " |" for r in rows])


def t_structure():
    a, b = S["structure"]["train_triplets"], S["structure"]["test_L2"]
    rows = [("Judgments", "judgments"), ("Rules", "rules"),
            ("Distinct program structures (names, constants removed)", "distinct_structures"),
            ("Signature classes", "signature_classes"), ("Conditions needed per judgment, mean", "conditions_mean"),
            ("Conditions needed per judgment, max", "conditions_max"), ("Dependency depth, mean", "depth_mean"),
            ("Dependency depth, max", "depth_max"), ("Evidence mentions per case, mean", "evidence_mentions_mean"),
            ("Groups with competing mentions of the target concept (%)", "competing_mentions_pct"),
            ("Judgments with a temporal operation (%)", "temporal_pct"),
            ("Judgments with a numeric comparison (%)", "numeric_pct"),
            ("Judgments with an exception (constraint rule) (%)", "exception_pct")]
    return md_table(["", "train_triplets", "test_L2"], [(lab, a[k], b[k]) for lab, k in rows])


def t_overlap():
    o = S["overlap"]
    rows = [(short(n), o[n]["rules"], o[n]["program_pct"], o[n]["structure_pct"], o[n]["subexpression_pct"],
             o[n]["rule_text_pct"], f"{fmt(o[n]['templates_shared'])} of {fmt(o[n]['templates'])}",
             o[n]["cases_with_train_cue_pct"], o[n]["cases_with_train_relative_pct"],
             f"{fmt(o[n]['base_states_shared'])} of {fmt(o[n]['base_states'])}",
             o[n]["source_shared_with_train_pct"]) for n in SETS if n in o]
    return md_table(["Set", "Rules", "Program in train (%)", "Structure in train (%)", "Subexpressions in train (%)",
                     "Rule text in train (%)", "Templates shared", "Cases with a train cue word (%)",
                     "Cases with a train relative (%)", "Base states shared", "Source shared (%)"], rows)


REQ = [("rule_dependent_time_scope", "Rule-dependent time scope (time near-miss on a finding another rule counts in the past)"),
       ("rule_dependent_subject_scope", "Rule-dependent subject scope (first-degree relative a family-counting rule would count)"),
       ("competing_mentions", "Competing mentions (two mentions of the target concept in one case)"),
       ("temporal_selection", "Temporal selection (an older value crosses the threshold, the current one does not)"),
       ("composition", "Composition (constraint rule with two or more conditions)"),
       ("composition_with_other_condition_met", "... of which another condition is met in the base case"),
       ("numerical_semantics", "Numerical semantics (value at a strict threshold, or flip at an inclusive one)"),
       ("long_note", "Long note (15 or more unrelated lines)"),
       ("superseded_value", "Superseded value"), ("delabelled", "Delabelled allergy"),
       ("altered_threshold", "Altered threshold (L3-alt)"), ("none_of_these", "None of the above"),
       ("groups", "Groups")]


def t_requirements():
    r = S["requirements"]
    sets = [n for n in SETS if n in r]
    return md_table(["Requirement"] + [short(n) for n in sets],
                    [(lab, *[r[n].get(k, 0) for n in sets]) for k, lab in REQ])


def t_kinds():
    k = S["near_miss_kinds"]
    sets = [n for n in SETS if n in k]
    kinds = sorted({x for n in sets for x in k[n] if x != "groups"})
    return md_table(["Near-miss kind"] + [short(n) for n in sets],
                    [(x, *[f"{fmt(k[n][x]['n'])} ({fmt(k[n][x]['pct'])}%)" if x in k[n] else "0" for n in sets])
                     for x in kinds] + [("groups", *[k[n]["groups"] for n in sets])])


def t_checks():
    t = S["target_claim_check"]
    return md_table(["Set", "Groups", "Records"], [(short(n), t["groups"][n], t["records"][n]) for n in t["sets"]]
                    + [("total", t["groups_total"], t["records_total"])])


def t_rejects():
    lg = S["rejects"]["logged"]
    rows = [(short(n), v["proposed"], v["rejected"], v["by_reason"]) for n, v in sorted(lg.items())
            if n.split("/")[-1].startswith(("test", "dev", "train_natural", "train_balanced", "train_blocks",
                                            "train_triplets"))]
    tw = S["rejects"]["missing_twins_regenerated"]
    rows += [(short(n) + " (twins regenerated)", v["proposed"], v["rejected"], v["by_reason"]) for n, v in tw.items()]
    return md_table(["Set", "Proposed", "Rejected", "Reasons"], rows)


def t_reviewers():
    r = S["reviewers"]
    return md_table(["Round", "Session", "Started (UTC)", "Groups", "Reviewer"],
                    [(x["round"], x["reader"], x["started_utc"][:16].replace("T", " "), x["groups"], x["reviewer"])
                     for x in r["per_session"]])


def t_families():
    pf = S["structure"]["per_family"]
    fams = sorted(set(pf["train_triplets"]) | set(pf["test_L2"]))
    cols = ["judgments", "distinct_structures", "conditions_mean", "competing_mentions_pct", "temporal_pct",
            "numeric_pct", "exception_pct"]
    rows = []
    for f in fams:
        for sp in ("train_triplets", "test_L2"):
            if f in pf[sp]:
                rows.append((f, sp, *[pf[sp][f][c] for c in cols]))
    return md_table(["Family", "Split", "Judgments", "Structures", "Conditions (mean)", "Competing (%)",
                     "Temporal (%)", "Numeric (%)", "Exception (%)"], rows)


TABLES = {"structure": t_structure, "overlap": t_overlap, "requirements": t_requirements, "kinds": t_kinds,
          "checks": t_checks, "rejects": t_rejects, "reviewers": t_reviewers, "families": t_families}


def render(text):
    def sub(m):
        key = m.group(1).strip()
        if key.startswith("table:"):
            return TABLES[key[6:]]()
        return fmt(get(key))
    return re.sub(r"\{\{([^}]+)\}\}", sub, text)


def main():
    for t in sorted((ROOT / "docs" / "templates").glob("*.md.tmpl")):
        out = ROOT / "docs" / t.name[:-5]
        out.write_text(render(t.read_text(encoding="utf-8")), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    sys.exit(main())
