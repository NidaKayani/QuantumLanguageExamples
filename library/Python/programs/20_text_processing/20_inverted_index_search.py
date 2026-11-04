"""An inverted index with TF-IDF ranking, boolean AND/OR queries, and phrase search."""
import math
import re
from collections import Counter, defaultdict

DOCUMENTS = {
    "d1": "The compiler parses source code and builds an abstract syntax tree.",
    "d2": "An interpreter executes source code directly without a separate compile step.",
    "d3": "Type checking happens after parsing; the type checker walks the syntax tree.",
    "d4": "Register allocation assigns variables to machine registers during code generation.",
    "d5": "The parser reports syntax errors with line and column information.",
    "d6": "Code generation emits machine code from the optimised intermediate representation.",
}

STOP = {"the", "an", "a", "and", "with", "to", "from", "during", "after", "without"}


def tokenize(text):
    return [w for w in re.findall(r"[a-z]+", text.lower()) if w not in STOP]


class SearchIndex:
    def __init__(self, docs):
        self.docs = docs
        self.postings = defaultdict(dict)  # term -> {doc: [positions]}
        self.lengths = {}
        for doc_id, text in docs.items():
            terms = tokenize(text)
            self.lengths[doc_id] = len(terms)
            for pos, term in enumerate(terms):
                self.postings[term].setdefault(doc_id, []).append(pos)

    def idf(self, term):
        df = len(self.postings.get(term, {}))
        return math.log((1 + len(self.docs)) / (1 + df)) + 1

    def rank(self, query):
        scores = Counter()
        for term in tokenize(query):
            for doc_id, positions in self.postings.get(term, {}).items():
                tf = len(positions) / self.lengths[doc_id]
                scores[doc_id] += tf * self.idf(term)
        return sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))

    def boolean(self, query):
        result = None
        for clause in query.split(" AND "):
            docs = set().union(*(self.postings.get(t, {}).keys()
                                 for t in tokenize(clause.replace(" OR ", " "))))
            result = docs if result is None else result & docs
        return sorted(result or [])

    def phrase(self, phrase):
        terms = tokenize(phrase)
        hits = []
        for doc_id in self.postings.get(terms[0], {}):
            starts = self.postings[terms[0]][doc_id]
            if any(all(p + k in self.postings.get(t, {}).get(doc_id, ()) for k, t in enumerate(terms))
                   for p in starts):
                hits.append(doc_id)
        return sorted(hits)


def main():
    index = SearchIndex(DOCUMENTS)
    print(f"Indexed {len(DOCUMENTS)} documents, {len(index.postings)} terms")
    common = sorted(index.postings, key=lambda t: (-len(index.postings[t]), t))[:5]
    print("Most widespread terms:", [(t, len(index.postings[t])) for t in common])
    for query in ("syntax tree", "machine code generation", "interpreter"):
        print(f"Ranked {query!r}:")
        for doc_id, score in index.rank(query)[:3]:
            print(f"  {doc_id} {score:.4f}  {DOCUMENTS[doc_id][:55]}")
    print("Boolean 'code AND syntax':", index.boolean("code AND syntax"))
    print("Boolean 'parser OR interpreter':", index.boolean("parser OR interpreter"))
    print("Phrase 'source code':", index.phrase("source code"))
    print("Phrase 'code source':", index.phrase("code source"))


if __name__ == "__main__":
    main()
