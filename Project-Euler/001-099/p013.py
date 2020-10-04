import numpy as np
import sys

data = open("./src/p013-numbers.txt")

summ = 0
for line in data.readlines():
    summ += int(line)

print(str(summ)[:10])
