N, K = map(int, input().split())
h = list(map(int, input().split()))
print(len([hi for hi in h if hi >= K]))
