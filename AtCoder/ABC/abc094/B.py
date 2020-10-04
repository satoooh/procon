N, M, X = map(int, input().split())
A = list(map(int, input().split()))
print(min(len([a for a in A if a < X]), len([a for a in A if a > X])))
