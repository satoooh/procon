N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for _ in range(N):
	A = list(map(int, input().split()))
	AB = [0] * M
	for i in range(M):
		AB[i] = A[i] * B[i]
	if sum(AB) + C > 0:
		ans += 1
print(ans)
