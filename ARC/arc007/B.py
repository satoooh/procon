N, M = map(int, input().split())
CDs = [i for i in range(1, N+1)]
now_d, next_d = 0, 0

for _ in range(M):
    next_d = int(input())
    if next_d in CDs:
        CDs[CDs.index(next_d)] = now_d
    now_d = next_d

for i in range(N):
    print(CDs[i])
