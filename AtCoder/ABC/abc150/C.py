from itertools import permutations

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

nums = [i for i in range(1, N+1)]
all_list = list(permutations(nums))
a = all_list.index(P)
b = all_list.index(Q)
print(abs(a-b))
