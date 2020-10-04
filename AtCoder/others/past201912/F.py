S = input()
words = []
end = 0
for i in range(len(S)-1):
    if S[i].isupper() and S[i+1].isupper() and len(S[end:i+1]) > 1:
        words.append(S[end:i+1])
        end = i+1
words.append(S[end:])

words.sort(key=str.lower)
print("".join(words))
