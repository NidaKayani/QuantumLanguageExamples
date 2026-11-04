"""Identifier case conversion (camel, snake, kebab, title) and URL slug generation with regex."""
import re

ACCENTS = str.maketrans("\u00e0\u00e1\u00e2\u00e4\u00e8\u00e9\u00ea\u00eb\u00ec\u00ed\u00ee\u00ef"
                        "\u00f2\u00f3\u00f4\u00f6\u00f9\u00fa\u00fb\u00fc\u00e7\u00f1",
                        "aaaaeeeeiiiioooouuuucn")
WORD_BOUNDARY = re.compile(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+")


def words_of(identifier):
    return [w.lower() for w in WORD_BOUNDARY.findall(identifier)]


def to_snake(s):
    return "_".join(words_of(s))


def to_kebab(s):
    return "-".join(words_of(s))


def to_camel(s):
    first, *rest = words_of(s)
    return first + "".join(w.capitalize() for w in rest)


def to_pascal(s):
    return "".join(w.capitalize() for w in words_of(s))


def to_constant(s):
    return to_snake(s).upper()


def slugify(title, max_len=40):
    text = title.translate(ACCENTS).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rsplit("-", 1)[0]
    return text


def main():
    identifiers = ["parseHTTPResponse", "user_id", "XMLHttpRequest", "get-api-v2-token",
                   "MAX_RETRY_COUNT", "simpleName", "IOError", "base64Encode"]
    print(f"{'input':<20}{'snake':<22}{'camel':<20}{'Pascal':<20}{'kebab'}")
    for ident in identifiers:
        print(f"{ident:<20}{to_snake(ident):<22}{to_camel(ident):<20}"
              f"{to_pascal(ident):<20}{to_kebab(ident)}")
    print("Constant:", to_constant("requestTimeoutMs"))
    titles = ["Hello, World!", "  Python 3.13: What's New?  ",
              "Caf\u00e9 cr\u00e8me br\u00fbl\u00e9e recipe",
              "10 Tips & Tricks for Faster Builds (2024 Edition)",
              "A very long title that keeps going well beyond the configured slug limit"]
    for t in titles:
        print(f"slug: {slugify(t)!r}")
    print("str.title vs capwords-ish:", "they're bill's friends".title(),
          "|", " ".join(w.capitalize() for w in "they're bill's friends".split()))
    print("swapcase:", "Hello World".swapcase(), "| casefold:", "STRASSE".casefold())


if __name__ == "__main__":
    main()
