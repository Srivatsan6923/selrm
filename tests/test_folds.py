"""Signature classes and folds (A-D3)."""
from selrm import folds as FD
from selrm.library import LIBRARY, LIBRARY_BY_ID


def test_folds_partition_rules_and_hold_out_whole_classes():
    F = FD.make_folds(LIBRARY)
    assert F == FD.make_folds(LIBRARY)                       # deterministic
    held = [c for f in F["folds"].values() for c in f["l2_classes"]]
    assert len(held) == len(set(held))                       # each class held out at most once
    for f in F["folds"].values():
        parts = [set(f[k]) for k in ("l2_rules", "l1_rules", "train_rules")]
        assert set.union(*parts) == {r.rid for r in LIBRARY} and sum(map(len, parts)) == len(LIBRARY)
        assert len(f["l2_classes"]) >= 4
        assert {FD.sig_class(LIBRARY_BY_ID[x]) for x in f["l2_rules"]} == set(f["l2_classes"])
        train_cls = {FD.sig_class(LIBRARY_BY_ID[x]) for x in f["train_rules"]}
        assert not train_cls & set(f["l2_classes"])
        assert {FD.sig_class(LIBRARY_BY_ID[x]) for x in f["l1_rules"]} <= train_cls
        assert {c.split("|")[0] for c in train_cls} == set(FD.OPERATORS)


def test_signature_fields():
    s = FD.signature(LIBRARY_BY_ID["strep_amox"])
    assert s["operator"] == "single" and s["inputs"] == ["finding"] and s["applicability"] == ["current"]
    assert FD.sig_class(LIBRARY_BY_ID["curb65"]).startswith("score|")
