"""Wrap, fill, indent and dedent paragraphs with the textwrap module."""

import textwrap

paragraph = (
    "Python is a high-level, general-purpose programming language. Its design "
    "philosophy emphasizes code readability with the use of significant "
    "indentation. Python is dynamically typed and garbage-collected."
)

for width in (40, 60):
    print(f"--- width {width} ---")
    print(textwrap.fill(paragraph, width=width))

lines = textwrap.wrap(paragraph, width=30)
print(f"\n{len(lines)} lines when wrapped at 30; longest is {max(map(len, lines))}")

print("\nshortened:", textwrap.shorten(paragraph, width=50, placeholder=" [...]"))

print("\nhanging indent:")
print(textwrap.fill(paragraph, width=50, initial_indent="* ", subsequent_indent="  "))

code = """
    def greet(name):
        return f"hi {name}"
"""
print("\ndedented:")
print(textwrap.dedent(code).strip())

print("\nindented as quote:")
print(textwrap.indent("first line\nsecond line\n\nfourth line", "> "))


def justify(line, width):
    words = line.split()
    if len(words) == 1:
        return line.ljust(width)
    gaps = len(words) - 1
    spaces = width - sum(map(len, words))
    q, r = divmod(spaces, gaps)
    return "".join(w + " " * (q + (i < r)) for i, w in enumerate(words[:-1])) + words[-1]


print("\nfully justified:")
for line in textwrap.wrap(paragraph, 36):
    print("|" + justify(line, 36) + "|")
