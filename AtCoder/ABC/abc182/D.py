import numpy as np

N = int(input())
A = list(map(int, input().split()))

p = [A[i] for i in range(N)]
q = [A[i] for i in range(N)]
for i in range(1, N):
    p[i] = p[i-1] + A[i]
    q[i] = max(q[i-1], p[i])

ans = 0
x = 0
for i in range(N):
    ans = max(ans, x + q[i])
    x += p[i]

print(ans)
