N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B が小さいほど制約が大きいのでBが小さいものからみる
C = sorted(zip(A, B), key=lambda x: x[1])
A, B = map(list, zip(*C))

ans = 0
for i in range(N):
    if ans > N - 2:
        print("No")
        exit()
    if (A[i] > B[i]):
        if [k for k in A[i + 1:] if k <= B[i]]:
            j = A[i + 1:].index(max([k for k in A[i + 1:] if k <= B[i]]))
            A[i], A[j] = A[j], A[i]
            ans += 1
        else:
            print("No")
            exit()

print("Yes")
