def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

S = input()
N = len(S)
if is_palindrome(S) and is_palindrome(S[0:(N-1)//2]) and is_palindrome(S[(N+3)//2-1:]):
    print("Yes")
else:
    print("No")
