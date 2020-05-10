from itertools import product

N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = float("inf")

for now in product(range(2), repeat=N):
    res = 0
    An = [0 for _ in range(M)]
    for n in range(N):
        if now[n] == 1:
            res += A[n][0]
            An = [An[j] + A[n][j+1] for j in range(M)]
    if min(An) >= X:
        ans = min(ans, res)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
