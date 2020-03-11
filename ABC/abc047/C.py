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


S = input()
print(len(runLength(S)) - 1)
