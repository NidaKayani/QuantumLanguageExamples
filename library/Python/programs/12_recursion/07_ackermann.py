"""The Ackermann function: deeply recursive, evaluated only for tiny inputs."""

from functools import lru_cache

call_count = 0


def ackermann(m: int, n: int) -> int:
    global call_count
    call_count += 1
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


@lru_cache(maxsize=None)
def ackermann_memo(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann_memo(m - 1, 1)
    return ackermann_memo(m - 1, ackermann_memo(m, n - 1))


print("   m\\n " + "".join(f"{n:>6}" for n in range(5)))
for m in range(4):
    row = []
    for n in range(5):
        if m == 3 and n > 3:
            row.append("   ...")
            continue
        call_count = 0
        value = ackermann(m, n)
        row.append(f"{value:>6}")
    print(f"   {m}   " + "".join(row))

for m, n in [(1, 3), (2, 3), (3, 3)]:
    call_count = 0
    ackermann(m, n)
    print(f"A({m},{n}) = {ackermann_memo(m, n)} needed {call_count} plain calls")

print("closed forms check:", all(
    ackermann_memo(1, n) == n + 2 and ackermann_memo(2, n) == 2 * n + 3 and ackermann_memo(3, n) == 2 ** (n + 3) - 3
    for n in range(5)))
print("memo cache size:", ackermann_memo.cache_info().currsize)
