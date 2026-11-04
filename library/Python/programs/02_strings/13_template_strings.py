"""Use string.Template substitution and string module constants."""

from string import Template
import string

letter = Template("Dear $name,\nYour order #$order_id of $$${amount} ships on ${day}day.")
print(letter.substitute(name="Ms. Lovelace", order_id=1042, amount="59.90", day="Tues"))

partial = Template("Hello $who, welcome to $place")
print(partial.safe_substitute(who="friend"))

try:
    partial.substitute(who="friend")
except KeyError as e:
    print("missing placeholder:", e)

print("identifiers:", partial.get_identifiers())

rows = [{"item": "pen", "qty": 3}, {"item": "notebook", "qty": 1}]
line = Template("  - ${qty} x ${item}")
for r in rows:
    print(line.substitute(r))


class PercentTemplate(Template):
    delimiter = "%"


print(PercentTemplate("Progress: %pct%% done").substitute(pct=75))

print("ascii_letters:", string.ascii_letters)
print("digits:", string.digits, "| hexdigits:", string.hexdigits)
print("punctuation:", string.punctuation)
print("capwords:", string.capwords("hello   wide  world"))

formatter = string.Formatter()
parsed = [field for _, field, _, _ in formatter.parse("{a} and {b:>5} then {c!r}") if field]
print("fields in format string:", parsed)
