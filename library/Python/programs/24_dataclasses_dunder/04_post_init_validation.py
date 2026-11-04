"""__post_init__ for validation, normalization and derived fields, including InitVar parameters."""
import re
from dataclasses import InitVar, dataclass, field


@dataclass
class Email:
    address: str

    def __post_init__(self):
        self.address = self.address.strip().lower()
        if not re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", self.address):
            raise ValueError(f"invalid email: {self.address!r}")

    @property
    def domain(self):
        return self.address.split("@", 1)[1]


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)
    perimeter: float = field(init=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("dimensions must be positive")
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


@dataclass
class User:
    username: str
    password: InitVar[str]
    password_score: int = field(init=False)
    roles: tuple = ("user",)

    def __post_init__(self, password):
        checks = [len(password) >= 8, re.search(r"\d", password), re.search(r"[A-Z]", password),
                  re.search(r"[^\w]", password)]
        self.password_score = sum(bool(c) for c in checks)
        self.username = self.username.lower()


for raw in ["  Ann.Smith@Example.COM ", "bob@mail", "eve+news@sub.domain.org"]:
    try:
        e = Email(raw)
        print(f"ok   {e.address:<25} domain={e.domain}")
    except ValueError as exc:
        print("fail", exc)

r = Rectangle(3, 4.5)
print(r)
try:
    Rectangle(-1, 2)
except ValueError as exc:
    print("rectangle error:", exc)

for name, pw in [("Admin", "hunter2"), ("Carol", "Tr0ub4dor&3"), ("DAVE", "password")]:
    u = User(name, pw)
    print(u, "| has password attr:", hasattr(u, "password"))
