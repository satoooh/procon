from heapq import heappush, heappop

s = input()
K = int(input())

min_s = sorted(list(set(s)))

res = [min(s)]
q = []
x = 0

while len(set(q)) < K:
    min_index = [n for n, v in enumerate(s) if v == min_s[x]]
    for m in min_index:
        for i in range(1, 6):
            if m+i <= len(s):
                q.append(s[m:m+i])
    x += 1

ans = sorted(list(set(q)))[K-1]

print(ans)
