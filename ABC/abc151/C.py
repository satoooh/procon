N, M = map(int, input().split())
P = [0] * N  # 正解済みは1
wa = [0] * N  # WA の回数を記録
ac, penalty = 0, 0

for _ in range(M):
    # 読み込み
    p, S = input().split()
    p = int(p)
    if P[p-1] == 1:
        # すでに正解済みの場合は何もしない
        continue
    elif S == "WA":
        # 未正解で WA
        wa[p-1] += 1
    else:
        # 未正解で AC
        ac += 1
        penalty += wa[p-1]
        P[p-1] = 1
print(ac, penalty)
