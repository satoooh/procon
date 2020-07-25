def buy(my_money, A, count):
    return my_money%A, count + my_money//A

def sell(my_money, A, count):
    return my_money + A*count, 0

N = int(input())
A = list(map(int, input().split()))

now = 1000  # 所持金
kabu = 0

for i in range(N-1):
    if A[i] < A[i+1]:
        now, kabu = buy(now, A[i], kabu)
    else:
        now, kabu = sell(now, A[i], kabu)

now, kabu = sell(now, A[N-1], kabu)

print(now)
