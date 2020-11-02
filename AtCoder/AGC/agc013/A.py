# 単調増加か単調減少かが変わるたびに、次の列が単調増加か単調減少かを調べる必要がある点に注意。

def upper_or_lower(i):
    if A[i] < A[i + 1]:
        return "upper"
    elif A[i] > A[i + 1]:
        return "lower"
    else:
        return upper_or_lower(i + 1)


N = int(input())
A = list(map(int, input().split()))

state = "upper"  # state が upper か lower で判定
ans = 1

# i = 0 の処理
if (len(A) > 2) and (A[0] > A[1]):
    state = "lower"

for i in range(2, N):
    if (state == "upper") and (A[i - 1] > A[i]):
        ans += 1
        if i < N - 1:
            state = upper_or_lower(i)
    elif (state == "lower") and (A[i - 1] < A[i]):
        ans += 1
        if i < N - 1:
            state = upper_or_lower(i)
    else:
        continue

print(ans)
