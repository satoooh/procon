A, B = map(int, input().split())
a, b = abs(A), abs(B)
if a > b:
	print("Bug")
elif a < b:
	print("Ant")
else:
	print("Draw")
