"""A prefix trie with insert, search, delete, ranked autocomplete, and wildcard matching."""
from typing import Iterator


class TrieNode:
    __slots__ = ("children", "count", "terminal")

    def __init__(self):
        self.children = {}
        self.count = 0
        self.terminal = False


class Trie:
    def __init__(self, words=()):
        self.root = TrieNode()
        self.size = 0
        for w in words:
            self.insert(w)

    def insert(self, word, weight=1):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        if not node.terminal:
            self.size += 1
        node.terminal = True
        node.count += weight

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def __contains__(self, word):
        node = self._find(word)
        return bool(node and node.terminal)

    def __len__(self):
        return self.size

    def _walk(self, node, prefix) -> Iterator:
        if node.terminal:
            yield prefix, node.count
        for ch in sorted(node.children):
            yield from self._walk(node.children[ch], prefix + ch)

    def complete(self, prefix, limit=5):
        node = self._find(prefix)
        if node is None:
            return []
        matches = sorted(self._walk(node, prefix), key=lambda wc: (-wc[1], wc[0]))
        return [w for w, _ in matches[:limit]]

    def wildcard(self, pattern, node=None, prefix=""):
        node = node or self.root
        if not pattern:
            return [prefix] if node.terminal else []
        head, rest = pattern[0], pattern[1:]
        keys = sorted(node.children) if head == "." else [head] if head in node.children else []
        return [m for k in keys for m in self.wildcard(rest, node.children[k], prefix + k)]

    def delete(self, word):
        node = self._find(word)
        if node and node.terminal:
            node.terminal, node.count = False, 0
            self.size -= 1
            return True
        return False


def main():
    queries = ("car cart carbon card care careful cat catalog category dog dodge "
               "door car card card care cat cat cat").split()
    trie = Trie()
    for q in queries:
        trie.insert(q)
    print("Distinct words:", len(trie))
    for prefix in ("ca", "car", "do", "z"):
        print(f"complete({prefix!r}) -> {trie.complete(prefix)}")
    print("'cart' in trie:", "cart" in trie, "| 'ca' in trie:", "ca" in trie)
    print("Wildcard 'ca.':", trie.wildcard("ca."))
    print("Wildcard 'd..r':", trie.wildcard("d..r"))
    trie.delete("cat")
    print("After deleting 'cat':", trie.complete("ca", limit=10), "size", len(trie))
    print("All words:", [w for w, _ in trie._walk(trie.root, "")])


if __name__ == "__main__":
    main()
