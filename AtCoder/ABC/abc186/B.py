H, W = map(int, input().split())
m = 101
A = [[0 for _ in range(W)] for _ in range(H)]
for h in range(H):
    A[h] = list(map(int, input().split()))
    m = min(m, min(A[h]))

ans = 0
for h in range(H):
    for w in range(W):
        ans += A[h][w] - m

print(ans)
