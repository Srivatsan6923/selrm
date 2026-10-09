"""API judges (owner C; ROLE.md "Judge harness", INTERFACES 3). One OpenAI-compatible client
(OpenRouter by default). Readouts, fixed per model in configs/models.json:
  choice   the frozen CHOICE prompt in both orders (A = s, B = s_prime, then swapped); the same
           claim chosen twice = decision, d = +1 (s) or -1 (s_prime); split or unparsable = 0 (a
           tie, i.e. a failure). Scores: u(s) = d / 2, u(s_prime) = -d / 2, so d = u(s) - u(s_prime).
  logprob  the frozen verdict prompt, one output token; u = logprob("+") - logprob("-") from the
           first token's top log-probabilities (a sign missing from the top list gets the lowest
           listed log-probability minus 1; both missing -> u = 0).
  pointwise (missing twins of choice models, INTERFACES 3): the verdict prompt answered in text;
           u = +1 for "+", -1 for "-", 0 if unparsable; MR = both claims rejected (u < 0).
Every response is cached on disk under a key hashed from (model, messages, params); a run's cost is
estimated before it starts and checked against configs/budget.json and the spend ledger."""
from __future__ import annotations

import concurrent.futures as cf
import hashlib
import json
import os
import re
import threading
import time

from selrm.prompts import CHOICE_SYSTEM, choice_prompt, verdict_prompt

ANSWER = re.compile(r"answer\s*[:\-]?\s*\**\s*\(?([AB])\b", re.I)
SIGN = re.compile(r"^\s*\**\s*([+\-])")


def parse_choice(text):
    """'A', 'B' or None: the last 'Answer: X' in the reply."""
    hits = ANSWER.findall(text or "")
    return hits[-1].upper() if hits else None


def parse_sign(text):
    """'+', '-' or None: a reply that starts with the sign, or ends with a line that is only the sign."""
    if not text:
        return None
    m = SIGN.match(text)
    if m:
        return m.group(1)
    last = text.strip().splitlines()[-1].strip().strip("*").strip() if text.strip() else ""
    if last in ("+", "-"):
        return last
    m = re.search(r"answer\s*[:\-]?\s*\**\s*([+\-])\s*\**\s*$", text.strip(), re.I)
    return m.group(1) if m else None


class Cache:
    def __init__(self, root):
        self.root = root

    def key(self, model, messages, params):
        blob = json.dumps({"model": model, "messages": messages, "params": params}, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(blob.encode("utf-8")).hexdigest()

    def path(self, k):
        return os.path.join(self.root, k[:2], k + ".json")

    def get(self, k):
        try:
            return json.load(open(self.path(k), encoding="utf-8"))
        except (OSError, ValueError):
            return None

    def put(self, k, value):
        p = self.path(k)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        tmp = f"{p}.{os.getpid()}.{threading.get_ident()}.tmp"
        json.dump(value, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
        os.replace(tmp, p)


class Judge:
    """cfg: one entry of configs/models.json: {name, id, readout, params, price_in, price_out, ...}.
    client: an object with .chat.completions.create(**kw) (openai.OpenAI) or None for cache-only."""

    def __init__(self, cfg, client, cache, workers=16, log=print):
        self.cfg, self.client, self.cache, self.workers, self.log = cfg, client, cache, workers, log
        self.usage = {"calls": 0, "cached": 0, "prompt_tokens": 0, "completion_tokens": 0, "cost": 0.0, "errors": 0}
        self.lock = threading.Lock()

    def call(self, messages, extra=None):
        params = dict(self.cfg.get("params", {})) | (extra or {})
        k = self.cache.key(self.cfg["id"], messages, params)
        hit = self.cache.get(k)
        if hit is not None:
            with self.lock:
                self.usage["cached"] += 1
            return hit
        if self.client is None:
            raise RuntimeError("no API client (cache-only mode) and the response is not cached")
        for attempt in range(6):
            try:
                r = self.client.chat.completions.create(model=self.cfg["id"], messages=messages, **params)
                if not r.choices:                        # a provider error returned as a body without choices: retry
                    raise RuntimeError(f"no choices: {getattr(r, 'error', None)}")
                break
            except Exception as e:                       # rate limits and provider errors: back off
                if attempt == 5:
                    with self.lock:
                        self.usage["errors"] += 1
                    return {"error": f"{type(e).__name__}: {e}"[:500]}
                time.sleep(min(60, 2 ** attempt + 0.1 * attempt))
        ch = r.choices[0]
        lp = None
        if getattr(ch, "logprobs", None) and ch.logprobs.content:
            lp = [{"token": t.token, "logprob": t.logprob,
                   "top": [{"token": x.token, "logprob": x.logprob} for x in (t.top_logprobs or [])]}
                  for t in ch.logprobs.content[:1]]
        u = getattr(r, "usage", None)
        out = {"text": ch.message.content, "finish": ch.finish_reason, "logprobs": lp,
               "reasoning": getattr(ch.message, "reasoning", None),
               "usage": {"prompt_tokens": getattr(u, "prompt_tokens", None),
                         "completion_tokens": getattr(u, "completion_tokens", None),
                         "cost": getattr(u, "cost", None)} if u else None,
               "model_returned": getattr(r, "model", None), "time": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
        self.cache.put(k, out)
        with self.lock:
            self.usage["calls"] += 1
            if out["usage"]:
                self.usage["prompt_tokens"] += out["usage"]["prompt_tokens"] or 0
                self.usage["completion_tokens"] += out["usage"]["completion_tokens"] or 0
                self.usage["cost"] += out["usage"]["cost"] or 0.0
        return out

    def map(self, fn, items):
        with cf.ThreadPoolExecutor(self.workers) as ex:
            return list(ex.map(fn, items))

    # ---------------------------------------------------------------- readouts
    def choice_messages(self, rec_s, rec_sp, s_first):
        a, b = (rec_s, rec_sp) if s_first else (rec_sp, rec_s)
        return [{"role": "system", "content": CHOICE_SYSTEM},
                {"role": "user", "content": choice_prompt(rec_s["rule_text"], rec_s["case_text"],
                                                          a["claim_text"], b["claim_text"])}]

    def verdict_messages(self, rec):
        return [{"role": "user", "content": verdict_prompt(rec)}]

    def score_pairs(self, pairs):
        """pairs: [(rec_s, rec_sp)] -> [{d, raw, parsed}] with the choice readout in both orders."""
        jobs = [(i, s_first) for i in range(len(pairs)) for s_first in (True, False)]
        outs = self.map(lambda j: self.call(self.choice_messages(*pairs[j[0]], j[1])), jobs)
        res = []
        for i in range(len(pairs)):
            o1, o2 = outs[2 * i], outs[2 * i + 1]
            c1, c2 = parse_choice(o1.get("text")), parse_choice(o2.get("text"))
            pick1 = {"A": "s", "B": "s_prime"}.get(c1)          # order 1: A = s
            pick2 = {"A": "s_prime", "B": "s"}.get(c2)          # order 2: A = s_prime
            d = (1 if pick1 == "s" else -1) if pick1 is not None and pick1 == pick2 else 0
            res.append({"d": d, "raw": [o1.get("text"), o2.get("text")], "parsed": [c1, c2],
                        "order": ["s_first", "s_prime_first"], "errors": [o1.get("error"), o2.get("error")]})
        return res

    def score_logprob(self, recs):
        """[{u, top, raw}] from the first output token of the verdict prompt."""
        extra = {"max_tokens": 1, "logprobs": True, "top_logprobs": self.cfg.get("top_logprobs", 20)}   # some providers cap it at 5
        outs = self.map(lambda r: self.call(self.verdict_messages(r), extra), recs)
        res = []
        for o in outs:
            top = {x["token"].strip(): x["logprob"] for x in ((o.get("logprobs") or [{}])[0].get("top") or [])}
            lp = {s: top.get(s) for s in ("+", "-")}
            if lp["+"] is None and lp["-"] is None:
                u = 0.0
            else:
                floor = min(top.values()) - 1.0
                u = (lp["+"] if lp["+"] is not None else floor) - (lp["-"] if lp["-"] is not None else floor)
            res.append({"u": u, "top": lp, "raw": o.get("text"), "error": o.get("error")})
        return res

    def score_pointwise(self, recs):
        outs = self.map(lambda r: self.call(self.verdict_messages(r)), recs)
        res = []
        for o in outs:
            sgn = parse_sign(o.get("text"))
            res.append({"u": {"+": 1.0, "-": -1.0}.get(sgn, 0.0), "raw": o.get("text"), "parsed": sgn,
                        "error": o.get("error")})
        return res


# ---------------------------------------------------------------- cost

def approx_tokens(text):
    """Conservative token count for cost estimates (no model tokenizer for API models): chars / 3.5."""
    return int(len(text) / 3.5) + 8


def estimate_cost(cfg, prompts, completion_tokens):
    """USD for a list of prompt texts, each answered with `completion_tokens` (incl. reasoning)."""
    pin, pout = cfg["price_in"], cfg["price_out"]          # USD per million tokens
    return sum(approx_tokens(p) for p in prompts) * pin / 1e6 + len(prompts) * completion_tokens * pout / 1e6
