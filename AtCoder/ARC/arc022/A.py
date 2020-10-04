S = input().lower()

if "i" in S:
    ind = S.index("i")
    S = S[ind:]
else:
    print("NO")
    exit()

if "c" in S:
    ind = S.index("c")
    S = S[ind:]
else:
    print("NO")
    exit()

if "t" in S:
    print("YES")
else:
    print("NO")
