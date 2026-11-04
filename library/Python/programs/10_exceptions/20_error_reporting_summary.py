"""Running a batch of jobs, isolating failures, and summarizing errors by type."""
from collections import Counter, defaultdict
import math


def job_sqrt(x):
    return math.sqrt(x)


def job_ratio(pair):
    a, b = pair
    return a / b


def job_lookup(key):
    table = {"pi": 3.14159, "e": 2.71828}
    return table[key]


def job_parse(text):
    return int(text, 16)


JOBS = [
    (job_sqrt, 16), (job_sqrt, -4), (job_ratio, (9, 3)), (job_ratio, (1, 0)),
    (job_ratio, (1, 2, 3)), (job_lookup, "pi"), (job_lookup, "tau"),
    (job_parse, "ff"), (job_parse, "zz"), (job_parse, 255),
]


def run_all(jobs):
    results, failures = [], defaultdict(list)
    for func, arg in jobs:
        try:
            value = func(arg)
        except Exception as exc:
            failures[type(exc).__name__].append(f"{func.__name__}({arg!r})")
        else:
            results.append((func.__name__, arg, value))
    return results, failures


results, failures = run_all(JOBS)
print(f"{len(results)} succeeded, {sum(map(len, failures.values()))} failed")
for name, arg, value in results:
    print(f"  OK   {name}({arg!r}) = {value:g}")
for kind in sorted(failures):
    print(f"  FAIL {kind}: {', '.join(failures[kind])}")
counts = Counter({k: len(v) for k, v in failures.items()})
print("most common failure:", counts.most_common(1)[0])
print("success rate:", f"{len(results) / len(JOBS):.0%}")
