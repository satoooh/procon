from math import ceil

H = int(input())
W = int(input())
N = int(input())

print(ceil(N/(max(W, H))))
