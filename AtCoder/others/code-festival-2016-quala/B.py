N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    j = a[i] - 1
    if i < j and a[j] - 1 == i:
        ans += 1
print(ans)
