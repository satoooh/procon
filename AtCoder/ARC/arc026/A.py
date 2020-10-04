N, A, B = map(int, input().split())
print(B * min(5, N) + A * max(0, N - 5))
