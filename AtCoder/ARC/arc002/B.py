import datetime

def ok(date):
    Y, M, D = date.year, date.month, date.day
    return (Y % M == 0 and (Y//M) % D == 0)

S = input()
date = datetime.datetime.strptime(S, "%Y/%m/%d")

while not ok(date):
    date += datetime.timedelta(days=1)

ans = date.strftime("%Y/%m/%d")
print(ans)
