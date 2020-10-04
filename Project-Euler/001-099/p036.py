def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

ans = 0

for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        ans += i

print(ans)
