N = int(input())

if N % 2 == 0:
    n = N // 2
    ans = 0
    k = 5
    while k <= n:
        ans += n // k
        k *= 5
    print(ans)
else:
    print(0)
