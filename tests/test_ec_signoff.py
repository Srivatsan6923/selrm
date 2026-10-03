import csv
import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("bec", Path(__file__).parents[1] / "scripts" / "build_ec_v1.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)


@pytest.fixture
def kit(tmp_path, monkeypatch):
    """Three rendered criteria, their sheet, a temporary registry and an empty sign-off folder."""
    items = B.load_items()
    keep, recs, _ = B.render(items)
    ids = [f["cand"] for f in keep[:3]]
    monkeypatch.setattr(B, "load_items", lambda: [f for f in items if f["cand"] in ids])
    monkeypatch.setattr(B, "ROOT", tmp_path)
    monkeypatch.setattr(B, "REVIEWS", tmp_path / "ec_signoff")
    monkeypatch.setattr(B, "SHEET", tmp_path / "EC_SIGNOFF.csv")
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "REGISTRY.json").write_text("{}", encoding="utf-8")
    (tmp_path / "ec_signoff").mkdir()
    fps = {f["cand"]: B.fingerprint(f, [r for r in recs if r["rid"] == f"ec_{f['cand']}"]) for f in keep[:3]}
    _csv(tmp_path / "EC_SIGNOFF.csv", [{"crit_id": c, "fingerprint": fp} for c, fp in fps.items()])
    return ids, fps


def _csv(path, rows, fields=None, delimiter=","):
    with open(path, "w", encoding="utf-8-sig", newline="") as f:          # Excel's 'CSV UTF-8' adds a BOM
        w = csv.DictWriter(f, fieldnames=fields or list(rows[0]), delimiter=delimiter)
        w.writeheader()
        w.writerows(rows)


def _review(tmp_path, who, rows, **kw):
    _csv(tmp_path / "ec_signoff" / f"{who}.csv", rows, B.REVIEW_COLS, **kw)


def _row(c, fp, p="yes", k="yes", comment=""):
    return {"crit_id": c, "fingerprint": fp, "program_ok": p, "cases_ok": k, "comment": comment}


def test_freeze_merges_reviews_and_restores(kit, tmp_path):
    ids, fps = kit
    _review(tmp_path, "author1", [_row(c, fps[c]) for c in ids] + [_row("", "", "", "")] * 2)   # blank rows
    with pytest.raises(SystemExit, match="at least two"):
        B.freeze()
    _review(tmp_path, "author2", [_row(ids[0], fps[ids[0]], "no", "", "threshold differs from the trial"),
                                  _row(ids[1], fps[ids[1]]), _row(ids[2], fps[ids[2]])])
    _review(tmp_path, "author3", [_row(ids[1], fps[ids[1]], "yes", "no", "a case is ambiguous"),
                                  _row(ids[2], "", "", "", "left to author1 and author2")])   # a comment is no review
    B.freeze()
    d = tmp_path / "data" / "ec_v1" / "test"
    man = json.loads((d / "MANIFEST.json").read_text(encoding="utf-8"))
    assert man["signed_off"] == [ids[2]] and man["rejected_at_signoff"] == sorted(ids[:2])   # any no rejects
    assert man["reviewers"][ids[1]] == ["author1", "author2", "author3"]
    records = (d / "records.jsonl").read_text(encoding="utf-8")
    (d / "records.jsonl").unlink()
    B.restore()
    assert (d / "records.jsonl").read_text(encoding="utf-8") == records


@pytest.mark.parametrize("change, message", [
    (lambda rows: rows[0].update(fingerprint="0" * 16), "earlier version"),       # signed an older rendering
    (lambda rows: rows[0].update(fingerprint=""), "fingerprint missing"),
    (lambda rows: rows.append(dict(rows[0])), "appears 2 times"),                 # a duplicated row
    (lambda rows: rows[0].update(program_ok="no"), "needs a comment"),
    (lambda rows: rows[0].update(cases_ok="maybe"), "yes or no")])
def test_freeze_refuses_incomplete_sign_off(kit, tmp_path, change, message):
    ids, fps = kit
    _review(tmp_path, "author1", [_row(c, fps[c]) for c in ids])
    rows = [_row(c, fps[c]) for c in ids]
    change(rows)
    _review(tmp_path, "author2", rows)
    with pytest.raises(SystemExit, match=message):
        B.freeze()


def test_stale_sheet_template_and_file_problems(kit, tmp_path):
    ids, fps = kit
    for who in ("author1", "author2"):
        _review(tmp_path, who, [_row(c, fps[c], "no", "", "vague") for c in ids])
    with pytest.raises(SystemExit, match="nothing to freeze"):
        B.freeze()
    _csv(tmp_path / "ec_signoff" / "TEMPLATE.csv", [_row(ids[0], fps[ids[0]])])
    with pytest.raises(SystemExit, match="TEMPLATE.csv holds decisions"):
        B.freeze()
    (tmp_path / "ec_signoff" / "TEMPLATE.csv").unlink()
    _review(tmp_path, "author2", [_row(c, fps[c]) for c in ids], delimiter=";")
    with pytest.raises(SystemExit, match="separated by ';'"):
        B.freeze()
    _review(tmp_path, "alice", [_row(ids[0], fps[ids[0]])])
    with pytest.raises(SystemExit, match="rename"):
        B.freeze()
    _csv(tmp_path / "EC_SIGNOFF.csv", [{"crit_id": c, "fingerprint": "x"} for c in ids])
    with pytest.raises(SystemExit, match="does not match the cases rendered now"):
        B.freeze()
    with pytest.raises(SystemExit, match="refusing to prepare"):          # sign-off in progress
        B.prepare()
