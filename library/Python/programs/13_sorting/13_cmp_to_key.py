"""Custom comparison functions converted with functools.cmp_to_key."""

from functools import cmp_to_key


def largest_number_cmp(a: str, b: str) -> int:
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def largest_number(nums: list[int]) -> str:
    parts = sorted(map(str, nums), key=cmp_to_key(largest_number_cmp))
    joined = "".join(parts)
    return "0" if joined.startswith("0") else joined


def version_cmp(a: str, b: str) -> int:
    pa, pb = [int(x) for x in a.split(".")], [int(x) for x in b.split(".")]
    length = max(len(pa), len(pb))
    pa += [0] * (length - len(pa))
    pb += [0] * (length - len(pb))
    return (pa > pb) - (pa < pb)


def suit_rank_cmp(card_a, card_b):
    order = "23456789TJQKA"
    suits = "CDHS"
    ra, sa = card_a
    rb, sb = card_b
    if sa != sb:
        return suits.index(sa) - suits.index(sb)
    return order.index(rb) - order.index(ra)  # high cards first within suit


for nums in ([10, 2], [3, 30, 34, 5, 9], [0, 0], [824, 8247, 12, 121]):
    print(f"largest from {nums}: {largest_number(nums)}")

versions = ["1.0", "1.0.1", "0.9.9", "1.10", "1.2", "1.0.0", "2"]
print("versions:", sorted(versions, key=cmp_to_key(version_cmp)))
print("newest:", max(versions, key=cmp_to_key(version_cmp)))

hand = ["KH", "2S", "AH", "TC", "3H", "QS", "9C", "AS"]
print("hand grouped by suit:", sorted(hand, key=cmp_to_key(suit_rank_cmp)))

key = cmp_to_key(version_cmp)
print("key objects compare:", key("1.2") < key("1.10"), key("1.0") == key("1.0.0"))
