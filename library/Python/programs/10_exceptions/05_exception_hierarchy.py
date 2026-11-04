"""Designing a custom exception hierarchy and catching at different levels."""


class AppError(Exception):
    """Base class for all application errors."""
    code = 1


class ConfigError(AppError):
    code = 10


class MissingSetting(ConfigError):
    code = 11


class InvalidSetting(ConfigError):
    code = 12


class NetworkError(AppError):
    code = 20


class Timeout(NetworkError):
    code = 21


def run(task):
    errors = {
        "missing": MissingSetting("DATABASE_URL not set"),
        "invalid": InvalidSetting("PORT must be numeric"),
        "timeout": Timeout("server did not respond in 30s"),
        "network": NetworkError("connection refused"),
        "generic": AppError("something went wrong"),
    }
    if task in errors:
        raise errors[task]
    return f"{task} ok"


for task in ["build", "missing", "invalid", "timeout", "network", "generic"]:
    try:
        print(run(task))
    except ConfigError as exc:
        print(f"[config  code={exc.code}] {type(exc).__name__}: {exc}")
    except NetworkError as exc:
        kind = "retryable" if isinstance(exc, Timeout) else "fatal"
        print(f"[network code={exc.code}] {type(exc).__name__} ({kind}): {exc}")
    except AppError as exc:
        print(f"[app     code={exc.code}] {exc}")

print("Timeout MRO:", " > ".join(c.__name__ for c in Timeout.__mro__[:-2]))
print("all AppError subclasses:", sorted(c.__name__ for c in AppError.__subclasses__()))
