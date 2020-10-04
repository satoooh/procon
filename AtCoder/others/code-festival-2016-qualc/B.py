K, T = map(int, input().split())
a = list(map(int, input().split()))
print(max(0, 2 * max(a) - sum(a) - 1))
