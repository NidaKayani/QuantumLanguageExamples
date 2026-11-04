"""Count things with collections.Counter and its arithmetic."""

from collections import Counter

votes = ["alice", "bob", "alice", "carol", "bob", "alice", "dave", "carol", "alice"]
tally = Counter(votes)
print("tally:", tally)
print("winner:", tally.most_common(1)[0])
print("top 2:", tally.most_common(2))
print("missing key is zero:", tally["zoe"])

letters = Counter("abracadabra")
print("letters:", sorted(letters.items()))
print("total letters:", letters.total())
print("elements:", "".join(sorted(letters.elements())))

a = Counter(apples=3, pears=1, plums=5)
b = Counter(apples=1, pears=4, kiwis=2)
print("a + b:", dict(sorted((a + b).items())))
print("a - b:", dict(sorted((a - b).items())))
print("a & b:", dict(sorted((a & b).items())))
print("a | b:", dict(sorted((a | b).items())))

inventory = Counter(widgets=10, gadgets=4)
inventory.update(widgets=5, gizmos=2)
inventory.subtract(gadgets=6)
print("inventory:", dict(inventory))
print("positive only:", dict(+inventory))


def is_anagram(x, y):
    return Counter(x.replace(" ", "").lower()) == Counter(y.replace(" ", "").lower())


print("anagram:", is_anagram("Dormitory", "dirty room"), is_anagram("hello", "world"))


def can_build(note, magazine):
    return not (Counter(note) - Counter(magazine))


print("ransom note:", can_build("aab", "baa"), can_build("aabbc", "abcab"))

words = "the cat and the hat and the bat".split()
freq = Counter(words)
print("least common:", freq.most_common()[:-3:-1])
