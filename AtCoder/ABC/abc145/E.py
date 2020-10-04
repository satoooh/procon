"""
ナップサック問題で T - 1 分時点での美味しさの和の最大をもとめて、残ったものの最大を足し合わせたものが答え
"""
import copy

N, T = map(int, input().split())
item = [list(map(int, input().split())) for _ in range(N)]  # item = [[weight, value], ...]
capacity = T - 1
item_left = copy.copy(item)  # 残ったアイテムのリスト

# i番目以降のナップサックの価値の最大値
def knapsack(i, capacity):
    if i >= len(item):
        return 0, []
    elif capacity - item[i][0] < 0.0:
        return knapsack(i + 1, capacity)
    else:
        # i番目の品物を入れない場合
        v1, l1 = knapsack(i + 1, capacity)

        # i番目の品物を入れる場合
        v2, l2 = knapsack(i + 1, capacity - item[i][0])
        v2 += item[i][1]
        if item[i] in item_left:
            item_left.remove(item[i])
        if v1 > v2:
            return v1, l1
        else:
            return v2, l2

print(item_left)
print(sorted(item_left, key=lambda x: x[1]))
print(sorted(item_left, key=lambda x: x[1])[:: -1])

value, l_selected = knapsack(0, capacity)
last_one = sorted(item_left, key = lambda x: x[1])
print(last_one)
print(last_one[0])

print(value + last_one)
