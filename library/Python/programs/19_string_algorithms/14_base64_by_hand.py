"""Base64 encoding and decoding implemented by hand with bit manipulation."""
from string import ascii_uppercase, ascii_lowercase, digits

ALPHABET = ascii_uppercase + ascii_lowercase + digits + "+/"
URLSAFE = ALPHABET[:-2] + "-_"
REVERSE = {ch: i for i, ch in enumerate(ALPHABET)}


def b64encode(data: bytes, alphabet: str = ALPHABET) -> str:
    out = []
    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]
        n = int.from_bytes(chunk.ljust(3, b"\0"), "big")
        quad = [alphabet[(n >> shift) & 0x3F] for shift in (18, 12, 6, 0)]
        pad = 3 - len(chunk)
        out.append("".join(quad[:4 - pad]) + "=" * pad)
    return "".join(out)


def b64decode(text: str) -> bytes:
    text = text.rstrip("=")
    out = bytearray()
    buffer = bits = 0
    for ch in text:
        if ch not in REVERSE:
            raise ValueError(f"invalid base64 character {ch!r}")
        buffer = (buffer << 6) | REVERSE[ch]
        bits += 6
        if bits >= 8:
            bits -= 8
            out.append((buffer >> bits) & 0xFF)
    return bytes(out)


KNOWN = {
    b"": "",
    b"f": "Zg==",
    b"fo": "Zm8=",
    b"foo": "Zm9v",
    b"foob": "Zm9vYg==",
    b"fooba": "Zm9vYmE=",
    b"foobar": "Zm9vYmFy",
    b"Man": "TWFu",
}


def main():
    for raw, expected in KNOWN.items():
        enc = b64encode(raw)
        status = "ok" if enc == expected and b64decode(enc) == raw else "MISMATCH"
        print(f"{raw!r:<10} -> {enc:<10} {status}")
    original = "Hello, Quantum! \u00dcn\u00efc\u00f6d\u00e9 \u2713"
    message = original.encode("utf-8")
    enc = b64encode(message)
    print("UTF-8 message:", enc)
    decoded = b64decode(enc).decode("utf-8")
    print("Decoded back: ", ascii(decoded), "| matches:", decoded == original)
    binary = bytes(range(250, 256)) + bytes([0, 62, 63])
    print("Binary standard:", b64encode(binary))
    print("Binary URL-safe:", b64encode(binary, URLSAFE))
    try:
        b64decode("abc$")
    except ValueError as exc:
        print("Error:", exc)
    ratio = len(b64encode(bytes(300))) / 300
    print(f"Size overhead: {ratio:.3f}x")


if __name__ == "__main__":
    main()
