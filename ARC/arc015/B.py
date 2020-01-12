N = int(input())
count = [0, 0, 0, 0, 0, 0]
for _ in range(N):
    MT, mT = map(float, input().split())
    if (MT >= 35):
        count[0] += 1
    if (30 <= MT < 35):
        count[1] += 1
    if (25 <= MT < 30):
        count[2] += 1
    if (mT >= 25):
        count[3] += 1
    if (mT < 0) and (MT >= 0):
        count[4] += 1
    if (MT < 0):
        count[5] += 1

print(*count)
