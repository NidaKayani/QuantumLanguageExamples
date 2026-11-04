"""Tracing the exact order of try/except/else/finally across nested calls and exceptions."""

trace = []


def level3(mode):
    try:
        trace.append("L3 try")
        if mode == "inner":
            raise ValueError("inner failure")
    finally:
        trace.append("L3 finally")


def level2(mode):
    try:
        trace.append("L2 try")
        level3(mode)
        if mode == "middle":
            raise KeyError("middle failure")
    except ValueError:
        trace.append("L2 handled ValueError")
        if mode == "inner":
            raise TypeError("converted in L2")
    else:
        trace.append("L2 else")
    finally:
        trace.append("L2 finally")


def level1(mode):
    try:
        level2(mode)
    except (KeyError, TypeError) as exc:
        trace.append(f"L1 caught {type(exc).__name__}")
    else:
        trace.append("L1 else")
    finally:
        trace.append("L1 finally")


for mode in ["none", "inner", "middle"]:
    trace.clear()
    level1(mode)
    print(f"mode={mode}:")
    for step in trace:
        print("   ", step)


def loop_with_finally():
    out = []
    for i in range(5):
        try:
            if i == 1:
                continue
            if i == 3:
                break
            out.append(f"body{i}")
        finally:
            out.append(f"fin{i}")
    return out


print("loop with continue/break:", loop_with_finally())
