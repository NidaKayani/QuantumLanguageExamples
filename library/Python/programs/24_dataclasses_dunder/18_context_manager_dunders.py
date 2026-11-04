"""Context managers via __enter__/__exit__: transactions, temporary state and exception handling."""


class Transaction:
    def __init__(self, ledger):
        self.ledger = ledger
        self.pending = []

    def __enter__(self):
        print("  begin transaction")
        return self

    def record(self, account, amount):
        self.pending.append((account, amount))

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None and sum(a for _, a in self.pending) == 0:
            for account, amount in self.pending:
                self.ledger[account] = self.ledger.get(account, 0) + amount
            print(f"  committed {len(self.pending)} entries")
            return False
        reason = exc_type.__name__ if exc_type else "unbalanced"
        print(f"  rolled back ({reason})")
        return exc_type is ValueError  # swallow ValueError only


class Indent:
    level = 0

    def __init__(self, label):
        self.label = label

    def __enter__(self):
        print("  " * Indent.level + f"<{self.label}>")
        Indent.level += 1
        return self

    def __exit__(self, *exc_info):
        Indent.level -= 1
        print("  " * Indent.level + f"</{self.label}>")


class Override:
    """Temporarily set attributes on an object, restoring them afterwards."""

    def __init__(self, target, **changes):
        self.target, self.changes, self.saved = target, changes, {}

    def __enter__(self):
        for k, v in self.changes.items():
            self.saved[k] = getattr(self.target, k)
            setattr(self.target, k, v)
        return self.target

    def __exit__(self, *exc_info):
        for k, v in self.saved.items():
            setattr(self.target, k, v)


ledger = {"cash": 100}
print("transfer 1:")
with Transaction(ledger) as tx:
    tx.record("cash", -40)
    tx.record("savings", 40)
print("transfer 2:")
with Transaction(ledger) as tx:
    tx.record("cash", -10)
print("transfer 3:")
with Transaction(ledger) as tx:
    tx.record("cash", -5)
    tx.record("fees", 5)
    raise ValueError("card declined")
print("transfer 4:")
try:
    with Transaction(ledger) as tx:
        tx.record("cash", 1)
        raise KeyError("audit")
except KeyError as exc:
    print("  propagated KeyError", exc)
print("ledger:", ledger)

with Indent("html"):
    with Indent("body"), Indent("p"):
        print("  " * Indent.level + "hello")


class Settings:
    debug = False
    retries = 3


with Override(Settings, debug=True, retries=0) as s:
    print("inside:", s.debug, s.retries)
print("restored:", Settings.debug, Settings.retries)
