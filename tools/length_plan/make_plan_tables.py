"""Markdown tables for docs/LENGTH_PLAN.md, computed from the PDFs and the trial logs.

Usage: python make_plan_tables.py AUTHORS.pdf BASE_TECTONIC.pdf trial_run.txt move_lines.tsv
Prints: (1) the block inventory with measured heights in both builds, with totals;
        (2) the cumulative trial table.
"""
import re
import sys

import inventory
from calib import key

PITCH, PAGE = 13.55, 104

# section, block, v13 lines, key (normalised first words; FIG: caption prefix), move
SRC = [
    ("Front", "Abstract (heading and text)", "71-93", "abstract", ""),
    ("1", "Heading", "95", "1 introduction", ""),
    ("1", "P1 \"A reward model for medical reasoning...\"", "97-108", "a reward model for medical", ""),
    ("1", "Figure 1, example (`fig:example`)", "110-133", "FIG:One rule", ""),
    ("1", "P2 \"Both failures matter...\"", "135-152", "both failures matter", ""),
    ("1", "P3 \"We build the test...\"", "154-164", "we build the test", ""),
    ("1", "P4 \"Three things should be kept apart...\"", "166-173", "three things should be", ""),
    ("1", "Contribution (1)", "175-178", "1 a test triplets", ""),
    ("1", "Contribution (2)", "180-186", "2 a controlled comparison", ""),
    ("1", "Contribution (3)", "188-192", "3 transfer under named", ""),
    ("1", "Figure 2, overview, full width (`fig:overview`)", "194-242", "FIG:Overview", "20"),
    ("2", "Heading", "244", "2 related work", ""),
    ("2", "Validity of evaluators", "246-263", "validity of evaluators", ""),
    ("2", "Process rewards and symbolic supervision", "265-304", "process rewards and symbolic", "15 (two sentences)"),
    ("2", "Context against prior, and counterfactual data", "306-317", "context against prior", "15"),
    ("3", "Heading", "319-320", "3 rule triplets and", ""),
    ("3.1", "Heading", "322", "3 1 rule tier", ""),
    ("3.1", "Rules, states, claims", "324-344", "rules states claims", "7a (one sentence)"),
    ("3.1", "Edits and invariants", "346-372", "edits and invariants", "6 (missing twins)"),
    ("3.1", "Tests the renderer does not determine", "374-384", "tests the renderer does", "7c (one sentence)"),
    ("3.1", "Triplets", "386-390", "triplets a triplet crosses", ""),
    ("3.1", "Proposition 1 and proof (`prop:blind`)", "392-402", "proposition 1 let u", "1"),
    ("3.1", "\"Let h_k(x)...\" (feature collisions)", "404-418", "let h k x", "1"),
    ("3.1", "Metrics", "420-430", "metrics reversal rev", ""),
    ("3.2", "Heading", "432", "3 2 external tiers", ""),
    ("3.2", "\"Program-derived labels establish...\"", "434-440", "program derived labels establish", ""),
    ("3.2", "Table 1, sources and constructs (`tab:sources`)", "442-460", "FIG:Sources and constructs", "2"),
    ("3.2", "Source descriptions (registered criteria ... NLI4CT-P)", "464-488", "registered criteria are unambiguous", "12"),
    ("4", "Heading (`sec:diagnostic`)", "490-491", "4 diagnostics", "3"),
    ("4", "Parts and whole", "493-499", "parts and whole for", "3"),
    ("4", "\"Appendix F analyses how far...\"", "501-502", "appendix f analyses how", "3"),
    ("5", "Heading", "504-505", "5 ledger rm", ""),
    ("5", "Reader", "507-524", "reader the reader r", ""),
    ("5", "Judge, with Eq. (1)", "526-541", "judge the judge j", "7b (one sentence)"),
    ("5", "Training, with Eq. (2)", "543-565", "training on rules the", "9 (last three sentences)"),
    ("5", "What follows by construction, and what does not", "567-579", "what follows by construction", "4"),
    ("5", "Step check and combined reward", "581-592", "step check and combined", "18 (three sentences)"),
    ("6", "Heading", "594-595", "6 experimental setup", ""),
    ("6", "Rules and shifts", "597-621", "rules and shifts the", "8 (three sentences)"),
    ("6", "Training distributions", "623-638", "training distributions all trained", ""),
    ("6", "Representations", "640-651", "representations two one stage", ""),
    ("6", "Systems", "654-671", "systems audited signals", "7d (one sentence)"),
    ("6", "External data and protocol", "673-695", "external data and protocol", "5 (statistical protocol)"),
    ("7", "Heading", "697-698", "7 results", ""),
    ("7.1", "Heading", "700-701", "7 1 audit of", ""),
    ("7.1", "Table 2, audit (`tab:audit`)", "703-735", "FIG:Audit", ""),
    ("7.1", "\"The two failures separate the signals...\"", "737-753", "the two failures separate", ""),
    ("7.1", "\"Every signal reverses correctly...\" (composition gap)", "757-759", "every signal reverses correctly", "3"),
    ("7.2", "Heading", "761-762", "7 2 training distribution", ""),
    ("7.2", "Table 3, factorial (`tab:factorial`)", "764-790", "FIG:Triplet accuracy on L2", ""),
    ("7.2", "Flip pairs alone leave over-triggering unresolved", "792-809", "flip pairs alone leave", "17 (two sentences)"),
    ("7.2", "Does balance teach reversal?", "811-816", "does balance teach reversal", ""),
    ("7.2", "One stage against two", "818-826", "one stage against two with", ""),
    ("7.2", "Applicability structure against a matched two-stage baseline", "828-839", "applicability structure against a", ""),
    ("7.3", "Heading", "841-842", "7 3 transfer within", ""),
    ("7.3", "Table 4, transfer, full width (`tab:main`)", "844-892", "FIG:Transfer", "16 (caption notes)"),
    ("7.3", "Within rules", "894-910", "within rules trained on", ""),
    ("7.3", "From rules to clinical labels", "912-929", "from rules to clinical", ""),
    ("7.3", "Alternatives", "931-939", "alternatives a genprm style", "14"),
    ("7.4", "Heading", "941-942", "7 4 what the", ""),
    ("7.4", "Figure 3, diversity and selection curves (`fig:diversity`)", "944-990", "FIG:Not yet measured", "10"),
    ("7.4", "Does a decision bit explain the rule-tier result?", "992-999", "does a decision bit", ""),
    ("7.4", "Own against program-supplied ledgers", "1001-1010", "own against program supplied", "11"),
    ("7.4", "One stage against two (ablation)", "1012-1019", "one stage against two the", "11"),
    ("7.4", "Field interventions and the condition under test", "1021-1026", "field interventions and the", ""),
    ("7.4", "Near-miss kinds not seen in training", "1028-1033", "near miss kinds not", "11"),
    ("7.4", "Rule diversity, model size, missing inputs", "1035-1044", "rule diversity model size", "11"),
    ("7.5", "Heading", "1046-1047", "7 5 candidate selection", ""),
    ("7.5", "Table 5, candidate selection (`tab:downstream`)", "1049-1076", "FIG:Reranking", "13"),
    ("7.5", "\"Table 5 tests the verifier as a process reward...\"", "1078-1092", "table 5 tests the", "19 (two sentences)"),
    ("8", "Heading", "1094", "8 conclusion", ""),
    ("8", "Conclusion", "1096-1101", "on executable rules reward", ""),
]


def heights(pdf):
    flow, floats = inventory.analyse(pdf)
    bl = inventory.blocks(flow)
    out = {i: 0.0 for i in range(len(SRC))}
    cur = None
    unmatched = []
    for b in bl:
        if b["text"] == "<<STOP>>":
            continue
        k = key(b["text"])
        hit = [i for i, s in enumerate(SRC) if not s[3].startswith("FIG:") and k.startswith(s[3])]
        if b["text"].strip() == "Abstract" or b.get("abstract"):
            hit = [0]
        if hit:
            cur = hit[0]
        elif cur is None:
            unmatched.append(b["text"][:40])
            continue
        out[cur] += b["height"]
    for f in floats:
        cap = re.sub(r"^(Table|Figure) \d+:\s*", "", f["cap"])
        hit = [i for i, s in enumerate(SRC) if s[3].startswith("FIG:") and cap.startswith(s[3][4:])]
        assert hit, f"float not matched: {f['cap']}"
        out[hit[0]] += f["space"]
    title = 2 * (inventory.TITLE_END - inventory.COL_TOP)
    return out, title, unmatched


def main():
    ha, ta, ua = heights(sys.argv[1])
    ht, tt, ut = heights(sys.argv[2])
    assert not ua and not ut, (ua, ut)
    print("| # | Sec. | Block | v13 lines | pdflatex (lines) | tectonic (lines) | Move |")
    print("|---|---|---|---|---|---|---|")
    print(f"| 0 | Front | Title and author box (both columns) | 63-69 | {ta / PITCH:.1f} | {tt / PITCH:.1f} | |")
    moved_a = moved_t = 0.0
    for i, s in enumerate(SRC):
        print(f"| {i + 1} | {s[0]} | {s[1]} | {s[2]} | {ha[i] / PITCH:.1f} | {ht[i] / PITCH:.1f} | {s[4]} |")
        if s[4] and "(" not in s[4]:
            moved_a += ha[i]
            moved_t += ht[i]
    tot_a = (sum(ha.values()) + ta) / PITCH
    tot_t = (sum(ht.values()) + tt) / PITCH
    print(f"| | | **Total** | | **{tot_a:.1f}** = {tot_a / PAGE:.3f} pages | **{tot_t:.1f}** = {tot_t / PAGE:.3f} pages | |")
    print()
    print(f"WHOLE_BLOCKS_MOVED pdflatex {moved_a / PITCH:.1f} lines, tectonic {moved_t / PITCH:.1f} lines")
    print()
    # trial table
    moves = {}
    for line in open(sys.argv[4], encoding="utf-8"):
        name, spans, doc = line.rstrip("\n").split("\t")
        moves[name] = (spans, doc)
    rows = []
    for line in open(sys.argv[3], encoding="utf-8"):
        m = re.match(r"\s*(\d+) (\w+)\s+rc=(\d+) pdfpages=(\d+) Limitations p(\d+)([LR]) y=\s*([\d.]+)"
                     r" heading=([\d.]+) effective=([\d.]+) undefined=(\[.*?\]) multiply=(\[.*?\])"
                     r" main_floats_after_Limitations=(\[.*?\])", line)
        if m:
            rows.append(m.groups())
    print("| Step | Move | v13 lines cut | Limitations heading (tectonic) | Main text incl. floats (pages) | Change (lines) | Main-text float after Limitations |")
    print("|---|---|---|---|---|---|---|")
    prev = None
    for g in rows:
        k, name, rc, npages, pg, col, y, head, eff, undef, multi, late = g
        eff = float(eff)
        ch = "" if prev is None else f"{(eff - prev) * PAGE:+.1f}"
        spans = moves.get(name, ("", ""))[0]
        col_name = "left" if col == "L" else "right"
        print(f"| {k} | {name} | {spans} | p{pg} {col_name} y={y} | {eff:.3f} | {ch} | {late if late != '[]' else 'none'} |")
        assert rc == "0" and undef == "[]" and multi == "[]", g
        prev = eff
    first, last = float(rows[0][8]), float(rows[-1][8])
    print()
    print(f"TOTAL_CHANGE {(last - first) * PAGE:.1f} lines ({first:.3f} -> {last:.3f} pages)")


if __name__ == "__main__":
    main()
