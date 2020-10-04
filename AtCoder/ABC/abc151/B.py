N, K, M = map(int, input().split())
A = list(map(int, input().split()))

ans = max(0, N * M - sum(A))
if ans > K:
    print(-1)
else:
    print(ans)
