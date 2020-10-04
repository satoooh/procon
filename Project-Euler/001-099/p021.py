def d(n):
    s = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i and i != 1:
                s += n // i
    return s


ans = 0
for i in range(10000):

    if d(d(i)) == i and d(i) != i:
        ans += i

print(ans)
