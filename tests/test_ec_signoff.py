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
    """Three rendered criteria, a temporary registry and an empty sign-off folder."""
    items = B.load_items()
    keep, recs, _ = B.render(items)
    ids = [f["cand"] for f in keep[:3]]
    monkeypatch.setattr(B, "load_items", lambda: [f for f in items if f["cand"] in ids])
    monkeypatch.setattr(B, "ROOT", tmp_path)
    monkeypatch.setattr(B, "REVIEWS", tmp_path / "ec_signoff")
    (tmp_path / "data").mkdir()
    (tmp_path / "data" / "REGISTRY.json").write_text("{}", encoding="utf-8")
    (tmp_path / "ec_signoff").mkdir()
    fps = {f["cand"]: B.fingerprint(f, [r for r in recs if r["rid"] == f"ec_{f['cand']}"]) for f in keep[:3]}
    return ids, fps


def _review(tmp_path, who, rows):
    with open(tmp_path / "ec_signoff" / f"{who}.csv", "w", encoding="utf-8-sig", newline="") as f:   # Excel BOM
        w = csv.DictWriter(f, fieldnames=B.REVIEW_COLS)
        w.writeheader()
        w.writerows(rows)


def _row(c, fp, p="yes", k="yes", comment=""):
    return {"crit_id": c, "fingerprint": fp, "program_ok": p, "cases_ok": k, "comment": comment}


def test_freeze_merges_two_reviewers(kit, tmp_path):
    ids, fps = kit
    _review(tmp_path, "author1", [_row(c, fps[c]) for c in ids])
    with pytest.raises(SystemExit, match="exactly two"):
        B.freeze()
    _review(tmp_path, "author2", [_row(ids[0], fps[ids[0]], "no", "", "threshold differs from the trial"),
                                  _row(ids[1], fps[ids[1]]), _row(ids[2], fps[ids[2]])])
    B.freeze()
    man = json.loads((tmp_path / "data" / "ec_v1" / "test" / "MANIFEST.json").read_text(encoding="utf-8"))
    assert man["signed_off"] == sorted(ids[1:]) and man["rejected_at_signoff"] == [ids[0]]
    assert man["reviewers"][ids[1]] == ["author1", "author2"]


@pytest.mark.parametrize("change, message", [
    (lambda rows: rows[0].update(fingerprint="0" * 16), "another version"),      # signed an older rendering
    (lambda rows: rows.append(dict(rows[0])), "appears 2 times"),                # a duplicated row
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


def test_nothing_approved_and_named_files(kit, tmp_path):
    ids, fps = kit
    for who in ("author1", "author2"):
        _review(tmp_path, who, [_row(c, fps[c], "no", "", "vague") for c in ids])
    with pytest.raises(SystemExit, match="nothing to freeze"):
        B.freeze()
    _review(tmp_path, "alice", [])
    with pytest.raises(SystemExit, match="rename"):
        B.freeze()
    with pytest.raises(SystemExit, match="refusing to prepare"):          # sign-off in progress
        B.prepare()
