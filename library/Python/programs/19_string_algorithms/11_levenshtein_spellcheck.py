"""Levenshtein and Damerau distances powering a tiny spelling corrector."""
from heapq import nsmallest

VOCAB = """the quick brown fox jumps over lazy dog python program language compiler
interpreter function variable recursion algorithm string search sorting
receive believe separate definitely necessary occurrence accommodate
government environment beginning restaurant tomorrow""".split()


def levenshtein(a, b):
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(previous[j] + 1, current[j - 1] + 1,
                               previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]


def damerau(a, b):
    d = {(i, -1): i + 1 for i in range(-1, len(a))}
    d.update({(-1, j): j + 1 for j in range(-1, len(b))})
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            cost = ca != cb
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + cost)
            if i and j and ca == b[j - 1] and a[i - 1] == cb:
                d[i, j] = min(d[i, j], d[i - 2, j - 2] + 1)
    return d[len(a) - 1, len(b) - 1]


def suggest(word, vocab=VOCAB, k=3, metric=damerau):
    return nsmallest(k, vocab, key=lambda w: (metric(word, w), w))


def main():
    pairs = [("kitten", "sitting"), ("flaw", "lawn"), ("ca", "abc"),
             ("teh", "the"), ("recieve", "receive"), ("", "abc")]
    print(f"{'a':<10}{'b':<10}{'lev':>4}{'dam':>4}")
    for a, b in pairs:
        print(f"{a:<10}{b:<10}{levenshtein(a, b):>4}{damerau(a, b):>4}")
    typos = ["teh", "pyhton", "recieve", "seperate", "definately", "algoritm",
             "goverment", "tommorow", "complier", "funtcion"]
    print("Spelling suggestions:")
    for typo in typos:
        best = suggest(typo)
        dist = damerau(typo, best[0])
        print(f"  {typo:<11} -> {best[0]:<12} (distance {dist}) alternatives {best[1:]}")


if __name__ == "__main__":
    main()
