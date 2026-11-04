"""sorted() and list.sort() with key, reverse and operator helpers."""

from operator import attrgetter, itemgetter, methodcaller
from dataclasses import dataclass


@dataclass
class City:
    name: str
    country: str
    population: int


cities = [
    City("Lagos", "NG", 15_388_000),
    City("Tokyo", "JP", 37_194_000),
    City("Osaka", "JP", 19_013_000),
    City("Abuja", "NG", 3_840_000),
    City("Lyon", "FR", 1_748_000),
    City("Paris", "FR", 11_208_000),
]

print("by population desc:")
for c in sorted(cities, key=attrgetter("population"), reverse=True):
    print(f"  {c.name:<6} {c.population:>12,}")

print("by country, then name:", [c.name for c in sorted(cities, key=attrgetter("country", "name"))])

words = ["Banana", "apple", "cherry", "Date", "elderberry", "fig"]
print("default (case-sensitive):", sorted(words))
print("case-insensitive:", sorted(words, key=str.lower))
print("by length then alpha:", sorted(words, key=lambda w: (len(w), w.lower())))
print("by last letter:", sorted(words, key=itemgetter(-1)))
print("by count of 'e':", sorted(words, key=methodcaller("count", "e"), reverse=True))

scores = {"amy": 82, "raj": 95, "tom": 82, "eva": 77}
ranking = sorted(scores.items(), key=itemgetter(1), reverse=True)
print("ranking:", ranking)

nums = [3, -7, 2, -1, 8, -4]
nums.sort(key=abs)
print("in-place by abs:", nums)
nums.sort(reverse=True)
print("in-place reversed:", nums)
print("sorted returns new list; reversed() iterator:", list(reversed(sorted(nums))))
print("sorted string chars:", "".join(sorted("sorting")))
