"""A regex-driven tokenizer with named groups for a small configuration language."""
import re
from typing import NamedTuple


class Token(NamedTuple):
    kind: str
    value: str
    line: int
    column: int


TOKEN_SPEC = [
    ("NUMBER", r"\d+(?:\.\d+)?"),
    ("STRING", r'"(?:\\.|[^"\\])*"'),
    ("KEYWORD", r"\b(?:let|if|else|while|return|true|false)\b"),
    ("IDENT", r"[A-Za-z_]\w*"),
    ("OP", r"==|!=|<=|>=|[+\-*/=<>]"),
    ("PUNCT", r"[(){};,]"),
    ("COMMENT", r"#[^\n]*"),
    ("NEWLINE", r"\n"),
    ("SKIP", r"[ \t]+"),
    ("MISMATCH", r"."),
]
MASTER = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))


def tokenize(source):
    line, line_start = 1, 0
    for match in MASTER.finditer(source):
        kind = match.lastgroup
        value = match.group()
        column = match.start() - line_start + 1
        if kind == "NEWLINE":
            line, line_start = line + 1, match.end()
            continue
        if kind in ("SKIP", "COMMENT"):
            continue
        if kind == "MISMATCH":
            raise SyntaxError(f"unexpected {value!r} at {line}:{column}")
        if kind == "NUMBER":
            value = float(value) if "." in value else int(value)
        elif kind == "STRING":
            value = value[1:-1].replace('\\"', '"')
        yield Token(kind, value, line, column)


SOURCE = '''\
let rate = 0.075;   # tax rate
let label = "Total \\"incl. tax\\"";
if (amount >= 100) {
    return amount * (1 + rate);
} else {
    return amount;
}
'''


def main():
    tokens = list(tokenize(SOURCE))
    for tok in tokens[:16]:
        print(f"  {tok.line}:{tok.column:<3} {tok.kind:<8} {tok.value!r}")
    print(f"  ... {len(tokens)} tokens total")
    kinds = {}
    for tok in tokens:
        kinds[tok.kind] = kinds.get(tok.kind, 0) + 1
    print("Token kinds:", dict(sorted(kinds.items())))
    idents = sorted({t.value for t in tokens if t.kind == "IDENT"})
    print("Identifiers:", idents)
    try:
        list(tokenize("let x = 5 @ 3;"))
    except SyntaxError as err:
        print("Error:", err)
    print("re.split on operators:", re.split(r"\s*([+\-*/])\s*", "12 + 7*x - 3 / y"))
    print("re.sub with function:", re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1 b22 c333"))


if __name__ == "__main__":
    main()
