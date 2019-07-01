"""
焦って苦戦した
"""

N, L = map(int, input().split())
a = N * (L - 1) + N * (N + 1) // 2
if L > 0:
	print(a - L)
elif L + N - 1 < 0:
	print(a - (L + N - 1))
else:
	print(a)
