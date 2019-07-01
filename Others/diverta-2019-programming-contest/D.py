N = int(input())
ans = 0

div = []  # Nの約数を全列挙してdivとする
for i in range(1, int(N ** 0.5) + 1):
	if N % i == 0:
		div.append(i)
		if i != N // i:
			div.append(N // i)

for j in range(len(div)):
	if div[j] == 1:  # m=0はskip
		pass
	else:
		m = div[j] - 1
		if N // m == N % m:
			ans += m

print(ans)
