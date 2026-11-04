"""Caesar and Vigenere ciphers with str.maketrans, plus frequency-analysis cracking of Caesar."""
from collections import Counter
from itertools import cycle
from string import ascii_lowercase, ascii_uppercase

ENGLISH_FREQ = {
    "e": 12.7, "t": 9.1, "a": 8.2, "o": 7.5, "i": 7.0, "n": 6.7, "s": 6.3, "h": 6.1,
    "r": 6.0, "d": 4.3, "l": 4.0, "c": 2.8, "u": 2.8, "m": 2.4, "w": 2.4, "f": 2.2,
    "g": 2.0, "y": 2.0, "p": 1.9, "b": 1.5, "v": 1.0, "k": 0.8, "j": 0.2, "x": 0.2,
    "q": 0.1, "z": 0.1,
}


def caesar(text, shift):
    shift %= 26
    table = str.maketrans(
        ascii_lowercase + ascii_uppercase,
        ascii_lowercase[shift:] + ascii_lowercase[:shift]
        + ascii_uppercase[shift:] + ascii_uppercase[:shift],
    )
    return text.translate(table)


def vigenere(text, key, decrypt=False):
    sign = -1 if decrypt else 1
    shifts = cycle(ord(k) - ord("a") for k in key.lower())
    out = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            out.append(chr((ord(ch) - base + sign * next(shifts)) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)


def chi_squared(text):
    letters = [c for c in text.lower() if c.isalpha()]
    counts = Counter(letters)
    n = len(letters)
    return sum((counts[c] - n * f / 100) ** 2 / (n * f / 100) for c, f in ENGLISH_FREQ.items())


def crack_caesar(ciphertext):
    scores = sorted((chi_squared(caesar(ciphertext, -s)), s) for s in range(26))
    return scores[0][1], scores[:3]


def main():
    message = "Meet me near the old clock tower at seven, bring the documents."
    secret = caesar(message, 13)
    print("ROT13:     ", secret)
    print("ROT13 x2:  ", caesar(secret, 13))
    enc = caesar(message, 7)
    shift, top = crack_caesar(enc)
    print("Caesar +7: ", enc)
    print(f"Cracked shift {shift}; top candidates {[(s, round(c, 1)) for c, s in top]}")
    print("Recovered: ", caesar(enc, -shift))
    key = "lemon"
    v = vigenere("Attack at Dawn!", key)
    print(f"Vigenere({key}): {v} -> {vigenere(v, key, decrypt=True)}")


if __name__ == "__main__":
    main()
