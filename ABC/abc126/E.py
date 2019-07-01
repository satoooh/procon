"""
Union-Find木
"""


class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n)]  # 親
		self.rank = [1] * n  # 深さ
		self.size = [1] * n  # size[i]はiを根とするグループのサイズ

	def find(self, x):  # xの親を返す
		if self.par[x] == x:
			return x
		else:
			return self.find(self.par[x])

	def unite(self, x, y):  # x,yの属する集合をマージする
		x = self.find(x)
		y = self.find(y)
		if x != y:
			if self.rank[x] < self.rank[y]:
				self.par[x] = y
				self.size[y] += self.size[x]
			else:
				self.par[y] = x
				self.size[x] += self.size[y]
				if self.rank[x] == self.rank[y]:
					self.rank[x] += 1

N, M = map(int, input().split())
X, Y, Z = [0] * M, [0] * M, [0] * M
for i in range(M):
	X[i], Y[i], Z[i] = map(int, input().split())

uf = UnionFind(N)

for j in range(M):
	uf.unite(X[j] - 1, Y[j] - 1)

roots = set([])
for k in range(N):
	roots.add(uf.find(k))
print(len(roots))
