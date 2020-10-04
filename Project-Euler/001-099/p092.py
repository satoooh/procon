from tqdm import tqdm
from copy import deepcopy

ans = 0
l = [0] * 10000000

for n in tqdm(range(1, 10000000)):
    res = deepcopy(n)
    while (res != 1 and res != 89):
        res = sum([int(i)**2 for i in str(res)])
        if l[res-1] == 1:
            res = 1
            break
        elif l[res-1] == 89:
            res = 89
            break
    if res == 1:
        l[n-1] = 1
    elif res == 89:
        l[n-1] = 89
        ans += 1

print(ans)
