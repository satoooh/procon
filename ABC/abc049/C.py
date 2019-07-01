import re

S = input()
if re.match("^(dream(er)?|erase(r)?)+$", S):
	print("YES")
else:
	print("NO")
