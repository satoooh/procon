N = int(input())
C = list(map(int, input().split()))
Q = int(input())
S = [input() for _ in range(Q)]

ans = 0

for s in S:
    if s[0] == "1":
        _, x, a = s.split(" ")
        x = int(x)
        a = int(a)
        if C[x-1] >= a:
            C[x-1] -= a
            ans += a
    elif s[0] == "2":
        _, a = s.split(" ")
        a = int(a)
        if min(C[0::2]) >= a:
            for i in range(N//2):
                C[2*i] -= a
            ans += a * (N//2)
    else:
        _, a = s.split(" ")
        a = int(a)
        if min(C) >= a:
            C = list(map(lambda x: x-a, C))
            ans += a * N

print(ans)
