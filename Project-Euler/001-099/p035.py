def is_prime(n):
    if n <= 1:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True


ans = 0
for num in range(1, 1000000):
    if is_prime(num):
        flag = True
        for i in range(len(str(num))):
            num = str(num)[1:] + str(num)[0]
            if is_prime(int(num)):
                continue
            else:
                flag = False
                break
        if flag:
            ans += 1

print(ans)
