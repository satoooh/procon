import numpy as np

N, M = map(int, input().split())
a = list(map(int, input().split()))

max_oishi = [0 for _ in range(N)]

min_tabeta = 0 # tabeta が 0 となる最小の 人

for i in range(M):
    if min_tabeta < N:
        # min_tabeta は候補に入る
        cand1 = min_tabeta
        cand2 = 0
        while (a[i] <= max_oishi[cand2] or cand2 < cand1):
            cand2 += 1
        if cand2 == cand1:
            ans = cand1
            min_tabeta += 1
            max_oishi[ans] = a[i]
            print(ans+1)
        else:
            ans = cand2
            max_oishi[ans] = a[i]
            print(ans+1)
    else:
        # min_tabeta は候補に入らない
        cand2 = 0
        while (a[i] <= max_oishi[cand2] or cand2 < N):
            cand2 += 1
        if cand2 == N:
            print(-1)
        else:
            ans = cand2
            max_oishi[ans] = a[i]
            print(ans+1)
