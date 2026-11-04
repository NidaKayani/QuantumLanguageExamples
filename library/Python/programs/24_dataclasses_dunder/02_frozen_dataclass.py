"""Frozen dataclasses as hashable value objects, updated with dataclasses.replace."""
from dataclasses import FrozenInstanceError, dataclass, replace


@dataclass(frozen=True)
class Coord:
    lat: float
    lon: float

    def shifted(self, dlat=0.0, dlon=0.0):
        return replace(self, lat=round(self.lat + dlat, 4), lon=round(self.lon + dlon, 4))


@dataclass(frozen=True)
class Version:
    major: int
    minor: int = 0
    patch: int = 0

    @classmethod
    def parse(cls, text):
        return cls(*map(int, text.split(".")))

    def bump(self, part):
        if part == "major":
            return replace(self, major=self.major + 1, minor=0, patch=0)
        if part == "minor":
            return replace(self, minor=self.minor + 1, patch=0)
        return replace(self, patch=self.patch + 1)

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.patch}"


home = Coord(51.5074, -0.1278)
try:
    home.lat = 0
except FrozenInstanceError as exc:
    print("cannot assign:", exc)

moved = home.shifted(dlat=0.01)
print("original:", home)
print("moved   :", moved)

visits = {home: "London", Coord(48.8566, 2.3522): "Paris"}
print("lookup by equal value:", visits[Coord(51.5074, -0.1278)])
print("hash equal for equal values:", hash(home) == hash(Coord(51.5074, -0.1278)))
print("unique coords:", len({home, moved, Coord(51.5074, -0.1278)}))

v = Version.parse("1.4.2")
history = [v]
for part in ["patch", "minor", "patch", "major", "minor"]:
    history.append(history[-1].bump(part))
print("version history:", " -> ".join(map(str, history)))
print("repr:", repr(history[-1]))
print("first is untouched:", v)

try:
    replace(v, build=7)
except TypeError as exc:
    print("replace with unknown field:", type(exc).__name__)
