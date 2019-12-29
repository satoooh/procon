from fractions import gcd

A, B = map(int, input().split())
G = gcd(A, B)
print(A*B // G)
