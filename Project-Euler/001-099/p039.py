ans = [0] * 1001

for a in range(1, 1001):
    for b in range(a, 1001 - a):
        for c in range(b, 1001 - a - b):
            if a**2 + b**2 == c**2:
                ans[a + b + c] += 1

print(ans.index(max(ans)))
