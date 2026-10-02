# salvage/

The first dataset build (1-2 Oct), kept for reference. Role A ports what fits
(rules, phrase banks, engine pieces) to the record format in `docs/INTERFACES.md`
and `selrm/schema.py` at the repo root; nothing here is imported by the main
package, and nothing here should be copied over as-is. `docs/SALVAGE.md` in this
folder lists every file, its tests and its known gaps. Copies of shared files
that the repo root already holds were left out.

Its tests use this folder's own `selrm` package, so run them from here:

    cd salvage && python -m pytest -q

The repo-root `conftest.py` keeps them out of the main test run.
