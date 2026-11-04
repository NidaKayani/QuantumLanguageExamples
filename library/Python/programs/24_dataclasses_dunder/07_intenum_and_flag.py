"""IntEnum for ordered integer constants and Flag for combinable permission bits."""
from enum import Flag, IntEnum, auto


class Level(IntEnum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


class Perm(Flag):
    NONE = 0
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    DELETE = auto()
    READ_WRITE = READ | WRITE
    ALL = READ | WRITE | EXECUTE | DELETE


messages = [(Level.INFO, "server started"), (Level.DEBUG, "cache miss"), (Level.ERROR, "db timeout"),
            (Level.WARNING, "slow request"), (Level.CRITICAL, "disk failure")]

threshold = Level.WARNING
print(f"messages at or above {threshold.name}:")
for level, text in messages:
    if level >= threshold:
        print(f"  [{level.name:<8}] ({int(level)}) {text}")

print("IntEnum arithmetic:", Level.ERROR + 5, Level.INFO * 2, Level.DEBUG < 15)
print("sorted levels:", [l.name for l in sorted(Level, reverse=True)])
print("from int:", Level(30).name, "| max:", max(messages)[0].name)

acl = {
    "alice": Perm.ALL,
    "bob": Perm.READ_WRITE,
    "carol": Perm.READ | Perm.EXECUTE,
    "guest": Perm.READ,
    "nobody": Perm.NONE,
}


def describe(p):
    return "|".join(m.name for m in Perm if m in p and m.name in {"READ", "WRITE", "EXECUTE", "DELETE"}) or "-"


for user, perms in acl.items():
    print(f"{user:<7} {describe(perms):<28} write={bool(perms & Perm.WRITE)} value={perms.value}")

bob = acl["bob"]
bob |= Perm.DELETE
print("bob gains delete:", describe(bob))
bob &= ~Perm.WRITE
print("bob loses write:", describe(bob))
print("carol can rw?", Perm.READ_WRITE in acl["carol"], "| alice can rw?", Perm.READ_WRITE in acl["alice"])
print("users with execute:", [u for u, p in acl.items() if Perm.EXECUTE in p])
print("combined of guest and carol:", describe(acl["guest"] | acl["carol"]))
