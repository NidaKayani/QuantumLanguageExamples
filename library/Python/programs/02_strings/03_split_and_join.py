"""Split strings on separators and join pieces back together."""

csv_line = "alice,30,engineer,,london"
print(csv_line.split(","))
print(csv_line.split(",", 2))
print(csv_line.rsplit(",", 1))

sentence = "  the quick   brown\tfox \n jumps  "
print(sentence.split())
print(sentence.split(" ")[:6])

multiline = "line one\nline two\r\nline three\n"
print(multiline.splitlines())
print(multiline.splitlines(keepends=True))

path = "/usr/local/lib/python3/site-packages"
parts = [p for p in path.split("/") if p]
print(parts)
print(" > ".join(parts))
print("/".join(reversed(parts)))

numbers = [3, 1, 4, 1, 5, 9]
print("+".join(map(str, numbers)), "=", sum(numbers))
print(", ".join(f"{n:02d}" for n in numbers))

# parse key=value pairs
config = "host=localhost; port=8080; debug=true; name=demo app"
settings = dict(item.strip().split("=", 1) for item in config.split(";"))
for key in sorted(settings):
    print(f"{key:>6}: {settings[key]}")

# split on any whitespace then rejoin with single spaces
messy = "too    many     spaces   here"
print(repr(" ".join(messy.split())))

# words to snake_case and camelCase
words = "Convert This Phrase Now".split()
print("_".join(w.lower() for w in words))
print(words[0].lower() + "".join(w.capitalize() for w in words[1:]))
