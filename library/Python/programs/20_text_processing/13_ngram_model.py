"""Character and word n-grams, a deterministic bigram text generator, and n-gram similarity."""
import re
from collections import Counter, defaultdict
from itertools import islice

CORPUS = """the quick brown fox jumps over the lazy dog . the lazy dog sleeps in the sun .
the quick cat chases the brown mouse . the mouse runs over the hill . a dog sees the cat .
the sun shines over the hill and the fox sleeps ."""


def ngrams(seq, n):
    return zip(*(islice(seq, i, None) for i in range(n)))


def build_bigram_model(words):
    model = defaultdict(Counter)
    for a, b in ngrams(words, 2):
        model[a][b] += 1
    return model


def generate(model, start, length=12):
    out, word = [start], start
    for _ in range(length - 1):
        if word not in model:
            break
        followers = model[word]
        best = max(followers.items(), key=lambda kv: (kv[1], kv[0]))
        followers[best[0]] -= 1
        if followers[best[0]] == 0:
            del followers[best[0]]
        word = best[0]
        out.append(word)
    return " ".join(out)


def char_ngram_profile(text, n=3):
    clean = re.sub(r"[^a-z ]", "", text.lower())
    return Counter("".join(g) for g in ngrams(f" {clean} ", n))


def jaccard(a, b):
    sa, sb = set(a), set(b)
    return len(sa & sb) / len(sa | sb) if sa | sb else 1.0


def main():
    words = CORPUS.split()
    model = build_bigram_model(words)
    print("Followers of 'the':", dict(sorted(model["the"].items(), key=lambda kv: (-kv[1], kv[0]))))
    trigrams = Counter(ngrams(words, 3))
    print("Top trigrams:", [" ".join(t) for t, _ in sorted(trigrams.items(), key=lambda kv: (-kv[1], kv[0]))[:3]])
    print("Generated:", generate(build_bigram_model(words), "the", 14))
    print("Generated:", generate(build_bigram_model(words), "a", 10))
    names = ["colour", "color", "colorful", "collar", "cooler"]
    base = char_ngram_profile(names[0])
    print("Character trigrams of 'colour':", sorted(base))
    for other in names[1:]:
        print(f"  jaccard(colour, {other}) = {jaccard(base, char_ngram_profile(other)):.3f}")
    print("Bigrams of 'banana':", ["".join(g) for g in ngrams("banana", 2)])


if __name__ == "__main__":
    main()
