"""Word ladder: BFS over an implicit graph using wildcard buckets."""
from collections import defaultdict, deque
from string import ascii_lowercase

WORDS = """cold cord card ward warm worm word wood good gold bold bolt boat coat
cost cast case cave gave game came cane cone code mode made fade face fate
hate have hive five fire hire here herd hard harm""".split()


def build_buckets(words):
    buckets = defaultdict(list)
    for w in words:
        for i in range(len(w)):
            buckets[w[:i] + "_" + w[i + 1:]].append(w)
    return buckets


def ladder(start, goal, words):
    buckets = build_buckets(words)
    prev = {start: None}
    queue = deque([start])
    while queue:
        word = queue.popleft()
        if word == goal:
            break
        for i in range(len(word)):
            for nxt in buckets[word[:i] + "_" + word[i + 1:]]:
                if nxt not in prev:
                    prev[nxt] = word
                    queue.append(nxt)
    if goal not in prev:
        return None
    chain = []
    while goal:
        chain.append(goal)
        goal = prev[goal]
    return chain[::-1]


def one_letter_neighbors(word, vocab):
    return sorted({word[:i] + ch + word[i + 1:]
                   for i in range(len(word)) for ch in ascii_lowercase
                   if ch != word[i]} & vocab)


def main():
    vocab = set(WORDS)
    print(f"Vocabulary size: {len(vocab)}")
    for a, b in [("cold", "warm"), ("cold", "fire"), ("boat", "game"), ("gold", "harm")]:
        chain = ladder(a, b, WORDS)
        if chain:
            print(f"{a} -> {b}: {' > '.join(chain)} ({len(chain) - 1} steps)")
        else:
            print(f"{a} -> {b}: no ladder")
    print("Neighbors of 'cave':", one_letter_neighbors("cave", vocab))
    buckets = build_buckets(WORDS)
    busiest = max(buckets.items(), key=lambda kv: (len(kv[1]), kv[0]))
    print(f"Busiest pattern {busiest[0]!r}: {sorted(busiest[1])}")


if __name__ == "__main__":
    main()
