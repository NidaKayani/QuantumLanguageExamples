"""Generator-based context managers built with contextlib.contextmanager."""
from contextlib import contextmanager


@contextmanager
def tag(name, out):
    out.append(f"<{name}>")
    try:
        yield
    finally:
        out.append(f"</{name}>")


@contextmanager
def temporary_setting(config, key, value):
    missing = object()
    old = config.get(key, missing)
    config[key] = value
    try:
        yield config
    finally:
        if old is missing:
            del config[key]
        else:
            config[key] = old


@contextmanager
def error_collector():
    errors = []
    try:
        yield errors
    except Exception as exc:
        errors.append(f"{type(exc).__name__}: {exc}")
    print(f"  collected {len(errors)} error(s): {errors}")


html = []
with tag("html", html):
    with tag("body", html):
        with tag("p", html):
            html.append("Hello")
print("".join(html))

config = {"debug": False, "level": 1}
with temporary_setting(config, "debug", True) as cfg:
    print("inside:", cfg)
with temporary_setting(config, "trace", "on"):
    print("inside:", config)
print("restored:", config)

with error_collector() as errs:
    errs.append("manual warning")
    int("not a number")
    print("never printed")
print("execution continues after collector")

partial = []
try:
    with tag("div", partial):
        raise RuntimeError("render failed")
except RuntimeError as exc:
    print("error:", exc, "| output still closed:", partial)
