# 地道に頑張る

N, M, A, B = map(int, input().split())
c = [int(input()) for _ in range(M)]
now = N
for i in range(M):
	if now <= A:
		now += B
	if now < c[i]:
		print(i + 1)
		exit()
	else:
		now -= c[i]
print("complete")
