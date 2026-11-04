"""Edit distance with an explicit operation script and weighted substitution costs."""
from enum import Enum


class Op(Enum):
    KEEP = "="
    SUB = "~"
    INS = "+"
    DEL = "-"


def edit_script(src, dst, sub_cost=1, ins_cost=1, del_cost=1):
    m, n = len(src), len(dst)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i * del_cost
    for j in range(1, n + 1):
        dp[0][j] = j * ins_cost
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            same = src[i - 1] == dst[j - 1]
            dp[i][j] = min(
                dp[i - 1][j - 1] + (0 if same else sub_cost),
                dp[i - 1][j] + del_cost,
                dp[i][j - 1] + ins_cost,
            )
    ops, i, j = [], m, n
    while i or j:
        if i and j and dp[i][j] == dp[i - 1][j - 1] + (0 if src[i - 1] == dst[j - 1] else sub_cost):
            ops.append((Op.KEEP if src[i - 1] == dst[j - 1] else Op.SUB, src[i - 1], dst[j - 1]))
            i, j = i - 1, j - 1
        elif i and dp[i][j] == dp[i - 1][j] + del_cost:
            ops.append((Op.DEL, src[i - 1], ""))
            i -= 1
        else:
            ops.append((Op.INS, "", dst[j - 1]))
            j -= 1
    return dp[m][n], ops[::-1]


def render(ops):
    top = "".join(a or "_" for _, a, _ in ops)
    mid = "".join(op.value for op, _, _ in ops)
    bot = "".join(b or "_" for _, _, b in ops)
    return top, mid, bot


def main():
    for a, b in [("kitten", "sitting"), ("intention", "execution"), ("sunday", "saturday")]:
        dist, ops = edit_script(a, b)
        top, mid, bot = render(ops)
        counts = {op.name: sum(1 for o, _, _ in ops if o is op) for op in Op}
        print(f"{a} -> {b}: distance {dist}")
        print(f"   {top}\n   {mid}\n   {bot}")
        print(f"   ops: {counts}")
    dist, _ = edit_script("kitten", "sitting", sub_cost=2)
    print("With substitution cost 2 (indel distance):", dist)


if __name__ == "__main__":
    main()
