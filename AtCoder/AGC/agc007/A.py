# 右と下に移動する場合は絶対に最短経路になるので、最短経路を出してそれ以外に#があったらアウト、の方針で
def end_impossible():
    print("Impossible")
    exit()


H, W = map(int, input().split())
A = [input() for _ in range(H)]
seen = []

if A[0][0] == ".":
    end_impossible()

seen.append([0, 0])
h, w = 0, 0

while h != H - 1 or w != W - 1:
    if h < H - 1 and A[h + 1][w] == "#":
        h += 1
    elif w < W - 1 and A[h][w + 1] == "#":
        w += 1
    else:
        end_impossible()
    seen.append([h, w])

for i in range(H):
    for j in range(W):
        if A[i][j] == "#" and [i, j] not in seen:
            end_impossible()

print("Possible")
