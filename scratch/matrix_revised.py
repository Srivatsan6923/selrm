"""One-off (2 Oct evening, lead's revised plan): add the 12 LOKO / dose rows, drop seeds 3-4 of the 16 non-key
factorial cells."""
import csv, io, json, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
p = "docs/RUN_MATRIX_B.csv"
rows = list(csv.DictReader(open(p, encoding="utf-8")))
fields = list(rows[0].keys())
KEY = {("verdict", "blocks"), ("verdict", "triplets"), ("ledger2", "blocks"), ("ledger2", "triplets")}
dropped = 0
for r in rows:
    parts = r["run_id"].split("-")
    if r["run_id"].startswith("B-F-") and r["seed"] in ("3", "4") and (parts[2], parts[3]) not in KEY:
        if r["status"] != "dropped":
            r["status"] = "dropped"
            r["notes"] = (r["notes"] + "; " if r["notes"] else "") + ("dropped 2 Oct (lead's revised plan): the queue "
                          "does not fit before the 7 Oct run freeze; non-key cells keep seeds 0-2")
            dropped += 1
have = {r["run_id"] for r in rows}
template = next(r for r in rows if r["run_id"] == "B-F-ledger2-triplets-s0")
new = []
for kind in ("subject", "negation", "time"):
    for fmt in ("verdict", "ledger2"):
        new.append({**template, "run_id": f"B-LOKO-{kind}-{fmt}-s0", "paper_item": "new: leave one near-miss kind out",
                    "what": f"{fmt} on triplets without {kind} near-misses; TA on the held-out kind (L2, L0) vs "
                            f"B-F-{fmt}-triplets-s0", "data": f"rule_v1/train_triplets_lo_{kind}", "seed": "0",
                    "est_hours": "", "measured_hours": "", "priority": "P1", "depends_on": "A (3e0c832)",
                    "status": "todo", "notes": "eval dev, test_L2, test_L0; subject first"})
for pct in ("05", "12", "25"):
    for fmt in ("verdict", "ledger2"):
        new.append({**template, "run_id": f"B-DOSE-{pct}-{fmt}-s0", "paper_item": "new: near-miss dose",
                    "what": f"{fmt} on blocks with {int(pct)}% of base cases replaced by near-misses (0% = "
                            f"B-F-{fmt}-blocks-s0, 50% = B-F-{fmt}-triplets-s0)", "data": f"rule_v1/train_dose_{pct}",
                    "seed": "0", "est_hours": "", "measured_hours": "", "priority": "P1", "depends_on": "A (3e0c832)",
                    "status": "todo", "notes": "eval dev, test_L2; TA, Hold, Rev vs near-miss share"})
added = [r for r in new if r["run_id"] not in have]
rows += added
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
w.writeheader()
w.writerows(rows)
open(p, "w", encoding="utf-8", newline="").write(buf.getvalue())
print(f"dropped {dropped} rows, added {len(added)} rows, {len(rows)} rows total")
