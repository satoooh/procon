from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

ans = sum(A)

Q = int(input())
for i in range(Q):
    B, C = map(int, input().split())
    ans += (C - B) * c[B]
    c[C] += c[B]
    c[B] = 0
    print(ans)
