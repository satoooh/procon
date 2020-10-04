import sys
sys.setrecursionlimit(10**9)

def cost(n, costs):
    if n == 0:
        return 0
    if 0 <= n < len(costs) and costs[n] != -1:
        return costs[n]
    else:
        res = []
        if n <= 10e+18:
            res.append(cost(n+1, costs)+D)
        if n >= 1:
            res.append(cost(n-1, costs)+D)
        if n%2 == 0 and n >= 2:
            res.append(cost(n//2, costs)+A)
        if n%3 == 0 and n >= 3:
            res.append(cost(n//3, costs)+B)
        if n%5 == 0 and n >= 5:
            res.append(cost(n//5, costs)+C)
            costs[n] = min(res)
        return min(res)

def solve(N, A, B, C, D):
    costs = [-1 for _ in range(2*N)]
    return cost(N, costs)

T = int(input())

for _ in range(T):
    n, a, b, c, d = map(int, input().split())
    print(solve(n, a, b, c, d))
