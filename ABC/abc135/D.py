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
    if S[i] == "?":
        for si in range(10):
            for j in range(13):
                dp[i][(j*10 + si)%13] += dp[i-1][j]
                dp[i][(j*10 + si)%13] %= MOD
    else:
        si = int(S[i])
        for j in range(13):
            dp[i][(j*10 + si)%13] += dp[i-1][j]
            dp[i][(j*10 + si)%13] %= MOD

print(dp[N-1][5])
