"""Basic try/except handling of common built-in exceptions."""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf") if a > 0 else float("-inf") if a < 0 else float("nan")


def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None


def get_item(seq, index):
    try:
        return seq[index]
    except IndexError:
        return f"<no index {index}>"
    except TypeError as exc:
        return f"<bad index: {exc}>"


print("10 / 4 =", safe_divide(10, 4))
print("10 / 0 =", safe_divide(10, 0))
print("-3 / 0 =", safe_divide(-3, 0))
print("0 / 0 =", safe_divide(0, 0))

for text in ["42", "-7", "3.14", "abc", " 12 "]:
    print(f"parse_int({text!r}) = {parse_int(text)}")

data = [10, 20, 30]
for idx in [0, 2, 5, -1, "1"]:
    print(f"get_item({idx!r}) = {get_item(data, idx)}")

inventory = {"apple": 3}
for fruit in ["apple", "pear"]:
    try:
        print(fruit, "count:", inventory[fruit])
    except KeyError as exc:
        print("missing key:", exc)

try:
    undefined_variable
except NameError as exc:
    print("NameError:", exc)
try:
    "5" + 5
except TypeError as exc:
    print("TypeError:", exc)
