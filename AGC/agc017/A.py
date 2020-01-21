N, P = map(int, input().split())
A = list(map(int, input().split()))
a = [i%2 for i in A]
zero = a.count(0)
one = a.count(1)

if one == 0 and P == 1:
    print(0)
else:
    print( (2**zero) * (2**(max(0, one-1))) )
