N, S = int(input()), input()
ans = 0
for i in range(N):
	X = S[: i]
	Y = S[i:]
	ans = max(ans, len(set(X) & set(Y)))
print(ans)
