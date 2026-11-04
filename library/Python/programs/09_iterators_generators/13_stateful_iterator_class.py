"""A peekable iterator wrapper class with lookahead and push-back support."""


class Peekable:
    _SENTINEL = object()

    def __init__(self, iterable):
        self._it = iter(iterable)
        self._buffer = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._buffer:
            return self._buffer.pop()
        return next(self._it)

    def peek(self, default=_SENTINEL):
        if not self._buffer:
            try:
                self._buffer.append(next(self._it))
            except StopIteration:
                if default is self._SENTINEL:
                    raise
                return default
        return self._buffer[-1]

    def push_back(self, item):
        self._buffer.append(item)

    def __bool__(self):
        return self.peek(None) is not None


def tokenize(expr):
    tokens = Peekable(expr.replace(" ", ""))
    out = []
    while tokens:
        ch = next(tokens)
        if ch.isdigit():
            digits = ch
            while tokens.peek("").isdigit():
                digits += next(tokens)
            out.append(int(digits))
        else:
            out.append(ch)
    return out


p = Peekable([10, 20, 30])
print("peek:", p.peek(), "| next:", next(p), "| peek:", p.peek(), "| next:", next(p))
p.push_back(15)
print("after push_back:", list(p))
print("peek on empty with default:", p.peek("empty"))
print("tokens:", tokenize("12 + 345*(6 - 78)"))
print("tokens:", tokenize("1+2+3"))
