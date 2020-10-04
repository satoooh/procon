fact = {0:1, 1:1, 2:2, 3:6, 4:24, 5:120, 6:720, 7:5040, 8:40320, 9:362880}

max_digit = 1
while (fact[9] * max_digit > int("9"*max_digit)):
    max_digit += 1
max_cand = int("9"*max_digit) + 1

print(max_cand)

ans = 0

for i in range(3, max_cand+1):
    if i == sum([fact[int(j)] for j in str(i)]):
        print(i)
        ans += i

print(ans)
