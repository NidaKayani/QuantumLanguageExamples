"""Parse and build URLs and query strings by hand, including percent-encoding and decoding."""
import re
from collections import defaultdict
from string import ascii_letters, digits

SAFE = set(ascii_letters + digits + "-._~")
URL_RE = re.compile(
    r"^(?P<scheme>[a-z][a-z0-9+.-]*)://(?:(?P<user>[^@/]+)@)?(?P<host>[^:/?#]+)"
    r"(?::(?P<port>\d+))?(?P<path>/[^?#]*)?(?:\?(?P<query>[^#]*))?(?:#(?P<fragment>.*))?$"
)


def percent_encode(text, plus_spaces=True):
    out = []
    for byte in text.encode("utf-8"):
        ch = chr(byte)
        if ch in SAFE:
            out.append(ch)
        elif ch == " " and plus_spaces:
            out.append("+")
        else:
            out.append(f"%{byte:02X}")
    return "".join(out)


def percent_decode(text):
    text = text.replace("+", " ")
    raw = bytearray()
    i = 0
    while i < len(text):
        if text[i] == "%" and re.fullmatch(r"[0-9A-Fa-f]{2}", text[i + 1:i + 3]):
            raw.append(int(text[i + 1:i + 3], 16))
            i += 3
        else:
            raw.extend(text[i].encode("utf-8"))
            i += 1
    return raw.decode("utf-8")


def parse_query(query):
    params = defaultdict(list)
    for pair in filter(None, query.split("&")):
        key, _, value = pair.partition("=")
        params[percent_decode(key)].append(percent_decode(value))
    return dict(params)


def build_query(params):
    return "&".join(f"{percent_encode(k)}={percent_encode(str(v))}"
                    for k, values in params.items()
                    for v in (values if isinstance(values, list) else [values]))


def main():
    url = ("https://alice@shop.example.com:8443/search/results?q=caf%C3%A9+au+lait"
           "&tag=hot&tag=sweet&price=%3C5&empty=&flag#reviews")
    parts = URL_RE.match(url).groupdict()
    for key, value in parts.items():
        print(f"{key:>9}: {value}")
    params = parse_query(parts["query"])
    print("Query params:")
    for key, values in params.items():
        print(f"  {key!r}: {ascii(values)}")
    rebuilt = build_query({"q": "50% off & free shipping", "lang": ["en", "fr"], "n": 3})
    print("Built query:", rebuilt)
    print("Round trip:", parse_query(rebuilt))
    print("Encode path segment:", percent_encode("reports/2024 Q3.pdf", plus_spaces=False))
    print("Bad URL match:", URL_RE.match("not a url"))


if __name__ == "__main__":
    main()
