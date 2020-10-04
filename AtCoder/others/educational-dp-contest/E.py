N, W = map(int, input().split())
w, v = [0] * N, [0] * N
for i in range(N):
	w[i], v[i] = map(int, input().split())

V = sum(v)
# dp[i][j]:i番目までの品物から価値がj以上になるよう選んだときの重さの総和の最小値
dp = [[float("inf")] * (V + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
	for j in range(V + 1):
		# i+1番目を選ぶ場合
		if j - v[i] >= 0:
			dp[i + 1][j] = min(dp[i + 1][j], dp[i][j - v[i]] + w[i])
		# i+1番目を選ばない場合
		dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

# dp[N][j]がW以下であるようなjの最大値が答えになる
ans = 0
for j in range(V + 1):
	if dp[N][j] <= W:
		ans = j

print(ans)
