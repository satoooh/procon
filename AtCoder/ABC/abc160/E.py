from heapq import heapify, heappushpop

X, Y, A, B, C = map(int, input().split())
# 大きい順にソートして受け取っておく
p = sorted(list(map(int, input().split())))[::-1]
q = sorted(list(map(int, input().split())))[::-1]
r = sorted(list(map(int, input().split())))[::-1]
ans_list = p[:X] + q[:Y]  # 着色しない場合
heapify(ans_list)
for ri in r:
    if ri > ans_list[0]:
        heappushpop(ans_list, ri)
    else:
        break
print(sum(ans_list))
