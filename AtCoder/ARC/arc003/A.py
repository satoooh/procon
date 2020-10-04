N = int(input())
r = input()
ans = 0
for i in range(N):
	if r[i] == "A":
		ans += 4
	elif r[i] == "B":
		ans += 3
	elif r[i] == "C":
		ans += 2
	elif r[i] == "D":
		ans += 1
print(ans / N)
