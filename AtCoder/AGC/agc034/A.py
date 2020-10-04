N, A, B, C, D = map(int, input().split())
S = input()
if "##" in S[A - 1: max(C, D)]:
	print("No")
	exit()
for i in range(B - 1, D):
	if S[i] == "." and S[i - 1] == ".":
		if D == N or C < D:
			print("Yes")
			exit()
		else:
			if S[i + 1] == ".":
				print("Yes")
				exit()
print("No")
