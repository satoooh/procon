def ddcc2018_qual_b(n):
    if n % 2 == 1:
        return ddcc2018_qual_b(n - 1) + 1
    else:
        return n * (n - 2) // 2


print(ddcc2018_qual_b(int(input())))
