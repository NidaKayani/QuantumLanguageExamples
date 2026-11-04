"""Encode and decode text with UTF-8 and other codecs and inspect the bytes."""

text = "naïve café – 日本"

utf8 = text.encode("utf-8")
print("chars:", len(text), "utf-8 bytes:", len(utf8))
print("utf-8:", utf8)
print("hex:", utf8.hex(" "))
print("decoded:", ascii(utf8.decode("utf-8")))

utf16 = text.encode("utf-16-le")
print("utf-16-le bytes:", len(utf16))

for errors in ("ignore", "replace", "xmlcharrefreplace", "backslashreplace"):
    print(f"ascii/{errors}: {text.encode('ascii', errors=errors)}")

try:
    text.encode("ascii")
except UnicodeEncodeError as e:
    print("strict failure at position", e.start, "char", ascii(e.object[e.start]))

bad = b"valid \xff\xfe bytes"
print("decode replace:", ascii(bad.decode("utf-8", errors="replace")))

latin = "café".encode("latin-1")
print("latin-1:", latin, "-> as utf-8 with replace:", ascii(latin.decode("utf-8", "replace")))

for ch in "Aé€😀":
    print(f"{ch!a}: U+{ord(ch):04X}, utf-8 = {ch.encode().hex()}, {len(ch.encode())} bytes")

print("chr(9731):", ascii(chr(9731)), "| ord('Z'):", ord("Z"))

raw = bytes([72, 101, 108, 108, 111])
print(raw, raw.decode(), list(raw))
ba = bytearray(b"hello")
ba[0] = ord("J")
ba.extend(b"!")
print(ba, ba.decode().upper())
