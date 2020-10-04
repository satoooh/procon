N = int(input())
m = list(map(int, input().split()))
ans = 0
for mi in m:
    ans += max(0, 80 - mi)
print(ans)
