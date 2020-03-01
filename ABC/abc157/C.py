N, M = map(int, input().split())
ans = [0] * N
ans_flag = [0] * N  # s桁目に条件がきたら1

for _ in range(M):
    s, c = map(int, input().split())
    if N != 1 and s == 1 and c == 0:  # 一番左が1の時点でN(>=2)桁がありえない
        print(-1)
        exit()
    elif ans_flag[s-1] == 1 and ans[s-1] != c:
        print(-1)
        exit()
    else:
        ans[s-1] = c
        ans_flag[s-1] = 1

if N != 1 and ans[0] == 0:  # 一番左が0の場合は1にすれば最小になる
    ans[0] = 1

print(int("".join(map(str, ans))))
