"""Writing context managers as classes with __enter__ and __exit__."""


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc, tb):
        self.level -= 1
        return False

    def print(self, text):
        print("    " * self.level + text)


class Transaction:
    def __init__(self, store):
        self.store = store

    def __enter__(self):
        self.snapshot = dict(self.store)
        print("  begin transaction")
        return self.store

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            print("  commit")
        else:
            self.store.clear()
            self.store.update(self.snapshot)
            print(f"  rollback due to {exc_type.__name__}: {exc}")
        return exc_type is ValueError  # swallow ValueError only


with Indenter() as ind:
    ind.print("level one")
    with ind:
        ind.print("level two")
        with ind:
            ind.print("level three")
    ind.print("back to one")

db = {"balance": 100}
with Transaction(db) as data:
    data["balance"] -= 30
print("after commit:", db)

with Transaction(db) as data:
    data["balance"] -= 500
    if data["balance"] < 0:
        raise ValueError("negative balance")
print("after rollback:", db)

try:
    with Transaction(db) as data:
        data["owner"] = "x"
        raise KeyError("boom")
except KeyError as exc:
    print("KeyError propagated:", exc, "| db:", db)
