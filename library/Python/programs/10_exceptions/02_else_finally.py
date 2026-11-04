"""The else and finally clauses of try statements and their execution order."""


def process(value):
    steps = []
    try:
        steps.append("try")
        result = 100 // value
    except ZeroDivisionError:
        steps.append("except")
        result = None
    else:
        steps.append("else")
        result += 1
    finally:
        steps.append("finally")
    return result, steps


def early_return(flag):
    try:
        if flag:
            return "returned from try"
        return "also from try"
    finally:
        print(f"  finally runs even on return (flag={flag})")


def finally_overrides():
    try:
        return "try value"
    finally:
        print("  finally executed before the function actually returns")


for v in [5, 0, 3]:
    result, steps = process(v)
    print(f"process({v}) -> {result}; path: {' -> '.join(steps)}")

print(early_return(True))
print(early_return(False))
print(finally_overrides())

attempts = 0
for attempt in range(1, 6):
    try:
        attempts += 1
        if attempt < 3:
            raise ConnectionError(f"attempt {attempt} failed")
    except ConnectionError as exc:
        print("  retrying:", exc)
        continue
    else:
        print(f"  succeeded on attempt {attempt}")
        break
    finally:
        print(f"  [attempt {attempt} done]")
print("total attempts:", attempts)
