"""Cooperative multiple inheritance where every __init__ passes **kwargs along super()."""


class Component:
    def __init__(self, **kwargs):
        if kwargs:
            raise TypeError(f"unexpected arguments: {sorted(kwargs)}")
        self.parts = []


class Named(Component):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.parts.append("Named")


class Positioned(Component):
    def __init__(self, x=0, y=0, **kwargs):
        super().__init__(**kwargs)
        self.x, self.y = x, y
        self.parts.append("Positioned")


class Colored(Component):
    def __init__(self, color="black", **kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.parts.append("Colored")


class Sprite(Named, Positioned, Colored):
    def __init__(self, speed=1, **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.parts.append("Sprite")

    def __repr__(self):
        return (f"Sprite({self.name!r}, at=({self.x},{self.y}), "
                f"color={self.color!r}, speed={self.speed})")


hero = Sprite(name="hero", x=10, y=5, color="red", speed=3)
ghost = Sprite(name="ghost")
print(hero)
print(ghost)
print("init order (innermost first):", hero.parts)
print("MRO:", [c.__name__ for c in Sprite.__mro__])
try:
    Sprite(name="bad", size=9)
except TypeError as exc:
    print("TypeError:", exc)
