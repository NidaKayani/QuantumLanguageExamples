"""A retry decorator that catches selected exceptions and computes a backoff schedule."""
from functools import wraps


class TransientError(Exception):
    pass


class PermanentError(Exception):
    pass


def retry(times=3, on=(TransientError,), base_delay=0.1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            delays = []
            for attempt in range(1, times + 1):
                try:
                    result = func(*args, **kwargs)
                    return result, attempt, delays
                except on as exc:
                    if attempt == times:
                        raise RuntimeError(f"{func.__name__} failed after {times} attempts") from exc
                    delays.append(round(base_delay * 2 ** (attempt - 1), 3))
        return wrapper
    return decorator


def flaky_service(failures_before_success):
    state = {"calls": 0}

    @retry(times=4)
    def call():
        state["calls"] += 1
        if state["calls"] <= failures_before_success:
            raise TransientError(f"temporary failure #{state['calls']}")
        return "payload"
    return call


for failures in [0, 2, 3, 5]:
    service = flaky_service(failures)
    try:
        result, attempts, delays = service()
        print(f"failures={failures}: {result} after {attempts} attempt(s), waited {delays}")
    except RuntimeError as exc:
        print(f"failures={failures}: {exc}; last cause: {exc.__cause__}")


@retry(times=5)
def broken():
    raise PermanentError("disk is read-only")


try:
    broken()
except PermanentError as exc:
    print("not retried:", exc)
