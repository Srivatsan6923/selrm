"""MedCalc-V (mcv_v1): score specifications over the released entity dictionaries of MedCalc-Bench Verified.

A score is a list of items; an item gives points from the released entities. Specifications are written from
the score text shipped in each instance's explanation (STAGE2_TASKS_A, A1), never from the benchmark's code.
"""
import ast
import csv
import hashlib
import importlib
import pkgutil
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
EXT = ROOT / "data" / "_ext" / "medcalc"
PIN = {"repo": "github.com/nikhilk7153/MedCalc-Bench-Verified", "tag": "v1.0.8",
       "commit": "801592132bfd833f049b517a4e013e00a5fc40fa", "licence": "CC BY-SA 4.0 (data)",
       "sha256": {"test_data.csv": "9d296b09668d945d7c4ad8136032e984a3a3b8b0a7b046eb0f9f787331d9d97d",
                  "train_data.csv": "bd0292576be31e2fa8140c2e9eb456168335a85d1986155f010082d64f497845"}}
RULE_BASED = ("risk", "severity", "diagnosis")


@dataclass(frozen=True)
class Item:
    """One scored item of a score.

    points(ent) -> the points this item gives for an entity dictionary (absent keys follow the convention the
    instance text states). inputs: entity keys the item reads. thresholds: {input key: (unit, cut values)}
    for numeric items, in the unit the score text uses. time is 'current', 'ever' or 'unstated'; support
    quotes the phrase of the score text behind the subject and time scope ('' when the text is silent).
    """
    name: str                      # item heading of the score text, without comparators or numbers
    levels: tuple                  # every point value the item can give
    points: Callable
    inputs: tuple
    kind: str                      # 'numeric' | 'finding' | 'mixed'
    thresholds: dict = field(default_factory=dict)
    subject: str = "patient"
    time: str = "unstated"
    support: dict = field(default_factory=dict)


@dataclass(frozen=True)
class Score:
    cid: int                       # Calculator ID of the benchmark
    name: str
    items: tuple
    conventions: tuple = ()        # absent-key conventions, each with the instance text it is taken from

    def item_points(self, ent):
        return [(it.name, it.points(ent)) for it in self.items]

    def total(self, ent):
        return sum(p for _, p in self.item_points(ent))


def flag(ent, key, absent=False):
    """A finding: True/False from the dictionary; an unmentioned finding takes `absent`."""
    v = ent.get(key, absent)
    return bool(v) if not isinstance(v, (list, tuple)) else bool(v[0])


def num(ent, key, to=None):
    """A numeric input in the score text's unit, or None if the key is absent.

    to: {unit as released (lower case): factor or function}; a released unit that is not listed raises.
    """
    if key not in ent or ent[key] is None:
        return None
    v = ent[key]
    if not isinstance(v, (list, tuple)):
        return float(v)
    val, unit = float(v[0]), str(v[1]).strip().lower()
    to = {k.lower(): f for k, f in (to or {}).items()}
    if unit not in to:
        raise KeyError(f"{key}: unit {v[1]!r} not handled")
    f = to[unit]
    return f(val) if callable(f) else val * f


def stratum(item, ent):
    """stated: an input is released with a number or True; denied: released as False; default: absent."""
    seen = [ent[k] for k in item.inputs if k in ent]
    if any(v is not False for v in seen):
        return "stated"
    return "denied" if seen else "default"


def score_text(explanation):
    """The score definition shipped in the instance: the explanation up to its summing sentence."""
    m = re.search(r"^.*\bby summing\b.*$", explanation, re.M)
    if not m:                      # 28 SOFA explanations start mid-way and ship no definition
        return None
    return "\n".join(line.rstrip() for line in explanation[:m.end()].strip().splitlines())


def rows(split, check=True):
    """Rule-based rows of one CSV ('test' | 'train') as dicts with parsed entities."""
    path = EXT / f"{split}_data.csv"
    if check:
        h = hashlib.sha256(path.read_bytes()).hexdigest()
        assert h == PIN["sha256"][path.name], f"{path.name}: sha256 {h} differs from the pin"
    out = []
    with open(path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if r["Category"] in RULE_BASED:
                r["cid"] = int(r["Calculator ID"])
                r["ent"] = ast.literal_eval(r["Relevant Entities"])
                r["answer"] = float(r["Ground Truth Answer"])
                out.append(r)
    return out


def load_scores():
    """{cid: Score} for every module in selrm/mcv/scores that defines SCORE."""
    from selrm.mcv import scores as pkg
    out = {}
    for m in pkgutil.iter_modules(pkg.__path__):
        s = getattr(importlib.import_module(f"selrm.mcv.scores.{m.name}"), "SCORE", None)
        if s is not None:
            out[s.cid] = s
    return out
