# 正規表現を利用する。
import re
if re.match("[A-Z]*?C[A-Z]*?F[A-Z]*?", input()):
	print("Yes")
else:
	print("No")

# 別解: 普通にCの位置を探す
s = input()
if "C" in s:
	i = s.index("C")
	if "F" in s[i + 1:]:
		print("Yes")
		exit()
print("No")
