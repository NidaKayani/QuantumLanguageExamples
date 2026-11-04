"""Encrypt and decrypt text with a Caesar cipher using str.maketrans."""

import string


def make_table(shift):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    shifted = lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]
    return str.maketrans(lower + upper, shifted)


def encrypt(text, shift):
    return text.translate(make_table(shift % 26))


def decrypt(text, shift):
    return encrypt(text, -shift)


def crack(ciphertext):
    # score each shift by how many common English letters appear
    common = set("etaoinshr")
    best = max(range(26), key=lambda s: sum(c in common for c in decrypt(ciphertext, s).lower()))
    return best, decrypt(ciphertext, best)


message = "The Quick Brown Fox Jumps Over The Lazy Dog!"
for shift in (1, 3, 13, 25):
    secret = encrypt(message, shift)
    print(f"shift {shift:2d}: {secret}")
    assert decrypt(secret, shift) == message

rot13 = encrypt("Hello, World", 13)
print("rot13 twice:", encrypt(rot13, 13))

ciphertext = encrypt("attack at dawn, retreat at nightfall", 7)
shift, plain = crack(ciphertext)
print(f"cracked shift {shift}: {plain}")

# deleting characters with translate
no_vowels = str.maketrans("", "", "aeiouAEIOU")
print(message.translate(no_vowels))
print("Hello".translate({ord("l"): "L", ord("o"): None}))
