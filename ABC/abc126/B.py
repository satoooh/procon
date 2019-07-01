S = input()
a, b = int(S[: 2]), int(S[2:])
if a == 0 and b == 0:
	print("NA")
elif a >= 13 and b >= 13:
	print("NA")
elif a == 0 and b >= 13:
	print("NA")
elif a >= 13 and b == 0:
	print("NA")
elif 1 <= a <= 12 and 1 <= b <= 12:
	print("AMBIGUOUS")
elif 1 <= a <= 12 and b == 0:
	print("MMYY")
elif 1 <= a <= 12 and b >= 13:
	print("MMYY")
elif a == 0 and 1 <= b <= 12:
	print("YYMM")
else:
	print("YYMM")
