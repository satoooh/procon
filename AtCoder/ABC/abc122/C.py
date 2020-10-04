N, Q = map(int, input().split())
S = input()
count = [0]*N  # count[i] は i 番目まで S[:i+1] の解
for i in range(1, N):
    count[i] = count[i-1]
    if S[i-1: i+1] == "AC":
        count[i] += 1
for _ in range(Q):
    l,r = map(int, input().split())
    print(count[r-1] - count[l-1])
