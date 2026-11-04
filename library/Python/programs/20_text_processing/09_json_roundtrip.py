"""JSON round trips: dumps/loads options, custom encoders for dataclasses and Decimals, object hooks."""
import json
from dataclasses import dataclass, asdict, field
from decimal import Decimal
from enum import Enum


class Status(Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"


@dataclass
class Account:
    owner: str
    balance: Decimal
    status: Status
    tags: list = field(default_factory=list)


class AppEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return {"__decimal__": str(obj)}
        if isinstance(obj, Enum):
            return {"__enum__": f"{type(obj).__name__}.{obj.name}"}
        if isinstance(obj, Account):
            return {"__account__": asdict(obj)}
        if isinstance(obj, (set, frozenset)):
            return sorted(obj)
        return super().default(obj)


def decode_hook(d):
    if "__decimal__" in d:
        return Decimal(d["__decimal__"])
    if "__enum__" in d:
        _, name = d["__enum__"].split(".")
        return Status[name]
    if "__account__" in d:
        return Account(**d["__account__"])
    return d


def main():
    config = {"name": "quantum", "version": [2, 4, 1], "debug": False, "ratio": 0.75,
              "nested": {"empty": None, "unicode": "caf\u00e9"}}
    compact = json.dumps(config, separators=(",", ":"))
    print("Compact:", compact)
    print("ASCII-escaped length:", len(compact), "| raw UTF-8 length:",
          len(json.dumps(config, ensure_ascii=False, separators=(",", ":")).encode()))
    print("Pretty, sorted:")
    print(json.dumps(config, indent=2, sort_keys=True))
    assert json.loads(compact) == config
    accounts = [Account("ana", Decimal("1024.50"), Status.ACTIVE, ["vip"]),
                Account("bo", Decimal("-3.10"), Status.SUSPENDED)]
    payload = json.dumps({"accounts": accounts, "regions": {"eu", "us", "apac"}}, cls=AppEncoder)
    print("Encoded payload:", payload)
    restored = json.loads(payload, object_hook=decode_hook)
    for acct in restored["accounts"]:
        print(f"  {acct.owner}: {acct.balance} ({type(acct.balance).__name__}) {acct.status}")
    print("Round trip equal:", restored["accounts"] == accounts)
    print("Parse floats as Decimal:", json.loads("[0.1, 0.2]", parse_float=Decimal))
    try:
        json.loads('{"broken": [1, 2,}')
    except json.JSONDecodeError as exc:
        print(f"JSONDecodeError: {exc.msg} at line {exc.lineno} col {exc.colno}")


if __name__ == "__main__":
    main()
