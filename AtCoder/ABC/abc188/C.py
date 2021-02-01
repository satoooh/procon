N = int(input())
A = list(map(int, input().split()))

# 準優勝するのは、A を前半後半で半分に分けたときの前半の最大値と後半の最大値のうち、小さい方
cand1, cand2 = max(A[:2**(N-1)]), max(A[2**(N-1):])
print(A.index(min(cand1, cand2)) + 1)
