from collections import Counter

N = int(input())
A = sorted(list(map(int, input().split())))

# エラトステネスの篩っぽく処理
ans_list = [True for _ in range(A[-1] + 1)]
ans = 0

# ダブリを省くために先に数える
c = Counter(A)

for a in A:
    if ans_list[a] == True:
        if c[a] == 1:
            ans += 1
        i = 2
        while a * i <= A[-1]:
            ans_list[a * i] = False
            i += 1

print(ans)
