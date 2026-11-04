"""Demonstrate the assignment expression (walrus) operator in loops and comprehensions."""

import re

data = [3, 8, 1, 12, 7, 20, 5]

# reuse a computed value inside a condition
if (n := len(data)) > 5:
    print(f"list is long ({n} elements)")

# consume a stack with walrus in the while condition
stack = list(range(1, 6))
while (top := stack.pop() if stack else None) is not None:
    print("popped", top)

# filter and transform without recomputing
def expensive(x):
    return x * x - 10

results = [y for x in data if (y := expensive(x)) > 20]
print("squares-minus-10 above 20:", results)

# regex match with walrus
lines = ["id=42", "name=bob", "id=7", "junk", "id=x"]
ids = []
for line in lines:
    if (m := re.fullmatch(r"id=(\d+)", line)) is not None:
        ids.append(int(m.group(1)))
print("parsed ids:", ids)

# running total with walrus in a comprehension
total = 0
running = [total := total + x for x in data]
print("running totals:", running, "final:", total)

# chunked reading from an iterator
chars = iter("abcdefghij")
chunks = []
while chunk := "".join(c for _, c in zip(range(3), chars)):
    chunks.append(chunk)
print("chunks:", chunks)
