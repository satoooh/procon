N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = float("inf")

for i in range(2**N):
    now = bin(i)[2:].zfill(N)  # now[i]: 参考書iを買う
    res = 0
    An = [0] * M
    for n in range(N):
        if now[n] == "1":
            res += A[n][0]
            An = [An[j] + A[n][j+1] for j in range(M)]
    if min(An) >= X:
        ans = min(ans, res)

if ans == float("inf"):
    print(-1)
else:
    print(ans)
