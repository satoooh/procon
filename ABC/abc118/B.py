N, M = map(int, input().split())
A =[list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(1, A[0][0] + 1):
	flag = True
	a = A[0][i]
	for j in range(1, N):
		if a not in A[j][1:]:
			flag = False
	if flag:
		ans += 1
print(ans)
