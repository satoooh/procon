N, L = map(int, input().split())
amida = [input() for _ in range(L)]
now = input().index("o") // 2 # o の初期位置

# だんだん上に登りながら now を更新する
for li in range(L):
    if now > 0 and amida[L-li-1][2*now-1] == "-":
        now -= 1
    elif now < N-1 and amida[L-li-1][2*now+1] == "-":
        now += 1

print(now+1)
