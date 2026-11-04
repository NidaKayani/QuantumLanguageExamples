"""Sorting items by frequency with Counter and tie-breaking rules."""

from collections import Counter

nums = [4, 6, 2, 6, 4, 4, 3, 2, 6, 9, 2, 6]
counts = Counter(nums)
print("counts:", sorted(counts.items()))
print("most_common:", counts.most_common())

by_freq_then_value = sorted(nums, key=lambda x: (-counts[x], x))
print("by frequency desc, then value:", by_freq_then_value)

first_seen = {}
for i, x in enumerate(nums):
    first_seen.setdefault(x, i)
by_first = sorted(counts, key=lambda x: (-counts[x], first_seen[x]))
print("distinct by freq, ties by first occurrence:", by_first)

text = "it was the best of times it was the worst of times"
word_counts = Counter(text.split())
print("top words:", sorted(word_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:4])

letters = Counter(c for c in "mississippi river")
ordered = "".join(ch * n for ch, n in sorted(letters.items(), key=lambda kv: (-kv[1], kv[0])) if ch != " ")
print("letters by frequency:", ordered)

print("least common two:", sorted(counts.items(), key=lambda kv: (kv[1], kv[0]))[:2])
