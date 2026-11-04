"""Burrows-Wheeler transform with its inverse, followed by move-to-front coding."""
from collections import Counter

SENTINEL = "$"


def bwt(text):
    s = text + SENTINEL
    rotations = sorted(s[i:] + s[:i] for i in range(len(s)))
    return "".join(r[-1] for r in rotations)


def inverse_bwt(last):
    counts = Counter(last)
    first_index, total = {}, 0
    for ch in sorted(counts):
        first_index[ch] = total
        total += counts[ch]
    seen = Counter()
    lf = []
    for ch in last:
        lf.append(first_index[ch] + seen[ch])
        seen[ch] += 1
    out, row = [], last.index(SENTINEL)
    for _ in range(len(last) - 1):
        row = lf[row]
        out.append(last[row])
    return "".join(reversed(out))


def move_to_front(text):
    table = sorted(set(text))
    out = []
    for ch in text:
        idx = table.index(ch)
        out.append(idx)
        table.insert(0, table.pop(idx))
    return out, sorted(set(text))


def undo_mtf(codes, alphabet):
    table, out = list(alphabet), []
    for idx in codes:
        ch = table.pop(idx)
        out.append(ch)
        table.insert(0, ch)
    return "".join(out)


def main():
    for text in ("banana", "abracadabra", "mississippi", "she sells sea shells by the sea shore"):
        transformed = bwt(text)
        restored = inverse_bwt(transformed)
        assert restored == text
        codes, alphabet = move_to_front(transformed)
        assert undo_mtf(codes, alphabet) == transformed
        zeros = codes.count(0)
        print(f"text: {text!r}")
        print(f"  bwt: {transformed!r}")
        print(f"  mtf: {codes}")
        print(f"  zeros {zeros}/{len(codes)} ({zeros / len(codes):.0%}), round trip ok")
    s = "banana" + SENTINEL
    print("Sorted rotation matrix of 'banana$':")
    for r in sorted(s[i:] + s[:i] for i in range(len(s))):
        print(f"  {r[0]} {r[1:-1]} {r[-1]}")


if __name__ == "__main__":
    main()
