"""Handling several exception types with separate clauses, tuples, and ordering."""
import json


def load_config(text):
    try:
        config = json.loads(text)
        port = int(config["port"])
        ratio = config["workers"] / config["cpus"]
        return f"port={port} ratio={ratio:.2f}"
    except json.JSONDecodeError as exc:
        return f"invalid JSON at column {exc.colno}"
    except KeyError as exc:
        return f"missing setting {exc}"
    except (ValueError, TypeError) as exc:
        return f"bad value ({type(exc).__name__}): {exc}"
    except ZeroDivisionError:
        return "cpus must not be zero"


samples = [
    '{"port": "8080", "workers": 8, "cpus": 4}',
    '{"port": 80, "workers": 4}',
    '{"port": "eighty", "workers": 4, "cpus": 2}',
    '{"port": 80, "workers": "4", "cpus": 2}',
    '{"port": 80, "workers": 4, "cpus": 0}',
    '{port: 80}',
]
for s in samples:
    print(f"{s:<45} -> {load_config(s)}")


def classify(exc):
    try:
        raise exc
    except LookupError:
        return "LookupError family"
    except ArithmeticError:
        return "ArithmeticError family"
    except Exception:
        return "some other Exception"


for e in [KeyError("k"), IndexError(0), ZeroDivisionError(), OverflowError(), RuntimeError()]:
    print(f"{type(e).__name__:<18} caught as {classify(e)}")
