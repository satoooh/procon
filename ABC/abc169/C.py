S = input()
A, B = S.split(" ")
A = int(A)
b1, b2, b3 = int(B[0]), int(B[2]), int(B[3])

ans = A*b1 + (A*10*b2 + A*b3)//100

print(ans)
