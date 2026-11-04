"""A trie (prefix tree) for word storage, autocomplete and prefix counting."""


class TrieNode:
    __slots__ = ("children", "is_word", "count")

    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False
        self.count = 0  # words passing through this node


class Trie:
    def __init__(self, words=()):
        self.root = TrieNode()
        for w in words:
            self.insert(w)

    def insert(self, word):
        node = self.root
        node.count += 1
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
            node.count += 1
        node.is_word = True

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def __contains__(self, word):
        node = self._find(word)
        return bool(node and node.is_word)

    def count_prefix(self, prefix):
        node = self._find(prefix)
        return node.count if node else 0

    def complete(self, prefix):
        node = self._find(prefix)
        results = []

        def walk(n, path):
            if n.is_word:
                results.append(path)
            for ch in sorted(n.children):
                walk(n.children[ch], path + ch)

        if node:
            walk(node, prefix)
        return results

    def longest_common_prefix(self):
        node, prefix = self.root, ""
        while len(node.children) == 1 and not node.is_word:
            ch, node = next(iter(node.children.items()))
            prefix += ch
        return prefix


words = ["car", "card", "care", "careful", "cart", "cat", "dog", "dot", "dove", "do"]
trie = Trie(words)
for w in ["car", "ca", "dove", "doves"]:
    print(f"{w!r} in trie: {w in trie}")
for p in ["car", "do", "ca", "x"]:
    print(f"prefix {p!r}: count={trie.count_prefix(p)} words={trie.complete(p)}")
print("LCP of flower/flow/flight:", repr(Trie(["flower", "flow", "flight"]).longest_common_prefix()))
print("LCP of all words:", repr(trie.longest_common_prefix()))
