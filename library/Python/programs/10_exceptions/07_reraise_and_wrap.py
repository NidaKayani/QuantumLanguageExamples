"""Re-raising exceptions with bare raise after logging, and wrapping at layer boundaries."""

audit_log = []


def parse_amount(text):
    try:
        return float(text)
    except ValueError:
        audit_log.append(f"parse failure: {text!r}")
        raise


class TransferError(Exception):
    pass


def transfer(accounts, src, dst, amount_text):
    try:
        amount = parse_amount(amount_text)
        if accounts[src] < amount:
            raise TransferError(f"{src} has insufficient funds")
        accounts[src] -= amount
        accounts[dst] += amount
    except KeyError as exc:
        raise TransferError(f"unknown account {exc}") from exc
    except ValueError as exc:
        raise TransferError(f"bad amount {amount_text!r}") from exc


accounts = {"alice": 100.0, "bob": 50.0}
for src, dst, amt in [("alice", "bob", "30"), ("bob", "carol", "10"),
                      ("alice", "bob", "ten"), ("bob", "alice", "500"),
                      ("bob", "alice", "80")]:
    try:
        transfer(accounts, src, dst, amt)
        print(f"ok: {src} -> {dst} {amt}")
    except TransferError as exc:
        cause = type(exc.__cause__).__name__ if exc.__cause__ else "-"
        print(f"failed: {exc} (cause: {cause})")

print("balances:", accounts)
print("audit log:", audit_log)

try:
    parse_amount("1,000")
except ValueError as exc:
    print("re-raised original:", type(exc).__name__, "-", exc)
