# Goldbach's other conjecture
# とりあえず答えがなるべく小さいことを願いながら全探索してみる

import sys

INF = 10**6 + 7 # 答えの探索範囲の上限、だんだん増やしていく

def is_prime(n):  # 素数かどうかを判定する関数isPrime()を定義
    if n == 1:
        return False
    for p in range(2, int(n ** 0.5) + 1):
        if n % p == 0:
            return False
    return True

# 素数テーブルと平方数の2倍テーブルを作っておく
primes = [2] + [i for i in range(3, INF+1, 2) if is_prime(i)]
twice_a_squares = [i**2 * 2 for i in range(1, int(INF**0.5)+1)]

x = 9
while (True):
    if x not in primes:
        flag = True
        for tx in twice_a_squares:
            if tx >= x:
                break
            else:
                if x - tx in primes:
                    flag = False
                    break
        if flag:
            print(f"The answer is {x}.")
            exit()
    x += 2
    if x >= INF:
        print(f"x = {x} over INF ={INF}")
        exit()
