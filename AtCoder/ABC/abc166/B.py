N, K = map(int, input().split())

A = set([])
for i in range(K):
    d = int(input())
    Ai = set(list(map(int, input().split())))
    A = A.union(Ai)

print(N - len(A))
