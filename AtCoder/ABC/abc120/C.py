S = input()
One = S.count("1")
Zero = S.count("0")
print(len(S) - max(One, Zero) + min(One, Zero))
