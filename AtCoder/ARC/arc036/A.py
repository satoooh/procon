N, K = map(int, input().split())
t = [int(input()) for _ in range(N)]

for i in range(2, N):
	if t[i - 2] + t[i - 1] + t[i] < K:
		print(i + 1)
		exit()
print(-1)
