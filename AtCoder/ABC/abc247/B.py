N = int(input())
st = [list(input().split()) for _ in range(N)]

for i in range(N):
    target0, target1 = st[i][0], st[i][1]
    flag0, flag1 = False, False # 名前が被っているかどうか
    for j in range(N):
        if i != j:
            s, t = st[j][0], st[j][1]
            if target0 == s or target0 == t:
                flag0 = True
            if target1 == s or target1 == t:
                flag1 = True
    if flag0 == True and flag1 == True:
        print('No')
        exit()

print('Yes')
