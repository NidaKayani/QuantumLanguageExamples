"""Nested dataclasses converted with asdict/astuple, serialized to JSON and rebuilt."""
import json
from dataclasses import asdict, astuple, dataclass, field
from typing import Optional


@dataclass
class Address:
    street: str
    city: str
    postcode: str


@dataclass
class Person:
    name: str
    age: int
    address: Address
    phones: list[str] = field(default_factory=list)
    manager: Optional["Person"] = None

    @classmethod
    def from_dict(cls, data):
        data = dict(data)
        data["address"] = Address(**data["address"])
        if data.get("manager"):
            data["manager"] = cls.from_dict(data["manager"])
        return cls(**data)


boss = Person("Grace", 52, Address("1 Main St", "Springfield", "11111"), ["555-0100"])
emp = Person("Alan", 29, Address("9 Elm Rd", "Shelbyville", "22222"), ["555-0199", "555-0142"], boss)

as_dict = asdict(emp)
print("asdict keys:", list(as_dict))
print("nested address dict:", as_dict["address"])
print("manager name via dict:", as_dict["manager"]["name"])
print("astuple(address):", astuple(emp.address))

text = json.dumps(as_dict, indent=2, sort_keys=True)
print("JSON lines:", len(text.splitlines()))
print(text[:180])

rebuilt = Person.from_dict(json.loads(text))
print("round trip equal:", rebuilt == emp)
print("rebuilt manager type:", type(rebuilt.manager).__name__, "| city:", rebuilt.manager.address.city)

as_dict["phones"].append("000")
print("asdict makes deep copies:", emp.phones)

compact = json.dumps(asdict(boss), separators=(",", ":"))
print("compact JSON:", compact)

flat = {f"address_{k}" if k in asdict(emp.address) else k: v
        for k, v in {**asdict(emp), **asdict(emp.address)}.items() if k not in ("address", "manager")}
print("flattened row:", flat)
