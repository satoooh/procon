import collections

N = int(input())
a = list(map(int, input().split()))
c = collections.Counter(a)
ans = 0

for ai in set(a):
    if c[ai] < ai:
        ans += c[ai]
    else:
        ans += c[ai] - ai

print(ans)
