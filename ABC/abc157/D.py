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

    def same(self, x, y):  # x,yが同じ集合に属するか判定する
        return self.find(x) == self.find(y)

    def group_size(self, x):  # xが属する集合の大きさを返す
        return self.size[self.find(x)]


N, M, K = map(int, input().split())
A, B = [0] * M, [0] * M
C, D = [0] * K, [0] * K

# 全部 0-indexed に合わせる

g_direct =[[] for _ in range(N)]
uf = UnionFind(N)  # 友達関係をまとめた UnionFind 木

for i in range(M):
    A[i], B[i] = map(int, input().split())
    A[i] -= 1
    B[i] -= 1
    g_direct[A[i]].append(B[i])
    g_direct[B[i]].append(A[i])
    uf.unite(A[i], B[i])

for i in range(K):
    C[i], D[i] = map(int, input().split())
    C[i] -= 1
    D[i] -= 1
    if uf.same(C[i], D[i]):  # 同じ連結成分内にない場合は無視してもよい
        g_direct[C[i]].append(D[i])
        g_direct[D[i]].append(C[i])


ans = [0] * N
# (i の連結成分のサイズ) - (i と j が同じ連結成分に含まれて、 i と j が友達関係もしくはブロック関係にあるような j の個数) - 1
for i in range(N):
    ans[i] = uf.group_size(i) - len(g_direct[i]) - 1
print(*ans)
