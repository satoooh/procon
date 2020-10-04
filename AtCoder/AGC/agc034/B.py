s = input().replace("BC", "D")
ans, cnt = 0, 0
for i in range(len(s)):
	if s[i] == "A":
		cnt += 1
	elif s[i] == "D":
		ans += cnt
	else:
		cnt = 0
print(ans)
