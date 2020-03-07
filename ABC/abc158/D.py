S = input()
Q = int(input())
reverse = False
pref, suf = "", ""

for i in range(Q):
    query = list(input().split())
    if query[0] == "1":
        reverse = not reverse
    else:
        if reverse == False:
            if query[1] == "1":
                pref = query[2] + pref
            else:
                suf = suf + query[2]
        else:
            if query[1] == "1":
                suf = suf + query[2]
            else:
                pref = query[2] + pref

if reverse == False:
    ans = pref + S + suf
else:
    ans = suf[::-1] + S[::-1] + pref[::-1]

print(ans)
