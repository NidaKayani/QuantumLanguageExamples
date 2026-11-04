"""Inspecting exception objects: args, str/repr, notes added with add_note, and related attributes."""


class HttpError(Exception):
    def __init__(self, status, message):
        super().__init__(status, message)
        self.status = status

    def __str__(self):
        return f"HTTP {self.status}: {self.args[1]}"


errors = [
    ValueError("invalid literal"),
    KeyError("user_id"),
    OSError(2, "No such file or directory"),
    HttpError(404, "Not Found"),
    ZeroDivisionError("division by zero"),
    Exception(),
]
for err in errors:
    print(f"{type(err).__name__:<18} args={err.args!r:<40} str={str(err)!r}")

print("repr:", repr(errors[0]), repr(errors[3]))
print("OSError errno/strerror:", errors[2].errno, errors[2].strerror)

try:
    try:
        int("12a")
    except ValueError as exc:
        exc.add_note("while parsing field 'quantity'")
        exc.add_note("record #17")
        raise
except ValueError as exc:
    print("message:", exc)
    for note in exc.__notes__:
        print("  note:", note)

try:
    [].pop()
except IndexError as exc:
    print("caught:", type(exc).__name__, "| message:", exc)
    print("traceback object present:", exc.__traceback__ is not None)
print("exception variable is cleared after except:", "exc" not in dir())
