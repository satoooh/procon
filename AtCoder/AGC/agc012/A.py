N = int(input())
a = sorted(list(map(int, input().split())))[::-1]

ans = 0
for i in range(N):
    ans += a[1+2*i]

print(ans)
