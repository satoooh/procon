N = int(input())

ans = [0 for i in range(N)]  # f(i) = ans[i-1] とする

for x in range(1, int(N**0.5)+1):
    if N-x**2 >= 0:
        for y in range(1, int((N-x**2)**0.5)+1):
            if N-x**2-y**2-x*y >= 0:
                for z in range(1, int((N-x**2-y**2-x*y)**0.5)+1):
                    tar = x**2 + y**2 + z**2 + x*y + y*z + z*x
                    if 1 <= tar <= N:
                        ans[tar-1] += 1

for i in range(1, N+1):
    print(ans[i-1])
