"""Point-free text analytics: a word-frequency and n-gram pipeline built from small pure functions."""
import re
from collections import Counter
from functools import reduce, partial
from itertools import islice
from operator import itemgetter

TEXT = """
It was the best of times, it was the worst of times, it was the age of wisdom,
it was the age of foolishness, it was the epoch of belief, it was the epoch of
incredulity, it was the season of Light, it was the season of Darkness.
"""

STOP = frozenset({"it", "was", "the", "of"})


def pipeline(*steps):
    return lambda data: reduce(lambda acc, step: step(acc), steps, data)


def top(n):
    return lambda counter: counter.most_common(n)


def ngrams(n):
    return lambda words: zip(*(islice(words, i, None) for i in range(n)))


def first(n):
    return lambda seq: seq[:n]


tokenize = partial(re.findall, r"[a-z']+")
drop_stop = partial(filter, lambda w: w not in STOP)
count_by_initial = partial(
    reduce, lambda acc, w: {**acc, w[0]: acc.get(w[0], 0) + 1}
)

word_freq = pipeline(str.lower, tokenize, drop_stop, Counter, top(5))
print("Top content words:", word_freq(TEXT))

all_words = pipeline(str.lower, tokenize)(TEXT)
print("Total words:", len(all_words), "| distinct:", len(set(all_words)))

bigrams = pipeline(ngrams(2), partial(map, " ".join), Counter, top(3))
print("Top bigrams:", bigrams(all_words))

trigram_count = pipeline(ngrams(3), Counter, len)
print("Distinct trigrams:", trigram_count(all_words))

lengths = pipeline(partial(map, len), Counter, dict.items, sorted)
print("Word length histogram:", lengths(all_words))

longest = pipeline(set, partial(sorted, key=lambda w: (-len(w), w)), first(3))
print("Longest words:", longest(all_words))

capitalized = pipeline(partial(re.findall, r"\b[A-Z][a-z]+"), set, sorted)
print("Capitalized in source:", capitalized(TEXT))

by_first_letter = pipeline(
    drop_stop,
    lambda words: count_by_initial(words, {}),
    dict.items,
    partial(sorted, key=itemgetter(1), reverse=True),
    first(5),
)
print("Content words by first letter:", by_first_letter(all_words))
