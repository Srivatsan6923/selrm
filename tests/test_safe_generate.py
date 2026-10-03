"""SafeGenerate (scripts/eval_c.py): an out-of-memory generate() is split in halves and the outputs keep the
layout callers slice (prompt columns, then generated tokens right-padded after each row's end).
  python tests/test_safe_generate.py"""
import os, sys

import torch

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))
from eval_c import SafeGenerate

PAD, EOS = 0, 9


class Fake:
    """Generates row r's tokens r+1 times then EOS (stops early per row, padded like HF); OOM above 2 rows."""
    calls = []

    def generate(self, input_ids, attention_mask, **kw):
        n = len(input_ids)
        Fake.calls.append(n)
        if n > 2:
            raise torch.OutOfMemoryError("fake")
        rows = [[int(input_ids[j, -1])] * (int(input_ids[j, -1]) + 1) + [EOS] for j in range(n)]
        w = max(len(r) for r in rows)
        gen = torch.tensor([r + [PAD] * (w - len(r)) for r in rows])
        return torch.cat([input_ids, gen], dim=1)


ids = torch.tensor([[PAD, 1], [PAD, 2], [3, 3], [PAD, 4], [PAD, 1]])
att = (ids != PAD).long()
out = SafeGenerate(Fake(), PAD, log=lambda *_: None).generate(ids, att, max_new_tokens=8)
gen = out[:, ids.shape[1]:].tolist()
for j, row in enumerate(gen):
    v = int(ids[j, -1])
    cut = row.index(EOS)
    assert row[:cut] == [v] * (v + 1) and all(t == PAD for t in row[cut + 1:]), (j, row)
assert out.shape[1] == ids.shape[1] + max(int(x) for x in ids[:, -1]) + 2
assert Fake.calls == [5, 2, 3, 1, 2], Fake.calls      # 5 fails, 2 fits, 3 fails -> 1 + 2
print("ok")
