"""Create, index, append, insert and remove list elements."""

fruits = ["apple", "banana", "cherry"]
print("start:", fruits, "len", len(fruits))

fruits.append("date")
fruits.insert(1, "apricot")
fruits.extend(["elderberry", "fig"])
print("after adds:", fruits)

print("first:", fruits[0], "last:", fruits[-1], "second last:", fruits[-2])

fruits[2] = "blueberry"
print("after assignment:", fruits)

removed = fruits.pop()
print("popped:", removed)
removed_first = fruits.pop(0)
print("popped index 0:", removed_first)
fruits.remove("cherry")
print("after remove:", fruits)

del fruits[1]
print("after del:", fruits)

print("index of 'date':", fruits.index("date"))
print("'fig' in fruits:", "fig" in fruits)
print("count of 'apricot':", fruits.count("apricot"))

try:
    fruits.remove("mango")
except ValueError as e:
    print("ValueError:", e)

try:
    fruits[10]
except IndexError as e:
    print("IndexError:", e)

empty = []
print("empty is falsy:", not empty, "| list('abc'):", list("abc"), "| list(range(4)):", list(range(4)))
mixed = [1, "two", 3.0, [4], None, True]
print("mixed types:", [type(x).__name__ for x in mixed])
fruits.clear()
print("cleared:", fruits)
