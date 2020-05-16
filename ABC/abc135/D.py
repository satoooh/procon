S = input()
N = len(S)

MOD = 10**9 + 7
dp = [[0 for _ in range(13)] for _ in range(N)]  # dp[i][j]: S[i]までみて13で割ってjあまるものの個数

# 初期値
if S[0] == "?":
    for j in range(10):
        dp[0][j] = 1
else:
    dp[0][int(S[0])] = 1


# dpテーブル更新式
for i in range(1, N):
    si = S[i]
    if si == "?":
        for si_cand in range(10):
            for j in range(13):
                dp[i][(j*10+si_cand)%13] += dp[i-1][j] % MOD
    else:
        for j in range(13):
            dp[i][(j*10+int(si))%13] += dp[i-1][j] % MOD

print(dp[N-1][5] % MOD)
