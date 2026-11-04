"""Serialize dictionaries to JSON strings and parse them back."""

import json

config = {
    "name": "demo-service",
    "version": 3,
    "enabled": True,
    "threshold": 0.75,
    "tags": ["web", "api"],
    "owner": None,
    "limits": {"cpu": 2, "memory_mb": 512},
}

compact = json.dumps(config)
print("compact:", compact)

pretty = json.dumps(config, indent=2, sort_keys=True)
print("pretty:")
print(pretty)

restored = json.loads(compact)
print("round trip equal:", restored == config)
print("types:", {k: type(v).__name__ for k, v in restored.items()})

# tuples become lists, int keys become strings
tricky = {1: (1, 2), "nested": {2: "two"}}
back = json.loads(json.dumps(tricky))
print("tricky round trip:", back, "| equal:", back == tricky)

print("separators:", json.dumps({"a": 1, "b": [1, 2]}, separators=(",", ":")))
print("non-ascii escaped:", json.dumps({"city": "São Paulo"}))

payload = '{"users": [{"id": 1, "name": "Ann", "admin": false}, {"id": 2, "name": "Bo", "admin": true}]}'
data = json.loads(payload)
admins = [u["name"] for u in data["users"] if u["admin"]]
print("admins:", admins)

try:
    json.loads("{'single': 'quotes'}")
except json.JSONDecodeError as e:
    print("decode error:", e.msg, "at pos", e.pos)


def encode_default(obj):
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(f"cannot serialize {type(obj).__name__}")


print("custom default:", json.dumps({"ids": {3, 1, 2}}, default=encode_default))
