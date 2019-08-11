from operator import mul
from functools import reduce
import collections


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    elif r < 0:
        return 0
    numer = reduce(mul, range(n, n - r, -1))
    denom = reduce(mul, range(1, r + 1))
    return numer // denom


N = int(input())
s = ["".join(sorted(input())) for _ in range(N)]
c = collections.Counter(s)
ans = 0
for si in set(s):
    n = c[si]
    ans += cmb(n, 2)
print(ans)
