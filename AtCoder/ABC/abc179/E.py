N, X, M = map(int, input().split())

A = [-1 for _ in range(M*2)]  # どうせ M 回以内でループに入るので
A[0] = X

is_seen = [0 for _ in range(M)]  # is_seen[i] : i がすでに現れたか
is_seen[X] = 1

first_sum = 0
loop_length = -1

for i in range(N):
    first_sum += A[i]
    A[i+1] = A[i]**2 % M
    if A[i+1] == 0:
        break
    elif is_seen[A[i+1]]:
        # すでに出現済みということで A[A.index(A[i+1])], ..., A[i] までがループであることがわかる
        loop_length = i - A.index(A[i+1]) + 1
        # 残りをループで足していく
        A_loop = A[A.index(A[i+1]):i+1]
        loop_sum = sum(A_loop)
        res = N - i  # 足さないといけない残り
        ans = first_sum + (res//loop_length) * loop_sum
        # はみ出したぶん
        if res % loop_length != 0:
            ans += sum( A_loop[:res%loop_length-1] )
        break
    else:
        is_seen[A[i+1]] = 1

if loop_length == -1:
    ans = first_sum

print(ans)
