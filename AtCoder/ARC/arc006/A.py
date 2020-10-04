# ひどいコードを書いてしまった

E, B, L = list(input().split()), input(), list(input().split())
if len([l for l in L if l in E]) == 6:
	print(1)
elif len([l for l in L if l in E or l == B]) == 6:
	print(2)
elif 3 <= len(set(E) & set(L)) <= 5:
	print(8 - len(set(E) & set(L)))
else:
	print(0)
