"""Custom exception classes carrying extra data and custom messages."""


class ValidationError(Exception):
    def __init__(self, field, value, reason):
        self.field = field
        self.value = value
        self.reason = reason
        super().__init__(f"{field}={value!r}: {reason}")


class InsufficientStock(Exception):
    def __init__(self, item, requested, available):
        super().__init__(item, requested, available)
        self.item, self.requested, self.available = item, requested, available

    def __str__(self):
        return f"wanted {self.requested} x {self.item}, only {self.available} left"


def validate_user(user):
    if not user.get("name"):
        raise ValidationError("name", user.get("name"), "must not be empty")
    if not 0 < user.get("age", 0) < 150:
        raise ValidationError("age", user.get("age"), "must be between 1 and 149")
    if "@" not in user.get("email", ""):
        raise ValidationError("email", user.get("email"), "must contain @")
    return True


users = [
    {"name": "Ann", "age": 30, "email": "ann@example.org"},
    {"name": "", "age": 30, "email": "x@y"},
    {"name": "Bob", "age": 200, "email": "bob@example.org"},
    {"name": "Cid", "age": 41, "email": "cid.example.org"},
]
for u in users:
    try:
        validate_user(u)
        print("valid:", u["name"])
    except ValidationError as err:
        print(f"invalid: {err} (field={err.field})")

stock = {"widget": 5}
try:
    if stock["widget"] < 8:
        raise InsufficientStock("widget", 8, stock["widget"])
except InsufficientStock as err:
    print("error:", err)
    print("args:", err.args, "| shortfall:", err.requested - err.available)
print("is Exception subclass:", issubclass(ValidationError, Exception))
