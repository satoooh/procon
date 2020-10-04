n = int(input())
a = list(map(int, input().split()))
ai = max(a)
diff = float("inf")
for aj in set(a):
    if abs(ai / 2 - aj) < diff:
        ans = [ai, aj]
        diff = abs(ai / 2 - aj)
print(' '.join(map(str, ans)))
