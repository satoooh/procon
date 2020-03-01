class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ

    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]

    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)

    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]


N, M, K = map(int, input().split())
A, B = [0] * M, [0] * M  # 入力時に 0-index に合わせる
C, D = [0] * K, [0] * K  # 入力時に 0-index に合わせる

direct =[[] for _ in range(N)]  # 同じ集合の友達もしくはブロック関係の人
uf = UnionFind(N)  # 友達関係をまとめた UnionFind 木

for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
    direct[A[i]].append(B[i])
    direct[B[i]].append(A[i])
    uf.unite(A[i], B[i])

for i in range(K):
    C[i], D[i] = map(int, input().split())
    C[i] -= 1
    D[i] -= 1
    if uf.is_same(C[i], D[i]):
        direct[C[i]].append(D[i])
        direct[D[i]].append(C[i])

ans = [0] * N
for i in range(N):
    ans[i] = uf.group_size(i) - len(direct[i]) - 1
print(*ans)
