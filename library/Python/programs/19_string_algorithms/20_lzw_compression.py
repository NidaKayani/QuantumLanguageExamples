"""LZW compression and decompression with a growing dictionary, plus bit-width accounting."""
from math import ceil, log2


def lzw_compress(text):
    dictionary = {chr(i): i for i in range(256)}
    current, codes = "", []
    for ch in text:
        candidate = current + ch
        if candidate in dictionary:
            current = candidate
        else:
            codes.append(dictionary[current])
            dictionary[candidate] = len(dictionary)
            current = ch
    if current:
        codes.append(dictionary[current])
    return codes, dictionary


def lzw_decompress(codes):
    if not codes:
        return ""
    dictionary = {i: chr(i) for i in range(256)}
    previous = dictionary[codes[0]]
    out = [previous]
    for code in codes[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = previous + previous[0]
        else:
            raise ValueError(f"bad code {code}")
        out.append(entry)
        dictionary[len(dictionary)] = previous + entry[0]
        previous = entry
    return "".join(out)


def bit_cost(codes):
    total, size = 0, 256
    for _ in codes:
        size += 1
        total += max(9, ceil(log2(size)))
    return total


def main():
    samples = [
        "TOBEORNOTTOBEORTOBEORNOT",
        "abababababababababababababababab",
        "the rain in spain stays mainly in the plain",
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "",
    ]
    for text in samples:
        codes, dictionary = lzw_compress(text)
        assert lzw_decompress(codes) == text
        bits = bit_cost(codes)
        raw = len(text) * 8
        ratio = f"{bits / raw:.1%}" if raw else "n/a"
        print(f"{text[:30]!r:<34} chars={len(text):3d} codes={len(codes):3d} bits={bits:4d} ratio={ratio}")
    codes, dictionary = lzw_compress("TOBEORNOTTOBEORTOBEORNOT")
    print("Codes:", codes)
    learned = {v: k for k, v in dictionary.items() if v >= 256}
    print("Learned entries:", ", ".join(f"{k}={v}" for k, v in sorted(learned.items())[:10]), "...")
    print("KwKwK case:", lzw_compress("ababababa")[0], "->", lzw_decompress(lzw_compress("ababababa")[0]))


if __name__ == "__main__":
    main()
