N = int(input())
q = [sorted(list(map(int, input().split()))) for _ in range(N-1)]

ans = 0

# 頂点数
for i in range(1, N+1):
    ans += i * (N - i + 1)

# 辺数
for qi in q:
    u, v = qi[0], qi[1]
    ans -= u * (N - v + 1)

print(ans)
