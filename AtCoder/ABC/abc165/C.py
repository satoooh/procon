from itertools import combinations_with_replacement

def point(A):
    res = 0
    for i in range(Q):
        if x[i][1] > len(A):
            continue
        else:
            if A[x[i][1]-1] - A[x[i][0]-1] == x[i][2]:
                res += x[i][3]
    return res


N, M, Q = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(Q)]

ans = 0
for A in combinations_with_replacement(range(1, M+1), N):
    ans = max(ans, point(A))

print(ans)
