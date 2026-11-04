"""Order-preserving deduplication with a seen set and with dict.fromkeys."""

from typing import Hashable, Iterable, Iterator, Callable, TypeVar

T = TypeVar("T")

def unique(items: Iterable[T], key: Callable[[T], Hashable] = lambda x: x) -> Iterator[T]:
    seen = set()
    for item in items:
        k = key(item)
        if k not in seen:
            seen.add(k)
            yield item

data = [5, 3, 5, 1, 3, 9, 1, 7, 9]
print("input:", data)
print("unique generator:", list(unique(data)))
print("dict.fromkeys:", list(dict.fromkeys(data)))
print("sorted(set()):", sorted(set(data)))

emails = ["Bob@x.com", "alice@y.org", "bob@X.com", "carol@z.net", "ALICE@y.org"]
print("case-insensitive unique:", list(unique(emails, key=str.lower)))

records = [("north", 3), ("south", 1), ("north", 8), ("east", 2), ("south", 6)]
first_per_region = list(unique(records, key=lambda r: r[0]))
print("first record per region:", first_per_region)

text = "abracadabra"
print("unique letters in order:", "".join(unique(text)))

dupes = set()
seen = set()
for x in data:
    (dupes if x in seen else seen).add(x)
print("values that repeated:", sorted(dupes))
