from heapq import heapify, heappop, heappush

# 次の桁の生成ルール ex. 1 -> 10, 11, 12
def next_int(n):
    if n == 0:
        return [0, 1]
    elif n == 9:
        return [8, 9]
    else:
        return [n-1, n, n+1]

K = int(input())
queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # とりあえず 1 桁の Lunlun Number を初期値にとる
heapify(queue)

for _ in range(K-1):
    now = heappop(queue)  # 最小値を取り出す
    # 取り出した値を使って次の桁の値を生成し queue に投げる
    for next_i in next_int(now%10):
        heappush(queue, now*10 + next_i)

print(queue[0])  # K 回目に取り出す最小値
