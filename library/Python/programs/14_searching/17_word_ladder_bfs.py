"""Word ladder: BFS over an implicit graph using wildcard pattern buckets."""

from collections import defaultdict, deque
from string import ascii_lowercase

WORDS = """cold cord card ward warm word wore core bore bare bard care cure pure
sure fold gold good goad load lord lard hold hole pole poll pool cool coal""".split()


def build_buckets(words):
    buckets = defaultdict(list)
    for w in words:
        for i in range(len(w)):
            buckets[w[:i] + "_" + w[i + 1:]].append(w)
    return buckets


BUCKETS = build_buckets(WORDS)


def ladder(start, goal):
    parent = {start: None}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        if word == goal:
            path = []
            while word:
                path.append(word)
                word = parent[word]
            return path[::-1]
        for i in range(len(word)):
            for nxt in BUCKETS[word[:i] + "_" + word[i + 1:]]:
                if nxt not in parent:
                    parent[nxt] = word
                    queue.append(nxt)
    return None


def neighbours_bruteforce(word, vocab):
    return sorted(word[:i] + ch + word[i + 1:] for i in range(len(word)) for ch in ascii_lowercase
                  if ch != word[i] and word[:i] + ch + word[i + 1:] in vocab)


for start, goal in [("cold", "warm"), ("pure", "bard"), ("gold", "pool"), ("cold", "hole"), ("cool", "sure")]:
    path = ladder(start, goal)
    if path:
        print(f"{start} -> {goal}: {' > '.join(path)} ({len(path) - 1} steps)")
    else:
        print(f"{start} -> {goal}: no ladder")

vocab = set(WORDS)
print("neighbours of 'core':", neighbours_bruteforce("core", vocab))
largest = max(BUCKETS.items(), key=lambda kv: (len(kv[1]), kv[0]))
print("largest bucket:", largest[0], sorted(largest[1]))
