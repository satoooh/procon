# PyPy3 で AC
N, X, Y = map(int, input().split())
# グラフの作成 数字が小さい方から大きい方への有向グラフ
g = [[i-1, i+1] for i in range(N)]
g[0].remove(-1)
g[N-1].remove(N)
g[X-1].append(Y-1)
g[Y-1].append(X-1)

ans_list = [0] * N
# 各頂点からの最短経路長を計算
for i in range(N):
    queue = g[i]
    seen = [False] * N
    length = 0
    while queue:
        length += 1
        add = []
        for qi in queue:
            if seen[qi] == False:
                if i < qi:
                    ans_list[length] += 1
                seen[qi] = True
                add += g[qi]
        queue = list(set(add))

# 答えの出力
for k in range(1, N):
    print(ans_list[k])
