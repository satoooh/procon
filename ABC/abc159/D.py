from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

# 先にk番目を抜かない場合を求めておく
ans = 0
for n in c.values():
    ans += n*(n-1)//2

# k番目を抜く場合の差分を加える
for k in range(N):
    m = c[A[k]]
    print(ans - (m-1))  # -m*(m-1)//2 + (m-1)*(m-2)//2
