X, Y = map(int, input().split())
if max(X, Y) - min(X, Y) < 3:
    print("Yes")
else:
    print("No")
