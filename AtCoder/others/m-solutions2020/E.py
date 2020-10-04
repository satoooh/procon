from heapq import heappush, heappop
from collections import Counter
from itertools import product, combinations

N = int(input())

X, Y, P = [0 for _ in range(N)], [0 for _ in range(N)], [0 for _ in range(N)]
hq = []
for i in range(N):
    X[i], Y[i], P[i] = map(int, input().split())

# P の大きい順にソート
px, py, p = zip(*sorted(zip(X, Y, P), key=lambda x: -x[2]))

# 考えるべき最大の K 、つまり K >= maxK で distance = 0 となる maxK を考える
cx, cy = Counter(X), Counter(Y)
maxK = N
for i in range(N):
    if cx[X[i]] >= 2:
        maxK -= 1
    elif cy[Y[i]] >= 2:
        maxK -= 1
maxK += len([v for v in cx.values() if v >= 2]) + len([v for v in cy.values() if v >= 2])

# print(f"maxK = {maxK}")

# こうすればあとは K = 0, 1, 2, ..., maxK-1 で考えればよい
# しかもこの maxK は最大で 15 なのでなんか全探索とかいけそう？
# たかだか 2^15 < 40000 通り

# K = 0
distance = sum([P[i] * min(abs(X[i]), abs(Y[i])) for i in range(N)])
print(distance)

# 通る点
# 同一直線状に複数点があるものは候補に含まれるので先に入れとく（そんなに多くないでしょきっと）
points = [(x, y) for x, y in zip(X, Y) if (cx[x] >= 2 or cy[y] >= 2)]

for K in range(1, maxK):
    # print(f"K = {K}")
    # K 個の通る点を選択
    points.append((px[K-1], py[K-1]))
    points = list(set(points))
    # print(f"points = {points}")
    # 2^K 通りの全探索を実施
    # points のそれぞれに対し、 直線 x = X[i] or y = Y[i] のどちらを選択するかで評価
    ans = float("inf")
    for now in product(range(2), repeat=len(points)):
        # now[i] == 0 ならば x = X[i] を選択
        lines = []
        for i in range(len(points)):
            if now[i] == 0:
                lines.append(("x", points[i][0]))
            else:
                lines.append(("y", points[i][1]))
        # print(f"  lines: {lines}")
        # lines から K 本とる
        for v in combinations(lines, K):
            # 実際の通る直線
            xlines, ylines = [], []
            for u in v:
                if u[0] == "x":
                    xlines.append(u[1])
                else:
                    ylines.append(u[1])
            # コストの計算
            res = 0
            for i in range(N):
                xcost = abs(X[i])
                for j in range(len(xlines)):
                    xcost = min(xcost, abs(X[i] - xlines[j]))
                ycost = abs(Y[i])
                for j in range(len(ylines)):
                    ycost = min(ycost, abs(Y[i] - ylines[j]))
                res += P[i] * min(xcost, ycost)
            # print(f"  now res = {res}")
            ans = min(ans, res)
    print(ans)

for _ in range(N - maxK + 1):
    print(0)
