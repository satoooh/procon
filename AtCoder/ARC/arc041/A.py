x, y = map(int, input().split())
k = int(input())
if k > y:
    print(x + y - (k - y))
else:
    print(x + k)
