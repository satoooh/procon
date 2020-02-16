N = int(input())
a = list(map(int, input().split()))
a_num = [i for i in range(1, N+1)]

# sort
a, a_num = zip(*(sorted(zip(a, a_num))[::-1]))
for i in a_num:
    print(i)
