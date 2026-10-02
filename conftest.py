# salvage/ has its own selrm package and tests; run those from inside salvage/
# (cd salvage && python -m pytest -q), never from the repo root.
collect_ignore = ["salvage"]
