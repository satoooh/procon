N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))

L = sorted([X[i+1] - X[i] for i in range(M-1)])
if N >= M:
    ans = 0
else:
    ans = sum(L[:M-N])

print(ans)
