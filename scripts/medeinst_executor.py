"""MedEinst executor audit (STAGE2_TASKS_C, C2). No model, no GPU.
  python scripts/medeinst_executor.py     -> results_git/C-S2-executor/summary.json, docs/MEDEINST_EXECUTOR.md
Executor: narrative -> evidence codes -> the stated procedure of the derived criterion (role A's
selrm/kb_criterion.py, kb_triplets.decide) -> one of the two diagnoses, or undecided.
1. Link. A reference (train) control case is linked to the DDXPlus patient whose row number is its case_id when
   age, sex and pathology agree (DDXPlus train and validate files).
2. Sentence table, from linked reference controls only. The narrative lists the patient's findings in the order
   of the patient's evidence list, symptoms before antecedents, the pain block first; a case whose sentence count equals its evidence
   count is aligned by position. A sentence enters the table with its majority evidence token (binary code,
   categorical code=value, multi-choice code) when it has >= MIN_VOTES aligned occurrences and the majority share
   is >= MIN_SHARE. Two further rounds align every linked case to the table of the round before (align()). The
   question texts of the binary findings of the knowledge base are added verbatim (trap edits use them).
3. Lexical matcher for sentences outside the table: Jaccard similarity of word sets with every table sentence;
   the best match is taken when its similarity is >= THETA.
   MIN_VOTES and MIN_SHARE are chosen on the reference split only: table from the linked cases with an even case
   number, grid scored on those with an odd case number (share of cases whose decision under the procedure equals
   the decision from the patient's true codes), no matcher. The final table uses every linked reference case.
   THETA is then chosen by pair accuracy on the reference pairs (their labels; trap cases have no linked patient).
4. Test: all 5,383 pairs. A case is right when the executor returns its ground-truth diagnosis; undecided is wrong.
Also a string-match baseline: for each exclusive list, the number of case sentences that equal a table sentence of
a listed finding; the diagnosis with more hits, a tie = undecided (no value reading, no procedure)."""
import collections, json, os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = f"{REPO}/scratch/acode_s2"                   # role A's code and the pinned DDXPlus files
sys.path.insert(0, A)
from selrm import kb_criterion as K, kb_triplets as T

RAW, OUT = f"{REPO}/data/clin_v1/medeinst_raw", f"{REPO}/results_git/C-S2-executor"
TRAIN_ZIP_SHA = "174ae1d56f36a15b7144838ecd214e1e1748a5369fc90c559529b6dc6ecfb218"   # release_train_patients.zip, 8 Oct 2026
GRID = [(v, s, 1.01) for v in (1, 2, 3) for s in (0.6, 0.8, 0.9)]          # table: no matcher
THETAS = (0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.01)
EV = K.kb()[1]
WORD = re.compile(r"[a-z0-9]+")


def load(p):
    with open(p, encoding="utf-8") as f:
        return [json.loads(l) for l in f]


def num(r):
    return int(r["case_id"].split("_")[1])


def units(narr):
    """[(sentence, [values])]: '- ' lines at any indent are sentences, '* ' lines are values of the last one."""
    out = []
    for ln in narr.split("\n"):
        s = ln.strip()
        if s.startswith("- "):
            out.append((s[2:], []))
        elif s.startswith("* ") and out:
            out[-1][1].append(s[2:])
    return out


PAIN = {f"E_{i}" for i in range(53, 60)}          # the pain block is written first (seen on the reference split)


def ordered(p):
    ans = T.answers(p["evidences"])
    ks = sorted(ans, key=lambda c: (bool(EV[c]["is_antecedent"]), c not in PAIN))
    return [(c if EV[c]["data_type"] != "C" else f"{c}={ans[c]}") for c in ks]


def align(U, tk, anchor):
    """Monotone alignment of sentences and tokens: [(sentence, token)]. A sentence the anchor table maps to the
    token scores 1, an unknown sentence 0.2, a contradiction -1; skipping either side costs 0.3."""
    n, m = len(U), len(tk)
    S = [[0.0] * (m + 1) for _ in range(n + 1)]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                continue
            c = []
            if i and j:
                a = anchor.get(U[i - 1][0])
                c.append((S[i - 1][j - 1] + (0.2 if a is None else 1.0 if a == tk[j - 1] else -1.0), 0))
            if i:
                c.append((S[i - 1][j] - 0.3, 1))
            if j:
                c.append((S[i][j - 1] - 0.3, 2))
            S[i][j], B[i][j] = max(c)
    out, i, j = [], n, m
    while i or j:
        b = B[i][j]
        if b == 0:
            out.append((U[i - 1][0], tk[j - 1]))
            i, j = i - 1, j - 1
        elif b == 1:
            i -= 1
        else:
            j -= 1
    return out


def link(cases, splits):
    """[(case, patient)] for control cases whose DDXPlus row agrees on age, sex and pathology."""
    need, P = {num(r) for r in cases if r["case_type"] == "control"}, collections.defaultdict(list)
    for split in splits:
        for p in T.patients(split):
            if p["pid"] in need:
                P[p["pid"]].append(p)
    out = []
    for r in cases:
        if r["case_type"] == "control":
            m = [p for p in P[num(r)] if (p["age"], p["sex"], p["pathology"]) == (r["age"], r["sex"], r["ground_truth"])]
            if m:
                out.append((r, m[0]))
    return out


def votes_of(linked, rounds=2):
    """Votes sentence -> token. Round 0: cases with as many sentences as tokens, by position. Later rounds: every
    case, by align() against the table of the previous round (>= 2 votes, majority share >= 0.8)."""
    votes, used = collections.defaultdict(collections.Counter), 0
    cases = [(units(r["narrative"]), ordered(p)) for r, p in linked]
    for U, tk in cases:
        if len(U) == len(tk):
            used += 1
            for (s, _), t in zip(U, tk):
                votes[s][t] += 1
    for _ in range(rounds):
        anchor, votes = table_of(votes, 2, 0.8), collections.defaultdict(collections.Counter)
        for U, tk in cases:
            for s, t in align(U, tk, anchor):
                votes[s][t] += 1
    return votes, used


def table_of(votes, min_votes, min_share):
    out = {}
    for s, v in votes.items():
        t, n = v.most_common(1)[0]
        if n >= min_votes and n / sum(v.values()) >= min_share:
            out[s] = t
    return out


class Reader:
    def __init__(self, table, theta):
        self.table, self.theta, self.memo = table, theta, {}
        self.words = [(s, frozenset(WORD.findall(s.lower()))) for s in table]

    def token(self, s):
        """(evidence token or None, 'exact' | 'matcher' | 'unmatched')"""
        if s in self.table:
            return self.table[s], "exact"
        if s not in self.memo:
            w = frozenset(WORD.findall(s.lower()))
            best = max(self.words, key=lambda x: len(w & x[1]) / max(1, len(w | x[1])))
            sim = len(w & best[1]) / max(1, len(w | best[1]))
            self.memo[s] = (self.table[best[0]], "matcher") if sim >= self.theta else (None, "unmatched")
        return self.memo[s]

    def read(self, narr):
        """(present codes, Counter of how the sentences were matched)"""
        out, how = set(), collections.Counter()
        for s, vals in units(narr):
            t, h = self.token(s)
            how[h] += 1
            if t is None:
                continue
            code, _, val = t.partition("=")
            e = EV[code]
            default = str(e["default_value"])
            if e["data_type"] == "B":
                out.add(code)
            elif e["data_type"] == "C":
                if val != default:
                    out.add(code)
            else:                                    # multi-choice: present unless every listed value is the default
                d = e["value_meaning"].get(default, {}).get("en")
                if any(v != d for v in vals) if vals else (d is None or d.lower() not in s.lower()):
                    out.add(code)
        return out, how


def pairs_of(cases):
    """{case number: (control, trap)}"""
    by = collections.defaultdict(dict)
    for r in cases:
        by[num(r)][r["case_type"]] = r
    return {k: (v["control"], v["trap"]) for k, v in by.items() if len(v) == 2}


def known(name):
    return name in K.kb()[0]


def pct(a, b):
    return 100.0 * a / b if b else None


def main():
    import hashlib
    h = hashlib.sha256(open(K.EXT / "release_train_patients.zip", "rb").read()).hexdigest()
    assert h == TRAIN_ZIP_SHA, f"release_train_patients.zip sha256 {h} differs from the pin"
    ref, test = load(f"{RAW}/train.jsonl"), load(f"{RAW}/test.jsonl")
    linked = link(ref, ("train", "validate"))
    n_ctrl = sum(r["case_type"] == "control" for r in ref)
    rp = pairs_of(ref)
    other = {k: (c["ground_truth"], t["ground_truth"]) for k, (c, t) in rp.items()}
    usable = [(r, p) for r, p in linked if all(known(x) for x in other[num(r)])]
    even, odd = [x for x in usable if num(x[0]) % 2 == 0], [x for x in usable if num(x[0]) % 2 == 1]
    v_even, _ = votes_of(even)
    grid = []
    for mv, ms, th in GRID:
        rd = Reader(table_of(v_even, mv, ms), th)
        same = codes = 0
        for r, p in odd:
            got, _ = rd.read(r["narrative"])
            true = T.present(T.answers(p["evidences"]))
            a, b = other[num(r)]
            same += T.decide(got, a, b) == T.decide(true, a, b)
            codes += got == true
        grid.append({"min_votes": mv, "min_share": ms, "theta": th, "same_decision": pct(same, len(odd)), "same_codes": pct(codes, len(odd))})
    best = max(grid, key=lambda g: (g["same_decision"], g["same_codes"], g["min_share"], g["theta"]))
    votes, used = votes_of(linked)
    table = table_of(votes, best["min_votes"], best["min_share"])
    n_induced = len(table)
    for c, e in EV.items():                       # trap edits also use the question text of the knowledge base verbatim
        if e["data_type"] == "B":
            table.setdefault(e["question_en"], c)
    theta_grid = []                               # matcher threshold: pair accuracy on the reference pairs (labels only)
    for th in THETAS:
        rd, ok = Reader(table, th), 0
        for k, (c, t) in rp.items():
            a, b = other[k]
            if known(a) and known(b) and a != b:
                ok += T.decide(rd.read(c["narrative"])[0], a, b) == a and T.decide(rd.read(t["narrative"])[0], a, b) == b
        theta_grid.append({"theta": th, "reference_pair_accuracy": pct(ok, len(rp))})
    best = best | max(theta_grid, key=lambda g: (g["reference_pair_accuracy"], g["theta"]))
    rd = Reader(table, best["theta"])

    # canonical sentences of each finding, for the string-match baseline
    sent_of = collections.defaultdict(set)
    for s, t in table.items():
        sent_of[t.partition("=")[0]].add(s)

    def baseline(narr, a, b):
        only_a, only_b, _ = K.lists(a, b)
        S = [s for s, _ in units(narr)]
        ha = sum(s in sent_of[c] for c in only_a for s in S)
        hb = sum(s in sent_of[c] for c in only_b for s in S)
        return a if ha > hb else b if hb > ha else None

    tp = pairs_of(test)
    how = {"control": collections.Counter(), "trap": collections.Counter()}
    tot, by_pair, rows, skipped = collections.Counter(), collections.defaultdict(collections.Counter), [], 0
    for k, (c, t) in sorted(tp.items()):
        a, b = c["ground_truth"], t["ground_truth"]
        if not (known(a) and known(b)) or a == b:
            skipped += 1
            continue
        res = {}
        for kind, r in (("control", c), ("trap", t)):
            got, hw = rd.read(r["narrative"])
            how[kind].update(hw)
            res[kind] = T.decide(got, a, b)
            res[kind + "_sm"] = baseline(r["narrative"], a, b)
        cell = {"n": 1, "control": res["control"] == a, "trap": res["trap"] == b, "pair": res["control"] == a and res["trap"] == b,
                "control_decided": res["control"] is not None, "trap_decided": res["trap"] is not None,
                "both_decided": res["control"] is not None and res["trap"] is not None,
                "any_decided": res["control"] is not None or res["trap"] is not None,
                "trap_follows_control": res["trap"] == a,
                "sm_control": res["control_sm"] == a, "sm_trap": res["trap_sm"] == b, "sm_pair": res["control_sm"] == a and res["trap_sm"] == b,
                "sm_both_decided": res["control_sm"] is not None and res["trap_sm"] is not None}
        tot.update({x: int(y) for x, y in cell.items()})
        by_pair[f"{a} -> {b}"].update({x: int(y) for x, y in cell.items()})
        rows.append({"case": k, "y_control": a, "y_trap": b, "control": res["control"], "trap": res["trap"]})
    n = tot["n"]
    # check of the reading on linked test controls (not used for any choice)
    tl = link(test, ("test", "train"))
    chk = sum(rd.read(r["narrative"])[0] == T.present(T.answers(p["evidences"])) for r, p in tl)
    summ = {"run_id": "C-S2-executor", "set": "clin_v1/medeinst_test (all pairs)", "no_model": True,
            "kb": K.PIN | {"release_train_patients.zip": TRAIN_ZIP_SHA},
            "reference": {"control_cases": n_ctrl, "linked": len(linked), "linked_pct": pct(len(linked), n_ctrl),
                          "aligned_for_table": used, "sentence_types_seen": len(votes), "table_entries": n_induced, "table_entries_with_question_texts": len(table),
                          "chosen": best, "grid": grid, "theta_grid": theta_grid, "tuning_cases": {"table": len(even), "scored": len(odd)}},
            "test": {"pairs": len(tp), "pairs_scored": n, "pairs_skipped_label_not_in_kb": skipped,
                     **{k: pct(tot[k], n) for k in tot if k != "n"},
                     "sentences": {kind: {"n": sum(c.values()), **{x: pct(c[x], sum(c.values())) for x in ("exact", "matcher", "unmatched")}}
                                   for kind, c in how.items()},
                     "reading_check_linked_test_controls": {"n": len(tl), "same_codes": pct(chk, len(tl))}},
            "by_label_pair": {p: {"n": c["n"], **{k: pct(c[k], c["n"]) for k in ("control", "trap", "pair", "both_decided", "any_decided")}}
                              for p, c in sorted(by_pair.items())}}
    os.makedirs(OUT, exist_ok=True)
    json.dump(summ, open(f"{OUT}/summary.json", "w", encoding="utf-8", newline="\n"), indent=1)
    with open(f"{OUT}/decisions.jsonl", "w", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    json.dump(table, open(f"{OUT}/sentence_table.json", "w", encoding="utf-8", newline="\n"), indent=0, sort_keys=True, ensure_ascii=False)
    t, f1 = summ["test"], lambda x: "-" if x is None else f"{x:.1f}"
    L = ["# MedEinst executor audit (C2; generated)", "",
         "Generated by `scripts/medeinst_executor.py` from `results_git/C-S2-executor/summary.json` (no typed numbers). "
         "The executor contains no model: sentence table and lexical matcher, then the procedure of the derived criterion.", "",
         f"Reference split: {len(linked)} of {n_ctrl} control cases link to their DDXPlus patient "
         f"({f1(summ['reference']['linked_pct'])}%); {used} of them align sentence by sentence; the table holds {n_induced} of "
         f"{len(votes)} sentence types (at least {best['min_votes']} aligned occurrences, majority share at least {best['min_share']}; "
         f"chosen on the reference controls; matcher threshold {best['theta']}, chosen by pair accuracy on the reference pairs, "
         f"{f1(best['reference_pair_accuracy'])}% there). Without the matcher the executor's decision equals the decision "
         f"from the patient's true codes on {f1(best['same_decision'])}% of the held-out linked cases and the code set is identical on "
         f"{f1(best['same_codes'])}%).", "",
         f"Test: {n} pairs scored ({skipped} skipped: a label outside the knowledge base or equal labels).", "",
         "| | control right | trap right | pair right | both cases decided | at least one decided | trap answered with the control diagnosis |",
         "|---|---|---|---|---|---|---|",
         f"| Executor | {f1(t['control'])} | {f1(t['trap'])} | {f1(t['pair'])} | {f1(t['both_decided'])} | {f1(t['any_decided'])} | {f1(t['trap_follows_control'])} |",
         f"| String match on the exclusive lists | {f1(t['sm_control'])} | {f1(t['sm_trap'])} | {f1(t['sm_pair'])} | {f1(t['sm_both_decided'])} | | |", "",
         f"Case decided: control {f1(t['control_decided'])}%, trap {f1(t['trap_decided'])}%.", "",
         "| sentences | n | in the table | by the matcher | unmatched |", "|---|---|---|---|---|",
         *[f"| {k} | {v['n']} | {f1(v['exact'])} | {f1(v['matcher'])} | {f1(v['unmatched'])} |" for k, v in t["sentences"].items()], "",
         f"Reading check (not used for any choice): on {t['reading_check_linked_test_controls']['n']} linked test controls the code set read "
         f"equals the patient's on {f1(t['reading_check_linked_test_controls']['same_codes'])}%.", "",
         "## By label pair (control diagnosis -> trap diagnosis)", "",
         "| pair | n | control | trap | pair | both decided |", "|---|---|---|---|---|---|",
         *[f"| {p} | {c['n']} | {f1(c['control'])} | {f1(c['trap'])} | {f1(c['pair'])} | {f1(c['both_decided'])} |" for p, c in summ["by_label_pair"].items()]]
    open(f"{REPO}/docs/MEDEINST_EXECUTOR.md", "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
    print("\n".join(L[:22]))


if __name__ == "__main__":
    main()
