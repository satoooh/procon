N = int(input())
a, b, c = [0] * N, [0] * N, [0] * N
for i in range(N):
	a[i], b[i], c[i] = map(int, input().split())
dp = [[0] * 3 for _ in range(N)]
dp[0] = [a[0], b[0], c[0]]
for i in range(N - 1):
	dp[i + 1][0] = max(dp[i + 1][0], dp[i][1] + a[i + 1], dp[i][2] + a[i + 1])
	dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + b[i + 1], dp[i][2] + b[i + 1])
	dp[i + 1][2] = max(dp[i + 1][2], dp[i][0] + c[i + 1], dp[i][1] + c[i + 1])
print(max(dp[N - 1]))
