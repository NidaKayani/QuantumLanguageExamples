"""Keyword-only parameters enforced with a bare star in the signature."""


def make_record(name, age, *, city="Unknown", active=True):
    status = "active" if active else "inactive"
    return f"{name} ({age}) from {city} [{status}]"


def sort_people(people, *, key, reverse=False):
    return sorted(people, key=key, reverse=reverse)


def connect(host, port, *, timeout=30, retries=3, secure):
    scheme = "https" if secure else "http"
    return f"{scheme}://{host}:{port} timeout={timeout} retries={retries}"


print(make_record("Alice", 30))
print(make_record("Bob", 25, city="Paris"))
print(make_record("Cara", 41, active=False, city="Oslo"))

try:
    make_record("Dan", 33, "Rome")
except TypeError as exc:
    print("TypeError:", exc)

people = [("Zoe", 22), ("Adam", 35), ("Mia", 29)]
print(sort_people(people, key=lambda p: p[1]))
print(sort_people(people, key=lambda p: p[0], reverse=True))

print(connect("example.org", 443, secure=True))
print(connect("localhost", 8080, secure=False, retries=5))
try:
    connect("localhost", 80)
except TypeError as exc:
    print("TypeError:", exc)

print("kwonly defaults:", connect.__kwdefaults__)
