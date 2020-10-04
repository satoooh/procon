A, B, N = map(int, input().split())

if N < B:
    print((A*N)//B)
else:
    qa, ra = divmod(A, B)
    rx = B-1
    print(qa*rx + (ra*rx)//B)
