N = int(input())
P = list(map(int, input().split()))

ans = 0
minP = N+1

for p in P:
    if (p < minP):
        ans += 1
        minP = p
print(ans)
