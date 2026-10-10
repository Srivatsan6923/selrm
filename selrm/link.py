"""Linker of the gate (STAGE2_SPEC section 7): a mention -> at most k terms of the onto_v1 snapshot, by exact
match, then normalised match, then nearest names. The reader then chooses one candidate or abstains; identifiers
are never generated freely (choose() only accepts an id among the candidates).
terms: iterable of {"id", "label", "synonyms": [...]}. embed: callable list[str] -> list of unit vectors (the
encoder; chosen and verified against its licence when onto_v1 is registered).
ponytail: without `embed` the third stage is difflib string similarity; top-10 recall on cls_v1/dev decides
whether the encoder is needed."""
import difflib, re


def norm(s):
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())


class Linker:
    def __init__(self, terms, embed=None):
        self.exact, self.normed, self.label = {}, {}, {}
        for t in terms:
            self.label[t["id"]] = t["label"]
            for name in [t["label"], *t.get("synonyms", [])]:
                self.exact.setdefault(name, []).append(t["id"])
                self.normed.setdefault(norm(name), []).append(t["id"])
        self.names = sorted(self.normed)
        self.embed = embed
        self.vecs = embed(self.names) if embed else None

    def candidates(self, mention, k=10):
        """[(id, label, stage)], best first, ids distinct."""
        out, q = {}, norm(mention)
        for i in self.exact.get(mention, []):
            out.setdefault(i, "exact")
        for i in self.normed.get(q, []):
            out.setdefault(i, "normalised")
        if len(out) < k and self.names:
            if self.embed:
                v = self.embed([q])[0]
                order = sorted(range(len(self.names)), key=lambda j: -sum(a * b for a, b in zip(v, self.vecs[j])))
                near = [self.names[j] for j in order[:4 * k]]
            else:
                near = difflib.get_close_matches(q, self.names, n=4 * k, cutoff=0.5)
            for name in near:
                for i in self.normed[name]:
                    out.setdefault(i, "nearest")
        return [(i, self.label[i], s) for i, s in list(out.items())[:k]]

    def in_text(self, text, k=10):
        """Terms named inside a quotation: every word n-gram (longest first) looked up by normalised name, then
        candidates(text) to fill up to k."""
        out, words = {}, norm(text).split()
        for n in range(min(len(words), 12), 0, -1):
            for i in range(len(words) - n + 1):
                for t in self.normed.get(" ".join(words[i:i + n]), []):
                    out.setdefault(t, "normalised")
        res = [(i, self.label[i], s) for i, s in out.items()][:k]
        return res + [c for c in self.candidates(text, k) if c[0] not in out][:k - len(res)]


def load_onto(path, embed=None):
    """Role A's data/onto_v1/classes.json -> {"closure": {class id: set of member ids}, "classes": {lower-case class
    name: id, None when two classes share a name}, "linker": Linker over every member, sibling and general term}."""
    import json
    closure, classes, names = {}, {}, {}
    for fams in json.load(open(path, encoding="utf-8")).values():
        for f in fams:
            if f.get("general"):
                names.setdefault(f["general"]["id"], []).append(f["general"]["name"])
            for c in f["classes"]:
                closure[c["id"]] = {m["id"] for m in c["members"]}
                key = c["name"].lower()
                classes[key] = c["id"] if classes.get(key, c["id"]) == c["id"] else None
                for m in c["members"] + c.get("siblings", []):
                    names.setdefault(m["id"], []).extend(n for n in m["names"] if n not in names.get(m["id"], []))
    terms = [{"id": i, "label": n[0], "synonyms": n[1:]} for i, n in names.items()]
    return {"closure": closure, "classes": classes, "linker": Linker(terms, embed)}


def choose(candidates, answer):
    """The reader's choice: an id among the candidates, else None (abstain)."""
    return answer if answer in {c[0] for c in candidates} else None
