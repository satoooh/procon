s = input()
g_cnt, p_cnt = 0, 0
ans = 0
for si in s:
    if si == "g":
        if p_cnt < g_cnt:
            p_cnt += 1
            ans += 1
        else:
            g_cnt += 1
    else:
        if p_cnt < g_cnt:
            p_cnt += 1
        else:
            g_cnt += 1
            ans -= 1
print(ans)
