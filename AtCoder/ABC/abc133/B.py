def dist(a, b):
	res = 0
	for i in range(D):
		res += (a[i] - b[i]) ** 2
	res = res ** 0.5
	return res


N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(N - 1):
	for j in range(i + 1, N):
		if dist(X[i], X[j]).is_integer():
			ans += 1
print(ans)
