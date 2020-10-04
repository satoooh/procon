ans = 0

for a in range(200//200+1):
    res = 200*a
    if res > 200:
        continue
    for b in range(200//100+1):
        res = 200*a + 100*b
        if res > 200:
            continue
        for c in range(200//50+1):
            res = 200*a + 100*b + 50*c
            if res > 200:
                continue
            for d in range(200//20+1):
                res = 200*a + 100*b + 50*c + 20*d
                if res > 200:
                    continue
                for e in range(200//10+1):
                    res = 200*a + 100*b + 50*c + 20*d + 10*e
                    if res > 200:
                        continue
                    for f in range(200//5+1):
                        res = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f
                        if res > 200:
                            continue
                        for g in range(200//2+1):
                            res = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g
                            if res > 200:
                                continue
                            for h in range(200//1+1):
                                res = 200*a + 100*b + 50*c + 20*d + 10*e + 5*f + 2*g + h
                                if res == 200:
                                    ans += 1

print(ans)
