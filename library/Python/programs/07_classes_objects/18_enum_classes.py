"""Enumerations with enum.Enum, auto, IntEnum, Flag, and methods on members."""
from enum import Enum, IntEnum, Flag, auto


class Color(Enum):
    RED = "#ff0000"
    GREEN = "#00ff00"
    BLUE = "#0000ff"

    @property
    def rgb(self):
        h = self.value.lstrip("#")
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
    ALL = READ | WRITE | EXECUTE


class Planet(Enum):
    MERCURY = (3.303e23, 2.4397e6)
    EARTH = (5.976e24, 6.37814e6)

    def __init__(self, mass, radius):
        self.mass, self.radius = mass, radius

    @property
    def surface_gravity(self):
        return 6.673e-11 * self.mass / (self.radius ** 2)


for c in Color:
    print(f"{c.name:<5} {c.value} rgb={c.rgb}")
print("lookup by value:", Color("#00ff00"), "| by name:", Color["BLUE"].name)
print("repr:", repr(Color.RED))

tasks = [("deploy", Priority.HIGH), ("lint", Priority.LOW), ("review", Priority.MEDIUM)]
print("by priority:", [name for name, p in sorted(tasks, key=lambda t: t[1], reverse=True)])
print("IntEnum math:", Priority.HIGH + 1, Priority.LOW < Priority.MEDIUM)

perm = Permission.READ | Permission.WRITE
print("perm:", perm, "| can write:", Permission.WRITE in perm, "| can exec:", Permission.EXECUTE in perm)
print("ALL contains READ:", Permission.READ in Permission.ALL)
for planet in Planet:
    print(f"{planet.name}: gravity {planet.surface_gravity:.2f} m/s^2")
print("members:", list(Priority.__members__))
