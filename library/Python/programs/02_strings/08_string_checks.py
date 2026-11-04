"""Classify characters and strings with the is* predicate methods."""

samples = ["hello", "Hello123", "12345", "3.14", "   ", "", "Ⅻ", "½", "²",
           "under_score", "MixedCase", "ALLCAPS", "tab\t", "Title Case"]

checks = ["isalpha", "isdigit", "isnumeric", "isdecimal", "isalnum",
          "isspace", "isupper", "islower", "istitle", "isidentifier"]

header = f"{'value':14}" + "".join(f"{c[2:7]:>7}" for c in checks)
print(header)
for s in samples:
    row = f"{s!a:14}"
    for c in checks:
        row += f"{'Y' if getattr(s, c)() else '.':>7}"
    print(row)

print()
print("isprintable('a\\nb'):", "a\nb".isprintable())
print("isascii('cafe'):", "cafe".isascii(), "| isascii('caf\\xe9'):", "caf\xe9".isascii())


def classify_password(pw):
    problems = []
    if len(pw) < 8:
        problems.append("too short")
    if not any(c.isupper() for c in pw):
        problems.append("no uppercase")
    if not any(c.islower() for c in pw):
        problems.append("no lowercase")
    if not any(c.isdigit() for c in pw):
        problems.append("no digit")
    if pw.isalnum():
        problems.append("no symbol")
    return "strong" if not problems else ", ".join(problems)


for pw in ("abc", "password", "Password1", "Pa$$w0rd!", "12345678"):
    print(f"{pw:12} -> {classify_password(pw)}")
