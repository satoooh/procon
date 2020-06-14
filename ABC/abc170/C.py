X, N = map(int, input().split())

if N == 0:
    print(X)
    exit()

p = list(map(int, input().split()))

if X not in p:
    print(X)
    exit()
else:
    sa = 1
    while True:
        if X - sa not in p:
            print(X - sa)
            exit()
        elif X + sa not in p:
            print(X + sa)
            exit()
        sa += 1
