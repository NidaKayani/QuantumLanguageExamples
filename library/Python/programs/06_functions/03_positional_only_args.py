"""Positional-only parameters using the slash marker, mixed with other kinds."""


def clamp(value, low, high, /):
    return max(low, min(value, high))


def describe(a, b, /, c, d=4, *, e, f=6):
    return f"a={a} b={b} c={c} d={d} e={e} f={f}"


def build(name, /, **options):
    # 'name' may also appear in options because the parameter is positional-only
    opts = ", ".join(f"{k}={v}" for k, v in sorted(options.items()))
    return f"{name}: {opts}"


print(clamp(15, 0, 10))
print(clamp(-3, 0, 10))
print(clamp(7, 0, 10))

try:
    clamp(value=5, low=0, high=10)
except TypeError as exc:
    print("TypeError:", exc)

print(describe(1, 2, 3, e=5))
print(describe(1, 2, c=30, d=40, e=50, f=60))
print(build("widget", color="red", size=3))
print(build("gadget", name="shadow", weight=1.5))

code = describe.__code__
print("posonly:", code.co_posonlyargcount,
      "args:", code.co_argcount,
      "kwonly:", code.co_kwonlyargcount)
