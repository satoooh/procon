"""
3桁の数の積で表される回分数のmaxを求める。
2.1s
"""


def is_palindrome_number(n):
    if str(n) == str(n)[:: -1]:
        return True
    else:
        return False


ans =[]
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome_number(i * j):
            ans.append(i * j)
print(max(ans))
