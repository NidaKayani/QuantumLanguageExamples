"""Show that strings are immutable and how to build modified copies."""

s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print("TypeError:", e)

capitalized = "H" + s[1:]
print(s, "->", capitalized)

chars = list(s)
chars[-1] = "0"
chars.insert(0, "[")
chars.append("]")
print("via list:", "".join(chars))

# methods return new strings
original = "  Mixed Case  "
changed = original.strip().upper()
print(repr(original), "->", repr(changed))

# string interning-independent equality
a = "".join(["py", "thon"])
b = "python"
print("equal:", a == b)

# += in a loop creates new strings each time
acc = ""
for word in ("immutable", "strings", "are", "safe"):
    acc += word.capitalize()
print(acc)

# replace a character at a position
def replace_at(text, index, ch):
    return text[:index] + ch + text[index + 1:]

print(replace_at("kitten", 0, "m"))
print(replace_at("python", 5, "N"))

# strings as dict keys because they are immutable
inventory = {"apple": 3}
key = "app" + "le"
inventory[key] += 1
print(inventory)

# multiplication shares nothing mutable
row = "-" * 5
rows = [row] * 3
rows[0] = rows[0].replace("-", "+")
print(rows)
