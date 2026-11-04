"""Duck typing versus inheritance: unrelated classes used through a shared protocol."""
from typing import Protocol, runtime_checkable


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...


class Circle:
    def __init__(self, r):
        self.r = r

    def draw(self):
        return f"circle(r={self.r})"


class Text:
    def __init__(self, content):
        self.content = content

    def draw(self):
        return f"text({self.content!r})"


class Group:
    def __init__(self, *items):
        self.items = items

    def draw(self):
        return "group[" + ", ".join(item.draw() for item in self.items) + "]"


class Sound:
    def play(self):
        return "beep"


def render(scene):
    out = []
    for obj in scene:
        try:
            out.append(obj.draw())
        except AttributeError:
            out.append(f"<cannot draw {type(obj).__name__}>")
    return out


scene = [Circle(2), Text("hello"), Group(Circle(1), Text("nested")), Sound()]
for line in render(scene):
    print(line)

print("protocol checks:", {type(o).__name__: isinstance(o, Drawable) for o in scene})
print("share a base class?", [type(o).__bases__[0].__name__ for o in scene])
drawables = [o for o in scene if hasattr(o, "draw")]
print("drawable count:", len(drawables))
