N, P = map(int, input().split())
S = input()
ans = 0

# dp[i][j] = S[i:j+1] でみたときの答え
dp = [[0] * N for _ in range(N)]

# 初期値の設定
for i in range(N):
    dp[i][i] = (int(S[i]) % P == 0)  # S[i] が P の倍数なら 1, そうでないなら 0

# 値の更新
for k in range(1, N):
    dp[0][0+k] = dp[0][0+k-1]
    for j in range(N-k):
        dp[j][j+k] += dp[j+1][j+k] + (int(S[j:j+k+1]) % P == 0)

# 求めたいのは dp[0][N-1]
print(dp[0][N-1])
