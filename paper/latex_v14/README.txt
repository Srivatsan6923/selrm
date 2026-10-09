Learning When to Change -- draft v14 (8 Oct 2026)

Build:  pdflatex main && bibtex main && pdflatex main && pdflatex main
Output: 28 pages; Sections 1-7 fit in 8 pages.

Placeholders
  \placeholderstrue (preamble) prints the red draft banner and allows red text.
  \ph{...}  red note: an experiment not run, or a fact to confirm.
  \tbd      red "tbd": a value that has not been measured.
  Black numbers are measured (status board of 3 Oct 2026).
  Switching to \placeholdersfalse makes the build fail on any remaining
  placeholder, so it can only be done once every value is measured.

Bibliography
  custom.bib marks entries "checked" (confirmed at the source on 8 Oct 2026)
  or "VERIFY" (to be opened at the source before submission).
