def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

N = int(input())
x, y = [0] * N, [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
ans = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        ans += dist(x[i], y[i], x[j], y[j])

ans = ans * 2 / N

print(ans)
