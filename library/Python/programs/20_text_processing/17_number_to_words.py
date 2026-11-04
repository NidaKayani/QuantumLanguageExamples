"""Spell out numbers in English words, ordinals, and cheque-style currency amounts."""
from decimal import Decimal, ROUND_HALF_UP

ONES = ("zero one two three four five six seven eight nine ten eleven twelve thirteen "
        "fourteen fifteen sixteen seventeen eighteen nineteen").split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
SCALES = [(10**12, "trillion"), (10**9, "billion"), (10**6, "million"), (1000, "thousand")]
ORDINAL_FIX = {"one": "first", "two": "second", "three": "third", "five": "fifth",
               "eight": "eighth", "nine": "ninth", "twelve": "twelfth"}


def below_thousand(n):
    parts = []
    hundreds, rest = divmod(n, 100)
    if hundreds:
        parts.append(f"{ONES[hundreds]} hundred")
    if rest:
        if rest < 20:
            parts.append(ONES[rest])
        else:
            tens, ones = divmod(rest, 10)
            parts.append(TENS[tens] + (f"-{ONES[ones]}" if ones else ""))
    return " ".join(parts)


def to_words(n):
    if n < 0:
        return "minus " + to_words(-n)
    if n < 1000:
        return below_thousand(n) or "zero"
    parts = []
    for value, name in SCALES:
        count, n = divmod(n, value)
        if count:
            parts.append(f"{to_words(count)} {name}")
    if n:
        parts.append(below_thousand(n))
    return " ".join(parts)


def ordinal_words(n):
    words = to_words(n)
    head, sep, last = words.rpartition(" ") if "-" not in words.split(" ")[-1] else words.rpartition("-")
    if last in ORDINAL_FIX:
        last = ORDINAL_FIX[last]
    elif last.endswith("y"):
        last = last[:-1] + "ieth"
    else:
        last += "th"
    return head + sep + last


def ordinal_suffix(n):
    if 10 <= n % 100 <= 20:
        return f"{n}th"
    return f"{n}{ {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th') }"


def cheque(amount):
    amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    dollars = int(amount)
    cents = int((amount - dollars) * 100)
    text = f"{to_words(dollars)} dollar{'s' if dollars != 1 else ''} and {cents:02d}/100"
    return text[0].upper() + text[1:]


def main():
    for n in (0, 7, 13, 42, 100, 115, 999, 1001, 20_024, 1_000_000, 7_654_321, -86, 2**40):
        print(f"{n:>15,}: {to_words(n)}")
    print("Ordinals:", ", ".join(ordinal_words(n) for n in (1, 2, 3, 5, 12, 20, 21, 99, 100, 1003)))
    print("Suffixes:", " ".join(ordinal_suffix(n) for n in (1, 2, 3, 4, 11, 12, 13, 21, 22, 101, 111, 1002)))
    for amount in ("1.00", "19.99", "1234.565", "1000000"):
        print(f"Cheque {amount:>10}: {cheque(amount)}")


if __name__ == "__main__":
    main()
