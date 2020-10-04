N, Q = map(int, input().split())
S = [input() for _ in range(Q)]

f = [["N"] * N for _ in range(N)]

for s in S:
    a = int(s[2])
    if s[0] == "1":
        # follow
        b = int(s[4])
        f[a-1][b-1] = "Y"
    elif s[0] == "2":
        # re-follow
        followed = [i for i in range(1, N+1) if f[i-1][a-1]=="Y"]
        for i in followed:
            f[a-1][i-1] = "Y"
    else:
        # follow-follow
        x_list = [x for x in range(1, N+1) if f[a-1][x-1]=="Y"]
        for x in x_list:
            # y: x follows y
            y_list = [y for y in range(1, N+1) if f[x-1][y-1]=="Y" and y != a]
            for y in y_list:
                f[a-1][y-1] = "Y"

for fi in f:
    print("".join(fi))
