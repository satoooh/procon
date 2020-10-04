from bisect import bisect_left

N, M = map(int, input().split())
X, Y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
now_time = 0

while True:
	if now_time > a[-1]:
		print(ans)
		exit()
	else:
		now_time = a[bisect_left(a, now_time)]
		now_time += X
		# print(now_time, "arrive at B")
		if now_time > b[-1]:
			print(ans)
			exit()
		else:
			now_time = b[bisect_left(b, now_time)]
			now_time += Y
			# print(now_time, "arrive at A")
			ans += 1
