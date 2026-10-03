"""Apply the length-plan moves to a copy of main.tex, build each cumulative
step with tectonic and measure where Limitations starts.

Usage: python apply_moves.py BASE_DIR OUT_DIR [N]
  BASE_DIR  folder with the v13 sources (main.tex, acl.sty, .bst, .bib, .bbl)
  OUT_DIR   scratch folder; step k (moves 1..k applied) is built in OUT_DIR/step_kk
  N         apply only the first N moves (default: all)

Each move cuts one or more spans (start marker .. end marker, inclusive;
spaces in a marker match any whitespace), leaves a pointer at the cut, and
pastes the cut text at an appendix anchor. Prose is pasted with its line
breaks joined; floats are pasted verbatim with [t] changed to [!ht].
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fitz  # noqa: E402
import floatcheck  # noqa: E402

TECTONIC = "D:/NAACL27/tools/tectonic.exe"


def rx(marker):
    return re.compile(r"\s+".join(re.escape(p) for p in marker.split()))


def find1(text, marker, start=0):
    hits = list(rx(marker).finditer(text, start))
    assert len(hits) == 1, f"marker found {len(hits)} times: {marker[:70]!r}"
    return hits[0]


def norm(s):
    s = " ".join(s.split())
    assert not re.search(r"(?<!\\)%", s), "unescaped % in prose being joined"
    return s


def cut(text, start, end, pointer=""):
    """Cut from the start marker to the end marker (inclusive); leave pointer."""
    a = find1(text, start)
    b = find1(text, end, a.start())
    return text[:a.start()] + pointer + text[b.end():], text[a.start():b.end()]


def cut_env(text, label):
    """Cut the float environment that carries \\label{label}; [t] -> [!ht]."""
    lab = find1(text, "\\label{" + label + "}")
    begin = max(text.rfind("\\begin{table", 0, lab.start()), text.rfind("\\begin{figure", 0, lab.start()))
    m = re.compile(r"\\end\{(table|figure)\*?\}").search(text, lab.end())
    env = re.sub(r"^(\\begin\{(?:table|figure)\})\[t\]", r"\1[!ht]", text[begin:m.end()])  # starred: keep [t]
    return text[:begin] + text[m.end():], env


def insert(text, anchor, payload, where="after"):
    m = find1(text, anchor)
    pos = m.end() if where == "after" else m.start()
    return text[:pos] + payload + text[pos:]


# ---------------------------------------------------------------- moves
def m01(t):
    """Proposition 1, proof and the feature-collision paragraph -> App F (start)."""
    t, mv = cut(t, "\\begin{proposition}", "sampled readouts are reported with tie rates and intervals.")
    t = insert(t, "ties are failures.", r" A deterministic scorer that uses only the claim, only the case, or only"
               r" whether the decisive concept is named solves no triplet, and flip pairs alone exclude only the"
               r" first two (Proposition~\ref{prop:blind}, Appendix~\ref{app:diag}).")
    return insert(t, "\\label{app:diag}", "\n\n" + mv.strip() + "\n")


def m02(t):
    """Table 1 (sources and constructs) -> App D (start)."""
    t, env = cut_env(t, "tab:sources")
    return insert(t, "\\label{app:qa}", "\n\n" + env + "\n")


def m03(t):
    """Section 4 (parts and whole, composition gap) and the 7.1 gap sentence -> App F."""
    t, mv = cut(t, "\\section{Diagnostics} \\label{sec:diagnostic}",
                "edit moves the preference relative to a missing-input baseline.")
    parts = norm(mv.split("\\paragraph{Parts and whole.}")[1].split("Appendix~\\ref{app:diag} analyses")[0])
    t, mv2 = cut(t, "Every signal reverses correctly on at least", "in which it solves both (Appendix~\\ref{app:diag}).")
    mv2 = norm(mv2).replace("(Appendix~\\ref{app:diag})", "(Table~\\ref{tab:pk})")
    t = insert(t, "determine matter.", r" Appendix~\ref{app:diag} decomposes reversal into reading and application"
               r" pairs and analyses how far a decisive edit moves the preference.")
    return insert(t, "\\paragraph{Near-miss decisions.}",
                  "\\paragraph{Parts and whole.}\n" + parts + " " + mv2 + "\n\n", where="before")


def m04(t):
    """'What follows by construction, and what does not' -> App E (end)."""
    t, mv = cut(t, "\\paragraph{What follows by construction, and what does not.}",
                "test a second pass that re-reads every entry against the case \\citep{agand2026venra}.")
    t = insert(t, "the program-supplied-ledger analysis measures that gap.",
               r" What follows from this design by construction, and what is learned and tested,"
               r" is set out in Appendix~\ref{app:ledger}.")
    return insert(t, "the string check cannot detect this.", "\n\n" + mv.strip() + "\n")


def m05(t):
    """Statistical protocol sentences of 'External data and protocol' -> App A."""
    t, mv = cut(t, "Systems are compared on identical items with paired",
                "versions with their own frozen tests (Appendix~\\ref{app:rules}).",
                pointer=r"Comparisons are paired on identical items, with rules as resampling clusters.")
    return insert(t, "\\noindent\\textbf{Selection and freezing.}",
                  "\\noindent\\textbf{Statistical protocol.} " + norm(mv) + "\n\n", where="before")


def m06(t):
    """Missing-twin semantics from 'Edits and invariants' -> App C."""
    t, mv = cut(t, "For \\emph{missing} twins we distinguish explicit",
                "external datasets keep their own conventions.",
                pointer=r"A \emph{missing} twin makes a decisive input unknown and is kept only if the target"
                        r" claim is then undetermined (Appendix~\ref{app:twins}).")
    mv = norm(mv).replace("otherwise; Appendix~\\ref{app:twins});", "otherwise, as stated above);")
    assert "as stated above" in mv
    return insert(t, "\\paragraph{Near-miss kinds.}", "\\paragraph{Missing twins.}\n" + mv + "\n\n", where="before")


def m07(t):
    """Four small items whose content is (or goes) in the appendix."""
    # (a) several mentions: already stated in App C "Semantics"
    t, _ = cut(t, "When a concept is mentioned more than once, a criterion uses the mentions its predicate counts:",
               "counted mention of a finding with status present.")
    # (b) scoring of malformed ledgers -> App E
    t, mv = cut(t, "A malformed ledger is an explicit invalid outcome:",
                "(log-odds are unbounded, so no finite floor is used).")
    mv = norm(mv).replace("A malformed ledger is an explicit invalid outcome: both claims are rejected and", "As a result")
    assert mv.startswith("As a result")
    t = insert(t, "invalid outcome and both claims are rejected.", " " + mv)
    # (c) rewritten cases: already stated in App C "Text tiers"
    t, _ = cut(t, "\\emph{Rewritten cases} are model rewrites kept only when two extractors",
               "audit set and are not scored (Appendix~\\ref{app:twins}).")
    # (d) why MedCEG is used only in policy training -> App G "Policy training"
    t, mv = cut(t, "MedCEG's reward needs a reference graph for the question,",
                "only in policy training (Appendix~\\ref{app:more}).")
    mv = norm(mv).replace(" (Appendix~\\ref{app:more})", "")
    return insert(t, "uses the answer for each case.", " " + mv)


def m08(t):
    """Manifest and frozen-set sentences of 'Rules and shifts' -> App B."""
    t, mv = cut(t, "MedCalc-Bench calculators \\citep{khandekar2024medcalc}",
                "dependency tests against the rule text.",
                pointer=r"Its manifest and program tests are described in Appendix~\ref{app:rules}.")
    mv = norm(mv)
    keep = mv.split(" A manifest records")[0] + " " + "Every program" + mv.split("Every program")[1]
    t = insert(t, "\\paragraph{Manifest and provenance.}", "\n" + keep)
    t, _ = cut(t, "Rule-side items, author-written cases, rewritten cases and registered criteria (\\S\\ref{sec:twins})",
               "are separate, separately frozen sets.")
    return t


def m09(t):
    """Implementation detail of the training objective -> App G 'Training'."""
    t, mv = cut(t, "In implementation the two terms are separate",
                "the program-supplied-ledger analysis measures that gap.",
                pointer=r"The two terms are separate supervised examples in one corpus, and $\lambda$ is their"
                        r" ratio (Appendix~\ref{app:more}).")
    mv = norm(mv).replace("In implementation the two terms",
                          "The two terms of the training loss (\\S\\ref{sec:ledger})")
    return insert(t, "LoRA rank 64, batch size 64", mv + "\n", where="before")


def m10(t):
    """Figure 3 (rule diversity; selection pressure) -> App G after the ablation table."""
    t, env = cut_env(t, "fig:diversity")
    return insert(t, "\\label{tab:ablation} \\end{table}", "\n\n" + env + "\n")


def m11(t):
    """Section 7.4: four analysis paragraphs -> App G after Figure 3."""
    t, a = cut(t, "\\emph{Own against program-supplied ledgers.}", "reaches \\ph{tbd}\\% against 98.0\\% without it.")
    t, b = cut(t, "\\emph{Near-miss kinds not seen in training.}", "evidence of abstention.",
               pointer=r"Program-supplied ledgers, the one-stage variant, near-miss kinds left out of training,"
                       r" rule diversity, model size and missing inputs are analysed in Appendix~\ref{app:more}"
                       r" (Table~\ref{tab:ablation}, Figure~\ref{fig:diversity}).")
    payload = "\n\n\\paragraph{Further analyses of the judge.}\n" + a.strip() + "\n\n" + b.strip() + "\n"
    return insert(t, "\\label{fig:diversity} \\end{figure}", payload)


def m12(t):
    """Section 3.2: descriptions of the external sources -> App D."""
    t, mv = cut(t, "\\emph{Registered criteria} are unambiguous", "consistency with base F1.",
                pointer=r"The external tiers are registered trial eligibility criteria with author-checked"
                        r" programs, physician criterion-level labels from the TrialGPT annotations"
                        r" \citep{jin2024trialgpt}, MedEinst control and trap cases \citep{chen2026medeinst},"
                        r" key pairs of exam questions from MedQA \citep{jin2021medqa} and CareQA"
                        r" \citep{ariasduart2025careqa} whose keyed answers each occur among the other's options,"
                        r" and NLI4CT-P statement edits \citep{jullien2024semeval}; Appendix~\ref{app:qa}"
                        r" describes each source and its protocol.")
    mv = norm(mv).replace("(protocol in Appendix~\\ref{app:qa})", "(protocol below)")
    assert "(protocol below)" in mv
    return insert(t, "\\paragraph{Releases.}", "\\paragraph{Sources.}\n" + mv + "\n\n", where="before")


def m13(t):
    """Table 5 (candidate selection) -> App G before 'Selection protocol'."""
    t, env = cut_env(t, "tab:downstream")
    return insert(t, "\\paragraph{Selection protocol.}", env + "\n\n", where="before")


def m14(t):
    """Section 7.3 'Alternatives' -> App G before 'Policy training'."""
    t, mv = cut(t, "\\paragraph{Alternatives.}", "leads on L2, key pairs and NLI4CT-P.")
    t = insert(t, "with diseases held out it is \\ph{58.9}\\% (Appendix~\\ref{app:qa}).",
               r" Verifiers that write and execute code, and the closed judge, are compared in"
               r" Appendix~\ref{app:more}.")
    return insert(t, "\\paragraph{Policy training.}", mv.strip() + "\n\n", where="before")


def m15(t):
    """Related-work detail -> new appendix section 'Further Related Work'."""
    t, ctx = cut(t, "\\paragraph{Context against prior, and counterfactual data.}", "\\citep{poliak2018hypothesis}.")
    t, other = cut(t, "Other work perturbs steps and keeps a verifier at", "\\citep{pronesti2026vprm}.")
    t, typed = cut(t, "Typed evidence records and distractors that are similar but irrelevant",
                   "physician-annotated judgments \\citep{jin2024trialgpt}.")
    t = insert(t, "representations under one budget.", r" Further related work, on step perturbation,"
               r" typed evidence records, knowledge conflicts, clinical anchoring and counterfactual data, is"
               r" discussed in Appendix~\ref{app:related}.")
    sec = ("\\section{Further Related Work}\n\\label{app:related}\n\n"
           "\\paragraph{Step perturbation and typed evidence.}\n" + norm(other) + " " + norm(typed) + "\n\n"
           + ctx.strip() + "\n\n")
    return insert(t, "\\ifplaceholders\\else", sec, where="before")


def m16(t):
    """Table 4 caption: notes on the rows -> App D."""
    t, mv = cut(t, "Black: measured, seed 0; rule-tier cells", "and its gap to 100 is extraction error.",
                pointer=r"MR is at the ceiling for every trained model and does not separate them; notes on the"
                        r" rows are in Appendix~\ref{app:qa}.")
    mv = norm(mv).replace("MR is at the ceiling for every trained model and does not separate them. ", "")
    assert "MR is at" not in mv
    return insert(t, "\\paragraph{NLI4CT-P.}",
                  "\\paragraph{Notes to Table~\\ref{tab:main}.}\n" + mv + "\n\n", where="before")


def m17(t):
    """7.2: corpora without unchanged-outcome cases and the DynaCF-style re-weighting -> App G."""
    t, mv = cut(t, "Data from a pipeline that keeps only interventions that change the",
                "of DynaCF to case edits, gives \\ph{tbd} (Table~\\ref{tab:ablation}).",
                pointer=r"Re-weighting by near-miss probes instead of training on near-misses, after DynaCF,"
                        r" is in Table~\ref{tab:ablation}.")
    return insert(t, "\\paragraph{Further analyses of the judge.}",
                  "\\paragraph{Training without unchanged-outcome cases.}\n" + norm(mv) + "\n\n", where="before")


def m19(t):
    """7.5: the no-near-miss ablation of selection and the effect of N -> App G 'Selection protocol'."""
    t, mv = cut(t, "Without near-misses in training the combined reward loses",
                "(Figure~\\ref{fig:diversity}, right).",
                pointer=r"The ablation without near-misses and the effect of $N$ are in Appendix~\ref{app:more}.")
    return insert(t, "A trace is eligible if it contains a final answer", norm(mv) + " ", where="before")


def m20(t):
    """Figure 2 (overview) -> App E (start), with a pointer in the introduction. Last resort."""
    t, env = cut_env(t, "fig:overview")
    t = insert(t, "each measuring a different construct (Table~\\ref{tab:sources}).",
               r" Figure~\ref{fig:overview} in Appendix~\ref{app:ledger} gives an overview of data, training,"
               r" inference and evaluation.")
    return insert(t, "\\label{app:ledger}", "\n\n" + env + "\n")


def m18(t):
    """Step check: why the minimum is a heuristic, and step-level reading -> App G 'Selection protocol'."""
    t, mv = cut(t, "The minimum is a heuristic: it is an upper bound",
                "the ledger can depend on it (Appendix~\\ref{app:ledger}).",
                pointer=r"The minimum is a heuristic; the product, a fitted combination and reliability gating"
                        r" \citep{evpv2026} are compared in Appendix~\ref{app:more}.")
    mv = norm(mv).replace(" (Appendix~\\ref{app:more})", "")
    return insert(t, "\\paragraph{Selection protocol.}", "\n" + mv + " ")


MOVES = [m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]

def build(folder):
    r = subprocess.run([TECTONIC, "-X", "compile", "main.tex", "--keep-logs"], cwd=folder,
                       capture_output=True, text=True)
    log = (Path(folder) / "main.log").read_text(errors="replace")
    undef = sorted(set(re.findall(r"Reference `([^']+)' on page \d+ undefined", log)))
    undef += sorted(set(re.findall(r"Citation `([^']+)' on page \d+ undefined", log)))
    multi = sorted(set(re.findall(r"Label `([^']+)' multiply defined", log)))
    return r.returncode, undef, multi


def main():
    base, out = Path(sys.argv[1]), Path(sys.argv[2])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else len(MOVES)
    text = (base / "main.tex").read_text(encoding="utf-8")
    out.mkdir(parents=True, exist_ok=True)
    for k in range(0, n + 1):
        if k > 0:
            text = MOVES[k - 1](text)
        d = out / f"step_{k:02d}"
        d.mkdir(exist_ok=True)
        for f in ("acl.sty", "acl_natbib.bst", "custom.bib", "main.bbl", "numbers.tex"):
            if (base / f).exists():
                shutil.copy(base / f, d / f)
        (d / "main.tex").write_text(text, encoding="utf-8", newline="\n")
        rc, undef, multi = build(d)
        doc = fitz.open(d / "main.pdf")
        lim, lim_pos, eff, report = floatcheck.check(str(d / "main.tex"), str(d / "main.pdf"))
        late = [r[1] for r in report if r[3]]
        missing = [r[1] for r in report if r[2] is None]
        name = "base" if k == 0 else MOVES[k - 1].__name__
        print(f"{k:2d} {name:4s} rc={rc} pdfpages={len(doc)} Limitations p{lim[0]}{lim[1]} y={lim[2]:6.1f}"
              f" heading={lim_pos:.3f} effective={eff:.3f} undefined={undef} multiply={multi}"
              f" main_floats_after_Limitations={late} unmatched={missing}", flush=True)


if __name__ == "__main__":
    main()
