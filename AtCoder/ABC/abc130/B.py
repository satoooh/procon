"""
階差になってるので和を取ればok
"""

N, X = map(int, input().split())
*L, = map(int, input().split())
D = [0] * (N + 1)
for i in range(N):
	D[i + 1] = D[i] + L[i]
ans = len([j for j in D if j <= X])
print(ans)
