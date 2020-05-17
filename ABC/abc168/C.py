from math import pi, cos, sqrt

A, B, H, M = map(int, input().split())

theta_a = 2 * pi * (H%12)/12 + 2 * pi / 12 * M/60
theta_b = 2 * pi * M/60

theta = abs(theta_a - theta_b)

ans = sqrt( A**2 + B**2 - 2*A*B*cos(theta) )
print(ans)
