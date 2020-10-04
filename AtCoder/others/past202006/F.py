from collections import Counter

N = int(input())

# 例外処理
if N == 1:
    print(input()[0])
    exit()

c = []
for _ in range(N):
    c.append(Counter(input()))

ans = []

for i in range(N//2):
    # c[i] と c[N-i-1] の両方に含まれている文字を S[i] に採用する
    ci = (c[i] & c[N-i-1]).keys()
    if ci:
        ans.append(list(ci)[0])
    else:
        print(-1)
        exit()

# 回文にする
if N%2 == 0:
    ans_str = "".join(ans) + "".join(ans[::-1])
else:
    ans_str = "".join(ans) + list(c[N//2].keys())[0] + "".join(ans[::-1])

print(ans_str)
