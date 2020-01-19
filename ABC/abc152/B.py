a, b = map(int, input().split())

A = str(a) * b
B = str(b) * a

print(min(A, B))
