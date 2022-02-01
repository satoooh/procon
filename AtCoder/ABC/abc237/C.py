def is_kaibun(s: str) -> str:
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return "No"
    return "Yes"

S = input()

a_start = 0
i = 0
while S[i] == "a" and i < len(S)-1:
    a_start += 1
    i += 1

a_end = 0
j = 0
while S[len(S)-j-1] == "a" and j < len(S)-1:
    a_end += 1
    j += 1

if a_start == len(S):
    print("Yes")
elif a_start > a_end:
    print("No")
else:
    surplus = a_end - a_start
    target = S[:len(S)-surplus]
    print(is_kaibun(target))
