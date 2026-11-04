"""Chaining constructors with super() through a three-level hierarchy."""


class Vehicle:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year
        print(f"  Vehicle.__init__({make}, {model}, {year})")

    def info(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, doors=4):
        super().__init__(make, model, year)
        self.doors = doors
        print(f"  Car.__init__(doors={doors})")

    def info(self):
        return f"{super().info()}, {self.doors} doors"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_kwh, **kwargs):
        super().__init__(make, model, year, **kwargs)
        self.battery_kwh = battery_kwh
        print(f"  ElectricCar.__init__(battery={battery_kwh})")

    def info(self):
        return f"{super().info()}, {self.battery_kwh} kWh battery"

    def range_km(self, km_per_kwh=6.2):
        return round(self.battery_kwh * km_per_kwh)


print("Creating Vehicle:")
v = Vehicle("Ford", "Transit", 2019)
print("Creating Car:")
c = Car("Honda", "Civic", 2021, doors=2)
print("Creating ElectricCar:")
e = ElectricCar("Tesla", "Model 3", 2023, 75, doors=4)

for obj in (v, c, e):
    print(f"{type(obj).__name__:<12} {obj.info()}")
print("estimated range:", e.range_km(), "km")
print("explicit parent call:", Car.info(e))
print("attributes:", sorted(vars(e)))
