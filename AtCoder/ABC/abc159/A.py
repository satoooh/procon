N, M = map(int, input().split())
# 奇数同士 or 偶数同士なので
print(N*(N-1)//2 + M*(M-1)//2)
