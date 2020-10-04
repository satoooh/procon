MAX = 100000

T = {n*(n+1)//2 for n in range(286, MAX)}
P = {n*(3*n-1)//2 for n in range(165, MAX)}
H = {n*(2*n-1) for n in range(143, MAX)}

cand = T & P & H
print(cand)
