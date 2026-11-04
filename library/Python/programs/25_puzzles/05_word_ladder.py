"""Word ladder: shortest transformation sequences via BFS over wildcard buckets."""
from collections import defaultdict, deque
from string import ascii_lowercase

WORDS = """
cold cord card ward warm word worm wore core corn born barn bard band bend bond
cold bold bolt boat coat cost cast case cash wash wish fish dish dash lash mash
head heal teal tell tall tail toil foil fool pool poll pole sole sale tale tile
love live line lane lone lose lost list lint mint mine wine wire fire fine find
hate have hive five fire hire here hare care cave gave game came cane cone code
""".split()


def build_buckets(words):
    buckets = defaultdict(set)
    for w in words:
        for i in range(len(w)):
            buckets[w[:i] + "_" + w[i + 1:]].add(w)
    return buckets


def ladder(start, goal, words):
    buckets = build_buckets(words)
    prev = {start: None}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        if word == goal:
            path = []
            while word:
                path.append(word)
                word = prev[word]
            return path[::-1]
        for i in range(len(word)):
            for nxt in sorted(buckets[word[:i] + "_" + word[i + 1:]]):
                if nxt not in prev:
                    prev[nxt] = word
                    queue.append(nxt)
    return None


def neighbors_by_letter(word, vocab):
    return sorted(word[:i] + ch + word[i + 1:] for i in range(len(word)) for ch in ascii_lowercase
                  if ch != word[i] and word[:i] + ch + word[i + 1:] in vocab)


vocab = set(WORDS)
print(f"Dictionary: {len(vocab)} four-letter words")
for start, goal in [("cold", "warm"), ("head", "tail"), ("love", "hate"), ("fish", "bird"), ("fool", "sage")]:
    path = ladder(start, goal, vocab)
    if path:
        print(f"{start} -> {goal}: {' > '.join(path)} ({len(path) - 1} steps)")
    else:
        print(f"{start} -> {goal}: no ladder")

print("Neighbors of 'fire':", neighbors_by_letter("fire", vocab))
buckets = build_buckets(vocab)
busiest = max(buckets.items(), key=lambda kv: (len(kv[1]), kv[0]))
print("Busiest pattern:", busiest[0], sorted(busiest[1]))
