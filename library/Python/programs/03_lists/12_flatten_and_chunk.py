"""Flatten nested lists recursively and split lists into chunks."""

from itertools import chain, islice, batched


def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def flatten_gen(items):
    for item in items:
        if isinstance(item, (list, tuple)):
            yield from flatten_gen(item)
        else:
            yield item


def chunk(seq, size):
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def chunk_iter(iterable, size):
    it = iter(iterable)
    while piece := list(islice(it, size)):
        yield piece


nested = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9], []]
print("recursive:", flatten(nested))
print("generator:", list(flatten_gen([1, (2, 3), [4, [5, (6,)]]])))

one_level = [[1, 2], [3], [4, 5, 6]]
print("chain.from_iterable:", list(chain.from_iterable(one_level)))
print("comprehension:", [x for sub in one_level for x in sub])

letters = list("abcdefghijk")
print("chunk(3):", chunk(letters, 3))
print("chunk_iter(4):", list(chunk_iter(range(10), 4)))
print("batched(5):", list(batched(range(12), 5)))


def depth(items):
    if not isinstance(items, list):
        return 0
    return 1 + max((depth(x) for x in items), default=0)


print("nesting depth:", depth(nested))
print("interleave:", [x for pair in zip("ace", "bdf") for x in pair])
