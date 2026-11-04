"""Exercise the format specification mini-language with f-strings and format()."""

pi = 3.141592653589793
n = 1234567
neg = -42

print(f"[{pi:.2f}] [{pi:10.4f}] [{pi:<10.3f}] [{pi:^10.1f}] [{pi:+.3e}]")
print(f"[{n:,}] [{n:_}] [{n:>12,}] [{n:012d}]")
print(f"[{neg:5d}] [{neg:<5d}] [{neg:^7d}] [{neg:=+6d}] [{42:+d}] [{42: d}]")
print(f"[{0.256:.1%}] [{1/3:.4g}] [{1234.5:g}] [{0.00001234:g}]")
print(f"[{255:b}] [{255:o}] [{255:x}] [{255:X}] [{255:#x}] [{255:#010b}]")
print(f"[{'left':<10}] [{'right':>10}] [{'mid':^10}] [{'fill':*^10}]")
print(f"[{'truncate me':.5}] [{'pad':-<8}]")

# nested format specs
for width, precision in ((8, 2), (12, 5)):
    print(f"[{pi:{width}.{precision}f}]")

# str.format with positional and named fields
print("{0} + {0} = {1}".format(2, 4))
print("{name} is {age} years old".format(name="Bob", age=29))
print("{:>8}|{:^8}|{:<8}".format("r", "c", "l"))
point = {"x": 3, "y": -1}
print("point: ({x}, {y})".format(**point))
print("{0[1]} and {1.real}".format(["a", "b"], 3 + 4j))

# conversions
s = "tab\there"
print(f"{s!s} | {s!r} | {'é'!a}")

# format() builtin and __format__
print(format(0.5, ".0%"), format(1e6, ",.0f"), format(7, "03"))

table = [("Widget", 4, 3.5), ("Gadget", 12, 19.99), ("Doohickey", 1, 120.0)]
print(f"{'Item':<10}{'Qty':>5}{'Price':>10}{'Total':>10}")
for item, qty, price in table:
    print(f"{item:<10}{qty:>5}{price:>10.2f}{qty * price:>10.2f}")
