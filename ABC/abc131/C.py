"""
ありがちな整数問題
"""

from fractions import gcd

A, B, C, D = map(int, input().split())
L = C * D // gcd(C, D)
a = (A - 1) - (A - 1) // C - (A - 1) // D + (A - 1) // L
b = B - B // C - B // D + B // L
print(b - a)
