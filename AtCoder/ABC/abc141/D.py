import heapq

N, M = map(int, input().split())
A = [-i for i in list(map(int, input().split()))]
heapq.heapify(A)
for m in range(M):
    A_max = -heapq.heappop(A)  # Aの最大値を削除して取り出す
    heapq.heappush(A, -(A_max // 2))
print(-sum(A))
