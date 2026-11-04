"""Tuple fundamentals: packing, indexing, slicing and methods."""

point = (3, 4)
single = (42,)
not_a_tuple = (42)
empty = ()
packed = 1, "two", 3.0

print("point:", point, "type:", type(point).__name__)
print("single:", single, "len", len(single), "| parenthesised int:", not_a_tuple)
print("empty:", empty, "packed:", packed)

colors = ("red", "green", "blue", "green", "yellow", "green")
print("colors[1]:", colors[1], "colors[-1]:", colors[-1])
print("slice [1:4]:", colors[1:4], "reversed:", colors[::-1])
print("count green:", colors.count("green"), "index of blue:", colors.index("blue"))
print("index of green after 2:", colors.index("green", 2))

combined = point + (5,) + single
print("concatenation:", combined)
print("repetition:", ("ab",) * 3)

try:
    point[0] = 10
except TypeError as exc:
    print("immutable:", exc)

nested = ([1, 2], [3])
nested[0].append(99)
print("tuple holding mutable list:", nested)

print("comparison (1, 2, 3) < (1, 3):", (1, 2, 3) < (1, 3))
print("max by lexicographic order:", max([(2, "b"), (2, "a"), (1, "z")]))
print("tuple from generator:", tuple(x * x for x in range(5)))
print("membership 'blue' in colors:", "blue" in colors)
