K, N = map(int, input().split())
A = list(map(int, input().split()))
diff = K - (A[N-1] - A[0])
for i in range(N-1):
    diff = max(diff, A[i+1] - A[i])
print(K - diff)
