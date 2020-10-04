"""
フィボナッチ数の計算は以下から拝借。
http://studies.hatenablog.com/entry/2017/03/21/224628
"""
from itertools import product


def mat2_mul(X, Y):
	z = [[0, 0], [0, 0]]
	for (i, j, k) in product(range(2), range(2), range(2)):
		z[i][j] += X[i][k] * Y[k][j]
	return z


def mat2_pow(X, n):
	if n == 0:
		return [[1, 0], [0, 1]]
	elif n % 2:
		return mat2_mul(X, mat2_pow(X, n - 1))
	else:
		half_pow = mat2_pow(X, n / 2)
		return mat2_mul(half_pow, half_pow)


def fib(n):
	if n == 0:
		return 0
	else:
		f = [[0, 1], [1, 1]]
	return mat2_pow(f, n - 1)[1][1]


i = 1
while True:
	if len(str(fib(i))) == 1000:
		print(i)
		exit()
	else:
		i += 1
