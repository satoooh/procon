N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))[::-1]
if A[M-1] >= sum(A)/4/M:
    print("Yes")
else:
    print("No")
