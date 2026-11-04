"""contextlib decorators: @contextmanager generators and ContextDecorator classes used as decorators."""
from contextlib import ContextDecorator, contextmanager, suppress

log = []


@contextmanager
def tag(name):
    log.append(f"<{name}>")
    try:
        yield name.upper()
    finally:
        log.append(f"</{name}>")


@contextmanager
def transaction(store):
    snapshot = dict(store)
    try:
        yield store
        print("  commit:", store)
    except Exception as exc:
        store.clear()
        store.update(snapshot)
        print(f"  rollback after {type(exc).__name__}: {store}")


class indented(ContextDecorator):
    level = 0

    def __enter__(self):
        indented.level += 1
        return self

    def __exit__(self, *exc):
        indented.level -= 1
        return False


def say(text):
    print("  " * indented.level + text)


with tag("html"):
    with tag("body") as upper:
        log.append(f"content in {upper}")
print("tags:", "".join(log))

accounts = {"ann": 100, "bob": 50}
with transaction(accounts) as acc:
    acc["ann"] -= 30
    acc["bob"] += 30
with transaction(accounts) as acc:
    acc["ann"] -= 500
    if acc["ann"] < 0:
        raise ValueError("overdrawn")
print("final accounts:", accounts)


@indented()
def section(title, items):
    say(title)
    for item in items:
        with indented():
            say(f"- {item}")


say("Report")
section("Fruits", ["apple", "pear"])
section("Tools", ["hammer"])
say("End (level back to %d)" % indented.level)

with suppress(KeyError, IndexError):
    print("before error")
    [][1]
    print("never printed")
print("suppress swallowed the IndexError")
