N = int(input())
s = [0] * N
for i in range(N):
	s[i] = input()
ans = 0

for j in range(N):
	ans += s[j].count("AB")

x, y, z = 0, 0, 0  # xは~A、yはB~、zはB~Aの個数
for k in range(N):
	if s[k][0] == "B" and s[k][-1] =="A":
		z += 1
	elif s[k][0] == "B":
		y += 1
	elif s[k][-1] == "A":
		x += 1

if x >= 1 and y >= 1:
	ans += z + min(x, y)
elif x >= 1 or y >= 1:
	ans += z
else:
	ans += max(0, z - 1)

print(ans)
