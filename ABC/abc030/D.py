N, a = map(int, input().split())
k = int(input())
b = list(map(int, input().split()))

now = a
l = []  # lには周期が発生するまで参照する要素を追加し、周期発生が確認されたら該当箇所だけ取り出す

for i in range(k):
	if now in l:
		l = l[l.index(now):]  # 周期発生部分だけ取り出す
		tmp = (k - i) % len(l)
		print(l[tmp])
		exit()
	else:
		l.append(now)
		now = b[now - 1]
	# print(l, now)

print(now)
