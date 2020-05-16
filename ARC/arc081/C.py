from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

Ac = sorted([i for i in c.keys() if c[i] >= 2], reverse=True)

if len(Ac) >= 2 and c[Ac[0]] >= 4:
    print(max(Ac[0] * Ac[1], Ac[0] * Ac[0]))
elif len(Ac) >= 2:
    print(Ac[0] * Ac[1])
elif len(Ac) == 1 and c[Ac[0]] >= 4:
    print(Ac[0] * Ac[0])
else:
    print(0)
