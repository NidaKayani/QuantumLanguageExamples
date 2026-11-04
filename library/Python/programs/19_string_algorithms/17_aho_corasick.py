"""Aho-Corasick automaton for simultaneous multi-keyword search, used as a profanity-style filter."""
from collections import deque


class AhoCorasick:
    def __init__(self, keywords):
        self.goto = [{}]
        self.fail = [0]
        self.output = [[]]
        for word in keywords:
            self._add(word)
        self._build()

    def _add(self, word):
        state = 0
        for ch in word:
            if ch not in self.goto[state]:
                self.goto.append({})
                self.fail.append(0)
                self.output.append([])
                self.goto[state][ch] = len(self.goto) - 1
            state = self.goto[state][ch]
        self.output[state].append(word)

    def _build(self):
        queue = deque(self.goto[0].values())
        while queue:
            state = queue.popleft()
            for ch, nxt in self.goto[state].items():
                queue.append(nxt)
                f = self.fail[state]
                while f and ch not in self.goto[f]:
                    f = self.fail[f]
                self.fail[nxt] = self.goto[f].get(ch, 0)
                self.output[nxt] = self.output[nxt] + self.output[self.fail[nxt]]

    def search(self, text):
        state = 0
        for i, ch in enumerate(text):
            while state and ch not in self.goto[state]:
                state = self.fail[state]
            state = self.goto[state].get(ch, 0)
            for word in self.output[state]:
                yield i - len(word) + 1, word


def censor(text, automaton):
    mask = [False] * len(text)
    for start, word in automaton.search(text.lower()):
        for k in range(start, start + len(word)):
            mask[k] = True
    return "".join("*" if m else ch for ch, m in zip(text, mask))


def main():
    ac = AhoCorasick(["he", "she", "his", "hers"])
    print("States:", len(ac.goto))
    print("Matches in 'ushers':", list(ac.search("ushers")))
    print("Matches in 'ahishers':", list(ac.search("ahishers")))
    genes = AhoCorasick(["ACG", "CGT", "GTA", "TAC", "ACGTAC"])
    found = sorted(genes.search("TTACGTACGTAA"))
    print("DNA motifs:", found)
    banned = AhoCorasick(["darn", "heck", "frick"])
    message = "Darn it, what the heck! Frickin' printer jammed again... darned thing."
    print("Censored:", censor(message, banned))
    counts = {}
    for _, w in banned.search(message.lower()):
        counts[w] = counts.get(w, 0) + 1
    print("Counts:", dict(sorted(counts.items())))


if __name__ == "__main__":
    main()
