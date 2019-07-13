n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
	tmp = a[i] % 6
	if tmp == 0:
		ans += 3
	elif tmp == 2 or tmp == 4:
		ans += 1
	elif tmp == 5:
		ans += 2
print(ans)
