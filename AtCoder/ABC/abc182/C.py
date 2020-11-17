from collections import Counter

N = input() # 文字列として受け取っておく
digit_sum = sum(map(int, N))
c = Counter([ni%3 for ni in map(int, N)])

if digit_sum%3 == 0:
    print(0)
elif digit_sum%3 == 1:
    if c[1] >= 1 and len(N) > 1:
        print(1)
    elif c[2] >= 2 and len(N) > 2:
        print(2)
    else:
        print(-1)
elif digit_sum%3 == 2:
    if c[2] >= 1 and len(N) > 1:
        print(1)
    elif c[1] >= 2 and len(N) > 2:
        print(2)
    else:
        print(-1)
