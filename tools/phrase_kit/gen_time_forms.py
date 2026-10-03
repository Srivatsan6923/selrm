"""Write banks/T.json: value-neutral past and superseded forms for numeric concepts.

Numeric time groups carry an old reading in every case (base and flip with a
default-side value, the near-miss with a flip-side value in the same template),
so these templates must read naturally for any value: no episode, no reason.
Frames are shared across concepts (4 train, 2 test); cue words follow the split.
"""
import json
from pathlib import Path

NAMES = {   # concept -> (name containing a keyword, unit)
    "alt_enzyme": ("ALT", "U/L"), "arterial_ph": ("arterial pH", ""), "bmi": ("body mass index", "kg/m2"),
    "bun": ("blood urea nitrogen", "mg/dL"), "calf_swelling": ("calf swelling", "cm"),
    "creatinine": ("serum creatinine", "mg/dL"), "egfr": ("eGFR", "mL/min/1.73 m2"),
    "heart_rate": ("heart rate", "/min"), "hemoglobin": ("Hgb", "g/dL"),
    "inr": ("international normalized ratio", ""), "map": ("mean arterial pressure", "mmHg"),
    "neutrophils": ("neutrophil count", "x10^9/L"), "platelets": ("platelet count", "x10^9/L"),
    "potassium": ("serum potassium", "mmol/L"), "rr": ("respiratory rate", "/min"),
    "sbp": ("systolic blood pressure", "mmHg"), "spo2": ("oxygen saturation", "%"),
    "temperature": ("temperature", "C"), "wbc": ("white cell count", "x10^9/L"), "weight": ("weight", "kg"),
}
PAST = ["In {year}, {name} was {val}.",
        "{Name} of {val} recorded in {year}.",
        "{Name} was {val} when measured in {year}.",
        "{Name} {val} at a hospital visit in {year}.",
        "Records from {year} list {name} at {val}.",
        "Back in {year}, {name} stood at {val}."]
SUPERSEDED = ["Yesterday, {name} was {val}; today's value replaces it.",
              "Previously, {name} was {val}; it has since been repeated.",
              "{Name} was {val} yesterday, before today's repeat.",
              "{Name} of {val} measured yesterday was replaced by a repeat measurement.",
              "Earlier this week, {name} was {val}; a newer reading supersedes it.",
              "Last month, {name} was {val}; the newest measurement replaces it."]


def fill(frame, name, unit):
    val = "{v}" + ("" if not unit else unit if unit[0] in "/%" else " " + unit)
    cap = name if name[1:2].isupper() else name[0].upper() + name[1:]   # eGFR stays eGFR
    return frame.replace("{Name}", cap).replace("{name}", name).replace("{val}", val)


out = {c: {"past": [fill(f, n, u) for f in PAST], "superseded": [fill(f, n, u) for f in SUPERSEDED]}
       for c, (n, u) in NAMES.items()}
(Path(__file__).parent / "banks" / "T.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print(f"T.json: {len(out)} concepts; e.g. {out['egfr']['past'][0]} | {out['spo2']['superseded'][4]}")
