x1, y1, r = map(int, input().split())
x2, y2, x3, y3 = map(int, input().split())

def in_circle(x, y):
    return (x-x1)**2 + (y-y1)**2 <= r**2

# check red area
if x2 <= x1-r and x1+r <= x3 and y2 <= y1-r and y1+r <= y3:
    print("NO")
else:
    print("YES")

# check blue area
if in_circle(x2, y2) and in_circle(x2, y3) and in_circle(x3, y2) and in_circle(x3, y3):
    print("NO")
else:
    print("YES")
