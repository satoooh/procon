import numpy as np
import sys

data = open("./p022-names.txt")

names = list(data.read().split(","))
names.sort()

score = 0

for i in range(len(names)):
    res2 = 0
    for c in names[i][1:-1]:
        res2 += ord(c)-64
    score += (i+1) * res2
    if i == 0:
        for c in names[i][1:-1]:
            print(c, ord(c)-64)
        print(i, names[i], score)

print(score)
