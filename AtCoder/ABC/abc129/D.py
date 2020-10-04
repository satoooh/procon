H, W = map(int, input().split())
S = [input() for _ in range(H)]

# そのマスを含めてLeft, Right, Up, Downにそれぞれ何マス分明かりを照らせるかを配列に記録
L = [[0] * W for _ in range(H)]
R = [[0] * W for _ in range(H)]
D = [[0] * W for _ in range(H)]
U = [[0] * W for _ in range(H)]

for i in range(H):
	for j in range(W):
		if S[i][j] == ".":
			if j == 0:
				L[i][j] = 1
			else:
				L[i][j] = L[i][j - 1] + 1

for i in range(H):
	for j in range(W - 1, -1, -1):
		if S[i][j] == ".":
			if j == W - 1:
				R[i][j] = 1
			else:
				R[i][j] = R[i][j + 1] + 1

for j in range(W):
	for i in range(H - 1, -1, -1):
		if S[i][j] == ".":
			if i == H - 1:
				D[i][j] = 1
			else:
				D[i][j] = D[i + 1][j] + 1

for j in range(W):
	for i in range(H):
		if S[i][j] == ".":
			if i == 0:
				U[i][j] = 1
			else:
				U[i][j] = U[i - 1][j] + 1


ans = 0
X = [[0] * W for _ in range(H)]
for i in range(H):
	for j in range(W):
		X[i][j] = L[i][j] + R[i][j] + D[i][j] + U[i][j] - 3
	ans = max(ans, max(X[i]))

print(ans)
