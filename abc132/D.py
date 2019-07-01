"""
高校数学っぽい場合の数の問題。
まずは赤いボールを一列に並べて、両端含めたこの間に青いボールを入れる。このとき青いボールはi個のグループに分ける必要がある。
ということで、青いボールのグループ分けの方法と入れ方の積が答えになり、これら2つの二項係数を求めればいい。

二項係数に関しては次のサイトを参考に改良した
https://qiita.com/derodero24/items/91b6468e66923a87f39f
"""


from operator import mul
from functools import reduce


def cmb(n, r):
	if n < r:
		return 0
	r = min(n - r, r)
	if r == 0:
		return 1
	numer = reduce(mul, range(n, n - r, -1))
	denom = reduce(mul, range(1, r + 1))
	return numer // denom % INF


N, K = map(int, input().split())
INF = 10 ** 9 + 7

for i in range(1, K + 1):
	print(cmb(K - 1, i - 1) * cmb(N - K + 1, i) % INF)
