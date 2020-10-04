def is_increased(n):
    flag = 1
    s = str(n)
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            flag = 0
    if flag:
        return True
    else:
        return False

def is_decreased(n):
    flag = 1
    s = str(n)
    for i in range(len(s)-1):
        if int(s[i]) < int(s[i+1]):
            flag = 0
    if flag:
        return True
    else:
        return False

def is_bouncy(n):
    if (not is_increased(n)) and (not is_decreased(n)):
        return True
    else:
        return False

print(133468, "is increased:", is_increased(133468))  # test
print(66420, "is decreased:", is_decreased(66420))  # test
print(155349, "is bouncy:", is_bouncy(155349))  # test


bouncy, not_bouncy = 0, 1

n = 2
while n < 100000000:
    if is_bouncy(n):
        bouncy += 1
    else:
        not_bouncy += 1
    if n in {538, 1000, 21780}:
        print("n =", n, ":", bouncy, bouncy / n)  # test
    if bouncy/n == 0.99:
        print("answer is", n)
        exit()
    n += 1
