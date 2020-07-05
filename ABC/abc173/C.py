H, W, K = map(int, input().split())
c = [input() for _ in range(H)]

# 各行・各列を選ぶか選ばないかで全列挙してbit

ans = 0

for hn in range(2**H):
    hbit = bin(hn)[2:].zfill(H)
    for wn in range(2**W):
        wbit = bin(wn)[2:].zfill(W)
        count = 0
        # hbit[h] == "1" and wbit[w] == "1" の場合は "#" が残ると考える
        for h in range(H):
            for w in range(W):
                if hbit[h] == "1" and wbit[w] == "1" and c[h][w] == "#":
                    count += 1
        if count == K:
            ans += 1

print(ans)

