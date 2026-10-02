import json
import subprocess
import sys
from pathlib import Path

from selrm import engine

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_shortcuts.py"


def _run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), "--boot", "50", *args],
                          capture_output=True, text=True)


def test_checkpoint_passes_on_generated_triplets():
    r = _run("--per-cell", "2")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "CHECKPOINT PASSED" in r.stdout and "[FAIL]" not in r.stdout


def _write(path, ts):
    path.write_text("".join(json.dumps(t) + "\n" for t in ts), encoding="utf-8")
    return str(path)


def test_checkpoint_reads_a_set_and_fails_on_a_corrupt_one(tmp_path):
    ts = [engine.make_triplet(*cell, "test", 0) for cell in engine.cells()]
    r = _run("--set", _write(tmp_path / "ok.jsonl", ts))
    assert r.returncode == 0, r.stdout + r.stderr
    ts[0]["cases"]["near"]["state"] = ts[0]["cases"]["flip"]["state"]
    r = _run("--set", _write(tmp_path / "bad.jsonl", ts))
    assert r.returncode == 1 and "[FAIL] no invariant violations" in r.stdout
