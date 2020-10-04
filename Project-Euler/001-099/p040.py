d = ""
for i in range(1000000):
    d += str(i)

ans = int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])
print(ans)
