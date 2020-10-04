# 重複を許してリストの共通部分をとる
from collections import Counter
n = int(input())
s = [list(input()) for _ in range(n)]
ans = s[0]
for i in range(1, n):
    ans = list((Counter(ans) & Counter(s[i])).elements())
print("".join(sorted(ans)))