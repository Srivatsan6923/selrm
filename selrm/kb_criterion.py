"""Pairwise criterion rendered from the public DDXPlus knowledge base (kb_v1; STAGE2_TASKS_A, A2).

render(A, B) gives one text for a pair of diagnoses: the findings listed for one only, for the other only and
for both (question text verbatim), then the fixed procedure of Appendix E. The text depends on the two names
only, never on a case or a label, and is identical for (A, B) and (B, A).
"""
import hashlib
import json
from functools import lru_cache
from pathlib import Path

EXT = Path(__file__).resolve().parents[1] / "data" / "_ext" / "ddxplus"
PIN = {"source": "DDXPlus, English release, figshare record 22687585 (doi 10.6084/m9.figshare.22687585.v2)",
       "licence": "CC BY 4.0",
       "sha256": {"release_conditions.json": "56edf4682d8e86a4209fc3a33932e50ce03d1cc1fecc326c26d5ef8fa5c24890",
                  "release_evidences.json": "281c78b044ae60514e28ecc9052d08a8225dd3e2db3f00f8788b99c47b05e0c0"}}
PROCEDURE = ("A finding listed for one diagnosis only excludes the other. If findings of both exclusive lists "
             "are present, or of neither, the criterion does not decide.")


@lru_cache(maxsize=None)
def kb():
    """(conditions, evidences) of the release, after a sha256 check of both files."""
    out = []
    for name in ("release_conditions.json", "release_evidences.json"):
        raw = (EXT / name).read_bytes()
        h = hashlib.sha256(raw).hexdigest()
        assert h == PIN["sha256"][name], f"{name}: sha256 {h} differs from the pin"
        out.append(json.loads(raw.decode("utf-8")))
    return tuple(out)


def findings(condition):
    """Evidence codes listed for a condition (symptoms and antecedents), in the order of the evidence file."""
    cond, ev = kb()
    listed = set(cond[condition]["symptoms"]) | set(cond[condition]["antecedents"])
    return [e for e in ev if e in listed]


def lists(a, b):
    """(a only, b only, both) as evidence codes."""
    fa, fb = findings(a), findings(b)
    return [e for e in fa if e not in fb], [e for e in fb if e not in fa], [e for e in fa if e in fb]


def render(a, b):
    """The criterion text of the unordered pair {a, b}; categorical and multi-choice findings by question only."""
    assert a != b
    ev = kb()[1]
    a, b = sorted((a, b))
    only_a, only_b, both = lists(a, b)

    def block(title, codes):
        return [title] + ([f"- {ev[e]['question_en']}" for e in codes] or ["- (none)"])

    lines = block(f"Findings listed for {a} only:", only_a) + [""]
    lines += block(f"Findings listed for {b} only:", only_b) + [""]
    lines += block(f"Findings listed for both {a} and {b}:", both) + ["", PROCEDURE]
    return "\n".join(lines)


def text_sha(a, b):
    return hashlib.sha256(render(a, b).encode("utf-8")).hexdigest()
