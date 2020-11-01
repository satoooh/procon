from collections import Counter

S = input()

# 3桁ない場合の処理
if len(S) == 1:
    if int(S)%8 == 0:
        print("Yes")
    else:
        print("No")
elif len(S) == 2:
    if int(S)%8 == 0 or int(S[::-1])%8 == 0:
        print("Yes")
    else:
        print("No")
else:
    cs = Counter(S)
    # 8 の倍数は下 3 桁が 8 の倍数になれば OK
    multiple8 = [str(i).zfill(3) for i in range(1, 1000) if i%8==0]

    for m in multiple8:
        cm = Counter(m)
        ok = True
        for k in cm.keys():
            if cm[k] > cs[k]:
                ok = False
        if ok:
            # print(S, m)
            print("Yes")
            exit()

    print("No")
