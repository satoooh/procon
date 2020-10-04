import numpy as np

N = int(input())
T = np.array([list(map(int, input().split())) for _ in range(N)])  # T[i][0] = K[i] (0<=i<N)
M = int(input())
a = list(map(int, input().split()))

for i in range(M):
    # i番目の客の処理
    max_T, max_T_ind, max_row = 0, 0, 0
    for row in range(N):
        if T[row][1:a[i]+1]:
            cand_max_T = max(T[row][1:min(T[row][0], a[i])+1])
            cand_max_T_ind = np.argmax(np.array(T[row][1:min(T[row][0], a[i])+1]))
            if cand_max_T > max_T:
                max_T = cand_max_T
                max_T_ind = cand_max_T_ind
                max_row = row
    #print(max_row, max_T)
    print(max_T)
    T[max_row][1:] = T[max_row][1:1+max_T_ind] + T[max_row][1+max_T_ind+1:]
    #print(T, "\n")
