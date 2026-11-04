"""Class attributes versus instance attributes, shared counters, and shadowing."""


class Robot:
    population = 0
    default_speed = 5
    registry = []

    def __init__(self, name, speed=None):
        self.name = name
        if speed is not None:
            self.default_speed = speed  # shadows the class attribute
        Robot.population += 1
        Robot.registry.append(name)
        self.serial = f"RB-{Robot.population:03d}"

    def retire(self):
        Robot.population -= 1
        Robot.registry.remove(self.name)

    @classmethod
    def census(cls):
        return f"{cls.population} robots: {', '.join(cls.registry)}"


r1 = Robot("Ada")
r2 = Robot("Bolt", speed=12)
r3 = Robot("Cog")
print(Robot.census())
print("serials:", r1.serial, r2.serial, r3.serial)
print("speeds:", r1.default_speed, r2.default_speed, r3.default_speed)
print("r2 has own speed:", "default_speed" in vars(r2), "| r1:", "default_speed" in vars(r1))

Robot.default_speed = 7
print("after class change:", r1.default_speed, r2.default_speed, r3.default_speed)

r2.retire()
print(Robot.census())

r1.population = 99
print("instance shadow:", r1.population, "class value:", Robot.population)
del r1.population
print("after del, r1 sees:", r1.population)
print("class dict keys:", sorted(k for k in vars(Robot) if not k.startswith("__")))
