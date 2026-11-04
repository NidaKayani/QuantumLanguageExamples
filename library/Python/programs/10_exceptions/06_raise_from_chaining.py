"""Explicit exception chaining with raise ... from, and suppressing context with from None."""


class DataLoadError(Exception):
    pass


RECORDS = {"u1": "Ann,31", "u2": "Bob,abc", "u3": "Cid"}


def load_user(uid):
    try:
        raw = RECORDS[uid]
        name, age = raw.split(",")
        return name, int(age)
    except KeyError as exc:
        raise DataLoadError(f"no record for {uid}") from None
    except ValueError as exc:
        raise DataLoadError(f"corrupt record for {uid}") from exc


def describe(exc):
    parts = [f"{type(exc).__name__}: {exc}"]
    if exc.__cause__ is not None:
        parts.append(f"caused by {type(exc.__cause__).__name__}: {exc.__cause__}")
    elif exc.__context__ is not None and not exc.__suppress_context__:
        parts.append(f"during handling of {type(exc.__context__).__name__}")
    parts.append(f"suppress_context={exc.__suppress_context__}")
    return " | ".join(parts)


for uid in ["u1", "u2", "u3", "u9"]:
    try:
        print(uid, "->", load_user(uid))
    except DataLoadError as err:
        print(uid, "->", describe(err))

try:
    try:
        {}["missing"]
    except KeyError:
        raise RuntimeError("implicit chaining")
except RuntimeError as err:
    print(describe(err))
    print("context type:", type(err.__context__).__name__, "| cause:", err.__cause__)
