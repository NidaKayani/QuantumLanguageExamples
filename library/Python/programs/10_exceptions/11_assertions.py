"""Assertions for internal invariants and how AssertionError reports failures."""


def mean(values):
    assert len(values) > 0, "mean() requires at least one value"
    return sum(values) / len(values)


def binary_search(items, target):
    assert all(a <= b for a, b in zip(items, items[1:])), "items must be sorted"
    lo, hi = 0, len(items)
    while lo < hi:
        mid = (lo + hi) // 2
        if items[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    found = lo < len(items) and items[lo] == target
    assert not found or items[lo] == target
    return lo if found else -1


def normalize(weights):
    total = sum(weights)
    result = [w / total for w in weights]
    assert abs(sum(result) - 1.0) < 1e-9, f"weights sum to {sum(result)}"
    return result


print("mean:", mean([2, 4, 9]))
try:
    mean([])
except AssertionError as exc:
    print("AssertionError:", exc)

print("search 7:", binary_search([1, 3, 5, 7, 9], 7))
print("search 4:", binary_search([1, 3, 5, 7, 9], 4))
try:
    binary_search([3, 1, 2], 1)
except AssertionError as exc:
    print("AssertionError:", exc)

print("normalized:", [round(w, 3) for w in normalize([1, 2, 3, 4])])

try:
    assert 2 + 2 == 5
except AssertionError as exc:
    print("bare assert message:", repr(exc.args))

checks = [("positive", 5 > 0), ("even", 7 % 2 == 0), ("short", len("abc") < 5)]
failures = []
for name, ok in checks:
    try:
        assert ok, name
    except AssertionError as exc:
        failures.append(str(exc))
print("failed checks:", failures)
