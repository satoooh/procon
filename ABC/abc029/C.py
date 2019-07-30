from itertools import product
N = int(input())
ans = product("abc", repeat = N)
for ai in ans:
	print("".join(ai))
