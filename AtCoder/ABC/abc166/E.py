from collections import Counter

N = int(input())
A = list(map(int, input().split()))

ans = 0

diff = [i - A[i] for i in range(N)]
summ = [i + A[i] for i in range(N)]

cdiff = Counter(diff)

for i in range(N):
    if summ[i] in cdiff.keys():
        ans += cdiff[summ[i]]

print(ans)
