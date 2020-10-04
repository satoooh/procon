N, L = map(int, input().split())
x = list(map(int, input().split()))
T1, T2, T3 = map(int, input().split())

hurdle = [0 for _ in range(L+4)]
for xi in x:
    hurdle[xi] = 1

INF = float("inf")
dp = [INF for _ in range(L+4)]  # dp[i] : 0 -> i に到達するまでの時間の min
dp[0] = 0

for i in range(L):
    if hurdle[i+1]:
        dp[i+1] = min(dp[i+1], dp[i] + T1 + T3)
    else:
        dp[i+1] = min(dp[i+1], dp[i] + T1)
    if hurdle[i+2]:
        dp[i+2] = min(dp[i+2], dp[i] + T1 + T2 + T3)
    else:
        dp[i+2] = min(dp[i+2], dp[i] + T1 + T2)
    if hurdle[i+4]:
        dp[i+4] = min(dp[i+4], dp[i] + T1 + 3*T2 + T3)
    else:
        dp[i+4] = min(dp[i+4], dp[i] + T1 + 3*T2)

# L をジャンプする場合を追加
dp[L] = min(dp[L], dp[L-1]+T1//2+T2//2, dp[L-2]+T1//2+T2//2*3, dp[L-3]+T1//2+T2//2*5)

ans = dp[L]
print(ans)
