"""Maybe and Result containers for chaining computations that can fail, without exceptions."""
from dataclasses import dataclass
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T

    def bind(self, f: Callable[[T], "Result"]) -> "Result":
        return f(self.value)

    def map(self, f):
        return Ok(f(self.value))

    def unwrap_or(self, default):
        return self.value


@dataclass(frozen=True)
class Err:
    error: str

    def bind(self, f):
        return self

    def map(self, f):
        return self

    def unwrap_or(self, default):
        return default


Result = Ok | Err


def parse_int(text: str) -> Result:
    text = text.strip()
    return Ok(int(text)) if text.lstrip("-").isdigit() else Err(f"not an integer: {text!r}")


def non_zero(n: int) -> Result:
    return Ok(n) if n != 0 else Err("division by zero")


def safe_reciprocal(text: str) -> Result:
    return parse_int(text).bind(non_zero).map(lambda n: 1 / n)


for raw in ["4", " -8 ", "0", "abc", "250"]:
    result = safe_reciprocal(raw)
    match result:
        case Ok(value):
            print(f"{raw!r:>8} -> Ok({value})")
        case Err(error):
            print(f"{raw!r:>8} -> Err({error})")


def lookup(mapping, *keys):
    result: Result = Ok(mapping)
    for key in keys:
        result = result.bind(lambda m, k=key: Ok(m[k]) if isinstance(m, dict) and k in m
                             else Err(f"missing key {k!r}"))
    return result


config = {"db": {"host": "db.local", "ports": {"primary": 5432}}}
print(lookup(config, "db", "ports", "primary"))
print(lookup(config, "db", "user", "name"))
print("host or default:", lookup(config, "db", "host").unwrap_or("localhost"))
print("user or default:", lookup(config, "db", "user").unwrap_or("guest"))


def sequence(results):
    values = []
    for r in results:
        if isinstance(r, Err):
            return r
        values.append(r.value)
    return Ok(values)


print("all parse:", sequence(map(parse_int, "1 2 3 4".split())))
print("one fails:", sequence(map(parse_int, "1 two 3".split())))
