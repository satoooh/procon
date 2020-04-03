N = int(input())
ans_list = [i for i in range(1, 555556) if len(set(str(i))) == 1]
print(ans_list[N-1])
