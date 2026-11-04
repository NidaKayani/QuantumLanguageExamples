"""Rich comparisons with __lt__ and friends, completed by functools.total_ordering."""
from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, text):
        self.parts = tuple(int(p) for p in text.split("."))

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key() == other._key()

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._key() < other._key()

    def _key(self):
        parts = list(self.parts)
        while parts and parts[-1] == 0:
            parts.pop()
        return tuple(parts)

    def __repr__(self):
        return "v" + ".".join(map(str, self.parts))


class Task:
    def __init__(self, priority, name):
        self.priority, self.name = priority, name

    def __lt__(self, other):
        return (self.priority, self.name) < (other.priority, other.name)

    def __repr__(self):
        return f"Task({self.priority}, {self.name!r})"


versions = [Version(v) for v in ["1.10", "1.2", "1.2.1", "0.9.9", "1.2.0", "2.0"]]
print("sorted:", sorted(versions))
print("max:", max(versions), "min:", min(versions))
print("1.2 == 1.2.0:", Version("1.2") == Version("1.2.0"))
print("1.10 > 1.9:", Version("1.10") > Version("1.9"))
print("1.2 >= 1.2.0:", Version("1.2") >= Version("1.2.0"))
print("2.0 <= 1.99:", Version("2.0") <= Version("1.99"))
try:
    Version("1.0") < "1.0"
except TypeError:
    print("cannot compare Version with str")

tasks = [Task(2, "write"), Task(1, "plan"), Task(2, "test"), Task(3, "ship")]
print("tasks:", sorted(tasks))
print("reflected >:", Task(5, "x") > Task(1, "y"))
