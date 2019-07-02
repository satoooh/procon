N, M = map(int, input().split())
A, B = [0] * N, [0] * N
for i in range(N):
	A[i], B[i] = map(int, input().split())

#  値段Aの昇順でソート
C = sorted(zip(A, B))
A, B = zip(*C)

ans, cnt, i = 0, 0, 0
while cnt < M:
	tmp = min(B[i], M - cnt)
	cnt += tmp
	ans += A[i] * tmp
	i += 1
print(ans)
