"""Build strings efficiently with join, lists, multiplication and comprehension."""

# join is the idiomatic way to build from many pieces
pieces = []
for i in range(1, 8):
    pieces.append(f"<{i}>")
print("".join(pieces))

# repetition and concatenation
print("-=" * 15 + "-")
print("ab" + "cd" * 3 + "e")

# implicit concatenation of adjacent literals
message = ("This is a long message "
           "split across several "
           "source lines.")
print(message)

# building a table row by row
data = [("Name", "Lang", "Year"), ("Guido", "Python", 1991), ("Bjarne", "C++", 1985), ("James", "Java", 1995)]
widths = [max(len(str(row[i])) for row in data) for i in range(3)]
lines = []
for row in data:
    lines.append(" | ".join(str(cell).ljust(w) for cell, w in zip(row, widths)))
lines.insert(1, "-+-".join("-" * w for w in widths))
print("\n".join(lines))

# run-length encoding
def rle_encode(s):
    out = []
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        out.append(f"{j - i}{s[i]}")
        i = j
    return "".join(out)


def rle_decode(s):
    import re
    return "".join(ch * int(n) for n, ch in re.findall(r"(\d+)(\D)", s))


for s in ("aaabccddddd", "abc", "zzzzzzzzzzzz"):
    enc = rle_encode(s)
    print(f"{s} -> {enc} -> {rle_decode(enc)}")

# str() vs repr() when building messages
values = ["text", 3, 2.5, None, [1, "x"]]
print("str: ", ", ".join(str(v) for v in values))
print("repr:", ", ".join(repr(v) for v in values))
