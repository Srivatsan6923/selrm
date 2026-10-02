"""Check code for the GenPRM-style verifier (B-TR-genprm): role A's render_check_code (A-D13) for
every record of a set, without its "# Rule:" / "# Claim:" header (the prompt states both). A's and
B's packages are both named selrm, so this runs in a process of its own with A's frozen code on
PYTHONPATH and imports nothing from B:
  PYTHONPATH=<A code dir> python scripts/render_checks.py RECORDS.jsonl OUT.jsonl"""
import json, os, sys

from selrm.reference import render_check_code


def body(code):
    head, sep, rest = code.partition("\n\n")
    assert head.startswith("# Rule: ") and "\n# Claim: " in head and sep, code[:200]
    return rest


def main():
    src, out = sys.argv[1], sys.argv[2]
    n = 0
    with open(out + ".tmp", "w", encoding="utf-8", newline="\n") as f:
        for line in open(src, encoding="utf-8"):
            r = json.loads(line)
            f.write(json.dumps({"iid": r["iid"], "code": body(render_check_code(r))}) + "\n")
            n += 1
    os.replace(out + ".tmp", out)
    print(f"{n} check codes -> {out}")


if __name__ == "__main__":
    main()
