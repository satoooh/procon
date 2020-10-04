from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]
B = [i for i in range(1, N+1)]

if set(A) == set(B):
    print("Correct")
    exit()

before = list(set(B) - set(A))[0]
ca = Counter(A)
after = ca.most_common()[0][0]

print(after, before)
