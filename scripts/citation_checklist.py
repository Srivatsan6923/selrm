"""Citation checklist for the authors (FINAL_TASKS_D P0.4, HUMAN_TASKS H5).

  python scripts/citation_checklist.py [paper_dir]

Reads main.tex and custom.bib in paper_dir (default: paper/latex_v13; a main.bbl
there is cross-checked) and writes

  docs/CITATIONS_TODO.csv     one row per cited key (utf-8-sig): bib fields,
                              mechanical flags, the source sentence of every
                              citation, and empty columns for the authors
  docs/CITATION_CHECKLIST.md  instructions, counts, entries never cited and
                              keys cited but missing from the bib

It extracts and flags only; it checks nothing against the cited papers. It
exits with status 1 if its own consistency checks fail.
"""
import csv
import hashlib
import os
import re
import sys
from bisect import bisect_left, bisect_right
from collections import Counter
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAPER = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "paper", "latex_v13")
TEX, BIB, BBL = (os.path.join(PAPER, n) for n in ("main.tex", "custom.bib", "main.bbl"))
OUT_CSV = os.path.join(ROOT, "docs", "CITATIONS_TODO.csv")
OUT_MD = os.path.join(ROOT, "docs", "CITATION_CHECKLIST.md")
LATEST_YEAR = 2026  # the paper is submitted in October 2026
VENUE_FIELDS = ("journal", "booktitle", "howpublished", "school", "institution", "organization", "publisher")
AUTHOR_COLS = ["title_ok", "authors_ok", "venue_ok", "attributed_sentence_ok", "checked_by", "action", "notes"]
COLS = ["key", "n_citations", "sections", "lines_in_main_tex", "entry_type", "title", "authors", "year",
        "venue", "url_doi_eprint", "note", "flags", "sentences"] + AUTHOR_COLS

# natbib commands that take keys (\citestyle, \citetext and the like do not)
CITE = re.compile(r"\\(nocite|[Cc]ite(?:t|p|alt|alp|author|fullauthor|year|yearpar|num|talias|palias)?)\*?(?![A-Za-z])")
CITE_SIMPLE = re.compile(CITE.pattern + r"\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}")  # second reading, for the self-check
HEAD = re.compile(r"\\appendix(?![A-Za-z])|\\(section|subsection)(\*?)\s*(?:\[[^\]]*\])?(?=\{)")
# Sentence boundaries. Paragraph breaks are found in the raw text, where a
# comment-only line is not blank (TeX does not end a paragraph there).
PARA = re.compile(r"\n[ \t]*\n")
HARD = re.compile(r"\\(?:(?:sub)*section|paragraph)\*?(?:\[[^\]]*\])?\{(?:[^{}]|\{[^{}]*\})*\}"
                  r"|\\(?:begin|end)\{[^}]*\}|\\(?:caption|footnote)\{|\\label\{[^}]*\}"
                  r"|\\item(?![A-Za-z])|\\\\|(?<!\\)&")
SENT_END = re.compile(r"[.?!]([)\]}'\"]*)(\s+)")
ABBREV = re.compile(r"(?:\b(?:e\.g|i\.e|et al|cf|vs|Figs?|Eqs?|Secs?|Tabs?|resp|approx)|(?<![A-Za-z])[A-Z])$")
ENTRY = re.compile(r"@[ \t]*(\w+)[ \t]*([{(])")
KEY = re.compile(r"\s*([^,\s{}]+)")
FIELD = re.compile(r"([A-Za-z][\w\-.:]*)\s*=\s*")
BARE = re.compile(r"[^\s,#{}()\"=]+")
WS = re.compile(r"\s*")
MARK = re.compile(r"\b(VERIFY|TODO)\b")
NEW_ID = re.compile(r"(\d{2})(\d{2})\.(\d{4,5})(v\d+)?")
OLD_ID = re.compile(r"[a-z\-]+(\.[A-Z]{2})?/\d{7}(v\d+)?")


def skip_ws(s, i):
    return WS.match(s, i).end()


def braced(s, i, tex=True):
    """s[i] is '{': return (content, index after the matching '}'). In TeX a
    backslash escapes the next character; BibTeX counts every brace."""
    depth, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\" and tex:
            j += 2
            continue
        depth += (c == "{") - (c == "}")
        if depth == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError(f"unbalanced braces from offset {i}")


def mask_comments(tex):
    """Blank out every %-comment (a % after an even number of backslashes); offsets stay valid."""
    return re.sub(r"(?<!\\)((?:\\\\)*)%[^\n]*",
                  lambda m: m.group(1) + " " * (len(m.group()) - len(m.group(1))), tex)


# ---------- BibTeX ----------
def bib_value(text, i, strings):
    """Field value at text[i:]: braced, quoted or bare parts joined by '#'. Returns (value, next index)."""
    parts = []
    while True:
        i = skip_ws(text, i)
        if text[i] == "{":
            v, i = braced(text, i, tex=False)
        elif text[i] == '"':
            j, depth = i + 1, 0
            while text[j] != '"' or depth:
                depth += (text[j] == "{") - (text[j] == "}")
                j += 1
            v, i = text[i + 1:j], j + 1
        else:
            m = BARE.match(text, i)
            if not m:
                raise ValueError(f"unexpected {text[i:i + 30]!r}")
            v, i = strings.get(m.group().lower(), m.group()), m.end()
        parts.append(v)
        i = skip_ws(text, i)
        if text[i] != "#":
            return " ".join("".join(parts).split()), i
        i += 1


def parse_bib(text):
    """Return ({key: entry}, {key: times defined} for keys defined more than once).
    An entry holds key, type, fields (lower-case names, whitespace collapsed), the
    %-lines directly above it (a blank line ends that block) and its line number."""
    entries, seen, strings, pos = {}, Counter(), {}, 0
    while m := ENTRY.search(text, pos):
        kind, line = m.group(1).lower(), text.count("\n", 0, m.start()) + 1
        comment = []
        for ln in reversed(text[pos:m.start()].split("\n")[:-1]):
            if not ln.strip().startswith("%"):
                break
            comment.insert(0, ln.strip().lstrip("%").strip())
        try:
            if m.group(2) == "(":
                raise ValueError("entries delimited by parentheses are not supported")
            if kind in ("comment", "preamble"):
                pos = braced(text, m.end() - 1, tex=False)[1]
                continue
            if kind == "string":
                f = FIELD.match(text, skip_ws(text, m.end()))
                strings[f.group(1).lower()], i = bib_value(text, f.end(), strings)
                pos = skip_ws(text, i) + 1
                continue
            k = KEY.match(text, m.end())
            key, i, fields = k.group(1), k.end(), {}
            while True:
                i = skip_ws(text, i)
                if text[i] == "}":
                    break
                if text[i] == ",":
                    i += 1
                    continue
                f = FIELD.match(text, i)
                if not f:
                    raise ValueError(f"expected a field at {text[i:i + 30]!r}")
                value, i = bib_value(text, f.end(), strings)
                fields.setdefault(f.group(1).lower(), value)  # BibTeX keeps the first of repeated fields
        except (AttributeError, IndexError, ValueError) as e:
            sys.exit(f"{BIB}, line {line}: cannot parse @{kind} ({e})")
        pos = i + 1
        seen[key] += 1
        entries.setdefault(key, {"key": key, "type": kind, "fields": fields,
                                 "comment": " ".join(comment), "line": line})
    return entries, {k: n for k, n in seen.items() if n > 1}


def venue(f):
    parts = [f[n] for n in VENUE_FIELDS if f.get(n)]
    if f.get("eprint"):
        parts.append(f"{f.get('archiveprefix') or f.get('eprinttype') or 'eprint'}:{f['eprint']}")
    return "; ".join(parts + [f"{n} {f[n]}" for n in ("volume", "number", "pages") if f.get(n)])


def arxiv_ids(f):
    ids = re.findall(r"arxiv(?::\s*|\.org/(?:abs|pdf)/)([^\s,;{}]+)", " ".join(f.values()), re.I)
    if f.get("eprint") and (f.get("archiveprefix") or f.get("eprinttype") or "").lower() == "arxiv":
        ids.append(f["eprint"])
    return sorted({re.sub(r"(\.pdf)?\.?$", "", i) for i in ids})


def arxiv_flags(aid, year, preprint_only):
    m = NEW_ID.fullmatch(aid)
    if not m:
        return [] if OLD_ID.fullmatch(aid) else [f"arXiv id {aid} has an unrecognised format"]
    yy, mm, digits = int(m.group(1)), int(m.group(2)), len(m.group(3))
    out, today = [], date.today()
    if not 1 <= mm <= 12 or (yy, mm) < (7, 4):
        out.append(f"arXiv id {aid}: {yy:02d}{mm:02d} is not a valid year and month for this id format")
    want = 5 if (yy, mm) >= (15, 1) else 4
    if digits != want:
        out.append(f"arXiv id {aid}: {digits}-digit number, {want} digits expected for 20{yy:02d}")
    if (2000 + yy, mm) > (today.year, today.month):
        out.append(f"arXiv id {aid} is dated after today")
    if year.isdigit() and (2000 + yy > int(year) or preprint_only and 2000 + yy != int(year)):
        out.append(f"arXiv id {aid} is from 20{yy:02d} but the year field is {year}")
    return out


def surname_only(name):
    """True for 'Zang', '{R-Align}' or 'Zang,': no given name or initials."""
    if "," in name:
        return not name.split(",", 1)[1].strip()
    return " " not in name.strip("{} ")


def entry_flags(e, owners):
    """[(kind, message)] for problems visible in the entry itself."""
    f, out = e["fields"], []
    for name in ("title", "author", "year"):
        if not f.get(name):
            out.append(("missing field", f"missing {name}"))
    named = [f[n] for n in VENUE_FIELDS if f.get(n)]
    if not named and not f.get("eprint"):
        out.append(("missing field", "missing venue"))
    for where, text in [("comment above the entry", e["comment"])] + [(f"field {n}", v) for n, v in f.items()]:
        if MARK.search(text):
            out.append(("VERIFY/TODO marker", f'custom.bib {where}: "{text}"'))
    year = f.get("year", "")
    if year and not re.fullmatch(r"\d{4}", year):
        out.append(("year", f"year {year!r} is not a 4-digit number"))
    elif year and int(year) > LATEST_YEAR:
        out.append(("year", f"year {year} is later than {LATEST_YEAR}"))
    ids = arxiv_ids(f)
    if not ids and any("arxiv" in v.lower() for v in named):
        out.append(("arXiv id", "arXiv named as venue but no arXiv id given"))
    for aid in ids:
        out += [("arXiv id", msg) for msg in arxiv_flags(aid, year, all("arxiv" in v.lower() for v in named))]
        others = [k for k in owners[aid] if k != e["key"]]
        if others:
            out.append(("arXiv id", f"arXiv id {aid} also used by {', '.join(others)}"))
    # Simplification: splits on every ' and ', also inside braces ({Barnes and Noble}); only a flag can go wrong
    names = [n.strip() for n in re.split(r"\s+and\s+", f.get("author", "")) if n.strip()]
    if names and names[-1] == "others":
        out.append(("author list", "author list cut short with 'and others'"))
    short = [n for n in names if n != "others" and surname_only(n)]
    if short:
        out.append(("author list", "author without first name or initials: " + ", ".join(short)))
    return out


# ---------- LaTeX ----------
def cite_keys(clean):
    """[(command, key, start, end)] for each key of each citation command."""
    out = []
    for m in CITE.finditer(clean):
        i = skip_ws(clean, m.end())
        while clean.startswith("[", i):  # optional arguments: \citep[see][p.~4]{key}
            i = skip_ws(clean, clean.index("]", i) + 1)
        if clean.startswith("{", i):
            body, end = braced(clean, i)
            out += [(m.group(1), k.strip(), m.start(), end) for k in body.split(",") if k.strip()]
    return out


def section_marks(clean):
    """[(offset, label)] for every section and subsection, numbered as LaTeX numbers them."""
    marks, sec, sub, num, appendix = [], 0, 0, "", False
    for m in HEAD.finditer(clean):
        kind, star = m.group(1), m.group(2)
        if not kind:  # \appendix: sections continue as A, B, ...
            appendix, sec = True, 0
            continue
        title = " ".join(braced(clean, m.end())[0].split())
        if kind == "section":
            sub = 0
            if not star:
                sec += 1
                num = chr(64 + sec) if appendix else str(sec)
        elif not star:
            sub += 1
        if star:
            label = title
        else:
            label = (f"{num} " if kind == "section" else f"{num}.{sub} ") + title
            if appendix:
                label = "Appendix " + label
        marks.append((m.start(), label))
    return marks


def boundaries(tex, clean):
    """Sorted (starts, ends) of the spans that separate sentences."""
    spans = [m.span() for m in PARA.finditer(tex)] + [m.span() for m in HARD.finditer(clean)]
    for m in SENT_END.finditer(clean):  # a lower-case next word means no sentence end, unless a group closed ('.}')
        if not ABBREV.search(clean[max(0, m.start() - 12):m.start()]) and (
                "}" in m.group(1) or not clean[m.end():m.end() + 1].islower()):
            spans.append(m.span(2))
    return sorted(a for a, _ in spans), sorted(b for _, b in spans)


def sentence(clean, starts, ends, a, b):
    """The source sentence around clean[a:b], whitespace collapsed, unmatched outer braces dropped."""
    i, j = bisect_right(ends, a), bisect_left(starts, b)
    s = " ".join(clean[ends[i - 1] if i else 0:starts[j] if j < len(starts) else len(clean)].split())
    while s.endswith("}") and s.count("}") > s.count("{"):
        s = s[:-1].rstrip()
    while s.startswith("{") and s.count("{") > s.count("}"):
        s = s[1:].lstrip()
    return s


# ---------- output ----------
def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, "/")


def cell(s):
    return " ".join(s.split()).replace("|", "\\|")


def main():
    raw = {p: open(p, "rb").read() for p in (TEX, BIB)}
    tex, bibtext = (raw[p].decode("utf-8-sig") for p in (TEX, BIB))
    clean = mask_comments(tex)
    entries, repeated = parse_bib(bibtext)
    bbl = (set(re.findall(r"\\bibitem\s*(?:\[.*?\])?\s*\{([^}]+)\}", open(BBL, encoding="utf-8").read(), re.S))
           if os.path.exists(BBL) else None)

    occ = cite_keys(clean)
    cites = [o for o in occ if o[0] != "nocite"]
    nocite = [o[1] for o in occ if o[0] == "nocite"]
    marks = section_marks(clean)
    mark_at = [p for p, _ in marks]
    starts, ends = boundaries(tex, clean)
    per_key = {}  # key -> [(line, section, sentence)], in order of first citation
    for _, key, a, b in cites:
        k = bisect_right(mark_at, a)
        per_key.setdefault(key, []).append((tex.count("\n", 0, a) + 1, marks[k - 1][1] if k else "front matter",
                                            sentence(clean, starts, ends, a, b)))
    for key in nocite:
        if key != "*":
            per_key.setdefault(key, [])

    owners = {}
    for key, e in entries.items():
        for aid in arxiv_ids(e["fields"]):
            owners.setdefault(aid, []).append(key)
    rows, kinds = [], Counter()
    for key, items in per_key.items():
        e = entries.get(key)
        flags = entry_flags(e, owners) if e else [("not in bib", "cited but not in custom.bib")]
        if key in repeated:
            flags.append(("repeated key", f"defined {repeated[key]} times in custom.bib; BibTeX uses the first"))
        if not items:
            flags.append(("nocite only", "only in \\nocite: printed in the references, cited in no sentence"))
        if bbl is not None and key not in bbl:
            flags.append(("main.bbl", "not in main.bbl (BibTeX has not been rerun since it was cited)"))
        kinds.update({kind for kind, _ in flags})
        f = e["fields"] if e else {}
        rows.append({
            "key": key, "n_citations": len(items),
            "sections": "; ".join(dict.fromkeys(s for _, s, _ in items)),
            "lines_in_main_tex": ", ".join(str(n) for n, _, _ in items),
            "entry_type": e["type"] if e else "",
            "title": f.get("title", ""), "authors": f.get("author", ""), "year": f.get("year", ""),
            "venue": venue(f),
            "url_doi_eprint": "; ".join(f"{n}: {f[n]}" for n in ("doi", "url", "eprint") if f.get(n)),
            "note": f.get("note", ""), "flags": "; ".join(msg for _, msg in flags),
            "sentences": " || ".join(s for _, _, s in items),
            **{c: "" for c in AUTHOR_COLS},
        })
    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    with open(OUT_CSV, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)

    # Self-check: a second, regex-only reading of the citation commands must find
    # every key occurrence in the CSV, with one sentence per occurrence that names the key.
    problems = []
    simple = Counter(k.strip() for m in CITE_SIMPLE.finditer(clean) if m.group(1) != "nocite"
                     for k in m.group(2).split(",") if k.strip())
    if simple != Counter(k for _, k, _, _ in cites):
        problems.append("the two readings of the citation commands disagree")
    with open(OUT_CSV, encoding="utf-8-sig", newline="") as fh:
        back = {r["key"]: r for r in csv.DictReader(fh)}
    for key, n in simple.items():
        r = back.get(key)
        sents = r["sentences"].split(" || ") if r else []
        if r is None or int(r["n_citations"]) != n or len(sents) != n:
            problems.append(f"{key}: missing from the CSV or counted wrongly")
        elif any(key not in s for s in sents):
            problems.append(f"{key}: a sentence does not contain the key")

    cited = {k for _, k, _, _ in cites}
    printed = cited | set(nocite)
    uncited = [] if "*" in nocite else [e for k, e in entries.items() if k not in printed]
    missing = [k for k in per_key if k not in entries]
    flagged = sum(bool(r["flags"]) for r in rows)
    n_cmds = len({a for _, _, a, _ in cites})
    sha = {p: hashlib.sha256(b).hexdigest() for p, b in raw.items()}
    if bbl is None:
        bbl_line = "- main.bbl: not present."
    else:
        bbl_line = (f"- main.bbl: {len(bbl)} `\\bibitem` entries; cited keys missing from it: "
                    f"{', '.join(sorted(cited - bbl)) or 'none'}; entries in it that are not cited: "
                    f"{', '.join(sorted(bbl - printed)) or 'none'}.")
    md = [
        "# Citation checklist",
        "",
        f"Generated by `python scripts/citation_checklist.py` on {date.today().isoformat()} from "
        f"`{rel(TEX)}` (sha256 {sha[TEX]}) and `{rel(BIB)}` (sha256 {sha[BIB]}). "
        "The script overwrites this file and `docs/CITATIONS_TODO.csv` each time it runs.",
        "",
        "## 1. Checking every cited entry (HUMAN_TASKS H5)",
        "",
        "**Purpose.** For every entry the paper cites, an author opens the cited paper and confirms its "
        "title, its authors, its venue, and that it supports each sentence in which the paper cites it. "
        "The script only extracts the entries and sentences and flags problems that can be found "
        "mechanically. Nothing in the CSV has been checked against a cited paper, and a row without "
        "flags is not thereby correct.",
        "",
        "**Rule: delete what cannot be confirmed.** If a paper cannot be found, or does not support a "
        "sentence that cites it, the citation is removed, and the sentence is rewritten or removed if it "
        "rests on that citation.",
        "",
        "**How to fill the CSV.**",
        "",
        "1. Copy `docs/CITATIONS_TODO.csv` to `docs/CITATIONS_CHECKED.csv` and fill in the copy, keeping "
        "the columns and saving as CSV UTF-8.",
        "2. Each row is one cited key, in order of first citation in main.tex. Split the rows among the "
        "authors; whoever checks a row writes their initials in `checked_by`.",
        "3. Open the paper at its source (publisher or proceedings page, ACL Anthology, arXiv listing), "
        "not through a citation index or a search result snippet.",
        "4. `title_ok`, `authors_ok`, `venue_ok`: yes or no. For no, write the correct value in `notes` "
        "(full author list, venue, year, identifier).",
        "5. `attributed_sentence_ok`: yes only if the paper supports every sentence in `sentences`. There "
        "is one sentence per citation, separated by ` || `, in the order of `lines_in_main_tex`; they are "
        "LaTeX source with comments removed, and the line numbers refer to the main.tex whose sha256 is "
        "given above. For no, give the line and the problem in `notes`.",
        "6. `action`: keep (every check is yes), fix (the paper is confirmed but the entry or a sentence "
        "must change; say what in `notes`) or delete (cannot be confirmed).",
        "7. Start with the rows that have `flags`: VERIFY or TODO notes in custom.bib, missing fields, "
        "author lists cut short with 'and others' or without first names, and arXiv identifiers that do "
        "not fit their format or the year. A flag points to a gap; it decides nothing.",
        "8. Fixes and deletions are then made in `custom.bib` and `main.tex`, and the script is run again.",
        "",
        "**Counts** (computed by the script from the two files above).",
        "",
        f"- Cited keys: {len(cited)}; keys cited but missing from custom.bib: {len(missing)}.",
        f"- Citation occurrences: {len(cites)} in {n_cmds} citation commands (one occurrence per key per "
        "command; commented-out text excluded).",
        f"- Rows in the CSV: {len(rows)}; flagged rows: {flagged}.",
        "- Flagged rows by kind of flag: "
        + ("; ".join(f"{k} {n}" for k, n in kinds.most_common()) or "none") + ".",
        f"- custom.bib: {len(entries)} entries; never cited: {len(uncited)} (section 2); keys defined more "
        f"than once: {', '.join(repeated) or 'none'}.",
        bbl_line,
        "",
        "**Regenerate:** `python scripts/citation_checklist.py` (optional argument: another paper folder; "
        "default `paper/latex_v13`).",
        "",
        "## 2. Entries never cited, keys missing from the bib",
        "",
        "### Entries in custom.bib that are never cited",
        "",
    ]
    if "*" in nocite:
        md += ["`\\nocite{*}` is used, so every entry in custom.bib is printed."]
    elif uncited:
        md += ["natbib prints only entries that are cited (or named in `\\nocite`), so these do not appear "
               "in the references. They need no check unless a citation to them is added; they can be "
               "removed from custom.bib.", "",
               "| key | custom.bib line | year | title |", "|---|---|---|---|"]
        md += [f"| {e['key']} | {e['line']} | {e['fields'].get('year', '')} | {cell(e['fields'].get('title', ''))} |"
               for e in uncited]
    else:
        md += ["None."]
    md += ["", "### Keys cited but missing from custom.bib", ""]
    md += [f"- `{k}`: main.tex lines {', '.join(str(n) for n, _, _ in per_key[k])}" for k in missing] or ["None."]
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(md) + "\n")

    if problems:
        sys.exit("CHECK FAILED\n  " + "\n  ".join(problems))
    print(f"{len(cited)} cited keys, {len(cites)} occurrences in {n_cmds} commands, {flagged} flagged rows, "
          f"{len(uncited)} uncited entries, {len(missing)} missing keys; wrote {rel(OUT_CSV)} and {rel(OUT_MD)}; "
          "self-check passed")


if __name__ == "__main__":
    main()
