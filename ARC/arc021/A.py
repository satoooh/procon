A = [list(map(int, input().split())) for _ in range(4)]
ans = "GAMEOVER"

for i in range(4):
	for j in range(3):
		if A[i][j] == A[i][j + 1]:
			ans = "CONTINUE"
			print(ans)
			exit()

for i in range(3):
	for j in range(4):
		if A[i][j] == A[i + 1][j]:
			ans = "CONTINUE"
			print(ans)
			exit()

print(ans)
