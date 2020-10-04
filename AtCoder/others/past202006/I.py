N = int(input())

transposed = 0
col = [i for i in range(N)]  # 行
row = [j for j in range(N)]  # 列

Q = int(input())

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # 行の交換（転置してたら列の交換）
        a, b = query[1]-1, query[2]-1
        if transposed:
            row[a], row[b] = row[b], row[a]
        else:
            col[a], col[b] = col[b], col[a]
    elif query[0] == 2:
        # 列の交換（転置してたら行の交換）
        a, b = query[1]-1, query[2]-1
        if transposed:
            col[a], col[b] = col[b], col[a]
        else:
            row[a], row[b] = row[b], row[a]
    elif query[0] == 3:
        transposed += 1
        transposed %= 2
    else:
        # 出力（転置してたら行と列を交換）
        a, b = query[1]-1, query[2]-1
        if transposed:
            ans = N*row[a] + col[b]
        else:
            ans = N*col[a] + row[b]
        print(ans, (a, b), transposed)
