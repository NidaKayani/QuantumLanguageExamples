"""Basic set creation, mutation and membership tests."""

fruits = {"apple", "banana", "cherry"}
print("initial:", sorted(fruits))

fruits.add("date")
fruits.add("apple")  # duplicates are ignored
print("after add:", sorted(fruits), "size", len(fruits))

fruits.discard("banana")
fruits.discard("kiwi")  # no error for missing items
print("after discard:", sorted(fruits))

try:
    fruits.remove("kiwi")
except KeyError as exc:
    print("remove failed with KeyError:", exc)

for candidate in ["apple", "banana", "date"]:
    status = "present" if candidate in fruits else "absent"
    print(f"  {candidate:>7}: {status}")

numbers = set([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
print("unique digits:", sorted(numbers))
print("min/max/sum:", min(numbers), max(numbers), sum(numbers))

empty = set()
print("empty set is falsy:", not empty, "repr:", repr(empty))

popped = set()
work = {10, 20, 30}
while work:
    popped.add(work.pop())
print("popped all:", sorted(popped), "remaining:", len(work))

copy_of = numbers.copy()
copy_of.clear()
print("original kept", len(numbers), "items; cleared copy has", len(copy_of))
