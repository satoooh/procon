N = int(input())
ans_list = ["a"]
alphabet = [chr(ord("a") + i) for i in range(N)]

for i in range(N - 1):
    ans_list = [ ans + x for ans in ans_list for x in alphabet[:len(set(ans)) + 1]]

for ans in ans_list:
    print(ans)
