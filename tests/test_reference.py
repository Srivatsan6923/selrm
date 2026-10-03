"""Check code and reference graphs (A-D13) agree with the labels."""
import contextlib
import io

from selrm import engine as E
from selrm.reference import reference_graph, render_check_code


def _run(code):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(code, {})
    return buf.getvalue().strip()


def test_check_code_reproduces_labels_and_graph_marks_the_decisive_criterion():
    for cell in E.cells()[::3]:
        for r in E.make_group(*cell, "test", 0, "t", "L0", missing=True):
            assert _run(render_check_code(r)) == ("+" if r["label"] else "-"), r["iid"]
            g = reference_graph(r)
            (dec,) = [n for n in g["nodes"] if n.get("decisive")]
            assert dec["id"] == f"c:{r['cid']}"
            if r["case_kind"] == "missing":
                assert dec["holds"] is None
            elif r["case_kind"] in ("base", "flip", "near", "pres") and r["claim_type"] == "criterion":
                assert dec["holds"] == ((r["claim_role"] == "s_prime") == bool(r["label"]))
