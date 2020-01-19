def runLength(str):
    """文字列strをランレングス圧縮して返す関数
    ex: "0000111101" => [(0,4), (1,4), (0,1), (1,1)]
    """
    res = []
    data, count = str[0], 1
    for i in range(1, len(str)):
        if str[i] == data:
            count += 1
        else:
            res.append((data, count))
            data, count = str[i], 1
    res.append((data, count))
    return res

S = input()  # S[0] == "R", S[-1] == "L"

ans = [0] * len(S)
ind = -1
for rl in runLength(S):
    if rl[0] == "R":
        ind += rl[1]
        ans[ind] += rl[1] - rl[1] // 2
        ans[ind+1] += rl[1] // 2
    else:
        ans[ind] += rl[1] // 2
        ans[ind+1] += rl[1] - rl[1] // 2
        ind += rl[1]

print(*ans)
