from collections import Counter

N = int(input())
A = list(map(int, input().split()))
c = Counter(A)

for i in range(1, N+1):
    if i in c.keys():
        print(c[i])
    else:
        print(0)
