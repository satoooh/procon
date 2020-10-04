import numpy as np

N, K = map(int, input().split())
MOD = 998244353
dp = [0 for _ in range(N)]
dp[0] = 1

L, R = [0 for _ in range(K)], [0 for _ in range(K)]
for k in range(K):
    L[k], R[k] = map(int, input().split())

for i in range(N):
    tmp = dp[i]
    for k in range(K):
        if i+L[k] < N:
            for d in range(L[k], min(R[k]+1, N-i)):
                dp[i+d] += tmp
                dp[i+d] %= MOD

ans = dp[N-1] % MOD
print(ans)
