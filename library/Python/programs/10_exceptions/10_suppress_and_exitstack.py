"""contextlib helpers: suppress, ExitStack, nullcontext, and closing."""
from contextlib import suppress, ExitStack, nullcontext, closing


class Resource:
    def __init__(self, name, log):
        self.name, self.log = name, log

    def __enter__(self):
        self.log.append(f"open {self.name}")
        return self

    def __exit__(self, *exc_info):
        self.log.append(f"close {self.name}")


class Connection:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True


cache = {"a": 1}
with suppress(KeyError):
    del cache["missing"]
print("suppress KeyError: still running, cache =", cache)

values = ["1", "x", "3", None, "5"]
total = 0
for v in values:
    with suppress(ValueError, TypeError):
        total += int(v)
print("sum of parseable values:", total)

log = []
with ExitStack() as stack:
    resources = [stack.enter_context(Resource(n, log)) for n in ("db", "cache", "queue")]
    stack.callback(log.append, "callback ran")
    log.append(f"working with {len(resources)} resources")
print("ExitStack order:", log)


def maybe_lock(use_lock, log):
    return Resource("lock", log) if use_lock else nullcontext("no-lock")


for flag in (True, False):
    log = []
    with maybe_lock(flag, log) as handle:
        name = handle.name if flag else handle
    print(f"use_lock={flag}: handle={name}, log={log}")

conn = Connection()
with closing(conn) as c:
    print("inside closing, closed =", c.closed)
print("after closing, closed =", conn.closed)
