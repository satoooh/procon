N = int(input())
l, r = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    l[i], r[i] = map(int, input().split())

if N%2 == 1:
    lm = sorted(l)[(N+1)//2-1]
    rm = sorted(r)[(N+1)//2-1]
    print(rm - lm + 1)
else:
    lm = sum(sorted(l)[N//2-1:N//2+1])/2
    rm = sum(sorted(r)[N//2-1:N//2+1])/2
    # 0.5 刻みで増えることに注意
    print(int((rm-lm+0.5)*2))
