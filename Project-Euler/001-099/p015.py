"""
nCrを計算して返す関数cmb(n, r)を定義
参考: https://qiita.com/derodero24/items/91b6468e66923a87f39f
"""

from operator import mul
from functools import reduce


def cmb(n, r):
	r = min(n - r, r)
	if r == 0:
		return 1
	numer = reduce(mul, range(n, n - r, -1))
	denom = reduce(mul, range(1, r + 1))
	return numer // denom


print(cmb(40, 20))
