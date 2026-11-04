"""A connection pool that uses context managers to guarantee resources are returned."""
from contextlib import contextmanager


class PoolExhausted(Exception):
    pass


class Pool:
    def __init__(self, size):
        self.free = [f"conn-{i}" for i in range(size)]
        self.in_use = set()
        self.events = []

    @contextmanager
    def connection(self):
        if not self.free:
            raise PoolExhausted(f"all {len(self.in_use)} connections busy")
        conn = self.free.pop(0)
        self.in_use.add(conn)
        self.events.append(f"acquire {conn}")
        try:
            yield conn
        except Exception as exc:
            self.events.append(f"error on {conn}: {exc}")
            raise
        finally:
            self.in_use.discard(conn)
            self.free.append(conn)
            self.events.append(f"release {conn}")

    def status(self):
        return f"free={sorted(self.free)} busy={sorted(self.in_use)}"


pool = Pool(2)
with pool.connection() as a:
    print("using", a, "|", pool.status())
    with pool.connection() as b:
        print("using", b, "|", pool.status())
        try:
            with pool.connection():
                pass
        except PoolExhausted as exc:
            print("exhausted:", exc)
print("after nested use:", pool.status())

try:
    with pool.connection() as c:
        raise ConnectionResetError("peer reset")
except ConnectionResetError as exc:
    print("query failed:", exc)
print("after failure:", pool.status())
print("event log:")
for e in pool.events:
    print("  ", e)
