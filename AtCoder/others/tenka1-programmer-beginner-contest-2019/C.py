N = int(input())
S = input()
A = [S.count(".")]
for i in range(N):
	if S[i] == "#":
		A.append(A[i] + 1)
	else:
		A.append(A[i] - 1)
print(min(A))
