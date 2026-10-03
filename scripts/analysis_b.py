"""FINAL_TASKS_B P0.1: analyses on existing predictions -> docs/ANALYSIS_B.md (generated; no typed numbers).
  python scripts/analysis_b.py > docs/ANALYSIS_B.md
Reads results_git/<run>/ (summaries, scores with reader outputs, meta.json) and the rule_v1 records (rebuilt
copy, SELRM_DATA, default scratch/rv1_local). A result that does not exist prints "not run"."""
import collections, glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from selrm.metrics import _flags, bootstrap_ci, decisions, paired_cluster_bootstrap, paired_test, seed_table, summarise
from report_b import DATA, RG, records

NL = "\n"
KINDS = ("boundary", "negation", "numeric", "subject", "time")
CELLS = [(f, c) for f in ("verdict", "rationale", "summary2", "value2", "ledger2")
         for c in ("natural", "balanced", "blocks", "triplets")]


def scores(rid, set_name, full=False):
    """{iid: row}; only u unless full (reader outputs are large)."""
    p = f"{RG}/{rid}/scores_{set_name.replace('/', '~')}.jsonl"
    if not os.path.exists(p):
        return None
    return {r["iid"]: (r if full else {"u": r["u"]}) for r in map(json.loads, open(p, encoding="utf-8"))}


SLIM = ("iid", "tid", "case_kind", "claim_type", "claim_role", "label", "rid", "nm_kind", "tier", "level", "family",
        "claim_text")
REG = json.load(open(f"{DATA}/REGISTRY.json"))
_rec_cache = {}


def recs(set_name):
    """Records without case texts, ledgers and prose (all the analyses need; cached per set)."""
    if set_name not in _rec_cache:
        _rec_cache[set_name] = [{k: r[k] for k in SLIM} for r in stream(set_name)]
    return _rec_cache[set_name]


def stream(set_name):
    """Records of a set, one line at a time (the full files hold case texts, ledgers and prose)."""
    return map(json.loads, open(f"{DATA}/{REG[set_name]['path']}", encoding="utf-8"))


_claims_cache = {}


def claims_by_unit(set_name):
    """{case unit: lower-cased claim texts}, the only record content the leakage check needs."""
    if set_name not in _claims_cache:
        c = collections.defaultdict(set)
        for r in stream(set_name):
            c["/".join(r["iid"].split("/")[:2])].add(r["claim_text"].strip().lower())
        _claims_cache[set_name] = c
    return _claims_cache[set_name]


def triplets(rid, set_name="rule_v1/test_L2"):
    S = scores(rid, set_name)
    if S is None:
        return None
    R = [r for r in recs(set_name) if r["iid"] in S]
    return decisions(R, [S[r["iid"]]["u"] for r in R])


def done(rid):
    return os.path.exists(f"{RG}/{rid}/DONE")


def pdiff(Ta, Tb, m):
    """a - b [95% CI], two-sided bootstrap p (C's paired_test: rules as clusters, reproducible order)."""
    d, lo, hi, p = paired_test(Ta, Tb, m)
    p = f"p {p:.3f}" if p > 0 else "p < 0.002"     # two-sided, 1,000 resamples: the smallest non-zero p is 0.002
    return f"{d:+.1f} [{lo:+.1f}, {hi:+.1f}], {p}"


def paired_section():
    print("## 1. Paired ledger minus summary (test_L2; triplets kept together, rules as clusters, 1,000 resamples)" + NL)
    for corpus in ("triplets", "blocks"):
        a, b = f"B-F-ledger2-{corpus}-s0", f"B-F-summary2-{corpus}-s0"
        if not (done(a) and done(b)):
            print(f"- {corpus}: not run ({b if not done(b) else a} missing)" + NL)
            continue
        Ta, Tb = triplets(a), triplets(b)
        print(f"**{corpus}** ({a} vs {b}, seed 0):" + NL)
        print("| metric | ledger | summary | ledger - summary [95% CI], p |")
        print("|---|---|---|---|")
        sa, sb = summarise(Ta)["all"], summarise(Tb)["all"]
        for m in ("TA", "Rev", "Hold"):
            print(f"| {m} | {sa[m]:.1f} | {sb[m]:.1f} | {pdiff(Ta, Tb, m)} |")
        print(NL + "Disagreement by near-miss kind (triplet solved = TA):" + NL)
        print("| near-miss kind | n | both | ledger only | summary only | neither |")
        print("|---|---|---|---|---|---|")
        cnt = collections.defaultdict(collections.Counter)
        for tid in Ta.keys() & Tb.keys():
            fa, fb = _flags(Ta[tid]), _flags(Tb[tid])
            if fa is None or fb is None:
                continue
            k = Ta[tid]["nm_kind"]
            cnt[k][("both" if fa["TA"] and fb["TA"] else "ledger only" if fa["TA"] else
                    "summary only" if fb["TA"] else "neither")] += 1
        for k in sorted(cnt):
            c = cnt[k]
            print(f"| {k} | {sum(c.values())} | {c['both']} | {c['ledger only']} | {c['summary only']} | {c['neither']} |")
        print()
        seeds = [s for s in range(5) if done(f"B-F-ledger2-{corpus}-s{s}") and done(f"B-F-summary2-{corpus}-s{s}")]
        if len(seeds) > 1:            # same-seed pairs pooled: items (seed, triplet), rules as clusters
            items = {m: [] for m in ("TA", "Rev", "Hold")}
            for s in seeds:
                A, B = triplets(f"B-F-ledger2-{corpus}-s{s}"), triplets(f"B-F-summary2-{corpus}-s{s}")
                for tid in sorted(A.keys() & B.keys()):
                    fa, fb = _flags(A[tid]), _flags(B[tid])
                    if fa is not None and fb is not None:
                        for m in items:
                            items[m].append({"u": A[tid]["rid"], "a": fa[m], "b": fb[m]})
            mean = lambda key: (lambda xs: 100.0 * sum(x[key] for x in xs) / len(xs))
            print(f"Seeds {', '.join(map(str, seeds))} pooled (same-seed pairs; rules as clusters):" + NL)
            print("| metric | ledger | summary | ledger - summary [95% CI], p |")
            print("|---|---|---|---|")
            for m, xs in items.items():
                r = paired_cluster_bootstrap(xs, "u", mean("a"), mean("b"))
                p = f"p {r['p']:.3f}" if r["p"] > 0 else "p < 0.002"
                print(f"| {m} | {mean('a')(xs):.1f} | {mean('b')(xs):.1f} | {r['diff']:+.1f} [{r['lo']:+.1f}, {r['hi']:+.1f}], {p} |")
            print()


VERDICT_PATTERNS = {
    "answer token line": re.compile(r"(?m)^\s*[+-]\s*$"),
    "answer/verdict word": re.compile(r"(?i)\b(answer|verdict)\s*[:=]"),
    "claim judged": re.compile(r"(?i)\bthe claim (is|was) (not )?(correct|incorrect|right|wrong|true|false)\b"),
    "criterion decided": re.compile(r"(?i)\b(criterion|condition) (is|was) (not )?(met|satisfied|fulfilled)\b"),
    "applies line": re.compile(r"(?i)^\s*applies\s*:\s*(yes|no)\b", re.M),
    "counts / does not count": re.compile(r"(?i)\b(counts|does not count) (for this patient|under the rule)\b"),
}


def leakage_section():
    print("## 2. Do generated summaries or ledgers contain a verdict?" + NL)
    print("Every reader output of the two-stage runs (one per case and condition, on every evaluated set) is checked "
          "for the record's own claim sentences (either claim, case-insensitive) and for decision phrasing: "
          + "; ".join(VERDICT_PATTERNS) + "." + NL)
    print("| run | reader outputs | contains a claim sentence | " + " | ".join(VERDICT_PATTERNS) + " |")
    print("|---|---|---|" + "---|" * len(VERDICT_PATTERNS))
    examples = []
    for f, c in CELLS:
        if f not in ("summary2", "value2", "ledger2"):
            continue
        for sd in range(5):
            rid = f"B-F-{f}-{c}-s{sd}"
            if not done(rid):
                continue
            m = json.load(open(f"{RG}/{rid}/meta.json"))
            outs, hit_claim, hits = {}, 0, collections.Counter()
            for s in m["eval_sets"]:
                S = scores(rid, s, full=True)
                if S is None:
                    continue
                claims = claims_by_unit(s)
                for iid, row in S.items():
                    unit = "/".join(iid.split("/")[:2])
                    if unit in outs or "reader_output" not in row:
                        continue
                    text = row["reader_output"]
                    outs[unit] = text
                    low = text.lower()
                    if any(cl and cl in low for cl in claims[unit]):
                        hit_claim += 1
                        if len(examples) < 6:
                            examples.append((rid, unit, "claim sentence", text[:160]))
                    for name, pat in VERDICT_PATTERNS.items():
                        if pat.search(text):
                            hits[name] += 1
                            if len(examples) < 6:
                                examples.append((rid, unit, name, text[:160]))
            print(f"| {rid} | {len(outs)} | {hit_claim} | " + " | ".join(str(hits[n]) for n in VERDICT_PATTERNS) + " |")
    if examples:
        print(NL + "Examples of flagged outputs (first 160 characters):" + NL)
        for rid, unit, name, text in examples:
            print(f"- {rid} {unit} [{name}]: `{text.replace(chr(10), ' / ')}`")
    print()


def transitions_section():
    print("## 3. Program-supplied ledger: transitions on test_L2 (B-F-ledger2-triplets-s0)" + NL)
    base, orc = "B-F-ledger2-triplets-s0", "B-AE-oracle-ledger"
    if not (done(base) and done(orc)):
        print(f"not run ({orc} pending)" + NL)
        return
    Tr, To = triplets(base), triplets(orc)
    cnt = collections.defaultdict(collections.Counter)
    for tid in Tr.keys() & To.keys():
        fr, fo = _flags(Tr[tid]), _flags(To[tid])
        if fr is None or fo is None:
            continue
        key = ("unchanged, solved" if fr["TA"] and fo["TA"] else "broken" if fr["TA"] else
               "rescued" if fo["TA"] else "unchanged, unsolved")
        cnt["all"][key] += 1
        cnt[Tr[tid]["nm_kind"]][key] += 1
    print("| near-miss kind | n | reader ledger solved, program ledger solved | rescued (reader wrong, program "
          "right) | broken (reader right, program wrong) | neither |")
    print("|---|---|---|---|---|---|")
    for k in ["all"] + sorted(x for x in cnt if x != "all"):
        c = cnt[k]
        print(f"| {k} | {sum(c.values())} | {c['unchanged, solved']} | {c['rescued']} | {c['broken']} | "
              f"{c['unchanged, unsolved']} |")
    so, sr = summarise(To)["all"], summarise(Tr)["all"]
    print(NL + f"TA with the program-supplied ledger {so['TA']:.1f} vs the reader's ledger {sr['TA']:.1f}; paired "
          f"difference {pdiff(To, Tr, 'TA')}." + NL)


def program_ledger_section():
    print("## 4. Rule program applied to the predicted ledger (B-F-ledger2-triplets-s0, test_L2)" + NL)
    rid = "B-AE-program-ledger"
    if not done(rid):
        print("not run (scripts/program_ledger.py pending)" + NL)
        return
    T, Tj = triplets(rid), triplets("B-F-ledger2-triplets-s0")
    s, sj = summarise(T)["all"], summarise(Tj)["all"]
    meta = json.load(open(f"{RG}/{rid}/summary_rule_v1~test_L2.json"))["eval"]      # test_L2 counts
    print(f"Program on the predicted ledger: TA {s['TA']:.1f} (Rev {s['Rev']:.1f}, Hold {s['Hold']:.1f}); the trained "
          f"judge on the same ledgers: TA {sj['TA']:.1f}; paired difference {pdiff(T, Tj, 'TA')}. "
          f"On test_L2, ledger entries matched to case mentions: {meta.get('matched')}; unmatched: {meta.get('unmatched')}; "
          f"malformed ledgers: {meta.get('malformed')}; records without a program answer: {meta.get('no_answer')}." + NL)


def macro_section():
    print("## 5. Macro-averages over rules and families (test_L2, seed 0)" + NL)
    print("| run | TA (pooled) | TA macro over rules | rules | TA macro over families | families |")
    print("|---|---|---|---|---|---|")
    for f, c in CELLS:
        rid = f"B-F-{f}-{c}-s0"
        if not done(rid):
            continue
        T = triplets(rid)
        if not T:
            continue
        by = {"rid": collections.defaultdict(list), "family": collections.defaultdict(list)}
        for t in T.values():
            fl = _flags(t)
            if fl is None:
                continue
            for k in by:
                by[k][t[k]].append(fl["TA"])
        mac = {k: 100.0 * sum(sum(v) / len(v) for v in d.values()) / len(d) for k, d in by.items()}
        print(f"| {rid} | {summarise(T)['all']['TA']:.1f} | {mac['rid']:.1f} | {len(by['rid'])} | {mac['family']:.1f} | "
              f"{len(by['family'])} |")
    print()


def natural_balanced_section():
    print("## 6. Reversal and near-miss correctness, natural and balanced corpora (test_L2, seed 0)" + NL)
    print("| run | Rev | Hold (near-miss correct) | base correct | near-miss correct given base correct | "
          "base and near-miss both correct | TA |")
    print("|---|---|---|---|---|---|---|")
    for f, c in CELLS:
        if c not in ("natural", "balanced"):
            continue
        rid = f"B-F-{f}-{c}-s0"
        if not done(rid):
            print(f"| {rid} | not run | | | | | |")
            continue
        T = triplets(rid)
        fl = [x for x in map(_flags, T.values()) if x is not None]
        n = len(fl)
        base = [x for x in fl if x["BaseAcc"]]
        print(f"| {rid} | {100 * sum(x['Rev'] for x in fl) / n:.1f} | {100 * sum(x['Hold'] for x in fl) / n:.1f} | "
              f"{100 * len(base) / n:.1f} | {100 * sum(x['Hold'] for x in base) / max(1, len(base)):.1f} | "
              f"{100 * sum(x['Hold'] and x['BaseAcc'] for x in fl) / n:.1f} | {100 * sum(x['TA'] for x in fl) / n:.1f} |")
    print()


def budget_section():
    print("## 7. Training budget per finished run" + NL)
    print("| run | GPU | corpus records | examples | reader targets | judge targets | tokens | completion tokens | "
          "steps | train h | eval h |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for d in sorted(os.listdir(RG)):
        if not (d.startswith("B-") and done(d)):
            continue
        m = json.load(open(f"{RG}/{d}/meta.json"))
        ps, tr = m.get("pretok_stats") or {}, m.get("train") or {}
        if not ps or not str(m.get("corpus", "")).startswith("rule_v1") or m.get("provisional"):
            continue
        parts = ps.get("parts", {})
        n_corpus = REG.get(m["corpus"], {}).get("n_records")
        print(f"| {d} | {m['gpu'].split(',')[0]} | {n_corpus} | {ps.get('examples')} | {parts.get('reader', '-')} | "
              f"{parts.get('judge', '-')} | {ps.get('tokens')} | {ps.get('completion_tokens')} | {tr.get('steps')} | "
              f"{tr.get('train_seconds', 0) / 3600:.2f} | {m.get('eval_seconds', 0) / 3600:.2f} |")
    print()


def resampling_section():
    print("## 8. Was donor-ledger resampling active?" + NL)
    print("Two-stage runs draw a judge pair's ledger, claim and label from another case of the same rule, condition "
          "and claim type with probability resample_p (DECISIONS_B). From the pre-tokenisation statistics:" + NL)
    print("| run | resample_p | judge examples | judge pairs (both claims) | pairs drawn from a donor case | share | "
          "(rule, condition, claim type) groups |")
    print("|---|---|---|---|---|---|---|")
    for d in sorted(os.listdir(RG)):
        if not (d.startswith("B-") and done(d)):
            continue
        m = json.load(open(f"{RG}/{d}/meta.json"))
        ps = m.get("pretok_stats") or {}
        if "pairs_swapped" not in ps or m.get("provisional"):
            continue
        key = m.get("train_key", "")
        p = re.search(r"__p([0-9.]+)__", key)
        judge = ps.get("judge", ps.get("parts", {}).get("judge")) or 0
        pairs = judge // 2
        print(f"| {d} | {p[1] if p else '-'} | {judge} | {pairs} | {ps['pairs_swapped']} | "
              f"{100.0 * ps['pairs_swapped'] / max(1, pairs):.1f}% | {ps.get('resample_groups')} |")
    print()


def field_section():
    print("## 9. Field interventions on the ledger x triplets adapter (test_L2)" + NL)
    e = f"{RG}/B-AE-field-edit/summary_rule_v1~test_L2~edit.json"
    s = f"{RG}/B-AE-field-swap/summary_rule_v1~test_L2~swap.json"
    if os.path.exists(e):
        d = json.load(open(e))
        print("Edit subject, status or time of one mention in a correct ledger; agreement of the judge with the program's "
              "verdict after the edit:" + NL)
        print("| group | n | verdicts that follow the program (%) |")
        print("|---|---|---|")
        for k, v in d["by"].items():
            print(f"| {k} | {v['n']} | {v['agreement']:.1f} |")
        cnt = collections.defaultdict(lambda: [0, 0])
        for line in open(f"{RG}/B-AE-field-edit/scores_rule_v1~test_L2~edit.jsonl", encoding="utf-8"):
            r = json.loads(line)
            ok = (r["u"] > 0) == (r["expected"] == 1)
            for key in ((r["kind"], r["field"], r["changed"]), ("case " + r["iid"].split("/")[1], r["field"], r["changed"])):
                cnt[key][0] += ok
                cnt[key][1] += 1
        print(NL + "By condition kind or case, field and whether the edit changes the program's verdict. The edit changes "
              "the field only; found keeps the case's quotation. A measurement edited to no applicable value is missing "
              "input (neither claim holds):" + NL)
        print("| group | field | verdict changes | n | follow the program (%) |")
        print("|---|---|---|---|---|")
        for k in sorted(cnt):
            print(f"| {k[0]} | {k[1]} | {'yes' if k[2] else 'no'} | {cnt[k][1]} | {100 * cnt[k][0] / cnt[k][1]:.1f} |")
    else:
        print("Edits: not run (B-AE-field-edit pending).")
    print()
    if os.path.exists(s):
        d = json.load(open(s))
        print(f"Swap in the ledger of another case (same rule, condition and claim): the judge returns the verdict that "
              f"ledger implies in {d['agreement']:.1f}% of {d['n']} records.")
    else:
        print("Swaps: not run (B-AE-field-swap pending).")
    print()


def loko_section():
    print("## 10. Leave one near-miss kind out (test_L2, triplets of the held-out kind; FINAL_TASKS_B P0.5)" + NL)
    print("| held-out kind | format | trained without the kind | trained on all kinds (B-F-<format>-triplets-s0) | "
          "without - all [95% CI], p |")
    print("|---|---|---|---|---|")
    for kind in ("subject", "time", "boundary"):
        for fmt in ("verdict", "summary2", "ledger2"):
            a, b = f"B-LOKO-{kind}-{fmt}-s0", f"B-F-{fmt}-triplets-s0"
            if not (done(a) and done(b)):
                print(f"| {kind} | {fmt} | not run | | |")
                continue
            Ta = {t: v for t, v in triplets(a).items() if v["nm_kind"] == kind}
            Tb = {t: v for t, v in triplets(b).items() if v["nm_kind"] == kind}
            print(f"| {kind} | {fmt} | {summarise(Ta)['all']['TA']:.1f} | {summarise(Tb)['all']['TA']:.1f} | "
                  f"{pdiff(Ta, Tb, 'TA')} |")
    print()


def case_visible_section():
    print("## 11. Summary pipeline whose judge also sees the case (test_L2, triplets corpus, seed 0; FINAL_TASKS_B P0.4)" + NL)
    a, b, c = "B-SC-summary2-triplets-s0", "B-F-summary2-triplets-s0", "B-F-ledger2-triplets-s0"
    if not all(map(done, (a, b, c))):
        print("not run" + NL)
        return
    T = {r: triplets(r) for r in (a, b, c)}
    print("| run | judge sees | TA | Rev | Hold |")
    print("|---|---|---|---|---|")
    for r, sees in ((a, "rule, case, prose record, claim"), (b, "rule, prose record, claim"), (c, "rule, ledger, claim")):
        s = summarise(T[r])["all"]
        print(f"| {r} | {sees} | {s['TA']:.1f} | {s['Rev']:.1f} | {s['Hold']:.1f} |")
    print(NL + f"Case-visible minus blind summary judge, TA: {pdiff(T[a], T[b], 'TA')}; ledger minus case-visible summary "
          f"judge, TA: {pdiff(T[c], T[a], 'TA')}." + NL)


def xr_section():
    print("## 12. Rule-side items (xr_v1/test; A's set, 400 items = 2 rules x 3 cases; conclusion claims)" + NL)
    print("An item is solved iff all its cells are right (crossed accuracy XA, selrm.metrics.crossed_accuracy; "
          "B-NS runs score a kept adapter, other runs evaluated the set themselves)." + NL)
    print("| run | XA | cell accuracy | XA currency | XA inclusivity | XA subject | XA window |")
    print("|---|---|---|---|---|---|---|")
    for sp in sorted(glob.glob(f"{RG}/*/summary_xr_v1~test.json")):
        x = json.load(open(sp)).get("xr", {}).get("conclusion")
        if x:
            g = lambda k: f"{x[k]:.1f}" if x.get(k) is not None else "-"
            print(f"| {os.path.basename(os.path.dirname(sp))} | {g('XA')} | {g('CellAcc')} | {g('XA_currency')} | "
                  f"{g('XA_inclusivity')} | {g('XA_subject')} | {g('XA_window')} |")
    print()


def seeds_section():
    print("## 13. Core cells across seeds (test_L2; FINAL_TASKS_B P0.3; mean and s.d. over the finished seeds)" + NL)
    print("| cell | metric | s0 | s1 | s2 | s3 | s4 | mean | s.d. | n |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for fmt in ("verdict", "summary2", "ledger2"):
        for corpus in ("blocks", "triplets"):
            S = {sd: json.load(open(p))["all"] for sd in range(5)
                 if os.path.exists(p := f"{RG}/B-F-{fmt}-{corpus}-s{sd}/summary_rule_v1~test_L2.json") and done(f"B-F-{fmt}-{corpus}-s{sd}")}
            for m in ("TA", "Rev", "Hold"):
                t = seed_table({sd: v[m] for sd, v in S.items()})
                cells = " | ".join(f"{S[sd][m]:.1f}" if sd in S else "-" for sd in range(5))
                f = lambda x: "-" if x is None else f"{x:.1f}"
                print(f"| {fmt} x {corpus} | {m} | {cells} | {f(t['mean'])} | {f(t['sd'])} | {t['n']} |")
    print()


def fields_section():
    print("## 14. What the ledger's subject/status/time fields add: ledger minus value ledger (test_L2, seed 0)" + NL)
    print("| corpus | metric | ledger | value ledger | ledger - value ledger [95% CI], p |")
    print("|---|---|---|---|---|")
    for corpus in ("blocks", "triplets"):
        a, b = f"B-F-ledger2-{corpus}-s0", f"B-F-value2-{corpus}-s0"
        if not (done(a) and done(b)):
            print(f"| {corpus} | | not run | | |")
            continue
        Ta, Tb = triplets(a), triplets(b)
        sa, sb = summarise(Ta)["all"], summarise(Tb)["all"]
        for m in ("TA", "Rev", "Hold"):
            print(f"| {corpus} | {m} | {sa[m]:.1f} | {sb[m]:.1f} | {pdiff(Ta, Tb, m)} |")
    print()


def ablation_section():
    print("## 15. Ablations (Table 9; test_L2, seed 0; each row against its own reference: B-F-ledger2-triplets-s0 "
          "unless named)" + NL)
    ref = "B-F-ledger2-triplets-s0"
    own = {"B-AB-pairwise-s0": "B-F-verdict-triplets-s0",      # verdict format, Bradley-Terry instead of pointwise
           "B-AB-probe-rw-s0": "B-F-ledger2-blocks-s0"}        # trained without near-misses (the '- near-misses' row)
    runs = sorted(os.path.basename(d) for d in glob.glob(f"{RG}/B-AB-*-s0") if done(os.path.basename(d)))
    runs += [r for r in ("B-AE-pred-bit-program", "B-AE-program-ledger", "B-AE-premise-gate") if done(r)]   # eval-only rows
    if not runs or not done(ref):
        print("not run" + NL)
        return
    Tr = triplets(ref)
    print("| run | TA | Rev | Hold | reference | TA minus reference [95% CI], p |")
    print("|---|---|---|---|---|---|")
    for r in [ref] + runs:
        T = triplets(r)
        if not T:
            continue
        s = summarise(T)["all"]
        rr = own.get(r, ref)
        cmp = "-" if r == ref else pdiff(T, Tr if rr == ref else triplets(rr), "TA") if done(rr) else "not run"
        print(f"| {r} | {s['TA']:.1f} | {s['Rev']:.1f} | {s['Hold']:.1f} | {'-' if r == ref else rr} | {cmp} |")
    print()


def main():
    sys.stdout.reconfigure(newline="\n")
    print("# Role B analyses on existing predictions (FINAL_TASKS_B P0.1)" + NL)
    print("Generated by scripts/analysis_b.py from results_git/ and the rule_v1 records; seed 0, provisional. "
          "\"not run\" = the input result does not exist yet." + NL)
    for f in (paired_section, leakage_section, transitions_section, program_ledger_section, macro_section,
              natural_balanced_section, budget_section, resampling_section, field_section, loko_section,
              case_visible_section, xr_section, seeds_section, fields_section, ablation_section):
        f()


if __name__ == "__main__":
    main()
