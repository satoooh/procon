s = input()

for i in range(len(s) // 2):
	if s[i] == s[len(s) - i - 1] or s[i] == "*" or s[len(s) - i - 1] == "*":
		continue
	else:
		print("NO")
		exit()
print("YES")
