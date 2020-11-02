C = int(input())

n, m, l = 0, 0, 0
for _ in range(C):
    c = sorted(list(map(int, input().split())))
    n = max(n, c[0])
    m = max(m, c[1])
    l = max(l, c[2])

print(n * m * l)
