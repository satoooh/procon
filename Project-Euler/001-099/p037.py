def is_prime(n):
    """素数判定
    """
    if n < 2:
        return 0
    elif n == 2:
        return 1
    if n%2 == 0:
        return 0
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return 0
    return 1

truncatable_primes = []
i = 11
while (len(truncatable_primes) < 11):
    if is_prime(i):
        s = str(i)
        flag = 1
        for si in range(len(s)):
            if not is_prime(int(s[:si+1])):
                flag = 0
                break
            if not is_prime(int(s[si:])):
                flag = 0
                break
        if flag:
            truncatable_primes.append(i)
    i += 2

print(truncatable_primes)
print(sum(truncatable_primes))
