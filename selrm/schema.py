"""Canonical instance record (INTERFACES.md, section 1). One JSON object per
(case, claim). Everything downstream (training, scoring, tables) reads this."""
REQUIRED = {
    "iid": str,         # "<tid>/<case_kind>/<claim_type>/<claim_role>"
    "tid": str,         # triplet id; groups base/flip/near/pres(/missing)
    "set": str,         # dataset version name, e.g. "rule_v1"
    "split": str,       # train | dev | test | smoke
    "tier": str,        # easy | long | superseded | delabelled | alt | rewritten
    "level": str,       # L0 | L1 | L2 | L3-inv | L3-alt | smoke
    "rid": str, "cid": str, "family": str,
    "nm_kind": str,     # numeric | boundary | subject | negation | time
    "case_kind": str,   # base | flip | near | pres | missing | read | apply
    "rule_text": str, "case_text": str,
    "condition": str,   # the condition under test, shown to the reader
    "claim_type": str,  # conclusion | criterion | applicability
    "claim_role": str,  # s | s_prime
    "claim_text": str,
    "label": int,       # 1 if the claim is correct for this case, else 0
    "state": list,      # mentions as dicts (program input)
    "ledger": list,     # program-generated entries: need/found/subject/status/time
    "prose": str,       # the same evidence as plain sentences (matched baseline)
    "meta": dict,       # template ids, seed, anything else
}
CASE_KINDS = {"base", "flip", "near", "pres", "missing", "read", "apply"}
CLAIM_TYPES = {"conclusion", "criterion", "applicability"}
LEDGER_KEYS = ("need", "found", "subject", "status", "time")


def validate(rec: dict) -> None:
    for k, t in REQUIRED.items():
        if k not in rec:
            raise ValueError(f"missing key {k} in {rec.get('iid')}")
        if not isinstance(rec[k], t):
            raise ValueError(f"{k} must be {t.__name__} in {rec.get('iid')}")
    if rec["case_kind"] not in CASE_KINDS:
        raise ValueError(f"bad case_kind {rec['case_kind']}")
    if rec["claim_type"] not in CLAIM_TYPES:
        raise ValueError(f"bad claim_type {rec['claim_type']}")
    if rec["claim_role"] not in ("s", "s_prime") or rec["label"] not in (0, 1):
        raise ValueError(f"bad claim_role/label in {rec['iid']}")
    for e in rec["ledger"]:
        if tuple(e.keys()) != LEDGER_KEYS:
            raise ValueError(f"bad ledger entry in {rec['iid']}: {e}")
