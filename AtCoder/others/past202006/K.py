N, Q = map(int, input().split())
c = [[i] for i in range(N)]

for _ in range(Q):
    f, t, x = map(int, input().split())
    # c[f-1] にある コンテナ x-1 とそれ以降を c[t-1] に付け加える
    i = c[f-1].index(x-1)
    c[t-1] = c[t-1] + c[f-1][i:]
    c[f-1] = c[f-1][:i]

for x in range(N):
    # コンテナ x がどこにあるか探して出力
    for i in range(N):
        if x in c[i]:
            print(i+1)
            break
