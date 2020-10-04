from math import ceil

N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(2, N+1):
    ans += A[ceil(i/2) - 1]

print(ans)
