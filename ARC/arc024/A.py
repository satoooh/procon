L, R = map(int, input().split())
l = list(map(int, input().split()))
r = list(map(int, input().split()))
ans = 0
for li in l:
	if li in r:
		r.remove(li)
		ans += 1
print(ans)
