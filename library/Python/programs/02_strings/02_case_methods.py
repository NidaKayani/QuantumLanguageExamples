"""Compare case-conversion methods like upper, lower, title, capitalize and casefold."""

samples = ["hello world", "PYTHON rocks", "mIxEd CaSe", "o'neil's café", "straße"]

for text in samples:
    print(f"original:   {text!a}")
    print(f"  upper:      {ascii(text.upper())}")
    print(f"  lower:      {ascii(text.lower())}")
    print(f"  title:      {ascii(text.title())}")
    print(f"  capitalize: {ascii(text.capitalize())}")
    print(f"  swapcase:   {ascii(text.swapcase())}")
    print(f"  casefold:   {ascii(text.casefold())}")

# case-insensitive comparison
a, b = "Strasse", "straße"
print("lower equal:", a.lower() == b.lower())
print("casefold equal:", a.casefold() == b.casefold())

# checking case
for word in ("ABC", "abc", "Abc", "Title Case Words", "123"):
    print(f"{word:18} isupper={word.isupper()!s:5} islower={word.islower()!s:5} istitle={word.istitle()}")


def smart_title(text, small=("a", "an", "the", "of", "in", "and")):
    words = text.lower().split()
    return " ".join(
        w if i and w in small else w.capitalize()
        for i, w in enumerate(words)
    )


print(smart_title("the lord of the rings"))
print(smart_title("a tale OF two cities and the sea"))
