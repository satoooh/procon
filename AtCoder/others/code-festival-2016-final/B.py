N = int(input())

ans_max = 0
while ans_max * (ans_max + 1) / 2 < N:
    ans_max += 1

num_remove = ans_max * (ans_max + 1) // 2 - N
for i in range(1, ans_max + 1):
    if i != num_remove:
        print(i)
