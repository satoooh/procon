def is_prime(X):
    if X <= 1:
        return False
    else:
        for i in range(2, int(X**0.5) + 1):
            if X % i == 0:
                return False
        return True


X = int(input())
num = X

while True:
    if is_prime(num):
        print(num)
        exit()
    else:
        num += 1
