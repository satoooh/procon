"""
難易度順にdをソートすると条件を満たすにはKは半分のところに来る必要があるので、
Kとしてあり得る値はd[N // 2 - 1] + 1からd[N // 2]までの合計d[N // 2] - d[N // 2 - 1]個
"""

N = int(input())
d = sorted(list(map(int, input().split())))
print(d[N // 2] - d[N // 2 - 1])
