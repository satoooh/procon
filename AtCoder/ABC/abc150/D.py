from fractions import gcd

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(set([i//2 for i in a]))

b_odd = [i for i in b if (i % 2 == 1)]
b_even = [i for i in b if (i % 2 == 0)]

if b_even == []:
    # b の最小公倍数を求める
    L = b_odd[0]
    for i in range(1, len(b_odd)):
        L = L * b_odd[i] // gcd(L, b_odd[i])
    print(M//L - M//(2*L))
else:
    # b_odd の最小公倍数を求める
    L_odd = b_odd[0]
    for i in range(1, len(b_odd)):
        L_odd = L_odd * b_odd[i] // gcd(L_odd, b_odd[i])
    # 1 ~ M の中で (L_odd*奇数) と表せる数字の個数が答えの候補
    # (L_oddの倍数の個数) - (2L_oddの倍数の個数)と考える
    tmp = M//L_odd - M//(2*L_odd)
    # つまり L_odd*1, L_odd*3, ..., L_odd*tmp が解答の候補
    # よって候補に対して検証を行う
    ans = 0
    res = [L_odd * i for i in range(1, tmp, 2)]
    for r in res:
        flag = 0
        for bi in b_even:
            if (r // bi) % 2 == 0:
                flag = 1
        if flag == 0:
            ans += 1
    print(ans)
