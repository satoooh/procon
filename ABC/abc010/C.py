def dist(x0, y0, x1, y1):
	res = (x0 - x1) ** 2 + (y0 - y1) ** 2
	res = res ** 0.5
	return res


txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
x, y = [0] * n, [0] * n
for i in range(n):
	x[i], y[i] = map(int, input().split())

# lは txa, tya → x[i], y[i] → txb, tyb の距離
for i in range(n):
	l = dist(txa, tya, x[i], y[i]) + dist(x[i], y[i], txb, tyb)
	if l <= T * V:
		print("YES")
		exit()
print("NO")
