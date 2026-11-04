"""Run-length encoding: itertools.groupby, a regex decoder, and the look-and-say sequence."""
import re
from itertools import groupby


def rle_encode(text):
    return "".join(f"{len(list(group))}{ch}" for ch, group in groupby(text))


def rle_decode(encoded):
    return "".join(ch * int(count) for count, ch in re.findall(r"(\d+)(\D)", encoded))


def rle_compact(text):
    parts = []
    for ch, group in groupby(text):
        n = sum(1 for _ in group)
        parts.append(ch if n == 1 else f"{n}{ch}")
    return "".join(parts)


def rle_compact_decode(encoded):
    return re.sub(r"(\d+)(\D)", lambda m: m.group(2) * int(m.group(1)), encoded)


def look_and_say(seed, steps):
    terms = [seed]
    for _ in range(steps):
        terms.append("".join(f"{len(list(g))}{d}" for d, g in groupby(terms[-1])))
    return terms


def encode_bitmap(rows):
    return [[(px, len(list(g))) for px, g in groupby(row)] for row in rows]


def main():
    samples = ["WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW",
               "aaabccddddd", "abc", ""]
    for s in samples:
        enc, compact = rle_encode(s), rle_compact(s)
        assert rle_decode(enc) == s and rle_compact_decode(compact) == s
        ratio = len(compact) / len(s) if s else 1.0
        print(f"{s[:20]!r:<24} -> {enc[:30]!r:<34} compact {compact[:24]!r} ({ratio:.0%})")
    print("Look-and-say from '1':")
    for term in look_and_say("1", 8):
        print("  ", term)
    lengths = [len(t) for t in look_and_say("1", 30)]
    print(f"Growth ratio at step 30: {lengths[-1] / lengths[-2]:.4f} (Conway's constant ~1.3036)")
    bitmap = ["....####....", "...######...", "..##....##..", "...######..."]
    for row, runs in zip(bitmap, encode_bitmap(bitmap)):
        print(f"  {row}  {runs}")


if __name__ == "__main__":
    main()
