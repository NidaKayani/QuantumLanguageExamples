"""Work with triple-quoted, raw and escape-sequence string literals."""

poem = """Roses are red,
  Violets are blue,
Python is "neat",
  and 'so' are you."""
print(poem)
print("lines:", len(poem.splitlines()))

escapes = "tab:\t| newline:\\n | quote:\" | backslash:\\ | unicode:\u00e9 | hex:\x41"
print(ascii(escapes))
print(repr("a\tb\nc"))

raw = r"C:\new\table\files"
print("raw:", raw, "length", len(raw))
print("not raw:", repr("C:\\new\\table"))

regex = r"\d+\.\d+"
print("raw regex:", regex)

# line continuation inside a string
long = "first part \
second part"
print(long)

# bytes and str literals
print(b"bytes literal", type(b"").__name__)
print("named unicode:", ascii("\N{GREEK SMALL LETTER ALPHA}\N{GREEK SMALL LETTER BETA}"))

doc_lines = __doc__.split()
print("module docstring has", len(doc_lines), "words")


def documented():
    """Return the answer.

    This docstring has several lines.
    """
    return 42


print(documented.__doc__.splitlines()[0])
print(f"""multi-line f-string:
  value = {documented()}
  doubled = {documented() * 2}""")
