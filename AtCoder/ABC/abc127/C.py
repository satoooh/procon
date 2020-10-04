N, M = map(int, input().split())
L, R = [0] * M, [0] * M
for i in range(M):
	L[i], R[i] = map(int, input().split())
print(max(min(R) - max(L) + 1, 0))
