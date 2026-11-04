"""Functions that build other functions: a tiny validation library using closures."""


def min_length(n):
    def check(value):
        return None if len(value) >= n else f"must be at least {n} characters"
    return check


def max_length(n):
    def check(value):
        return None if len(value) <= n else f"must be at most {n} characters"
    return check


def contains_any(chars, label):
    def check(value):
        return None if any(c in chars for c in value) else f"must contain a {label}"
    return check


def all_of(*checks):
    def check(value):
        errors = [msg for c in checks if (msg := c(value)) is not None]
        return errors or None
    return check


password_rules = all_of(
    min_length(8),
    max_length(20),
    contains_any("0123456789", "digit"),
    contains_any("!@#$%^&*", "symbol"),
    contains_any("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "capital letter"),
)

username_rules = all_of(min_length(3), max_length(12))

for pw in ["short", "longenoughpassword", "Str0ng!Pass", "x" * 25 + "A1!"]:
    errors = password_rules(pw)
    status = "OK" if errors is None else "; ".join(errors)
    print(f"password {pw[:12]!r:<16} {status}")

for name in ["al", "nida", "averyverylongusername"]:
    print(f"username {name!r}: {username_rules(name) or 'OK'}")
