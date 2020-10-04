import itertools
from heapq import heappush, heappop

N, K = map(int, input().split())
A = list(map(int, input().split()))

hq = []
hq_max = 0

for a1, a2 in itertools.combinations(A, 2):
    if ( len(hq) >= K ) and ( a1 * a2 >= hq_max ):
        continue
    else:
        heappush(hq, a1 * a2)
        hq_max = max(hq_max, a1 * a2)

for i in range(K):
    res = heappop(hq)
print(res)
