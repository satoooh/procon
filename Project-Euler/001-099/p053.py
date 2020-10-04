from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    numer = reduce(mul, range(n, n - r, -1))
    denom = reduce(mul, range(1, r + 1))
    return numer // denom

ans = 0

for n in range(1, 101):
    for r in range(0, n+1):
        ans += (cmb(n, r) > 1000000)

print(ans)
