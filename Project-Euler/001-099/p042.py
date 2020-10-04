triangle_num = [n*(n+1)//2 for n in range(1, 100)]  # 事前にscoreのmaxを調べておけば絞れる

data = open("./src/001-099/p042_words.txt")
words = list(data.read().split(","))

ans = 0

for i in range(len(words)):
    score = 0
    for c in words[i][1:-1]:
        score += ord(c)-64
    if score in triangle_num:
        ans += 1

print(ans)
