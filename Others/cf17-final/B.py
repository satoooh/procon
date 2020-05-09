from collections import Counter

S = input()
c = Counter(S)

if len(c) == 3 and max(c.values()) - min(c.values()) <= 1:
    print("YES")
elif len(c) == 2 and len(S) == 2:
    print("YES")
elif len(c) == 1 and len(S) == 1:
    print("YES")
else:
    print("NO")
