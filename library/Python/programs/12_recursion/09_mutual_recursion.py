"""Mutual recursion: even/odd, Hofstadter female/male sequences, and a parser."""

from functools import lru_cache


def is_even(n: int) -> bool:
    return True if n == 0 else is_odd(n - 1)


def is_odd(n: int) -> bool:
    return False if n == 0 else is_even(n - 1)


@lru_cache(maxsize=None)
def female(n: int) -> int:
    return 1 if n == 0 else n - male(female(n - 1))


@lru_cache(maxsize=None)
def male(n: int) -> int:
    return 0 if n == 0 else n - female(male(n - 1))


print("parity:", {n: ("even" if is_even(n) else "odd") for n in [0, 7, 10, 33]})
print("F:", [female(n) for n in range(15)])
print("M:", [male(n) for n in range(15)])

# Balanced nested lists grammar:  list := '[' items ']'   items := (atom | list) (',' items)?


def parse_list(s: str, i: int):
    assert s[i] == "["
    i += 1
    items = []
    if s[i] == "]":
        return items, i + 1
    while True:
        item, i = parse_item(s, i)
        items.append(item)
        if s[i] == ",":
            i += 1
        elif s[i] == "]":
            return items, i + 1
        else:
            raise SyntaxError(f"unexpected {s[i]!r} at {i}")


def parse_item(s: str, i: int):
    if s[i] == "[":
        return parse_list(s, i)
    j = i
    while s[j].isdigit():
        j += 1
    return int(s[i:j]), j


for text in ["[1,2,3]", "[[1],[2,[3,4]],[]]", "[10,[20,[30,[40]]]]"]:
    value, _ = parse_list(text, 0)
    print(f"{text:<22} -> {value}")
