# CHANGE REQUESTS (lead answers)

date | from | request | reason | decision
---|---|---|---|---
2026-10-02 | B | MANIFEST.json of every frozen dataset: add `sha256_lf` per file (sha256 of the file bytes with CRLF normalised to LF) and the exact build command + git commit, e.g. `python scripts/make_set.py ... --seed N`. | B trains on NRP (Kubernetes), which cannot read the shared Drive; B rebuilds each frozen set inside the cluster from A's commit and must verify it is byte-identical to A's build (same check already used for smoke_v2: configs/smoke_v2_sha256.json). Fallback if not possible: A uploads frozen sets to a private HF dataset repo that B can download in a CPU Job. |
