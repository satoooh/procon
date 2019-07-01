S = list(input())
ans = 0
if S[0] == "1":
	for i in range(len(S)):
		if i % 2 == 0 and S[i] == "0":
			ans += 1
		if i % 2 == 1 and S[i] == "1":
			ans += 1
else:
	for i in range(len(S)):
		if i % 2 == 0 and S[i] == "1":
			ans += 1
		if i % 2 == 1 and S[i] == "0":
			ans += 1
print(ans)
