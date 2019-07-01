"""
締切早いやつからこなしていく
"""

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]
X = sorted(X, key=lambda x: x[1])

# a[i]はA[i]=X[i][0]まで終わらせるためにかかる累積時間
a = [0] * N
a[0] = X[0][0]
for i in range(1, N):
	a[i] = a[i - 1] + X[i][0]

for j in range(N):
	if a[j] > X[j][1]:
		print("No")
		exit()
print("Yes")
