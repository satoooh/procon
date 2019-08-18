N = int(input())
v = sorted(list(map(int, input().split())))
ans = v[0]
for vi in v:
    ans /= 2
    ans += vi / 2
print(ans)
