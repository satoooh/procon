import math
N, K = map(int, input().split())
ans = 0
for i in range(1, N + 1):
	ans += 0.5 ** (math.ceil(max(math.log2(K / i), 0)))
print(ans / N)
