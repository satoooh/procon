D = list(map(int, input().split()))
J = list(map(int, input().split()))

ans = 0
for i in range(7):
	ans += max(D[i], J[i])
print(ans)
